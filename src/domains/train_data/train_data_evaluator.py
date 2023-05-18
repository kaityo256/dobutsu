from domains.abstract.evaluator import Evaluator
from consts.domain import *
from domains.train_data.train_data import TrainData

class TrainDataEvaluator(Evaluator):
    def __init__(self, train_data: TrainData):
        self.train_data = train_data

    def search_score(self, key: Key) -> Score:
        return self.train_data.search_score(key)