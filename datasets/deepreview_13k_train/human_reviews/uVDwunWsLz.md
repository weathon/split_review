# Benign Overfitting in Single-Head Attention

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
The phenomenon of \emph{benign overfitting}, where a trained neural network perfectly fits noisy training data but still achieves near-optimal test performance, has been extensively studied in recent years for linear models and fully-connected/convolutional networks. In this work, we study benign overfitting in a single-head softmax attention model, which is the fundamental building block of Transformers. We prove that under appropriate conditions, the model exhibits benign overfitting in a classification setting already after two steps of gradient descent. Moreover, we show conditions where a minimum-norm/maximum-margin interpolator exhibits benign overfitting. We study how the overfitting behavior depends on the signal-to-noise ratio (SNR) of the data distribution, namely, the ratio between norms of signal and noise tokens, and prove that a sufficiently large SNR is both necessary and sufficient for benign overfitting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies benign overfitting in a single-head attention model, proving that under certain signal-to-noise ratio (SNR) conditions, the model achieves benign overfitting after two gradient descent steps or through a max-margin solution.

### Strengths
The paper provides the theoretical analysis of benign overfitting in attention mechanisms, expanding understanding beyond linear and CNN models. It also establishes conditions for benign overfitting.

### Weaknesses
This paper relies on overly simplified settings and assumptions for its theoretical analysis. Additionally, its approach heavily depends on prior research, offering limited novelty and inheriting weaknesses from existing studies.

It seems that this paper primarily combines ideas from two prior works, "Benign Overfitting in Two-layer Convolutional Neural Networks" (Cao et al., NeurIPS 2024) and "Max-Margin Token Selection in Attention Mechanism" (Ataee Tarzanagh et al., NeurIPS 2024). By relying heavily on these works, it lacks novelty and inherits their weaknesses without addressing them. 
Additionally, it seems that the weaknesses in these individual studies interact in a way that undermines each other's strengths.

Q1. Can the analysis extend to multiple tokens? Also, is it possible to relax the strong signal-noise separability assumptions that have been identified as limitations in existing studies?
In Cao et al.'s CNN work, only two patches are considered, which has been criticized in OpenReview for oversimplifying the signal and noise separation. Similarly, this paper assumes only two tokens and retains assumptions of orthogonality and separability between signal and noise, as in Cao et al.'s paper. However, in an attention model, especially one focused on token selection, analyzing only two tokens is even more problematic. For applications like Vision Transformers and sequence modeling, the ability to select among multiple tokens is fundamental to the attention mechanism, and overlooking this critical functionality limits the paper’s scope. While Ataee Tarzanagh et al. analyze max-margin solutions for multi-token scenarios, this paper fails to leverage those benefits by retaining the two-token simplification.

Q2. What is the essential difference between this work and benign overfitting in a linear model with input by linearly interpolating signal and noize vectors?
Due to the highly simplified setup, the analysis in this paper appears comparable to a straightforward two-vector linear interpolation. With two tokens—one signal and one noise—the role of attention is reduced to a linear interpolation between the two vectors. Since the signal is fixed and noise orthogonal, analyzing the behavior of the attention weights boils down to tracking a single-dimensional parameter representing this linear combination like lambda*singal+(1-lambda)*noize. As a result, the model resembles a simple two-class linear classification task using signal-noise interpolation. Thus, is this analysis merely a study of benign overfitting in a linear model? Given the extensive research on benign overfitting in linear models, it is unclear what essential differences this work offers from simpler linear models.

Q3. Is it feasible to analyze benign overfitting conditions under fully converged solutions?
Although Cao et al.'s CNN paper contributes by analyzing gradient descent dynamics, this paper only examines two-step gradient descent without exploring convergence behaviors in depth. While it does provide max-margin solution analysis, it lacks a general guarantee of convergence to this solution using gradient descent. This limitation stems from a similar issue in Ataee Tarzanagh et al.'s study, where convergence guarantees hold only for initializations close to the solution—a known weakness that seems inherited

### Questions
It seems that this paper primarily combines ideas from two prior works, "Benign Overfitting in Two-layer Convolutional Neural Networks" (Cao et al., NeurIPS 2024) and "Max-Margin Token Selection in Attention Mechanism" (Ataee Tarzanagh et al., NeurIPS 2024). By relying heavily on these works, it lacks novelty and inherits their weaknesses without addressing them. 
Additionally, it seems that the weaknesses in these individual studies interact in a way that undermines each other's strengths.

Q1. Can the analysis extend to multiple tokens? Also, is it possible to relax the strong signal-noise separability assumptions that have been identified as limitations in existing studies?
In Cao et al.'s CNN work, only two patches are considered, which has been criticized in OpenReview for oversimplifying the signal and noise separation. Similarly, this paper assumes only two tokens and retains assumptions of orthogonality and separability between signal and noise, as in Cao et al.'s paper. However, in an attention model, especially one focused on token selection, analyzing only two tokens is even more problematic. For applications like Vision Transformers and sequence modeling, the ability to select among multiple tokens is fundamental to the attention mechanism, and overlooking this critical functionality limits the paper’s scope. While Ataee Tarzanagh et al. analyze max-margin solutions for multi-token scenarios, this paper fails to leverage those benefits by retaining the two-token simplification.

Q2. What is the essential difference between this work and benign overfitting in a linear model with input by linearly interpolating signal and noize vectors?
Due to the highly simplified setup, the analysis in this paper appears comparable to a straightforward two-vector linear interpolation. With two tokens—one signal and one noise—the role of attention is reduced to a linear interpolation between the two vectors. Since the signal is fixed and noise orthogonal, analyzing the behavior of the attention weights boils down to tracking a single-dimensional parameter representing this linear combination like lambda*singal+(1-lambda)*noize. As a result, the model resembles a simple two-class linear classification task using signal-noise interpolation. Thus, is this analysis merely a study of benign overfitting in a linear model? Given the extensive research on benign overfitting in linear models, it is unclear what essential differences this work offers from simpler linear models.

Q3. Is it feasible to analyze benign overfitting conditions under fully converged solutions?
Although Cao et al.'s CNN paper contributes by analyzing gradient descent dynamics, this paper only examines two-step gradient descent without exploring convergence behaviors in depth. While it does provide max-margin solution analysis, it lacks a general guarantee of convergence to this solution using gradient descent. This limitation stems from a similar issue in Ataee Tarzanagh et al.'s study, where convergence guarantees hold only for initializations close to the solution—a known weakness that seems inherited

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work examines the phenomenon of benign overfitting in a single-head attention model on a binary classification task with label noise. First, they show that two steps of GD, under signal-to-noise ratio (SNR) of $\Theta(1/\sqrt{n})$, exhibit benign overfitting. Next, they examine the max-margin/min-norm interpolator and show that the SNR requirement in that case is only $\Omega(1/\sqrt{n})$. Finally, they show that this is necessary (upto some constant factors), because for lower SNR, the max-margin interpolator exhibits harmful overfitting.

### Strengths
This work takes a step towards extending the understanding of benign overfitting from other neural network architectures to attention models.

Overall, the paper is well-written and easy to follow.

### Weaknesses
 - The main weakness is that the results are under very strong assumptions.
    - First, the authors consider prompt attention, not self-attention, which is the more prevalent attention architecture. The authors also assume that the number of tokens is two, which is far from practice. This simplification significantly limits the applicability of the results to realistic scenarios. The behavior of self-attention, with its quadratic interactions between tokens, can be substantially different from prompt attention, and the two-token assumption prevents the model from capturing the complexities of multi-token interactions.
    - Second, the authors only analyze two steps of gradient descent (GD), and not the full trajectory. While the experiments show that with large step size, the model converges in two steps of GD, the theoretical results, which are the main contribution, seem rather weak since only two steps of GD are analyzed. This is a significant limitation because the long-term behavior of gradient descent can exhibit different dynamics, and the analysis of only two steps may not be representative of the full training process. It also raises concerns about the stability of the solution after the initial two steps.
    - Third, the authors assume that the parameters are initialized at zero, instead of random initialization, which is used in practice. This assumption simplifies the analysis but may not reflect the behavior of the model under more realistic initialization schemes. The initial gradient direction and the subsequent trajectory can be significantly influenced by the initialization, and zero initialization may lead to a different convergence behavior compared to random initialization.
    
    Given the strong assumptions, it is not clear what insights they offer about training attention models.
    
- Other minor suggestions:
    - There are some missing references in the related work section on optimization in transformers, such as [1-4].
    - In line 89, overfitting is misspelled.

### Questions
- Would the results generalize to a more realistic model, such as self-attention and with more than two tokens?
- Can the authors discuss the challenges for analyzing further steps for GD instead of just two steps?
- Can the authors include some discussion on how the SNR requirement for benign overfitting for self-attention compares with other architectures, particularly CNNs, since similar data models have been considered for benign overfitting in CNNs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper analyzes benign overfitting in single-head attention depending on the signal-to-noise ratio (SNR) of the data distribution.
GD with the logistic loss shows benign overfitting when SNR is $\Theta(1/\sqrt{n})$. For minimum-norm interpolators, the requirement for the SNR becomes weaker ($\Omega(1/\sqrt{n})$) and this is tight.

### Strengths
I couldn't check all the technical details, but surely this paper has its strengths as follows:

- This paper provides a clear characterization of the role of the SNR (i.e., that of $d$ and $n$) for benign overfitting.

### Weaknesses
 - Some theory appear to lack empirical evidence. Can we confirm Theorem 6,8,10 (in Section 4) with some experiments on the max-margin learning rule? Experiments in Section 6 seem like they are only for Theorem 4. If not, which experiments (figures) correspond to which theorem?
- It would be better to have experiments (or at least a discussion) on a relatively complex model (e.g., multi-head attention, multi-layer Transformer, more than two tokens). For example, a complex model may have similar behavior with the simple one used in Section 6. We may get some intuition from the experiments that a simple structure is enough to exhibit benign overfitting or some complex structures are crucial.
- The single-attention $S(XWq)$ or $S(Xp)$ considered in the paper is linear in $X$ before taking the softmax which is not usual attention as the authors consider the query vector $q$ independent of the input $X$. Is there any justification that we can use such simplification? This is a big limitation of this paper.



### Questions
- Can you define the (unusual) notations SNR $\geq \Omega(1/\sqrt{n})$ or SNR $\leq O(1/\sqrt{n})$ explicitly? Is it something like "SNR $\geq f(n)$ and $f(n)=\Omega(1/\sqrt{n})$"?
- Why does $I-\mu_1\mu_1^\top/\rho-\mu_2\mu_2^\top/\rho$ in the covariance make that the noise token is orthogonal to the signal one?
- Can you draw (final or $t=2$ test-accuracy) vs ($n/d$ or $n^2/d$) plot to get a better intuitive explanation?
- Can we somehow neglect the cross term $\sum_{i,j} y_iy_j\theta_j^{t=1}\xi_i^\top \xi_j$ without the assumption item 2, at least experimentally?
- What if we use a normalized noise $\xi \sim N(0, \Sigma/d)$ so that SNR $=\rho$ where $\Sigma=I_d-\mu_1\mu_1^\top/\rho-\mu_2\mu_2^\top/\rho$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates benign overfitting within single-head softmax attention models, foundational components of Transformers, by examining when these models can fit noisy training data while still generalizing effectively to test data. The authors provide theoretical conditions under which gradient descent with logistic loss leads to benign overfitting within two iterations, requiring a specific signal-to-noise ratio (SNR) scaled as $\Theta(1/\sqrt{n})$. Additionally, they show that minimum-norm (or maximum-margin) interpolation allows for benign overfitting with a relaxed SNR requirement of $\Omega(1/\sqrt{n})$. Empirical results validate these findings, demonstrating that a sufficiently large SNR and input dimension are essential for benign overfitting, while lower SNR leads to harmful overfitting. This study offers new insights into the benign overfitting behavior of attention mechanisms, highlighting theoretical and empirical conditions for achieving this phenomenon in single-head attention models.

### Strengths
- The authors provide a rigorous theoretical analysis, supported by empirical validation. The proofs are well-structured, with assumptions and conditions clearly stated, lending robustness to the theoretical results.  

- The paper is clearly written and structured, allowing readers to follow the logical flow of arguments and results.

### Weaknesses
 - Compared to [1], the data model in this paper is similar; however, the attention network considered here is relatively simple. For example, [1] trains both the query and key matrices, whereas this work only trains a single vector within the softmax function. This simplification reduces the complexity of the analysis significantly but may also limit the applicability of the findings to more complex attention networks.

- For benign overfitting with gradient descent, the requirement for both upper and lower bounds on the Signal-to-Noise Ratio (SNR) restricts the scope of the data model, potentially limiting the range of scenarios where the results apply. The necessity of an *upper* bound on the SNR is particularly concerning, as it implies that the benign overfitting phenomenon is not robust to arbitrarily strong signals, which seems counterintuitive. This limitation needs further justification and exploration.

- The data model only considers two tokens, which could constrain the generality of the findings. An analysis including more tokens or varying token arrangements would strengthen the applicability of the conclusions. The current setup does not explore how the attention mechanism behaves with multiple competing signals or noise sources, which is a common scenario in real-world applications.

- Minor: Big-O notation (line 100-101)

### Questions
- For **Assumption 3**, why is an upper bound on the Signal-to-Noise Ratio (SNR) necessary? Additionally, how would the results change if a different step size is used during training, such as a larger or smaller step size?

- For **Assumption 3**, what would be the effect of not using zero initialization? For instance, have you considered using Gaussian initialization, and if so, how would this impact the behavior of benign overfitting?

- In the experiments, have you considered using a heatmap for test accuracy to illustrate the separation condition based on SNR values? Such a visualization could help clarify the relationship between SNR and model generalization in different settings.

### Soundness
3

### Presentation
3

### Contribution
2
