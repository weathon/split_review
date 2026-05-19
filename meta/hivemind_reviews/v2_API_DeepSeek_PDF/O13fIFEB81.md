## Summary
# Final Review Report

## Summary

This paper proposes a unified framework for watermarking diffusion models, organized along three design dimensions: (1) distribution of individual watermark elements, (2) specification of watermark regions within each channel, and (3) choice of channels for watermark embedding. Under this framework, the authors instantiate a training-free hybrid watermarking method that combines "Random Gaussian" and "Gaussian Ring" patterns, adapting the green/red list concept from LLM watermarking to the latent space of diffusion models. The method embeds watermarks directly into the initial latent noise tensor z_T by partitioning the standard Gaussian distribution at the median and assigning each element to the positive or negative domain based on the watermark bit. Two region specification strategies are proposed: randomized patch-based watermarking (for noise robustness) and ring-based watermarking (for geometric robustness), with a gradient-based channel selection mechanism to dynamically assign each channel to one of the two strategies. Experiments on Stable Diffusion (text-to-image) and instruct-pix2pix (image-to-image) show competitive robustness against standard augmentation-based attacks while maintaining visual quality.

**Strengths:**
- The three-dimension taxonomy provides a useful conceptual organization of the latent-representation watermarking design space.
- The hybridization of Random Gaussian and Gaussian Ring patterns is technically sound and ablation studies support their complementary roles.
- The extension to image-to-image models (instruct-pix2pix) is a practical contribution beyond the standard text-to-image focus.
- The theoretical analysis (distribution preservation in Lemma 4.1) is correctly motivated.

**Weaknesses at a glance:**
- The framework is presented as a descriptive catalog rather than a formal, testable taxonomy; formal definitions are missing.
- The DDIM inversion formula is ambiguous (forward step described as inversion).
- Proposition 4.2's correlation derivation appears to conflate "same patch" and "same position across different patches."
- The detection aggregation uses max over channels, which discards multi-channel redundancy and may inflate false positive rates.
- Several key claims ("outperforms existing methods," "first systematic approach," "significant advancement") are overscoped relative to the evidence.
- The conclusion lacks a limitations paragraph.
- Variance/uncertainty reporting is absent from experimental tables.
- External literature verification was unavailable in this run; novelty comparisons are deferred.

## Strengths
**S1 — Conceptual taxonomy of the watermarking design space.** The three-dimension framework (element distribution, region specification, channel selection) provides a clear, organized way to categorize existing latent-representation watermarking methods. This is a genuinely useful conceptual contribution that can help researchers understand design trade-offs and identify unexplored combinations.

**S2 — Training-free, distribution-preserving watermarking.** The adaptation of the green/red list method from LLM watermarking is well-motivated. Lemma 4.1 correctly shows that the marginal distribution of each element remains N(0,1) after watermarking. This is a rigorous theoretical property that distinguishes the method from constant-value approaches (Tree-Ring, DwtDctSVD) that introduce detectable distribution shifts.

**S3 — Complementary hybrid design with empirical support.** The combination of Random Gaussian (patch-based) and Gaussian Ring strategies is technically interesting and the ablation study (Table 8) provides clear evidence that these two components address different threat types: rings for geometric robustness and random patches for noise robustness. The gradient-based channel assignment is a principled way to allocate each method where it is most effective.

**S4 — First systematic evaluation on image-to-image models.** While the single-model scope (instruct-pix2pix) limits generalization, the extension beyond text-to-image is practically relevant and the results (Table 6, average AUC 0.927) demonstrate that the method works in this more challenging setting where inversion is less reliable.

**S5 — Comprehensive robustness evaluation.** The evaluation covers 10 different attack types (rotation, JPEG compression, cropping+resizing, blurring, Gaussian noise, color jitter, salt-and-pepper noise, denoising, flipping). This is broader than many prior watermarking papers and enables meaningful per-attack comparison (Table 2).

## Weaknesses
**W1 — Framework is descriptive rather than formal.** The three-dimension taxonomy (distribution, region, channels) is presented as a conceptual framework but lacks formal definitions. It is not specified what constitutes a dimension, whether dimensions are independent, or how to represent a method as a point in the product space. For an ICLR-level paper, the framework should be more rigorous: at minimum, define a tuple (D, R, C) with formal domains for each component.

**W2 — DDIM inversion formula is ambiguous (Page 3).** The equation presented as the DDIM inversion formula actually matches the forward DDIM sampling step, but the text describes it as the inverse process. The direction of the equation (from t to t+1) suggests forward sampling, not inversion which should go from 0 to T (or t-1). This ambiguity could lead readers to misunderstand the watermark detection process.

**W3 — Proposition 4.2 correlation derivation appears flawed.** The proof in Appendix B.2 assumes that elements in the "same position across different patches" share the same watermark bit. However, the problem setup states that different patches have independent watermark bits. The quantity P_s and the resulting correlation formula need to be rederived or clarified. This issue affects the claimed theoretical justification for the random patch advantage.

**W4 — Max-based detection aggregation discards multi-channel redundancy.** The detection formula Acc(m_hat) = max_c Acc(z^(c)_T, m_c) selects the single best channel, ignoring information from all other channels. This contradicts the paper's claim that embedding across all channels "enhances overall robustness." Furthermore, max-based aggregation inflates false positive rates because only one channel needs to match by chance. A statistically better approach would be average aggregation with a calibrated threshold as described in Appendix B.3.

**W5 — Overscoped contribution claims.** Multiple claims exceed what the evidence supports:
- "First systematic approach to watermarking image-to-image diffusion models" — only tested on one model (instruct-pix2pix).
- "Outperforms existing methods" — no statistical significance tests, comparable FID/CLIP scores suggest equivalent quality not superiority.
- "Significant advancement in digital watermarking" — not supported by the scope of experiments.

**W6 — Guidance scale mismatch between generation and inversion.** Generation uses classifier-free guidance scale 7.5, while inversion uses scale 1 (empty prompt). This CFG mismatch can significantly degrade inversion accuracy, yet the paper does not discuss or validate inversion reliability under these conditions.

**W7 — Missing variance and statistical significance.** All tables report point estimates without standard deviations or confidence intervals. The 3-seed averaging is mentioned but not shown in the tables. Given the known variance in diffusion model sampling, this omission makes it impossible to assess whether the reported differences are statistically reliable.

**W8 — Conclusion lacks limitations.** The concluding section does not discuss any limitations of the study, which is a significant omission for scientific transparency. Key limitations include the single image-to-image model, the CFG mismatch issue, the max-based detection aggregation concern, and the bounded attack set.

## Key Issues
**Issue 1 (Critical): Proposition 4.2 correlation formula needs correction or clarification.**
- **Location:** Page 6 - Region Specification: Proposition 4.2 paragraph
- **Problem:** The derivation in Appendix B.2 uses "same position across different patches" to compute correlation, but the problem setup states that different patches have independent watermark bits. The proof's event definition appears to conflate "same patch" with "same position across different patches."
- **Impact:** The claimed theoretical justification that randomized patches reduce element correlation may still be valid, but the specific formula and its derivation are unreliable as written.
- **Required action:** Re-derive the correlation under the correct event space (elements within the same patch share a bit; elements in different patches have independent bits). If the formula changes, update Proposition 4.2 and all downstream claims.

**Issue 2 (Major): DDIM inversion formula direction is unclear.**
- **Location:** Page 3 - Preliminaries: DDIM inversion equation
- **Problem:** The equation z_hat_{t+1} = ... shows a forward-time step (t to t+1) but is described as the inversion process. Standard DDIM inversion runs in the reverse direction.
- **Impact:** Readers cannot reliably reproduce the watermark detection process from the description.
- **Required action:** Clarify whether the shown equation is forward DDIM sampling (used to reconstruct z_T by running forward from z_0) or the actual inverse step. Add a note about the direction convention and cite the exact inversion formula from Dhariwal & Nichol.

**Issue 3 (Major): Max-based detection aggregation is suboptimal.**
- **Location:** Page 8 - Detection aggregation along channels: Acc(m_hat) = max_c Acc(...)
- **Problem:** Selecting the single best channel discards multi-channel redundancy and inflates FPR. The max-based approach contradicts the paper's stated goal of "embedding across all channels to enhance overall robustness."
- **Impact:** The claimed robustness advantage may be partially an artifact of the detection rule rather than a true signal. FPR calibration becomes unreliable.
- **Required action:** Replace max with average aggregation across channels and calibrate the detection threshold using the binomial statistical test described in Appendix B.3.

**Issue 4 (Major): Overscoped contribution claims in abstract and conclusion.**
- **Location:** Page 1 (Abstract), Page 2 (Contributions), Page 10 (Conclusion)
- **Problem:** The paper uses absolute superiority language ("outperforms existing methods," "significant advancement") and strong scope claims ("first systematic approach") without sufficient evidence. The image-to-image evaluation covers only one model (instruct-pix2pix).
- **Impact:** If a reviewer is familiar with a broader range of image-to-image watermarking literature, these claims could trigger rejection for overclaiming.
- **Required action:** Replace superiority claims with bounded comparative statements. Scope the image-to-image claim to the specific model tested.

**Issue 5 (Major): Guidance scale mismatch between generation and inversion is unaddressed.**
- **Location:** Page 8 - Experimental Setting
- **Problem:** Generation uses CFG scale 7.5 but inversion uses scale 1 (empty prompt). This mismatch can cause significant ODE trajectory divergence.
- **Impact:** Inversion accuracy may be poor under these conditions, but no inversion quality metrics (e.g., reconstruction PSNR) are reported.
- **Required action:** Report inversion reconstruction error (PSNR or MSE) on a sample of 100+ images. Discuss how the mismatch affects detection performance.

## Actionable Suggestions
### Suggestion 1: Formalize the three-dimension framework (Must)

**Problem:** The framework is currently a descriptive catalog. For ICLR-level rigor, provide formal definitions.

**Action:** Define a watermarking method as a tuple W = (D, R, C) where:
- D: distribution family for element values (e.g., constant, truncated Gaussian, learned weights)
- R: region function R: {1,...,c} → P({1,...,h}×{1,...,w}) mapping each channel to a spatial subset
- C ⊆ {1,...,c}: set of watermarked channels

Add a mapping table that locates each existing method (Tree-Ring, Gaussian Shading, Stable Signature, etc.) in this formal space. This directly strengthens the claimed "framework" contribution.

### Suggestion 2: Clarify DDIM inversion direction (Must)

**Problem:** The inversion equation direction is ambiguous.

**Action:** Replace or annotate the current equation with a clear statement. If it is the forward DDIM step used for reconstruction, rename it "forward reconstruction step." If it is the actual inversion, change the subscript direction from t→t+1 to t→t-1. Add: "We use the DDIM forward ODE solver from z_0 to z_T, relying on the approximation that the ODE trajectory is reversible when step sizes are sufficiently small [Dhariwal & Nichol 2021]."

### Suggestion 3: Fix Proposition 4.2 derivation (Must)

**Problem:** The correlation derivation conflates patch-bit independence.

**Action:** Re-derive Corr(X,Y) with the correct event space. Elements in the same patch (same bit) vs. elements in different patches (independent bits). If X and Y are from the same patch, Corr = 2/pi (since they share the bit). If from different patches, Corr = 0. The expected correlation for randomly selected element pairs is E[Corr] = (2/pi) * (n choose 2)/(N choose 2) where N = np. Update the proposition accordingly.

### Suggestion 4: Replace max-based detection with average-based aggregation (Must)

**Problem:** Max over channels discards redundancy and inflates FPR.

**Action:** Replace Acc(m_hat) = max_c Acc(...) with:

Acc(m_hat) = (1/|C_m|) * sum_{c in C_m} Acc(z^(c)_T, m_c)

Set the detection threshold tau using the binomial test from Appendix B.3: FPR(tau) = I_{1/2}(tau+1, k-tau) where k is the total number of watermarked bits across all channels. Report TPR@1%FPR using this corrected test.

### Suggestion 5: Add variance and significance to experimental tables (Must)

**Problem:** All metrics are point estimates without uncertainty quantification.

**Action:** Report all metrics as mean ± std over 3+ seeds in Tables 1-2 and the ablation tables. Add a significance test (paired bootstrap or Wilcoxon) comparing the proposed method against Tree-Ring and Gaussian Shading for the average adversarial TPR.

### Suggestion 6: Add inversion reliability validation (Must)

**Problem:** CFG mismatch between generation (7.5) and inversion (1) is unvalidated.

**Action:** Compute and report the average PSNR between original z_T and reconstructed z_hat_T over 100 test images. Report this separately for text-to-image and image-to-image settings. Include a short discussion of whether the mismatch affects detection accuracy.

### Suggestion 7: Add a limitations paragraph to the conclusion (Must)

**Problem:** The conclusion has no limitations discussion.

**Action:** Add the following paragraph before the final sentence:

"Limitations. This study has several limitations. First, the image-to-image evaluation covers only a single model (instruct-pix2pix); generalizing to other image-to-image architectures requires further validation. Second, the detection method relies on DDIM inversion, which may be fragile under classifier-free guidance mismatch or on models without deterministic inversion. Third, the max-based detection aggregation, while effective in our experiments, has not been statistically calibrated against false positive control. Fourth, the evaluated attack set, while diverse, does not include adaptive attacks specifically designed to defeat the proposed watermark. Addressing these limitations is an important direction for future work."

### Suggestion 8: Scope down overclaims (Must)

**Problem:** "Outperforms existing methods," "first systematic approach," "significant advancement" are unsupported.

**Action:** Replace with bounded claims:
- "Our method achieves competitive robustness against the evaluated attack types, outperforming selected baselines on average TPR@1%FPR under the tested conditions."
- "We extend watermarking to the image-to-image setting, demonstrating effectiveness on the instruct-pix2pix model."
- Remove "significant advancement" from the conclusion entirely.

### Suggestion 9: Improve related-work organization (Nice to have)

**Problem:** Related work is organized chronologically rather than by design dimensions.

**Action:** Restructure the related-work section using the three-dimension framework itself. Create a table mapping each existing method to its position on dimensions 1-3. This demonstrates the framework's utility and directly positions the paper's contribution.

### Suggestion 10: Generalize conditional distribution formula (Nice to have)

**Problem:** The conditional distribution formula only handles the k=2 case.

**Action:** Provide the general k-partition form: p(z^e_T | m=i) = phi(z^e_T) / (Phi(Q((i+1)/k)) - Phi(Q(i/k))) * 1{z^e_T ∈ (Q(i/k), Q((i+1)/k)]}, showing that the k=2 case is a special instance.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

The abstract should follow a 5-sentence structure:

**S1 (Problem + Domain):** "Diffusion models generate highly realistic images, but their deployment raises copyright and content-authentication challenges that can be addressed through image watermarking."

**S2 (Gap):** "Existing watermarking methods for diffusion models make diverse design choices — in how watermark elements are valued, which spatial regions carry the watermark, and which latent channels are modified — without a unified framework to understand or compare these choices."

**S3 (Proposed Framework):** "This paper introduces a unified framework that organizes these choices along three dimensions: element distribution, region specification, and channel selection."

**S4 (Method Instantiation):** "Under this framework, we instantiate a training-free hybrid watermarking method that combines distribution-preserving random-patch watermarks (robust to noise) with Gaussian-ring watermarks (robust to geometric transformations), allocated across latent channels via a gradient-based sensitivity criterion."

**S5 (Result + Scope):** "Experiments on Stable Diffusion (text-to-image) and instruct-pix2pix (image-to-image) show that our method preserves visual quality (FID 25.20, CLIP 0.363) while achieving an average TPR@1%FPR of 0.984 across ten attack types, outperforming selected baselines under comparable evaluation conditions."

### Introduction Outline (Complete)

**P1 — Establish stakes and concrete gap (revised):**
Role: Define the societal motivation (copyright, misuse) and immediately pivot to the technical gap — the lack of a systematic framework for understanding watermarking design choices.
Key claim: The design space of latent-representation watermarking has not been systematically decomposed.
Transition: "In this paper, we provide that systematic decomposition."

**P2 — Literature synthesis organized by framework dimensions:**
Role: Replace the current chronological survey with an organized comparison organized by the three dimensions. Show how Tree-Ring (constant, frequency ring, specific channels), Gaussian Shading (sub-distribution, spatial blocks, all channels), and Stable Signature (learned, full spatial, all channels) occupy different positions.
Key claim: Existing methods can be understood as points in this three-dimension space.
Transition: "This analysis reveals a gap: no existing method combines distribution-preserving sampling with randomized spatial redundancy and channel-adaptive hybridization."

**P3 — Method preview and key idea:**
Role: Present the method intuition before technical details. Explain the green/red list adaptation, the two region strategies, and the channel selection mechanism in plain language.
Key claim: The hybrid design addresses both geometric and noise-based attacks.
Transition: "We now formalize this approach."

**P4 — Contribution summary:**
Role: Concise list of three contributions (framework, method + theory, image-to-image extension).
Key claim: Each contribution is scoped to what the evidence supports.

### Current vs. Proposed Storyline Comparison

| Alignment Check | Current Storyline | Proposed Storyline |
|:---|:---|:---|
| Problem alignment | Stakes stated, gap implicit | Explicit gap (no systematic design-space decomposition) |
| Variable alignment | Framework introduced as a list | Framework formalized as (D,R,C) tuple |
| Contribution-evidence alignment | "Outperforms" — unsupported | "Competitive robustness" — evidence-matched |
| Reader-path test | Introduction → Method → Results → Conclusion (closed) | Same, but with clearer motivation-to-method bridge |

### Title Revision Option

Current: "Robust Watermarking for Diffusion Models: A Unified Multi-Dimensional Recipe"
Proposed: "A Three-Dimension Framework for Watermarking Diffusion Models: From Design Taxonomy to Robust Hybrid Instantiation"

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Must fix before resubmission]
├── Issue 2: DDIM inversion formula direction (Page 3)
│   └── Fix: Clarify forward vs inverse step
├── Issue 3: Max-based detection -> average-based (Page 8)
│   └── Fix: Replace max with average + binomial threshold
├── Issue 1: Proposition 4.2 correlation derivation (Page 6)
│   └── Fix: Re-derive with correct event space
├── Issue 5: CFG mismatch validation (Page 8)
│   └── Fix: Add inversion PSNR analysis
├── Issue 4: Overscoped claims (Abstract, Intro, Conclusion)
│   └── Fix: Bound all superiority/scope claims
└── Add limitations paragraph (Conclusion)

[P1: Should fix for strong revision]
├── Formalize framework as (D,R,C) tuple (Section 4.1)
├── Add variance/std to all experimental tables
├── Restructure related work by framework dimensions
└── Add statistical significance tests

[P2: Nice to have]
├── Generalize conditional distribution formula to k partitions
├── Test on additional image-to-image models
└── Evaluate under adaptive attacks
```

### Revision Order (Priority)

1. **Correct the DDIM inversion formula** (1-2 hours) — This is a textual clarification that directly affects reproducibility. High impact, low effort.

2. **Fix Proposition 4.2 derivation** (2-4 hours) — The theoretical justification for the random patch advantage needs to be correct. Re-derive and verify with simulation.

3. **Replace max-based detection with average aggregation** (4-8 hours) — Requires re-running detection experiments with the corrected statistic. High impact on result credibility.

4. **Scope down overclaims** (1 hour) — Textual changes to abstract, introduction, and conclusion. Low effort, high impact on first impression.

5. **Add inversion reliability validation** (4-8 hours) — Compute PSNR over 100 images. Important for demonstrating that the method works despite CFG mismatch.

6. **Add variance and significance to tables** (4-8 hours) — Re-run with 5+ seeds and report std. Essential for statistical credibility.

7. **Add limitations paragraph** (30 minutes) — Quick textual addition.

8. **Formalize the framework** (8-16 hours) — High conceptual impact. Define the tuple (D,R,C) and map existing methods. This would significantly strengthen the paper's core contribution.

### Expected Impact After Fixes

| Fix | Affected Section | Expected Improvement |
|:---|:---|:---|
| DDIM formula clarification | 3, Detection process | Reproducibility ↑ |
| Proposition 4.2 correction | 4.3, Appendix B.2 | Theoretical rigor ↑ |
| Detection aggregation fix | 4.4, 5.2 | Statistical validity ↑ |
| Scope-down claims | Abstract, 1, 6 | Defensibility ↑ |
| Inversion validation | 5.1 | Evidence completeness ↑ |
| Variance in tables | 5.2, 5.3 | Credibility ↑ |
| Limitations paragraph | 6 | Scientific transparency ↑ |
| Framework formalization | 4.1 | Contribution impact ↑ |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|:---|:---|:---|:---|:---|:---|:---|
| E1 | Main comparison (text-to-image) | SD, 512x512, 10 attack types vs 7 baselines | TPR@1%FPR, AUC, Acc, FID, CLIP | Ours: avg TPR 0.984 (Table 2) | Robustness of proposed method | No variance/std reported; max-based aggregation |
| E2 | Image-to-image extension | Instruct-pix2pix, 100 steps, same attacks | AUC per attack (Table 6) | Ours: avg AUC 0.927 | Cross-task generalizability | Single model tested |
| E3 | Watermark capacity & identification | 32 patterns, Ours vs Tree-Ring | Identification accuracy (Table 7) | Ours: 0.961 avg | Capacity advantage of distribution-based method | Only compared to Tree-Ring |
| E4 | Ablation: sampling methods | 5 samplers, clean + adversarial | TPR, CLIP-Score (Table 3) | All ~0.98 adversarial | Sampling-agnostic robustness | Adversarial condition is aggregate, not per-attack |
| E5 | Ablation: patch size | 4, 16, 64, 256 | TPR@1%FPR (Table 4) | 64: best quality-robustness tradeoff | Design parameter effect | Only 4 values tested |
| E6 | Ablation: ring radius | 5 radius ranges | TPR@1%FPR (Table 5) | 5-15: best rotation robustness | Design parameter effect | Rotation only, other geometry not tested |
| E7 | Ablation: component removal | w/o RG, w/o GR, Ours | TPR@1%FPR (Table 8, App A.4) | Both components contribute | Complementarity of hybrid design | Max-based aggregation confounds interpretation |
| E8 | Ablation: inversion/inference steps | 10/25/50/100 steps | TPR@1%FPR (Table 9, App A.5) | Robust across step mismatches | Detection robustness | No analysis of step-mismatch failure mode |
| E9 | Channel analysis | 4 channels, gradient vs accuracy | Accuracy + gradient bar chart (Fig 5) | Gradient correlates with channel robustness | Channel selection via gradient is reliable | Only 4 channels; no ablation of channel-specific assignment strategy |

### Research-Theme Gap Diagnosis

**New Knowledge Gap:** The framework contribution is potentially strong but currently under-developed as a descriptive catalog rather than a formal taxonomy. The theoretical justification (Proposition 4.2) has a derivation issue that undermines the claimed correlation analysis.

**Reproducibility Gap:** The DDIM inversion formula is ambiguous, making it unclear how to reproduce the detection process. Missing implementation details for the channel gradient computation (backprop depth, seed variance).

**Impact on Practice Gap:** The claim of "first systematic approach to image-to-image watermarking" is weakened by single-model validation. Without at least one additional image-to-image model (e.g., SDEdit, Palette), this claim cannot be substantiated.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before Resubmission, ~2 weeks):
├── Exp-A: Inversion reliability validation
│   ├── Compute PSNR(z_T, z_hat_T) over 100 images
│   ├── Report separately for T2I and I2I settings
│   └── Success: PSNR > 25dB average
├── Exp-B: Detection aggregation comparison
│   ├── Compare max vs average vs voting aggregation
│   ├── Calibrate threshold using binomial test (App B.3)
│   └── Success: Average aggregation maintains TPR @1%FPR
└── Exp-C: Variance reporting
    ├── Re-run Tables 1-2 with 5 seeds
    ├── Report mean ± std
    └── Success: std < 0.02 for primary metrics

P1 (During Revision, ~1 month):
├── Exp-D: Additional image-to-image model
│   ├── Test on SDEdit or Palette
│   ├── Same attack protocol as instruct-pix2pix
│   └── Success: AUC > 0.85 on new model
├── Exp-E: Statistical significance test
│   ├── Paired bootstrap test vs Tree-Ring and Gaussian Shading
│   ├── Per-attack and aggregate
│   └── Success: p < 0.05 for average TPR
└── Exp-F: Proposition 4.2 simulation verification
    ├── Monte Carlo simulation of correlation under correct model
    ├── Compare simulated vs analytical correlation
    └── Success: Simulation matches corrected formula

P2 (Extended Work):
├── Exp-G: Adaptive attack evaluation
│   ├── Design attack optimized to remove distribution-based watermark
│   └── Success: Attack can't reduce TPR below 0.8 @1%FPR
└── Exp-H: OOD/generalization test
    ├── Evaluate on unseen datasets (e.g., ImageNet)
    └── Success: FID and TPR within 5% of in-distribution
```

### Proposed Experiment Detail (Key P0 Experiments)

**Exp-A: Inversion Reliability**
- Target Claim: "DDIM inversion reliably reconstructs the initial noise" (used for detection)
- Hypothesis: Inversion under CFG mismatch (generation scale 7.5, inversion scale 1) has sufficient fidelity for watermark detection.
- Minimal Design: Sample 100 images from SD with known z_T. Run DDIM inversion with empty prompt, scale=1. Compute PSNR(z_T, z_hat_T). Report mean, std, and histogram of PSNR.
- Success Criterion: Mean PSNR > 25 dB, and TPR@1%FPR computed with inverted latents does not drop below 0.9 of the oracle (no-inversion) performance.
- Estimated Cost: ~4 GPU-hours.
- Expected Gain: Addresses a key reproducibility and validity concern.

**Exp-B: Detection Aggregation Comparison**
- Target Claim: "Max-based aggregation provides robust detection"
- Hypothesis: Average-based aggregation with calibrated binomial threshold provides equivalent or better robustness with controlled FPR.
- Minimal Design: Re-run detection on all attack settings from Table 2 using: (a) max, (b) average, (c) majority voting. For (b) and (c), calibrate threshold tau using the regularized incomplete beta function to achieve 1% theoretical FPR.
- Success Criterion: Average-based method achieves TPR@1%FPR >= 0.95 of max-based method, with better FPR control.
- Estimated Cost: ~8 GPU-hours.
- Expected Gain: Directly addresses a major methodological concern.

**Exp-C: Variance Reporting**
- Target Claim: All experimental results
- Hypothesis: Reported point estimates are stable across random seeds.
- Minimal Design: Re-run all main experiments (Tables 1, 2) with 5 different random seeds. Report mean ± std for each metric.
- Success Criterion: Standard deviation < 0.02 for all TPR/AUC metrics.
- Estimated Cost: ~16 GPU-hours (can parallelize across 5 GPUs).
- Expected Gain: Converts experimental evidence from Level 1 (descriptive) to Level 2 (statistically grounded).

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

**Rationale:** The paper presents a useful conceptual framework (three-dimension taxonomy) and a technically sound hybrid watermarking method with competitive empirical results. However, the score is constrained by several factors:

- **Research value (primary):** The framework contribution is currently under-developed — it is a descriptive catalog rather than a formal taxonomy. Once formalized, this could be a 7-8 level contribution.
- **Novelty strength (primary):** The adaptation of LLM green/red list to diffusion latent space is non-obvious but incrementally novel. The hybrid combination of Random Gaussian + Gaussian Ring is the most novel technical component. The framework itself is the primary novelty claim but needs formalization.
- **Validity risks:** The max-based detection aggregation issue, Proposition 4.2 derivation concern, and CFG mismatch problem all reduce confidence in the reported results.
- **Scope discipline:** Several claims exceed the evidence, which is a significant concern for reviewer perception.

**Post-Revision Target: [7, 8]/10**

This target assumes the following are fully addressed:
1. Proposition 4.2 is corrected/re-derived (fixing the derivation flaw)
2. Detection aggregation is changed to average-based with binomial test calibration
3. Overscoped claims are bounded to match evidence
4. Variance/std is added to all experimental tables
5. Inversion reliability is validated with reported metrics
6. The framework is formalized as a (D,R,C) tuple with existing methods mapped
7. A limitations paragraph is added

If all P0 and P1 fixes are executed, the paper could reach 8/10, reflecting a solid contribution to the field with rigorous theoretical and empirical support.