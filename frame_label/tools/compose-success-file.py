import csv
import sys


if __name__ == "__main__":

	if len(sys.argv) != 	2:
		print 'Usage:', sys.argv[0], 'turker.results'
		exit(-1)


	
	csv_file = open(sys.argv[1])
	csv_reader = csv.DictReader(csv_file, delimiter="\t")

	out_file = open('frame_label_m.success', 'w')
	out_file.write('hitid\thittypeid\n')
	counter = 0
	for row in csv_reader:
				
		if row['Answer.workerId'] == None or len(row['Answer.workerId']) == 0: # done hits
			continue

		hittypeid = row['hittypeid']
		hitid = row['hitid']
		out_file.write(hitid + '\t ' + hittypeid + '\n')

	out_file.close()

