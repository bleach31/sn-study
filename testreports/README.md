必要ライブラリ

pip install sphinx pytest sphinx-needs sphinx-test-reports 

pytestの実行

pytest -q --junitxml docs/source/_static/pytest_results.xml


htmlの生成
cd docs
make html

htmlの確認
cd docs/build/html
python3 -m http.server 8000