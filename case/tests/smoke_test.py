import pytest


@pytest.fixture()
def smoke():
    return True


def test_smoke(smoke):
    assert smoke
