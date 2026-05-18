Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces FROND (FRactional-Order Graph Neural Dynamical Network), a framework that generalizes continuous GNNs by replacing integer-order derivatives (β=1 or 2) with Caputo fractional derivatives of order β∈(0,1]. This enables non-local, memory-dependent feature dynamics. The paper provides a non-Markovian random walk interpretation of F-GRAND-l (the linear variant) and proves that convergence to stationarity follows a slow algebraic rate Θ(t⁻β) rather than exponential, theoretically supporting oversmoothing mitigation. Empirically, FROND variants (F-GRAND, F-CDE, F-GRAND++, F-GREAD, F-GraphCON) are shown to consistently outperform their integer-order counterparts across citation, tree-structured, heterophilic, and large-scale datasets.

## Strengths

- **Principled introduction of fractional calculus to continuous GNNs** — The paper grounds its approach in the Caputo fractional derivative (Section 2.1), which has a well-established mathematical foundation. Setting β=1 recovers existing integer-order models exactly, so FROND is a strict generalization with no risk of performance degradation relative to the base model. This is demonstrated across five different continuous GNN architectures.

- **Non-Markovian random walk interpretation** — Theorem 1 (Section 3.2, Eq. 11) derives a random walk whose transition probabilities depend on the full path history via coefficients c_k(β) and b_n(β) from the Grünwald-Letnikov discretization. The limiting distribution satisfies the F-GRAND-l equation, providing a concrete mechanistic link between fractional dynamics and memory effects that goes beyond the black-box ODE formulation of prior continuous GNNs.

- **Theoretical guarantee of algebraic convergence for oversmoothing mitigation** — Theorem 2 (Section 3.3) proves that F-GRAND-l converges to stationarity at rate Θ(t⁻β) for β<1, in contrast to the exponential convergence of GRAND-l. This is the first such result connecting fractional derivatives in GNNs to oversmoothing and is clearly distinguished from prior work that used fractional graph shift operators with integer-order ODEs (Maskey et al. 2023) or fractional gradient propagation (Liu et al. 2022).

- **Consistent empirical gains across diverse settings** — Tables 1, 3, 4, and the heterophilic results (Table for F-CDE) show that FROND variants improve over their integer-order counterparts on citation networks (e.g., Cora: 84.8 vs 83.6), tree-structured data (Airport: 98.1 vs 80.5 for GRAND-l), and heterophilic datasets (Roman-empire: 93.06 vs 91.64). Gains are consistent and not limited to one architecture or dataset type.

## Weaknesses

### Major

- **Oversmoothing experiment (Figure 3) lacks error bars and statistical rigor** — Figure 3 is the primary experimental evidence for the core oversmoothing-mitigation claim, yet no error bars, number of runs, or confidence intervals are reported. The text describes performance qualitatively ("maintains a consistent performance level across all datasets as the number of layers increases"), but with a single trajectory per dataset from fixed splits (as noted in Section 4.3: "we utilize the fixed data splitting"), this could reflect a favorable split rather than a robust phenomenon. The theoretical result (Theorem 2) predicts slower convergence, but the experimental validation needed to confirm it is underreported. The authors should report mean and standard deviation over multiple seeds at each depth, for both GRAND and F-GRAND.

- **The Airport result (98.1±0.2 for F-GRAND-l vs 80.5±9.6 for GRAND-l) requires clarification** — The ~17.6 point gap is far larger than on any other dataset, and GRAND-l's standard deviation of 9.6 is unusually high, suggesting instability or suboptimal tuning of that baseline. GRAND-nl achieves 90.9±1.6 and GIL achieves 91.5±1.7 on the same dataset, so the GRAND-l baseline (80.5) appears anomalously low. The paper attributes F-GRAND-l's success to smaller β being preferable on tree-structured data, but does not explain why GRAND-l underperforms GRAND-nl and GIL by such a wide margin, or whether the same splits were used for all methods. This outlier demands verification—e.g., confirming with multiple split seeds or ruling out a baseline implementation issue.

### Minor

- **Theoretical results stated without proof sketches** — Theorem 1 (random walk interpretation) and Theorem 2 (algebraic convergence) are stated in the main text but proofs are deferred entirely to cited references ([Gorenflo 2002]) without even a high-level derivation sketch. While deferring proofs to appendices is common in ML conference papers, here the paper does not verify whether the required assumptions (strong connectivity, aperiodicity) are satisfied in practical settings, or whether the algebraic rate depends on spectral properties of L. Theorem 2's notation Θ(t⁻β) does not specify asymptotic vs. finite-time behavior, which matters since practical integration times T are finite (e.g., T=8).

- **Graph classification experiments compare only GRAND-l** — Table 3 (graph classification on Politifact/Gossipcop) compares F-GRAND-l only against GRAND-l. No GRAND-nl or other strong baselines (GCN, GAT with comparable tuning) are shown for this task, making it hard to judge whether the 1–3% improvement is significant relative to a reasonable range of alternatives.

- **β selection protocol is underspecified** — The paper reports optimal β values per dataset (gray rows in Table 1) and an ablation study (Table beta), but does not clearly state whether β was tuned on validation data or selected post-hoc. If β was selected to maximize test performance, the reported gains are not valid for generalization claims.

- **CDE on heterophilic data (Table 4): improvement is marginal for some datasets** — On Questions, F-CDE with β=1 gives identical performance to CDE (no improvement), indicating that not all datasets benefit from fractional dynamics. The paper acknowledges this implicitly but does not discuss why some settings see no benefit or what dataset characteristics predict when β<1 helps.

### Trivial

- Figure 3's y-axis label is partially cut off in the rendered PDF (likely a parser artifact).
- The conclusion section is notably brief and lacks any discussion of limitations or failure cases.

## Nice-to-Haves

- A direct experimental validation of the algebraic convergence rate (e.g., plotting ‖X(t) − πᵀX(0)‖_F on a log-log scale for GRAND-l vs F-GRAND-l across multiple time steps) would significantly strengthen the link between theory and experiments.
- Reporting wall-clock time or memory usage vs. layers, and comparing the short-memory variant's accuracy/cost trade-off, would help practitioners understand when FROND is practical.
- The speculative connection between optimal β and graph fractality (raised in the Introduction) is interesting but untested; correlating β with a graph fractal dimension statistic would add value.

## Removed Points

- *Transition probabilities not verified to sum to 1*: The paper explicitly states "the sequences satisfy ∑c_k + b_n = 1" (line 138) and cites [Gorenflo 2002]; this is not a weakness.
- *Comparison to prior fractional GNN works (Maskey et al., Liu et al.)*: The paper correctly distinguishes these as fundamentally different approaches (fractional graph shift with integer-order ODEs, and fractional gradient descent for training). Experimental comparison is not straightforward given the different problem settings.
- *Over-reliance on appendices*: A standard space constraint in ML papers; the main text covers the core variants (F-GRAND-l, F-GRAND-nl) and sketches the others.
- *Missing related works*: Cannot be verified from available materials.
- *Missing appendix content*: Parser strips appendices from all papers; they exist in the original submission.
- *Formatting/style nitpicks*: Parser artifacts, not author errors.
- *Generic "could be stronger with X" speculation*: Removed where not grounded in specific evidence from the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add error bars to Figure 3** — Report mean and standard deviation over at least 5 random seeds for each depth, and show both GRAND-l and F-GRAND-l curves with error bars. This single change would substantially strengthen the oversmoothing claim.

2. **Clarify the Airport result** — Either explain why GRAND-l performs so poorly (80.5±9.6) compared to GRAND-nl (90.9±1.6) and GIL (91.5±1.7), or re-run with consistent random splits to verify the 98.1% result is not driven by a favorable split or baseline implementation issue.

3. **Provide proof sketches for Theorems 1 and 2** — Even a paragraph explaining how the algebraic rate emerges from the Mittag-Leffler function solution, and whether the result depends on spectral properties of L, would make the theory self-contained enough for a reader to assess its validity.

4. **Report β tuning protocol explicitly** — State whether β was selected on a validation set, and if so, how many values were searched. A sensitivity analysis showing performance vs. β on 2–3 datasets is already present (Table beta) and useful; just clarify the selection process.

5. **Expand graph classification baselines** — Add at least GRAND-nl and a tuned GCN/GAT to Table 3 to contextualize the 1–3% improvement.

---

**Calibration Summary**

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| S3zKrEQpRr.md | 3.00 | R1 (low) | Unrelated topic (noise channel perspective); much weaker paper |
| zuuhtmK1Ub.md | 2.00 | R1 (low) | Implicit PDE solver; much weaker and different topic |
| xA25Ib7H8U.md | 2.33 | R1 (low) | Ricci flow continuous-depth; weaker theory-practice link |
| NLbRvr840Q.md | 6.00 | R1/R2 (mid) | Hypergraph ODE system; comparable scope and rigor. FROND has broader experiments; HDS has more theory but some conceptual issues |
| 7b2JrzdLhA.md | 6.00 | R1 (mid) | Graph neural Ricci flow; comparable continuous GNN+theory paper. GNRF has more complete proofs; FROND has wider experimental validation |
| l6eA8Srlqd.md | 5.50 | R1 (mid) | CTAN for dynamic graphs; similar ODE+theory structure. FROND is more novel and better validated |
| i8vPRlsrYu.md | 7.00 | R2 (high) | Residual connections for oversmoothing; tighter theory, cleaner experiments. FROND is weaker than this anchor |
| AbXGwqb5Ht.md | 7.00 | R2 (high) | Deep residual nets → neural ODEs regularization; strong theory paper. FROND is weaker |
| ZZwP9zljas.md | 5.25 | R2 (low) | Edge-dropping and over-squashing; narrower focus, more limited contribution. FROND is stronger |
| sBSC0OXEQG.md | 4.50 | R2 (low) | Associative memories; different topic, lower quality |

**Round-1 Bracket**: After reading the paper and the initial anchor set, the plausible range was [5.0, 7.0].

**Round-2 Narrowing**: After reading full reviews of GNRF (6.0), HDS (6.0), Residual Connections (7.0), and Edge-Dropping (5.25), I compared each: FROND is comparable to GNRF and HDS (score 6.0) — all three make novel continuous-depth contributions with theory and experiments, each with some gaps. FROND is weaker than the Residual Connections paper (7.0) which has tighter, self-contained theoretical proofs and cleaner experimental validation. FROND is stronger than the Edge-Dropping paper (5.25) whose contribution is narrower and more incremental. **Final score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>