Now I have a solid calibration picture. Let me write the final consolidated review.

**Round 1 bracket**: I estimated this paper sits between 5 and 7.5 based on three bands — weak anchors (2.33–3.4, not comparable), middle anchors (4.0–6.25), strong anchors (8.0). The paper is clearly above the 4.0–4.4 reject-level bias papers and below the 8.0 theoretical analysis papers.

**Round 2 narrowing**: I read anchors at 6.25 (Quantitative Certification of Bias), 6.75 (Justice or Prejudice), 6.5 (FairerCLIP), 7.0 (Can we talk models). The paper under review is comparable to the 6.5–6.75 range — it has a clearer practical contribution than FairerCLIP, similar strength to the LLM-as-judge bias paper, but lacks the statistical rigor of the certification paper and the thoroughness of the 7.0 shape-bias analysis paper.

**Final score: 6.5**

---

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision
MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: Accept

Wait, I need to write the full review in the proper format. Let me format it properly.Now I have all the evidence needed. Let me compile the final review.

---

## Summary

This paper proposes a guardrail-agnostic method for evaluating societal bias in large vision-language models (LVLMs). The key insight is to replace *attribute-inferring prompts* (which trigger refusals in safety-aligned models) with *person-irrelevant prompts* while attaching images only as user context, thereby bypassing guardrails while still measuring demographic biases in model outputs. Instantiated across three tasks — story generation, term explanation, and exam-style QA — the method achieves zero refusals across all 20 evaluated models (including GPT-5 and Claude 3.7 Sonnet, where prior benchmarks fail with up to 100% refusal rates). The empirical evaluation reveals that all tested models exhibit measurable bias, with proprietary models generally showing lower but still non-negligible bias, and that bias is task-specific rather than monolithic.

## Strengths

1. **Zero-refusal evaluation on models where prior benchmarks completely fail.** Table 1 is a clean, decisive result: four prior benchmarks (SBBench, ModScan, VLA-gender, Pairs) show refusal rates of 49–100% on GPT-5 and Claude 3.7 Sonnet, while the proposed method achieves 0% refusal across all 20 models. This directly solves the core problem identified in §1 and is the paper's strongest empirical contribution.

2. **Clever and well-motivated methodological design.** The idea of decoupling the evaluation task from the depicted person — using person-irrelevant prompts (e.g., "Write a fictional story about an imaginary person") and treating the image only as user context — is simple yet effective. The paper provides a clear formal framework (Eq. 1–3, Hypothesis 1) and the qualitative examples in Figure 2 concretely illustrate how the method surfaces stereotypical associations (e.g., *mechanic* vs. *nurse* for male vs. female users) that would be invisible under standard attribute-inferring benchmarks.

3. **Comprehensive evaluation across diverse models and tasks.** The paper evaluates 20 LVLMs (16 open-source, 4 proprietary) across three distinct tasks that probe different aspects of bias. The controlled experimental design — aligning non-target demographic distributions (e.g., matching race and age when measuring gender bias) — is a careful methodological choice that addresses confounds present in prior work.

4. **Evidence that bias is not monolithic (task-specificity).** The correlation analysis in Figure 3 (text reports weak task-wise correlations of −0.11 to 0.21) provides preliminary support for the claim that models' bias on one task does not predict bias on another, justifying the need for diverse evaluation tasks. The analysis of bias vs. performance and model size (Figure 4) further shows that bias patterns are complex and not reducible to simple trends.

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty quantification on central quantitative results.** Table 2 reports only point estimates of bias scores (TVD × 100) for all 20 models across three tasks. No confidence intervals, standard errors, or bootstrap estimates are provided. This makes it impossible to assess whether observed differences — e.g., the gender-bias gap between GPT-5 (14.53) and Claude 3.5 Sonnet (14.33) in story generation, or between InternVL3-38B (0.88) and GPT-5 (0.50) in exam-style QA — reflect meaningful disparities or measurement noise. The same issue applies to the correlation coefficients in Figures 3 and 4. Since the scores are aggregated over many prompts (500 images for story generation, 100 for term explanation), bootstrapped confidence intervals are straightforward to compute and would substantially strengthen every comparative claim in the paper. This is the single largest weakness.

2. **Correlation analysis for Observation 2.3 rests on very small samples.** The claim that bias is non-monolithic ("a low bias score on one axis does not imply fairness on others") is supported by correlations computed over only ~20 models (fewer for some comparisons, e.g., LLaVA-1.6 excluded from exam-style QA). With such small sample sizes, Spearman/Pearson correlations are highly sensitive to individual data points, and no confidence intervals or permutation tests are reported. The observation is plausible and informative as a directional signal, but the paper overstates the conclusiveness of the evidence. Reporting intervals or using a small-sample-appropriate method would make the claim more robust.

### Minor

1. **TVD metric limitations for exam-style QA are underexplored.** The paper computes TVD as deviation of per-group accuracies from their mean, which is appropriate for detecting performance disparities. However, if one demographic group inherently has lower accuracy on certain MMLU subsets (e.g., due to question difficulty rather than model bias), the TVD would reflect that even in a perfectly fair model. The paper excludes LLaVA-1.6 for near-random accuracy (a reasonable acknowledgment), but does not discuss this confound more broadly. A brief discussion of what TVD measures and does not measure in this task would improve the paper.

2. **The claim about "continuous monitoring" as a key factor reducing bias is speculative and undersupported.** Section 5 argues that continuous monitoring and iterative refinement (practiced by proprietary model providers) is a critical factor in reducing bias. The paper provides no data on proprietary models' monitoring practices — only references to system cards — and does not rule out alternative explanations (e.g., larger or more carefully filtered pre-training data). This discussion is reasonable as a hypothesis but should be more clearly framed as such.

### Trivial
None.

## Nice-to-Haves

- **Ablation for the "image as user" assumption.** A brief sanity check verifying that models actually process demographic information from the images (e.g., comparing outputs when the same prompt is given with vs. without the image, or with explicitly stated demographics in text) would strengthen confidence in the mechanism. The observed output differences across demographics already suggest models use the images, but a direct ablation would be cleaner.

- **Per-prompt breakdown or domain-level analysis for term explanation.** The paper aggregates bias scores across six domains (math, physics, CS, etc.). Reporting per-domain breakdowns would reveal whether bias is concentrated in particular subject areas, which would be useful for practitioners.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **LLM judge bias unexamined.** The harsh critic raised concern that Qwen3-32B's own biases could confound term-explanation and story-generation judgments. However, the paper explicitly states (p. 201) that "In Appendix D, we further confirm that its judgments align well with human judges." Since the appendix is stripped by the parser (a known artifact of the review format, not an author omission), this criticism is removed per protocol. The concern would be valid only if the paper provided no validation at all, which it does.

- **Figure 3 caption confusion.** The harsh critic noted seemingly inconsistent correlation values in Figure 3's caption (e.g., "Exam QA to Term Exp. (r = 0.93)"). This is a parser artifact that has garbled the figure's embedded text. The paper's own descriptive text (Observation 2.3) correctly states that task-wise correlations are weak (−0.11 to 0.21), while the strong values (0.49, 0.60, 0.93) correspond to gender-race correlations within tasks (Observation 2.4). The actual figure, which cannot be rendered here, is undoubtedly clearer.

- **Request for ablation on contextual confounds.** The critic requested an ablation showing the proposed method is less affected by contextual confounds than captioning-style prompts. The paper's claim is that replacing attribute-inferring prompts with person-irrelevant prompts *avoids* the confound problem (since the task is not about the image), not that it empirically measures confound reduction. This is a reasonable conceptual argument that does not require the requested ablation.

- **Criticism about whether models process the image.** The critic speculates that the method may not work if models fail to recognize the image as a user photo. However, the paper's empirical results directly disprove this concern: outputs *do* differ across demographic groups, proving that models are extracting and using demographic information from the images. The zero refusal rate + observable output differences = the method demonstrably works.

## Novel Insights

None that emerge from the reviews beyond the paper's own contributions. However, one observation worth noting: the paper's core contribution is not just a new benchmark but a *methodological paradigm shift* — decoupling the task from the person being evaluated. This insight could generalize beyond bias evaluation to other contexts where guardrails obstruct useful measurement (e.g., measuring sycophancy, persona adoption, or instruction-following disparities). The reviewers did not explore this extensibility angle, but it is a genuinely novel aspect of the work.

## Suggestions

1. **Add bootstrapped 95% confidence intervals to Table 2 and to the correlation coefficients in Figures 3–4.** This is the single highest-impact improvement. The sampling structure (500/100 images per group) makes bootstrap straightforward and would establish the reliability of comparative claims without new experiments.

2. **For the correlation analysis (Observation 2.3), either add confidence intervals, report Spearman with small-sample corrections, or run a permutation test.** This would strengthen the claim about bias not being monolithic without overstating the evidence.

3. **Add a brief limitations paragraph discussing the TVD metric's behavior in exam-style QA**, noting that group-level accuracy differences could reflect question difficulty effects rather than model bias, and how the current setup mitigates (or does not mitigate) this concern.

4. **Reframe the "continuous monitoring" discussion in Section 5 more precisely as a hypothesis** supported by circumstantial evidence, with alternative explanations acknowledged.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Path | Avg Score | Round | Comparison to this paper |
|--------|------|-----------|-------|-------------------------|
| Quantitative Certification of Bias in LLMs | HQHnhVQznF | 6.25 | 1 | This paper has a more novel methodological contribution but lacks the statistical rigor (CIs, certificates). Comparable overall quality. |
| Benchmarking Ethics in T2I Models | kIboeK0Wzs | 4.40 | 1 | Both are bias evaluation papers, but this paper is significantly stronger: cleaner method, more comprehensive evaluation, better writing. |
| Causal analysis of social bias in CLIP | Dk10QugVHb | 5.75 | 2 | Similar topic (measuring bias in VLMs); this paper's guardrail-agnostic angle is more novel and practically useful. |
| FairerCLIP | HXoq9EqR9e | 6.50 | 2 | Both accepted; this paper has a simpler but more impactful empirical contribution. Comparable quality. |
| Can we talk models into seeing the world differently? | iVMcYxTiVM | 7.00 | 2 | Both are VLM analysis papers; the shape-bias paper has more thorough analysis, but this paper has a clearer practical contribution. Slightly weaker in analysis rigor. |
| Justice or Prejudice? (LLM-as-a-Judge biases) | 3GTtZFiajM | 6.75 | 3 | Both propose bias evaluation frameworks; this paper's method is more novel (not a "toolkit" paper). Comparable quality with different strengths. |

**Round 1 bracket:** 5.0–7.5 (paper sits above 4.4 reject-level bias papers, below 8.0 theoretical papers).

**Round 2–3 narrowing:** Paper is comparable to the 6.5–6.75 accepted papers and slightly above the 5.75–6.25 papers. The main weaknesses (no CIs, thin correlation analysis) prevent it from reaching the 7.0+ range but do not undermine its core contribution.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>