import abc


class CurrencyService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_currency_rate(self, currency):
        pass


class CbrCurrencyService(CurrencyService):
    def get_currency_rate(self, currency):
        return 0.57


class ProxyService(CurrencyService):
    def __init__(self):
        # ссылка на реальный сервис
        self.currency_rate_service = CbrCurrencyService()
        # кэш
        self.rates = dict()

    def get_currency_rate(self, currency):
        """
        Метод проверяет наличие валюты и возвращает корректировку из кэша при наличии там данных или
        из базы данных, если данных в кэше нет
        :param currency:
        :return:
        """
        if currency in self.rates.keys():
            # если есть, то из кэша
            print('выдаем значение из кэша')
        else:
            # если нет, то делаем запрос
            print('делаем запрос')
            rate = self.currency_rate_service.get_currency_rate(currency)
            self.rates[currency] = rate
        return rate


currency_rate = ProxyService()
print(currency_rate.get_currency_rate('rub'))
print(currency_rate.get_currency_rate('usd'))
print(currency_rate.get_currency_rate('eur'))
