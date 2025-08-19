要件定義側（リンクデモ）
========================
 
.. need:: 足し算が正しい
   :id: REQ_001
   :tags: addition

.. need:: 足し算が失敗する
   :id: REQ_002
   :tags: addition_fail

.. need:: スキップされるテスト
   :id: REQ_003
   :tags: skipped



テストケースのID指定読み込み(suite, caseは必須）
＋独自ID指定

.. test-case:: Test Case
   :id: TESTCASE_002
   :file: _static/pytest_results.xml
   :suite: pytest
   :case: test_TC002