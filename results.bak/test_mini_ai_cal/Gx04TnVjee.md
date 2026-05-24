Now I have all the information I need. Let me compose the final review.

## Summary

This paper proposes 3DTrajMaster, a framework for controlling multi-entity 3D motions in text-to-video generation by conditioning on per-entity 6DoF pose sequences (rotation + translation per frame). The core technical contribution is a plug-and-play 3D-motion grounded object injector that uses gated self-attention to associate individual entity descriptions with their corresponding 3D trajectories while preserving the base diffusion model's prior. A synthetic 360°-Motion Dataset is constructed using UE rendering, and domain adaptor (LoRA) + annealed sampling are introduced to mitigate quality degradation from synthetic training data. The method is evaluated against 2D baselines (MotionCtrl, Direct-a-Video, Tora) and reports large quantitative margins.

## Strengths

- **Novel problem formulation and clean architecture for multi-entity 6DoF motion control.** The paper is the first to tackle multi-entity *3D* motion control in video generation using per-entity 6DoF pose sequences. The gated self-attention injector (Section 3.2) that entity-wisely adds text and trajectory embeddings before fusion is well-motivated, and the ablation study (Table ablation_main) confirms its superiority over cross-attention fusion and alternative placement. This is a genuine architectural contribution that goes beyond simple 2D-to-3D adaptation.

- **Strong qualitative evidence of capabilities that 2D methods fundamentally cannot achieve.** Figure main_comparison shows 3DTrajMaster producing a 180° turn-back and a continuous inward 90° turn-around, and correctly handling 3D occlusion (a man walking in front of a zebra). These are motions that 2D representations (points, boxes) cannot express regardless of prompt quality, providing compelling evidence for the method's core value proposition that is independent of the prompt confound.

- **Large quantitative margins over baselines even accounting for the prompt confound.** The reported numbers (RotErr 0.265 vs next best 0.771, TransErr 0.037 vs 0.049, FVD 157.72 vs 221.82) show gaps far larger than what prompt simplification alone could plausibly explain. While the comparison is imperfect, the magnitude of the advantage suggests genuine superiority in motion control.

- **Well-designed synthetic data pipeline and effective domain mitigation techniques.** The 360°-Motion Dataset construction (70 animated assets, ~96 GPT-generated trajectory templates, 12 cameras on 4 platforms, yielding 54K videos) is thorough and addresses a real data scarcity problem. The LoRA-based domain adaptor + annealed sampling combination is shown in ablation to be critical for quality (FVD 157.72 → 302.15 without adaptor), and the ablations are clean.

## Weaknesses

### Major

1. **Baseline comparison confounded by mismatched text prompts.** The paper states (line 218): *"For baselines, we simplify the entity description, such as changing 'a man with messy black hair, tall frame, a red shirt' to 'a man' or 'a man in red'. Otherwise, they may fail to generate videos with detailed descriptions."* This means 3DTrajMaster receives richer prompts than baselines in the same evaluation. While the paper is transparent about this, the quantitative results in Table main_comparison compare methods under *different prompt conditions*. It is impossible to fully disentangle whether the gap is due to motion control capability or prompt informativeness. The paper should either (a) use identical prompts for all methods and report failure rates where baselines break, or (b) provide a controlled experiment showing that using detailed prompts for baselines does not change the relative ordering. This does not invalidate the qualitative evidence (2D methods cannot produce 3D rotations regardless of prompts), but it substantially weakens the quantitative claims.

2. **Quantitative motion accuracy is only evaluated on human entities.** Trajectory accuracy (RotErr, TransErr) is computed exclusively on human subjects via GVHMR pose estimator (line 182). The paper claims control over diverse entity categories (animals, cars, robots, natural forces) and shows qualitative examples, but provides *no quantitative metric* for any non-human entity. Since the 360°-Motion Dataset has ground-truth 6DoF poses for all entities (it was rendered with known camera and object poses), the paper could have validated non-human motion accuracy on held-out synthetic samples. This is a straightforward and directly relevant experiment that is conspicuously absent, leaving a significant gap between the broad claims and the narrow evaluation.

### Minor

3. **Built on an internal, non-public video diffusion model.** The method is trained on an internal ~1B parameter video diffusion model (line 175). While this is common in industry-affiliated video generation work and does not invalidate the contribution, it limits reproducibility and independent verification. Combined with the custom synthetic dataset (release status not committed to), this makes the results difficult to build upon directly.

4. **Key hyperparameters deferred to supplementary.** The paper references but does not report the annealed sampling timestep \(T_c\), LoRA rank, or LoRA \(\alpha\) value in the main paper (see Algorithm 1 and Section 3.3). While authors cite the supplementary for these details, the main text is self-contained only if the reader can access supplementary material, which the parser strips. These should be stated in the main paper.

### Trivial

- Algorithm 1 describes a "negative motion prompt" (static motion) but the paper states (line 151) it is *not adopted* due to quality decline. The description in the algorithm and surrounding text is slightly confusing — it would be cleaner to either remove the extraneous description or clearly mark it as an optional variant that was not used.

## Nice-to-Haves

- **Synthetic validation for non-human entities:** Use held-out examples from the 360°-Motion Dataset (which has ground-truth 6DoF for all entity types) to provide quantitative trajectory accuracy for animals, cars, etc. This would directly strengthen the paper's central claim of generalization across diverse entities.
- **Statistical significance reporting:** Provide confidence intervals or standard deviations (at least over seeds) for the main quantitative metrics.
- **Ablation of 2D-projected 3D trajectories as a baseline:** A natural ablation would be a version of 3DTrajMaster that uses 2D projections of the 3D trajectories, to isolate the benefit of the 3D representation itself.

## Removed Points

- **Reproducibility as a fatal weakness (Harsh Critic's Point 3):** The critic argues that the internal model and unclear dataset release severely limit reproducibility. While the internal model is indeed a limitation, the rule against questioning availability of cited entities applies — the paper does not claim the model is public. Moreover, many top-venue video generation papers use internal base models. This is demoted to a Minor weakness (see #3 above) rather than treated as a fatal flaw.

- **"Negative motion prompt should be removed or clarified" (from Section-by-Section notes):** The paper already states (line 151) that it is not adopted. The description in the algorithm is slightly confusing but not a substantive issue. Demoted to Trivial.

- **"44 novel pose templates may be distributionally similar to training" (Section-by-Section notes):** Purely speculative. No evidence is presented that the templates are distributionally identical. Removed.

- **"Evaluation dataset only 100 videos" (statistical significance concern):** 100 videos is modest but standard for this type of evaluation in video generation papers. The concern about missing confidence intervals is kept as a Nice-to-Have.

- **Various reproducibility nitpicks (undisclosed hyperparameters, training logs):** Removed per hard rules on reproducibility nitpicks. The missing \(T_c\) and LoRA rank are kept as Minor weaknesses since they are substantive for understanding the method.

- **"Baseline with 3D input adaptation" (from Strengthening section):** This is a nice-to-have suggestion, not a weakness. The paper compares against 2D methods because no 3D motion control baselines exist (which is exactly the paper's point). Moved to Nice-to-Haves.

- **Strength Finder's overclaim about "state-of-the-art quantitative results" —** The confidence of this claim is tempered by the prompt confound, so the strength is retained but with the caveat made explicit.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension that the paper itself recognizes: the strongest evidence for 3D motion superiority is qualitative (2D methods simply cannot produce 3D rotations/occlusions by their nature), while the quantitative comparison — which attempts to measure this gap with numbers — is compromised by unequal prompt conditions. A synthetic ground-truth experiment on non-human entities from the paper's own dataset would be the single highest-leverage improvement, directly addressing both evaluation weaknesses at once.

## Suggestions

1. **Re-run the baseline comparison with identical text prompts** for all methods. Report both success/failure rates and quantitative metrics. If some baselines fail too often, explicitly document this and report metrics only on successful runs, or use a failure-tolerant evaluation protocol.
2. **Add a synthetic validation experiment** on held-out 360°-Motion Dataset samples with known ground-truth 6DoF poses to provide quantitative trajectory accuracy for non-human entities, directly supporting the generalization claim.
3. **Report hyperparameter values** (\(T_c\), LoRA rank, LoRA \(\alpha\)) in the main paper rather than deferring to supplementary.
4. **Add confidence intervals or standard deviations** to the main quantitative results.

## Score and Decision

**Calibration Anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| MotionFlow (camera trajectory control) | OBTmkKBmQW.md | 4.00 | R1 | Weaker — ours has larger margins and more novel problem formulation; both have evaluation confounds |
| VD3D (camera control for transformers) | 0n4bS0R5MM.md | 6.20 | R1/R2 | Stronger — cleaner evaluation with user study, despite similar baseline fairness concerns |
| FlexMotion (motion generation) | 7652tHbbVE.md | 5.20 | R2 | Comparable — both have evaluation gaps; ours has better problem novelty |
| MGF-IMM (motion in-betweening) | xNwmWaq2KN.md | 5.33 | R2 | Comparable — ours has better method specification but worse evaluation fairness |
| Physics discovery in video diffusion | ZyLkNVHBZF.md | 5.50 | R2 | Slightly stronger — cleaner, more controlled experiments within a narrower scope |
| Video inverse problems via image diffusion | TRWxFUzK9K.md | 6.50 | R2 | Stronger — cleaner evaluation and better experimental support for claims |

**Round 1 bracket:** 3.5 – 7.5 (clear contribution but significant evaluation issues)

**Round 2 narrowing:** Between 4.00 (MotionFlow, Reject) and 6.20 (VD3D, Accept); closer to 5.0-5.5 range. The paper has stronger novelty than MotionFlow but weaker evaluation than VD3D. The Physics discovery paper (5.50) provides a useful anchor — it had clean, well-scoped experiments for a narrower set of claims, while this paper has broader claims but messier evaluation.

**Final score: 5.0.** The core contribution (first 6DoF multi-entity motion control, clean injector design, effective domain adaptation) is solid and the qualitative evidence is compelling. However, the confounded baseline comparison and the absence of quantitative motion accuracy for non-human entities are substantive evaluation weaknesses that prevent the paper's central claims from being fully supported as presented.

**Decision: Reject.** The paper requires major revisions to the evaluation methodology. If the authors address the prompt confound (identical prompts with documented failures) and add quantitative non-human evaluation (using synthetic ground truth from their own dataset), the paper would be a strong contribution. In its current form, the evidence does not adequately support the headline claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>