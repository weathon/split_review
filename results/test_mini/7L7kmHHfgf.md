Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (RGB + surface normals). It proposes three modules: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) using a GRU to update prototypes at test time, and Multimodal Normality Communication (MNC) exchanging normal cues across modalities via GAT alignment and cross-attention injection. Experiments on MVTec 3D-AD, Eyecandies, and Real-IAD D3 show consistent improvements over baselines, with 85% fewer FLOPs than the recent FIND baseline.

## Strengths

- **Consistent few-shot SOTA across multiple benchmarks.** On MVTec-3D-AD, PIRN outperforms the strongest baseline (INP-Former) by +3.9, +3.7, and +2.4 AUROC_I in 5-, 10-, and 50-shot settings, respectively (Table 1). Similar margins hold on Eyecandies. The paper evaluates on three datasets including the challenging Real-IAD D3.

- **Computational efficiency is genuinely impressive.** PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency — 85% fewer FLOPs and 4.35× faster than FIND (Table 4). This is rare for a prototype-based reconstruction method and is a practical advantage.

- **Module-level contribution is separately verifiable.** Table 3 confirms that RGB+SN (with MNC) consistently outperforms either modality alone across all shot settings (e.g., 0.922 vs. 0.827/0.879 at 10-shot). Table 7 validates that the balanced OT aggregation in APR outperforms global averaging and top-k averaging. These ablations provide evidence for core design choices.

- **Clear intuition and well-motivated design.** The three modules target distinct and well-articulated problems: BPA addresses codebook collapse in few-shot training, APR bridges train-test distribution shifts, and MNC provides cross-modal knowledge without dense alignment. The t-SNE visualization (Figure 1) directly illustrates BPA's effect.

## Weaknesses

### Major

- **No statistical significance for few-shot results.** Table 1 reports only point estimates with no standard deviations, confidence intervals, or number of random trials. Few-shot evaluation (randomly sampling K examples per class) has inherent variance, and the claimed +3–4 AUROC_I gains cannot be assessed for statistical reliability. This is the most consequential weakness because the paper's central contribution is few-shot performance. The same issue affects all ablation tables.

### Minor

- **Baselines not adapted for the few-shot regime.** The paper compares against M3DM, CFM, AST, 3D-ADNAS — all designed and evaluated in full-shot settings. There is no mention of tuning their hyperparameters (e.g., memory bank size, alignment loss weights) for few-shot. The paper does adapt INP-Former to a two-stream architecture, but analogous adaptations are not applied to multimodal baselines. While this is common practice, it makes the claimed "consistently superior" comparisons somewhat fragile.

- **Ablation study has an unexplained anomaly.** Table 2 shows an intermediate configuration achieving 0.967 AUROC_I, which is higher than the full model's 0.922. The paper's claim that "removing each component from the full model results in a consistent performance drop" cannot explain why an ablated configuration outperforms the full model. This needs clarification. (Note: the table header has a typo — *BFA* should be *BPA* — and the parser garbles the checkmark pattern, but the numeric inconsistency is real.)

- **Key hyperparameter decisions lack justification for the few-shot setting.** The prototype count K=10 and decoder depth L=2 are ablated only in the all-shot setting (K, Table 5) or 10-shot setting (L, Table 6), not in the most challenging 5-shot regime where optimal values could differ. The KNN graph in MNC uses an unspecified number of neighbors with only 10 prototypes per modality, and the stability of this graph under few-shot data is not analyzed.

- **The APR anomaly-robustness claim is not directly measured.** The paper states that anomalous tokens "tend to be assigned more diffusely across prototypes" and that the GRU gating "restricts the integration of unreliable anomalous contexts," but neither claim is empirically verified. A controlled experiment with synthetic anomalies at varying severity would strengthen this.

- **The training loss is underspecified.** The paper says it uses "a soft mining loss (Luo et al., 2025), e.g., cosine distance" without specifying the exact formulation. Given that the loss is central to training, this is a reproducibility gap.

- **Abstract overstates relative to the full-shot Real-IAD result.** PIRN achieves AUROC_J=0.873 on Real-IAD D3, second to D^3M's 0.890 (Table 8). The paper acknowledges D^3M uses three modalities vs. PIRN's two, but the abstract's claim of "consistently achieving superior performance" should be qualified to clearly separate few-shot and full-shot settings.

### Trivial

- Table 2 header has a typo: "BFA" should be "BPA."
- The paper does not specify the number of neighbors k used in the MNC graph construction (Stage 1).

## Nice-to-Haves

- Break down MNC's two stages separately in the ablation (Stage 1 prototype alignment vs. Stage 2 cross-attention injection).
- Ablate the uniform constraint in BPA against entropic regularization alone.
- Include FIND in the main few-shot comparison (Table 1) if possible, since it is cited as SOTA.
- Release code and preprocessed surface-normal maps to improve reproducibility.

## Removed Points

- **Criticism about missing related work on few-shot AD:** Per instructions, I cannot verify the existence of missing references and must not mention them.
- **Criticism about typos/formatting:** The garbled checkmarks in Table 2 and the "BFA" typo are parser artifacts from extraction, not author errors. However, the numeric anomaly (0.967 > 0.922) is a real issue I have kept.
- **Criticism about the problem statement lacking independent evidence:** The paper cites prior work (CFM, LSFA, M3DM, SG-DM) in the introduction and related work to establish the failure modes of existing methods. This is adequate for a paper of this type.
- **Criticism that FIND comparison is "cherry-picked":** The efficiency comparison (Table 4) includes M3DM and CFM alongside FIND, which is a reasonable set of baselines. FIND is included because it is the most recent SOTA; its omission from Table 1 is noted as a minor concern, not cherry-picking.
- **Criticism about testing on K=1,2:** This is scope creep beyond the paper's stated few-shot settings (5/10/50).
- **Requests for video MAD or multi-view experiments:** Outside the stated scope. Mentioned above as nice-to-have.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report mean and std over at least 5 random seeds for all few-shot results.** This is the single most important revision. Without it, the core claim of superiority in few-shot settings rests on unquantified point estimates.
2. **Clarify the Table 2 ablation anomaly.** Explain why an intermediate configuration (0.967) outperforms the full model (0.922), or provide the correct numbers.
3. **Tune or at least discuss hyperparameter choices for baselines in the few-shot regime.** If tuning is infeasible, add a simple nearest-neighbor-on-frozen-features baseline with tuned k as a sanity check.
4. **Specify the exact loss formulation** instead of deferring to a citation.
5. **Qualify the abstract** to separate few-shot claims from full-shot performance.

## Score and Decision

**Calibration Anchors** (all from the human review corpus):

| Path | Avg Score | Comparison to PIRN |
|------|-----------|-------------------|
| FoundAD (YRrlJ8oVEH.md) | 6.00 | Stronger: simpler method, cleaner ablation, accepted as poster. PIRN has more extensive multi-dataset evaluation but lacks error bars. |
| Two-Layer Conv AE Theory (FnbGlnKbIU.md) | 5.50 | Comparable quality: theoretical paper with limited experiments vs. PIRN's empirical breadth. Both have notable limitations for their respective types. |
| DCR^2-AD (qqlWHIjJ24.md) | 5.00 | Comparable: both have methodological contributions undermined by missing experiments. PIRN's evaluation is broader. |
| MultiMisD (E0udlUz8wQ.md) | 4.00 | Weaker: flawed methodology core. PIRN's approach is better motivated and more sound. |
| SD-MAD (0wJuW3snwU.md) | 4.00 | Weaker: similar missing-experiment issues but less extensive evaluation than PIRN. |
| DPNR (iO9CRytDvf.md) | 2.00 | Much weaker: factual inaccuracies, missing results. PIRN is clearly stronger. |

PIRN is positioned between the 4.0-level papers (which have more fundamental issues) and the 5.5–6.0 papers (which have cleaner experimental evidence). The missing error bars for the core few-shot claim are the main factor holding it back. It has real contributions and broad evaluation, but the lack of statistical rigor means the central claim is not fully established.

**Score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>