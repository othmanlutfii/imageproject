"""
Module: feature.py

This module contains functions for extracting information from KTP (Kartu Tanda Penduduk) using OCR.

Functions:
- ktp_ocr(data): Perform OCR on KTP data and extract relevant information.
"""
import re
from ..apps import OcrConfig
from ..libraries import utils


def ktp_ocr(data):
    """
    Perform OCR on KTP data.

    Args:
        data (str): The input data for OCR.

    Returns:
        dict: A dictionary containing extracted information, including all text,
        NIK, name, and address.
    """

    ktp_ocr_model = OcrConfig.ocr_model
    ocr_reader = ktp_ocr_model.ocr(data)
    utils.delete_uploaded_image(data)
    # List untuk menyimpan teks
    texts = []
    for sentences in ocr_reader:
        for item in sentences:
            # teks
            text = item[1][0]
            texts.append(text)
    texts_list = [item.replace(':', '') for item in texts]
    # Mengambil teks yang panjangnya tepat 16 karakter
    nik = [item for item in texts_list if re.match(r'^\d{16}$', item)]

    # Mencari indeks di mana "nama" muncul
    nama_indices = [i for i, item in enumerate(texts_list) if "nama" in item.lower()]

    for i in nama_indices:
        if i + 1 < len(texts_list) and "/" not in texts_list[i + 1]:
            nama = texts_list[i + 1]
        else:
            nama = texts_list[i + 2]

    # Mencari indeks di mana "nama" muncul
    alamat_indices = [
        i
        for i, item in enumerate(texts_list)
        if ("alamat" in item.lower()) or ("alamal" in item.lower())
    ]

    for i in alamat_indices:
        if (
            i + 1 < len(texts_list) and
            "gol" not in texts_list[i + 1].lower() and
            "darah" not in texts_list[i + 1].lower()
        ):
            alamat = texts_list[i + 1]
        elif (
            i + 2 < len(texts_list) and
            "gol" not in texts_list[i + 2].lower() and
            "darah" not in texts_list[i + 2].lower()
        ):
            alamat = texts_list[i + 2]

        if (
            i + 3 < len(texts_list) and
            "rt" not in texts_list[i + 3].lower() and
            "rw" not in texts_list[i + 3].lower()
        ):
            alamat += " " + texts_list[i + 3]
    data = {
        "all_text" : texts_list,
        "nik": nik[0],
        "nama": nama,
        "alamat": alamat
    }
    return data
