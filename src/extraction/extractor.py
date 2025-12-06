# from langchain_openai import ChatOpenAI, AzureChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableParallel, RunnableMap, RunnablePassthrough
# from src.extraction.schema import ContractSchema
# from src.extraction.prompts import BASE_EXTRACTION_PROMPT
# from src.utils.config_loader import load_settings
# from src.utils.helpers import extract_json
#
#
# class ContractExtractor:
#     def __init__(self, config_path: str = "config.toml"):
#         settings = load_settings(config_path)
#
#         # Decide provider (openai / azure)
#         if settings.provider == "openai":
#             self.llm = ChatOpenAI(
#                 model=settings.llm.model_name,
#                 temperature=settings.llm.temperature,
#                 openai_api_key=settings.openai.api_key,
#             )
#
#         elif settings.provider == "azure":
#             self.llm = AzureChatOpenAI(
#                 azure_endpoint=settings.azure.endpoint,
#                 api_version=settings.azure.api_version,
#                 azure_deployment=settings.azure.deployment_name,
#                 openai_api_key=settings.azure.api_key,
#                 temperature=settings.llm.temperature,
#             )
#
#         else:
#             raise ValueError(
#                 f"Invalid provider '{settings.provider}'. Use 'openai' or 'azure'."
#             )
#
#         # Prompt
#         self.prompt = PromptTemplate.from_template(
#             BASE_EXTRACTION_PROMPT + "\n\nContract text:\n{contract_text}"
#         )
#
#         # LCEL pipeline: prompt → llm
#         self.chain = self.prompt | self.llm
#
#     def extract(self, text: str) -> ContractSchema:
#         # invoke instead of run
#         response = self.chain.invoke({"contract_text": text})
#
#         # print(response.content)
#
#         # LangChain returns a ChatResult-like object; extract the text;  Extract raw text content (ChatResult or string)
#         response_text = response.content if hasattr(response, "content") else str(response)
#
#         # Remove code fences and return pure JSON
#         cleaned_json = extract_json(response_text)
#
#         # Validate and parse JSON into Pydantic schema
#         return ContractSchema.model_validate_json(cleaned_json)

from pathlib import Path
from langchain_core.prompts import PromptTemplate
from src.extraction.schema import ContractSchema
from src.extraction.prompts import BASE_EXTRACTION_PROMPT
from src.extraction.retry_handler import retry_llm_call
from src.extraction.llm_client import init_llm
from src.utils.helpers import extract_json
from src.utils.logger import setup_logger
from src.utils.config_loader import load_settings


# IMPORTANT: determine project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]


class ContractExtractor:
    def __init__(self, config_path="config.toml", provider_override=None):
        config_full_path = PROJECT_ROOT / config_path

        print(f"Using config file: {config_full_path}")

        self.settings = load_settings(config_full_path)

        # override provider if benchmark or manual override requests it
        if provider_override:
            print(f"Benchmark override: Using provider = {provider_override}")
            self.settings.provider = provider_override

        self.logger = setup_logger("contract_extractor")
        self.llm = init_llm(self.settings)

        self.prompt = PromptTemplate.from_template(
            BASE_EXTRACTION_PROMPT + "\n\nContract text:\n{contract_text}"
        )
        self.chain = self.prompt | self.llm


    def extract(self, text: str) -> ContractSchema:
        self.logger.info("Starting extraction...")

        @retry_llm_call
        def _call():
            return self.chain.invoke({"contract_text": text})

        response = _call()

        # Extract chat message content
        raw_text = response.content if hasattr(response, "content") else str(response)
        cleaned = extract_json(raw_text)

        self.logger.info(f"Raw response: {cleaned}")

        return ContractSchema.model_validate_json(cleaned)

