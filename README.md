# F-kLang

被 Swift 编译器气到之后做的整活项目。

把 Swift 关键字换成 f-k 风格的同义词，用正则转译回标准 Swift，再交给 swiftc 编译成机器码。

## 语法对照

| F-kLang | Swift |
|---------|-------|
| fuck    | func  |
| damn    | let   |
| shit    | var   |
| screw   | print |
| whatever| if    |
| otherwise| else |
| again   | while |
| bullshit| return|
| ass     | Int   |
| assf    | Double|
| words   | String|
| truth   | Bool  |

## 快速开始

```bash
chmod +x build.sh
./build.sh examples/hello.fuck