# GitHub身份验证指南

## 问题说明

您在尝试推送代码到GitHub时遇到了以下错误：

```
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/zbin8523/tomato-timer-pwa.git/'
```

这是因为GitHub从2021年8月13日起已停止支持使用密码进行身份验证，现在需要使用个人访问令牌(Personal Access Token)来代替密码。

## 解决方案

### 第一步：创建个人访问令牌(Personal Access Token)

1. 登录您的GitHub账号
2. 点击右上角的头像，选择「Settings」(设置)
3. 在左侧菜单栏中，滚动到底部并点击「Developer settings」(开发者设置)
4. 在左侧菜单中，点击「Personal access tokens」(个人访问令牌)，然后选择「Tokens (classic)」
5. 点击「Generate new token」(生成新令牌)，然后选择「Generate new token (classic)」
6. 在「Note」(备注)字段中，输入一个描述性名称，如「Tomato Timer PWA」
7. 选择令牌的有效期限（建议选择30天或更长时间）
8. 在「Select scopes」(选择范围)部分，勾选「repo」(仓库)选项，这将授予对您仓库的完全访问权限
9. 滚动到底部，点击「Generate token」(生成令牌)按钮
10. **重要：** 立即复制生成的令牌！这是您唯一能够看到令牌的机会，离开页面后将无法再次查看完整的令牌

### 第二步：使用个人访问令牌进行身份验证

#### 方法一：在推送时使用令牌

当您执行`git push`命令时，Git会要求您输入用户名和密码。输入您的GitHub用户名，然后在密码字段中粘贴您的个人访问令牌。

```bash
git push -u origin main
# 当提示输入密码时，粘贴您的个人访问令牌
```

#### 方法二：更新远程URL以包含令牌

您可以更新远程仓库的URL，使其包含您的个人访问令牌：

```bash
git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/tomato-timer-pwa.git
```

请将以下内容替换为您的实际信息：
- `YOUR_USERNAME`: 您的GitHub用户名
- `YOUR_TOKEN`: 您的个人访问令牌

#### 方法三：配置凭据管理器

您可以使用Git的凭据管理器来存储您的凭据：

```bash
# 启用凭据存储
git config --global credential.helper store

# 下次推送时，输入您的用户名和个人访问令牌作为密码
git push -u origin main
```

输入一次后，您的凭据将被保存，以后就不需要再次输入。

### 第三步：推送您的代码

配置好身份验证后，再次尝试推送您的代码：

```bash
git push -u origin main
```

## 注意事项

1. 个人访问令牌与密码一样重要，请妥善保管，不要分享给他人
2. 如果您忘记了令牌，可以在GitHub中生成一个新的令牌，并更新您的凭据
3. 为了安全起见，建议为令牌设置合理的有效期限
4. 如果您使用的是公共计算机，请不要使用`credential.helper store`选项

## 其他身份验证方法

除了个人访问令牌外，GitHub还支持以下身份验证方法：

1. **SSH密钥**：这是一种更安全的身份验证方式，特别适合开发人员
2. **GitHub CLI**：GitHub的命令行工具，提供了简化的身份验证流程

如果您需要关于这些方法的更多信息，请参考[GitHub官方文档](https://docs.github.com/en/authentication)。