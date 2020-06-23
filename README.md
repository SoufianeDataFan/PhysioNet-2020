# PhysioNet-2020


For now, this repo contains only scripts to help download data of the challenge and gather it in one directory automatically.

### Prerequisites

You'll need `gs` google cloud sdk installed on your machine. If you don't have it, just run this commands on your


- linux machine
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

You should find all files in `data` dir. 
