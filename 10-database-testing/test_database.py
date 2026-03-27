import unittest
import database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        database.init_database()
        database.delete_all_users()

    def tearDown(self):
        database.delete_all_users()

    def test_create_user(self):
        user_id = database.create_user("Alice", "alice@example.com", 30)
        self.assertIsNotNone(user_id)
        user = database.get_user_by_id(user_id)
        self.assertEqual(user["name"], "Alice")
        self.assertEqual(user["email"], "alice@example.com")
        self.assertEqual(user["age"], 30)

    def test_create_duplicate_user(self):
        database.create_user("Alice", "alice@example.com", 30)
        with self.assertRaises(ValueError):
            database.create_user("Bob", "alice@example.com", 25)

    def test_get_user_by_id(self):
        user_id = database.create_user("Alice", "alice@example.com", 30)
        user = database.get_user_by_id(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Alice")
        # nonexistent id
        self.assertIsNone(database.get_user_by_id(9999))

    def test_get_user_by_email(self):
        database.create_user("Alice", "alice@example.com", 30)
        user = database.get_user_by_email("alice@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Alice")
        # nonexistent email
        self.assertIsNone(database.get_user_by_email("nobody@example.com"))

    def test_get_all_users(self):
        database.create_user("Alice", "alice@example.com", 30)
        database.create_user("Bob", "bob@example.com", 25)
        users = database.get_all_users()
        self.assertEqual(len(users), 2)

    def test_update_user(self):
        user_id = database.create_user("Alice", "alice@example.com", 30)
        result = database.update_user(user_id, name="Alicia", age=31)
        self.assertTrue(result)
        user = database.get_user_by_id(user_id)
        self.assertEqual(user["name"], "Alicia")
        self.assertEqual(user["age"], 31)
        self.assertEqual(user["email"], "alice@example.com")

    def test_update_nonexistent(self):
        result = database.update_user(9999, name="Ghost")
        self.assertFalse(result)

    def test_delete_user(self):
        user_id = database.create_user("Alice", "alice@example.com", 30)
        result = database.delete_user(user_id)
        self.assertTrue(result)
        self.assertIsNone(database.get_user_by_id(user_id))

    def test_delete_nonexistent(self):
        result = database.delete_user(9999)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
