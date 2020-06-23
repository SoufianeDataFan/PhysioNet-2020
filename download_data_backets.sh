gsutil -m cp -R gs://physionet-challenge-2020-12-lead-ecg-public/ .
cd physionet-challenge-2020-12-lead-ecg-public/
# unzip files
for file in *.tar.gz; do tar -zxf "$file"; done

python ~/PhysioNet-2020/move_files.py
