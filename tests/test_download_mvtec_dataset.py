# file tests/test_download_mvtec_dataset.py
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

# add root project to sys
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))
from ingestion.download_mvtec_ad_dataset import download_dataset  # noqa: E402


@pytest.fixture
def tmp_data_dir(tmp_path):
    return tmp_path / "data" / "raw"


@patch("ingestion.download_mvtec_ad_dataset.requests.get")
@patch("ingestion.download_mvtec_ad_dataset.tarfile.open")
def test_download_dataset(mock_tar, mock_get, tmp_data_dir):
    # mock http response
    mock_response = MagicMock()
    mock_response.headers = {"content-length": "1024"}
    mock_response.iter_content = lambda chunk_size: [b"x" * 1024]
    mock_get.return_value = mock_response

    # mock tar extraction
    mock_tar_instance = MagicMock()
    mock_tar.return_value.__enter__.return_value = mock_tar_instance
    mock_tar_instance.getmembers.return_value = []

    # start mocked download
    download_dataset(output_path=str(tmp_data_dir))

    # assertions
    assert tmp_data_dir.exists()
    mock_get.assert_called_once()
    mock_tar.assert_called_once()
