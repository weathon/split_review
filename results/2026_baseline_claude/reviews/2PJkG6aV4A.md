## Summary
The paper proposes a "guardrail-agnostic" framework for evaluating societal bias in large vision-language models (LVLMs). The authors identify a critical flaw in existing benchmarks: modern safety-guardrailed LVLMs (GPT, Claude, and increasingly open-source models) frequently refuse "attribute-inferring prompts" (e.g., "Is this person a CEO or a secretary?"), breaking the statistical assumptions underlying current evaluation methods. The proposed fix is to use "person-irrelevant prompts" (e.g., "Write a fictional story about an imaginary person.") while attaching the user's photo as provisional context, then measuring whether model outputs differ statistically across demographic groups. The framework is instantiated across three tasks—story generation, term explanation, and exam-style QA—and applied to 20 LVLMs, finding universal societal bias with proprietary models exhibiting less bias than open-source ones.

---

## Strengths

- **Timely and well-documented problem**: Table 1 provides compelling empirical evidence that existing bias benchmarks are practically unusable on modern guardrailed models (e.g., Claude 3.7 Sonnet refuses 100% of SBBench prompts, GPT-5 refuses 97% of VLA-gender prompts). This is a real, growing problem that the community needs to address.
- **Elegant methodological pivot**: The "person-irrelevant prompt + image as user context" design is genuinely novel and achieves zero refusals across all 20 evaluated models. The idea of decoupling the task from the person while still extracting demographic cues is simple, principled, and immediately practical.
- **Comprehensive evaluation at scale**: 20 models spanning open-source (7B–38B) and proprietary families, two demographic axes (gender and 7-category race), and three structurally distinct task types with careful demographic confound control (Sec. 4.1), represents a thorough empirical study.
- **Multi-dimensional findings with policy implications**: The observation that task-level bias scores are weakly correlated (−0.11 to 0.21), that gender and racial biases are interdependent (r = 0.49–0.93), and the argument that continuous post-deployment monitoring may matter more than one-time safety alignment are substantive insights that go beyond the benchmark paper template.
- **Illustrated, concrete examples**: Figure 2 shows clear stereotyping (mechanic vs. nurse, middle-class vs. poor for White vs. Black users) from GPT-4o and Claude 3.7 Sonnet, making the abstract bias scores tangible and credible.

---

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in Hypothesis 1's normative claim.** The core theoretical premise—that an unbiased model's outputs on person-irrelevant tasks should be statistically independent of user demographics—is asserted rather than argued. The setup explicitly invites personalization: users are told "I've attached my photo," so the model is not covertly reading demographics; it is responding to a user-provided signal. There is a genuine conceptual distinction between *harmful stereotyping* (assigning poor economic status to Black characters, limiting STEM explanations for women) and *benign personalization* (adapting tone or narrative style to a user who has voluntarily shared their photo). The paper's framework conflates these, yet its hypothesis only holds unambiguously for the former. The paper briefly nods to this in Sec. 5 but does not address it systematically. A deeper normative justification—or an explicit acknowledgment of when demographic-conditioned outputs are vs. are not acceptable—is needed given that this hypothesis underpins the entire evaluation.

2. **Residual confounds in the "image as user" setup.** The paper critiques captioning-based methods for suffering from spurious contextual cues correlated with demographics, and controls for age and race when measuring gender bias (Sec. 4.1). However, FairFace face images still carry non-controlled visual signals—apparent grooming style, expression, clothing visible in face-centric crops—that may be correlated with both demographic groups and model outputs. The paper does not demonstrate that remaining confounds are negligible. An ablation using generated/synthesized faces with controlled demographic attributes would substantially strengthen the causal interpretation.

3. **LLM-as-judge reliability for story attribute extraction.** The story generation task's bias scores depend critically on Qwen3-32B correctly extracting occupations and other attributes from generated stories. Edge cases (e.g., occupation not mentioned, ambiguous phrasing, fictional occupations without real-world counterparts) could systematically bias TVD scores. While the paper mentions human agreement in Appendix D, the main text provides no quantitative summary of agreement rates or error analysis, leaving the reliability of the most prominent task (story generation) partially unverified for the reader.

### Minor

1. **Statistical significance not reported.** Bias scores (TVD × 100) are reported as point estimates without confidence intervals or hypothesis tests. With 500 samples per group for story generation, small differences may not be statistically meaningful. The paper does not report whether the observation that, e.g., Claude 3.5 Sonnet gender bias (14.33) is meaningfully lower than Qwen2-VL-7B (37.83) passes any significance threshold.

2. **Exam-style QA interpretation ambiguity.** Accuracy differences on MMLU questions across demographic images could reflect either biased reasoning (the model actively downgrades performance for certain demographic users) or simple attentional distraction (the presence of an off-topic face image degrades performance, and this degradation differs by image type due to irrelevant visual complexity). The paper does not distinguish these, yet they have different implications for what "bias" means in this task.

3. **Design of term explanation prompts.** The 20 terms per domain were presumably selected by the authors; no details are given about whether the selection was systematic or pre-registered. Selection of domain-specific terms that differ in recognizability across groups could introduce prompt-level confounds in the difficulty-ranking judgments.

### Trivial
None.

---

## Nice-to-Haves

- An ablation where the "I've attached my photo." prefix is removed (to isolate how much bias is driven by the image alone vs. the explicit framing as user context) would be informative.
- Including a "no-image" control condition to measure how much output variation is due to image-conveyed demographics vs. noise would sharpen causal claims.
- A brief discussion of whether the three tasks have different *sensitivity* (i.e., how large a real-world bias would need to be to be detectable at a given sample size) would help practitioners calibrate the framework.

---

## Novel Insights

The most genuinely novel observation beyond the methodological contribution is that societal bias is task-specific and multi-dimensional in a structured way: it scales with task openness (story > explanation > QA), gender and racial biases are strongly correlated within tasks but independent across tasks, and no simple proxy (model size, general capability) predicts the full bias profile. This suggests that bias is not a scalar model property but a complex function of task structure—an insight with practical implications for both evaluation design and debiasing efforts. The hypothesis that continuous post-deployment monitoring, rather than one-time safety-alignment training, may be the dominant factor distinguishing proprietary from open-source models is speculative but plausibly supported and worth further investigation.

---

## Suggestions

- Add a normative subsection that clearly delineates which demographic-conditioned output differences constitute "bias" under the proposed framework and which might constitute legitimate personalization, ideally by citing or adapting fairness definitions from the ML fairness literature (e.g., demographic parity vs. calibration).
- Report confidence intervals or bootstrapped standard errors on all TVD scores in Table 2 to enable readers to assess whether cross-model differences are statistically reliable.
- Include a brief report of the LLM-judge agreement rate (e.g., Cohen's kappa with human annotators) in the main text, not only in the appendix, given that story generation is the paper's flagship task.
- Consider a brief ablation (or at least discussion) of whether the results change when using synthesized/generated demographically annotated faces rather than real photographs, to address residual visual confounds.

---

## Score and Decision

The paper addresses a genuine, timely problem with a clean and practical methodological solution, documents the solution across 20 models with careful experimental design, and produces findings that matter to the community. The primary concern—that Hypothesis 1 conflates harmful stereotyping with benign personalization—is real and deserves more attention, but it does not invalidate the identified bias examples, which are clearly problematic under any reasonable definition. The statistical and confound concerns are minor relative to the overall contribution. This is a solid accept.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>