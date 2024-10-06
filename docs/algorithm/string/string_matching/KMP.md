---
date:

    created:2024-10-04
---
# KMP（Knuth-Morris-Pratt）算法

Knuth-Morris-Pratt (KMP) 算法是由 D.E.Knuth, J.H.Morris 和 V.R.Pratt 同时发现的，主要用于进行字符串的匹配。其能够在时间复杂度为 $O(n+m)$（其中 $n$ 为文本长度，$m$ 为模式长度）内找到模式字符串在文本中的位置。它通过部分匹配表（也称为"前缀函数"）实现跳跃式的模式匹配。

## 特点
**优点**

- 时间复杂度低，只有 $O(n+m)$
- KMP 适合在长文本中多次匹配较短模式，特别是在模式字符串包含重复前缀的情况下，能够显著减少重复计算。

**缺点**

- 不适合某些特殊匹配场景，如果文本和模式中包含较少的重复结构，KMP算法的部分匹配表的作用可能不会显著提升性能


## 步骤

TODO


## 流程图

TODO


## 一个栗子

TODO

## 代码

=== "🔵 Python"
    ```python
    def kmp(s, t):
        if not t: return 0
        pi = [0] * len(t)
        j = 0
        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = pi[j-1]
            if t[i] == t[j]:
                j += 1
            pi[i] = j

        j = 0
        for i, c in enumerate(s):
            while j > 0 and t[j] != c:
                j = pi[j-1]
            if t[j] == c:
                j += 1
            if j == len(t):
                return i - j + 1

        return -1

    if __name__ == '__main__':
        text = "abababaabc"
        pattern = "ababaab"
        res = kmp(text, pattern)
        print(res)
    ```

    ??? success "可视化代码 [:material-open-in-new:](https://pythontutor.com/iframe-embed.html#code=def%20kmp%28s,%20t%29%3A%0A%20%20%20%20if%20not%20t%3A%20return%200%0A%20%20%20%20pi%20%3D%20%5B0%5D%20*%20len%28t%29%0A%20%20%20%20j%20%3D%200%0A%20%20%20%20for%20i%20in%20range%281,%20len%28t%29%29%3A%0A%20%20%20%20%20%20%20%20while%20j%20%3E%200%20and%20t%5Bi%5D%20!%3D%20t%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20pi%5Bj-1%5D%0A%20%20%20%20%20%20%20%20if%20t%5Bi%5D%20%3D%3D%20t%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20%20%20%20%20pi%5Bi%5D%20%3D%20j%0A%0A%20%20%20%20j%20%3D%200%0A%20%20%20%20for%20i,%20c%20in%20enumerate%28s%29%3A%0A%20%20%20%20%20%20%20%20while%20j%20%3E%200%20and%20t%5Bj%5D%20!%3D%20c%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20pi%5Bj-1%5D%0A%20%20%20%20%20%20%20%20if%20t%5Bj%5D%20%3D%3D%20c%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20%20%20%20%20if%20j%20%3D%3D%20len%28t%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20i%20-%20j%20%2B%201%0A%0A%20%20%20%20return%20-1%0A%0Aif%20__name__%20%3D%3D%20'__main__'%3A%0A%20%20%20%20text%20%3D%20%22abababaabc%22%0A%20%20%20%20pattern%20%3D%20%22ababaab%22%0A%20%20%20%20res%20%3D%20kmp%28text,%20pattern%29%0A%20%20%20%20print%28res%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false){:target="\_blank"}"

        <iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20kmp%28s,%20t%29%3A%0A%20%20%20%20if%20not%20t%3A%20return%200%0A%20%20%20%20pi%20%3D%20%5B0%5D%20*%20len%28t%29%0A%20%20%20%20j%20%3D%200%0A%20%20%20%20for%20i%20in%20range%281,%20len%28t%29%29%3A%0A%20%20%20%20%20%20%20%20while%20j%20%3E%200%20and%20t%5Bi%5D%20!%3D%20t%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20pi%5Bj-1%5D%0A%20%20%20%20%20%20%20%20if%20t%5Bi%5D%20%3D%3D%20t%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20%20%20%20%20pi%5Bi%5D%20%3D%20j%0A%0A%20%20%20%20j%20%3D%200%0A%20%20%20%20for%20i,%20c%20in%20enumerate%28s%29%3A%0A%20%20%20%20%20%20%20%20while%20j%20%3E%200%20and%20t%5Bj%5D%20!%3D%20c%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20pi%5Bj-1%5D%0A%20%20%20%20%20%20%20%20if%20t%5Bj%5D%20%3D%3D%20c%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20%20%20%20%20if%20j%20%3D%3D%20len%28t%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20i%20-%20j%20%2B%201%0A%0A%20%20%20%20return%20-1%0A%0Aif%20__name__%20%3D%3D%20'__main__'%3A%0A%20%20%20%20text%20%3D%20%22abababaabc%22%0A%20%20%20%20pattern%20%3D%20%22ababaab%22%0A%20%20%20%20res%20%3D%20kmp%28text,%20pattern%29%0A%20%20%20%20print%28res%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

=== "🔴 C++"
    ```C++
    Coming soon.
    ```
    