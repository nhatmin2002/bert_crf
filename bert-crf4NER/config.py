class Config(object):	
	apr_dir = '../model/'
	data_dir = '../corpus/'
	model_name = 'model_4.pt'
	epoch = 20
	bert_model = 'vinai/phobert-base'
	lr = 5e-5
	eps = 1e-8
	batch_size = 16
	mode = 'prediction' # for prediction mode = "prediction"
	training_data = 'train.txt'
	val_data = 'dev.txt'
	test_data = test.txt'
	test_out = 'test_prediction.csv'
	raw_prediction_output = 'raw_prediction.csv'
