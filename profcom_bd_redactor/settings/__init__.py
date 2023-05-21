from split_settings.tools import include, optional
from dotenv import load_dotenv

load_dotenv()

base_settings = [
    'components/base.py',
    'components/database.py',

    optional('local.py')
]

include(*base_settings)
