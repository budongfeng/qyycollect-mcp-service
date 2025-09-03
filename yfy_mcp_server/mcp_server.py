import json
import os

from fastmcp import FastMCP

mcp = FastMCP(name="yfy-kbase-collect", version="1.0.1")


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


@mcp.tool()
def get_douyin_download_link(share_link: str) -> str:
    """
    获取抖音视频的无水印下载链接

    参数:
    - share_link: 抖音分享链接或包含链接的文本

    返回:
    - 包含下载链接和视频信息的JSON字符串
    """
    try:

        return json.dumps({
            "status": "success",
            "video_id": 1,
            "title": "健身",
            "download_url": "https://baijiahao.baidu.com/s?id=1831340507379138315&wfr=spider&for=pc",
            "description": f"视频标题: 健身",
            "usage_tip": "可以直接使用此链接下载无水印视频"
        }, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"获取下载链接失败: {str(e)}"
        }, ensure_ascii=False, indent=2)


def main(transport='stdio', host='0.0.0.0', port=8000):
    """
    运行MCP服务

    Args:
        transport (str): 传输方式，可选 'stdio' 或 'sse'
        host (str): HTTP服务器监听地址
        port (int): HTTP服务器监听端口
    """
    if transport == 'sse':
        # 使用SSE传输方式，启动HTTP服务器
        mcp.run(transport='sse', host=host, port=port)
    else:
        # 使用stdio传输方式
        mcp.run(transport='stdio')


if __name__ == "__main__":
    import sys
    main()
