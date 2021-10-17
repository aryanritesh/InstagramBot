import os
from instapy import InstaPy
username=os.environ.get('username')
password=os.environ.get('pass')
session=InstaPy(username=username,password=password)
session.login()
session.do_comment(enabled=True, percentage=100)
session.set_comments(['Beauty','love your content so much❤❤','Amazing post','thiss is soooo coool','❤👌'])
session.set_do_follow(enabled=True,percentage=50)
session.follow_by_tags(['fashion','beauty','instareels','reels','music','musician','indianreels','indiansongas'],amount=10)
set
session.like_by_tags(use_smart_hashtags=True,amount=20)
session.end()