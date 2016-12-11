from decompressor import Decompressor

with open('input.txt') as file_handle:
    decompressor = Decompressor()

    decompressed_string = decompressor.decompress(file_handle.read().strip())

    print "Decompressed String Length: " + str(len(decompressed_string))

    
