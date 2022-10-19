{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNk8em0jJAu+sNobd0OjsIw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/anoganteryannico/CPEN65-1/blob/main/Area_of_the_Cirlce_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PZCWQdY-Btmn",
        "outputId": "d8cbd526-501e-4982-b31a-25f86e4e2c8f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Determine the value. Input (D) for diameter, (R) for radius: Radius\n",
            "Input the value of radius or diameter here: 10\n",
            "The area of the circle given its radius is  314.1592653589793\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "\n",
        "unknown = str(input(\"Determine the value. Input (D) for diameter, (R) for radius: \"))\n",
        "value = float(input(\"Input the value of radius or diameter here: \"))\n",
        "\n",
        "\n",
        "class Circle:\n",
        "  def Area(self):\n",
        "    if unknown == \"Radius\":\n",
        "      rad = value**2*(math.pi)\n",
        "      print(\"The area of the circle given its radius is \", rad)\n",
        "    elif unknown == \"Diameter\":\n",
        "      diam = value**2*(math.pi)*0.25\n",
        "      print(\"The area of the circle given its diameter is \", diam)\n",
        "    else:\n",
        "      print(\"Syntax Error\")\n",
        "\n",
        "Circle.Area(0)\n"
      ]
    }
  ]
}