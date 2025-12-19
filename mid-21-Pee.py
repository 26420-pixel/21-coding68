{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP7c2GkRwSB2Yik8BPwYc5r",
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
        "<a href=\"https://colab.research.google.com/github/26420-pixel/21-coding68/blob/main/mid-21-Pee.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fv0OLcy6pxW-",
        "outputId": "3ee0bb71-4e6c-4e91-858d-1982b2de5c54"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " อณุหภมิของเหล็ก(องศา)1600\n",
            "สถานะของเหลว\n"
          ]
        }
      ],
      "source": [
        "Irontemperature =int(input(\" อณุหภมิของเหล็ก(องศา)\"))\n",
        "if Irontemperature >1538:\n",
        "   print(\"สถานะของเหลว\")\n",
        "else:\n",
        "    print(\"สถานะของแข็ง\")"
      ]
    }
  ]
}