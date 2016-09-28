import json
node_array = [(0,'adam'),
(1,'bob'),(2,'cherry'), (3,'dan'), (4,'david'),
(5,'eli'), (6,'faruq'), (7,'greg'), (8,'harry'),
(9,'indy'),(10,'jack'), (11,'kaylee'), (12,'kevin'),
(13,'larry'), (14,'matt'), (15,'nate'), (16,'ophelia')]

edge_array = [(1,2,1), (2,3,1), (3,4,1), 
(4,5,1), (5,6,1), (6,7,1), (7,8,1), 
(8,9,1), (9,10,1), (10,11,1), (11,12,1), 
(12,13,1), (13,14,1), (14,15,1), (15,16,1), 
(1,3,2), (1,4,2), (1,5,2), (1,6,2), (2,7,2),
(2,8,2),(2,9,2),(2,10,2),(2,11,2),(4,12,2),(5,13,2),
(6,14,2),(7,15,2)]

node_dict = []
link_dict = []

for node in node_array:
	node_dict.append({"name":node[1],"group": node[0]})

for edge in edge_array:
	link_dict.append({"source":edge[0],"target": edge[1], "value":edge[2]})


json_object = {
		"nodes": node_dict, 
		"links": link_dict
		}

with open('data.json', 'w') as outfile:
	json.dump(json_object, outfile, ensure_ascii=False)

print json_object
