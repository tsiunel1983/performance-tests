from pydantic import BaseModel, Field, ConfigDict, EmailStr

class TariffSchema(BaseModel):
    """
    Описание структуры тарифа.
    """
    url: str
    document: str


class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения тарифа.
    """
    tariff: TariffSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения контракта.
    """
    contract: DocumentSchema