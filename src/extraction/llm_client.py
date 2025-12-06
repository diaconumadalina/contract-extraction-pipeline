# from langchain_openai import ChatOpenAI, AzureChatOpenAI
#
#
# def init_llm(settings):
#     if settings.provider == "openai":
#         return ChatOpenAI(
#             model=settings.llm.model_name,
#             openai_api_key=settings.credentials.openai_api_key,
#             temperature=settings.llm.temperature,
#         )
#     elif settings.provider == "azure":
#         return AzureChatOpenAI(
#             azure_endpoint=settings.azure.endpoint,
#             azure_deployment=settings.azure.deployment_name,
#             api_version=settings.azure.api_version,
#             api_key=settings.azure.api_key,
#             temperature=settings.llm.temperature,
#         )
#
#     raise ValueError("Invalid provider: openai or azure required")

# from langchain_openai import ChatOpenAI, AzureChatOpenAI
#
#
# def init_llm(settings):
#     if settings.provider.lower() == "openai":
#         return ChatOpenAI(
#             api_key=settings.openai_api_key,
#             model=settings.model_name,
#             temperature=0
#         )
#
#     if settings.provider.lower() == "azure":
#         return AzureChatOpenAI(
#             api_key=settings.azure_api_key,
#             azure_endpoint=settings.azure_endpoint,
#             azure_deployment=settings.azure_deployment_name,
#             api_version=settings.azure_api_version,
#             model=settings.model_name,
#             temperature=0
#         )
#
#     raise ValueError(f"Unknown provider: {settings.provider}")

import os

def init_llm():
    provider = os.getenv("PROVIDER", "openai")
    model = os.getenv("MODEL_NAME", "gpt-4o-mini")

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model,
            temperature=0
        )

    elif provider == "azure":
        from langchain_openai import AzureChatOpenAI
        return AzureChatOpenAI(
            api_key=os.getenv("AZURE_API_KEY"),
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
            model=model,
            temperature=0
        )

    else:
        raise ValueError(f"Unknown provider: {provider}")
