#Copyright (c) 2022. telegram.me/ask_admin001

import re
import asyncio
import requests
from typing import Any, List
from urllib.parse import urlparse
from .exception import LinkInvalid


class Mdisk:

    "Unofficial Mdisk API Wrapper"
    
    def __init__(self, api_key:str):
        self.__api_key = api_key
        self.__base_url = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'

        if not self.__api_key:
            raise Exception("API key not provided")


    async def convert(self, link:str, silently_fail:bool = False) -> str:
        """
        It takes a link, checks if it's a valid mdisk link, and if it is, it sends a POST request to the
        mdisk API with the link and the API key, and returns the sharelink
        
        :param link: The link to be converted
        :type link: str
        :param silently_fail: If True, the function will return the given link instead of raising an exception, only if the function raise an exception,
        defaults to False
        :type silently_fail: bool (optional)
        :return: The link to the file on mdisk.
        """
        is_mdisk_link = await self.is_mdisk_link(link)
        if is_mdisk_link:
            try:
                data = {
                    'token': self.__api_key,
                    'link':link
                }
                res = requests.post(self.__base_url, json = data)
                return res.json()['sharelink']
            except requests.exceptions.Timeout as errt:
                print("Timeout Error: ",errt)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting: ",errc)
            except Exception as e:
                return await self.__error_handler(url=link, silently_fail=silently_fail, exception=Exception)
        else: 
            return await self.__error_handler(url=link, silently_fail=silently_fail, exception=LinkInvalid)


    async def bulk_convert(self, urls:list, silently_fail:bool=True) -> List:
        """
        It converts a list of URLs to a list of shortened URLs.
        
        :param urls: A list of urls to convert
        :type urls: list
        :param silently_fail: If True, the function will return the given link instead of raising an exception, only if the function raise an exception,
        defaults to True
        :return: A list of the converted links.
        """
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(self.convert(link=url, silently_fail=silently_fail))
            tasks.append(task)
        return await asyncio.gather(*tasks, return_exceptions=True)


    async def convert_from_text(self, text:str, silently_fail:bool=True) -> str:
        """
        It takes a string, finds all the links in it, converts them, and then replaces the original links
        with the converted ones
        
        :param text: The text to be converted
        :type text: str
        :param silently_fail: If True, the function will return the given link instead of raising an exception, only if the function raise an exception,
        defaults to True
        :return: A text of converted links
        """
        links = re.findall(r'https?://mdisk.me[^\s`!()\[\]{};:".,<>?«»“”‘’]+', text)
        converted_links = await self.bulk_convert(links, silently_fail=silently_fail)

        for i, mdisk_link in enumerate(converted_links):
            text = text.replace(links[i], mdisk_link)

        return text


    async def get_filename(self, link:str) -> str:
        """
        It takes a link and returns the filename of the file
        
        :param link: The link to the file you want to download
        :return: The filename of the file that is being downloaded.
        """

        if not await self.is_mdisk_link(link):
            raise LinkInvalid(link)

        url = 'https://diskuploader.mypowerdisk.com/v1/tp/filename'
        rid = await self.__get_rid(link)
        res = requests.get(url, params={'token':self.__api_key,'rid':rid})
        data = res.json()

        if res.status_code == 200 and data['status'] == 'ok':
            return data['filename']
        elif data['status'] == 'reject':
            raise Exception('Check if the given link is saved in your Mdisk account')
        else:
            raise LinkInvalid(link)

    async def change_filename(self, link: str, filename: str) -> str:
        """
        It takes a link and a filename as parameters, gets the rid of the link, then sends a POST request to
        the API with the rid and filename as parameters, and returns the filename if the request is
        successful
        
        :param link: The link to the file you want to change the name of
        :param filename: The name of the file you want to change to
        :return: The changed filename is being returned.
        """
        
        if not await self.is_mdisk_link(link):
            raise LinkInvalid(link)

        rid = await self.__get_rid(link)
        url = 'https://diskuploader.mypowerdisk.com/v1/tp/info'
        param = {'token': self.__api_key, 'rid':rid,'filename':filename}
        res = requests.post(url, json = param)
        data = res.json()

        if res.status_code == 200 and data['status'] == 'ok':
            return filename
        elif data['status'] == 'reject':
            raise Exception('Check if the given link is saved in your Mdisk account')
        else:
            raise LinkInvalid(link)


    async def __get_rid(self, link):
        """
        It takes a link, splits it by the '/' character, and returns the last item in the list
        
        :param link: The link to the reddit post
        :return: The last element of the list.
        """
        return link.split('/')[-1]


    async def __error_handler(self, url:str, silently_fail:bool, exception=Exception, message="Some error occurred during converting: %s") -> Any | Exception:
        """
        If the URL is valid, return it. If it's not, return it or raise an exception, depending on the value
        of the `silently_fail` parameter
        
        :param url: The URL to be validated
        :type url: str
        :param silently_fail: If True, then if the URL is not valid, return the original URL. If False,
        raise an exception
        :type silently_fail: bool
        :param exception: The exception to raise if the URL is not valid
        :return: The url is being returned.
        """
        if silently_fail:
            return url
        else:
            raise exception(message % url)


    @staticmethod
    async def is_mdisk_link(link:str) -> bool:
        """
        It checks if the link is a valid mdisk link.
        
        :param link: The link to the file
        :type link: str
        :return: True if the link is a valid mdisk link, False otherwise
        """
        domain = urlparse(link).netloc
        if 'mdisk.me' in domain:
            return True
        return False
