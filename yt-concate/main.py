from Pipeline.steps.get_video_list import GetVideoList
from Pipeline.steps.step import StepException

from Pipeline.pipline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    data = None
    p = Pipeline(steps)
    p.run(inputs)


# for step in steps:
#     try:
#         step.process()
#     except StepException as e:
#         print('Exception happened in step', e)
#         break

if __name__ == '__main__':
    main()
