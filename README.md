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
- Return/output of good class indecies as python list for further usage
- Automatic cleanup of Cinderella outputs if they are not needed (configs and class images)
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
This does not do anything spectecular (yet), just returns the Cinderella wrapper instance.

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
Use `cinderella.predict( class_averages, model [, output])`

- `class_averages`: path to an MRC file containing the class averages
- `model`: path to .h5 model file
- `outut`: (optional) folder to write output in. If not provided, no output will be created

`return` value: Python list of good class indecies.

Example:
```Python
# predict good classes from cryosparc_P7_J37_020_class_averages.mrc using the trained weights stored in model.h5
# This will not create any output files, only return a list of good classes
classes = cinderella.predict("/home/data/2D_training_data/cryosparc_P7_J37_020_class_averages.mrc", "model.h5")

# Print list of good class indecies
print(classes)

# predict good classes from cryosparc_P7_J37_020_class_averages.mrc using the trained weights stored in model.h5
# This will not create a folder "sorted_classes" that will contain good/bad.mrcs files
classes = cinderella.predict("/home/data/2D_training_data/cryosparc_P7_J37_020_class_averages.mrc", "model.h5", output="sorted_classes")
```
### Train a new model
cinderella.train("good", "bad", "new_model.h5")


Use `cinderella.train( folder_good, folder_bad, model [, weights])`

- `folder_good`: path to a folder containing positive exapmles as mrcs stacks
- `folder_bad`: path to a folder containing negative exapmles as mrcs stacks
- `model`: filename of the .h5 model file to be saved
- `weights`: (optional) pre-calculated weigts for training

`return` value: nothing (yet).

### Reads JSON config file
cinderella.read_config("config.json")

### Writes configuration to JSON config file
cinderella.write_config("config.json")





```
