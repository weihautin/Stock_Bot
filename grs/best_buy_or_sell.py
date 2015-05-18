# -*- coding: utf-8 -*-
''' Best buy or sell '''
# Copyright (c) 2012, 2013, 2014 Toomore Chiang, http://toomore.net/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class BestFourPoint(object):
    """ 四大買點組合

        :param grs.Stock data: 個股資料
    """
    def __init__(self, data):
        self.data = data

    def bias_ratio(self, positive_or_negative=False):
        """ 判斷乖離

            :param bool positive_or_negative: 正乖離 為 True，負乖離 為 False
        """
        return self.data.check_moving_average_bias_ratio(
                               self.data.moving_average_bias_ratio(3, 6)[0], #三日乖離率與六日乖離率的差
                               positive_or_negative=positive_or_negative)[0]

    def golden_cross(self, m, n, back_to_test_n_days, positive_or_negative=False):
        """ 黃金交叉         

            :rtype: str or False
        """
	return self.data.golden_cross_5_20(back_to_test_n_days,       
                               self.data.moving_average_bias_ratio(m, n)[0],
                               positive_or_negative=positive_or_negative)

	# return self.data.moving_average_bias_ratio(5, 20)[0]

       # return self.data.golden_cross_5_20(tmp, sample)

    def golden_cross_no_back_test(self, m, n):
        """
        傳統黃金交叉,m日均線高於n日均線(黃金交叉)
        """
        return self.data.moving_average(m)[0][-1] >  self.data.moving_average(n)[0][-1] and \
               self.data.moving_average(m)[0][-2] <= self.data.moving_average(n)[0][-2]

    def best_5_10_20(self): 
        """ 
        5>10>20日均線
        """
        return self.data.moving_average(5)[0][-1] >  self.data.moving_average(10)[0][-1] > self.data.moving_average(20)[0][-1]

    def best_5_10_20_backtest(self,n): 
        """ 
        5>10>20日均線,含n日回測
        """
        tmp = True
        initial = 1

        while initial <= n:
		if self.data.moving_average(5)[0][-initial] >  self.data.moving_average(10)[0][-initial]  > self.data.moving_average(20)[0][-initial]:
		 	pass	
		else:
			tmp = False
	       	initial+=1
	return tmp


#        return self.data.check_moving_average_bias_ratio(
#                               self.data.moving_average_bias_ratio(m, n)[0])[0] \
#               and self.data.moving_average(m)[0][-1] >  self.data.moving_average(n)[0][-1] 


    def check_plus_bias_ratio(self):
        """ 正乖離扣至最大 """
        return self.bias_ratio(True)

    def check_mins_bias_ratio(self):
        """ 負乖離扣至最大 """
        return self.bias_ratio()

    ##### 四大買點 #####

    def today_great_ma5(self, ntimes):
	""" 今天量大於昨天前的五日均量N倍
	"""
        result = ( self.data.value[-1] / self.data.moving_average_value(5)[0][-2] ) > ntimes and \
                 self.data.price[-1] > self.data.openprice[-1] and self.data.value[-1] > 1000 
        return result


    def y_v_t_r(self):
        """ 昨天暴量長紅,今天又上漲
        """
        result = self.data.value[-2] > self.data.value[-3] and self.data.price[-2] > self.data.openprice[-2] and \
                 self.data.price[-1]/self.data.price[-2] >= 1.01  and self.data.price[-1]/self.data.price[-2] <= 1.07 and self.data.value[-1] > 1000 
        return result

    def otc_y_v_t_r(self):
        """ 昨天暴量長紅,今天又上漲
        """
        result = self.data.value[-2] > self.data.value[-3] and self.data.price[-2] > self.data.openprice[-2] and \
                 self.data.price[-1]/self.data.price[-2] >= 1.01  and self.data.price[-1]/self.data.price[-2] <= 1.07 and self.data.value[-1]*1000 > 1000  
        return result

	


    def red_2(self):
        """ 量大收紅(今日量>昨日量 and 收盤價格>開盤價格 and 負乖離股價在移動平均線下)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] > self.data.openprice[-1] and \
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] > self.data.openprice[-2]
        return result

    def red_3(self):
        """ 量大收紅(今日量>昨日量 and 收盤價格>開盤價格 and 負乖離股價在移動平均線下)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] > self.data.openprice[-1] and \
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] > self.data.openprice[-2] and \
                 self.data.value[-3] > self.data.value[-4] and self.data.price[-3] > self.data.openprice[-3]
        return result

    def red_4(self):
        """ 量大收紅(今日量>昨日量 and 收盤價格>開盤價格 and 負乖離股價在移動平均線下)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] > self.data.openprice[-1] and \
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] > self.data.openprice[-2] and \
                 self.data.value[-3] > self.data.value[-4] and self.data.price[-3] > self.data.openprice[-3] and \
                 self.data.value[-4] > self.data.value[-5] and self.data.price[-4] > self.data.openprice[-4]
        return result

    def black_2(self):
        """ 量大收黑(今日量>昨日量,今日收盤)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] < self.data.openprice[-1] and\
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] < self.data.openprice[-2] 
        return result


    def black_3(self):
        """ 量大收黑(今日量>昨日量,今日收盤)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] < self.data.openprice[-1] and\
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] < self.data.openprice[-2] and\
                 self.data.value[-3] > self.data.value[-4] and self.data.price[-3] < self.data.openprice[-3]
        return result

    def black_4(self):
        """ 量大收黑(今日量>昨日量,今日收盤)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] < self.data.openprice[-1] and\
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] < self.data.openprice[-2] and\
                 self.data.value[-3] > self.data.value[-4] and self.data.price[-3] < self.data.openprice[-3] and\
                 self.data.value[-4] > self.data.value[-5] and self.data.price[-4] < self.data.openprice[-4]
        return result

    def black_5(self):
        """ 量大收黑(今日量>昨日量,今日收盤)
        """
        result = self.data.value[-1] > self.data.value[-2] and self.data.price[-1] < self.data.openprice[-1] and\
                 self.data.value[-2] > self.data.value[-3] and self.data.price[-2] < self.data.openprice[-2] and\
                 self.data.value[-3] > self.data.value[-4] and self.data.price[-3] < self.data.openprice[-3] and\
                 self.data.value[-4] > self.data.value[-5] and self.data.price[-4] < self.data.openprice[-4] and\
                 self.data.value[-5] > self.data.value[-6] and self.data.price[-5] < self.data.openprice[-5]
        return result



    def best_buy_1(self):
        """ 量大收紅(今日量>昨日量 and 收盤價格>開盤價格 and 負乖離股價在移動平均線下)
        """
        result = self.data.value[-1] > self.data.value[-2] and \
                 self.data.price[-1] > self.data.openprice[-1]
        return result

    def best_buy_2(self):
        """ 量縮價不跌(今日量<昨日量 and 今日收盤價格>昨日收盤價格 and 負乖離股價在移動平均線下)
        """
        result = self.data.value[-1] < self.data.value[-2] and \
                 self.data.price[-1] > self.data.price[-2]
        return result

    def best_buy_3(self):
        """ 三日均價由下往上
        """
        return self.data.moving_average(3)[1] == 1

    def best_buy_4(self):
        """ 三日均價大於六日均價
        """
        return self.data.moving_average(3)[0][-1] > \
               self.data.moving_average(6)[0][-1]

    ##### 四大賣點 #####
    def best_sell_1(self):
        """ 量大收黑(今日量>昨日量,今日收盤)
        """
        result = self.data.value[-1] > self.data.value[-2] and \
                 self.data.price[-1] < self.data.openprice[-1]
        return result

    def best_sell_2(self):
        """ 量縮價跌
        """
        result = self.data.value[-1] < self.data.value[-2] and \
                 self.data.price[-1] < self.data.price[-2]
        return result

    def best_sell_3(self):
        """ 三日均價由上往下
        """
        return self.data.moving_average(3)[1] == -1

    def best_sell_4(self):
        """ 三日均價小於六日均價
        """
        return self.data.moving_average(3)[0][-1] < \
               self.data.moving_average(6)[0][-1]

    def best_four_point_to_buy(self):
        """ 判斷是否為四大買點

            :rtype: str or False
        """
        result = []
        if self.check_mins_bias_ratio() and \
            (self.best_buy_1() or self.best_buy_2() or self.best_buy_3() or \
             self.best_buy_4()):

#        if  (self.best_buy_1() or self.best_buy_2() or self.best_buy_3() or \
#             self.best_buy_4()):

            if self.best_buy_1():
                result.append(self.best_buy_1.__doc__.strip().decode('utf-8'))
            if self.best_buy_2():
                result.append(self.best_buy_2.__doc__.strip().decode('utf-8'))
            if self.best_buy_3():
                result.append(self.best_buy_3.__doc__.strip().decode('utf-8'))
            if self.best_buy_4():
                result.append(self.best_buy_4.__doc__.strip().decode('utf-8'))
            result = ', '.join(result)
            #result = '\n  '.join(result)
        else:
            result = False
        return result

    def best_four_point_to_sell(self):
        """ 判斷是否為四大賣點

            :rtype: str or False
        """
        result = []
        if self.check_plus_bias_ratio() and \
            (self.best_sell_1() or self.best_sell_2() or self.best_sell_3() or \
             self.best_sell_4()):
            if self.best_sell_1():
                result.append(self.best_sell_1.__doc__.strip().decode('utf-8'))
            if self.best_sell_2():
                result.append(self.best_sell_2.__doc__.strip().decode('utf-8'))
            if self.best_sell_3():
                result.append(self.best_sell_3.__doc__.strip().decode('utf-8'))
            if self.best_sell_4():
                result.append(self.best_sell_4.__doc__.strip().decode('utf-8'))
            result = ', '.join(result)
        else:
            result = False
        return result



    def best_four_point(self):
        """ 判斷買點或賣點

            :rtype: tuple
            :returns: (bool, str)
        """
        buy = self.best_four_point_to_buy()
        sell = self.best_four_point_to_sell()

        if buy:
            return True, buy
        elif sell:
            return False, sell

        return None 
