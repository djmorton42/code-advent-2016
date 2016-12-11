import re

class Decompressor:
    MARKER_PATTERN = re.compile('\(([0-9]+)x([0-9]+)\)')

    def decompress(self, input_text):
        decompressed_string = ''

        text = input_text

        while (len(text) > 0):
            match = self.MARKER_PATTERN.search(text)
           
            if match is not None:
                match_index = match.start()

                decompressed_string += text[:match_index]

                group_length = int(match.group(1))
                repetitions = int(match.group(2))

                compressed_group = text[match.end():match.end() + group_length]
                for _ in range(repetitions):
                    decompressed_string += compressed_group

                text = text[match.end() + group_length:]
            else:
                decompressed_string += text
                text = ''

        return decompressed_string
