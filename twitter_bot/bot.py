import random


class TwitterIdStore():
    def __init__(self, infos: dict) -> None:
        self.twitter_id = infos['id']

        self._consumer_key = infos['consumer_key']
        self._consumer_secret_key = infos['consumer_secret_key']
        self._access_token = infos['access_token']
        self._secret_access_token = infos['secret_access_token']

        self.max_send_message = infos['max_send_message']
        self.direct_messages = [
            infos['direct_messages1'],
            infos['direct_messages2'],
            infos['direct_messages3']
        ]

        self.like_keyword = infos['like_keyword']
        self.max_like = infos['max_like']

        self.follow_keyword = infos['follow_keyword']
        self.max_follow = infos['max_follow']

    def update_dmLimit(self, valse: int):
        self.max_send_message = valse

    def update_likeLimit(self, valse: int):
        self.max_like = valse

    def update_followLimit(self, valse: int):
        self.max_like = valse

    def get_message(self) -> str:
        return random.choice(self.direct_messages)
