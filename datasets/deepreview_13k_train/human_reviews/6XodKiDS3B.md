# Permutation Invariant Learning with High-Dimensional Particle Filters

- Decision: Reject
- Scores: 3, 8, 6, 5

## Abstract
Sequential learning in deep models often suffers from challenges such as catastrophic forgetting and loss of plasticity, largely due to the permutation dependence of gradient-based algorithms, where the order of training data impacts the learning outcome. In this work, we introduce a novel permutation-invariant learning framework based on high-dimensional particle filters. We theoretically demonstrate that particle filters are invariant to the sequential ordering of training minibatches or tasks, offering a principled solution to mitigate catastrophic forgetting and loss-of-plasticity. We develop an efficient particle filter for optimizing high-dimensional models, combining the strengths of Bayesian methods with gradient-based optimization. Through extensive experiments on continual supervised and reinforcement learning benchmarks, including SplitMNIST, SplitCIFAR100, and ProcGen, we empirically show that our method consistently improves performance, while reducing variance compared to standard baselines. Project website and code is available 
\href{https://aneeshers.io/PermutationInvariantLearning/}{here}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In sequential learning, the permutation dependency of prevalent optimization algorithms such as gradient descent might suffer from catastrophic overfitting -- severe degradation in performance on earlier tasks -- or loss of plasticity -- limited adaptive capabilities to the new tasks. Nearly permutation-invariant training strategies can address these challenges. This paper proposes particle filters as an instantiation of nearly permutation-invariant training strategies and presents guarantees under some ideal assumption on the quality of the particle filters. To deal with the high-dimensional nature of machine learning papers, a gradient-based particle filter is proposed and evaluated on continual learning and lifelong reinforcement learning.

### Strengths
The paper identifies an interesting perspective based on permutation invariance to tackle two challenges observed in sequential learning. Experimentally, the results seem to correlate with this idea.

### Weaknesses
1. Idealization of the particle filter updates: it is unclear why (6) and (7) hold for suitable constants. I recommend authors to give some examples so that this is more understandable. Specifically, the assumption that the discrepancy between updated particle filter distributions is bounded by a constant times the initial discrepancy requires more justification. The Lipschitz continuity argument is insufficient without specifying the exact form of the update and the metric $D$. Similarly, the error term $\epsilon$ in (7) needs to be explicitly linked to the particle filter's approximation method (e.g., number of particles, specific resampling strategy) and not just stated as an approximation error.

2. The bounds in (8), (9), (12) are all exponential in $T$ and are potentially vacuous. These exponential terms in $T$ are considered as some constants and not discussed at all. I recommend authors to explain why they think these constants are small. As an example, consider Theorem 2 and (12). The loss is upper bounded by $M$ and I don't see why the exponential term is going to be much smaller than $M$ and it seems like (12) is vacuous. The argument that $C$ is close to 1 is not convincing without empirical evidence or theoretical justification for the specific particle filter implementation. Furthermore, even if $C$ is close to 1, the accumulation of errors over $T$ steps can still lead to a significant exponential term, making the bound practically useless for long sequences.

3. It is unclear why the approximate solution in (15) satisfies the Bayesian properties of particle filters. This is stated in L329-331 but no justification isn't given apart from Theorem 3 which is for a very restricted setting. Therefore, I am skeptical that this is any different from N models independently trained with gradient descent. The Gaussian approximation and linearization of the loss function, while common, do not guarantee that the resulting particle filter maintains the correct posterior ratios, especially when the loss function is highly non-linear. The claim that the method differs from independent gradient descent because particle weights are updated based on likelihoods is not sufficient to establish that it is a proper Bayesian approximation.

### Questions
1. Can you explain the notation $\hat{p}[L]$?
2. Can you explain what do you mean in L147? Does the particle filter verify two competing conditions: estimating the full distribution $p_t$ and estimating the global minimizer of $p_t$? If all particles are estimates of the global minimizer, how come they represent the full distribution? 
3. Why do you think it is possible to verify (6) and (7) for particle filters in high-dimensional problems?
4. Can you comment on exponential nature of your bounds in $T$. Aren't they strictly worse that linear bounds in $T$? Any sublinear regret bounds from online optimization seems to be much tighter for the problem setting at hand.

### Soundness
1

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
The authors introduce a novel particle-filter based method for learning in deep neural networks. This method uses a set of particles and updates each particle using a local first-order approximation to the loss, which theoretically grounds both the updates to the particle itself and its weight with respect to the overall set of particles. This method therefore combines the appealing properties of gradient descent with respect to high-dimensional weight spaces with appealing properties of particle filters, in particular their (approximate) permutation independence. They then demonstrate that this method improves performance on a number of continual and lifelong learning benchmarks, in particular when combined with other continual learning methods.

### Strengths
This is an excellent paper. The authors nicely set up the motivation by explaining prevailing challenges in continual learning, clearly explain why particle filters can address this challenge, and then explain their own method. The benchmark experiments nicely demonstrate the strength of their method. Indeed, I believe that this method could inspire a host of follow-up research, further digging into how to combine particle filters and gradient descent-based optimization. I therefore strongly recommend acceptance.

Below are a few parts of papers I appreciated in particular:
- The introduction really clearly sets up the lens of permutation invariance, which provides a great motivation for particle filters.
- Section 3 provides a set of mathematical insights that make this intuition rigorous.
- The introduced algorithm is theoretically principled and I really appreciated that the authors were able to explain it so succinctly in the main text.
- I thought the authors' finding that this method can be combined with a range of other continual learning methods was really insightful and moved beyond a mere benchmark comparison.

### Weaknesses
I have two primary concerns I'd like to see the authors address:

**1 Further related work**

Your method seems related to the use of ensembles for continual learning, e.g. [1-3]. Could you discuss the relation of your paper to this prior work?

**2 Connection between sections 3.2-3.3 and 3.4**

In sections 3.2 and 3.3 you provided a set of guarantees about particle filters under assumptions (6) and (7). You then introduce your own method, but don't explain whether this method meets these assumptions. Could you discuss whether your method meets these assumptions and if so, what these constants are for your method? If it is unknown whether your method meets these assumption, could you make that clear?

### Questions
See weaknesses.pure 

Further questions/suggestions:
- It seems that you're providing an initial connection between particle filters and gradient descent which seems to provides a lot of potential for future work in extending these methods, e.g. with adaptive gradients. You note the potential for such future work in the last sentence, but I'm curious if you have any directions for future work that you are particularly excited about?
- L. 256: Under linear approximation, yes, but in practice, this equality is approximate, right? So when defining $w_{t+1}^{(i)}$, do you use the approximation or the exact quantity for $L_{t+1}(x_{t+1}^{(i)})$?
- A minor point: I think formatting table 1 to clearly delineate continual learning baselines versus continual learning baselines + particle filters (e.g. by using two different columns for the baseline alone versus the baseline + PF) would make it easier for the reader to compare them both to each other and to the Particle Methods above.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper "Permutation Invariant Learning with High-Dimensional Particle Filters" proposes a particle-filtering inspired continual learning system. A bound is dericed to show that the method is approximately permutation invariant, and a connection to the avoidance of catastrophic forgetting is established. Under the assumpation of Gaussian probability masses around the particles, a gradient-based update is derived. Empirically the method is shown to perform very competitive on two continual learning supervised datasets (SplitMNIST and SplitCIFAR100), and in one reinforcement learnign setting (ProcGen).

### Strengths
+ the method outperforms, or performs very well against the baselines. In addition, it is shown that method is complementary, and when combined with other methods, can improve their performance.
+ the idea of the paper can be followed well (though due to the complexity of the problem some central derivations are in the appendix)
+ moving towards more real-world problems, the topic of continual learning is an important one to tackle for the community

### Weaknesses
 - The document should contain a section on Limitations. One thing that should be mentioned is that the algorithm needs N times more memory to keep the model parameters (or compute) for N being the particles, than a simple standard method with N=1. In particular, given that the community moved to very large models, this is a potentially very big limitation. If you made any design choices to overcome this limitation this should be discussed (or metnioned as future work).
- the writing could be made more accessible. Overall the authors do a good job in explicating the ideas. However, the paper would profit from some high-level summaries and previews before more complex topics. For example, I'd recommend adding a summary description of the derivation in section 3.4 (Gaussian approximation of the particles and Taylor approximation + simplification of terms) before actually doing it. It should also be discussed that the algorithm is independently operating on all i (?) - the only coupling is in the ensembling with the weights. This is important for parallelization, which should be discussed. 
- In the abstract, it should be mentioend that the permutation invariance is approximate and not exact. E.g. change the text 'we introduce a novel permutation-invariant ...' to 'we introduce a novel approximately permutation-invariant ...'.
- In Table 1 please make the best performing nubmers bold

### Questions
- as the particle filter 'replicates' the model N times - how would a system of N times the size perform (potentially with other regularizations)? There are many architectures to make such a system efficient as well (e.g. Mixture of Expert ...). An experiment analyzing the performance as a function of model size (could be for N=1, but should be compared to the method proposed) should be added to clarify this.

### Soundness
3

### Presentation
2

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
This paper discusses a particle filter scheme (named as WPF) which tentatively provide a solution of continual tasks learning given high-dimensional parametrized models. WPF method reweighs each particle samples by manipulating the posterior distribution of parameters with gradient of task losses which are computed in a sequential order. Authors justify that WPF methods is permutation-invariant, can prevent notorious forgetting behavior and can prevent "loss of plasticity". There are some experiments conducted over SplitMNIST, SplitCIFAT1100 and ProcGen to show that: i) WPF can be a replacement of vanilla gradient-based optimizer and it can combine with loss regularization techniques (SI, LWF, EWC in this paper) to show performance improvement under both CL and LRL environments ii)  WPF effectively reduces the variance under both CL and LRL environments;

### Strengths
The idea to apply particle filter technique is not particularly novel. However, the efficient realization in a high-dimensional parameter space and show its improvement in continual learning setup is a solid contribution. The author conduct extensive experiments to quantitatively justify the claim.

### Weaknesses
The major disappointment is the inconsistency between what authors attempt to justify in theory and what practical experiments reflect. Frist of all, the notation setup in Section 3.1 is leading confusion. In Equation (2)(3), a better statement of the posterior distribution is to define $p_t$ under conventional setup: $p_t(x):= p(x_t|L_{1:t})$, and it will improve the readability. While defining the distribution with sequential observation of loss using $\hat{p}_0[L_1,L_2,\ldots,L_T]$ is valid, the sudden show up of $\hat{p}[L]$ in line 158 is not properly defined. Adding some notation explanations would be appreciated.

Secondly, I personally did not view permutation invariance as a contribution bulletin. Theorem 1 (line 177-182) justify that a distance metric $D$ is bounded by some constant (including $N,\epsilon,T,C$), and these constants do not have any constraints to indicate if the distance metric converges. Throughout the paper authors fail to give one example of a practical formula of metric $D$. Moreover, the author then justify in line 182-183 that Equation (9) implies particle filters are "**approximately** permutation invariant", without any further qualitative analysis. I am expected to see if there are some experiments to justify/support Theorem 1 , but the only statement in line 510-525 is the performance improvement of reweighted particles which convey readers that "variance reduction implies permutation invariant". Please justify why permutation invariant can be verified by computing variance of repetitive experiments. I understand that WPF is capable of achieving better performance and lower variance under 10 different permutations runs, but this has nothing to do with the statement in Theorem 1.

To strengthen the claim, there are two potential improvements. One way is to show that variance-reduced gradient descent scheme (rather than using a fixed-step gradient descent scheme as per baseline), fail to achieve better overall performance over many runs of permutations. One classical variance-reduced gradient descent scheme is  [SVRG](https://papers.nips.cc/paper_files/paper/2013/hash/ac1dd209cbcc5e5d1c6e28598e8cbbe8-Abstract.html). Another way is to assign a computable metric (e.g. Wasserstein distance) and quantitatively validate theorem 1.

Besides, even though I assume all proof is correct, the author fails to bring attention in experiments to see which part of the result reflect that theorem 2 is correct, which is an upper bound of loss. All reported numbers are mean performance by weighted average of model parameters, and its variance accordingly. Moreover, two assumptions stated in theorem 2 is not validated in experiments as well.

Lastly, an equivalent statement of author's implementation, after reading algorithm 1, is: "WPF repeat gradient descent $N$ times, where $N$ is the number of particles, and reweigh each particles by an exponential term along the path." Then, I am expected to see authors justify why this is not considered as an Mixture-of-Expert(MoE) scheme, and authors ignored the existence of MoEs at all. It would be better if, at least, discuss or compare MoE schemes under this continual learning setups.

This paper has some presentation flaws of experimental details as well, please refer to questions for details.

### Questions
Apart from aforementioned concerns, there are some specific questions that I wish to hear from authors.

Major doubts:
*    For all conducted experiments, are there any numbers regarding dimension of particles can be reported?
*    Though WPF can be combined seamlessly with other schemes, what is the additional computation cost introduced by flowing multiple particles? From my understanding, the cost increases linearly with number of particles. Any specific runtime comparisons between WPF and baseline methods, as well as how the runtime scales with the number of particles?
*    In Theorem 3, linear loss function is assumed. However, in classification task setup (e.g. SplitMNIST,SplitCIFAR100), I presume the loss is the CrossEntropy loss, am I right? If sequential losses are CrossEntropy losses, then follow-up questions pops up: how to justify probability density matches in this case?  How Theorem 3 relates to the experimental setup with non-linear loss functions?
*    If in Algorithm $1$, we set number of particles $N=1$, is it equivalent to a fixed step size gradient-descent? If so, in experiments, is the benchmark GD implemented with fixed step size? 
*    Following up the previous question, what is the  hyperparameter $\sigma$'s role in controlling the WPF's performance. I didn't find the hyperparameter setup $\sigma$ in Section 4. Please specifiy the number used in experiments and if possible, justify the choice of such numbers.

Minor questions/suggestions:
*    In line 117, what does $L_t\in \mathbb{R}^d\rightarrow \mathbb{R}$ mean? If $L_t$ is a loss function, then please cosider revise the notation.
*    Is BC listed in Table 2 abbreviation of "Behavior Cloning"?
*    Considering adding statement in Figure 3 to indicate the uncertainty band is under one-times standard deviation, two-times standard deviations or three-times standard deviations. Two blue lines is not a good idea either.
*    Line 461, please consider avoid using colloquial statement like "interestingly".

### Soundness
2

### Presentation
2

### Contribution
2
