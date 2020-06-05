{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "> <ipython-input-2-ce724d748aa5>(6)<module>()\n",
      "-> x += y\n",
      "(Pdb) x\n",
      "0\n",
      "(Pdb) y\n",
      "0\n",
      "(Pdb) c\n",
      "> <ipython-input-2-ce724d748aa5>(5)<module>()\n",
      "-> pdb.set_trace()\n",
      "(Pdb) x\n",
      "0\n",
      "(Pdb) y\n",
      "1\n",
      "(Pdb) c\n",
      "> <ipython-input-2-ce724d748aa5>(6)<module>()\n",
      "-> x += y\n",
      "(Pdb) x\n",
      "1\n",
      "(Pdb) y\n",
      "2\n",
      "(Pdb) c\n",
      "> <ipython-input-2-ce724d748aa5>(5)<module>()\n",
      "-> pdb.set_trace()\n",
      "(Pdb) x\n",
      "3\n",
      "(Pdb) y\n",
      "3\n",
      "(Pdb) n\n",
      "> <ipython-input-2-ce724d748aa5>(6)<module>()\n",
      "-> x += y\n",
      "(Pdb) n\n",
      "> <ipython-input-2-ce724d748aa5>(4)<module>()\n",
      "-> for y in range(10):\n",
      "(Pdb) n\n",
      "> <ipython-input-2-ce724d748aa5>(5)<module>()\n",
      "-> pdb.set_trace()\n",
      "(Pdb) n\n",
      "> <ipython-input-2-ce724d748aa5>(6)<module>()\n",
      "-> x += y\n",
      "(Pdb) c\n",
      "> <ipython-input-2-ce724d748aa5>(5)<module>()\n",
      "-> pdb.set_trace()\n",
      "(Pdb) n\n",
      "> <ipython-input-2-ce724d748aa5>(6)<module>()\n",
      "-> x += y\n",
      "(Pdb) n\n",
      "> <ipython-input-2-ce724d748aa5>(4)<module>()\n",
      "-> for y in range(10):\n",
      "(Pdb) y\n",
      "5\n",
      "(Pdb) x\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "import pdb\n",
    "\n",
    "x = 0\n",
    "for y in range(10):\n",
    "    pdb.set_trace()\n",
    "    x += y\n",
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
