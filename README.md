# NLog for IronPython

## 概要

このプロジェクトは、.NETのロギングライブラリである[NLog](https://nlog-project.org/)を、IronPythonから利用するためのパッケージを生成するサンプルです。

## 前提条件

*   **.NET 8 SDK**
*   **Visual Studio 2022（slnxが開けること）**
*   **IronPython 3.4**

## セットアップ手順

1.  `ExampleOfNLog.slnx` を Visual Studioで開きます。

2.  **NuGet パッケージの復元:**
    ソリューションを開くと、必要な NuGet パッケージ (NLog) が自動的に復元されます。
    
    もし復元されない場合は、Visual Studio上で［表示］→［ターミナル］として以下を実行してください。    `dotnet add package` をcsprojファイルのあるフォルダで実行することがポイントです。

    ```shell
    cd ExampleOfNLog
    dotnet add package NLog --version 5.3.4 --source https://api.nuget.org/v3/index.json
    ```

3.  ソリューションをビルドします。（ビルド構成は `Debug` または `Release` を選択）

4.  IronPythonのインストールフォルダにある `Lib` フォルダ内に、`nlog` という名前の新しいフォルダを作成します。（例: `C:\IronPython34\Lib\nlog`）

5.  ビルドで生成された下記のアセンブリとファイルを、先ほど作成した `nlog` フォルダにコピーします。
    *   **コピー元**: `bin\Debug\net8.0-windows\`
    *   **コピーするファイル/フォルダ**:
        *   `example.dll`
        *   `NLog.dll`
        *   `__init__.py`
        *   `examples` フォルダ（このフォルダごとコピーします）

6.  実行スクリプトと同じ階層に `NLog.config` を配置します。デフォルトでは、ログはデスクトップに `YYYY-MM-DD.log` というファイル名で保存されます。

## サンプルスクリプトの使用方法

以下のコードで、IronPythonからNLogのロギング機能を実行できます。

```python
# 'nlog' パッケージから 'examples' モジュールをインポートし、
# さらにその中の 'sample' スクリプトをインポート
from nlog.examples import sample

# sampleスクリプト内のrun()関数を実行
sample.run()
```