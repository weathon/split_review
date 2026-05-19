## Summary
# Final Review Report

## Summary

This paper studies the tension between two critical failure modes of LLMs in summarization tasks: hallucination (generating content that contradicts the provided context) and privacy leakage (regurgitating sensitive information from the context). The authors propose a formal definition of **context influence** grounded in Pointwise Mutual Information (PMI) and Differential Privacy (DP), and introduce **Context Influence Decoding (CID)**, a tunable interpolation between the posterior (context-conditioned) and prior (context-free) logits controlled by a parameter λ.

The key analytical result is Theorem 3.1, which bounds context influence by λ × PMI, formalizing a tradeoff: amplifying context to reduce hallucination (λ > 1) increases context influence, which can inadvertently increase privacy leakage. Theorem 3.2 further connects context influence to DP auditing. The empirical evaluation on CNN-DM and PubMedQA across multiple LLMs (OPT, GPT-Neo, LLaMA 3) shows that CAD (λ=1.5) can improve ROUGE-L by 10% on CNN-DM for LLaMA 3 while increasing context influence by 1.5×. Additional experiments characterize how model capacity, context size, response length, and token n-grams affect the tradeoff.

**Strengths:** The paper addresses an important and timely problem—the underexplored privacy implications of hallucination-mitigation decoding strategies. The definition of context influence and the CID framework provide a principled lens for analyzing this tradeoff. The multi-factor empirical analysis (model size, context size, n-gram granularity) is comprehensive and reveals practically relevant patterns (e.g., first 10 tokens are most influenced, n=128 optimal for influence).

**Core Weaknesses:** (1) Theorem 3.2's DP construction is non-constructive (requires knowing PMI before generating yt), limiting its practical applicability. (2) The context influence definition (Def 3.1) requires O(|D|) forward passes per n-gram, constraining scalability. (3) Conclusion overclaims by presenting descriptive observations as prescriptive privacy guidance without causal validation. (4) No variance/confidence intervals reported despite N=1000 samples. (5) Novelty/comparison cannot be fully assessed in this review due to Retrieval-Disabled Mode.

## Strengths
1. **Timely and practically important problem formulation.** The paper identifies a genuine tension in modern LLM deployment: techniques that reduce hallucination by amplifying context reliance (e.g., CAD) can inadvertently increase the risk of leaking sensitive context information. This dual-risk framing is underexplored in prior work and has direct implications for RAG system design.

2. **Principled formal framework.** The context influence definition (Def 3.1) is cleanly motivated by P-XCMI and DP, providing a measurable quantity that connects two previously separate research threads (hallucination mitigation and privacy leakage). The CID formulation (Eq. 4) elegantly generalizes CAD through a single tunable parameter λ, enabling continuous interpolation between privacy-focused (λ < 1), standard (λ = 1), and hallucination-focused (λ > 1) decoding regimes.

3. **Theoretical grounding.** Theorem 3.1 establishes a clear upper bound on context influence (|λ × PMI|), rigorously formalizing the intuition that amplifying PMI to reduce hallucination must increase the model's sensitivity to context. The proof via convexity of log-sum-exp is technically sound.

4. **Comprehensive multi-factor empirical analysis.** The paper goes beyond a single tradeoff demonstration by systematically examining model capacity (125M-66B parameters), context size (32-2048 tokens), generation length (token positions 1-50), and token n-gram granularity (1-2048). This breadth provides practically useful guidance (e.g., first 10 tokens most influenced, optimal n-gram size ~128) that individual narrow studies cannot offer.

5. **Honest acknowledgment of limitations.** The paper explicitly states that CID with fixed λ does not achieve DP (ϵ = ∞) and that context influence is a lower-bound audit measure rather than a constructive DP mechanism. This transparency is commendable.

6. **Clear qualitative illustrations.** The example in Table 2 and the n-gram heatmap (Table 3) effectively communicate the verbatim regurgitation behavior to readers, making the abstract influence concept concrete.

## Weaknesses
1. **Non-constructive DP guarantee (Major).** Theorem 3.2 defines λ* = ϵ / (2·PMI), but PMI depends on the token yt that has not yet been generated. This makes Algorithm 1 an audit procedure rather than a practical generative mechanism. The paper acknowledges this indirectly ("this does not achieve DP since it could be ϵ=∞"), but the section 3.3 framing (titled "Context influence lower bounds privacy leakage") could mislead readers into thinking CID provides a practical DP guarantee during generation.

2. **Computational cost of context influence definition (Major).** Definition 3.1 requires a separate forward pass for every D' subset of interest. For n-gram analysis (Sec 4.4), this means O(|D|) forward passes per n-gram size. The paper limits to 100 contexts but does not discuss the computational wall, which limits the practical applicability of the metric for real-time auditing.

3. **Overclaimed practical recommendations (Major).** The Conclusion (Section 6) makes three prescriptive claims that go beyond the evidence: (a) placing sensitive information at the end of the prompt reduces influence—this may be confounded by information relevance; (b) adaptive privacy levels based on token position (Figure 4a) can be implemented—but no validation is provided; (c) "privatized tokens" are referenced as if CID provides privacy guarantees, which it does not (ϵ could be ∞).

4. **Missing statistical rigor (Moderate).** No variance, confidence intervals, or significance tests are reported despite N=1000 samples per setting. The improvements reported in Table 1 (e.g., ROUGE-L differences of 1-2 points) could be within noise range without CI reporting. The model size analysis (Figure 2) is described as "noisy" but no R² or correlation coefficient is provided.

5. **Causal attribution overreach in model size analysis (Moderate).** The interpretation that "larger models have larger capacity to memorize their pre-training data, so they can rely on their prior knowledge" (Page 7) conflates capacity with memorization. The 6.7B model is an unexplained outlier—it shows lower context influence than 13B and 30B, contradicting the capacity narrative. Alternative explanations (different training data, optimization dynamics, attention head utilization) are not considered.

6. **Restricted experimental scope (Moderate).** Only two datasets (CNN-DM, PubMedQA) and four model families are tested. The response length cap T=50 is short for abstractive summarization. Temperature sampling τ=0.8 is justified but not compared against other sampling strategies. The n-gram analysis is limited to only 100 contexts.

7. **Weak introduction narrative framing (Minor).** The introduction opens with ICL capability rather than the central privacy-hallucination tension, delaying the reader's understanding of the paper's core contribution. The first paragraph does not clearly establish the practical stakes (RAG systems leaking PII) before introducing technical details.

## Key Issues
### Issue 1 (Major): Non-constructive DP guarantee — Algorithm 1 cannot run before generation
**Location:** Page 4 - Section 3.3, Theorem 3.2 and Algorithm 1 (Page 14)

Theorem 3.2 defines λ* = ϵ / (2·PMI(pθ(yt; D, x, y<t))). However, PMI depends on yt, the token being generated. This creates a circular dependency: to set λ for generating yt, one must already know yt to compute PMI. Algorithm 1 (Bounded CID) takes yt as input, meaning it operates as a post-hoc audit check, not a generative mechanism. The paper partially acknowledges this (ϵ can be ∞ without pre-specification), but the structure of Section 3.3 and the title "Context influence lower bounds privacy leakage" suggest a stronger privacy connection than is technically supported.

**Required action:** Restructure Section 3.3 to clearly separate the post-hoc audit interpretation from any claim of constructive DP. Add a forward reference to Algorithm 1 as an audit procedure. Replace "tokens generated by CID can achieve DP" with "context influence provides a lower bound on what a DP mechanism would need to protect."

### Issue 2 (Major): Conclusion overclaims practical privacy guidance
**Location:** Page 10 - Section 6 (Discussion and Conclusion)

The conclusion makes three unvalidated recommendations: (1) place sensitive information at the end of prompts based on positional influence patterns, (2) adopt adaptive privacy levels (strict at start, relaxed later) based on Figure 4a, and (3) reference "privatized tokens" as if CID provides privacy guarantees. Claim (1) is confounded because earlier context positions may contain more relevant information (the paper acknowledges this but does not control for it). Claim (2) has no empirical or theoretical validation in the paper. Claim (3) is technically incorrect—CID without DP calibration does not produce privatized tokens.

**Required action:** Rewrite the conclusion to present these as open research directions requiring validation, not as established design principles. Add explicit caveats about the relevance-confound for positional claims.

### Issue 3 (Major): Missing statistical significance and variance reporting
**Location:** Page 5 - Table 1, Page 7 - Figure 2, throughout experimental section

All results are reported as point estimates without standard deviations, confidence intervals, or significance tests. The ROUGE-L differences between λ=1.0 and λ=1.5 are often small (e.g., LLaMA 3 on PubMedQA: 19.20 vs 18.79), making it impossible to assess whether observed patterns are statistically reliable. The model size analysis (Figure 2) is described as "noisy" but no goodness-of-fit or correlation measure is reported.

**Required action:** Compute and report 95% bootstrap confidence intervals for all main results (Table 1). Report at least 3 random seeds per setting. For model size analysis, report Spearman correlation or R².

### Issue 4 (Moderate): Model size analysis has confounded causal interpretation
**Location:** Page 7 - "Model size effect" paragraph

The claim that "larger models have larger capacity to memorize their pre-training data" conflates model capacity with actual memorization propensity. The 6.7B OPT model is a clear outlier (lower context influence than 13B), contradicting the monotonic trend narrative. Different OPT sizes may have different training data mixtures, optimization hyperparameters, or training horizons—none of which are controlled.

**Required action:** Acknowledge confounders explicitly. Report pre-training data overlap statistics for each model size with PubMedQA. Consider adding a control analysis using a model family with documented training data composition (e.g., Pythia or OLMo).

### Issue 5 (Moderate): Computational practicality of context influence metric
**Location:** Page 3 - Definition 3.1, Page 8 - Section 4.4

The definition requires O(|D|) forward passes per n-gram evaluation, limiting practical deployment. The n-gram analysis (Sec 4.4) can only process 100 contexts due to this cost. This scalability constraint should be presented as a limitation of the definition itself, not just a practical compromise.

**Required action:** Add a paragraph in Section 3.1 discussing the computational complexity of the definition and potential approximations (e.g., using influence functions or gradient-based attribution as cheaper alternatives).

## Actionable Suggestions
### S1: Restructure Section 3.3 to clearly separate audit from constructive DP (Must)
**Target:** Page 4, lines 73-99
**Action:** Replace the sentence "Since sampling from a probability distribution inherently induces privacy, it is not hard to show that tokens generated by CID can achieve DP" with: "Context influence provides a post-hoc lower bound on the privacy leakage of a generated token, following the auditing methodology of Jagielski et al. (2020). A constructive DP mechanism would require pre-specifying λ without knowledge of the future token yt, which is not feasible in the current framework."
**Expected benefit:** Prevents reader confusion about achievable DP guarantees.

### S2: Add variance reporting for all main results (Must)
**Target:** Table 1 and Figures 2-4
**Action:** Re-run all experiments with 3 random seeds. Report mean ± std in Table 1. Add error bars (95% CI via bootstrap) to Figures 2-4. For the model size analysis (Figure 2), report Spearman's ρ between model size and context influence, and note the 6.7B outlier explicitly.
**Expected benefit:** Allows readers to assess statistical reliability of observed patterns.

### S3: Rewrite Conclusion to bound claims (Must)
**Target:** Page 10, lines 59-74
**Action:** Replace the three prescriptive recommendations with conditional statements:
- "The positional pattern suggests that earlier context positions tend to have higher influence, but this may reflect inherent information relevance rather than position alone. Controlled experiments with randomized position assignment are needed to establish causality."
- "Token-level influence decay (Figure 4a) suggests potential for position-adaptive privacy strategies, but the current framework does not provide a constructive DP mechanism for implementing them."
- Remove the term "privatized tokens" entirely.
**Expected benefit:** Aligns claims with evidence, improves scientific credibility.

### S4: Add computational complexity discussion for Definition 3.1 (Nice-to-have)
**Target:** Page 3, after Definition 3.1
**Action:** Add: "Computational cost: for a context of length |D|, evaluating f_infl for all possible n-grams requires O(|D|) forward passes per n-gram size. For the full study, we limit n-gram evaluation to 100 randomly sampled contexts due to this cost. Developing more efficient approximations (e.g., gradient-based influence estimation) is left for future work."
**Expected benefit:** Transparency about definition's scalability.

### S5: Improve introduction narrative structure (Nice-to-have)
**Target:** Page 1, lines 82-87
**Action:** Restructure the first paragraph to open with the practical problem (RAG systems leaking PII while trying to reduce hallucination), then introduce the technical gap, then the proposed solution. See annotation on Page 1 for a Mentor Revised Version.
**Expected benefit:** Clearer communication of the paper's core contribution and stakes.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
- P1: ICL capability → context-conflicting hallucination
- P2: CAD mitigation → privacy risk (Figure 1)
- P3: Prior work on memorization vs context attribution → gap
- Contribution list

**Problem:** The narrative opens with ICL rather than the core privacy-hallucination tension. The reader does not understand until P2 that the paper is about the *tradeoff* between hallucination reduction and privacy leakage. The stakes (RAG systems, PII leakage) appear only in P2, too late for first-impression framing.

**Alignment Checks:**
- (a) Problem-solution alignment: The stated challenge (context-conflicting hallucination) → proposed solution (CID as measurement framework) is valid but underemphasizes the privacy dimension.
- (b) Variable alignment: Core concepts (context influence, PMI, λ) appear in both intro and method. ✓
- (c) Contribution-evidence alignment: The 10% ROUGE-L / 1.5x influence claim is directly from experiments. ✓

### Recommended Storyline (Option A — "Privacy-First Framing")

P1 (Stakes): "As LLMs are deployed in retrieval-augmented generation systems, they must summarize documents that may contain personally identifiable information. Two failure modes—hallucination and privacy leakage—are linked by a common mechanism: reliance on the context vs. prior knowledge."

P2 (Gap): "Prior work mitigates hallucination by amplifying context reliance (CAD), but this can increase the risk of regurgitating sensitive content. Simultaneously characterizing both risks is understudied."

P3 (Solution): "We propose context influence, a formal measure of how much an LLM's output depends on the provided context, and Context Influence Decoding (CID), a tunable framework that interpolates between context-only and prior-only decoding."

P4 (Contributions): List C1-C4 as in current paper.

### Alternative Storyline (Option B — "Measurement-First Framing")

P1: "Quantifying how much an LLM relies on provided context vs. its pre-training knowledge is critical for understanding hallucination, privacy, and faithfulness."

P2: "Existing metrics measure memorization of training data (requiring retraining) or provide attribution maps (interpretability, not quantification). We need a single inference-time measure."

P3: "We define context influence as the log-probability change when context is removed, and show it simultaneously bounds hallucination (via PMI) and privacy leakage (via DP)."

P4: + same as current.

### Abstract Outline (Complete — 5 Sentences)

**S1 (Problem):** LLMs in summarization tasks face a dual risk: hallucinating content that contradicts the context, and leaking private information by regurgitating it.

**S2 (Gap):** Prior work addresses these risks independently, leaving their interaction—amplifying context to reduce hallucination can worsen privacy leakage—uncharacterized.

**S3 (Method):** We formalize context influence as the log-probability change when context is removed, and propose Context Influence Decoding (CID), a tunable parameter λ that interpolates between prior-only (λ=0) and context-only (λ=1) decoding, with λ>1 amplifying context (CAD).

**S4 (Key Result):** On CNN-DM and PubMedQA, reducing hallucination via CAD (λ=1.5) increases context influence by up to 1.5× over regular decoding, with a 10% ROUGE-L gain for LLaMA 3.

**S5 (Scope):** We further characterize how model capacity, context size, generation length, and token n-grams shape this tradeoff, providing a framework for privacy-aware decoding design.

### Introduction Outline (Complete — 4 Paragraphs)

**P1 (Big Picture → Gap):** Open with the practical stakes of RAG systems handling sensitive documents. State the two risks (hallucination, privacy leakage) and the key insight that they share a mechanism. End with: "It is therefore critical to jointly characterize context influence under both reliability and privacy constraints."

**P2 (Prior Work → Limitation):** Review two threads: (a) PMI-based decoding for hallucination mitigation (CAD, DoLA) and (b) memorization/privacy literature. Point out that these threads have not been connected. "Prior memorization measures require training without a data point; context attribution methods focus on interpretability, not quantification."

**P3 (Proposed Solution → Evidence Preview):** "We bridge this gap with a formal definition of context influence (Def 3.1) grounded in PMI and DP, and introduce CID (Eq. 4) which generalizes CAD through a single tunable parameter λ. Theorem 3.1 shows context influence ≤ λ·PMI, formalizing the tradeoff."

**P4 (Contributions + Roadmap):** Same 4-point contribution list as current paper, but preceded by: "Our contributions are as follows:"

## Priority Revision Plan
### P0 (Must — Publication-Critical)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P0.1 | Non-constructive DP framing (Sec 3.3) | Rewrite to clearly separate audit from constructive DP. Remove "tokens generated by CID can achieve DP." Clarify Algorithm 1 as post-hoc audit. | Low (text edit) | High — Prevents misleading readers about DP guarantees |
| P0.2 | Conclusion overclaims (Sec 6) | Replace prescriptive recommendations with conditional statements. Remove "privatized tokens." Add explicit caveats about relevance confound for position claims. | Low (text edit) | High — Aligns claims with evidence |
| P0.3 | Missing variance/statistics (Table 1, Figs 2-4) | Add 95% CI via bootstrap or multi-seed std. Report at least 3 seeds for main results. | Medium (compute) | High — Enables reliability assessment |

### P1 (Must — Important for Credibility)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P1.1 | Model size analysis confounders (Sec 4.3) | Acknowledge confounders explicitly. Report pre-training data overlap. Note 6.7B outlier. | Low (text edit) | Medium — Improves scientific accuracy |
| P1.2 | Computational cost of Def 3.1 (Sec 3.1) | Add complexity analysis paragraph. Discuss potential approximations. | Low (text edit) | Medium — Transparency about scalability |
| P1.3 | Notational issues (Eq. 2, y_t typo) | Fix pθ(yt|x,yt) → pθ(yt|x,y<t). Distinguish CAD-modified distribution from original posterior in Eq. 2. | Low (text edit) | Low-Medium — Correctness |

### P2 (Nice-to-Have — Quality Improvement)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P2.1 | Introduction narrative (P1) | Restructure to open with privacy-hallucination tension rather than ICL (see Storyline Options). | Medium (rewrite) | Medium — Improves reader engagement |
| P2.2 | Qualitative example statistics (Table 2) | Add quantitative verbatim-copying metric (e.g., % of generated n-grams overlapping with context). | Medium (compute) | Medium — Strengthens qualitative claims |
| P2.3 | Response length T=50 constraint | Discuss potential truncation effects on ROUGE-L. | Low (text edit) | Low — Transparency |
| P2.4 | n-gram influence variance (Sec 4.4) | Report variance across 100 sampled contexts. | Low (compute) | Low — Rigor |

### Revision Order

1. **First pass (P0):** Fix DP framing, conclusion, and add variance reporting. These directly affect the paper's scientific validity and credibility.
2. **Second pass (P1):** Address model size analysis caveats, computational complexity, and notational fixes.
3. **Third pass (P2):** Improve narrative, add supporting experiments, and polish.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Context influence-hallucination tradeoff (Table 1) | PubMedQA + CNN-DM; OPT-1.3B, GPT-Neo-1.3B, LLaMA 3 8B, LLaMA 3 8B IT; λ=0.5,1.0,1.5 | E[f_infl], ROUGE-L, BERTScore, FactKB, AlignScore | λ=1.5 (CAD) increases influence 1.5-2× over RD; faithfulness improves | C2 (tradeoff), C3 (empirical) | No variance/CI; T=50 short; single seed |
| E2 | Qualitative generation examples (Table 2) | LLaMA 3 on CNN-DM; λ=0.5,1.0,1.5 | Qualitative comparison | CAD regurgitates verbatim; λ=0.5 uses broader terms | C3 (illustration) | Single example; no quantitative verbatim metric |
| E3 | Model size effect (Figure 2) | OPT 125M-66B on PubMedQA; λ=1.0 | E[f_infl], ROUGE-L, FactKB | Noisy trend; larger models less influenced; 6.7B outlier | C4 | Confounded by training data/hparams; no R² |
| E4 | Context size effect (Figure 3) | OPT-1.3B on PubMedQA; |D|=32-2048; λ=1.0 | E[f_infl], ROUGE-L, FactKB | Influence increases up to 256 tokens, then plateaus | C4 | Single model; synthetic truncation |
| E5 | Response length effect (Figure 4a) | OPT-1.3B on PubMedQA; token positions 1-50 | Per-position E[f_infl] | First 10 tokens most influenced | C4 | Confounds attention mechanism with context reliance |
| E6 | Token n-gram influence (Figure 4b,c) | OPT-1.3B on PubMedQA; n=1-2048; 100 contexts | E[f_infl] per n-gram | Bell curve centered at n=128; earlier tokens more influential | C4 | Only 100 contexts; no variance; no CI |
| E7 | Temperature effect (Figure 7, Appendix D) | OPT-6.7B on PubMedQA; τ=0-1; λ=1.0 | E[f_infl], ROUGE-L, FactKB | τ→0 increases influence exponentially; faithfulness drops at τ<0.4 | C4 | Single model |
| E8 | λ sweep (Figure 8, Appendix D) | OPT-1.3B on PubMedQA; λ=0-2 | E[f_infl], ROUGE-L, FactKB | Higher λ → more influence & faithfulness; similarity degrades at λ>1.25 | C2 | Single model |

### Research-Theme Gap Diagnosis

- **New knowledge:** The paper's core contribution is a novel *analytical* connection between context influence, PMI, and DP. This is conceptually new and well-supported. However, the novelty cannot be fully assessed without external literature comparison (Retrieval-Disabled Mode).
- **Reproducibility:** The experimental setup is well-documented (datasets, models, hyperparameters, evaluation code from Xu 2023). Major gaps: no random seeds reported, no variance estimates, temperature sampling details (τ=0.8) but no comparison with top-p/k.
- **Impact on practice/understanding:** The paper provides useful descriptive observations (positional effects, n-gram size) but the prescriptive claims in the conclusion are not yet validated. The practical impact would be significantly strengthened by a controlled validation of the proposed design recommendations.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: Controlled causal test of position effect
- **Target Claim:** "Earlier context information influences LLMs more than later information" (C4, §4.4)
- **Hypothesis:** The observed positional gradient is caused by position, not by the higher relevance of earlier information.
- **Minimal Design:** Take 100 PubMedQA contexts. Randomly permute the order of sentences within each context. Measure E[f_infl] per position before and after permutation. If the positional gradient persists after randomization, it supports a position effect; if it disappears, the original pattern was driven by relevance.
- **Controls/Baselines:** Same model (OPT-1.3B), same λ=1.0, same N=1000 responses.
- **Metrics:** E[f_infl] per position bin (1-32, 33-64, ...); compare original vs. permuted.
- **Success Criterion:** Statistically significant (p<0.05) difference in positional gradients between original and permuted conditions.
- **Estimated Cost:** ~2 GPU-hours (only requires forward passes on permuted contexts).
- **Expected Gain:** Validates or refutes a central practical claim; high impact on paper credibility.

#### P1 Experiment: Verbatim copying quantification
- **Target Claim:** "CAD increases regurgitation of context" (C3, qualitative)
- **Hypothesis:** The fraction of generated tokens that overlap verbatim with the context increases with λ.
- **Minimal Design:** For all N=1000 responses per λ setting in Table 1, compute the proportion of generated token n-grams (n=4,8,16) that appear verbatim in the source context D. Report E[overlap] per λ.
- **Controls:** Same datasets, models, and decoding settings.
- **Metrics:** % of generated 4-grams/8-grams that overlap with context; Jensen-Shannon divergence between generated and context token distributions.
- **Success Criterion:** Statistically significant monotonic increase in overlap with λ.
- **Estimated Cost:** ~0.5 GPU-hour (text processing only, no forward passes).
- **Expected Gain:** Replaces qualitative claim with quantitative evidence; directly links context influence to regurgitation risk.

#### P2 Experiment: Multi-seed reproducibility
- **Target Claim:** All numerical results in Table 1 and Figures 2-4
- **Hypothesis:** Reported patterns are reproducible across random seeds.
- **Minimal Design:** Repeat the three main λ settings (0.5, 1.0, 1.5) for LLaMA 3 on CNN-DM with 5 random seeds. Compute mean ± std for E[f_infl], ROUGE-L, FactKB.
- **Controls:** Identical preprocessing and hyperparameters.
- **Metrics:** Coefficient of variation (CV) across seeds for each metric.
- **Success Criterion:** CV < 10% for all metrics at all λ settings.
- **Estimated Cost:** ~5 GPU-hours.
- **Expected Gain:** Essential for statistical credibility of all reported trends.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Week 1): Position causality test
  [Permute context sentences]
      → [Measure per-position influence]
      → [Compare original vs permuted gradients]
      → [Validate/reject position effect claim]

P1 (Week 2): Verbatim overlap quantification
  [Compute generated n-gram overlap with context]
      → [Stratify by λ]
      → [Report E[overlap] + CI]
      → [Quantify regurgitation risk]

P2 (Week 3): Multi-seed reproducibility
  [Run 5 seeds for LLaMA 3 on CNN-DM]
      → [Report mean±std for all metrics]
      → [CV < 10% check]
      → [Final statistical validation]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Scoring Rationale

The paper addresses a timely and important problem (privacy-hallucination tradeoff in LLM summarization) with a clean formal framework and comprehensive multi-factor empirical analysis. However, the score is constrained by several factors:

- **Research value/novelty (primary dimension):** The conceptual contribution—linking context influence, PMI, and DP—is solid and well-motivated. However, full novelty assessment requires external literature comparison that is unavailable in this run (Retrieval-Disabled Mode). The paper builds directly on CAD (Shi et al., 2023) and PMI-based decoding (Van der Poel et al., 2022), positioning itself as a synthesis/extension rather than a breakthrough. Deferred novelty verification is needed.

- **Validity/soundness:** The theoretical results (Theorem 3.1, Theorem 3.2) are technically sound given stated assumptions, but Theorem 3.2 has a non-constructive limitation that reduces its practical significance. The empirical analysis is broad but lacks statistical rigor (no variance, no CIs, no significance tests). The conclusion overclaims relative to available evidence.

- **Reproducibility:** The experimental setup is well-documented, but missing random seed reporting, variance estimates, and code release details limit full reproducibility.

**Final Score: 6/10**

This reflects a paper with a solid conceptual contribution and broad empirical analysis, held back by (a) a non-constructive DP framing, (b) lack of statistical rigor in experimental reporting, (c) overclaimed practical recommendations, and (d) deferred novelty verification.

**Post-Revision Target: [7, 8]/10**

If the authors address all P0 and P1 items (restructure DP framing, add variance reporting, rewrite conclusion to bound claims, acknowledge confounders, add computational complexity discussion), the paper could achieve 7-8/10. Reaching 8 would additionally require the P0 experiment (controlled position causality test) and P1 experiment (verbatim copying quantification) to strengthen the practical claims.

| Score Component | Current | Post-Revision Target |
|----------------|---------|---------------------|
| Research Value / Novelty | 6 | 7-8 (pending literature comparison) |
| Validity / Soundness | 6 | 7 (with CI and conclusion rewrite) |
| Reproducibility | 5 | 7 (with seeds and variance) |
| Clarity / Presentation | 7 | 8 (with intro rewrite) |
| Practical Impact | 5 | 7 (with validated recommendations) |

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: Privacy-hallucination tradeoff in LLM summarization]
    │
    ├── C1: Context influence definition (Def 3.1)
    │       └── Evidence: Formal derivation from P-XCMI + DP
    │
    ├── C2: CID framework + analytical bound (Thm 3.1)
    │       └── Evidence: Proof via convexity of log-sum-exp
    │       └── Gap: Thm 3.2 non-constructive (circular dependency on yt)
    │
    ├── C3: Empirical tradeoff demonstration (Table 1)
    │       └── Evidence: 10% ROUGE-L gain ↔ 1.5× influence increase
    │       └── Gap: No variance/CIs; single seed
    │
    └── C4: Multi-factor characterization (Figs 2-4)
            └── Evidence: Model size, context size, position, n-gram effects
            └── Gap: Model size confounded; position effect may be relevance artifact

[Core Defect Board - Top 5]
1. Non-constructive DP guarantee (Severity: Major, Validity Risk: High, Fixable: Yes)
2. Conclusion overclaims (Severity: Major, Validity Risk: Medium, Fixable: Yes)
3. Missing statistical rigor (Severity: Moderate, Validity Risk: High, Fixable: Yes)
4. Model size causal overreach (Severity: Moderate, Validity Risk: Medium, Fixable: Yes)
5. Computational practicality unstated (Severity: Minor, Validity Risk: Low, Fixable: Yes)
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Non-constructive DP framing (P0.1)]
    → [Reword Sec 3.3: audit vs constructive separation]
    → [Expected: Clearer scientific communication]

[Conclusion overclaims (P0.2)]
    → [Replace prescriptive with conditional claims]
    → [Remove "privatized tokens"]
    → [Expected: Evidence-claim alignment]

[Missing variance/statistics (P0.3)]
    → [Add bootstrap CIs + 3 seeds]
    → [Expected: Statistical credibility]

[Model size confounders (P1.1)]
    → [Acknowledge confounders + 6.7B outlier]
    → [Expected: Scientific accuracy]

[Computational cost (P1.2)]
    → [Add complexity paragraph]
    → [Expected: Transparency]
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Context Influence in LLM Summarization (Root)
├── Branch 1: Hallucination Mitigation
│   ├── Leaf 1.1: PMI-based decoding (CAD, DoLA)
│   │   └── Van der Poel et al. 2022, Shi et al. 2023
│   ├── Leaf 1.2: Contrastive decoding
│   │   └── Li et al. 2022, Chuang et al. 2023
│   └── Leaf 1.3: Fine-tuning for factuality
│       └── Zhu et al. 2020, Cao et al. 2018
├── Branch 2: Memorization & Privacy
│   ├── Leaf 2.1: Training data extraction
│   │   └── Carlini et al. 2019, 2021, 2022
│   ├── Leaf 2.2: Counterfactual memorization
│   │   └── Feldman & Zhang 2020, Zhang et al. 2023
│   └── Leaf 2.3: Context-level DP
│       └── Wu et al. 2023, Tang et al. 2023, Duan et al. 2024
└── Branch 3: Context Attribution
    ├── Leaf 3.1: Interpretability-based
    │   └── Fernandes et al. 2021, Sarti et al. 2023
    └── Leaf 3.2: Inference-time influence (This paper)
        └── Context influence (Def 3.1) + CID (Eq. 4)
```