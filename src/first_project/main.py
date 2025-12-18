#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

# PROJE ADIN 'first_project' OLDUĞU İÇİN BURASI ÇOK ÖNEMLİ:
from first_project.crew import FirstProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    # Girdilerimiz (Inputs)
    inputs = {
        'sehir': 'Roma',
        'gun_sayisi': '3',
        'ilgi_alanlari': 'Tarih, Kolezyum, İtalyan Makarnası, Sokak Müzisyenleri',
        'para_birimi': 'Euro'
    }

    try:
        # FirstProject sınıfını çalıştırıyoruz
        FirstProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

# Aşağıdakiler hata vermemesi için boş bırakıldı
def train():
    pass

def replay():
    pass

def test():
    pass