# Example of "NLog" (for 64bit)

Example of "NLog" in Ironpython script.  
The library of C# is used. Requires VisualStudio 2017 or higher.

## File

* "ExampleOfNLog.sln"
  * To install "NLog".
  * To generate "nlog" package.

## Notes on execution

* Open "ExampleOfNLog.sln".
* Install "NLog" with NuGet.
* Build.
* Copy the "x64/debug/nlog" or "x64/release/nlog" folder to IronPython's "Lib" folder.
* Environment variable "IRONPYTHON_HOME" is required. It is the installation location of IronPython.
* "example.py" and "example.exe" are example program.
  * After copying "NLog.config" to "c:/tmp/" folder, do the following.

```
import nlog
import example

example.RunExample()
```