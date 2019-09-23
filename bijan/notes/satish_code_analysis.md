marcc stuffs

execute run.py

run.py calls "run_experiment" with parameters
  "run_one_layer_deep_conv_rf", "DeepConvRF (1-layer, unshared)", type="unshared"

https://github.com/NeuroDataDesign/deep-conv-rf/blob/master/experiments/run.py#L218
run_experiment checks train and test data and dest file, then runs "experiment = run_one_layer_deep_conv_rf" with parameters
  "dataset name", "numpy data", "chosen classes", "sub_train_indices", "rf type"

https://github.com/NeuroDataDesign/deep-conv-rf/blob/master/experiments/random_forest/deep_conv_rf_runners.py#L16
run_one_layer_deep_conv_rf takes the above params, splits data into train and test, creates a specific DeepConvRF class based on fun used
  calls "convolve_fit"
  calls "convolve_fit_predict"
  ^ you can stack these for "depth"

https://github.com/NeuroDataDesign/deep-conv-rf/blob/master/experiments/random_forest/deep_conv_rf.py#L10
_convolve_chop used often, computed out_dim based on kernel size and stride (no padding), then passes kernel through. adds label vector if its there

https://github.com/NeuroDataDesign/deep-conv-rf/blob/master/experiments/random_forest/deep_conv_rf.py#L53
calls _convolve_chop
creates RandomForestClassifier object (sporf if needed), and fits to images from _convolve_chop

https://github.com/NeuroDataDesign/deep-conv-rf/blob/master/experiments/random_forest/deep_conv_rf.py#L126
takes test images from _convolve_chop
self.kernel_forest[i][j].predict_proba(


yay!
