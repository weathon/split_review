# Bayesian Binary Search

- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 3, 6, 5

## Abstract
We present Bayesian Binary Search (BBS), a novel probabilistic variant of the classical binary search/bisection algorithm. BBS leverages machine learning/statistical techniques to estimate the probability density of the search space and modifies the bisection step to split based on probability density rather than the traditional midpoint, allowing for the learned distribution of the search space to guide the search algorithm. Search space density estimation can flexibly
be performed using supervised probabilistic machine learning techniques (e.g., Gaussian process regression, Bayesian neural networks, quantile regression) or unsupervised learning algorithms (e.g., Gaussian mixture models, kernel density estimation (KDE), maximum likelihood estimation (MLE)). We demonstrate significant efficiency gains of using BBS on both simulated data across a variety of distributions and in a real-world binary search use case of probing channel balances in the Bitcoin Lightning Network, for which we have deployed the BBS algorithm in a production setting.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This work proposes to use bayesian method to do binary search where the midpoint is not equal to the average of an internal, in contrast to the classical binary search method.

Although this idea sounds interesting, I am not convinced by the proposed method, either based on the experimental results or the presentation.

Experiment:
The authors spent so much time listing all variants of binary search in the introduction. However, during the experiments, the authors only compare with the most basic baseline, ignoring everything the authors have discussed at the beginning.

### Strengths
The authors ask a good research question --- how we should perform binary search when the uniform distribution assumption does not hold.

### Weaknesses
Lack of baselines. The authors discuss many variants of binary search during introduction. However, none of them are used as baselines for comparison other than the classical binary search method.

Plus, the proposed method described here is not very different from doing active learning using Gaussian Process.

One more thing, doing density estimation can be time consuming. This could ultimately slow down the the search process and be much slower than the classical binary search method.

### Questions
Can you compare with all baselines you listed in your introduction paragraph and report results during rebuttal?

How is your method different from active learning via the help of Gaussian Process?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present a modified version of the standard binary search algorithm by incorporating probabilistic techniques. They consider the input to their Bayesian Binary Search (BBS) algorithm as an ordered sequence of integers, $x_1, \ldots, x_n$, where each $x_i$ is assumed to be an IID sample from an unknown distribution $\mathbb{P}$.

If the distribution $\mathbb{P}$ were known and had a density function $p$, binary search could be optimized by using the median $m$ of the distribution as the pivot:
$$
\int_{-\infty}^m p(x) \, \mathrm{d}x = 0.5
$$
instead of using the midpoint of the current upper and lower bounds in the sequence.

Since the distribution $\mathbb{P}$ is typically unknown, the authors propose estimating the density of the sequence $x_1, \ldots, x_n$ to obtain an approximation $\hat{\mathbb{P}}$ of $\mathbb{P}$, using it as a surrogate in their probabilistic binary search algorithm.

The authors conduct an empirical evaluation of the algorithm, using synthetic data generated from a discretized univariate Gaussian distribution and a real-world dataset from the Lightning Network.

### Strengths
BBS is shown to improve efficiency in non-uniform search spaces, as evidenced by lower average steps to reach target values compared to standard binary search, especially in scenarios with a known or estimable distribution of search targets.

The real-world example on the Lightning Network demonstrates a potential real-world use of the algorithm, if implemented appropriately.

### Weaknesses
There is nothing "Bayesian" about the proposed algorithm. Perhaps a more appropriate name would be "Probabilistic Binary Search".

On the Lightning network experiment:

The primary weakness of the experiment lies in a misalignment between the stated motivation for Bayesian Binary Search (BBS) and its actual implementation.

- The experiment does not apply BBS to actual probing in the Lightning Network, where probing costs (in terms of network resources and latency) are the main concern. Instead, they simulate probing by using inexpensive predictions from a random forest model, which removes the practical need for BBS to reduce costly network probes.

- Since predictions from the random forest are computationally cheap, the added complexity of BBS (which relies on density estimation and probabilistic bisection) offers limited benefit in this context. 

- There is no reported raw computation time. The added computational overhead of first performing density estimation would likely be much larger than the marginal gains achieved when performing BBS over binary search.

In summary, the experiment does not convincingly demonstrate BBS’s utility in addressing real-world probing expenses. Without actual network interaction, it fails to showcase how BBS would reduce probing costs in a live setting, which is the central argument for its use.

### Questions
Have the authors considered demonstrating the use of BBS in a live, online setting, where probing costs are relevant? Since the current experiment is based on offline predictions, it’s unclear if the BBS approach would indeed reduce costs in a real-world probing scenario within the Lightning Network.

### Soundness
2

### Presentation
1

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
This paper introduces Bayesian Binary Search (BBS), a probabilistic approach compared to the traditional binary search, and it aims to improve search efficiency when the target distribution is non-uniform and the probing is expensive. BBS modifies the traditional binary search by replacing the midpoint splitting with median splitting w.r.t an estimated PDF.

Contributions include
1. Novel algorithm framework: the formulation of BBS integrates PDFs into binary search, and various of PDF estimation methods are supported in this framework. This framework promises better efficiency for non-uniform distribution, while reduces to traditional binary search when the distribution is uniform.
2. BBS demonstrates robust performance through KL divergence simulations, which shows graceful degradation as PDF estimation accuracy decreases
3. Showcase a real-world application in Bitcoin Lightning Network. The development of random forest PDF estimation methods using network features is itself valuable for practical implementations with BBS.

### Strengths
Originality
1. Creatively combines classical binary search with probabilistic methods and introduces a flexible framework for incorporating various of PDF estimation methods
2. Provides a new perspective on search optimization through statistical learning

Quality
1. Clear mathematical formulation and intuitive algorithm design
2. Rigorous analysis of robustness of BBS through KL divergence degradation simulation

Clarity
1. The paper is well structured and the clarity is pretty good

Significance
1. Interesting application to Bitcoin Lightning Network
2. This proposed framework can be easily implemented using various existing ML tools, and its significant performance improvements make it highly practical

### Weaknesses
1. Lack the theoretic analysis of optimality of median split strategy
2. Lack theoretic analysis for convergence bounds with imperfect PDF estimation
3. The paper mentioned a few methods for PDF estimation (RF, GPR, BNN, etc.), however, only RF was used for the Bitcoin Lighting Network problem. Since PDF estimation is a crucial piece in the algorithm framework, it is necessary to offer comparative analysis among different PDF estimation approaches, as well as discussion of the trade-offs.
4. Simulation study covered only the three basic distributions, but for real-world applications, it is common that the distribution is heavy-tailed or complex. I would expect more comprehensive analysis over real-world distribution patterns

### Questions
1. Beyond Lightning Network, can you elaborate on other applications you think would benefit most from BBS?
2. What characteristics make an application suitable for BBS?
3. Other than median splitting strategy, have you considered other strategies in probability space, and what are the trade-offs?

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
The authors revisit bisection by introducing a probability density over the search interval rather than the usual uniform assumption. The main change is to cut where the probability reaches 50% rather than in the middle of the search interval. To estimate the required probability density, several alternatives are proposed. Then some simulation experiments are proposed.

### Strengths
- The experiments show some improvements over a simple baseline.
- A realistic application is considered: probing channel balances in the Bitcoin Lightning Network.

### Weaknesses
 - The problem definition lacks the assumptions: for instance, bisection can only work if the underlying function is monotonous.  Otherwise, the problem may be of contour or level set estimation.
- It is not possible to separate the contribution from what already exists in the literature.
- The comparison is against a single simple baseline. Why not including comparisons with some of the cited references, like Waeber et al., or Jedynak et al?

- The empirical evaluation lacks sufficient comparisons to existing methods. While the authors propose a novel approach to bisection by incorporating a probability density, the experimental section does not adequately demonstrate its superiority over existing methods. The comparison to a single baseline is insufficient to validate the proposed method's effectiveness, especially given the existence of other probabilistic bisection algorithms. The lack of comparison with these algorithms makes it difficult to assess the true contribution of the proposed method.

- The variance over repeated runs is zero in some tables, which suggests that the experimental setup might be too simplistic or that the method is not being evaluated under sufficiently challenging conditions. The fact that the number of steps to reach a bracket size is independent of the target location for standard bisection is not surprising, but it raises questions about the relevance of the experiments. The use of rounding to find the next median introduces a minor source of variance, but this does not fully explain the zero variance in some cases. This suggests that the experimental setup needs to be re-evaluated to ensure that the method is tested under a wider range of conditions.

### Questions
Could you clarify the assumptions and highlight better the contribution? 
Under which conditions is the search provably successful? How does it depend on the estimated pdf error?

How is the variance over repeated runs zero in some tables? Perhaps the problem is too simple?

For Bayesian optimization: see e.g., Garnett, R. (2023). Bayesian optimization. Cambridge University Press. And for other probabilistic bisection algorithms: 
- Rodriguez, S., & Ludkovski, M. (2020). Probabilistic bisection with spatial metamodels. European Journal of Operational Research, 286(2), 588-603.
- Frazier, P. I., Henderson, S. G., & Waeber, R. (2019). Probabilistic bisection converges almost as quickly as stochastic approximation. Mathematics of Operations Research, 44(2), 651-667.

Typos:
- specifoed
- Maxmimum

### Soundness
2

### Presentation
2

### Contribution
2
