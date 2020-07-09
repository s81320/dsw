def create_set_link_ids(file_links ):
	file_ids = set()

	# ids from the links we already collected

	with open( file_links , "r") as link_file:
		all_lines = link_file.readlines()
		for line in all_lines:
			print(line[-14:-1])
			file_ids.update([line[-14:-1]]) # put the string in [] or else it will be split into characters

	return(file_ids)


def main():

	bestands_file = "links-nytimes-2020-07-07.txt" # appears once in code 
	scraped_file = "links-nytimes-2020-07-08.txt" # appears twice in code and is used to create the name for the output file

	ids_bestand = create_set_link_ids(bestands_file)
	ids_scraped = create_set_link_ids(scraped_file)

	ids_new = set(ids_scraped).difference(set(ids_bestand))

	split_string = scraped_file.split('.',1) # split at the dot, split only once and into two parts
	new_file = split_string[0]+'-new.'+split_string[1] # file for new links

	with open(new_file , "w") as write_file , open(scraped_file , "r") as read_file:
		all_lines = read_file.readlines()
		for line in all_lines:
			#print(line)
			if(line[-14:-1] in ids_new):
				write_file.write(line)

if __name__ == "__main__":
	main()


