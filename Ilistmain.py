from Error import IntError
class Ilist(list):
    def __init_subclass__(self) -> None:
        return super().__init_subclass__()
        
    def filter_Ints(self):
        for i in self:
            if isinstance(i, int):
                pass
            elif isinstance(i, tuple) or isinstance(i, list):
                for s in  i:
                    if isinstance(s, int):
                        pass
                    elif not isinstance(s, int) or isinstance(s, bool):
                        raise IntError(s)
            elif not isinstance(i, int) or isinstance(i, bool):
                raise IntError(i)
