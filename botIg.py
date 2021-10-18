from instapy import InstaPy
from instapy import smart_run
# name=os.environ.get('username')
# passw=os.environ.get('pass')
session=InstaPy(headless_browser=True)
session.login()
with smart_run(session):
    session.set_relationship_bounds(enabled=True,delimit_by_numbers=True,max_followers=4000,min_followers=500,min_following=200)
session.set_do_follow(enabled=True,percentage=70,times=1)
session.follow_commenters(['jazzzyy.x','radhikasethh','shirleysetia','memezar'],amount=10,daysold=200,max_pic=20,sleep_delay=600,interact=False)
#session.set_user_interact(amount=5, randomize=True, percentage=100, media='Photo')
session.like_by_tags(['fashion','reels','music','musician','indianreels','indiansongs','memes'],amount=10)
#session.like_by_tags(use_smart_hashtags=True,amount=20)
session.end()