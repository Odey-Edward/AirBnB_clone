#!/usr/bin/env python3
"""Definition of the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects
    Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): the User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
