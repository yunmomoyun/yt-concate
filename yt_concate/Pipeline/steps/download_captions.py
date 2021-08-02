from util import utils
from pytube import YouTube
from Pipeline.steps.step import Step
from Pipeline.steps.step import StepException
import time


class DownloadCaptions(Step):
    def process(self, data, input):
        start = time.time()
        for url in data:
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)

            text_file = open(utils.get_video_id_from_url(url),
                             "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')
