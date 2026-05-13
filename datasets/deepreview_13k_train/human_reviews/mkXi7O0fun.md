# Data Value Estimation on Private Gradients

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
For gradient-based machine learning (ML) methods commonly adopted in practice such as stochastic gradient descent, the de facto differential privacy (DP) technique is perturbing the gradients with random Gaussian noise. Data valuation attributes the ML performance to the training data and is widely used in privacy-aware applications that require enforcing DP such as data pricing, collaborative ML, and federated learning (FL). Can existing data valuation methods still be used when DP is enforced via gradient perturbations? We show that the answer is no with the default approach of injecting i.i.d. random noise to the gradients because the estimation uncertainty of the data value estimation paradoxically linearly scales with more estimation budget, producing estimates almost like random guesses. To address this issue, we propose to instead inject carefully correlated noise to provably remove the linear scaling of estimation uncertainty w.r.t. the budget. We also empirically demonstrate that our method gives better data value estimates on various ML tasks and is applicable to use cases including dataset valuation and FL.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper considers the question of data valuation under differential privacy. For each data point, we aim to produce a number describing the "value" of that example. This could be used later, for example in an auction. The paper focuses on adapting existing nonprivate techniques for data value estimation based on stochastic gradient descent to the private gradient descent setting.

I will note that this is a rather unusual goal within the study of differentially private algorithms, as we aim to infer details about each example, rather than statistics about the underlying dataset or distribution. At least one of the prior works cited, Wang et al. 2023, operates in a different privacy model: the $i$-th value estimates is released only to the $i$-th individual.

### Strengths
This is an interesting topic, clearly connected to prior work. There is a lot of interest in estimating data values.

The techniques here are non-trivial. It seems plausible to me that the experiments demonstrate a privacy-utility tradeoff that is acceptable for some uses.

### Weaknesses
I see three main issues with the submission. I look forward to discussion with the authors and other reviewers.

**First,** I did not understand why this notion of estimation uncertainty (Eq 3) is meaningful. An algorithm that always returns $\psi_j=0$ is perfectly private and has no variance. So I don't know how to interpret Proposition 5.3, which says that we can bound the variance by a constant. Is that good? Perhaps the correlated noise technique is simply bringing us closer to the $\psi_j=0$ example?

**Second,** I feel the paper is missing a basic discussion of what is possible here. Consider a setting where each example is blatantly either "valuable" or "not valuable." This is reasonable: maybe some examples are random noise. Here, the best private estimate of the value us randomized response, where each individual returns their true value with probability $e^\epsilon/(e^\epsilon+1)$. If, analogous to the experiment in Figure 3, 30% of examples are not valuable, then by Bayes theorem with $\epsilon=1$ we expect roughly 14% of examples that returned "valuable" to not be so.

Some passages may give the reader the wrong idea. Both the Remark on p4 and Appendix B.4 suggest one can accurately preserve the ranks under differential privacy (so that valuable data receives higher estimates). But, as the above example shows, privacy also constrains our ability to do this.

**Third,** Propositions 5.2 and 5.3 assume the following: for a given point $j$, its $k$ gradient estimates are iid and sub-Gaussian about a fixed mean. I'm confused about the assumption on a technical level (the distribution is isotropic, so isn't $\Sigma$ the identity?), but more importantly I don't understand how we could expect something like this to hold, even approximately. The assumption of independence between gradient estimates seems particularly strong, as these gradients are computed from the same model parameters and likely share dependencies through the loss function and data. Furthermore, the assumption of a fixed mean for the gradients is questionable, as the model parameters are updated during the stochastic gradient descent process, which would cause the gradients to vary over time. Even if the gradients were sub-Gaussian, the assumption of an isotropic distribution, implying equal variance in all directions, is unlikely to hold in practice, as different parameters may have different sensitivities to the input data.

I look forward to discussing this assumption with the authors and other reviewers, but even if it is reasonable I disagree with the informal discussion around it. For example, the abstract says you "provably remove the linear scaling of estimation uncertainty," but what is actually proven seems much weaker.

### Questions
Are there any settings where the iid sub-Gaussian gradient assumption is satisfied?

### Soundness
2

### Presentation
2

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
This paper addresses the differential privacy (DP) data valuation problem with perturbed gradients. The authors demonstrate that when i.i.d. noise is added to gradients, the estimation uncertainty does not decrease as the number of draws $k$ increases, because the variance of both the information and noise parts grows linearly with $k$. Assuming the data distribution is i.i.d., they propose an adaptive noise-adding mechanism with $O(\log k)$ variance, which bypasses the linear scaling of variance due to the added DP noise.

### Strengths
1. Both the motivation and problem setting are stated clearly, and the proposed adaptive mechanism provably beats the i.i.d. mechanism

2. comprehensive experiments are conducted to illstruate the proposed theory.

### Weaknesses
1. The statement of assumptions is unclear. In Proposition 5.2, the authors state that the isotropic sub-gaussian assumption is made for the distribution but then introduce the covariance matrix $\Sigma$. Does isotropic mean that the covariance is the identity matrix?(e.g. Definition 3.2.1 in https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.pdf )

2. While I don't think the isotropic assumption is restrictive, I wonder whether the previously proposed binary counting mechanism( https://dl.acm.org/doi/10.1145/2043621.2043626 ) can also achieve the same performance bound as the proposed adaptive mechanism under this assumption, since it seems that the main task in this setting is to continually release a sequence of averaged gradient to reduce the variance.

### Questions
My main concern is whether the previously proposed method can achieve similar performance to those proposed in this paper, as mentioned in point 2 of the weaknesses. I am willing to raise my score if the authors can provide more explanation on this point.

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
4

### Summary
This paper addresses the data value estimation problem using privately released gradients. To
compare the performance of various data value estimators, the authors introduce the concept of
estimation uncertainty and demonstrate that it grows linearly with the number of evaluations in
the naive method that injects independent Gaussian noise. To reduce the uncertainty, the authors
devise an algorithm that injects correlated noise into the gradients and demonstrates that it eliminates
the estimation uncertainty’s linear dependence on the number of evaluations.

### Strengths
- It considers an interesting problem of data value attribution that has wide-ranging applications
in many real-world scenarios.
- The authors introduce the concept of estimation uncertainty and, using this metric, devise two
algorithms for data value estimation.
- The theoretical analysis of the estimation uncertainty of proposed algorithms shows that their
method provably reduces the dependence on the number of evaluations from linear to log-squared
k, where k is the number of evaluations.
- The authors further reduce the dependence of the algorithm’s estimation uncertainty on the number of evaluations to a constant.

### Weaknesses
 - The proposed method is somewhat simple, as it essentially computes a simple weighted average
of previously released private gradients. While the simplicity of the proposed method does not
imply a lack of novelty, the existence of prior work that also carefully generates the correlated
noise to reduce the variance of released statistics suggests that there might be room for further
improvement in the proposed approach.
- In essence, the introduced estimation uncertainty is the variance of released gradients. The
variance of released statistics has long been used as a utility metric in differential privacy
literature. However, an important distinction is that most works employing the variance as
a utility metric consider unbiased statistics. In the paper, the private gradients are biased, and
I am curious to know how the proposed approach affects the bias of these gradients. Especially,
as the proposed algorithm takes the average of gradients evaluated in the preceding locations
in the optimization trajectory, the proposed approach may increase the bias. It
will be interesting if the authors can show that this is not the case.
- The graphs presented in the paper are not properly labeled. While the captions provide some
explanation, it’s still not easy to read and interpret the graphs. The figures should be self-contained and interpretable on its own.

### Questions
- How is the proposed solution $X^∗$ derived? Is it a solution (or an approximation solution) of
constrained optimization problem that minimizes the estimation uncertainty?
- In Figure 3, the performance of proposed method with burn-in seems to drastically decrease
when q is set too high. Is there a rule of thumb for setting this hyperparameter?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a novel method for estimation of data value under differentially private training based on the notion of estimation uncertainty which is introduced by the addition of DP noise and propose a new way to mitigate this by injecting correlated noise instead.

### Strengths
The work is well-motivated and addresses an important problem (the privacy-utility trade-off, where utility is a value function over the dataset the model could have access to). The structure is clear, the statements are supported by both the empirical and the theoretical results. I also appreciate the openness about some of the limitations i.e. that the fundamental scientific problem of privacy-utility with respect to the theoretical information loss is still unsolved, but this work proposes a method which can alleviate it to some extent by maintaining the ranking of the values.

While a lot of what is discussed in this paper is well-known, this is a very nice attempt to formalise these notions through uncertainty.

### Weaknesses
While the results are certainly interesting, they seem to rely on a number of assumptions and limitations. The empirical results only feature a handful of datapoints on 2 relatively simple benchmark datasets (ML evaluation), V being deterministic and model parameters fixed etc. I would like to see more a) utility functions covered, b) larger dataset sizes and c) range of epsilon values. The last one being particularly important because (as discussed in the works linked below), DP diminishes value not just because of noise, but clipping. And it is important to consider the trade-off between noise and clipping (and not just correlated vs independent noise) in more detail when it comes to methods for valuation. Some of the models used in evaluation (the resnet family) is additionally well-protected against the effects of gradient clipping, meaning that this effect is not observed in full detail in the evaluations. You may consider adding another baseline model to discuss the comparative utility loss of clipping vs noise.

The presentation of the figures and algorithms is rather confusing. I found most of the figures (e.g. 1 and 2) to be unreadable even on larger screens and algorithm 1 is difficult for me to digest: are all 3 colors integrated into it already or are they mutually exclusive drop-ins which we need to evaluate separately? Figure 2 in particular needs a rework, there is too much happening at the same time with too little explanation.

I personally think its a bit of an odd choice to move some of the most important results (i.e. how the method 'actually' protects privacy under MIAs) to the appendix. Moreover, there seems to be no comparison to traditional DP and the only one you are comparing against is the uncalibrated non-private method which already has pretty poor performance to begin with. I am not convinced how 'private' this really is given that your budget is 1.0 and with a budget of infinity the attack is better by 5% on average and 10% at most (which could have been a convincing results, but I am yet to see how different budgets or a standard DP mechanism e.g. DP-SGD would perform in comparison).

There are some recent works which show that there are valuation methods which are usable even under DP (and in particular for FL use cases), which are not mentioned in this work [1,2]. Additionally there are also works which discuss the use of privatised statistics under DP training in order to obtain better privacy-utility trade-offs [3,4]. While these rely on different values (and different issues of DP when it comes to utility loss), these should also be part of the prior works (and ideally a set of baselines). [4] actually does something really similar to this work, but under DP-FTRL rather than DP-SGD.

### Questions
Minor:

Which neighbouring definition is used for DP here? Add/remove or replace one?

Please elaborate on algorithm 1, it is not clear how to interpret the different options.

### Soundness
3

### Presentation
3

### Contribution
3
