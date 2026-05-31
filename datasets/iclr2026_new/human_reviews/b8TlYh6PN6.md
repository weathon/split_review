## Human Reviewer 1

### Summary
In this paper, the authors propose a characterization of equivalence classes of causal graphs with both latent variables and cycles. To this end, they propose a novel graphical tool of edge ranks (which is dual to path ranks), which makes results cleaner and more intuitive than path ranks do. They further provide a straightforward algorithm to traverse this set of distributionally equivalent causal models.

### Strengths
1. The classification of equivalence classes of causal models with cycles and latent variables is an important topic.
2. Edge ranks seem to be a very useful tool for future results.
3. Despite the complexity of the topic, the paper is clearly written and examples are well-chosen.

### Weaknesses
1. It would be nice to have a little more description of the algorithm in the main paper, especially the decomposition of global rank constraints into local rank queries.
2. It is unclear how this method works when we do not have an OICA oracle, and in particular when we don't know the number of latent variables.

### Questions
1. Your paper currently focuses on minimal DGs, where minimality is measured in terms of numbers of variables. However, one might also be interested in minimally cyclic graphs, at the cost of more latent factors. Is there any way to establish results to determine equivalence classes of such graphs?
2. Your paper currently makes LiNG assumptions. However, low-dimensional bottlenecks should still be noticeable in linear Gaussian, or in nonlinear settings. What prevents us from generalizing the approach to these cases?
3. Given this classification of equivalence classes, is there any hope (and need) for a GES-like algorithm to learn the (equivalence class of) the causal graph? Would this provide any benefit?
4. Would it be possible to explain more about why certain graphs are not equivalent? For example, in the example in section C.2, Figure 5, one could think that the graph $G_1$, but with the edge $X_3 \rightarrow X_1$ removed (equivalently, $G_10$ with the edge $X_3 \rightarrow X_2$ removed) might lie in the same equivalence class. 

As a side note, it appears that your sections D.1-D.3 and their contents are currently struggling a little with formatting.

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper studies a fundamental problem in causal discovery: the distributional equivalence criterian of causal structure from observational data when both latent confounders and cycles are allowed, in linear non-Gaussian models. It provides graphical characterization of equivalence class under arbitrary latent structures and loops via path and edge rank constraints. It also provides graphical transformation rules to traverse within equivalence class. An algorithm glvLiNG is proposed for structure learning from data.

### Strengths
- This work is the first equivalence characterization for causal models with latent variables and cycles, providing the foundation needed for future assumption-free latent causal discovery.
- It introduces the edge rank constraints, a new local graphical tool complementing path-rank constraints.
- It provides clean connection between algebraic rank constraints and graph operations.
- The examples provided in Figure 1-3 are helpful for readers to understand the concepts.

### Weaknesses
See questions.

### Questions
- Do the geometric equivalence results in this paper, such as Lemma 3, 5, 6, generalize beyond LiNG models? It seems they also hold in general models. 
- What is formally the faithfulness assumption in Line 440-441 for the proposed algorithm to work?
- Alhough improving on Lemma 3 from paths to edges, it is still hard to check equivalence via Lemma 5, as one needs to verify for all sets of variables $Z,Y$. The condition is is still not as clean as simply stating something like "same skeleton + v-structures".

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
2

---

## Human Reviewer 3

### Summary
The paper provides a transformational characterization of observationally equivalent latent linear nonGaussian (possibly cyclyc) directed graphical models, including helpful tools (edge ranks, and an interactive equivalence class explorer) along the way, as well as an ICA-based learning algorithm.
I think this is a solid paper considering the foundation it provides for future work and the interesting mathematics it uses, but it perhaps falls short in terms of potential for direct impact, due to its theoretical focus.

### Strengths
- addresses an important open problem
- provides a rigorous, elegant solution
- overall well written, including helpful examples

### Weaknesses
The main weakness is the lack of immediate applicability to real problems. While the paper makes great progress on an extremely challenging problem, it remains unclear to me (and unsupported by the experiments) how useful the current implementation actually is. If the authors could provide a real-data application and show meaningful practical interpretation of the (accurately) learned equivalence class, I would change my mind about this.

### Questions
The main reason I didn't rate the paper higher is because of limited (direct) potential impact. I think this is inline with how the authors present the work in the paper (e.g., presenting the glvLiNG algorithm as a "proof of concept" rather than a practical tool for causal discovery from real data), but nevertheless answers to the following questions could lead me to increase my rating: 
1. Do the authors have any real-data applications in mind, where the learned equivalence classes are sufficiently informative? I'm thinking of how a CPDAG can still be relatively useful in practice, while it's less clear how useful one of these equivalence classes would be.
2. Any ideas for an interpretable representative a given equivalance class (analogous to a CPDAG)?
3. Any ideas for how to refine these to interventional equivalence classes?

The following are suggestions I hope the authors will find useful but that don't require a response and don't affect my rating:
1. Without providing finite sample guarantees, it doesn't really make sense to talk about "identifying" a graph from data---the graph is rather identified from (parameters of) the data-generating distribution. In many but not all instances, the paper correctly uses "recover" (and "estimate" or "learn" would also be appropriate words) for this case, but there are still some places where "identify" is used incorrectly (including L015, L027, L064).
2. L211: "share the same latent variables" seems too strong; can the authors justify the step from the same *number* of latents in the previous sentence to the same latent variables here? or use more precise language here if nothing more is meant.
writing: L238 ("is" -> "are", or "constraints" -> "constraint"), L297 ("to the" -> "in"), L346 ("in edges term" -> "in terms of edge ranks").
3. reference formatting: ensure all words (e.g., 'Bayesian') are capitalized correctly; use the correct characters in Dénes Kőnig's name.
4. Consider adding additional citations, e.g., to work on transformational characterizations for other settings [1], [2], [3], [4], [5], and identifiability in nonparametric latent measurement models (without graphical assumptions beyond acyclicity) [6], [7], [8].
5. Remove the "if not all" part in the second sentence of the abstract. Papers [6], [7], and [8] (and I imagine others) don't make structural assumptions---they just use minimality, which is essentially the author's irreducibility but for identifiability up to nonparametric independence model equivalence rather than up to LiNG distributional equivalence.

[1] Zhang, J., & Spirtes, P. (2005). A transformational characterization of Markov equivalence for directed acyclic graphs with latent variables. In Proceedings of the Twenty-First Conference on Uncertainty in Artificial Intelligence (pp. 667-674).

[2] Chickering, D. M. (1995). A Transformational Characterization of Equivalent Bayesian Network Structures. In UAI (pp. 87-98).

[3] Johnson, J., & Semnani, P. (2025). Characteristic Imsets for Cyclic Linear Causal Models and the Chickering Ideal. arXiv preprint arXiv:2506.13407.

[4] Markham, A., Deligeorgaki, D., Misra, P., & Solus, L. (2022). A transformational characterization of unconditionally equivalent Bayesian Networks. In International Conference on Probabilistic Graphical Models (pp. 109-120). PMLR.

[5] Améndola, C., Boege, T., Hollering, B., & Misra, P. (2025). Structural Identifiability of Graphical Continuous Lyapunov Models. arXiv preprint arXiv:2510.04985.

[6] Markham, A., & Grosse-Wentrup, M. (2020). Measurement dependence inducing latent causal models. In Conference on Uncertainty in Artificial Intelligence (pp. 590-599). PMLR.

[7] Jiang, Y., & Aragam, B. (2023). Learning nonparametric latent causal graphs with unknown interventions. Advances in Neural Information Processing Systems, 36, 60468-60513.

[8] Pearl, J. and Verma, T. (1995). A theory of inferred causation. In Studies in Logic and the Foundations of Mathematics, volume 134, pages 789–811. Elsevier.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper studies characterization and learning of distributional equivalence classes in linear non-Gaussian models with latent confounding and cycles. It first gives a graphical condition under which a latent variable is not reducible and a reduction procedure to the irreducible form. It then relates the rank of submatrices of the mixing matrix $A$ to path rank (a global property that is costly to check) and introduces a local notion, edge rank, proving a duality between the two. Using edge ranks, the paper provides a graphical characterization of equivalence (Theorem 2) and a way to traverse the class. The learning pipeline runs OICA to estimate columns of $A$ up to scaling/permutation and then applies the graphical operations to recover the equivalence class.

### Strengths
- A local graphical notion (edge rank) that makes rank constraints easier to verify.

- A full graphical characterization of distributional equivalence with latent variables and cycles.

- A constructive traversal algorithm for the equivalence class with the admissible moves.

### Weaknesses
- As mentioned by the authors, the learning algorithm relies on solving the OICA problem, which, in general, is hard to solve with existing methods. That being said, the result of characterizing the equivalence class has a theoretical contribution regardless of the learning algorithm.

- The evaluation mostly counts class sizes and compares to a MILP baseline for rank-realization under oracle ranks. There is no empirical test in the finite sample case.

### Questions
- For linear non-Gaussian cyclic models without latent confounding, (Sharifian et al. 2025) characterized the distributional equivalence class and showed it corresponds to perfect matchings in a bipartite graph. It would be valuable to check whether your paper’s equivalence conditions (via edge rank) reduce to theirs in the no-latent case.

- In the acyclic setting with latent confounding, (Salehkaleybar et al. 2020) gave graphical conditions when a model is irreducible. It would be good to clarify that your irreducibility condition matches the one in there in acyclic models.

- Given only a recovered $A$ from OICA, how should we test the coloop condition in Lemma 7? How can we have a robust solution in the finite sample case?

- What is the computational complexity of the two phases in the learning algorithm?

Sharifian, E., Salehkaleybar, S., & Kiyavash, N. (2025). Near-Optimal Experiment Design in Linear Non-Gaussian Cyclic Models. arXiv:2509.21423. 

Salehkaleybar, S., Ghassami, A., Kiyavash, N., & Zhang, K. (2020). Learning Linear Non-Gaussian Causal Models in the Presence of Latent Variables. Journal of Machine Learning Research, 21(39): 1–24.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4