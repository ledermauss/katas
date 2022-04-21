class Column:
    def __init__(self, name, start, end, rows = None):
        self.name = name
        self.start = start
        self.end = end
        if rows is None:
            self.rows = []
        else:
            self.rows = rows

    def __eq__(self, other):
        if not isinstance(other, Column):
            return False
        rows_equal = len(self.rows) == len(other.rows)
        if not rows_equal:
            return False
        for i in range(len(self.rows)):
            rows_equal = rows_equal and (self.rows[i] == other.rows[i])
        return self.name == other.name and \
    self.start == other.start and self.end == other.end and rows_equal



class DataFrame:
    def __init__(self, columns):
        self.columns = columns

    def __eq__(self, other):
        if not isinstance(other, DataFrame):
            return False
        columns_equal = True
        for i in range(len(self.columns)):
            columns_equal = columns_equal and (self.columns[i] == other.columns[i])
        return columns_equal
        

if __name__ == "__main__":
    data_frame = None
    with open("weather.dat", "r") as dat:
        data = dat.readlines()
        data_frame = read_dataframe(data)


def read_dataframe(lines):
    columns = get_columns(lines[0])
    for line in lines:
        columns = assign_content_to_columns(columns, line)
    return DataFrame(columns)


def get_columns(header):
    starts, ends = get_content_indexes(header)
    names = header.split()
    columns = []
    for n, s, e in zip(names, starts, ends):
        columns.append(Column(n, s, e))
    return columns


def get_content_indexes(content):
    return get_content_starts(content), get_content_ends(content)


def get_content_starts(header):
    starts = []
    if is_char(header[0]):
        starts.append(0)
    for i in range(1, len(header)):
        if is_char(header[i]) and not is_char(header[i-1]):
            starts.append(i)
    return starts

    
def get_content_ends(header):
    ends = []
    for i in range(1, len(header)):
        if not is_char(header[i]) and is_char(header[i-1]):
            ends.append(i-1)
    if is_char(header[-1]):
        ends.append(len(header)-1)
    return ends


def is_char(c):
    return c != " "


# todo: add to Dataframeclass
def assign_content_to_columns(columns, line):
    starts, ends = get_content_indexes(line)
    idx = 0
    for column in columns:
        if idx >= len(starts):
            column.rows.append(None)
        elif content_is_in_column(starts[idx], ends[idx], column.start, column.end):
            column.rows.append(parse_content(line[starts[idx]:ends[idx]+1]))
            idx += 1
        else:
            column.rows.append(None)
            idx+=1
    return columns


def content_is_in_column(content_start, content_end, column_start, column_end):
    return not (content_start > column_end or content_end < column_start)


def parse_content(content):
    content = content.replace("*", "")
    if any(letter.isalpha() for letter in content):
        return content
    else:
        return float(content)



def get_spread(data_frame):
    return
