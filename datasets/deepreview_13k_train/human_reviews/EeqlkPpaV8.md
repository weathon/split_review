# The adaptive complexity of log-concave sampling

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
In large-data applications, such as the inference process of diffusion models, it is desirable to design sampling algorithms with a high degree of parallelization. In this work, we study the adaptive complexity of sampling, which is the minimal number of sequential rounds required to achieve sampling given polynomially many queries executed in parallel at each round. For unconstrained sampling, we examine distributions that are log-smooth or log-Lipschitz and log strongly or non-strongly concave. 
We show that an almost linear iteration algorithm cannot return a sample with a specific exponentially small accuracy under total variation distance.
For box-constrained sampling, we show that an almost linear iteration algorithm cannot return a sample with sup-polynomially small accuracy under total variation distance for log-concave distributions.
Our proof relies upon novel analysis with the characterization of the output for the hardness potentials based on the chain-like structure with random partition and classical smoothing techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides lower bounds for the problem of adaptive sampling from a distribution over $\mathbb{R}^d$ with probability density functions proportional to $exp(-f)$ for some smooth, Lipschitz or convex function $f:\mathbb{R}^d\rightarrow\mathbb{R}$. The algorithm can have access to a 0-th order oracle (i.e can query the values of $f$) that can also be translated to gradient queries with a polynomial blowup in the number of queries. Before making each query, the algorithm can also see the replies of the oracle to the previous queries. The lower bounds are also extended to box-constrained sampling. In the latter, the total variation distance between the true and the sampled distribution (sampling accuracy) is inverse polynomial in the dimension, while in the former case, it is inverse exponential. The lower bounds are linear on the dimension $d$ up to logarithmic factors, while the best known upper bounds are higher degree polynomial depending on the function $f$.

### Strengths
First attempt for a lower bound on adaptive sampling applicable to a wide range of distributions.

### Weaknesses
The paper only has negative results (lower bounds), which are not tight for any parameter regime. 
The writeup could also be improved in terms of typos/grammar as well as clarity of the presentation (especially in section 3).



Minor comments:
Line 15: “minimal”->”minimum”
Line 21 and 100: “sup-”->”sub-”
Line 21: “small accuracy” sounds weird (because it means “high accuracy” here). Maybe “small error” would be better. 
Line 85: Mention that c<1. 
Section 3: There are multiple occasions where you are correctly describing a reduction FROM hypothesis testing TO sampling, which is indeed the way to translate a hypothesis testing lower bound to a samling lower bound. However, you incorrectly claim the reduction is the other way around, which is a bit confusing. (e.g see Lines 225-226, 235,269,274).  

Line 267: “total variance”->”total variation”

### Questions
Can you comment on the possibility to close the gap between upper and lower bounds in some parameter regime?

### Soundness
2

### Presentation
2

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
This paper studies the problem of parallel sampling, and shows a lower bound of $\widetilde O(d)$ for the number of parallel iterations necessary in the "high-accuracy" regime for log-concave sampling. The paper also shows a similar result for the box-constrained setting. To achieve these lower bounds, the paper leverages techniques from the optimization literature that have been used to show lower bounds for adaptive algorithms for optimization. The paper also studies some other sampling regimes such as composite sampling, showing similar bounds.

### Strengths
This paper studies an interesting problem, and shows how to leverage techniques from a different but related area to show lower bounds for parallel sampling. The lower bounds are of interest to both theoreticians and practitioners, since parallel sampling methods for diffusion models have recently been proposed and have gained popularity.

Generally, the paper is well-written and easy to understand. I recommend acceptance

### Weaknesses
It would be nice to see some results for diffusion models, since it seems like they should naturally follow from your results. It would also be nice to cite the recent works from the diffusion literature on parallel sampling (see [1, 2, 3]). This would make this work far more appealing to practitioners.

It would also be nice to have a thorough description of the barriers in extending your techniques to the low-accuracy regime, and any specific intermediate conjectures towards proving such results.

### Questions
1) Can your results be extended to diffusion models in a direct way?
2) What can you say about the low-accuracy regime?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper shows lower bounds for a number of different log-concave sampling problems.  Specifically, they show a lower bound of $\tilde{\Omega}(d)$ objective function evaluations for the problem of sampling from a unconstrained distribution.  They also show a lower bound of $\\tilde{\Omega}(d)$ objective function evaluations for the problem of sampling from a “box-constrained” logconcave distribution constrained to the unit cube.  In addition to applying to any unconstrained or box-constrained distribution, their lower bounds also handle the special cases when the log-density is smooth and Lipschitz.  However, they do not obtain lower bounds for the special case where the log-density is strongly convex.

### Strengths
The paper improves over previous works which show lower bounds for the problem of sampling from a logconcave distribution.  

The comparison to previous works for upper bounds is very clearly stated.   However, the comparison to previous works on lower bounds is less clear, as there are different situations where such lower bounds apply (e.g., different accuracy levels) (see weaknesses below)

### Weaknesses
The writing in the paper could be improved in certain aspects.  In particular, the comparison to prior works is somewhat confusing and could be made more clear.

As mentioned above, the comparison to previous works for upper bounds is very clearly stated, with a clear table—which is good.      However, the comparison to previous works on lower bounds is less clear, as there are different situations where such lower bounds apply (e.g., different accuracy levels).  It would be good to include a side-by-side comparison with previous works on lower bounds, perhaps as an additional table in the appendix if there is not enough room in the main body of the paper.

Additionally, it would be helpful to have a more intuitive discussion of the difference between adaptive complexity vs. query complexity.  I am more familiar with query complexity, but adaptive complexity seems to be a less common term and it would be good to highlight the differences between the two concepts, and to explain with respect to which concepts the authors improve on previous lower bounds.

### Questions
Could the authors clarify in what settings/regimes they improve over lower bounds from prior works?   Under what assumptions on the objective function, and for what required accuracy levels were the improvements, and by how much was the improvement? In what regimes were lower bounds previously available/not available?  In what settings were they available, but improved by the authors?  In what regimes were they not improved?

Also, I understand that the authors results apply both to zeroth-order oracle and first-order oracles, which is good. However, do they improve on previous lower bounds for first-order oracles, or is the improvement only for zeroth-order oracles?

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
This paper studies the round complexity of sampling from log-concave distributions $\propto e^{-f}$ in $\mathbb{R}^d$ given (zeroeth order) query access to $f$. For unconstrained sampling from strongly log-concave and log-smooth densities, the present work shows that achieving target accuracy which is exponentially small in $d$ requires $\tilde{\Omega}(d)$ many rounds. They also extend the lower bound in this paper to give an $\tilde{\Omega}(d)$ lower bound for box-constrained sampling of log-concave and log-smooth/Lipschitz densities to inverse super-polynomial error. These lower bounds are within a polynomial of the right answer, e.g. in the unconstrained setting Anari et al. previously gave a parallel algorithm with round complexity $O(\log^2(d/\epsilon))$, which is $O(d^2)$ for exponentially small $\epsilon$. While the query complexity of log-concave sampling has been studied previously for low-dimensional distributions and for sampling Gaussians to constant accuracy, this paper appears to be the first to study the orthogonal question of getting lower bounds in the high-accuracy regime.

At a high level, the lower bound is based on constructing a certain potential $f$ which is a smoothing of a certain function which, for bounded-norm inputs, behaves like the following piecewise linear function. It is parametrized by an unknown partition of the coordinates into blocks of polylogarithmic size, and given an input $\mathbf{x}$, the function adds to the weight of $\mathbf{x}$ on the first set in the partition the following sum. It computes the imbalance between the weight of $\mathbf{x}$ for each consecutive pair of consecutive sets in the partition and, if the imbalance exceeds some threshold $t$ for that pair, it adds to the running sum how much that imbalance exceeds $t$. So for inputs on which the weights of $\mathbf{x}$ over the sets in the partition are roughly equal, this potential outputs something close to the weight of $\mathbf{x}$ on just the first set of the partition. 

This potential is designed in such a way that in the first $\tau$ rounds of any parallel algorithm, if one thinks of the subsets in the partition as randomly chosen in sequence, then with high probability over the randomness of the subsequent subsets of the partition, the queries up to that point reveal no information about what the subsequent subsets are. This effectively forces the algorithm to run for $\tilde{\Omega}(d)$ rounds before it can query parts of space on which the potential is non-negligibly different from the weight of $\mathbf{x}$ on the first subset of the partition.

### Strengths
Deriving good lower bounds on query complexity is a central question in the area of log-concave sampling, and this paper makes solid progress towards understanding the optimal parallel query complexity in a natural setting, namely the high-accuracy regime. The lower bound construction is a nice blend between the techniques used to show adaptive complexity bounds in submodular optimization and the information-theoretic approach used in prior work of Chewi et al on query lower bounds for sampling. Additionally, it is interesting that they can derive a linear-in-$d$ lower bound even in the relatively low-accuracy regime in the box-constrained setting.

### Weaknesses
While these results are only relevant in the setting where the dimension $d$ is quite large, it is not clear that the lower bounds really get at the fundamental question of why there should be a dimension dependence in the query complexity of log-concave sampling. In particular, the fact that the authors get a near-linear lower bound for the unconstrained sampling setting feels more like a by-product of the fact that they are working in the high-accuracy regime than of the fact that the distribution lives in high dimensions (in particular, their lower bound could be consistent with a world in which the true round complexity is $\tilde{\Theta}(\log(1/\epsilon))$). Admittedly the near-linear lower bound in the box-constrained setting applies in the regime of only $1/d^{\omega(1)}$ error, but the argument seems almost verbatim the same as the argument in the unconstrained setting, suggesting that the fact they get such a lower bound in the relatively low error regime is more a quirk of the constrained setting than something fundamental about dimension dependence for log-concave sampling.

The writing could be clarified in various places, e.g:
- In Lemma 4.3, the terminology "up to addictive error $O(t/2)$" it is only clarified later in the proof to mean that every *coordinate* is off by at most $O(t/2)$ (also why is there a big-O with a factor of 1/2?)
- The definition of $X_i(\mathbf{x}')$ seems off, as the subscript $i$ is then used to index over $i\in[\ell]$ in $\cup_{i\in[\ell]} P_i$
- The terminology "concentration of conditioned Bernoullis" is a little confusing as it is unclear what is being conditioned on. A more standard phrasing could be "concentration of linear functions over the Boolean slice
- When "partition $\mathcal{P} = (P_1,\ldots,P_{r+1})$ over the ground set" was introduced, it was not clear to me that the ground set was referring to the set of coordinates of the Euclidean space in which the target distribution lives

### Questions
The writing could be clarified in various places, e.g:
- In Lemma 4.3, the terminology "up to addictive error $O(t/2)$" it is only clarified later in the proof to mean that every *coordinate* is off by at most $O(t/2)$ (also why is there a big-O with a factor of 1/2?)
- The definition of $X_i(\mathbf{x}')$ seems off, as the subscript $i$ is then used to index over $i\in[\ell]$ in $\cup_{i\in[\ell]} P_i$
- The terminology "concentration of conditioned Bernoullis" is a little confusing as it is unclear what is being conditioned on. A more standard phrasing could be "concentration of linear functions over the Boolean slice
- When "partition $\mathcal{P} = (P_1,\ldots,P_{r+1})$ over the ground set" was introduced, it was not clear to me that the ground set was referring to the set of coordinates of the Euclidean space in which the target distribution lives

### Soundness
3

### Presentation
2

### Contribution
2
