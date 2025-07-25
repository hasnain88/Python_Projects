import os
import zlib,base64



def compress(inputfile, outputfile):
    script_dir = os.path.dirname(__file__)  # Folder of the script
    # file_path = os.path.join(script_dir, 'demo.txt')

    data = open(os.path.join(script_dir, inputfile),'r').read()
    data_bytes = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(os.path.join(script_dir, outputfile),'w')
    compressed_file.write(decoded_data)

# compress('demo.txt','ot.txt')

def decompress(inputfile, outputfile):
    script_dir = os.path.dirname(__file__)  # Folder of the script
    file_content  = open(os.path.join(script_dir, inputfile),'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(os.path.join(script_dir, outputfile),'w')
    file.write(decoded_data)
    file.close

decompress('ot.txt','dc1.txt')