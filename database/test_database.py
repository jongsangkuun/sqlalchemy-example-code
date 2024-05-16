from database import Database
from test_schema import (
    SearchManyTable,
    SearchOneTable,
    InsertManyTable,
    InsertOneTable,
    UpdateOneTable,
    UpdateManyTable,
    DeleteManyTable,
    DeleteOneTable,
)
import unittest


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(config_type="test_database")

    def test_search_one(self):
        user = self.db.search_one(SearchOneTable, email="test1@example.com")

        self.assertIsNotNone(user)
        self.assertEqual(user.email, "test1@example.com")

    def test_search_many(self):
        input_data = [
            {"id": 2, "name": "test2", "email": "test2@example.com"},
            {"id": 3, "name": "test3", "email": "test3@example.com"},
            {"id": 4, "name": "test4", "email": "test4@example.com"},
            {"id": 5, "name": "test5", "email": "test5@example.com"},
        ]
        search_data = self.db.search_many(SearchManyTable)
        self.assertEqual(input_data, search_data)

    def test_insert_one(self):
        data = {"id": 16, "name": "test16", "email": "test16@example.com"}
        self.db.insert_one(data=data, table=InsertOneTable)

        self.assertIsNotNone(
            self.db.search_one(InsertOneTable, email="test16@example.com")
        )
        self.assertEqual(
            self.db.search_one(InsertOneTable, email="test16@example.com").email,
            "test16@example.com",
        )

    def test_insert_many(self):
        input_data = [
            {"id": 17, "name": "test17", "email": "test17@example.com"},
            {"id": 18, "name": "test18", "email": "test18@example.com"},
            {"id": 19, "name": "test19", "email": "test19@example.com"},
            {"id": 20, "name": "test20", "email": "test20@example.com"},
        ]

        self.db.insert_many(data=input_data, table=InsertManyTable)
        search_data = self.db.search_many(InsertManyTable)
        self.assertEqual(input_data, search_data)

    def test_update_one(self):
        # Update
        update_data = {"name": "updated_test6", "email": "updated_test6@example.com"}
        self.db.update_records(
            UpdateOneTable, update_data, filter_by={"email": "test6@example.com"}
        )

        # Verify
        updated_user = self.db.search_one(
            UpdateOneTable, email="updated_test6@example.com"
        )
        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user.email, "updated_test6@example.com")

    def test_update_many(self):
        # Update
        update_data = {"name": "updated_test2", "email": "updated_test2@example.com"}
        filter_by_list = [
            {"email": "test7@example.com"},
            {"email": "test8@example.com"},
            {"email": "test9@example.com"},
            {"email": "test10@example.com"},
        ]
        for filter_by in filter_by_list:
            self.db.update_records(UpdateManyTable, update_data, [filter_by])

        # Verify
        updated_users = self.db.search_many(UpdateManyTable)
        self.assertEqual(len(updated_users), len(filter_by_list))
        for user in updated_users:
            self.assertEqual(user["name"], "updated_test2")
            self.assertEqual(user["email"], "updated_test2@example.com")

    def test_delete_one(self):
        # Delete
        self.db.delete_records(
            table=DeleteOneTable, filter_by={"email": "test11@example.com"}
        )

        # Verify
        deleted_user = self.db.search_one(DeleteOneTable, email="test11@example.com")
        self.assertIsNone(deleted_user)

    def test_delete_many(self):
        # Delete
        delete_data = [
            {"email": "test12@example.com"},
            {"email": "test13@example.com"},
            {"email": "test14@example.com"},
            {"email": "test15@example.com"},
        ]
        self.db.delete_records(DeleteManyTable, filter_by=delete_data)

        # Verify
        deleted_users = self.db.search_many(DeleteManyTable)
        self.assertEqual(len(deleted_users), 0)


if __name__ == "__main__":
    unittest.main()
