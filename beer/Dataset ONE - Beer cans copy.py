{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Homework 7, Part One: Lots and lots of questions about beer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Do your importing and your setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "#justincase"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Read in the file `craftcans.csv`, and look at the first first rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"craftcans.csv\", na_values=\"Does not apply\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How many rows do you have in the data? What are the column types?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2416 entries, 0 to 2415\n",
      "Data columns (total 7 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Beer      2416 non-null   object \n",
      " 1   Brewery   2410 non-null   object \n",
      " 2   Location  2410 non-null   object \n",
      " 3   Style     2405 non-null   object \n",
      " 4   Size      2410 non-null   object \n",
      " 5   ABV       2348 non-null   object \n",
      " 6   IBUs      1405 non-null   float64\n",
      "dtypes: float64(1), object(6)\n",
      "memory usage: 132.2+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.50%</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Maggie's Leap</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Milk / Sweet Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.90%</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.80%</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Pumpion</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.00%</td>\n",
       "      <td>38.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Stronghold</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American Porter</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.00%</td>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2411</th>\n",
       "      <td>Mama's Little Yella Pils</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Czech Pilsener</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.30%</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2412</th>\n",
       "      <td>GUBNA Imperial IPA</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.90%</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2413</th>\n",
       "      <td>Old Chub</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Scottish Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.00%</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2414</th>\n",
       "      <td>Gordon Ale (2009)</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.70%</td>\n",
       "      <td>85.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2415</th>\n",
       "      <td>Dale's Pale Ale</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.50%</td>\n",
       "      <td>65.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2416 rows ?? 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                          Beer              Brewery         Location  \\\n",
       "0                 Get Together    NorthGate Brewing  Minneapolis, MN   \n",
       "1                Maggie's Leap    NorthGate Brewing  Minneapolis, MN   \n",
       "2                   Wall's End    NorthGate Brewing  Minneapolis, MN   \n",
       "3                      Pumpion    NorthGate Brewing  Minneapolis, MN   \n",
       "4                   Stronghold    NorthGate Brewing  Minneapolis, MN   \n",
       "...                        ...                  ...              ...   \n",
       "2411  Mama's Little Yella Pils  Oskar Blues Brewery     Longmont, CO   \n",
       "2412        GUBNA Imperial IPA  Oskar Blues Brewery     Longmont, CO   \n",
       "2413                  Old Chub  Oskar Blues Brewery     Longmont, CO   \n",
       "2414         Gordon Ale (2009)  Oskar Blues Brewery     Longmont, CO   \n",
       "2415           Dale's Pale Ale  Oskar Blues Brewery     Longmont, CO   \n",
       "\n",
       "                               Style    Size    ABV   IBUs  \n",
       "0                       American IPA  16 oz.  4.50%   50.0  \n",
       "1                 Milk / Sweet Stout  16 oz.  4.90%   26.0  \n",
       "2                  English Brown Ale  16 oz.  4.80%   19.0  \n",
       "3                        Pumpkin Ale  16 oz.  6.00%   38.0  \n",
       "4                    American Porter  16 oz.  6.00%   25.0  \n",
       "...                              ...     ...    ...    ...  \n",
       "2411                  Czech Pilsener  12 oz.  5.30%   35.0  \n",
       "2412  American Double / Imperial IPA  12 oz.  9.90%  100.0  \n",
       "2413                    Scottish Ale  12 oz.  8.00%   35.0  \n",
       "2414  American Double / Imperial IPA  12 oz.  8.70%   85.0  \n",
       "2415         American Pale Ale (APA)  12 oz.  6.50%   65.0  \n",
       "\n",
       "[2416 rows x 7 columns]"
      ]
     },
     "execution_count": 258,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Checking out our alcohol"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top 10 producers of cans of beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Brewery Vivant                62\n",
       "Oskar Blues Brewery           46\n",
       "Sun King Brewing Company      38\n",
       "Cigar City Brewing Company    25\n",
       "Sixpoint Craft Ales           24\n",
       "Hopworks Urban Brewery        23\n",
       "Stevens Point Brewery         22\n",
       "Great Crescent Brewery        20\n",
       "21st Amendment Brewery        20\n",
       "Bonfire Brewing Company       19\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Brewery.value_counts().head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is the most common ABV? (alcohol by volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.00%    215\n",
       "Name: ABV, dtype: int64"
      ]
     },
     "execution_count": 260,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.value_counts().head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Oh, weird, ABV isn't a number. Convert it to a number for me, please.\n",
    "\n",
    "It's going to take a few steps!\n",
    "\n",
    "### First, let's just look at the ABV column by itself"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       4.50%\n",
       "1       4.90%\n",
       "2       4.80%\n",
       "3       6.00%\n",
       "4       6.00%\n",
       "        ...  \n",
       "2411    5.30%\n",
       "2412    9.90%\n",
       "2413    8.00%\n",
       "2414    8.70%\n",
       "2415    6.50%\n",
       "Name: ABV, Length: 2416, dtype: object"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hm, `%` isn't part of  a number. Let's remove it.\n",
    "\n",
    "When you're confident you got it right, save the results back into the `ABV` column.\n",
    "\n",
    "- *Tip: In programming the easiest way to remove something is to *replacing it with nothing*.\n",
    "- *Tip: \"nothing\" might seem like `NaN` sinc we talked about it a lot in class, but in this case it isn't! It's just an empty string, like \"\"*\n",
    "- *Tip: `.replace` is usually used for replacing ENTIRE cells, while `.str.replace` is useful for replacing PARTS of cells*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.ABV = df.ABV.str.replace('%', \"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Now let's turn `ABV` into a numeric data type\n",
    "\n",
    "Save the results back into the `ABV` column (again), and then check `df.dtypes` to make sure it worked.\n",
    "\n",
    "- *Tip: We used `.astype(int)` during class, but this has a decimal in it...*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.ABV = df.ABV.astype(float)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What's the ABV of the average beer look like?\n",
    "\n",
    "### Show me in two different ways: one command to show the `median`/`mean`/etc, and secondly show me a chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.6"
      ]
     },
     "execution_count": 264,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.mean()\n",
    "df.ABV.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.ABV.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We don't have ABV for all of the beers, how many are we missing them from?\n",
    "\n",
    "- *Tip: You can use `isna()` or `notna()` to see where a column is missing/not missing data.*\n",
    "- *Tip: You just want to count how many `True`s and `False`s there are.*\n",
    "- *Tip: It's a weird trick involving something we usually use to count things in a column*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False    2348\n",
       "True       68\n",
       "Name: ABV, dtype: int64"
      ]
     },
     "execution_count": 266,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.isna().value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Looking at location\n",
    "\n",
    "Brooklyn used to produce 80% of the country's beer! Let's see if it's still true."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top 10 cities in the US for canned craft beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Grand Rapids, MI    66\n",
       "Chicago, IL         55\n",
       "Portland, OR        52\n",
       "Indianapolis, IN    43\n",
       "San Diego, CA       42\n",
       "Boulder, CO         41\n",
       "Denver, CO          40\n",
       "Brooklyn, NY        38\n",
       "Seattle, WA         35\n",
       "Longmont, CO        33\n",
       "Name: Location, dtype: int64"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Location.value_counts().head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the beer from Brooklyn, NY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>115</th>\n",
       "      <td>4Beans</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Baltic Porter</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>10.0</td>\n",
       "      <td>52.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>210</th>\n",
       "      <td>Jammer</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Gose</td>\n",
       "      <td>12 oz. Slimline</td>\n",
       "      <td>4.2</td>\n",
       "      <td>16.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>246</th>\n",
       "      <td>Abigale</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Belgian Pale Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>404</th>\n",
       "      <td>Nomader Weiss</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Berliner Weissbier</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>421</th>\n",
       "      <td>Rad</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Fruit / Vegetable Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>3.2</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>439</th>\n",
       "      <td>Molotov Lite</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.5</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>588</th>\n",
       "      <td>Bengali</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>24 oz. \"Silo Can\"</td>\n",
       "      <td>6.5</td>\n",
       "      <td>62.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>713</th>\n",
       "      <td>Sensi Harvest</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.7</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>969</th>\n",
       "      <td>Hi-Res</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>111.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>987</th>\n",
       "      <td>KelSo Nut Brown Lager</td>\n",
       "      <td>KelSo Beer Company</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Euro Dark Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.7</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1057</th>\n",
       "      <td>Global Warmer</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Strong Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>7.0</td>\n",
       "      <td>70.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1074</th>\n",
       "      <td>Autumnation (2013)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.7</td>\n",
       "      <td>74.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1093</th>\n",
       "      <td>KelSo India Pale Ale</td>\n",
       "      <td>KelSo Beer Company</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>64.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1267</th>\n",
       "      <td>The Crisp</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>German Pilsener</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.4</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1268</th>\n",
       "      <td>Sweet Action</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Cream Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>34.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1269</th>\n",
       "      <td>Righteous Ale</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Rye Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.3</td>\n",
       "      <td>57.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1270</th>\n",
       "      <td>Bengali Tiger</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.4</td>\n",
       "      <td>62.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1305</th>\n",
       "      <td>KelSo Pilsner</td>\n",
       "      <td>KelSo Beer Company</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Czech Pilsener</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>23.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1365</th>\n",
       "      <td>Hipster Ale (Two Roads Brewing)</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1366</th>\n",
       "      <td>Bikini Beer</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>2.7</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1373</th>\n",
       "      <td>East India Pale Ale</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English India Pale Ale (IPA)</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.8</td>\n",
       "      <td>47.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1624</th>\n",
       "      <td>3Beans</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Baltic Porter</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>85.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1836</th>\n",
       "      <td>Brownstone</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.9</td>\n",
       "      <td>47.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1857</th>\n",
       "      <td>Brooklyn Summer Ale</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English Pale Mild Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1962</th>\n",
       "      <td>Hipster Ale (Westbrook Brewing)</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1970</th>\n",
       "      <td>Apollo</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Wheat Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1971</th>\n",
       "      <td>Harbinger</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Saison / Farmhouse Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1972</th>\n",
       "      <td>Resin</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.1</td>\n",
       "      <td>103.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2027</th>\n",
       "      <td>East India Pale Ale</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English India Pale Ale (IPA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.8</td>\n",
       "      <td>47.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2062</th>\n",
       "      <td>Diesel</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.3</td>\n",
       "      <td>69.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2074</th>\n",
       "      <td>Autumnation (2011-12) (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>48.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2140</th>\n",
       "      <td>The Crisp (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>German Pilsener</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.4</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2141</th>\n",
       "      <td>Sweet Action (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Cream Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>34.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>Righteous Ale (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Rye Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.3</td>\n",
       "      <td>57.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>Bengali Tiger (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.4</td>\n",
       "      <td>62.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2219</th>\n",
       "      <td>Brooklyn Summer Ale (2011)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English Pale Mild Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2350</th>\n",
       "      <td>Brooklyn Lager (16 oz.)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Amber / Red Lager</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2351</th>\n",
       "      <td>Brooklyn Lager (12 oz.)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Amber / Red Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 Beer              Brewery      Location  \\\n",
       "115                            4Beans  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "210                            Jammer  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "246                           Abigale  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "404                     Nomader Weiss    Evil Twin Brewing  Brooklyn, NY   \n",
       "421                               Rad  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "439                      Molotov Lite    Evil Twin Brewing  Brooklyn, NY   \n",
       "588                           Bengali  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "713                     Sensi Harvest  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "969                            Hi-Res  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "987             KelSo Nut Brown Lager   KelSo Beer Company  Brooklyn, NY   \n",
       "1057                    Global Warmer  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1074               Autumnation (2013)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1093             KelSo India Pale Ale   KelSo Beer Company  Brooklyn, NY   \n",
       "1267                        The Crisp  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1268                     Sweet Action  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1269                    Righteous Ale  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1270                    Bengali Tiger  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1305                    KelSo Pilsner   KelSo Beer Company  Brooklyn, NY   \n",
       "1365  Hipster Ale (Two Roads Brewing)    Evil Twin Brewing  Brooklyn, NY   \n",
       "1366                      Bikini Beer    Evil Twin Brewing  Brooklyn, NY   \n",
       "1373              East India Pale Ale     Brooklyn Brewery  Brooklyn, NY   \n",
       "1624                           3Beans  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1836                       Brownstone  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1857              Brooklyn Summer Ale     Brooklyn Brewery  Brooklyn, NY   \n",
       "1962  Hipster Ale (Westbrook Brewing)    Evil Twin Brewing  Brooklyn, NY   \n",
       "1970                           Apollo  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1971                        Harbinger  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1972                            Resin  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2027              East India Pale Ale     Brooklyn Brewery  Brooklyn, NY   \n",
       "2062                           Diesel  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2074     Autumnation (2011-12) (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2140                 The Crisp (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2141              Sweet Action (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2142             Righteous Ale (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2143             Bengali Tiger (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2219       Brooklyn Summer Ale (2011)     Brooklyn Brewery  Brooklyn, NY   \n",
       "2350          Brooklyn Lager (16 oz.)     Brooklyn Brewery  Brooklyn, NY   \n",
       "2351          Brooklyn Lager (12 oz.)     Brooklyn Brewery  Brooklyn, NY   \n",
       "\n",
       "                               Style               Size   ABV   IBUs  \n",
       "115                    Baltic Porter             12 oz.  10.0   52.0  \n",
       "210                             Gose    12 oz. Slimline   4.2   16.0  \n",
       "246                 Belgian Pale Ale             12 oz.   8.0    NaN  \n",
       "404               Berliner Weissbier             12 oz.   4.0    NaN  \n",
       "421           Fruit / Vegetable Beer             16 oz.   3.2    7.0  \n",
       "439   American Double / Imperial IPA             16 oz.   8.5    NaN  \n",
       "588                     American IPA  24 oz. \"Silo Can\"   6.5   62.0  \n",
       "713          American Pale Ale (APA)             12 oz.   4.7   50.0  \n",
       "969   American Double / Imperial IPA             12 oz.   9.9  111.0  \n",
       "987                  Euro Dark Lager             12 oz.   5.7   19.0  \n",
       "1057             American Strong Ale             12 oz.   7.0   70.0  \n",
       "1074                    American IPA             16 oz.   6.7   74.0  \n",
       "1093                    American IPA             12 oz.   6.0   64.0  \n",
       "1267                 German Pilsener             16 oz.   5.4   42.0  \n",
       "1268                       Cream Ale             16 oz.   5.2   34.0  \n",
       "1269                        Rye Beer             16 oz.   6.3   57.0  \n",
       "1270                    American IPA             16 oz.   6.4   62.0  \n",
       "1305                  Czech Pilsener             12 oz.   5.5   23.0  \n",
       "1365         American Pale Ale (APA)             12 oz.   5.5    NaN  \n",
       "1366                    American IPA             12 oz.   2.7    NaN  \n",
       "1373    English India Pale Ale (IPA)             16 oz.   6.8   47.0  \n",
       "1624                   Baltic Porter             12 oz.   9.9   85.0  \n",
       "1836              American Brown Ale             16 oz.   5.9   47.0  \n",
       "1857           English Pale Mild Ale             12 oz.   4.5    NaN  \n",
       "1962         American Pale Ale (APA)             12 oz.   5.5    NaN  \n",
       "1970         American Pale Wheat Ale             16 oz.   5.2   11.0  \n",
       "1971          Saison / Farmhouse Ale             16 oz.   4.9   35.0  \n",
       "1972  American Double / Imperial IPA             12 oz.   9.1  103.0  \n",
       "2027    English India Pale Ale (IPA)             12 oz.   6.8   47.0  \n",
       "2062                  American Stout             16 oz.   6.3   69.0  \n",
       "2074                     Pumpkin Ale             16 oz.   6.0   48.0  \n",
       "2140                 German Pilsener             16 oz.   5.4   42.0  \n",
       "2141                       Cream Ale             16 oz.   5.2   34.0  \n",
       "2142                        Rye Beer             16 oz.   6.3   57.0  \n",
       "2143                    American IPA             16 oz.   6.4   62.0  \n",
       "2219           English Pale Mild Ale             12 oz.   4.5    NaN  \n",
       "2350      American Amber / Red Lager             16 oz.   5.2    NaN  \n",
       "2351      American Amber / Red Lager             12 oz.   5.2    NaN  "
      ]
     },
     "execution_count": 268,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query('Location == \"Brooklyn, NY\"') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What brewery in Brooklyn puts out the most types of canned beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sixpoint Craft Ales    24\n",
       "Brooklyn Brewery        6\n",
       "Evil Twin Brewing       5\n",
       "KelSo Beer Company      3\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 269,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query('Location == \"Brooklyn, NY\"').Brewery.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the five styles of beer that Sixpoint produces the most cans of?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      4\n",
       "Baltic Porter                     2\n",
       "American Double / Imperial IPA    2\n",
       "German Pilsener                   2\n",
       "Cream Ale                         2\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 270,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query('Location == \"Brooklyn, NY\" & Brewery == \"Sixpoint Craft Ales\"').Style.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the breweries in New York state.\n",
    "\n",
    "- *Tip: We want to match **part** of the `Location` column, but not all of it.*\n",
    "- *Tip: Watch out for `NaN` values! You might be close, but you'll need to pass an extra parameter to make it work without an error.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sixpoint Craft Ales              24\n",
       "Matt Brewing Company             13\n",
       "Brooklyn Brewery                  6\n",
       "Evil Twin Brewing                 5\n",
       "Blue Point Brewing Company        4\n",
       "Butternuts Beer and Ale           4\n",
       "The Bronx Brewery                 3\n",
       "KelSo Beer Company                3\n",
       "Chatham Brewing                   2\n",
       "Montauk Brewing Company           2\n",
       "Bomb Beer Company                 2\n",
       "Upstate Brewing Company           2\n",
       "Newburgh Brewing Company          1\n",
       "Southampton Publick House         1\n",
       "The Manhattan Brewing Company     1\n",
       "Dundee Brewing Company            1\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 271,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ny_df = df[df.Location.str.contains(\" *.NY\", na=False)]\n",
    "ny_df.Brewery.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Now *count* all of the breweries in New York state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 272,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ny_df.Brewery.nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Measuring International Bitterness Units\n",
    "\n",
    "## Display all of the IPAs\n",
    "\n",
    "Include American IPAs, Imperial IPAs, and anything else with \"IPA in it.\"\n",
    "\n",
    "IPA stands for [India Pale Ale](https://www.bonappetit.com/story/ipa-beer-styles), and is probably the most popular kind of beer in the US for people who are drinking [craft beer](https://www.craftbeer.com/beer/what-is-craft-beer)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      424\n",
       "American Double / Imperial IPA    105\n",
       "Belgian IPA                        18\n",
       "English India Pale Ale (IPA)       13\n",
       "American White IPA                 11\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 275,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipa_df = df[df.Style.str.contains(\" *.IPA\", na=False)]\n",
    "ipa_df.Style.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "IPAs are usually pretty hoppy and bitter (although I guess hazy IPAs and session IPAs are changing that since I first made this homework!). IBU stands for [International Bitterness Unit](http://www.thebrewenthusiast.com/ibus/), and while a lot of places like to brag about having the most bitter beer (it's an American thing!), IBUs don't necessary *mean anything*.\n",
    "\n",
    "Let's look at how different beers have different IBU measurements."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Try to get the average IBU measurement across all beers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "42.71316725978647"
      ]
     },
     "execution_count": 276,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Beer         object\n",
       "Brewery      object\n",
       "Location     object\n",
       "Style        object\n",
       "Size         object\n",
       "ABV         float64\n",
       "IBUs        float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 274,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Oh no, it doesn't work!\n",
    "\n",
    "It looks like some of those values *aren't numbers*. There are two ways to fix this:\n",
    "\n",
    "1. Do the `.replace` and `np.nan` thing we did in class. Then convert the column to a number. This is boring.\n",
    "2. When you're reading in your csv, there [is an option called `na_values`](http://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.read_csv.html). You can give it a list of **numbers or strings to count as `NaN`**. It's a lot easier than doing the `np.nan` thing, although you'll need to go add it up top and run all of your cells again.\n",
    "\n",
    "- *Tip: Make sure you're giving `na_values` a LIST, not just a string*\n",
    "\n",
    "### Now try to get the average IBUs again"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "42.71316725978647"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Draw the distribution of IBU measurements, but with *twenty* bins instead of the default of 10\n",
    "\n",
    "- *Tip: Every time I ask for a distribution, I'm looking for a histogram*\n",
    "- *Tip: Use the `?` to get all of the options for building a histogram*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.IBUs.hist(bins = 20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hm, Interesting distribution. List all of the beers with IBUs above the 75th percentile\n",
    "\n",
    "- *Tip: There's a single that gives you the 25/50/75th percentile*\n",
    "- *Tip: You can just manually type the number when you list those beers*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    1405.000000\n",
       "mean       42.713167\n",
       "std        25.954066\n",
       "min         4.000000\n",
       "25%        21.000000\n",
       "50%        35.000000\n",
       "75%        64.000000\n",
       "max       138.000000\n",
       "Name: IBUs, dtype: float64"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Citra Ass Down', 'London Balling', 'Rico Sauvin', 'Pile of Face',\n",
       "       'Excess IPL', 'Hoponius Union', 'Habitus (2014)', 'Solis',\n",
       "       'Habitus', 'Yeti Imperial Stout',\n",
       "       \"98 Problems (Cuz A Hop Ain't One)\", 'Train Hopper', 'Csar',\n",
       "       'Saucy Intruder', 'The Gadget', 'Gone A-Rye', 'Heavy Lifting',\n",
       "       'Jah Mon', 'Flying Mouse 4', 'Soul Doubt', 'Bimini Twist',\n",
       "       'Long Leaf', 'Double Duckpin', 'Hop A-Peel', 'Wobble',\n",
       "       'Hopkick Dropkick', 'Union Jack', 'India Pale Ale', 'Self Starter',\n",
       "       'Nugget Nectar', 'Mission IPA', 'Bay of Bengal Double IPA (2014)',\n",
       "       'Newport Storm IPA', 'Clean Shave IPA', 'Big Star White IPA',\n",
       "       'Firestarter India Pale Ale', 'Back Bay IPA', '4000 Footer IPA',\n",
       "       'Unchained #18 Hop Silo', 'Harness the Winter', 'Rule G IPA',\n",
       "       'Yellow Wolf Imperial IPA', 'Third Eye Enlightened Pale Ale',\n",
       "       'The Green Room', '2014 IPA Cicada Series',\n",
       "       'Sinister Minister Black IPA', 'O???Malley???s IPA',\n",
       "       'Perpetual Darkness', 'Watershed IPA', 'Hoodoo Voodoo IPA',\n",
       "       'Hopportunity Knocks IPA', 'Mothman Black IPA', 'Homefront IPA',\n",
       "       'The Power of Zeus', 'Salamander Slam', 'Torpedo', 'Ranger IPA',\n",
       "       'Dark Voyage Black IPA (2013)', 'Scarecrow', \"Lil' Helper\",\n",
       "       'Hopworks IPA', 'Worthy IPA', 'Abominable Winter Ale',\n",
       "       'Tsunami IPA', 'Mound Builder IPA', 'Dream Crusher Double IPA',\n",
       "       'City of the Sun', '3:33 Black IPA', 'Booming Rollers', 'Aurora',\n",
       "       'More Cowbell', 'Brutus', '1916 Shore Shiver', 'Arcus IPA',\n",
       "       'Epitome', 'Hop Stalker Fresh Hop IPA', '8 Barrel',\n",
       "       'Dead-Eye DIPA', 'Count Hopula (Vault Series)', 'Dankosaurus',\n",
       "       'Might As Well IPL', \"Captain's Daughter\", 'Infamous IPA',\n",
       "       'Tropicalia', 'Vertex IPA', 'Operation Homefront',\n",
       "       'Wandering Pelican', 'Giant DIPA', 'Fistful Of Hops Red',\n",
       "       'Fistful of Hops Orange', 'Fistful Of Hops Blue',\n",
       "       'Fistful of Hops Green', 'Sky-Five', '077XX', 'Almanac IPA',\n",
       "       'Missile IPA', 'Second Fiddle', 'Let It Ride IPA',\n",
       "       'Bent Hop Golden IPA', 'Groupe G', 'Hill 88 Double IPA',\n",
       "       'Hoperation Overload', 'Hop Freak', 'El Chingon IPA',\n",
       "       'Saint Archer IPA', 'BLAKKR', 'Supergoose IPA', 'IPA & a Half',\n",
       "       'Truth', 'American India Red Ale',\n",
       "       'Squatters Hop Rising Double IPA', 'Quarter Mile Double IPA',\n",
       "       'Hoptopus Double IPA', \"Filthy Hoppin' IPA\", '2020 IPA',\n",
       "       'Golden Ratio IPA', 'Hemlock Double IPA', 'Mississippi Fire Ant',\n",
       "       'Red Cockaded Ale', 'Hop Nosh IPA', 'Big Sky IPA',\n",
       "       'Wolf Among Weeds IPA', 'Be Hoppy IPA', 'Hi-Res',\n",
       "       'Irregardless IPA', 'Squatters Hop Rising Double IPA (2014)',\n",
       "       'The Great Return', 'Troopers Alley IPA', 'Madra Allta',\n",
       "       'Chaotic Double IPA', 'Manzanita IPA', 'King Street IPA',\n",
       "       'Sobek & Set', 'Evo IPA', 'Lucky Day IPA',\n",
       "       'Terrace Hill Double IPA', 'Catch 23', 'Better Weather IPA',\n",
       "       \"Hop Drop 'N Roll IPA\", 'Hop Slayer Double IPA', 'Half Cycle IPA',\n",
       "       'Initial Point India Pale Ale', 'Global Warmer', 'Good Vibes IPA',\n",
       "       'Dagger Falls IPA', 'Autumnation (2013)', '12th Round',\n",
       "       'RoughTail IPA', 'Centennial IPA', 'Double Trunk', 'Batch 69 IPA',\n",
       "       'Farmer Wirtz India Pale Ale', 'Proxima IPA', 'Monkey Fist IPA',\n",
       "       \"G'KNIGHT\", 'Ten Fidy', 'Modus Hoperandi', 'Worthy IPA (2013)',\n",
       "       'Perpetual IPA', 'Country Boy IPA', 'Valkyrie Double IPA',\n",
       "       'Blazing World', 'Pilzilla', 'Falling Down Brown Ale',\n",
       "       'Shipwrecked Double IPA', 'Moirai India Pale Ale',\n",
       "       'Overlord Imperial IPA', \"Dale's Pale Ale\", 'F5 IPA',\n",
       "       'Wood Chipper India Pale Ale', 'Grapefruit Jungle (GFJ)',\n",
       "       'Larry Imperial IPA', \"Mind's Eye PA\", 'Big Eye India Pale Ale',\n",
       "       'Heal the Bay IPA', 'Laughing Dog IPA', 'Cascadian Dark Ale',\n",
       "       'Sanitas Black IPA', 'Elephant Rock IPA', 'Crank Yanker IPA',\n",
       "       'Bourbon Barrel Aged Timmie', 'Alphadelic IPA', 'Habitus IPA',\n",
       "       \"Dreamin' Double IPA\", \"Deviant Dale's IPA\", \"Hop Ottin' IPA\",\n",
       "       'Upslope Imperial India Pale Ale', 'Face Plant IPA',\n",
       "       'Bozone HopZone IPA', 'Nice Rack IPA',\n",
       "       'Old Grogham Imperial India Pale Ale', '5 Day IPA',\n",
       "       'Forest Fire Imperial Smoked Rye', 'Bad Axe Imperial IPA',\n",
       "       'Duluchan India Pale Ale', 'Dodgy Knight Imperial IPA',\n",
       "       'Indian Paintbrush IPA', 'Mutiny IPA', 'Redacted Rye IPA',\n",
       "       'Evolutionary IPA (2012)', \"Old Devil's Tooth\",\n",
       "       'Nebraska India Pale Ale', 'Humidor Series India Pale Ale',\n",
       "       'Jai Alai IPA Aged on White Oak', 'Jos?? Mart?? American Porter',\n",
       "       'Psychopathy', 'Overrated! West Coast Style IPA', 'Heady Topper',\n",
       "       'Descender IPA', 'Hop Notch IPA (2013)', 'Hop Shock IPA',\n",
       "       'Disconnected Red', 'Outlaw IPA', 'Lower De Boom', '3Beans',\n",
       "       'Sculpin IPA', 'Ethos IPA', 'Red Cockaded Ale (2013)',\n",
       "       'Elevation Triple India Pale Ale', 'Watershed IPA (2013)',\n",
       "       'Winterfest', 'Bitter Bitch Imperial IPA', 'Rude Parrot IPA',\n",
       "       'Des Moines IPA', 'Black IPA', 'Topcutter India Pale Ale',\n",
       "       'Twister Creek India Pale Ale', 'Deep Ellum IPA',\n",
       "       'Fascist Pig Ale', \"Frankenlou's IPA\",\n",
       "       'Abominable Winter Ale (2012)', 'Oasis',\n",
       "       'Ex Umbris Rye Imperial Stout', 'Odyssey Imperial IPA',\n",
       "       \"Dale's Pale Ale (10 Year Anniversary)\", 'Hop Abomination',\n",
       "       'Cane and Ebel', 'Interurban IPA', 'PRO-AM (2012) (2012)',\n",
       "       'On the Wings of Armageddon', \"Dale's Pale Ale (2012)\",\n",
       "       'Gordon Imperial Red (2010)', 'Gordon (2005)',\n",
       "       'Ten Fidy Imperial Stout (2008)', 'Ten Fidy Imperial Stout (2007)',\n",
       "       '21st Amendment IPA (2006)', 'Brew Free! or Die IPA (2008)',\n",
       "       'Brew Free! or Die IPA (2009)', 'Caldera IPA (2009)',\n",
       "       'Caldera IPA (2007)', 'Ace IPA', 'Double Haul IPA (2009)',\n",
       "       'Double Haul IPA (2006)', \"Dale's Pale Ale (2011)\",\n",
       "       \"Dale's Pale Ale (2010)\", 'Burning Bush Smoked IPA',\n",
       "       'Wolf Among Weeds IPA (2012)',\n",
       "       'Old Grogham Imperial India Pale Ale (2012)',\n",
       "       \"Dale's Pale Ale (2008)\", \"Dale's Pale Ale (2006)\",\n",
       "       \"Dale's Pale Ale (2004)\", \"Dale's Pale Ale (2003)\",\n",
       "       \"Dale's Pale Ale (2002)\", 'Hop Slayer Double IPA (2011)',\n",
       "       'California Sunshine Rye IPA', 'Midnight Ryder',\n",
       "       \"G'KNIGHT (16 oz.)\", 'Over the Rail Pale Ale',\n",
       "       'Hop A Potamus Double Dark Rye Pale Ale', 'Rodeo Clown Double IPA',\n",
       "       'Elevated IPA', 'Hopworks IPA (2012)', 'Isis', 'Hoppy Boy',\n",
       "       'Monkeynaut IPA', 'Ryeteous Rye IPA (2012)', 'Resin',\n",
       "       'Independence Pass Ale', 'HGH (Home Grown Hops): Part Duh',\n",
       "       'Big Sky IPA (2012)', 'Westbrook IPA', 'Tocobaga Red Ale',\n",
       "       'Eclipse Black IPA', 'Jai Alai IPA', 'Old Elephant Foot IPA',\n",
       "       'Big Cock IPA', 'Grapefruit Jungle (GFJ) (2011)', 'Diesel',\n",
       "       'Evolutionary IPA (2011)', 'Alphadelic IPA (2011)',\n",
       "       'Missouri Mule India Pale Ale', 'Hop Box Imperial IPA',\n",
       "       'Hopadillo India Pale Ale', \"Bourbon's Barrel Stout\",\n",
       "       'Great Crescent Stout', \"Flyin' HI.P.Hay\", 'Sockeye Red IPA',\n",
       "       'Hop Crisis', 'Shiva IPA', 'Anti-Hero IPA',\n",
       "       'Crank Yanker IPA (2011)', \"G'KNIGHT (12 oz.)\",\n",
       "       'Black Adder IBA (Current)', 'Upstate I.P.W.',\n",
       "       \"Hop Ottin' IPA (2011)\", 'WET', 'Gandhi-Bot Double IPA ',\n",
       "       'Vortex IPA', 'Hop Shock IPA (2010)', 'Snake Handler Double IPA',\n",
       "       'Lucky U IPA', 'The Corruption', 'Stowaway IPA', 'Back in Black',\n",
       "       'Ranger IPA (Current)', 'Avery India Pale Ale', 'Oasis (2010)',\n",
       "       'Third Eye Pale Ale', 'Double Haul IPA', 'Ballz Deep Double IPA',\n",
       "       'Caldera IPA', 'Big Swell IPA', '113 IPA', 'Abrasive Ale',\n",
       "       'Furious', 'Brew Free! or Die IPA', 'Ten Fidy Imperial Stout',\n",
       "       'GUBNA Imperial IPA', 'Gordon Ale (2009)'], dtype=object)"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IBUs > 64\").Beer.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the beers with IBUs below the 25th percentile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([\"Wall's End\", \"Sho'nuff\", 'Bloody Show', 'The Brown Note',\n",
       "       'House Lager', 'Leisure Time', 'Park', 'Westfalia', 'KSA',\n",
       "       'Sparkle', 'Hotbox Brown', 'Gold', 'Cafe Leche',\n",
       "       'Damascene Apricot Sour', 'Sex Panther', 'Vanilla Porter', 'Gose',\n",
       "       'Vermont Pilsner', 'Ginger Peach Saison', 'Weissenheimer',\n",
       "       'Passion Fruit Prussia', 'Send Help', 'Daft Funk',\n",
       "       'Bat Outta Helles', 'Rye Wit', 'Yo Soy Un Berliner',\n",
       "       \"Farmer's Daughter Blonde\", 'Honey Rye', 'Honey Badger Blonde',\n",
       "       'Old Pro', 'Vanilla Java Porter', 'Saddle Bronc Brown Ale',\n",
       "       'Bomber Mountain Amber Ale', 'Jammer', 'Blackberry Wheat',\n",
       "       'Rhode Island Blueberry', 'Watermelon Ale',\n",
       "       'Bunker Hill Blueberry Ale', 'Deception', 'P-Town Pilsner',\n",
       "       'Nonstop Hef Hop', 'Laka Laka Pineapple', 'Blood Orange Honey',\n",
       "       'Mr. Blue Sky', 'Weisse Versa (2012)', '18th Anniversary Gose',\n",
       "       'Point Special (Current)', 'Point Special',\n",
       "       'Morning Wood Wheat (Current)', 'Hunny Do Wheat', 'Gansett Light',\n",
       "       'Shotgun Betty', 'Knotty Blonde Ale', \"PUNK'N\", 'Sunbru K??lsch',\n",
       "       'River House', 'Summer Brew', 'Suzy B Dirty Blonde Ale', 'Rad',\n",
       "       'Lobo Lito', 'American Lager', 'American Amber', 'American Light',\n",
       "       'Lake House', \"Ermal's\", 'Honey Kolsch', 'Copperhead Amber',\n",
       "       'Twisted X', 'Sol Drifter', '312 Urban Wheat Ale',\n",
       "       'Couch Select Lager', 'Double D Blonde', 'Lost Meridian Wit',\n",
       "       'Joey Wheat', 'Onyx Black Ale', 'Robert Earl Keen Honey Pils',\n",
       "       \"Summer's Wit\", 'Point Special (2013)', 'Point Special (2012)',\n",
       "       'Broken Bridge', 'Point Special Lager', 'What the Butler Saw',\n",
       "       'Laughing Dog Cream Ale', 'Apr?? Shred', 'Blood Orange Wit',\n",
       "       'Hop Up Offa That Brett (2014)', 'Boathouse Blonde', 'Noche Dulce',\n",
       "       'Weize Guy', 'UFO Gingerland', 'Skylight', 'Pub Ale',\n",
       "       \"Here Gose Nothin'\", 'Ale Cider', 'The Great Pumpcan',\n",
       "       'Cherry Ale', 'LuckenBock', 'FMB 101', 'Upland Wheat Ale',\n",
       "       'Monkey Chased the Weasel', 'SunSpot Golden Ale', 'Beach Blonde',\n",
       "       'Alaskan Amber', 'Black Market Hefeweizen',\n",
       "       'Gutch English Style Mild Ale', 'Whitecap Wit',\n",
       "       'Seiche Scottish Ale', 'Local Buzz', 'Saint Archer White Ale',\n",
       "       'Porch Rocker', 'LIFT', '#9', 'The Tradition', 'Hot Date Ale',\n",
       "       'Hijack', 'Stone Fort Brown Ale', 'When Helles Freezes Over',\n",
       "       'Bronx Summer Pale Ale', 'A Slice of Hefen', '805',\n",
       "       'Wick For Brains', 'Schweet Ale', 'KelSo Nut Brown Lager',\n",
       "       'King Street Hefeweizen', 'Chai Ale', 'Banner American Rye',\n",
       "       'Pumpkin Beast', 'Chickawawa Lemonale',\n",
       "       'Sly Fox Christmas Ale 2013', 'Fat Tire Amber Ale',\n",
       "       'Four Peaks Peach Ale', 'Lahaina Town Brown',\n",
       "       'Sweet Yamma Jamma Ale', 'Starr Pils', 'Agave Wheat',\n",
       "       'Barney Flats Oatmeal Stout', 'Shark Bait',\n",
       "       'Golden Road Hefeweizen', 'Summer Paradise',\n",
       "       'Oval Beach Blonde Ale', 'Wolverine Premium Lager',\n",
       "       'Hideout Helles', 'Dead Eye Dunkel',\n",
       "       'Parcae Belgian Style Pale Ale', 'Norns Roggenbier',\n",
       "       'Laimas K??lsch Style Ale', \"Stone's Throw IPA\",\n",
       "       'Weiss Trash Culture', 'K??lsch 151', 'Tybee Island Blonde',\n",
       "       'Horny Monk', 'Two-One Niner', 'Old Forge Pumpkin Ale',\n",
       "       'Sanitas Saison Ale', 'Double D Blonde (2013)', 'Beaver Logger',\n",
       "       'Half Full Bright Ale', 'Point Oktoberfest', 'Schuylkill Punch',\n",
       "       '541 American Lager', 'Summer Solstice', 'UFO Pumpkin',\n",
       "       'Float Trip Ale', 'Greenbelt Farmhouse Ale', 'Hardywood Cream Ale',\n",
       "       'Boont Amber Ale', 'Big Rod Coconut Ale',\n",
       "       'Wild Wolf Wee Heavy Scottish Style Ale',\n",
       "       'Steel Rail Extra Pale Ale', 'Westbrook Gose',\n",
       "       'Estival Cream Stout', 'Dog Days Lager',\n",
       "       'Samuel Adams Octoberfest', 'Longboard Island Lager',\n",
       "       'El Hefe Speaks', 'Dos Pistolas', 'Cotton Mouth', 'Wild Night',\n",
       "       'Love Street Summer Seasonal (2014)',\n",
       "       'Point Nude Beach Summer Wheat', \"SUM'R\",\n",
       "       'Twisted Helles Summer Lager', 'Bomber Mountain Amber Ale (2013)',\n",
       "       'Saddle Bronc Brown Ale (2013)', 'Wagon Box Wheat Beer',\n",
       "       'Wild Plum Farmhouse Ale', 'Peninsula Brewers Reserve (PBR)',\n",
       "       'Hazy Day Belgian-Style Wit', \"Mo's Gose\", 'Lumberyard Pilsner',\n",
       "       'Woolybugger Wheat', 'EOS Hefeweizen', 'Brunette Nut Brown Ale',\n",
       "       'Samuel Adams Summer Ale', 'Helles Golden Lager', 'Elder Betty',\n",
       "       'Sweet As Pacific Ale', 'Epicenter Amber Ale', 'SanTan HefeWeizen',\n",
       "       'Barn Burner Saison', 'Vanilla Bean Buffalo Sweat',\n",
       "       \"The Hole in Hadrian's Wall\", 'Honey Wheat', 'The Lawn Ranger',\n",
       "       'Country Pale Ale', 'Orange Wheat', 'Hangar 24 Helles Lager',\n",
       "       'Tallgrass Pub Ale', 'Get Up Offa That Brown',\n",
       "       'Booyah Farmhouse Ale', 'Sly Fox Christmas Ale 2012 (2012)',\n",
       "       'Northern Lights Amber Ale', 'Polar Pale Ale', 'Pumpkan',\n",
       "       'Wheat the People', 'Apricot Blonde', 'Lawnmower Lager',\n",
       "       'Dry Dock Hefeweizen', 'Widespread Wit', 'Bombshell Blonde',\n",
       "       'Sex Panther (2014)', 'Black Walnut Wheat',\n",
       "       'Boont Amber Ale (2010)', 'Hell or High Watermelon Wheat (2009)',\n",
       "       '21st Amendment Watermelon Wheat Beer (2006)', 'Choc Beer (2003)',\n",
       "       'Mr. Pineapple', 'Blueberry Blonde Ale',\n",
       "       'Point Nude Beach Summer Wheat (2011)', 'Buffalo Sweat',\n",
       "       'Cold Smoke Scotch Ale (2007)',\n",
       "       'Summer Solstice Cerveza Crema (2009)',\n",
       "       'Fat Tire Amber Ale (2011)', \"Hilliard's Blonde\",\n",
       "       'Devils Tramping Ground Tripel', 'Lava Lake Wit',\n",
       "       'Halcyon Unfiltered Wheat', 'Blue Point Summer Ale',\n",
       "       'Three Kings Ale', 'Full Boar Scotch Ale', 'Cherry Ale (1)',\n",
       "       'Apollo', 'Blacktop Blonde', 'Wachusett Blueberry Ale',\n",
       "       'UFO White', 'Rosa Hibiscus Ale', 'Schlafly Hefeweizen',\n",
       "       'Snowshoe White Ale', '312 Urban Wheat Ale (2012)', 'White Thai',\n",
       "       'Blackbeary Wheat', 'Barney Flats Oatmeal Stout (2012)',\n",
       "       'Jon Boat Coastal Ale', 'Golden Road Hefeweizen (2012)',\n",
       "       'La Perouse White', 'Florida Cracker Belgian Wit',\n",
       "       'Dirty Blonde Ale', 'Tin Roof Blonde Ale', \"Atwater's Lager\",\n",
       "       'Winter Solstice', 'McKinney Eddy Amber Ale', 'SoDo Brown Ale',\n",
       "       'Purple Haze', 'Abita Amber', 'Double D Blonde (2011)',\n",
       "       'Great Crescent Belgian Style Wit', 'Joseph James American Lager',\n",
       "       'Top Rope Mexican-style Craft Lager', 'Weisse Versa',\n",
       "       'Dundee Summer Wheat Beer', 'Mustang Golden Ale', 'Washita Wheat',\n",
       "       'Bottom Up Belgian Wit', 'Snake River Lager',\n",
       "       'Black Star Double Hopped Golden Lager ',\n",
       "       'Pyramid Hefeweizen (2011)', 'Wild Onion Summer Wit',\n",
       "       'SummerBright Ale', 'Whitsun', 'Mexican Logger', 'Festie',\n",
       "       'Narragansett Fest Lager', 'Mana Wheat',\n",
       "       'SanTan HefeWeizen (2010)', 'Flaming Damsel Lager (2010)',\n",
       "       'Point Nude Beach Summer Wheat (2010)', 'Point Amber Classic',\n",
       "       \"O'Fallon Wheach\", 'Epicenter Amber Ale (2010)', 'White Rascal',\n",
       "       'Ellie???s Brown Ale', 'K??ld Lager (2010)', 'Buffalo Sweat (2010)',\n",
       "       'Colorado K??lsch', 'Cold Smoke Scotch Ale', 'Avalanche Ale',\n",
       "       'Haywire Hefeweizen (2010)', 'Boont Amber Ale (2011)',\n",
       "       'Summer Solstice (2011)', 'Fat Tire Amber Ale (2008)',\n",
       "       'Sunlight Cream Ale', 'Schlafly Summer Lager',\n",
       "       'Bikini Blonde Lager', 'Royal Weisse Ale', 'Hell',\n",
       "       'Hell or High Watermelon Wheat'], dtype=object)"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IBUs < 21\").Beer.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List the median IBUs of each type of beer. Graph it.\n",
    "\n",
    "Put the highest at the top, and the missing ones at the bottom.\n",
    "\n",
    "- Tip: Look at the options for `sort_values` to figure out the `NaN` thing. The `?` probably won't help you here."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Style'>"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x1440 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#df.groupby(by='Style').IBUs.median().sort_values().plot(kind=\"barh\")\n",
    "\n",
    "df.groupby(by='Style').IBUs.median().sort_values(na_position='first').plot(kind='barh', figsize=(5,20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hmmmm, it looks like they are generally different styles. What are the most common 5 styles of high-IBU beer vs. low-IBU beer?\n",
    "\n",
    "- *Tip: You'll want to think about it in three pieces - filtering to only find the specific beers beers, then finding out what the most common styles are, then getting the top 5.*\n",
    "- *Tip: You CANNOT do this in one command. It's going to be one command for the high and one for the low.*\n",
    "- *Tip: \"High IBU\" means higher than 75th percentile, \"Low IBU\" is under 25th percentile*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      195\n",
       "American Double / Imperial IPA     72\n",
       "American Pale Ale (APA)            18\n",
       "American Black Ale                 15\n",
       "American Strong Ale                 9\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IBUs > 64\").Style.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American Pale Wheat Ale    43\n",
       "American Blonde Ale        36\n",
       "Fruit / Vegetable Beer     28\n",
       "Hefeweizen                 21\n",
       "Witbier                    20\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IBUs < 21\").Style.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the average IBU of \"Witbier\", \"Hefeweizen\" and \"American Pale Wheat Ale\" styles\n",
    "\n",
    "I'm counting these as wheat beers. If you see any other wheat beer categories, feel free to include them. I want ONE measurement and ONE graph, not three separate ones. And 20 to 30 bins in the histogram, please.\n",
    "\n",
    "- *Tip: I hope that `isin` is in your toolbox*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18.982142857142858"
      ]
     },
     "execution_count": 253,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df.query(Style = \"Witbier\")\n",
    "\n",
    "wheat = [\"Witbier\", \"Hefeweizen\", \"American Pale Wheat Ale\"]\n",
    "\n",
    "df.query(\"Style in @wheat\").IBUs.mean()\n",
    "\n",
    "df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Draw a histogram of the IBUs of those beers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.query(\"Style in @wheat\").IBUs.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the average IBU of any style with \"IPA\" in it (also draw a histogram)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "71.94897959183673"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipa_df.IBUs.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ipa_df.IBUs.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Plot those two histograms on top of one another\n",
    "\n",
    "To plot two plots on top of one another, you *might* just be able to plot twice in the same cell. It depends on your version of pandas/matplotlib! If it doesn't work, you'll need do two steps.\n",
    "\n",
    "1. First, you make a plot using `plot` or `hist`, and you save it into a variable called `ax`.\n",
    "2. You draw your second graph using `plot` or `hist`, and send `ax=ax` to it as a parameter.\n",
    "\n",
    "It would look something like this:\n",
    "\n",
    "```python\n",
    "ax = df.plot(....)\n",
    "df.plot(ax=ax, ....)\n",
    "``` \n",
    "\n",
    "And then youull get two plots on top of each other. They won't be perfect because the bins won't line up without extra work, but it's fine!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ipa_df.IBUs.hist()\n",
    "df.query(\"Style in @wheat\").IBUs.hist()\n",
    "\n",
    "#hist(alpha=0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "metadata": {},
   "outputs": [],
   "source": [
    "#ax = df.plot(x=\"Style in @wheat\", y=df.IBUs, kind='hist')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Compare the ABV of wheat beers vs. IPAs : their IBUs were really different, but how about their alcohol percentage?\n",
    "\n",
    "Wheat beers might include witbier, hefeweizen, American Pale Wheat Ale, and anything else you think is wheaty. IPAs probably have \"IPA\" in their name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.043715846994536"
      ]
     },
     "execution_count": 238,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Style in @wheat\").ABV.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.879285714285714"
      ]
     },
     "execution_count": 239,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipa_df.ABV.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Good work!\n",
    "\n",
    "For making it this far, your reward is my recommendation for Athletic Brewing Co.'s products as the best non-alcoholic beer on the market. Their Run Wild IPA and Upside Dawn are both very solid."
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
   "version": "3.10.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
