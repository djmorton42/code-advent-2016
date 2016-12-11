import re

class Decompressor:
    MARKER_PATTERN = re.compile('\(([0-9]+)x([0-9]+)\)')

    def calculate_decompressed_length(self, input_text):
        decompressed_length = self.process(input_text)
        return decompressed_length

    def process(self, input_text):
        first_compressed_sequence_match = self.MARKER_PATTERN.search(input_text)
        
        if first_compressed_sequence_match is None:
            #No compressed sequences
            return len(input_text)
        else:
            leading_character_count = first_compressed_sequence_match.start()
            text = input_text[leading_character_count:]

            return leading_character_count + self.process_compressed_sequence(text)

    def process_compressed_sequence(self, input_text):
        matcher = self.MARKER_PATTERN.search(input_text)
 
        compressed_sequence_length = int(matcher.group(1))
        repetitions = int(matcher.group(2))

        compressed_text = input_text[matcher.end():matcher.end() + compressed_sequence_length]
        remainder = input_text[matcher.end() + compressed_sequence_length:]

        remainder_length = 0 if len(remainder) == 0 else self.process(remainder)

        compressed_sequence_length = repetitions * self.process(compressed_text)

        return remainder_length + compressed_sequence_length

