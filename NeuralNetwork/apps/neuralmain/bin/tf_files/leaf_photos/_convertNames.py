raw_file = open('_plant_dict.leafsp', 'r')
reformated_file = open('_plant_dict_reformated.leafsp', 'w')

for line in raw_file:
    reformated_file.write("'" + line.replace(':', "':'").replace('\n', '') + "',\n")

print('>>>Reformat Done')
raw_file.close()
reformated_file.close()
