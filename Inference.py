import json
import chromadb
from sentence_transformers import SentenceTransformer
import time


# Load the data back from the JSON file
try:
    with open('sections_data.json', 'r', encoding='utf-8') as json_file:
        loaded_data = json.load(json_file)
        print("Data successfully loaded from sections_data.json")
        print(loaded_data)
except FileNotFoundError:
    print("The JSON file does not exist.")




client = chromadb.Client()



embedding_model = SentenceTransformer("all-mpnet-base-v2")

new_collection = client.create_collection(name="my_new_collection_8")

# print([obj["id"] for obj in loaded_data])

from collections import Counter

def get_duplicates(input_list):
    element_counts = Counter(input_list)
    duplicates = [element for element, count in element_counts.items() if count > 1]
    return duplicates

my_list = [obj["id"] for obj in loaded_data]
print("Duplicate elements:", get_duplicates(my_list))  # Output: Duplicate elements: [2, 3]

new_collection.add(
    documents = [obj["text"] for obj in loaded_data],
    embeddings = embedding_model.encode([obj["text"] for obj in loaded_data]),
    # metadatas = [{"source": "cricket"},{"source": "football"},{'source':'election'},{"source":"ai revolution"}],
    ids = [obj["id"] for obj in loaded_data]
)

def getResults2(msg):
    return msg

def getResults(query):
  start_time = time.time()  # Record the start time

  results = new_collection.query(
      query_embeddings=embedding_model.encode([query]),
      n_results=1
  )

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"\nTime taken: {elapsed_time:.2f} seconds")   

  print('section--> ',results['ids'][0][0])
  print('distances--> ',results['distances'])
  print(results)
  results['genarated_link']=f"https://avishkanirmitha.github.io/karbon-doc/#{results['ids'][0][0]}"
  return results

# getResults('what is the trading')