import os


ANSI_COLOURS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}


def colour_text(colour: str):
    """
    Decorator to wrap the return value of a function with an ANSI color code.
    Args:
        colour (str): The color name to apply.
    Returns:
        function: Wrapped function that outputs colored text.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            colour_code = ANSI_COLOURS.get(colour.lower(), ANSI_COLOURS["reset"])
            return f"{colour_code}{result}{ANSI_COLOURS['reset']}"

        return wrapper

    return decorator


class CustomFile:
    """
    A custom object to represent and operate on .txt files.
    Provides file validation, reading via a generator, and file combination.
    """

    def __init__(self, filepath):
        """
        Initialize CustomFile instance and validate the file.
        Args:
            filepath (str): Path to a valid .txt file.
        """
        self.filepath = filepath

    @property
    def filepath(self):
        """Getter for the file path."""
        return self._filepath

    @filepath.setter
    def filepath(self, new_filepath):
        """
        Setter for the file path with validation.
        Raises:
            ValueError: If the file is not a .txt file.
            FileNotFoundError: If the file does not exist.
        """
        if not CustomFile.is_txt_file(new_filepath):
            raise ValueError("The given filepath is not a txt file")

        if not os.path.exists(new_filepath):
            raise FileNotFoundError("The file does not exist.")

        self._filepath = new_filepath

    def read_file(self):
        """
        Generator to read the file line by line.
        Yields:
            str: Each line in the file, stripped of newline characters.
        """
        with open(self.filepath, "r") as file:
            for line in file:
                yield line.strip()

    @staticmethod
    def is_txt_file(filename):
        """
        Check if a file has a .txt extension.
        Args:
            filename (str): Filename to check.
        Returns:
            bool: True if it's a .txt file, False otherwise.
        """
        return filename.endswith(".txt")

    @colour_text("magenta")
    def __str__(self):
        """
        String representation of the object, styled in magenta.
        Returns:
            str: File description string.
        """

        return f"CustomFile: (path='{self.filepath}')"

    def __add__(self, other, output_path="combined_files.txt"):
        """
        Concatenate this file with another CustomFile and save the result.
        Args:
            other (CustomFile): Another file to concatenate.
            output_path (str): Path to the output file.
        Returns:
            CustomFile: New CustomFile instance for the combined output.
        """

        if not isinstance(other, CustomFile):
            return NotImplemented

        with open(output_path, "w") as new_file:
            for line in self.read_file():
                new_file.write(line + "\n")
            for line in other.read_file():
                new_file.write(line + "\n")

        return CustomFile(output_path)


class ExtendedFile(CustomFile):
    """
    An advanced subclass of CustomFile with additional functionality.
    Overrides __str__ and adds support for concatenating many files.
    """

    @colour_text("blue")
    def __str__(self):
        """
        String representation of the object, styled in blue.
        Returns:
            str: File description string.
        """
        return f"AdvancedFile: (path='{self.filepath}')"

    @classmethod
    def concat_many_files(cls, *files, output_path="multi_combined_files.txt"):
        """
        Concatenate multiple CustomFile instances into one file.
        Args:
            *files (CustomFile): Files to concatenate.
            output_path (str): Path to the output file.
        Returns:
            AdvancedFile: A new instance representing the combined file.
        Raises:
            TypeError: If any input is not a CustomFile instance.
        """
        for f in files:
            if not isinstance(f, CustomFile):
                raise TypeError(f"Expected CustomFile, got {type(f).__name__}")
        with open(output_path, "w") as out:
            for f in files:
                for line in f.read_file():
                    out.write(line + "\n")

        return cls(output_path)
