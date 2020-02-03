class Config:
    '''
    General configuration parent class
    '''
    pass
    NEWS_API_SOURCES_URL ='https://api.newsapi.org/v2/sources?language=en&country={}&category={}api_key={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True