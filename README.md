## File Descriptions:
- Apriori.py : loads dataset and mines strong association rules based on Apriori  
- logger.py : definition of a class 'Logger'  
- Datebase : dataset (e.g. supermarket shopping dataset)  
- log : includes a series of log files keeping the result of Apriori under different experimental configurations  

## Conclusions:
1. Min_Conf remains unchanged. The larger Min_Sup is, the fewer frequent itemsets are mined, and the running time of the Apriori algorithm is relatively reduced.
2. Min_Sup remains unchanged. The larger Min_Conf is, the fewer strong association rules are mined. There is no specific change pattern in the running time of the Apriori algorithm.
3. When Min_Sup=0.3，Min_Conf=0.95, we still have:  
        - 1  ['常温熟食类', '进口食品'] -> ['饮料']  Conf=0.969957  Sup=0.302949  
        - 2  ['散装休闲食品', '进口食品'] -> ['饮料']  Conf=0.950207  Sup=0.306971  
        - 3  ['常温熟食类', '散装休闲食品'] -> ['饮料']  Conf=0.951020  Sup=0.312332  

## Reference:
https://github.com/ZbWeR/Association-rule-mining  
