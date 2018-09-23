# Thist script cats all the text files in the results directory.
find ./results/ -name 'm*.txt' -exec cat {} \;
