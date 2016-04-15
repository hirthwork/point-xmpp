workers = 8
senders = 8

libs = ['/home/point/core/lib']

# redis
cache_socket = 'unix:///var/run/redis/cache.sock'
storage_socket = 'unix:///var/run/redis/storage.sock'
pubsub_socket = 'unix:///var/run/redis/pubsub.sock'
queue_socket = 'unix:///var/run/redis/queue.sock'
imgproc_socket = 'unix:///var/run/redis/imgproc.sock'
queue_timeout = 5

feed_fetch_timeout = 30

feed_queue_socket = 'unix:///var/run/redis/feed.sock'
feed_queue_timeout = 5

feed_min_update_timeout = 60
feed_max_update_timeout = 86340

db = {
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'point',
    'user': 'point',
    'password': 'point',
    'maxsize': 10
}

domain = 'point.im'

xmpp_jid = 'p@point.im'
xmpp_resource = 'point'
xmpp_password = ''

template_path = '/home/point/xmpp/templates'
avatars_path = '/home/point/img/a'

media_path = '/home/point/img/m'
media_root = '://i.point.im/m'

lang = 'en'
timezone = 'Europe/Moscow'

i18n_dir = 'templates/i18n'
i18n_langs = ['en', 'ru', 'uk', 'by']

session_expire = 1800

# Web sessions
session_backend = 'geweb.session.redis.RedisBackend'
session_prefix = 'geweb-session-'
session_socket = storage_socket

sphinx_host = 'localhost'
sphinx_port = 9312

login_key_expire = 3600

actions_interval = 2

edit_expire = 120
edit_ratio = .95
edit_distance = 10

page_limit = 20

stoplist_file = '/home/point/core/stoplist.txt'
stoplist_expire = 600 # 10 minutes

logger = 'xmpp'
logformat = u'%(asctime)s %(process)d %(filename)s:%(lineno)d:%(funcName)s %(levelname)s  %(message)s'
logfile = '/home/point/log/xmpp.log'
loglevel = 'error'
logrotate = None
logcount = 7

debug = False

proctitle_prefix = 'point'

secret = 'my secret phrase'

cache_markdown = True

cache_expire_max = 86400

try:
    from settings_local import *
except ImportError:
    pass

