Now I have all the information needed to produce the consolidated review.

## Summary
PIRN proposes a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD). It introduces three components: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) to update prototypes at test time, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange. Experiments on MVTec 3D-AD, Eyecandies, and Real-IAD show consistent gains over baselines.

## Strengths

1. **Well-motivated problem framing and solution design.** The paper clearly identifies why both cross-modal alignment and memory-bank methods fail in few-shot MAD (lines 23-24), and the three proposed components (BPA, APR, MNC) each target a specific failure mode. This principled decomposition is a genuine strength.

2. **BPA's balanced OT assignment prevents codebook collapse with supporting evidence.** The t-SNE visualization (Figure 1 Right) directly shows that BPA yields a more uniform prototype distribution over normal features compared to softmax assignment, which collapses prototypes into a single cluster. Table 2 (row 1→2, parser artifacts notwithstanding) shows a +0.055 AUROC_I improvement from adding BPA to the baseline.

3. **MNC demonstrably improves cross-modal detection, especially in data-scarce regimes.** Table 3 shows that RGB+SN (0.900) substantially outperforms either modality alone (RGB: 0.794, SN: 0.854) under 5-shot, and the gap narrows as data increases. This directly supports the claim that cross-modal communication is most valuable when per-modality normality is underrepresented.

4. **Consistent few-shot gains across multiple benchmarks.** In Table 1, PIRN improves over the strongest baseline (INP-Former) by +3.9/3.7/2.4 AUROC_I on MVTec-3D-AD and +3.6/4.0/2.2 on Eyecandies at 5/10/50-shot settings, respectively. Gains are consistent across both image-level and pixel-level metrics.

5. **Computational efficiency is a concrete practical advantage.** Table 4 shows PIRN requires only 103.36G FLOPs and 17.49ms latency — 85% fewer FLOPs and 4.35× faster than FIND — while achieving comparable or better AUROC_I (0.922 vs 0.921).

6. **Systematic ablation studies validate design choices.** Tables 5, 6, and 7 examine prototype count K, decoder depth L, and token aggregation method, providing insight into how each hyperparameter affects performance. The K=10 optimum and degradation at K=100 are consistent with the claimed information-bottleneck role of the codebook.

## Weaknesses

### Major

1. **No variance or confidence intervals reported for any results.** All main results in Tables 1 and 8 are given as point estimates with no standard deviation, confidence interval, or indication of statistical significance. In few-shot settings where random splits can induce large variance, it is impossible to assess whether reported gains (e.g., +3.9 AUROC_I at 5-shot) are reliable or within the noise of a single run. This is the most significant evidential gap in the paper.

2. **APR's robustness to anomaly contamination is asserted but not experimentally validated.** The paper claims (lines 116-122) that anomalous patches "tend to be assigned more diffusely across prototypes" and that the GRU gating mechanism "restricts the integration of unreliable anomalous contexts." However, no controlled experiment verifies this behavior. If a subtle anomaly (e.g., a small scratch on a flat surface) has high affinity to a "flat-surface" prototype, the OT assignment may not be diffuse, and the prototype could partially encode the anomaly. The paper does not measure prototype drift under anomalous inputs or provide a sanity check (e.g., feeding an entirely anomalous sample and measuring whether OT assignments are actually diffuse). This gap weakens a core assumption of the APR design.

### Minor

3. **FLOPs accounting needs clarification.** Table 4 reports 103.36G FLOPs for PIRN, but the model uses two frozen DINOv2 ViT-B/14 encoders whose combined forward pass is approximately ~110 GFLOPs at 224×224. The reported total being lower than the encoder cost alone suggests the FLOPs count may only include the decoder portion or uses a specific counting method that should be stated. The paper should clarify what computations are included.

4. **The image-level anomaly score uses the maximum over the fused heatmap.** This is standard but can be sensitive to small false-positive regions. Reporting mean or percentile-based metrics alongside the max would improve robustness and is common practice in anomaly detection benchmarks.

5. **The Real-IAD evaluation (Table 8) uses full-data training, which deviates from the paper's few-shot framing.** While these results provide useful additional validation, they do not directly support the paper's core few-shot claim. The paper is transparent about this shift but the connection to the main narrative could be strengthened.

6. **The INP-Former baseline adaptation is simple (two independent streams fused by element-wise summation).** The paper describes this transparently and treats it as a straightforward adaptation of a unimodal method. However, the lack of any cross-modal interaction in the baseline means the comparison partly reflects the presence vs. absence of cross-modal design, rather than isolating PIRN's specific innovations. A stronger multimodal adaptation (e.g., adding cross-attention fusion to INP-Former) would provide a more controlled comparison.

### Trivial

7. **Table 2 header contains a typo ("BFA" instead of "BPA").** Minor labeling issue.

8. **The textual description of Table 2's ablation ("Removing each component from the full model results in a consistent performance drop") is contradicted by the parsed table rendering where row 4 (0.967) exceeds the full model (0.922).** This appears to be a table alignment artifact from PDF extraction; the original submission likely has a clean table.

## Nice-to-Haves

- Report standard deviations over at least 3-5 random seeds or splits for the 5- and 10-shot settings to support the statistical reliability of the claimed improvements.
- Conduct a controlled experiment verifying APR's diffuse-assignment claim: feed samples with synthetic anomalies of known severity and measure whether prototypes drift (e.g., cosine similarity between updated and original prototypes as a function of anomaly size).
- Analyze cross-modal contamination risk: if APR is applied to one modality only, does MNC propagate contamination to the other? This could be tested by measuring performance when APR is disabled in one branch.
- Provide prototype utilization analysis (e.g., effective rank or entropy of the assignment distribution) under BPA vs. softmax to substantiate the codebook-collapse prevention claim quantitatively.
- Include mean or percentile-based image-level scoring alongside max to assess robustness to small false-positive regions.

## Removed Points

These points were raised in input reviews but are removed or demoted for the following reasons:

- **"Table 2 is garbled/unreadable"** — Removed. This is a PDF parser artifact (all rows show identical checkmarks). The original submission has a properly formatted table.
- **"APR-only contribution is not isolated from MNC"** — Removed. This is factually incorrect: Table 7 directly compares "wo APR module" (0.916) vs. Balanced OT (0.922), isolating APR's contribution.
- **"Cross-modal contamination through MNC creates a positive feedback loop"** — Removed. This is a speculative extrapolation that depends entirely on APR contamination existing (which is itself unproven). Without evidence that APR actually contaminates prototypes, the claimed feedback loop is hypothetical.
- **"D³M comparison is incomplete/uncontrolled"** — Removed. The paper already acknowledges that D³M uses tri-modal input while PIRN uses two modalities (lines 325-326), so the concern is already addressed.
- **"BPA OT nuance about assignment mass vs. count"** — Removed. This is a theoretical nitpick about the OT formulation that doesn't correspond to any demonstrated empirical problem; the t-SNE visualization and ablation results already show BPA works as intended.
- **"Qualitative displacement visualization may be circular"** — Removed. The displacement is computed in the original feature space and then projected to PCA for visualization, which is standard practice.
- **"Insufficient baseline comparison"** (INP-Former adaptation) — Demoted from Major to Minor. The paper is transparent about the adaptation, and demanding a stronger engineered baseline is speculative ("would almost certainly outperform").
- Generic strengths from Strength Finder about "addressing an important problem" — Removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses do not surface a genuinely novel observation about the method or its implications that the paper itself does not already articulate.

## Suggestions

1. Add standard deviations over multiple random seeds (at least 3 runs) for all few-shot settings in Table 1. Without this, the core few-shot claim is evidentially weak.
2. Include a controlled experiment validating APR's claim that anomalous patches receive diffuse OT assignments (e.g., analyze OT weight entropy on held-out anomalous test samples vs. normal ones).
3. Clarify the FLOPs counting methodology in Table 4 — specify whether frozen encoder computations are included or excluded.
4. Report the effective rank or entropy of prototype assignment distributions under BPA vs. softmax to quantitatively substantiate the codebook-collapse prevention claim.
5. Strengthen the Real-IAD narrative by connecting full-data results back to the few-shot setting (e.g., does PIRN also outperform at lower data regimes on this dataset?).

## Score and Decision

The paper tackles a well-motivated problem with a principled architecture and demonstrates consistent gains across multiple benchmarks. However, the complete absence of statistical variance reporting in a few-shot setting is a significant evidential gap that prevents full confidence in the claimed improvements. The second major weakness — the unvalidated APR contamination assumption — is a structural gap that could affect the method's reliability on certain anomaly types. These issues are real but addressable; the core contributions (BPA, MNC) are well-supported by experiments and ablations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>