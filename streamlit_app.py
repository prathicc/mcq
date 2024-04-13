import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.MCQ_Generator.utils import read_file,get_table_data
import streamlit as st
from src.MCQ_Generator.mcqgenerator import generate_evaluate_chain
from src.MCQ_Generator.logger import logging

