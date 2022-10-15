import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5023911804:AAFLjLzGpIExMvTT6Lbot-QiNSjrbOmUmDg")
      API_ID = int(os.environ.get("API_ID", 534493))
      API_HASH = os.environ.get("API_HASH", "ac922823455e814e44020a9f3ee17914")
      OWNER_ID = int(os.environ.get("OWNER_ID", 621617473))

