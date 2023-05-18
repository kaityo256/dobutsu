import pickle
from domains.train_data.train_data import TrainData
from domains.train_data.const import TrainDataDic


class TrainDataFileFactory:
    def __init__(self, filename: str = 'test') -> None:
        self._read(filename)

    def _read(self, filename: str) -> None:
        with open(f"train_data/{filename}", "rb") as file:
            self._data: TrainDataDic = pickle.load(file)

    def create(self) -> TrainData:
        return TrainData(self._data)