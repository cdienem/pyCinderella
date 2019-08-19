#!/bin/python




from pyCinderella import Cinderella



# Initialize teh wrapper
cinderella = Cinderella()

#Check whether cinderella is actually there
cinderella.check()

# Enable GPU 0 for running Cinderella
cinderella.gpu = 0

#Set the selection threshold to 0.8
cinderella.threshold = 0.8

# Predict good classes
classes = cinderella.predict("/home/data/2D_training_data/cryosparc_P7_J37_020_class_averages.mrc", "model.h5")
print(classes)

# Train the classifyer
cinderella.train("good", "bad", "new_model.h5")