from yt_concate.util import utils
from yt_concate.Pipeline.steps.get_video_list import GetVideoList
from yt_concate.Pipeline.steps.download_captions import DownloadCaptions
from yt_concate.Pipeline.pipline import Pipeline
from yt_concate.Pipeline.steps.step import StepException
from yt_concate.Pipeline.steps.preflight import Preflight
from yt_concate.Pipeline.steps.postflight import Postflight

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
