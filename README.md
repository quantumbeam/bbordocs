## ドキュメント構造
- トップページは/jaにリダイレクトされる仕様です。


## ソースファイル
- ドキュメントはすべてdocs/にあります。
- 基本的に文章はSphinxのsubstituteディレクティブを使って、jaまたはenで置換してビルドします。日本語テキストは/vars/ja.rstに、英語テキストは/vars/en.rstに書きます。
- en.rstはtranslate.pyを使うと自動で埋まります。


## ビルド
- ソースファイルを更新してプッシュすると、Github Actionsによるビルドが起こり、HTMLファイルがbuiltブランチに生成され、自動で[Github Pages](https://quantumbeam.github.io/bbordocs)が更新されます。
- ローカルでビルドするときは、```(uv run) python auto-rebuild-reload.py```とすることでhttp://localhost:3000 に日本語ページが立ち上がり、ソースファイルを更新すると自動ビルドが走り自動で反映されます。
- 手動で更新するときは以下のコマンドになります。
    ```bash
    (uv run) make [ja|en]
    (uv run) python http.server -d _build/ja 3000
    ```

