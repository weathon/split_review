- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper applies reinforcement learning (RL) to fine-tune a raw-waveform TTS diffusion model (WaveGrad2), using UTMOS as a reward signal. It compares several policy-gradient methods from the text-to-image literature (RWR, DDPO, DPOK, KLinR) and introduces DLPO, which incorporates the original diffusion-model loss as a penalty in the reward function. Experiments show that DLPO, along with other KL-regularized methods (DPOK, KLinR), improves speech quality over the base model, while unregularized methods (RWR, DDPO) degrade. DLPO achieves the best automatic metric scores (UTMOS 3.65, NISQA 4.02) and receives 67% preference in a human listening test over the baseline.

## Strengths

- **First systematic application of online RL fine-tuning to a waveform-based TTS diffusion model.** The paper transfers techniques from text-to-image diffusion RL (RWR, DDPO, DPOK, KLinR) to the TTS setting and evaluates them under a consistent protocol, establishing how well these methods work for waveform generation. This is a concrete extension beyond prior work (e.g., Nagaram et al. on emotional expression in Grad-TTS).

- **DLPO achieves the highest automatic metric scores among all compared methods.** Table 1 shows DLPO attains UTMOS 3.65 (baseline 2.90) and NISQA 4.02 (baseline 3.74), while maintaining a low WER of 1.2%. The differences from baseline are supported by two-sample t-tests (p < 10⁻²⁰). Figure 1 confirms stable training curves for DLPO relative to methods that plateau or degrade.

- **Use of a separate evaluation metric (NISQA) guards against reward overfitting.** The paper explicitly uses NISQA, a different pretrained quality model trained on an independent corpus, to evaluate all methods, which strengthens the reliability of the reported results beyond the UTMOS reward model.

- **Ablation studies isolate the role of the diffusion-loss penalty.** The comparison with "OnlyDL" (diffusion loss alone) shows that the reward signal is necessary for meaningful improvement, and the 1-step vs. 10-step denoising ablation (Table 2) demonstrates that more denoising steps improve NISQA and WER. These ablations provide insight into what drives DLPO's performance.

- **Human preference study on a public demo page provides supplementary perceptual validation.** 67% of listener comparisons favor DLPO over the baseline, with only 14% preferring the baseline.

## Weaknesses

### Fatal
None.

### Major

1. **Gradient derivation in Eq. (11) is mathematically incorrect.** The paper specifies an objective in Eq. (10) that adds the diffusion loss as a penalty to the reward, then states the gradient in Eq. (11) as  
   `E[ -(α r - β ∇_θ ||ε̃ - ε_θ||²) ∇_θ log p_θ ]`.  
   This is not a correct derivation from Eq. (10). If the diffusion loss is intended as part of a scalar reward in a REINFORCE-style update, the ∇_θ should not appear inside the parentheses (the term should be `-β ||ε̃ - ε_θ||²`, not `-β ∇_θ ||ε̃ - ε_θ||²`). If a separate direct diffusion gradient is intended, it should be added outside the REINFORCE term, not multiplied by `∇_θ log p_θ`. The algorithm pseudocode (Algorithm 1) compounds the confusion by stating "Compute the gradient using Eq. (10)" — but Eq. (10) is the objective, not the gradient. This mathematical imprecision makes the method specification unreliable and hinders reproducibility. *Why it matters*: a reader cannot confidently implement DLPO from the equations as written, undermining the paper's central methodological contribution.

2. **The comparative evaluation lacks important training details and hyperparameter justification.** No learning rate or optimizer is reported for any method. All methods are run with the same `α=1, β=1` without explanation of how these values were chosen. Furthermore, β=1 is listed for DDPO in Table 1, yet DDPO as originally formulated has no β parameter — the paper never explains what β means for DDPO or whether DDPO was modified to include a diffusion-loss term. Without knowing whether the baselines were properly tuned, the claim that "RWR and DDPO do not improve TTS models" is weakened. *Why it matters*: the main comparative conclusions depend on fair and reproducible baselines; missing hyperparameters and an undefined β for DDPO undercut this comparison.

3. **Checkpoint selection and evaluation protocol are underspecified.** The paper saves "top three checkpoints" per model for evaluation but does not state the selection criterion (top by UTMOS? NISQA? some combination?). A single run is reported without variance across random seeds or training runs, so it is unclear whether the observed ranking is statistically robust beyond the reported t-tests against the baseline. *Why it matters*: the main results table (Table 1) presents point estimates with no variance, making it impossible to assess the significance of differences between methods (e.g., DLPO vs. DPOK on NISQA: 4.02 vs. 3.76).

### Minor

1. **Human evaluation is small-scale and lacks statistical reporting.** The listening test uses 11 raters and 20 audio pairs. While the 67% preference rate is suggestive, no confidence interval or significance test is provided, and the sample size is modest for a strong claim about perceptual quality. (The automatic metrics are the primary evidence, so this is not a fatal issue.)

2. **No ablation of the penalty weight β.** The sensitivity of DLPO to its key hyperparameter β is not explored. A sweep or trade-off analysis (reward vs. diffusion-loss alignment) would strengthen understanding of the method's behavior.

3. **Training curves are shown for only 160 episodes.** Some methods (e.g., KLinR) appear to decline after 120 episodes; it is unclear whether further training would change the relative ranking. The paper's conclusions are drawn from a fixed 5.5-hour budget rather than from convergence.

4. **Statistical tests compare only DLPO vs. baseline, not DLPO vs. other methods.** The reported t-tests (p < 10⁻²⁰) compare DLPO against the base model but not against DPOK or KLinR. No multiple-comparison correction is applied. This limits the statistical support for the claim that DLPO "outperforms" other methods.

### Trivial
None.

## Nice-to-Haves

- A hyperparameter search (or at least a sensitivity analysis) for each RL baseline, especially RWR and DDPO, to determine whether they can be made to work with appropriate scaling or KL control.
- Reporting results across multiple random seeds with means and standard deviations.
- An analysis of how the diffusion-loss penalty weight β affects the trade-off between reward optimization and speech quality.

## Removed Points

The following criticisms from the inputs were removed after cross-checking against the paper:

- *"The formulation of OnlyDL is never specified precisely"* — **Removed.** The paper explicitly gives the OnlyDL loss function on line 203: `−log p_θ(x_{t-1}|x_t,c) * (−||ε̃ − ε_θ||²)`.
- *"Novelty claim should be qualified by Nagaram et al."* — **Removed.** The paper already cites Nagaram et al. (2024) in the Related Works section and distinguishes their work on emotional expression from the paper's focus on speech quality.
- *"RWR and DDPO might improve with more training or different hyperparameters"* — **Removed (as a standalone argument).** This is speculative; the paper's claim that they "do not improve TTS models" is about the tested conditions. The valid concern about missing hyperparameter search is retained in Major weakness #2.
- *"Methods might improve further with longer training beyond 160 episodes"* — **Removed as a specific criticism.** This is speculative without evidence; the observation that KLinR declines is retained in Minor weakness #3 as a concern about limited training horizon.
- *"Missing learning rate, optimizer details"* — **Retained** in Major weakness #2 (not removed, as these are important for reproducibility).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the gradient derivation.** Provide a mathematically precise expression for the DLPO update. If the diffusion loss is used as part of the reward in REINFORCE, state it simply as `E[-(α r - β||ε̃ - ε_θ||²) ∇_θ log p_θ]`. If a separate direct gradient of the diffusion loss is added, write it as a sum of the REINFORCE term and the direct gradient term. Clarify the pseudocode in Algorithm 1 to match.

2. **Report learning rate, optimizer, and checkpoint selection criteria.** These are essential for reproducibility. If the same setting (e.g., Adam with a fixed LR) was used for all methods, state it explicitly.

3. **Clarify the meaning of β for each baseline in Table 1**, especially for DDPO and RWR. If β is not applicable to a method, leave it as "—" (as done for RWR). If DDPO was modified to include a diffusion-loss term, describe the modification.

4. **Report variance** across at least 2–3 seeds or training runs for the main results table, so readers can assess the stability of the reported ranking.

5. **Add confidence intervals to the human evaluation** and consider increasing the number of raters and/or audio pairs.
