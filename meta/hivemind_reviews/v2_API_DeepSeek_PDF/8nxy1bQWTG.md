## Summary
# Final Review Report

## Summary

This paper presents DiffEnc, a modification of variational diffusion models (VDM) that introduces a learned, time-dependent encoder to parameterize the mean of the forward diffusion process. The encoder is used only during training and discarded at sampling time, so the approach incurs no additional sampling cost. The paper makes two main contributions: (1) a class of diffusion models with a data- and depth-dependent mean function (DiffEnc), and (2) a theoretical analysis of relaxing the assumption that forward and backward noise variances are equal, proving that in the continuous-time limit they must be equal for a well-defined ELBO.

The empirical results show a modest but statistically significant improvement in bits-per-dimension (BPD) on CIFAR-10 (2.62 vs 2.64, p=0.03) using a large model configuration, driven primarily by improved diffusion loss. On ImageNet32, the total loss is identical to the VDM baseline (3.46 BPD). The learned encoder produces time-dependent transformations that are qualitatively interpretable: fine-grained edge enhancement at early timesteps and global structure encoding at late timesteps.

**Strengths:** The idea is clean and well-motivated — adding flexibility to the forward process without affecting sampling is practically valuable. The theoretical analysis of the variance ratio is rigorous and provides useful insights about weighted losses in finite-depth hierarchies. The experimental methodology is sound, with multi-seed reporting and ablation of trainable vs. non-trainable encoders.

**Core weaknesses:** (1) The empirical gains are modest (0.02 BPD on one dataset) and do not generalize to ImageNet32, limiting the scope of the claimed improvement. (2) A key methodological component — the approximation of the encoder gradient in the generative counterterm — is acknowledged as approximate but never validated. (3) The contribution on variance relaxation (C2) is purely theoretical with no empirical demonstration of its practical benefit. (4) The significance claim (p=0.03) relies on only 3 seeds and is fragile. (5) The related-work section is organized as a list rather than structured comparison.

**External literature verification:** Not available in this run (Retrieval-Disabled Mode). Novelty and comparison conclusions are deferred for manual verification.

## Strengths
1. **Clean and well-motivated idea**: The core concept — introducing a learnable time-dependent encoder in the forward diffusion process that is discarded at sampling time — is elegant and practically motivated. It addresses a genuine limitation of standard diffusion models (fixed, data-independent forward process) without compromising sampling efficiency.

2. **Rigorous theoretical analysis of variance ratio**: The analysis of the assumption that $\sigma_P^2 = \sigma_Q^2$ is thorough. The derivation of the optimal $\sigma_P^2$ in closed form (Appendix F) and the proof that the variances must be equal in the continuous-time limit for a well-defined ELBO (Appendix G) are significant theoretical contributions. The connection to weighted diffusion losses for finite-depth hierarchies is insightful.

3. **Sound experimental methodology**: The experiments use multiple seeds (3-5), report standard errors, and include both trainable and non-trainable encoder variants as controls. The ablation between fixed and trainable noise schedules provides useful insights. The comparison of loss components (total, latent, diffusion, reconstruction) helps isolate where the encoder provides benefit.

4. **Qualitative analysis of learned encoder**: Figure 2 and Appendix W provide informative heatmap visualizations showing that the encoder learns distinct behaviors at different timesteps — fine-grained edge enhancement at early timesteps evolving to global structure encoding at late timesteps. This analysis helps build intuition about what the encoder learns.

5. **Honest discussion of limitations**: The paper acknowledges the increased training cost, the fact that likelihood and visual quality are not directly linked, and that the approach does not improve sampling speed relative to other diffusion acceleration techniques. The code is provided for reproducibility.

## Weaknesses
1. **Limited empirical scope (Major)**: The headline result — 0.02 BPD improvement on CIFAR-10 — is the only dataset where DiffEnc improves total loss. On ImageNet32, the total loss is identical to the VDM baseline (3.46 BPD). On MNIST and small CIFAR-10 models, improvements are within standard error. The abstract and introduction frame this as a general improvement, but the evidence only supports a dataset-specific, model-size-dependent benefit.

2. **Unvalidated gradient approximation (Major)**: In Section 4, the paper acknowledges that the gradient $dx_\phi/d\lambda_t$ for the trainable encoder cannot be straightforwardly expressed in terms of $\hat{x}_\theta$, and uses the same approximation as the non-trainable encoder ($\sigma_t^2 \hat{x}_\theta$). This approximation is never validated — no ablation, no empirical comparison, no analysis of the error it introduces. Since this term appears directly in the training loss (Eq. 19), an inaccurate approximation would mean the model is not actually optimizing the intended objective.

3. **Fragile statistical significance (Major)**: The p-value of 0.03 is based on a t-test with only 3 seeds per condition. With such a small sample, the result is highly sensitive to individual seed outcomes. Additionally, no correction for multiple comparisons is reported (two datasets, multiple model sizes). The improvement is presented as "statistically significant" without the necessary caveats about sample size.

4. **Variance-ratio contribution is purely theoretical (Medium)**: The second contribution — relaxing the $\sigma_P = \sigma_Q$ assumption — is thoroughly analyzed theoretically, but has zero empirical validation. The paper explicitly sets $w_t = 1$ for all experiments and leaves the finite-depth weighted loss to "future work." A purely theoretical contribution with no experimental counterpart weakens the paper's overall impact.

5. **Overclaim in contributions (Medium)**: The first contribution claims "a new, more powerful class of diffusion models." The term "more powerful" is not bounded to specific settings, and the only clear win is 0.02 BPD on CIFAR-10. On the FID metric, the two models produce nearly indistinguishable scores (Table 8).

6. **Related work is a list (Minor)**: Section 6 reads as a chronological survey rather than a structured comparison. The paper would benefit from organizing related methods by comparison axes (e.g., linear vs. nonlinear corruptions, data-space vs. latent-space encodings) with a side-by-side comparison table.

7. **Missing quantitative limitation on training cost (Minor)**: The paper notes the approach has "longer training time" but never quantifies this. For practitioners evaluating whether to adopt DiffEnc, knowing whether the overhead is 10%, 50%, or 100% is essential.

## Key Issues
### Issue 1 (Top Priority): Unvalidated gradient approximation in the core training loss
**Page 5 - Section 4: Parameterization of the Encoder and Generative Model**

The paper introduces a counterterm in $\mu_P$ to approximately cancel the mean shift term $dx_\phi/d\lambda_t$. For the trainable encoder, the true gradient is:
$$\frac{dx_\phi}{d\lambda_t} = \alpha_t^2 \sigma_t^2 x + \sigma_t^2 \frac{dy_\phi}{d\lambda_t} - \alpha_t^2 \sigma_t^2 y_\phi$$
The paper acknowledges that the $dy_\phi/d\lambda_t$ and $y_\phi$ terms "cannot as straightforwardly be expressed in terms of $\hat{x}_\theta$" and uses $\sigma_t^2 \hat{x}_\theta$ as an approximation — the same formula used for the much simpler non-trainable encoder. The residual error of this approximation is $\sigma_t^2(dy_\phi/d\lambda_t - \alpha_t^2 y_\phi)$, which could be substantial when the encoder learns nontrivial transformations. **No validation of this approximation is provided.** Since this term appears directly in the loss (Eqs. 18-20), an inaccurate approximation means the model optimizes a biased objective. This is a major validity concern.

**Required action:** Add a validation experiment comparing the approximate gradient against a finite-difference or Monte Carlo estimate on a trained encoder. Report the relative error across timesteps. If the error is large, discuss implications or develop an exact gradient estimator.

### Issue 2 (High Priority): Limited empirical evidence for core claim
**Page 7 - Section 5: Results**

The central claim that DiffEnc "improves likelihood" is supported by a single dataset (CIFAR-10, 0.02 BPD improvement with p=0.03, 3 seeds). On ImageNet32, the improvement is zero. On MNIST, improvements are within standard error. The paper's narrative presents this as a general result, but the evidence only supports a specific claim: "DiffEnc improves likelihood on CIFAR-10 under a large-model configuration with a fixed noise schedule." The broader claim of "more powerful" diffusion models is not justified by the available evidence.

**Required action:** (a) Restructure the abstract and conclusion to explicitly bound the empirical scope. (b) Add a discussion section analyzing why ImageNet32 shows no improvement — is it model capacity, data diversity, or the fixed noise schedule? (c) Report seed-level results for transparency.

### Issue 3 (Medium Priority): Fragile statistical significance
**Page 8 - Section 5: Results (P8 L12)**

The p-value of 0.03 is based on a one-sided t-test over only 3 seeds per condition. With such a small sample, the test has low power and is sensitive to outliers. Additionally, the paper tests multiple datasets and model configurations without correcting for multiple comparisons. A p-value of 0.03 that does not survive multiple-testing correction would weaken the significance claim considerably.

**Required action:** (a) Report bootstrap confidence intervals or Bayesian credible intervals in addition to the t-test. (b) Apply a Bonferroni or Benjamini-Hochberg correction if multiple hypotheses are tested. (c) Consider increasing the number of seeds, at least for the CIFAR-10 large-model comparison.

### Issue 4 (Medium Priority): Variance-ratio contribution lacks empirical validation
**Page 2 - Introduction/Contributions, Page 5 - Section 4**

The paper makes a theoretical contribution about the optimal $\sigma_P^2$ and the necessity of equal variances in continuous time. However, all experiments use $w_t = 1$ (equal variances), so this contribution has no experimental component. The paper mentions that weighted losses for finite depth are "of interest" but leaves this to future work. A purely theoretical contribution without any empirical demonstration limits the paper's overall impact.

**Required action:** At minimum, include a small-scale experiment (e.g., MNIST or toy data) demonstrating the effect of using the optimal $\sigma_P^2$ vs. $\sigma_P^2 = \sigma_Q^2$ in a finite-depth setting. This would validate that the theoretical analysis translates to a practical benefit.

### Issue 5 (Medium Priority): Overclaim in contribution statements
**Page 2 - Contribution list**

The contribution list states "We define a new, more powerful class of diffusion models." The word "more powerful" is ambiguous and not directly supported by the empirical evidence. The only clear improvement is 0.02 BPD on CIFAR-10. On FID scores, the models are statistically indistinguishable. On ImageNet32, they are identical. The paper should qualify "more powerful" with the specific setting where improvement is observed.

**Required action:** Replace "more powerful" with a specific, bounded claim such as "We define a class of diffusion models that achieves improved likelihood on CIFAR-10 under large-model configurations."

## Actionable Suggestions
### S1 (Must): Validate the gradient approximation for the trainable encoder counterterm
**Target: Page 5 - Section 4, Eqs. (17)-(18)**

Add a validation experiment comparing the approximate gradient $\sigma_t^2 \hat{x}_\theta$ against a numerical estimate of $dx_\phi/d\lambda_t$ (computed via finite differences through the encoder network) on a held-out validation set. Report the relative L2 error across timesteps $t \in [0, 1]$. If the error exceeds, say, 20% of the gradient norm for any $t$, either develop an exact gradient estimator (e.g., by reparameterizing the counterterm to use $\partial y_\phi/\partial \lambda_t$ directly) or explicitly bound the bias and discuss implications.

**Cost:** Low-to-medium (one additional evaluation script, no new training).

### S2 (Must): Bound the empirical scope of claims
**Target: Abstract (Page 1), Contribution list (Page 2), Conclusion (Page 9)**

Revise the following:
- **Abstract**: Replace "achieves a statistically significant improvement in likelihood on CIFAR-10" with a statement that contextualizes the gain (0.02 BPD) and notes that ImageNet32 results are comparable to the baseline.
- **Contribution list**: Replace "more powerful class of diffusion models" with "a class of diffusion models that achieves improved likelihood on CIFAR-10."
- **Conclusion**: Add an explicit sentence: "On ImageNet32 and with smaller model configurations, the total loss was comparable to the VDM baseline, suggesting that the benefit of the learned encoder is most pronounced with larger models and datasets of intermediate complexity."

### S3 (Must): Improve statistical reporting
**Target: Page 7-8 - Section 5: Results**

(a) Report individual seed results for the CIFAR-10 large-model comparison in a supplementary table.
(b) Add bootstrap-based 95% confidence intervals for the BPD difference between DiffEnc-32-4 and VDMv-32.
(c) Note that the p-value of 0.03 is uncorrected for multiple comparisons, and state whether it survives a Bonferroni correction (e.g., $\alpha = 0.05/3 = 0.017$ for three dataset comparisons).
(d) Consider training 5+ seeds for the key CIFAR-10 comparison to increase reliability.

### S4 (Should): Demonstrate the variance-ratio contribution empirically
**Target: Page 5 - Section 4, Figure (new)**

Add a small-scale experiment (e.g., on MNIST with a finite-depth hierarchy, e.g., T=100) comparing:
- Standard diffusion ($\sigma_P = \sigma_Q$)
- Optimal $\sigma_P^2$ (from Eq. 70) estimated during training
- Fixed non-equal $\sigma_P$ (e.g., $w_t = 2$)

Report likelihood and qualitative samples. This would validate that the theoretical analysis translates to practical benefit, even if modest.

**Cost:** Low (can reuse existing MNIST training setup with minor modifications).

### S5 (Should): Restructure Related Work by comparison axes
**Target: Page 8-9 - Section 6**

Reorganize into three subsections or comparison-driven paragraphs:
1. **Linear data-space corruptions**: Blurring diffusion [Hoogeboom & Salimans, 2022; Rissanen et al., 2022], Soft diffusion [Daras et al., 2022]. Key difference: DiffEnc uses nonlinear, learned transformations.
2. **Nonlinear data-space corruptions**: Implicit nonlinear diffusion [Kim et al., 2022b], Neural diffusion models [Bartosh et al., 2023]. Key differences: no invertibility requirement, prediction target.
3. **Latent-space diffusion**: Latent diffusion [Rombach et al., 2022], score-based latent models [Vahdat et al., 2021]. Key difference: DiffEnc operates in data space with a time-dependent encoder.

### S6 (Should): Quantify the training overhead
**Target: Page 9 - Section 7: Limitations**

Add one sentence quantifying the additional training cost, e.g.: "Training DiffEnc requires approximately [X]% more wall-clock time per step compared to the baseline VDM, primarily due to the forward and backward passes through the encoder network."

### S7 (Nice-to-have): Add intuitive interpretation for optimal sigma_P formula
**Target: Page 4 - Section 2: Preliminaries**

Add a sentence after Eq. (70): "This result has a natural interpretation: the optimal generative variance equals the diffusion variance plus the expected squared prediction error. When the denoising model is accurate, the generative process operates near the minimal noise level; when uncertain, it adds extra stochasticity."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: Diffusion models are SOTA across many domains (laundry list of applications).
- P2-P3 (column break): Diffusion as hierarchical VAEs with three restrictions; the paper relaxes restriction (1).
- P3-P4: The encoder idea, loss roadmap, experiments preview, and variance-ratio analysis.
- Contribution bullet list.

**Problems:** (1) The opening paragraph does not establish stakes or a research gap — it reads as a literature review. (2) The paper's central tension (fixed forward process vs. desired flexibility) appears only midway through the introduction. (3) The three core questions (what is missing, what is solved, why is it better) are answered implicitly rather than explicitly.

### Proposed Storyline (Recommended)

**Title:** Keep current title but consider adding a problem-method-effect framing: "DiffEnc: Improving Diffusion Model Likelihood with a Learned Time-Dependent Encoder" — this makes the practical payoff explicit.

**Abstract Outline (5 sentences):**
- S1 (Problem): "Diffusion models treat the forward corruption process as fixed and data-independent, limiting their ability to adapt to input structure."
- S2 (Gap): "While this simplicity enables efficient training, it prevents the model from reshaping the signal-to-noise trajectory to make the denoising task easier."
- S3 (Method): "We introduce DiffEnc, which replaces the fixed mean of the diffusion process with a learned, time-dependent encoder that is used only during training and discarded at sampling time."
- S4 (Theory): "Additionally, we analyze the ratio of forward and backward noise variances, proving that equal variances are required in continuous time while finite hierarchies admit weighted loss formulations."
- S5 (Result): "DiffEnc improves likelihood on CIFAR-10 by 0.02 bits per dimension (p=0.03) with no additional sampling cost, while on ImageNet32 the total loss is comparable to the baseline."

### Introduction Outline (5 paragraphs)

**P1 — Establish territory and gap:**
- Open with the success of diffusion models, but immediately pivot to their limitation.
- "Diffusion models have achieved state-of-the-art results in generative modeling, yet a key design choice — the fixed, data-independent forward process — limits their flexibility."
- "This rigidity means the corruption trajectory cannot adapt to input structure, potentially making the denoising task harder than necessary."

**P2 — Diffusion as hierarchical VAE and the three restrictions:**
- Explain the VAE perspective (Sohl-Dickstein, Ho, Kingma et al.).
- List the three restrictions: fixed forward process, Markovian generative model, parameter sharing.
- State clearly: "This paper relaxes only the first restriction — the fixed forward process — while preserving the Markov property and parameter sharing that make diffusion models scalable."

**P3 — Proposed solution (DiffEnc):**
- Introduce the time-dependent encoder intuition.
- "We replace the mean of the forward diffusion with a learned function $x_\phi(\lambda_t)$ that depends on both the data and the timestep."
- Key advantage: "Because the encoder is discarded after training, sampling is unaffected."
- Brief roadmap: Section 3 derives the modified loss; Section 4 introduces the counterterm.

**P4 — Variance-ratio analysis:**
- Second contribution: relaxing $\sigma_P = \sigma_Q$.
- "This relaxation yields a weighted loss interpretation for finite depth, but we prove that continuous-time ELBO requires equal variances."
- Set expectations: "This analysis is theoretical; all experiments use the continuous-time formulation with equal variances."

**P5 — Contributions and paper outline:**
- Three contributions (bounded wording):
  1. "DiffEnc: a class of diffusion models with a time-dependent encoder that improves likelihood without increasing sampling cost."
  2. "Theoretical analysis of the variance ratio, including the optimal $\sigma_P^2$ and the necessity of equal variances in continuous time."
  3. "Empirical demonstration of improved likelihood on CIFAR-10, with analysis of the learned encoder's time-dependent behavior."

### Alternative Storyline 2 (Application-First)

Restructure the entire paper around the practical question: "Can we make diffusion models more flexible without making them slower?" Use the encoder as a specific answer to this question. This would make the paper more approachable to practitioners but may sacrifice depth on the VDM formulation.

## Priority Revision Plan
### P0 — Must-fix before any resubmission

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0 | Gradient approximation unvalidated (Issue 1) | Add validation experiment; report error across timesteps | High — addresses core validity concern | Low-Med |
| P0 | Overclaim in contributions (Issue 5) | Rewrite abstract, contribution list, conclusion with bounded wording | High — aligns claims with evidence | Low |
| P0 | Limited empirical scope not acknowledged (Issue 2) | Add explicit scope bounds in abstract and conclusion | High — clarifies truthful scope | Low |

### P1 — Strongly recommended

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1 | Fragile significance (Issue 3) | Add bootstrap CIs, multi-seed results, discuss multiple comparisons | Medium — strengthens statistical credibility | Low-Med |
| P1 | Variance-ratio contribution lacks empirical demo (Issue 4) | Small-scale MNIST experiment with optimal vs. equal sigma_P | Medium — validates theoretical contribution | Low |
| P1 | Related Work as list (Weakness 6) | Reorganize by comparison axes | Medium — improves positioning clarity | Low |

### P2 — Quality improvements

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2 | Missing training cost quantification (Weakness 7) | Add one sentence with wall-clock overhead | Low — aids reproducibility | Low |
| P2 | Introduction narrative (Storyline) | Restructure per recommended outline | Medium — improves reader engagement | Medium |
| P2 | Table 1 ImageNet comparison clarity | Add column for ImageNet version | Low — prevents confusion | Low |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Issue: Unvalidated gradient approximation]
    -> [Fix: Finite-difference validation experiment]
    -> [Expected: Confirm or bound approximation error]
    -> [If error small: Add validation appendix and note in text]
    -> [If error large: Develop exact gradient estimator]

[Issue: Overclaiming and limited empirical scope]
    -> [Fix: Rewrite abstract, contributions, conclusion]
    -> [Expected: Claims match evidence boundaries]

[Issue: Fragile statistical significance]
    -> [Fix: Bootstrap CIs, more seeds, correction for multiple comparisons]
    -> [Expected: More reliable significance assessment]

[Issue: Variance-ratio contribution is purely theoretical]
    -> [Fix: MNIST experiment with optimal vs. fixed sigma_P]
    -> [Expected: Empirical validation of theoretical claims]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Likelihood comparison on CIFAR-10 | CIFAR-10 train/test, fixed noise schedule, VDMv-32 vs DiffEnc-32-4, 8M steps, 3 seeds | BPD (total, latent, diffusion, reconstruction) | DiffEnc-32-4: 2.62 BPD; VDMv-32: 2.64 BPD (0.02 BPD diff, p=0.03) | C1, C3 | Only 3 seeds; p=0.03 uncorrected; effect size small |
| E2 | Likelihood comparison on ImageNet32 | ImageNet32 (Chrabaszcz), fixed noise schedule, VDMv-32 vs DiffEnc-32-8, 1.5M steps, 3 seeds | BPD | Both: 3.46 BPD | None (null result) | Not discussed as limitation |
| E3 | Likelihood comparison on MNIST | MNIST train/test, fixed+trainable noise, VDMv-8 vs DiffEnc-8-2, 2M steps, 5 seeds | BPD | 0.003-0.007 BPD improvement (within SE) | C1 (weak) | Small model, small improvement |
| E4 | Non-trainable encoder ablation | Same as E1/E3 but with DiffEnc-8-nt (non-trainable x_nt) | BPD | Diffusion loss always worse than VDM | Supports C1 by negative contrast | No analysis of why non-trainable hurts |
| E5 | FID comparison | CIFAR-10, 50K samples, DiffEnc-32-4 vs VDMv-32 | FID (10K/50K, train/test) | Statistically indistinguishable (all within SE) | None (qualitative only) | Not optimized for FID; mentioned but under-discussed |
| E6 | Encoder visualization | MNIST, DiffEnc-8-2, encoded images at t={0,0.3,0.5,0.7,0.8,0.9} | Visual | Encoder preserves identity up to t=0.7, blurring after t=0.8 | C1 (qualitative) | Subjective; no quantitative metric |
| E7 | Heatmap analysis | CIFAR-10, all 10 classes, (x_t-x_s)/(t-s) for t=0.1..1.0 | Heatmap visualization | Fine changes near t=0, global changes near t=1 | C1 (qualitative) | Summed over channels loses color info |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper contributes a novel architecture (time-dependent encoder) and theoretical analysis (variance ratio). However, the empirical demonstration of new knowledge is limited by (a) the small effect size on CIFAR-10, (b) the null result on ImageNet32, and (c) the lack of validation for the gradient approximation.

**Reproducibility:** The paper provides code, detailed architecture descriptions, and training hyperparameters. However, the unvalidated gradient approximation makes it unclear whether the reported results are reproducible with independent implementations, since the loss function depends on an ad-hoc approximation.

**Potential to Change Practice:** DiffEnc's conceptual contribution (learned encoder, discarded at sampling) is practically valuable if it generalizes beyond CIFAR-10. The current evidence does not yet establish this generalization, limiting the paper's potential impact on practice.

### Proposed Research Experiments

**Experiment P0-A: Gradient approximation validation**
- **Target Claim:** The approximation $\sigma_t^2 \hat{x}_\theta$ is a valid proxy for $dx_\phi/d\lambda_t$.
- **Hypothesis:** The relative error between the approximate and true gradients is below 10% for most timesteps.
- **Minimal Design:** Use a pre-trained DiffEnc-32-4 model. Compute $dx_\phi/d\lambda_t$ numerically via central finite differences through the encoder. Compare against $\sigma_t^2 \hat{x}_\theta(\lambda_t)$ at 20 evenly spaced timesteps. Report mean relative L2 error.
- **Controls/Baselines:** Compare against zero baseline (no counterterm) and against the non-trainable encoder gradient.
- **Metrics:** Relative L2 error $||\text{approx} - \text{exact}||_2 / ||\text{exact}||_2$.
- **Success Criterion:** Relative error < 20% for all $t$ and < 10% for $t \in [0.2, 0.8]$.
- **Estimated Cost/Time:** 1-2 days (requires running a pre-trained model through evaluation, no training).
- **Expected Paper-Quality Gain:** High — validates or bounds the core methodological concern.

**Experiment P0-B: Statistical robustness**
- **Target Claim:** "Statistically significant improvement" on CIFAR-10.
- **Hypothesis:** The 0.02 BPD gap persists with more seeds and survives multiple-testing correction.
- **Minimal Design:** Train VDMv-32 and DiffEnc-32-4 for 5 additional seeds each (total 8 per condition). Report bootstrap 95% CI on the BPD difference. Apply Bonferroni correction for 3 comparisons.
- **Controls/Baselines:** Same as existing experiments.
- **Metrics:** BPD, bootstrap CI width, adjusted p-value.
- **Success Criterion:** p-adjusted < 0.05 AND bootstrap CI excludes zero.
- **Estimated Cost/Time:** High (each training run ~3-5 GPU-days for large models). Fallback: use existing checkpoints with different random seeds.
- **Expected Paper-Quality Gain:** Medium-high — strengthens confidence in the main result.

**Experiment P1-A: Variance-ratio empirical demonstration**
- **Target Claim:** C2 (variance-ratio analysis has practical benefit).
- **Hypothesis:** Using the optimal $\sigma_P^2$ (Eq. 70) improves likelihood over fixed $\sigma_P = \sigma_Q$ in finite-depth settings.
- **Minimal Design:** MNIST, T=100 steps. Compare (a) $\sigma_P = \sigma_Q$, (b) $\sigma_P^2 = \sigma_Q^2 + \frac{1}{d}E[||\mu_P - \mu_Q||^2]$ (estimated via running average), (c) $\sigma_P = 2\sigma_Q$.
- **Controls/Baselines:** Standard VDM with equal variances.
- **Metrics:** BPD, diffusion loss.
- **Success Criterion:** (b) outperforms (a) and (c) in diffusion loss.
- **Estimated Cost/Time:** Low (existing setup, 1-2 GPU-days).
- **Expected Paper-Quality Gain:** Medium — validates the theoretical contribution empirically.

**Experiment P1-B: Larger model on ImageNet32**
- **Target Claim:** The encoder benefit scales with model capacity.
- **Hypothesis:** A larger diffusion model (e.g., VDMv-64) would show improvement on ImageNet32 with DiffEnc.
- **Minimal Design:** Train DiffEnc with a VDMv-64 backbone and correspondingly larger encoder on ImageNet32 for 2M steps.
- **Controls/Baselines:** VDMv-64 with v-parameterization.
- **Metrics:** BPD, diffusion loss improvement.
- **Success Criterion:** DiffEnc outperforms VDMv-64 in total BPD.
- **Estimated Cost/Time:** High (8-10 GPU-days). Fallback: train for fewer steps and check if loss trajectories diverge.
- **Expected Paper-Quality Gain:** High if positive — establishes generalization; clarifies scope if null.

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0, immediate, Low cost):
    [Gradient approx. validation (Exp P0-A)]
    [Bounded claim wording in text]

Stage 2 (P0-P1, concurrent, Medium cost):
    [Statistical robustness: more seeds + bootstrap (Exp P0-B)]
    [Variance-ratio empirical demo: MNIST (Exp P1-A)]

Stage 3 (P1, conditional, High cost):
    [ImageNet32 larger model (Exp P1-B)]
        -> If positive: strengthens generalization claim
        -> If null: confirms scope limitation; revise claims accordingly
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Reasoning:** The score prioritizes research value and novelty as primary dimensions. The core idea (learned encoder, discarded at sampling) is clean and novel. The theoretical analysis of variance ratios is rigorous. However, the empirical evidence is limited to a 0.02 BPD improvement on a single dataset (CIFAR-10) with fragile statistical significance (p=0.03, 3 seeds). The null result on ImageNet32 and the lack of validation for the gradient approximation are significant weaknesses that prevent a higher score. The paper is accepted at ICLR 2024, which is consistent with a solid but not outstanding contribution.

**Score breakdown:**
- Research value / contribution: 6/10 (modest empirical gains, novel but bounded idea)
- Novelty: 7/10 (clean concept, related concurrent work exists)
- Validity / soundness: 6/10 (unvalidated approximation, fragile significance)
- Reproducibility: 7/10 (code provided, but loss implementation details need clarity)
- Presentation / clarity: 6/10 (well-structured but intro narrative can be improved, Related Work is list-like)

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors address the P0 issues (validating the gradient approximation, bounding claims to match evidence, improving statistical reporting), the score could reach 7.0-7.5. Further empirical validation on ImageNet32 with larger models (Exp P1-B) could push toward 7.5. The upper bound is limited by the modest effect size and the dataset-specific nature of the improvement.