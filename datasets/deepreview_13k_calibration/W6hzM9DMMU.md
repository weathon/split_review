# The Benefit of Being Bayesian in Online Conformal Prediction

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 3, 5, 8

## Abstract
Based on the framework of Conformal Prediction (CP), we study the online construction of valid confidence sets given a black-box machine learning model. By converting the target confidence levels into quantile levels, the problem can be reduced to predicting the quantiles (in hindsight) of a sequentially revealed data sequence. Two very different approaches have been studied previously:
\begin{itemize}
    \item \emph{Direct approach:} Assuming the data sequence is iid or exchangeable, one could maintain the empirical distribution of the observed data as an algorithmic belief, and directly predict its quantiles. 
    \item \emph{Indirect approach:} As statistical assumptions often do not hold in practice, a recent trend is to consider the adversarial setting and apply first-order online optimization to moving quantile losses \citep{gibbs2021adaptive}. It requires knowing the target quantile level beforehand, and suffers from certain validity issues on the obtained confidence sets, due to the associated loss linearization.
\end{itemize}

This paper presents a novel Bayesian CP framework that combines their strengths. Without any statistical assumption, it is able to both
\begin{itemize}
    \item answer multiple arbitrary confidence level queries online, with provably low regret; and
    \item overcome the validity issues suffered by first-order optimization baselines, due to being ``data-centric'' rather than ``iterate-centric''. 
\end{itemize}
In addition, it can adapt to an iid environment with the correct coverage probability guarantee. 

From a technical perspective, our key idea is to regularize the algorithmic belief of the above direct approach by a Bayesian prior, which ``robustifies'' it by simulating a non-linearized \emph{Follow the Regularized Leader} (FTRL) algorithm on the output. For statisticians, this can be regarded as an online adversarial view of Bayesian inference. Importantly, the proposed belief update backbone is shared by prediction heads targeting different confidence levels, bringing practical benefits analogous to the recently proposed concept of \emph{U-calibration} \citep{kleinberg2023u}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an algorithm to compute prediction sets in the context of online conformal prediction : given a sequence of previous input and labels, the goal is to compute (for a new observed input) a score threshold leading to a prediction set. 
The main idea of their algorithm is to define, at each step, a mixture of a prior distribution P_0 and the empirical distribution of the previous scores, and to use the quantile of this mixture as score thresholds. This approach is similar to the Follow The Regularized Leader (FTRL) in the bandits literature. From this similarity, the authors compute a regret bound for their algorithm and show that for a simple choice of prior (uniform distribution), their algorithm has a regret of O(\sqrt{T}). In the case of distribution shift, a variant of their algorithm reaches constant discounted regret.
Moreover, contrary to other existing approaches, the authors claim that the prediction intervals computed using their method satisfy a form of monoticity (meaning that the score thresholds for a higher coverage will be higher than those  for a lower coverage). 
Numerical experiments show that the method performs competitively with other approaches (online gradient descent, ERM, etc.)

### Strengths
The paper is overall clearly written (I did not check carefully the math in Appendix B) and the proposed method is both simple and seems to have good guarantees.

### Weaknesses
I would have like more details on the numerical experiments. From what I understand, the figures only show that the method reaches the target coverage, but what about the size of the prediction sets that it produces ? How does it compare to other methods ? Also, the memory usage of the method ( O(\sqrt(T}) for the quantized version) seems redhibitory at first glance, but is not evaluated in practice in the experiments.

### Questions
- In general in Bayesian methods for UQ, the role of the prior is very important to have good performance. So I would be curious to know if other reasonable choices of priors for the score thresholds would improve the regret compared to the uniform prior (apart from the one mentioned in line 320). Is this something that you have explored ?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper  presents a  novel approach to online conformal prediction (CP) that uses Bayesian regularization to overcome the limitations of previous direct and indirect CP methods. Conventional methods rely either on empirical quantile predictions (direct approach) or on adversarial optimization (indirect approach).  The Bayesian approach presented here addresses these issues by introducing a regularized Bayesian framework that combines empirical and prior-based distributions, thereby enabling more robust predictions without statistical assumptions about the data distribution.

Key contributions include:
- by implementing Bayesian regularization, the model provides reliable confidence sets that avoid the validity problems of purely adversarial CP methods, such as non-monotonicity across confidence levels.
- The Bayesian CP model achieves an optimal regret boundary, maintains competitive performance across different confidence levels, and provides stable results in both iid and adversarial contexts.
- Unlike traditional methods that require a single preset confidence level, the Bayesian approach supports online responses to arbitrary confidence queries - a critical improvement for dynamic, real-world applications.

The framework is theoretically validated with regret bounds and empirically demonstrated on both synthetic and real-world datasets, showing superior adaptability and efficiency compared to existing CP methods.

### Strengths
- The paper is clearly written and comprehensively explains its novel Bayesian approach to online conformal prediction. It effectively outlines the limitations of existing methods and clearly presents its contributions. The theoretical foundations are well-developed, and the empirical results are presented to complement the theory, making the concepts accessible to readers. The structure allows for an easy understanding of the core ideas, technical details, and the practical advantages of the proposed method.
- The paper contains many interesting results, which are novel to my best knowledge
    - Theorem 2 establishes the regret bound for the Bayesian CP algorithm, showing that it achieves \( O(R\sqrt{T}) \) regret for any sequence length \( T \) and confidence level \( \alpha \) in adversarial settings.
    - Theorem 3 introduces the quantized version of the algorithm, demonstrating that it achieves the same \( O(R\sqrt{T}) \) regret bound with reduced memory requirements of \( O(\sqrt{T}) \).
   -  Theorem 4 shows, under the iid assumption,  that the Bayesian CP algorithm achieves probabilistic coverage guarantees similar to ERM-based CP in iid contexts.
   - Theorem 5  addresses the excess quantile risk under the iid assumption, demonstrating that the Bayesian CP algorithm achieves similar performance as traditional ERM approaches in iid environments.
   - Theorem 6 provides a discounted regret bound for the variant of the Bayesian CP algorithm designed to handle continual distribution shifts. This bound matches minimax optimality, indicating the algorithm’s resilience in non-stationary environments.

### Weaknesses
I do not see serious weak points.

### Questions
- Can you provide more details on MultiOGD [in Section 2]. The current version is so sketchy that it is difficult to read.
- Provide more details in Section 3 [I know that the paper is short, you could provide more details in the appendix for example]

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors aim to contribute to the burgeoning literature on conformal prediction, in particular the approach based on quantile tracking.  The main goal of the paper is to develop a method that treats a set of alpha values, and not a single alpha value that has been fixed a priori.  The technical approach is essentially follow-the-regularized leader (FTRL) on the pinball loss, with an interpretation of the regularization in FTRL as a (nonparametric) Bayesian prior.

### Strengths
It is true, and perhaps helpful, to point out that quantile-tracking algorithms can be incoherent in terms of the confidence sets that they deliver for different values of alpha.  It is also useful to point out that FTRL can address this issue.  Some of the other detailed critiques of Gibbs & Candes (e.g., the overshooting) are reasonable.

### Weaknesses
I'm not entirely sure what I've learned from the paper, other than being reminded of some of the virtues of FTRL.

Indeed, I want to emphasize that as best I can tell, this is a FTRL paper.  The connection to Bayesian inference is weak at best, and not very helpful.  There's a regularizer, but that alone doesn't make for Bayesian inference.  At the end of the paper, there's a suggestion that when regularization involves adding a uniform distribution to an empirical distribution we can interpret this as the (posterior mean) of a Dirichlet process, but I'm at a loss as to why that kind of Bayesian nonparametric terminology is called for here.  Note in particular that a Bayesian would consider the observations forming the empirical distribution to be iid draws from a multinomial, quite out of the spirit of the "no statistical assumptions" statement that the authors make.  Moreover, if one is really wanting to be Bayesian here, then it's the entire quantile process that should be the object of inference.

The main motivation of the paper doesn't seem to be Bayesian at all, but rather simply online learning, in a setting in which quantiles corresponding to multiple alpha values are desired.  Now, I'm not sure exactly when and how multiple alpha values might be desired by a downstream user.  Is there a decision-theoretic justification for asking for this?  The authors don't go much beyond simply suggesting that it's desirable in some intuitive sense.

There are frameworks in statistics for making repeated tentative decisions over time, e.g., the nonnegative supermartingale
approach, and such decision-theoretic frameworks are clearer (to me) ways of getting at the issue being hinted at here.

The other motivation for pursuing this approach is the "paradox" (lack of invariance to permutations) associated with quantile tracking. 
But this critique seems to lose its punch when one remembers that one of the main motivations for the quantile tracking approaches
is that of handling nonstationarity.

### Questions
My main suggestion is to be clearer on what exactly a downstream user might be asking for, in specific inferential use cases, to support the goal of tracking with respect to multiple alpha values simultaneously.  A secondary suggestion is to clarify in what sense this is really Bayesian inference, beyond simply having a sum-of-distributions interpretation.  Why isn't this just an FTRL story pure and simple.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method for online conformal prediction leveraging a Follow-the-Regularized-Leader approach, where the regularization is derived from a prior. Theoretical justification for the method is provided by the means of regret bounds. The method is empirically evaluated on synthetic data as well as financial time series.

### Strengths
The key idea of having an online conformal prediction method mimic online bayesian inference methods is interesting, and, as far as I am aware, original. The text is reasonably clear, and the authors provide a substantial number of theoretical guarantees, substantiating their method's strength. The inclusion of analyses in the IID case (i.e., not just an arbitrarily adversarial case) is appreciated.

### Weaknesses
The paper has a number of significant weaknesses.

- Line 117: The first paradox does not seem paradoxical at all. We are in a setting where, in principle, exchangeability does not hold. That precisely means that the order in which we have observed our data carries information. So our method *should not* be invariant to this order!
- The paper is about online conformal prediction, and thus for settings where exchangeability & IID do not hold. However, the paper focuses excessively on the IID setting, except for a single section (Section 3.3), which introduces a separate algorithm (dubbed 'Discounted') and a corresponding theorem (Theorem 6), and Theorem 2. And Theorem 6 does not seem to agree with the text surrounding it; the 'optimal' predictions considered for the regret bound seems to be constant over the course of the whole time (since the min over $r$ is outside the sum over time), which is deeply uninteresting. Any minimally decent predictor in the continual distribution shift setting should have predictions that change over time. Theorem 2 suffers from the same issue. (A simple case where these things really matter is when your are in an adversarial setting with increasing conformity scores over time. No single prediction is going to be enough, you must increase your intervals over time!)
- The experimental evaluation is very weak. Online conformal prediction is a topic that requires significant experimental evaluation. The paper's theoretical contributions aren't notable enough nor are any new things possible with the proposed method, so an advantage of the method validated through experiments (e.g., that the coverage would be more robust, or that the intervals would be smaller) is essential.
    - The only data considered was one synthetic dataset and stock market data. The main problem is, of course, with the real data; only stock market data was considered. Data coming from the stock market (and especially price time series) have very particular structure. The authors should consider many other time series. Moreover, considering all the attention that the authors laid on the IID setting, there was no dataset considering it (but, to be clear, I would rather the authors deemphasize the IID setting than an additional focus of experiments on IID data).
    - The baselines being considered are severly lacking. The authors consider ACI (Gibbs & Candès, 2021) and MVP (Bastani et al., 2022). While I wholeheartedly agree that these two methods should be present, they are already a bit dated, and considering only them brings a misleading comparison, as they are not quite the state-of-the-art anymore. Here are some other methods I suggest comparing against:
        - AgACI (https://arxiv.org/abs/2202.07282)
        - Bellman CP (https://arxiv.org/abs/2402.05203)
        - Copula CP (https://arxiv.org/abs/2212.03281)
        - Conformal PID control (https://arxiv.org/abs/2307.16895)
    - Finally, I must note that even with the lacking experimental comparison, I don't exactly see an advantage of the proposed method compared to the baselines.

Additionally, a number of nitpicks (which do not impact my score, but should probably be improved upon):

- Line 073: "without any statistical assumption at all" -- that's not right. While the assumptions are indeed quite lax, there _are_ statistical assumptions: namely, that the protocol described in lines 054-063 is followed (which implies, e.g., that confidence level chosen for a time step is independent of the outcome conditional on the past along with the new covariates).
- On the definition of the quantile in equation (2), you should consider the infimum rather than the minimum to ensure that the quantile is well-defined.
- Line 096: I'd expect a reader of this paper to be familiar with exchangeability. " a relaxation of iid called exchangeability" sounds like talking down. Also, consider citing https://arxiv.org/abs/2005.06095, which is an excellent reference on exchangeability and CP.
- Section 2 should probably be moved to the experiments section, or even the supplementary material. The experiment and the fact that it is embasing has already been mentioned in the introduction; additional motivation is not needed.
- Calling the proposed method 'Bayesian' feels a bit like a misnormer. There is no statistical model being used for Bayesian inference, no likelihood and no Bayes update. It is only related to Bayesian inference by the analogy of regularization being typically equivalent to some form of Bayesian inference and the specification of a 'prior' distribution. That said, again, this is a nitpick and has not weighted into my decision.

### Questions
My main gripes with the paper are:

- Too much focus on the IID setting (which is not what online conformal prediction is about)
- Theoretical results for non-IID data being lacking;
- Lacking experimental analysis;
- From the existing experimental analysis, I see no clear advantage of the method, and the theoretical contributions are not notable enough to compensate for it.

(All of them are better described in the 'Weaknesses' section.)

Any clarification or improvement on these points are appreciated.

I believe that, in its current form, the paper is not ready for acceptance, due to the issues raised above, and have thus opted for rejection.
That said, I would be willing to increase my score (and perhaps substantially) should my concerns above be resolved.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose a Bayesian frame work for comformal prediction, bridging the two scenarios of "data-centric" approach where usually iid/exchangibility assumption is required, and the "iterate-centric" approach which is more robust towards distributional shift.

The Bayescian CP method has a few desired properties: the confidence sets are montone in the nominal confidence level $\alpha$ for the online prediction; the $O(\sqrt{T})$ regret bound is achieved; the method adapts to both the iid case and distributional shift case with properly chosen step size.

### Strengths
The paper is well-written and clear to its points. The Bayesian method proposed is easy to understand and implement. The theoretical guarantees of a tight regret bound is provided, and the CIs are monotone in the nominal level $\alpha$. The method enjoys both desired properties for "data-centric" and "iterate-centric" approaches, and is able to recover previous known bounds under properly chosen learning rate. Numerical experiments comparing to previous benchmarks were provided.

### Weaknesses
1. The uniform prior is robust, but as the authors had mentioned, if certain knowledge is known a tighter bound could be achieved potentially. I would be interested to see more fine-grained analysis in this scenario, and whether there is a way to update the regularized belief instead of using the same one upon observing more data. Specifically, the paper does not explore how the choice of prior affects the convergence rate or the tightness of the confidence intervals, beyond the general robustness of the uniform prior. A more detailed analysis of how different priors, especially those incorporating some form of prior knowledge, could lead to improved performance would be valuable. For instance, a Gaussian prior centered around a reasonable initial estimate could potentially lead to faster convergence in certain scenarios, but the paper does not explore this direction.
2. For the continual distribution shift case, the learning rate is constant for the discounted regret. There seems to be a gap of choosing diminising ($O(1/\sqrt{t})$) step size and $O(1)$ step size, and how to choose this adaptively. The paper does not provide a clear mechanism for adapting the learning rate to the severity of the distribution shift. A fixed learning rate might be suboptimal in scenarios where the distribution shift is either very slow or very abrupt. It would be beneficial to investigate adaptive learning rate strategies that can automatically adjust to the changing environment, potentially by monitoring some measure of distribution change.

### Questions
1. Is it possible to achieve lower regret by adpatively choosing the regularized belief?
2. Is there a way to detect distributional shift such that the step size can be chosen adaptively? Is there a uniform way to measure the performance/regret for both the iid/exchangeable case and the distribution shift case?

### Soundness
4

### Presentation
4

### Contribution
3
