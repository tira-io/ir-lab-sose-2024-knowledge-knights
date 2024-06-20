
# Imports
from tira.third_party_integrations import ensure_pyterrier_is_loaded, persist_and_normalize_run
from tira.rest_api_client import Client
import pyterrier as pt

from pyterrier.measures import *

if not pt.started():
    pt.init(boot_packages=['mam10eks:custom-terrier-token-processing:0.0.1', 'com.github.terrierteam:terrier-prf:-SNAPSHOT'])
    from jnius import autoclass

tira = Client()

# This line creates an IRDSDataset object and registers it under the name provided as an argument.
pt_dataset = pt.get_dataset('irds:ir-lab-sose-2024/ir-acl-anthology-20240504-training')

# A (pre-built) PyTerrier index loaded from TIRA
index = tira.pt.index('ir-lab-sose-2024/tira-ir-starter/Index (tira-ir-starter-pyterrier)', pt_dataset)

#definition of BM25 retrieval pipeline
bm25 = pt.BatchRetrieve(index, wmodel="BM25")

#starting the run
print('First, we have a short look at the first three topics:')
pt_dataset.get_topics('text').head(3)

print('Now we do the retrieval...')
run = bm25(pt_dataset.get_topics('text'))

print('Done. Here are the first 10 entries of the run')
run.head(10)

persist_and_normalize_run(run, system_name='bm25-baseline', default_output='../runs')