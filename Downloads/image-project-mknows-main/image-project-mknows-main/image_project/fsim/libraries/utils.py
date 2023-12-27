from ..models import Face

def find_saved_signatures_by_nik(nik):
    """
    Find the saved signature images for a given National Identity Number (NIK).

    This function retrieves the paths of the anchor and 
    test signature images associated with the specified NIK.

    Parameters:
        nik (str): The National Identity Number (NIK) for 
        which signature images are to be retrieved.

    Returns:
        tuple: A tuple containing the paths of the anchor and test signature images.

    Example:
        >>> from ..function import find_saved_signatures_by_nik
        >>> anchor_path, test_path = find_saved_signatures_by_nik('1234567890')

    Note:
        - The function assumes there is one anchor and one 
        test signature image for the specified NIK.
        - The paths are obtained from the 'img' attribute of Face objects in the database.
    """
    anchor_sign = Face.objects.get(nik=nik, is_anchor=True)
    test_sign = Face.objects.get(nik=nik, is_anchor=False)
    anchor_path = anchor_sign.img.path
    test_path = test_sign.img.path

    return anchor_path, test_path


def delete_signature_data_by_nik(nik):
    """
    Delete signature data for a given National Identity Number (NIK).

    This function deletes all signature data associated with the specified NIK from the database.

    Parameters:
        nik (str): The National Identity Number (NIK) for which signature data is to be deleted.

    Example:
        >>> from ..function import delete_signature_data_by_nik
        >>> delete_signature_data_by_nik('1234567890')

    Note:
        - All Face objects in the database with the specified NIK are deleted.
        - Use with caution, as it permanently removes signature data.
    """
    Face.objects.filter(nik=nik).delete()
