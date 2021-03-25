{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "TUGAS DATAMINING PRAKTIKUM.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6gWFVrmRszE9"
      },
      "source": [
        "          Modul 1 praktikum datamining\n",
        "        Manipulasi array menggunakan numpy\n",
        "\n",
        " \n",
        " \n",
        " kode 1 F\n",
        "\n",
        "f.\tBuatlah array 2D berikut menggunakan numpy\n",
        "\n",
        "![lk.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANIAAABiCAIAAACqMRpgAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAhdEVYdENyZWF0aW9uIFRpbWUAMjAyMTowMzoxMSAwNTo1MjowNG9Nz2EAAAT+SURBVHhe7d1BVuJAEAZgnWP4WBGOoVv1AC68ApyBC8QD4NYdXkG35nkKceU9mH+omrykMTEvBKrK/N+C6QbfvB9SdNLSLefb7faM6LT+6L9EJ8SyIwMsOzLAsiMDLDsywLIjAyw7MsCyIwMsOzJQ+5Ti/PxcW0S9dPzQKy270J+VMb+t7vl5kiUDLDsywLIjAyw7MsCyIwPByg5zJdBOQEHzLxYLSS6en5/1gb4ilR2e/M3NjXYCCp1/Pp9v/7u/v9d7+wpTdkVRvL6+LpdL7UcTPf+wwpTd1dXV09OTdgKKnv/x8VHOsLe3t3rXAWKUHU5PGOQvLy+1H030/KvVSs+v2+3Lywuejj7Qm/5nO0nXibe3tzJYtb2P+U8gz/Msy7RT1z1/gNHu/f0dtzLC41Ql7cMnUycTPf++2Wymrd60/HaSrkPRR4uI+TebDSbgZRsh1+u1dBPd80f6BQqZmE6nuJXRGqdX1Nzhv0DhwidHxpOfox0ZYNmRAZYdGWDZkYF0SqEtol46TinSshvJTMonzmSJjohlRwZYdmSAZUcGWHZkIEDZfX5+YoqUwJ36cBBFUWj0gRbompD82jkEZrylpOtTnuflOpyE2/yy3mmz2Wi/gfPXfz6fyxYk7e/pnr/2c86ftkDIw9d7nRiOVlPmKs+vP945WZYNtV6w9nOen7ZoWVENbvMjGGLjVuDg6QN1eEhb/kjskZYdErYMG27zV2PjndOU021+nF4BjTGWHY5ce0K3+REMB0zasi782+s8n/mrpTZU2UX6BcpyuZShIhycYb++vrQTzVG2IGn57SRdV34c6sBtfpyhyktStMPNxEujO8nisMnlRQvn+REPyvrb5zm/GKrsuPDJkfHk54djZIBlRwZYdmQgvbbTFlEvHa/t0rIbySWtT5xSEB0Ry44MsOzIAMuODLDsyECMsqtupwi3EeF37AUREl47B4hRdlmW5XmOyTl8fHw8PDzoAxFMp1NJLmQviPyJzFiG/DoXfTF2kq4TyaqH9XrdtIjDZ/4EQjYtkPacH0cBL/uIlnleXFzgtlxXOJlMZIFuRBincfAO/9u/pzfw17lo+e0kXT9kjWeVPlDXdL8fSNg01IHb/P92Uox2L4WIe5KVN492vuMzf7XURnSSTWCov76+1k4oQfeCjHovhZDD1rS93nP+H4c68P/6DzXaxViBgmDa2tVc028f3OaH2WyGQXq1Wmn/O57zi6IoMOA1heyeP0bZdcT8trrn54djZIBlRwZYdmSAZUcG0imFtoh66TilSMtuJDMpnziTJToilh0ZYNmRAZYdGWDZkYEwZRf660Sq4ReLhd4bxFG2IGHGW0q6fsh6m6b1TiW3+bMsk/DyRHAr9yfc5q+SLUjaqeueP0bZ/YKvEymhBJueS4j8CHl4/hhlh2A4WrgVcUeL9sWe/vNjqGvaUQDd89d+zu3TRrDyHSYLjKWdcJu/utWt5VIBj2rLKyRsOe10zx9mSjGZTKRxd3eH21i76qs7tDFahJtVCNk/Mchuyxhlh0MV9+tEEhitg/4liiG3IOl7cCfp+jGP/HUiOKtWr4fQlj2n+9y+/tB+VSq656/9nOenjaOFeFA9hAm3+VFnEh6aag7wqLb8aXm3lLrn58InR8aTnx+OkQGWHRlg2ZGB9NpOW0S9dLy2i30NS0HxJEsGWHZkgGVHBlh2dHJnZ38BdO3JaCMznHMAAAAASUVORK5CYII=)\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pn2mbKces4Tb",
        "outputId": "a604c813-33fb-4533-d5b6-cf725e994b8e"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([[4,4,5],[7,6,4],\n",
        "                [9,7,4],[6,3,7]])\n",
        "print(arr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[4 4 5]\n",
            " [7 6 4]\n",
            " [9 7 4]\n",
            " [6 3 7]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "37IofS8ntz34"
      },
      "source": [
        "Jawaban kode 1 G\n",
        "\n",
        "g.\tBuatlah array 3D berikut menggunakan numpy\n",
        "\n",
        "![lkhg.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "faiUEAqmt3JQ",
        "outputId": "4a06fb31-8961-4157-9ef8-538ab2360cdb"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([[[7,8,5],[4,7,7],[7,1,9],[5,4,10]],\n",
        "                [[2,1,2],[9,8,5],[3,7,3],[4,9,9]],\n",
        "                [[2,9,3],[2,4,8],[1,6,6],[8,1,3]]])\n",
        "print(arr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[ 7  8  5]\n",
            "  [ 4  7  7]\n",
            "  [ 7  1  9]\n",
            "  [ 5  4 10]]\n",
            "\n",
            " [[ 2  1  2]\n",
            "  [ 9  8  5]\n",
            "  [ 3  7  3]\n",
            "  [ 4  9  9]]\n",
            "\n",
            " [[ 2  9  3]\n",
            "  [ 2  4  8]\n",
            "  [ 1  6  6]\n",
            "  [ 8  1  3]]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_1txSAAB1nTi"
      },
      "source": [
        "Jawaban Kode 2 D\n",
        "\n",
        "d.\tTambahkan angka 1 pada setiap bilangan di baris ganjil array berikut. kemudian tambahkan angka 2 pada setiap bilangan di kolom genap array berikut.\n",
        "\n",
        "\n",
        "![d.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J4dodJkSWjYB",
        "outputId": "4207e87f-bf6b-4a48-de5a-3f8970217d1c"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([[1,8,8,2],\n",
        "                [8,2,1,2],\n",
        "                [10,1,4,7],\n",
        "                [1,4,7,8],\n",
        "                [8,2,3,4]])\n",
        "print(arr)\n",
        "for i in range(len(arr)):\n",
        "  for j in range(len(arr[0])):\n",
        "    if i % 2 == 1:\n",
        "      arr[i][j] +=1\n",
        "    if j % 2 == 0:\n",
        "      arr[i][j] +=2\n",
        "\n",
        "print(\"\\n\" + \"______HASIL______\" + \"\\n\")\n",
        "print(arr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[ 1  8  8  2]\n",
            " [ 8  2  1  2]\n",
            " [10  1  4  7]\n",
            " [ 1  4  7  8]\n",
            " [ 8  2  3  4]]\n",
            "\n",
            "______HASIL______\n",
            "\n",
            "[[ 3  8 10  2]\n",
            " [11  3  4  3]\n",
            " [12  1  6  7]\n",
            " [ 4  5 10  9]\n",
            " [10  2  5  4]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "54xgjjnH1wPB"
      },
      "source": [
        "Jawaban kode 2 E\n",
        "\n",
        "e.\tBaliklah sumbu z array 3D berikut\n",
        "\n",
        "![lkhg.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LKkvvK3aojJ2",
        "outputId": "1feedcf8-8f9b-46c6-b211-d4862b0df0c9"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([[[7,8,5],[4,7,7],[7,1,9],[5,4,10]],\n",
        "                [[2,1,2],[9,8,5],[3,7,3],[4,9,9]],\n",
        "                [[2,9,3],[2,4,8],[1,6,6],[8,1,3]]])\n",
        "print(arr)\n",
        "reversed_arr = arr[::-1]\n",
        "print(\"\\n\" + \"______HASIL______\" + \"\\n\")\n",
        "print(reversed_arr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[ 7  8  5]\n",
            "  [ 4  7  7]\n",
            "  [ 7  1  9]\n",
            "  [ 5  4 10]]\n",
            "\n",
            " [[ 2  1  2]\n",
            "  [ 9  8  5]\n",
            "  [ 3  7  3]\n",
            "  [ 4  9  9]]\n",
            "\n",
            " [[ 2  9  3]\n",
            "  [ 2  4  8]\n",
            "  [ 1  6  6]\n",
            "  [ 8  1  3]]]\n",
            "\n",
            "______HASIL______\n",
            "\n",
            "[[[ 2  9  3]\n",
            "  [ 2  4  8]\n",
            "  [ 1  6  6]\n",
            "  [ 8  1  3]]\n",
            "\n",
            " [[ 2  1  2]\n",
            "  [ 9  8  5]\n",
            "  [ 3  7  3]\n",
            "  [ 4  9  9]]\n",
            "\n",
            " [[ 7  8  5]\n",
            "  [ 4  7  7]\n",
            "  [ 7  1  9]\n",
            "  [ 5  4 10]]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_sBhpizU19J4"
      },
      "source": [
        " Kode 2 F\n",
        "\n",
        "f.\tUbahlah array pada soal e menjadi array 2D berukuran 6 x 6 (hint : gunakan perintah reshape)\n",
        "\n",
        "![lkhg.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tjxqsw2WGTyA",
        "outputId": "71e9b76c-517a-4a43-8706-a07407ef8322"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([[[7,8,5],[4,7,7],[7,1,9],[5,4,10]],\n",
        "                [[2,1,2],[9,8,5],[3,7,3],[4,9,9]],\n",
        "                [[2,9,3],[2,4,8],[1,6,6],[8,1,3]]])\n",
        "print(arr)\n",
        "newarr = arr.reshape(6, 6)\n",
        "print(\"\\n\" + \"______HASIL______\" + \"\\n\")\n",
        "print(newarr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[ 7  8  5]\n",
            "  [ 4  7  7]\n",
            "  [ 7  1  9]\n",
            "  [ 5  4 10]]\n",
            "\n",
            " [[ 2  1  2]\n",
            "  [ 9  8  5]\n",
            "  [ 3  7  3]\n",
            "  [ 4  9  9]]\n",
            "\n",
            " [[ 2  9  3]\n",
            "  [ 2  4  8]\n",
            "  [ 1  6  6]\n",
            "  [ 8  1  3]]]\n",
            "\n",
            "______HASIL______\n",
            "\n",
            "[[ 7  8  5  4  7  7]\n",
            " [ 7  1  9  5  4 10]\n",
            " [ 2  1  2  9  8  5]\n",
            " [ 3  7  3  4  9  9]\n",
            " [ 2  9  3  2  4  8]\n",
            " [ 1  6  6  8  1  3]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nPDRn2OBrqh6"
      },
      "source": [
        "kode 3\n",
        "\n",
        "e.\tUbahlah matris kiri menjadi matriks sebelah kanan\n",
        "\n",
        "![sdsasas.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nG8e7g7h42HQ",
        "outputId": "0b47f286-5947-457f-a100-36badeb19734"
      },
      "source": [
        "\n",
        "import numpy as np\n",
        "arr = np.array([\n",
        "    [[5, 10, 10, 7], \n",
        "    [7, 8, 4, 10], \n",
        "    [9, 10, 2, 5], \n",
        "    [1, 8, 9, 3], \n",
        "    [6, 10, 5, 2], \n",
        "    [4, 6, 9, 4]]\n",
        "    ])\n",
        "\n",
        "print(arr)\n",
        "print(\"_\"*30)\n",
        "variabel = arr[:, :, :2].copy()\n",
        "print(variabel)\n",
        "arr[:, :, :2] = arr[:, :, 2:]\n",
        "print('\\n',arr[:, :, 2:] )\n",
        "arr[:, :, 2:] = variabel\n",
        "print(\"_\"*30)\n",
        "\n",
        "\n",
        "variabel2 = arr[:, :3, :].copy()\n",
        "print(variabel2)\n",
        "arr[:, :3, :] = arr[:, 3:, :]\n",
        "print('\\n',arr[:, 3:, :])\n",
        "arr[:, 3:, :] = variabel2\n",
        "print(\"_\"*30)\n",
        "print(arr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[ 5 10 10  7]\n",
            "  [ 7  8  4 10]\n",
            "  [ 9 10  2  5]\n",
            "  [ 1  8  9  3]\n",
            "  [ 6 10  5  2]\n",
            "  [ 4  6  9  4]]]\n",
            "______________________________\n",
            "[[[ 5 10]\n",
            "  [ 7  8]\n",
            "  [ 9 10]\n",
            "  [ 1  8]\n",
            "  [ 6 10]\n",
            "  [ 4  6]]]\n",
            "\n",
            " [[[10  7]\n",
            "  [ 4 10]\n",
            "  [ 2  5]\n",
            "  [ 9  3]\n",
            "  [ 5  2]\n",
            "  [ 9  4]]]\n",
            "______________________________\n",
            "[[[10  7  5 10]\n",
            "  [ 4 10  7  8]\n",
            "  [ 2  5  9 10]]]\n",
            "\n",
            " [[[ 9  3  1  8]\n",
            "  [ 5  2  6 10]\n",
            "  [ 9  4  4  6]]]\n",
            "______________________________\n",
            "[[[ 9  3  1  8]\n",
            "  [ 5  2  6 10]\n",
            "  [ 9  4  4  6]\n",
            "  [10  7  5 10]\n",
            "  [ 4 10  7  8]\n",
            "  [ 2  5  9 10]]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xIyD9uQFOHKp",
        "outputId": "80ecd56f-e050-41c3-d7c2-f67ea61ec5f6"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([\n",
        "    [[5, 10, 10, 7], \n",
        "    [7, 8, 4, 10], \n",
        "    [9, 10, 2, 5], \n",
        "    [1, 8, 9, 3], \n",
        "    [6, 10, 5, 2], \n",
        "    [4, 6, 9, 4]]\n",
        "    ])\n",
        "\n",
        "print(arr)\n",
        "variabel = arr[:, :, :2].copy()\n",
        "arr[:, :, :2] = arr[:, :, 2:]\n",
        "arr[:, :, 2:] = variabel\n",
        "print(\"-----\")\n",
        "\n",
        "\n",
        "variabel2 = arr[:, :3, :].copy()\n",
        "arr[:, :3, :] = arr[:, 3:, :]\n",
        "arr[:, 3:, :] = variabel2\n",
        "\n",
        "print(arr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[ 5 10 10  7]\n",
            "  [ 7  8  4 10]\n",
            "  [ 9 10  2  5]\n",
            "  [ 1  8  9  3]\n",
            "  [ 6 10  5  2]\n",
            "  [ 4  6  9  4]]]\n",
            "______________________________\n",
            "[[[ 5 10]\n",
            "  [ 7  8]\n",
            "  [ 9 10]\n",
            "  [ 1  8]\n",
            "  [ 6 10]\n",
            "  [ 4  6]]]\n",
            "\n",
            " [[[10  7]\n",
            "  [ 4 10]\n",
            "  [ 2  5]\n",
            "  [ 9  3]\n",
            "  [ 5  2]\n",
            "  [ 9  4]]]\n",
            "______________________________\n",
            "[[[10  7  5 10]\n",
            "  [ 4 10  7  8]\n",
            "  [ 2  5  9 10]]]\n",
            "\n",
            " [[[ 9  3  1  8]\n",
            "  [ 5  2  6 10]\n",
            "  [ 9  4  4  6]]]\n",
            "______________________________\n",
            "[[[ 9  3  1  8]\n",
            "  [ 5  2  6 10]\n",
            "  [ 9  4  4  6]\n",
            "  [10  7  5 10]\n",
            "  [ 4 10  7  8]\n",
            "  [ 2  5  9 10]]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RwGJmlkFSi3E",
        "outputId": "3a80214f-ade8-4788-e60b-959885c8053e"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([\n",
        "    [[5, 10, 10, 7], \n",
        "    [7, 8, 4, 10], \n",
        "    [9, 10, 2, 5], \n",
        "    [1, 8, 9, 3], \n",
        "    [6, 10, 5, 2], \n",
        "    [4, 6, 9, 4]]\n",
        "    ])\n",
        "\n",
        "print(arr)\n",
        "print(\"\\n----------------\\n\")\n",
        "\n",
        "variabel = arr[:, :, :2].copy() #start, end, step \n",
        "print(variabel)\n",
        "arr[:, :, :2] = arr[:, :, 2:]#start mengiris array : sebanyak 2*baris step koma secara horizontal dan berarti memotong secara vertikal\n",
        "print('\\n',arr[:, :, 2:] )#setelah di slice hasilnya di .copy() : untuk menyalin hasil slicing tanpa mengubah nilai asli ><.view \n",
        "arr[:, :, 2:] = variabel# 2:diambil lagi dr nilai setelahnya slicing pertama (diambil 2 lagi atau setengahnya)\n",
        "print(\"\\n----------------\\n\")\n",
        "\n",
        "\n",
        "variabel2 = arr[:, :3, :].copy()#start, end, step \n",
        "print(variabel2)\n",
        "arr[:, :3, :] = arr[:, 3:, :]#batas slice dimana berakhir pada index ke 3*kolom jadi masing2 3 kolom secara vertikal dan memotong secara horizontal\n",
        "print('\\n',arr[:, 3:, :]) #setelah di slice hasilnya di .copy() : untuk menyalin hasil slicing tanpa mengubah nilai asli ><.view \n",
        "arr[:, 3:, :] = variabel2#3:  diambil lagi dr nilai setelahnya slicing pertama (diambil 3 lagi atau setengahnya)\n",
        "print(\"\\n----------------\\n\")\n",
        "print(arr) #setelah itu penggambungan hasil akhirnya"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[[ 5 10 10  7]\n",
            "  [ 7  8  4 10]\n",
            "  [ 9 10  2  5]\n",
            "  [ 1  8  9  3]\n",
            "  [ 6 10  5  2]\n",
            "  [ 4  6  9  4]]]\n",
            "\n",
            "----------------\n",
            "\n",
            "[[[ 5 10]\n",
            "  [ 7  8]\n",
            "  [ 9 10]\n",
            "  [ 1  8]\n",
            "  [ 6 10]\n",
            "  [ 4  6]]]\n",
            "\n",
            " [[[10  7]\n",
            "  [ 4 10]\n",
            "  [ 2  5]\n",
            "  [ 9  3]\n",
            "  [ 5  2]\n",
            "  [ 9  4]]]\n",
            "\n",
            "----------------\n",
            "\n",
            "[[[10  7  5 10]\n",
            "  [ 4 10  7  8]\n",
            "  [ 2  5  9 10]]]\n",
            "\n",
            " [[[ 9  3  1  8]\n",
            "  [ 5  2  6 10]\n",
            "  [ 9  4  4  6]]]\n",
            "\n",
            "----------------\n",
            "\n",
            "[[[ 9  3  1  8]\n",
            "  [ 5  2  6 10]\n",
            "  [ 9  4  4  6]\n",
            "  [10  7  5 10]\n",
            "  [ 4 10  7  8]\n",
            "  [ 2  5  9 10]]]\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}