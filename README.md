##  This is an implementation of our paper [Aggressive Language Detection Using VGCN-BERT for Spanish Texts](https://link.springer.com/chapter/10.1007/978-3-030-91699-2_25)

this Repo contains a dataset, pre-processing, and VGCN-BERT model using Python.

### Description
-  preparadataset.py
-  datasetvgraph.py
-  data(folder) where our dataset is located MEX-A3T, and a sample of other
-  output(folder) with the results(txt) and the weights of the VGCN_BERT16(using it if you want to test for inference purposes).
-  error analysis and other utility Python scripts

> **Note:** if you want to see experiments please look at the `output` folder and check results_...txt files, where all the parameters and the scores are saved after training.

## Setup and requirements:

download the PyTorch BETO SPANISH pre-trained model by this [site](https://github.com/dccuchile/beto) in the Download section choose Pytorch uncased if not work click [here](https://users.dcc.uchile.cl/~jperez/beto/uncased_2M/pytorch_weights.tar.gz), then go the folder called `pytorch_pretrained_bert`an change line 723 in `modeling.py` to the file located custom on my case in desktop and other additional setting may you have to do, in other words:

-- `resolved_archive_file ='/home/wilderd/Desktop/BETO/pytorch/pytorch_model.bin' `
to `resolved_archive_file ='/home/USER/Desktop/BETO/pytorch/pytorch_model.bin' `

## dependencies installations
* we are using virtual env from Anaconda with ubuntu 20.4 LTS
* and running with Python 3.7
* other specific frameworks may you require are listed below:
*
```
python         3.6
pytorch        1.7.0
transformers   3.5.0
pytorch_pretrained_bert 0.6.2
nlkt           3.5

```
## run 🚀 
* train and test results are made in the `train.py` script, So please use this script for running the test itself(sorry for not providing separate file 😄 )
```
python train.py --ds mx --sw 1
```
## cite 📜

if this was useful for you don't forget to cite:
```
@inproceedings{mamani2021aggressive,
  title={Aggressive Language Detection Using VGCN-BERT for Spanish Texts},
  author={Mamani-Condori, Errol and Ochoa-Luna, Jos{\'e}},
  booktitle={Brazilian Conference on Intelligent Systems},
  pages={359--373},
  year={2021},
  organization={Springer}
}
```
