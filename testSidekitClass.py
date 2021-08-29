import sidekit
import os

directory='/home/galymzhan/Документы'
files=os.listdir(directory)
audios=[x for x in os.listdir() if x.endswith(".wav")]
show_list=audios
print(audios)

extractor = sidekit.FeaturesExtractor(audio_filename_structure="{}",
feature_filename_structure=directory+"{}.h5",
sampling_frequency=8000,
lower_frequency=200,
higher_frequency=3800,
filter_bank="log",
filter_bank_size=24,
window_size=0.025,
shift=0.01,
ceps_number=13,
pre_emphasis=0.97,
save_param=["cep"],
keep_all_features=True
)
extractor.save_list(show_list=show_list,
channel_list=[0,1,0,1,0,1,0,1,0,1], 
num_thread=10)

fs1=sidekit.FeaturesServer(
feature_filename_structure=directory+"{}.h5",
dataset_list=["cep"],
mask="[1-12]",
delta=True,
double_delta=True
)

feat = fs1.stack_features(show_list=show_list,channel_list=[0,1,0,1,0,1,0,1],feature_filename_list=None,label_list=None,start_list=None,stop_list=None)
print(feat.shape)