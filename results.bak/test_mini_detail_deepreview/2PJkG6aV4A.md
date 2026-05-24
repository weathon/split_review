Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes a guardrail-agnostic framework for evaluating societal bias in large vision-language models (LVLMs). The key insight is to replace attribute-inferring prompts (e.g., "Is this person a CEO or a secretary?"), which trigger safety refusals in guardrailed models, with person-irrelevant prompts (e.g., "Write a fictional story"), treating the image only as provisional user context. The method is instantiated across three tasks — story generation, term explanation, and exam-style QA — and evaluated on 20 recent LVLMs including proprietary models like GPT-5 and Claude 3.7. The method achieves zero refusals across all models (vs. 35–100% on prior benchmarks) and reveals that all models exhibit bias, though proprietary models show lower bias than open-source ones.

## Strengths

- **Zero refusals across all models (Tab. 1):** Prior benchmarks show refusal rates of 35–100% even for modern models, while the proposed method achieves 0% refusal for all 6 listed models including GPT-5 and Claude 3.7 Sonnet. This directly demonstrates that decoupling the task from the depicted person solves the answer-refusal problem that motivates the paper.

- **Bias detected in heavily guardrailed proprietary models (Tab. 2):** GPT-5, the most safety-aligned model tested, still shows gender bias (TVD×100 of 14.53) and racial bias (16.80) in story generation. This provides concrete evidence that the method reveals bias where prior attribute-inferring benchmarks fail, delivering on its core claim.

- **Task-specific bias correlations quantified (Fig. 3):** Weak cross-task correlations (−0.11 to 0.21) and strong within-task gender–race correlations (0.49 to 0.93) support the claim that bias is not monolithic and that diverse tasks are necessary — a finding that goes beyond simply stating the existence of bias.

- **Performance and model size fail to explain bias (Fig. 4):** Bias–performance correlations vary wildly across tasks (e.g., r = −0.81 for exam QA gender vs. r = 0.23 for term explanation gender), and bias–model-size correlations also differ (e.g., r = 0.72 for story generation racial bias vs. r = −0.44 for exam QA gender). These results rule out trivial explanations and add empirical depth.

## Weaknesses

### Major

1. **The paper claims to "reduce the impact of spurious image contexts" without providing evidence.** The paper correctly identifies that captioning-style prompts suffer from contextual confounds (§2, line 153): non-person visual features (backgrounds, objects) can correlate with demographics in FairFace, making it unclear whether disparities reflect stereotyping or dataset artifacts. The paper then claims its method "reducing the impact of spurious image contexts" (line 155) but provides no empirical verification. While the logic — that person-irrelevant tasks give the model less reason to use background features — is reasonable, the absence of any controlled experiment (e.g., comparing outputs with and without the image, or using synthetic images that swap demographic labels while keeping background constant) leaves the central claim partially unvalidated. This does not invalidate the method (the measured disparities still reflect real differential treatment of users), but it does mean the paper overstates how cleanly the scores isolate "societal bias" from visual confounds.

2. **No statistical significance testing or confidence intervals for bias scores.** Tab. 2 reports raw TVD×100 scores without any measure of uncertainty. Given the finite sample (500 images per group for story generation, 100 per group for other tasks), some of the smaller scores (e.g., 0.50/0.36 for GPT-5 exam-style QA) may not be statistically distinguishable from zero, and comparison across models lacks error bars. This limits the rigor of claims about which models are "less biased."

### Minor

3. **The LLM judge (Qwen3-32B) used for term explanation and story generation is a potential confound.** The paper states that its judgments "align well with human judges" (Appendix D, unseen), but no quantitative alignment (e.g., Cohen's κ) is reported in the main text. Since the judge model's own biases could influence the relative technicality assessments, this dependency should be more transparently characterized.

4. **The claim that "existing benchmarks fail" is somewhat overstated for certain open-source models.** Tab. 1 shows that VLA-gender has 0% refusal for LLaVA-1.6 and Pairs has only 10% refusal for LLaVA-1.6. These models *can* be evaluated on those benchmarks. The paper acknowledges this nuance in its discussion of "strong safety guardrails" (line 108) but the blanket characterization misleadingly suggests universal failure. The method's primary value is for guardrailed models, which is a sufficient contribution — the framing should be more precise.

5. **The discussion of "continuous monitoring" as a factor in proprietary models' lower bias (§5) is speculative.** The paper frames this as discussion, not a proven result, which is appropriate. However, the language ("can be a critical factor," line 402) overreaches relative to the correlational evidence presented. This section would benefit from clearly labeling the argument as a hypothesis for future work.

### Trivial

None beyond standard presentation issues common to camera-ready formatting.

## Nice-to-Haves

- **Validate against known biases on less-guardrailed models.** A sanity check showing that the method recovers well-established gender-occupation stereotypes on older models (e.g., LLaVA-1.6) against a known bias benchmark would help establish that the method measures the *same kind* of bias as prior work, not a new artifact.
- **A controlled confound experiment.** The most impactful addition would be face-swapping or synthetic images that hold visual context constant while varying demographic labels. This would directly address the construct-validity concern and substantially strengthen the paper.

## Removed Points

The following points from the input reviews are removed with justification:

1. **"The method provides no evidence that the model actually uses the image as user information"** — Removed because it is factually contradicted by the paper's own results. Tab. 2 shows systematic disparities across demographic groups; if the model were ignoring the image, there would be no such disparities. The systematic differences *are* the evidence.

2. **"Exclusion of LLaVA-1.6 from exam-style QA is a red flag"** — Removed. The paper explicitly and transparently notes this exclusion (Tab. 2 caption, line 211) with a valid methodological reason: near-random accuracy compresses bias scores. This is correct handling, not a flaw.

3. **"The method likely measures spurious correlations in the image dataset rather than societal bias — a structural flaw that undermines the central claim"** — Downgraded from "fatal" to "major" (weakness 1 above). The critic's claim that this is a "structural flaw that undermines the central claim" is overstated. For term explanation (technicality of explanations) and exam-style QA (accuracy), there is no plausible pathway for background image features to cause the measured disparities in a systematically biased way. The method does measure real differential treatment, even if the exact causal attribution to "demographic stereotyping" vs. "visual confounds" is not fully disentangled. The weakness is that the paper provides no evidence for its claim of "reducing" confounds, not that the method is fundamentally invalid.

4. **"Weak correlations could also reflect dataset artifacts, not interdependent biases"** — Removed as speculation. Both interpretations are equally plausible from the available data. The paper's interpretation is standard and reasonable.

5. **"Continuous monitoring discussion is pure speculation with no causal evidence"** — Weakened to minor (weakness 5). The paper frames this as discussion, but the language could be more measured.

6. **"No validation against known biases"** — Moved to Nice-to-Haves.

## Novel Insights

The harsh critic raises a genuine concern about visual confounds that the paper does not adequately address. However, the critic's framing of this as a fatal structural flaw overreaches: the three tasks differ fundamentally in how the image could influence the output, and for term explanation and exam-style QA the pathway from image background features to systematic output disparities is highly implausible. The more interesting observation (which is not articulated by either reviewer) is that **the paper's strongest evidence for construct validity is actually implicit in its own task design**: the fact that bias scores across the three tasks are only weakly correlated suggests that the method is not measuring a single monolithic confound but rather task-specific demographic effects, which is precisely what one would expect from a valid bias measurement. A deeper exploration of this point — showing that specific known stereotypes (e.g., gender-occupation) appear in story generation while other predictable patterns appear in term explanation — would have substantially strengthened the paper.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak anchors (< 3.5): Unrelated topics (person detection bias, caption evaluation, concept banks). These are clearly weaker than the current paper.
- Middle anchors (3.5–7.5): 
  - *Debias your VLM with Counterfactuals* (5.0, Reject) — proposes a VLM debiasing method. Had limited novelty, only tested gender bias, and lacked strong baselines. The current paper has a more novel core idea, cleaner results, and broader evaluation, making it stronger.
  - *See It from My Perspective* (6.0, Accept) — studies cultural bias in VLMs with controlled experiments. Comparable in quality: both have a clear question and good experimental design. The current paper has a more novel methodological contribution but slightly weaker causal validation.
  - *Can we talk models into seeing the world differently?* (7.0, Accept) — studies shape/texture bias in VLMs. Thorough analysis, well-written. The current paper is less technically deep and has a more significant confound concern.
  - *First-Person Fairness in Chatbots* (7.25, Accept) — studies name-based bias in chatbots. Very similar evaluation paradigm (using user proxy for demographics). The current paper tests more models but has less validation of the evaluation tool.
- Strong anchors (> 7.5): Unrelated to bias evaluation (synthetic data detection, multimodal comprehension benchmarks).

**Round 1 bracket:** 5.0–7.0.

**Round 2 — Narrowing:**
- *FairerCLIP* (6.5, Accept) — debiasing CLIP with RKHS methods. Technically sound but somewhat narrow scope. The current paper addresses a broader and more practical problem.
- *SANER* (7.0, Accept) — CLIP debiasing. Well-executed but specialized. The current paper has a more generally applicable contribution but less rigorous validation.
- *Towards reporting bias* (6.0, Reject) — bimodal augmentation for reporting bias. Similar score range but different topic.

**Final placement:** The paper sits between the 5.0 (CVLD) anchor and the 6.0–6.5 anchors. It is genuinely clever and addresses a real problem with clean results, but the unaddressed confound concern and missing statistical rigor prevent it from reaching the 6.5–7.0 level of the stronger papers. It is most comparable to *See It from My Perspective* (6.0), sharing similar strengths (clear motivation, extensive experiments) and weaknesses (some overclaiming, limited validation of one component). I place it at **6.0**.

### Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>