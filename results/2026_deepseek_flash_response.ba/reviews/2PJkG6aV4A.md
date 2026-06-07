Now I have a good sense of the calibration. Let me write the final review.

## Summary

This paper proposes a guardrail-agnostic method for evaluating societal bias in large vision-language models (LVLMs). The key innovation is changing the role of images from "target of inquiry" to "provisional user information" and replacing attribute-inferring prompts (which safety guardrails block) with person-irrelevant prompts (story generation, term explanation, exam-style QA). The method achieves zero refusals across 20 models (including strongly-guardrailed GPT-5 and Claude 3.7 Sonnet) where prior benchmarks fail. The large-scale evaluation reveals that all models exhibit demographic differences in outputs, with proprietary models showing lower but non-zero bias compared to open-source ones.

## Strengths

- **Zero refusals across all evaluated models (Table 1).** The method achieves 0% refusal on 6 diverse models spanning open-source (LLaVA-1.6-34B, Qwen2.5-VL-32B, Gemma3-27B, InternVL3.5-38B) and proprietary (GPT-5, Claude 3.7 Sonnet), while four prior benchmarks show 49–100% refusal on the same models. This directly validates the core guardrail-agnostic claim.

- **Principled reformulation of the evaluation setup (Sec. 3.1, Fig. 1).** Changing the image role from "target" to "user context" and switching from attribute-inferring to person-irrelevant prompts is a clean conceptual innovation. It bypasses guardrails structurally (by changing what the task asks) rather than through adversarial prompting, which is both more elegant and more robust.

- **Comprehensive evaluation across 20 recent LVLMs on three tasks (Table 2, Sec. 4.3).** The evaluation spans 16 open-source models (7B–38B) and 4 proprietary models (Claude 3.5/3.7 Sonnet, GPT-4o, GPT-5) across gender and racial bias on three distinct tasks. This scale enables comparative findings (e.g., proprietary models show lower but non-zero bias) that no single-model or single-task study could support.

- **Demonstration that bias is not monolithic (Obs. 2.3, weak cross-task correlations).** The weak cross-task correlations (−0.11 to 0.21) provide empirical evidence that a model's bias on one task does not predict its bias on another, with practical implications for evaluation design.

- **Explicit control for non-target demographic distributions (Sec. 4.1).** When measuring gender bias, race and age distributions are matched between female and male user image sets, and vice versa for racial bias. This methodological precaution isolates the target demographic axis from confounds.

## Weaknesses

### Major

- **Construct validity ambiguity: the paper does not fully establish that it measures "societal bias" rather than "demographic personalization."** The core Hypothesis 1 ("outputs for person-irrelevant prompts should be statistically independent of user demographics") is a normative claim that the paper treats as self-evident but does not adequately justify. For story generation in particular, a model writing a story with a protagonist matching user demographics could be interpreted as contextually appropriate personalization, not harmful bias. The paper provides anecdotal evidence of stereotypical patterns (Fig. 2 shows *mechanic* vs. *nurse*, *middle-class* vs. *poor*) that suggest harmful stereotyping, but this is not quantified systematically across all outputs. The exam-style QA task is the cleanest case (demographic differences in math accuracy are clearly undesirable), and its very low bias scores (0.36–3.44 on a 0–100 scale) are consistent with models largely not doing this — which somewhat undercuts the broader narrative. The paper would be significantly strengthened by a systematic "stereotype directionality" analysis showing whether demographic differences are stereotypically harmful or merely diverse.

- **No validation against existing bias benchmarks.** The paper could have correlated its bias scores with those from prior benchmarks on models (e.g., older open-source models) that do not refuse attribute-inferring prompts, to establish convergent validity. The absence of this validation weakens the claim that the method measures "societal bias" in the same sense as prior work. Without it, the reader cannot assess whether the method captures the same construct or a different one.

- **No confidence intervals or statistical uncertainty quantification.** Table 2 reports bias scores as point estimates without any measure of uncertainty. For story generation (500 images per group), bootstrapped confidence intervals would be feasible and would help assess whether differences between models are meaningful. The correlation analyses (n=20 models) are underpowered; reported correlation coefficients lack confidence intervals or p-values.

### Minor

- **LLM-as-judge pipeline introduces a potential bias confound.** The Qwen3-32B model is used for extracting character attributes from stories and for judging technicality of explanations. This introduces a second model's biases into the measurement pipeline. The paper references Appendix D (removed in the extracted version) about alignment with human judges, which cannot be verified from the available text.

- **The Discussion's causal claims about "continuous monitoring" (Sec. 5) are speculative.** The paper observes lower bias in proprietary models and hypothesizes that continuous monitoring and iterative refinement (rather than one-time safety training) is the cause. The evidence is correlational (proprietary vs. open-source) with numerous confounds (model size, architecture, training data, RLHF). The paper itself notes that Gemma3 (which reports safety mitigation) shows high bias, which undercuts the safety-training explanation but does not provide positive evidence for the monitoring hypothesis. This section should be more clearly labeled as speculation.

- **The paper studies only gender and racial bias but frames findings in terms of "societal bias" broadly.** While the focus on these two axes is standard practice and reasonable for scope, the framing throughout (title, abstract, discussion) implies broader coverage than the experiments support.

### Trivial

None.

## Nice-to-Haves

- Add bootstrapped confidence intervals to all bias score estimates in Table 2.
- Add a systematic analysis of whether demographic differences are stereotype-directional (specifically harmful) vs. merely diverse, especially for story generation.
- Validate the method against prior bias benchmarks on non-refusing models to establish convergent validity.
- Report confidence intervals or p-values for all correlation coefficients (n=20 is small).

## Removed Points

These points from the reviewers were considered and removed as unjustified:

1. **"Figure correlation values are internally inconsistent"** — The figure description in the extracted text is a parser artifact. The paper's text clearly separates cross-task correlations (−0.11 to 0.21, Observation 2.3) from within-task gender-race correlations (0.49–0.93, Observation 2.4). The asymmetric listing in the figure caption is a formatting artifact of the parser, not an error in the original paper.

2. **"Table 1 comparison is inherently misleading"** — The comparison is used to demonstrate the extent of the refusal problem (motivation) and to validate that the proposed method solves it. The paper is not claiming that its method is a better measure of the *same construct* as prior benchmarks; it is proposing a *different approach* to bias measurement. This is a misunderstanding of the paper's contribution.

3. **"Exam QA may be text-only and not use images"** — This is pure speculation with no evidence. LVLMs by design process image+text inputs. If a model ignored the image, that would itself be a finding about its behavior, not a flaw in the evaluation.

4. **Strength Finder claimed "the single most important piece of evidence"** — This is a generic evaluative statement, not a concrete strength. Removed as puffery.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Explicitly reframe the contribution as measuring "demographic sensitivity in person-irrelevant tasks" rather than "societal bias," or add a section acknowledging the normative ambiguity and arguing why the observed effects constitute harm. A "stereotype directionality" analysis would be the most direct way to resolve this.
- Add bootstrapped confidence intervals to all bias scores in Table 2.
- Include a correlation analysis with prior benchmarks on models that do not refuse them, to establish convergent validity.
- Clearly label the "continuous monitoring" hypothesis in the Discussion as speculative and note the confounds.

## Score and Decision

**Calibration procedure and anchors:**

*Round 1 (bracketing):* Three queries targeting different score bands on bias evaluation in VLMs/LLMs. Weak-band anchors (score < 3.5) included papers with avg ~2.5–3.4 that were clearly weaker (e.g., "Uncovering Intersectional Stereotypes," avg 3.0 — poorly conceptualized benchmark, weak methodology). Middle-band anchors (3.5–7.5) included "Quantitative Certification of Bias" (avg 6.25, Accept), "Unraveling Safety Alignment Degradation" (avg 4.50, Reject), and "Debias your VLM with Counterfactuals" (avg 5.0, Reject). Strong-band anchors (>7.5) included comprehensive benchmark papers (avg 8.0) that are clearly more polished and rigorous.

*Round 1 bracket:* 4.5–6.5.

*Round 2 (narrowing):* Two queries targeting (3.5–6.0) and (5.5–7.5). Compared against "See It from My Perspective" (avg 6.0, Accept) — a cultural bias study in VLMs with cleaner construct validity but narrower scope; "Can we talk models into seeing the world differently?" (avg 7.0, Accept) — a comprehensive bias analysis with clearer contributions; and "Debias your VLM" (avg 5.0, Reject) — limited scope and novelty.

*Comparison assessment:*
- The current paper has a stronger methodological contribution than "Debias your VLM" (5.0) but a more ambiguous construct.
- The current paper has broader empirical scope than "See It from My Perspective" (6.0) but a less resolved core framing.
- The current paper is clearly stronger than the rejected anchors at 4.0–5.0 but has a significant unresolved weakness that the 6.0+ anchors do not.

*Final positioning:* The paper presents a genuine methodological innovation and extensive empirical evaluation, but the construct validity concern over what exactly is being measured is a nontrivial issue that prevents the paper from meeting the top-venue bar in its current form. The core empirical finding — that models exhibit demographic differentiation on person-irrelevant tasks with zero refusals — is robust, but its normative interpretation as "societal bias" requires more justification.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>