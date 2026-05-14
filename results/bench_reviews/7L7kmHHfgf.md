Now I have a complete picture. Let me produce the final consolidated review.

---

## Summary

PIRN proposes a prototype-based reconstruction framework for few-shot multimodal (RGB + 3D surface normals) anomaly detection. It introduces three components: (1) Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, (2) Adaptive Prototype Refinement (APR) for test-time prototype adaptation via GRU gating, and (3) Multimodal Normality Communication (MNC) that exchanges normalcy knowledge across modalities through graph-aligned cross-attention. Evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3, PIRN demonstrates consistent improvements over existing baselines under few-shot settings.

## Strengths

- **Consistent SOTA few-shot performance**: PIRN achieves substantial AUROC_I gains over the best baseline across MVTec-3D-AD (+3.9 at 5-shot, +3.7 at 10-shot, +2.4 at 50-shot) and Eyecandies (+3.6 to +4.0), as shown in Table 1. These gains are consistent across all shot settings and metrics, not cherry-picked.

- **Well-motivated architectural design**: Each component addresses a clearly identified failure mode of existing approaches: BPA tackles codebook collapse from softmax assignment (validated via t-SNE visualization in Fig. 1 Right), APR addresses the train-test distribution gap under scarce data, and MNC enables cross-modal knowledge transfer without unreliable dense patch-to-patch alignment. The design follows a logical progression from intra-modal to cross-modal constraints.

- **Strong computational efficiency**: Table 4 shows PIRN achieves the best AUROC_I (0.922) on 10-shot MVTec-3D-AD while requiring only 103.36G FLOPs and 17.49ms latency — ~85% fewer FLOPs and 4.35× faster than FIND, the previous SOTA. This makes the method genuinely practical for deployment.

- **Thorough ablation coverage**: The paper evaluates prototype count (Table 5), decoder depth (Table 6), token aggregation strategies in APR (Table 7), prototype assignment methods (Table 9), and backbone variants (Table 10), providing reasonable evidence for most design choices.

- **Generalization to real-world data**: On the challenging Real-IAD D3 benchmark (Table 8), PIRN achieves best pixel-level localization (AUROC_P 0.961) using only two modalities, outperforming tri-modal methods in several categories.

- **Complementary modality analysis**: Table 3 shows surface normals outperform RGB alone, and the fusion gain is largest at 5-shot (where individual modalities are most starved), directly supporting the paper's claim that cross-modal communication matters most under extreme data scarcity.

## Weaknesses

### Fatal

None.

### Major

- **FIND omitted from main benchmark tables**. FIND (Li et al., 2025) is the most directly comparable recent few-shot multimodal method and is acknowledged as SOTA. It appears only in the efficiency table (Table 4, one shot setting), not in the main results (Table 1, all shot settings) or Real-IAD (Table 8). Table 4 does show PIRN edges FIND (0.922 vs 0.921) on 10-shot MVTec-3D-AD, which partially mitigates the concern. However, the absence of FIND across the full range of shot settings and on Eyecandies means the paper does not fully establish its margin over the most relevant competitor. This can be addressed in rebuttal.

### Minor

- **No variance reporting in few-shot experiments**. The few-shot protocol involves random selection of a small number of normal training samples, yet no standard deviations, confidence intervals, or number of random seeds are reported. While many papers in this subfield similarly omit variance, the very small gains in some ablations (e.g., APR contributing +0.006 AUROC_I in Table 2; balanced OT vs top-k only +0.001 in Table 7) would benefit from statistical context. This does not invalidate the main results but weakens confidence in marginal improvements.

- **Ablation table (Table 2) does not cleanly isolate each component**. The table reports only 5 of 8 possible factorial combinations for the three binary components. Crucially, the row for {BPA=✓, APR=✓, MNC=✗} is absent, making it impossible to directly read off MNC's contribution over a model that already has both BPA and APR. The paper's textual claim that "removing each component from the full model results in a consistent performance drop" cannot be verified from the table as presented. A full 2³ factorial ablation would strengthen the paper substantially.

- **APR's gating against anomalous context is not quantitatively validated**. The paper argues that the GRU update gate prevents prototype corruption by anomalous patches, and Appendix B.1 describes the mechanism. However, there is no ablation comparing the GRU-based update against a simpler non-gated alternative (e.g., weighted average), and no experiment measuring prototype drift under anomalous inputs. The qualitative evidence (Fig. 6) is suggestive but not conclusive. This remains a design claim rather than an empirically demonstrated property.

- **No failure case discussion**. The paper presents only successful detection examples. A discussion of where PIRN still fails — e.g., anomaly types that are well-reconstructed by the prototypes, categories where performance is below baselines — would delineate the method's limitations and better serve the community.

### Trivial

- **Missing hyperparameter details for MNC components**: the number of KNN neighbors for the graph, number of GAT heads, and whether prototypes are ℓ₂-normalized before graph construction are not specified. The Sinkhorn entropic regularization strength ε is mentioned conceptually but its value is never stated.

- **The gating scalars g_rgb, g_sn introduced in Eq. (4)**: their final learned values across layers are not reported. While the paper's claim does not hinge on these values, reporting them would help readers understand the MNC module's behavior.

## Nice-to-Haves

- A comparison of MNC with a simpler alternative (e.g., cross-attention without the graph-alignment stage, or direct prototype concatenation) would strengthen the claim that the two-stage design is necessary.
- Reporting learned gating values across layers would help verify that the MNC module is actively contributing rather than being gated to near-zero.
- Extending FIND to Table 1 and Table 8 across all shot settings would fully close the comparison gap.
- Measuring prototype drift under controlled anomalous inputs would convert the APR robustness claim from design intent to empirically validated property.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"MNC contributes negligibly (+0.006)"**: This claim from the harsh critic compares the {BPA=✗, APR=✓, MNC=✗} row (0.916) to the full model {BPA=✓, APR=✓, MNC=✓} (0.922). The +0.006 difference conflates the addition of both BPA and MNC, not MNC alone. This is a misreading of Table 2 and does not reflect the paper's actual ablation. **Removed.**

- **"GRU training not described"**: The paper states (line 425) that PIRN is trained end-to-end with an intra-modal reconstruction loss, and Appendix B.1 provides the full GRU equations and gating mechanism description. The training regime is adequately described. **Removed.**

- **"Gating scalars could simply be zero, making MNC inactive"**: Pure speculation without evidence. The paper reports that MNC contributes to performance; if the gates were zero, MNC would have no effect and the ablation would not show any difference. **Removed.**

- **"Figure 1 (left) misleadingly plots PIRN's performance"**: I cannot verify the figure's content from the extracted text alone. The paper text describes it as a comparison with SOTA methods on the Eyecandies dataset. This is an unverifiable visual critique. **Removed.**

- **Strength finder: "MNC provides the largest cross-modal benefit (0.922 to 0.867 drop)"**: The claimed drop conflates MNC removal with BPA removal in Table 2. The actual isolated contribution of MNC cannot be cleanly read from the table as presented. This specific numeric claim is unreliable. **Removed.**

- **Strength finder: "APR enables robust test-time adaptation" with +0.006 gain**: The +0.006 gain is small and the Table 2 reading conflates components. While APR has qualitative support (Fig. 4, 6), the quantitative evidence is ambiguous. **Weakened in main review.**

## Novel Insights

The paper's most interesting empirical finding is that surface-normal features alone substantially outperform RGB features for anomaly detection (0.879 vs 0.827 AUROC_I at 10-shot, Table 3), and that the cross-modal fusion gain is inversely proportional to the amount of training data — largest at 5-shot where individual modalities suffer most from underrepresentation. This suggests prototype-level cross-modal knowledge transfer is not merely additive but serves a compensatory role when per-modality coverage is thin, a dynamic that goes beyond simple late fusion. This pattern, if robust, has implications for when multimodal architectures are truly worth their added complexity in data-scarce regimes.

## Suggestions

- Add FIND to Table 1 (all shot settings) and Table 8. This is the highest-impact change the authors can make and is feasible within a rebuttal period.
- Report at minimum the standard deviation over 3–5 random seeds for the few-shot settings, at least for the final model and the strongest baseline.
- Present a complete 2³ ablation in Table 2 showing all eight {BPA, APR, MNC} combinations, or clearly state which reference model is used for each "removal" comparison.
- Include one quantitative experiment on APR robustness: e.g., inject synthetic anomalies into normal test images and measure prototype drift with vs. without the GRU gating, or ablate the GRU against a simple weighted-average update.

## Score and Decision

### Anchor comparison:

| Path | Avg Score | Comparison to PIRN |
|------|-----------|---------------------|
| `/home/wg25r/review_agent/human_reviews_2026/Mam9PS8ENb.md` (UIP-AD) | 4.00 | Similar topic (multimodal AD with prototypes) but weaker: missing core ablations, missing baselines, rejected. PIRN has substantially more thorough experiments and clearer contributions. |
| `/home/wg25r/review_agent/human_reviews_2026/iO9CRytDvf.md` (DPNR) | 2.00 | Very weak prototype-based AD paper with factual errors and missing results. PIRN is far stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/tRO6G20Qba.md` (D²4FAD) | 5.00 | Few-shot anomaly detection (medical). Accept poster. PIRN has more architectural novelty, more benchmarks, and better ablations. |
| `/home/wg25r/review_agent/human_reviews_2026/ny5Jrfhy61.md` (TokenCLIP) | 5.50 | Zero-shot AD with OT. Strong results but rejected due to unclear OT mechanism and missing sensitivity analysis. PIRN is more complete experimentally. |
| `/home/wg25r/review_agent/human_reviews_2026/fNFbGqu6Rg.md` (MindTS) | 5.50 | Multimodal time series AD. Accept poster. PIRN has comparable novelty and better efficiency analysis. |
| `/home/wg25r/review_agent/human_reviews_2026/YRrlJ8oVEH.md` (FoundAD) | 6.00 | Few-shot AD with foundation encoders. Accept poster. Simple but effective. PIRN has more methodological depth (3 novel components vs 1), multimodal scope, and comparable empirical strength. |
| `/home/wg25r/review_agent/human_reviews_2026/yKDqg9HwZX.md` (MetaEmbed) | 7.00 | Multimodal retrieval. Accept oral. Different subfield, not directly comparable. |

PIRN is clearly stronger than the 4.0–5.5 band (UIP-AD, DPNR, D²4FAD, TokenCLIP, MindTS). It is comparable to FoundAD (6.0) in empirical rigor and exceeds it in methodological novelty and multimodal scope, but has a notable weakness (FIND omission from main tables) that FoundAD did not have in its baseline coverage. PIRN does not reach the 7.0 band represented by MetaEmbed (oral-quality work in a different subfield with stronger theoretical grounding). I place PIRN at **6.0**, consistent with a solid accept (poster) — strong, well-executed work with addressable weaknesses.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>