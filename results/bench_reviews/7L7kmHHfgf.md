Now let me write the consolidated review.

---

## Summary

This paper proposes PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection that uses RGB and surface-normal modalities. The framework introduces three components: Balanced Prototype Assignment (BPA) via optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) for test-time prototype adaptation, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange. The method achieves strong results on MVTec-3D-AD and Eyecandies benchmarks under few-shot settings, with solid ablation studies validating most components.

## Strengths

- **BPA effectively mitigates codebook collapse via optimal transport**: The t-SNE visualization (Fig. 1, right) and ablation (Table 9) demonstrate that the balanced OT assignment produces a more uniform prototype distribution than softmax alternatives. Removing BPA causes a substantial AUROC_I drop (~0.039 in Table 2), confirming its role in preserving diverse normal patterns under limited data.

- **MNC provides meaningful cross-modal gains**: Table 3 shows that combining RGB and surface-normal modalities via MNC yields significant improvements over single-modality baselines (e.g., 5-shot AUROC_I 0.890 fused vs. 0.794 RGB-only on MVTec-3D-AD). The ablation in Table 2 confirms a ~0.055 AUROC_I drop when MNC is removed, validating the contribution of prototype-level cross-modal exchange.

- **Consistent few-shot improvement across benchmarks**: Table 1 shows PIRN outperforms all listed baselines on MVTec-3D-AD and Eyecandies across 5-, 10-, and 50-shot settings, with gains of +3.9, +3.7, and +2.4 AUROC_I respectively over the strongest baseline on MVTec-3D-AD.

- **Strong computational efficiency**: Table 4 demonstrates that PIRN achieves its best performance with 103.36G FLOPs and 17.49ms latency — approximately 85% fewer FLOPs and 4.35× faster than FIND, the prior SOTA.

- **Prototype-driven reconstruction yields interpretable anomaly discrimination**: Fig. 4 visualizes feature displacement through the reconstruction pipeline, showing that normal tokens undergo only small shifts near prototype clusters while anomalous tokens require large displacements, corroborating the information-bottleneck design.

- **Comprehensive ablation studies**: The paper ablates each core component (BPA, APR, MNC), codebook size, decoder depth, backbone choice, and assignment strategies, providing a clear picture of each design choice's contribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **FIND omitted from the main few-shot comparison (Table 1)**: The paper identifies FIND (Li et al., 2025) as the current state-of-the-art, reporting its 10-shot AUROC_I of 0.921 on MVTec-3D-AD (Table 4). Yet FIND is absent from Table 1 — the paper's primary few-shot results table — where it would be the most relevant comparator. FIND is included in the efficiency comparison (Table 4), which shows PIRN edges it out by only 0.001 (0.922 vs. 0.921). Including FIND in Table 1 would give a more honest picture of the performance margin and would not undermine the paper's contribution, since PIRN still holds advantages in efficiency and in the 50-shot regime.

- **APR claims overstated relative to empirical contribution**: The paper presents APR as a key innovation for bridging the train–test distribution gap and preventing prototype corruption. However, the ablation in Table 2 shows that removing APR drops AUROC_I from 0.922 to only 0.916 — a marginal 0.006 improvement. While the mechanism (OT-weighted context + GRU gating) is technically sound, the claim that the GRU "restricts the integration of unreliable anomalous contexts" relies on the assumption that the GRU, trained only on normal data, will close its gate on out-of-distribution contexts. The paper provides no quantitative validation of this behavior (e.g., measuring prototype drift on normal vs. anomalous test samples). The qualitative Fig. 6 provides some support, but the gap between the strong narrative claims and the modest ablation gain should be acknowledged.

- **No statistical validation for few-shot results**: Table 1 reports single-run metrics. In few-shot regimes, the specific samples chosen for training can substantially affect outcomes. Reporting mean ± std over multiple random draws (≥5) would establish whether the reported improvements are statistically reliable. This is a common expectation for few-shot evaluations, though not universally practiced in the anomaly detection literature.

- **Few-shot protocol details not described**: The paper does not specify how few-shot training splits were constructed (random seed, number of repeats, whether any hyperparameter tuning or validation was performed using test-set knowledge). This impairs reproducibility.

### Trivial

- Several implementation details are not specified: the number of KNN neighbors in the MNC graph, the number of GAT heads, and how the learnable gating scalars (γ_rgb, γ_sn) are initialized.

## Nice-to-Haves

- Evaluating PIRN on few-shot Real-IAD D3 (currently only reported in the full-shot setting) would strengthen the few-shot narrative.

- Investigating dynamic codebook sizes per object category and whether the uniform-mass assumption in BPA should adapt to category-specific pattern diversity could be a productive direction.

- A direct empirical test of APR's robustness (measuring prototype vector change before/after APR on normal vs. anomalous test images) would substantiate the claimed mechanism.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic point about "missing statistical validation" treated as a fatal flaw**: Moved to Minor. While important, this is not a fatal error — it's a common limitation in the anomaly detection literature, and the performance margins are large enough that the overall trend is unlikely to reverse under multiple runs. The anchor paper FoundAD (score 6.0, accepted) had similar concerns raised about its few-shot protocol without being rejected.

- **Harsh Critic claim that APR's mechanism is "entirely unsupported"**: Softened. The paper provides a two-layer argument (OT weighting + GRU gating) and the GRU discussion in Appendix B.1 gives a technically reasonable explanation. The real issue is the gap between the strong claims and the modest empirical gain, not that the mechanism is nonsensical.

- **Harsh Critic claim about BTF baseline adaptation disadvantage**: Not substantiated. BTF (Horwitz & Hoshen, 2023) is not purely 3D — it uses both RGB and 3D features. The paper doesn't describe the exact adaptation procedure, but this is a minor documentation gap, not evidence of unfair comparison.

- **Strength Finder claim about APR "closing train-test distribution gap"**: Kept but qualified — the ablation supports a real but modest contribution. The original strength overstated the evidence.

- **Strength Finder generic claims**: Removed generic statements about "the problem being important" — these are not concrete strengths.

- **Grammar/typo/formatting complaints**: Removed per instructions — these are parser artifacts, not author errors.

- **Missing related works complaint**: Removed per instructions.

- **"Missing appendix/proofs" or "absent references" complaints**: Removed per instructions — the appendix is stripped by the parser.

## Novel Insights

The integration of balanced optimal transport for prototype assignment in multimodal anomaly detection is genuinely novel. Unlike prior prototype-based AD methods that treat modalities separately, PIRN shows that forcing uniform prototype utilization through OT not only prevents codebook collapse but naturally creates a foundation for cross-modal communication — balanced prototypes provide stable anchors that make graph-based alignment and cross-attention injection more effective. The ablation pattern (BPA contributing ~0.039, MNC contributing ~0.055, and APR contributing only ~0.006) reveals that the prototype utilization strategy matters more than the test-time adaptation gating for this task, which is an insight the paper could draw out more explicitly.

## Suggestions

- Include FIND in Table 1 for transparency. The near-identical performance at 10-shot (0.922 vs. 0.921) does not diminish PIRN's contribution — the efficiency advantage and better 50-shot performance remain compelling.

- Run the few-shot experiments over multiple random draws (≥5) and report mean ± std in a revised Table 1 or appendix. This would directly address the most persistent concern about result reliability.

- Either provide quantitative validation of APR's claimed robustness (prototype drift measurements) or modestly reframe the APR narrative to match its empirical contribution — acknowledging it as a helpful but secondary component rather than a key pillar.

- Specify the missing implementation details (KNN neighbors, GAT heads, gating scalar initialization) in the main text or appendix.

## Score and Decision

**Anchor paper comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/Mam9PS8ENb.md` (UIP-AD, avg 4.00, Reject): Similar topical area (multimodal anomaly detection with prototypes). PIRN is substantially stronger — it has comprehensive ablations for every component, clear technical motivation, and efficiency analysis that UIP-AD lacked. PIRN's weaknesses are more about presentation and validation rigor rather than missing core ablations.

- `/home/wg25r/review_agent/human_reviews_2026/YRrlJ8oVEH.md` (FoundAD, avg 6.00, Accept/Poster): Few-shot anomaly detection with foundation encoders. FoundAD is conceptually simpler and cleaner, with strong results. PIRN has more technical depth (three novel components) and more comprehensive ablations, but FoundAD has fewer presentation issues and no "missing SOTA from main table" concern. PIRN is slightly below FoundAD in execution polish.

- `/home/wg25r/review_agent/human_reviews_2026/TQkFiW3AEX.md` (MRAD, avg 6.00, Accept/Poster): Zero-shot anomaly detection with memory retrieval. MRAD had missing latency/variance studies as weaknesses but was still accepted. PIRN has more comprehensive ablations but the FIND omission issue.

- `/home/wg25r/review_agent/human_reviews_2026/ny5Jrfhy61.md` (TokenCLIP, avg 5.50, Reject): OT-based token alignment for anomaly detection. TokenCLIP suffered from unclear implementation details and sensitivity analysis. PIRN has similar presentation gaps (missing protocol details, missing FIND from main table) but stronger empirical grounding through ablations. Comparable quality.

- `/home/wg25r/review_agent/human_reviews_2026/qqlWHIjJ24.md` (DCR^2-AD, avg 5.00, Reject): MLLM-based anomaly reasoning. PIRN is stronger in technical contribution and empirical validation.

- `/home/wg25r/review_agent/human_reviews_2026/iO9CRytDvf.md` (DPNR, avg 2.00, Reject): Prototype-based anomaly detection with weak experiments. PIRN is far superior in experimental rigor.

- `/home/wg25r/review_agent/human_reviews_2026/OXOGZxjCsN.md` (MAD, avg 4.00, Reject): Multimodal anomaly detection for manufacturing. PIRN is stronger in novelty and empirical scope.

- `/home/wg25r/review_agent/human_reviews_2026/CtcKEAojoE.md` (ProtoMM, avg 4.00, Reject): Shared prototypes for multimodal biosignals. Different domain, but PIRN has better ablations and clearer technical contributions.

- `/home/wg25r/review_agent/human_reviews_2026/J9VRPrhwjM.md` (SteelNet, avg 2.00, Reject): Multimodal industrial representation learning. PIRN is substantially stronger.

PIRN sits between the 4.00 rejected papers (UIP-AD, MAD) and the 6.00 accepted papers (FoundAD, MRAD). It has stronger technical contributions and more comprehensive experiments than the 4.00-5.00 tier, but has presentation and validation issues (FIND omission, overstated APR claims, missing statistical validation) that prevent it from reaching the clean acceptance level of the 6.00 tier. It is most comparable to TokenCLIP (5.50) in overall quality but with better ablations. I assign 5.5.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>