from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class InfoParser(BaseModel):
    tg_id: int
    title: str
    url: str
    xpath: str
    price: Decimal

    model_config = ConfigDict(from_attributes=True)
