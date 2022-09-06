import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01' ,
    authenticator = authenticator
)

language_translator.set_service_url('{url}')

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def french_to_english(text1):
    translation = language_translator.translate(
        text = text1 ,
        model_id = 'fr-en'
    ).get_result()
    return translation.get("translations")[0].get("translation")

def english_to_french(text1):
    translation = language_translator.translate(
        text = text1 ,
        model_id = 'en-fr'
    ).get_result()
    return translation.get("translations")[0].get("translation")