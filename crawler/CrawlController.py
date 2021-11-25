from datetime import datetime, timedelta
from crawler import Crawler

class CrawlController:
    def __init__(self):
        self.crawler = Crawler()
        self.url_format = "https://news.naver.com/main/list.naver?mode=LSD&sid1=001&mid=sec&listType=title&date={}&page={}"
        self.date_array = []
        self.page_array = [i for i in range(20)]
        self.url_array = []
        self.news_data = {}

        # default
        self.start_date = "20211125"
        self.end_date = "20211125"


    @staticmethod
    def __is_date_type(date):
        """
        date의 형식을 확인하는 메소드
        :param date: String
        :return: True / False
        """
        # 날짜 길이 8자를 넘어가는 경우
        if len(date) != 8:
            return False
        # 월이 1월에서 12월 사이가 아닌 경우
        elif 1 > int(date[4:6]) or int(date[4:6]) > 12:
            return False
        # 일이 1일에서 31일 사이가 아닌 경우
        elif 1 > int(date[6:]) or int(date[6:]) > 31:
            return False
        # 그 외 존재하지 않는 일인 경우 (ex. 2월의 윤년, 31일 없는 날) 설정 필요
        return True

    @staticmethod
    def __get_date_range(start_date, end_date):
        """
        start_date와 end_date 사이의 날짜를 배열로 리턴. (start와 end 포함)
        포매팅까지 진행
        :param start_date: String
        :param end_date: String
        :return: dates array
        """
        trans_start_date = start_date[:4] + "-" + start_date[4:6] + "-" + start_date[6:]
        trans_end_date = end_date[:4] + "-" + end_date[4:6] + "-" + end_date[6:]

        start = datetime.strptime(trans_start_date, "%Y%m%d")
        end = datetime.strptime(trans_end_date, "%Y%m%d")
        dates = [(start + timedelta(days=i)).strftime("%Y%m%d") for i in range((end - start).days + 1)]
        return dates

    def _set_start_date(self, start_date):
        """
        크롤링 시작 날짜 설정
        :param start_date: String
        :return: True / False
        """
        # 형식 유지 확인 필요
        if self.__is_date_type(start_date):
            self.start_date = start_date
            return True
        else:
            print("시작 날짜 형식이 적합하지 않습니다.")
            return False

    def _set_end_date(self, end_date):
        """
        크롤링 끝 날짜 설정
        :param end_date: String
        :return: True / False
        """
        # 형식 유지 확인 필요
        if self.__is_date_type(end_date):
            self.end_date = end_date
            return True
        else:
            print("끝 날짜 형식이 적합하지 않습니다.")
            return False

    def _set_crawl_url(self, start_date, end_date):
        """
        self.url_array에 크롤링 할 url을 모두 계산해 삽입하는 메소드
        :param start_date: String
        :param end_date: String
        :return: True
        """
        if not self._set_start_date(start_date):
            return

        if not self._set_end_date(end_date):
            return

        self.date_array = self.__get_date_range(start_date, end_date)

        for date in self.date_array:
            for page in self.page_array:
                self.url_array.append(self.url_format.format(date, page))

        return True
