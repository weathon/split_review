# Towards Learning High-Precision Least Squares Algorithms with Sequence Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
This paper investigates whether sequence models can learn to perform numerical algorithms, e.g. gradient descent, on the fundamental problem of least squares. Our goal is to inherit two properties of standard algorithms from numerical analysis: (1) machine precision, i.e. we want to obtain solutions that are accurate to near floating point error, and (2) numerical generality, i.e. we want them to apply broadly across problem instances. We find that prior approaches using Transformers fail to meet these criteria, and identify limitations present in existing architectures and training procedures. First, we show that softmax Transformers struggle to perform high-precision multiplications, which prevents them from precisely learning numerical algorithms. Second, we identify an alternate class of architectures, comprised entirely of polynomials, that can efficiently represent high-precision gradient descent iterates. Finally, we investigate precision bottlenecks during training and address them via a high-precision training recipe that reduces stochastic gradient noise. Our recipe enables us to train two polynomial architectures, gated convolutions and linear attention, to perform gradient descent iterates on least squares problems. For the first time, we demonstrate the ability to train to near machine precision. Applied iteratively, our models obtain $100,000\times$ lower MSE than standard Transformers trained end-to-end and they incur a $10,000\times$ smaller generalization gap on out-of-distribution problems. We make progress towards end-to-end learning of numerical algorithms for least squares.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper shows that the in-context learning setup for transformers cannot learn linear regression solutions with machine precision or numerical generality, and identify architectural and optimization factors that contribute to this phenomenon. It then proposes a new recipe for training to machine precision, including using BaseConv architecture, explicitly learning gradients, and reducing stochastic gradient noise.

### Strengths
The paper addresses a novel idea, namely learning high-precision algorithms with transformers. Their proposed training setup is well motivated by empirical observations.

### Weaknesses
1. Not all the notation needed to understand the main text is defined in the main text itself, e.g. What are the arguments to MULTIPLY? This makes some parts hard to understand without jumping to the appendix.

2. As part of their training setup, the authors propose to learn GD iterates explicitly, which requires knowing the value of the gradient. It is not clear to me why this setup is comparable to the standard in-context setup, which never explicitly computes gradients of the regression instance, or how this scenario could arise in practice.

3. It is unclear whether the proposed setup can generalize to practical scenarios beyond simple linear regression.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper observes empirically that standard (softmax-attention-based) transformers cannot achieve machine precision or numerical generality for solving linear regression and proposes an alternative polynomial architecture based on the BaseConv module that achieves nearly machine precision and numerical generality close to that of gradient descent (GD).

### Strengths
- The observations that standard transformers cannot solve linear regression to machine precision and are brittle to changes in distribution are interesting as they discredits a hypothesis supported by a plethora of recent literature that simplified and standard transformers learn to perform GD on linear regression problems. This is especially the case for the machine precision observation, as it is novel as far as I know (brittleness to changes in distribution has been observed elsewhere, e.g. [1] below).

- Theoretical and experimental claims are well-substantiated. The experiments are thorough and well-executed within the scope of the problem.

- The paper is very well-written.

### Weaknesses
While I think that observation that standard transformers are not learning to perform GD or Newton's method on linear regression is an important and relevant contribution, I'm not sure that coming up with a new architecture and developing a training procedure for solving linear regression to machine precision is of interest to the ICLR community, for the following reasons:

- Outside of scientific ML, solving linear regression to machine precision is not of interest. The paper does not discuss whether the proposed model and training procedure can shed insights on other problems besides solving linear regression to MP. It is unclear if the BaseConv architecture and its training methodology offer any benefits beyond this specific task. The paper should explore the potential for generalization to other numerical tasks or machine learning problems.

- Within scientific ML, it is not clear why practitioners would want to solve linear regression with a large and costly model that requires 50-80 layers to solve even small-scale problems to machine precision (as suggested by the experiments) rather than simply running GD. The computational overhead of the proposed method seems significant compared to standard iterative methods, and the paper lacks a discussion of the trade-offs between precision and computational cost. The authors should provide a more detailed analysis of the computational complexity of their approach and compare it to existing methods.

-  I can understand why it is interesting from a theoretical perspective, however to cater to a theoretical audience, I think the paper can use more theoretical development. In particular, I think the paper should move their proof of the inability of softmax attention to express multiplication from the appendix to the main body, and further develop this theory to show that standard transformers cannot express GD. Of the two theoretical results currently in the paper, one is borrowed from another paper, and the other is an informal statement that does not fully show the claimed expressivity of their proposed BaseConv model, since it does not show that BaseConv can achieve zero population gradient. The theoretical analysis should be expanded to include a more rigorous treatment of the training dynamics of BaseConv and provide a formal proof that it can achieve zero population gradient, which is crucial for establishing its theoretical properties.

(Minor) Missing related works:

[1] Zhang et al., Trained Transformers Learn Linear Models In-Context, JMLR 2024 -- Like Ahn et al. 2024, shows that linear transformers learn GD.

[2] Collins et al., In-Context Learning with Transformers: Softmax Attention Adapts to Function Lipschitzness, arxiv 2024 -- (and Related Works therein) -- also argues that standard transformers are not solving regression with GD.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates whether sequence models can learn to perform numerical algorithms. This paper finds that Transformer fails to meet criteria, such as machine precision and numerical generality, and instead propose alternative architectures that overcomes these limitations.

### Strengths
The strength of this paper is not only showing the limitation of Transformer, but also proposing alternative architecture that experimentally makes progress toward learning to solve numerical algorithms. Furthermore, there are several theoretical analyses to support experiments. For instance, it is interesting to show that, in Theorem D.34, single-head causal softmax attention cannot represent a square function.

### Weaknesses
As mentioned in Discussion and Limitations, proposed methods seem to be challenging in maintaining stable and precise training with deep networks.

### Questions
Out of interest, could you explore some theoretical analysis of proposed methods such as universal approximation or convergence of training? For instance, similarly in [Yun et al 2020] that shows the universality of Transformer, can we (expect to) show the universality of proposed architecture?

### Soundness
3

### Presentation
3

### Contribution
3
