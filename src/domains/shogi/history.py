from typing import List, Tuple
from domains.shogi.const import Step
from domains.shogi.shogi_state import ShogiState

class History:
    def __init__(self) -> None:
        self.list: List[ShogiState] = []
        self.pop_count = 0

    def add_state(self, data: Tuple[ShogiState, Step]) -> None:
        self.list.append(data)

    def __iter__(self) -> 'History':
        return self
    
    def __next__(self) -> ShogiState:
        if  self.pop_count % 2 == 0:
            return self.list.pop()
        else:
            return self.list.pop().turn()
