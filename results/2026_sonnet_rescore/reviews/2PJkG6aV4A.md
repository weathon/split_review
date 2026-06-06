## Summary
This paper proposes a guardrail-agnostic societal bias evaluation framework for large vision-language models (LVLMs). The key innovation is replacing attribute-inferring prompts (which trigger safety refusals in models like GPT and Claude) with *person-irrelevant* prompts while attaching the user's face image as provisional contextual information. The method achieves 0% refusal rates across all 20 evaluated LVLMs while still detecting meaningful gender and racial biases across three tasks: story generation, term explanation, and exam-style QA.

---

## Strengths

- **Zero-refusal evaluation is empirically demonstrated on real models.** Table 1 directly shows that all four prior benchmarks suffer 35–100% refusal rates on models like Claude 3.7 Sonnet (100% on SBBench) and GPT-5, while the proposed method achieves 0% across all models — including strongly guardrailed proprietary systems. This is the paper's central empirical claim and it is unambiguously supported.

- **Bias is still reliably extracted despite zero refusals.** Table 2 confirms that the method does not merely avoid refusals at the cost of signal: all 20 models exhibit non-negligible bias scores. For example, GPT-5 scores 14.53/16.80 (gender/race) on story generation, and Figure 2 provides qualitative grounding with examples like "mechanic" vs. "nurse" for male/female users in GPT-4o outputs.

- **Multi-task design is empirically validated.** The near-zero task-to-task bias correlations (r = −0.11 to 0.21) demonstrate that each task captures orthogonal bias dimensions, substantiating the design choice of using three diverse person-irrelevant probes rather than a single one.

- **Empirical finding that gender and racial biases are strongly interdependent** is a useful insight backed by correlation values of r = 0.49, 0.60, 0.93 across the three tasks (Figure 3, dotted lines), suggesting joint debiasing strategies should be preferred.

- **Model size and general performance do not reliably predict bias** — an important practical finding. Figure 4 shows r = −0.81 for exam-style QA but r = −0.17 and r = 0.23 for story generation and term explanation, refuting naive scaling-based explanations.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No sensitivity analysis on the "I've attached my photo" framing.** The image is always delivered with the self-referential prefix "I've attached my photo," which explicitly invites the model to treat the image as representing the user. A framing that omits this self-reference (e.g., "Here is an image:" or a purely visual attachment) might substantially change demographic-conditioned outputs because the self-referential cue is what signals to the model that it should infer demographic context from the image. Without at least one ablation condition, it is impossible to know whether the method is measuring a stable bias property of the model or a framing-induced artifact specific to this prompt construction. This directly bears on the method's ecological validity for real deployment scenarios, which the paper gestures toward in Section 5.

- **Weak cross-task correlations are underpowered with only 20 models.** Observation 2.3 claims "bias is not a monolithic property of a model" based on task-to-task correlations of r = −0.11 to 0.21. With n = 20 models, even moderate true correlations (r ≈ 0.4) would not reach conventional significance. The paper does not discuss statistical power, so the weak correlations may reflect noise rather than a genuine absence of relationship. The conclusion about non-monolithic bias would be more convincing with a larger model set or confidence intervals.

- **The normative foundation of Hypothesis 1 in story generation merits explicit acknowledgment.** For exam-style QA, Hypothesis 1 is intuitive: a math question should yield the same accuracy regardless of the user's face. For story generation, the prompt says "Write a fictional story about an *imaginary* person" — which makes demographic-correlated character attributes clearly inappropriate rather than adaptive personalization. That said, the paper could benefit from a brief acknowledgment of this distinction (personalization vs. stereotyping) to preempt reader confusion and to clarify why Hypothesis 1 applies uniformly across all three tasks. The examples in Figure 2 (mechanic/nurse, middle-class/poor) are intuitive illustrations of stereotyping, and a sentence in Section 3.1 explaining why "imaginary person" stories should not reflect the user's demographics would strengthen the theoretical grounding.

### Trivial

- **LLM-as-judge dependency is unaddressed in the main text.** Qwen3-32B is used to judge term-explanation difficulty for outputs from related Qwen2-VL models. Human agreement statistics from Appendix D are not summarized in the main text; at minimum, a brief agreement statistic (e.g., Kappa or accuracy against human labels) would improve confidence in the term-explanation bias scores.

- **No variance or confidence intervals are reported for TVD scores.** Given that scores in Table 2 span a wide range, knowing whether differences between adjacent models (e.g., GPT-4o at 26.29 vs. GPT-5 at 14.53) are statistically reliable would help practitioners interpret rankings.

---

## Nice-to-Haves

- An ablation comparing the "I've attached my photo" prefix against alternative framings (or no prefix) would significantly strengthen confidence in the method's framing-independence.
- A ground-truth validity check: for any models with known public bias records, cross-validating that the framework's scores rank them consistently would provide convergent validity.
- Reporting per-domain TVD scores in the main body (rather than only Appendix E) for exam-style QA would make the task-level granularity more accessible to readers.
- The discussion in Section 5 on "continuous monitoring" as a driver of proprietary model superiority is speculative; the authors appropriately hedge but could further enumerate alternative explanations (e.g., different training data composition, larger post-training budgets) to make the discussion more balanced.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **[Harsh Critic — S2/Table 1: Open-source refusal variation as "underexplored"]** The critique notes that refusal rate variation across open-source models (e.g., LLaVA-1.6-34B at 61% vs. Qwen2.5-VL-32B at 90% on SBBench) is underexplored. This is a tangential observation that does not affect the paper's core contribution; the paper's goal is to show that prior benchmarks are unreliable, not to explain why open-source refusal rates vary. Removed as out-of-scope.

- **[Harsh Critic — TVD metric justification]** The critic notes that TVD is mentioned in a footnote rather than in-text. The paper states "TVD is a robust alternative to KL divergence (Ji et al., 2023), and the detailed explanation is in Appendix A." This is a reasonable placement for a benchmark paper. The choice is not contested on technical grounds. Removed as scope creep / presentation nitpick.

- **[Harsh Critic — story generation cherry-picking]** The Figure 2 examples are described as "cherry-picked qualitative cases." This is a standard critique applicable to any qualitative illustration; the actual bias measurement uses the quantitative TVD score over 500 images per group, not the individual examples. Removed as not a methodological flaw.

- **[Harsh Critic — pairwise transitivity of term explanation]** The claim that pairwise explanation comparisons might be non-transitive is speculative. The bias score is computed as a TVD across group-wise selection ratios, not as a transitive ranking chain. The concern does not correspond to how the metric is actually computed. Removed as misunderstanding the method.

- **[Strength Finder — "addresses an important problem"]** Generic framing of importance without specific grounding. Replaced by the concrete strength about zero refusals backed by Table 1.

---

## Novel Insights

The paper surfaces an empirically grounded observation that goes beyond confirming bias exists: **bias across tasks is largely orthogonal (r = −0.11 to 0.21 task-to-task), yet gender and racial biases within the same task are strongly coupled (r = 0.49–0.93)**. This structure implies that model developers cannot assume a debiasing intervention on one behavioral axis (e.g., story generation) transfers to another (e.g., QA reasoning), but can assume that fixing gender bias within a task tends to also fix racial bias on that same task. This has practical implications for targeted mitigation strategies. The finding that larger, more capable models do not uniformly exhibit lower bias — with exam-style QA showing strong negative correlation (r = −0.81) while story generation shows near-zero correlation — further reveals that general capability improvements and societal bias reduction are decoupled in creative, open-ended tasks, pointing to the need for task-specific intervention rather than general-purpose scaling.

---

## Suggestions

1. **Add a framing ablation**: Run the method with at least one alternative image prefix (e.g., "Here is an image:" or no prefix) on a subset of models to test whether the "I've attached my photo" framing is driving demographic cue uptake or is merely one of several equivalent formulations.

2. **Address Hypothesis 1 for story generation explicitly in Section 3.1**: Add one sentence explaining that because the story is about an *imaginary* person (not the user), any demographic reflection in the imaginary character constitutes bias rather than user-adaptive personalization.

3. **Add statistical summaries for TVD scores**: Report either standard deviation across prompts (already computed during aggregation) or a simple permutation-test p-value to allow readers to distinguish reliably different models from ones within noise.

4. **Summarize Appendix D agreement statistics** in the main text with a single number (e.g., "Qwen3-32B agrees with human judges at X% on N examples") to support the term-explanation results.

5. **Strengthen Section 5 discussion** by enumerating alternative explanations for the proprietary/open-source gap more systematically (training data composition, post-training compute, reinforcement learning from human feedback intensity) alongside the continuous monitoring hypothesis, rather than citing only provider system cards.

---

## Evaluation on Key Axes

- **Originality**: The conceptual move of decoupling the task from the depicted person and using the image as user context is clean and novel. No prior work, as described by the paper, applies this paradigm to bias evaluation. High originality.
- **Importance of research question**: As safety guardrails spread across LVLM deployments, evaluating societal bias becomes increasingly impractical with existing benchmarks. The problem is timely and consequential.
- **Claims well-supported**: The main claims (zero refusals, non-zero bias in all models, proprietary < open-source bias, task-uncorrelated bias) are all backed by concrete numbers in Tables 1–2 and Figure 3. The speculative discussion in Section 5 is appropriately hedged.
- **Soundness of experiments**: Three tasks × 20 models × 500/100 images per group is reasonable for a benchmark paper. The LLM-as-judge dependency and missing framing ablation are gaps but do not invalidate the findings.
- **Clarity of writing**: The paper is well-organized, clearly motivated, and the method is described with enough precision to reproduce. Hypothesis 1 could be better defended but is not obscure.
- **Value to research community**: The framework is extensible to any person-irrelevant task, directly applicable to deployment monitoring, and provides baseline bias scores for 20 current LVLMs including GPT-5 and Claude 3.7 Sonnet that prior work cannot evaluate. High practical value.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>