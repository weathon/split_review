## Summary

This paper proposes an exact distributed Bayesian network structure-learning framework via "conditional P-map reductions." It defines formal conditions under which variables can be partitioned into overlapping subsets such that each subset's structure can be learned independently (via any exact structure learner) and the results provably concatenated into the exact global P-map. Three algorithms are sketched: a cover-finding routine (Algorithms 2/3) and a distributed learner (Algorithm 1). Experiments on seven small benchmark datasets show up to 2× speedup on 30 CPUs with no significant loss in accuracy compared to centralized PC.

## Strengths

- **Rigorous formal framework for exact distributed decomposition.** Definitions 3.1–3.4 (P-map reduction, conditional P-map, conditional P-map reduction, separated-by cover) provide theoretically precise conditions under which distributed structure learning yields the exact global P-map rather than an approximation. This contrasts with prior distributed approaches (e.g., Gu & Zhou, 2020) that the paper correctly notes produce only estimates. The theoretical framing is the paper's clearest contribution.

- **Bounded conditioning set size.** The approach constrains the conditioning set during decomposition to at most \(W\) variables, which the conclusion (line 121) correctly identifies as a departure from prior exact distributed algorithms (Xie et al., 2006; Liu et al., 2017) that require high-order conditioning or expert knowledge.

- **Concrete dependency-matrix procedure for testing a separator.** The paper describes constructing a symmetric dependency matrix \(D_{\mathcal{W}}\) for a candidate separator \(\mathcal{W}\) and finding connected components in \(O(n^2)\) time (line 89), providing a practical subroutine for the decomposition step.

## Weaknesses

### Major

- **Experimental evidence does not support the paper's central scalability claim.** The paper claims to "open the door for structure learning for a 'giant' number of variables" (Abstract, line 4), yet:
  - All seven datasets are small (largest ~70 variables; none remotely at "giant" scale).
  - The decomposition parameter is set to \(d = 0.75n\) (line 106), meaning components are barely smaller than the original problem. For ASIA (8 vars), \(d=6\) — the decomposition is essentially trivial.
  - The maximum speedup is 2× on 30 CPUs (~7% parallel efficiency). A method whose selling point is scalability needs to demonstrate, at minimum, that it enables structure learning on problems where centralized learning is infeasible.
  - No experiments vary \(d\) or \(W\) to study the tradeoffs discussed qualitatively in the conclusion (line 117).

  These limitations are verifiable from lines 106 and 117. The gap between the claimed contribution and the experimental evidence is substantial.

- **No complexity analysis in a methods paper motivated by computational feasibility.** The paper provides no runtime or sample complexity analysis for any of its algorithms. The cover-finding step's cost — which could dominate the total runtime — is neither analyzed nor reported separately. For a paper whose core argument is that centralized methods cannot scale and a distributed alternative can, this omission is critical.

- **Cover-finding algorithm description is underspecified and raises unaddressed complexity concerns.** Algorithm 2 (line 99) is described in prose as picking the largest component and "check[ing] if any subset \(\mathcal{W} \subset \mathcal{U}\) separates the component," with the power set \(\mathcal{P}(\mathcal{U})\) explicitly noted. For an initial component \(\mathcal{U} = \mathcal{X}\) of size \(n\), a naive interpretation would involve testing \(2^n\) candidate separators. The paper does not explain how this search is performed efficiently, does not analyze its complexity, and does not acknowledge the concern. While Algorithm 3 (which was actually used in the experiments, per line 106) may avoid this issue, its mechanism is not described in the main text, so the reader cannot evaluate it. The paper thus presents a cover-finding algorithm whose prose description suggests intractability, and whose practical variant is opaque.

- **No comparison against any parallelized baseline.** The only baseline is single-threaded PC. The paper itself cites parallel CI testing methods (Zarebavani et al., 2019; line 14) and acknowledges them in the conclusion (line 119), but does not compare against them. Since Algorithm 1 uses 30 CPUs, the relevant comparison is against a parallelized version of the baseline — otherwise, the observed speedup may simply reflect parallel CI testing rather than the algorithmic benefits of decomposition. This makes the 2× speedup difficult to interpret as a validation of the decomposition approach.

### Minor

- **No characterization of when a conditional P-map reduction exists.** The paper gives one counterexample (Figure 2a) where a P-map reduction fails but a conditional one succeeds, but provides no characterization of the class of DAGs for which the overall approach can succeed. This limits the reader's ability to assess the method's applicability to new problems.

- **No runtime breakdown.** The paper does not report how time is distributed across cover-finding, local structure learning, and boundary reconciliation. This makes it impossible to identify bottlenecks or to assess whether the cover-finding step could become a computational barrier at larger scales.

### Trivial

- None that carry any weight in evaluation. The parser introduces several formatting artifacts (e.g., \(\not\subset\) for \(\not\perp\) in line 89, inconsistent use of \(\chi\) vs \(\mathcal{X}\)), but these are not author errors.

## Nice-to-Haves

- A dedicated experiment on a problem where the full set cannot be learned on a single machine (e.g., 200+ variables) would directly test the scalability claim.
- Ablation studies varying \(d\) and \(W\) would illuminate the tradeoffs discussed in the conclusion and help practitioners choose parameters.
- Comparison against a parallelized PC baseline would isolate the contribution of the decomposition from the gains of parallel CI testing.

## Removed Points

The following points from the reviewer inputs are removed as not valid for the final review:

- **Dependency matrix symbol error** (Harsh Critic's point 3): The \(\not\subset\) symbol is a parser artifact — the original LaTeX likely used \(\not\perp\). Per instructions, formatting artifacts from PDF parsing are not author errors.
- **Boundary PC algorithm not specified** (Harsh Critic's point 4): The description of the Boundary PC algorithm and other algorithmic details referenced as "Remark A" are in the appendix, which was stripped by the parser. Per instructions, missing appendix content is not flagged.
- **Algorithm 3 not described in main text** (Harsh Critic): Same rationale — Algorithm 3's description is likely in the stripped appendix. The weakness about complexity concerns from Algorithm 2's prose description is retained as a separate point.
- **No runtime variance reported**: Too generic to merit inclusion as a distinct weakness; absorbed into the broader experimental concerns.
- **Wilcoxon test low power on 7 datasets**: Overly pedantic for a conference paper; not a meaningful threat to validity.
- **Strength Finder's claim of "statistically significant speedup" as a core strength**: Demoted from a core strength because the experimental design (small datasets, d=0.75n, no parallel baseline) makes the practical significance of this result unclear — this is reflected in the Major weaknesses above.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not reveal any observation about the method or problem that the paper itself does not make.

## Suggestions

1. **Acknowledge and analyze the complexity of the cover-finding step.** Either show that Algorithm 2 has bounded worst-case complexity (e.g., because the search space is limited by \(d\) or \(W\)), or state clearly that Algorithm 3 is the practical variant and describe its approach and complexity in the main text.

2. **Redesign the experiments to match the claims.** Demonstrate the method on a problem with enough variables that centralized learning is memory- or time-infeasible. Report the wall-clock breakdown (cover-finding vs. local learning vs. boundary reconciliation). Compare against a parallelized version of PC (e.g., parallel CI testing per Zarebavani et al., 2019) to isolate the decomposition's contribution.

3. **Provide ablations over \(d\) and \(W\),** showing how these parameters affect decomposition depth, total CI test count, and total runtime. This would substantiate the tradeoff discussion in Section 5 and give practitioners guidance.

4. **Characterize the class of DAGs for which a conditional P-map reduction exists** (or provide a sufficient condition). This would clarify the method's scope of applicability beyond the counterexample in Figure 2a.

## Score and Decision

The paper makes a genuine theoretical contribution in its formal framework for exact distributed structure learning. However, the experimental validation is mismatched to the paper's central scalability claims, the complexity of the algorithms is unanalyzed, the cover-finding algorithm description raises unanswered tractability concerns, and no parallelized baselines are included. The gap between the claimed contribution and the supporting evidence is too large for acceptance at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>