import unittest.mock as mock
import requests
import Random_GUI.doc_pytest.Mock.service as service


@mock.patch("Random_GUI.doc_pytest.Mock.service.get_user_from_id")
def test_get_user_by_id(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_id(1)

    assert user_name == "Mocked Alice"

"""test function using unittest.mock to mock the behavior of an API request using the requests library"""
@mock.patch("requests.get")
def test_get_user_through_api(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "rohit prasad"}
    mock_get.return_value = mock_response
    data = service.get_user_through_api()
    assert data == {"id": 1, "name": "rohit prasad"}

"""
In the test code test_get_user_through_api, we put mock_response into mock_get because mock_get is a mock object that 
simulates the requests.get function. By assigning mock_response to mock_get.return_value, we are configuring the mock 
object to return mock_response whenever requests.get is called within the get_user_through_api function.
"""

"""
When the test runs and get_user_through_api is called, instead of making a real HTTP request to 
https://jsonplaceholder.typicode.com/todos/1, the patched requests.get function (represented by mock_get) 
returns mock_response.This allows the test to control the response of the API call and verify that get_user_through_api
 handles the response correctly.
"""