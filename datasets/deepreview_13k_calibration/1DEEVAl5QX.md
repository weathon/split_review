# Mini-batch Submodular Maximization

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
We present the first *mini-batch* algorithm for maximizing a non-negative monotone *decomposable* submodular function, $F=\sum_{i=1}^N f^i$, under a set of constraints. 
We consider two sampling approaches: uniform and weighted. We show that mini-batch with weighted sampling improves over the state of the art sparsifier based approach both in theory and in practice. Surprisingly, we experimentally observe that uniform sampling achieves superior results to weighted sampling. However, it is *impossible* to explain this using worst-case analysis. Our main contribution is using *smoothed analysis* to provide a theoretical foundation for our experimental results. We show that, under *very mild* assumptions, uniform sampling is superior for both the mini-batch and the sparsifier approaches. We empirically verify that these assumptions hold for our datasets. Uniform sampling is simple to implement and has complexity independent of $N$, making it the perfect candidate to tackle massive real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers maximization of decomposable monotone submodular functions over a ground set of size $n$, meaning that the objective function $f$ is a sum of $N$ monotone submodular functions $f_1,...,f_N$. If $N$ is large, then evaluations of $f$ may be computationally demanding. Previous work on the topic (Rafiey & Yoshida, 2022; Kenneth & Krauthgamer 2023) proposes constructing a random sparsified version of $f$ that is a weighted sum of some subset of the functions, and is within a multiplicative $\epsilon$ factor approximation on all sets. A sparsifier such as those mentioned could be constructed as a preprocessing step for an algorithm, and then the algorithm would be run using the sparsifier in place of the original function. The state of the art is that of Kenneth & Krauthgamer, where a sparsifier of $O(k^2n\epsilon^{-2})$ functions is constructed using $O(Nn)$ oracle calls. The sparsifier is constructed by iterating over the functions, computing a probability $p_i$ for each function $f_i$ to be included, and then sampling that function with probability $p_i$ (which takes a total of $O(Nn)$ queries). Then querying the sparsifier takes $O(k^2n\epsilon^{-2})$ function evaluations, compared to $O(N)$ function evaluations to query the original $f$. If $N$ is relatively large, the sparsifier is more efficient.

Instead of computing a sparsifier as a preprocessing step for an algorithm, this paper proposes a "mini-batch method" (which have been used in other areas of ML) for this problem (Algorithm 3). That is, a new sparsifier is sampled every iteration of the greedy algorithm. The approach in this paper uses the same sampling probabilities $p_i$ as Kenneth & Krauthgamer, and therefore still needs the $O(Nn)$ queries as a preprocessing step to compute the $p_i$. In order to prove some of the results in their paper, they make additional assumptions on the problem setting (Models 1 and 2). Several analyses are done on the number of function queries needed for their algorithm. Finally, they include an experimental comparison of their algorithm and related works.

### Strengths
- Exploring submodular optimization algorithms that do not view the function $f$ as simply a black box is an interesting research direction that I think deserves attention.
- They explained their results clearly and the paper was easy to understand.

### Weaknesses
 - It seems a lot of the difficulty of these sparsification approaches is because the sampling of the $f_i$ is non-uniform, but it is still unclear to me that this is so much better than uniform sampling. According to this paper, uniform sampling does better in practice, and requires no preprocessing to compute the $p_i$ since they would be uniform. It is also stated that no theoretical bound can be gotten for uniform sampling. But if we assume that all the $f_i$ are bounded by some value $R$, why can't concentration inequalities be used to get a theoretical guarantee for the uniform approach?
- Some of the results are dependent on assuming Models 1 or 2 (see Table 1), but it isn't clear to me that these models are realistic for applications of the problem.
- Improvements over Kenneth and Krauthgamer mainly include the curvature of the function in the bound on the number of function queries, so the bounds are instance dependent.
- The bounded curvature results (which don't depend on Models 1 and 2) don't use ideas that are that novel compared to related work. It seems the biggest difference from Kenneth and Krauthgamer is computing the sparsifier at each round of the greedy algorithm, and only relatively minor changes are needed to the argument of Kenneth and Krauthgamer.

### Questions
* If the $f_i$ are all bounded by a value $R$, could theoretical guarantees be gotten for uniform sampling?
* Do you expect Models 1 and 2 would hold widely in applications of decomposable functions?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of maximizing a non-negative, monotone, decomposable submodular function under the cardinality constraint and $p$-system constraint. It introduces the first mini-batch algorithm with weighted sampling for this problem, demonstrating that it outperforms the sparsifier-based approach both theoretically and empirically. Additionally, the authors observe that, in experiments, uniform sampling outperforms weighted sampling. To explain this outcome, they define two smoothing models. The first model provides theoretical guarantees for both the mini-batch and sparsifier algorithms on some datasets, while the second model applies only to the mini-batch algorithm but is effective across all datasets tested.

### Strengths
Overall, the paper is well-structured and easy to understand. The definitions and explanations are clear, and related work is discussed in sufficient detail. 

The discussion on uniform and weighted sampling, along with the smoothing model, helps bridge the gap between theoretical results and the empirical performance of the algorithms. It provides insights into why an algorithm without a worst-case guarantee can still perform well in experiments.

### Weaknesses
The algorithm is simple, and the analysis is quite straightforward. The technical contribution is limited. 

With 12 indistinguishable lines in Figure 1, it is hard to see which algorithm with $\beta=10^{-2}$ achieves the best performance.

### Questions
It might be better to put Section 4 before Section 3 to ensure the continuity of the analysis.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies a sampling-based algorithm for faster non-negative monotone *decomposable* submodular maximization subject to
cardinality or $p$-system constraints. In particular, it builds on work of
[Kenneth-Krauthgamer, ICALP 2024] (please update reference in paper), which sparsifies
and reweights the set of functions $f^{(i)}(S)$ for the input function $F(S) = \sum_{i=1}^N f^{(i)}(S)$.
The goal of this paper is to eliminate the dependence on $N$, which the authors do under mild assumptions
via *smoothed analysis*. They also show that this is not possible in the general case with a simple pathological example.
In short, the main idea is to sample a subset of $f^{(i)}(S)$ functions at each step to form a
"mini-batch" for approximating the full $F(S)$. The algorithm then greedily
select the next element based on the sampled funciton (which changes in each iteration), not $F$ itself.

Further, under the mild realistic assumptions, they prove why uniform sampling is a competitive approach,
which helps explain initially surprising experimental observations.
Lastly, this work provides a clean set of experiments comparing their mini-batch sampling-based methods to
a full lazy greedy algorithm and the sparsification idea in [Kenneth-Krauthgamer, ICALP 2024].

### Strengths
- Uses smoothed analysis to more accurately study realistic inputs
- Table 1 cleanyl describes the results, including a comparison with [Kenneth-Krauthgamer, ICALP 2024]
- Draws connections to the lazier-than-lazy greedy algorithm of [Mirzasoleiman et al., AAAI 2015]
  and explains how the two ideas can be combined to reduce query complexity by a factor of $\Theta(k)$
- Good comprehensive set of experiments for cardinality constraints, though the
  values of $k \le 20$ are quite small. It would be nicer to increase $k$ to see
  how fast the different algorithms converge (relatively) to lazy greedy

### Weaknesses
 - The lunch menu optimization example, while a clear illustration, does not
  really motivate the problem from a practioner's perspective
- There are no $p$-system experiments
- It is unclear if ICLR is an appropriate venue for this work. The
  non-exhaustive list of topics in the Call for Papers includes "optimization",
  but submodular maximization in its raw form seems one hop away from the
  target areas of ICLR (deep learning)
- In the introduction, you claim that "in many of the above applications, $N$
  (the number of underlying submodular functions) is extremely large, making the
  evaluation of $F$ prohibitively slow." Are there realistic examples where $N
  \gg 1000$? It's not clear to me how often we really encounter $N$ *distinct*
  personalized submodular functions.
- What exactly is the quantity $A_e$ when you first introduce it on page 3?
  This should be made more clear. Initially, I thought it was a vector of all
  marginal values, but then in model 1 you say it's a random variable.
- For the Uber pickups experiment, why do you use Llyod's algorithm to find
  centers instead of a data-indepedndent grid?

### Questions
- In the introduction, you claim that "in many of the above applications, $N$
  (the number of underlying submodular functions) is extremely large, making the
  evaluation of $F$ prohibitively slow." Are there realistic examples where $N
  \gg 1000$? It's not clear to me how often we really encounter $N$ *distinct*
  personalized submodular functions.
- What exactly is the quantity $A_e$ when you first introduce it on page 3?
  This should be made more clear. Initially, I thought it was a vector of all
  marginal values, but then in model 1 you say it's a random variable.
- For the Uber pickups experiment, why do you use Llyod's algorithm to find
  centers instead of a data-indepedndent grid?

### Soundness
3

### Presentation
3

### Contribution
2
