# Toward a Mechanistic Understanding of Stepwise Inference in Transformers: A Synthetic Graph Navigation Model

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
Stepwise inference protocols, such as scratchpads and chain-of-thought, help language models solve complex problems by decomposing them into a sequence of simpler subproblems.
Despite the significant gain in performance achieved via these protocols, the underlying mechanisms of stepwise inference have remained elusive.
To address this, we propose to study autoregressive Transformer models on a synthetic task that embodies the multi-step nature of problems where stepwise inference is generally most useful.
Specifically, we define a graph navigation problem wherein a model is tasked with traversing a path from a start to a goal node on the graph.
Despite is simplicity, we find we can empirically reproduce and analyze several phenomena observed at scale: (i) the stepwise inference reasoning gap, the cause of which we find in the structure of the training data; (ii) a diversity-accuracy tradeoff in model generations as sampling temperature varies; (iii) a simplicity bias in the model's output; and (iv) compositional generalization and a primacy bias with in-context exemplars.
Overall, our work introduces a grounded, synthetic framework for studying stepwise inference and offers mechanistic hypotheses that can lay the foundation for a deeper understanding of this phenomenon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces and explores a novel paradigm that casts stepwise inference, a crucial element in logical reasoning, as a graph navigation challenge. Using directed acyclic graphs (DAGs) inspired by computational graphs and execution traces, the paper proposes a synthetic autoregressive language model setup for solving navigation tasks. The primary aim is to simplify, control, and interpret the mechanisms behind stepwise inference in Large Language Models (LLMs). This work serves as a foundational step towards creating a controllable and interpretable data generation process, offering insights into the stepwise inference in autoregressive transformers, which can inspire future research in logical reasoning and stepwise inference.

### Strengths
1. This paper presents an innovative framework that leverages stepwise inference within transformer models to navigate complex graph structures, showcasing a significant advance in understanding logical reasoning paths. The method enhances the interpretability of models but with a deeper mechanistic insight.
2. The paper integrates theoretical concepts with empirical validation, showcasing a comprehensive study on synthetic graph navigation tasks. Experimental design and results, particularly the diversity vs. accuracy trade-off, provide a compelling case for the model's efficacy and reliability.
3. The paper also introduces a data generating process that augments the richness of training datasets, allowing for more robust model training.

### Weaknesses
1. While the paper claims to address stepwise inference in transformers and introduces a graph navigation model, the experiments seem to focus narrowly on synthetic tasks without sufficient evidence of the model's generalizability to a more realistic or applicable datasets.
2. The approach primarily involves modeling the decision-making process using directed acyclic graphs (DAGs). However, there are concerns that the model may overfit these synthetic graph structures. The paper does not adequately address how the model handles noisy real-world graphs, which may exhibit cycles, incomplete information, or random behavior that are common in real-world applications. In this context, a deeper analysis of the robustness of the proposed method is crucial.

### Questions
Illustrated in the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to study the step-wise inference mechanism by exploring the graph navigation problem.

### Strengths
+ Originality:

    The idea of modeling step-wise inference as graph navigation is interesting.

### Weaknesses
- Quality:

    i) Although the authors claim to reveal the connection between graph navigation and the step-wise inference mechanism in transformer, the experiments, to my understanding, are solely about training transformers on the synthesized graph dataset. It remains unclear to me how this set-up can be translated into the study of step-wise inference mechanism, despite the conceptual similarity between DAG and the step-wise inference mechanism. It is unclear whether this finding on the synthesized graph dataset can be safely transferred to real-world large-scale dataset.

    ii) The definition of hierarchical graph and random graph is confusing to me. It seems possible to convert the random graph in fig. 10 into a hierarchical graph by simply re-grouping the nodes.

- Significance:

    The highlighted finding, i.e., the step-wise inference gap is influenced by (i) the underlying DAG structure, and (ii) the length of the training samples is only studied in a very shallow level. The DAG structure in the context seems to be not well-defined and well-categorized. The discussion about the length of the training samples mainly focuses on how it affects the length of the model output.

### Questions
Please see the weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To analyze the stepwise inference in large language models, the authors examine a synthetic graph navigation problem and replicate several phenomena originally observed in LLMs. This work provides a simplified platform for researchers to study properties of LLM.

### Strengths
1. A comprehensive framework of DAG is provided as substitute for stepwise inference in LLM
2. Reasoning gap, the diversity-accuracy tradeoff, in-context control are replicated in well-designed experiments, showing the effectiveness of the proposed enviroment.
3. Well-written, easy to follow.

### Weaknesses
1.While several phenomena originally observed in LLMs were replicated in this DAG couterpart. It will be more convincing if some extraoplated property in DAG system can be found in LLMs which was not discovered before.

2. Emergent abilities of large language lodels were thought to be a consequence of unpredictable scaling, therefore, I doubt if a simpilified DAG substitute can replicate this behaviour.

### Questions
I will increase my score if my concern is well addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper sheds light on step-wise inference in LLMs by casting the problem as a graph navigation problem. A dataset of random DAGs is generated with start and goal nodes and an autoregressive transformer is trained to navigate the graph from start to goal by next step prediction. The problem can be mapped to step-wise inference in LLMs and the paper investigates several settings in which this is manifested.

### Strengths
I have found the problem setting of the paper interesting - these are important questions and some of the more challenging aspects of LLMs are investigated here.

The casting to DAG navigation is a good choice - it covers a lot of potentially related inference problems with a simple model which is easy to generate data for and train.

### Weaknesses
I think my main issue with the paper is that LLMs are trained on very very different data (though in a roughly similar setup).
I am not sure the mapping between DAG navigation and what LLMs actually learn is as simple as claimed in the paper as LLMs need to do many other things when trained.

### Questions
Would the authors shed more light on the limitations and dissimilarities between the proposed model and actual LLM training?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
