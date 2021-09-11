#!/usr/bin/env bash
pytest && coverage run --branch --source gilded_rose,gilded_rose_test gilded_rose_test.py && coverage report -m && coverage html