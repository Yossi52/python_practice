from internet_speed_twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 100

bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
internet_speed = bot.get_internet_speed()

if float(bot.down) < bot.PROMISED_DOWN or float(bot.up) < bot.PROMISED_UP:
    msg = f"Hey Internet Provider, why is my internet speed {bot.down}down / {bot.up}up when " \
          f"I pay for {bot.PROMISED_DOWN}down / {bot.PROMISED_UP}up?" \
        # f"@prodiver_name"
    bot.tweet_at_provider(msg)
