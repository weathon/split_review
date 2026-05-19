## Summary
# Final Review Report

## Summary

This paper proposes **LabelDP-Pro**, a family of label differentially private training algorithms that interleave gradient projection operations with DP-SGD. The core insight is that in the LabelDP setting (where input features are public), structural priors — specifically, the span or convex hull of per-example per-class gradients — can be computed using only the feature information and used to denoise the privatized gradients from DP-SGD. The authors propose three denoiser variants (SELF SPAN, SELF CONV, ALTCONV), with ALTCONV being the primary practical contribution due to its compatibility with privacy amplification by subsampling. A memory-efficient projection via forward/backward autodiff is provided, along with a coefficient smoothing regularization to stabilize training.

**Strengths:** The paper addresses a well-motivated problem (high-privacy LabelDP), provides a technically sound algorithmic improvement over both RR-based baselines and DP-SGD, and includes theoretical analysis (convex setting) to support the design choices. The empirical results are extensive across four benchmarks and also extend to a real-world advertising dataset with user-level privacy.

**Weaknesses:** Missing variance/confidence intervals in main results tables; theory-empirical alignment claim is not quantitatively supported (convex vs. non-convex gap); "first practical method" claim lacks verified novelty scope; SelfSL comparison with PATE-FM is confounded by different representation pipelines; user-level experiment uses re-sampling augmentation without validation; conclusion does not fully bound limitations. External literature verification was unavailable in this run, so novelty and SOTA comparison conclusions are deferred.

## Strengths
1. **Well-motivated problem formulation:** The paper correctly identifies that in the LabelDP setting, standard RR-based mechanisms suffer from exponential noise scaling at small ε (high privacy), while DP-SGD provides better noise scaling but overprotects by also covering features. This gap is clearly articulated and practically relevant for advertising and other applications where features are public.

2. **Technically elegant algorithmic contribution:** The projection-based denoising framework (SELF SPAN → SELF CONV → ALTCONV) is theoretically grounded and the design is incremental in a productive way — each variant addresses a practical limitation of the previous one (span → convex hull → amplification compatibility). The autodiff-based memory-efficient projection (Section 3.2) is a thoughtful engineering contribution that makes the method practical for deep networks.

3. **Strong empirical results in high-privacy regime:** The experimental results convincingly demonstrate that LabelDP-Pro outperforms prior LabelDP baselines (RR, RR-Debiased, LP-2ST, ALIBI) and DP-SGD when ε < 1.0 across four image benchmarks. The gains are substantial: e.g., MNIST at ε=0.2 achieves 92.9% with LabelDP-Pro vs 10.9% with the best baseline. The CIFAR-10 results at ε=0.05 show LabelDP-Pro achieving 16.0% (above random guessing) while all baselines remain at 10.0%.

4. **User-level privacy extension:** The extension to user-level privacy on a real-world advertising dataset (Criteo) goes beyond typical image classification evaluations and demonstrates practical relevance. The consistent improvement over RR (e.g., AUC 0.780 vs 0.562 at ε=0.1, k=2) is significant.

5. **Theoretical motivation:** The convex optimization analysis in Section 4 provides formal excess risk bounds that justify the denoiser design choices (removing dimension dependence via projection, convex hull improvement over span, ALTCONV's advantage via amplification). While the convexity gap is a limitation, the theory serves as a useful design justification.

6. **Clear writing and good structure:** The paper is well-organized, with clear Algorithm 1 pseudocode, helpful denoiser summary table (Table 1), and thorough ablation of regularization (Table 2) and denoiser variants (Table 3). The appendices provide implementation details and additional results.

## Weaknesses
### W1. Missing Variance Estimates in Main Results (Severity: Major)
The main experimental results (Tables 5, 6, 7) report accuracy/AUC without standard deviations, confidence intervals, or significance tests. The experimental setup mentions launching "three independent runs" for hyperparameter search but does not report multi-seed variance for the final selected configurations. Given that many comparisons involve small margins (e.g., CIFAR-10 at ε=0.2: LabelDP-Pro 30.8% vs LP-2ST 17.9% — large gap, but still needs variance; CIFAR-10 SelfSL at ε=0.29: 87.2% vs RRWithPrior 76.8%), the absence of variance estimates undermines statistical reliability.

### W2. Theory-Empirical Alignment Claim Not Quantitatively Verified (Severity: Major)
Page 7 (lines 44-47) states that the convex-theory bounds "align well with the experimental findings" without providing a quantitative comparison. The theoretical bounds (Table 4) are derived for convex loss functions with O(1/√T) rates, while experiments use non-convex deep networks with finite training steps. The claim of alignment is purely qualitative and does not specify which bound maps to which experimental result or by what metric alignment is judged.

### W3. "First Practical Method" Claim Lacks Verified Scope (Severity: Major)
The contributions bullet (Page 2, lines 26-29) claims LabelDP-Pro is "the first practical method that fully utilizes the flexibility of the LabelDP definition, the central DP setting, and the approximate-DP guarantee." This claim is difficult to verify without external literature retrieval. Notably, ALIBI (cited as a baseline) also operates under central DP with approximate-DP guarantees, though using a different mechanism (Laplace noise + Bayesian inference). The claim needs tighter qualifiers and explicit differentiation from prior work.

### W4. SelfSL vs PATE-FM Comparison Confounded (Severity: Major)
The comparison in Section 5.3 mixes two variables: (a) the privacy mechanism and (b) the representation learning pipeline (SelfSL with 90.9% non-private accuracy vs SemiSL with 95.5% non-private accuracy). While LabelDP-Pro shows better results at ε=0.18 and 0.29 despite the weaker feature extractor, this does not establish LabelDP-Pro as superior to PATE-FM under matched conditions. A controlled comparison using the same representations is needed.

### W5. User-Level Data Augmentation by Re-Sampling May Introduce Bias (Severity: Major)
The Criteo experiment (Section 6) augments users with fewer than k examples via "random re-sampling," creating duplicate examples. This violates i.i.d. assumptions and may differentially affect compared methods (RR vs DP-SGD vs LabelDP-Pro). The fraction of users requiring augmentation is not reported.

### W6. Convexity Gap in Theory (Severity: Minor)
The theoretical analysis (Section 4) is restricted to convex loss functions, while all experiments use non-convex deep neural networks. This is acknowledged (Page 7, line 44) but the implications for the claimed "alignment" are not discussed. The theoretical bounds are also not predictive of finite-sample behavior.

### W7. Computation Overhead Underestimated (Severity: Minor)
The conclusion mentions "approximately 200 iterations to reach convergence" as a bottleneck, but the runtime overhead (Table 11: 1.11x–3.84x over DP-SGD) is reported at the epoch level without accounting for the total training cost. For CIFAR-10, LabelDP-Pro takes 493s/epoch vs DP-SGD's 128s/epoch (3.84x), and the method requires 50-100 epochs, leading to potentially 7-14 hours of additional computation.

### W8. Conclusion Not Fully Bounded (Severity: Minor)
The conclusion (Section 7) mentions only computation and regression extension as future directions. Other limitations (variance reporting, convexity gap, limited domain scope, SelfSL confound) are not acknowledged.

## Key Issues
### Issue 1: Missing Statistical Reliability in Main Results (W1)
**Root cause:** Tables 5-7 report single-value accuracy/AUC without standard deviation, confidence intervals, or multi-seed summary statistics. While Appendix D.2 mentions hyperparameter search involves "three independent runs with different random seeds," the final selected configurations are reported without variance.

**Impact:** Without variance, readers cannot assess whether observed gains (especially moderate ones like +0.3% at ε=0.29 in Table 6) are statistically significant or within noise range. This reduces confidence in the claim that LabelDP-Pro "consistently" outperforms baselines.

**Required action (Must):** Report mean ± std over ≥3 seeds for all main result tables. Add a brief statistical significance discussion for key comparisons.

### Issue 2: Non-Quantified Theory-Empirical Alignment (W2)
**Root cause:** Page 7 claims that theoretical bounds "align well" with experiments, but no quantitative mapping is provided. The theory is for convex losses (O(1/√T) bounds), while experiments use non-convex deep networks.

**Impact:** Readers cannot verify the alignment claim. The theory serves as motivation but not as a predictive or explanatory model for the empirical results.

**Required action (Must):** Either (a) provide a quantitative comparison by evaluating a convex analog (e.g., logistic regression) and comparing bound ratios to accuracy ratios, or (b) retract the alignment claim and reframe the theory as design intuition only.

### Issue 3: Novelty Claim Overreach (W3)
**Root cause:** The "first practical method" claim (Page 2) is stated without explicit comparison to ALIBI and other prior central-DP LabelDP methods.

**Impact:** If prior methods also operate under central DP with approximate-DP guarantees, the claim may be rejected, weakening the paper's positioning.

**Required action (Must):** Add tighter scope qualifiers: "To our knowledge, the first approach that jointly exploits central DP privacy accounting and gradient projection with public features for LabelDP."

### Issue 4: Confounded SelfSL/PATE-FM Comparison (W4)
**Root cause:** Two variables differ simultaneously between LabelDP-Pro (SelfSL, 90.9% non-private) and PATE-FM (SemiSL, 95.5% non-private).

**Impact:** The claim that LabelDP-Pro "outperforms" PATE-FM is not fully supported; a matched-representation comparison is missing.

**Required action (Must):** Add a controlled experiment using identical pre-trained representations for both methods, or explicitly acknowledge this limitation.

## Actionable Suggestions
### S1. Add Variance Reporting to All Main Tables (Must, addresses W1)
For Tables 5, 6, and 7, report accuracy as `mean ± std` over at least 3 independent seeds with different random initializations. For the hyperparameter search (Appendix D.2), keep the best configuration as reported, but add a note confirming that the same configuration was used for all seeds. For borderline comparisons (e.g., Table 6 at ε=0.29: 87.2% vs 86.9%, gap 0.3%), add a paired significance test or bootstrap confidence interval.

**Location:** Tables 5, 6, 7 (Main paper) and Tables 14, 15 (Appendix).

### S2. Provide Quantitative Theory-Empirical Comparison (Nice-to-have, addresses W2)
Add a small-scale convex experiment (e.g., multinomial logistic regression on a subset of MNIST features) where the theoretical bounds from Table 4 can be quantitatively evaluated. Plot the excess risk of each denoiser alongside the theoretical bound rates. This would make the "alignment" claim concrete. Alternatively, if this is impractical, replace the alignment statement with: "The qualitative trends — ALTCONV > SELF SPAN > NOOP at small ε — are consistent with the theoretical analysis, though a direct quantitative comparison would require extensions to non-convex settings."

**Location:** Section 4, last paragraph (Page 7).

### S3. Tighten Novelty Claims with Explicit Scope (Must, addresses W3)
Replace "first practical method" with a bounded claim that specifies the exact combination of techniques that is novel: "To our knowledge, this is the first approach that combines (i) central DP privacy accounting via Poisson subsampling with (ii) gradient projection onto convex hulls of per-class gradients computed from public features for LabelDP." Also explicitly acknowledge ALIBI and other central-DP LabelDP methods, explaining how the projection approach differs.

**Location:** Page 2, contribution bullet 3; also Page 15 (Related Work appendix).

### S4. Add Matched-Representation Experiment for SelfSL Comparison (Must, addresses W4)
Run PATE-FM or the strongest baseline using the same SimCLR representations (90.9% non-private accuracy) as used for LabelDP-Pro. If PATE-FM is not compatible with SelfSL features, state this limitation explicitly: "PATE-FM requires a semi-supervised pipeline with confidence thresholding, which is not directly applicable to SelfSL features. A matched comparison under identical representations is therefore not feasible with existing methods, and the observed advantage at ε=0.18-0.29 should be interpreted with this caveat."

**Location:** Section 5.3 (Page 8).

### S5. Validate User-Level Re-Sampling Ablation (Must, addresses W5)
Add a footnote or appendix ablation confirming that the Criteo conclusions hold without re-sampling. Select a subset of users who naturally contribute ≥k examples and compare LabelDP-Pro vs RR vs DP-SGD on this subset for at least one condition (e.g., k=2, ε=0.5). Report the fraction of users needing augmentation in the training set.

**Location:** Section 6 (Page 9), or Appendix D.4.

### S6. Expand Conclusion Limitations (Nice-to-have, addresses W8)
Add a dedicated limitations paragraph after the current conclusion (Page 9-10) covering: (a) convexity gap in theory, (b) variance reporting needed for statistical rigor, (c) limited domain scope (image + ad attribution only), (d) computational overhead (3.84x for CIFAR-10). Keep the tone constructive and forward-looking.

**Mentor Revised Version (new paragraph):**
"In addition to computational efficiency, we acknowledge several limitations. First, our theoretical analysis is restricted to convex loss functions; extending it to non-convex settings would strengthen the connection to deep learning practice. Second, our main results report accuracy without variance estimates; adding confidence intervals over multiple seeds would improve statistical rigor. Third, our evaluation focuses on image classification and advertising attribution; the method's effectiveness on other modalities (text, speech) remains to be verified. Addressing these limitations is a natural direction for future work."

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction (Page 1-2) uses a 3-paragraph structure: (P1) DP background + online advertising motivation + LabelDP definition + prior work listing; (P2) High-privacy regime challenge with RR-based methods; (P3) DP-SGD as alternative + LabelDP-Pro solution + contribution bullet list. The main issues are: (1) P1 combines too many functions (problem, example, definition, literature review) into one paragraph; (2) The transition from "RR fails at small ε" to "DP-SGD scales better" to "our method" is compressed into a single paragraph (P3); (3) The specific technical gap — no prior method combines central DP accounting with public-feature gradient denoising — is not stated explicitly before the contribution list.

### Abstract Outline (Complete)

**S1 (Problem):** "Label differentially private (label DP) algorithms protect label privacy when input features are known to the adversary."

**S2 (Gap):** "Existing label DP methods based on randomized response suffer from exponentially degraded signal-to-noise ratios in the high-privacy (small ε) regime, often yielding over 84% incorrect labels."

**S3 (Method):** "We propose LabelDP-Pro, a family of algorithms that interleaves gradient projection operations with DP-SGD, using public features to project privatized gradients onto the span or convex hull of per-class gradients — a denoising operation that reduces noise without accessing labels."

**S4 (Key Result):** "On four benchmark datasets, LabelDP-Pro improves accuracy over prior label DP baselines by up to 57 percentage points at ε=0.01 and consistently outperforms DP-SGD in the high-privacy regime (ε<1)."

**S5 (Theory + Limitation):** "Theoretical analysis via convex optimization bounds explains the bias-variance trade-off. The main limitation is a 1.1x–3.8x computation overhead from iterative projection optimization."

### Introduction Outline (Complete)

**P1 — Problem and Setting:** 
"Define differential privacy. State that standard DP protects both features and labels. Introduce LabelDP for settings where only labels are sensitive (e.g., online advertising)."
*Key claim:* Full-DP overprotects when features are public.

**P2 — Prior Work Gap:**
"Describe RR-based LabelDP mechanisms. Show their failure at small ε: probability of correct label = e^ε/(e^ε+K-1). For K=10, ε=0.5, >84% labels flipped. Explain the local-DP vs central-DP distinction."
*Key claim:* RR-based methods have exponential noise scaling because they operate under local DP.

**P3 — DP-SGD Alternative and Its Limitation:**
"DP-SGD provides better (linear) noise scaling but protects both features and labels, which is overly stringent for LabelDP. This overprotection wastes utility."
*Key claim:* DP-SGD is a better building block but still suboptimal for LabelDP.

**P4 — Proposed Solution:**
"Key insight: public features in LabelDP can be used to compute structural priors (span/convex hull of per-class gradients). Projecting noisy gradients onto these structures denoises them without accessing labels. Introduce LabelDP-Pro framework and the three denoiser variants (SELF SPAN, SELF CONV, ALTCONV)."
*Key claim:* Projection-based denoising combines DP-SGD's noise scaling with label-free feature information.

**P5 — Contribution List:**
"Explicit numbered contributions: (1) projection-based denoising framework, (2) memory-efficient autodiff projection, (3) first combination of central DP + public-feature projection for LabelDP, (4) empirical gains across four benchmarks, (5) user-level privacy extension, (6) theoretical analysis."

### Alternative Storyline Options

**Option A (Problem-First, current structure but refined):**
Follow the 5-paragraph structure above. Emphasize the noise-scaling contrast (RR: exponential vs DP-SGD: linear) with a concrete figure in the introduction (Figure 1 already partially serves this).

**Option B (Algorithm-First):**
Start with the LabelDP-Pro algorithm (Algorithm 1), then explain why it works: because the gradient of cross-entropy loss decomposes as a convex combination of per-class gradients. This would appeal to method-oriented readers but may lose readers unfamiliar with DP.

**Option C (Application-First):**
Lead with the advertising application (Criteo) and user-level privacy scenario, then generalize to the LabelDP framework. This would ground the motivation more concretely but may narrow the perceived applicability.

**Recommendation:** Option A is the strongest because it builds the motivation incrementally and makes the noise-scaling argument the central narrative thread, which directly supports the algorithmic choices.

## Priority Revision Plan
### P0 (Critical — Must Fix Before Resubmission)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P0.1 | Missing variance/std in main tables | Add mean±std over ≥3 seeds for Tables 5, 6, 7 | Section 5, Tables 5-7 | Scientific credibility, statistical rigor |
| P0.2 | Novelty claim overreach ("first practical method") | Tighten scope to specific technique combination | Page 2, bullet 3; Page 15 (Related Work) | Defensibility against novelty rejection |
| P0.3 | Confounded SelfSL/PATE-FM comparison | Add matched-representation experiment or explicit caveat | Section 5.3, Page 8 | Fairness of comparison claims |

### P1 (High Priority — Strongly Recommended)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P1.1 | Theory-empirical alignment claim unsupported | Replace with qualitative-only claim or add convex experiment | Section 4, last paragraph (Page 7) | Scientific honesty, prevents overclaim critique |
| P1.2 | User-level re-sampling bias | Add ablation without augmentation for one condition | Section 6 or Appendix D.4 | Validity of user-level conclusions |
| P1.3 | Conclusion limitations incomplete | Add explicit limitations paragraph | Section 7, new paragraph after Page 9 | Balanced paper positioning |

### P2 (Nice-to-Have — Quality Improvement)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P2.1 | Introduction storyline density | Restructure into 5 paragraphs (Problem → Prior work gap → DP-SGD alternative → Proposed solution → Contributions) | Section 1, Pages 1-2 | Readability, narrative clarity |
| P2.2 | λ sensitivity analysis | Add λ sensitivity experiment across ε values and datasets | Section 3.3, Page 5 | Practical usability |
| P2.3 | Computation overhead discussion | Add total training cost (hours) comparison in addition to per-epoch | Section 7 or Appendix D.4 | Practical deployment assessment |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Compare LabelDP-Pro vs RR/RR-Debiased/LP-2ST/ALIBI on item-level LabelDP (MNIST) | MNIST-10, ε∈[0.01, 2.0], batch 1024, SGD | Test accuracy | LabelDP-Pro outperforms all baselines at ε<1.0 (e.g., 92.9% vs 10.9% at ε=0.2) | C1 (projection denoising improves utility) | No variance/std reported |
| E2 | Same as E1 on CIFAR-10 | CIFAR-10, ε∈[0.05, 10.0] | Test accuracy | LabelDP-Pro outperforms baselines at ε<1.0 (e.g., 30.8% vs 17.9% at ε=0.2) | C1, C3 | Gains at ε≥1.0 are reversed (RR better) |
| E3 | Ablate denoiser variants (NOOP, SELF SPAN, SELF CONV, ALTCONV) | MNIST, ε∈[0.1, 2.0] | Test accuracy | ALTCONV ≈ SELF CONV > SELF SPAN > NOOP at small ε | C1, theoretical bounds (Table 4) | ALTCONV and SELF CONV not separated at small ε |
| E4 | Evaluate coefficient smoothing (λ) | MNIST, ε∈[0.1, 2.0] | Test accuracy | λ=0.75 gives +4-6% over vanilla (λ=1) | C1 (stability) | No λ sensitivity across datasets |
| E5 | Evaluate LabelDP-Pro with SelfSL | CIFAR-10, Wide-ResNet18, SimCLR | Test accuracy | LabelDP-Pro outperforms RR, RRWithPrior, and PATE-FM at ε≤0.5 | C1 (generic LabelDP method) | Confounded by different representation pipelines |
| E6 | User-level LabelDP on Criteo | Criteo Attribution, k∈{2,5,10}, ε∈[0.1,5.0] | AUC | LabelDP-Pro > RR at ε<5; advantage grows with k | C1 (user-level applicability) | Re-sampling augmentation may introduce bias |
| E7 | Additional item-level datasets | FashionMNIST, kMNIST | Test accuracy | Consistent improvement at small ε | C1 | Same variance limitation as E1 |
| E8 | Runtime comparison | All tasks, batch 1024 | Epoch time (s) | LabelDP-Pro: 1.11x–3.84x over DP-SGD | C2 (efficient autodiff) | Total training cost not reported |

### Research-Theme Gap Diagnosis

The paper's main research-value claims are: (1) new knowledge about projection-based denoising for LabelDP, (2) practical feasibility of the method, (3) applicability to both item-level and user-level privacy. The main gaps in evidence are:

- **Statistical rigor:** No variance reporting reduces reproducibility confidence (affecting claim 2).
- **Theory-empirical alignment:** Not quantitatively verified (affecting claim 1).
- **Controlled comparison:** SelfSL vs PATE-FM confounded (affecting claim 2-3).
- **Domain diversity:** Only image classification + ad attribution tested; text/speech not covered (affecting claim 3).

### Proposed Research Experiments

**P0 Experiment: Multi-Seed Variance Reporting**
- *Target Claim:* C1 (improvement over baselines is statistically significant)
- *Hypothesis:* Gains >2% exceed 95% CI across 3 seeds
- *Minimal Design:* Re-run Tables 5-7 with 5 seeds each, report mean±std
- *Controls:* Same hyperparameter configuration across seeds
- *Metrics:* Accuracy/AUC mean, std, and Cohen's d effect size
- *Success Criterion:* All reported gains >1% have std < gain/2
- *Estimated Cost:* 5x current compute (~2-4 GPU-days)
- *Expected Gain:* Scientific credibility, statistical rigor

**P1 Experiment: Controlled SelfSL Comparison**
- *Target Claim:* C3 (LabelDP-Pro achieves superior utility)
- *Hypothesis:* Under identical representations, LabelDP-Pro still matches or exceeds PATE-FM
- *Minimal Design:* Use SimCLR features for both LabelDP-Pro and a PATE-FM variant adapted to SelfSL (or use stronger SemiSL features for LabelDP-Pro)
- *Controls:* Same pre-trained feature extractor for both methods
- *Metrics:* Test accuracy at ε=0.1, 0.2, 0.5
- *Success Criterion:* LabelDP-Pro achieves ≥95% of PATE-FM accuracy under matched features
- *Estimated Cost:* ~10 GPU-hours (re-train classifier only)
- *Expected Gain:* Removes confound, strengthens comparison validity

**P1 Experiment: User-Level Re-Sampling Ablation**
- *Target Claim:* C1 (LabelDP-Pro improves user-level LabelDP)
- *Hypothesis:* Conclusions hold without re-sampling augmentation
- *Minimal Design:* Subset of users with ≥k natural examples; compare LabelDP-Pro vs RR for k=2, ε=0.5
- *Controls:* Same subset for both methods
- *Metrics:* AUC
- *Success Criterion:* Relative ordering unchanged (LabelDP-Pro still > RR)
- *Estimated Cost:* Already have data; ~1 GPU-hour
- *Expected Gain:* Validity of user-level results

**P2 Experiment: Convex Benchmark for Theory Verification**
- *Target Claim:* Theoretical bounds (Table 4) predict experimental trends
- *Hypothesis:* O(1/√T + αR) bound rates match empirical excess risk on convex problem
- *Minimal Design:* Multinomial logistic regression on MNIST features; compare NOOP, SELF SPAN, ALTCONV excess risk vs theoretical bounds
- *Controls:* Same C, n₁, n₂ as in deep network experiments
- *Metrics:* Excess risk (L(¯w_T) - L(w*)) at different T
- *Success Criterion:* Bound shape (rate in T) matches empirical observation
- *Estimated Cost:* ~2 GPU-hours
- *Expected Gain:* Quantitative support for theory-empirical alignment

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5 / 10

**Rationale:** The paper presents a technically sound and practically motivated contribution to LabelDP with convincing empirical results in the high-privacy regime. The projection-based denoising framework is well-designed, and the engineering contributions (memory-efficient autodiff projection, coefficient smoothing) add practical value. However, the score is constrained by: (1) missing variance reporting in main results, which limits statistical confidence in the reported gains; (2) a theory-empirical alignment claim that is not quantitatively supported; (3) novelty claims ("first practical method") that are difficult to verify without external literature comparison (deferred verification); (4) a confounded comparison in the SelfSL section; and (5) potential bias from re-sampling in the user-level experiment. These issues are fixable with moderate additional work, and the core technical contribution remains valuable.

**Post-Revision Target:** [7.0, 8.0] / 10

**Rationale:** If all P0 and P1 issues are addressed (variance reporting, novelty claim tightening, controlled SelfSL comparison, user-level ablation, theory-empirical alignment clarification, conclusion limitations), the paper would achieve a score in the 7-8 range. The main factors preventing a higher score are the inherent convexity gap in theory (which cannot be fully closed without extending analysis) and the computational overhead (which is a genuine limitation of the projection approach). The core algorithmic contribution and strong empirical results in the high-privacy regime are solid and likely sufficient for acceptance at a top venue with the recommended revisions.