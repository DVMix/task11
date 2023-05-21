import zipfile
import glob
from tqdm import tqdm
from multiprocessing import Pool

path_to_zips = './data/archieves'
directory_to_extract_to = './data'


def extractor(path_to_zip_file):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


def main():
    zip_files = glob.glob(f'{path_to_zips}/*.zip')
    # with Pool(4) as p:
    #     r = list(tqdm(p.imap(extractor, zip_files), total=len(zip_files)))
    for file in tqdm(zip_files):
        extractor(file)


if __name__ == '__main__':
    main()
