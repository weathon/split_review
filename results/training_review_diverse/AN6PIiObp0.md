Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes SALSA, a modification to PPO-based RLHF that replaces the standard single SFT reference model with a "model soup" — the weight-space average of two independently fine-tuned SFT models. The intuition is that the soup lives in a higher-reward region of parameter space, providing a better anchor for KL-regularized policy optimization. Experiments on Llama2-7B, Mistral-7B, and Gemma-2B across MT-Bench, Arena-Hard, and UltraFeedback show consistent win-rate advantages over vanilla PPO, with margins of ~1–7%.

## Strengths

1. **Well-motivated and simple intervention.** The idea to replace the reference model with a weight-space average is clean, easy to implement (one extra SFT run + averaging), and directly addresses a known limitation of PPO-based RLHF — that the KL penalty ties exploration to a potentially suboptimal anchor.

2. **Reward analysis validates the soup's advantageous position before RLHF.** Figures 3a/3b show that interpolation between two SFT models yields peak mean reward at α=0.5, and Figure 3c extends this to three models where the barycentric center achieves highest reward. This pre-RLHF evidence supports the claim that the soup is a better launching point, and this is a genuinely novel observation beyond the known accuracy benefits of model soups.

3. **Consistent directional advantage across 3 models × 3 benchmarks.** Table 1 reports SALSA vs. PPO win rates all above 50% (50.68%–57.19% across 9 comparisons). The consistency across models (Llama2-7B, Mistral-7B, Gemma-2B) and benchmarks (MT-Bench, Arena-Hard, UltraFeedback) provides support that the benefit is not limited to a single configuration.

4. **Ablations isolate the source of improvement.** The α-ablation (Figure 5a) shows peak at α=0.5 with degradation at extremes, ruling out trivial explanations. The MKL comparison (Figure 5b) shows that averaging two separate KL terms does not work, isolating the benefit to the weight-space averaging itself. The soup-n experiment (Figure 6) shows monotonic improvement with more models.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical uncertainty reported for any result.** The main win rates (Table 1) are in the 50.7–57.2% range — tight margins that could easily flip under noise. The paper provides no confidence intervals, no standard errors, and no mention of multiple training runs or seeds. With a single training run per condition and a noisy GPT-4 judge, the reader cannot assess whether these differences are reliable. This is the single most significant evidential gap.

2. **Central causal mechanism is asserted without measurement.** The paper repeatedly claims SALSA "permits greater deviation in KL divergence" / "allows for larger deviation in KL" (abstract, Section 4.2, conclusion), but never reports KL(π_θ ∥ π_ref) or KL(π_θ ∥ π_soup) over the course of training. Without these measurements, the claimed mechanism is entirely unverified — the improvement could come from the soup being a better initialization for PPO's reward optimization independently of any KL flexibility.

### Minor

3. **Hyperparameter β tuned on the evaluation metric.** The paper states (Section 4.1): "For both PPO and SALSA, we use the KL coefficient β that achieves the highest win rate." This is tuning on the test set without held-out calibration, risking overfitting to the specific benchmark. While both methods receive the same treatment, the reported win rates likely overstate the methods' true relative performance in a properly held-out setting.

4. **"Adjusted Win Rate" is never defined.** Table 1 uses this term throughout, but the paper offers no explanation of what "adjusted" means, how it differs from raw win rates, or what normalization/debiasing procedure (if any) was applied.

5. **The 3-model reward plane experiment is under-described.** The paper evaluates rewards "on a plane defined by these three models, both inside and outside this space" (Section 4.2) but provides no details on how the plane is parameterized, how many points were sampled, or whether the surface is smooth vs. noisy. This makes Figure 3c difficult to interpret or reproduce.

6. **Reward analysis uses the same reward model used for RLHF training.** The reward model trained on UltraFeedback is used both (a) to evaluate the soup's pre-RLHF reward and (b) to guide PPO/SALSA training. This circularity means the "higher reward" claimed for the soup could partly reflect biases in this specific reward model. Using an independent evaluator (e.g., GPT-4 reward scoring) for the reward analysis would strengthen the claim.

7. **No comparison to alternative reference-mitigating methods.** The paper discusses SimPO (reference-free) and Gorbatovski et al.'s dynamic reference model in related work, both addressing the same limitation of static reference models. While the paper scopes itself to PPO-based methods, comparing against at least one directly competing solution to the same problem would ground SALSA's performance in the broader landscape. This is a scope-constrained weakness — the paper's own comparisons within PPO are sufficient for its stated contribution, but the claimed advantage over "reference model limitations" would benefit from this contrast.

8. **No discussion of computational cost.** SALSA requires training an additional SFT model (π_other) plus the soup construction. While modest relative to the full RLHF pipeline, this cost should be acknowledged.

### Trivial

- The paper references a non-existent Section `\ref{sec:kl-divergence}` (line 255), which was likely stripped by the parser; this cross-reference would need to be resolved in a camera-ready version.

## Nice-to-Haves

- **KL divergence measurements over training** for both PPO and SALSA would directly validate or refute the paper's central mechanistic claim. This is listed as "Major" above because it is essential to the paper's narrative; including it would transform a major weakness into a strength.
- **Qualitative examples** of outputs where SALSA improves over PPO would strengthen the alignment narrative.
- **A comparison to the dynamic reference method** (Gorbatovski et al., 2024) would be the most directly relevant baseline outside standard PPO.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No comparison to DPO/SimPO"** — The paper explicitly scopes itself to PPO-based methods (Section 2: "In this paper, we focus on Proximal Policy Optimization (PPO) for its demonstrated robustness..."). DPO and SimPO are reward-free methods in a different methodological class. Demanding these comparisons evaluates the paper against the wrong class of expectations. A weakened version comparing to Gorbatovski et al.'s dynamic reference (which is reward-based) is retained as Minor #7 above.

2. **"Per-token vs sequence-level KL not clarified"** — The paper writes KL(π_θ(y|x) ∥ π_ref(y|x)), which is the standard sequence-level formulation used in PPO-based RLHF. The notation is conventional.

3. **"Initial penalty spike from π_ref initialization"** — The reviewer notes that KL(π_θ ∥ π_soup) ≠ 0 at initialization. This is a known property of changing the reference; the KL penalty simply starts at a non-zero value and is minimized during training. Not a meaningful flaw.

4. **"Reward model calibration concern"** — Using the trained reward model to evaluate pre-RLHF models is standard practice in the RLHF literature; requiring separate calibration studies is beyond what is normally expected.

5. **"No qualitative examples"** — Moved to Nice-to-Haves. The paper's contribution is quantitative (win rates, rewards); qualitative examples are supplementary.

6. **"No error bars on soup-n experiment"** — Already covered by Major weakness #1 (no uncertainty throughout).

## Novel Insights

None beyond the paper's own contributions. The core insight — that the model soup reference enables a better exploration starting point for PPO — is the paper's own. The reviewers do not surface any unappreciated implication or novel connection the authors missed.

## Suggestions

1. **Provide confidence intervals or bootstrap estimates** for all win rates reported in Table 1. Even a simple statement of "we ran training 3 times with different seeds" would substantially increase credibility.
2. **Report KL(π_θ ∥ π_ref) and KL(π_θ ∥ π_soup) over the course of training** for both PPO and SALSA to directly validate the claimed mechanism of "larger deviation in KL divergence."
3. **Define "Adjusted Win Rate"** clearly in the main text.
4. **Use a held-out validation set for β selection**, or at minimum acknowledge the limitation of tuning on the evaluation metric.
5. **Provide implementation details for the 3-model plane experiment** (parameterization, sampling grid, number of points).

## Score and Decision

The paper proposes a simple, well-motivated idea and provides consistent directional evidence across multiple models and benchmarks. However, the evidence is weakened by the absence of any statistical uncertainty quantification on narrow-margin results (50.7–57.2%), the complete lack of KL measurements to support the claimed causal mechanism, and tuning on the evaluation metric. These are addressable in revision, but in its current form the paper's central empirical claims are not sufficiently supported.

**Originality:** 6/10 — Model soup as a reference in PPO is novel.
**Importance:** 7/10 — Addressing exploration limitations in RLHF is relevant.
**Claims support:** 4/10 — Main claim is directionally supported but statistically ungrounded; mechanistic claim is entirely unverified.
**Soundness:** 5/10 — Experimental design has methodological gaps (β tuning, no variance).
**Clarity:** 6/10 — Generally well-written but plagued by undefined terms ("adjusted").
**Value to community:** 6/10 — Simple and useful if results hold; currently insufficiently evidenced.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>