from pathlib import Path

def find_project_root(current_path: Path, marker: str = '.git') -> Path:
    """
    Traverse upwards from the current path to find the project root.

    This function traverses parent directories from the specified path until
    it finds a directory containing a specified marker, which indicates the
    project root.

    Args:
        current_path (Path): The starting directory path.
        marker (str): A filename or directory name that marks the root.
                      Defaults to '.git'.

    Returns:
        Path: The root directory of the project.

    Raises:
        FileNotFoundError: If the root directory with the specified marker
                           is not found.

    Usage example:
        project_root = find_project_root(Path('/path/to/a/project/subdir'))
        print(project_root)
    """
    for parent in current_path.parents:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError((f"Unable to find the root directory. No "
                             "'{marker}' found."))
