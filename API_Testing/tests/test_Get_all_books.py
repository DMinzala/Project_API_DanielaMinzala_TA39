from requests_folder.Get_all_books import get_all_books


class Test_get_books:

    def test_get_all_books_no_filter_check_response_status(self):
        response = get_all_books()
        assert response.status_code == 200, f"Error: the expected status code is 200 but got {response.status_code}"

    def test_get_all_books_no_filter_check_number_of_results(self):
        response = get_all_books().json()
        assert len(response) == 6, f"Error: the number of results returned is incorrect"

    def test_get_all_books_filter_by_type_fiction(self):
        response = get_all_books("fiction").json()
        assert len(response) == 4, f"Error: the number of results returned is incorrect"
        for i in range(len(response)):
            assert response[i]["type"] == "fiction", "Error: the type of the book is incorrect"

    def test_get_all_books_filter_by_type_non_fiction(self):
        response = get_all_books("non-fiction").json()
        assert len(response) == 2, f"Error: the number of results returned is incorrect"
        for i in range(len(response)):
            assert response[i]["type"] == "non-fiction", "Error: the type of the book is incorrect"

    def test_get_all_books_filter_by_type_non_existing_type(self):
        response = get_all_books("comedy")
        assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
        assert response.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

    def test_get_all_books_filter_by_type_invalid_type_special_characters(self):
        response = get_all_books("!@£$%^&*()_-=[];'\\,./<>?:|{}")
        assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
        assert response.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

    def test_get_all_books_filter_by_type_invalid_type_numbers(self):
        response = get_all_books("12234567890")
        assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
        assert response.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

    def test_get_all_books_filter_by_type_with_space(self):
        response = get_all_books("non fiction")
        assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
        assert response.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

    def test_get_all_books_filter_by_limit_inf(self):
        response = get_all_books(limit=1)
        assert response.status_code == 200, f"Error: the expected status code is 200 but got {response.status_code}"
        assert len(response.json()) == 1, f"Error: the number of results returned is incorrect"

    def test_get_all_books_filter_by_limit_between(self):
        response = get_all_books(limit=5)
        assert response.status_code == 200, f"Error: the expected status code is 200 but got {response.status_code}"
        assert len(response.json()) == 5, f"Error: the number of results returned is incorrect"

    def test_get_all_books_filter_by_limit_sup(self):
        response = get_all_books(limit=21)
        assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
        assert response.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", f"Invalid error message. Expected: 'Invalid value for query parameter 'limit'. Cannot be greater than 20.', actual: {response.json()['error']}"

    def test_get_all_books_filter_by_limit_negative(self):
        response = get_all_books(limit=-1)
        assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
        assert response.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0.", f"Invalid error message. Expected: 'Invalid value for query parameter 'limit'. Must be greater than 0.', actual: {response.json()['error']}"
