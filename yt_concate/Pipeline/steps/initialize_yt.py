from .step import Step
from yt_concate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, input, utils):
        return [YT(url, utils) for url in data]
