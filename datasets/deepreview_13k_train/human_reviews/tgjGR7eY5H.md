# RL4CO: a Unified Reinforcement Learning for Combinatorial Optimization Library

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Deep reinforcement learning offers notable benefits in addressing combinatorial problems over traditional solvers, reducing the reliance on domain-specific knowledge and expert solutions, and improving computational efficiency. Despite the recent surge in interest in neural combinatorial optimization, practitioners often do not have access to a standardized code base. Moreover, different algorithms are frequently based on fragmentized implementations that hinder reproducibility and fair comparison. To address these challenges, we introduce RL4CO, a unified Reinforcement Learning (RL) for Combinatorial Optimization (CO) library. We employ state-of-the-art software and best practices in implementation, such as modularity and configuration management, to be flexible, easily modifiable, and extensible by researchers. Thanks to our unified codebase, we benchmark baseline RL solvers with different evaluation schemes on zero-shot performance, generalization, and adaptability on diverse tasks. Notably, we find that some recent methods may fall behind their predecessors depending on the evaluation settings. We hope RL4CO will encourage the exploration of novel solutions to complex real-world tasks, allowing the community to compare with existing methods through a unified framework that decouples the science from software engineering. We open-source our library at https://anonymous.4open.science/r/rl4co-iclr.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a unified toolbox to evaluate and implement auto-regressive methods for combinatorial optimization. The authors demonstrate that some SOTA methods actually underperform under out-of-distribution data and that policy gradient methods seem to outperform value-based methods.

### Strengths
The existence of a unified toolbox for implementation and evaluation of ML methods for CO is important as this community expands. The paper also empirically validates various interesting hypotheses regarding out-of-distribution data and policy gradient methods for training when compared to value-based methods.

### Weaknesses
While I find the contribution to be useful and the paper to be well-written, the primary concern is the lack of novelty in the context of a research track submission. The paper presents a unified toolbox for the implementation and evaluation of auto-regressive (AR) methods for combinatorial optimization (CO), which is valuable for the community. However, it does not introduce fundamentally new algorithms, methodologies, or problem formulations. The research track typically expects novel contributions that push the boundaries of the field. Although the empirical validation of interesting hypotheses regarding out-of-distribution data and the performance of policy gradient methods versus value-based methods is noteworthy, it does not constitute a novel research contribution on its own. Therefore, while the toolbox is a valuable asset, it aligns more closely with a benchmark or tool track submission rather than the research track.

### Questions
In your opinion, why do policy optimization methods seem to outperform value-based methods in neural CO?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces RL4CO, a modular, flexible, and unified Reinforcement Learning library for solving combinatorial optimization problems. It is built upon the best software practices and libraries and implements several classical RL for CO algorithms. The introduction of this library could enable a fair and unified comparison among different methods.

### Strengths
1. RL4CO addresses the reproducibility problems and the fair comparison among different RL methods in NCO, which I believe is one important contribution to the research in the relevant field.
2. The library provides an easy-to-use interface to implement different RL algorithms, facilitating research in this field.
3. This paper makes a comprehensive empirical comparison of different models, problems, and search algorithms, which are impressive and helpful to future research. 
4. The presentation is very good, the whole paper is well-motivated and easy to follow.

### Weaknesses
I appreciate the effort of the authors in introducing this easy-to-use library, but I also want to point out that the contribution of this work is not as significant as it claims.
1. This paper quite narrows the idea of RL algorithms for CO. There could be different ways to formulate the CO as an RL problem, not limited to the one outlined in Equation (1) - (3).  For example, neighborhood search first constructs an initial feasible solution and optimizes the current solution at each step [1,2], DIMES predicts a solution directly and optimizes the model with REINFORCE (one-step RL) [3]. 
2. Most CO problems presented in the paper are routing problems, other classical CO problems like set covering, and maximum independent set are not covered.

### Questions
I note that DIMES is listed as a supervised approach (footnote on page 1), which I think is incorrect. I'm wondering if the authors have any specific criterion for the method classification or it is just a mistake (relevant to the first point in weaknesses).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a general reinforcement learning framework for solving combinatorial optimization problems. They aim to unify several existing methods into one general code library called RL4CO. The code repository is employed with SOTA software, which makes it flexible, modifiable, and extensible to the users. Based on their proposed RL4CO, they are able to conduct multiple evaluations for existing methods.

### Strengths
1. This paper is well-written and easy to follow.
2. The proposed unified framework is necessary for the community, and the code is open-source.

### Weaknesses
1. Though the authors claim that they aim to propose a unified framework, the methods considered in their paper are mainly based on AM and POMO, in other words, the auto-regressive methods. As far as I know, there are also other methods other than auto-regressive, such as Local-rewrite[1]. Instead of constructing the solution from scratch, methods like Local-rewrite aim to improve an existing solution. Are these kinds of methods able to integrate into the proposed RL4CO framework?
2. The proposed unified framework mainly focuses on TSP/VRP and the graph-based CO problems. However, there are other kinds of CO such as bin-packing, job scheduling, and mixed integer programming. I wonder if the proposed RL4CO covers these CO problems.
3. In the experiments, only three methods are considered as baselines. I think the authors should test more RL4CO methods as they claimed they propose a unified library. 
4. Still in the experiments, the size of TSP/VRP is only 50. I consider this size to be relatively small.

### Questions
As I mentioned before, I consider the proposed unified framework to be meaningful to the community, but I think the authors may over-claim their work. They call their framework "RL4CO", but they only cover 3 RL methods and limited CO problems.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The RL4CO paper introduces a unified Reinforcement Learning for Combinatorial Optimization library that provides a standardized code base for practitioners to address combinatorial problems using deep reinforcement learning. The library is designed to be flexible, easily modifiable, and extensible by researchers, and it benchmarks baseline RL solvers with different evaluation schemes on zero-shot performance, generalization, and adaptability on diverse tasks. The paper also discusses the limitations and areas of improvement with the current library and benchmark experiments. The paper aims to provide a comprehensive resource for researchers and practitioners to develop and evaluate RL-based approaches for combinatorial optimization problems.

### Strengths
1. This work introduces a benchmark that applies the most common RL methods to solve routing-related problems such as TSP and CVRP, and it is implemented in a modular way. This is beneficial for the community and practitioners to quickly compare results.    
2. The paper presents some interesting results that might be helpful for the community, like some recent approaches might not match the performance of earlier methods under certain evaluation conditions.

### Weaknesses
1. The title of this paper is RL4CO, but it only addresses routing-related problems. Would it be more appropriate to name it RL4Routing?    
2. While this paper is confined to the scope of RL4Routing, it implements various RL methods for these problems. However, at their core, these methods belong to the same category (and share very similar algorithm procedures), and there is a lack of insights to organize this category effectively. If this article could provide some useful conclusions or derive new methods based on these benchmarks, it would become novel.             
3. Additionally, one cannot ignore the issue that, for example, in the case of TSP problems, many non-autoregressive (or non-RL) methods [1,2,3] have recently achieved better performance than RL-based, like faster inference time, lower optimal gap, and runnable on larger instances (TSP1000 and TSP10000). Therefore, as a benchmark for routing problems(TSP, CVRP, etc.), the comparison of methods is not comprehensive enough.

### Questions
See the weakness part of the review.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
