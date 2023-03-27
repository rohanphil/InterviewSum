import utils
import whisper

import warnings
warnings.filterwarnings("ignore")

# Get configs
configs = utils.getconfig().conf()

whisper_model = configs["WHISPER_MODEL"]



# Load the model
model = whisper.load_model(whisper_model)

# Transcribe the results
result = model.transcribe("lex_ai_sam_altman.mp3")
transcript = result["text"]

# Store in file

path = configs["TRANSCRIPT_STORE"] + '/transcript' + str(int(configs["TRANSCRIPT_COUNT"])+1) + '.txt'

with open(path,'w') as trans:
	trans.write(transcript)
utils.getconfig().update_count(str(int(configs["TRANSCRIPT_COUNT"])+1))

