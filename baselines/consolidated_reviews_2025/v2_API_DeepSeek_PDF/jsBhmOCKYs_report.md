## Summary
# Final Review Report

## Summary

This paper presents "Denoising as Adaptation" (Noise-Space Domain Adaptation for Image Restoration), accepted at ICLR 2025. The core idea is to use a diffusion model's noise prediction loss as a training signal for domain adaptation in image restoration. The restoration network is jointly trained with a conditional diffusion model: the diffusion loss penalizes poor restoration by measuring how well the diffusion model can denoise a noisy version of the synthetic ground truth when conditioned on restored outputs. After training, the diffusion model is discarded, leaving only the restoration network for inference. Two anti-shortcut strategies—channel shuffling and residual-swapping contrastive learning—prevent the diffusion model from ignoring real-world data. Results on denoising, deblurring, and deraining show substantial improvements over feature-space and pixel-space domain adaptation baselines.

**Strengths:** (1) The noise-space adaptation concept is novel and well-motivated by an empirical observation about diffusion model behavior. (2) The shortcut-learning analysis (three-stage training dynamics) is insightful and leads to well-designed mitigation strategies. (3) The framework is architecture-agnostic and demonstrates consistent improvements across different network backbones. (4) The training-time-only diffusion model incurs no extra inference cost.

**Critical weaknesses:** (1) The conclusion contains a factual contradiction—claiming to surpass self-supervised methods while Table 5 shows C2N (35.35 PSNR) outperforms the base Ours (34.71 PSNR). (2) Several key hyperparameters (margin δ in Eq. 3, residual map definitions) are underspecified, harming reproducibility. (3) Comparison fairness with domain adaptation baselines is questionable due to untuned GAN losses and absent statistical significance reporting. (4) Novelty claims ("first attempt," "cannot be achieved using existing losses") are overstated without external verification.

All novelty/comparison conclusions in this review are marked as deferred manual verification due to Retrieval-Disabled Mode.

## Strengths
1. **Conceptually Novel Noise-Space Domain Adaptation:** The paper introduces a genuinely new perspective for domain adaptation in image restoration—operating in the noise space via a diffusion loss. This differs fundamentally from existing feature-space (DANN, DSN) and pixel-space (PixelDA, CyCADA) approaches. The core insight that diffusion prediction error correlates with condition quality is empirically demonstrated and well-utilized as a training signal.

2. **Insightful Shortcut Learning Analysis and Mitigation:** The identification of three training stages (I: both degraded, II: synthetic restored, III: diffusion ignores real data) is a valuable diagnostic contribution. The channel shuffling layer and residual-swapping contrastive learning strategy are clever, lightweight solutions that directly address the asymmetry problem in Eq. (1). The ablation results (Table 4) clearly show their individual contributions (+0.84 dB from CS, +1.80 dB from RS).

3. **Architecture-Agnostic and General Framework:** The method works across multiple backbone architectures (U-Net variants, Uformer variants) and three distinct restoration tasks (denoising, deblurring, deraining). The scalability analysis (Fig. 7) convincingly shows that the proposed method prevents the overfitting that plagues large vanilla models on synthetic data. The training-only diffusion model imposes no inference overhead.

4. **Strong Empirical Results on Denoising:** On the SIDD dataset, the method achieves 34.71 dB PSNR (base) and 35.52 dB PSNR (Ours*), substantially outperforming feature-space (best: CyCADA at 30.81 dB) and pixel-space (best: PixelDA at 29.24 dB) domain adaptation methods by a large margin. These gains are consistent across qualitative comparisons (Fig. 4).

5. **Honest Limitation Disclosure:** The paper explicitly acknowledges that the method works best for high-frequency degradations (noise, rain) and less effectively for low-frequency distortions (blur). This transparency helps readers calibrate expectations and suggests a clear direction for future improvement.

## Weaknesses
1. **Factual Contradiction in Conclusion (SEVERITY: MAJOR):** The conclusion claims "scalability surpassing that of self-supervised methods across a range of image restoration tasks." However, Table 5 (Page 10) shows C2N (self-supervised) achieves 35.35 PSNR on SIDD, while the base Ours achieves 34.71 PSNR. Only Ours* (with deeper layers) marginally exceeds C2N at 35.52 PSNR. On deblurring and deraining, no self-supervised comparison is made. This is an empirically unsupported claim that must be corrected. Location: Page 10 — Conclusion.

2. **Unverifiable Novelty/Capability Claims:** The abstract and contribution list contain absolute negative claims ("cannot be achieved using existing losses") and a "first attempt" claim. These are not directly testable from the presented experiments and invite reviewer skepticism. With Retrieval-Disabled Mode active, these claims cannot be externally verified. Location: Page 1 — Abstract; Page 2 — Contribution list.

3. **Missing Hyperparameters and Underspecified Components (SEVERITY: MAJOR):** (a) The margin δ in Eq. (3) is never reported or ablated. (b) The residual maps Rs, Rr in Eq. (2) are not defined (image-space vs. feature-level). (c) The expectation in Eq. (1) lacks subscripts specifying which random variables are marginalized. These omissions directly harm reproducibility. Location: Pages 4-6 — Methodology, Eqs. (1)-(3).

4. **Baseline Comparison Fairness (SEVERITY: MAJOR):** The domain adaptation baselines (DANN, DSN, PixelDA, CyCADA) all use adversarial loss (LRes+LGan) which is known to be unstable and requires careful tuning for low-level vision. The paper states baselines were "retrained with the same standard settings and datasets" but does not verify whether the GAN training was stable or whether the adversarial weight was optimized. No variance or significance testing (multi-seed, confidence intervals) is reported for any comparison. Location: Page 7 — Experiments Section 4.1.

5. **Asymmetric Diffusion Loss Design:** Eq. (1) defines a diffusion loss where the noisy input ˜ys is derived from synthetic ground truth ys, not from real-world data. This means the diffusion loss directly supervises only the synthetic output ˆys through backpropagation to the condition. The real-world output ˆyr is only indirectly supervised through channel shuffling and residual swapping. This asymmetry is acknowledged but its implications for training dynamics are not fully discussed. Location: Page 4 — Eq. (1).

6. **Limited Advantage on Non-Denoising Tasks:** On deraining (+0.22 PSNR over Restormer) and deblurring (+0.10 PSNR over CyCADA), the improvements are marginal or the comparisons are with a single baseline. Without statistical testing, the practical significance of these gains is unclear. Location: Pages 7-8 — Tables 2-3.

7. **Self-Supervised Methods Are Strong Competitors:** The paper acknowledges that C2N (35.35 PSNR) and AP-BSN (34.90 PSNR) are competitive or better than Ours (34.71 PSNR). The discussion in Section 4.3 frames this as a scalability advantage, but it also implies the proposed method does not achieve SOTA on denoising compared to task-specific self-supervised methods, which limits the practical impact. Location: Page 9 — Table 5, Section 4.3 Discussion.

## Key Issues
### Ranked Defect Board (by Severity | Research-Value Impact | Validity Risk | Fixability)

| Rank | Issue | Severity | Impact | Root Cause | Fixability | Required Action |
|------|-------|----------|--------|------------|------------|-----------------|
| 1 | Conclusion contradicts Table 5: "surpassing self-supervised methods" unsupported | Major | Research validity, overclaim | Factual error in writing | Easy (text fix) | Rewrite final sentence of Conclusion |
| 2 | Margin δ and residual map definition missing | Major | Reproducibility | Omission in method description | Easy (report values) | Add δ value and Rs/Rr definition |
| 3 | Baseline comparison fairness (untuned GAN, no variance) | Major | Validity of empirical claims | Incomplete evaluation protocol | Moderate (add experiments) | Multi-seed reporting + statistical tests |
| 4 | Unverifiable "first attempt" / "cannot be achieved" claims | Major | Novelty perception | Overclaiming without literature verification | Easy (rewording) | Replace with scoped wording |
| 5 | Asymmetric diffusion loss (Eq. 1) biases toward synthetic domain | Medium | Method transparency | Design choice not fully discussed | Easy (add discussion) | Explicit paragraph explaining trade-off |
| 6 | Marginal gains on deraining/deblurring without significance tests | Medium | Practical impact | Small effect size | Moderate (add stats) | Report confidence intervals |
| 7 | Related Work reads as list, not comparison | Minor | Readability | Structural weakness | Moderate (restructure) | Reorganize by comparison axes |

## Actionable Suggestions
### S1 (Must) — Fix Conclusion Claim Contradiction
**Location:** Page 10 — Conclusion, final sentence.
**Problem:** The conclusion claims "scalability surpassing that of self-supervised methods," contradicting Table 5 where C2N (35.35) > Ours (34.71).
**Fix:** Replace with bounded wording:
> "Experimental results demonstrate the effectiveness of our approach over feature-space and pixel-space domain adaptation methods, and show that it offers a general and scalable framework that is competitive with task-specific self-supervised methods across multiple image restoration tasks."
**Effort:** 5 minutes. **Impact:** High (removes factual error).

### S2 (Must) — Report Missing Hyperparameters
**Location:** Page 5-6 — Eqs. (2)-(3).
**Problem:** Margin δ in Eq. (3) and residual map definitions (Rs, Rr) in Eq. (2) are not specified, breaking reproducibility.
**Fix:** (a) Add the margin value used (e.g., δ = 0.2), (b) Clarify: "Rs = G(xs) − xs and Rr = G(xr) − xr are pixel-wise residual images in the spatial domain." (c) Add expectation subscript in Eq. (1): $\mathbb{E}_{t\sim U(1,T), \epsilon\sim N(0,I)}$.
**Effort:** 15 minutes. **Impact:** High (reproducibility).

### S3 (Must) — Add Statistical Significance Reporting
**Location:** Page 7-8 — Tables 1-3, Section 4.1.
**Problem:** No variance or significance testing across any method.
**Fix:** Run all methods with ≥3 random seeds and report mean±std for PSNR/SSIM/LPIPS. For the top-2 comparisons, add a paired Welch's t-test or Mann-Whitney U test p-value.
**Effort:** 2-3 GPU-days. **Impact:** High (validity of empirical claims).

### S4 (Must) — Replace Overclaimed Novelty Wording
**Location:** Page 1-2 — Abstract and Contribution 1.
**Problem:** "First attempt" and "cannot be achieved using existing losses" are unverifiable.
**Fix:** Replace with: "We introduce a noise-space domain adaptation approach for image restoration, which to our knowledge has not been explored in prior work. We show that diffusion loss provides an effective training signal for domain adaptation, offering benefits complementary to existing loss functions."
**Effort:** 10 minutes. **Impact:** High (defensibility).

### S5 (Nice-to-Have) — Strengthen Baseline Fairness
**Location:** Page 7 — Section 4.1.
**Problem:** GAN-based baselines may be undertuned.
**Fix:** Add a control experiment where the strongest baseline (CyCADA) is re-implemented with task-specific tuning (e.g., gradient penalty, adjusted adversarial weight search). Report the tuned results alongside original.
**Effort:** 1-2 GPU-days. **Impact:** Medium (fairness assurance).

### S6 (Nice-to-Have) — Add Asymmetric Loss Discussion
**Location:** Page 4 — After Eq. (1).
**Problem:** Diffusion loss only uses synthetic GT as denoising target.
**Fix:** Add one paragraph: "Note that the diffusion loss uses synthetic ground truth ys as the denoising target, creating an asymmetric training signal where ˆyr is only indirectly supervised through the condition. This design is intentional: the clean distribution knowledge 'leaked' from ys to the diffusion model guides ˆyr through the multi-step denoising process. The channel shuffling and contrastive learning strategies are specifically designed to prevent the model from exploiting this asymmetry as a shortcut."
**Effort:** 30 minutes. **Impact:** Medium (method transparency).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

The current abstract is functional but can be tightened. Recommended structure (4 sentences):

- **S1 (Problem + Significance):** "Learning-based image restoration methods suffer from limited real-world generalization due to the domain gap between synthetic training data and real-world degradations."
- **S2 (Prior Gap):** "Existing domain adaptation methods in feature or pixel space often overlook low-level details or suffer from training instability."
- **S3 (Proposed Method):** "We introduce noise-space domain adaptation, which leverages a conditional diffusion model's noise prediction loss to guide a restoration network to align both synthetic and real-world outputs with a clean target distribution. Two anti-shortcut strategies—channel shuffling and residual-swapping contrastive learning—prevent the diffusion model from ignoring real-world data."
- **S4 (Key Result + Bounded Implication, optional):** "On three tasks (denoising, deblurring, deraining), our method substantially improves over feature/pixel-space adaptation baselines while being architecture-agnostic and imposing no inference overhead."

### Introduction Outline (Complete — Five Paragraphs)

**P1 — Problem Statement** (Role: Establish stakes and specific challenge)
- Open with: "Image restoration models trained on synthetic paired data consistently underperform on real-world images due to the domain gap—synthetic degradation assumptions cannot capture the diversity of real-world distortions."
- Close with: "This paper investigates domain adaptation for image restoration using both synthetic paired data and unlabeled real-world degraded images."

**P2 — Prior Work and Its Limitations** (Role: Categorize and critique existing solutions)
- Organize by approach: (a) improved data synthesis, (b) blind degradation estimation, (c) self-supervised learning, (d) domain adaptation (feature-space, pixel-space).
- Key critique: "Feature-space methods align high-level representations but miss low-level details. Pixel-space methods are computationally expensive and training unstable. No existing method operates in the noise space, which is naturally aligned with image restoration's pixel-level objective."

**P3 — Core Idea and Intuition** (Role: Present the key insight)
- Start with the observation from Fig. 1(a): diffusion model prediction error correlates with condition quality.
- Then: "We leverage this property by conditioning a diffusion model on the outputs of the restoration network. The diffusion loss serves as a training signal that incentivizes the restoration network to produce outputs that are easier for the diffusion model to denoise—i.e., closer to the clean target distribution."
- End with: "Both networks are trained jointly; the diffusion model is discarded at inference."

**P4 — The Shortcut Problem and Solutions** (Role: Identify the challenge and design response)
- "A key challenge emerges during joint training: the diffusion model can exploit the pixel similarity between the synthetic condition and the noisy input as a shortcut, ignoring real-world data."
- "We propose two solutions: (i) a channel-shuffling layer that randomizes condition order, and (ii) a residual-swapping contrastive learning strategy that forces the diffusion model to process both conditions equally."

**P5 — Contributions and Roadmap** (Role: Summary of claims and paper structure)
- Three crisp, defensible contribution claims (avoiding "first" and "cannot be achieved" language).
- Brief note on tasks and metrics.
- Roadmap sentence: "We present the method in Section 3, experimental validation in Section 4, and limitations in Section 4.4."

### Alternative Storyline Comparison

| Storyline Version | Big Picture → Gap → Solution → Evidence | Problem Alignment | Variable Alignment | Contribution-Evidence Alignment |
|---|---|---|---|---|
| **Current** | Introduces problem → catalogs prior work → presents idea → contributions | Good | Good (diffusion loss ↔ conditions) | Conclusion overclaims vs Table 5 |
| **Candidate A (above)** | Stakes → gap critique → key insight → challenge → solutions | Better (tighter problem framing) | Same | Fixed (bounded claims) |
| **Candidate B** | Start with empirical observation (Fig 1a) → derive method → explain shortcut → experiments | Good (motivation-driven) | Same | Requires bounded conclusion |

**Recommended: Candidate A** — It provides the clearest narrative arc and directly addresses the biggest weaknesses (overclaiming, missing gap analysis). The key change from the current version is: (1) replace the literature-survey style P1 with a sharper problem framing, (2) merge the two idea paragraphs into one crisp intuition paragraph, (3) use bounded contribution language.

## Priority Revision Plan
### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: Conclusion contradicts Table 5]
    -> [Fix S1: Reword final sentence of Conclusion]
    -> [Expected gain: Remove factual error, improve credibility]
    
[Problem: Missing hyperparameters (δ, Rs/Rr)]
    -> [Fix S2: Report δ value, define residuals, add expectation subscript]
    -> [Expected gain: Full reproducibility]
    
[Problem: No statistical testing]
    -> [Fix S3: Add multi-seed std + significance tests]
    -> [Expected gain: Valid empirical claims]
    
[Problem: Overclaimed novelty wording]
    -> [Fix S4: Replace "first/cannot" with scoped wording]
    -> [Expected gain: Defensible claims, reduced reviewer skepticism]
    
[Problem: Baseline fairness concern]
    -> [Fix S5: Tuned CyCADA control experiment]
    -> [Expected gain: Fairer comparison, strengthened positioning]
    
[Problem: Asymmetric diffusion loss not discussed]
    -> [Fix S6: Add design rationale paragraph]
    -> [Expected gain: Method transparency]
```

### Priority Order (P0 → P1 → P2)

| Priority | Action | Effort | Impact | Type |
|----------|--------|--------|--------|------|
| **P0** | S1: Fix conclusion contradiction | 5 min | High | Must |
| **P0** | S2: Report δ, define residuals | 15 min | High | Must |
| **P0** | S4: Replace overclaimed novelty wording | 10 min | High | Must |
| **P1** | S3: Add multi-seed std + significance tests | 2-3 GPU-days | High | Must |
| **P1** | S5: Tuned CyCADA control | 1-2 GPU-days | Medium | Nice-to-have |
| **P2** | S6: Add asymmetric loss discussion | 30 min | Medium | Nice-to-have |

### Expected Impact After All Fixes
- **Validity**: High (statistical testing + fairer baselines)
- **Reproducibility**: High (reported hyperparameters, definitions)
- **Novelty Perception**: Medium (scoped claims, no overreach)
- **Readability**: Medium (restructured Related Work, tighter introduction)

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Tab 1) | Denoising on SIDD (real-world) | U-Net baseline vs DA methods; AWGN σ∈[0,75]; train on synthetic+SIDD | PSNR/SSIM/LPIPS | Ours 34.71 dB vs CyCADA 30.81 dB | C1 (noise-space DA works) | No multi-seed variance; GAN baselines potentially undertuned |
| E2 (Tab 2) | Deraining on SPA | Same U-Net; Rain13K+SPA | PSNR/SSIM/LPIPS (Y channel) | Ours 34.39 vs Restormer 34.17 (+0.22) | C1 (generalizable) | Marginal gain; single baseline comparison |
| E3 (Tab 3) | Deblurring on RealBlur-J | Same U-Net; GoPro+RealBlur-J | PSNR/SSIM/LPIPS | Ours 26.46 vs CyCADA 26.36 (+0.10) | C1 (generalizable) | Very marginal gain; no significance test |
| E4 (Tab 4) | Ablation: noise range, CS, RS | Variants on SIDD denoising | PSNR/SSIM | Full: 34.71; w/o CS: 32.91; w/o RS: 32.07 | C2 (shortcut mitigation works) | Only denoising task ablated |
| E5 (Tab 4 bottom) | Data necessity: Only syn/Only real | SIDD denoising | PSNR/SSIM | Only syn: 26.83; Only real: 32.60 | Both data types needed | Components held constant not specified |
| E6 (Fig 7, Tab 5) | Scalability: different architectures | 6 variants (Unet-T/S/B, Uformer-T/S/B) on SIDD | PSNR vs GMACs | Ours improves over Vanilla for all architectures | C3 (architecture-agnostic) | Non-monotonic: Uformer-B < Unet-B unexplained |
| E7 (Tab A1) | Extension: unpaired condition | Ours-Ex vs Ours on all 3 tasks | PSNR/SSIM/LPIPS | Ours-Ex competitive on deraining/deblurring | Extension viable | Slightly lower than paired on denoising |

### Research-Theme Gap Diagnosis

- **New Knowledge**: The noise-space DA concept is genuinely new and well-executed. However, the theoretical understanding of *why* diffusion loss works better than GAN-based losses for restoration is not deeply analyzed.
- **Reproducibility**: Weakened by missing hyperparameters (δ, residual definitions). Partially addressed by released code on the project website.
- **Impact on Practice**: Limited because task-specific self-supervised methods (C2N, AP-BSN) achieve comparable or better performance on denoising without requiring a diffusion model for training.

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment — Statistical Robustness Package**
- **Target Claim:** All empirical comparisons (Tab 1-3)
- **Hypothesis:** Reported gains are statistically significant
- **Design:** Run all methods with 5 random seeds. Compute mean±std for PSNR/SSIM/LPIPS.
- **Controls:** Same seed set across all methods, same data splits.
- **Metrics:** PSNR mean±std, Cohen's d effect size, paired t-test p-value (Ours vs best baseline).
- **Success Criterion:** p<0.05 for denoising; p<0.10 for deraining/deblurring.
- **Cost:** ~3 GPU-days. **Gain:** High (validates all empirical claims).

**P1 Experiment — Fair Baseline Control**
- **Target Claim:** Ours outperforms feature/pixel-space DA methods
- **Hypothesis:** With proper tuning, CyCADA can approach Ours's denoising performance
- **Design:** Re-implement CyCADA with (a) gradient penalty for GAN stability, (b) grid search over adversarial weight λ∈{0.01, 0.1, 1.0}, (c) same U-Net backbone.
- **Controls:** Same optimizer, batch size, learning rate.
- **Metric:** PSNR on SIDD test.
- **Success Criterion:** Report both original and tuned CyCADA results.
- **Cost:** ~1 GPU-day. **Gain:** Medium (fairness assurance, stronger positioning).

**P2 Experiment — Cross-Task Noise Range Ablation**
- **Target Claim:** Full noise range [1,1000] is optimal across tasks
- **Hypothesis:** Different tasks have different optimal noise ranges
- **Design:** Repeat the noise range ablation (Table 4 rows b-d) on SPA deraining and RealBlur-J deblurring.
- **Controls:** Same U-Net, optimizer, hyperparameters.
- **Metric:** PSNR/SSIM.
- **Success Criterion:** Identify whether the optimal noise range is task-dependent.
- **Cost:** ~0.5 GPU-days per task. **Gain:** Medium (generalizability evidence).

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0, before resubmission):
    ┌─────────────────────────────┐
    │ Multi-seed std + t-tests    │  ← 3 GPU-days
    │ for Tables 1-3             │
    └──────────┬──────────────────┘
               ↓
Stage 2 (P1, before resubmission):
    ┌─────────────────────────────┐
    │ Tuned CyCADA baseline       │  ← 1 GPU-day
    │ with gradient penalty       │
    └──────────┬──────────────────┘
               ↓
Stage 3 (P2, follow-up):
    ┌─────────────────────────────┐
    │ Cross-task noise ablation   │  ← 1 GPU-day
    │ on deraining + deblurring   │
    └─────────────────────────────┘
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: **6.5 / 10**

**Primary scoring dimensions (research value + novelty weighted most):**

- **Novelty (7/10):** The noise-space domain adaptation concept is genuinely new and well-motivated. The shortcut-learning analysis and mitigation strategies are insightful contributions. However, two of the three claimed contributions overlap in scope, and the "first attempt" framing is unnecessarily aggressive. Novelty verification against external literature is deferred. A well-executed conceptual contribution with minor framing issues.
- **Research Value (6.5/10):** The method shows strong improvements on denoising but more marginal gains on deraining and deblurring. The architecture-agnostic nature is valuable for practitioners. The main limitation is that task-specific self-supervised methods (C2N, AP-BSN) achieve comparable or better absolute performance, reducing the practical advantage. The framework is elegant and principled, which raises its scientific value.
- **Validity/Soundness (6/10):** The core method is sound and the ablation studies are well-designed. However, comparison fairness concerns (untuned GAN baselines, no statistical significance testing) and a factual contradiction in the conclusion reduce confidence. Several missing hyperparameters harm reproducibility.
- **Reproducibility (5/10):** The paper provides training details (batch size, learning rate, noise schedule, EMA decay) and releases code on a project page. However, the margin δ in Eq. (3), residual map definitions, and expectation subscripts are missing, which makes the method description incomplete for independent reimplementation.
- **Presentation & Clarity (6.5/10):** The paper is generally well-written with clear figures. The introduction could be tightened (avoids current literature-survey style). The Related Work section reads as a list rather than a comparison. The limitation section is honest and helpful.

### Post-Revision Target: **[7.5, 8.0] / 10**

This target assumes the following are fully addressed:
- P0 fixes: conclusion contradiction corrected, missing hyperparameters reported, overclaimed novelty wording replaced (validity/reproducibility → 7-8)
- P1 fixes: multi-seed statistical testing added + tuned baseline control (empirical validity → 7.5-8)
- P2 fix: cross-task noise ablation strengthens generalizability evidence

The upper bound (8.0) requires that the revised conclusion and claims are fully defensible, all hyperparameters are reported, and statistical testing confirms the main results are significant. The lower bound (7.5) assumes statistical tests reveal marginal significance on deraining/deblurring.

**Current strengths outweigh weaknesses:** The core idea is solid and well-executed. The identified weaknesses are fixable (text revisions, hyperparameter reporting, additional experiments). No fatal flaws were detected. With moderate revision effort, the paper can be a solid contribution to the image restoration and domain adaptation communities.