from pandas import DataFrame, Series

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea', 
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts_df = DataFrame({'country_name':Series(countries),'gold':Series(gold),'silver':Series(silver),'bronze':Series(bronze)})

"""
##code snippets executed in shell

>>> olympic_medal_counts_df

    bronze    country_name  gold  silver
0        9    Russian Fed.    13      11
1       10          Norway    11       5
2        5          Canada    10      10
3       12   United States     9       7
4        9     Netherlands     8       7
5        5         Germany     8       6
6        2     Switzerland     6       3
7        1         Belarus     5       0
8        5         Austria     4       8
9        7          France     4       4
10       1          Poland     4       1
11       2           China     3       4
12       2           Korea     3       3
13       6          Sweden     2       7
14       2  Czech Republic     2       4
15       4        Slovenia     2       2
16       3           Japan     1       4
17       1         Finland     1       3
18       2   Great Britain     1       1
19       1         Ukraine     1       0
20       0        Slovakia     1       0
21       6           Italy     0       2
22       2          Latvia     0       2
23       1       Australia     0       2
24       0         Croatia     0       1
25       1      Kazakhstan     0       0




>>> olympic_medal_counts_df[['country_name',]]

      country_name
0     Russian Fed.
1           Norway
2           Canada
3    United States
4      Netherlands
5          Germany
6      Switzerland
7          Belarus
8          Austria
9           France
10          Poland
11           China
12           Korea
13          Sweden
14  Czech Republic
15        Slovenia
16           Japan
17         Finland
18   Great Britain
19         Ukraine
20        Slovakia
21           Italy
22          Latvia
23       Australia
24         Croatia
25      Kazakhstan



>>> olympic_medal_counts_df[['country_name','gold']]

      country_name  gold
0     Russian Fed.    13
1           Norway    11
2           Canada    10
3    United States     9
4      Netherlands     8
5          Germany     8
6      Switzerland     6
7          Belarus     5
8          Austria     4
9           France     4
10          Poland     4
11           China     3
12           Korea     3
13          Sweden     2
14  Czech Republic     2
15        Slovenia     2
16           Japan     1
17         Finland     1
18   Great Britain     1
19         Ukraine     1
20        Slovakia     1
21           Italy     0
22          Latvia     0
23       Australia     0
24         Croatia     0
25      Kazakhstan     0




>>> olympic_medal_counts_df.loc[1]
bronze              10
country_name    Norway
gold                11
silver               5
Name: 1, dtype: object




>>> olympic_medal_counts_df[olympic_medal_counts_df['gold']>8]
   bronze   country_name  gold  silver
0       9   Russian Fed.    13      11
1      10         Norway    11       5
2       5         Canada    10      10
3      12  United States     9       7



>>> olympic_medal_counts_df['country_name'][olympic_medal_counts_df['gold']>8]
0     Russian Fed.
1           Norway
2           Canada
3    United States
Name: country_name, dtype: object

