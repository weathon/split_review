# LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization

- Decision: Accept
- Scores: 10, 8, 8

## Abstract
Low-rank adaption (LoRA) is a widely used parameter-efficient finetuning method for LLMs that reduces memory requirements. 
However, current LoRA optimizers lack transformation invariance, which leads to weight updates that depend on how the two LoRA factors are scaled or rotated. This deficiency leads to inefficient learning and sub-optimal solutions in practice. 
This paper introduces LoRA-RITE, a novel adaptive matrix preconditioning method for LoRA optimization, which achieves transformation invariance while being computationally efficient. 
We provide theoretical analysis to demonstrate the benefit of our method and conduct experiments on various LLM tasks with different models including Gemma 2B, 7B, and mT5-XXL. The results demonstrate consistent improvements over existing optimizers. 
For example, replacing Adam with LoRA-RITE during LoRA fine-tuning of Gemma-2B yields 4.6\% accuracy gain on Super-Natural Instructions and 3.5\% accuracy gain across other four LLM benchmarks (HellaSwag, ArcChallenge, GSM8K, OpenBookQA).

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper introduces an enhancement to the existing LoRA method. LoRA, which stands for Low-Rank Adaptation, is a parameter-efficient fine-tuning technique widely employed in training Large Language Models. However, a significant limitation of LoRA is that matrix $A$ is typically much larger than matrix $B$, leading to reduced training efficiency of LoRA. The authors leverage the concept of transformation invariance to formally capture this phenomenon, demonstrating that LoRA weight updates remain consistent across different decomposition results. They further define a weaker version, termed "scalar scale invariance," which only examines whether decompositions with varying magnitude distributions in matrices $A$ and $B$ yield different weight updates. The authors demonstrate that transformation invariance is crucial for efficient feature learning, propose a method to preserve this invariance while considering optimizer implementation, and conduct experiments across various models to illustrate the advantages of their approach.

### Strengths
The authors take a significant step beyond simple intuitions by delving into the core of training efficiency, proposing a novel approach to fully achieve transformation invariance in LoRA models. For soundness, they provide rigorous proofs for all mathematical statements in the paper and conduct extensive experiments across various LoRA advancement methods and benchmarks to demonstrate the superiority of their method. In terms of contribution, given that LoRA is a widely-used training method and their work is computationally inexpensive, individuals training Large Language Models and potentially other AI models can greatly benefit from their advancements.

### Weaknesses
The paper lacks visual illustrations of loss curves to cross-validate the effectiveness of their method in accelerating convergence. Although they state that matrix $A$ remains nearly identical during training, they do not provide visual evidence of how the magnitude of $A$ updates after applying their method, which could further validate its effectiveness. Additionally, the authors do not address potential numerical instability issues. Specifically, their algorithm involves inverting the matrix $R_A$, which could be zero at the initial training step. The conclusion and limitations section is somewhat lacking, as it only discusses the limitations of the base LoRA method rather than potential limitations of their proposed method.

### Questions
Will your method be susceptible to numerical instability? If not, why? If so, how will you address this issue?

In terms of contributing to the LLM community, open-sourcing the related code would be highly appreciated.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper points out the issue of standard LoRA training on the decomposed matrices A and B and then enforces the transformation invariant property into optimization, which further improve the representation capability for better performance

### Strengths
1. The paper propose a new optimization approach that retains the transformation invariant for the LoRA-type fine-tuning, which is widely used in the large model fine-tuning. Moreover, the paper presented the convergence analysis theoretically. 

2. The experimental results demonstrate significant improvement with marginal computation increase, results in a better trade-off compared to all SOTA methods.

### Weaknesses
1. As the paper focuses on the optimization, a convergence analysis should be conducted to better justify the proposed method, e.g. the norm of A and B, like in figure 1.

2. The analysis over experimental results are limited, e.g., for some datasets, the proposed method demonstrates significant performance gain compared to LoRA (Adam), what is property of dataset such that the proposed optimization can results such improvement?

### Questions
See weaknesses

Questions:

1. As analyzed in at line 322, from time complexity perspective, the proposed method is r times slower than Adam, but in Table 4, it is only 8% slower, it will be interesting to elaborate more the inconsistency.

2. At table 3, when LoRA rank is higher, the improvement over other methods become smaller, I wonder the authors have any insight of that?

3. Why the LAMB paper is cited twich in different way? (line 642, 646)

4. At line 345, LoRA-Rite should be LoRA-RITE for consistency.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on improving LoRA, a novel adaptive matrix preconditioning method, and names the proposed method as LoRA-RITE for LoRA optimization. Authors argue that LoRA’s ability to decompose the fine-tuned weight Z in multiple ways is not the best approach for optimization, and they propose a new way for invariant decomposition. Authors have applied the new optimization function, named LoRA-RITE, on Gemma for several datasets and show strong performance on multiple LLM benchmarks.

### Strengths
* The overall mathematical proofs are reasonable and appear to be correct.
* With the implementation of LoRA-RITE, authors have shown significant improvement over other optimizers on different language benchmarks.

### Weaknesses
I do not have major technical concerns for this paper. It is relatively solid in both performance and implementation analysis. Authors mentioned that they are searching for the learning rate between 2e-6 and 2e-2; it would be interesting to present the best learning rate for different strategies in this work after the search.

### Questions
Please check weaknesses section. Authors mentioned that they are searching for the learning rate between 2e-6 and 2e-2; it would be interesting to present the best learning rate for different strategies in this work after the search.

### Soundness
4

### Presentation
4

### Contribution
3
