class NetworkConfig(object):
  scale = 100

  max_step = 1000 * scale
  
  initial_learning_rate = 0.0001
  learning_rate_decay_rate = 0.96
  learning_rate_decay_step = 5 * scale
  entropy_weight = 0.1

  save_step = 1 * scale
  max_to_keep = 1000

  #Conv
  Conv2D_out = 128
  Dense_out = 128
  batch_norm = False
  
  optimizer = 'RMSprop'
  #optimizer = 'Adam'
    
  logit_clipping = 10           #10 or 0, = 0 means logit clipping is disabled

  l2_regularizer = 0

class Config(NetworkConfig):
  version = 'TE_3.2'

  project_name = 'FlexEntry'

  model_interval = 'custom'
  models_num = 6             #number of sub-models
  #the first element should be 0, which means no critical entries should be selected
  model_critical_entries_number = [0, 10, 15, 20, 25, 30, 35]

  #topology_file = 'Abilene'
  topology_file = 'Ebone'
  #topology_file = 'Sprintlink'
  #topology_file = 'Tiscali'
  #topology_file = 'nobel'
  #topology_file = 'Germany50'

  #only choose one sub-model
  max_moves = 1

  method = 'actor_critic'
  
  model_type = 'Conv'

  traffic_file = 'TM1'
  test_traffic_file = 'TM2'

  tm_history = 1
  predict_interval = 0

  num_agents = 20

  num_iter = 50

def get_config(FLAGS):
  config = Config

  for k, v in FLAGS.__flags.items():
    if hasattr(config, k):
      setattr(config, k, v.value)

  return config
