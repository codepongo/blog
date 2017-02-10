Latex 数学符号和公式
==================================
TeX是排版引擎，LaTeX是宏包。


出版的第一步是作者将他们的手稿交给出版公司，然后由图书设计者
来决定整本书的版面形式（包括栏宽、字体、标题前后的间距…………）。图
书设计者会把他的排版说明写进手稿里，一起交给排版者，排版者最后根
据这些说明完成这本书的排版工作。
在LaTeX环境中，LaTeX代替了图书设计者的角色，TeX 则是它的排版者。

## 数学符号和公式（ mathematics ）


不允许有空行，每个公式中只能有一个段落。


每个字符都将被看作是一个变量名并以此来排版。如果你希望在公式
中出现普通的文本（使用正体字并可以有空格），那么你必须使用命
令 \textrm{...} 来输入这些文本。


数学模式中的命令仅对其后面第一个字符起作用。所以，如果你
希望某一命令作用于多个字符的话，那么你就必须将它们放置于括号
中：{...}。


小写希腊字母（Lowercase Greek letters ）的输入命令为：\alpha,
\beta, \gamma, ...，相应地，大写形式的输入命令为：\Gamma, \Delta,
...。


指数和下标可用 ^ 和 _ 后加相应的字符来实现。


平方根（square root）的输入命令为：\sqrt，n 次方根相应地为:
\sqrt[n]。方根符号的大小由 LaTeX自动加以调整。
也可用 \surd 仅给出符号。


<img alt="" src="http://latex.codecogs.com/png.latex?\sqrt[3]3">

命令 \overline 和 \underline 在表达式的上、下方画出水平线。


<img alt="" src="http://latex.codecogs.com/png.latex?\overline{a+b+c}" />




命令 \overbrace 和 \underbrace 在表达式的上、下方给出一水平的
大括号。


<img alt="" src="http://latex.codecogs.com/png.latex?\underbrace{a+b+c}" />



向量（Vectors）通常用上方有小箭头（arrow symbols）的变量表
示。这可由 \vec 得到。另两个命令 \overrightarrow 和 \overleftarrow
在定义从 A 到 B 的向量时非常有用。




用命令 \cdot 将圆点符表示出来


<img alt="" src="http://latex.codecogs.com/png.latex?1+2+3+\cdot\cdot\cdot+n" />


重要函数名用于排版


\arccos \cos \csc \exp \ker \limsup \min
\arcsin \cosh \deg \gcd \lg \ln \Pr
\arctan \cot \det \hom \lim \log \sec
\arg \coth \dim \inf \liminf \max \sin
\sinh \sup \tan \tanh


排版模函数（modulo function）：\bmod \pmod


<img alt="" src="http://latex.codecogs.com/png.latex?a\bmod{b}\qquad%20a\pmod{b}" />


分数（fraction）使用 \frac{...}{...} 排版


排版二项系数或类似的结构可以使用命令 {... \choose ...} 或
{... \atop ...}


<img alt="" src="http://latex.codecogs.com/png.latex?{n%20\choose%20k}\qquad%20{x%20\atop%20y+2}" />

对于二元关系，将符号堆在一起可能更有用。\stackrel 将第一项中
的符号以上标大小放在处于正常位置的第二项上。


<img alt="" src="http://latex.codecogs.com/png.latex?\stackrel{!}{=}" />

 
积分运算符（integral operator）用\int来生成。求和运算符（sum
operator）由 \sum 生成。乘积运算符（product operator）由 \prod 生
成。上限和下限用 ^ 和 _ 来生成，类似于上标和下标 4 。


圆括号和方括号可以用相应的键输入。花括号
用 \{。


某些情况下有必要手工指出数学分隔符的正确大小，这可以使用命令
\big, \Big, \bigg 及 \Bigg 作为大多数分隔符命令的前缀。


<img alt="" src="http://latex.codecogs.com/png.latex?$\big(\Big(\bigg(\Bigg($\quad$\big\}\Big\}\bigg\}\Bigg\}$\quad$\big\|\Big\|\bigg\|\Bigg\|$" />



空格和分行都将被忽略。 所有的空格或是由数学表达式逻辑的衍生，
或是由特殊的命令如 \,，\quad 或 \qquad 来得到。
\, 对应于 3/18 quad, 
\: 对 应于 4/18 quad, 
\; 对应于 5/18 quad。


脱离的空格符号 \ˆ 生成中等大小的空格。
\quad 和 \qquad  产生大空格。
\quad 的大小对应于目前字体中字符 ‘M’ 的宽度。
\! 命令生成负空格  -3/18 quad。


将三个圆点（three dots）输入公式可以使用几种命令。\ldots 将点
排在基线上。\cdots 将它们设置为居中。除此之外，可用 \vdots 命令使
其垂直，而用 \ddots 将得到对角型（diagonal dots）。


使用 array 环境来排版数组（arrays）


<img alt="" src="http://latex.codecogs.com/png.latex?\left(%20\begin{array}{ccc}%20x_{11}%20&%20x_{12}%20&%20\ldots%20\\%20x_{21}%20&%20x_{22}%20&%20\ldots%20\\%20\vdots%20&%20\vdots%20&%20\ddots%20\end{array}%20\right)" />



我们无法看到幻影（phantom），但是它们在许多人印象中仍然会占据
一些空间。垂直对齐文本时使用 ^ 和 _, 我们也可以使用这些作一些有趣的空格技巧。


<img alt="" src="http://latex.codecogs.com/png.latex?{}^{12}_{\phantom{1}6}\textrm{C}%20\qquad%20\textrm{versus}%20\qquad%20{}^{12}_{6}\textrm{C}" />


## 引用
* 摘自《一份不太简短的 LaTeX2e介绍》
