#!/bin/python

"""
Only supports mrc files so far
"""

import subprocess
import mrcfile
import json
import os
import glob
import numpy as np

class Cinderella:
	""" Python3 wrapper for running Cinderella """
	def __init__(self):
		# GPU ID, is -1 when not using GPUs
		self.gpu = -1
		# Configuration, can be overwritten by read_config
		self.config = { "model":{}, "train":{} }
		self.config["model"]["input_size"] = [75, 75]
		self.config["train"]["batch_size"] = 32
		self.config["train"]["good_classes"] = ""
		self.config["train"]["bad_classes"] = ""
		self.config["train"]["pretrained_weights"] = ""
		self.config["train"]["saved_weights_name"] = ""
		self.config["train"]["learning_rate"] = 1e-4
		self.config["train"]["nb_epoch"] = 100
		self.config["train"]["nb_early_stop"] = 15
		# Threshold for class selection
		self.threshold = 0.7
		# Makes Cindarella less loud
		self.silent = False
	
	def check(self):
		result = subprocess.run(["which","sp_cinderella_predict.py"], stdout=subprocess.PIPE)
		location = result.stdout.decode("UTF-8")
		if location == "":
			return False
		else:
			return True

	def train(self, good, bad, model, weights=None):
		# Put parameters to config dictionary
		self.config["train"]["good_classes"] = good
		self.config["train"]["bad_classes"] = bad
		self.config["train"]["saved_weights_name"] = model
		
		if weights != None:
			self.config["train"]["saved_weights_name"] = weights
		# Write the config
		configuration = self.write_config("tmp_config.json")

		# Running sp_cinderella_train.py
		cmd = "sp_cinderella_train.py -c "+configuration+" --gpu "+str(self.gpu)
		if self.silent == False:
			print("Running: "+cmd)
		with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as train_process:
			for line in train_process.stdout:
				if self.silent == False:
					print(line, end='')

		# Clean up
		os.remove(configuration)

	def predict(self, data, model, output=None):
		#data: path to the mrc class averages
		#model: path to the h5 model file
		#output: optional path to keep output mrc files

		#returns a list good class ids

		if output == None:
			output = "tmp"

		# Running sp_cinderella_predict.py
		cmd = "sp_cinderella_predict.py -i "+str(data)+" -t "+str(self.threshold)+" -w "+str(model)+" -o "+str(output)+" --gpu "+str(self.gpu)
		if self.silent == False:
			print("Running: "+cmd)
		predict_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

		# Wait for the prediction to finish.
		while True:
			if predict_process.poll() == 0:
				break

		# Give some output
		if self.silent == False:
			print(predict_process.stdout.read().decode())

		# Sort out classes by image comparison
		good_classes = mrcfile.open(glob.glob(output+"/*_good.mrcs")[0])
		all_classes =  mrcfile.open(data)
		class_id = 0
		classification = []
		for class_id in range(0, len(all_classes.data)):
			for good in good_classes.data:
				if np.array_equal( all_classes.data[class_id], good):
					classification.append(class_id)
			class_id = class_id+1

		# Clean up if no output should be left
		if output == "tmp":
			filelist = glob.glob("tmp/*.mrcs")
			for file in filelist:
				os.remove(file) 
			os.rmdir(output)

		# A list of good class ids
		return classification
		

	def write_config(self, filename):
		data = json.dumps(self.config)
		file = open(filename,"w")
		file.write(data)
		file.close()
		return filename

	def read_config(self, filename):
		file = open(filename)
		file_data = file.read()
		self.config = json.loads(file_data)
		return self.config