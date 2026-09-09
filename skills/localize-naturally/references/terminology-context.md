# Contextual terminology

相同拼写可以指不同概念；同一概念的词形又可以随语法变化。先记录含义，再选择译词。不要因为英文一样就合并两个翻译键。

每个需要维护的条目记录：

- semantic_id：稳定概念，如 meal.log.action / meal.log.entry / meal.log.history。
- meaning、surface、example：动作/对象/状态、使用位置和一句上下文；能定位时记录资源key。
- locale、region、term：各语言对应形式，含必要的性、数、格或适用语境。
- protected / rejected：不可译品牌、保留标识符、已拒绝用法及原因。
- status：existing（当前资源用法，未经本轮语言审定）、candidate（待审候选）、approved（有真实批准依据）、deprecated（已替代）。
- evidence、reviewed_at、reviewer：源文件/用户决定/真实语言审校依据和日期；没有真人审核就不填写“native reviewed”。

源文件中的现有译文可提取成existing索引，以便后续不重新猜词；不能因此自动成为approved。只填本轮有证据的内容，不编造其他语言“已批准”译法。

语法允许变形；品牌保留、术语含义与产品事实不随变形改变。术语变更只更新有关surface；不因字符串一致全局替换。

高频词先覆盖记录动作/一条记录/历史集合、热量估算、营养估算、可用次数。订阅、额度、隐私等事实须查当前实现后再产生译文，不能从旧术语反推权益。
