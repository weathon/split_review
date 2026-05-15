Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper introduces Subgraph Multilinear Extension (SubMT), a theoretical framework that formulates interpretable subgraph learning in XGNNs via the multilinear extension of the subgraph distribution. It identifies that existing attention-based XGNNs fail to reliably approximate SubMT due to the non-linearity of GNNs (the Jensen gap), and proposes Graph Multilinear neT (GMT) with two variants — GMT-lin (linearized message passing) and GMT-sam (MCMC subgraph sampling) — that provably reduce this approximation error. Extensive experiments across regular and geometric graph benchmarks show consistent improvements of up to 10–15% in interpretability and 13–16% in generalization over prior XGNNs.

## Strengths

- **Novel theoretical framework connecting XGNNs to multilinear extension.** The SubMT formulation (Definition 3.1) is the first to formally characterize XGNN expressivity through the lens of multilinear extension — a well-studied tool in combinatorial optimization. This provides a principled foundation for analyzing why prior methods fail, going beyond purely empirical observations to identify a fundamental representational limitation.

- **Counterfactual fidelity as a principled faithfulness metric.** Definition 4.1 introduces a theoretically grounded measure that jointly captures interpretability and generalization. Proposition 4.2 links it to SubMT approximation, and the empirical evidence (Fig. 2b,c) confirms that GSAT's counterfactual fidelity is 2–3× lower than simulated SubMT — directly validating the theoretical analysis.

- **Provably better architecture with sampling guarantees.** Theorem 5.1 proves that GMT-sam with MCMC sampling achieves high-probability SubMT approximation and satisfies $(\delta, 1 - \frac{\epsilon C}{\delta})$-counterfactual fidelity. This is a principled improvement over weighted message-passing schemes, backed by theoretical guarantees rather than heuristic design.

- **Consistent and substantial empirical gains across diverse settings.** Tables 1–4 show GMT (both variants) outperforms state-of-the-art XGNNs (GSAT, LRI, DIR, IB-subgraph) by up to 10–15% in interpretation AUC and 13–16% in prediction accuracy across regular graph benchmarks (BA-2Motifs, Spurious-Motif, MNIST-75sp, OGBG-MOLHIV) and geometric benchmarks (ACTSTRACK, TAU3MU, SYNMOL, PLBIND) with GIN, PNA, and EGNN backbones.

- **Ablation evidence connecting theory to practice.** Figure 3a directly demonstrates that GSAT has lower counterfactual fidelity than GMT-lin and GMT-sam, confirming that the theoretical SubMT approximation gap manifests in measurable faithfulness degradation.

## Weaknesses

### Fatal

None. The paper's core claims are supported by a combination of theoretical analysis and extensive empirical evidence. No errors invalidate the central contribution.

### Major

- **Interpretation AUC metric is never defined.** The paper reports "Interpretation Performance (AUC)" in Tables 1 and 3 without specifying what quantity AUC measures — whether it is edge-level ROC AUC for detecting ground-truth motif edges, or something else. Without this definition, the reader cannot independently evaluate the headline empirical claims. This is particularly problematic for datasets like OGBG-MOLHIV where no known ground-truth causal subgraph exists. While AUC for interpretation is a standard metric in the XGNN literature (GSAT, DIR), the paper should state it explicitly rather than leave it implicit.

- **Theoretical scope gap between Proposition 3.3 and the paper's narrative.** Proposition 3.3 formally establishes that **linearized GNNs** (Wu et al., 2019) with k>1 layers cannot approximate SubMT due to the Jensen gap. This is a valid technical result for its stated scope. However, the paper's broader narrative — particularly the abstract's claim that "existing XGNNs can have a huge gap in fitting SubMT" — implicitly extends this finding to non-linear GNNs used in practice. The paper does not provide a general bound for non-linear architectures with arbitrary activations, where the function may be neither convex nor concave and the Jensen gap need not be systematic. The empirical counterfactual fidelity results (Fig. 2, 3) partially bridge this gap, but the theoretical foundation is narrower than the narrative suggests. Theorem 5.1's guarantee for GMT-sam, while valid, is a standard concentration bound (Hoeffding) with constant $C = |\mathcal{Y}|$ that may be loose in practice.

### Minor

- **Practical counterfactual fidelity estimator does not enforce the $\delta$ condition.** Definition 4.1 requires that perturbations $\widetilde{G}$ satisfy $d(P(Y|G), P(Y|\widetilde{G})) \geq \delta$ (meaningful minimal distance). The practical estimator (Eq. 12) uses random Gaussian perturbations to the attention matrix without verifying this condition, so perturbed subgraphs may not correspond to causally distinct interventions. The paper acknowledges this is a "practical estimation" but does not discuss how violations of the $\delta$ condition affect the reliability of the measure.

- **Computational cost of GMT-sam not reported.** GMT-sam requires $t$ sampling rounds (10–100 in experiments), but the paper provides no runtime or overhead comparison with baselines. This is important for practitioners evaluating the practical trade-off between interpretability gains and inference cost.

- **"Neural SubMT" learning justification is heuristic.** The proposal to retrain a new classifier with a frozen extractor to approximate the MCMC estimator (lines 228–232) is presented without theoretical justification for why this distillation should succeed. The paper acknowledges that approximating MCMC with a neural network is "inherently challenging" and appeals to the causal subgraph assumption, but does not analyze the approximation error of this step.

- **The derivation from Eq. 2 to Eq. 3** is presented without explicit justification of how the cross-entropy minimization follows from the mutual information maximization in the XGNN context. While the steps are ultimately correct, the presentation is compressed.

### Trivial

None.

## Nice-to-Haves

- Visual examples of extracted subgraphs from GMT vs. GSAT/LRI on datasets with known motifs (BA-2Motifs, MUTAG) would strengthen the qualitative case for improved interpretability.
- Evaluation on node-level tasks would broaden the claimed generality.
- Discussion of how the SubMT framework could extend beyond the independent Bernoulli edge model to more structured subgraph distributions (e.g., connected subgraph constraints) would deepen the theoretical contribution.

## Removed Points

These points from the reviewers were checked against the paper and removed:

- **"Missing baselines (CIGA, DGNN)"** — Per policy, this criticism cannot be verified without external sources and is removed.
- **"Tables are images; exact numbers not readable"** — This is a parser artifact; the original submission contains proper tables.
- **"Proofs deferred to appendix"** — The parser strips appendix content; proofs exist in the original submission.
- **"Simulated SubMT is confirmation by construction"** — This misreads the experiment: the simulation uses GSAT's attention weights to test whether they yield good SubMT estimates, which is a valid check.
- **"Proposition 3.3 claims general impossibility"** — The proposition specifically targets linear GNNs (Eq. 9); the paper's broader narrative is supported by empirical evidence.
- **Strength Finder strengths about the paper addressing important problems** — These generic endorsements add no specific content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define the interpretation AUC metric explicitly** in Section 6.1: specify whether it measures edge-level ROC AUC against ground-truth motif edges, and how ground truth is established for each dataset (including datasets like OGBG-MOLHIV where no explicit ground-truth subgraph exists). This single fix would substantially strengthen the empirical contribution.
2. **Refine the scope language** around Proposition 3.3 to distinguish between the formal result (linearized GNNs) and the broader empirical claim about non-linear architectures.
3. **Report inference-time costs** for GMT-sam at various sampling rounds to help readers assess the accuracy-efficiency trade-off.

## Score and Decision

The paper makes a genuine theoretical contribution by connecting XGNN expressivity to multilinear extension, identifies a real limitation of the attention-based paradigm, and proposes a well-motivated solution with consistent empirical support across diverse benchmarks. The weaknesses are real but addressable — the undefined AUC metric is the most significant, but it follows a field convention and does not invalidate the results. The paper would be strengthened by a revision that clarifies metrics and sharpens the theoretical scope claims, but its core contribution is solid.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>