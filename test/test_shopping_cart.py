from unittest.mock import Mock
import pytest
from doc_pytest import shoppingcart as s
from doc_pytest.item_database import ItemDatabase


@pytest.fixture
def cart():
    # All setup for the cart here…
    return s.ShoppingCart(5)

def test_add_items_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1

def test_when_add_more_then_one_items_should_fail(cart):
    for _ in range(6):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")

# def test_if_total_prize_of_each_match_or_not(cart):
#     # cart = s.ShoppingCart(5)
#     cart.add("apple")
#     cart.add("orange")
#     prize_map = {
#         "apple":1.0,
#         "orange": 2.0
#     }
#
#     assert cart.prize(prize_map) == 3.0

def test_if_total_prize_of_each_match_or_not(cart):
    # cart = s.ShoppingCart(5)
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item:str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.prize(item_database) == 3.0
