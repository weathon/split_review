# Regret-Optimal List Replicable Bandit Learning: Matching Upper and Lower Bounds

- Decision: Accept
- Scores: 3, 6, 8, 8

## Abstract
This paper investigates *list replicability* [Dixon et al., 2023] in the context of multi-armed (also linear) bandits (MAB). We define an algorithm $A$ for MAB to be $(\ell,\delta)$-list replicable if with probability at least $1-\delta$, $A$ has at most $\ell$ traces in independent executions even with different random bits, where a trace means sequence of arms played during an execution. For $k$-armed bandits, although the total number of traces can be $\Omega(k^T)$ for a time horizon $T$, we present several surprising upper bounds that either independent of or logarithmic of $T$: (1) a $(2^{k},\delta)$-list replicable algorithm with near-optimal regret, $\widetilde{O}({\sqrt{kT}})$, (2) a $(O(k/\delta),\delta)$-list replicable algorithm with regret $\widetilde{O}\left(\frac{k}{\delta}\sqrt{kT}\right)$, (3) a $((k+1)^{B-1}, \delta)$-list replicable algorithm with regret $\widetilde{O}(k^{\frac{3}{2}}T^{{\frac{1}{2}}+2^{-(B+1)}})$ for any integer $B>1$. On the other hand, for the sublinear regret regime, we establish a matching lowerbound on the list complexity (parameter $\ell$). We prove that there is no $(k-1,\delta)$-list replicable algorithm with $o(T)$-regret. This is optimal in list complexity in the sub-linear regret regime as there is a $(k, 0)$-list replicable algorithm with $O(T^{2/3})$-regret.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies list replicability in multi-armed bandits (MAB), defining an algorithm as list replicable if it limits the distinct arm sequences (traces) across independent executions with high probability. Further, this paper proposes three algorithms with different parameters of list replicability. Finally, this paper investigates a lower bound of bandits with list replicability.

**---After rebuttal---**

My primary concern pertains to the main claims of the paper, as highlighted in the title: "Regret-Optimal" and "Matching Upper and Lower Bounds." Following a detailed discussion with the authors, I have observed that the paper fails to provide any lower bound in terms of regret for their setting, even in Section 6. Consequently, the claims of "Regret-Optimal" and "Matching Upper and Lower Bounds" appear highly questionable.

In their latest response, the authors stated that their claim of "regret-optimality" is based on achieving a $\tilde{O}(\sqrt{T})$ regret. However, to the best of my knowledge in the field of bandits, it is not standard practice to assert optimality of regret solely with respect to the parameter $T$, while disregarding other critical parameters (e.g., $K$). Given this significant issue of overclaim, I am unable to recommend this paper for acceptance.

### Strengths
1. The problem setting proposed is both novel and intriguing, characterized by a rigorously defined concept of bandit replicability in Definition 2.2.
2. The theoretical analysis provided is exhaustive, introducing three distinct algorithms tailored to various parameters of replicability.

### Weaknesses
1. Algorithms 1 and 2 exhibit considerable similarities. Could there be a method to consolidate these two algorithms into a unified framework?

2. In Theorem 6.1, the designation "lower bound" appears misapplied as it does not seem to correspond to the lower bounds of any algorithms discussed previously. Notably, in Theorem 6.1 we have $l \approx k$, whereas in prior algorithms $l \gg k$ in most cases. In my humble opinion, a valid lower bound should be able to explain whether the proposed algorithms can be further optimized in general.
Furthermore, why the authors said "We show that result (3) is nearly tight for B=2" in the abstract. What's the hidden constant behind $\Omega(B) $ in (3). Do you mean the regret of (3) is $O(T)$ for $B=2$?

3. Would it be more accurate to describe what is currently referred to as "lower bounds" in Theorem 6.1 as "impossibility results"? I think Theorem 6.1 is quite trivial because any pair of traces should share more than two arms if the total number of traces is less than $K$.

4. The absence of experimental validation in this paper is notable. Including even preliminary numerical simulations or toy experiments could significantly enhance the validity and impact of the proposed algorithms.

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
This paper studies list replicability in multi-armed bandits and linear bandits. It comes up with the notion of $(\ell, \delta)$-list replicability, and proved various trade-off between replicability and regret dependency on number of arms and on time horizon. Furthermore, the paper extends the results to linear bandits setting.

### Strengths
1. The paper proposes a definition of reproducibility in bandits problems.
2. The paper proves tight trade-off between replicability and regret dependency on $T$. 
3. The proof to the lower bound is quite insightful.

### Weaknesses
1. The algorithms are generally based on successive elimination, so it contains less insight on more widely used bandits algorithms like UCB.
2. The proofs to the upper bounds are quite simple and lack enough novelty given their similarity to successive elimination.

### Questions
1. Line 18, $\widetilde O \sqrt{kT}$ missing parentheses.
2. The notion of $O(\cdot)$ and $\Omega(\cdot)$ was a little abused. The paper contains regret bound like $\widetilde O (k^{\frac32} T^{\frac12 + 2^{-\Omega(B)}})$. Here, it's inappropriate to use $\Omega(\cdot)$ in $\widetilde O(T^{2^{-\Omega(B)}})$, because the constant before $B$ cannot be ignored, e.g., $T^{2^{-B}}$ and $T^{2^{-2B}}$ have very different order.

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
3

### Summary
The paper introduces replicability to the multi-armed bandit area through the concept of list replicability and proposes algorithms for both k-armed and linear bandits. Notably, for k-armed bandits, the authors provide a lower bound demonstrating that one proposed algorithm is nearly optimal.

### Strengths
The paper is well-written and structured, with a clear motivation. Tho short, it presents a comprehensive set of results for both k-armed and linear bandits, though the linear bandit results appear to be preliminary.

### Weaknesses
- It would be helpful to clarify which variables the hidden logarithmic factors depend on, and whether these factors are consistent throughout the paper.
- No experiments are presented.

### Questions
- While it seems that replicability papers often omit experiments, bandit experiments are generally straightforward to conduct. Did the authors consider demonstrating some experimental results?
- Most of the algorithms appear to be adaptations of standard elimination-based bandit algorithms for both k-armed and linear bandit problems. It would be valuable if the authors could reference each classical elimination algorithm and include a side-by-side comparison showing what aspects of these algorithms break replicability and how the new modifications enable it.
- Given that the study addresses regret minimization—typically dominated by UCB-type algorithms for stronger instance guarantees—the authors’ choice of elimination-based algorithms is interesting. Could you clarify the rationale behind this choice?

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
4

### Summary
This paper introduces the concept of list replicability to the multi-armed bandit model, where the sequence of arm pulls must lie in a small finite list with high probability. The authors design and analyze three algorithms, each providing different levels of guarantees on list replicability and high-probability regret. Additionally, a nearly matching lower bound is proved for any algorithm with sub-linear regret. The paper also extends the study to linear bandits.

### Strengths
1. Although the paper is highly theoretical, it is well-presented and clearly conveys the key ideas behind the algorithm designs and proofs.

2. Three algorithms with varying levels of guarantees are introduced, each with its own significance. Notably, the first algorithm achieves near-optimal cumulative regret, and the total number of possible traces is independent of T. The last algorithm is based on a subroutine from Dixon et al. (2023) and is nearly optimal, given the lower bound in Section 6.

3. The theoretical contributions are nontrivial, and the analysis of the phase-elimination algorithm is novel, which should be of interest to the bandit community. It is also interesting that the lower bound is proven using the Sperner/KKM lemma, a combinatorial result in coloring.

### Weaknesses
The main criticism of the paper might lie in its motivation. In the introduction, it is suggested that list replicability might be beneficial for safety-critical applications, as one could be prepared for the action sequence being played. However, although the proposed algorithms can ensure a small number of traces with high probability, these possible traces cannot be known without exact knowledge of the problem instance. Therefore, outside of the theoretical domain, the practical application of list replicability seems limited.

### Questions
1. Could you compare $\rho$-replicability and list replicability with respect to their potential practical applications, such as in clinical trials?
2. Why is $C$ referred to as the number of shifts? Do you mean the number of possible shift $r$?
3. Minor typos: Line 207: Theorem 2.1 -> Assumption 2.1; Line 210: lemma -> lemmas; Line 346: the of -> the number of.
4. Thomson sampling and UCB are two well-established algorithms in the bandit literature. Thomson sampling is randomized, making it tricky to provide strong list replicability guarantees. Could you discuss the potential challenges in adapting UCB? My intuition is that UCB might achieve good list replicability with appropriate early-stage modifications.

### Soundness
4

### Presentation
4

### Contribution
3
