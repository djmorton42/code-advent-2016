from decompressor import Decompressor

with open('input.txt') as file_handle:
    decompressor = Decompressor()

    print "Decompressed String Length: " + str(decompressor.calculate_decompressed_length(file_handle.read().strip()))
