- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 5, 8, 3
Now I have all the information needed to construct the final review. Let me write it.

## Summary

This paper presents MUSE (MUltimodal Similarity-keeping contrastivE learning), a framework for zero-shot EEG-based image classification. The authors propose: (1) novel EEG encoder architectures (STConv with upstream spatial convolution, and NervFormer with graph attention), (2) a similarity-keeping (SK) regularizer added to InfoNCE contrastive loss, and (3) model interpretation via Grad-CAM. On the ThingsEEG dataset (200-way zero-shot), MUSE-SK achieves 19.3% top-1 and 48.8% top-5 accuracy, outperforming prior methods NICE-GA (15.6%) and BraVL (5.8%). The paper identifies a meaningful problem and assembles a reasonable pipeline, but the individual contributions have uneven support.

## Strengths

- **State-of-the-art zero-shot classification accuracy on ThingsEEG**: The MUSE framework (with or without SK) consistently achieves ~19% top-1 and ~49% top-5 accuracy across 10 subjects, clearly surpassing prior methods NICE-GA (15.6% top-1) and BraVL (5.8% top-1). The 3.7pp top-1 improvement over the prior best method is substantial for this domain. Statistical significance vs. NICE-GA is confirmed via Wilcoxon Signed-Rank Test (p<0.01).

- **Systematic architectural exploration of EEG encoders**: The paper develops and compares multiple encoder designs (STConv, STConv-GA, NervFormer, NervFormer-GA) and tests each with and without the SK loss and Graph Attention modules. This creates a clear ablation hierarchy that allows readers to isolate the effect of each component (Tables 1–3).

- **Model interpretation reveals biologically plausible attention patterns** (e.g., the occipital cortex focus during 100–500ms, consistent with the bottom-up visual hierarchy). While this confirms known neuroscience rather than discovering new phenomena, it provides useful validation that the learned representations correspond to expected neural signatures.

## Weaknesses

### Fatal
None.

### Major

- **The SK regularizer's contribution on the best-performing architecture (STConv) is marginal and not statistically validated against its own ablation baseline.** On STConv, MUSE (19.2%) vs. MUSE-SK (19.3%) is only a 0.1pp gain; on STConv-GA, MUSE-GA (18.8%) vs. MUSE-SK-GA (19.3%) is a 0.5pp gain. The paper itself states (line 205) that "MUSE, MUSE-SK, and MUSE-SK-GA exhibit similar average performance levels." While SK does show a larger 1.6pp improvement on plain NervFormer (14.7%→16.3%), SK actually hurts NervFormer-GA (19.0%→18.6%). No statistical test is reported comparing MUSE with and without SK specifically—the only reported significance test (p<0.01) is against NICE-GA. Since the SK loss is framed as the "pioneering" algorithmic contribution, this inconsistent and often marginal benefit, combined with the absence of a targeted significance test, weakens the core methodological claim.

- **No variance or uncertainty reporting.** Results are "averaged over five random seeds" but no standard deviations, standard errors, or per-seed ranges are reported anywhere. For a 200-way task with ~19% top-1 accuracy, a fluctuation of even 1–2pp across seeds could change method rankings. Without variance information, it is impossible to know whether the 0.1pp SK gain on STConv is meaningful or noise, or whether the 3.7pp gap over NICE-GA is robust. This undermines every comparative claim.

- **Baseline comparison fairness is not established.** The paper reports prior methods (BraVL, NICE, NICE-SA, NICE-GA) but does not state whether these were re-implemented under identical conditions (same optimizer, epochs, image encoder, data splits) or whether numbers are taken from prior papers. Since MUSE uses CLIP-ViT as a fixed image encoder and baselines may use different backbones, the reported gains could partially reflect implementation choices rather than algorithmic superiority. The paper should clarify this.

### Minor

- **The model interpretation contribution is overclaimed as "neuroscientific insights."** The Grad-CAM analysis (Section 4.4) confirms that higher-performing models attend to the occipital cortex during 100–500ms, consistent with the known bottom-up visual hierarchy. This is a useful sanity check but does not constitute a new neuroscientific finding. The paper should recalibrate how this contribution is described.

- **Loss formulation has notational ambiguity.** In Equation 2, `S(·,·)` is used both for cosine similarity between individual vectors (`S_{E,I}`) and for cosine similarity between matrices of similarities (`S(S_{E,E}, S_{I,I})`). Algorithm 1 (lines 99–101) clarifies the computation, but a reader relying only on Equation 2 would find the shapes ambiguous.

- **"Win" (subject score #) column lacks a clear definition.** The tables report a "Win" or "subject score #" column but do not explain the scoring rule. From context it appears to count the number of top-1/top-5 bests across 10 subjects (20 opportunities), but this should be specified explicitly.

- **Grad-CAM visualizations are shown for only one subject (subject 10, the best performer).** This introduces selection bias; showing a range of subjects (including lower-performing ones) would give a more complete picture of the model's behavior.

### Trivial
None.

## Nice-to-Haves

- Report standard deviations or per-seed ranges for all main results.
- Clarify whether baselines were re-implemented or numbers cited from prior papers.
- Add a controlled experiment directly comparing MUSE with and without SK, with a statistical test (e.g., paired Wilcoxon across subjects).
- Report final learned values of β and τ and test sensitivity to β initialization.
- Provide per-class accuracy breakdown (e.g., animate vs. inanimate) to shed light on what EEG information is being decoded.
- Include a limitations section (the paper currently lacks one).

## Removed Points

- **"SK loss provides no meaningful improvement" (Harsh Critic #1, blanket form)**: Removed because this claim is factually too strong. SK provides a 1.6pp improvement on plain NervFormer (14.7%→16.3%) and a 0.5pp improvement on STConv-GA, and the paper honestly acknowledges the modest effect on STConv. The criticism is retained in a moderated form in Major Weaknesses above.

- **Criticism about missing appendix, proofs, or supplementary material**: Removed per instructions — these sections are stripped by the parser but exist in the original submission.

- **"Model interpretation does not constitute a contribution" (as a fatal/major criticism)**: Down-graded to Minor. The analysis does have value as a sanity check that the model attends to expected brain regions and time windows. The issue is overclaiming, not that the analysis is worthless.

- **Criticism about ThingsEEG test image consistency across subjects**: The paper says the test set has "200 test classes, each with 1 image" — these are the same images for all subjects (the dataset defines them). This concern is speculative and not grounded in what the paper actually states.

- **Strength Finder's #3 (model interpretation) about "neuroscientific validation"**: Kept but reframed. The analysis validates that learned representations align with known visual system mechanisms; the "neuroscientific insight" framing is toned down.

## Novel Insights

None beyond the paper's own contributions. The two reviews provide useful triangulation: the Strength Finder correctly identifies the SOTA results and systematic ablation design, while the Harsh Critic correctly identifies that the SK loss's benefit on the main model is marginal and under-validated. The most informative cross-section is the tension between the paper's ambitious framing (three contributions) and the actual evidence (the main algorithmic novelty yields at best 0.1–0.5pp on STConv, with no variance estimates).

## Suggestions

1. **Run a controlled paired experiment** comparing MUSE vs. MUSE-SK on the STConv architecture alone, report per-subject differences with a statistical test (Wilcoxon signed-rank across 10 subjects), and include standard deviations. This would either confirm or refute the SK loss's contribution.
2. **Explicitly state** whether baselines were re-implemented under identical conditions. If they were, report the reproduction setup. If numbers are cited, acknowledge this limitation and discuss potential confounds.
3. **Add standard deviations** to all tables, or at minimum report the per-seed range for the main comparisons.
4. **Recalibrate the model interpretation contribution**: frame it as a model validation/sanity check rather than a novel neuroscientific insight.
5. **Clarify the loss notation** in Equation 2 so that matrix-level cosine similarity is distinguished from vector-level cosine similarity.
6. **Add a limitations section** acknowledging the modest absolute accuracy, subject-dependent variance, and potential confounds in EEG decoding.
