## Summary
# Final Review Report

## Summary

This paper presents Control-GIC, a controllable generative image compression framework based on VQGAN that enables variable-bitrate adaptation with a single model. The core idea is to correlate local patch information density (measured by spatial entropy) with multi-granularity feature representations: smooth patches use coarse features (16×16), textured patches use fine features (4×4). By adjusting the ratios of fine/medium/coarse granularities (r1, r2, r3), the model controls the number of VQ-indices transmitted, thereby achieving continuous bitrate control. A probabilistic conditional decoder reconstructs images by progressively injecting multi-granularity encoder features into the decoder layers. A statistical entropy coding module precomputes codebook frequency statistics from training data for efficient lossless compression.

The method is evaluated on Kodak, DIV2K, and CLIC2020 against generative (HiFiC, MRIC, MS-ILLM, CDC), variable-rate (SCR, CTC), classical NIC (M&S Hyperprior), and traditional codecs (BPG, VVC). Results show competitive perceptual quality (LPIPS, DISTS, NIQE) with faster encoding/decoding, while a single model supports flexible bitrate control across approximately 0.07–0.6 bpp.

**Strengths:** The granularity-based rate control is a novel and well-motivated approach that bridges VQGAN with variable-rate compression. The unified single-model paradigm addresses a practical deployment concern. The decoder ablation study cleanly validates the contribution of each granularity condition. The efficiency analysis (encoding/decoding speed) demonstrates practical advantage.

**Core Weaknesses:** (1) Overclaimed "first" novelty claim without adequate differentiation from existing variable-rate generative methods. (2) "Probabilistic conditional decoder" naming is misleading — the implementation is a deterministic feature replacement, not probabilistic. (3) No statistical variance reported for any experimental result. (4) Key hyperparameters (GAN loss λ, MSE/LPIPS weighting, training ratio) are unreported. (5) Entropy coding comparison uses a weak baseline.

## Strengths
1. **Novel Granularity-Based Rate Control Mechanism.** The core idea of correlating local patch information density (spatial entropy) with multi-granularity VQ representations (fine 4×4, medium 8×8, coarse 16×16) is a principled and well-motivated approach. Unlike prior variable-rate methods that adjust scalar quantization parameters or truncation thresholds, Control-GIC directly controls the number of transmitted VQ-indices at the patch level, enabling continuous bitrate adjustment across a wide range (~0.07–0.6 bpp) with a single trained model. This bridges VQGAN-based generative compression with the rate-adaptation problem in a natural way.

2. **Single-Model Flexibility with Competitive Perceptual Quality.** The paper convincingly demonstrates that a single Control-GIC model achieves perceptual quality competitive with state-of-the-art generative methods (HiFiC, MRIC, MS-ILLM, CDC) that require separate models per bitrate. This is a meaningful practical achievement for deployment scenarios requiring multiple bitrate points. The qualitative results (Figures 6, 12, 13) show that Control-GIC preserves texture integrity better than several baselines.

3. **Efficiency Advantage.** The encoding/decoding speed analysis (Figure 5) shows Control-GIC achieves the fastest inference among compared methods (e.g., 7× faster encoding than MS-ILLM, 4× faster than MRIC). This speed advantage, combined with single-model flexibility, is a compelling practical contribution.

4. **Clean Ablation Design.** The decoder ablation study (Figure 8) systematically removes medium-grained and fine-grained conditions to isolate their contributions. The finding that fine-grained conditioning provides more benefit than medium-grained is insightful and supports the design choice of prioritizing fine-grained features in deeper decoder layers.

5. **Thorough Evaluation Suite.** The paper evaluates on three standard benchmarks (Kodak, DIV2K, CLIC2020) using a comprehensive set of perceptual (LPIPS, DISTS), distortion (PSNR), generative (FID, KID), and no-reference (NIQE) metrics, providing a multi-faceted view of performance.

## Weaknesses
1. **Overclaimed Novelty ("First" Claim).** The abstract and contribution statement claim Control-GIC is "the first capable of fine-grained bitrate adaptation across a broad spectrum" in generative compression. However, the paper itself cites Iwai et al. (2024) and Guo et al. (2023) as prior work on scalable/variable-rate generative compression. Without explicit differentiation regarding what aspect is genuinely novel (continuous granularity vs. discrete preset levels), this "first" claim is unsubstantiated and vulnerable during review. [Severity: Major]

2. **Misleading "Probabilistic" Decoder Labeling.** The decoder is described as "probabilistic conditional decoder" with Eq. (3) using conditional probability notation (y2 ∼ p(y2 | ...)). However, the actual implementation in Eq. (4) is a deterministic feature replacement: y2 = D1(y1)⊙(1−m2) + (ˆz)↓2⊙m2. There is no distribution learning, no sampling, and no probabilistic inference. This naming is misleading and misrepresents the technical contribution. [Severity: Major]

3. **No Statistical Variance in Experiments.** Every metric (LPIPS, PSNR, FID, KID, etc.) is reported as a single-point estimate without standard deviations, confidence intervals, or multi-seed runs. Given that perceptual metrics have known variance, readers cannot assess whether observed differences between methods are statistically significant. The paper also lacks significance tests. [Severity: Major]

4. **Missing Hyperparameter Reporting.** Key training hyperparameters are unreported: (a) The GAN loss weight λ in Eq. (8) is never specified. (b) The weighting of MSE vs. LPIPS in Eq. (6) is not defined — simply writing (dM + dP) ignores the scale mismatch between MSE and LPIPS values. (c) The training granularity ratio (50%, 40%, 10%) is used without ablation or justification. [Severity: Major]

5. **Weak Entropy Coding Baseline Comparison.** Table 1 compares statistical entropy coding against "Huffman coding with uniform frequency," which is deliberately suboptimal. A realistic baseline would be per-image adaptive Huffman coding (computing frequency per image and transmitting the codebook) or arithmetic coding with a learned entropy model. The reported 5% savings may not hold against stronger baselines. [Severity: Minor]

6. **Related Work Reads as Paper List.** Both related-work paragraphs are organized chronologically rather than thematically. The paper does not include a comparison table or explicit dimension-based positioning of Control-GIC against closest baselines (Mao et al. for VQGAN compression, Iwai et al. for scalable generative, SCR for variable-rate). [Severity: Minor]

7. **Encoder Architecture Underspecified.** The granularity-informed encoder description (Section 3.1) does not specify how three multi-scale feature maps (z1, z2, z3) are produced. The mapping from per-patch entropy values to spatial positions in feature maps at different resolutions is not explained. This limits reproducibility. [Severity: Minor]

8. **No Limitation Disclosure in Conclusion.** The conclusion (Section 5) restates contributions without acknowledging any limitations. The appendix (A.4) reveals that small faces are challenging and require "more targeted design in future work," but this is absent from the main conclusion. [Severity: Minor]

9. **Potential Distribution Mismatch in Entropy Coding.** The statistical entropy coding uses a single global frequency table computed over the training set (OpenImages). The paper does not analyze how per-image code distribution deviates from the global average, which could cause inefficiency for out-of-distribution test images. [Severity: Minor]

10. **Missing Fairness Discussion in Comparisons.** The paper compares against methods with different training data, training budgets, and optimization targets without a fairness discussion paragraph. For example, HiFiC uses a different training set, CDC uses a diffusion backbone. This context is needed for honest interpretation of the results. [Severity: Minor]

## Key Issues
### Issue 1: Overclaimed "First" Novelty + Misleading "Probabilistic" Decoder Label (Priority P0)

These two issues together undermine the paper's scientific rigor. The "first" claim (Abstract, Page 1, Contribution C1 on Page 3) is unsubstantiated given existing variable-rate generative work (Iwai et al., Guo et al.). The "probabilistic conditional decoder" label (Page 5, Section 3.2) misrepresents a deterministic feature replacement as probabilistic modeling. Both issues can be fixed with wording adjustments, but they signal a pattern of overclaiming that must be addressed.

**Required Actions:**
- Replace "first" with "to our knowledge, the first to enable continuous granularity-level bitrate control in a VQGAN-based generative compression framework, complementing existing discrete-level variable-rate generative methods."
- Replace "probabilistic conditional decoder" with "conditional feature refinement decoder" throughout the paper.
- Replace probabilistic notation in Eq. (3) with deterministic function notation.

### Issue 2: Missing Statistical Variance and Hyperparameter Reporting (Priority P0)

The absence of variance metrics and key hyperparameter values significantly impacts reproducibility and trustworthiness of reported results. Without standard deviations, readers cannot assess whether Control-GIC's improvements over MS-ILLM or MRIC are significant.

**Required Actions:**
- Report mean ± std over at least 3 seeds for LPIPS, PSNR, DISTS, FID on Kodak and DIV2K.
- Report the GAN loss weight λ and MSE/LPIPS weighting coefficients.
- Report λ selection method (validation-based or heuristic).

### Issue 3: Weak Entropy Coding Baseline (Priority P1)

The entropy coding ablation compares against a straw-man baseline (uniform frequency Huffman). Realistic baselines would include per-image adaptive Huffman and arithmetic coding.

**Required Actions:**
- Add comparison against per-image adaptive Huffman coding.
- If adaptive coding adds overhead for codebook transmission, include this cost in the bitrate.

### Issue 4: Missing Limitation Disclosure (Priority P1)

The conclusion is purely promotional and does not disclose known limitations (small face handling, theoretical vs actual bpp discrepancy).

**Required Actions:**
- Add a limitation paragraph to the conclusion covering: (1) reduced quality on small objects at coarse granularity, (2) bpp approximation error (<0.05), (3) no OOD generalization evaluation.

## Actionable Suggestions
### Suggestion 1: Fix Novelty and Decoder Claims (Must)

**Problem:** The abstract says "the first capable of fine-grained bitrate adaptation across a broad spectrum" (Page 1) and C1 says "To our knowledge, this is the first that allows highly flexible and controllable bitrate adaptation" (Page 3). The decoder is called "probabilistic" but is deterministic (Page 5).

**Action:**
- Replace "first" language with a scoped claim: "To our knowledge, this is the first VQGAN-based generative compression framework to achieve continuous granularity-level bitrate control."
- Rename Section 3.2 from "Probabilistic Conditional Decoder" to "Conditional Feature Refinement Decoder."
- Replace Eq. (3)'s `∼ p(...)` notation with deterministic functional notation: `y2 = f_D1(y1, (ˆz)↓2⊙m2)`, `y3 = f_D2(y2, ˆz⊙m1)`.

### Suggestion 2: Add Statistical Variance and Hyperparameters (Must)

**Problem:** No standard deviations reported for any metric (Page 6-10). Key hyperparameters λ and MSE/LPIPS weighting unreported (Page 6).

**Action:**
- Retrain with 3 random seeds; report mean±std for all main metrics on Kodak at 3 bitrate points.
- Add a table specifying: λ = ?, α (MSE weight) = ?, β (LPIPS weight) = ? in a new "Implementation Details" subsection.
- Add a sensitivity analysis for training ratio (r1=40-60%, r2=30-50%, r3=5-15%).

### Suggestion 3: Improve Entropy Coding Ablation (Nice-to-Have)

**Problem:** Table 1 (Page 10) compares against uniform-frequency Huffman only.

**Action:**
- Add per-image adaptive Huffman coding baseline.
- Report average per-image code distribution KL divergence from global training distribution.
- If KL is large, discuss the efficiency gap and consider a lightweight adaptation mechanism.

### Suggestion 4: Restructure Related Work (Nice-to-Have)

**Problem:** Related Work (Page 3) is a chronological paper list without thematic organization.

**Action:**
- Reorganize into two comparison-driven paragraphs:
  1. "Generative Compression Paradigms": group GAN-based, diffusion-based, VQGAN-based methods.
  2. "Rate-Adaptation Strategies": compare variable-rate vs. progressive with a clear table showing supported bitrate range, granularity, and perceptual quality.

### Suggestion 5: Add Encoder Architecture Details (Nice-to-Have)

**Problem:** Section 3.1 (Page 4) does not specify how z1/z2/z3 are produced.

**Action:**
- Add 2-3 sentences describing the encoder as a shared backbone with multi-scale feature extraction (e.g., "The encoder E is a convolutional network with stride-2 downsampling. Features at strides 4, 8, and 16 are extracted as z1, z2, z3, respectively.").
- Clarify patch size for entropy computation (e.g., "patches of size 4×4 aligned with fine granularity").

### Suggestion 6: Add Limitation Paragraph to Conclusion (Nice-to-Have)

**Problem:** Conclusion (Page 10) has no limitations.

**Action:**
- Add: "Limitations: (i) reconstruction quality degrades for small objects when using coarse-only granularity (Appendix A.4); (ii) the theoretical bpp query table has up to 0.05 bpp approximation error; (iii) all evaluations are on in-domain benchmarks — OOD generalization has not been tested."

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction (Page 1-2) follows this structure:
- P1: Historical evolution (Shannon → Traditional codecs → Learned → Generative compression), ending with the gap (separate models per bitrate).
- P2: Critique of variable-rate CNN-based methods (limited range + MSE issues), ending with note that generative variable-rate methods are still constrained.
- P3: Solution paragraph describing Control-GIC components at high level.

**Assessment:** The current storyline is functional but front-loads too much historical context before identifying the core research gap. The gap (multi-model deployment cost) appears ~15 lines into the introduction. The contribution bullet list (Page 3) does not effectively differentiate from prior generative methods.

### Recommended Storyline (Best Candidate)

**Abstract Outline:**
- S1 (Problem): Generative image compression achieves high perceptual quality but requires separate models per bitrate, limiting deployment flexibility.
- S2 (Gap): Existing variable-rate methods support only a limited bitrate range or sacrifice perceptual quality.
- S3 (Solution): Control-GIC uses VQGAN with entropy-guided multi-granularity encoding to enable continuous bitrate control in a single model.
- S4 (Key Result): On Kodak/DIV2K/CLIC2020, Control-GIC achieves competitive LPIPS/DISTS/NIQE with state-of-the-art generative methods while offering flexible bitrate adaptation and faster inference.
- S5 (Implication): This work demonstrates that VQGAN-based variable-rate compression can match per-model generative quality, opening new possibilities for deployment-efficient compression.

**Introduction Outline (Paragraph-by-Paragraph):**
- P1 (Stakes + Gap): "Deploying learned image compression across diverse bandwidths and devices requires supporting multiple bitrates. While generative methods achieve high perceptual quality, they require training n separate models for n bitrates — incurring substantial storage and deployment cost. Variable-rate methods reduce model count but support a limited bitrate range or compromise perceptual quality." [Role: Establish practical problem + gap]

- P2 (Prior attempts + residual gap): "CNN-based variable-rate and progressive methods [citations] adjust quantization or importance maps to achieve multiple bitrates in one model, but operate within a narrow range and are typically optimized with MSE, yielding blurry reconstructions at low bitrates. Recent generative variable-rate methods [Iwai et al., Guo et al.] improve perceptual quality but still discretize the bitrate into preset levels, limiting fine-grained control." [Role: Show that existing solutions are insufficient]

- P3 (Proposed approach): "We propose Control-GIC, which rethinks rate control through the lens of VQ-based discrete representation. By correlating local patch information density with granularity (fine/medium/coarse VQ codes), Control-GIC enables continuous bitrate adjustment by simply varying the proportion of patches assigned to each granularity level — all within a single model. A conditional feature refinement decoder preserves reconstruction quality across bitrates." [Role: Present solution intuition]

- P4 (Evidence preview + contributions): "Experiments on three benchmarks demonstrate competitive perceptual quality against state-of-the-art methods trained per-bitrate, while offering fine-grained control from 0.07 to 0.6 bpp with faster encoding/decoding. Our contributions are: (1) A continuous granularity-level rate control mechanism for VQGAN, (2) An entropy-guided granularity assignment strategy, and (3) A conditional decoder that progressively refines multi-granularity features." [Role: Provide evidence and explicit, bounded contributions]

### Alternative Storyline (Short-Form)

For a shorter, more direct introduction: Open with a concrete scenario ("Deploying image compression on a streaming platform requires serving images at dozens of quality levels"), then immediately state the problem (n models for n bitrates), then propose the granularity-based solution. This would be more engaging for a broader ML audience.

## Priority Revision Plan
```text
Rank | Issue                        | Effort | Impact | Priority
-----|------------------------------|--------|--------|--------
P0   | Fix "first" claim + decoder  | Low    | High   | Must do before resubmission
     | labeling                     |        |        |
P0   | Add variance + hyperparams  | Medium | High   | Must do before resubmission
P1   | Add limitation disclosure   | Low    | Medium | Nice-to-have
P1   | Improve entropy coding      | Low    | Medium | Nice-to-have
     | baseline                    |        |        |
P2   | Restructure Related Work    | Low    | Low    | Quality improvement
P2   | Add encoder architecture    | Low    | Low    | Quality improvement
     | details                     |        |        |
```

### Priority 0 (Must Fix Before Resubmission)

**P0.1 — Fix "first" and "probabilistic" overclaims.** Estimated effort: 1 hour.
- Replace "first" with scoped language throughout (Abstract, Introduction, Contribution C1).
- Rename "probabilistic conditional decoder" to "conditional feature refinement decoder."
- Replace probabilistic notation in Eq. (3) with deterministic functional form.
- **Expected impact:** Eliminates two easily-targeted reviewer criticisms and improves scientific accuracy.

**P0.2 — Add statistical variance and hyperparameter reporting.** Estimated effort: 2-3 GPU-days for 3 seeds.
- Retrain with 3 seeds on the same OpenImages subset.
- Report mean±std for LPIPS, PSNR, DISTS, FID, NIQE on Kodak at 3 bitrate points (~0.15, 0.3, 0.5 bpp).
- Report λ value, MSE/LPIPS weighting, training ratio selection process.
- **Expected impact:** Makes results statistically meaningful. Without this, reviewers cannot determine if improvements are significant.

### Priority 1 (Should Fix for Stronger Paper)

**P1.1 — Add limitation paragraph to conclusion.** Estimated effort: 30 minutes.
- Add 3-4 sentences covering known limitations from Appendix A.4 and bpp approximation error.
- **Expected impact:** Improves scientific integrity and preempts reviewer concerns about overclaiming.

**P1.2 — Improve entropy coding baseline.** Estimated effort: 1 day.
- Implement per-image adaptive Huffman coding as baseline.
- Report KL divergence between per-image and global code distribution.
- **Expected impact:** More honest evaluation of the entropy coding contribution.

### Priority 2 (Quality Improvements)

**P2.1 — Restructure Related Work.** Estimated effort: 2 hours.
- Rewrite as thematic comparison paragraphs.
- Add a small positioning table.
- **Expected impact:** Easier novelty assessment for readers.

**P2.2 — Add encoder architecture details.** Estimated effort: 1 hour.
- Clarify multi-scale feature extraction process.
- Specify patch size for entropy computation.
- **Expected impact:** Improved reproducibility.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | R-D performance on Kodak | 24 images, 4 metrics, 7 methods | LPIPS, DISTS, PSNR, NIQE | Competitive with MS-ILLM/MRIC; surpasses SCR/CTC | C1 (single-model quality) | No variance; single seed |
| E2 | R-D performance on DIV2K | 100 images, 6 metrics | +FID, KID | Consistent competitiveness | C1 | No variance; single seed |
| E3 | R-D performance on CLIC2020 (Appendix A.5) | 428 images, 6 metrics | All 6 metrics | Superior to BPG/VVC/SCR/CTC; competitive with generative methods | C1 | Appendix only |
| E4 | Model efficiency (Figure 5) | Kodak, encoding/decoding time, BD-rate, training steps | Time (s), BD-rate (%), steps (M) | Fastest encoding/decoding; competitive BD-rate | C1 (efficiency) | No absolute time values; training step comparison incomplete |
| E5 | Qualitative comparison (Figure 6) | Kodak images | Visual inspection | Control-GIC preserves texture integrity | C1 | Single image per method |
| E6 | Fine-grained control demo (Figure 7) | Single image, varying r2 | bpp, LPIPS | Continuous control at 0.001 bpp granularity | C1 (flexibility) | Single image only |
| E7 | Decoder ablation (Figure 8) | DIV2K, w/o med/fin, w/ med, w/ fin, full | LPIPS, DISTS | Both conditions improve; fin more beneficial | C3 | No statistical testing |
| E8 | Entropy coding comparison (Table 1) | Kodak, 3 granularity ratios | bpp, bit saving (%) | Up to 5% saving vs uniform Huffman | C2 | Weak baseline comparison |
| E9 | Extreme low bitrate (Appendix A.6) | Kodak, CLIC2020, <0.05 bpp | LPIPS | Better LPIPS than Mao et al. at lower bpp | C1 | Only one baseline |
| E10 | Small face analysis (Appendix A.4) | Small face images | Visual + LPIPS | Fine granularity helps; coarse fails | C1 (limitation) | Qualitative only |

### Research-Theme Gap Diagnosis

1. **Statistical Reliability Gap:** No experiment reports variance across seeds or initialization. This is the most critical gap — without it, the reported improvements may not be statistically significant.

2. **Fairness Gap:** Comparisons are made against methods trained on different data (e.g., HiFiC uses different training data, CDC uses diffusion backbone). No discussion of how training budget, data, and protocol differences affect comparability.

3. **Generalization Gap:** All evaluations are on standard in-domain benchmarks (Kodak, DIV2K, CLIC2020). No out-of-distribution or robustness testing (noisy images, compression artifacts as input, domain shift).

4. **Ablation Depth Gap:** The decoder ablation tests granularity conditions but does not ablate: (a) the entropy-guided masking strategy vs. random masking, (b) the number of granularity levels (why 3?), (c) codebook size sensitivity.

### Proposed Research Experiments (P0/P1/P2)

**P0-Exp1: Multi-Seed Variance Analysis**
- **Target Claim:** C1 (single-model quality comparable to per-model methods)
- **Hypothesis:** Control-GIC's performance is stable across different initialization seeds
- **Design:** Train with 3 different random seeds; report mean ± std for all metrics on Kodak at 3 bitrate points
- **Controls:** Fixed training data split, fixed granularity ratios
- **Metrics:** LPIPS, PSNR, DISTS, FID
- **Success Criterion:** Standard deviation < 5% of mean for all metrics
- **Cost:** ~3 GPU-days on RTX 3090
- **Expected Gain:** Provides statistical grounding for all empirical claims in the paper

**P0-Exp2: Hyperparameter Sensitivity**
- **Target Claim:** C1, C2 (robustness of method)
- **Hypothesis:** Performance is robust to moderate changes in training granularity ratio and λ
- **Design:** Sweep λ ∈ {0.01, 0.05, 0.1, 0.2}; sweep training ratio (r1,r2,r3) across 3 configurations; report R-D curves for each setting on Kodak
- **Metrics:** LPIPS, PSNR
- **Success Criterion:** At most 0.01 LPIPS variation across λ settings with proper GAN tuning
- **Cost:** ~6 GPU-days
- **Expected Gain:** Demonstrates practical usability and informs λ/ratio selection

**P1-Exp3: Ablation of Entropy-Guided Masking vs. Random Masking**
- **Target Claim:** C2 (entropy guidance is beneficial)
- **Hypothesis:** Entropy-based granularity assignment outperforms random assignment at the same bitrate
- **Design:** Replace entropy-sorted assignment with random assignment at matched bitrates; compare LPIPS on Kodak at 3 bitrates
- **Controls:** Same model weights, same (r1,r2,r3) ratios
- **Metrics:** LPIPS, DISTS
- **Success Criterion:** Entropy-guided assignment should be consistently better
- **Cost:** 1 GPU-day
- **Expected Gain:** Directly validates the core design choice of entropy-guided granularity

**P2-Exp4: Out-of-Distribution Robustness**
- **Target Claim:** C1 (generality)
- **Hypothesis:** Control-GIC maintains reasonable quality on OOD images
- **Design:** Evaluate on artificially corrupted images (Gaussian noise, JPEG compression artifacts) and domain-shifted images (art, sketching)
- **Metrics:** LPIPS, NIQE
- **Success Criterion:** Relative LPIPS degradation from clean images < 20%
- **Cost:** 0.5 GPU-day
- **Expected Gain:** Supports generality claim and identifies failure modes

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### ASCII Diagram — Paper Structure & Evidence Map

```text
[CORE IDEA: VQGAN + Entropy-Guided Granularity = Single-Model Variable Bitrate]
                      |
        +-------------+-------------+
        |             |             |
   [Granularity-] [Statistical ] [Conditional Decoder]
   [Informed Enc] [Entropy Code] [Feature Refinement]
        |             |             |
   z1/z2/z3 at   Global Huffman  y2 = D1(y1)⊙(1-m2)
   strides 4/8/16  table from    + (ˆz)↓2⊙m2
   + masks m1,m2   training set         |
        |             |             |
        +------+------+------+------+
               |             |
         [R-D Curves]   [Efficiency]
         Kodak/DIV2K/   Enc/Dec time
         CLIC2020       BD-rate saving
         LPIPS/DISTS/   Training steps
         PSNR/FID/KID/
         NIQE
               |
        [GAPS IDENTIFIED]
    1. No variance/significance
    2. No OOD generalization
    3. Weak entropy baseline
    4. Overclaimed novelty
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem]                          [Fix]                         [Expected Outcome]
   |                                 |                                |
Overclaimed "first"         →  Scope novelty claim          →  Reviewer trust
+ "probabilistic" label        Rename decoder                  Scientific accuracy
   |                                 |                                |
No variance in results       →  3-seed retraining            →  Statistical validity
Unreported hyperparams          Report λ, α, β                  Reproducibility
   |                                 |                                |
Weak entropy baseline         →  Add adaptive Huffman         →  Honest evaluation
                                KL divergence analysis
   |                                 |                                |
Missing limitations           →  Add limitation paragraph     →  Completeness
   |                                 |                                |
Related Work as list          →  Thematic reorganization      →  Clearer positioning
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Image Compression (Root)
├── Branch 1: Neural Image Compression
│   ├── Leaf 1.1: CNN-based autoencoders + entropy models
│   │   └── Ballé et al. 2017, 2018; Minnen et al. 2018
│   ├── Leaf 1.2: GAN-based generative compression
│   │   └── Agustsson et al. 2019; Mentzer et al. (HiFiC) 2020
│   ├── Leaf 1.3: Diffusion-based compression
│   │   └── Yang & Mandt (CDC) 2024
│   └── Leaf 1.4: VQGAN-based compression
│       └── Esser et al. 2021; Mao et al. 2023; Xue et al. 2024
│           └── [This paper: Control-GIC — adds rate control to VQGAN]
│
├── Branch 2: Rate-Adaptation NIC
│   ├── Leaf 2.1: Variable-rate (parameter adjustment)
│   │   └── Choi et al. 2019; Yang et al. 2021; Cui et al. 2021
│   │   └── Lee et al. (SCR) 2022b
│   ├── Leaf 2.2: Progressive / scalable bitstream
│   │   └── Toderici et al. 2017; Johnston et al. 2018
│   │   └── Jeon et al. (CTC) 2023b; Zhang et al. 2024a
│   └── Leaf 2.3: Generative + rate-adaptive
│       └── Iwai et al. 2024 (scalable generative)
│       └── Guo et al. 2023 (variable-rate generative)
│           └── [Control-GIC differentiation: continuous granularity-level
│                control via VQ-indices, not preset quantization levels]
│
└── Branch 3: Traditional Codecs (baselines)
    ├── BPG (Bellard)
    └── VVC/VTM10.0 (Bross et al. 2021)
```

### Contribution-Level Novelty Conclusion

External literature verification was unavailable in this run (paper_search service not available). The following novelty conclusions are deferred for manual verification.

**C1 (Unified single-model variable bitrate):** Deferred. The paper cites Iwai et al. (2024) and Guo et al. (2023) as prior variable-rate generative works. Whether Control-GIC's continuous granularity control is sufficiently distinct requires manual literature comparison.

**C2 (Granularity-informed encoder + statistical entropy coding):** Deferred. VQ-index compression has been explored in Mao et al. (2023). The novelty of entropy-guided multi-granularity assignment needs verification against prior VQ-based variable-rate methods.

**C3 (Probabilistic conditional decoder):** Deferred. The "probabilistic" label is misleading (deterministic feature replacement). The actual contribution — conditional feature injection — may overlap with existing multi-scale skip-connection designs in image compression literature.

### Final Score

**Final Score: 6/10**

Rationale (research value + novelty as primary dimensions):
- Research value: The single-model variable-rate VQGAN approach addresses a genuine deployment need. The granularity-based control is well-motivated. Efficiency advantage is demonstrated.
- Novelty: Moderately incremental. The granularity-level control idea is novel within VQGAN-based compression, but the overall architecture (VQGAN + multi-scale encoder + GAN loss + Huffman coding) combines known components. The "probabilistic" labeling overstates novelty.
- Validity concerns: No statistical variance, unreported hyperparameters, and weak entropy baseline reduce confidence in the reported results.
- Reproducibility: Partially limited by missing implementation details (encoder architecture, λ, loss weighting).

**Post-Revision Target: [7, 8]/10**

If the authors: (1) fix overclaims and decoder naming, (2) add multi-seed variance and hyperparameter reporting, (3) add limitation disclosure, and (4) improve entropy coding baseline — the paper would become a solid contribution with well-validated results. The upper bound of 8 assumes these issues are fully addressed; 7 reflects residual concerns about incremental novelty vs. strongest baselines that require manual verification.