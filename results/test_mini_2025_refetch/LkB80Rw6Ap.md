Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes Curvature-Constrained Message Passing (CCMP), a framework that modifies standard GNN message passing by restricting aggregation to edges of a specific curvature sign (positive or negative, based on Ollivier or Augmented Forman curvature). The paper also introduces a curvature-constrained homophily measure (β⁺, β⁻) that quantifies label agreement conditioned on edge curvature. Experiments on 11 datasets (7 heterophilic, 4 homophilic) with GCN and GAT backbones show that CCMP achieves substantial accuracy gains on heterophilic datasets (often 12–16 percentage points above the strongest rewiring baseline), while being competitive on homophilic data. The method is simple, architecture-agnostic, and comes with evidence that one-hop curvature variants increase the normalized spectral gap (5%–87%), suggesting over-squashing mitigation.

## Strengths

- **Novel curvature-constrained homophily measure.** Table 1 shows that β⁺ and β⁻ capture label-structure correlations that standard edge homophily misses. For Actor, β⁺ = 0.73 versus β = 0.32 (131% gain). This provides a principled lens for understanding when curvature-based messaging should help.

- **Consistent and large accuracy gains on heterophilic node classification.** On 6 out of 7 heterophilic datasets with both GCN and GAT backbones, at least one CCMP variant achieves the highest accuracy (Tables 4 and 5). The improvements are often substantial (e.g., Wisconsin with GCN: CCMP_A 67.80 vs. next-best SDRF 58.49; Cornell with GAT: CCMP_O 60.43 vs. FOSR 48.30). These results are averaged over 100 random 60/20/20 splits with standard deviations reported.

- **Architecture-agnostic design.** CCMP is formulated as a drop-in modification to the aggregation step (Equation 8) and is validated on two distinct backbones (GCN and GAT) with consistent gains, demonstrating generalizability.

- **Spectral gap evidence for over-squashing mitigation.** Section 4.4 reports that one-hop curvature increases the normalized spectral gap by 5%–87% on Squirrel, Actor, and Roman-Empire, which is a standard proxy for bottleneck removal in the rewiring literature (Topping et al. 2022, Karhadkar et al. 2023).

## Weaknesses

### Fatal
None.

### Major

1. **Configuration selection protocol is underspecified.** The paper reports per-dataset "optimal configurations" (Appendix A.3) — which combination of curvature sign (±), hop length (1/2/mixed), and per-layer assignment works best — but never states *how* these were selected. Were configurations chosen on a held-out validation split, via cross-validation, or by comparing all six variants on test data? The standard in this area (Pei et al. 2020, Platonov et al. 2023) uses a fixed 60/20/20 split with early stopping, but configuration selection is a distinct hyperparameter choice that requires a reproducible protocol. Without this clarification, the reported gains cannot be fully trusted as reflecting a genuine advantage rather than post-hoc configuration fitting. Given that the experiments use 100 random splits, the concern is ameliorated but not eliminated — the paper must specify whether configuration selection was performed per-split on the validation set or globally on test data.

2. **The over-squashing mitigation claim is only partially substantiated.** The paper claims CCMP "mitigates over-squashing" (Abstract, Conclusion) but the only experimental evidence is accuracy gains on node classification and a brief report of spectral gap increases (5%–87%) on three datasets. Accuracy improvements could equally stem from better handling of heterophily or reduced over-smoothing. The spectral gap is a standard proxy (linked to the Cheeger constant via Equation 3), so the claim is not unfounded, but it would be significantly strengthened by a direct over-squashing metric (e.g., influence scores measuring sensitivity to distant nodes, as in Topping et al. 2022). Without this, the central claim is asserted more strongly than the evidence supports.

### Minor

3. **The diameter claim for one-hop curvature is not supported.** Section 3.4 states that removing edges via one-hop curvature "drastically reduce[s] the diameter of the graph." Removing edges can increase rather than decrease the diameter (e.g., if bridging negative-curvature edges are removed, nodes in different communities become farther apart). No empirical evidence of diameter reduction is provided. The paper should either retract or substantiate this claim with measurements.

4. **No statistical significance tests.** On several datasets, CCMP's margin over the second-best baseline is modest (e.g., Squirrel with GCN: CCMP_A 54.79±0.31 vs. FOSR 52.63±0.30). The paper reports means and standard deviations over 100 runs, which is good practice, but a paired significance test (e.g., Wilcoxon) would clarify whether these differences are reliable.

5. **The curvature-constrained homophily measure is disconnected from the core algorithm.** β⁺ and β⁻ are introduced in Section 3.3 as a motivational tool but are not used to automatically select curvature sign, hop length, or configuration. The paper would be substantially stronger if this measure served a direct algorithmic role (e.g., "use positive curvature if β⁺ > β⁻, negative otherwise"), which would also address the configuration selection concern.

6. **Distinction from Ye et al. (2019) is not clearly articulated.** Ye et al. (2019) already apply Ollivier curvature in GNNs via attention weighting. The paper cites this work but does not explain why using curvature to *filter* edges (hard selection) is distinct from using it to *weight* them (soft selection). A brief comparison would help readers understand the novelty.

### Trivial
None.

## Nice-to-Haves

- A direct over-squashing analysis using influence scores on a subset of datasets (e.g., Squirrel, Actor, Roman-Empire) would significantly strengthen the paper's central claim.
- A systematic ablation showing performance of *all six* configurations per dataset with a validation-based selection rule (e.g., "always use negative curvature for heterophilic, positive for homophilic" or a β⁺/β⁻-based rule).
- Computational cost analysis including curvature precomputation time. Table 2 reports Ollivier curvature time (e.g., 836s on Squirrel) but the paper does not discuss whether the accuracy gain justifies this overhead for practitioners.

## Removed Points

- **"Missing comparison with heterophilic-specific GNNs (GPRGNN, H2GCN, LINKX)"**: The paper explicitly scopes its comparison to *graph rewiring methods* (DIGL, FA, SDRF, FOSR). Evaluating against architecture-level heterophilic GNNs addresses a different research question and is outside the paper's stated scope.
- **"FA/SDRF baselines are non-competitive"**: FA is a known, simple baseline that performs poorly in heterophilic settings; SDRF's >48h runtime on large datasets is a legitimate practical limitation. Including them as baselines is standard practice and does not bias the comparison.
- **"Reproducibility concerns about missing hyperparameters"**: The experimental setup (Section 4.3) specifies learning rate, dropout, weight decay, hidden dimensions, patience, and data splits. Standard details are provided. The configuration selection concern (kept above) is separate.
- **"Two-hop construction is vague"**: The description "following a chain of positively curved edges of size 2" (Figure 2 caption) is sufficiently clear for a standard GNN context. Multiple path handling and weighting are implicit in the adjacency matrix construction.
- **"Related work missing"**: Not verifiable without external sources per instructions.
- **Various formatting and presentation nitpicks**: Handled by the parsers.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's simple and elegant idea (filter message passing by curvature sign) and the experimental uncertainty introduced by dataset-specific configuration hand-picking. The curvature-constrained homophily measure is a genuinely useful diagnostic tool that reveals *why* the method works — on heterophilic datasets, β⁻ (negative-curvature homophily) is often higher than β (line 155), suggesting that negatively curved edges carry more label-consistent information. This insight could be turned into a self-tuning rule, which would transform the contribution from a set of good empirical results into a design principle. The reviewer contrast highlights that the paper's main weakness is not in its core idea (which is sound) but in how the experimental evidence is presented and defended — the missing validation protocol for configuration selection is the single bottleneck preventing this from being a stronger contribution.

## Suggestions

1. **Clarify the configuration selection protocol.** State explicitly whether configurations were chosen on the validation split across the 100 runs or tuned globally. If the latter, provide a validation-based selection rule (or show that a single rule works for all datasets).
2. **Add influence-score experiments on 2–3 heterophilic datasets** to directly substantiate the over-squashing claim that is currently supported only by spectral gap proxy and accuracy.
3. **Either retract or empirically support the diameter claim** in Section 3.4. Measure and report the diameter change for the one-hop variants on the datasets used.
4. **Consider integrating β⁺/β⁻ into an automated configuration rule**, e.g., "use positive curvature if β⁺ > β⁻, negative otherwise, 2-hop if the dataset is small." This would address both the disconnected homophily measure and the configuration selection concern simultaneously.

## Score and Decision

**Round 1 bracket [initial anchoring]**: Papers in the 3–3.5 range (Charge Dirichlet Energy, WISE-GNN, KAN for Graphs) are clearly weaker — they have poor results, unclear contributions, or major presentation issues. Papers in the 7.5–8 range (Joint Graph Rewiring and Feature Denoising) are substantially stronger — with theoretical grounding, joint optimization, and comprehensive evaluation. **Initial bracket: [4.0, 6.5]**.

**Round 2 narrowing**: Reading Spectro-Riemannian GNN (CUSP, avg 5.75, accepted poster), Probabilistically Rewired MPNN (PR-MPNN, avg 6.67, accepted poster), and Understanding Heterophily (avg 5.80, rejected) provides sharper anchors. CCMP is empirically stronger than Understanding Heterophily (rejected for limited novelty — CCMP has clearer novelty) and comparable in contribution level to CUSP (accepted — similar curvature focus, CCMP has larger empirical gains but less technical depth). CCMP is slightly weaker than PR-MPNN (accepted — had theoretical analysis and learned rewiring, but also more weaknesses). **Final score: 5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>