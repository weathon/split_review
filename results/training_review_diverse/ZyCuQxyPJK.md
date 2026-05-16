Now I have a thorough understanding of the paper and can cross-check all claims. Here is my consolidated review.

---

## Summary

This paper introduces NeuroLifting, a method that reparameterizes MAP inference in Markov Random Fields by embedding discrete variables into continuous GNN representations and minimizing expected energy via gradient descent. The approach is evaluated on synthetic MRFs, UAI 2022 competition instances, and PCI (cellular network) data, with comparisons against LBP, TRBP, and the exact solver Toulbar2. The core idea — using GNN features as a learned reparameterization for MRF optimization — is interesting and shows promise on large-scale instances.

## Strengths

- **Competitive results on large-scale MRFs (50k nodes):** On synthetic pairwise instances with 50k nodes (Table 1, P_potts_4–9, P_random_4–9), NeuroLifting often achieves the lowest energy among all baselines, including Toulbar2. This is the paper's strongest empirical result and supports its claim of practical scalability.

- **Principled connection between GNN reparameterization and MRF structure:** The paper grounds the choice of GraphSAGE (equal-weight neighbor aggregation) in the MRF property that neighbors should be treated symmetrically (Section 3.2–3.3), and justifies the GNN-as-lifting analogy by observing that expanding discrete variables into continuous embeddings mirrors the optimization-lifting paradigm of adding dimensions to ease computation (Section 3.5). This provides a conceptually coherent motivation.

- **Practical applicability demonstrated on PCI data:** On larger real-world PCI instances (PCI_4–5 and all synthetic PCI cases, Table 5), NeuroLifting achieves the best energy values, outperforming both LBP/TRBP and Toulbar2 (which is limited by its 3600s time budget). This demonstrates value on an applied engineering problem.

- **Ablation studies on design choices:** The paper compares GNN backbones (GraphSAGE vs. GCN vs. GAT, Fig. 3) and optimizers (Adam vs. RMSprop vs. SGD, Fig. 4), providing evidence for the chosen configuration.

## Weaknesses

### Major

1. **No variance or multiple-run reporting despite random initialization.** The method uses randomly initialized GNN parameters and random initial features, yet all results are reported as point estimates from single runs without standard deviations, confidence intervals, or even a note that results are representative. For a non-convex optimization procedure, single-run numbers are not statistically meaningful — a 2–4% gap versus LBP could be noise. This is the most serious methodological gap and undermines the reliability of all comparative claims.

2. **Broad performance claims contradicted by the paper's own data on small/medium instances.** The abstract and introduction state that NeuroLifting "outperforms all existing approximate inference strategies in terms of solution quality" and "delivers superior solution quality against all baselines." However, on small synthetic instances (1k–10k nodes, Table 1), NeuroLifting is consistently the worst method — worse than LBP, TRBP, and Toulbar2 on P_potts_1–3 and P_random_1–3. On UAI pairwise instances (Table 3), Toulbar2 always finds the optimal solution and NeuroLifting often trails LBP and TRBP on ProteinFolding and Grids problems. These patterns do not support the claimed universal superiority. The claims should be scoped to large-scale instances, where the evidence is genuinely stronger.

3. **Complexity analysis is incomplete for high-order cliques.** The derived complexity \(O(|\mathcal{X}|(|\mathcal{V}| + c_{\max}|\mathcal{C}|) + K|\mathcal{V}|(\mathcal{N}_v + d))\) (Section 3.5) treats the loss computation as linear in \(|\mathcal{X}|\) per clique. But the loss \(L(\theta) = \sum \langle \psi(C_k), P_k \rangle\) with \(P_k = \bigotimes_{i \in C_k} p_i\) requires a tensor product and inner product that cost \(O(|\mathcal{X}|^{|C_k|})\) per clique — exponential in clique size, not linear. The paper evaluates on high-order instances (Table 2) without addressing this cost. While the analysis is reasonable for pairwise MRFs (the primary focus), the omission of the exponential factor for high-order cases is a material inaccuracy in the claimed scalability.

### Minor

4. **Missing comparison to other neural/learned inference methods.** The paper compares only to LBP, TRBP, and Toulbar2 (an exact solver). Given that this is a neural-network-based method, several relevant baselines are absent: learned optimization approaches for graphical models, neural belief propagation variants, or even a simple learned mean-field baseline. Without such comparisons, it is difficult to isolate whether the GNN reparameterization itself is the driver of performance or whether a simpler learned baseline would achieve similar results.

5. **Time-limited comparison with exact solvers favors NeuroLifting on large instances.** On PCI data (Table 5) and some UAI high-order instances (Table 4), Toulbar2 is given a time limit (1200s or 3600s) and NeuroLifting achieves lower energy. Since Toulbar2 is an exact solver (optimal given unlimited time), this only demonstrates that Toulbar2 did not finish within the budget. The paper acknowledges this implicitly but does not discuss whether Toulbar2 would eventually find better solutions or prove optimality.

6. **Padding strategy not empirically validated.** The padding choice (filling with max energy of the original term) is described and rationalized (Section 3.2, Remark 1), but there is no ablation comparing alternative strategies (e.g., masking, a very large constant). The remark itself notes that other strategies "are also being considered," which implicitly acknowledges uncertainty. This is a design decision that could affect solution quality and should be ablated.

### Trivial

7. **Loss landscape visualization (Fig. 6) shown for only one instance (Segmentation_19).** This is insufficient to support the general claim that deeper layers "expand feasible regions." The choice of perturbation directions \(\delta\) and \(\eta\) for the 2D visualization is not explained.

8. **No discussion of limitations.** The paper does not discuss when the method might fail (e.g., small instances where it underperforms LBP, sensitivity to hyperparameters, the exponential cost of high-order cliques). A brief limitations paragraph would improve the paper.

## Nice-to-Haves

- A comparison with a simple learned baseline (e.g., a single-layer GNN or MLP trained with the same loss) would help isolate whether the multi-layer GNN structure or the lifting analogy adds value.
- Reporting the actual clique sizes in the high-order instances (Table 2 and Table 4) would clarify whether the exponential tensor cost is actually incurred.
- An empirical check on rounding quality (e.g., proportion of variables with probability mass concentrated near 1.0) would support the claim that "we won't see any multi-assignment issue."

## Removed Points

These points from the reviews are flagged to be removed; treat them with caution.

- **"NA in H_Instances_2 has no explanation":** The caption of Table 2 explicitly states "NA denotes that no solution was found within the specified time limits." The reviewer missed this.
- **"Table 1 caption mentions bracketed numbers that don't appear":** The brackets likely contain the loss value; their absence in the extracted text is a parser/formatting artifact, not an author error.
- **"UAI pairwise claim contradicted by data (NL 'often performs worse than LBP'):** On Segmentation instances (Table 3), NeuroLifting achieves lower energy than LBP on 6 of 10 cases, higher on 2, and approximately tied on 2. The claim of being "on par with LBP/TRBP" is reasonable on this subset; the reviewer's characterization is inaccurate.
- **"The GNN is parametric, not non-parametric":** The paper uses "non-parametric lifting" to mean that the initial features are unstructured random embeddings (no hand-crafted features), not that the GNN has no parameters. This is a semantic debate, not a substantive flaw.
- **"Complexity analysis is linear in key problem parameters" (from Strength Finder):** This strength conflicts with the verified weakness (the analysis is incomplete for high-order cliques). Moved here per the rule that verified weaknesses override conflicting strengths.
- **"No code release" criticism:** A code release is a nice-to-have; its absence is not a structural weakness of the paper's scientific contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Temper all broad claims ("outperforms all existing approximate inference strategies") to match the evidence: NeuroLifting excels on large-scale instances but underperforms LBP on small ones. Scope the claims accordingly.
2. Run experiments with at least 5–10 random seeds and report mean ± std. Without this, the reader cannot assess whether the observed gaps are significant.
3. Correct the complexity analysis to reflect the exponential dependence of the tensor product on clique size, and discuss when this is manageable and when it is not.
4. Add at least one learned baseline (e.g., a simple MLP trained with the same expected-energy loss) to help contextualize the contribution of the GNN architecture.
5. Add an ablation comparing the chosen padding strategy (max-energy padding) against alternatives (large constant, masking) on a representative subset of instances.

## Score and Decision

The paper presents a reasonable and interesting approach — GNN-based reparameterization for MRF MAP inference — with promising results on large-scale problems. However, the most serious weakness — complete absence of variance reporting despite random initialization — undermines the statistical reliability of all empirical comparisons. Combined with overclaimed novelty/performance and an incomplete complexity analysis, the paper in its current form does not make a convincing case. The core idea has merit, but the experimental methodology and claims require substantial revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>