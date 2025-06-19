# RAG介绍

## 1. 什么是RAG，它有什么特点

### 1.1 初识RAG

- RAG（Retrieval Augmented Generation）为生成式模型与外部世界互动提供了一个很有前景的解决方案。
- RAG的主要作用类似搜索引擎，找到用户提问最相关的知识或者是相关的对话历史，并结合原始提问（查询），创造信息丰富的prompt，指导模型生成准确输出。
- 其本质上应用了情境学习（In-Context Learning）的原理。
- **设置提示**：
    - **RAG（检索增强生成）** = **检索技术 + LLM 提示**

### 1.2 RAG的特点

关于 RAG 有如下特点：

1. **依赖大语言模型来强化信息检索和输出**：RAG需要结合大型语言模型（LLM）来进行信息的检索和生成，但如果单独使用RAG，它的能力会受到限制。也就是说，RAG需要依赖强大的语言模型支持，才能更有效地生成和提供信息。
2. **能与外部数据有效集成**：RAG能够很好地接入和利用外部数据库的数据资源。这一特性弥补了通用大模型在某些垂直或专业领域的知识不足，比如行业特定的术语和深度内容，能提供更精确的答案。
3. **数据隐私和安全保障**：通常，RAG所连接的私有数据库不会参与到大模型的数据集训练中。因此，RAG既能提升模型的输出表现，又能有效地保护这些私有数据的隐私性和安全性，不会将敏感信息暴露给大模型的训练过程。
4. **表现效果因多方面因素而异**：RAG的效果受多个因素的影响，比如所使用的语言模型的性能、接入数据的质量、AI算法的先进性以及检索系统的设计等。这意味着不同的RAG系统之间效果差异较大，不能一概而论。

## 2. RAG技术体系的总体思路

> 参考：[https://aibook.ren/archives/what-is-rag](https://aibook.ren/archives/what-is-rag)

- RAG可分为5个基本流程：**知识文档的准备；嵌入模型（embedding model）；向量数据库；查询检索 和 生产回答**。

<center>
    <img src="../fig/10-RAG.png">
</center>



<!-- <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113464395696515&bvid=BV1tvmmY3EgS&cid=26715621376&p=1" scrolling="yes" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe> -->