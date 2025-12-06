# import toml
# from pathlib import Path
# from pydantic import BaseModel, ValidationError
#
#
# class OpenAISettings(BaseModel):
#     api_key: str
#
#
# class AzureSettings(BaseModel):
#     api_key: str
#     endpoint: str
#     deployment_name: str
#     api_version: str
#
#
# class CredentialsSettings(BaseModel):
#     openai_api_key: str
#
#
# class LLMSettings(BaseModel):
#     model_name: str = "gpt-4.1"
#     temperature: float = 0.0
#     top_p: float = 1.0
#
#
# class BenchmarkSettings(BaseModel):
#     repeat: int = 3
#     providers: list[str] = ["openai", "azure"]
#     model_openai: str = "gpt-4.1"
#     model_azure: str = "gpt4o-deployment"
#
#
# class AppSettings(BaseModel):
#     provider: str
#     credentials: CredentialsSettings
#     azure: AzureSettings
#     llm: LLMSettings
#     benchmark: BenchmarkSettings
#
#
# def load_settings(config_path: str | Path = None) -> AppSettings:
#     """
#     Load and validate config.toml no matter where script is executed from.
#     """
#     # Always resolve project root dynamically
#     project_root = Path(__file__).resolve().parents[2]
#
#     # If no path given → assume config lives in project root
#     config_file = Path(config_path) if config_path else project_root / "config.toml"
#
#     if not config_file.exists():
#         raise FileNotFoundError(
#             f"Config file not found at: {config_file}\n"
#             f"Make sure config.toml exists in project root."
#         )
#
#     raw_data = toml.load(config_file)
#
#     try:
#         return AppSettings(**raw_data)
#     except ValidationError as e:
#         raise RuntimeError(
#             f"Invalid configuration. Details: {e}"
#         ) from e

import os


class Settings:
    provider: str = os.getenv("PROVIDER", "openai")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    azure_api_key: str | None = os.getenv("AZURE_API_KEY")
    azure_endpoint: str | None = os.getenv("AZURE_ENDPOINT")
    azure_deployment_name: str | None = os.getenv("AZURE_DEPLOYMENT_NAME")
    azure_api_version: str | None = os.getenv("AZURE_API_VERSION")


def load_settings(_=None):
    return Settings()
