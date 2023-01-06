from tablecontent.utils import find_max
# pathlib types:relative and absolute path
from pathlib import Path


path = Path("tablecontent")
for file in path.glob('*.py'):
    print(file)

numbers = [5, 10, 25, 15]
result = find_max(numbers)
print(result)
