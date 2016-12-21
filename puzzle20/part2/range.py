class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def union(self, other_range):
        if other_range.start >= self.start and other_range.end > self.end:
            self.end = other_range.end
        elif other_range.start < self.start and other_range.end <= self.end:
            self.start = other_range.start
        elif other_range.start < self.start and other_range.end > self.end:
            self.start = other_range.start
            self.end = other_range.end

    def intersects(self, other_range):
        if other_range.start >= self.start and other_range.end <= self.end:
            return True
        elif other_range.start >= self.start and other_range.start <= self.end and other_range.end > self.end:
            return True
        elif other_range.start < self.start and other_range.end >= self.start and  other_range.end <= self.end:
            return True
        elif other_range.start < self.start and other_range.end > self.end:
            return True
        else:
            return False

    def number_of_ips_in_range(self):
        return self.end - self.start + 1

    def __str__(self):
        return "Range: " + str(self.start) + " -> " + str(self.end) + " (" + str(self.number_of_ips_in_range()) + " numbers)"
