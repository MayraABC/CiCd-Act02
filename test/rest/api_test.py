import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def get_status(self, url):
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            return response.status
        except HTTPError as e:
            return e.code

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_add_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/add/a/3", f"{BASE_URL}/calc/add/3/b",
            f"{BASE_URL}/calc/add/None/6", f"{BASE_URL}/calc/add/b/None",
            f"{BASE_URL}/calc/add/object()/r", f"{BASE_URL}/calc/add/23/object()",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_substract(self):
        for url in [
            f"{BASE_URL}/calc/substract/10/-6", f"{BASE_URL}/calc/substract/-2/1",
            f"{BASE_URL}/calc/substract/1/0",
        ]:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_substract_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/substract/a/3", f"{BASE_URL}/calc/substract/3/b",
            f"{BASE_URL}/calc/substract/None/6", f"{BASE_URL}/calc/substract/b/None",
            f"{BASE_URL}/calc/substract/object()/r", f"{BASE_URL}/calc/substract/23/object()",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_multiply(self):
        for url in [
            f"{BASE_URL}/calc/multiply/2/2", f"{BASE_URL}/calc/multiply/1/0",
            f"{BASE_URL}/calc/multiply/-1/0", f"{BASE_URL}/calc/multiply/-1/2",
            f"{BASE_URL}/calc/multiply/0/0", f"{BASE_URL}/calc/multiply/0/2",
        ]:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_multiply_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/multiply/a/3", f"{BASE_URL}/calc/multiply/3/b",
            f"{BASE_URL}/calc/multiply/None/6", f"{BASE_URL}/calc/multiply/b/None",
            f"{BASE_URL}/calc/multiply/object()/r", f"{BASE_URL}/calc/multiply/23/object()",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_divide_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/divide/90/0", f"{BASE_URL}/calc/divide/2/P",
            f"{BASE_URL}/calc/divide/A/32", f"{BASE_URL}/calc/divide/None/56",
            f"{BASE_URL}/calc/divide/2/None", f"{BASE_URL}/calc/divide/None/2",
            f"{BASE_URL}/calc/divide/None/None", f"{BASE_URL}/calc/divide/object()/r",
            f"{BASE_URL}/calc/divide/23/object()", f"{BASE_URL}/calc/divide/2/object()",
            f"{BASE_URL}/calc/divide/object()/2",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_power(self):
        for url in [
            f"{BASE_URL}/calc/power/2/3", f"{BASE_URL}/calc/power/3/2",
            f"{BASE_URL}/calc/power/2/0", f"{BASE_URL}/calc/power/0/2",
            f"{BASE_URL}/calc/power/0/0", f"{BASE_URL}/calc/power/2/-3",
        ]:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_power_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/power/2/P", f"{BASE_URL}/calc/power/A/32",
            f"{BASE_URL}/calc/power/None/56", f"{BASE_URL}/calc/power/2/None",
            f"{BASE_URL}/calc/power/None/2", f"{BASE_URL}/calc/power/None/None",
            f"{BASE_URL}/calc/power/object()/r", f"{BASE_URL}/calc/power/23/object()",
            f"{BASE_URL}/calc/power/2/object()", f"{BASE_URL}/calc/power/object()/2",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_sqrt(self):
        for url in [f"{BASE_URL}/calc/sqrt/4", f"{BASE_URL}/calc/sqrt/0"]:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_sqrt_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/sqrt/-1", f"{BASE_URL}/calc/sqrt/P",
            f"{BASE_URL}/calc/sqrt/None", f"{BASE_URL}/calc/sqrt/object()",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_log10(self):
        for url in [f"{BASE_URL}/calc/log10/10", f"{BASE_URL}/calc/log10/1"]:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    def test_api_log10_falla_con_datos_errados(self):
        for url in [
            f"{BASE_URL}/calc/log10/0", f"{BASE_URL}/calc/log10/-1",
            f"{BASE_URL}/calc/log10/P", f"{BASE_URL}/calc/log10/None",
            f"{BASE_URL}/calc/log10/object()",
        ]:
            self.assertEqual(self.get_status(url), http.client.BAD_REQUEST, f"Error en la petición API a {url}")
