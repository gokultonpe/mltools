import csv
import sys
import onnx
import json
import time
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import Parse


print("ONNX Model Parser")
print("Current Capabilites")
print("-->Convert ONNX model to JSON Format")
print("-->Dump all the ONNX operators to a output csv file")
if(len(sys.argv) < 3):
        print("Please specify input ONNX model")
        print("Usage: onnxtojson.py <onnx_model.onnx> <model_name>")
        sys.exit()

# Convert onnx model to JSON
#model_path = "sqv76g30v9x360_DB.onnx"
#model_path = "best_fastmask_query_resnet18.onnx"
model_path = sys.argv[1]
model_name = sys.argv[2]

onnx_model = onnx.load(model_path)
s = MessageToJson(onnx_model)
onnx_json = json.loads(s)

# Convert JSON to String
onnx_str = json.dumps(onnx_json,indent = 4)

#timestr = time.strftime("%Y%m%d-%H%M%S")
#outfilename = timestr+""
outfile_csv_name = "%s_operatorlist.csv" %model_name
outfile_json_name = "%s.json" %model_name
OperatorList = []

OutputCsvFieldNames = ['Operators']
#Outputcsvfile = open('OperatorList.csv', 'w', newline='')
Outputcsvfile = open(outfile_csv_name, 'w', newline='')
Outputcsvwriter = csv.DictWriter(Outputcsvfile, fieldnames=OutputCsvFieldNames)
Outputcsvwriter.writeheader()

print("Generating model json... ",outfile_json_name)
with open(outfile_json_name, "w") as outfile: 
	outfile.write(onnx_str)

print("Generating Operator list csv... ", outfile_csv_name)
outfile = open("outfile", "r")
lines = outfile.readlines()

#PArse lines
for line in lines:
        line = line.strip()
        #wordpress
        if line.find("opType") != -1:
        	v = line.partition(":")[2]
        	OperatorList.append(v)
        	Outputcsvwriter.writerow({'Operators':v})

print("Done")
#print("OperatorList=",OperatorList)
