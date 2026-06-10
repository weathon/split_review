Here is my final consolidated review:

## Summary

This paper proposes an active test-time prompt tuning framework for Vision-Language Models (CLIP). At test time, it selectively queries human annotators for labels on high-entropy samples using a dynamically adjusted threshold, stores them in a class-balanced limited-size buffer, and optimizes multimodal prompts using both unsupervised (marginal entropy minimization, distribution alignment) and supervised (cross-entropy on queried samples) losses. Experiments across 10 cross-dataset transfer and 4 domain generalization datasets report average gains of +0.34% and +0.22% over PromptAlign under a 5% annotation budget.

## Strengths

1. **Novel problem framing and fair evaluation protocol (Section 4.2).** Combining active learning with test-time prompt tuning for streaming VLMs is genuinely underexplored, and the paper carefully designs an evaluation protocol where samples are evaluated *before* their labels are queried, avoiding label leakage. This is a non-trivial methodological contribution that strengthens the credibility of the results.

2. **Consistent directional improvement across most datasets (Tables 2, 3).** The method outperforms PromptAlign on 9/10 cross-dataset transfer tasks and 3/4 domain generalization tasks. While the margins are small, the consistency across a broad benchmark suite (14 datasets) suggests the approach is not cherry-picked.

3. **Ablation evidence for individual components (Section 4.4, Figures 2, 4b).** The paper validates its design choices: the class-balanced eviction policy outperforms random deletion (Figure 2, 4 datasets), and the active selection policy outperforms random selection at the same budget (Figure 4b, 4 datasets). These ablations provide meaningful evidence that the specific mechanisms matter.

## Weaknesses

### Fatal
None.

### Major

1. **Small gains with no error bars — statistical significance is unclear.** The method achieves average gains of only +0.34% (cross-dataset) and +0.22% (domain generalization) over PromptAlign. Results are averaged over 3 seeds, but no standard deviations or confidence intervals are reported anywhere. On typical VLM benchmark evaluations, standard deviations of 0.3–0.8% over 3 seeds are common, meaning these headline margins could easily be within the noise. Without variance estimates, the reader cannot assess whether the claimed improvements are statistically meaningful. This is especially problematic given that the method has access to 5% ground-truth labels — if the active learning component were genuinely effective, one would expect more substantial gains.

2. **Missing critical baseline on the main benchmarks.** The main results (Tables 2, 3) compare the proposed method (which uses 5% labels) against baselines (TPT, PromptAlign, CoOp, MaPLe) that use 0% labels. While there is a useful practical question ("does spending a 5% annotation budget beat not spending anything?"), the paper's headline claim of "consistent improvement over the state-of-the-art" conflates two effects: (a) the benefit of having *any* 5% of labels versus none, and (b) the benefit of the *active selection* mechanism specifically. The ablation in Figure 4b compares active vs. random selection at the same 5% budget, but this is only done on 4 datasets and is not reflected in the main benchmark tables. The central claim cannot be properly evaluated without a comparison showing active > random at the same budget on the full 14-dataset benchmark.

3. **Per-dataset tuning of the loss coefficient α for domain generalization (Section 4.1).** The values of α are 1.0 for ImageNet-R and ImageNet-V2, 0.15 for ImageNet-A, and 0.5 for ImageNet-Sketch, with the post-hoc justification that these datasets have "a greater number of outlier samples." This degree of per-dataset tuning within the same benchmark family (ImageNet variants) undermines the claim of robustness and generality. It is not reported whether the baselines received similar per-dataset hyperparameter tuning.

### Minor

1. **Motivating experiment (Table 1) is inadequately documented.** The paper claims to show that "marginal entropy minimization on uncertain samples reinforces errors" and presents this as critical motivation. However, Table 1 is an embedded image with no accompanying quantitative description in the text — no setup details (threshold, datasets, magnitude of improvement) are provided. This key empirical finding cannot be assessed or reproduced from the paper as written.

2. **Per-claim novelty positioning.** The paper claims "to the best of our knowledge, this is a novel setting and we are the first to apply Active Learning in a Test Time setting for VLMs." Given that ATTA (Gui et al., 2024) does active test-time adaptation and Bang et al. (2024) combines prompt learning with active learning, the distinctiveness of this work should be stated more precisely — the novelty lies in the *combination* of streaming single-sample inference + active learning + VLM prompt tuning. The paper implies broader novelty than it should.

3. **No error bars on ablation results either.** All ablations (Figures 2, 3, 4) report point estimates without variance. This is a systemic issue that weakens the paper's empirical rigor.

### Trivial
- Table 1 and the tables in Figures 2, 3, 4 are embedded images; the numerical values are not accessible as text.

## Nice-to-Haves

- A breakdown of what the active selection mechanism actually buys: e.g., class distribution of queried samples, entropy distribution of selected vs. skipped samples, qualitative examples of what the threshold policy captures versus misses.
- Discussion of practical annotation cost: for ImageNet-scale test sets, 5% = 2,500 annotations. Is this realistic for the deployment scenarios described (autopilot, medical)? A cost-benefit discussion would strengthen the motivation.

## Removed Points

The following criticisms from the harsh review were removed or substantially weakened after verification:

- **"z parameter is underspecified (methodological gap)"** — The paper states the algorithm is detailed in Appendix D (Algorithm 1). Per policy, appendix content is stripped by the parser; this is not a gap in the original submission.
- **"Unfair comparison is a structural issue / fundamentally unfair"** — This framing is too strong. The evaluation protocol (Section 4.2) correctly avoids label leakage, and comparing against 0-label baselines tests the practical question of whether a small annotation budget helps. The *real* issue (categorized as Major above) is the missing same-budget baseline on the main benchmarks, not "unfairness."
- **"If simply skipping uncertain samples already helps, then the added value of the annotation budget needs to be isolated"** — This is correct in spirit but the paper's protocol uses *both* skipping (via the threshold) and labeling. The critic's suggestion to disentangle these is a valid ablation that could strengthen the paper; moved to nice-to-have territory.
- **Speculative weaknesses about what the active selection "actually buys you" (class distribution, etc.)** — Generic sweeping concerns, not specific identified problems with concrete anchors in the paper.
- **General reproducibility nits about hyperparameters, implementation details, etc.** — These are either addressed in the paper or are standard practices.
- **Style and formatting nitpicks** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent concern about evaluation rigor (lack of error bars, missing same-budget baselines on main benchmarks) but do not add new technical insights beyond what the paper itself provides.

## Suggestions

1. **Run the random-selection baseline at the 5% budget on all 14 datasets** and include it in the main results tables. This is the single most important experiment: it would isolate the value of the *active* component from the value of having *any* labels.
2. **Report standard deviations over seeds for all main results** (Tables 2, 3) and ablation figures.
3. **Add an ablation that disentangles skipping vs. labeling** — compare: (a) update on all samples (vanilla TPT), (b) skip high-entropy samples entirely (no update), (c) skip high-entropy samples but store and later use actively labeled ones (proposed). This would clarify which mechanism drives gains.
4. **Reduce per-dataset hyperparameter tuning** or show that the method is robust to α within a reasonable range on all domain generalization datasets, not just the 4-dataset ablation set.
5. **Provide the z-adjustment schedule explicitly** — either in the main paper or ensure it is present in the supplementary (if not already).

## Score and Decision

**Overall assessment:** This paper tackles a novel and well-motivated problem — active test-time prompt tuning for VLMs. The evaluation protocol is carefully designed, and the ablations validate individual components. However, the empirical evidence for the central claim is insufficient. The headline gains (+0.34%, +0.22%) are small and unreported with variance, making their statistical significance unclear. The most critical experiment — comparing active selection against random selection at the same budget on the full benchmark — is only done on a 4-dataset subset, not on the 14-dataset benchmark where the headline claims are made. Per-dataset tuning of the loss coefficient further weakens the claims of generality. The paper's core idea has merit, but in its current form the evaluation does not support acceptance at a top-tier venue like ICLR.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>