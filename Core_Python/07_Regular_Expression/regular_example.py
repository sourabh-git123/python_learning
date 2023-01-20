

import re

pattern = re.compile('\[(.*?)\]')

word = "Aye, [said Mr. Gibenson] Stark"

find_from_pattern = pattern.findall(word)

print(f"find from pattern = {find_from_pattern}  ")

print("=================================================")

find_from_pattern = find_from_pattern[0][1:-1]

print(f"find from pattern = {find_from_pattern}  ")

