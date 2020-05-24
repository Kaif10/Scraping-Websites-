{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pure\n",
      "adjective,\n",
      "free from anything of a different, inferior, or contaminating kind; free from extraneous matter: pure gold; pure water.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Creating an algorithm that scrapes part of speech and algorithm of words that we input in the program using Beautiful Soup.\n",
    "Note: Using Python 2 may result in unicode errors so use Python 3 or above\n",
    "'''\n",
    "# Import required modules\n",
    "import sys\n",
    "import requests\n",
    "from bs4 import BeautifulSoup as bs\n",
    "\n",
    "#we are going to scrape dictionary.com website to find the meaning of the words that is givenas input in the algorithm\n",
    "url = \"https://www.dictionary.com/browse/\"\n",
    "\n",
    "# read the word as input\n",
    "word = input()\n",
    "#append the word to url like https://www.dictionary.com/browse/apple\n",
    "url += word\n",
    "\n",
    "\n",
    "# load the website's source code\n",
    "\n",
    "r = requests.get(url)\n",
    "# Here i am using the lxml parser. U can use the parser of uour choice\n",
    "soup = bs(r.content, 'lxml')\n",
    "\n",
    "\n",
    "\n",
    "# parse the source to obtain all necessary info\n",
    "\n",
    "\n",
    "# the header which provides the part of speech of the word\n",
    "header = soup.findAll(\"span\", {\"class\": \"luna-pos\"})\n",
    "print(header[0].text)\n",
    "\n",
    "# the answer_list which provides the meaning\n",
    "answer_list = soup.findAll(\"span\", {\"class\": \"one-click-content css-1p89gle e1q3nk1v4\"} )\n",
    "print(answer_list[0].text)\n",
    "\n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
