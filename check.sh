#!/bin/bash

for f in *.py; 
    do python -m py_compile "$f"; 
done