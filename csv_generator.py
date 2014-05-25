class CSVGenerator():

    def __init__(self):
        pass


    def generate(self, n_rows, n_cols):
        headers = []

        for i in range(n_cols):
            headers.append("col" + str(i))

        data = []

        data.append(headers)

        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                row.append(str(i) + str(j))

            data.append(row)

        return data





