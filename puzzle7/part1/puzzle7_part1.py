from segment import Segment

def do_any_hypernet_segments_contain_abba_sequence(segments):
    return len(
        [
            segment 
            for segment 
            in segments 
            if segment.is_hypernet_segment and segment.has_abba_sequence()
        ]
    ) > 0

def do_any_regular_segments_contain_abba_sequence(segments):
    return len(
        [
            segment 
            for segment 
            in segments 
            if not segment.is_hypernet_segment and segment.has_abba_sequence()
        ]
    ) > 0

with open('input.txt') as file_handle:
    count = 0

    for line in file_handle:
        sequences = [''] 
    
        for char in line:
           if char == '[':
               sequences.append(char)
           elif char == ']':
               sequences[len(sequences) - 1] += char
               sequences.append('')
           elif not char == '\n':
               sequences[len(sequences) - 1] += char

        segments = [Segment(sequence) for sequence in sequences]

        if (do_any_regular_segments_contain_abba_sequence(segments) 
            and not do_any_hypernet_segments_contain_abba_sequence(segments)):
            
            count += 1 

    print str(count) + " IPs support TLS"
