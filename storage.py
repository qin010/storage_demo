def binary_search(lis, num):
    """二分查找算法
    Args:
        lis (list): 要查找的列表
        num (): 要查找列表里的元素
    Returns:
        mid (int): 对应元素的数组索引
    """
    left = 0
    right = len(lis) - 1
    while left <= right:  # 循环条件
        mid = (left + right) // 2  # 获取中间位置，数字的索引（序列前提是有序的）
        if num < lis[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找，
            right = mid - 1  # 来到左边后，需要将右变的边界换为mid-1
        elif num > lis[mid]:  # 如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1  # 来到右边后，需要将左边的边界换为mid+1
        else:
            return mid  # 如果查询数字刚好为中间值，返回该值得索引
    return -1  # 如果循环结束，左边大于了右边，代表没有找到


class ProxyStorage(object):
    """存储代理配置项的类：存储所有数据"""
    def __init__(self):
        """
        Args:
            proxy_instance (list,instance): proxy类的实例
        """
        self.proxy_instance = []
        self.id_list = []

    def add_proxy_instance(self, add_instance):
        """添加proxy类的实例
        Args:
            add_instance (instance): 要添加的proxy类的实例
        """
        self.proxy_instance.append(add_instance)
        self.id_list.append(add_instance.id)

    def del_proxy_instance(self, delete_instance):
        """删除对应proxy类的实例
        Args:
            delete_instance (instance): 要删除的proxy类的实例
        """
        index = binary_search(self.id_list, delete_instance.id)
        del self.proxy_instance[index]
        del self.id_list[index]

    def replace_proxy_instance(self, replace_instance):
        """替换/更新对应proxy类的实例
        Args:
            replace_instance (instance): 要替换的proxy类的实例
        """
        index = binary_search(self.id_list, replace_instance.id)
        self.proxy_instance[index] = replace_instance

    def id_find(self, search_id):
        """ 根据id查找到对应的Proxy实例 """
        index = binary_search(self.id_list, search_id)
        if index >= 0:
            return self.proxy_instance[index]
        else:
            print("查找id不存在")
            return False


class Proxy(object):
    """代理配置项的类"""
    id_count = 0

    def __init__(self, type, avaliable, last_check_time, protocol, ip=None, domain=None):
        """
        Args:
            id (int)：代理的唯一标识符
            type (int): 代理类型
            ip (string): 代理ip（可为空）
            domain (string)：代理域名（可为空）
            avaliable (bool)：代理是否可用
            last_check_time (string)：上次检查是否可用的时间
            protocol (int)：代理协议
        """
        self.id = Proxy.id_count
        Proxy.id_count += 1

        self.type = type
        self.ip = ip
        self.domain = domain
        self.avaliable = avaliable
        self.last_check_time = last_check_time
        self.protocol = protocol


proxy_storage = ProxyStorage()
proxy_1 = Proxy(type=11, avaliable=True, last_check_time="2022.4.1", protocol=30, ip=1111, domain="www.baidu.com")
proxy_storage.add_proxy_instance(proxy_1)
proxy_2 = Proxy(type=12, avaliable=True, last_check_time="2022.4.1", protocol=32, ip=None, domain=None)
proxy_storage.add_proxy_instance(proxy_2)
proxy_3 = Proxy(type=13, avaliable=True, last_check_time="2022.4.1", protocol=42, ip=None, domain=None)
proxy_storage.add_proxy_instance(proxy_3)

proxy_storage.del_proxy_instance(proxy_3)

proxy_2.avaliable=False
proxy_storage.replace_proxy_instance(proxy_2)

a = proxy_storage.id_find(1)
b = proxy_storage.id_find(2)
c = 1


