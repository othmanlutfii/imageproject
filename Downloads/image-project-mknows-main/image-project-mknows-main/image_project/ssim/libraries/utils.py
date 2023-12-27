"""

This module provides utility functions for working with signature data.

"""

from ..models import Signature

def find_saved_signatures_by_nik(nik):
    """
    Finds saved anchor and test signature paths by the given National Identification Number (NIK).

    Parameters:
    - nik (str): National Identification Number.

    Returns:
    - Tuple containing the file paths of the anchor and test signatures.

    """
    anchor_sign = Signature.objects.get(nik=nik, is_anchor=True)
    test_sign = Signature.objects.get(nik=nik, is_anchor=False)
    anchor_path = anchor_sign.img.path
    test_path = test_sign.img.path

    return anchor_path, test_path

def delete_signature_data_by_nik(nik):
    """
    Deletes signature data associated with the given National Identification Number (NIK).

    Parameters:
    - nik (str): National Identification Number.

    """
    Signature.objects.filter(nik=nik).delete()
