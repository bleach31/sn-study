
`Chapter18 <https://zenn.dev/y_mrok/books/sphinx-no-tsukaikata/viewer/chapter18>`_
=================================================================================================


言語指定なし（自動判定）
----------------------------

.. code-block::

   public class HelloWorld{
      public static void main(String[] args){
        System.out.println("hello, world");
      }
   }


.. code-block::

    message: str = "こんにちは, Python!"
    if len(message) > 0:
        for i in range(3):
            print(f"{i}: {message}")


.. code-block::

    #include <iostream>
    #include <string>

    int square(int x) { return x * x; }

    int main() {
        std::string message = "Hi, C++!";
        if (!message.empty()) {
            for (int i = 0; i < 3; ++i) {
                std::cout << i << ": " << message << '\n';
            }
        }
        std::cout << square(5) << '\n';
        return 0;
    }


言語指定あり
---------------------
こっちのが良く効く。指定すべき。

行表示オプション ``linenos``

.. code-block:: java
   :linenos:

   public class HelloWorld{
      public static void main(String[] args){
        System.out.println("hello, world");
      }
   }

特定の行をハイライトオプション ``emphasize-lines``

.. code-block:: python
   :emphasize-lines: 2, 4

    message: str = "こんにちは, Python!"
    if len(message) > 0:
        for i in range(3):
            print(f"{i}: {message}")


.. code-block:: cpp
   :emphasize-lines:  1-2

    #include <iostream>
    #include <string>

    int square(int x) { return x * x; }

    int main() {
        std::string message = "Hi, C++!";
        if (!message.empty()) {
            for (int i = 0; i < 3; ++i) {
                std::cout << i << ": " << message << '\n';
            }
        }
        std::cout << square(5) << '\n';
        return 0;
    }


シンタックスハイライトなし
---------------------------------

何用？

.. code-block:: none   

   public class HelloWorld{
      public static void main(String[] args){
        System.out.println("hello, world");
      }
   }


コードをファイルから読むこむ
------------------------------------

この場合、言語指定はroleでやる。


.. literalinclude:: ../../lumache.py
    :language: python
    :linenos:

