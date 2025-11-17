import textwrap
from mcp.server.fastmcp import FastMCP, Context

# Initialize FastMCP server
mcp = FastMCP("prompt-provider")

# 提供したいプロンプトを定義
MY_AWESOME_PROMPT = textwrap.dedent("""
あなたはプロのPythonコードのレビュアーです。
回答は必ず日本語で回答してください。
レビュー結果を以下の形式で返してください:
    - コードの課題や改善点
    - コードの改善提案
    - コードのスコア (0-100)

{code}
""")

@mcp.tool()
async def code_review(ctx: Context) -> str:
    """
    ソースコードをレビューするための定型プロンプトを取得します。
    プロンプトエンジニアリングに使えます。
    """
    await ctx.info("Code review requested for")
    return MY_AWESOME_PROMPT

if __name__ == "__main__":
    mcp.run()
