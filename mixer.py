#!/usr/bin/env python -B
# -*- coding: utf-8 -*-

# Mixer v.0.08
# Mixer originated by James Puckett of Dunwich Type Founders
# Mixer is licensed under the Apache License: https://www.apache.org/licenses/LICENSE-2.0
# Mixer can be downloaded at github.com/DunwichType
# Mixer is a tool for generating permutations of glyphs from lists. I use it for building font proofs.
# Mixer is intended to be edited on-the-fly, adding and removing function calls as needed. This is easier than making all this stuff work with command-line switches that you won’t remember anyway.

# Mixer contains lots of encoding and codecs functions to get the non-ASCII stuff working. Some of them were added years ago and aren’t necessary anymore. But it’s easier to just leave them in than it is to figure out which ones can be deleted. 

# Codecs module is needed to generate working text files
import codecs

# Glyphs lists have their own modules
# Import glyph lists
import LatinGlyphs
from LatinGlyphs import *

import KannadaGlyphs
from KannadaGlyphs import *

import DevanagariGlyphs
from DevanagariGlyphs import *

#outputter creates the file we output text to
def outputter (title):
	global output
	output = open( title+'.txt', 'w')
	output.write
	output.write ( title.encode( "utf-8" ))#Output in UTF-8 so we can see all the cool non-Latin stuff.
	output.write( '\n')

# mixer is the function that iterates through the lists, combining them
# dough and chips are lists. Title is the title of the file that will be output.
# mixer  mixes the permutation using dough as the base glyph for each permutation. 
def mixer (dough, chips, title):
	# Prepare output file for writing
	outputter (title)
	for i in dough:
		mix = ''
		for z in chips:
			mix += i 
			mix += z
		output.write( mix.encode( "utf-8" ))
		output.write( '\n')
	output.close()

# reverse mixes the permutation using chips as the base glyph for each permutation.    
def reverse (dough, chips, title):
	# Prepare output file for writing
	outputter (title)
	for i in chips:
		mix = ''
		for z in dough:
			mix += i 
			mix += z
		output.write( mix.encode( "utf-8" ))
		output.write( '\n')
	output.close()

# mixerSpaced adds spaces after chips. 
# It’s useful for building test strings for punctuation and virama.
def mixerSpaced (dough, chips, title):
	# Prepare output file for writing
	outputter (title)
	for i in dough:
		mix = ''
		for z in chips:
			mix += i
			mix += z
			mix += " "
		output.write( mix.encode( "utf-8" ))
		output.write( '\n')
	output.close()
	
# mixerKnConjunct	is used for generating permutations of Kannada subscript conjuncts
def mixerKnConjunct (dough, chips, title):
	
	# Prepare output file for writing
	output = open( title+'.txt', 'w')
	output.write( codecs.BOM_UTF8 )
	
	output.write ( title.encode( "utf-8" ))
	output.write( '\n')
	for i in dough:
		mix = ''
		for z in chips:
			mix += i
			mix += u"್"
			mix += z
		output.write( mix.encode( "utf-8" ))
		output.write( '\n')
	output.close()
    
# make the mixes!
# instead of using CLUI switches you have to delete the # at the beginning 
# of each line so it calls the relevant function. 

#Latin Mixes
mixer(majbasic, majbasic, 'Basic_Caps')
#mixer(majbasic, minbasic, 'Basic_Mixed')
#mixer(minbasic, minbasic, 'Basic_Lowercase')
#mixer(majuscules, majuscules, 'All_Caps')
#mixer(majuscules, minuscules, 'All_Mixed')
#mixer(minuscules, minuscules, 'All_Lowercase') 
#mixer(majuscules, punct, 'All_UC_Punct')
#mixer(minuscules, punct, 'All_LC_Punct')
#mixer(numerals, numerals, 'Numbers')
#mixer(numerals, math, 'Numbers_Math')
#mixer(numerals, currency, 'Numbers_Currency')
#mixer(numerals, prebuilt, 'Numbers_Prebuilts')
#mixer(prebuilt, math, 'Math_Prebuilts')
#mixer(numerals, numerals, 'All_Numbers')
#mixer(allbasic, numerals, 'Numbers_Alpha')
#mixer (majbasic, lc_control, 'CapsLCtest')
#mixer (adhesion, adhesion, 'adhesion_lc')
#mixer (adhesion, ADHESION, 'adhesion_mix')
#mixer (ADHESION, adhesion, 'adhesion_caps')
#mixer (adhesion, basicpunct, 'lc_punct')
#mixer (ADHESION, basicpunct, 'uc_punct')
#mixer (hamburgefontivs, hamburgefontivs, 'hamburgefontivs')
#mixer (numerals, allbasic, 'numerals_alpha')

#Devanagari Mixes
mixer (devaHalfConsonants, devaConsonants, 'deva_halfs')
reverse (devaHalfConsonants, devaConsonants, 'deva_halfs_reverse')
#mixer (devaNumerals, devaNumerals, 'deva_Numerals')
#mixer (devaNaRa, devaConsonants, 'deva_NaRa')
#reverse (devaNaRa, devaConsonants, 'deva_NaRa_reverse')

#Kannada Mixes
mixerSpaced (KannadaConsonants, KannadaVowels, 'KannadaVowelBruteForce')
mixerKnConjunct (KannadaConsonants, KannadaConsonants, 'KannadaConjunctsBruteForce')