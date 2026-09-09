# Locale profiles

只读当前任务涉及的语言。这里提供 12 个语言与地区的起始档案，不限定项目支持的语言集合。项目扩展语言时同时补档案，不静默回退英文。

地区、称呼、数字系统、货币、历法和服务可用性分别判断；脚本相同不等于地区相同。

| 资源 locale | 地区／用途基线 | 专项档案 |
| --- | --- | --- |
| `en` | English — United States | [en](locales/en.md) |
| `zh-Hans` | 简体中文 — 中国大陆用语 | [zh-Hans](locales/zh-Hans.md) |
| `zh-Hant` | 繁體中文 — 台灣用語 | [zh-Hant](locales/zh-Hant.md) |
| `ja` | 日本語 — 日本 | [ja](locales/ja.md) |
| `ko` | 한국어 — 대한민국 | [ko](locales/ko.md) |
| `es` | Español — UI neutral; tienda España | [es](locales/es.md) |
| `fr` | Français — France par défaut | [fr](locales/fr.md) |
| `de` | Deutsch — Deutschland | [de](locales/de.md) |
| `pt-BR` | Português — Brasil | [pt-BR](locales/pt-BR.md) |
| `it` | Italiano — Italia | [it](locales/it.md) |
| `ru` | Русский — русскоязычный интерфейс | [ru](locales/ru.md) |
| `ar` | العربية — فصحى معاصرة متعددة المناطق | [ar](locales/ar.md) |

## How to use

1. 按项目真实 locale 集合选取；en-US→en、de-DE→de、ja-JP→ja 等只有在项目映射已确认后才作为资源别名。zh-CN→zh-Hans、zh-TW→zh-Hant不表示其他繁体地区已被覆盖。
2. 每个语言档案与项目术语共同使用。用户既有判断、目标OS文案和已审定术语优先于外部项目习惯。
3. 语言档案的审校信号不是禁词或自动替换规则。区分确定错误、可选风格优化、事实／语境待确认。可接受同义词不当错误。
4. 需要新增或变更术语时读取 [terminology-context.md](terminology-context.md)。校验skill行为时读取 [locale-evaluation.md](locale-evaluation.md)。
5. 来源按文件与规则判断：专用skill、社区指南、标准各有用途。仓库名称、星数和自报分数都不证明语言质量；不引入来源中的品牌事实、授权流程或整套工具链。

## Research coverage and rejected guidance

2026-09-08：逐种检索了GitHub skill；德/日已在同一任务前段检索。法语与西语未找到值得优先采用的独立自然化skill，改用真实项目语言指南；pt-BR专项skill偏HTML拼装且有片段化、alt与locale映射问题，未采用实现。繁体中文以MozTW台湾指南补齐。每份档案标明实际读过的来源，未把搜索命中当审阅完成。

- 通用结构参考：[FormatJS translate](https://github.com/formatjs/formatjs/blob/4611a1ff618888d6e76c0f2ae0a9d400dc033b78/.agents/skills/translate/SKILL.md) 与 [localization-review](https://github.com/formatjs/formatjs/blob/4611a1ff618888d6e76c0f2ae0a9d400dc033b78/.agents/skills/localization-review/SKILL.md)。吸收消息上下文、参数类型与语法结构、术语含义和证据分类；React专属实现不套入Swift/Android。
- 韩语来源将部分不确定表达改成断言：不采用；不得增强健康、AI或付款承诺。
- Mozilla阿拉伯语README含斯瓦希里语内容，排除整份；方向与数字差异使用W3C Arabic Layout，复数用CLDR。
- 法语Mozilla入口指向的wiki读取失败，未当作已读资料；使用实际读到的Zulip指南并排除英文大小写约定。
- 不把“原文相同”视为“语境相同”；不以一套敬称、句号、复数分支或品牌规则覆盖所有地区。
