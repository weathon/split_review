# Breaking Neural Network Scaling Laws with Modularity

- Decision: Reject
- Scores: 8, 5, 6

## Abstract
Modular neural networks outperform nonmodular neural networks on tasks ranging from visual question answering to robotics. These performance improvements are thought to be due to modular networks' superior ability to model the compositional and combinatorial structure of real-world problems. However, a theoretical explanation of how modularity improves generalizability, and how to leverage task modularity while training networks remains elusive. Using recent theoretical progress in explaining neural network generalization, we investigate how the amount of training data required to generalize on a task varies with the intrinsic dimensionality of a task's input. We show theoretically that when applied to modularly structured tasks, while nonmodular networks require an exponential number of samples with task dimensionality, modular networks' sample complexity is independent of task dimensionality: modular networks can generalize in high dimensions. We then develop a novel learning rule for modular networks to exploit this advantage and empirically show the improved generalization of the rule, both in- and out-of-distribution, on high-dimensional, modular tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the sample complexity of modular neural networks and shows theoretically how the sample complexity of modular networks doesn't depend on the intrinsic dimensionality of the input. This is proven for linear models. The theory is supported by experiments on 1) sin wave regression and 2) compositional CIFAR10. The paper further proposes a learning rule to ensure the modularity of the task is aligned with the modularity of the network.

### Strengths
1. This is the first paper to conduct a rigorous theoretical analysis of modular neural networks. Understanding the empirical success of modular neural networks is an important open problem. 

2. The theoretic analysis and the effect of different terms in the generalization bound are presented clearly. 

3. Assumptions for the theoretical analysis are presented clearly. 

4. Related work is covered well and in thorough detail.

### Weaknesses
1. Including synthetic experiments in the linear model to demonstrate how the sample complexity changes for modular and non-modular networks in a specific setting.

### Questions
N/A

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a theoretical model of NN learning, specifically predicts that while the sample complexity of non-modular NNs varies exponentially with task dimension, sample complexity of modular NNs is independent of task dimension. The authors then develop a learning rule to align NN modules to modules underlying high-dimensional modular tasks, and presents empirical results which demonstrate improved performance of modular learning.

### Strengths
The paper presents the first theoretical model to explicitly compute non-asymptotic expressions for generalization error in modular architectures, develops new modular learning rules based on the theory and empirically demonstrated the improved performance of the new method.

### Weaknesses
Validation of theoretical results is only shown in the appendix, with large discrepancy between theoretical predictions and numerics, I think more empirical evaluations are needed to verify the theoretical result. The discrepancy between the predicted and actual test loss, particularly the underestimation of the loss for small training data and the smaller-than-predicted error spike at the interpolation threshold, raises concerns about the applicability of the linear model approximation to the highly non-linear neural network. Furthermore, the limited range of the similarity score in Figure 4, and also in Figure 3b, makes it difficult to assess the practical significance of the improvement over the baseline. The small absolute differences in similarity scores, even if statistically significant, might not translate to substantial improvements in real-world performance or indicate that the method is truly capturing the underlying modular structure.

### Questions
1. What causes the large deviation of the test loss between actual and predicted in Figure 5?
2. In figure 4 (also figure 3b), the total range of the similarity score is quite small, it is therefore difficult to say whether the result is a significant improvement from baseline.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper seeks to understand scaling laws for modular neural networks and proposes a method for training them. Modular neural network here refers to models that sum the output of their constituent modules each of which receive (different) low-dimensional projections of the input. The paper theoretically shows that when the modules are linear neural networks that receive a linear projection of the input into a fixed dimensional space, and the data comes from a model of the same form, sample complexity is independent of the task intrinsic dimension $m$ (in contrast to the monolithic case where it is exponential in $m$). The paper then proposes a kernel-based rule to learn the initializations of the input projections from data and test the empirical performance on a sine wave regression task and compositional CIFAR.

### Strengths
Understanding the sample complexity of training modular vs. monolithic neural networks is an important open problem for which a theoretical contribution is potentially impactful.
The theory identifies a reasonable setting for a tractable analysis and is overall convincing (without having checked the proofs in the appendix).
Overall the paper is well presented and transparent about the merits and limitations of the analysis.

### Weaknesses
The scaling behaviour is studied theoretically in the case of linear neural networks for tractability. A more thorough empirical investigation to what extent this scaling law is practically relevant in the nonlinear setting would have been useful. As far as I understand the experiments conducted do not reflect the theoretical result of constant sample complexity in the input dimension. I was missing a discussion on this point.

I am a bit worried about the reproducibility of the empirical part of the paper since no code was provided as part of the submission. I also encourage the authors to specify the exact number of seeds per experiment in Figure 3b as "up to five seeds" as stated in the caption could technically mean only one seed is reported.

### Questions
1. The modular learning rule minimizing the norm of the $\theta_i$ is applied as a pretraining step assuming that the $\varphi(X;\hat{U}_i$ are sufficiently expressive. Since this is before training, can you elaborate why this assumption might be justified and to what extent the algorithm is robust to a violation of it? 
2. There are discrepancies between the theory and toy model in Figure 5 as the paper points out in App A.2. Can you elaborate why this is not a matter of concern for the theory, i.e. what exactly causes the mismatch?
3. Figure 5 is missing labels and the caption is a bit sparse. Could you specify how exactly the four plots differ? Maybe adding a colour bar to indicate the values of the light lines could be helpful? How do the theoretical predictions look like for individual (light) lines?
4. Figure 12 is missing a legend for what the colours encode. Could you please clarify?

Suggestions / typos:
- I think it would be useful to show both the theoretical prediction and empirical validation in Figure 2 (similar to Figure 5 in Appendix A).
- Page 7 "and the test loss and dependence of the test loss"

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
