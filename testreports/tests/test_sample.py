import pytest
# 関数名をIDとして、SNから:caseを使って参照可能
# pytestのテスト関数は、test_で始まる必要があり

def test_TC001():
    assert 1 + 1 == 2

def test_TC002(): 
    assert 1 + 2 == 3

def test_TC003():
    assert 1 + 1 == 3  # わざと失敗

def test_TC004():
    assert 1 + 2 == 4  # わざと失敗

@pytest.mark.skip(reason="デモ用にスキップ")
def test_TC005():
    assert True