{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1d70b778-1ed9-406a-969d-d3d9d896b318",
   "metadata": {},
   "outputs": [],
   "source": [
    "# bradcasting   --> operations on arrays of different shapes\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6ed82684-df93-4e50-aee8-24800703637a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 3]\n",
      " [4 5 6 7]]\n",
      "[ 8  9 10 11]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.arange(8).reshape(2,4)\n",
    "arr2 = np.arange(8,12)\n",
    "print(arr1)\n",
    "print(arr2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "eba87f9a-c523-417a-9e1d-e1ab28aa3d00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 8, 10, 12, 14],\n",
       "       [12, 14, 16, 18]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1+arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66a65cb2-48b3-4af3-a8d6-17bfdd1fedc0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
