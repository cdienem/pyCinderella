# pyCinderella
pyCinderella is a Python wrapper to run Cinderella: https://github.com/MPI-Dortmund/sphire_classes_autoselect
## Requirements
- Cinderella
- Python >3.5
- Non-standard Python modules
   - mrcfile
   - numpy 

## Installation
Just download pyCinderella.py and import it as a module in your Python program (also see Usage).

## Features
pyCinderella gives acess to the following features of Cinderella (and beyond):
- Prediction of good/bad 2D class averages
- Output of good class indecies for further usage
- Automatic cleanup to not leave configs and outputs around
- Training of new models or existing calculated weights

## Usage
### Import to your program
```Python
from pyCinderella import Cinderella
```



### Initialize the wrapper
```Python
cinderella = Cinderella()
```

### Check if Cinderella executables are present
```Python
cinderella.check()
```
This will return True/False.

### Set GPU usage
```Python
cinderella.gpu = 0
```
This will make Cinderella use GPU with ID 0. This only works with the GPU version of Cinderella.
### Set selection threshold
```Python
cinderella.threshold = 0.8
```
Set the selection threshold to 0.8. Default is 0.7.
### Predict good classes
```Python
classes = cinderella.predict("/home/data/2D_training_data/cryosparc_P7_J37_020_class_averages.mrc", "model.h5")

# Print a list of good class indecies
# This will not leave any class average stacks around!
print(classes)

classes = cinderella.predict("/home/data/2D_training_data/cryosparc_P7_J37_020_class_averages.mrc", "model.h5", output="sorted_classes")
# This will leave good/bad averages as mrcs stacks in the location specified by output
```
### Train a new model
cinderella.train("good", "bad", "new_model.h5")

### Reads JSON config file
cinderella.read_config("config.json")

### Writes configuration to JSON config file
cinderella.write_config("config.json")





```
