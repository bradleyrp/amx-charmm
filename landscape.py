#!/usr/bin/env python

import json

def write_charmm_landscape():
	"""
	WILL BE REMOVED IN PLACE OF LANDSCAPE OBJECT IN AMX/FFTOOLS ... !!!
	"""
	#---note that the following is hardcoded and lipids are autodetected
	ff_name = 'charmm36'
	land = {'objects':{},'alias':{}}
	land['alias']['protein'] = ['GLH','ILE','ALAD','GLUH','GLN','HISH','ASN1','HYP','GLY','HIP',
		'ARGN','MSE','CYS1','GLU','CYS2','CYS','HISE','ASP','SER','HSD','HSE','PRO','CYX','ASPH',
		'ORN','HSP','HID','HIE','LYN','DAB','ASN','CYM','HISD','VAL','THR','HISB','HIS','HIS1',
		'HIS2','TRP','HISA','ACE','ASH','CYSH','PGLU','LYS','PHE','ALA','QLN','MET','LYSH','NME',
		'LEU','ARG','TYR']
	#---note that MARTINI generates ION,NA+ (this is handled in lib_place_proteins.detect_composition)
	land['objects'] = {
		'NA':{'charge':1,'is':'ion','parts':['resname'],'ffs':[ff_name]},
		'CL':{'charge':-1,'is':'ion','parts':['resname'],'ffs':[ff_name]},
		'SOL':{'charge':0,'is':'water','parts':['resname'],'ffs':[ff_name]},}
	#---add lipids from settings
	for mol in state.lipids:
		if mol in land['objects']: raise Exception('molecule %s is already in the landscape'%mol)
		land['objects'][mol] = {'is':'lipid','parts':['resname'],'ffs':[ff_name]}
	with open(state.landscape_at,'w') as fp: fp.write(json.dumps(land))
