import os


ANSI_COLOURS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m',
}


def colour_text(colour: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            colour_code = ANSI_COLOURS.get(colour.lower(), ANSI_COLOURS['reset'])
            return f"{colour_code}{result}{ANSI_COLOURS['reset']}"
        return wrapper
    return decorator


class CustomFile:
    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, new_filepath):

        if not CustomFile.is_txt_file(new_filepath):
            raise ValueError("The given filepath is not a txt file")

        if not os.path.exists(new_filepath):
            raise FileNotFoundError(f"The file does not exist.")

        self._filepath = new_filepath

    def read_file(self):
        with open(self.filepath, 'r') as file:
            for line in file:
                yield line.strip()

    @staticmethod
    def is_txt_file(filename):
        return filename.endswith('.txt')

    @colour_text('magenta')
    def __str__(self):
        return f"CustomFile: (path='{self.filepath}')"

    def __add__(self, other, output_path='combined_files.txt'):
        if not isinstance(other, CustomFile):
            return NotImplemented

        with open(output_path, 'w') as new_file:
            for line in self.read_file():
                new_file.write(line + '\n')
            for line in other.read_file():
                new_file.write(line + '\n')

        return CustomFile(output_path)


class AdvancedFile(CustomFile):

    @colour_text('blue')
    def __str__(self):
        return f"AdvancedFile: (path='{self.filepath}')"

    @classmethod
    def concat_many_files(cls, *files, output_path='multi_combined_files.txt'):
        for f in files:
            if not isinstance(f, CustomFile):
                raise TypeError(f"Expected CustomFile, got {type(f).__name__}")
        with open(output_path, 'w') as out:
            for f in files:
                for line in f.read_file():
                    out.write(line + '\n')

        return cls(output_path)
