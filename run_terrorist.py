from core.search import search

KEYWORD = 'teroris OR terroris lang:id'
TARGET_RESULTS = 100000
SAVING_PATH = 'terroris_009.csv'
END_TIME = None # in the future, will be fetched first
START_TIME = '2021-11-29T05:52:36.000Z' # in the past, will be fetched at the end

search(
    keyword=KEYWORD,
    maximum_result=TARGET_RESULTS,
    saving_path=SAVING_PATH,
    include_retweet=False,
    end_time=END_TIME,
    start_time=START_TIME)


