from weather import Column, DataFrame, read_dataframe

def remove_slashes(data_input):
    no_slashes = []
    for line in data_input:
        no_slashes.append(line.replace("-", ""))
    clean_data = filter(lambda x: x != "", no_slashes)
    return list(clean_data)

if __name__ == "__main__":
    data_frame = None
    with open("football.dat") as dat:
        data = dat.readlines()
        data_frame =  read_dataframe(remove_slashes(data))
        # next: find the actual difference
        # possible problems: the first column has no header
