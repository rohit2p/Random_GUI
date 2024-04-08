import unittest.mock as mock
import doc_pytest.Mock.service as service


@mock.patch("doc_pytest.Mock.service.get_user_from_id")
def test_get_user_by_id(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_id(1)

    assert user_name == "Mocked Alice"