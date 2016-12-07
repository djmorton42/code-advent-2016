import operator

positional_histograms = None

recovered_message = ''

with open('input.txt') as file_handle:
    for line in file_handle:
        if positional_histograms is None:
            positional_histograms = []
            for _ in range(len(line.strip())):
                positional_histograms.append({})

        for index, char in enumerate(line.strip()):
            histogram = positional_histograms[index]    
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1


    for histogram in positional_histograms:
        recovered_message += min(histogram.iteritems(), key=operator.itemgetter(1))[0]

print "Message: " + recovered_message
