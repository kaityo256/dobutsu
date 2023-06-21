import numpy as np
from src.domains.ready_data.ready_data import ReadyData, one_hot_encode, proccess_key
from src.domains.train_data.train_data import TrainData

key = '867090040213000000'
answer = [
    0,0,0,0,0,0,0,0,1,0,0,
    0,0,0,0,0,0,1,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,1,0,
    1,0,0,0,0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,1,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,1,0,0,0,0,0,0,0,0,
    0,1,0,0,0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,0,0,0,0,
]

a_key = '8670a0040213000000'
a_answer = [
    0,0,0,0,0,0,0,0,1,0,0,
    0,0,0,0,0,0,1,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,1,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,1,0,0,0,0,0,0,0,0,
    0,1,0,0,0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,0,0,0,0,
]

class TestCreate:
    def test_one_hot(self):
        assert np.allclose(one_hot_encode(4), [0,0,0,0,1,0,0,0,0,0,0])

    def test_proccess_key(self):
        one_hot_chain = proccess_key(key)
        assert np.allclose(one_hot_chain, answer)

    def test_create_ready(self):
        train_data = TrainData({
            a_key: [0.5, 3]
        })
        ready_data = ReadyData(train_data)
        assert np.allclose(ready_data.x, [a_answer])
        assert np.allclose(ready_data.y, [0.5])