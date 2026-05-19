## Summary
# Final Review Report

## Summary

This paper presents **Instructive Decoding (ID)** , a training-free decoding-time method that improves instruction adherence in instruction-tuned language models. ID operates by contrasting next-token logits from the original instruction against logits from a systematically corrupted "noisy" instruction, using the same model for both forward passes. Four noisy instruction variants are explored: Trunc-Shuf (truncation + shuffling), Null (no instruction), Rand Words (random word replacement), and Opposite (a deliberately misleading directive). The key finding is that the 'Opposite' variant, which causes the most performance degradation when used alone, yields the largest improvement when integrated into ID. Experiments across Tk-Instruct (770M–11B), T0 (3B), Alpaca (7B), and OpenSNI (7B) models on SUPNATINST and UNNATINST datasets show consistent Rouge-L improvements of approximately 1–2 points in zero-shot settings. The paper also introduces two auxiliary metrics (Label Adherence and Label Coherence) to analyze classification task performance.

**Overall assessment:** ID is a conceptually elegant and practically simple method. The core idea — contrastive decoding using instruction perturbation within a single model — is novel in its specific formulation, and the empirical evaluation covers a reasonable range of models and tasks. However, the paper has several notable weaknesses: (1) the main results lack statistical significance testing and variance reporting, (2) the degradation-enhancement correlation claim is based on only 6 data points, (3) key mechanistic claims about the anchoring effect are asserted rather than causally verified, and (4) the computational cost (2× inference) is not measured. Novelty and comparison conclusions are deferred due to unavailability of external literature retrieval in this run.

## Strengths
1. **Conceptual simplicity and practical applicability.** ID is remarkably straightforward: it requires only one additional forward pass with a modified instruction and a simple logit subtraction. No parameter updates, no auxiliary models, no task-specific tuning. This makes it easy to integrate into existing instruction-tuned pipelines.

2. **Consistent empirical gains across diverse models.** The method is evaluated across multiple model families (Tk-Instruct Large/XL/XXL, T0, Alpaca, OpenSNI) spanning different architectures (T5-based, LLaMA-based) and scales (770M to 11B). ID consistently improves Rouge-L scores, with the 'Opposite' variant showing the most robust gains. The fact that models not trained on SUPNATINST (Alpaca, T0) also benefit suggests the method has cross-dataset generalization potential.

3. **Interesting degradation-enhancement correlation.** The finding that noisy instructions which cause the largest performance drop when used alone produce the largest gains when integrated into ID is non-obvious and provides a useful heuristic for practitioners: choose the noisy instruction that maximizes divergence.

4. **Auxiliary metrics (LA, LC).** The introduction of Label Adherence and Label Coherence provides a more nuanced evaluation beyond Rouge-L for classification tasks. This is a methodological contribution in its own right, as standard n-gram overlap metrics often fail to capture instruction-following quality.

5. **Thorough ablation on hyperparameter epsilon.** Figure 6 shows that ID is relatively robust to the smoothing coefficient epsilon in the [0.1, 0.4] range, which is practically useful for deployment without extensive tuning.

## Weaknesses
1. **Missing statistical significance and variance reporting.** All main results (Table 1) are presented as single-point Rouge-L estimates without standard deviations, confidence intervals, or significance tests. The reported gains (typically 1–2 Rouge-L points) are modest relative to the baseline range (23–48), and without variance information the reader cannot assess whether these improvements are statistically reliable. The ablation on epsilon (Figure 6) shows that performance can vary by ~0.5 points within the stable range, which is comparable to some of the reported gains.

2. **Small-sample correlation claim.** The degradation-enhancement correlation (Pearson R ≈ 0.88–0.90) is computed over only 6 noisy instruction variants. With N=6, the correlation is highly sensitive to individual points, and no p-values or confidence intervals are reported. The strong verbal claim ("a strong positive correlation") overstates the statistical reliability of this finding.

3. **Unverified mechanistic claims.** The paper attributes ID's success to "the anchoring effect" and "counterbalancing inherent model biases," but these are asserted rather than causally tested. The only mechanistic evidence is a t-SNE visualization (Figure 7b) showing that different noisy instructions produce separable embeddings — this demonstrates that the model processes them differently but does not prove that contrastive subtraction removes "biases." No controlled ablation isolates what type of bias is being corrected.

4. **Computational cost not measured.** ID requires two forward passes per token (one for original instruction, one for noisy instruction), effectively doubling inference cost. The paper acknowledges this in the Limitations (Appendix B.1) but does not report actual latency, memory usage, or throughput numbers. For practitioners considering deployment, this cost is a critical factor.

5. **Qualitative analysis based on limited examples.** The claim that combining original + noisy instructions "does not lead to improved performance" (Section 4) is based on visual inspection of two binary classification tasks. Central mechanistic conclusions about how ID works should be supported by quantitative evidence across all tasks, not illustrative examples.

6. **Related work lacks explicit differentiation.** The Related Work section (Section 5) surveys prior methods but does not explicitly differentiate ID from the most similar single-model contrastive approaches (DExperts, DoLa). The novelty claim is weakened by the absence of head-to-head comparison with these methods on the same tasks.

## Key Issues
### Issue 1: Lack of Statistical Reliability for Main Results (Severity: Major)
**Location:** Page 5–6, Section 3.2 (Result Overview, Table 1)
**Evidence:** All entries in Table 1 are single-point Rouge-L estimates. No variance, confidence intervals, or significance tests are reported anywhere in the main paper or appendix. The gains are modest (e.g., Tk-XL: 45.36 → 46.69, +1.33; OpenSNI-7B: 48.05 → 49.47, +1.42). The epsilon sensitivity analysis (Figure 6) shows performance varies by ~0.5 within the stable range, which is comparable to some per-category gains.
**Risk:** Without uncertainty quantification, the central empirical claim ("ID consistently outperforms") cannot be verified as statistically significant. This is a validity-critical weakness.
**Fix:** Report mean ± std over ≥3 seeds for all main results. Add a paired bootstrap significance test or Wilcoxon signed-rank test comparing each ID variant against baseline across 119 tasks.

### Issue 2: Degradation-Enhancement Correlation Overclaimed (Severity: Major)
**Location:** Page 6, Section 3.2 (From Degradation to Enhancement paragraph)
**Evidence:** Pearson R = 0.9039 (Tk-XL) and 0.8789 (OpenSNI-7B) computed over only 6 noisy instruction types. No p-values or confidence intervals reported. With N=6, the correlation is highly unstable.
**Risk:** A reader or reviewer familiar with statistics will immediately question the reliability of a correlation with N=6. This weakens the theoretical contribution about the degradation-enhancement relationship.
**Fix:** Report exact p-value, 95% bootstrap CI for R. Explicitly note the small-N caveat. Add per-variant numerical values in a table.

### Issue 3: Mechanism Claims Not Causally Verified (Severity: Major)
**Location:** Page 8, Section 4 (Discussion paragraphs)
**Evidence:** The paper claims ID works through "anchoring effect" and "counterbalancing biases," but provides only t-SNE visualization (showing embeddings are separable) and two-task qualitative plot as evidence. No controlled experiment isolates whether the improvement comes from bias correction, variance reduction, or simple output smoothing.
**Risk:** The theoretical framing (anchoring effect, bias correction) could be incorrect; the improvement might simply come from softening sharp logit distributions rather than any instruction-specific alignment.
**Fix:** Add an ablation that isolates whether the improvement is specific to instruction-contrastive signal or simply a generic smoothing effect. Compare ID against a control that replaces noisy-instruction logits with random Gaussian noise.

### Issue 4: Computational Cost Not Quantified (Severity: Minor)
**Location:** Page 15, Appendix B.1 (Limitations)
**Evidence:** The limitation paragraph acknowledges "two separate inferences" but provides no measured latency, throughput, or memory numbers.
**Risk:** For ICLR, where practical impact is valued, the absence of efficiency metrics limits assessment of real-world applicability.
**Fix:** Report tokens-per-second and peak GPU memory for baseline vs. ID across model sizes.

### Issue 5: Opposite Variant Phrasing Not Justified (Severity: Minor)
**Location:** Page 4, Section 2.3
**Evidence:** The 'Opposite' variant wording is presented as a single fixed template with no ablation or justification. No alternative opposite-style phrasings are tested.
**Risk:** Reproducibility concern — would a different "opposite" phrasing produce similar gains? The paper's main result (best variant) rests on an arbitrary linguistic choice.
**Fix:** Add a small experiment comparing 3-4 opposite-style phrasings on one model-dataset pair to demonstrate robustness.

## Actionable Suggestions
### Suggestion 1: Add Statistical Significance and Variance to All Main Results (Must)
Replace the single-point estimates in Table 1 with mean ± std over 3+ random seeds. For each model and ID variant, add a column showing the p-value from a paired Wilcoxon signed-rank test (comparing per-task Rouge-L against baseline). This is the single highest-impact revision for improving scientific credibility.

### Suggestion 2: Strengthen the Degradation-Enhancement Analysis (Must)
- Report the exact sample size (N=6), Pearson R, p-value, and 95% bootstrap confidence interval for each reported correlation.
- Add a scatter plot with per-variant labels (already in Figure 4a) but also provide a table showing: (variant, degradation_RougeL, improvement_RougeL) numerically.
- Explicitly add a caveat: "With only six noisy variants, the correlation should be interpreted as a qualitative trend rather than a statistically validated relationship."

### Suggestion 3: Quantify the "Combined Instruction" Analysis (Must)
Rather than showing two scatter plots for two tasks, compute across all 58 classification tasks: mean prediction confidence, accuracy, and label entropy for (a) baseline, (b) opposite-only, and (c) opposite+base. Present in a small table. This would provide quantitative support for the claim that adding the original instruction dampens the contrastive effect.

### Suggestion 4: Report Computational Cost (Nice-to-have)
Add a small table showing:
- Tokens per second (baseline vs. ID)
- Peak GPU memory (baseline vs. ID)
- Total generation time for a fixed-length output
Report these for at least one model size (e.g., Tk-XL) on one representative task.

### Suggestion 5: Test Alternative Opposite Phrasings (Nice-to-have)
Test 3-4 variants of the opposite instruction (e.g., "Say the opposite of the correct answer," "Invert your response," "Disagree with the instruction") on one model-dataset pair (e.g., Tk-XL on SUPNATINST) to verify that the choice of opposite wording does not qualitatively change results.

### Suggestion 6: Clarify Algorithm 1 (Minor)
Replace `yt = arg max(SOFTMAX [zt − ϵ ∗ ˜zt])` with `yt = arg max(zt − ϵ ∗ ˜zt)` since softmax is order-preserving and redundant before argmax.

### Suggestion 7: Condense Section 2.1 (Minor)
Reduce the preliminary notation paragraph to 2-3 sentences and remove discussion of nucleus sampling, which is not used in the main experiments.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction follows a 3-paragraph structure: (P1) background on LMs and instruction-tuning, (P2) challenges and limitations of existing approaches, (P3) anchoring effect inspiration and ID overview. The contribution list appears at the end of the introduction. The main issues are: (a) the first paragraph reads as a literature list rather than a problem hook, (b) the research gap is not stated crisply until the middle of paragraph 2, (c) the anchoring effect motivation in paragraph 3 is interesting but the logical connection to the actual algorithm is not explained.

### Alternative Storyline Candidate: "Problem-First" Arc
This restructures the introduction to answer the three core questions in order: what is missing → what we solve → why better.

**P1 (Problem Hook):** Start with a concrete statement: "Instruction-tuned LMs achieve impressive zero-shot generalization, but their performance degrades sharply when instructions differ from training data." Then pose the central question: "Can we improve instruction adherence at decoding time without any parameter updates?"

**P2 (Gap & Prior Insufficiency):** "Existing approaches address this through dataset expansion (costly) or prompt engineering (task-specific). Decoding-time methods like Contrastive Decoding require a separate amateur model, limiting applicability." End with: "A single-model, training-free method that exploits the model's own sensitivity to instruction variations is missing."

**P3 (Method & Key Insight):** "We propose Instructive Decoding (ID), which contrasts logits from the original instruction against logits from a systematically corrupted 'noisy' instruction using the same model. The key insight: noisy instructions that push predictions toward task-irrelevant outputs encode biases that can be subtracted out."

**P4 (Evidence Preview):** "ID with the 'opposite' noisy instruction consistently improves Rouge-L by 1–2 points across 4 model families and 119 unseen tasks, with particular gains in label coherence."

### Abstract Outline (Complete)
Target 5 sentences following the compact structure:

**S1 (Problem domain):** "Instruction-tuned language models exhibit strong zero-shot generalization but struggle when presented with instructions outside their training distribution."

**S2 (Prior gap):** "Existing solutions rely on costly dataset expansion or task-specific prompt engineering, and decoding-time methods typically require separate auxiliary models."

**S3 (Proposed method):** "We introduce Instructive Decoding (ID), a training-free approach that improves instruction adherence by contrasting next-token logits from the original instruction against logits from a systematically corrupted 'noisy' instruction using the same model."

**S4 (Key result with numbers):** "Across instruction-tuned models from 770M to 11B parameters and 119 unseen tasks, ID with the 'opposite' noisy instruction consistently improves Rouge-L scores (e.g., +1.33 for Tk-XL, +1.42 for OpenSNI-7B)."

**S5 (Bounded implication):** "ID requires no parameter updates and is applicable to any instruction-tuned model, though it doubles inference cost due to two forward passes per token."

### Introduction Outline (Complete)

**Paragraph 1 — Problem Hook + Stakes:**
*Role:* Establish importance and specific challenge.
*Target claim:* Instruction-tuned LMs are powerful but brittle under instruction distribution shift.
*Transition logic:* Opens with capability, then immediately identifies the gap.
*Required evidence:* Cite instruction-tuning papers and zero-shot generalization results.

**Paragraph 2 — Prior Work Gap:**
*Role:* Contrast expensive/complex prior approaches with the need for a lightweight solution.
*Target claim:* Existing mitigation strategies (data scaling, prompt engineering, CD with amateur models) have fundamental limitations.
*Transition logic:* "However" connecting from P1's capability to P2's insufficiency.
*Required evidence:* Cite dataset scaling papers and CD papers; state their limitations concisely.

**Paragraph 3 — Method Intuition:**
*Role:* Explain the core idea of ID without technical overload.
*Target claim:* Contrasting original-conditioned and noisy-conditioned logits within a single model corrects instruction-independent biases.
*Transition logic:* Introduce anchoring effect as inspiration, then connect to algorithmic implementation.
*Required evidence:* Reference Jones & Steinhardt and Malkin et al. for anchoring in LMs.

**Paragraph 4 — Evidence Preview + Contributions:**
*Role:* Summarize main results and list contributions.
*Target claim:* ID consistently improves across models; 'Opposite' variant is best; gains correlate with degradation.
*Transition logic:* "We demonstrate this across..."
*Required evidence:* Preview of Table 1's key numbers and Figure 4's correlation.

## Priority Revision Plan
### P0 (Must fix before resubmission — validity-critical)
| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | Missing variance/significance in Table 1 | Add mean±std over 3+ seeds + paired Wilcoxon test | Establishes statistical reliability of main claims |
| P0.2 | Degradation-enhancement R over N=6 | Add p-value, bootstrap CI, explicit caveat | Prevents statistical overclaim |
| P0.3 | Unverified mechanism claim | Add control ablation (random noise vs. noisy instruction) | Validates that contrastive effect is instruction-specific |

### P1 (Highly recommended — strengthens contribution)
| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | Qualitative-only combined-instruction analysis | Quantify across all 58 tasks (accuracy, entropy) | Provides quantitative support for mechanistic claim |
| P1.2 | Missing computational cost | Report tokens/sec, peak memory for baseline vs. ID | Enables practitioners to assess deployment trade-off |
| P1.3 | Undifferentiated related work | Add explicit comparison with DExperts, DoLa | Clarifies novelty positioning |

### P2 (Quality improvement — nice to have)
| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Opposite phrasing not justified | Test 3-4 alternative phrasings | Improves reproducibility |
| P2.2 | Redundant softmax in Algorithm 1 | Simplify to argmax(logits) | Eliminates confusion |
| P2.3 | Overly verbose preliminary (Section 2.1) | Condense to 2-3 sentences | Saves space for more analysis |
| P2.4 | Conclusion overclaiming | Tighten to evidence-grounded scope | Improves scientific credibility |

### Revision Order
1. **Week 1-2:** Run multi-seed experiments for all model×variant combinations (P0.1). This is the most time-consuming but most critical task.
2. **Week 2-3:** Compute bootstrap CI for Pearson R (P0.2) and run control ablation (P0.3).
3. **Week 3:** Quantify combined-instruction analysis (P1.1) and measure computational cost (P1.2).
4. **Week 4:** Revise Related Work (P1.3), test opposite phrasings (P2.1), tighten conclusion (P2.4).
5. **Week 4-5:** Copy-editing: fix Algorithm 1 (P2.2), condense preliminary (P2.3), rewrite introduction per storyline outline.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 (Table 1) | ID improves zero-shot task generalization | Tk-Large/XL/XXL, OpenSNI-7B on SUPNATINST 119 tasks | Rouge-L | ID (esp. Opposite) consistently outperforms baseline | C1, C2 | No variance, no significance test |
| E2 (Table 2) | Cross-dataset generalization | Tk-Large on UNNATINST; T0-3B, Alpaca-7B on SUPNATINST | Rouge-L | ID outperforms baseline across datasets | C1 | Opposite not always best; small gains |
| E3 (Table 3) | Few-shot setting | Tk-Large/XL, Alpaca-7B with 0/2 demo examples | Rouge-L | Gains smaller in few-shot, but no degradation | C1 | Only 2-shot tested |
| E4 (Figure 4a) | Degradation-enhancement correlation | Tk-XL, OpenSNI-7B with 6 noisy variants | Rouge-L (degradation vs. improvement) | Strong positive Pearson R (~0.88-0.90) | C2 | N=6, no CI/p-value |
| E5 (Figure 5) | Granular analysis on classification tasks | Tk-Large/XL/XXL on 58 classification tasks | EM, LA, LC | Opposite improves LC; trunc-shuf improves LA | C3 | No statistical test for interaction |
| E6 (Figure 6) | Epsilon sensitivity | Tk-XL with ID-null, epsilon in [-0.5, 0.5] | Rouge-L | Stable range [0.1, 0.4] | C2 | Only null variant tested |
| E7 (Figure 7a) | Distribution shift in classification | Tk-XL on 2 binary tasks | Probability(True) vs Prob(False) | Opposite diversifies predictions | C3 | Only 2 tasks; qualitative |
| E8 (Table 16, Appendix H) | MMLU zero-shot | Tk-Large/XL, OpenSNI-7B on 57 tasks | EM | Opposite/Null improve EM slightly | C1 | Small gains (1-3 EM points) |
| E9 (Figure 8) | ID vs CD with amateur models | Tk family; small/base/large/XL as expert/amateur | Rouge-L improvement | ID-amateur less sensitive to model size than CD | C2 | Limited analysis depth |
| E10 (Appendix D) | LA/LC metric validation | 58 classification tasks | LA, LC | NA (metric proposal) | C3 | Manual label expansion |

### Research-Theme Gap Diagnosis

1. **Causal mechanism (new knowledge):** The paper claims ID works through "anchoring effect" and "bias correction" but does not provide causal evidence. The central "why" question remains unanswered: is the improvement from bias subtraction, output smoothing, or variance reduction?

2. **Reproducibility/reusability:** The method is clearly described (Algorithm 1), but the arbitrary choice of 'Opposite' instruction phrasing, lack of computational cost reporting, and missing multi-seed variance reduce reproducibility confidence.

3. **Impact on practice/understanding:** The paper shows ID can improve off-the-shelf instruction-tuned models, which is practically useful. However, without efficiency metrics or comparisons with other lightweight methods (DExperts, DoLa), the practical value is not fully benchmarked.

### Proposed Research Experiments

#### P0 Experiment: Statistical Reliability Validation
- **Target Claim:** C1 (ID consistently outperforms baseline)
- **Hypothesis:** ID gains are statistically significant across tasks
- **Minimal Design:** Run each model×variant combination with 3 random seeds; report mean±std Rouge-L
- **Controls/Baselines:** Same as Table 1
- **Metrics:** Rouge-L mean±std, paired Wilcoxon p-value per variant vs baseline
- **Success Criterion:** p < 0.05 for opposite variant on at least 3 of 4 model families
- **Estimated Cost/Time:** ~3-5 GPU-days (depends on model size); 1-2 weeks
- **Expected Paper-Quality Gain:** High — establishes statistical foundation for central claim

#### P0 Experiment: Mechanism Control Ablation
- **Target Claim:** C2 (contrastive logit subtraction using noisy instructions is the key mechanism)
- **Hypothesis:** The improvement is specific to instruction-structured noise, not simply logit smoothing
- **Minimal Design:** Replace noisy-instruction logits z_q with (a) random Gaussian noise of same norm, (b) uniform logits, (c) null logits from an unrelated task instruction; compare ID gains
- **Controls/Baselines:** Original ID with opposite instruction
- **Metrics:** Rouge-L, LA, LC
- **Success Criterion:** ID with Gaussian noise does not produce comparable gains to instruction-based noise
- **Estimated Cost/Time:** 1-2 GPU-days; 1 week
- **Expected Paper-Quality Gain:** High — validates that the effect is instruction-specific, not a generic artifact

#### P1 Experiment: Combined Instruction Quantification
- **Target Claim:** C3 (analysis of ID behavior)
- **Hypothesis:** Opposite-only contrast outperforms opposite+base contrast across all classification tasks
- **Minimal Design:** For all 58 classification tasks, compute: accuracy, average prediction confidence, label entropy for baseline / opposite-only / opposite+base
- **Controls/Baselines:** Baseline (standard instruction)
- **Metrics:** Mean accuracy, mean confidence, mean entropy per condition
- **Success Criterion:** Opposite-only significantly improves over opposite+base on accuracy and entropy
- **Estimated Cost/Time:** <1 GPU-day; 2-3 days
- **Expected Paper-Quality Gain:** Medium — converts qualitative claim to quantitative evidence

#### P1 Experiment: Computational Cost Measurement
- **Target Claim:** C1 (practical applicability)
- **Hypothesis:** ID's 2× inference cost has measurable but manageable overhead
- **Minimal Design:** For Tk-XL on one task, measure tokens/sec, peak GPU memory, total generation time for baseline and ID
- **Controls/Baselines:** Baseline greedy decoding, ID with opposite, ID with null
- **Metrics:** Tokens/sec, peak memory (GB), latency per 100 tokens
- **Success Criterion:** Transparent reporting regardless of outcome
- **Estimated Cost/Time:** <0.5 GPU-day; 1 day
- **Expected Paper-Quality Gain:** Medium — enables practitioners to assess trade-off

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale:** The paper presents a conceptually elegant and practically simple method with consistent empirical gains across multiple models and tasks. However, the score is constrained by three major weaknesses that affect research value assessment: (1) the absence of statistical significance testing for all main results, which prevents reliable assessment of whether the gains are meaningful; (2) the overclaimed degradation-enhancement correlation based on only 6 data points; and (3) the unverified causal mechanism claims. The method's research value — a training-free, single-model contrastive decoding approach using instruction perturbation — is genuinely interesting, but the empirical rigor does not yet match the strength of the claims. Novelty assessment is deferred due to unavailability of external literature retrieval in this run; the score may need adjustment upward or downward pending manual literature verification.

**Post-Revision Target: [7.5, 8.5]/10**

**Rationale:** If the authors address the P0 items (multi-seed variance + significance tests, controlled mechanism ablation, proper statistical treatment of the correlation analysis), the empirical foundation would be substantially strengthened. Full P0+P1 implementation could raise the score to 7.5–8.5, contingent on the statistical results being favorable and the novelty claim holding up under literature verification.