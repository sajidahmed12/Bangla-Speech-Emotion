import os


class Hyper:
    # audio
    audio_preemph = 0.97
    audio_nfft = 2048
    audio_samplerate = 22050
    audio_winlen = 0.05
    audio_winstep = 0.0125
    audio_melfilters = 80
    audio_refdB = 20
    audio_maxdB = 100
    audio_power = 1.5  # Exponent for amplifying the predicted magnitude
    audio_niter = 50  # Number of inversion iterations
    temporal_rate = 4

    # dir
    root_dir = ""
    feat_dir = os.path.join(root_dir, "features")
    logdir = os.path.join(root_dir, "logdir")
    data_dir = "data"
    
    # data
    #vocab = "PE abcdefghijklmnopqrstuvwxyz'.?"  # P: padding, E: end of string
    vocab = "PE অআইঈউঊঋএওঐঔৃীুৈৌিূেোাফষভৎ০১২৩৪৫৬৭৮৯ক্খগঘঙচছজঝঞটঠডঢণতথদধনপবমযরলশসহড়ঢ়য়ংঃ্যঁও"
    #vocab = "PE &্0123456789অoোyয়ওঐৌৈঔüuুwউঊূaাআàâeèéেêএিইঈীiংঙঞঃশষসsহhণনnটtঠডdঢৎতথদধপpফfবbভvমmলlযঝজjzছচcxকkqখগgঘঋৃড়rর" # P: Padding, E: EOS.

    data_max_text_length = 200   ## Previously it was 200
    data_max_mel_length = 240     ## previously it was 240

    # net
    dim_f = 80  # the dim of audio feature
    dim_e = 128
    dim_d = 256  # the hidden layer of Text2Mel
    dim_c = 512  # the hidder layer of SuperRes
    # dropout
    dropout = 0.05
    # train
    batch_size = 16
    num_batches = 1000000
    device_text2mel = "cuda:0"
    device_superres = "cuda:0"
    guide_g = 0.2  # bigger g, bigger guide area
    guide_weight = 100.0
    guide_decay = 0.99999
    guide_lowbound = 1

    # adam
    adam_alpha = 2e-4
    adam_betas = (0.5, 0.9)
    adam_eps = 1e-6
