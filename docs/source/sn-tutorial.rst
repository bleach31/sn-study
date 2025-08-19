sphinx-needs tutorial
=================================================

このサイトに従ってチュートリアルを実施する。

https://sphinx-needs.readthedocs.io/en/latest/tutorial.html

ああああ

.. req:: Basic need example
    :id: 0A001Z

    A basic example of a need item.


いいいい

.. tutorial-project:: Our new car
    :id: T_CAR
    :tags: tutorial
    :layout: clean_l
    :collapse: true

    Presenting the “TeenTrek,” an autonomous driving car tailored for teenagers without a driving license.
    Equipped with advanced AI navigation and safety protocols, it ensures effortless and secure transportation.
    The interior boasts entertainment systems, study areas, and social hubs, catering to teen preferences.
    The TeenTrek fosters independence while prioritizing safety and convenience for young passengers.

うううう


The project is described in more detail in :need:`0A001Z`.

The project is described in more detail in :need:`[[title]] <0A001Z>`.


.. req:: test me
   :id: A0001
   :impacts: T_CAR
   :

   

   A requirement, which needs to be tested

.. test:: test a requirement
   :id: A0002
   :tests: test_req

   Perform some tests
ええええ