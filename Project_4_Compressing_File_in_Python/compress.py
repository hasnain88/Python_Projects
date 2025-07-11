import os
import zlib,base64



script_dir = os.path.dirname(__file__)  # Folder of the script
file_path = os.path.join(script_dir, 'demo.txt')

# with open(file_path, 'r') as f:
#     data = f.read()

# print(data)


data = open(file_path,'r').read()
data_bytes = bytes(data,'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
decoded_data = compressed_data.decode('utf-8')
compressed_file = open(os.path.join(script_dir, 'compressed.txt'),'w')
compressed_file.write(decoded_data)


decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)

