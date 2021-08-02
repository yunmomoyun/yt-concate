import urllib.request
import json

from Pipeline.steps.step import Step
from Pipeline.steps.step import StepException
from settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + \
            'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
                API_KEY, channel_id)

        video_links = []
        url = first_url
        while True:
            try:
                inp = urllib.request.urlopen(url)
                resp = json.load(inp)
            except KeyError:
                raise StepException

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        self.write_to_file(video_links)
        return video_links


def write_to_file(self, video_link, filepath):
    with open(filepath, 'w') as f:
        for url in video_link:
            f.write(url + '\n')
