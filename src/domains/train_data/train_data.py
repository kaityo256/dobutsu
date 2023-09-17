import pickle
from typing import Dict
from src.consts.domain import *
from src.domains.train_data.const import AppearanceCount, TrainDataDic

class TrainData:
    def __init__(self, dict: TrainDataDic):
        self.dict = dict

    def search_score(self, key: Key) -> Score:
        found = self.dict.get(key)
        if found == None:
            return 0
        else:
            return found[0]
    
    def search_appearance_count(self, key: Key) -> AppearanceCount:
        found = self.dict.get(key)
        if found == None:
            return 0
        else:
            return found[1]
    
    def get_size(self) -> int:
        return len(self.dict)
    
    def get_except_one_appearance_size(self) -> int:
        return len([value for value in self.dict.values() if value[1] > 1])
    
    def compress(self) -> 'TrainData':
        ret: TrainDataDic = {}
        for key, value in self.dict.items():
            if value[1] > COMPRESSION_THRESHOLD:
                ret[key] = value
        return TrainData(ret)
    
    def show_appearance_distribution(self) -> Dict[AppearanceCount, int]:
        distribution = {}
        for value in self.dict.values():
            if value[1] in distribution:
                distribution[value[1]] += 1
            else:
                distribution[value[1]] = 1
        return distribution

    def save(self, filename: str = 'test') -> None:
        with open(f"data/train_data/{filename}.pkl", "wb") as file:
            pickle.dump(self.dict, file)
