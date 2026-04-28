# Minimax optimality of convolutional neural networks for infinite dimensional input-output problems and separation from kernel methods

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Recent deep learning applications, exemplified by text-to-image tasks, often involve high-dimensional inputs and outputs. While several studies have investigated the function estimation capabilities of deep learning, research on dilated convolutional neural networks (CNNs) has mainly focused on cases where input dimensions are infinite but output dimensions are one-dimensional, similar to many other studies. However, many practical deep learning tasks involve high-dimensional (or even infinite dimensional) inputs and outputs.
In this paper, we investigate the optimality of dilated CNNs for estimating a map between infinite-dimensional input and output spaces 
by analyzing their approximation and estimation abilities. 
For that purpose, we first show that approximation and estimation errors depend only on the smoothness and decay rate with respect to the infinity norm of the output, and their estimation accuracy actually achieve the {\it minimax optimal} rate of convergence.
Second, we demonstrate that the dilated CNNs outperform {\it any} linear estimators including kernel ridge regression and $k$-NN estimators in a minimax error sense, highlighting the usefulness of feature learning realized by deep neural networks.
Our theoretical analysis particularly explains the success of deep learning in recent high-dimensional input-output tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors consider the regression problem with infinite dimensional input and output. This setting  is motivated by recent applications such as image to text mapping.  For their target function, they assume that it belongs to certain gamma smooth spaces, which can be thought as extensions of mixed Besov spaces and anisotropic Besov spaces to infinite dimension output.  They consider learning this class of functions using dilated CNNs, which consists of multilayer convolutions followed by fully connected neural networks. Assuming that the ERM can be constructed, they characterize the approximation and estimation rates, and show that dilated CNNs achieve the minimax optimal rate for norm $p \geq 2$. They further prove a lower bound for linear estimator, which shows that dilated CNNs have better rates under some conditions.

### Strengths
- This paper belongs to a long tradition that has sought to study neural networks by decoupling the statistical from the computational aspects. By considering directly the properties of the empirical risk minimizers, one can probe the adaptivity property of neural networks by studying their decay rates for different function classes.  Within this context, the authors do a serious job in carefully constructing the function target class and deriving tight statistical rates.
- The paper is well written and clear despite the amount of technical notations.

### Weaknesses
 - As a general criticism of this line of work (not particular to this paper), it is unclear how much it informs practical neural networks. However, one can consider these results to be an important background for the study of neural networks.

 - As a general criticism, the lack of non-linear activation functions within the convolutional layers raises questions about the model's capacity to learn complex features. While linear operations are mathematically tractable, their practical relevance in capturing intricate patterns present in real-world data such as images or text remains limited. The absence of non-linearities might hinder the network's ability to model non-linear relationships, which are often crucial for accurate regression tasks. This choice could lead to a model that is less expressive than typical CNN architectures used in practice.

 - The definitions of 'adaptive' and 'non-adaptive' approaches, particularly in section 4.1 and the conclusion, are not sufficiently clear. The term 'adaptive' is used in the context of feature selection, but the mechanism by which dilated CNNs achieve this adaptivity, especially concerning the sparsity of the parameter $a$, is not explicitly detailed in the main text. Without a clear explanation, it is difficult to fully grasp the significance of this adaptive behavior and how it translates to improved performance compared to non-adaptive methods. The connection to the width dependency also requires further clarification.

### Questions
- Is there no activation in the convolutional layer?
- What does non-adaptive approach/adaptive approach refer to in section 4.1 and in the conclusion? I guess, this would improve the dependency over the width.
- As a personal taste, I would replace the last line of the abstract "explains the success of deep learning", by a sentence of the type "provide a theoretical basis for understanding the success".

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the optimality of dilated CNNs in estimating mappings between infinite-dimensional input and output spaces. Through analysis of their approximation and estimation capabilities, the authors establish that the accuracy of approximation and estimation errors is influenced by the smoothness and decay rate of the output relative to the infinity norm. They also provide evidence showing that dilated CNNs outperform linear estimators like kernel ridge regression and k-NN estimators in terms of minimizing estimation errors. This finding emphasizes the efficacy of feature learning accomplished by deep neural networks.

### Strengths
1. The paper provides a thorough analysis of the approximation and estimation abilities of dilated CNNs for estimating mappings between infinite-dimensional input and output spaces.

2. The authors demonstrate that the estimation accuracy achieved by dilated CNNs aligns with the minimax optimal rate of convergence.

3. The authors show that dilated CNNs are adaptive to the unknown smoothness structure.

### Weaknesses
1. The absence of empirical validation on real-world datasets weakens the practical relevance of the findings

2. The paper briefly mentions potential future directions for research but does not thoroughly discuss the limitations of the study

3. Assumption 3 seems to be a little bit strong. Could you provide a specific example to illustrate it more concretely?

4. The computational aspect can pose challenges due to the infinite-dimensional nature of both the input and output, particularly when dealing with large-scale data.

5. Can the dilated CNN be used to learn linear operator? Will the estimation rate be improved?

### Questions
1. Assumption 3 seems to be a little bit strong. Could you provide a specific example to illustrate it more concretely?

2. The computational aspect can pose challenges due to the infinite-dimensional nature of both the input and output, particularly when dealing with large-scale data.

3. Can the dilated CNN be used to learn linear operator? Will the estimation rate be improved?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study the setting of estimation in infinite dimensional input and output using dilated CNNs. They derive approximation and estimation errors when the true function satisfies certain smoothness type conditions. Additionally, they show that these CNNs achieve the minimax optimal rate for estimation accuracy. Finally, they also show that dilated CNNs outperform other models for infinite dimensional estimation like kernel ridge regression and k-NN again in a minimax sense.

### Strengths
1. The main theoretical results appear to be novel, and are a significant improvement over previous results.
2. The convergence rate of the estimation error of the dilated CNNs is also shown to be minimax optimal up to poly-log factors under a specific regime.
3. Further, the paper also contains theoretical results which show that dilated CNNs outperform linear estimators, which seems to provide some theoretical justification for the successes of deep learning in high-dimensional spaces.
4. The paper is well written and the proofs seem correct.

### Weaknesses
1. The results are specific to the dilated CNN model, and it is not clear how to extend them other model classes.



### Questions
1. Can the authors provide some more intuition and insight on how the parameter $r$ affects the class of functions being studied? 
2. As a followup, what is the motivation behind where assumption 3 comes from, and can you say anything about example problems in practice that satisfy this assumption?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
