import requests
import pytest

BASE_URL = "http://127.0.0.1:8000"


def test_consulta_cnpj():
    cnpj_valido = "27865757000102"
    response = requests.get(f"{BASE_URL}/consulta_cnpj/{cnpj_valido}")
    assert response.status_code == 200

    expected_cnpj_raiz = "27865757"
    expected_razao_social = "GLOBO COMUNICACAO E PARTICIPACOES S/A"

    actual_data = response.json()

    assert actual_data["cnpj_raiz"] == expected_cnpj_raiz
    assert actual_data["razao_social"] == expected_razao_social
