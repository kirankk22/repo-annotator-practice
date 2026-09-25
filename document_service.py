def fetch_document(document_id):
    # Pretend this calls an external service
    return {
        "id": document_id,
        "title": "Sample Document",
        "status": "active"
    }


def get_document_title(document_id):
    document = fetch_document(document_id)
    return document["title"]