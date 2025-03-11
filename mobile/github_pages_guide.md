# 使用GitHub Pages部署番茄钟PWA并转换为Android应用

本指南将帮助您将番茄钟PWA应用部署到GitHub Pages，然后使用PWA Builder将其转换为Android应用。

## 第一步：创建GitHub仓库

1. 登录您的GitHub账号（如果没有，请先在[GitHub](https://github.com)注册）
2. 点击右上角的"+"按钮，选择"New repository"
3. 仓库名称填写为：`tomato-timer-pwa`（或您喜欢的其他名称）
4. 描述可以填写："番茄时钟PWA应用"
5. 选择"Public"（公开）
6. 点击"Create repository"创建仓库

## 第二步：上传PWA文件到GitHub

### 方法一：使用Git命令行（推荐）

1. 在您的计算机上打开终端
2. 导航到番茄钟PWA项目的mobile文件夹：
   ```bash
   cd /Volumes/storage/trae/tomato/mobile
   ```
3. 初始化Git仓库：
   ```bash
   git init
   ```
4. 添加所有文件到暂存区：
   ```bash
   git add .
   ```
5. 提交更改：
   ```bash
   git commit -m "初始提交番茄钟PWA应用"
   ```
6. 添加远程仓库（替换`YOUR_USERNAME`为您的GitHub用户名）：
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/tomato-timer-pwa.git
   ```
7. 推送到GitHub：
   ```bash
   git push -u origin master
   ```

### 方法二：直接在GitHub网页上传

1. 进入您刚创建的GitHub仓库页面
2. 点击"Add file" > "Upload files"
3. 将您的PWA文件夹中的所有文件拖拽到上传区域
4. 添加提交信息："初始提交番茄钟PWA应用"
5. 点击"Commit changes"完成上传

## 第三步：配置GitHub Pages

1. 在您的仓库页面，点击"Settings"（设置）
2. 在左侧菜单中，找到并点击"Pages"（页面）
3. 在"Source"（源）部分，选择"Deploy from a branch"
4. 在"Branch"（分支）下拉菜单中，选择"master"（或"main"）分支，文件夹选择"/ (root)"，然后点击"Save"（保存）
5. 等待几分钟，GitHub会自动部署您的网站
6. 部署完成后，您会在页面顶部看到一个绿色的成功消息，其中包含您的网站URL，格式通常为：
   `https://YOUR_USERNAME.github.io/tomato-timer-pwa/`

## 第四步：验证PWA功能

1. 在浏览器中访问您的GitHub Pages URL
2. 测试PWA的各项功能是否正常工作
3. 确认Service Worker是否正确注册（可以在浏览器开发者工具的Application标签页中查看）
4. 测试离线功能是否正常

## 第五步：使用PWA Builder转换为Android应用

1. 访问[PWA Builder网站](https://www.pwabuilder.com/)
2. 在首页输入您的GitHub Pages URL（例如：`https://YOUR_USERNAME.github.io/tomato-timer-pwa/`）
3. 点击"开始"按钮，PWA Builder将分析您的PWA
4. 分析完成后，查看报告并修复任何潜在问题
5. 点击"生成包"按钮
6. 选择"Android"选项
7. 根据需要自定义应用设置（如应用名称、图标等）
8. 点击"下载"按钮获取生成的APK文件
9. 将APK文件安装到您的Android设备上

## 注意事项

1. 确保您的`manifest.json`中的`start_url`设置正确，对于GitHub Pages部署，可能需要修改为相对路径
2. 如果您的PWA使用了绝对路径引用资源，可能需要更新为相对路径
3. 确保Service Worker正确缓存了所有必要的资源
4. 如果您的PWA依赖后端API，请确保API端点可以从GitHub Pages访问（考虑CORS问题）

## 故障排除

1. 如果页面无法加载，检查GitHub Pages是否已成功部署
2. 如果PWA功能不正常，检查Service Worker是否正确注册
3. 如果PWA Builder分析失败，检查您的manifest.json和Service Worker配置
4. 如果生成的APK无法安装，确保您的Android设备允许安装来自未知来源的应用

## 更新应用

当您需要更新应用时，只需将更新后的文件推送到GitHub仓库，GitHub Pages会自动更新您的网站。然后，您可以再次使用PWA Builder生成新版本的APK。