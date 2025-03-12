# 番茄时钟 PWA 转 Android 应用指南

本文档将指导您如何使用 PWA Builder 在线服务将番茄时钟 PWA (渐进式 Web 应用) 转换为可安装的 Android 应用。

## 使用 PWA Builder 打包 Android 应用

### 准备工作

确保您已经获取了项目根目录中的 `pwa.zip` 文件，该文件包含了完整的 PWA 应用代码和资源，包括：
- manifest.json 配置文件
- service-worker.js 服务工作线程
- 应用图标和其他资源文件
- HTML、CSS 和 JavaScript 文件

### 详细步骤

1. 访问 PWA Builder 网站
   - 打开浏览器，访问 [PWA Builder](https://www.pwabuilder.com/)
   - 在首页点击 "Start" 按钮

2. 上传 PWA 文件
   - 在 PWA Builder 页面上，选择 "Package your PWA" 选项
   - 点击 "Upload a .zip file" 按钮
   - 选择并上传项目根目录中的 `pwa.zip` 文件
   - 等待文件上传完成和分析过程

3. 选择 Android 平台
   - 在平台选择页面，找到 "Android" 选项
   - 点击 "Build" 按钮开始构建过程
   - 根据提示配置应用信息（如有需要）：
     * 应用名称
     * 包名
     * 版本号
     * 图标（已包含在zip文件中）

4. 下载 APK 文件
   - 构建完成后，系统会自动生成 APK 文件
   - 点击 "Download" 按钮下载生成的 APK 文件
   - 将文件保存到您的计算机上

5. 安装到 Android 设备
   - 将 APK 文件传输到 Android 设备
   - 在设备上找到并点击 APK 文件
   - 按照提示完成安装过程
   - 注意：可能需要在设备设置中允许「安装未知来源应用」

### 注意事项

1. 确保 `pwa.zip` 文件包含了所有必要的文件和资源
2. 上传文件大小可能有限制，请确保文件大小适中
3. 生成的 APK 文件可能需要签名才能在 Google Play 商店发布
4. 如果遇到问题，可以查看 PWA Builder 的帮助文档或联系支持团队

### 优势

- 无需编程知识
- 操作简单直观
- 快速获得可安装的 Android 应用
- 保留 PWA 的所有功能
- 可以离线使用

如果您在转换过程中遇到任何问题，请参考 [PWA Builder 文档](https://docs.pwabuilder.com/) 或在项目 Issues 中提出问题。