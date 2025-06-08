import os


ANSI_COLORS = {
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
            color_code = ANSI_COLORS.get(colour.lower(), ANSI_COLORS['reset'])
            return f"{color_code}{result}{ANSI_COLORS['reset']}"
        return wrapper
    return decorator


class CustomFile:
    def __init__(self, filepath):
        self._filepath = filepath

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, new_filepath):

        if not CustomFile.is_txt_file(new_filepath):
            raise ValueError("The given filepath is not a txt file")

        if not os.path.exists(new_filepath):
            raise FileNotFoundError(f"The file does not exist.")

        if not os.access(new_filepath, os.R_OK):
            raise PermissionError(f"Cannot read file.")

        self._filepath = new_filepath

    def read_file(self):
        with open(self.filepath, 'r') as file:
            for line in file:
                yield line

    @staticmethod
    def is_txt_file(filename):
        return filename.endswith('.txt')

    @classmethod
    def from_default_file(cls):
        default_path = 'default.txt'
        if not os.path.exists(default_path):
            with open(default_path, 'w') as f:
                f.write("This is a default file.\n")
        return cls(default_path)

    @colour_text('magenta')
    def __str__(self):
        return f"CustomFile: (path='{self.filepath}')"

    def __add__(self, other):
        if not isinstance(other, CustomFile):
            return NotImplemented

        new_filepath = 'combined_files.txt'

        with open(new_filepath, 'w') as new_file:
            for line in self.read_file():
                new_file.write(line)
            for line in other.read_file():
                new_file.write(line)

        return CustomFile(new_filepath)


class AdvancedFile(CustomFile):

    @colour_text('red')
    def __str__(self):
        return f"AdvancedFile: (path='{self.filepath}')"

    def read_file(self):
        with open(self.filepath, 'r') as file:
            for line in file:
                yield line

    @classmethod
    def concat_many_files(cls, *files):
        output_file = 'multi_combined_files.txt'
        with open(output_file, 'w') as out:
            for f in files:
                if not isinstance(f, CustomFile):
                    raise TypeError(f"Expected CustomFile, got {type(f).__name__}")
                for line in f.read_file():
                    out.write(line + '\n')

        return cls(output_file)


file = AdvancedFile("large_file.txt")
print(file)

