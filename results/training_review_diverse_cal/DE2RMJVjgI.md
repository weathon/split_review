Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

The paper proposes FS-PTAL, a point-supervised temporal action localization framework that targets action-background confusion through four components: (a) a label extension module that up-samples regions around annotated action frames, (b) a pseudo label mining strategy that generates additional action and background point-level labels, (c) an optimized score contrast module that fixes a flaw in the standard OIC loss where the outer scope of a long action can incorrectly include an adjacent short action, and (d) a feature separation module that applies contrastive learning with cosine similarity on point-level embeddings to pull apart action and background features. Experiments on THUMOS'14 (shown in the main paper) report 56.74% average mAP, outperforming prior point-supervised methods such as LACP by ~4%, and the ablation study attributes gains of 2.1% (label extension), 7.4% (pseudo label mining), 4.2% (score contrast), and 5.1% (feature separation) to the individual modules.

## Strengths

1. **Clear performance gains on THUMOS'14 with meaningful comparisons.** The paper reports results in Table 1 (shown as an image) comparing FS-PTAL against frame-level, video-level, and point-level methods. The text specifies that FS-PTAL outperforms LACP by nearly 4% on both Avg(0.1:0.5) and Avg(0.3:0.7), with particularly notable improvements at higher IoU thresholds, supporting the claim of better action-background separation.

2. **Ablation study validates individual module contributions.** Table 2 (shown as an image) and the accompanying analysis (lines 208-209) quantify each module's contribution: label extension (+2.1%), pseudo label mining (+7.4%), score contrast (+4.2%), and feature separation (+5.1%). The pseudo label mining module providing the largest gain is consistent with the stated motivation that label sparsity is a core bottleneck.

3. **Concrete improvement to the OIC loss.** The paper identifies a genuine flaw in prior work (Lee & Byun, 2021; Shou et al., 2018) where the standard outer-inner contrast calculation can inadvertently include adjacent short actions within the outer scope of a long action (Figure 3). The proposed fix in Eq. 8 adjusts the outer scope using adjacent segment boundaries rather than a fixed function of segment length alone. This is a well-motivated, targeted improvement over the existing OIC formulation.

4. **Error-analysis-driven motivation.** The paper uses the diagnostic tool of Alwassel et al. (2018) to show that Localization Err. and Background Err. dominate for existing WS-TAL methods BackTAL and ASM (Figure 1). This grounds the proposed framework in a concrete failure analysis rather than a generic observation.

5. **Annotation-cost justification.** The paper cites Ma et al. (2020) showing that point-level labeling costs ~45s per minute of video, similar to video-level labels (50s) and far cheaper than frame-level labels (300s), establishing the practical relevance of the point-supervised setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The feature separation module's novelty claim is overstated.** The paper states that prior works (Min & Corso, 2020; Lee & Byun, 2021) "use segment-level coarse-grained features and destroyed the integrity of feature information during the pooling and feature sampling, whereas ours introduces feature embedding space, which not only preserves complete feature information but also enhances it." In practice, the module uses two convolutional layers to produce an embedding space, followed by cosine-similarity-based contrastive loss with hard-example mining and threshold constraints. This is a straightforward application of standard contrastive learning at point-level granularity. The claimed "novel" difference — point-level vs. segment-level features — is a legitimate incremental improvement, but the language implies architectural novelty where the actual contribution is a reasonable design choice (contrastive loss on frame embeddings rather than pooled segment embeddings). A more measured description would better reflect the module's actual technical depth.

2. **Sequential ablation design masks potential interactions.** The ablation (Table 2) adds modules cumulatively (baseline → +A → +A+B → +A+B+C → +A+B+C+D). This sequential addition conflates interaction effects: the gain attributed to the score contrast module (+4.2%) is measured only when label extension AND pseudo label mining are already present. Removing each module individually from the full model would be a more informative complement, as it would reveal whether any module's benefit depends on the presence of another. That said, sequential addition is a common ablation pattern in TAL papers, and the overall pattern of positive contributions is still clear.

### Trivial
None.

## Nice-to-Haves
- For the score contrast module, an ablation comparing the proposed outer-scope calculation (Eq. 8) with the standard OIC calculation on an otherwise-identical model would directly demonstrate that the fix matters beyond the cumulative gain reported in the main ablation.
- A t-SNE or UMAP visualization of the learned feature embedding space (action vs. background frame features) would provide direct visual evidence for the claimed fine-grained separation.

## Removed Points

These points were flagged by reviewers but are removed following the review guidelines. They are listed here for transparency but should not factor into the overall assessment.

- **"Incomplete experimental reporting — ActivityNet v1.3, BEOID, GTEA results deferred to appendix."** The paper states these results are in the supplementary material (removed by the parser). Per the guidelines, criticisms about missing appendix content are removed because those sections exist in the original submission.
- **"Critical algorithmic details deferred to appendix."** Multiple references to algorithmic details (label extension algorithm, pseudo label mining algorithm, inference procedure, hyperparameter settings) being in "the Sec." concern content that was removed by the parser. The main paper still provides the core formulas, loss functions, and descriptive text needed to understand the method.
- **"THUMOS'14 per-IoU values and comparisons missing."** This is factually incorrect — Table 1 (present as an image in the paper) displays per-IoU results across the full range of IoU thresholds and includes comparisons with multiple baselines.
- **"Ablation gains reported relative to an unreported baseline mAP."** Table 2 (present as an image) would show the baseline mAP as its first row. The text describes percentage gains relative to the baseline shown in the table. This is standard practice.
- **"Equation (8) is garbled."** The garbled appearance is a parser/formatting artifact, not an error in the original submission.
- **"The score contrast module's improvement is a 'reasonable fix.'"** This is a positive or neutral observation, not a weakness.
- Various criticisms about the absence of appendix-dependent content, missing hyperparameter values, and formatting issues that either stem from parser artifacts or concern content removed by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that recontextualizes the work in a way the authors themselves did not articulate.

## Suggestions

1. **Tone down the novelty framing for the feature separation module.** Replace language like "introduces feature embedding space" and "enhances it" with a more precise statement: "applies contrastive learning at point-level granularity rather than on pooled segment features, which preserves per-frame information." This better reflects the actual technical contribution.

2. **Add a complementary ablation that removes each single module from the full model** (i.e., full model − A, full model − B, etc.) in addition to the sequential addition ablation. This would disentangle interaction effects and strengthen the causal claims about individual module contributions.

3. **Include the diagnostic error analysis** (Alwassel et al., 2018) **for FS-PTAL** in the main paper — or at minimum summarize the key conclusion — as this directly supports the paper's central claim that the method reduces Localization Err. and Background Err. The paper currently only promises this analysis "in the Sec."

## Score and Decision

This paper makes a solid, incremental contribution to point-supervised temporal action localization. The four-module framework is well-motivated by the error analysis (Figure 1), and the core claim — that better action-background separation leads to improved TAL performance — is supported by the THUMOS'14 results and ablation study. The score contrast module's fix to the OIC loss is a genuine, well-identified improvement over prior work. The primary weakness is that the feature separation module's novelty is somewhat overstated relative to its technical content, but this does not undermine the paper's overall contribution. The paper is technically sound, clearly written (modulo parser artifacts), and addresses a practically relevant problem in video understanding. It would benefit from the suggested additions but is acceptable in its current form as a conference paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>