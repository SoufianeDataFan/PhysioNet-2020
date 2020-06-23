# PhysioNet-2020


For now, this repo contains only scripts to help download data of the challenge and gather it in one directory automatically.

### Prerequisites

You'll need `gs` google cloud sdk installed on your machine. If you don't have it, run this commands on your terminal
```
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

if you have windows go to this [link](https://cloud.google.com/storage/docs/gsutil_install#windows) to install `gs`.


### How does it work?

Clone this repo and run this `download_data_backets.sh` file

```
git clone https://github.com/SoufianeDataFan/PhysioNet-2020.git ; cd PhysioNet-2020
bash download_data_backets.sh
```

You should find all files in `data` dir. Final dir tree shoudl be like this : 

```
PhysioNet/
├── physionet-challenge-2020-12-lead-ecg-public
│   ├── data
│   ├── Training_2
│   ├── Training_PTB
│   ├── Training_StPetersburg
│   ├── Training_WFDB
│   └── WFDB
```

Feel free to remove `physionet-challenge-2020-12-lead-ecg-public` because all your files are moved in `data` dir
