{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4684fa4c",
   "metadata": {},
   "source": [
    "# Exercise 7\n",
    "# operator to perform arithmetic addition on two numbers\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "734e9a73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "TwoLists\n",
      "TwoTwoTwo\n"
     ]
    }
   ],
   "source": [
    "print (1 + 2)\n",
    "# to merge two lists\n",
    "print (\"Two\" + \"Lists\")\n",
    "# Concatenate two strings\n",
    "print (\"Two\"*3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a61e436",
   "metadata": {},
   "source": [
    "# Exercise 8\n",
    "# Write a NumPy program to test whether none of the elements of a given array is zero."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aff97682",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 3, 1, 0, 5, 7])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([2,3,1,0,5,7])\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3f00430b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2  is not zero\n",
      "3  is not zero\n",
      "1  is not zero\n",
      "Zero value found at Index 3\n",
      "5  is not zero\n",
      "7  is not zero\n"
     ]
    }
   ],
   "source": [
    "for index,item in enumerate(a):\n",
    "    if item==0:\n",
    "        print('Zero value found at Index',index)\n",
    "    else:\n",
    "        print(item,\" is not zero\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "277cab57",
   "metadata": {},
   "source": [
    "# Write a NumPy program to test whether any of the elements of a given array is non-zero."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5542b27c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array\n",
      "[10 33 56 36  0  3  8  9  0  6]\n",
      "Test whether any of the elements of a given array is non-zero\n",
      "True\n",
      "Original array:\n",
      "[10 33 56 36  0  3  8  9  0  6]\n",
      "Test whether any of the elements of a give array is non-zero\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([10,33,56,36,0,3,8,9,0,6])\n",
    "print(\"Original array\")\n",
    "print(a)\n",
    "print(\"Test whether any of the elements of a given array is non-zero\")\n",
    "print(np.any(a))\n",
    "a = np.array([10,33,56,36,0,3,8,9,0,6])\n",
    "print(\"Original array:\")\n",
    "print(a)\n",
    "print(\"Test whether any of the elements of a give array is non-zero\")\n",
    "print(np.any(a))\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed52159a",
   "metadata": {},
   "source": [
    "# Exercise 9"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66e63f1e",
   "metadata": {},
   "source": [
    "# 1.Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e4f13754",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array\n",
      "[23.  0.  1. nan inf]\n",
      "Test a given array element-wise for finiteness :\n",
      "[ True  True  True False False]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([15, 0, 1, np.nan, np.inf])\n",
    "print(\"Original array\")\n",
    "print(a)\n",
    "print(\"Test a given array element-wise for finiteness :\")\n",
    "print(np.isfinite(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d035dd6a",
   "metadata": {},
   "source": [
    "# 2.Write a NumPy program to test element-wise for positive or negative infinity.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93dc20b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a = np.array([15, 0, 1, np.nan, np.inf])\n",
    "print(\"Original array\")\n",
    "print(a)\n",
    "print(\"Test element-wise for positive or negative infinity :\")\n",
    "print(np.isinf(np.inf))\n",
    "print(np.isinf(np.nan))\n",
    "print(np.isinf(np.NINF))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "abf34f2e",
   "metadata": {},
   "source": [
    "# Exercise 10"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1d20e46",
   "metadata": {},
   "source": [
    "# Write a NumPy program to test element-wise for NaN of a given array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ac2dacfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array\n",
      "[ 1.  0. nan inf]\n",
      "Test element-wisefor NaN :\n",
      "[False False  True False]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([1, 0, np.nan, np.inf])\n",
    "print(\"Original array\")\n",
    "print(a)\n",
    "print(\"Test element-wisefor NaN :\")\n",
    "print(np.isnan(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "660f2dbb",
   "metadata": {},
   "source": [
    "# Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f9271bd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array\n",
      "[1.+1.b 1.+0.b 8.+0.b 0.+0.b 0.+5.b]\n",
      "Checking for complex number :\n",
      "[ True False False False  True]\n",
      "Checking for real number : \n",
      "[False  True  True  True False]\n",
      "Checking for scalar type :\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([1+1b, 1+0b, 8, 0, 5b])\n",
    "print(\"Original array\")\n",
    "print(a)\n",
    "print(\"Checking for complex number :\")\n",
    "print(np.iscomplex(a))\n",
    "print(\"Checking for real number : \")\n",
    "print(np.isreal(a))\n",
    "print(\"Checking for scalar type :\")\n",
    "print(np.isscalar(3.1))\n",
    "print(np.isscalar([3.1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d49e96a9",
   "metadata": {},
   "source": [
    "# Exercise 11"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce6025c0",
   "metadata": {},
   "source": [
    "# 1.Write a NumPy program to test whether two arrays are element-wise equal within a tolerance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7e91853d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original numbers :\n",
      "[  87   98 -100   23  -15   56   80]\n",
      "[  80   56  -15   23 -100   98   87]\n",
      "Comparison - equal :\n",
      "[False False False  True False False False]\n",
      "Comparison - equal within a tolerance :\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.array([87, 98, -100, 23, -15, 56, 80])\n",
    "y = np.array ([80, 56, -15, 23, -100, 98, 87])\n",
    "print(\"Original numbers :\")\n",
    "print(x)\n",
    "print(y)\n",
    "print(\"Comparison - equal :\")\n",
    "print(np.equal(x,y))\n",
    "print(\"Comparison - equal within a tolerance :\")\n",
    "print(np.allclose(x, y))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be2dd9f2",
   "metadata": {},
   "source": [
    "# 2.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "445cd964",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original numbers :\n",
      "[10 20]\n",
      "[15 25]\n",
      "Comparison - greater\n",
      "[False False]\n",
      "Comparison - greater_equal\n",
      "[False False]\n",
      "Comparison - less\n",
      "[ True  True]\n",
      "Comparison - less_equal\n",
      "[ True  True]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.array ([10, 20])\n",
    "y = np.array([15, 25])\n",
    "print(\"Original numbers :\")\n",
    "print(x)\n",
    "print(y)\n",
    "print (\"Comparison - greater\")\n",
    "print(np.greater(x, y))\n",
    "print(\"Comparison - greater_equal\")\n",
    "print(np.greater_equal(x, y))\n",
    "print(\"Comparison - less\")\n",
    "print(np.less(x, y))\n",
    "print(\"Comparison - less_equal\")\n",
    "print(np.less_equal(x, y))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74a275e9",
   "metadata": {},
   "source": [
    "# Exercise 12"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d771d6c0",
   "metadata": {},
   "source": [
    "# 1.Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c8763fe0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original numbers :\n",
      "[  13   24   98    0   77   65 1000]\n",
      "[  10    2   78    0   23 1050    6]\n",
      "Comparison - equal :\n",
      "[False False False  True False False False]\n",
      "Comparison - equal within a tolerance\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.array([13, 24, 98, 0, 77, 65, 1000])\n",
    "y = np.array([10, 2, 78, 0, 23, 1050, 6])\n",
    "print(\"Original numbers :\")\n",
    "print(x)\n",
    "print(y)\n",
    "print(\"Comparison - equal :\")\n",
    "print(np.equal(x, y))\n",
    "print(\"Comparison - equal within a tolerance\")\n",
    "print(np.allclose(x, y))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5ba6323",
   "metadata": {},
   "source": [
    "# 2.Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8a923b43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array :\n",
      "[  1   7  13 105]\n",
      "Size of the memory occupied by the array\n",
      "16 bytes\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.array([1,7,13,105])\n",
    "print(\"Original array :\")\n",
    "print(x)\n",
    "print(\"Size of the memory occupied by the array\")\n",
    "print(\"%d bytes\" % (x.size * x.itemsize))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81371ac7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}