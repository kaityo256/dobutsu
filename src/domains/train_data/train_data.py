import pickle
from consts.domain import *
from domains.train_data.const import TrainDataDic

class TrainData:
    def __init__(self, dict: TrainDataDic):
        self.dict = dict

    def search_score(self, key: Key) -> Score:
        found = self.dict[key]
        if found == None:
            return 0
        else:
            return found[0]
        
    def save(self, filename: str = 'test') -> None:
        with open(f"train_data/{filename}", "wb") as file:
            pickle.dump(self.dict, file)