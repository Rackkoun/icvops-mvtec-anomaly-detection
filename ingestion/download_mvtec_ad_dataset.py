# file ingestion/download_mvtec_ad_dataset.py
from pathlib import Path
import tarfile
from tqdm import tqdm
import requests

MVTEC_DATASET_URL = "https://www.mydrive.ch/shares/38536/3830184030e49fe74747669442f0f283/download/420938113-1629960298/mvtec_anomaly_detection.tar.xz"


def download_dataset(output_path: str = "data/raw") -> None:
    root_path = Path(__file__).cwd().resolve()
    output_dir = root_path / output_path
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = "mvtec_anomaly_detection.tar.xz"
    filepath = output_dir / filename
    # check if already downloaded
    if filepath.exists():
        print(f"Dataset already exists at: {filepath}")
        return
    # download dataset
    response = requests.get(MVTEC_DATASET_URL, stream=True)
    # get file total size
    total_size = int(response.headers.get("content-length", 0))

    with open(filepath, "wb") as f:
        with tqdm(
            total=total_size, unit="B", unit_scale=True, desc="Downloading MVTec AD..."
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                pbar.update(len(data))

    # extract dataset
    with tarfile.open(filepath, "r:xz") as tar:
        members = tar.getmembers()
        for member in tqdm(members, desc="Extracting MVTec Dataset..."):
            tar.extract(member, output_dir)

    # remove archive file
    filepath.unlink()
    print(f"Dataset extractd to: {output_dir}")
    print("Done!")


if __name__ == "__main__":
    download_dataset()
