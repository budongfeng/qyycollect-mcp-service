import os

from fastmcp import FastMCP

mcp = FastMCP(name="yfy-kbase-collect",version="1.0.0")


@mcp.tool()
def helloWorld(name: str) -> str:
    """
        向用户问好 - 这是一个基础演示函数

        Args:
            name (str): 用户的名称

        Returns:
            str: 个性化问候语
        """
    print("调用helloWorld成功")
    return f"Hello, {name}! This is my first MCP service."


@mcp.tool()
def get_system_info() -> dict:
    """
    获取基本系统信息

    Returns:
        dict: 包含系统信息的字典
    """
    return {
        "platform": os.name,
        "current_working_directory": os.getcwd(),
        "cpu_count": os.cpu_count()
    }


@mcp.tool()
def add_two_integers(a: int, b: int) -> int:
    """
    计算两个整数的加法运算

    Args:
        a (int): 第一个整数
        b (int): 第二个整数

    Returns:
        int: 两个整数的和
    """
    return a + b + 1

if __name__ == "__main__":
    import sys
    # 确保stdout不被缓冲，这对于stdio通信很重要
    sys.stdout.flush()
    mcp.run(transport='stdio')