def select_proxy(proxy_list):
    """
    Returns the proxy with the lowest workload.
    """
    return sorted(proxy_list, key=lambda x: x["hosts"])[0]


if __name__ == "__main__":
    proxies = [
        {"name": "proxy01", "hosts": 150},
        {"name": "proxy02", "hosts": 90},
        {"name": "proxy03", "hosts": 120}
    ]

    selected = select_proxy(proxies)
    print(f"Selected proxy: {selected['name']}")
