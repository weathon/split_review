I now have enough information. Let me produce the final consolidated review.

**Round 1 bracket: 4.5 - 6.5**

**Round 2 narrowing:**
- f-SNN (avg 4.67) — most topically similar, accepted poster. FROND has stronger theory (algebraic convergence proof, non-Markovian random walk) and broader experiments. FROND is somewhat stronger.
- HOD-GNN (avg 5.50) — accepted poster. Similar theory+experiment balance. FROND's theory aligns better with its experiments.
- Opinion Dissensus (avg 4.67) — rejected. Has strong theory but comparison issues.
- Adversarial GNN Benchmarks (avg 5.50) — rejected. Different contribution type.

Final score: 5.5 — FROND is stronger than f-SNN (4.67) in theoretical depth and experimental breadth, comparable to HOD-GNN (5.50). The comparison fairness concern is real but not fatal; the core theoretical contribution is solid and the oversmoothing experiment is properly controlled.

---

## Summary

This paper introduces FROND (FRactional-Order graph Neural Dynamical network), a framework that generalizes integer-order continuous GNNs (GRAND, GRAND++, CDE, GREAD, GraphCON) by replacing their integer-order derivatives with Caputo fractional derivatives of order β ∈ (0,1]. The core intellectual contributions are: (1) a non-Markovian random walk interpretation showing how fractional dynamics introduce path-dependent memory; (2) a proof (Theorem 3) that F-GRAND-l converges to stationarity at a slow algebraic rate Θ(t⁻ᵝ) rather than exponentially, theoretically mitigating oversmoothing; (3) experimental validation showing F-GRAND-l outperforms GRAND-l on 8 of 10 node-classification datasets and F-CDE outperforms CDE on 5 of 6 heterophilic datasets.

## Strengths

1. **Novel and well-motivated theoretical framework.** Introducing fractional calculus into continuous GNNs is a genuinely new direction. The Caputo derivative is well-justified, and the connection to fractal graph datasets (Section 1) provides a compelling motivation grounded in physical principles. The framework properly subsumes integer-order models as the special case β = 1.

2. **Algebraic convergence rate proof for oversmoothing mitigation (Theorem 3).** The paper proves that F-GRAND-l converges to the stationary distribution at rate Θ(t⁻ᵝ), contrasting with the exponential convergence of integer-order diffusion. This is a clean theoretical result that directly supports the oversmoothing claim and is corroborated by the controlled experiment in Figure 3, where F-GRAND-l maintains stable accuracy up to 128 layers while GRAND-l degrades sharply on the Airport dataset.

3. **Non-Markovian random walk interpretation (Theorem 1, Corollary 1).** The paper establishes a precise connection between the fractional diffusion equation and a random walk whose transition probabilities depend on the full path history. This gives an interpretable mechanism for the "memory" in FROND and clarifies how β controls the degree of memorization.

4. **Generality across multiple continuous GNN architectures.** FROND is applied to five distinct integer-order continuous GNNs (GRAND, GRAND++, GREAD, CDE, GraphCON), and experimental results for F-GRAND, F-CDE, and additional variants in the appendix show consistent improvement. This demonstrates that FROND is a plug-in enhancement rather than a single-model contribution.

5. **Ablation study on β (Table 3).** The paper systematically varies β (0.1–1.0) on Cora and Airport, showing that optimal β varies by dataset (0.9 for Cora, 0.5 for Airport) and that β=1 is suboptimal for both. This substantiates the claim that β is a meaningful hyperparameter tied to dataset topology.

## Weaknesses

### Major

1. **Lack of controlled comparison for integer-order baselines (structural concern).** The paper states: *"Where available, results from the paper [chamberlain2021grand] are used"* (line 309) and for CDE: *"results from the original paper are reported"* (line 396). This means the GRAND and CDE results in Tables 1 and 5 may have been produced under different training conditions (hyperparameters, learning rates, epochs, random seeds, compute budget) than the FROND variants. While the paper's stated goal is "not to achieve state-of-the-art results" (line 297), the central empirical claim is that FROND *consistently outperforms* integer-order counterparts, and this comparison is not fully controlled. For the strongest version of this claim, the integer-order baselines should be re-run in the same pipeline with equivalent hyperparameter search effort (including over T and step size). This weakness does not undermine the theoretical contributions but weakens the experimental evidence.

2. **Solver ambiguity in the oversmoothing experiment.** The oversmoothing experiment (Section 4.3, Figure 3) compares F-GRAND-l (using the basic predictor, Eq. 4) against GRAND-l. When β = 1, the basic predictor reduces to forward Euler. However, the paper does not explicitly confirm that the GRAND-l results in Figure 3 were obtained using the *same* basic predictor with β = 1. If the GRAND-l results come from a different implementation or solver, the comparison conflates solver choice with fractional order. Given that the oversmoothing claim is central and the theory (Theorem 3) is about the continuous dynamics, isolating β as the sole variable is critical. The paper should state clearly whether GRAND-l was run with the basic predictor (β=1) or otherwise.

### Minor

3. **β-tuning methodology under-specified.** The paper reports "optimal β" for each dataset but does not state the search range, step size, or validation strategy used for tuning β (lines 383, 396). This affects reproducibility. The ablation in Table 3 uses T=8 but it is unclear whether T was jointly optimized with β in the main results.

4. **Missing entries and omitted variants in tables.** In Table 1, GIL results for Computer, Photo, CoauthorPhy, and ogbn-arxiv are listed as "--" without explanation. For graph classification (Table 2), only F-GRAND-l and GRAND-l are reported; the nonlinear variant and other FROND-based models are omitted. While the paper references the appendix for additional results, the main paper's comparison is narrower than the claimed generality.

5. **Oversmoothing theory vs. experimental overreach.** Theorem 3 and the oversmoothing mitigation claim are proven for the *linear* diffusion case (F-GRAND-l). The paper states that FROND (generally) mitigates oversmoothing (e.g., abstract: "oversmoothing can be mitigated"), but the theoretical guarantee does not extend to the nonlinear (nl) variants used in most experiments. The gap is acknowledged indirectly but should be stated explicitly.

### Trivial

6. The paper references many appendix sections (e.g., `\cref{sec.app_moredynamic}`) that are not present in the extracted text but presumably exist in the full submission.

## Nice-to-Haves

- Re-running all integer-order baselines (GRAND, CDE, etc.) with the same training pipeline and equivalent hyperparameter search (including T and step size) would substantially strengthen the core empirical claim.
- A small empirical study linking optimal β to estimated graph fractal dimension (e.g., box-counting) would connect the motivation to the results.
- Clarifying whether GRAND-l results in the oversmoothing experiment were produced from the same basic predictor code with β=1.

## Removed Points

- *"Introduction motivation not validated"* — The paper acknowledges this as future work (referencing appendix sections on fractality). This is scope-appropriate for a first paper proposing the framework. **Reason: acknowledged as future work, not a current claim.**
- *"Missing related works"* — Not verifiable without external sources; per instructions, this is excluded. **Reason: rule-based removal.**
- *"β as extra hyperparameter without controlling for T"* — Partially addressed. The ablation in Table 3 uses T=8, showing β matters at fixed T. The critic's suggestion to tune T for integer-order is a nice-to-have but not a fatal gap, since the paper shows that FROND (with β<1) at the *same* T outperforms β=1. **Reason: partially addressed; demoted to nice-to-have.**
- *"Missing confidence intervals"* — Not a standard requirement for large-scale GNN benchmarks; single-run evaluation is common. **Reason: standard practice in the field.**
- *"Unfair comparison favors author's method"* — The disparity (baselines from different papers) is a genuine concern, retained as Major #1. But the critic's characterization of it as "fatal" or "invalidating the experimental foundation" is overstated — the paper's theory is independent, and the oversmoothing experiment is controlled. **Reason: retained but downgraded from Fatal to Major because the paper's core theoretical claims stand independently.**
- *"Reproducibility: undisclosed hyperparameters"* — Minor concern about β search strategy (retained as Minor #3). Other hyperparameter criticisms are too generic. **Reason: merged into Minor #3.**

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the comparison fairness issue is the most insightful external point, but it identifies a methodological gap rather than providing a new scientific insight about the paper's domain.

## Suggestions

1. In a rebuttal or revision, clarify whether the GRAND-l and CDE baselines were re-run in the same training pipeline as the FROND variants. If they were, state this explicitly. If not, either re-run them or clearly delineate which results are from the authors' controlled pipeline vs. cited from prior work.
2. For the oversmoothing experiment, explicitly state that GRAND-l was run with the same basic predictor (β=1), confirming that the only difference is the fractional order.
3. Report the β search strategy (range, step size, validation protocol) in the main text.
4. Acknowledge explicitly in Section 4.3 that the oversmoothing theory covers only the linear variant, and that the nonlinear results are empirical.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>