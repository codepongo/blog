zanders3json
=================

[https://github.com/zanders3/json](https://github.com/zanders3/json)是一个C#实现的json库，只有几百行代码，为了简便牺牲了效率（No JIT Emit support to parse structures quickly）。


## 接口 ##


* 将json字符串解析成c#中的T类型


<pre data-language="C#">
T TinyJson.JSONParser.FromJson< T >(this string json)
</pre>

* 将C#的object导出成json格式的字符串

<pre data-language="C#">
string TinyJson.JSONWriter.ToJson(this object item)
</pre>

## json结构与C#的对应关系 ##

* object应设为c#中的dictionary`<string,object>`或object；

* array映射为ArrayList；number映射为int，float或double；

* string还是string；boolean还是boolean。


## 实现思路##
如果是基本数据类型则直接返回，如果是容器类型则以递归的方式根据不同类型调用不同方法进行解析和序列化。


## 示例 ##


<pre data-language="C#">
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using TinyJson;
namespace TinyJsonTester
{
    class Program
    {
        static void Main(string[] args)
        {
            object json = new Dictionary< string, object >
            {
                {"string", "" },
                {"number", new Dictionary< string, object > {
                                {"int",0 },
                                {"float", 0.1f },
                                {"double", 0.0001 }
                            }
                },
                {"array", new ArrayList {
                                    0,
                                    "0",
                                    null,
                                    true
                                }
                }
            };
            string jsonText = JSONWriter.ToJson(json);
            Console.WriteLine(jsonText);
            Dictionary< string, object > root = JSONParser.FromJson< Dictionary< string, object > > (jsonText);
            string stringValue = (string)root["string"];
            //Dictionary< string, object > number = (Dictionary< string, object >)root["number"];
            float f = (float)(double)((Dictionary< string, object >)root["number"])["float"];
            //List< object > array = (List< object >)root["array"];
            int zero = (int)(((List< object >)root["array"])[0]);
            Console.WriteLine($"{root}, {stringValue}, {f} , {zero}");
        }
    }
}
</pre>
