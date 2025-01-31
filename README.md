# Camera model identification based on forensic traces extracted from homogeneous patches

### Note: The code from the [pytorch-lightning](https://github.com/bgswaroop/scd-images/tree/pytorch-lightning) branch will replace the code in this branch. Simplifying training + evaluation flow for easy replication of results with additional documentation. 

This repository consists of code to reproduce the results reported in our paper. Experiments were conducted on
the Dresden data set. Access to the published [open access paper](https://doi.org/10.1016/j.eswa.2022.117769).

## Steps to get started / re-produce the results
### 1. Prepare the Dataset
- Download the Dresden dataset from the official website - https://dl.acm.org/doi/10.1145/1774088.1774427 (in case the link to the dataset download is not working, check the alternate resource here https://github.com/bgswaroop/scd-images/issues/1#issuecomment-1711647633)
- Restructure the data as shown below:

  - Retain the image file names and the names of the device directories as specified in the downloaded dataset.

            dataset_dir
            │
            ├── device_dir1
            │   ├── img_1
            │   ├── img_2
            │   └── ...
            ├── device_dir2
            │   ├── img_1
            │   ├── img_2
            │   └── ...
            └── ...

- Extract the homogeneous crops from each image and save the patches in an .lmdb database
  - project/data_modules/utils/extract_and_save_homo_patches.py

              homogeneous_crops_dir
              │
              ├── device_dir1
              │   ├── data.mdb
              │   └── lock.mdb
              │
              ├── device_dir2
              │   ├── data.mdb
              │   └── lock.mdb
              └── ...

- Create Train / Test splits 
  - Adjust the parameters to suit the splits. The default parameters correspond to the ones used in the paper.
  - project/data_modules/utils/train_test_split.py
  - No need to run this file manually, will be automatically called during execution train/test


#### Documentation is in progress - will be updated soon


  
### Citation

```
@article{bennabhaktula2022camera,
  title={Camera model identification based on forensic traces extracted from homogeneous patches},
  author={Bennabhaktula, Guru Swaroop and Alegre, Enrique and Karastoyanova, Dimka and Azzopardi, George},
  journal={Expert Systems with Applications},
  pages={117769},
  year={2022},
  publisher={Elsevier}
}
```   
