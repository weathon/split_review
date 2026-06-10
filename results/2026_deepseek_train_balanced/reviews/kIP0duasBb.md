Now let me write the finalized review.

## Summary

This paper proposes RLCF (Reinforcement Learning with CLIP Feedback), a test-time adaptation framework that uses a frozen CLIP model as a reward signal and the REINFORCE algorithm to update a VLM at test time on a single sample. The method replaces the entropy minimization objective used in prior TTA methods (e.g., TPT) with CLIPScore maximization, and is demonstrated across three tasks: zero-shot classification on OOD data, text-image retrieval, and image captioning. The core idea is well-motivated — avoiding the "blindly confident" trap of entropy minimization by grounding adaptation in an external reward signal.

## Strengths

1. **RLCF with a smaller model (CLIP-B/16) surpasses a larger reward model (CLIP-L/14) on several OOD benchmarks** (ImageNet-A/V2/R, lines 424–426) and similarly in retrieval (line 458, outperforming CLIP-L/14-336). This is a genuinely interesting finding that goes beyond straightforward distillation, where the student is typically weaker than the teacher.

2. **RLCF avoids the degradation that plagues entropy-minimization TTA.** Figures 3b/3c empirically show that TPT's top-5 accuracy drops with more adaptation steps while RLCF remains stable (lines 432–434), and the expected calibration error of RLCF is lower (Fig 3a, lines 429–431).

3. **RLCF works with both prompt tuning and image encoder tuning**, whereas TPT underperforms with image encoder tuning (lines 261–262). This demonstrates broader applicability to different adaptation strategies.

4. **The momentum buffer mechanism** (lines 335–346) for incremental learning while preserving episodic safety is a practical contribution that bridges the gap between episodic TTA and continual adaptation.

## Weaknesses

### Major

- **Missing critical ablation: same-model reward.** The paper never tests RLCF where the adapted VLM and the reward model are the same size/architecture (e.g., CLIP-B/16 as both). Without this, it is impossible to tell how much of the benefit comes from the REINFORCE-based RL objective itself versus simply injecting knowledge from a larger, more capable reward model. If the benefit is entirely from the larger model, the paper should be reframed accordingly. This is the single most important experiment needed to support the paper's core claims.

- **No computational cost analysis.** TTA methods are intended for deployment. RLCF requires: generating 64 augmented views, running inference on all of them in the adapted model, running additional CLIP-model inference for each of K candidates per view, and performing multiple gradient steps — all per test sample. The paper provides zero quantification (FLOPs, wall-clock time, or memory) for any of this. For a method to be practically usable, this information is essential.

### Minor

- **The claimed distinction from knowledge distillation is overstated and the corresponding failure mode is unacknowledged.** The paper uses a cherry-picked example (lines 285–288) where the student has a correct top-1 prediction. It never discusses the symmetric case: if the student's top-K sampling (K=3) excludes the ground-truth class entirely, RLCF cannot recover it because the reward model only scores candidates the student already produced. This is a real limitation of the finite-sample approach that should be explicitly discussed.

- **No ablation on the reward baseline.** The paper frames the average-score baseline as a key innovation that enables CLIPScore as a standalone reward (lines 206–214, contributions point 2). But subtracting a baseline is textbook REINFORCE (Williams, 1992) — a variance reduction technique. The paper does not compare the average baseline against a greedy baseline or no baseline, so the claim that this specific baseline is what makes CLIPScore "usable alone" is unsupported by evidence.

- **The ensemble weighting scheme is ad-hoc.** Line 327: "We assign scores based on human preference for different CLIP models: {CLIP-ViT-L/14-336: 10, CLIP-ViT-L/14: 5, CLIP-RN50×64: 3}." What "human preference" data were used? Were these weights validated on a held-out set? This is not a reproducible procedure. (Note: the main results use a single reward model, so this is not fatal, but the ensemble variant's results rest on an unprincipled choice.)

- **No ablation on the sampling factor K.** K varies substantially across tasks (3 for classification, 12–20 for retrieval, 6–10 for captioning) with no justification and no study of how K affects the reward estimate, gradient variance, or final performance.

- **No limitations section.** The paper does not discuss any failure cases, settings where RLCF might hurt performance, or the constraint that the method cannot recover ground truth absent from the student's top-K.

### Trivial

None.

## Nice-to-Haves

- An analysis of *why* the smaller model + RLCF surpasses the larger reward model would substantially strengthen the paper. Is it because the smaller model has favorable inductive biases on specific OOD datasets, or because test-time optimization provides an advantage over static zero-shot inference?
- Ablations on the number of TTA steps.
- Comparison against RLCF with the same-size reward model.
- Histogram or boxplot showing the distribution of reward values to demonstrate that the average baseline indeed provides useful negative feedback.

## Removed Points

These points were flagged by reviewers but removed or demoted after verification:

- **"Selective reporting"** (Harsh Critic): The paper specifically states improvements "on ImageNet-A/V2/R" (line 424), which is a precise claim about those three datasets. There is no evidence of selective reporting.
- **"ECE mentioned without numbers"** (Harsh Critic): ECE is shown in Figure 3a, which is a standard way to present calibration information. The paper explicitly cites the figure and states the qualitative trend.
- **"Contribution is just incremental modification to TPT"** (Harsh Critic): TPT only handles classification with prompt tuning. RLCF additionally handles image encoder tuning, retrieval, and captioning, making the "first universal" claim defensible even if the core innovation (swapping entropy for CLIP-reward) is conceptually simple.
- **Strength Finder claim about "average baseline makes CLIPScore usable standalone"** was weakened to a minor weakness because the paper lacks the ablation to support it.
- **Various formatting and grammar nitpicks** removed per review guidelines.

## Novel Insights

None beyond the paper's own contributions. The observation that a smaller CLIP model adapted via RLCF can outperform a larger static CLIP model is the paper's most striking result, but the reviews did not produce a deeper explanation for this phenomenon beyond what the paper already offers (combined merits of both models through the feedback mechanism).

## Suggestions

1. **Run the same-model ablation** (CLIP-B/16 as both adapted VLM and reward model) and report whether RLCF still improves over the zero-shot baseline. This cleanly separates the effect of the RL objective from the effect of the larger reward model.
2. **Add a limitations paragraph** that discusses the finite-top-K failure mode, when RLCF might underperform, and computational costs.
3. **Provide computational cost numbers** (wall-clock time per sample, total FLOPs relative to zero-shot inference) across the three tasks.
4. **Add ablations on the reward baseline** (no baseline, average baseline, greedy baseline) and on the sampling factor K.
5. **Justify or remove the ad-hoc ensemble weighting scheme**, or show that results are robust to the specific weights.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>