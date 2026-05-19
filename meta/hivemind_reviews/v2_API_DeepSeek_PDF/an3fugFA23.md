## Summary
# Final Review Report

## Summary

This paper presents Glimpse, a method for estimating full token-level probability distributions from the partial (top-K) probabilities returned by proprietary LLM APIs. The key insight is that many white-box detection methods (Entropy, Rank, Log-Rank, Fast-DetectGPT) only require the probability values—not the token identities—and can therefore operate on estimated distributions. The authors propose three estimation algorithms: Geometric distribution, Zipfian distribution, and an MLP-based model. Experiments across five state-of-the-art LLMs (ChatGPT, GPT-4, Claude-3 Sonnet/Opus, Gemini-1.5 Pro), four datasets covering seven languages, and multiple scoring models show that Glimpse-equipped detectors achieve strong detection accuracy, with Fast-Detect(GPT-3.5) reaching an average AUROC of ~0.954. The paper is well-structured, technically sound, and addresses a practical bottleneck in LLM-generated text detection. The main limitations are: (1) the "first" and "universal detector" claims require external literature verification that is deferred in this review; (2) the relative improvement metric ("51% relative to remaining space") is non-standard and potentially misleading; (3) small sample sizes (150 per condition) without variance reporting limit fine-grained statistical conclusions; and (4) the causal motivation for Glimpse (distribution mismatch hypothesis) is stated but not empirically validated.

## Strengths
1. **Practical and well-motivated technical contribution.** The core problem—white-box detection methods cannot be applied to proprietary LLMs—is real and important. Glimpse provides a clean, practical solution: estimate the full distribution from the top-K probabilities that standard APIs already return. The three estimation algorithms (Geometric, Zipfian, MLP) are each justified and ablated, giving practitioners choices based on their constraints.

2. **Comprehensive empirical evaluation.** The paper evaluates across 5 source models (ChatGPT, GPT-4, Claude-3 Sonnet/Opus, Gemini-1.5 Pro), 4 datasets covering 7 languages, and multiple scoring models ranging from Babbage-1.3B to GPT-4. The use of Mix3 and Mix6 aggregated datasets adds robustness. The inclusion of multi-lingual evaluation (M4 dataset) and paraphrasing attack analysis (DIPPER) strengthens the practical relevance.

3. **Clear methodology exposition.** The method section is well-organized: Section 2.1 defines the task and terminology, Section 2.2 explains the integration with Fast-DetectGPT, Section 2.3 presents the three estimation algorithms with formal constraints, and Section 2.4 discusses universality. The equations are clearly written and the notation is consistent throughout.

4. **Reproducibility-oriented presentation.** The paper releases code and data, reports hyperparameter details (top-K values, rank-list sizes, prompts), and provides ablation studies for key design choices (estimation algorithm, top-K, rank-list size, prompt sensitivity). This transparency enables verification and follow-up work.

5. **Interesting cross-model finding.** The observation that "larger LLMs can also serve as universal detectors" (contrary to prior work claiming smaller models are better) is an intriguing empirical finding that could influence future detector design. The fact that Babbage (1.3B) outperforms Neo-2.7 (2.7B) suggests that model architecture or training data distribution matters more than raw parameter count for detection efficacy.

## Weaknesses
1. **Relative improvement metric is non-standard and potentially misleading.** The paper uses "X% relative to the remaining space" (i.e., (AUROC_gain)/(1-AUROC_baseline)) throughout the abstract and Section 3.3. This metric inflates perceived gains (e.g., 51% improvement from an absolute gain of 0.048 AUROC). Most readers will interpret "51% improvement" as a 51% relative increase, which is impossible since AUROC is bounded at 1.0. This metric is not defined at first use in the abstract, making it uninterpretable without reading the full method section.

2. **Core motivational hypothesis is unvalidated.** The paper claims that Fast-DetectGPT's lower accuracy on GPT-4 is caused by "distribution mismatch between the small surrogate model and the large source models." This hypothesis drives the entire Glimpse design, but no diagnostic experiment directly measures the mismatch or its correlation with detection accuracy. Alternative explanations (e.g., capacity limits, training data differences) remain plausible.

3. **"First" and "universal" claims require external verification.** The claim "To our knowledge, we are the first to investigate white-box detection methods using proprietary models" (Page 2) and "larger LLMs can be universal detectors" (Page 8) cannot be verified in this run due to retrieval unavailability. While appropriately scoped with "to our knowledge" for the first claim, the "universal" claim overstates the evidence (only five tested models).

4. **Small sample size and missing statistical rigor.** Each evaluation condition uses only 150 samples per class. No confidence intervals, standard deviations, or significance tests are reported. Given that many methods cluster within 0.01-0.02 AUROC of each other in Table 1, the fine-grained ranking among top methods is not statistically supported.

5. **Related Work section has structural and formatting issues.** The White-Box Methods paragraph is a chronological list rather than a principled grouping. The Other Detection Methods paragraph contains duplicate references (Solaiman et al., 2019 and Fagni et al., 2021 each appear twice), which is a basic editing oversight.

6. **MLP training-inference distribution shift unaddressed.** The MLP estimation algorithm is trained on Neo-2.7B distributions but applied to GPT-3.5/GPT-4 distributions, which the paper itself shows are "sharper." The paper does not analyze how this distribution shift affects estimation quality.

## Key Issues
### Ranked Core Defect Board

| Rank | Issue | Severity | Research-Value Impact | Validity Risk | Confidence | Fixable? |
|------|-------|----------|----------------------|--------------|------------|----------|
| 1 | Non-standard "remaining space" relative metric used without definition in abstract | Major | Medium—misleads readers, inflates perceived gain | Low (metric is correct but presentation is problematic) | High | Yes—report absolute AUROC |
| 2 | Core distribution-mismatch hypothesis unvalidated | Major | Medium—weakens causal narrative | Medium (alternative explanations exist) | High | Yes—add diagnostic KL-divergence experiment |
| 3 | "First" and "universal" novelty claims deferred—cannot be verified externally | Major | High—affects novelty verdict | Medium | Medium | Yes—scope claims tighter |
| 4 | Missing statistical significance (no CIs, no std, small n=150) | Major | Medium—limits fine-grained comparisons | Low | High | Yes—add bootstrap/DeLong tests |
| 5 | MLP training-inference distribution shift unaddressed | Minor | Low—empirically MLP works | Low | High | Yes—add diagnostic analysis |
| 6 | Related Work: duplicate references and chronological listing | Minor | Low—editing quality | None | High | Yes—deduplicate and restructure |

### Detailed Analysis of Top 3 Issues

**Issue 1: Misleading relative improvement metric.** The abstract states "improving the score by 51% relative to the remaining space of the open source baseline." This maps to (0.954-0.906)/(1-0.906) ≈ 51%. While mathematically correct, this is non-standard and can be misinterpreted as a 51% relative increase in AUROC, which is impossible. The same metric appears in Section 3.3. The paper should report absolute AUROC values and define "remaining space" explicitly. (See annotation on Page 1 - Abstract and Page 8 - Latest LLMs paragraph.)

**Issue 2: Unvalidated causal hypothesis.** The paper's motivation relies on the claim that Fast-DetectGPT's lower accuracy on GPT-4 is caused by "distribution mismatch between the small surrogate model and the large source models." This is presented as speculation ("We speculate that...") but then the entire Glimpse method is built to address it without validation. A simple diagnostic experiment—computing KL divergence between surrogate and source distributions across token positions and correlating it with per-position detection accuracy—would directly support or refute this hypothesis. (See annotation on Page 2 - Fast-DetectGPT paragraph.)

**Issue 3: Novelty claims require external verification.** The "first to investigate white-box detection methods using proprietary models" claim and the "universal detector" claim both depend on literature context that cannot be verified in this run due to retrieval unavailability. The "universal" claim is particularly concerning because only five source models are tested. While the paper appropriately includes "to our knowledge" qualifiers, the conclusion restates the "first" claim without this qualifier. (See annotations on Page 2 - novelty claim paragraph and Page 8 - Universal detectors paragraph.)

## Actionable Suggestions
### P0: Must-Fix (publication-critical)

**S1. Replace non-standard relative metric with absolute AUROC in abstract and main text.**
- **Where:** Page 1 (Abstract), Page 8 (Section 3.3), and any occurrence of "X% relative to the remaining space."
- **Current:** "improving the score by 51% relative to the remaining space of the open source baseline."
- **Replace with:** "improving average AUROC from 0.906 (open-source baseline) to 0.954 (Glimpse with GPT-3.5), an absolute gain of +0.048." If the relative metric is kept for comparison with prior work, define it explicitly at first use and always report the absolute value alongside it.

**S2. Validate the distribution-mismatch hypothesis with a diagnostic experiment.**
- **Where:** Page 2 (Introduction) or Appendix.
- **Action:** Compute per-token-position KL divergence between surrogate (Neo-2.7B) and source model (GPT-4) distributions on a held-out corpus. Report the correlation between per-position KL divergence and detection accuracy. This would either confirm the hypothesis (strong correlation) or suggest alternative explanations (weak correlation).
- **Acceptance criterion:** Show that KL divergence between surrogate and source model distributions is significantly higher for GPT-4 than for open-source models (p < 0.05), and that this divergence is negatively correlated with detection accuracy.

**S3. Add statistical significance reporting for main results.**
- **Where:** Page 7 (Table 1) and Page 21 (Tables 7-8).
- **Action:** Report mean ± std over at least 3 runs with different random seeds. Add DeLong test p-values for the difference between the top method and the strongest baseline. For the main results (Table 1), add a column showing 95% confidence intervals.
- **Expected benefit:** Enables readers to assess whether the reported differences (e.g., Geometric vs Zipfian: 0.9537 vs 0.9438) are statistically meaningful.

**S4. Scope the "universal detector" claim and add a qualifier.**
- **Where:** Page 8 (Section 3.3).
- **Action:** Replace "larger LLMs can be universal detectors" with "larger LLMs, when equipped with Glimpse, can serve as effective detectors across the five tested source models and six languages." Add a sentence acknowledging that generalization to unseen generators requires further validation.

### P1: High-Impact Improvements

**S5. Deduplicate references and restructure Related Work.**
- **Where:** Page 10 (Section 4).
- **Action:** Remove duplicate citations (Solaiman et al., 2019; Fagni et al., 2021 appear twice each). Restructure the White-Box paragraph into thematic groups: probability-based, rank-based, curvature-based, embedding-based.

**S6. Add MLP distribution shift analysis.**
- **Where:** Appendix A.3.
- **Action:** Add a scatter plot comparing open-source (Neo-2.7B) and proprietary (GPT-3.5) log-probability decay patterns. Report correlation (Spearman rho) between them. Discuss why the MLP trained on one distribution transfers to another.

**S7. Fix grammatical issues.**
- **Where:** Page 9, "We assessment" → "We assess."
- **Where:** Page 10, Related Work: "rely human-authored texts" → "rely on human-authored texts."
- **Where:** Page 6, Datasets: space before comma in "Bulgarian , where".

### P2: Nice-to-Have Improvements

**S8. Add a limitation on the language confound in multilingual evaluation.**
- **Where:** Page 9 (Section 3.5).
- **Action:** Acknowledge that different languages use different data sources (News, Wikipedia, RuATD conversations), so domain and language are confounded.

**S9. Clarify the entropy sign convention in Eq. (4).**
- **Where:** Page 4 (Section 2.2).
- **Action:** Add a note: "The token-level mean $\tilde{\mu}_j$ as defined equals the negative Shannon entropy. This sign convention is applied consistently across all terms and does not affect the final curvature metric."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction (Page 1-2) follows this structure:
- P1: LLMs are powerful and pose risks → detection is needed → detection becomes harder as LLMs improve.
- P2: White-box methods need full access (restricted to open-source); black-box methods work with proprietary models but are less efficient → Glimpse bridges this.
- P3: Fast-DetectGPT as a running example → distribution mismatch problem → need for large models as surrogate.
- P4: Glimpse proposed (probability distribution estimation from partial observations).
- P5: Results preview with numbers.
- P6: "First" novelty claim.

**Problem alignment check:** The introduction correctly identifies the core problem (white-box methods cannot use proprietary models). **Variable alignment check:** Core concepts (partial observation, full distribution estimation, curvature metric) appear consistently throughout Methods and Experiments. **Contribution-evidence alignment check:** The claims in the introduction (improved accuracy, efficiency) are supported by the experiments.

**Main issue:** The introduction compresses the problem-motivation-solution chain across many short paragraphs (six paragraphs in ~1.5 pages), which can feel fragmented. The "white-box methods are less efficient" claim in P2 is stated without quantitative backing.

### Recommended Storyline (Option A - Most Coherent)

Follow a tighter 4-paragraph structure:

**P1 (Big Picture + Gap):** Start with the detection problem and the fundamental dilemma—white-box methods are accurate but cannot access proprietary models, black-box methods work but are inefficient. End with a clear gap statement: "No existing method combines the accuracy of white-box detection with the power of proprietary LLMs."

**P2 (Solution Intuition):** Introduce Glimpse at a high level. Explain that standard API responses already include top-K log probabilities, and that white-box metrics can be computed from probability values alone (no token identities needed). State the three estimation approaches without technical detail.

**P3 (Fast-DetectGPT Example + Validation):** Use Fast-DetectGPT as a concrete running example. Report its GPT-4 accuracy gap (AUROC 0.91 vs 0.99) and state the distribution-mismatch hypothesis. Then transition: "We validate this hypothesis by measuring KL divergence between surrogate and source distributions (Section 3)... This validates the need for using the source model itself as the surrogate."

**P4 (Contributions):** Bullet-style or numbered contributions: (1) Glimpse—probability estimation from partial observations; (2) First application of white-box methods to proprietary models; (3) Empirical results across 5 models, 4 datasets, 7 languages showing ~0.95 AUROC.

### Complete Writing Blueprint

**Abstract Outline (5 sentences):**
- S1 (Problem): "LLMs can generate text nearly indistinguishable from human writing, motivating reliable detection methods."
- S2 (Gap): "Current zero-shot detectors face a dilemma: accurate white-box methods cannot access proprietary models, while black-box methods that can are inefficient."
- S3 (Solution): "We propose Glimpse, which estimates full token-level probability distributions from the top-K probabilities available through standard LLM APIs, enabling white-box methods to be applied to proprietary models."
- S4 (Key Result): "With Fast-DetectGPT and GPT-3.5, Glimpse achieves an average AUROC of 0.954 across five state-of-the-art source models, an absolute gain of +0.048 over the open-source baseline."
- S5 (Implication): "These results demonstrate that advanced LLMs, when equipped with distribution estimation, can serve as effective detectors of their own outputs."

**Introduction Outline (4 paragraphs):**
- P1: LLM detection challenge → white-box vs black-box dilemma → specific gap (accuracy vs access trade-off). **Transition:** "We bridge this gap by enabling white-box methods to operate on proprietary models."
- P2: Glimpse intuition—API returns top-K probabilities, metrics depend only on probability values, estimation is feasible. **Transition:** "We instantiate this idea through three estimation algorithms."
- P3: Fast-DetectGPT case study—its GPT-4 accuracy gap, distribution mismatch hypothesis, validation. **Transition:** "Validating this hypothesis motivates using the source model as the surrogate."
- P4: Contribution summary with scoped, non-hyped language.

## Priority Revision Plan
The revision order prioritizes issues by fixability and impact. The plan is divided into three stages.

### Stage 1: Immediate Fixes (Before Next Submission)

| Task | Description | Expected Impact | Effort |
|------|-------------|-----------------|--------|
| P0-S1 | Replace non-standard relative metric with absolute AUROC in Abstract, Table 1, and Section 3.3 | Prevents misinterpretation; improves scientific honesty | Low (text edits) |
| P0-S4 | Scope "universal detector" claim and add qualifier | Aligns claim strength with evidence | Low (text edits) |
| P1-S5 | Deduplicate References section and restructure Related Work | Improves editing quality and readability | Low (text edits) |
| P1-S7 | Fix grammatical errors ("We assessment", missing prepositions, spacing) | Improves professional presentation | Low (text edits) |
| P1-S9 | Add entropy sign convention note to Eq. (4) | Prevents reader confusion | Low (one-sentence addition) |

### Stage 2: Medium-Effort Improvements (During Revision)

| Task | Description | Expected Impact | Effort |
|------|-------------|-----------------|--------|
| P0-S2 | Validate distribution-mismatch hypothesis with KL divergence diagnostic | Strengthens causal narrative and method motivation | Medium (one experiment + appendix) |
| P0-S3 | Add statistical significance: confidence intervals, DeLong tests for Table 1 | Enables meaningful comparison between methods | Medium (re-run with different seeds, compute CIs) |
| P1-S6 | Add MLP distribution shift analysis (scatter plot + correlation) | Increases methodological transparency | Low-Medium (one figure + paragraph) |

### Stage 2b: Experiment Enhancement

| Task | Description | Expected Impact | Effort |
|------|-------------|-----------------|--------|
| P2-S8 | Acknowledge language-domain confound in multilingual evaluation | Improves scientific honesty | Low (one sentence) |
| Proposed-E1 | Add OOD generalization test (detect outputs from an unseen model) | Tests "universal" claim directly | Medium (one additional model) |

### Stage 3: Nice-to-Have Enhancements

| Task | Description |
|------|-------------|
| Rewrite Abstract with absolute metrics (see Storyline Options) |
| Tighten introduction to 4 paragraphs (see Storyline Options) |
| Add bootstrap analysis for method ranking |

### Revision Strategy Roadmap (ASCII Diagram)

```text
Stage 1 (Days 1-2): Claim and Language Fixes
  [Non-standard metric] -> [Replace with absolute AUROC]
  [Universal detector claim] -> [Scope to tested models]
  [Duplicate references] -> [Deduplicate + restructure]
  [Grammar errors] -> [Fix]

Stage 2 (Days 3-5): Experimental Validation
  [Distribution-mismatch hypothesis] -> [KL divergence diagnostic]
  [Missing significance] -> [Add CIs + DeLong tests]
  [MLP distribution shift] -> [Scatter plot analysis]

Stage 3 (Days 6-7): Writing Polish
  [Abstract] -> [Rewrite with absolute metrics]
  [Introduction] -> [Tighten to 4 paragraphs]
  [Related Work] -> [Thematic reorganization]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Main detection accuracy (Table 1) | 5 source models, 4 scoring models, 3 datasets (XSum, Writing, PubMed) + Mix3 | AUROC | Fast-Detect (GPT-3.5/4) achieves ~0.95 AUROC across source models | C1: Glimpse enables white-box methods on proprietary models | No confidence intervals; small n=150 |
| E2 | KL divergence analysis (Figure 2-3) | Neo-2.7B distributions vs estimated (Geom/Zipf/MLP) | KL divergence, AUROC correlation | MLP has lowest KL; Geometric has highest KL but competitive AUROC | C1: Estimation is effective | Only tested on Neo-2.7B; no proprietary model KL |
| E3 | Ablation on estimation algorithm (Figure 4) | 3 datasets, 2 scoring models (GPT-3.5, GPT-4) | AUROC per dataset per algorithm | Dataset-specific preference; Geometric best on Writing/PubMed, Zipfian on XSum | C1: No universal best algorithm | Small sample size per dataset |
| E4 | Ablation on top-K (Figure 5) | K=1,3,5,7,10; 2 methods (Fast-Detect, LogRank); 2 scoring models | AUROC | Higher K generally helps Geometric; Zipfian/MLP exceptions with K=1 | C1: Glimpse works even with K=1 for suitable algorithms | Only tested on GPT-4 generated texts |
| E5 | Robustness across source models (Table 7) | Single threshold from ChatGPT Mix3 applied to all models | ACC | Fast-Detect (GPT-3.5) highest ACC (0.8955) across all models | C2: Glimpse is robust | Threshold optimized on ChatGPT only |
| E6 | Robustness across domains (Table 8) | Cross-validation across XSum/Writing/PubMed | ACC | Glimpse methods have smallest accuracy drop (0.014-0.022) | C2: Robust across domains | Only 3 English domains |
| E7 | Multilingual robustness (Table 2) | 6 languages from M4 dataset | AUROC | Near-perfect for Urdu/Indonesian/Arabic; Russian lower (0.8555) | C2: Robust across languages | Domain confounded with language (different datasets per language) |
| E8 | Paraphrasing attack (Table 9) | DIPPER (60L, 60O) on ChatGPT outputs | TPR@1%FPR | Babbage best under attack; GPT-3.5 vulnerable on XSum | C2: Partial robustness | Only DIPPER attack tested |
| E9 | Ablation on rank-list size (Figure 8) | M=100-1000; Geometric and Zipfian | AUROC | Larger M helps Geometric; inconsistent for Zipfian | C1: Hyperparameter sensitivity | MLP skipped |
| E10 | Ablation on prompt (Figure 9) | 5 prompts (empty to complex) on Babbage/GPT-3.5/GPT-4 | AUROC | GPT-4 most prompt-sensitive (0.73-0.97); Babbage least | C2: Methodology understanding | Only 5 manual prompts |

### Research-Theme Gap Diagnosis

1. **New Knowledge (Partial):** The paper demonstrates that full distributions can be usefully estimated from top-K probabilities, enabling a practical bridge between white-box detection and proprietary models. However, the core hypothesis (distribution mismatch) is not validated, which weakens the knowledge contribution.

2. **Reproducibility/Reusability (Good):** Code and data are released. Hyperparameters are documented. The method is computationally lightweight (462s vs 1911s for DNA-GPT). This is a strength.

3. **Potential to Change Practice/Understanding (Moderate):** If validated, the finding that larger LLMs (with Glimpse) are more effective detectors than smaller models could shift detector design. However, without OOD generalization testing and without external literature verification, the practical impact remains uncertain.

### Proposed Research Experiments (P0/P1/P2)

**E-P0-1: Distribution-Mismatch Validation**
- **Target Claim:** C1 (motivation)—the accuracy gap is caused by distribution mismatch.
- **Hypothesis:** KL divergence between surrogate and source model distributions correlates negatively with detection accuracy.
- **Minimal Design:** For 3 surrogate models (Neo-2.7B, GPT-J, GPT-3.5) and 3 source models (ChatGPT, GPT-4, Gemini), compute per-token-position KL(p_surrogate || p_source) on a held-out corpus of 1000 tokens. Correlate per-model KL mean with detection AUROC.
- **Controls:** Same text input across all models; identical tokenization where possible.
- **Metrics:** Spearman correlation between KL mean and AUROC, per-model and aggregated.
- **Success Criterion:** rho < -0.5 (strong negative correlation) supports the hypothesis.
- **Estimated Cost/Time:** Low (API calls for logprobs, ~$20, 1 day).
- **Expected Paper-Quality Gain:** Validates the core motivation, strengthening causal narrative.

**E-P0-2: Statistical Significance for Main Results**
- **Target Claim:** All claims depending on method ranking.
- **Hypothesis:** Top methods are statistically distinguishable from baselines.
- **Minimal Design:** Re-run Table 1 with 5 random seeds; report mean ± std; compute DeLong test [1] between Fast-Detect (GPT-3.5) and Likelihood (GPT-3.5) for each source model.
- **Controls:** Same seeds across all methods.
- **Metrics:** AUROC with 95% CI, DeLong p-values.
- **Success Criterion:** p < 0.05 for the primary comparison.
- **Estimated Cost/Time:** 5x the current compute, ~$50 API costs.
- **Expected Paper-Quality Gain:** Enables reliable method comparison.

**E-P1-1: OOD Generalization Test**
- **Target Claim:** C2—Glimpse-equipped larger LLMs are effective detectors across diverse settings.
- **Hypothesis:** Fast-Detect (GPT-3.5) maintains AUROC > 0.85 on a model not seen during method development (e.g., Mixtral 8x7B or Llama-3-70B).
- **Minimal Design:** Generate 150 texts from an unseen source model on XSum/Writing/PubMed. Apply existing Glimpse detectors without retuning. Report AUROC.
- **Controls:** Same procedure as main experiments.
- **Metrics:** AUROC per dataset; comparison to in-distribution performance.
- **Success Criterion:** All per-dataset AUROC > 0.85.
- **Estimated Cost/Time:** Low-Medium (one additional model, ~$15 API, 1-2 days).
- **Expected Paper-Quality Gain:** Directly tests the "universal" claim under a more challenging condition.

**E-P1-2: Ablation of Glimpse Estimation Error on Detection Accuracy**
- **Target Claim:** C1—Glimpse estimation quality directly affects detection accuracy.
- **Hypothesis:** Methods with lower estimation KL divergence achieve higher detection accuracy.
- **Minimal Design:** For each estimation algorithm (Geom/Zipf/MLP) and each top-K value, compute per-position KL(real || estimated). Correlate with detection AUROC per source model.
- **Controls:** Same real distributions from the source model.
- **Metrics:** Spearman correlation per (algorithm, K) combination.
- **Success Criterion:** Significant negative correlation across most settings.
- **Estimated Cost/Time:** Low (reuses existing KL data, 1 day analysis).
- **Expected Paper-Quality Gain:** Quantifies the sensitivity of detection accuracy to estimation quality.

### Experiment Upgrade Plan (ASCII Diagram)

```text
Stage A: Immediate Validation (P0)
  [Distribution-mismatch hypothesis]
          |
          v
  [KL divergence diagnostic] -> [Correlation with AUROC]
          |
          v
  [Validates or refutes core motivation]

Stage B: Statistical Rigor (P0)
  [Multi-seed runs] -> [CIs + DeLong tests]
          |
          v
  [Reliable method ranking]

Stage C: Scope Testing (P1)
  [OOD model test] -> [Unseen generator]
          |
          v
  [Tests "universal detector" claim]

Stage D: Mechanism Understanding (P1)
  [KL-to-AUROC correlation per algorithm]
          |
          v
  [Quantifies estimation-accuracy link]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

Rationale: The paper makes a practical and clearly demonstrated contribution (enabling white-box detection methods on proprietary LLMs through distribution estimation). The empirical evaluation is broad (5 source models, 7 languages, multiple scoring models). However, the score is constrained by: (1) the non-standard relative improvement metric that inflates perceived gains without adding scientific value; (2) the core motivational hypothesis (distribution mismatch) remains unvalidated; (3) the "first" and "universal" novelty claims cannot be externally verified in this run; (4) missing statistical significance testing limits the reliability of fine-grained method comparisons; and (5) the small sample size (n=150) without confidence intervals. These issues are fixable, but they reduce confidence in the current presentation.

**Post-Revision Target: [7.5, 8.0]/10**

If the authors address the P0 items (replace non-standard metric, add distribution-mismatch diagnostic, add confidence intervals, scope overclaims) and P1 items (add significance tests, restructure Related Work), the paper's validity, clarity, and impact would increase substantially. The core technical contribution—demonstrating that full distributions can be usefully estimated from top-K probabilities for detection—is solid and would remain the main strength. The upper bound is 8.0 because the method's API dependency (requires Completion API with logprobs) is an inherent limitation, and the small dataset size (n=150) is a field-wide convention that is unlikely to change in revision but constrains the evidence base.