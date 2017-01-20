import numpy as np

##please read the txt file that is attached 
##I'm assuming that the files are in same directory
##in order to active, please comment off the bottom part

Bger = open("GCA_000762945.1_Bger_1.0_genomic.fna", "r").read()
terp =  open("GCA_001728815.2_terp_v2_2_genomic.fna", "r").read()
OryCun =  open("GCF_000003625.3_OryCun2.0_genomic.fna", "r").read()
icsasg = open("GCF_000233375.1_ICSASG_v2_genomic.fna", "r").read()
Xenopus =  open("GCF_001663975.1_Xenopus_laevis_v2_genomic.fna", "r").read()
mystery = open("mystery.fna", "r").read()

##mystery = ("GGTGTACCTCTAGAAAAAGACCCACATCCCCACCTCAactcgacaggaggcctgacaccccttttacTCGGGAGGATATcaagttccatgcctcaacatcAACACGAGTTGAGGCCCGACTCCCCTGTTGAAACACAATGGGaaacctgagatccctgtcacaacTGGAAAGGAACCCTGATTCCCGCCTCAACCTTAAATGAGCTCCTATATCACTTCAGCTACTTGATAGGAATCCCAAGGTGGCCCTCACAAGTTGAAAGGAGGCCTGAGTTCCCTGCAGcaacatgagaggctcactgaggtCTCCCTCGAAACTCAAGAGCAACCCAAAGCttcccgctgcaactcgagaaacaccacAAGATTTCCCCCTCAATTCTAAATAAGGCCCATCTCCCCCTCAGTGACTTGAAACCAATCCTGCACAACCCTTGCACCTCGAAAGGAGCCTAAACTAAACTCAGCCAAGACGAGAGGTACCCTGAGGTCTCcgtcacaacttgagaggaacccaaAGCTTCAGGCCGCAACTTGAGAAACACCACGAGATTCCAACCcaacgcgagatgaggccctttcccctgcagtgactctAGAGGAATCATGAGGTGCCCCTCACAACGCAAAATAGAGACCTGTCTTCCTTGAGGCAACAATAGCTGGTCACTGAGGTCACTgtcgcaactcaagaggaaccccatGCTTcccactgcaact")
##terp = ("TGTGGTATGATGAAGAGCCAATTGGTGCAAGGACAGATTGGGGTGAAGCATGGGATATCGTGGCCATTTCAGGGATGCTCCAAGATGGACTAATATTGCTCTCTTGGATACAgtttctctttgttctccaaagAGAATAAACACAAAAGTCCAAACTCCTGGCCAGCTGACCCTTAGCTGCCATCTGAACAACTTCCTCAGAGAACTTTACAAATAAGAATAACTGTTTAGCTTGTAACTCCGTTACTGTTTTGAGCTTGCTTTCAATTCCAGATTTCATTTCAGAATGCAGCAGAAGGCTAAGAACATTATTATTATGTATGGAAAACAGTCCTGCTTTATGATAGGGCCCAATCCAACCCCACTGAACTCTATGGGAGTCTTCCTGGACtttagtgagctttggatcaggccctaaatttggATTAAAAGAAGTGATTATTGAAGTCAGTGCAACTCATTTGAAGGACATTGAAGAGGATTTCTGATAAGAAGGTAATTCTAATAATTTGGAAAAGTTATTAATGTTAATAGCTAGGAACTGCAACCACTTTTATCTAAAATATCAGAGCTGGTTAAATTGAATCTAGTGACAGGAAGACAGTTTACCAGTggcaactttttaaaatctcaggacTATTTAAAGATAATTCTTGTGCATGAAATTAGTTCTTGGGAAACATGGAAAatgtaaatactttgcatttgcttAATAAAAAG")
def sequence_compare(seq_a, seq_b):
        len1= len(seq_a)
        len2= len(seq_b)
        mismatches = []
        for pos in range (0,min(len1,len2)) :
              if seq_a[pos] == seq_b[pos]:
                  mismatches.append(1)
              else:
                  mismatches.append(0)
	return mismatches
        ##print (seq_a)
        ##print (mismatches)
        ##print (seg_b)
		
def sequence_matching(matches):
	##it does division of 100, but it could larger, i don't recommend smaller
	averageFloat = len(matches)/float(100)
	averageInt = len(matches)/100
	scoreArray = []
	##somehow it was keep saying an error of cannot slice a 0-d array, so I did this way
	inithold = matches[:averageInt]
	initscore = sum(inithold)/averageFloat
	scoreArray.append(initscore)
	for i in range(averageInt - 1):
		threshold = matches[(i+1)*averageInt:(i+2)*averageInt]
		score = sum(threshold)/averageFloat
		scoreArray.append(score)
	# scoreArray = []
	# np.array_split(x,100)
	# for i in range(len(x)):
		# counter = 0
		# percentage = 0.0
		# for g in range(len(x[i])):
			# if "1":
				# counter += 1
		# percentage = counter/float(average)
		# scoreArray.append(percentage)
	for y in range(len(scoreArray)):
		if scoreArray[y] > 0.8:
			scoreArray.pop(y)
	overall = sum(scoreArray)/float(len(scoreArray))
	return overall	

def answer(match1, match2, match3, match4, match5):
	print ("Bger match is %s" (match1))
	print ("terp match is %s" (match2)) 
	print ("OryCun match is %s" (match3)) 
	print ("icsasg match is %s" (match4))
	print ("Xenopus match is %s" (match5)) 
	list =[match1, match2, match3, match4, match5]
	print("This one is more likely to the mystery gene %d", (max(list)))

#BgerMystery = sequence_compare(Bger,mystery)
#terpMystery = sequence_compare(terp,mystery)
OryCunMystery = sequence_compare(OryCun,mystery)
#icsasgMystery = sequence_compare(icsasg,mystery)
#XenopusMystery = sequence_compare(Xenopus,mystery)

#Bgermatch = sequence_matching(BgerMystery)
#terpmatch = sequence_matching(terpMystery)
OryCunmatch = sequence_matching(OryCunMystery)
#icsasgmatch = sequence_matching(icsasgMystery)
#Xenopusmatch = sequence_matching(XenopusMystery)
print(OryCunmatch)
#answer(Bgermatch, terpmatch, OryCunmatch, icsasgmatch, Xenopusmatch)