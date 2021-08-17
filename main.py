from googleapiclient.discovery import build
a = "AIzaSyBb96J0bvrLnHS-0xgcEM9LIy_GGZQxphc"
b = "8be1c5c23f30c6fb6"

def get_wiki_links(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res
