from segment import Segment

def get_aba_sequences(segments):
    aba_segments = []

    for segment in segments:
        if not segment.is_hypernet_segment:
            aba_segments.extend(segment.get_aba_sequences())

    return aba_segments

def do_any_hypernet_segments_contain_aba_sequence(segments, aba_sequences):
    return sum([segment.contains_bab_sequence(aba_sequences) for segment in segments if segment.is_hypernet_segment]) > 0

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

        aba_sequences = get_aba_sequences(segments)

        if do_any_hypernet_segments_contain_aba_sequence(segments, aba_sequences):
            count += 1

    print str(count) + " IPs support SSL"
