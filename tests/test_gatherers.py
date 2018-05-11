from nscollector import gatherers
from unittest.mock import Mock


def test_clean_census_objects():
    assert gatherers._clean_census_objects(
        [
            Mock(get=Mock(return_value=42), getText=Mock(return_value='forty-two')),
            Mock(get=Mock(return_value=43), getText=Mock(return_value='forty-three'))
        ]
    ) == [(43, 'forty-three'), (42, 'forty-two')]  # Alfabetical sorting based on t[1]


def test_issues_exist():
    mock_html_obj = Mock(getText=Mock(return_value='42'))
    assert gatherers._issues_exist([mock_html_obj]) == '42'
    mock_html_obj = Mock(getText=Mock(return_value=''))
    assert not gatherers._issues_exist([mock_html_obj])
