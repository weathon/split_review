# Beyond Laplace and Gaussian: Exploring the Generalized Gaussian Mechanism for Private Machine Learning

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 8, 3, 1

## Abstract
Differential privacy (DP) is obtained by randomizing a data analysis algorithm, which necessarily introduces a tradeoff between its utility and privacy. Many DP mechanisms are built upon one of two underlying tools: Laplace and Gaussian additive noise mechanisms. We expand the search space of algorithms by investigating the Generalized Gaussian (GG) mechanism, which samples the additive noise term $x$ with probability proportional to $e^{-\frac{| x |}{\sigma}^{\beta} }$ for some $\beta \geq 1$. The Laplace and Gaussian mechanisms are special cases of GG for $\beta=1$ and $\beta=2$ respectively. 

In this work, we prove that all members of the GG family satisfy differential privacy, and provide an extension to an existing numerical accountant (the PRV accountant) to do privacy accounting. We apply the GG mechanism to two canonical tools for private machine learning, PATE and DP-SGD; we show that $\beta$ has a weak relationship with test-accuracy, and that $\beta=2$ (Gaussian) is often a near-optimal value of $\beta$ for the privacy-accuracy tradeoff of both algorithms. This provides justification for the widespread adoption of the Gaussian mechanism in DP learning. That said, we do observe a minor improvement in the utility of both algorithms for $\beta\neq 2$, suggesting that further exploration of general families of noise distributions may be a worthy pursuit to improve performance in DP mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In differential privacy literature, most papers focus on either Laplace or Gaussian Mechanism due to the simplicity of analysis and proven effectiveness in practice. This paper studies the Generalized Gaussian Mechanism instead. It shows that the mechanism is differentially private and through experiments on common benchmarks, it also shows the effectiveness of the mechanism on deep learning tasks.

### Strengths
- The paper provides some empirical evidence on why Gaussian Mechanism is popular. In their experiments, the model usually achieves the best accuracy when the noise added is roughly Gaussian.

- The Generalized Gaussian Mechanism can be useful for tasks that require very high accuracy. By tuning the $\beta$ carefully, it's possible that the model can achieve better results (as shown by some improvements on cifar10 tasks).

- The paper is well-written overall.

### Weaknesses
 - The experiments are conducted on fairly small datasets and deep learning architectures so it's hard to get a grasp of how well the generalized gaussian mechanism works. Specifically, the datasets used, such as CIFAR-10, are relatively low-dimensional and do not fully represent the challenges of applying differential privacy to more complex, high-dimensional data. The deep learning architectures explored are also shallow, which may not reflect the behavior of the mechanism in modern deep learning scenarios with much larger models. This makes it difficult to extrapolate the findings to more practical settings.

- While the study is fairly interesting, I'm not sure if the technical contribution is enough. The main takeaway is Gaussian and Laplace are pretty much the best choices as expected. Generalized Gaussian Mechanism is fairly hard to analyze since it doesn't have a closed-form relationship between $\beta$ and $\epsilon, \delta$. The experiment also requires the tuning of $\beta$ which in the end ends up being Gaussian and Laplace mechanism anyway. The lack of a clear theoretical understanding of how the parameter $\beta$ interacts with privacy parameters $\epsilon$ and $\delta$ makes it difficult to use the generalized Gaussian mechanism in practice. The need to tune $\beta$ experimentally, without a principled way to determine its optimal value, further limits the practical applicability of the proposed mechanism. The fact that the optimal values of $\beta$ often converge to the Gaussian or Laplace mechanisms suggests that the added complexity of the generalized Gaussian mechanism may not be justified.

### Questions
- In page 18, I think the RHS should be $(\frac{\alpha-1}{\alpha})^{1/\beta}$?

- Also as $x<0$, shouldn't $\frac{|x|}{|x-\mu|}$ be $\frac{-x}{\mu-x}$ instead? Fortunately, I don't think it affects the argument.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper takes a deeper look at the generalized Gaussian mechanism.
The first contribution is to extend the privacy proof of the GGM to work with the PRV accountant to allow tighter analysis than previous bounds. 
They then plug the mechanism into various ML applications and observe the effect of varying beta on accuracy.
In general, they find support for using the Gaussian mechanism, but also that more fine-tuned versions of beta (fractional values) can lead to slight improvements in accuracy.

### Strengths
- Even though the results didn't yield significant changes while varying beta, I see great value in a study that supports the approximate optimality of the Gaussian mechanism. In general, there are so many hyperparameters to tune, so giving practitioners support in using the Gaussian mechanism as a default is useful.
- Very well-written paper with clear descriptions.

### Weaknesses
 - Claiming STOA with three runs: The results on machine learning had quite a high variance due to limited runs. I think claiming STOA when the accuracy is better by such a small amount is not significant. Perhaps more runs and a hypothesis test/confidence interval would give more definitive results (although STOA is not the primary goal of the work).

- One more hyperparameter: the very small gains in accuracy would surely be outweighed by the cost of tuning beta in practice. I see the main contribution of this work is showing that the beta doesn't have too much effect rather than improving the accuracy of current mechanisms. 

- End of Section 3.2, last paragraph "change subsequently change".
- A.1 Proof of theorem 4 has a missing ref.

### Questions
- What would be the solution to fix the artifacts in Figure 3? Perhaps more values in the grid?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the generalized Gaussian mechanism for private machine learning, especially DP-SGD and PATE. The generalized Gaussian mechanism is a mechanism utilizing the generalized Gaussian noise that encompasses Laplace, Gaussian, and arbitrary noise distribution associated with the density function proportional to $e^{-\frac{|x-\mu|^\beta}{\sigma}}$. The paper investigates the optimal $\beta$ in the generalized Gaussian in terms of utility-privacy trade-off in DP-SGD and PATE. To this end, the authors proposed $\beta$-DP-SGD and GGNMax algorithms which are variants of DP-SGD and LNMax by replacing the noise distribution with the generalized Gaussian. The authors show empirically that choosing $\beta=2$ is near-optimal in test accuracy.

### Strengths
This paper is well-written and well-organized. I found that investigating the optimal parameter $\beta$ of the generalized Gaussian mechanism for private ML is interesting and important in ML society. I found that $\beta=2$ is near-optimal is very interesting, and I think it opens other research directions.

### Weaknesses
Generally, I do not see much contribution in this paper. Several things I am concerned about are listed:
- The proposed mechanisms ($\beta$-DP-SGD and GGNMax) are a straightforward generalization of the existing mechanisms by replacing noise distribution. 
- The analysis using the PRV accountant is not novel.
- I felt that there are not many analytical results in the generalized Gaussian mechanisms. Most of the results are empirical findings, and I doubt that the experiments are sufficient to claim the findings.



### Questions
Main questions:
1) Is Theorem 1 saying there exists $\epsilon$ and $\delta$ for $(\epsilon,\delta)$-DP? Isn't it obvious that every mechanism has $\epsilon=1$ and $\delta=1$ if I am not mistaken?
2) For "However, unlike the results ... larger than $\beta>3$" on page 8, is there any reason why this happens?
3) If I am not mistaken, the comparisons regarding $\beta$ are done after hyper-parameter optimization. If they are, I have some questions:
- Is it reasonable to perform the comparison by fixing hyperparameters that are optimal in non-DP training? 
- For fixed hyperparameters, $\beta=2$ is still near-optimal? or is it dependent on hyperparameters?

Some minor questions are as follows:
1) In the caption of Figure 4, it is written that the reported three epsilons are based on the minimum epsilon giving $0.98$ accuracy. Why then the accuracy is much worse than $0.98$ in the plots even for $\epsilon^\prime$?
2) Renyi DP is defined in the main paper but is not used as a main part after that. Is there any reason for defining it in the main paper?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the Generalized Gaussian mechanism in Differential Privacy, as extention of typical Laplace and Gaussian noise additions. It proves that the GG family satisfies DP and adapts an existing privacy accounting tool, the PRV accountant, for this purpose. Applying the GG mechanism to PATE and DP-SGD machine learning tools, the authors claim that the Gaussian distribution often optimally balances privacy and accuracy.

### Strengths
The flow of this paper is very easy to follow.

### Weaknesses
The exploration of alternative distributions for DP in this paper does not offer new insights. Previous research, such as the work by Awan and Dong (2022) [1], already provides a comprehensive study on log-concave and multivariate canonical noise distributions in DP. These studies not only predate but also surpass the current paper's approach by offering tightly derived privacy profiles instead of relying on the numerical experiment method adopted here.

The paper's "Privacy Accounting for GG Mechanisms" relies heavily on numerical experiments without robust error control or rigorous proofs. This methodology is particularly concerning since the privacy profile of this noise family is already well-established in the literature. The paper's focus on a single privacy budget (\(\delta=10^{-5}\)) is both arbitrary and unconvincing. For instance, releasing a \(10^{-5}\) portion of the total data satisfies \(\delta=10^{-5}\) with \(\epsilon=0\), making it theoretically superior to all other mechanisms discussed in terms of this metric.

The experiments (PATE, DP-SGD) conducted under the privacy budget of \(\delta=10^{-5}\) are too limited to convincingly demonstrate the superiority of any specific \(\beta\) values. At this \(\delta\) setting, the noise variance added by the mechanisms varies widely, which is very likely to be the true reason behind the differing outcomes. 

For example. for a fixed \(\epsilon\), the Gaussian mechanism will perform poorly for very small \(\delta\) values as the required variancediverge rapidly. In contrast, for the Laplace mechanism, the scale of the Laplace noise remains approximately unchanged. Conversely, when considering Gaussian Differential Privacy (GDP) as the privacy budget, the Gaussian mechanism generally outperforms the Laplace mechanism. There is no intrinsic advantage or disadvantage for either of these two algorithms; their efficacy largely depends on the specific form of the privacy constraint. The statement "This provides a justification for the widespread adoption of the Gaussian mechanism in DP learning" seems coincidental within the scope of this research approach. The preference for the Gaussian mechanism may be more attributed to its strong alignment with GDP accounting, rather than any inherent superiority deduced from the methods used in this research.

It is incorrect (vastly loose) to compute composition privacy budget from a single pair of epsilon and delta (think about composition of Gaussian mechanisms).

In Section B.2, titled "Mechanisms with Equivalent Privacy Guarantees," the selection of \(\sigma\) is derived through random search, not through analytical computation. This approach does not guarantee the avoidance of numerical stability issues (which is very likely to happen for very small $\delta$ when using the PRV accountant's random search to determine \(\epsilon\). The method should at least be executed using well-established mechanisms (Gaussian and Laplace) to validate the outputs against their analytically true values.

Some citations in this paper can be improved to be more relevant. For example, (Kairouz, P., Oh, S., & Viswanath, P. (2015)) [2] as optimal compostion for epsilon,delta DP is more suitable than (Abadi et al., 2016) which is not directly related to the topic after definition 4.

There are some confusions in the proof and presentation (see questions).
For example:
Holder’s Inequality is listed as a lemma
Page 19: "As x goes to infinity, the power of the exponent is negative". It might be better to say " ... is negative for sufficiently large x in terms of ..."
Also see questions


There is some broken link (for example, at the beginning of C.6).

### Questions
What is the purpose for Figure 11? What are the pattens to be shown here?

On page 23 what does "bound the probability of not being (ϵ, 0)-DP" mean? Being DP or not is an intrinsic property of an algorithm, where does the randomness come from?

What is a "'single composition' of the GG mechanism"?

### Soundness
1 poor

### Presentation
4 excellent

### Contribution
1 poor
