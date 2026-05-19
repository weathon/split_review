## Summary
# Final Review Report

## Summary

This paper presents Raidar, a method for detecting AI-generated text by prompting an LLM to rewrite the input and measuring the character-level editing distance between the original and rewritten output. The core insight is that LLMs tend to modify AI-generated text less than human-written text, which the authors attribute to the lower perplexity of AI text under the same autoregressive distribution. Raidar operates on discrete token outputs only (no log probabilities needed), making it compatible with black-box API LLMs like GPT-3.5 and GPT-4.

The method is evaluated on six datasets (News, Creative Writing, Student Essay, Code, Yelp Reviews, Arxiv Abstracts) spanning diverse domains, using F1 score as the primary metric. Raidar outperforms existing detectors including DetectGPT and Ghostbuster in most settings, with in-domain F1 gains ranging from roughly 5–29 points. Cross-model experiments show the detector generalizes across generator models (Ada, Davinci, GPT-3.5, GPT-4, LLaMA 2), and multi-prompt training provides some robustness against adaptive rephrasing attacks.

**Strengths:** The idea of using rewriting edit distance as a detection signal is intuitive and well-motivated. The approach addresses a genuine practical need (black-box API compatibility). The evaluation is broad across domains and generator models.

**Core Weaknesses:** (1) Claims about robustness are overstated — single-prompt detectors collapse under adaptive attacks (F1 drops from 95.38 to 25.64), and multi-prompt training introduces domain-dependent trade-offs. (2) The causal mechanism linking "low perplexity" to "fewer edits" is assumed rather than verified. (3) The "equivariance" terminology is mathematically imprecise and the uncertainty formula lacks pairwise normalization. (4) The code detection data pipeline introduces a specification-reinterpretation confound. (5) No limitations section is provided. Novelty comparison is deferred due to external retrieval being unavailable in this run.

## Strengths
1. **Conceptually clean and practical detection paradigm.** The core idea — using LLM rewriting edit distance as a detection signal — is intuitive, easy to understand, and directly addresses the practical constraint that many state-of-the-art LLMs (GPT-3.5, GPT-4) only provide black-box API access without token-level probabilities. This makes Raidar applicable in settings where probability-based detectors like DetectGPT and Ghostbuster cannot be deployed.

2. **Broad empirical evaluation across diverse domains.** The paper evaluates on six datasets spanning news articles, creative writing, student essays, code, business reviews, and academic abstracts. This breadth strengthens the claim that the rewriting discrepancy is a general phenomenon rather than an artifact of a single domain.

3. **Cross-generator generalization analysis.** Table 4 systematically evaluates the detector on text from five different generator models (Ada, Text-Davinci-002, GPT-3.5-turbo, GPT-4-turbo, LLaMA 2) using a fixed rewriting model. The strong in-distribution performance (80.00–98.46 F1) and reasonable OOD generalization demonstrate that the method is not tied to a specific generator.

4. **Prompt sensitivity analysis.** Figure 6 provides useful insight into how different rewriting prompts affect detection performance. This analysis is valuable for practitioners who need to select effective prompts, and it honestly reveals that no single prompt is universally optimal.

5. **Honest human study in Appendix A.4.** The human evaluation (Table 8) showing that machine-generated text is preferred only 26.7% of the time on Arxiv abstracts (vs. 53.3% on Yelp reviews) is a candid admission that the "high quality" assumption has limits. This nuance is welcome and should be incorporated into the main text's framing.

## Weaknesses
1. **Overclaimed robustness against adaptive attacks (Page 7 – Table 3, Page 2 – Contribution Paragraph).** The introduction claims "our detection remains robust even when the text generation is aware of our detection mechanism," but Table 3 shows that single-prompt detectors suffer catastrophic degradation under adaptive rephrasing — Code F1 drops from 95.38 to 25.64 (a 73% collapse). The method only regains robustness after multi-prompt training, which itself introduces a domain-dependent trade-off (Yelp non-adaptive F1 drops from 87.75 to 58.04). The current narrative understates this fragility.

2. **Unverified causal mechanism (Page 1 – Abstract, Page 3 – Section 3.1).** The paper attributes the editing discrepancy to LLMs "perceiving AI-generated text as high-quality" with "inherently lower loss." However, no experiment directly measures perplexity or loss to confirm this causal link. The observed correlation (lower edit distance for AI text) could alternatively be explained by stylistic homogeneity, lower lexical diversity, or statistical regularity in AI text that makes rewriting easier regardless of quality. The "high quality" framing should be softened to "distributional alignment."

3. **Mathematical imprecision in signal definitions (Page 3 – Section 3.1, Page 5 – Section 3.2).** (a) The "equivariance" measurement $L = D(F(T^{-1}, F(p, F(T, x))), F(p, x))$ measures cycle consistency, not mathematical equivariance. This could confuse readers with a formal background. (b) The uncertainty formula $U = \sum_{i=1}^{K-1} \sum_{j=i}^{K} D(x'_i, x'_j)$ is unnormalized by the number of pairs $\binom{K}{2}$, making it dependent on $K$. (c) The Levenshtein ratio formula is missing a closing parenthesis: $max(len(s_k), len(x))$. (d) The bag-of-words edit does not specify the value of $n$ (unigrams? bigrams?), preventing exact reproducibility.

4. **Missing limitations section (Page 9 – Conclusion).** The conclusion lists no limitations despite the method having several: vulnerability to adaptive attacks without multi-prompt training, prompt sensitivity, cost of API calls for rewriting, and potential bias toward longer texts (acknowledged in Figure 5 but not critically discussed).

5. **Confounded code detection data pipeline (Page 13 – Appendix A.1).** AI-generated code is produced via a two-step process: GPT first describes the HumanEval specification, then generates code from its own description. This means the AI code solves a GPT-interpreted specification rather than the original specification that humans used. The observed detection advantage could partly stem from this specification reinterpretation gap rather than from the AI generation itself.

6. **Data quality concerns for detection benchmarks (Page 6 – Table 1).** The Student Essay dataset has a large size imbalance (22,172 human vs. 13,629 machine) and human-written samples come from the British Academic Written English corpus while machine-generated ones use a different generation process. Without explicit confirmation that the two sets are matched on topic, writing prompt, and difficulty, detection accuracy could be inflated by topical confounds rather than genuine generation signals.

7. **No significance testing or variance reporting.** All F1 scores in Tables 1–5 are reported as point estimates without confidence intervals, standard deviations, or significance tests. Given that many gains are modest (e.g., 5–8 points in some settings), the statistical reliability of the ranking is unclear.

8. **Lack of dedicated discussion on API cost and latency.** The method requires at least one LLM API call per input (and more for equivariance/uncertainty). For real-world deployment at scale, this introduces non-trivial cost and latency that are not discussed or compared against the cost of probability-based methods.

## Key Issues
### Issue 1: Disconnect between robustness claims and experimental evidence (SEVERITY: HIGH)
- **Location:** Page 1 – Abstract, Page 2 – Introduction (contribution paragraph), Page 7 – Table 3, Page 9 – Conclusion
- **Problem:** The paper repeatedly claims robustness to detection-aware generation, but single-prompt detectors collapse under adaptive attacks (Code: 95.38 → 25.64 F1). Multi-prompt training recovers robustness but at a cost (Yelp: 87.75 → 58.04 on non-adaptive text). These trade-offs are not discussed in the abstract or conclusion.
- **Fix:** Qualify all robustness claims to distinguish single-prompt (fragile) vs. multi-prompt (conditionally robust) settings. Add a paragraph explicitly discussing the robustness–standard-accuracy trade-off.

### Issue 2: Causal mechanism is asserted without verification (SEVERITY: HIGH)
- **Location:** Page 1 – Abstract, Page 3 – Section 3.1
- **Problem:** The claim that LLMs edit AI text less because it has "inherently lower loss" is stated as an explanation, but no perplexity/loss measurements are reported. The human study (Appendix A.4, Table 8) actually shows that humans do *not* consistently prefer machine-generated text (only 26.7% for Arxiv), which weakens the "high quality" narrative.
- **Fix:** Replace causal certainty ("because LLMs often perceive AI-generated text as high-quality") with correlational language ("consistent with the hypothesis that"). Report perplexity measurements for at least one dataset to support the mechanism claim, or explicitly state it as a hypothesis requiring further study.

### Issue 3: Mathematical errors and ambiguities in method definitions (SEVERITY: MEDIUM)
- **Location:** Page 3 – Section 3.1 (equivariance), Page 5 – Section 3.2 (uncertainty, Levenshtein ratio)
- **Problem:** (a) "Equivariance" is misused — the paper measures cycle consistency, not equivariance. (b) Uncertainty formula unnormalized by $\binom{K}{2}$. (c) Levenshtein ratio formula missing closing parenthesis. (d) Bag-of-words edit unspecified for $n$.
- **Fix:** Rename "equivariance" to "cycle consistency" or "transformation consistency." Normalize uncertainty by $\binom{K}{2}$. Fix typographical errors. Specify $n=1$ (unigrams) for bag-of-words.

### Issue 4: Missing limitations section (SEVERITY: MEDIUM)
- **Location:** Page 9 – Conclusion
- **Problem:** The conclusion discusses only positive results. No limitations are acknowledged despite several being evident (adaptive attack vulnerability, API cost, prompt sensitivity, data confounds for code detection).
- **Fix:** Add a limitations paragraph explicitly addressing: (a) adaptive attack vulnerability without multi-prompt training, (b) dependency on rewriting LLM quality, (c) API cost for real-time detection, (d) potential confounds in the code detection data pipeline.

### Issue 5: Code detection data pipeline confound (SEVERITY: MEDIUM)
- **Location:** Page 13 – Appendix A.1 (Code Dataset)
- **Problem:** AI-generated code is produced by first having GPT describe the HumanEval specification, then regenerate code from that description. This two-step reinterpretation introduces a specification gap — human code solves the original spec, AI code solves a GPT-interpreted spec. Detection gains may partly reflect this interpretation difference rather than AI generation per se.
- **Fix:** Generate AI code directly from the original HumanEval specification in a single step, or control for specification reinterpretation by having humans also code from GPT-generated descriptions. Add a note acknowledging this potential confound.

## Actionable Suggestions
### S1: Restructure robustness claims (Must)
- **Location:** Page 1 – Abstract, Page 2 – Introduction, Page 9 – Conclusion
- **Action:** Replace "inherently robust on new content" and "our detection remains robust even when the text generation is aware of our detection mechanism" with bounded claims that distinguish single-prompt (fragile) vs. multi-prompt (conditionally robust) settings.
- **Mentor Revised Version for Abstract:** "Our detection is compatible with black-box LLMs. Under single-prompt training, Raidar achieves strong in-domain detection but is vulnerable to adaptive rephrasing attacks; multi-prompt training substantially mitigates this vulnerability, though with a domain-dependent trade-off."

### S2: Add perplexity verification experiment (Must)
- **Location:** Page 3 – Section 3.1
- **Action:** For at least one dataset (e.g., Yelp), report the average perplexity/loss of human vs. AI-generated text under the rewriting LLM. Show a scatter plot of perplexity vs. edit distance to verify the assumed monotonic relationship.
- **Expected benefit:** Directly supports the core hypothesis and distinguishes between "lower perplexity → fewer edits" (causal) and "AI text is statistically more predictable" (correlational).

### S3: Fix mathematical and terminological errors (Must)
- **Location:** Page 3 – Section 3.1, Page 5 – Section 3.2
- **Action:**
  - Rename "Equivariance" to "Cycle Consistency" throughout the paper, including Figures 2 and 4.
  - Normalize the uncertainty formula: $U = \frac{2}{K(K-1)} \sum_{i=1}^{K-1} \sum_{j=i+1}^{K} D(x'_i, x'_j)$
  - Fix the missing parenthesis in the Levenshtein ratio: $D_k(x, s_k) = 1 - \frac{\text{Levenshtein}(s_k, x)}{\max(\text{len}(s_k), \text{len}(x))}$
  - Specify $n=1$ (unigrams) for bag-of-words edit, or clarify the exact $n$ used.

### S4: Add limitations paragraph (Must)
- **Location:** Page 9 – Conclusion
- **Action:** Insert a dedicated limitations paragraph covering: (a) adaptive attack vulnerability without multi-prompt training, (b) API cost of rewriting calls, (c) prompt sensitivity, (d) data confounds in code detection, (e) unverified causal mechanism.

### S5: Report statistical significance (Nice-to-have)
- **Location:** Page 6 – Tables 1 and 2
- **Action:** Add confidence intervals (e.g., bootstrapped 95% CI) or standard deviations for all F1 scores. At minimum, report results over 3+ random seeds for the classifier training step. This is especially important for settings where Raidar's gain over baselines is small (e.g., News dataset: 60.29 vs. 54.74 for GPT Zero-Shot).

### S6: Control for code specification confound (Must)
- **Location:** Page 13 – Appendix A.1
- **Action:** Regenerate the AI code dataset using a single-step prompt directly from the original HumanEval specification (e.g., "Write a Python function that [specification]"). Re-run the Code detection experiment and compare results. Report both the original and corrected numbers.

### S7: Discuss API cost and latency (Nice-to-have)
- **Location:** Page 6 – Section 4 or Page 9 – Conclusion
- **Action:** Add a brief paragraph or table quantifying: (a) number of API calls per detection (1 for invariance, 3+ for equivariance, K for uncertainty), (b) approximate cost per 1000 detections using GPT-3.5-turbo pricing, (c) average latency per detection. Compare these to the cost of probability-based methods where applicable.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current title "RAIDAR: GENERATIVE AI DETECTION VIA REWRITING" identifies the method but does not communicate the problem framing or the key insight (invariance discrepancy). The introduction follows this structure: (P1) Risks of LLMs → (P2) Prior detection limitations → (P3) Raidar presented → (P4) Key hypothesis + results preview.

**Problem:** The introduction front-loads risks (P1) before establishing the detection challenge as a *technical* problem. P2 covers prior work limitations well, but P4's key hypothesis is slightly vague (conflates quality with distribution alignment). The abstract uses causal language that overstates evidence.

### Recommended Storyline (Option A — Problem-First)

**New Title:** "Raidar: Detecting AI-Generated Text by Measuring LLM Rewriting Edit Distance"

**Abstract Outline (4 sentences):**
- **S1 (Problem):** "Detecting AI-generated text is critical for mitigating risks in education, journalism, and online platforms, but existing detectors require access to internal model log-probabilities unavailable in black-box APIs."
- **S2 (Observation):** "We observe that LLMs systematically produce fewer character-level edits when rewriting AI-generated text compared to human-written text, a discrepancy we attribute to distributional alignment rather than quality perception."
- **S3 (Method):** "We introduce Raidar, which prompts an LLM to rewrite input text and uses the normalized Levenshtein edit distance as a classification feature, requiring only discrete token outputs."
- **S4 (Results + bound):** "Across six domains and five generator models, Raidar improves F1 scores by 5–29 points over existing methods under in-domain evaluation, and multi-prompt training provides robustness against adaptive rephrasing attacks—though detection-aware generation remains a challenge."

**Introduction Outline (4 paragraphs):**
- **P1 (Big Picture + Gap):** "The rapid adoption of LLMs has created an urgent need for reliable AI-text detection, especially in education, cybersecurity, and academic publishing. However, the most effective current methods [DetectGPT, Ghostbuster] rely on token-level log probabilities that are inaccessible through black-box APIs like GPT-3.5 and GPT-4. This access gap means that many real-world detection scenarios remain unaddressed by existing tools."
- **P2 (Prior Work + Limitations):** Summarize probability-based detectors (DetectGPT, Ghostbuster) and watermarking, emphasizing the black-box API limitation. Note that perturbation-based methods (DetectGPT) are zero-shot but require model access, while feature-based methods (Ghostbuster) need generated documents from the target model.
- **P3 (Our Insight):** "We hypothesize that text generated by an autoregressive LLM occupies a region of the distribution that a second LLM will assign relatively low perplexity to. When prompted to rewrite the input, the LLM therefore makes fewer structural changes to AI-generated text than to human-written text. This rewriting discrepancy can be measured using only character-level edit distance—no internal model access required."
- **P4 (Our Method + Results):** "We operationalize this insight through Raidar, which computes the normalized Levenshtein distance between an input and its LLM-rewritten version as a detection feature. Across six diverse datasets, Raidar achieves F1 scores of 60–95%, outperforming prior methods by 5–29 points. Multi-prompt training further provides conditional robustness against adaptive attacks, though we discuss limitations where detection remains vulnerable."

### Alternative Storyline (Option B — Method-First)

**Title:** "Black-Box AI Text Detection via Rewriting Invariance"
**Structure:** Start with a concrete example (Figure 1) of the rewriting discrepancy, then motivate why this happens, then contrast with existing methods, then present results. This narrative is more accessible for practitioner audiences.

### Alignment Checks

| Check | Current Storyline | Option A | Option B |
|---|---|---|---|
| Problem-Method Alignment | Adequate but gap not precisely stated | Strong — explicitly ties black-box access gap to method design | Moderate — method first, problem second |
| Variable Alignment | Core terms (invariance, rewriting, edit distance) appear in method | Consistent | Consistent |
| Claim-Evidence | Robustness claims overreach | Bounded claims match evidence | Bounded claims match evidence |

**Recommended:** Option A for submission; its problem-first structure better frames the contribution.

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before resubmission)

| ID | Task | Effort | Impact | Location |
|---|---|---|---|---|
| P0.1 | Add limitations paragraph | Low | High | Page 9 – Conclusion |
| P0.2 | Correct risk framing of robustness claims | Low | High | Pages 1, 2, 9 |
| P0.3 | Fix mathematical errors (equivariance name, uncertainty normalization, parenthesis) | Low | Medium | Pages 3, 5 |
| P0.4 | Control for code data generation confound | Medium | High | Page 13 – Appendix A.1 |

### P1 — High Priority (Should fix for strong revision)

| ID | Task | Effort | Impact | Location |
|---|---|---|---|---|
| P1.1 | Add perplexity verification experiment | Medium | High | Page 3 – Section 3.1 |
| P1.2 | Replace causal "high quality" language with distributional framing | Low | Medium | Pages 1, 3 |
| P1.3 | Report confidence intervals or significance tests for key F1 scores | Medium | Medium | Page 6 – Tables 1, 2 |
| P1.4 | Restructure related work around comparative axes | Low | Medium | Page 2 – Section 2 |
| P1.5 | Discuss API cost and latency | Low | Medium | Page 6 or 9 |

### P2 — Quality Improvement (Nice-to-have)

| ID | Task | Effort | Impact | Location |
|---|---|---|---|---|
| P2.1 | Reproduce Section 3.2 bag-of-words with explicit $n$ | Low | Low | Page 5 |
| P2.2 | Add human study results to main text discussion | Low | Low | Page 3 or 8 |
| P2.3 | Expand intro paragraph 1 to focus on detection challenge | Low | Low | Page 1 – Introduction |
| P2.4 | Compare with DetectGPT's zero-shot advantage fairly | Low | Low | Page 2 – Related Work |

```text
ASCII Diagram — Revision Strategy Roadmap

[Overclaimed robustness]
    → Fix: Bound claims (single vs multi-prompt)
    → Expected: Accurate contribution framing

[Unverified causal mechanism]
    → Fix: Add perplexity experiment + soften language
    → Expected: Supported core hypothesis

[Math errors (equivariance, uncertainty, formula)]
    → Fix: Rename + normalize + correct typo
    → Expected: Precise technical definitions

[Missing limitations]
    → Fix: Add dedicated paragraph in Conclusion
    → Expected: Complete, honest paper structure

[Code data confound]
    → Fix: Single-step generation + re-run detection
    → Expected: Cleaner experimental evidence
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | In-domain detection (Table 1) | 6 datasets, logistic regression/XGBoost on edit distance features | F1 score | Raidar (Invariance) achieves 60.29–95.38 F1, best in 5/6 datasets | C1 (invariance works), C2 (symbolic detection) | No variance/CI reported; baseline comparisons not all matched on train data |
| E2 | Out-of-domain detection (Table 2) | Train on one domain, test on another (3 domains) | F1 score | Raidar outperforms Ghostbuster by 2–22 points | C1, C2 (generalization) | Only 3 domains; single train/test pair per domain |
| E3 | Adaptive attack robustness (Table 3) | Single vs multi-prompt training; 2 adaptive rephrase prompts | F1 score | Single-prompt: catastrophic drops (95→25). Multi-prompt: recovers to 87–93 | C1 (conditionally robust) | Yelp trade-off unexplained; adaptive prompts are limited to 2 variants |
| E4 | Cross-generator detection (Table 4) | 5 generator models, ID and OOD settings | F1 score | ID: 80–98 F1. OOD: 49–91 F1 | C2 (cross-model compatibility) | Rewriting LLM is fixed (GPT-3.5); no test with different rewriting LLMs for same generator |
| E5 | Rewriting LLM comparison (Table 5) | 4 rewriting LLMs (Ada, Davinci, GPT-3.5, LLaMA 2) | F1 score | GPT-3.5 turbo best on 5/6 datasets | C2 (rewriting model matters) | No analysis of why larger models help |
| E6 | Prompt sensitivity (Figure 6) | 5–7 prompts per dataset | F1 score | Performance varies significantly by prompt | C1 (prompt matters) | No systematic prompt optimization analysis |
| E7 | Length analysis (Figures 5, 7–9) | Binned input lengths | F1 score | Longer inputs generally improve detection | C1 (auxiliary analysis) | Some datasets show non-monotonic trends (Student Essay, Code) not explained |
| E8 | Non-native speaker fairness (Table 10) | Train on Arxiv/ASAP, test on ASAP | F1 score | 81.16 (cross-training), 98.76 (in-domain) | C2 (fairness) | Only 200 samples; only one non-native dataset |
| E9 | Feature combination (Table 13) | Combine invariance + equivariance + uncertainty | F1 score | Combined worse than single on 2 datasets | C1 (individual signals suffice) | Only 2 datasets tested; no statistical test |

### Research-Theme Gap Diagnosis

- **New Knowledge (partial):** The core insight — LLMs edit AI text less during rewriting — is empirically demonstrated but the causal mechanism is unverified. The paper does not establish *why* this happens, only that it does.
- **Reproducibility (partial):** The method is conceptually simple, but bag-of-words $n$ is unspecified, classifier hyperparameters are minimal, and no seed-based variance is reported.
- **Impact on Practice (moderate):** Black-box compatibility is practically valuable, but the API cost and latency trade-offs are not quantified, limiting deployment guidance.

### Proposed Research Experiments

| ID | Target Claim | Hypothesis | Minimal Design | Control/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|---|---|---|---|---|---|---|---|---|
| P0-Exp1 | Causal link: perplexity → edit distance | Edit distance is positively correlated with perplexity of input under rewriting LLM | Compute GPT-3.5 perplexity for 500 human + 500 AI Yelp reviews; plot vs edit distance | Spearman correlation | Correlation coefficient $r$, scatter plot | $r > 0.3$ with $p < 0.01$ | Low (1 day) | Supports core claim with direct evidence |
| P0-Exp2 | Code detection confound correction | Direct-generation AI code will show reduced but still positive detection vs human code | Generate AI code via single-step prompt from original HumanEval spec; re-run Code detection | Original two-step vs one-step AI data | F1 difference, $\Delta$F1 | $\Delta$F1 < 10 points (method still works) | Medium (2 days) | Removes confound; strengthens code experiment |
| P1-Exp3 | Multi-prompt training trade-off analysis | The Yelp performance drop under multi-prompt training is systematic and correlates with prompt diversity | Analyze Yelp data by rewriting prompt; measure inter-prompt edit distance distributions | Single-prompt baseline | Per-prompt F1, inter-prompt feature variance | Identifiable cause for Yelp drop | Low (1 day) | Explains Table 3 anomaly |
| P1-Exp4 | Statistical significance of F1 gains | Raidar's gains over Ghostbuster are statistically significant | Bootstrap 95% CIs for Table 1 scores (1000 resamples) | Ghostbuster confidence intervals | CI overlap, $\Delta$F1 significance | Non-overlapping CIs for key comparisons | Low (0.5 day) | Quantifies result reliability |
| P2-Exp5 | Black-box adversarial attack robustness | Raidar is more robust to black-box attacks than probability-based methods | Test against 2 black-box attack methods (e.g., textfooler, genetic algorithm) | DetectGPT, Ghostbuster under same attacks | F1 drop under attack | Smaller relative F1 drop than baselines | Medium (3 days) | Strengthens robustness claims |

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

P0 (Pre-Submission Critical)
├── P0-Exp1: Perplexity-Edit Distance Correlation [Low cost, High impact]
│   └── Verify core causal hypothesis
├── P0-Exp2: Single-Step Code Generation [Medium cost, High impact]
│   └── Remove specification confound
│
P1 (Strong Revision)
├── P1-Exp3: Yelp Multi-Prompt Trade-off Analysis [Low cost, Medium impact]
├── P1-Exp4: Bootstrap CI for Table 1 [Low cost, Medium impact]
│
P2 (Quality Improvement)
└── P2-Exp5: Black-Box Adversarial Attack Test [Medium cost, Medium impact]
    └── Strengthen robustness narrative
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Reasoning:* The paper presents a creative and practically motivated detection paradigm with broad empirical evaluation. The core idea (rewriting edit distance as detection signal) is intuitive and addresses a genuine need (black-box API compatibility). However, the score is held back by: (1) overclaimed robustness that is contradicted by the paper's own Table 3 data, (2) unverified causal mechanism presented as established fact, (3) mathematical imprecision in key signal definitions, (4) missing limitations section, and (5) a confounded code detection pipeline. The research value is moderate — the method is practical but the scientific understanding of *why* it works remains shallow. Novelty position cannot be fully assessed without external literature retrieval, which was unavailable in this run.

**Post-Revision Target: [7.0, 7.8] / 10**

*Reasoning:* If the authors address all P0 and P1 items (add limitations, fix robustness claims, correct mathematical errors, add perplexity verification experiment, control for code confound, add confidence intervals), the paper would significantly improve its scientific rigor and claim accuracy. The upper bound of 7.8 reflects that even after these fixes, the method remains a practical engineering contribution rather than a fundamental scientific advance — the detection mechanism is heuristic and lacks theoretical grounding. Full novelty verification (unavailable this run) could further adjust this range upward if the rewriting-based detection paradigm is genuinely novel relative to prior work, or downward if substantial overlap exists.