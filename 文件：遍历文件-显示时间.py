import datetime
from pathlib import Path


def timestamp2datetime(timestamp, convert_to_local=True, utc=8, is_remove_ms=True):
    """
    转换 UNIX 时间戳为 datetime对象
    :param timestamp: 时间戳
    :param convert_to_local: 是否转为本地时间
    :param utc: 时区信息，中国为utc+8
    :param is_remove_ms: 是否去除毫秒
    :return: datetime 对象
    """
    if is_remove_ms:
        timestamp = int(timestamp)
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    if convert_to_local:
        dt = dt + datetime.timedelta(hours=utc)
    return dt


def convert_date(timestamp):
    format = '%Y-%m-%d %H:%M:%S'
    dt = timestamp2datetime(timestamp)
    return dt.strftime(format)


basepath = Path('D:/pythonProject/MyPractice')
for entry in basepath.iterdir():
    if entry.is_file():
        info = entry.stat()
        print('{} 上次修改时间为 {}'.format(entry.name, convert_date(info.st_mtime)))