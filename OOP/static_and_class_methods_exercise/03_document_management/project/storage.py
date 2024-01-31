from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object(object_id, list_objects):
        return next((o for o in list_objects if o.id == object_id), None)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self.__find_object(category_id, self.categories)
        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self.__find_object(document_id, self.documents)
        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        category = self.__find_object(category_id, self.categories)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id) -> None:
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id) -> None:
        document = self.__find_object(document_id, self.documents)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id) -> "Document":
        return self.__find_object(document_id, self.documents)

    # def edit_category(self, category_id: int, new_name: str) -> None:
    #     category = next((c for c in self.categories if c.id == category_id))
    #     category.name = new_name
    #
    # def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
    #     topic = next((t for t in self.topics if t.id == topic_id))
    #     topic.topic = new_topic
    #     topic.storage_folder = new_storage_folder
    #
    # def edit_document(self, document_id: int, new_file_name: str) -> None:
    #     document = next((d for d in self.documents if d.id == document_id))
    #     document.file_name = new_file_name

    # def delete_category(self, category_id) -> None:
    #     category = next((c for c in self.categories if c.id == category_id))
    #     self.categories.remove(category)
    #
    # def delete_topic(self, topic_id) -> None:
    #     topic = next((t for t in self.topics if t.id == topic_id))
    #     self.topics.remove(topic)
    #
    # def delete_document(self, document_id) -> None:
    #     document = next((d for d in self.documents if d.id == document_id))
    #     self.documents.remove(document)
    #
    # def get_document(self, document_id) -> "Document":
    #     document = next((d for d in self.documents if d.id == document_id))
    #     return document

    def __repr__(self) -> str:
        return "\n".join([str(d) for d in self.documents])
