Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper proposes CALoR, a defense framework against model inversion attacks (MIAs) that integrates three components targeting distinct weaknesses in the MIA pipeline: a confidence adaptation (CA) loss that reduces prediction confidence to misalign the attacker's optimization target, low-rank compression (LoR) of the classification head to reduce information leakage, and a Tanh activation function to induce gradient vanishing during attacker optimization. The method is evaluated on face recognition benchmarks (FaceScrub, CelebA) against four prior defenses and multiple attack methods, showing substantial reductions in attack accuracy — notably 38.4% and 52.0% reductions against IF and PLG in high-resolution settings where prior defenses largely fail.

## Strengths

1. **Novel synthesis of three complementary defense mechanisms** — The paper is the first to jointly target three distinct vulnerabilities in the MIA pipeline (objective mismatch, MI overfitting, and gradient vanishing) within a single framework. While individual weaknesses are known from prior work (LOMMA, PPA), no existing defense simultaneously addresses all three. The CALoR framework cleanly maps each component to a specific weakness: CA loss → attack objective bias (§3.2), LoR → reducing leaked information (§3.3), Tanh → impeding optimization (§3.3).

2. **Strong and well-documented empirical results, especially in challenging high-resolution settings** — In the high-resolution scenario with MS-Celeb-1M backbone (test accuracy >96%), CALoR reduces IF attack accuracy by 38.4% and PLG accuracy by 52.0% compared to the undefended model, while prior defenses (MID, BiDO, LS, TL) show minimal or no reduction (§4.2, Table 2). These are precisely the settings where real-world deployment matters and where prior methods fail.

3. **Fair evaluation protocol maintaining comparable utility across defenses** — The paper carefully adjusts hyperparameters to keep "nearly identical classification accuracy on the test set" across all defense methods (§4.2), ensuring that robustness improvements are not simply artifacts of utility loss. This strengthens the validity of the defense comparisons.

4. **Comprehensive attack evaluation** — The paper evaluates against seven attack methods (GMI, KED, Mirror, PPA, LOMMA, PLG, IF), multiple architectures (IR-152, ResNet-152, ViT-B/16, Swin-v2), and both low- and high-resolution settings, providing confidence that the defense generalizes across diverse scenarios.

5. **Principled motivation for the CA loss** — Figure 3 provides direct empirical evidence that lower average confidence on private images correlates with lower attack accuracy, grounding the CA loss design in data rather than intuition alone.

## Weaknesses

### Major
*None.*

### Minor

1. **Missing direct comparison of CA loss against standard label smoothing** — The CA loss reduces confidence to exp(−1/b) < 1, which is functionally similar to label smoothing (LS). The paper compares against LS as a full defense method (which includes other components), but does not ablate whether the *specific form* of the CA loss outperforms a simple fixed-target label smoothing regularizer under otherwise identical conditions. Without this comparison, it is unclear whether the CA loss is a genuine methodological contribution or whether a simpler confidence-reducing regularizer would achieve similar gains (§3.2, Table 5). This does not invalidate the overall CALoR result, but it weakens the novelty claim for the CA component specifically.

2. **Incomplete specification of the fine-tuning loss** — The paper states that in the second stage the model is "fine-tune[d] with a confidence adaptation loss" (§3.2) but does not explicitly state whether the CA loss is used alone or combined with the cross-entropy loss during fine-tuning. The figure caption says "followed by fine-tuning with a confidence adaptation loss (L_CA)," suggesting L_CA alone, but this should be stated directly in the text. This is a reproducibility concern.

3. **No error bars or multiple-run statistics** — The paper does not report standard deviations, confidence intervals, or results averaged over multiple seeds/runs. In defense papers, where variability across target model initializations and attack runs can be substantial, this omission makes it difficult to assess the reliability of the reported improvements. While this is not uncommon in the MIA defense literature, reporting it would significantly strengthen the paper.

4. **Test accuracy values under each defense not shown in a table** — The paper states that test accuracy is "nearly identical" across defenses but does not report the actual numbers in a table alongside the attack results (§4.2). Readers cannot verify the utility-robustness trade-off quantitatively.

5. **Ablation study is fragmented** — The contributions of the three components are scattered across separate tables: CA alone (Table 5, with CA), rank without CA (Table 6, appendix), activation functions without CA (Table 7, §4.3). A single combinatorial ablation table showing all 2³ combinations (CE-only, CA-only, LoR-only, Tanh-only, CA+LoR, CA+Tanh, LoR+Tanh, all three) would cleanly demonstrate whether the components are additive or whether one dominates. This is a presentation issue rather than a methodological flaw, as the individual ablations do exist.

### Trivial

1. **"First comprehensive analysis" framing is slightly overstated** — The paper claims "the first to conduct comprehensive analyses of weaknesses inherent in MIAs" (§1, §3.1). Individual weaknesses (MI overfitting from LOMMA, gradient vanishing from PPA) are discussed in prior work, and the paper does cite these works in the analysis section. The contribution is better described as the *synthesis* and *joint exploitation* of these weaknesses in a unified defense, which is genuinely novel. The current framing invites unnecessary pushback and should be softened.

## Nice-to-Haves

- A comparison of the CA loss against standard label smoothing (e.g., target 0.9) as a drop-in replacement during fine-tuning, to isolate the benefit of the CA loss's specific functional form.
- Reporting test accuracy numbers for each defense in the main tables.
- A brief discussion of computational overhead (training/inference cost) of the low-rank compression, which may be a practical advantage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Paper does not cite LS, LOMMA, or PPA in the analysis section"** — Factually incorrect. LOMMA is cited in §3.1 for MI overfitting ("the MI overfitting problem \citep{lomma}"), and PPA is cited in §3.1 for optimization challenges ("faces several challenges \citep{ppa}"). Only LS is absent from the analysis section, but LS is cited as a baseline defense.
- **"Comparison set of defenses is outdated"** — The paper compares against the four most relevant SOTA defenses (MID, BiDO, LS, TL). Speculation that "there may well be more recent methods" is unfounded, and the paper's choice of baselines is defensible within the MIA defense literature.
- **"No evaluation on non-face datasets"** — The paper explicitly focuses on face recognition, the standard domain in MIA research. Demanding medical/CIFAR experiments is scope creep; this would turn the paper into a broader study than intended.
- **"Low-rank compression section is too short"** — The section uses `\input{section/lrc_v2}`, meaning its content is in an included file not visible in the extracted text. The criticism is based on incomplete evidence.
- **"CA loss lacks principled motivation"** — The paper provides both empirical motivation (Fig. 3) and theoretical analysis (convergence to exp(−1/b)). The motivation is adequate for a defense loss design.
- **"The analysis is largely a restatement of known observations"** — While individual elements are discussed in prior work, the synthesis of all three weaknesses into a single defense framework is novel. The reviewer's framing understates the paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews identify a set of standard but important gaps (missing label-smoothing comparison, fragmented ablation, no error bars) that are typical for a solid but not flawless paper. The most interesting observation is that the paper's core contribution — the joint exploitation of three MIA weaknesses — is undercut by its own disconnected ablation presentation, which prevents clean verification of additivity.

## Suggestions

1. Add a direct comparison of the CA loss against standard label smoothing in the ablation study to justify its specific functional form.
2. Clarify in §3.2 whether the second-stage fine-tuning uses L_CA alone or L_CA + L_CE.
3. Consolidate the three component ablations into a single combinatorial table (2³ design) in the main paper.
4. Report test accuracy values in the main comparison tables and add error bars (or at minimum, a statement about number of runs).
5. Soften the "first comprehensive analysis" language to "we synthesize and jointly exploit three inherent weaknesses" to avoid unnecessary credibility concerns.

## Score and Decision

The paper presents a well-motivated defense framework with strong empirical results across diverse settings. The weaknesses identified are genuine but do not threaten the paper's core claims — they are about missing comparisons, fragmented presentation, and overclaimed framing, not about flawed methodology or incorrect results. With relatively minor revisions (clarifying the fine-tuning loss, adding a label-smoothing comparison, consolidating ablations, and reporting test accuracies/error bars), the paper would be a solid contribution to the MIA defense literature. In its current form, the paper is above the acceptance threshold but would benefit from the suggested revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>