Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

The paper proposes a dual-stream network for micro-expression recognition (MER) with three key components: a Continuous Vertical Attention (CVA) block that applies attention only along the y-axis (motivated by the observation that vertical facial muscle movements are more informative for MER), a Facial Position Focalizer (FPF) module based on Swin Transformer for spatial position encoding, and AU embedding as auxiliary information. The method achieves 94.35% accuracy on CASME II and 86.76% on SAMM, outperforming prior SOTA. Extensive ablation studies decompose the contribution of each component.

## Strengths

- **Novel vertical attention mechanism (CVA) with clear biological motivation.** The paper identifies that vertical facial muscle movements (brow raising, eyelid tightening, lip pressing) are especially discriminative for micro-expressions, and designs attention only along the y-axis to capture this. The idea is clean, intuitive, and well-motivated. Table 3 directly supports the claim by showing vertical-only attention outperforms horizontal-only and both-directions configurations.

- **Strong empirical results on two standard benchmarks.** The model achieves 94.35% accuracy (CASME II) and 86.76% (SAMM), surpassing prior works including MMNet (+6%) and μ‑BERT (+10.87% on CASME II). The gains are substantial by the standards of the field.

- **Thorough component-level ablation.** Tables 2–7 systematically isolate each design choice: individual contributions of CVA, FPF, and AU embedding (Table 2); vertical vs. horizontal vs. both-directions (Table 3); continuous vs. independent attention (Table 4); Swin vs. ViT (Table 5); single vs. dual-frame input (Table 6); and AU embedding (Table 7). This provides solid evidence that each proposed component contributes meaningfully.

- **Principled choice of Swin Transformer over ViT for position embedding.** The paper justifies this choice by noting that MER requires modeling long-range dependencies across distributed facial regions, which Swin's shifted-window mechanism handles better than ViT. Table 5 validates this empirically.

## Weaknesses

### Fatal
None.

### Major

1. **No variance, confidence intervals, or statistical tests reported for any result.** With only 26–32 subjects per dataset and leave-one-subject-out (LOSO) cross-validation, per-fold variance can be substantial. Every reported accuracy and F1-score is a single point estimate (e.g., 94.35% on CASME II, 86.76% on SAMM). A 6% improvement over a baseline could easily lie within one standard deviation. Without variance estimates, the reliability of any claimed improvement — including the headline SOTA comparison — cannot be assessed. This is the single most impactful weakness, as it undermines the interpretability of all experimental evidence in the paper.

2. **No per-class precision, recall, or F1 reported despite known class imbalance.** Both CASME II and SAMM have heavily imbalanced distributions (with "others" dominating). The paper reports only average accuracy and macro-average F1, but without per-class breakdowns or confusion matrices, the reader cannot determine whether the high accuracy reflects genuine recognition of minority classes (happiness, surprise, contempt, etc.) or is driven by the majority class. Macro-F1 partially mitigates this concern but does not eliminate it — per-class metrics are the standard for diagnosing minority-class performance in MER.

3. **Baseline comparisons in Table 1 may not be controlled.** The paper compares against published numbers from prior work without verifying that the same preprocessing, data splits, class mappings, or evaluation protocols were used. For example, μ‑BERT may have used different emotion taxonomies or input modalities. While cross-paper comparison is common practice in MER, the paper's central claims hinge on beating SOTA by margins that could be artifacts of protocol differences. This does not invalidate the results, but it means the "improvement" claims should be interpreted cautiously.

### Minor

4. **Both-directions attention < vertical-only is not analyzed.** Table 3 shows that using both vertical and horizontal attention yields *lower* accuracy than vertical-only. The paper interprets this as supporting its vertical-dominance thesis, but there is an alternative explanation: the horizontal pathway may be poorly integrated (e.g., feature interference, suboptimal fusion), and the result could reflect an architectural limitation rather than a property of facial movements. The paper does not discuss this alternative or analyze why both-directions underperforms. While this does not invalidate the core contribution (vertical attention works well), it is a missed opportunity for deeper analysis.

5. **Weight decay of 0.6 is unusually high and unexplained.** AdamW with weight decay 0.6 is far outside typical ranges (1e‑4 to 1e‑2). The paper does not discuss or justify this choice. If it is a typo (e.g., 0.06 or 0.006), it should be corrected; if intentional, the rationale and sensitivity analysis should be provided.

6. **The activation function \(F_{act}(x) = x \cdot \text{ReLU}(x+3)/6\) is unusual and unexplained.** It resembles a shifted Swish variant, but no motivation is given. While this is a minor implementation detail, unexplained activation choices hinder reproducibility.

7. **Near-identical improvement margins across two datasets.** Table 2 shows accuracy gains of 13.23% (CASME II) and 13.2% (SAMM), and F1 gains of 18.2% and 18.26%, when combining all three modules over the ResNet-18 baseline. These numbers are suspiciously close given that the two datasets have different subjects, class distributions, and recording conditions. The paper does not remark on this coincidence.

8. **No evaluation on the SMIC dataset.** SMIC is one of the three standard MER benchmarks. Evaluating on only two datasets limits generalization claims, although this is a scope limitation rather than a flaw in what is reported.

9. **The "proved" language in the abstract is over-claiming.** The paper states "We also proved that including AU can further enhance accuracy" — this is empirical evidence, not proof. Similarly, the claim that "vertical facial muscle movement plays a more significant role" (line 36, 55) is stated as fact without anatomical citation (though it is later supported empirically).

### Trivial
- Some table captions (Tables 3–7) do not explicitly state which dataset they refer to, requiring the reader to infer from surrounding text.
- The reduction factor \(\max\{8, C/32\}\) in the CVA module is stated without justification or ablation.
- The number of stacked CVA modules (four) is not ablated.
- Patch size for the Swin Transformer input is not specified.

## Nice-to-Haves
- Reporting standard deviation across LOSO folds and per-class metrics would greatly strengthen the paper.
- Attention map visualizations from the CVA block would help verify that the model focuses on vertical muscle regions (brow, eyelid, mouth) rather than identity-related areas.
- An ablation on the fusion method for combining vertical and horizontal attention (e.g., concatenation vs. addition vs. gating) could illuminate why both-directions underperforms.

## Removed Points
These points from the input reviews were removed with justification:

- **"Both-direction attention performs worse, revealing a fundamental design flaw" (Harsh Critic #1, strong version).** The paper's central claim is that vertical attention *alone* works best. The result that vertical-only > both-directions is *consistent with* this thesis, not contradictory to it. The reviewer's assertion that adding horizontal attention "should not degrade performance" assumes an idealized optimization scenario; in practice, adding weakly informative dimensions can hurt due to feature competition or overfitting. The paper's lack of analysis on this point is legitimate (kept as Minor #4), but the "fundamental design flaw" framing is factually incorrect about what this result implies and has been removed accordingly.

- **"Unfair comparison" claims where the asymmetry favors baselines (not applicable here — no such asymmetry was found).**

- **Formatting/style nitpicks and grammar concerns** (these are PDF-extraction artifacts, not author errors).

- **Generic strengths from the Strength Finder** such as "addressed an important problem" — these were dropped as they lack specific content.

## Novel Insights
None beyond the paper's own contributions. The reviewers did not identify a novel observation that the paper itself does not make.

## Suggestions

1. **Add variance.** Report accuracy and F1 with standard deviation or per-fold breakdowns for all experiments. This is the single most impactful improvement.
2. **Report per-class precision, recall, and F1** for both CASME II and SAMM, or at minimum provide confusion matrices.
3. **Discuss the both-directions result.** Acknowledge the alternative interpretation (architectural fusion issue) and, if possible, probe it with a simple ablation (e.g., learnable weighted fusion of vertical and horizontal paths).
4. **Clarify the weight decay value.** Confirm whether 0.6 is correct or a typo, and justify or correct it.
5. **Clarify the activation function and reduction factor choices** briefly in the text or supplement.
6. **Replace "proved" with "demonstrated" or "showed"** in the abstract to accurately reflect the nature of the evidence.

## Score and Decision

The paper presents a genuinely interesting idea (vertical-only attention for MER) backed by extensive ablation experiments and strong benchmark results. The core contribution is solid. However, the absence of any variance estimates, per-class metrics, and controlled baseline re-implementations means the reported gains cannot be fully evaluated. These are addressable weaknesses — they do not invalidate the approach but they prevent the paper from being accepted in its current form. With proper statistical reporting and the minor analyses suggested above, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>