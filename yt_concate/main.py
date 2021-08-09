from util import utils
from Pipeline.pipline import Pipeline
from Pipeline.steps.step import StepException
from Pipeline.steps.postflight import Postflight
from Pipeline.steps.download_videos import DownloadVideos
from Pipeline.steps.edit_video import EditVideo
from Pipeline.steps.search import Search
from Pipeline.steps.read_caption import ReadCaption
from Pipeline.steps.download_captions import DownloadCaptions
from Pipeline.steps.initialize_yt import InitializeYT
from Pipeline.steps.get_video_list import GetVideoList
from Pipeline.steps.preflight import Preflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
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
