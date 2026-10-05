from contacts import find_contact, get_list_items, edit_list, delete_list_item

def test_find_contact_not_found():
    contacts = [
        {"id": 1, "name": "Ali"}
    ]

    result = find_contact(999, contacts)

    assert result is None

def test_find_contact():
    contacts = [
        {"id": 1, "name": "Ali"}
    ]

    result = find_contact(1, contacts)

    assert result["name"] == "Ali"

def test_get_list_items(monkeypatch):
    inputs = iter(["", "0912", "n"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_list_items("Phone: ")

    assert result == ["0912"]

def test_edit_list(monkeypatch):
    items = ["0912", "0935"]
    inputs = iter([5])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    edit_list(items, "Enter new phone: ")

    assert items == ["0912", "0935"]

def test_delete_list_item(monkeypatch):
    items = ["0912", "0935", "0991"]
    inputs = iter([6])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    delete_list_item(items)

    assert items == ["0912", "0935", "0991"]