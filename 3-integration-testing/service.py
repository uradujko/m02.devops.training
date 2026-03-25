import datastore


def process_and_store(key, raw_value):
    processed = raw_value.strip().upper()
    datastore.store_value(key, processed)
    return processed


def retrieve_processed(key):
    value = datastore.get_value(key)
    if value is not None:
        return value.lower()
    return None


def update_value(key, raw_value):
    processed = raw_value.strip().upper()
    datastore.store_value(key, processed)
    return processed


def delete_value(key):
    return datastore.delete_value(key)


def list_all_keys():
    return datastore.list_keys()
