# FedDA: Faster Adaptive Gradient Methods for Federated Constrained Optimization

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Federated learning (FL) is an emerging learning paradigm where a set of distributed clients learns a task under the coordination of a server. The FedAvg algorithm is one of the most widely used methods in FL. In FedAvg, the learning rate is a constant rather than changing adaptively. Adaptive gradient methods have demonstrated superior performance over the constant learning rate schedules in non-distributed settings, and they have recently been adapted to FL. However, the majority of these methods are designed for unconstrained settings. Meanwhile, many crucial FL applications, like disease diagnosis and biomarker identification, often rely on constrained formulations such as Lasso and group Lasso. It remains an open question as to whether adaptive gradient methods can be effectively applied to FL problems with constrains. In this work, we introduce \textbf{FedDA}, a novel adaptive gradient framework for FL. This framework utilizes a restarted dual averaging technique and is compatible with a range of gradient estimation methods and adaptive learning rate schedules.  Specifically, an instantiation of our framework FedDA-MVR achieves sample complexity $\tilde{O}(K^{-1}\epsilon^{-1.5})$ and communication complexity $\tilde{O}(K^{-0.25}\epsilon^{-1.25})$ for finding a stationary point $\epsilon$ in the constrained setting with $K$ be the number of clients. We conduct experiments over both constrained and unconstrained tasks to confirm the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an adaptive gradient approach for federated constraint optimization. While existing schemes have focused separately on federated optimization and adaptive gradient approaches for the centralized setting, they combine these two lines of research. Specifically, they derive order results for the convergence and the communication complexity of their proposed scheme and perform numerical experiments for a variety of homogenous and non-homogenous datasets.

### Strengths
The authors have filled a missing gap in proposing adaptive gradient schemes for FL, which did not seem to exist in the open literature before. This is useful for constraint optimization in a federated setting, for example for regularization.

### Weaknesses
To my opinion, there are two major weaknesses. First, I think that the underlying idea of combining dual averaging with federated constraint optimization is fairly straightforward. The merit of the work is rather in the theoretical order complexity results. Specifically, the application of mirror descent to adaptive gradients in the dual space, while novel in the federated setting, is not conceptually complex. The core idea of disentangling the constraint condition from the adaptive gradient updates, while practically useful, lacks significant theoretical depth. The aggregation of dual states by fixing the adaptive matrix during local updates, although a key component, is a relatively simple averaging technique. The theoretical analysis, while challenging, does not overcome the conceptual simplicity of the approach.

Second, the paper lacks important information, and thus it is difficult to evaluate their results, specifically with respect to the adaptive gradient results. Specifically, they state on page 5 that the mapping matrix H is updated in line 11 of Algorithm 1, however, line 11 is not present in that algorithm. This makes it difficult to understand how the adaptive gradient is actually implemented and how it relates to the theoretical claims.

### Questions
What is the comparison of the sample and communication complexity to other non-adaptive schemes? A little table containing these results would be useful.

In Figs. 1 and 2, the third plot from the right is not explained in the text. Also, here, essentially the gain of FedDA is due to the addition of a regularization constraint (Lasso). Is there also a gain over benchmark schemes (as FedAvg) for settings where these schemes are not overfitting and why?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach to addressing the problem of constrained federated learning by leveraging adaptive gradient methods. In conventional, non-federated contexts, various techniques and algorithms are available for finding local minimizers of functions, with adaptive gradient methods being particularly effective. The authors extend this idea into the federated learning framework by creating a general adaptive gradient framework.

This framework includes multiple adaptive gradient methods that rely on a restarted dual averaging technique. The authors begin by adopting a mirror descent perspective of adaptive gradient methods. The central concept in this paper is that if all clients share a common mirror map, they will operate in the same dual space. Consequently, the server can aggregate the local dual states of different clients effectively.

The paper provides a theoretical analysis of the convergence rate for a specific instantiation of this framework, which employs a momentum-based variance reduction technique. To validate their approach, the authors conduct empirical experiments on various datasets, demonstrating its effectiveness.

### Strengths
- The authors propose an algorithm that solves the under-explored field of constrained federated learning with optimal convergence rates for the constrained setting (up to my knowledge).
- The algorithm proposed by the authors is projection-free which is remarkable in a constrained optimization problem.

### Weaknesses
 - I found the paper to be poorly written and presented.
- While I did not found the proposed method to be highly competitive in the unconstrained setting, I believe it holds significant promise in the constrained setting. In my view, the authors should have emphasized the motivation and results from this perspective, rather than aiming to compete with potentially more efficient existing methods.
- This algorithm is more computationally demanding compared to other algorithms. The added computational cost arises from computing an argmin at each iteration. It remains unclear whether, with this additional step, the proposed algorithm maintains the same level of computational efficiency as its competitors and achieves similar theoretical and experimental results within the same computational budget.
- While the assumptions made by the authors are common in the analysis of adaptive gradient methods, I find some of them to be rather restrictive, particularly Assumptions 5.1 and 5.4. In light of this observation, the comparison with non-adaptive methods seems somewhat unfair.

### Questions
- Can we check that assumption 5.4 really holds for the provided update of the adaptive matrix in the case of the momentum-based variance reduction instantiation?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose FedDA, an adaptive gradient method for constrained optimization in the Federated Learning context. The proposed method builds on top of previously released approaches in local adaptive gradients, and Federated composite optimization. The authors make their claims clear with both theoretical and experimental results (under homogeneous and heterogeneous data distributions). The main motivation behind their approach is to accelerate federated constrained optimization, by adopting the Mirror Descent view of momentum-based acceleration methods.

### Strengths
1- The method FedDA is general and can incorporate several adaptive gradient methods.

2- FedDA-MVR, the momentum-based variance-reduction gradient estimation, achieves the optimal  iteration complexity rates of non-convex stochastic optimization, without bounded gradient assumption.

3- FedDA performs better or on par with existing methods, on constrained biomarker identification tasks. FedDA-MVR performs well on image classification tasks, even on the challenging non-i.i.d. setting (Fig.12 in appendix).

Overall, the authors provide a clear overview of dual and/or adaptive Federated methods both theoretically (Table.1) and numerically (>5 concurrent methods tested in Fig.3).

### Weaknesses
1- $\tilde{x}_t$ in equation.9 is not defined in the main text. In particular, how do you compute the L2 distance in between $x_t$ and $\tilde{x}_t$? Your random variable $\mathcal{G}_t$ gives an upper-bound (rk.B.17) of L2-norm of the gradient on $\tilde{x}$ in the unconstrained case. Can we obtain the same for $x$? If yes, is the convergence rate to first order stationary point the same ? It is unclear how the virtual global state $\tilde{x}_{\tau, i}$ relates to the actual global state $x_\tau$ used in the algorithm, especially since the update in Algorithm 1 uses $x_\tau$ directly, not $\tilde{x}_{\tau, i}$. The connection between the theoretical analysis using $\tilde{x}_t$ and the practical implementation using $x_\tau$ needs to be explicitly clarified. Specifically, the manuscript should detail how the convergence results for $\tilde{x}_t$ translate to convergence guarantees for the actual iterates $x_\tau$. The current presentation leaves a gap in understanding how the theoretical analysis directly supports the practical algorithm.

2- I understand fine-tuning NNs on large image classification tasks can be time consuming. However, did you carefully tune the hyper-parameters for FedAvg method? FedAvg is known to perform well under the unconstrained homogeneous setting, but is below $45$% of test accuracy in your experiment on CIFAR-10 (homogeneous; Fig.3). Maybe playing on the local step value $I$, or increasing the batch size (fixed at $16$ in your experiments) can give better gradients estimates, and better performances for FedAvg. The choice of a batch size of 16 seems unusually small for CIFAR-10, and it's not clear if this choice was made to intentionally handicap FedAvg. The manuscript should provide a more detailed justification for the hyperparameter choices, especially for the baseline methods, to ensure a fair comparison. A more thorough hyperparameter search for FedAvg, including varying the local steps and batch size, is needed to establish a reliable baseline for comparison.

3- Some typos about referencing your algorithms can be confusing (see details in the Questions section below).

### Questions
1- At the end of page.5, I think there is a typo about lines 9, 10, 11 of your Algo.1. In particular there is no line.11 in your Algo.1.

2- Minor: Please check your references before updating the final version. For instance the MiME paper is cited twice (on page.11 and on page.12). There is also a typo at the beginning of Section.6.1: PATHMN(I)ST.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
