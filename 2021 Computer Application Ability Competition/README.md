# 学生信息 

刘正涛  东华大学计算机科学与技术 2018 级 

纪之昀  东华大学信息管理与信息系统  2018 级          

吴文俊  东华大学金融学  2018 级 

指导教师 

孙国豪  东华大学计算机学院

## 1   作品简介 

党的十九大报告指出，现阶段中国社会的主要矛盾已转化为人民日益增长的美好生活 需要和不平衡  不充分的发展之间的矛盾，今后工作的重点是解决发展不平衡不充分的问题。 从多维角度看，不平等不仅包括收入分配不平等，还涉及健康不平等等。与此同时，2019 年中国肥胖人口规模超 2.5 亿人，肥胖人群规模的发展，以及由肥胖引起的健康问题已逐渐 成为社会关注的焦点。七成受访网民认为形体管控与健康相关，国民对于个人体重健康相关 意识较强。

对此，我们结合数据分析、数据可视化、卷积神经网络等技术，努力建立动态化展示 界面，聚焦食品健康相关分析与预测，展示食品营养价值信息，致力于打造一个集健康预测， 食物查询，体质记录三位一体的平台，为推动全面健康奉献自己的力量。

## 2   作品效果图

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_1.png)

<center> 图 1 </center>

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_2.png)

<center> 图 2 </center>

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_3.png)

<center> 图 3 </center>

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_4.png)

<center> 图 4 </center>

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_5.png)

<center> 图 5 </center>

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_6.png)

<center> 图 6 </center>

## 3   设计思想

### 1. 项目背景

随着大众对食品健康等方面关注度的不断提升，健康与饮食领域也得到了空前发展，健康管 理主要包括食品的安全性及食品的营养搭配性，之前人们的关注点一直都集中在食品安全问 题上，而且也出现很多因食品安全造成的不良后果，随着大数据时代的来临不仅要对食品安 全进行追根溯源，信息化技术还能为消费者提供更加多元化的健康管理建议，同时也为食品 营养运用与发展提供更加宽阔的发展空间。党的十九大报告指出，现阶段中国社会的主要矛 盾已转化为人民日益增长的美好生活需要和不平衡  不充分的发展之间的矛盾，今后工作的 重点是解决发  展不平衡不充分的问题。从多维角度看，不平等不仅包括收入分配不平等， 还涉及健康不平等等。

目前，人们对食品问题的关注度非常高，绿色食品、有机食品、无公害食品等宣传名 头在各大商场和超市中琳琅满目，人们对食品的营养成分和安全性也有不同的见解和认识， 虽然食品的种类繁多，其中也不乏有很多商家的广告噱头，常常搞得消费者一头雾水，可见

其内容和信息量之庞大。除此之外，食品营养成分是健康管理领域中不可或缺的重要研究内 容。食品中营养成分的数据分析和报告都要以非常严谨的数据形式呈现，随着人们的生活水 平不断提高，人们的饮食数量、种类也越来越多，因此食品的营养成分更加多样性和多元化， 相关研究的数据和内容也更加复杂化。与此同时，2019 年中国肥胖人口规模超 2.5 亿人，肥 胖人群规模的发展，以及由肥胖引起的健康问题已逐渐成为社会关注的焦点。七成受访网民 认为形体管控与健康相关，国民对于个人体重健康相关意识较强。

### 2. 设计构思与创意 

本平台利用混沌多输入卷积神经网络(MultiInput Convolutional Neural Network)， 通过分析用户的身体数据、饮食情况、饮食状况、家庭情况四方面的指数进行体质分析；同 时搜集整理了食品成分相关数据，方便用户查询；此外可以在平台上记录自己的体征数据， 方便用户进行体质管理。

### 3. 项目模块与功能 

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_7.png)

### 4. 技术运用与特色 

项目后端基于 python 的 Django 框架，利用 djangoMTV 框架对网站进行架构，实现网 站后端存储，中间调用，前端展示的功能。利用 bootstrap 框架进行网页前端搭建，利用 echarts 进行数据可视化。

为了分析用户的体征数据，我们搜集查找已有数据集进行分析，最终选用 UCI 机器学习 数据集中的肥胖数据，对已有数据集进行预处理后，多次实践选用了混沌多输入卷积神经网 络进行分类。为了预测用户的健康体征数据，我们爬取了 UCI 公开数据集上的数据，其数据 真实可靠。该数据集中有 16 个特征，我们将其分为 4 组，分别代表身体情况、饮食情况、 饮食习惯、生活习惯。利用混沌多输入卷积神经网络进行分类预测，为每一组加一层全连接

层去提取特征，我们使用非线性的激活函数 Sigmoid 和 Tanh 进行压缩，将所得到的信号继 续往下传递。通过多次调整与尝试之后，我们发现 Adam  算法收敛速度在我们模型框架中 达到了最优。最后得到的输出是选到 4 个变量的概率，我们挑选概率最大的 y 作为我们判断 的结果。我们对模型应用到了测试集上进行评估，结果如下:准确率，精确率，召回率，F1 均达到了 0.98 以上，证明了我们模型的准确性。

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_8.png)

整体的网络模型结构如下图：

![](https://github.com/June24-Wu/Project_in_DHU/blob/master/2021%20Computer%20Application%20Ability%20Competition/IMG/Picture_9.png)

### 4   指导教师自评

首先，该系统在允许用户不断更新自身的健康相关信息，如体重，腰围，体脂率，血脂 和血糖的同时，采用了折线图的形式来展示这些信息，可以非常直观的让用户感受到自身相 关数值的变化。其次，该系统也非常全面的列出了各类食物所蕴含的卡路里，碳水，蛋白质 以及脂肪的含量，对用户的日常健康饮食具有非常高的参考价值。另外，系统也提供了健康 测试的功能，让用户可以在输入自身相关信息后得到自身健康与否的一个预测和参考。综上 所诉，该系统对于个人健康管理具有很强的实用性。同时该系统提供的信息展示，食物查询

以及健康测试的功能也具有很强的创新性。
