# Optimality of Matrix Mechanism on $\ell_p^p$-metric

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
In this paper, we introduce the $\ell_p^p$-error metric (for $p \geq 2$) when answering linear queries under the constraint of differential privacy. We characterize such an error under $(\epsilon,\delta)$-differential privacy in the natural add/remove model. Before this paper, tight characterization in the hardness of privately answering linear queries was known under $\ell_2^2$-error metric (Edmonds et al. 2020) and $\ell_p^2$-error metric for unbiased mechanisms in the substitution model (Nikolov et al. 2024). As a direct consequence of our results, we give tight bounds on answering prefix sum and parity queries under differential privacy for all constant $p$ in terms of the $\ell_p^p$ error, generalizing the bounds in Hhenzinger et al. for $p=2$.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the so-called "factorization mechanism" for answering linear queries privately. To recap, a workload of $n$ linear queries over a domain of size $m$ can be described by a matrix $A: [\pm 1]^{n\times m}$. The private query releasing algorithm asks to estimate $Ax$ while preventing the privacy of $x$ w.r.t. any adjacent $x'$ s.t. $\|x-x'\|_1 <= 1$.

The standard approach is to publish $Ax + N(0, sigma^2)$ where the Gaussian noise is calibrated to the sensitivity of $A$. The factorization mechanism tries to improve over this by writing $A = L R$ and publish $L ( Rx + N(0, (\sigma')^2))$ where $\sigma'$ is calibrated to the sensitivity of $R$ only.

There is a lot of work studying the power and limitations of the factorization mechanism, trying to argue it is the "optimal" mechanism for this task. Generally, the theme along this line of research is to fix an arbitrary algorithm $\mathcal{A}$ (not necessarily following the paradigm above), and let $\mathcal{B}$ be the optimal factorization mechanism (following the approach above with an optimal $L,R$). Then, argue that for some error metric $err$, one has $err(\mathcal{A}) \preceq err(\mathcal{B}))$ up to insignificant factors. The optimality of the factorization mechanism has been established for $\ell_2^2$-error metric, the $\ell^2_p$ metric (be a recent work [Nikolov-Tang'24]. 

The current paper is a close follow-up of [Nikolov-Tang'24]. It proved that the factorization mechanism is optimal under the $\ell^p_p$ metric, defined as
$$
err = \mathbb{E}[ \| \mathcal{A}(x) - Ax \|_p^p ]
$$
Namely, this is the $p$-th moment of the ``error vector''. Some motivations are provided, for one, as $p$ increases from $2$ to $\infty$, this error smoothly interpolates between the mean-squared error and the worst-case. Second, this paper argues that the error metric is more natural than $\ell_p^2$ norm considered in prior work. 

The lower bound on error, implied by the proof, depends on a mysterious factorization norm and is hard to interpret. This paper gives some applications of their general lower bound to specific query families of interest. These include prefix-sum queries and sparse parity queries (or some might prefer to call it $k$-way marginals)

### Strengths
* I like the motivation of interpolating between $\ell_2$ and $\ell_\infty$ error via $\ell_p^p$.
* The introduction of the paper is largely clear and easy to follow (perhaps with some background knowledge).

### Weaknesses
 * Although the gentle introduction is clear, once it goes into a more technical part, it becomes significantly harder for me to appreciate the discussion. I take Lines 254-255 "The main technical obstacle of Theorem 2.1 lies in ..." as the punchline of this paper. However, I have little idea what this means in terms of technical novelty. Given my limited time reading, I hope the authors can clarify some of my questions below.

* Some discussions in the introduction may be improved (see some of my questions below).

* Line 111: you argued that $\ell_p^p$ is more natural. I somewhat agree with this point from a notational aesthetic point. However, can you comment on why the Nikolov-Tang paper was working with an "unnatural" measure of $\ell_p^2$? This might make your claim more convincing.

* Pargraphy beginning on Line 508: I struggled to understand why this paragraph means the Nikolov-Tang result is "instance optimal". Then I looked into their paper and found that their definition of instance optimality was somewhat nuanced, and your description was indeed accurate (but not super informative, IMO). I acknowledge it might be hard to convey the result of Nikolov-Tang concisely. But it might be worth rephrasing your conclusion a little bit.

* Technical question: I think the current Section 2 is quite dense, and you seem to be citing Nikolov-Tang heavily. Could you maybe try to distill some of your technical punchlines and pin down the exact manipulation where you differ from prior works? I would be ok if you defer a "complete proof sketch" to appendix or so.

### Questions
* Line 111: you argued that $\ell_p^p$ is more natural. I somewhat agree with this point from a notational aesthetic point. However, can you comment on why the Nikolov-Tang paper was working with an "unnatural" measure of $\ell_p^2$? This might make your claim more convincing.

* Pargraphy beginning on Line 508: I struggled to understand why this paragraph means the Nikolov-Tang result is "instance optimal". Then I looked into their paper and found that their definition of instance optimality was somewhat nuanced, and your description was indeed accurate (but not super informative, IMO). I acknowledge it might be hard to convey the result of Nikolov-Tang concisely. But it might be worth rephrasing your conclusion a little bit.

* Technical question: I think the current Section 2 is quite dense, and you seem to be citing Nikolov-Tang heavily. Could you maybe try to distill some of your technical punchlines and pin down the exact manipulation where you differ from prior works? I would be ok if you defer a "complete proof sketch" to appendix or so.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper investigates the asymptotic lower bounds of the expected $\ell_p$ errors of differentially private algorithms for answering linear queries. Specifically, given a collection of linear queries represented by a query matrix $A$, it presents an asymptotic error lower bound that any differentially private algorithm will incur, expressed in terms of the matrix $A$ and privacy parameters. 

After establishing this lower bound, the paper demonstrates that the matrix mechanism can achieve it, up to logarithmic factors. Additionally, it explores two specific linear queries: the prefix sum and the parity queries, deriving their error lower bounds as special cases of the general lower bound obtained. It also presents specific matrix mechanisms that achieve asymptotic tight upper bounds (again, up to logarithmic factors).

### Strengths
1. The problem addressed is of fundamental importance.
2. The paper successfully derives asymptotic lower bounds for matrix mechanisms under $\ell_p$ error.
3. It demonstrates sophisticated applications of existing techniques.

### Weaknesses
1. The paper demonstrates that the matrix mechanism is asymptotically optimal, rather than instance optimal, for the error metric considered. This means that while the mechanism achieves the best possible error rate in the limit, it may not be optimal for any specific instance of the problem, which limits its practical applicability. It would be more impactful if the paper could show instance optimality, or at least discuss the practical implications of this asymptotic result.
2. The writing is generally good, but there are parts that lack consistency. For example, the presentation of Theorem 1.3 in the introduction feels disconnected from the surrounding discussion. The motivation for including this theorem, and its connection to the main results, is not clearly explained. Additionally, the use of notation and terminology could be more consistent throughout the paper. For instance, the definition of err() is not always clear, and its relationship to the $\ell_p$ error is not always explicitly stated.
3. In line 113, the use of $v_1^p + \ldots + v_m^p$ is not correct; it should be $|v_1|^p + \ldots + |v_m|^p$. This is a critical error, as it affects the correctness of the subsequent analysis. Furthermore, the explanation of why the approach of Nikolov & Tang doesn't explain the additive noise mechanism is not entirely clear. It seems to suggest that the additive noise mechanism might not be unbiased, but this point needs further elaboration. The connection between unbiasedness and the applicability of their approach is not clearly established.
4. The term “symmetry” in line 128 is vague and requires further clarification. It's not immediately clear what kind of symmetry is being referred to, and how it relates to the mathematical analysis. Similarly, the phrase “the mathematical object the sequence captures…” in line 130 is also unclear. It's not obvious what sequence is being referred to, and what mathematical object it represents. This lack of clarity makes it difficult to understand the significance of this point. Finally, in line 286, the phrase “the measure of the new distribution” should be changed to “the new distribution.”

### Questions
1. In Theorem 1.2, the distribution of $z$ does not incorporate the privacy parameter $\epsilon$. It seems that something is missing here.
2. In the next paragraph, change “also obtain a characterization of err() that is tight up to log factors” to “also obtain an err() that is tight up to log factors.”
3. Why is Theorem 1.3 included in the introduction? It appears disconnected from the surrounding discussion. For instance, do you use Theorem 1.3 to prove the lower bound of the prefix sum later in the paper?
4. Line 113: Change $v_1^p + \ldots + v_m^p$ to $|v_1|^p + \ldots + |v_m|^p$.
5. In line 113, why doesn’t the approach of Nikolov & Tang explain the additive noise mechanism? Is it because the additive noise mechanism might not be unbiased?
6. Is it common to encounter biased additive noise mechanisms? Would it be challenging to derive a lower bound for the biased case by reducing it to the unbiased one, using techniques similar to those presented in Lemma 2.3?
7. Could you elaborate a bit more on the term “symmetry” in line 128? What does it signify in this context? Also, in line 130, clarify “the mathematical object the sequence captures…”
8. Line 286: Change “the measure of the new distribution” to “the new distribution.”

### Soundness
4

### Presentation
2

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
This paper studies the $\ell_p^p$-error of privately answering linear queries. The authors show a lower bound on the error in terms of a certain factorization norm ($\gamma_{(p)}(A)$), suggesting that the classical matrix factorization mechanism is optimal up to logarithmic factors. Based on this main result, they also provide an easy-to-use lower bound that depends on the Schatten-1 norm of the workload matrix. They then apply their results to two kinds of queries: prefix-sum and parity, and obtain nearly tight bounds for both tasks.

### Strengths
1. Linear query release is a fundamental problem in private data analysis. This article characterizes the error of this task with respect to $\ell_p^p$-metric, contributing to a deeper understanding of the role of differential privacy.
2. The writing is clear. Also, the technical details are well-organized and easy to follow.

### Weaknesses
1. It appears that the upper bound and lower bound only match in the high privacy regime. In the low privacy regime, where $\varepsilon = \Omega(1)$, the presented upper bound cannot match the lower bound.
2. When $p$ is not a constant, the proposed bounds may not be tight for certain regimes of the parameters. For example, when $n = p$, the upper bound in Theorem 1.5 is $O(\log^{1.5} (p))$ while the lower bound is $\Omega(\log (p))$.

However, I think both of the above are not serious issues.

### Questions
I do not understand what the workload matrix for parity queries is like. Can you provide a small example?

### Soundness
4

### Presentation
3

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
The paper studies worst-case lower bounds for answering linear queries under add-remove approximate differential privacy for an $\ell_p^p$ error metric. In contrast, past work derived instance-specific lower bounds for unbiased mechanisms under substitution approximation differential privacy in terms of $\ell_p^2$ metrics. Its main result is a lower bound  that is characterized by the factorization norm of the query matrix (Theorem 1.4). This lower bound is almost tight with an upper bound that is also provided using, as a long line of recent work has done, the matrix mechanism (Theorem D.1). The paper also specializes this result to the specific problems of prefix sum and parity by explicitly analyzing the problems' factorization norms (Theorem 1.5 and 1.6).

### Strengths
To the best of my knowledge, the claimed novelty in the paper is accurate, and it is nice to have a more complete lower bound picture for linear queries. The paper does a reasonable job of providing high-level explanations for some of its technical challenges and solutions. It is mostly easy to read with careful explanations.

### Weaknesses
To me, the paper's primary weakness is significance. While the paper explores add/remove vs substitute, $\ell_p^p$ vs $\ell_p^2$, and potentially biased vs unbiased mechanisms, each of these directions feels niche, particularly since the focus is on lower bounds. The matrix mechanism upper bound, as I think the authors would agree, is not a significant contribution here. The paper does not convincingly argue why expanding known results in these directions is worthwhile, beyond it being technically possible. For lower bounds, a stronger argument is needed to show how these results add "morally" to our understanding of private mechanisms. 

Specifically, the distinction between add-remove and substitution is presented in a confusing way. The database is presented as a vector in $\mathbb{R}^n$, where $n$ is unclear. If $n$ is the size of the data universe and $x$ is a histogram, as suggested by Appendix B.3 and the study of add-remove privacy, then neighboring databases should have a number of data points that literally differ by 1. However, the paper uses the condition $\|\|x-x'\|\|_1 \leq 1$, which seems more like a "fractional" contribution model. This is further confused by the claim that Edmonds-Nikolov-Ullman [1] uses the same neighboring notion as this paper, while Nikolov-Tang [2] uses a different one. In fact, Edmonds-Nikolov-Ullman [1] appears to use the same notion as Nikolov-Tang [2].

Furthermore, considering general $\ell_p$ norms feels like generalization for its own sake. While the paper argues that $p \neq 2$ is more "natural", these arguments are vague. What do these different error metrics meaningfully add to our understanding beyond what is already known for $p=2$? The authors should make a more cogent case that generalizing $p$ actually tells us something useful.

Similarly, the inclusion of biased mechanisms does not seem to significantly add to our understanding of privacy in the context of lower bounds. While biased mechanisms might be useful in other contexts, it is not clear that they are the key to better worst-case error guarantees here. Their inclusion feels more like a technical wrinkle that necessitates different arguments rather than a substantial contribution to the field.

### Questions
Overall, I think expending more effort trying to explain why the directions of novelty add up to an "interesting" result could go a long way for this paper, but as is the qualitative improvement over known results feels weak. Some specifics:

1) The paper repeatedly emphasizes the distinction between add-remove and substitution, but this is described in a confusing way. Throughout, the database is presented as a vector in $\mathbb{R}^n$ -- what is $n$ here? Is it the size of the data universe, or the number of data points? Since neighboring databases both lie in $\mathbb{R}^n$ and the paper claims to study add-remove privacy -- where I'd expect neighboring databases to literally have # data points that differ by 1 -- I expect that $n$ is the size of the data universe and $x$ is a histogram, and Appendix B.3 seems to agree. But then, I don't know why it's more natural to allow neighboring databases to have $\|\|x-x'\|\|_1 \leq 1$, which is more like a strange "fractional" contribution model where a user can technically contribute $<1$ to many items. Edmonds-Nikolov-Ullman also appears to use the same neighboring notion as Nikolov-Tang, despite this paper's claim that it uses the same notion as this paper. Overall: I am confused by this bit.

2) Considering general $\ell_p$ norms typically feels to me like generalization for its own sake. The paper makes a few attempts to argue that $p \neq 2$ is more "natural", but the arguments are vague. The error metrics are clearly different, but what do they meaningfully add to our understanding? I think this paper would be stronger if the authors would try to make as cogent as possible a case that generalizing $p$ actually tells us something useful.

3) I have pretty much the same reaction to biased vs unbiased as I do to $p$ vs 2. I don't think anybody expected that biased mechanisms were the key to better worst-case error guarantees, so their inclusion again feels more like a technical wrinkle that necessitates different arguments than something that significantly adds to our understanding of privacy (and since it's lower bounds, I think adding to understanding matters more -- if there were new upper bounds, there would be a much simpler case that it's just a new useful thing).

### Soundness
4

### Presentation
3

### Contribution
2
