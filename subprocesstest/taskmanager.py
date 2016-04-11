#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE, STDOUT
import os

# def _relay_stream(ori_uri, des_uri, stdout_file, stderr_file):
#     cmd = "ffmpeg -i %s -c copy -f flv %s" % (ori_uri, des_uri)
#     return Popen(cmd, shell=True, stdout=stderr_file, stderr=stderr_file)

def _relay_stream(ori_uri, des_uri):
    cmd = "ffmpeg -i %s -c copy -f flv %s" % (ori_uri, des_uri)
    return Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)

def main():
	session_id = 1
	session_stdout_path = os.path.join(
										os.path.dirname(__file__),
										r'./data/sessionlog/%s_stdout.log' % session_id
									)
	stdout_file = open(session_stdout_path, 'w')
	session_stderr_path = os.path.join(
										os.path.dirname(__file__),
										r'./data/sessionlog/%s_stderr.log' % session_id
									)
	stderr_file = open(session_stderr_path, 'w')
	pull_url = "rtmp://rtmplive01.e.vhall.com/vhall/935598495"
	push_url = "rtmp://rtmplive01.e.vhou.net/vhall?token=alibaba/883018441"
	relay_task = _relay_stream(pull_url, push_url)
	print relay_task.stdout.readline()
	relay_task.wait()
	# relay_task.kill()
	stdout_file.close()
	stderr_file.close()

if __name__ == '__main__':
	main()
