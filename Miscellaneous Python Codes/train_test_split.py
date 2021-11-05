import splitfolders  # or import split_folders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
input_path = 'test_all'
splitfolders.ratio(input_path, output="dataset_split", seed=1337, ratio=(.16, .84), group_prefix=None) # default values