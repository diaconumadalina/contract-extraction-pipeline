from typing import Optional
from pydantic import BaseModel, Field

class ContractSchema(BaseModel):
    contract_title: Optional[str] = Field(default=None)
    buyer: Optional[str] = Field(default=None)
    supplier: Optional[str] = Field(default=None)
    contract_value: Optional[str] = Field(default=None)
    start_date: Optional[str] = Field(default=None)
    end_date: Optional[str] = Field(default=None)
