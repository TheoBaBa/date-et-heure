import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
from datetime import datetime
from pytz import timezone
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

def verbalise_hour(i):
	if i == 0:
		return "minuit"
	elif i == 1:
		return "une heure"
	elif i == 12:
		return "midi"
	elif i == 21:
		return "vingt et une heures"
	else:
		return "{0} heures".format(str(i)) 

def verbalise_minute(i):
	if i == 0:
		return ""
	elif i == 1:
		return "une"
	elif i == 21:
		return "vingt et une"
	elif i == 31:
		return "trente et une"
	elif i == 41:
		return "quarante et une"
	elif i == 51:
		return "cinquante et une"
	else:
		return "{0}".format(str(i)) 


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()

	if intent_message.intent.intent_name == 'Reveil:askTime':

		sentence = 'Il est '
		print(intent_message.intent.intent_name)

		now = datetime.now(timezone('Europe/Paris'))

		sentence += verbalise_hour(now.hour) + " " + verbalise_minute(now.minute)
		print(sentence)

		# hermes.publish_continue_session(intent_message.session_id, sentence, ["Joseph:greetings"])
		hermes.publish_end_session(intent_message.session_id, sentence)

	elif intent_message.intent.intent_name == 'Reveil:askDay':

                sentence2 = 'Il est '
		print(intent_message.intent.intent_name)

		now = datetime.now(timezone('Europe/Paris'))

		sentence2 += verbalise_hour(now.hour) + " " + verbalise_minute(now.minute)
		print(sentence2)


		hermes.publish_end_session(intent_message.session_id, sentence2)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()

