#!/usr/bin/env python

import os
import sys
import docker
import subprocess
import tarfile

DEFAULT_BUFFER_LENGTH = 10
USAGE_ALIAS = "Usage: docker-cp [--buffer-length] <src_path_1> [src_path_2] ..... [src_path_n] <dest_path>"
PROCESS_ERROR_CODE = -1

def copyFileFromContainer(c_id, src_file_path, dest_file_path, buffer_length):
	client = docker.from_env()
	try:
		container = client.containers.get(c_id)
	except Exception as ex:
		print "Error in getting the container:", ex
		return False
	
	src_file_stream = None
	try:
		src_file_stream = container.get_archive(src_file_path)
	except Exception as ex:
		print "Error in getting the file stream:", ex
		return False

	src_raw_buffer = src_file_stream[0]
	src_file_name = src_file_stream[1]["name"]

	is_dest_path_directory = False
	try:
		is_dest_path_directory = os.path.isdir(dest_file_path)
	except Exception as ex:
		print "Error in reaching destination path:", ex
		return False

	if is_dest_path_directory:
		dest_file_path = os.path.join(dest_file_path, src_file_name)
	else:
		dest_file_path = os.path.join(".", dest_file_path)

	dest_file = None
	try:
		dest_file = open(dest_file_path, "w")
	except Exception as ex:
		print "Error in writing to destination file:", ex
		return False

	copy_buffer = None
	while True:
		copy_buffer = src_raw_buffer.read(buffer_length)
		if not copy_buffer:
			break
		dest_file.write(copy_buffer)
	dest_file.close()

	# Backup filename collision with possible actual filename is to be considered
	with tarfile.open(dest_file_path) as tar:
		tar_member = tar.getmembers()[0]
		tar_member.name = os.path.basename(dest_file_path) + "____.bak"
		tar.extract(tar_member, os.path.dirname(dest_file_path))

	os.rename(dest_file_path + "____.bak", dest_file_path)
	
	return True


if __name__ == "__main__":
	buffer_length = DEFAULT_BUFFER_LENGTH

	# Remove all options from paths
	all_path_args = []
	for arg in sys.argv[1:]:
		if arg.startswith("--buffer-length="):
			try:
				buffer_length = int(arg.lstrip("--buffer-length="))
			except Exception as ex:
				print "Warning: Exception in option parsing:", ex	
		else:
			all_path_args.append(arg)

	# Fetch destination path. If it fails, quickly terminate
	dest_file_path = ""
	if all_path_args:
		dest_file_path = all_path_args[-1]
	else:
		print "Error: Destination path is not found!"
		print USAGE_ALIAS
		os._exit(PROCESS_ERROR_CODE)

	# Fetch all source containers and path. Skip the invalid ones
	containers_and_files = []
	for arg in all_path_args[:-1]:
		delimiter_index = arg.find(":")
		if delimiter_index < 0:
			print "Warning: No ':' delimiter to separate host & path. Skipping", arg
		else:
			c_id = arg[:delimiter_index]
			c_file_path = arg[delimiter_index + 1:]
			containers_and_files.append((c_id, c_file_path))

	if not containers_and_files:
		# Check if there are valid source paths. If there are not, quickly terminate
		print "Error: There are not any valid source paths in parameters!"
		print USAGE_ALIAS
		os._exit(PROCESS_ERROR_CODE)
	else:
		# For each valid path, do the copy operation
		for c_id, c_file_path in containers_and_files:
			retval = copyFileFromContainer(c_id, c_file_path, dest_file_path, buffer_length)
			if not retval:
				print "Warning: File", c_id + ":" + c_file_path, "cannot be copied!"
	

