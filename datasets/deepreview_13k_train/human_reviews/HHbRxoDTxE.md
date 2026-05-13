# Looped Transformers are Better at Learning Learning Algorithms

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
Transformers have demonstrated effectiveness in \emph{in-context solving} data-fitting problems from various (latent) models, as reported by \citet{Garg2022WhatCT}. 
However, the absence of an inherent iterative structure in the transformer architecture presents a challenge in emulating the iterative algorithms, which are commonly employed in traditional machine learning methods.
To address this, we propose the utilization of \emph{looped} transformer architecture and its associated training methodology, with the aim of incorporating iterative characteristics into the transformer architectures. Experimental results suggest that the looped transformer achieves performance comparable to the standard transformer in solving various data-fitting problems, while utilizing less than 10\%  of the parameter count.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use looped transformers to solve in-context learning, which achieves comparable performance to the standard transformer, but utilizes less than 10% of the parameters.

### Strengths
It is interesting to see looped transformers work well for in-context learning.

The paper provides a thorough evaluation and ablations of looped transformers for in-context learning. 

The paper is well written.

### Weaknesses
My primary concern lies in the relevance of looped transformers to in-context learning. It appears that their main advantage is in reducing the number of parameters. However, it's not entirely clear why this reduction in parameters is crucial for in-context learning, especially in cases involving linear functions, sparse linear functions, random decision trees, and 2-layer ReLU networks. I find that the paper lacks in-depth mathematical insights or a thorough exploration of the practical implications that would help address this concern. Specifically, while parameter reduction is often a goal in machine learning, the paper does not articulate why this is particularly beneficial for in-context learning compared to standard transformers, especially given that the tasks used for evaluation appear to be relatively low-dimensional. Furthermore, the paper does not sufficiently explore the potential trade-offs between parameter reduction and the ability to generalize to unseen in-context examples. It is not clear if the looped architecture is learning fundamentally different representations than standard transformers, or if it is simply achieving similar results with fewer parameters.

### Questions
What is the mathematical insight of looping transformers for in-context learning?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a training methodology for looped transformers to effectively emulate iterative algorithms and provides empirical evidence that demonstrate the advantages of looped transformer on in-context learning. However, since all experiments are made on simulated datasets, whether the proposed method is effective in dealing with real-world data remains to be validated.

### Strengths
(1) The paper uses the looped transformer to emulate iterative learning algorithms and presents a novel methodology to train the looped transformer under reasonable assumptions.
(2) The paper provides a wide range of evaluation and detailed ablation studies of the proposed method on simulated datasets and demonstrates its superior performance compared to standard, non-recursive transformers.

### Weaknesses
(1) Since all experiments are made on simulated datasets, whether the proposed method is effective in dealing with real-world data remains to be validated. It is unclear if the performance gains observed on these synthetic datasets will translate to more complex, real-world scenarios with inherent noise and higher dimensionality. The paper lacks a discussion on the potential limitations of the proposed method when applied to datasets with characteristics different from the simulated ones. 
(2) The classes of functions studied in the paper (including linear regression, decision tree, 2-layer ReLU NN, etc.) are ideal and relatively simple compared to the functions emerged in practical applications. The paper should provide a more thorough justification for the choice of these specific function classes and discuss their limitations in representing real-world complexities. Specifically, the decision tree implementation, with its fixed depth and random feature selection at each node, may not be representative of real-world decision tree learning scenarios.

### Questions
1. Can you provide more details about the probability distribution over the used classes of functions, especially for decision trees and 2-layer ReLU NN?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the paper the authors examine the applicability of looped transformers to the task of learning linear regression in context (giving sampled examples). They compare the performance of a looped transformer with a standard 12 layer transformer and a least squares solver. They show that for some settings the looped transformer matches or even outperforms the performance of a standard transformer on the task of linear regression, while incorporating significantly less parameters.

### Strengths
- It is an interesting approach to use looped transformers for the task of linear regression in-context. It seems to work well with significantly less parameters.
- The authors examine different settings, like using input injection, choosing the number of iterations, altering the number of layers, heads and the dimension of the embeddings.
- The experimental evaluation is convincing.

### Weaknesses
 - The application of the looped transformer (in order to match the performance of a standard transformer) requires an extensive hyperparameter search for b and T. The authors make suggestions how this could be avoided, which should maybe be subject to further research.
- The structure of the paper can be improved, e.g., by ending the paper with a short conclusion instead of the related works.

Minor details:
- "It is worth noting" instead of "it's worth noting"
- "use the scheduling does not significantly impact the outcome" instead of "use the scheduling doesn’t significantly impact the outcome"
- The Figures are too small
- Fig. 2: The curve for the least squares solver is difficult to see
- Fig. 2 description: (left) and (right) should not be written after the punctuation in the sentence but before.

### Questions
- What is the experimental setting for the plots shown in Figure 2? 
- Why are the curves for the looped transformer and the standard Transformer in Figure 2 exactly overlapping?
- How much time and resources does it take to find optimal values for b and T?
- If you consider the hyperparameter search is it still more useful to apply looped transformers instead of the standard transformers?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
