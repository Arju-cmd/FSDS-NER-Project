import argparse
import os
import logging

import yaml
from src.NER_utils import read_yaml, create_directories
from datasets import load_dataset

print(read_yaml("params.yaml"))