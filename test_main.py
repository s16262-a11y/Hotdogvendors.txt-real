import unittest
from Main import linear_search, total_hotdogs_by_vendor


class TestHotdogFunctions(unittest.TestCase):

    def test_linear_search_found(self):
        records = [
            ["DD_056", "Dolly Dogs", 202313, 40, 140, 10.5, 1],
            ["KK_745", "Korner Kart", 202313, 60, 130, 10.5, 2]
        ]

        result = linear_search(records, "DD_056")

        self.assertEqual(result, records[0])

    def test_linear_search_not_found(self):
        records = [
            ["DD_056", "Dolly Dogs", 202313, 40, 140, 10.5, 1]
        ]

        result = linear_search(records, "XX_999")

        self.assertIsNone(result)

    def test_total_hotdogs_by_vendor(self):
        records = [
            ["DD_056", "Dolly Dogs", 202313, 40, 140, 10.5, 1],
            ["DD_056", "Dolly Dogs", 202314, 40, 170, 15.0, 2]
        ]

        result = total_hotdogs_by_vendor(records, "DD_056")

        self.assertEqual(result, 390)


if __name__ == "__main__":
    unittest.main()