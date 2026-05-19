Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket:** I placed the paper between 5.0 and 7.0 based on comparisons to weak anchors (avg 2-3, papers with major flaws) and strong anchors (avg 8+, much higher-impact work on different topics).

**Round 2 narrowing:** The paper compares favorably to the 5.0-5.5 anchors (Promise at 5.0, M2TPT at 5.33, VisCoP at 5.5, CRPA at 5.0, L-TTA at 5.0) due to its clearer method and more thorough ablation. It is comparable to the 6.0 anchors (Compo-ReAlign at 6.0, PSP at 6.0, RLAP-CLIP at 6.0) — similar experimental rigor but the λ-selection ambiguity slightly weakens the empirical claims relative to these papers.

**Final score: 6.0** — solid contribution with good experimental methodology, held back by the hyperparameter selection ambiguity and overclaim on domain generalization.

---

## Summary

The paper proposes CoPrompt, a fine-tuning method for vision-language models that enforces a consistency constraint between a trainable (prompt+adapter) model and the frozen pre-trained encoder, using LLM-generated text perturbations and image augmentations as regularized inputs. The method combines prompt tuning and adapters in a single framework. Evaluated across base-to-novel generalization (11 datasets), cross-dataset transfer (10 datasets), and domain generalization (4 ImageNet variants), it achieves 80.48% harmonic mean in base-to-novel — a +0.51% improvement over PromptSRC — and 67.00% in cross-dataset evaluation — +0.70% over MaPLe.

## Strengths

1. **Consistency-constrained training that demonstrably reduces overfitting.** The ablation study (Table 3) shows that removing the consistency constraint while keeping adapters causes the harmonic mean to drop to 78.45% — even *below* the MaPLe baseline (78.55%). This cleanly demonstrates that the additional learnable capacity from adapters harms generalization without the regularizer, making a clear empirical case for the core mechanism.

2. **Enables training more prompt layers without degradation.** CoPrompt achieves its best accuracy using all 12 prompt layers (Table 6a), whereas prior work MaPLe peaked at 9 layers. This provides concrete evidence that the consistency constraint allows more learnable parameters to be safely trained in few-shot settings — a non-obvious benefit.

3. **Thorough, multi-faceted ablation study.** The paper systematically ablates each component (consistency, input perturbations, adapters), examines modality-specific effects (text vs. image consistency, text vs. image adapters), evaluates different consistency criteria (cosine, L1, MSE), compares LLM choices (GPT-2 vs. GPT-3), and studies augmentation strategies — all on the same benchmark. This level of dissection is more comprehensive than most papers in this area.

4. **Cross-dataset improvement is robust across 8 of 10 target datasets.** In Table 2, CoPrompt improves on 8 out of 10 target datasets compared to MaPle and PromptSRC, with a particularly strong gain on EuroSAT (51.90% vs. next best 48.06%), suggesting the method offers genuine generalization benefits, not just a narrow advantage.

## Weaknesses

### Fatal
None.

### Major

1. **Hyperparameter (λ) selection protocol is unclear and potentially unfair.** The sensitivity analysis (Table 6, `weight_sensitivity`) shows that the optimal λ varies substantially across datasets: λ=0.1 for EuroSAT (85.84 HM), λ=2 for Aircraft (39.76) and UCF (83.07), and λ=8 for most others. The reported main results match these *specific per-dataset optimal values*. If CoPrompt was tuned per-dataset while baselines (MaPLe, PromptSRC) used fixed hyperparameters as reported in their original papers, the comparison is unfair. Moreover, computing the average HM with a *fixed* λ=8 across all 11 datasets yields approximately 79.58%, which falls *below* PromptSRC's 79.97%. This means the claimed +0.51% improvement may be entirely an artifact of per-dataset λ selection. The paper must state the exact selection protocol and, ideally, verify that results hold with a single λ or under the same per-dataset tuning regime applied to baselines.

### Minor

1. **Abstract overclaims on domain generalization.** The abstract states that "CoPrompt outperforms existing methods on... domain generalization," but Table 4 shows CoPrompt achieves 60.42% average accuracy vs. PromptSRC's 60.65% and Bayesian Prompt's 60.44%. The paper's main text correctly says "comparable performance," but the abstract is inaccurate. The domain generalization results should be characterized honestly.

2. **Method description reuses variable name without clarification.** The consistency loss L_cc is redefined in Equations (3), (4), and (5) with different meanings (same-input consistency → perturbed-input consistency → adapter-augmented consistency). While the final definition in Eq. (5) is the actual loss used, the reuse of L_cc across all three equations without renaming or distinguishing them is confusing. A reader could mistake the intermediate definitions for the final objective.

### Trivial

None.

## Nice-to-Haves

- Adding confidence intervals or variance estimates across runs would help assess whether the modest improvements (+0.51% HM) are statistically reliable, though this is not standard practice in this literature.

- A "Limitations" section discussing the sensitivity to λ and the domain generalization shortfall would strengthen the paper's honesty.

## Removed Points

These points were identified in the inputs but removed after cross-checking against the paper:

1. **"Not clear which model receives which input"** (Harsh Critic): The paper's equations (4)-(5) are explicit: φ(s_y) is the frozen encoder on LLM text, φ^a(φ(t_y)) is the learnable adapter on prompted text, θ(x') is the frozen encoder on augmented images, and θ^a(θ(i)) is the learnable adapter on prompted images. This is clear from the notation.

2. **Missing appendix, proofs in appendix, absent references** (Harsh Critic): Per instructions, these are parser artifacts and should not be counted as weaknesses.

3. **Missing related works** (Harsh Critic): Per instructions, this should not be mentioned since external sources cannot confirm omissions.

4. **Request for additional baseline comparing PromptSRC with adapters** (Harsh Critic): This is scope creep — the paper is evaluated against published methods in its setting; requesting bespoke re-implementations is not a valid criticism.

5. **Demand for a "Limitations" section** (Harsh Critic): A useful suggestion but not a flaw in the paper's technical contribution.

6. **Generic strengths from Strength Finder** removed as generic/superficial: Several were rephrased and condensed into the strengths section above; the rest (e.g., "addressed an important problem") are too generic to retain.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's suggestion to reframe the contribution around the consistency constraint (rather than the adapter-prompt combination) is a useful framing insight: the ablation clearly shows the consistency mechanism is the primary driver of improvement, while adapters contribute a smaller but non-trivial secondary gain. This reframing would make the paper's narrative more precise.

## Suggestions

1. **Clarify the λ selection protocol explicitly.** State whether per-dataset optimal λ was chosen for the main results. If so, provide a table showing each dataset's λ. Ideally, report results with a single, fixed λ (e.g., λ=8) to demonstrate robustness, and discuss why EuroSAT requires a different setting.

2. **Correct the abstract's domain generalization claim** to say "competitive performance" rather than "outperforms."

3. **Rename the intermediate L_cc definitions** in Equations (3)-(5) or add a forward reference explaining which definition is the final one used in the overall loss.

4. **Add a brief limitations paragraph** acknowledging the λ sensitivity and the domain generalization results.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>