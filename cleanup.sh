# Script for removing generated files.  To show the files being generated
# run this first, then the python script.
# NOTE: The Python script removes files before re-logging.
#       see fa_logger.remove_previous_files
find ./results/ -name '*.*' -delete
