# Twitter API Maneger
このプログラムはTwitter APIを使用したTwitter自動管理アプリです。  
プログラムはFlaskで書かれており、フロントサーバーとbotサーバーに分かれています。

# フロントサーバー(twitter_maneger)
フロントサーバーtwitter_manegerはFlaskで開発されたWebアプリケーションです。  
twitter_manegerはユーザー管理機能と管理者権限機能を持っており、管理者の許可なくユーザーを作成することはできません。  
また、TwiiterAPI情報を登録する画面をもっており、API情報や自動メッセージ・最大送信数などを登録できます。

# APIサーバー（twiiter_bot）
APIサーバーtwiiter_botはリクエストに応じてBotの可動と制御を行います。（実装中）

