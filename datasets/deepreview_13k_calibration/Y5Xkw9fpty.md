# Smooth Min-Max Monotonic Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
noindent
Monotonicity constraints are powerful regularizers in statistical modelling. They can support fairness in computer-aided decision making and increase plausibility in data-driven scientific models. The seminal min-max (MM) neural network architecture ensures monotonicity, but often gets stuck in undesired local optima during training because of partial derivatives of the MM nonlinearities being zero. We propose a simple modification of the MM network using strictly-increasing smooth minimum and maximum functions that alleviates this problem. The resulting smooth min-max (SMM) network module inherits the asymptotic approximation properties from the MM architecture. It can be used within larger deep learning systems trained end-to-end. The SMM module is conceptually simple and computationally less demanding than state-of-the-art neural networks for monotonic modelling. Our experiments show that this does not come with a loss in generalization performance compared to alternative neural and non-neural approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose modification to min-max networks by replacing max and min by appropriate log sum exp functions.

This is done to improve the learning signal.

Some theoretical/empirical analysis is provided.

### Strengths
The paper is very clear, I could understand most of it in first reading.

The authors consider an important problem: sometimes "worse" models can be empirically better as it is easier to optimise.

### Weaknesses
Are there different types of relaxation of min/max that can be used?

I think the results of type Thm 1 are not very meaningful as the network size can increase very quickly when epsilon decreases.

The empirical results are not very strong. Is e.g. ChestXRay statistically significant? The differences in Table 3 look mostly statistically insignificant.

### Questions
See above.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the training and empirical performance of neural networks and non-neural approaches that ensures monotonicity with respect to input parameters. The authors propose a new network module architecture based on min-max (MM) architecture [Sill (1997)] which aims to tackle the problem of silent neurons and non-smoothness properties by applying a LogSumExp function to the max/min function. The authors support their claims by providing empirical evidence on toy examples and on practical data sets.

### Strengths
1) This paper is well-written and is easy to follow. The authors presented their ideas and results clearly.
2) The proposed SMM architecture is simple and seems to be an intuitive way to ensure monotonicity through smoothening.
3) The authors did extensive comparisons of their proposed SMM against other models which aim to ensure monotonicity, and aided readers to understand the potential advantages of SMM over comparable models.

### Weaknesses
1) I am not entirely sure about the novelty of this idea of smoothening non-smooth neurons to address the problem of vanishing gradients or silent neurons in the context of monotonic networks. The main idea of this work of using LogSumExp to act as a smooth approximation while preserving monotonicity does not seem too non-trivial due to its popularity in statistic modelling. However, I am not familiar with the line of work with monotone networks thus I will defer this discussion to other reviewers.
2) While the empirical comparisons are sufficient, they do not provide evidence (especially after accounting the error bars) to suggest that SSM has significant advantage over existing approaches. It is then unclear why practitioners should prefer SSMs over LMNs or XGBoost.

### Questions
1) How should the scaling factor $\beta$ chosen in practice? My understanding is that tuning it to ensure that the output network is monotone is not trivial and requires retraining the entire network.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses an intriguing aspect of machine learning: monotonic modeling, focusing specifically on the min-max architecture. The authors thoroughly summarize various techniques and identify a key issue for min-max architecture known as the "silent neuron" problem. In response, they propose a smooth variant and develop what they term the SMM architecture. This new architecture demonstrates strong experimental results.

### Strengths
This SMM architecture is not only innovative but also well-motivated solution by transitioning from the conventional hard min-max to a LogSumExp-based approach. Furthermore, the paper establishes theoretical guarantees about model's approximation property when the parameter $\beta$ is sufficiently large.

The experimental results are another major strength of this work. The authors demonstrate the effectiveness of the smooth min-max (SMM) architecture, thereby confirming both the practicality and the potential of their approach.

### Weaknesses
One significant concern lies in the treatment of $\beta$ as a learnable parameter. The authors' exploration of this parameter is fascinating, particularly in light of Corollary 1's suggestion that a lower bound on fitting error is inherently linked to the value of $\beta$. This implies that a $\beta$ not sufficiently large would fail to approximate certain functions. Conversely, an excessively large $\beta$ might impact the training dynamics adversely, as some nearly silent neurons may remain untrained. 

While the authors utilize trainable $\beta$ in experiments, the paper could benefit from a deeper exploration of $\beta$'s behavior during training, such as its trajectory and its relationship with loss changes. Reporting the final values of $\beta$ after training would also have provided valuable insights. The paper lacks a clear explanation of how the optimization landscape changes with respect to $\beta$, and how that affects training. The potential for $\beta$ to get stuck in local minima, especially in relation to the vanishing gradient problem, is also not fully addressed. This is a critical gap in the analysis.

### Questions
The observation that test errors can vary significantly with different initial $\beta$ values raises an important question. 
Does it suggest that the optimization process may not fully converge or that $\beta$ plays a more complex role in the model's training dynamics than currently understood?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
