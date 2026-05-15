Now I'll produce the final consolidated review.

## Summary

This paper applies two existing long-tail regularization methods—contrastive loss (Makansi et al., 2021) and PLM re-weighting (Kozerawski et al., 2022)—to a probabilistic trajectory prediction model (Trajectron++), evaluating on both pedestrian and vehicle classes in the NuScenes dataset using distribution-aware KDE-NLL metrics. The central finding is that for pedestrians, both methods yield modest improvements in average and long-tail KDE, while for vehicles, neither method reliably improves long-tail KDE—a negative result invisible to the minADE/minFDE metrics used in prior work.

## Strengths

- **First evaluation on a probabilistic model with distributional metrics**: Prior work applied these regularization methods only to non-probabilistic models (Trajectron++EWTA) evaluated on minADE/minFDE. By using Trajectron++ (a CVAE that outputs trajectory distributions with likelihoods) and evaluating with KDE-NLL, the paper addresses an important gap: whether these methods generalize to models that output full predictive distributions. This choice is well-motivated and the results contribute new knowledge (Sec. 1, Sec. 3.2, Tables 2, 4).

- **Comparison across agent types reveals method-specific failures**: The paper evaluates on both pedestrians and vehicles, finding that methods that improve pedestrian KDE (Table 2) do not generalize to vehicles—PLM re-weighting actually regresses 95th/98th/99th percentile KDE for vehicles (Table 4), while contrastive loss shows inconsistent improvements. This cross-agent comparison is a genuinely useful finding that goes beyond prior work, which evaluated on a single agent type (Sec. 4.2.1–4.2.2, Figures 2c–2d).

- **Distribution-aware metric exposes hidden degradation**: The KDE metric reveals that PLM re-weighting for vehicles improves most-likely FDE tail metrics (Table 3) while simultaneously worsening KDE tail metrics (Table 4). The paper correctly identifies that this pattern is consistent with the model predicting a "mean" long-tail trajectory rather than a multimodal distribution—a finding that minADE/minFDE could not capture (Sec. 4.2.2, lines 160–164).

- **Clear methodological description**: The paper provides a detailed diagram (Figure 1) and explicit equations for how contrastive loss is applied to the CVAE latent embedding and how PLM re-weighting modifies per-example loss, including hyperparameter defaults (Sec. 3.2.1–3.2.2). The discussion of metric equivalence between different tail definitions (Makansi's difficulty scoring vs. Kozerawski's percentiles) is well-reasoned (Sec. 4.1.1).

## Weaknesses

### Major

None. The paper's core claims are supported by quantitative evidence, and no issue fundamentally invalidates the conclusions.

### Minor

- **Ablation study mentioned but not reported**: The paper states in Sec. 3.2.2 (line 91) that "we also perform an ablation study to see how applying more or less regularization might affect the model," yet no results from this study appear anywhere in the paper. This is a significant gap in experimental reporting. Without sensitivity analysis on the regularization hyperparameters (which were taken as defaults from the original papers, designed for a different base model), the reader cannot fully assess whether the negative results for vehicles reflect method limitations or suboptimal hyperparameter choices.

- **No variance/error bars across runs**: All metrics (Tables 1–4) are reported as single values without standard deviations, confidence intervals, or multiple seeds. The pedestrian KDE improvements are numerically small (e.g., average KDE from −1.500 to −1.543, −1.553), and the vehicle results are mixed across percentiles. Without run-to-run variance, the statistical reliability of these differences is unclear. This is standard practice in trajectory prediction benchmarks, but it weakens the confidence in small-margin comparisons.

- **Vehicle failure mechanism is speculative**: The paper attributes PLM re-weighting's vehicle failure to predicting "mean" long-tail trajectories (Sec. 4.2.2, line 162), but provides no quantitative evidence for this mechanism (e.g., measuring prediction diversity, average pairwise distance among trajectory samples for long-tail examples). The claim is plausible and consistent with the data, but remains an untested hypothesis.

- **Qualitative analysis lacks quantitative support**: The paper claims the contrastive model produces higher-variance predictions (Sec. 4.3, line 171) based on visual inspection, without reporting any diversity metric (e.g., average sample variance across the test set or long-tail subset). The qualitative section adds limited value beyond the quantitative results.

- **Contrastive loss embedding space not analyzed**: The paper places the contrastive loss on the CVAE latent embedding (before the decoder) but does not discuss whether this space is appropriate for the contrastive objective (e.g., dimensionality, normalization, semantic structure). This is a methodological detail that could affect whether the contrastive loss works as intended (Sec. 3.2.1).

### Trivial

None.

## Nice-to-Haves

- Reporting average pairwise distance among trajectory samples (prediction diversity) for long-tail examples would strengthen the "mean trajectory" hypothesis for vehicles.
- A cumulative distribution plot of KDE errors (as a supplement to the log-scale histograms in Figure 2) would more clearly show tail differences across models.
- The paper's future work suggestions (map-based re-weighting, ensemble models) are reasonable but vague; more specific, grounded next steps would strengthen the conclusion.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism about minADE/minFDE not being reported** (Harsh Critic, Issue 3): The paper explicitly and reasonably argues that minADE/minFDE are less appropriate than most-likely FDE and KDE for probabilistic models with likelihoods (Sec. 4.1, lines 107, 131, 160). The paper's stated contribution is to re-evaluate with distribution-aware metrics. Demanding the original metrics amounts to scope creep—the authors made a deliberate methodological choice and explained it.

2. **Criticism about the "only two regularization methods" claim in the introduction**: The paper acknowledges Wang et al. (2023) as using "a mixture of experts...not regularization" (Sec. 2.3, line 40). Anderson et al. (2019) is cited as a data augmentation method that "could be used" for upsampling, not as a regularization method for long-tailed learning. The paper's claim about regularization methods is appropriately scoped.

3. **Criticism about "first to report performance on both pedestrian and vehicle classes" being unverifiable**: This is a novelty claim that cannot be verified without an exhaustive literature review, which is the reviewers' responsibility, not the paper's. The instruction explicitly states to remove criticisms about missing related works.

4. **Criticism about the abstract not previewing negative vehicle results**: The abstract frames the contribution accurately; previewing every experimental outcome in the abstract is not standard practice.

5. **Criticism about missing appendix/proofs**: The parser strips these sections from all papers. The original submission likely contained additional material.

6. **Generic formatting/style nitpicks**: Removed as per instructions.

## Novel Insights

The paper's most interesting finding is the asymmetry between pedestrians and vehicles: the same regularization methods that modestly improve pedestrian long-tail KDE degrade vehicle long-tail KDE. This suggests that the difficulty structure of the long tail differs qualitatively between agent types—for vehicles, the "hard" examples may involve map-constrained, multi-modal maneuver choices (turn vs. straight) where predicting a "mean" trajectory is harmful, whereas for pedestrians the tail reflects more continuous diversity (e.g., varying speeds, subtle path deviations) where regularization helps. This insight, while not fully analyzed mechanistically, is a valuable observation for future work on long-tailed trajectory prediction.

## Suggestions

1. **Report the ablation study results** in the main paper or a clearly referenced supplement. This is the single most important addition, as it addresses whether the negative vehicle results are artifacts of default hyperparameters.

2. **Add error bars or multiple-run statistics** for the key quantitative comparisons (Tables 2, 4). At minimum, note whether single-run evaluation is standard practice for this benchmark and dataset.

3. **Add a quantitative diversity metric** (e.g., average pairwise distance among predicted trajectory samples) to support the "mean trajectory" hypothesis for vehicle failure, rather than relying on speculation.

4. **Tighten the qualitative analysis**: either add quantitative support for the variance and diversity claims, or reduce the qualitative section to what the visual evidence directly supports.

5. **Clarify the ablation study scope**: if it was performed but cut for space, note this explicitly; if it was planned but not completed, remove the mention from the method section to avoid misleading readers.

## Score and Decision

**Originality**: 5/10 — Applies existing methods to a new model class and agent type; the negative result is novel but the methodology is not.

**Importance of question**: 7/10 — Long-tailed learning in regression for safety-critical prediction is an important problem.

**Claims supported**: 5/10 — The central claims are directionally supported, but the missing ablation and lack of error bars weaken confidence in the quantitative comparisons.

**Soundness of experiments**: 5/10 — The experimental design is reasonable, but the missing ablation and single-run evaluation are notable gaps.

**Clarity of writing**: 7/10 — The paper is clearly written, well-structured, and the methodological choices are explained.

**Value to community**: 6/10 — The cross-agent negative result is useful; the paper will likely inform future work on long-tail methods for probabilistic trajectory models.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>