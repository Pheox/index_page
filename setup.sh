#!/bin/sh

VIRTENV=flask

virtualenv $VIRTENV
source $VIRTENV/bin/activate
pip install -r reqs.txt
