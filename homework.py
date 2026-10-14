from ipaddress import *

funcs_to_run = {}


def task(number: int):
    def decorator(func):
        funcs_to_run[number] = func
        return func

    return decorator


class Homework:
    strict_value = False

    @classmethod
    def into_bin(cls, number: str) -> str:
        number = int(number)
        binary_number = f"{int(number):08b}"
        return binary_number

    @staticmethod
    @task(1)
    def solution1(host1: str = "126.115.78.15", host2: str = "126.115.84.26") -> int:
        result = []
        for mask in range(16, 33):
            net1 = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
            net2 = ip_network(f"{host2}/{mask}", strict=Homework.strict_value)
            res = 0
            if net1 == net2:
                for host in net1:
                    if f"{int(host):032b}".count("1") == 22:
                        res += 1
                result.append(res)
        return min(result) if result else 0

    @staticmethod
    @task(2)
    def solution2(host1: str = "218.194.82.148", mask: str = "255.255.255.192") -> str:
        net = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
        max_host = str(net[-2])
        return str(max_host.replace(".", ""))

    @staticmethod
    @task(3)
    def solution3(host1: str = "132.118.34.161") -> int:
        result = []
        for mask in range(22, 33):
            net1 = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
            res = 0
            for host in net1:
                if f"{int(host):032b}".count("1") == 13:
                    res += 1
            if res == 35:
                result.append(mask)
        return 32 - result[0] if result else 0

    @staticmethod
    @task(4)
    def solution4(host1: str = "94.253.128.0", mask: str = "255.255.128.0") -> int:
        net = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
        res = 0
        for host in net:
            if f"{int(host):032b}".count("1") % 6 != 0 and f"{int(host):032b}"[-3:] == "101":
                res += 1
        return res

    @staticmethod
    @task(5)
    def solution5(host1: str = "102.141.0.0", mask: str = "255.255.192.0") -> int:
        net = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
        res = 0
        for host in net:
            if f"{int(host):032b}".count("1") % 7 == 0 and f"{int(host):032b}"[-4:] == "1011":
                res += 1
        return res

    @staticmethod
    @task(6)
    def solution6(host1: str = "123.20.103.136", host2: str = "123.20.103.151") -> str:
        res = []
        for mask in range(1, 33):
            net1 = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
            net2 = ip_network(f"{host2}/{mask}", strict=Homework.strict_value)
            if net1 != net2:
                res.append(mask)
        resn = ip_network(f"{host1}/{min(res)}", strict=Homework.strict_value)
        return str(resn.netmask).split('.')[-1]

    @staticmethod
    @task(7)
    def solution7(host1: str = "193.45.192.104", host2: str = "193.45.206.210") -> int:
        result = []
        for mask in range(16, 33):
            net1 = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
            net2 = ip_network(f"{host2}/{mask}", strict=Homework.strict_value)
            if net1 == net2:
                res = 0
                for host in net1:
                    if f"{int(host):032b}".count("1") % 2 == 0:
                        res += 1
                result.append(res)
        return min(result)

    @staticmethod
    @task(8)
    def solution8(host1: str = "154.63.206.129", host2: str = "154.63.100.75") -> int:
        max_oct = -1
        for mask in range(16, 33):
            net1 = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
            net2 = ip_network(f"{host2}/{mask}", strict=Homework.strict_value)
            if net1 == net2:
                result = net1.netmask.packed[2]
                if result > max_oct:
                    max_oct = result
        return max_oct

    @staticmethod
    @task(9)
    def solution9(host1: str = "186.135.80.0", mask: str = "255.255.252.0") -> int:
        net1 = ip_network(f"{host1}/{mask}", strict=Homework.strict_value)
        result = 0
        for host in net1:
            host_octets_list = str(host).split(".")
            host_octets_list = list(map(Homework.into_bin, host_octets_list))
            if host_octets_list[0].count("1") + host_octets_list[1].count("1") > host_octets_list[2].count("1") + \
                    host_octets_list[3].count("1"):
                result += 1
        return result


def run() -> None:
    for num, func in sorted(funcs_to_run.items()):
        print(f"{num} задание: {func()}")


if __name__ == "__main__":
    run()
