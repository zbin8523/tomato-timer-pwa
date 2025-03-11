# 番茄时钟 PWA 转 Android 应用指南

本文档将指导您如何将番茄时钟 PWA (渐进式 Web 应用) 转换为可安装的 Android 应用。

## 准备工作

我们已经完成了以下准备工作：

1. 创建了完整的 PWA 应用，包括：
   - 完整的 manifest.json 配置
   - 注册并配置了 service-worker.js
   - 创建了各种尺寸的应用图标
   - 确保应用可以离线工作

2. 测试了 PWA 功能，确保在浏览器中可以正常工作

## 将 PWA 转换为 Android 应用的方法

### 方法一：使用 PWA Builder（推荐，最简单）

1. 访问 [PWA Builder 网站](https://www.pwabuilder.com/)
2. 在首页输入您的 PWA 网址（如果您已将此 PWA 部署到网络上）
3. 点击"开始"按钮，PWA Builder 将分析您的 PWA
4. 分析完成后，点击"生成包"按钮
5. 选择"Android"选项
6. 下载生成的APK文件
7. 将APK文件安装到您的Android设备上

### 方法二：使用第三方在线转换服务

#### 1. GoNative.io

1. 访问 [GoNative 网站](https://gonative.io/)
2. 输入您的PWA网址
3. 填写应用基本信息（名称、图标等）
4. 选择需要的功能（如推送通知、地理位置等）
5. 点击"构建我的应用"按钮
6. 下载生成的APK文件并安装到设备上

#### 2. AppMaker

1. 访问 [AppMaker 网站](https://appmaker.xyz/)
2. 注册并登录账号
3. 创建新项目，选择"Web应用转换"
4. 输入您的PWA网址
5. 自定义应用外观和功能
6. 生成并下载APK文件

### 方法三：使用Capacitor或Cordova框架

如果您有一定的开发经验，可以考虑使用以下框架：

#### 1. Capacitor

1. 安装Capacitor：`npm install @capacitor/core @capacitor/android`
2. 初始化项目：`npx cap init [应用名称] [应用ID]`
3. 添加Android平台：`npx cap add android`
4. 复制您的PWA文件到www文件夹
5. 同步项目：`npx cap sync`
6. 使用Android Studio打开生成的Android项目：`npx cap open android`
7. 在Android Studio中构建APK

#### 2. Cordova

1. 安装Cordova：`npm install -g cordova`
2. 创建项目：`cordova create [项目文件夹] [应用ID] [应用名称]`
3. 添加Android平台：`cordova platform add android`
4. 将您的PWA文件复制到www文件夹
5. 构建应用：`cordova build android`
6. 在`platforms/android/app/build/outputs/apk/debug`目录找到生成的APK文件

### 方法四：使用Bubblewrap (TWA)

1. 安装Bubblewrap CLI：`npm install -g @bubblewrap/cli`
2. 初始化项目：`bubblewrap init --manifest=[您的PWA网址]/manifest.json`
3. 构建APK：`bubblewrap build`
4. 在生成的目录中找到APK文件并安装