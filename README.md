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
- Cleanup functions to not leave configs and outputs around
- Training of new models or existing calculated weights

## Usage
```Python

from pyCinderella import Cinderella



# Initialize the wrapper
cinderella = Cinderella()

#Check whether cinderella is actually available as a command
cinderella.check()
# Return True/False

# Enable GPU 0 for running Cinderella
cinderella.gpu = 0
# Only for the GPU Version of Cinderella

#Set the selection threshold to 0.8
cinderella.threshold = 0.8


# Predict good classes
classes = cinderella.predict("/home/data/2D_training_data/cryosparc_P7_J37_020_class_averages.mrc", "model.h5")
# Print a list of good class indecies
print(classes)

# Train the classifyer on examples located in the folders "good" and "bad"
cinderella.train("good", "bad", "new_model.h5")

# Reads a JSON config file
cinderella.read_config("config.json")

# Writes the current configuration to a JSON config file
cinderella.write_config("config.json")





```
