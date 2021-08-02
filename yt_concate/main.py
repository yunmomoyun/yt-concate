from util import Utils
from Pipeline.steps.get_video_list import GetVideoList
from Pipeline.steps.download_captions import DownloadCaptions
from Pipeline.pipline import Pipeline
from Pipeline.steps.step import StepException
from Pipeline.steps.preflight import Preflight
from Pipeline.steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
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
