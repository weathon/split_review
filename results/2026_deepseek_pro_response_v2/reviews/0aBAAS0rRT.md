Now I have sufficient calibration. Let me synthesize my final assessment.

**Calibration comparison:**

| Anchor | Score | Comparison to SigMap |
|--------|-------|---------------------|
| Wi-GATr (9TClCDZXeh) | 7.00 | SigMap is weaker — Wi-GATr has cleaner methodology and better-specified components |
| EM-GANSim (29JDZxRgPZ) | 6.00 | SigMap is weaker — similar novelty level but SigMap has structural overclaim and missing mechanism descriptions |
| FS-SINR (QaQrWKPWdG) | 5.75 | SigMap is weaker — FS-SINR has cleaner methodology (its main weakness is limited novelty) |
| MLO-MAE (oVZ9XaOSFK) | 4.40 | SigMap is stronger — more genuine novelty and better empirical validation |
| Sound source localization (S2WUJUETyc) | 4.00 | SigMap is stronger — more substantive contributions |

SigMap has genuine novelty (map-as-prompt, cycle-adaptive masking) and good empirical results, but is held back by: (1) zero-shot overclaim in abstract/contributions contradicted by few-shot protocol, (2) missing methodological description of the NLoS-aware attention mechanism identified as "the key advantage," and (3) under-specified cycle-adaptive masking. These structural issues place it below FS-SINR (5.75) but above MLO-MAE (4.40). **Final score: 5.0.**

---

## Summary

This paper proposes SigMap, a two-stage wireless localization framework combining cycle-adaptive masked autoencoding for self-supervised CSI pre-training with geographic prompt tuning that encodes 3D building geometry into soft prompt tokens via GNNs. The model is pre-trained on DeepMIMO O1_3p5 and fine-tuned on downstream localization tasks with a frozen backbone. Results show strong performance on single-BS and multi-BS localization, with few-shot generalization to unseen environments (DeepMIMO O2, WAIR-D).

## Strengths

- **Well-specified geographic prompt generation pipeline**: Section 3.4 and Algorithm 1 provide a concrete, end-to-end procedure for transforming 3D geographic data (building vertices, BS positions) into prompt tokens via Delaunay triangulation, GNN processing, global pooling, and projection. This is more detailed than prior work that merely mentions incorporating map data.

- **Clean map prompt ablation**: Table 4 (Section 4.4) provides a graded ablation across 3D mesh (1.564m MAE), 2D bird's-eye (1.692m MAE), and no-map (2.275m MAE) on single-BS localization. The 8% degradation from 3D to 2D versus the 31% gap from 2D to no-map cleanly demonstrates that most benefit comes from topological/LoS cues.

- **Cross-scenario generalization results**: Table 4.5 evaluates on two entirely held-out environments (DeepMIMO O2, WAIR-D with 100 real-world city scenes) using only ~100 fine-tuning samples per scenario with a frozen backbone. SIGMAP achieves 1.026m MAE on O2 and 1.880m on WAIR-D, substantially outperforming LWLM.

- **Cycle-adaptive masking ablation**: Table 3 compares adaptive masking (0.673m MAE, 84.5% CDF@1m) against grid-only (0.770m, 80.3%) and strip-only (0.753m, 75.3%), providing direct evidence that dynamic periodicity-aware masks improve learned representations.

- **Parameter efficiency quantified**: Table 5 reports 0.085M trainable parameters (0.7% of 11.73M total), 30-minute fine-tuning, and 0.83ms inference per sample — demonstrating practical deployability.

- **Well-specified multi-BS attention fusion**: Equations 9–10 in Section 3.5 formalize an attention-weighted fusion over per-BS [CLS] tokens, a principled extension beyond simple averaging.

## Weaknesses

### Fatal
None.

### Major

- **"Zero-shot" claim contradicted by experimental protocol**: The abstract (line 9) and contributions (Section 1.2, line 43) claim "strong zero-shot generalization in unseen environments." However, Section 4.5 (line 317) explicitly describes the protocol as "This few-shot learning setup" with "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)." Fine-tuning on 100 labeled examples is few-shot adaptation, not zero-shot generalization. The headline claim in the abstract and contribution list is directly contradicted by the paper's own experimental description. The few-shot results themselves are valuable, but the abstract and contributions must be rewritten to match what was actually tested.

- **NLoS-aware attention mechanism (Equation 11) has no methodological description**: Section 4.2 introduces Eq 11 and states "The key advantage stems from our NLoS-aware attention mechanism." This equation — with undefined symbols `o_s^(i)`, `W_NLoS`, and `φ` — appears only in the results section. Section 3 (Methodology) contains no corresponding description of what this mechanism operates on, how it is trained, or how it relates to the transformer backbone or geographic prompt. A component identified as the primary performance driver is absent from the methodological description, making this aspect unreproducible.

- **Cycle-adaptive masking is under-specified**: The computation of `d_final` — the periodicity shift that makes the masking "cycle-adaptive" — is described only as "comput[ing] row-wise cross-correlation" (Section 1.2, line 41; Section 3.3, line 133). No algorithm, formula, or implementation procedure is provided. The dimensionality of the cross-correlation (over which CSI axis?), the method for selecting dominant periodicities, and handling of multiple detected periods are all unspecified. Since `d_final` is the parameter that distinguishes adaptive masking from fixed masking, this under-specification prevents independent reproduction of the paper's primary methodological contribution.

### Minor

- **Numerical inconsistency in generalization results**: Table 4.5 reports SIGMAP (w/map) MAE as 1.880m on WAIR-D Scenario-2, but the prose (line 340) states "1.580 m on WAIR-D Scenario-2." These values differ by 0.3m (16%), which is larger than the reported improvement over SIGMAP (w/o map). The reader cannot determine which number is correct.

- **Generalization experiments compare only against LWLM**: Section 4.5 drops CNN, SWiT, and OMP baselines that appear in the main results (Tables 1–2). Without these comparisons, the reader cannot assess whether SIGMAP's cross-scenario advantage is genuine or whether LWLM is simply a weak baseline for transfer (its RMSE degrades from 5.822m in-domain to 11.837m on O2).

- **NLoS-aware attention mechanism is never ablated**: Table 3 ablates masking strategies and Table 4 ablates map modalities, but neither isolates the contribution of the NLoS-aware attention mechanism from Eq 11. Since the paper identifies this as "the key advantage," its contribution should be separately quantified.

- **GCN formulation mismatch**: Algorithm 1 line 7 uses separate weight matrices W^(l) (self) and U^(l) (neighbor) with unnormalized summation, while the prose GCN equation (line 189) uses the standard normalized adjacency formulation with a single weight matrix. The paper uses both without clarifying which is implemented.

- **Pre-training scope is narrow for "foundation model" framing**: Pre-training on a single simulated scenario (DeepMIMO O1_3p5) is a narrow base for the "foundation model" label. The framing should be tempered or the limitation explicitly acknowledged.

### Trivial

- **Figure reference error**: Section 4.4 refers to "Figure 1" for the 2D/3D side-by-side visualization, but Figure 1 is the propagation paths diagram.

## Nice-to-Haves

- A qualitative analysis connecting geographic prompt attention patterns to building geometries would substantiate the "interpretable fusion" claim, which currently rests entirely on ablation numbers.
- Standard deviations in result tables (especially for the generalization experiments with only 100 samples) would help assess statistical reliability.
- The RMSE discrepancy in Table 1 (SIGMAP w/map: 5.675m vs. LWLM: 5.822m, despite a 34% MAE gap) suggests a different error distribution worth discussing.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's demand for multi-scenario pre-training**: Requiring multi-scenario pre-training is scope creep. The paper's contribution is the method itself; single-scenario pre-training is a limitation (retained as Minor) but not a fatal flaw.

- **Harsh critic's claim about 1000-epoch fine-tuning being "excessive"**: Given that fine-tuning takes only 30 minutes total (1.8s/epoch) and updates only 0.7% of parameters, the epoch count is not a meaningful concern. Removed.

- **Strength Finder's "strong baselines" in generalization**: Only LWLM is compared in Section 4.5. The generalization results are still a strength but the baseline claim is overstated. The strength is retained with appropriate qualification.

- **Pure formatting/style nitpicks**: Removed per hard rules.

- **Harsh critic's claim that the zero-shot issue is "categorically false" and "structural" at the fatal level**: While the contradiction is real, the few-shot adaptation results remain valid and valuable. The issue is an overclaim in framing, not a methodological invalidation of the results. Classified as Major rather than Fatal.

## Novel Insights

The reviewers' critiques converge on an important observation about the paper's architecture: the geographic prompt pipeline (Algorithm 1) and the NLoS-aware attention mechanism (Eq 11) appear to be two separate ways of incorporating environmental information, but their relationship is never clarified. Eq 11 seems to operate on per-path representations (`o_s^(i)`) to weight NLoS vs. LoS contributions, while the geographic prompt encodes building geometry into a single token. Understanding whether these mechanisms are complementary, redundant, or intended to model different aspects of the environment would substantially clarify the method's design rationale. The paper's strongest empirical signal — that 2D topology captures most of the 3D map benefit (Table 4) — independently supports the intuition that LoS/NLoS reasoning is the primary mechanism, but the paper does not connect this ablation result to the Eq 11 mechanism.

## Suggestions

- Replace "zero-shot generalization" with "few-shot generalization" or "parameter-efficient cross-scenario adaptation" throughout the abstract, contributions, and conclusion to match the experimental protocol.
- Move the NLoS-aware attention mechanism (Eq 11) to Section 3 with full notation definitions, and add a row to Table 3 or a new ablation isolating its contribution.
- Provide the full cross-correlation procedure for computing `d_final`: over which CSI dimensions, with what window, and using what peak-selection criterion. An ablation with a deliberately wrong periodicity would directly test whether adaptivity matters.
- Resolve the 1.880m vs. 1.580m inconsistency in the WAIR-D result.
- Add CNN and SWiT baselines to the generalization experiments, or explain why they are omitted.
- Clarify whether Algorithm 1 line 7 or the normalized adjacency GCN (line 189) is the implemented formulation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>