from Pipeline.steps.read_caption import ReadCaption
from Pipeline.steps.postflight import Postflight
from Pipeline.steps.preflight import Preflight
from Pipeline.steps.step import StepException
from Pipeline.pipline import Pipeline
from Pipeline.steps.download_captions import DownloadCaptions
from Pipeline.steps.get_video_list import GetVideoList
from util import utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


# for step in steps:
#     try:
#         step.process()
#     except StepException as e:
#         print('Exception happened in step', e)
#         break

if __name__ == '__main__':
    main()
