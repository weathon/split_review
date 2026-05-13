# Variational Search Distributions

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
We develop \gls{vsd}, a method for finding and generating discrete, combinatorial designs of a rare desired class in a batch sequential manner with a fixed experimental budget. We formalize the requirements and desiderata for active generation and formulate a solution via variational inference. In particular, \gls{vsd} uses off-the-shelf gradient based optimization routines, can learn powerful generative models for designs, and can take advantage of scalable predictive models. We derive asymptotic convergence rates for learning the true conditional generative distribution of designs with certain configurations of our method. After illustrating the generative model on images, we empirically demonstrate that \gls{vsd} can outperform existing baseline methods on a set of real sequence-design problems in various biological systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper casts sequential black-box optimization as a variational inference (i.e. amortized optimization) problem, and uses this perspective to unify a collection of different black-box optimization algorithms under a common theoretical framework and presents some proof of concept results on easy sequence optimization tasks.

#### UPDATE - 12/02/2024 ####
After extended discussion and an exceptionally thorough response from the authors, my concerns have been addressed and I am recommending acceptance. I believe this paper presents a very nice conceptual view of the topic of active generation and the empirical results raise interesting questions. I encourage my fellow reviewers to review the updated manuscript and re-evaluate their scores. I have left my original review unaltered for any interested readers.

### Strengths
This paper demonstrates a clarity of thought and composition that is commendable, I particularly enjoyed the related work section.

Likewise I do not have any major concerns regarding the technical soundness of the results presented.

As a good conceptual introduction to the topic, I think this draft could be useful to researchers new to the topic with some revisions.

### Weaknesses
I have two general impressions of this paper. 

First, it seems like the authors have not really chosen a direction for the paper. There are at least three different directions here, A) a unifying view of sequential black box optimization algorithms, B) a practical algorithm for sequential BBO, and C) theoretical analysis of convergence rates of a particular sequential BBO algorithm under strong assumptions. I would suggest you pick no more than two directions, preferably one. I actually think this particular subfield could really benefit from a more holistic perspective of the work that has been done, as I constantly see minor variations of these algorithms in my social media feed and review stack with no apparent awareness of the relationships between them. From what I can tell from this draft, it seems that A and C likely play more to your strengths.


Second, the authors seem blissfully unaware of a substantial body of work on this topic. To be quite candid, the paper reads like it was written circa September 2021. This is not mere rhetoric. The most recent baseline the authors consider was published at ICML 2021. It is also odd that two of the baselines you did include, DbAS and CbAS, are not even designed for the sequential setting. As a very active researcher in this exact area, I struggle to understand who this paper is for and how the authors pictured their place in the broader dialogue on this topic. I am sure you worked very hard on this paper and I commend your effort, but I honestly believe the best advice I can give you is to talk to more people working on this topic, preferably from outside your immediate academic circle. While it is difficult to hear this feedback, one of the functions of peer review is to reveal "unknown unknowns". I want to be sure this review is constructive, so I will provide some key references if you are serious about diving into this topic. You should also consider making use of tools like [Connected Papers](https://www.connectedpapers.com/) to improve your literature review process and avoid this situation in the future. 

You can start with [A survey and benchmark of high-dimensional Bayesian optimization of discrete sequences](https://arxiv.org/abs/2406.04739). This work is the most up-to-date complete survey on the topic I have seen, and the benchmarking rigor is notably good. This paper is associated with two repositories, [poli](https://github.com/MachineLearningLifeScience/poli) and [poli-baselines](https://github.com/MachineLearningLifeScience/poli-baselines). The former contains a suite of test functions that are much more up to date than the combinatorially complete landscapes considered in this paper, and the latter contains a suite of baseline solvers. You may even want to consider contributing your method as a solver to poli-baselines at some point.

Some key axes of variation to consider: 

How is the optimization problem solved? Most fall into one of three categories, directed evolution (which you seem to be familiar with based on your inclusion of AdaLead and PEX), generative search with explicit guidance, e.g. [2, 3, 4, 5, 6], and generative search with implicit guidance [7, 8], which can also be seen as a kind of amortized search. I could cite more papers but I believe I have made my point. Algorithms also differ in their handling of constraints, and their approach to managing the feedback covariate shift induced by online active data collection by an agent. 

In particular I will draw your attention to [a tutorial for LaMBO-2](https://github.com/prescient-design/cortex/blob/main/tutorials/4_guided_diffusion.ipynb) if you want to start considering more up to date baselines, however I would recommend using the solver interface provided in poli-baselines for actual experiments. You may also be interested in Ehrlich functions if you would like a convenient test function that is much more difficult to solve than small combinatorially complete landscapes but still easy to work with [9]. Ehrlich functions are available in [a small standalone package](https://github.com/prescient-design/holo-bench) or [as part of the poli package](https://machinelearninglifescience.github.io/poli-docs/using_poli/objective_repository/ehrlich_functions.html).

While I'm sure this is not the outcome you hoped for, science is a dialogue, and good science requires awareness of what is happening outside your academic niche. Hopefully my feedback is clear and actionable enough to benefit this work and your progression as a scientist.

### Questions
The following questions are sincere:

- Who is the audience for this paper? 

- What questions is this paper answering?

- What does the variational inference framing get us in the end? Access to a set of tools for theoretical analysis?

### Soundness
4

### Presentation
3

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
The authors propose a black box varoiational inference approachfor discrete designs generation. The authors derive asymptotic convergence rates for learning the true conditional generative distribution of designs. Compelling results on high dimensional sequence-design problems are demonstrated.

### Strengths
* The problem is important as it has applications in pharmaceutical drugs/enzyme design.
* The paper paper is well written and the method is sound
* Experimental results on high dimensional datasets demonstrate superiority of the approach

### Weaknesses
 * The method lacks novelty, it's based on putting together blocks that have already been proposed in the litterature
* The paper clarity can be improved with an overview plot of the method



### Questions
* What's 'x' in the title of Figure 1?
* What are the limitations of this approach?
* How is diversity within a batch enforced? 
* The reverse KLD is known to result in mode collapse. Why wasn't this an issue?
* Which variation reduction method did you use for the gradient estimator?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper develops the variational search distribution method to solve the active search problem in biological design. VSD estimates the super level-set distribution in a sequential manner by generating batches of data points for sequential experiments. Empirical results on optimizing protein fitness in several datasets showcase the effectiveness of VSD.

### Strengths
- The paper formulates the batch active search problem in the variational inference framework and provides theoretical guarantees to the learned distribution based on the sequentially attained data.
- Experimental results on real-world biological datasets demonstrate the practical use of the algorithm and its effectiveness to solve the problem.

### Weaknesses
 - The precision of VSD and most other methods is decreasing with more rounds in TrpB and TFBIND8 datasets while the recall values are in general low. However, an ideal method should achieve a better estimation of the ground truth super level-set distribution as more samples are collected. This may be due to the initial training set size being too large or the fitness landscape being easy to model. How do the models perform with a smaller initial training set size? Specifically, it is unclear if the observed decrease in precision is due to the method's inability to explore the space effectively after initial rounds, or if the fitness landscape is simply being exhausted of novel designs. A more detailed analysis of the precision-recall curves, perhaps broken down by the novelty of the discovered sequences, would be beneficial.
- How is VSD compared with the simple and commonly used directed evolution method? It is not clear whether the reported improvements are solely due to the use of a fitness prediction model (as in AdaLead), or if the variational search distribution method itself provides additional benefits over simpler active search strategies. A direct comparison with a basic directed evolution approach, without the use of a fitness prediction model, would help clarify the contribution of the proposed method.

### Questions
- How robust are the results to the selection of the threshold $\tau$ and the batch size $B$?
- While the reviewer is not familiar with the field, could the authors give some intuitions about the difference between VSD and active learning approaches like Bayesian optimization, and why VSD is better?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a novel variational method for learning to sample from rarely observed events, aiming to minimize a distance between the distribution of interest, namely $p(x∣y>t)$, and its parametric variational counterpart $q(x|\phi)$. The problem is reformulated to leverage the “whole dataset,” not just rarely observed events, and is expressed as Equation (5), which comprises two terms: $log p (y>t∣x)$ and the negative KL divergence between$q(x|\phi)$ and $p(x)$. The authors' final proposal is to estimate $p(y>t∣x)$ using a parametric function instead of a simple PI estimate. The variational distribution is optimized by a REINFORCE gradient estimator.

### Strengths
The paper is clear, well-written, and aligns with well-established benchmarks in the field, such as CBAS (Brookes et al.). 
The model is supported by convergence analysis and an extensive set of well-handled experiments.

### Weaknesses
While the model description is clear, the model comprise a parametric distribution $p(x|D_0)$ which might be the biggest model shortcoming originating from the model own formulation. 

Its major impact is that it reweights the gradient estimates of $q(x|\phi)$. Intuitively, how would that compare simply to the iterative strategy of Cbas ?

In a limited and  high dimensional data regimen, the model $p(x|D)$ can be inaccurate or even difficult to fit. It is also dependent on the collection method, for instance in the GFP setting, mutants are observed based on random mutation conducted in wet-labs experiments making it more difficult to interpret.

### Questions
1.Since your algorithm heavily relies on another model ($p(x | D)$), I would be highly interested in better understanding the influence of a good prior on your variational distribution.
2. Regarding the GFP experiments, do you sample already existing sequences ? What is the influence of the relative poor performance of the oracle on ood data on the interpretation of the results  ?
3. How can you explain that only a very simple prior such as a mean field performs on average better ?  It seems quite logical for GFP for instance where a wild type exists, however it is less intuitive for datasets without wild type.

Typo: the recall and precision have the same expression.

### Soundness
4

### Presentation
3

### Contribution
3
