# Approximation algorithms for combinatorial optimization with predictions

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
\noindent
We initiate a systematic study of utilizing predictions to improve over approximation guarantees of classic algorithms, without increasing the running time.
We propose a systematic method for a wide class of optimization problems that ask to select a feasible subset of input items of minimal (or maximal) total weight.
This gives simple (near-)linear time algorithms for, e.g., Vertex Cover, Steiner Tree, Min-Weight Perfect Matching, Knapsack, and Clique.
Our algorithms produce optimal solutions when provided with perfect predictions and their approximation ratios smoothly degrade with increasing prediction error.
With small enough prediction error we achieve approximation guarantees that are beyond reach without predictions in the given time bounds, as exemplified by the NP-hardness and APX-hardness of many of the above problems.
Although we show our approach to be optimal for this class of problems as a whole, there is a potential for exploiting specific structural properties of individual problems to obtain improved bounds; we demonstrate this on the Steiner Tree problem.
We conclude with an empirical evaluation of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work falls under the he newly evolving area of learning-augmented algorithms.  Consider an optimization problem of the form:  There are $n$ items with weights $w_1, w_2, \cdost w_n$. Given a (implicit) collection of subsets of $[n]$ find a subset whose weight is minimized/maximized. Suppose that we are given a prediction $\cap{X}$ for the optimal solution. Can the algorithm exploit this additional data and design algorithms with better approximation ratio?

This work studies the above question and proves that depending on how close $\cap{X}$ is to the optimal solution (closeness measured in terms of false positives and false negatives), we can obtain algorithms with improved approximation ratio.

### Strengths
1. The problem studied is very interesting, natural, and timely
2. The solution presented is very intuitive and the proofs are easy to follow (this should be taken as negative).
3. For the general setting, the bounds obtained are optimal.

### Weaknesses
1. The paper is a bit too verbose with many unnecessary details.   For example, detailed discussed of example applications in sections 2.1 and 3.1 is not needed, as these problems fit into the framework in a straightforward manner.

2. I do not know much about the learning-augmented algorithms. So, I am not able evaluate the novelty of the proofs of the present work (this perhaps is the reviewer's weakness, not the paper's weakness). However, a more detailed description of various other models to represent predictions and the algorithmic techniques places this work in context.

### Questions
1. What if predictions come in the form of probabilities/confidences? For each item  $i$, a confidence value $\alpha_i$, representing the confidence that item $i$ is in the optimal solution set.  How does this model compare to the current work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper provides a generic transformation of worst-case approximation algorithms to approximation equipped with machine learnt advice. The general setting is that of positively weighted selection problems that are subject to combinatorial constraints (e.g., vertex cover, Steiner tree, weighted machine, knapsack, etc). The main result is that given a nearly correct (yet perhaps unfeasible) solution to the optimization problem, one can derive an approximation guarantee close to 1, using as a black box any approximation algorithm for the problem (in particular, a very efficient one). The idea is very simple. For minimization problems, replace the weights of the elements in the advised solution by 0, then run the approximation algorithm on the modified instance. An analogous solution works for maximization problems.

They also show that under the unique games conjecture, the result is optimal for some problems (e.g., vertex cover). For Steiner tree, they give a better algorithm that is a slight variation of the above general method: instead of zeroing the weight of the advised elements, damp the weights by some factor.

Finally, they provide some empirical evaluation of their methods, on a known benchmark. It's hard to judge the meaning, because it's not clear that this benchmark was design to challenge machine learning approaches, so possibly it is easy to learn and thus overfit the above approach to the dataset (which is quite small; 199 examples).

### Strengths
I like the generality of the approach, and its simplicity makes it practically appealing.

### Weaknesses
It's restricted to selection problems, so, for instance irrelevant to partition problems such as clustering. Also, it requires an approximation algorithm for the weighted case, even if the optimization problem that needs to be solved is unweighted. By exploring the combinatorial structure of the problem, one might derive better solutions (as demonstrated for Steiner tree). The reliance on a 'nearly correct' solution, while practically motivated, introduces a dependency on the quality of the advice which is not fully explored. The paper does not discuss the sensitivity of the final approximation ratio to the error in the advised solution. Furthermore, the empirical evaluation, while present, is limited by the small size of the dataset and the lack of a clear rationale for the benchmark's suitability for evaluating machine learning-guided algorithms. This raises concerns about the generalizability of the empirical findings.

### Questions
None.

### Soundness
4

### Presentation
4

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
The paper explores learning-augmented approximation algorithm design for a general selection problem. In this problem, we are given a set of ground elements, each with a non-negative weight, along with an implicit collection of all feasible subsets of these elements. The objective is to select a feasible subset that minimizes or maximizes the total weight.

The authors focus on the setting where the algorithm can access an (imperfect) prediction of an optimal solution and propose a general framework for integrating classic approximation algorithms with this prediction. For the minimization model, the framework achieves an approximation ratio of $1+(\eta^+ + (\rho-1)\eta^-)/ OPT$, where $(\eta^+,\eta^-)$ are prediction errors, $\rho$ is the classic approximation and $OPT$ is the optimal objective value.  For maximization problems, the framework yields an approximation ratio of $ 1- ((\rho-1)\eta^++\eta^- )/OPT$. The authors apply this framework to several concrete applications. In particular, for the Steiner tree problem, they leverage the characteristics of the problem to provide an improved ratio.

### Strengths
- Learning-augmented algorithmic design was originally applied in online optimization to leverage learning in order to address uncertainty. This paper extends this approach to offline approximation algorithm design, aiming to break through computational complexity—an interesting idea.

- The paper is well-organized. The basic idea is clean and easy to follow.

### Weaknesses
 - Although the model is novel, the proposed learning-augmented framework seems quite natural, and the analysis is technically simple. One shortcoming of the framework is that when the given prediction is the whole element set, $\eta^- =0 $, while $\eta^+$ can become infinitely large, leading to an infinite approximation (if the robust operation in the corollary is not used). This is a little weird. Could this be fixed by adding a step in the framework to apply classic approximation algorithms to the predicted subset of elements if it is infeasible?

### Questions
- See the weakness above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper is about learning-augmented approximation algorithms for combinatorial set selection problems. More specifically, the authors consider the (abstract) problem of selecting a set of elements of a universe of minimum total weight such that the selected set is feasible. A classic example of such a problem is the Vertex Cover problem. An approximation algorithm runs in polynomial time and computes a solution that is within an $\alpha$ factor of an optimal objective value. This factor is called the approximation factor of the algorithm. Typical applications for approximation algorithms are optimization problems that are NP-hard to solve optimally.
Moreover, for some problems such as Vertex Cover, finding a better-than-2 approximation algorithm would contradict standard complexity assumptions such as the Unique Games Conjecture or $P \neq NP$.

Learning-augmented algorithms are a recently popular method of beyond worst-case analysis, and are nowadays an established subfield in the intersection of algorithm theory and machine learning. The idea is to give an algorithm access to an additional input - a prediction - and analyze a learning-augmented algorithms performance w.r.t. the quality of this prediction. Only a few works have considered approximation algorithms under this framework so far.

The present paper considers the prediction model where a predicted solution is given to the algorithm. They present algorithms for the general set selection problem that achieve a near optimal performance for perfect predictions and a smooth degradation w.r.t. the number of false positive and false negatives of the prediction compared to some optimal solution.
At the same time, the approximation ratio of the currently best-known approximation algorithm can be achieved by running both algorithms and selecting the better solution.

Further results include:
- A similar result for maximization problems
- An algorithm with a controlable tradeoff between consistency and smoothness
- Lower bounds w.r.t. the Unique Games Conjecture showing that their algorithms are essentially best-possible.
- Empirical experiments

### Strengths
- The paper provides learning-augmented algorithms for various problems as well as general tight lower bounds on these results. The approximation guarantees in the case of good predictions improve over complexity lower bounds in the setting without predictions. 
- There are only few papers on approximation algorithms with predictions. Thus, I have the feeling that its simplicity and strong results have an impact, and these results may be important for future works.
- The proposed algorithms are simple yet essentially best-possible.
- The paper is very well written, gives a structured overview of related work, and provides some empirical insights.

### Weaknesses
 - One minor weakness is that the results are achieved using quite simple standard techniques. However, given that the analysis is essentially tight, and this is an AI conference and not a TCS conference, I think this is really only a minor issue.
- Compared to online algorithms with predictions, one can guarantee robustness for approximation algorithms for free by running both algorithms in parallel. Thus, there are no interesting insights between consistency and robustness for approximation algorithms. However, the authors show that similar trade-off are present between consistency and smoothness, give paramterized results and moreover discuss how to choose such parameters. Thus, I think that this is also only a minor weakness.
- I would have liked a concluding discussion about the impact of these results and a potential outlook at future questions at the end of the paper. This could be addressed in a camera-ready version though.
- In the "results" paragraph of the empirical evaluation, I was missing your takes on how your algorithm compares to CIMAT, given that it is part of your experiments. In general, I would have liked to see a larger discussion here. This could be also easily addressed in a revised version.
- L128: Can we conclude from this example that the linear depedence $(\rho - 1) \eta^-$ is necessary? As far as I understand, this example only gives lower bounds on the endpoints of the error functions, so in principle one could have a non-linear dependence.


Further comments on the writeup:
- L81: I think it would improve the readability if you explain before that the idea is to predict a solution (= some set).
- L114: Here I was wondering what happens if there are multiple optimal solutions. Maybe you can add some note here. Later in the theorem, you solved it differently.
- L317: "In other words, using the terminology of" sounds a bit redundant.
- L327: I think it must be $X \subseteq V$, because in a graph where all edges are self-loops, we have $X = V$.
- L361: "this problem is not known to be NP-hard" sounds a bit confusing given that it is known to be in $P$.
- L479: "it scales the weight [...] by parameter $\alpha$" Here I was unsure what this means, i.e., if it is $w/\alpha$ or $w \cdot \alpha$. Of course, it is precise in the algorithm.
- L525: "since the Mehlhorn's algorithm is". I think it is "since Mehlhorn's algorithm is".
- L1000: I would have like a bit more details why Theorem 8 implies that Theorem 1 cannot be improved.

### Questions
Questions:
- L128: Can we conclude from this example that the linear depedence $(\rho - 1) \eta^-$ is necessary? As far as I understand, this example only gives lower bounds on the endpoints of the error functions, so in principle one could have a non-linear dependence.



Further comments on the writeup:
- L81: I think it would improve the readability if you explain before that the idea is to predict a solution (= some set).
- L114: Here I was wondering what happens if there are multiple optimal solutions. Maybe you can add some note here. Later in the theorem, you solved it differently.
- L317: "In other words, using the terminology of" sounds a bit redundant.
- L327: I think it must be $X \subseteq V$, because in a graph where all edges are self-loops, we have $X = V$.
- L361: "this problem is not known to be NP-hard" sounds a bit confusing given that it is known to be in $P$.
- L479: "it scales the weight [...] by parameter $\alpha$" Here I was unsure what this means, i.e., if it is $w/\alpha$ or $w \cdot \alpha$. Of course, it is precise in the algorithm.
- L525: "since the Mehlhorn's algorithm is". I think it is "since Mehlhorn's algorithm is".
- L1000: I would have like a bit more details why Theorem 8 implies that Theorem 1 cannot be improved.

### Soundness
3

### Presentation
4

### Contribution
3
