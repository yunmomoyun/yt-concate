from .step import Step
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
from yt_concate.util import utils


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('video to download = ', len(yt_set))

        for found in data:
            yt = found.yt
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading', url)
            YouTube(url).streams.first().download(
                output_path=VIDEOS_DIR, filename=yt.id)

        return data
