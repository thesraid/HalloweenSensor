#!/bin/bash
ffmpeg -r 24 -pattern_type glob -i '*.jpg' -c:v copy output.avi
