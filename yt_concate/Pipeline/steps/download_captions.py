import time
import os
from .step import StepException
from .step import Step
from yt_concate.util import utils
from pytube import YouTube


class DownloadCaptions(Step):
    def process(self, data, input, utils):
        start = time.time()
        for yt in data:
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            print(url)
            try:

                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (
                    en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for', yt.url)
                continue

            print(en_caption_convert_to_srt)
            text_file = open(utils.get_video_id_from_url(yt.url),
                             "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')

        return data
