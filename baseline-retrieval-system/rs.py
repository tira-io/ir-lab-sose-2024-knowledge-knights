# Imports
from tira.third_party_integrations import ensure_pyterrrier_is_loaded, persist_and_normalize_run
from tira.rest_api_client import Client
import pyterrier as pt

# Create a REST client to the TIRA platform for retrieving the pre-indexed data.
ensure_pyterrier_is_loaded()
tira = Client()