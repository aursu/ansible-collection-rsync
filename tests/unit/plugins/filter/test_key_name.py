import unittest
from ansible.errors import AnsibleFilterError
from ansible_collections.aursu.rsync.plugins.filter.generate_key_name import generate_key_name

class TestKeyNameGeneration(unittest.TestCase):
    def test_invalid_key_type(self):
        """Test that invalid key type raises AnsibleFilterError"""
        with self.assertRaises(AnsibleFilterError) as context:
            generate_key_name("example.com", key_type="invalid")
        self.assertIn("Invalid key type", str(context.exception))

    def test_empty_target_host(self):
        """Test that empty target host raises AnsibleFilterError"""
        with self.assertRaises(AnsibleFilterError):
            generate_key_name("")
        with self.assertRaises(AnsibleFilterError):
            generate_key_name("   ")

    def test_special_characters_in_host(self):
        """Test that special characters in host name are properly sanitized"""
        result = generate_key_name("test.example!@#$%.com")
        self.assertTrue(result.startswith("id_ed25519_test_example_com_"))
        self.assertEqual(len(result.split("_")[-1]), 7)  # Check hash length

    def test_unique_hashes(self):
        """Test that multiple calls produce unique hashes"""
        results = set()
        for _ in range(5):
            key_name = generate_key_name("example.com")
            parts = key_name.split("_")
            self.assertGreaterEqual(len(parts), 4)
            hash_part = parts[-1]
            self.assertEqual(len(hash_part), 7)
            self.assertNotIn(hash_part, results)
            results.add(hash_part)


if __name__ == '__main__':
    unittest.main()
