from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.data):
            raise StopIteration
        items_per_page = 3  # Adjust this number based on how many items you want per page
        page_items = list(self.data.values())[self._iter_index:self._iter_index + items_per_page]
        self._iter_index += items_per_page
        return "\n".join(str(item) for item in page_items)
