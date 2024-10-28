from EDQClientRest import EDQClientRest
class DQhandler(EDQClientRest):
    def __init__(self) -> None:
        self.s3_handler = s3_handler()
        super().__init__(self)
    
    def _read_s3_file(self):


