import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da URL base
URL = "https://news.ycombinator.com/"