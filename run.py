#!/usr/bin/python

# Runs the game.

import os
import sys
import argparse

# Directory for the Jack compiler script.
jack_compiler = "/home/matt/Dropbox/College/2016-2017/Fall/CSCE-312/nand2tetris/tools/JackCompiler.sh"
# Directory for VM emulator script.
vm_emulator = "/home/matt/Dropbox/College/2016-2017/Fall/CSCE-312/nand2tetris/tools/VMEmulator.sh"
# Current directory.
cwd = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='Run the thingy.')
parser.add_argument('-v','--vm_dir', help='Directory for VM emulator. Defaults to ' + vm_emulator, required=False)
parser.add_argument('-c', '--compiler_dir', help='Directory for the Jack compiler. Defaults to ' + jack_compiler, required=False)
parser.add_argument('-r', '--run', action='store_true', help='Whether to start the emulator.', required=False)
args = vars(parser.parse_args())

if args['vm_dir']:
	vm_emulator = args['vm_dir']
if args['compiler_dir']:
	jack_compiler = args['compiler_dir']

os.system("bash " + jack_compiler + " " + cwd)
if args['run']:
	os.system("bash " + vm_emulator)