import configparser

config = configparser.ConfigParser()

config['Default'] = {
	'OPENAI_API_KEY' : "None",
	'WHISPER_MODEL' : "base",
	"GPT_model" : "base",
	"TRANSCRIPT_STORE" : "transcripts",
	"TRANSCRIPT_COUNT" : '0'
}

with open('config.ini', 'w') as configfile:

	config.write(configfile)
