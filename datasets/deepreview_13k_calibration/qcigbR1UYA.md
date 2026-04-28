# Performance Bounds for Active Binary Testing with Information Maximization

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
In many applications like experimental design, group testing, medical diagnosis, and active testing, the state of a random variable $Y$ is revealed by successively observing the outcomes of binary tests about $Y$, where new tests are selected adaptively based on the history of outcomes observed so far. If the number of states of $Y$ is finite, the process ends when $Y$ can be predicted with a desired level of confidence or all available tests have been used. Finding the strategy that minimizes the expected number of tests needed to predict $Y$ is virtually impossible in most real applications due to high dimensions. Therefore, the commonly used strategy is the greedy heuristic of information maximization that selects tests sequentially in order of information gain. However, this can be far from optimal for certain families of tests. In this paper, we argue that in most practical settings, for a given set of tests, there exists a $0 \ll \delta \ll \frac{1}{2}$, such that in every iteration of the greedy strategy, the selected binary test will have conditional probability of being `true', given the history, within $\delta$ units of one-half. Under this assumption, we first study the performance of the greedy strategy for the simpler case of oracle tests, that is, when all tests are functions of $Y$, and obtain tighter bounds than previously reported in literature. Subsequently, under the same assumption, we extend our analysis to incorporate noise in the test outcomes. In particular, we assume the outcomes are corrupted through a binary symmetric channel and obtain bounds on the expected number of tests needed to make accurate predictions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper deals with the problem of determining the value of a random variable Y, by adaptively performing a series of tests with binary output. The goal is to minimize the expected number of tests needed to determine the value of Y with the desired confidence. In the case where any possible binary test on the values of $Y$ is available, this problem has been shown to be almost optimally solvable with at most $H(Y)+1$ tests, where $H(Y)$ denoted the entropy, via the information maximization strategy (i.e each time selecting the test with probability closest to $1/2$). However, the authors consider the more practical setting where a specific set $\mathcal{T}$ of tests is available. The results of the paper identify sufficient conditions that this family of tests has to satisfy in combination with the expected number of tests needed. In particular, the notion of $\delta$-unpredictability is considered for the test families, where $\delta$ is a measure of uncertainty for the test outcomes. The main result is that one can identify the value of Y using in expectation $\frac{H(Y)}{\log (½+\delta)^{-1}}$ test from a $\delta$-unpredictable family using the greedy information maximization strategy. This setting is also extended to the case where the test outcomes are noisy as a result of independently passing through a binary symmetric channel and a similar result is shown involving an additional parameter $\gamma$ representing the target confidence for the value of $Y$.

### Strengths
The paper deals with a fundamental problem from the perspective of more realistic and practical settings than the ones previously considered including a noise model.

### Weaknesses
There is no discussion about lower bounds on the number of tests needed for either the noisy or the oracle (noiseless) case. I believe one should be able to derive something using information theory, but it's not clear to me if those bounds would match the upper bounds in the paper.  
The presentation could be improved since the results and contributions are not entirely clear form the introduction. 


Minor cpmments
-In Theorem 1 (and similarly for Theorem 4): The use of absolute value in the denominator is confusing since the expressing inside is always negative.    I suggest using $\log (½+\delta)^{-1}$ instead. 
-Page 3, "noisy tests" paragraph, line 7: By "pre-noise" did you want to say "de-noise"? 
-Page 4, line 17: the word "after" is probably missing after the word "or"

### Questions
1. Are there any results for the case where all tests are chosen (non adaptively) in the beginning?
2. Can the expression in Theorem 1 (and similarly Theorem 4) be written with respect to the entropy $H(½+\delta)$ of a Bernoulli distribution? One would expect this because this seems to be the amount of information revealed with each test.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the problem of identifying the value of a random variable $Y$ through a sequence of binary tests. The paper focuses on studying the Information Maximization procedure where at each step we greedily choose the test that maximizes the conditional mutual information.

The paper first considers the case where the sets of allowed tests are deterministic functions (called oracle tests), and then studies the case where the output of the oracles are corrupted by noise. In both cases, the paper assumes that the set of tests satisfies a "$\delta$-unpredictability property" where at each $k$-th stage of the InfoMax procedure, it is always possible to find a test $T_k$ such that $Pr[T_k=1|T_1,\ldots,T_{k-1}]$ is at most $\delta$ away from 1/2 (unless of course we already identified $Y$ at the desired accuracy). In other words, we can always find a test that approximately bisects the set of possible values of $Y$.

Assuming that the set of tests satisfies the $\delta$-unpredictability property, the paper proves an upper bound on the expected number of tests needed to identify $Y$. The bound depends on $\delta$ and is proportional to the entropy $H(Y)$. In the noisy case, the bound also depends on the noise-level $\alpha$.

### Strengths
The problem considered in the paper is interesting, and the bound that is given is optimal up to constant factors since it is proportional to the entropy H(Y).

### Weaknesses
I have to admit that I am not very familiar with the literature of this topic in particular, but from an information-theoretic perspective, the novelty/contribution is a bit limited: The techniques used in the paper are very simple and the results are not too surprising. Specifically, the core of the analysis relies on a rather straightforward application of the chain rule for mutual information and a relatively simple bounding argument based on the unpredictability assumption. While the final bound is indeed proportional to the entropy, the path to get there does not involve any sophisticated information-theoretic tools or insights. The analysis of the noisy case also follows a similar pattern, with the added complexity of dealing with the noise parameter, but the underlying techniques remain quite basic. The paper essentially shows that a greedy approach with a specific unpredictability condition leads to a bound proportional to the entropy, which is not surprising given the nature of the greedy approach and the unpredictability assumption.

### Questions
Did the authors consider extending the work to more general tests where a test consists of passing $Y$ through a noisy channel of input alphabet $\mathcal{Y}$ (the set of possible value of $Y$) and of output alphabet $\{0,1\}$?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of predicting a random variable using tests. Specifically, the authors analyse the commonly used greedy heuristic of information maximization under the assumption that the set of tests are $\delta$-unpredictable. The main contribution of the paper is new upper bounds on the number of tests needed for information maximazation under both the oracle tests and the noisy tests. The obtained bound for oracle tests is tighter in certain regime of parameters than previous bounds, while the bound for noisy tests is the first such results.

### Strengths
1. The paper is very well-written. I really appreciate the authors for including proof sketch and discussion of high-level ideas, which makes the paper easy-to-follow even for readers that are not familiar of the problem of active testing.
2. I think understanding the performance of greedy heuristic that has practical application is an important question. The obtained bound for oracle tests gives tighter guarantee than previous results in certain regimes of parameters and the paper presents detailed comparison with previous bounds. This paper is also the first to obtain bound for information maximization for noisy tests.

### Weaknesses
1. As the authors comment the limitation section, the assumption that the tests are $\delta$-unpredictable is not very useful in practice since it is not know how to compute the corresponding $\delta$. Furthermore, the assumption itself, that there exists a $\delta$ such that the probability of any test outcome is bounded away from 0 and 1 by $\delta$, is quite strong and may not hold in many real-world scenarios. For instance, if a test is highly specific to a rare condition, its probability of being true could be extremely low, violating the $\delta$-unpredictability assumption. This limits the applicability of the theoretical results.
2. The assumption of i.i.d. noise for noisy tests also limits the practical application of the results since the noise is often dependent on the value of $Y$ and the tests outcomes are not independent. Specifically, the noise model does not account for the possibility of systematic errors in the tests, where the noise is correlated with the underlying variable $Y$ or with the outcomes of other tests. For example, if a certain test is prone to false positives when $Y$ is high, this dependence is not captured by the i.i.d. noise assumption, which can lead to inaccurate predictions in practice.

### Questions
Does the authors have any insights in resolving weaknesses mentioned above?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to provide a tighter bound for the well-known active binary testing with information maximization (Informax). The approach is similar to Garey and Graham (1974) or Loveland (1985) which uses a key assumption that the sequence of tests are $(\gamma,\delta)$-unpredictable to derive the minimum expected number of binary tests to predict a target variable $Y$.

### Strengths
+ For oracle binary tests, the proposed bound can improve the existing bounds for the same setting such as Garey and Graham (1974) or Loveland (1985). The most interesting contribution is to reduce $\log_2(|\mathcal{Y}|)$ to $H(Y)$ (cf. Theorem 1). 
+ Experiments on datasets CUB-2011 (20Q with birds) and AwA2 (20Q with animals) are provided, which demonstrate that the proposed bounds (for oracle tests) can be better than Garey and Graham (1974) or Loveland (1985)'s counterparts. 
+ The authors give a new bound for the noisy binary tests (cf. Theorem 4), and there haven't any existed bounds for this model.

### Weaknesses
 + It is hard to think of how to design a binary test sequence which is $(\gamma,\delta)$-unpredictable although this is the key assumption to achieve results in this paper. Hence, the proposed bounds (for both oracle and noisy tests) do not guide us how to design an active binary test sequence based on Informax principle to achieve them.  
+ The tightness of the given bound also depends on $\delta$. However, in general, it looks hard to find the optimal value of $\delta$ for an existing sequence of binary tests. 
+  In the two provided experiments, the authors assume that $Y$ is uniformly distributed on some finite set $\mathcal{Y}$, so $H(Y)=\log_2(|\mathcal{Y}|)$. Therefore, the improvements of the authors' bound in Theorem 1 over Loveland's bound (cf. 6), which are shown in Fig. 2 (or Table 1  in Appendix), is mainly originated from a better control of constant factor (depending on $\delta$). The main interesting contribution that reduces $\log_2(|\mathcal{Y}|)$ to $H(Y)$ is not shown in these experiments.  
+ In Section 5, the authors mention some obtained bounds for noisy tests (via BSC), which are achieved based on the decomposition $T(Y)=D_T(Y)\oplus N_T$. The design of binary tests to achieve these bounds is based on having knowledge of $D_T(Y)$ (Lemma 2) or $I(T;Y|\mathcal{A}_{1:t})$ (cf. (1)), which looks very hard to obtain in practice. In addition, the tightness of these bounds is not verified in the paper.

### Questions
I don't have any question. Please see the weaknesses above and let me know if I misunderstand anything. 

Some typos and improvements:

+  Repetition in (27) and (28). Please remove the redundancy. 
+  You should mention that $T(Y) \in \{0,1\}$ for any test $T$ in Section 3. This means that your results are limited to the binary test (yes/no questions).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
