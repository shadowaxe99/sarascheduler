#!/bin/bash

black .
flake8 .
mypy .
