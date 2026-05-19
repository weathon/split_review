## Summary
# Final Review Report

## Summary

This paper presents AdvI2I, a framework that generates adversarial images to induce Image-to-Image (I2I) diffusion models to produce Not Safe for Work (NSFW) content while keeping text prompts benign. The approach has three stages: (1) extracting an NSFW concept vector from contrastive prompt pairs, (2) training an adversarial image generator (using a pre-trained VAE architecture) to shift input images such that their latent diffusion features match those conditioned on NSFW-shifted text embeddings, and (3) deploying the generator to convert any benign image into an adversarial one. An adaptive variant, AdvI2I-Adaptive, adds a loss term to minimize cosine similarity with safety checker NSFW embeddings and incorporates Gaussian noise during training to maintain high attack success rates (ASR) under defenses.

The paper addresses a timely and important security concern in generative AI safety. The experimental results show ASR of 81-83% without defenses on InstructPix2Pix and SDv1.5-Inpainting, with the adaptive variant maintaining >70% ASR under safety checker defenses. The core contribution — demonstrating that image-condition manipulation can bypass text-only safety mechanisms in I2I models — is well-motivated and practically relevant.

However, the manuscript has several significant weaknesses: (1) the loss formulation (Eq. 2-3) is underspecified for reproducibility, (2) all experiments lack variance/statistical significance reporting, (3) the MMA-Diffusion baseline is compared in an adapted image-only variant rather than its original multimodal form, (4) the dataset is sourced from a narrow domain ('sexy' category non-NSFW images) which may overstate generalization, (5) the SLD defense is evaluated with heavily modified parameters (guidance scale=1000 vs standard ~7.5), and (6) the conclusion omits key limitations including the sharp ASR drop to 34% on SDv3.0 (data-filtered model). Novelty verification is deferred as external paper search is unavailable in this run.

## Strengths
**S1 — Timely and important research problem.** The paper addresses a genuine and urgent safety concern: adversarial image attacks on I2I diffusion models. As these models become widely deployed for image editing, understanding their vulnerability surface is critical. The paper correctly identifies that existing safety research has focused predominantly on text-prompt attacks, leaving image-condition attacks under-explored.

**S2 — Well-motivated logical narrative.** The introduction builds a clear chain: (1) diffusion models can generate NSFW content due to dataset contamination, (2) adversarial text prompts can do this but are detectable by filters, (3) therefore we need to examine the image condition side. This narrative effectively motivates the need for the AdvI2I framework.

**S3 — Clean technical pipeline with three well-defined stages.** The three-step framework (NSFW concept extraction → adversarial generator training → inference) is logically structured and easy to follow. The decision to train a generator rather than per-image optimization is practical and supports the claim of universal transferability.

**S4 — Comprehensive defense evaluation.** The paper evaluates against five defense strategies (SLD, Negative Prompt, Gaussian Noising, Safety Checker, and four text filters) across two diffusion models and two NSFW concepts (nudity, violence). This coverage provides a reasonably thorough assessment of the attack's robustness.

**S5 — Adaptive variant demonstrates genuine improvement.** AdvI2I-Adaptive's ability to maintain >70% ASR under Safety Checker defense (vs 10-18% for standard AdvI2I) is a meaningful empirical contribution. The adaptive loss design, despite its formulation issues, shows clear practical effectiveness.

**S6 — Transferability evaluation across model versions.** The paper evaluates cross-version transferability (SDv1.5 → SDv2.0/v2.1/v3.0) and cross-architecture transferability (InstructPix2Pix → SD-Turbo, SDv1.5-Inpainting → FLUX.1-dev). While the results expose important limitations, the inclusion of this analysis is commendable and provides useful insights about the attack's data-dependency.

## Weaknesses
**W1 — Reproducibility-critical underspecification (Major).** The loss function in Eq. (2) uses an undefined feature map $f^t_\theta(x, \tau)$. The paper does not specify whether this is a UNet bottleneck feature, a cross-attention layer output, or the predicted noise itself. The VAE "generator" $g_\psi$ is described as using a "pre-trained VAE" but does not specify where learnable parameters $\psi$ are added (fine-tuned decoder? additional perturbation network?). Without these details, the core algorithm cannot be independently reproduced.

**W2 — No statistical significance or variance reporting (Major).** All ASR results are single-point estimates without standard deviation, confidence intervals, or multi-seed averaging. Given the stochastic nature of diffusion sampling, the 3-13% differences between methods may not be statistically significant. This is a critical gap for a security evaluation paper where claims of superiority depend on these numbers.

**W3 — MMA-Diffusion baseline comparison is unfair (Major).** MMA-Diffusion is adapted into an image-only variant (pre-computed adversarial text prompts, then only image perturbations trained), rather than compared in its original multimodal form (joint text+image optimization). This understates MMA's capability and makes the "AdvI2I outperforms MMA" claim questionable. MMA achieves 68.5% ASR even in this weakened form, suggesting the original multimodal MMA may be a much stronger competitor.

**W4 — Dataset bias toward sexually suggestive content (Major).** The training/evaluation images come from the "sexy" category of the NSFW Data Scraper, filtered to remove explicitly NSFW images. These images predominantly contain human bodies in suggestive contexts, making them semantically closer to NSFW concepts than neutral images. This selection bias likely inflates ASR compared to a truly neutral test set (e.g., COCO, ImageNet). The 200-sample test set is also small.

**W5 — SLD defense evaluation uses heavily modified parameters (Major).** The SLD defense is evaluated with a guidance scale of 1000 (vs standard ~7.5) and other modified hyperparameters tuned to preserve I2I image quality. The paper does not report ASR under standard SLD settings, making the defense comparison potentially misleading. A defense that must be weakened to preserve functionality is not evaluated fairly.

**W6 — Conclusion omits key limitations (Major).** The conclusion does not mention: (a) the sharp ASR drop to 34% on SDv3.0 (data-filtered model), (b) the dataset domain limitation, (c) the lack of significance testing, or (d) the limited cross-architecture transferability. This gives an overly optimistic impression of the attack's practical threat.

**W7 — Related Work is a literature list, not a comparison (Minor).** The Related Work section reads as chronological summaries without organizing by comparison axes or explicitly differentiating AdvI2I from closest prior work (Ring-A-Bell, MMA-Diffusion). This weakens the novelty positioning.

**W8 — Face-Adapter image quality comparison is mismatched (Minor).** The comparison against Face-Adapter (a face-swapping method) in Table 14 is methodologically inappropriate — different objectives (adversarial attack vs identity preservation), different domains (full-body vs face), and different constraints (bounded perturbation vs unbounded editing). This does not strengthen the paper.

**W9 — Abstract lacks quantitative results (Minor).** The abstract describes the attack qualitatively but does not provide key ASR numbers or bounded scope conditions, reducing its self-contained impact.

**W10 — Grammar issues (Minor).** Contribution bullet 1 reads "We systematically evaluates" (subject-verb disagreement). Several sentences have missing spaces (e.g., "ofadversarial"). Table 4 title says "Model" repeated. These reduce professionalism.

## Key Issues
The following ranked error board lists the core defects by (Severity, Research-Value Impact, Validity Risk, Fixability, Confidence):

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Summary |
|------|-------|----------|---------------|------------|------------|---------|
| 1 | Loss formulation underspecified (Eq. 2-3, $f^t_\theta$, $g_\psi$ architecture) | Major | High | Easy | High | Core algorithm cannot be reproduced; define $f^t_\theta$ explicitly, specify $g_\psi$ parameters, fix Eq. (3) notation |
| 2 | No variance/statistical-significance reporting on all ASR results | Major | High | Medium | High | Without std/CI, reported differences may be noise; add 3-seed experiments + McNemar tests |
| 3 | MMA-Diffusion compared in weakened image-only form | Major | High | Medium | High | Original multimodal MMA not evaluated; add MMA-Full baseline + clarify adaptation |
| 4 | Dataset bias from 'sexy' category non-NSFW images | Major | Medium | Medium | High | Likely inflates ASR vs neutral domain; add COCO/ImageNet test set |
| 5 | SLD evaluated with non-standard parameters (guidance=1000) | Major | Medium | Easy | High | Report ASR under standard SLD settings alongside modified config |
| 6 | Undisclosed limitations in Conclusion (SDv3.0 drop, dataset bias) | Major | Low | Easy | High | Restructure conclusion with validated findings + bounded limitations + specific future work |
| 7 | Face-Adapter comparison is methodologically mismatched | Major | Low | Easy | High | Remove or reframe as unrelated-domain reference only |
| 8 | NSFW concept vector extraction lacks prompt details, N, sensitivity analysis | Major | Low | Easy | Medium | Provide prompt templates, N count, and c robustness analysis |
| 9 | Related Work lacks comparison axes and explicit differentiation | Minor | Low | Medium | High | Reorganize by attack modality/defense type with differentiation table |
| 10 | Text filter evaluation non-adaptive only | Minor | Low | Medium | Medium | Add adaptive-attack filter evaluation or bound claims

## Actionable Suggestions
### Suggestion 1 (Priority P0 — Must): Specify $f^t_\theta$ and $g_\psi$ architecture

**Location:** Page 5 — Adversarial Image Generator Training

**Problem:** The latent feature $f^t_\theta$ is not formally defined; the VAE generator $g_\psi$ architecture is not described.

**Action:** 
1. Define $f^t_\theta(x, \tau) = z_{t-1}$ after one denoising step: $z_{t-1} = \alpha_t(z_t - \gamma_t \epsilon_\theta(z_t, \mathcal{E}(x), \tau, t)) + \sigma_t\varepsilon$.
2. Specify $g_\psi$: if it is a lightweight CNN appended to the VAE decoder, state it explicitly. If the VAE encoder-decoder is fine-tuned, report which layers are updated.
3. Fix Eq. (3): Remove $\tau_\theta(p)$ from decoder $D$'s input — the safety checker operates on decoded images, not text-conditioned features.

### Suggestion 2 (Priority P0 — Must): Add statistical significance and variance

**Location:** Page 7-9 — Results and Analysis

**Problem:** All ASR values in Tables 3-6, 9-11 are single-point estimates.

**Action:** 
1. Run all experiments with at least 3 random seeds and report mean $\pm$ std.
2. Add McNemar's test comparing AdvI2I vs MMA under each defense condition.
3. Report NudeNet confidence score distributions alongside binary ASR.
4. Update the narrative to explicitly note which differences are statistically significant.

### Suggestion 3 (Priority P0 — Should): Add MMA-Full baseline

**Location:** Page 7 — Baselines

**Problem:** MMA-Diffusion is adapted to an image-only variant, understating its capability.

**Action:**
1. Add a MMA-Full baseline that jointly optimizes text and image perturbations as originally designed.
2. Clearly label the existing adaptation as "MMA-ImageOnly."
3. Discuss the comparison: does AdvI2I's advantage persist when MMA uses its full multimodal capability?

### Suggestion 4 (Priority P0 — Should): Add neutral-domain test set

**Location:** Page 6 — Experimental Settings: Datasets

**Problem:** Dataset from "sexy" category non-NSFW images may be biased.

**Action:**
1. Supplement with 200-400 images from COCO or ImageNet (non-human, non-suggestive categories).
2. Report ASR separately on the two test sets.
3. If ASR drops significantly on neutral images, discuss the implications for the practical threat model.

### Suggestion 5 (Priority P0 — Should): Report standard SLD configuration

**Location:** Page 14 — Configuration of SLD (Appendix A.3)

**Problem:** SLD uses guidance scale = 1000 (vs standard ~7.5) and other modified parameters.

**Action:**
1. Report ASR under both standard SLD ("Medium") and the I2I-tuned configuration.
2. Report image quality metrics (FID, CLIP score) for benign editing under both configurations.
3. Discuss the trade-off: if standard SLD breaks I2I functionality, it may not be a viable defense.

### Suggestion 6 (Priority P1 — Should): Revise Conclusion

**Location:** Page 9 — Conclusion

**Action:**
Restructure into three paragraphs:
- Paragraph 1: Validated findings with key ASR numbers (81-83% w/o defense, >70% adaptive under SC).
- Paragraph 2: Bounded limitations: dataset domain, SDv3.0 drop (34% ASR), no significance tests.
- Paragraph 3: Specific future directions: (a) adversarially robust I2I training, (b) joint text+image filtering, (c) broader threat model evaluation.

### Suggestion 7 (Priority P1 — Should): Reorganize Related Work

**Location:** Page 2 — Related Work

**Action:** 
Organize by comparison axes: (a) Attack modality (text-only vs multimodal vs image-only), (b) Optimization target (steering vectors, latent features, pixel space), (c) Defense awareness. Add a differentiation table comparing AdvI2I vs Ring-A-Bell and MMA-Diffusion on key design dimensions.

### Suggestion 8 (Priority P1 — Should): Add NSFW concept extraction details

**Location:** Page 5 — NSFW Concept Vector Extraction

**Action:**
1. Provide the full prompt pair templates in an Appendix table.
2. Report $N$ (number of pairs) per concept.
3. Add sensitivity analysis: vary prompt pairs and measure impact on ASR.
4. Show t-SNE/PCA visualization of the embedding shift $\tilde{\tau}$.

### Suggestion 9 (Priority P2 — Nice-to-have): Add adaptive filter evaluation

**Action:** Re-optimize adversarial prompts with filter-awareness (e.g., differentiable perplexity surrogate) to test whether the "filters are effective" claim holds under adaptive attacks.

### Suggestion 10 (Priority P2 — Nice-to-have): Remove or reframe Face-Adapter comparison

**Action:** The Face-Adapter comparison in Table 14 is mismatched. Either remove it or reframe as "unrelated-domain reference only" and add a proper adversarial image quality baseline (e.g., PGD attack quality metrics).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

The abstract should follow a tight 4-sentence structure with concrete numbers:

- **S1 (Problem):** "Recent advances in Image-to-Image (I2I) diffusion models have enabled high-quality image editing, but also introduced risks of generating Not Safe for Work (NSFW) content."
- **S2 (Limitation of prior work):** "Existing safety research focuses on detecting adversarial text prompts, which can be effectively filtered by perplexity- and LLM-based detectors with attack success rate (ASR) reductions of 58-80%."
- **S3 (Proposed method and key idea):** "We expose a previously overlooked vulnerability — adversarial image attacks on I2I diffusion models — and propose AdvI2I, which trains an adversarial image generator to produce perturbations that, when used as conditioning input, induce NSFW generation while keeping text prompts benign."
- **S4 (Key result, bounded):** "On InstructPix2Pix and SDv1.5-Inpainting, AdvI2I achieves 81-83% ASR without defenses; the adaptive variant (AdvI2I-Adaptive) maintains >70% ASR under safety checker defenses, demonstrating that current I2I safeguards are insufficient against image-condition attacks."
- **S5 (Broader implication):** "These findings highlight the urgent need for joint text-image safety mechanisms in diffusion model deployment."

### Introduction Outline (Complete)

The introduction should follow a Big Picture → Gap → Solution → Evidence → Contribution arc. Current introduction is close to this but can be tightened:

**P1 (Establish territory and problem importance):**
- Role: Define the task (diffusion models for image synthesis), the problem (NSFW generation from dataset contamination), and the stakes (safety-critical deployment).
- Current issue: The phrase "malicious users" introduces unnecessary intent attribution.
- Recommendation: Use neutral threat-model language ("adversarial actors").
- Transition sentence: "Existing defenses have focused on filtering text prompts, but..."

**P2 (Identify the gap — why text-only defense is insufficient):**
- Role: Show that adversarial text prompts are detectable, motivating the need for image-side attacks.
- Current issue: Reports experimental numbers (58% ASR reduction, <20% after LLM filter) without methodological context.
- Recommendation: State the high-level claim that adversarial prompts are detectable, move detailed numbers to Section 3.1.
- Keep the key question: "Does the rejection of adversarial text prompts truly ensure the safety of diffusion models?"

**P3 (Present the proposed solution and intuition):**
- Role: Introduce AdvI2I, the key idea (shifting NSFW concepts from text space to image perturbations), and the I2I threat model.
- Current strength: The "president example" is vivid but potentially problematic. Replace with "a photograph of a public figure."
- Add: Concrete intuition about how the adversarial generator works (noise generator + latent feature matching).

**P4 (Method overview + adaptive variant):**
- Role: Describe the two-step framework (concept extraction → generator training) and the adaptive enhancement.
- Keep the three-step explanation from current text but improve conciseness.

**P5 (Contributions — concrete and non-hype):**
- Current issue: Contribution 3 ("raises awareness") is not a verifiable contribution.
- Recommendation: Replace with a concrete deliverable (code release, benchmark dataset) or merge into context.
- Revised contributions:
  (1) Systematic evaluation showing text filters reduce adversarial prompt ASR by 58-80%, motivating image-side analysis.
  (2) AdvI2I: the first adversarial image attack on I2I diffusion models, achieving 81-83% ASR.
  (3) AdvI2I-Adaptive: defense-aware variant maintaining >70% ASR under safety checkers, with released generator and evaluation dataset.

### Alternative Storyline Candidates

**Candidate A (Current — Problem-Driven):** Filter detectability of text prompts → Image-side vulnerability → AdvI2I framework → Results → Implications. Best choice because: (a) strong problem alignment (filter detectability directly motivates image attack), (b) clear variable alignment (filters in intro → evaluated in experiments), (c) contribution-evidence alignment (detectability claim → Table 2 evidence). Recommended to keep with tightening.

**Candidate B (Threat-Model Driven):** I2I diffusion models are increasingly deployed → Existing safety focuses on text → Image condition is an open attack surface → AdvI2I demonstrates practical exploitation → Urgent need for joint defense. Would work for a security-focused venue but less effective for ICLR audience.

**Candidate C (Method-First):** Adversarial image generators → Latent feature matching → NSFW concept extraction → Empirical validation. Less effective because it front-loads technical details before establishing the problem stakes and gap.

**Recommendation:** Keep the current problem-driven narrative (Candidate A) with the tightening edits described above.

## Priority Revision Plan
The revision plan is organized by priority (P0 = publication-critical, P1 = strongly recommended, P2 = quality improvement) and expected effort.

```text
ASCII Diagram — Revision Strategy Roadmap

[Core Algorithm Underspecified (P0)]
    → Define f^t_θ, specify g_ψ architecture, fix Eq. (3) notation
    → Expected impact: Reproducibility restored, reviewer confidence improved

[No Statistical Significance (P0)]
    → Add 3-seed experiments + std + McNemar tests
    → Expected impact: Claims become verifiable, comparisons credible

[MMA Baseline Unfair (P0)]
    → Add MMA-Full (original multimodal form), label adapted variant
    → Expected impact: Fair comparison, honest positioning

[Dataset Domain Bias (P0)]
    → Add COCO/ImageNet neutral test set, report ASR separately
    → Expected impact: Generalizability assessed, threat model scoped

[SLD Misconfiguration (P0)]
    → Report standard SLD ASR + image quality metrics
    → Expected impact: Defense evaluation becomes fair and informative

[Conclusion Missing Limitations (P1)]
    → Restructure into validated findings + limitations + future work
    → Expected impact: Scientific completeness, honesty

[Related Work Reorganization (P1)]
    → Organize by comparison axes, add differentiation table
    → Expected impact: Novelty positioning strengthened

[NSFW Concept Extraction Details (P1)]
    → Provide prompt templates, N, sensitivity analysis
    → Expected impact: Reproducibility improved

[Face-Adapter Removal (P2)]
    → Remove or reframe as unrelated reference
    → Expected impact: Cleaner evaluation section

[Adaptive Filter Evaluation (P2)]
    → Optional experiment for strengthened motivation
    → Expected impact: Motivation narrative reinforced
```

| Priority | Task | Effort | Expected Gain | Acceptance Criteria |
|----------|------|--------|---------------|---------------------|
| P0 | Specify $f^t_\theta$, $g_\psi$, fix Eq. (3) | Low | Reproducibility, reviewer trust | Formal definitions added to Section 3.2 |
| P0 | 3-seed experiments + std + significance tests | Medium | Statistical credibility | Tables 3-6 updated with mean±std |
| P0 | Add MMA-Full baseline | Low | Fair comparison, honest positioning | New column in Tables 3-4 |
| P0 | Add neutral-domain test set (COCO) | Medium | Assess true generalization | Extra row in Table 5 |
| P0 | Report standard SLD configuration results | Low | Fair defense evaluation | Extra column in Tables 3-4 |
| P1 | Revise Conclusion with limitations | Low | Scientific completeness | Paragraphs restructured |
| P1 | Reorganize Related Work | Medium | Clearer positioning | Section reorganized by axes |
| P1 | Add NSFW prompt details + sensitivity | Low | Reproducibility | Appendix table + analysis |
| P2 | Remove/reframe Face-Adapter comparison | Low | Cleaner evaluation | Table 14 removed or reframed |
| P2 | Adaptive filter evaluation | Medium | Stronger motivation | Extra experiment (optional) |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Filter detectability of adversarial prompts | 4 filters × 5 attack methods on SD | ASR reduction % | 58% avg ASR reduction; LLM filter reduces to <20% | C1: Text filters are effective | Non-adaptive only; LLM filter details missing |
| E2 | AdvI2I attack effectiveness (InstructPix2Pix) | Nudity/violence, 5 defenses | ASR | 81.5% (nudity, no defense) | C2: AdvI2I induces NSFW | No variance/std; single seed |
| E3 | AdvI2I attack effectiveness (SDv1.5-Inpainting) | Same as E2 | ASR | 82.5% (nudity, no defense) | C2 | No variance/std; single seed |
| E4 | AdvI2I-Adaptive under Safety Checker | Adaptive loss + Gaussian noise | ASR | 70.5% (InstructPix2Pix, SC) | C3: Adaptive variant resilient | Eq. (3) formulation issue; gradient path unclear |
| E5 | Unseen image/prompt generalization | Held-out samples from same source | ASR | 63.5-76.5% (unseen images) | C2: Generalizable | Same data source; no cross-domain test |
| E6 | Noise bound variation | ϵ = 32/64/128, InstructPix2Pix | ASR | 76.5-84.5% w/o defense | C2 | No variance/std |
| E7 | Concept strength α variation | α = 2.2/2.5/2.8 | ASR | Peak 82.5% at α=2.8 | C2 | Small effect range; no analysis |
| E8 | W/o Generator ablation | Direct perturbation vs generator | ASR | 18.5% vs 81.5% (AdvI2I) | Generator is essential | Demonstrates clear necessity |
| E9 | SLD configuration tuning | Guidance=1000, warmup=7, etc. | Image quality, ASR | ASR 72.5-78.0% | SLD is partially effective | Non-standard config not validated against standard |
| E10 | Model transferability (SDv1.5→SDv2.0/2.1/3.0) | Cross-version | ASR | 80.5-84.0% (v2.0/2.1), 34% (v3.0) | C2 | Drop on v3.0 unexplained mechanism |
| E11 | Cross-architecture transferability | InstructPix2Pix→SD-Turbo, SD→FLUX | ASR | 35% (Turbo), 74% (FLUX) | C2 | Inconsistent across architectures |
| E12 | Safety checker transferability | ViT-L/14→ViT-B/32 | ASR | 72.0%→66.5% | C3: Partial transfer | Single target model |

### Research-Theme Gap Diagnosis

The following core research-value claims are weakly supported:

1. **"New knowledge" — Is the image-side vulnerability truly novel?** The paper acknowledges that MMA-Diffusion already uses image modalities. The differentiation is that MMA jointly optimizes text+image while AdvI2I is image-only. However, without a fair MMA-Full comparison, the incremental novelty cannot be assessed. **Gap:** Missing MMA-Full baseline and explicit differentiation analysis.

2. **"Reproducibility/Reusability" — Can the method be reproduced?** The underspecified loss function ($f^t_\theta$ undefined, $g_\psi$ architecture unclear) and missing prompt pair details prevent independent reproduction. **Gap:** Technical details insufficient.

3. **"Potential to change practice/understanding" — How urgent is the threat?** The paper claims a "significant but underexplored security vulnerability" but the 34% ASR on SDv3.0 suggests the threat is highly dependent on training data contamination. The threat model's scope is unclear. **Gap:** No discussion of when the attack does and does not work.

### Proposed Research Experiments

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

P0 (Before Resubmission):
  ┌─ E13: Multi-seed experiments (3 seeds) + std + McNemar tests
  │     → Tables 3-6, 9-11 updated
  ├─ E14: MMA-Full baseline (original multimodal form)
  │     → New column in Tables 3-4
  ├─ E15: COCO/ImageNet neutral test set
  │     → Extra row in Table 5
  └─ E16: Standard SLD configuration evaluation
        → Extra column in defense tables

P1 (Before Resubmission, if time allows):
  ┌─ E17: NSFW concept vector sensitivity analysis
  │     → Vary prompt pairs, measure ASR stability
  ├─ E18: Latent feature visualization (t-SNE of τ(p) vs τ̃)
  │     → Figure demonstrating embedding shift
  └─ E19: Per-concept (nudity vs violence) prompt pair analysis
        → Separate c vectors, compare effectiveness

P2 (Future Work):
  ┌─ E20: Adaptive filter evaluation
  │     → Re-optimize prompts with filter awareness
  ├─ E21: Human evaluation of adversarial image quality
  │     → 50 participants, forced-choice detection
  └─ E22: Ablation of timestep t choice in Eq. (2)
        → Compare t ∈ {1, 5, 10, 50}
```

**Experiment Details:**

| ID | Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Priority |
|----|-------------|-----------|---------------|----------|---------|-------------------|----------|
| E13 | All claims | ASR differences are statistically robust | 3 seeds, same hyperparameters | Same data splits | Mean±std ASR, McNemar p-value | p<0.05 for AdvI2I vs MMA in no-defense setting | P0 |
| E14 | C2 (novelty) | AdvI2I's advantage persists under fair comparison | MMA-Full: jointly optimize text+image perturbations | Same training budget, epochs | ASR | ASR(AdvI2I) > ASR(MMA-Full) | P0 |
| E15 | C2 (generalization) | ASR drops on neutral images | 200 COCO images, same prompt set | Compare vs 'sexy' category ASR | ASR | Report delta; no threshold required | P0 |
| E16 | C3 (robustness) | Standard SLD more effective than tuned version | Standard SLD "Medium" settings | Same test pipeline | ASR, FID, CLIP score | Report both; discuss trade-off | P0 |
| E17 | C1 (foundation) | c vector is stable under prompt perturbation | Subsampling prompt pairs | 5 random subsets | ASR | Std < 3% across subsets | P1 |
| E20 | C1 (motivation) | Adaptive attacks bypass text filters | Filter-aware prompt optimization | Same filter pipeline | ASR before/after adaptation | Report degradation | P2 |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

The paper addresses a timely and practically important security problem with a well-motivated pipeline and generally convincing empirical results. However, several significant weaknesses prevent a higher score:

- **Novelty/Research Value (primary dimension):** The core idea — adversarial image attacks on I2I diffusion models — is well-motivated and the adaptive variant shows clear practical improvement. However, without a fair comparison to MMA-Diffusion in its original multimodal form, the incremental novelty cannot be fully assessed. The strong reliance on existing techniques (steering vectors from Ring-A-Bell, contrastive prompt pairs, latent feature matching) means the technical novelty is moderate. The paper's primary value is in *systematizing* and *demonstrating* the I2I image-side threat rather than introducing a fundamentally new attack paradigm. **Score contribution: 6/10.**

- **Validity/Soundness:** The experimental evaluation is comprehensive (2 models, 2 concepts, 5 defenses) but undermined by (a) no statistical significance testing, (b) a dataset that may inflate ASR, (c) an unfairly adapted MMA baseline, and (d) a heavily modified SLD configuration. These issues reduce confidence in the claimed attack superiority. **Score contribution: 5/10.**

- **Reproducibility:** The underspecified loss function, undefined VAE generator architecture, and missing prompt pair details significantly hinder independent reproduction. **Score contribution: 4/10.**

- **Presentation/Clarity:** The paper is generally well-written with a clear narrative structure. The pipeline figure is helpful. However, the Related Work is a list rather than structured comparison, the third contribution is not concrete, and the conclusion omits key limitations. **Score contribution: 7/10.**

**Post-Revision Target: [7.5, 8.5] / 10**

If the following P0 issues are addressed: (1) specify $f^t_\theta$, $g_\psi$, and fix Eq. (3), (2) add 3-seed experiments with statistical tests, (3) add MMA-Full baseline, (4) add neutral-domain test set, (5) report standard SLD configuration, and (6) revise conclusion with limitations — the paper could reach 7.5-8.5/10 by substantially improving validity, fairness, and reproducibility. The core research value is solid; the main barriers to a higher score are methodological rigor gaps rather than fundamental flaws in the approach or motivation.