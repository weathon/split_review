# Learning under Temporal Label Noise

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Many time series classification tasks, where labels vary over time, are affected by label noise that also varies over time. Such noise can cause label quality to improve, worsen, or periodically change over time. We first propose and formalize temporal label noise, an unstudied problem for sequential classification of time series. In this setting, multiple labels are recorded over time while being corrupted by a time-dependent noise function. We first demonstrate the importance of modelling the temporal nature of the label noise function and how existing methods will consistently underperform. We then propose methods that can train noise-tolerant classifiers by estimating the temporal label noise function directly from data. We show that our methods lead to state-of-the-art performance under diverse types of temporal label noise on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript introduced temporal label noise in time series classification tasks and proposed a novel framework that are robust to it. Experiments were conducted on 4 datasets with synthetic noise injection and a real-world noisy labelled dataset, in which the method proposed in the manuscript is superior to other methods. The authors also visualized the dynamic evolution of label noise over time.

### Strengths
1.	The problem proposed by the authors is novel and interesting, and they evaluate it on real-world datasets.
2.	The method introduced in the manuscript is cleverly crafted and has a theoretical foundation.

### Weaknesses
1.	In many settings, the performance of Plug-In method is inferior to that of static methods.
2.	Only one of the five datasets in the manuscript contains both clean and noisy labels. In the remaining real-world scenarios, there is no experimental evidence to confirm that “the label noise evolves over time” actually exists.
3.	The experimental scenarios are focused on healthcare; validating the work in more diverse scenarios would broaden its applicability.

### Questions
1.	What is the meaning of variable d in line 126? Is that mean a multivariate time series with d variables?
2.	When performing a train-test split on the datasets, were individuals also split?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper discusses the problem of learning from time series classification task, where the label noise can vary over time. Each instance is a sequence over T time steps, where at iteration $t$ we have access to the features at time $t$, and a noisy label $\tilde y_t$ obtained from the true label $y_t$. Each of this instance is i.i.d., and the assumption is that the true label $y_t$ at time $t$ only depends on the past features $x_{1:t}$, and the noisy labels are conditionally independent to the features given by the true labels. In particular, the authors assume there exists a noise mapping $Q_t$ that describes the noise process at time $t$. They propose a novel method to learn a classifier that maps sequences $x_{1:t}$ to a label $y$. This model simultaneously approximates the noisy mapping $Q_t$ (Eq 3), that is used to approximate the true labels, which are used during training

### Strengths
Learning from time series data is an interesting problem. The paper addresses a challenging problem, where the label noise can change over time, and it is well-motivated. Overall, the introduction of the paper and the experimental sections are well-written and easy to follow. I found the use of the minimum-volume simplex assumption as an objective to solve the problem to be intriguing.

### Weaknesses
 (**important**). The appendix of the paper is only a draft and it looks like it was not finished to be written. It also seems to be dissociated to the main paper.
- Appendix A is self contained and not referenced in the main paper. It is not discussed what the content of this section adds as a contribution.
- Appendix B looks dissociated to the main paper. First of all, three assumptions are introduced (they seems related to the 2 assumptions used in the main paper. In this case, why re-introduce them, and why do we use 3 assumptions rather than 2?). Most of the proofs are just a sequence of mathematical equations with text. Lines 810 to 840 are just a sequence of equations without text (maybe do a table?). The proof of Proposition 1 does not appear, which is only the theoretical result in the main paper (is Theorem 3 the proof of Proposition 1? Why does it have  different notation?).
- Section G.2 is empty. Page 25 to 47 include a sequence of a lot of figure without almost no text. I recommend the authors to only include the figures that are used to “say” something, together with a text explaination.

The technical section is also sometimes unclear.

Notations is sometimes unclear. What is q_t in line 140? According to the notation defined in the paper $\mathcal{X} \subseteq \mathbb{R}^{d \times T}$, but the function $h_{\theta}$ that has domain $\mathcal{X}$ can also have an input matrix $d \times t$.

There is no comment on the assumptions 1 and 2 (except that they are two standard assumptions). I believe a few lines commenting on those assumptions would be helpful.

In lines 259-261, why is the Frobenius norm a convex surrogate for the volume? (A citation is also probably needed).

In Line 260, should $R_t$ be defined over $\tilde{y}$ rather than $y$?

 In lines 262-264, my understanding is that $\lambda$ is the Lagrange multiplier of the constraint of Equation~2. I would be clearer on this, since $\lambda$ does not appear in Eq 2.

### Questions
See also weakness.

The model does not use the noisy label in the prediction (the predictor h_{\theta} only depends on x_{1:t}).  I believe it would be interesting to include the noisy label in the prediction of the true label (i.e., if the noisy label is always accurate, can we use it for prediction? I understand this is a slightly different setting, as the goal of the paper is to learn a predictor).   

The fact that we learn a noisy label structure Q_w(t) that is “continual” over time seems implicit in Eq. (3). However, it is not clear what the difference is between Eq(3) and the model discussed in “discontinuous estimation”. It seems to me that $t$ is an integer, and $Q_w(t)$ could be completely different than $Q_w(t+1)$ in principle (what is the temporal relationship discussed in line 274)

It is a bit unclear how Section 2, in particular section 2.2, is related to the proposed method in Section 3. It seems to me, that the “loss of the classifier” is embedded in the constraint of Equation 2. Lines 233-234 says that Eq(2) minimizes the forward temporal loss as in Def 2, but this loss does not actually appear on Equation 2.   

Typos: 277 continuuity

### Soundness
2

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
The paper proposes a model to incorporate varying noise rates for time-series classification. The method specifies a matrix-valued function indicating label-noise distribution. This noise function is incorporated into a forward temporal loss over noisy labels that is used to learn a classifier (using a neural net) minimizing the loss. The authors describe three approaches: continuous, discontinuous, and plug-in. They empirically evaluate these approaches in various benchmark datasets. They also demonstrate the approach in a real-world dataset within the healthcare domain in which the authors claim that the problem of temporal noisy labels is prevalent in time-series classification. The empirical results clearly indicate that the proposed approach works well compared to SOTA static approaches that treat noisy labels as static rather than temporal.

### Strengths
1) The formulation of the proposed methodology is clear and concise.
2) The motivation and subsequent real-world example is well demonstrated.

### Weaknesses
(1) It is not clear how is learning achieved when weights are initialized for each time step in discontinuous estimation. It looks like the dataset is small for the learning models to converge as all the datasets largely seem to have less than 1000 samples. Specifically, the discontinuous approach learns a separate noise transition matrix, Q_t, for each time step. Given the limited number of samples, it is unclear if the optimization process can reliably estimate these parameters, especially when the number of classes is not small. The paper does not provide sufficient detail on the optimization procedure for this discontinuous case, such as the learning rate, batch size, or number of epochs used for training each Q_t. This lack of detail makes it difficult to assess the robustness of the approach.
(2) Can the estimator in the discontinuous case be replaced by a simpler model (with lesser number of parameters)? If so, can such an alternative be used as baseline mechanisms to compare for temporal noise (as all alternative mechanisms shown in the paper are for static cases)? The paper does not explore the impact of the complexity of the noise model on the overall performance. A simpler model, such as a linear model or a low-rank approximation of Q_t, could potentially achieve similar performance with fewer parameters and less computational cost. It would be beneficial to compare the proposed method against such simpler alternatives to better understand the trade-off between model complexity and performance.
(3) It is interesting that both continuous and discontinuous estimations perform quite similarly on the real-world stress detection example. Does this mean that the proposed approach works best when there is large variance in noise rates? The similar performance of continuous and discontinuous methods on the stress detection dataset raises questions about the practical utility of the more complex continuous approach. It is not clear if the continuous approach offers any significant advantages over the discontinuous approach in real-world scenarios. Further investigation is needed to determine the conditions under which each method performs best, and whether the added complexity of the continuous approach is justified.

### Questions
(1) Is there an assumption that all data instances have equal number of time steps?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the problem of temporal label noise, where label quality fluctuates over time due to time-dependent noise. This type of noise may improve, deteriorate, or change periodically, impacting the accuracy of predictions. The authors define this problem and highlight that existing methods fail to handle the temporal aspect of label noise effectively. They propose methods to estimate the time-varying noise function directly from data, allowing the development of noise-tolerant classifiers. Experiments on real-world datasets validate their proposal, demonstrating its effectiveness under various types of temporal label noise.

### Strengths
1. The problem of Temporal Label Noise is both interesting and important, and this paper is the first to formally define it.

2. The paper is well-organized, clearly written, and easy to follow.

3. The mathematical symbols and equations are well-defined and easy to understand.

### Weaknesses
1. My primary concern is with the problem formulation, or more specifically, the goal of the problem. In Section 2.1, the paper aims to "estimate parameters $\hat{\theta}$ for a model robust to noise," which implicitly assumes the existence of a **fixed and static optimal model** $\theta^\star$—i.e., that p(y_t|x_t) remains consistent across all timestamps. However, in time-series problems, the environment is constantly changing, and the optimal model for different timestamps should also be changing. This assumption of a static optimal model may limit the applicability of the proposed method in real-world scenarios where non-stationarity is prevalent.

2. The other major concern relates to the methodology. The paper appears to assume that the function Q is known to the learner, and focuses only on optimizing the parameter w. However, I think that **obtaining an appropriate function Q is the most challenging aspect of this problem**. Although in Section 3.2, the authors select Q as a fully connected neural network as a general form for the practical scenarios, it seems to be inconsistent with the earlier discussions in Table 1. Specifically, while the authors claim that their method can capture a wide variety of temporal noise using a DNN for Q, the choice of a specific function class (DNN) limits the types of noise that can be effectively modeled. The learner does not learn the type of noise function, but rather the parameters of a pre-defined function class, which is a crucial distinction.

3. Another concern is about the experiments. The authors seem to only conduct experiments on low-dimensional datasets. I think that including experiments on larger-sized datasets with higher dimensionality and longer time series would strengthen the results and make the findings more convincing. The current experiments may not fully demonstrate the scalability and robustness of the proposed method in more complex real-world settings.

### Questions
See Weaknesses above

### Soundness
3

### Presentation
3

### Contribution
2
