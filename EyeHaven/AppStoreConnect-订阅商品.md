# App Store Connect：美国英文版订阅（一次性）

本地已有 `Products.storekit`（Xcode 调试用）。真机收费前，请在苹果后台建同样商品。

**美国价格（与中文版 ¥9.9 / ¥78 不同）：**

| 参考名称 | 产品 ID（必须一字不差） | 时长 | 美国价格 |
|----------|-------------------------|------|----------|
| Learning Pass Monthly | `com.eyehaven.en.sub.monthly` | 1 个月 | **$3.99** |
| Learning Pass Yearly | `com.eyehaven.en.sub.yearly` | 1 年 | **$24.99** |

## 步骤

1. 打开 [App Store Connect](https://appstoreconnect.apple.com) → 英文版 App → **订阅**。
2. 新建订阅组，名称：`Guangguang Learning Pass`。
3. 在组里新建两个**自动续订**，产品 ID 与上表一致。
4. 价格选美国档位：$3.99 / 月，$24.99 / 年（其他国家可按同档或另调）。
5. 英文显示名：
   - 月：`Learning Pass Monthly`
   - 年：`Learning Pass Yearly`
6. 描述写清：**Eye break timer, rest, and check-in stay free. Pass = story updates + nicer voices + weekly parent note.**
7. 提交审核前，把订阅随 App 版本一起送审。

建好后，App 能拉到商品就会按免费试听额度限制；建好之前不锁库。

中文版仍用 ¥9.9 / ¥78，两边商店定价分开设，不要混成同一套人民币价。
