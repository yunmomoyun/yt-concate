from Pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, input, utils):
        print('in Postflight')
