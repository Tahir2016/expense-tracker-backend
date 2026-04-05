
def transaction_entity(txn):
    return {
        "id" : str(txn["_id"]),
        "title" : txn["title"],
        "amount" : txn["amount"],
        "type" : txn["type"],
        "category" : txn["category"],
        "created_at": txn["created_at"].isoformat() if txn.get("created_at") else ""
    }

def transactions_entity(txns):
    result = []
    for txn in txns:
        result.append(transaction_entity(txn))
    return result

# [transaction_entity(txn) for txn in txns]