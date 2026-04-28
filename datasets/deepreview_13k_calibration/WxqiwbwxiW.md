# An Information-Theoretic Analysis of Thompson Sampling for Logistic Bandits

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
We study the performance of the Thompson Sampling algorithm for logistic bandit problems, where the agent receives binary rewards with probabilities determined by a logistic function $\exp(\beta \langle a, \theta \rangle)/(1+\exp(\beta \langle a, \theta \rangle))$. We focus on the setting where the action $a$ and parameter $\theta$ lie within the $d$-dimensional unit ball\notes{ with the action space encompassing the parameter space}. Adopting the information-theoretic framework introduced by~\cite{russo_information-theoretic_2015}, we analyze the information ratio, which is defined as the ratio of the expected squared difference between the optimal and actual rewards to the mutual information between the optimal action and the reward. Improving upon previous results, we establish that the information ratio is bounded by $\tfrac{9}{2}d$. Notably, we obtain a regret bound in $O(d\sqrt{T \log(\beta T/d)})$ that depends only logarithmically on the parameter $\beta$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates Thompson Sampling (TS) in the context of logistic bandit problems, where rewards are binary and determined by a logistic function. The authors analyze the information ratio to provide a refined regret bound that scales logarithmically with the slope parameter of the logistic function, $\beta$, independent of the number of actions. This approach purportedly improves upon prior bounds that exhibit exponential dependency on $\beta$. Additionally, the paper presents conditions under which dependence on certain alignment constants can be reduced, along with theoretical regret bounds based on this framework.

### Strengths
1: The paper offers a refined theoretical analysis for Thompson Sampling in logistic bandits, claiming improved regret bounds that scale logarithmically with $\beta$.

2: The use of information-theoretic concepts, particularly the information ratio, is well-aligned with recent trends in bandit research and has the potential to contribute to a deeper understanding of the regret of logistic bandits.

### Weaknesses
1. Lack of technical novelty: while the paper presents a refined analysis, the techniques used are predominantly based on established methods. The information-theoretic approach and analysis of TS have been well-studied in prior work. The paper could benefit from highlighting the unique challenges or technical hurdles in applying these methods to logistic bandits, which are not sufficiently emphasized.

2. Narrow scope: The scope of the study is somewhat limited to logistic bandits without any exploration into a broader class, such as generalized linear models. 

3. The paper does not introduce any new algorithms or propose an experimental validation to support its theoretical claims. 

4. Bayesian Regret Bounds: The preference for Bayesian regret bounds over frequentist bounds may not appeal to other audiences.

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
The paper studies the performance of Thompson sampling for logistic bandit problems and improves upon previous results.

### Strengths
Using the information theoretic framework of (Russo & Van Roy, 2015), this paper improves upon the previous regret bounds for Thompson sampling in logistic bandit problems. In particular, it removes dependence on the "fragility dimension" which is known to grow exponentially in some cases.

### Weaknesses
1. In Lines 77 to 83, it is claimed that the main result of (Dong et al, 2019) is incorrect. This is a strong claim that requires an equally strong proof.  
First, it is claimed that they do not provide a rigorous proof for generalizing their bound to larger values of $\beta$. However, there is no discussion about the specifics of this proof or why it might not be rigorous.     
Second, it is claimed that their regret analysis relies on the rate-distortion bound in (Dong & Van Roy, 2018) which specifically requires a bound on the "one-step compressed Thompson sampling information ratio". However, the result of (Dong & Van Roy, 2018) that is used in (Dong et al, 2019) is stated in the form of Proposition 9 in (Dong et al, 2019) and does not require such bounds. It is true that this result, as it is written does not appear in (Dong & Van Roy, 2018). Proposition 9 in (Dong et al, 2019) is based on Theorem 4 in (Dong & Van Roy, 2018) which uses the notion of one-step compressed information ratio. However, when the (normal notion of) information ratio is bounded, then the result seems to be simpler to prove. In fact, looking at the proof of Theorem 4 in (Dong & Van Roy, 2018), it seems that the the notion of one-step compressed information ratio only appears through Conjecture 1 and if we instead have a uniform bound on information ratio, then we could directly use Proposition 1 instead of Theorem 1 and obtain the result stated in (Dong et al, 2019).  If my understanding is correct, then the mistake in (Dong et al, 2019) is that they didn't include an argument in the spirit of what I described, but their result holds.

2. Proposition 11 in (Dong et al, 2019) states that no regret bound of the form $f(\alpha)p(d)T^{1 - \epsilon}$ is possible. This does not imply that removing dependence on alpha is not possible. A claim that is mentioned both in the paragraph from lines 292 to 298 and in the conclusion section. Instead, what it implies is that removing dependence on both beta and eta *at the same time* (without introducing other problem-dependent terms) is not possible. The regret bound of (Dong et al, 2019), specifically in their Theorem 5, removes dependence on beta, but depends on eta. (which in some cases may grow exponentially) Your regret bound, in Theorem 2, removes dependence on eta, but depends on beta.

3. In the case A = O, Corollary 2 seems to be a weaker version of Theorem 1 in (Dong et al, 2019). A sentence should be added next to the Corollary to discuss how it compares to that theorem.

### Questions
Why can we assume that the mapping $\pi_*$ is one-to-one?
This is mentioned in the footnote of page 3, but this argument seems to be about settings where we could duplicate actions.
Is this trivial that we could do that in the logistic bandit setting?

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
4

### Summary
The paper analyses the Thompson Sampling (TS) algorithm applied to logistic bandit problems, where an agent selects actions based on binary rewards determined by a logistic function. The author defines the minimax alignment constant $\alpha:= \min_{\theta \in \mathcal{O}} \max_{a\in \mathcal{A}} <a, \theta>$ to be included in the regret upper bound (also appears in Dong et al., 2019 as the \textit{ worst-case optimal log odds}) where $\mathcal{O}$ is the parameter space and $\mathcal{A}$ is the action space. The final regret bound is $O(d/\alpha \cdot T^{1/2})$ ignoring the logarithmic factor, where $d$ is the dimension of the parameter space and $T$ is the time horizon. The author improves the regret bound shown in Dong et al., which is believed to be the most relevant proceeding work, by dropping the fragility dimension $\eta$. Since $\eta$ could go exponentially with dimension $d$, dropping the dependency on $\eta$ can tighten the regret upper bound.
The regret bound present in this work is also believed to be the first regret bound for logistic bandits that achieve $\log(\beta)$ dependency.

### Strengths
The paper is well-written with clear explanations and well-structured arguments that enhance the accessibility of complex ideas. The upper bound of regret is tighter than the most advanced result in the literature. The proof stream is clear to the reader.

### Weaknesses
In comparing results from multiple works (table 1), Dong et al. have not been included, while it should be an important preceding since some major concepts are borrowed from there, such as the minimax alignment constant. Essentially, the work should emphasize the improvement of Dong et al.

Also, the details of the Thompson Sampling algorithm could be elaborated more, such as how the posterior sampling distribution has been established and how the parameters have been updated once the agent collects a new reward.

### Questions
Please refer to the weaknesses.

### Soundness
3

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
The authors derive regret bounds for Thompson sampling applied to a logistic bandit setting. In particular, the authors use the information-ratio technique (Russo & Van Roy) to first upper bound the information ratio, and use that to obtain the regret bound. Crucially, the regret bound is only logarithmically dependent on the "logistic function parameter". Furthermore, though the general regret bound the authors propose has a 1/\alpha term, \alpha being the minmax alignment constant, and this is impossible to remove (as observed in Dong & Van Roy), the authors look at special cases where the dependency can indeed be removed, leading to sub-linear regret bound \tilde{O}(d\sqrt{T}).

### Strengths
The main strength of the paper is that it resolves previous gaps in the theory for Thompson sampling applied to logistic bandits. Specifically, this is the first work that has a log dependency on the logistic function parameter, when the number of actions can be large. The authors also show that in the case when the action spaces encompasses the parameter space, the expected regret of Thompson sampling does not depend on the min-max alignment constant, which was previously known to be an obstacle in obtaining good regret bounds.

### Weaknesses
I don't have any particular weaknesses in mind, except the compatibility of the paper to the conference. It would also be nice for the authors to talk about some practical implications.

### Questions
Can the results be extended to information directed sampling?

### Soundness
3

### Presentation
3

### Contribution
3
