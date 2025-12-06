from langchain_openai import ChatOpenAI, AzureChatOpenAI


def init_llm(settings):
    if settings.provider == "openai":
        return ChatOpenAI(
            model=settings.llm.model_name,
            openai_api_key=settings.credentials.openai_api_key,
            temperature=settings.llm.temperature,
        )
    elif settings.provider == "azure":
        return AzureChatOpenAI(
            azure_endpoint=settings.azure.endpoint,
            azure_deployment=settings.azure.deployment_name,
            api_version=settings.azure.api_version,
            api_key=settings.azure.api_key,
            temperature=settings.llm.temperature,
        )

    raise ValueError("Invalid provider: openai or azure required")
