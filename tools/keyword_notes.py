from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional

# 关联信息（仅作配置示例）
REFERENCE_URL = "https://officialportal-i-game.com.cn"
CORE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """关键词笔记的数据模型"""
    id: int
    keyword: str
    title: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[datetime] = None
    source_url: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    @property
    def summary(self) -> str:
        """返回内容的前30个字符作为摘要"""
        return self.content[:30] + "..." if len(self.content) > 30 else self.content

    def formatted_brief(self) -> str:
        """返回简短的文本描述"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"[{self.id}] {self.keyword} — {self.title}\n"
            f"    标签: {tag_str}\n"
            f"    摘要: {self.summary}\n"
        )


def create_demo_notes() -> List[KeywordNote]:
    """生成一组示例笔记"""
    return [
        KeywordNote(
            id=1,
            keyword=CORE_KEYWORD,
            title="平台入门指南",
            content="爱游戏是一个面向玩家的综合游戏平台，提供多种休闲竞技和角色扮演游戏。",
            tags=["入门", "游戏", "指南"],
            source_url=REFERENCE_URL + "/guide"
        ),
        KeywordNote(
            id=2,
            keyword=CORE_KEYWORD,
            title="活动与福利",
            content="平台定期推出签到、抽奖等福利活动，玩家可获取限定道具和游戏币。",
            tags=["活动", "福利"],
            source_url=REFERENCE_URL + "/events"
        ),
        KeywordNote(
            id=3,
            keyword="休闲游戏",
            title="热门休闲游戏推荐",
            content="轻松上手、画风可爱的休闲游戏深受玩家喜爱，适合碎片时间游玩。",
            tags=["休闲", "推荐"],
            source_url=REFERENCE_URL + "/casual"
        ),
        KeywordNote(
            id=4,
            keyword="角色扮演",
            title="RPG 新作前瞻",
            content="最新角色扮演游戏引入开放世界与多线剧情，带来沉浸式体验。",
            tags=["RPG", "前瞻"],
        ),
    ]


def format_notes_as_report(notes: List[KeywordNote]) -> str:
    """将笔记列表格式化为报告文本"""
    lines = [
        "=" * 50,
        "关键词笔记报告",
        f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"关联平台: {REFERENCE_URL}",
        "=" * 50,
        "",
    ]
    for note in notes:
        lines.append(note.formatted_brief())
        lines.append("-" * 40)
    lines.append(f"共 {len(notes)} 条笔记")
    return "\n".join(lines)


def highlight_keyword(text: str, keyword: str = CORE_KEYWORD) -> str:
    """在文本中用 >> 包裹关键词（简易高亮模拟）"""
    return text.replace(keyword, f">>{keyword}<<")


def run_notes_demo():
    """直接运行时的演示函数"""
    notes = create_demo_notes()
    report = format_notes_as_report(notes)

    print("=== 原始报告 ===")
    print(report)
    print()

    # 演示高亮
    sample = notes[0].title + " — " + notes[0].content
    highlighted = highlight_keyword(sample)
    print("=== 高亮示例 ===")
    print(highlighted)


if __name__ == "__main__":
    run_notes_demo()