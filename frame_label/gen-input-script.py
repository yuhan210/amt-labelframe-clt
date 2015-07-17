import sys
import os

if __name__ == "__main__":
	
	if  len(sys.argv) != 3:
		print 'Usage', sys.argv[0], ' video_list anno_folder'
		exit(-1)

	#output_file = 'frame_label.input'
	videos = [x.strip() for x in open(sys.argv[1]).readlines()]
	frame_folder = sys.argv[2]
	
	#out_fh = open(output_file, 'w')
	#out_fh.write('images\n');

	counter = 0
	for video in videos:
		counter_2 = 0
		for f in os.listdir(os.path.join(frame_folder, video)):
				#out_fh.write(video + '&frame_name=' + f.split('.')[0] + '.jpg' + '\n')
			counter += 1
			counter_2 += 1		
		print video, counter_2


	print counter
	#out_fh.close()
		
