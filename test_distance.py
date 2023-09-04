from distance import *
from tud_test_base import *
import pytest

def test_payprogram():
    set_keyboard_input(["Sibu","Kuching",450])
    main()
    output = get_display_output()

    assert output == [
        "Calculate Trip Duration\n",
        "\tEnter the starting location: ",
        "\tEnter the ending location: ",
        "\tEnter the distance between the locations: ",
        "\nDetails",
        "\tStart:\t\tSibu",
        "\tEnd:\t\tKuching",
        "\tDistance:\t450.0 km",
        "\tDuration:\t9.0 hours",
    ]