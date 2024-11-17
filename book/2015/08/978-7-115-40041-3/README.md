# 函数式编程思维

- 作者：Neal Ford
- 出版社：人民邮电出版社
- 出版时间：2015-08
- ISBN：978-7-115-40041-3
- 豆瓣：https://book.douban.com/subject/26587213
- 封面：

![](../../../../image/2024/11/978-7-115-40041-3/cover.jpg)

# 第 1 章 为什么

学习一种全新的编程范式，困难并不在于掌握新的语言。毕竟能拿起这本书的读者，学过的编程语言少说也有一箩筐——语法不过是些小细节罢了。真正考验人的，是怎么学会用另一种方式去思考。

## 1.1 范式转变

题目：读入一个文本文件，确定所有单词的使用频率并从高到低排序，打印出所有单词及其频率的排序列表

```java
// 例 1-1 词频统计的 Java 实现
public class Words {
	private Set < String > NON_WORDS = new HashSet < String > () {
		{
			add("the");
			add("and");
			add("of");
			add("to");
			add("a");
			add("i");
			add("it");
			add("in");
			add("or");
			add("is");
			add("d");
			add("s");
			add("as");
			add("so");
			add("but");
			add("be");
		}
	};
	public Map wordFreq(String words) {
		TreeMap < String, Integer > wordMap = new TreeMap < String, Integer > ();
		Matcher m = Pattern.compile("\\w+").matcher(words);
		while(m.find()) {
			String word = m.group().toLowerCase();
			if(!NON_WORDS.contains(word)) {
				if(wordMap.get(word) == null) {
					wordMap.put(word, 1);
				}
				else {
					wordMap.put(word, wordMap.get(word) + 1);
				}
			}
		}
		return wordMap;
	}
}
```

Java 8 新增了 Stream API 和以 lambda 块方式实现的高阶函数

```java
// 例 1-2 词频统计的 Java 8 实现
private List < String > regexToList(String words, String regex) {
	List wordList = new ArrayList < > ();
	Matcher m = Pattern.compile(regex).matcher(words);
	while(m.find()) wordList.add(m.group());
	return wordList;
}
public Map wordFreq(String words) {
	TreeMap < String, Integer > wordMap = new TreeMap < > ();
	regexToList(words, "\\w+").stream().map(w - > w.toLowerCase()).filter(w - > !NON_WORDS.contains(w)).forEach(w - > wordMap.put(w, wordMap.getOrDefault(w, 0) + 1));
	return wordMap;
}
```

Clojure 语言（ http://clojure.org ）的发明人 Rich Hickey 在 Strange Loop 会议上做过一堂题为“Simple Made Easy” 的 演 讲（ http://www.infoq.com/presentations/Simple-Made-Easy ），他翻出了一个已经很少用到的老词——“交织”（complect）：穿插缠绕地合为一体，使错综复杂。命令式编程风格常常迫使我们出于性能考虑，把不同的任务交织起来，以便能够用一次循环来完成多个任务。而函数式编程用 `map()`、`filter()` 这些高阶函数把我们解放出来，让我们站在更高的抽象层次上去考虑问题，把问题看得更清楚。

## 1.2 跟上语言发展的潮流

如果我们关注各种语言的发展情况就会发现，所有的主流语言都在进行函数式方面的扩充。

## 1.3 把控制权让渡给语言/运行时

> 人生苦短，远离 malloc

随着时间的推移，开发者们越来越多地把乏味单调的任务托付给语言和运行时。对于我日常编写的应用程序类型来说，失去对内存的直接控制没什么可惋惜的，放弃这些反而让我能够专注于更重要的问题。Java 接管内存分配减轻了我们的负担，函数式编程语言让我们用高阶抽象从容取代基本的控制结构，也有着同样的意义。

## 1.4 简洁

*Working with Legacy Code* 的作者 Michael Feathers 用寥寥数语（ https://twitter.com/mfeathers/status/29581296216 ）捕捉到了函数式抽象和面向对象抽象的关键区别：

> 面向对象编程通过封装不确定因素来使代码能被人理解；函数式编程通过尽量减少不确定因素来使代码能被人理解。——Michael Feathers

请回想一下你熟悉的封装、作用域、可见性等面向对象编程（OOP）构造，这些机制的存在意义，都是为了精细地控制谁能够感知状态和改变状态。

而当涉及多线程的时候，对状态的控制就更复杂了。这些机制就属于 Michael Feathers 所谓的“不确定因素”（movingparts）。

大多数函数式语言在这个问题上采取了另一种做法，它们认为，与其建立种种机制来控制可变的状态，不如尽可能消灭可变的状态这个不确定因素。其立论的根据是这样的：假如语言不对外暴露那么多有出错可能的特性，那么开发者就不那么容易犯错。

在面向对象的命令式编程语言里面，重用的单元是类和类之间沟通用的消息，这些都可以用类图（class diagram）来表述。这个领域的代表性著作《设计模式：可复用面向对象软件的基础》（*Design Patterns: Elements of Reusable Object-Oriented Software，作者 ErichGamma、Richard Helm、Ralph Johnson、John Vlissides*）就在每一个模式的说明里都附上了至少一幅类图。

OOP 的世界提倡开发者针对具体问题建立专门的数据结构，相关的专门操作以“方法”的形式附加在数据结构上。

函数式语言提倡在有限的几种关键数据结构（如 list、set、map）上运用针对这些数据结构高度优化过的操作，以此构成基本的运转机构。开发者再根据具体用途，插入自己的数据结构和高阶函数去调整机构的运转方式。

函数式程序员喜欢用少数几个核心数据结构，围绕它们去建立一套充分优化的运转机构。面向对象程序员喜欢不断地创建新的数据结构和附属的操作，因为压倒一切的面向对象编程范式就是建立新的类和类间的消息。把所有的数据结构都封装成类，一方面压制了方法层面的重用，另一方面鼓励了大粒度的框架式的重用。函数式编程的程序构造更方便我们在比较细小的层面上重用代码。

# 第 2 章 转变思维

## 2.1 普通的例子

当垃圾收集成为主流，一下子将若干难以调试的错误类别连根拔起，程序员也因为运行时接管了复杂且容易出错的内存管理而获得解脱。函数式编程希望在算法编写上给予程序员同样的帮助，一方面程序员得以在更高的抽象层次上工作，另一方面运行时也有了执行复杂优化的自由空间。开发者从中获得的好处体现在更低的复杂性和更高的性能，这点与垃圾收集相同，不过，函数式编程对个人的影响更直接，因为它改变的是你的解答思路。


### 2.1.1 命令式解法

命令式编程是按照“程序是一系列改变状态的命令”来建模的一种编程风格

题目：将除去单字符条目之外的列表内容，放在一个逗号分隔的字符串里返回，且每个名字的首字母都要大写

```java
// 例 2-1 典型的公司业务处理例子

package com.nealford.functionalthinking.trans;
import java.util.List;
public class TheCompanyProcess {
	public String cleanNames(List < String > listOfNames) {
		StringBuilder result = new StringBuilder();
		for(int i = 0; i < listOfNames.size(); i++) {
			if(listOfNames.get(i).length() > 1) {
				result.append(capitalizeString(listOfNames.get(i))).append(",");
			}
		}
		return result.substring(0, result.length() - 1).toString();
	}
	public String capitalizeString(String s) {
		return s.substring(0, 1).toUpperCase() + s.substring(1, s.length());
	}
}
```

### 2.1.2 函数式解法

函数式编程将程序描述为表达式和变换，以数学方程的形式建立模型，并且尽量避免可变的状态。

```
// 例 2-2 伪代码表示的“公司业务处理过程”
listOfEmps
	-> filter(x.length > 1)
	-> transform(x.capitalize)
	-> convert(x + "," + y)
```

```scala
// 例 2-3 函数式的处理过程（Scala 实现）
val employees = List("neal", "s", "stu", "j", "rich", "bob", "aiden", "j", "ethan","liam", "mason", "noah", "lucas", "jacob", "jayden", "jack")

val result = employees
.filter(_.length() > 1)
.map(_.capitalize)
.reduce(_ + "," + _)
```

```java
// 例 2-4 Java 8 实现的处理过程

public String cleanNames(List < String > names) {
	if(names == null) return "";
	return names.stream().filter(name - > name.length() > 1).map(name - > capitalize(name)).collect(Collectors.joining(","));
}

private String capitalize(String e) {
	return e.substring(0, 1).toUpperCase() + e.substring(1, e.length());
}
```

```Groovy
// 例 2-5 Groovy 实现的处理过程
public static String cleanUpNames(listOfNames) {
	listOfNames
		.findAll { it.length() > 1 }
		.collect { it.capitalize() }
		.join ','
}
```

```Clojure
;; 例 2-6 Clojure 实现的处理过程
(defn process [list-of-emps]
	(reduce str (interpose ","
		(map s/capitalize (filter #(< 1 (count %)) list-of-emps)))))
```

```Clojure
;; 例 2-7 通过 thread-last 宏改善代码的可读性
(defn process2 [list-of-emps]
	(->> list-of-emps
		(filter #(< 1 (count %)))
		(map s/capitalize)
		(interpose ",")
		(reduce str)))
```

学会用更高层次的抽象来思考有什么好处？

1. 会促使我们换一种角度去归类问题，看到问题的共性
2. 让运行时有更大的余地去做智能的优化。有时候，在不改变最终输出的前提下，调整一下作业的先后次序会更有效率（例如减少了需要处理的条目）
3. 让埋头于实现细节的开发者看到原本视野之外的一些解决方案

```Scala
<!-- 例 2-8 Scala 实现的并行化处理过程 -->
val parallelResult = employees
.par
.filter(_.length() > 1)
.map(_.capitalize)
.reduce(_ + "," + _)
```

```Java
// 例 2-9 Java 8 实现的并行化处理过程
public String cleanNamesP(List < String > names) {
    if (names == null) return "";
    return names
        .parallelStream()
        .filter(n - > n.length() > 1)
        .map(e - > capitalize(e))
        .collect(Collectors.joining(","));
}
```

map、reduce、filter等函数式操作也存在类似的互利关系。Clojure下的Reducers扩展库（ http://dwz.cn/reducers-library ）就是一个绝佳的例子。其作者RichHickey以库的形式对Clojure语言进行了扩展，提供了新版本的vector和map实现（以及用来转换原版vector和map的新的fold函数），他的实现在内部运用Java的Fork/Join框架来完成对集合的并行处理。

> 多从结果着眼，少纠结具体的步骤。

## 2.2 案例研究：完美数的分类问题

古希腊数学家 Nicomachus 发明了一种自然数的分类方法，任意一个自然数都唯一地被归类为过剩数（abundant）、完美数（perfect）或不足数（deficient）。一个完美数的真约数（即除了自身以外的所有正约数）之和，恰好等于它本身。例如 6 是一个完美数，因为它的约数是 1、2、3，而 6 = 1 + 2 + 3；28 也是一个完美数，因为 28 = 1 + 2 + 4 + 7 + 14。

表2-1：自然数分类规则

|||
|:---:|---|
| 完美数 | 真约数之和 = 数本身 |
| 过剩数 | 真约数之和 > 数本身 |
| 不足数 | 真约数之和 < 数本身 |

实现中用到一个数学概念，真约数和（aliquot sum），其定义就是除了数本身之外（一个数总是它本身的约数），其余正约数的和。

### 2.2.1 完美数分类的命令式解法

```Java
// 例 2-10 完美数分类的 Java 实现
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
public class ImpNumberClassifierSimple {
    private int _number; // ➊
    private Map < Integer, Integer > _cache; // ➋
    public ImpNumberClassifierSimple(int targetNumber) {
        _number = targetNumber;
        _cache = new HashMap < > ();
    }
    public boolean isFactor(int potential) {
        return _number % potential == 0;
    }
    public Set < Integer > getFactors() {
        Set < Integer > factors = new HashSet < > ();
        factors.add(1);
        factors.add(_number);
        for (int i = 2; i < _number; i++)
            if (isFactor(i))
                factors.add(i);
        return factors;
    }
    public int aliquotSum() { // ➌
        if (_cache.get(_number) == null) {
            int sum = 0;
            for (int i: getFactors())
                sum += i;
            _cache.put(_number, sum - _number);
        }
        return _cache.get(_number);
    }
    public boolean isPerfect() {
        return aliquotSum() == _number;
    }
    public boolean isAbundant() {
        return aliquotSum() > _number;
    }
    public boolean isDeficient() {
        return aliquotSum() < _number;
    }
}
```

- ➊ 内部状态，存放待分类的目标数字
- ➋ 内部缓存，防止重复进行不必要的求和运算
- ➌ 计算“真约数和”aliquotSum，即正约数之和减去数字本身

### 2.2.2 稍微向函数式靠拢的完美数分类解法

```Java
// 例 2-11 稍微向函数式靠拢的完美数分类实现
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
public class NumberClassifier {
    public static boolean isFactor(final int candidate, final int number) { // ➊
        return number % candidate == 0;
    }
    public static Set < Integer > factors(final int number) { //  ➋
        Set < Integer > factors = new HashSet < > ();
        factors.add(1);
        factors.add(number);
        for (int i = 2; i < number; i++)
            if (isFactor(i, number))
                factors.add(i);
        return factors;
    }
    public static int aliquotSum(final Collection < Integer > factors) { // ➌
        int sum = 0;
        int targetNumber = Collections.max(factors);
        for (int n: factors) {
            sum += n;
        }
        return sum - targetNumber;
    }
    public static boolean isPerfect(final int number) {
            return aliquotSum(factors(number)) == number;
        } // ➍
    public static boolean isAbundant(final int number) {
        return aliquotSum(factors(number)) > number;
    }
    public static boolean isDeficient(final int number) {
        return aliquotSum(factors(number)) < number;
    }
}
```

- ➊ 众多方法都必须加上 `number` 参数，因为没有可以存放它的内部状态
- ➋ 所有方法都带 `public static` 修饰，因为它们都是 **纯函数**，并因此可以在完美数分类之外的领域使用
- ➌ 注意例中对参数类型的选取，尽可能宽泛的参数类型可以增加函数重用的机会
- ➍ 例子目前在重复执行分类操作的时候效率较低，因为没有缓存

在例 2-11 稍微向函数式风格靠拢的 `NumberClassifier` 里面，所有方法都是自足的、带 `public` 和 `static` 作用域的纯函数（即没有副作用的函数）。而由于类里面根本不存在任何内部状态，也就没有理由去“隐藏”任何一个方法。

面向对象系统里粒度最小的重用单元是类，开发者往往忘记了重用可以在更小的单元上发生

这一版的实现没有为求和结果设计缓存机制。缓存意味着持续存在的状态，可是这一版的实现根本没有可以放置状态的地方。例 2-11 对比例 2-10 相同功能的实现，效率上要低一些。这是因为失去了存放求和结果的内部状态，只好每次都重新计算。

### 2.2.3 完美数分类的Java 8实现

`lambda` 块是最令 Java 8 面目一新的改进，它其实就是高阶函数

```Java
// 例 2-12 完美数分类的 Java 8 实现
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import static java.lang.Math.sqrt;
import static java.util.stream.Collectors.toList;
import static java.util.stream.IntStream.range;
public class NumberClassifier {
    public static IntStream factorsOf(int number) {
        return range(1, number + 1)
            .filter(potential - > number % potential == 0);
    }
    public static int aliquotSum(int number) {
        return factorsOf(number).sum() - number;
    }
    public static boolean isPerfect(int number) {
        return aliquotSum(number) == number;
    }
    public static boolean isAbundant(int number) {
        return aliquotSum(number) > number;
    }
    public static boolean isDeficient(int number) {
        return aliquotSum(number) < number;
    }
}
```

例 2-12 的代码明显比原来的命令式解法（例 2-10）以及不完全的函数式版本（例 2-11）短得多，也简单得多。

物理上把机械能分成储蓄起来的 **势能** 和 **释放** 出来的动能。在版本8以前的Java，以及它所代表的许多语言里，集合的行为可以比作动能：各种操作都立即求得结果，不存在中间状态。函数式语言里的 `stream` 则更像势能，它的操作可以引而不发。被 `stream` 储蓄起来的有数据来源（例中的数据来源是 `range()` 方法），还有我们对数据设置的各种条件，如例中的筛选操作。只有当程序员通过 `forEach()`、`sum()` 终结操作来向 `stream` “要”求值结果的时候，才触发从“势能”到“动能”的转换。在“动能”开始释放之前，`stream` 可以作为参数传递并后续附加更多的条件，继续积蓄它的“势能”。这里关于“势能”的比喻，用函数式编程的说法叫作缓求值（`lazy evaluation`），我们将在第4章详细讨论。

### 2.2.4 完美数分类的 Functional Java 实现

开源框架 Functional Java 针对 1.5 以上版本的 Java 运行时，以尽可能低的侵入性为代价引入了尽量多的函数式编程手法。例如Functional Java 可以通过泛型和匿名内部类，在 Java 1.5 时代的 JDK 上模拟出它所缺少的高阶函数特性。

```Java
// 例 2-13 使用 Functional Java 框架实现的完美数分类
import fj.F;
import fj.data.List;
import static fj.data.List.range;
public class NumberClassifier {
    public List < Integer > factorsOf(final int number) {
        return range(1, number + 1)				// ➊
            .filter(new F < Integer, Boolean > () {
                public Boolean f(final Integer i) {
                    return number % i == 0;
                }
            });									// ➋
    }
    public int aliquotSum(List < Integer > factors) {	// ➌
        return factors.foldLeft(fj.function.Integers.add, 0) - factors.last();
    }
    public boolean isPerfect(int number) {
        return aliquotSum(factorsOf(number)) == number;
    }
    public boolean isAbundant(int number) {
        return aliquotSum(factorsOf(number)) > number;
    }
    public boolean isDeficient(int number) {
        return aliquotSum(factorsOf(number)) < number;
    }
}
```

- ➊ Functional Java 的 `range()` 函数圈出来的是一个左闭右开区间
- ➋ 筛选操作代替了迭代
- ➌ 折叠（fold）操作代替了迭代

例 2-13 与例 2-11 的主要区别表现在 `aliquotSum()` 和 `factorsOf()` 这两个方法上。Functional Java 在其 `List` 类中提供的 `foldLeft()` 方法为 `aliquotSum()` 提供了很大的便利

“fold left”（即左折叠操作）的含义是：

1. 用一个操作（或者叫运算）将初始值（例中为 0）与列表中的第一个元素结合；
2. 继续用同样的操作将第 1 步的运算结果与下一个元素结合；
3. 反复进行直到消耗完列表中的元素

例 2-13 另一个值得注意的地方是 `factorsOf()` 方法，它很好地体现了“多着眼结果，少纠结步骤”的格言。寻找一个数的约数，这个问题的实质是什么？或者可以换一种方式来叙述：在从 1 到目标数字的整数列表里，我们怎么确定其中哪些数字是目标数的约数？这样一来，筛选操作就呼之欲出了——我们可以逐一筛选列表中的元素，去除那些不满足筛选条件的数字。

例 2-13 使用了 `foldLeft()` 方法，它依次向左方，即向着第一个元素合并列表。对于满足交换律的加法来说，折叠的方向并不影响结果。万一我们需要使用某些结果与折叠次序相关的操作，还有 `foldRight()` 方法可供选择。

> 高阶函数消除了摩擦

> 不要增加无谓的摩擦

## 2.3 具有普遍意义的基本构造单元

### 2.3.1 筛选

筛选（filter）是列表的一种基本操作：根据用户定义的条件来筛选列表中的条目，并由此产生一个较小的新列表

![](../../../../image/2024/11/978-7-115-40041-3/2-1.jpg)

图 2-1：从较大的列表中筛选出一个数字列表

```Java
// 例 2-14 Java 8 的筛选操作
public static IntStream factorsOf(int number) {
    return range(1, number + 1)
        .filter(potential - > number % potential == 0);
}
```

```Groovy
// 例 2-15 Groovy 的筛选操作（叫作 findAll()）
static def factors(number) {
	(1..number).findAll {number % it == 0}
}
```

> 需要根据筛选条件来产生一个子集合的时候，用 filter

### 2.3.2 映射

映射（map）操作对原集合的每一个元素执行给定的函数，从而变换成一个新的集合

![](../../../../image/2024/11/978-7-115-40041-3/2-2.jpg)

```Groovy
<!-- 例 2-17 Groovy 版的约数查找优化算法 -->
static def factors(number) {
	def factors = (1..round(sqrt(number)+1)).findAll({number % it == 0})
	(factors + factors.collect {number / it}).unique()
}
```

```Clojure
;; 例 2-18 Clojure 写成的 (classify ) 函数将所有行为封装在了几行赋值语句里
(defn classify [num]
	(let [factors (->> (range 1 (inc num)) ; ➊
		(filter #(zero? (rem num %)))) ; ➋
		sum (reduce + factors) ; ➌
		aliquot-sum (- sum num)] ; ➍
	(cond ; ➎
	(= aliquot-sum num) :perfect
	(> aliquot-sum num) :abundant
	(< aliquot-sum num) :deficient)))
```

- ➊ 方法成了赋值语句
- ➋ 把筛选过的区间赋给约数列表
- ➌ 把化约（reduce）过的约数列表赋给 sum
- ➍ 计算真约数和
- ➎ 返回代表分类结果的关键字（枚举）

> 需要就地变换一个集合的时候，用 map

### 2.3.3 折叠/化约

foldLeft 和 reduce 都是 catamorphism 这种范畴论的态射概念具体应用到列表操纵上面的变体，catamorphism 是对列表“折叠”（fold）概念的推广

> 需要把集合分成一小块一小块来处理的时候，用 reduce 或 fold

函数式编程不会用很多抽象，但每个抽象的泛化程度都很高（特化的方面通过高阶函数注入）。函数式编程以参数传递和函数的复合作为主要的表现手段，我们不需要掌握太多作为“不确定因素”存在的其他语言构造之间的交互规则，这一点对于我们的学习是有利的。

## 2.4 函数的同义异名问题

继承函数式传统的语言喜欢按照范式术语来命名基本函数，而出自脚本语言背景的则更喜欢使用描述性的名字（有时候还会起多个名字，实质是指向相同函数的别名）

### 2.4.1 筛选

筛选函数将用户（通常以高阶函数的形式）给定的布尔逻辑作用于集合，返回由原集合中符合条件的元素组成的一个子集

筛选操作与查找（find）函数的关系很密切，查找函数返回的是集合中第一个符合条件的元素

#### 1. Scala

```Scala
// 筛选条件为可被 3 整除的元素
val numbers = List.range(1, 11)
numbers filter (x => x % 3 == 0)
// List(3, 6, 9)

//  更简短版本
numbers filter (_ % 3 == 0)
// List(3, 6, 9)
```

```Scala
// 用 partition() 函数把数字列表分成了两部分
numbers partition (_ % 3 == 0)
// (List(3, 6, 9),List(1, 2, 4, 5, 7, 8, 10))
```

```Scala
// find() 返回第一个匹配项
numbers find (_ % 3 == 0)
// Some(3)
```

`find()` 并不直接把匹配项作为返回值，而是 `Option` 类作了一层包装。`Option` 有两个可能的取值：`Some` 或者 `None`。Scala 也像别的函数式语言一样，用 `Option` 来作为一种迂回手段，以避免在无返回值的情况下返回 `null`

```Scala
numbers find (_ < 0)
// None
```

```Scala
// takeWhile() 函数从集合头部开始，一直取到第一个不满足断言的元素
List(1, 2, 3, -4, 5, 6, 7, 8, 9, 10) takeWhile (_ > 0)
// List(1, 2, 3)
```

```Scala
// dropWhile() 函数则从集合头部开始，一直丢弃满足断言的元素，直到遇到第一个非匹配项
val words = List("the", "quick", "brown", "fox", "jumped",
				"over", "the", "lazy", "dog")
words dropWhile (_ startsWith "t")
// List(quick, brown, fox, jumped, over, the, lazy, dog)
```

#### 2. Groovy

```Groovy
(1..10).findAll {it % 3 == 0}
// [3, 6, 9]
```

```Groovy
(1..10).split {it % 3}
// [ [1, 2, 4, 5, 7, 8, 10], [3, 6, 9] ]
```

```Groovy
(1..10).find {it < 0}
// null
```

Groovy 也有 `takeWhile()` 和 `dropWhile()` 方法，其语义和 Scala 的版本差不多

#### 3. Clojure

Clojure 用于操纵集合的招式数量多得惊人，而且因为 Clojure 语言的动态类型特征，这些函数一般还都是泛型的函数

```Clojure
(def numbers (range 1 11))
(filter (fn [x] (= 0 (rem x 3))) numbers)
; (3 6 9)
```

```Clojure
(filter #(zero? (rem % 3)) numbers)
; (3 6 9)
```

```Clojure
(def words ["the" "quick" "brown" "fox" "jumped" "over" "the" "lazy" "dog"])
(filter #(= 3 (count %)) words)
; (the fox the dog)
```

### 2.4.2 映射

传给映射函数的是一个高阶函数和一个集合，它在对集合中的每一个元素施用传入的函数之后，产生另一个集合作为返回值

#### 1. Scala

```Scala
List(1, 2, 3, 4, 5) map (_ + 1)
// List(2, 3, 4, 5, 6)

words map (_.length)
// List(3, 5, 5, 3, 6, 4, 3, 4, 3)
```

嵌套的列表在函数式编程语言中运用得极为频繁，因此各语言普遍地具备用来消除嵌套的库函数，一般将此操作称为“展平”（flattening）

```Scala
List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9)) flatMap (_.toList)
// List(1, 2, 3, 4, 5, 6, 7, 8, 9)

words flatMap (_.toList)
// List(t, h, e, q, u, i, c, k, b, r, o, w, n, f, o, x, ...
```

#### 2. Groovy

映射操作在 Groovy 语言里对应的是若干 `collect()` 函数

```Groovy
(1..5).collect {it += 1}
// [2, 3, 4, 5, 6]

def words = ["the", "quick", "brown", "fox", "jumped",
"over", "the", "lazy", "dog"]
words.collect {it.length()}
// [3, 5, 5, 3, 6, 4, 3, 4, 3]
```

Groovy 也有一个类似于 `flatMap()`，用来消除嵌套结构的方法，叫作 `flatten()`

```Groovy
[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ].flatten()
// [1, 2, 3, 4, 5, 6, 7, 8, 9]

(words.collect {it.toList()}).flatten()
// [t, h, e, q, u, i, c, k, b, r, o, w, n, f, o, x, j, ...
```

#### 3. Clojure

```Clojure
(map inc numbers)
; (2 3 4 5 6 7 8 9 10 11)

(map #(count %) words)
; (3 5 5 3 6 4 3 4 3)

(flatten [[1 2 3] [4 5 6] [7 8 9]])
; (1 2 3 4 5 6 7 8 9)
```

### 2.4.3 折叠/化约

#### 1. Scala

Scala 的各种折叠操作最为丰富，其中部分原因是它需要更多地面对某些类型相关的场景，而这些场景在动态类型的 Groovy 和 Clojure 语言中根本不存在

传给 `reduce()` 的函数或运算符一般接受两个参数，且仅返回单一值，就好像原集合被“消耗”掉了一样

```Scala
List.range(1, 10) reduceLeft((a, b) => a + b)
// 45

List.range(1, 10).reduceLeft(0)(_ + _)
// 45

List.range(1, 10) reduceRight(_ - _)
// 8 - 9 = -1
// 7 - (-1) = 8
// 6 - 8 = -2
// 5 - (-2) = 7
// 4 - 7 = -3
// 3 - (-3) = 6
// 2 - 6 = -4
// 1 - (-4) = 5
// result: 5

words.reduceLeft((a, b) => if (a.length > b.length) a else b)
// jumped
```

Scala 语言支持运算符重载，`foldLeft` 和 `foldRight` 作为十分常用的折叠操作，也分别有各
自对应的运算符 `/:` 和 `:\`

```Scala
(0 /: List.range(1, 10)) (_ + _)
// 45

(List.range(1, 10) :\ 0) (_ - _)
// 5
```

#### 2. Groovy

Groovy 提供了两个版本的 `inject()` 来完成化约操作，分别对应于 Scala 众多同类方法中的 `reduce()` 和 `foldLeft()`

```Groovy
(1..10).inject {a, b -> a + b}
// 55

// 带初始值的版本
(1..10).inject(0, {a, b -> a + b})
// 55
```

#### 3. Clojure

Clojure 在它的 Reducers 库（ http://clojure.org/reducers ）里提供了更多与化约操作相关的高级功能
