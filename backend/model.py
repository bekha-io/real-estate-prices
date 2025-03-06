from pydantic import BaseModel, Field, field_validator, AfterValidator
from typing import Annotated
from enum import Enum
import pandas as pd
from collections import Counter
from catboost import CatBoostRegressor

model = CatBoostRegressor()
model.load_model("catboost_model.cbm")

class RenovationType(str, Enum):
    NEW = 'Новый ремонт'
    WITH_RENNOVATION ='С ремонтом'
    NO_RENNOVATION = 'Без ремонта (коробка)'

class BathroomType(str, Enum):
    SEPARATE = 'Раздельный'
    COMBINED = 'Совмещенный'

class PrepaymentType(str, Enum):
    TWO_MONTHS = '2 месяца'
    THREE_MONTHS = '3 месяца'
    SIX_MONTHS = '6 месяцев'
    TWELVE_MONTHS = "12 месяцев"
    NO_PREPAYMENT = 'Без предоплаты'

class HouseType(str, Enum):
    NEW_CONSTRUCTION = 'Новостройка'
    SOVIET = 'Советский дом'

class DistrictType(str, Enum):
    SHOKHMANSUR = 'шохмансур'
    DOMPECHAT = 'домпечать'
    DRUGIE = 'другие'
    KARABOLO = 'караболо'
    SINO = 'сино'
    SADBARG = 'садбарг'
    MKR_102 = '102мкр'
    ISOMONI = 'исомони'
    ASHAN = 'ашан'
    OVIR = 'овир'
    MKR_91 = '91мкр'
    SPARTAK = 'спартак'
    ZARAFSHON = 'зарафшон'
    FIRDAVSI = 'фирдавси'
    PROFSOYUZ = 'профсоюз'
    MKR_92 = '92мкр'
    TSUM = 'цум'
    ALFEMO = 'алфемо'
    VATAN = 'ватан'
    MKR_112 = '112мкр'
    MKR_82 = '82мкр'
    MEKHREGON = 'мехргон'
    MKR_84 = '84мкр'
    VODANASOS = 'воданасос'

class ModelInput(BaseModel):
    area: int = Field(..., ge=0)
    floor: int = Field(..., gt=0, le=23)
    has_heating: bool
    animals_allowed: bool
    rennovation: RenovationType
    house_type: HouseType
    prepayment: PrepaymentType
    district: DistrictType
    bathroom: BathroomType


class Model():
    data: ModelInput
    def __init__(self, data: ModelInput):
        self.data = data
    
    def predict(self) -> float:
        input_data = {
            'Площадь': [self.data.area],
            'Этаж': [self.data.floor],
            'Домашние животные': ['Разрешены' if self.data.animals_allowed else 'Запрещены'],
            'Отопление': ['Есть' if self.data.has_heating else 'Нет'],
            'Район': [self.data.district.value],
            'Ремонт': [self.data.rennovation.value],
            'Санузел': [self.data.bathroom.value],
            'Срок предоплаты': [self.data.prepayment.value],
            'Тип застройки': [self.data.house_type.value],
        }
        input_df = pd.DataFrame(input_data)
        pred = model.predict(input_df)
        return round(float(pred))