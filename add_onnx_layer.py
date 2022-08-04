# IMPORTING PYTHON PACKAGES
import sclblonnx as so
import onnx
import os
# print(os.getcwd())

# LOAD ONNX MODEL FROM FILE
graph1 = so.graph_from_file('../modified_A_ARS.onnx')

# DISPLAYING INPUTS AND OUTPUTS
print(so.list_inputs(graph1))
print(so.list_outputs(graph1))

# DELETE THE PREVIOUS UNUSED OUTPUT - NOT REQUIRED
so.delete_output(graph1, "converted_conv2d_4_Conv2D_0")

# ADD THE NEW OUTPUT WITH REQUIRED TYPE AND SHAPE
final_graph = so.add_output(graph1, "Conv1_Conv2D_0", "FLOAT16", [1,32,112,160])

# LIST OUTPUT AND CHECK MODEL IN NETRON
print(so.list_outputs(final_graph))
print(so.display(final_graph))

# EXPORT NEW MODEL TO FILE
g = so.graph_to_file(final_graph, "../output_modified_A_ARS.onnx", onnx_opset_version=8)

# MODEL IS GENERATED WITH ONNX IR VERSION 8
# RELOAD MODEL, CONVERT IT TO IR VERSION 4 AS IN THE ORIGINAL MODEL AND RESAVE IT
model = onnx.load('../output_modified_A_ARS.onnx')
model.ir_version=4
onnx.save(model, '../output_modified_A_ARS_irv4.onnx')

