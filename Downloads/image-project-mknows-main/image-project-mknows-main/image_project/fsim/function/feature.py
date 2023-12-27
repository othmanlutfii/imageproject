"""
Module for face-related tasks using OpenCV and DeepFace.

This module includes functionality for face-related tasks, 
utilizing the OpenCV and DeepFace libraries.
It also imports utility functions from the 'utils' module.

Imports:
    - `cv2`: OpenCV library for computer vision tasks.
    - `DeepFace`: A deep learning-based face recognition library.
    - `utils` from `..libraries`: Utility functions for face-related tasks.

Example:
    >>> import cv2
    >>> from deepface import DeepFace
    >>> from ..libraries import utils

Note:
    Ensure that the required libraries and utilities are installed and accessible.

See Also:
    - [OpenCV documentation](https://docs.opencv.org/) for OpenCV usage.
    - [DeepFace documentation](https://github.com/serengil/deepface) for DeepFace library usage.
    - 'utils' module for utility functions related to face tasks.
"""
import cv2
from deepface import DeepFace
from ..libraries import utils



def predict_similarity(serializer):
    """
    Predict face similarity based on signature images.

    This function takes a serializer containing face data, 
    retrieves the corresponding signature images,
    and uses the DeepFace library to verify the similarity between the images.

    Parameters:
        serializer: The serializer containing face data, 
        including the National Identity Number (NIK).

    Returns:
        tuple: A tuple containing the predicted similarity percentage and 
        a boolean indicating if the faces are similar.

    Example:
        >>> from ..serializers import FaceSerializer
        >>> from ..function import predict_similarity
        >>> serializer = FaceSerializer(data={'nik': '1234567890', ...})
        >>> similarity, is_similar = predict_similarity(serializer)

    Note:
        - The function relies on the 'utils' module for retrieving and deleting signature data.
        - The similarity is calculated as a percentage based on the distance returned by DeepFace.
        - If the faces are verified as similar, the corresponding signature data is deleted.
    """
    nik = serializer.data.get('nik')
    anchor_path, test_path = utils.find_saved_signatures_by_nik(nik)
    image1 = cv2.imread(anchor_path)
    image2 = cv2.imread(test_path)
    result = DeepFace.verify(image1, image2)
    verified = result['verified']

    if result['verified'] == True:
        jarak = result['distance']
        kemiripan = (((4 - jarak) / 4) * 100)
        utils.delete_signature_data_by_nik(nik)
        return kemiripan, verified
    else:
        kemiripan = 0
        utils.delete_signature_data_by_nik(nik)
        return kemiripan, verified
