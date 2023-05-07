class File:
    def add(self, text: str):
        with open('output/tokens.txt', 'w') as file:
            file.write(f'{text}\n')
            