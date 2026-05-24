Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper proposes a guardrail-agnostic method for evaluating societal bias in large vision-language models (LVLMs). The key insight is to decouple the task from the depicted person: instead of asking models to infer attributes of people in images (which triggers safety refusals), the method uses person-irrelevant prompts (e.g., "Write a fictional story") and attaches the image only as provisional user context. This achieves zero refusals across all 20 tested LVLMs, including heavily-guardrailed proprietary models like GPT-5 and Claude 3.7 Sonnet. The framework is instantiated across three tasks — story generation, term explanation, and exam-style QA — and reveals that all models exhibit measurable societal bias, with proprietary models showing lower but still non-negligible bias than open-source ones.

## Strengths

- **Zero-refusal achievement is compelling and well-demonstrated.** Table 1 shows 0% refusal rates for the proposed method across all six tested models, while prior benchmarks (SBBench, ModScan, VLA-gender, Pairs) suffer from refusal rates up to 100%. This directly validates the central claim that the method circumvents safety guardrails and enables bias evaluation where existing benchmarks fail.

- **Broad and systematic empirical coverage.** The evaluation spans 20 LVLMs (16 open-source, 4 proprietary), three distinct person-irrelevant tasks, and both gender and racial bias axes (Table 2). This scale provides a genuinely informative picture of the bias landscape across today's model ecosystem.

- **Convincing qualitative evidence.** Figure 2 provides concrete, interpretable examples — e.g., GPT-4o generating "mechanic" for male users vs. "nurse" for female users in story generation, and Claude 3.7 Sonnet producing more technical CS explanations for male/White users. These examples make the abstract TVD scores tangible and align with well-documented societal stereotypes.

- **The core methodological idea is clever and well-motivated.** Reframing bias evaluation by treating images as user context rather than as prompt targets is a simple but effective design choice. The refusal-rate crisis in existing benchmarks (Table 1) is clearly documented and establishes a genuine need for the proposed approach. The method is extensible to any person-irrelevant task, as discussed in Section 5.

- **Analytically informative beyond mere bias reporting.** The observation that inter-task bias correlations are weak (Observation 2.3, Figure 3) and that gender-race biases are strongly interdependent (Observation 2.4) provides insight into how bias manifests differently across tasks and demographics. Figure 4's analysis of bias vs. performance/size relationships (e.g., strong negative correlation in exam-style QA, r ≈ −0.8) adds useful nuance.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Asymmetric correlation values in Figure 3 are unexplained and potentially erroneous.** The figure caption reports bidirectional task-wise correlations with differing values for the same pair (e.g., "Story Gen. to Term Exp. r = 0.49" vs. "Term Exp. to Story Gen. r = 0.60"; "Exam QA to Term Exp. r = 0.08" vs. "Term Exp. to Exam QA r = 0.93"). Pearson's r is symmetric, so these discrepancies either reflect an error or an unstated methodological choice (e.g., different model subsets per direction due to LLaVA-1.6 exclusion from Exam QA). This undermines confidence in the correlation analysis and must be corrected or explained. The overall claim of weak inter-task correlations remains plausible, but the specific numerical values are not trustworthy as reported.

- **No reporting of measurement uncertainty.** All bias scores in Table 2 and correlations in Figures 3–4 are presented as point estimates without confidence intervals, standard errors, or significance tests. Several bias scores are small (e.g., Exam-Style QA scores below 2 in many cells), and without variance estimates it is impossible to judge whether differences between models or tasks are distinguishable from noise. While not all bias-benchmark papers report uncertainty, the scale and detail of this paper's comparative claims warrant it.

- **The normative basis (Hypothesis 1) could be better defended.** The paper asserts that an unbiased model's outputs for person-irrelevant prompts should be statistically independent of user demographics. This is a reasonable starting point, and the paper does define the "ideal uniform distribution" per task (e.g., equal occupation proportions across groups for story generation). However, the paper does not discuss potential objections — for instance, whether certain distributional shifts might reflect benign personalization rather than harmful stereotyping, or how the framework distinguishes between the two. A brief discussion of why independence is the appropriate standard for person-irrelevant tasks, and what its limitations are, would strengthen the conceptual grounding.

### Trivial

- The TVD scale (0–100 after multiplication) is implied but never explicitly bounded in the main text. Clarifying this in Table 2's caption would help readers.
- The rationale for excluding LLaVA-1.6 variants from Exam-Style QA ("near-random accuracies that lead to misleadingly low bias scores") is stated but the accuracy threshold is not specified.
- The LLM assistant's alignment with human judges (Appendix D) is referenced but key numbers (e.g., agreement rates) should be summarized in the main text, given how central the assistant is to attribute extraction and explanation comparison.

## Nice-to-Haves

- **Validate against an existing benchmark where refusal is low.** For models with moderate refusal rates on benchmarks like Pairs (10–61% in Table 1), computing bias scores under both the proposed method and the existing benchmark (for answered prompts) would test whether the two approaches rank models similarly. This would strengthen the claim that the new method measures the same underlying construct of societal bias. Note: this is not essential to the paper's core contribution (enabling evaluation where existing benchmarks fail), but would bolster external validity.

- **Refine the normative framing around Hypothesis 1.** A brief analysis distinguishing stereotyping from benign demographic variation — perhaps by auditing top-weighted attributes for stereotypical content — would preempt the objection that the metric penalizes any demographic-conditional behavior equally.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic: "The equal-outcome definition of bias is insufficiently motivated... This sets the standard at demographic parity... conflating potentially benign variation with stereotyping."** → Removed as a *fatal* characterization. The paper's Hypothesis 1 is applied to *person-irrelevant* tasks, where demographic independence is a natural baseline. The "benign variation" concern (e.g., generating stories featuring women for female users) is in fact exactly the kind of demographic cue usage the method is designed to detect — the model should not use the user's photo to decide the gender of a fictional character. A more nuanced defense would help but the hypothesis is defensible as-is. Retained as a Minor weakness (normative framing could be better defended).

- **Harsh Critic: "No validation against existing bias benchmarks where refusal is not a problem... This is a critical methodological gap."** → Demoted from Major/Fatal to Nice-to-Have. The paper's contribution is enabling evaluation where existing benchmarks *cannot* work. Cross-validation would strengthen the paper but is not required to support its central claim. Qualitative examples (Figure 2) already show the method captures known stereotypes.

- **Harsh Critic: "The paper's claim that 'these benchmarks fail to reliably measure societal bias' might be too absolute."** → Removed. This is a framing preference, not a substantive problem. Table 1 shows refusal rates up to 100%, which makes the claim factually accurate for those models/benchmarks.

- **Strength Finder: "Practical discussion and deployment guidance."** → Kept but noted as speculative. Section 5's discussion of continuous monitoring and refinement as a bias-reduction factor is plausible but not empirically demonstrated in this paper.

- **Strength Finder: "Well-defined task instantiations and bias metrics."** → Kept with qualification — the TVD definitions per task are clear, but the TVD scale bounding and some implementation details are deferred to the appendix (which is stripped in this review copy).

## Novel Insights

Beyond the paper's own contributions, the review process highlights an interesting tension in bias evaluation: the paper's Hypothesis 1 (independence = fairness for person-irrelevant tasks) is simultaneously its greatest strength and its least-defended assumption. The field lacks consensus on what "fair" outputs look like when a model is given demographic context it wasn't asked to use. This paper implicitly adopts a strict standard — any demographic influence is bias — which is clean and operationalizable, but future work may need to grapple with whether some forms of demographic-conditional behavior (e.g., varying explanation style to match a user's demonstrated preferences) are actually desirable. The framework's extensibility (Section 5) makes it well-positioned to explore this question.

## Suggestions

- Fix the Figure 3 correlation reporting. If bidirectional correlations are genuinely different due to different model subsets, explicitly state which models are included in each computation. If this is an error, correct it. In either case, Pearson r values for the same pair of variables computed on the same data must be symmetric.
- Add bootstrap confidence intervals to Table 2 and report them alongside point estimates. Even 95% CIs from 1,000 bootstrap resamples would substantially strengthen the evidential weight of the comparative claims.
- Move the key finding from Appendix D (LLM assistant's agreement with human judges) into the main text, even if just as a single sentence with the agreement rate.
- Consider a brief paragraph in Section 3.1 addressing the scope and limits of Hypothesis 1 — acknowledging when demographic independence is the right standard and when it may be too strict.

## Score and Decision

**Round 1 bracket:** After comparing against anchors, the paper sits between the 5.0 cluster (CVLD at 5.00, SCOPE at 5.00 — debiasing/evaluation papers with moderate novelty and empirical limitations) and the 6.5–7.0 cluster (FairerCLIP at 6.50, "Can we talk models" at 7.00 — well-executed papers with clear contributions and comprehensive experiments). Initial bracket: **5.0–7.0**.

**Round 2 narrowing:** The paper is stronger than SCOPE (5.00) — it has a more novel core idea and broader empirical coverage — and stronger than CVLD (5.00). It is comparable to FairerCLIP (6.50) in execution quality, though FairerCLIP has deeper technical novelty while this paper has broader empirical scope and a more timely problem framing. The paper falls slightly below "Can we talk models" (7.00) due to the unresolved correlation asymmetry and lack of uncertainty quantification. Final placement: **6.0**.

### Anchor comparison summary

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| J6nKxekCCo (Intersectional Stereotypes) | 3.00 | 1 | Our paper is substantially stronger — broader evaluation, clearer contribution |
| 2iPvFbjVc3 (Caption Evaluation) | 3.40 | 1 | Not directly comparable |
| FwdnG0xR02 (Balancing the Picture) | 4.67 | 1 | Our paper has broader scope, more models, and a more novel core idea |
| xx05gm7oQw (CVLD) | 5.00 | 1 | Our paper has stronger novelty and broader evaluation |
| 72H3w4LHXM (SCOPE) | 5.00 | 2 | Our paper is stronger — more novel idea, cleaner methodology, broader coverage |
| HXoq9EqR9e (FairerCLIP) | 6.50 | 1,2 | Comparable quality; FairerCLIP has deeper technical contribution, our paper has broader empirical scope |
| iVMcYxTiVM (Can we talk models) | 7.00 | 2 | Slightly stronger than our paper — better presentation clarity and more robust analysis |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>