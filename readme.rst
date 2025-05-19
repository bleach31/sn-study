
ここのイメージをつかってdevcontainerを作る（作った）

https://sphinx-needs.readthedocs.io/en/latest/docker.html

sphinxのチュートリアルをする
https://www.sphinx-doc.org/en/master/tutorial/getting-started.html


ビルド
sphinx-build -M html docs/source/ docs/build/

生成されたHTMLを確認するには
cd docs/build/html
python3 -m http.server 8000
