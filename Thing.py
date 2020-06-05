{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pdb\n",
    "\n",
    "x = 0\n",
    "\n",
    "def lots_of_math(x):\n",
    "    y = x**4\n",
    "    y = y - 17\n",
    "    y = y / 3\n",
    "    y = y ** .5\n",
    "    return y\n",
    "\n",
    "for y in range(5):\n",
    "    pdb.set_trace()\n",
    "    x += lots_of_math(y)\n",
    "    \n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "learn-env",
   "language": "python",
   "name": "learn-env"
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
