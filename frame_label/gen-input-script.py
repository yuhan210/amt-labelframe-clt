import sys
import os

if __name__ == "__main__":
	
	if  len(sys.argv) != 4:
		print 'Usage', sys.argv[0], ' video_list anno_folder imgs_per_task(9)'
		exit(-1)

	output_file = 'frame_label.input'
	videos = [x.strip() for x in open(sys.argv[1]).readlines()]
	anno_folder = sys.argv[2]
	img_per_task = int(sys.argv[3])
	out_fh = open(output_file, 'w')
	out_fh.write('images\n');

	total_counter = 0

	start_idx = 51
	end_idx = 200
	output_str = ''
	for v_idx, video in enumerate(videos):
		if v_idx < start_idx or v_idx > end_idx:
			continue

		anno_path = os.path.join(anno_folder, video)

		if not os.path.exists(anno_path):
			continue

		video_counter = 0
	
		output_str = ''
		for f in os.listdir(anno_path):
			## check image exists
			frame_name = f.split('.')[0]+ '.jpg'

			frame_path = os.path.join('/var/www/amt/images/' + video, f.split('.')[0] + '.jpg')
			if not os.path.exists(frame_path):
				print frame_path, 'does not exist'
				continue

			if os.path.exists(os.path.join('/var/www/amt/labels/' + video, f)):
				#print video, f , 'has been labeled'
				continue

			if video_counter % img_per_task == 0:

				if video_counter/img_per_task == 0: # the very first one
					output_str = video + '&frame_names=' + frame_name

				else:
					out_fh.write(output_str + '\n')
					output_str = video + '&frame_names=' + frame_name
			else:
				output_str += ';' + frame_name
		
			
			total_counter += 1
			video_counter += 1
		if len(output_str.split('=')[-1].split(';')) >= 8:
			out_fh.write(output_str + '\n')
		
		print video, video_counter
		if v_idx == end_idx:
			break

	print total_counter
	out_fh.close()
		
