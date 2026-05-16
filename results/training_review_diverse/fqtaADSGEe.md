Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper identifies labeling errors in the RefCOCO/+/g benchmarks (reporting 14%, 24%, and 5% error rates), releases cleaned versions, and introduces Ref-L4 — a new REC benchmark with 45,341 annotations, 365 object categories, expressions averaging 24.2 words, and a vocabulary of 22,813 unique words. The authors evaluate 24 large multimodal models (LMMs) on Ref-L4 using accuracy at multiple IoU thresholds, scale-aware metrics, and per-category analysis.

## Strengths

- **Systematic discovery and quantification of labeling errors in established REC benchmarks.** The paper manually examines validation and test sets, reporting error rates of 14% (RefCOCO), 24% (RefCOCO+), and 5% (RefCOCOg) (Table 1). This directly challenges the validity of prior evaluations and is a concrete contribution — prior work had not identified errors at this scale.

- **Demonstration that removing noisy labels changes model rankings.** After cleaning, four LMMs show accuracy improvements of 1.57–3.08 points across all three benchmarks (Table 2). For example, CogVLM-Grounding rises from 92.44% to 94.58% on RefCOCO. This provides direct evidence that benchmark noise materially affected prior conclusions about model capability.

- **Construction of Ref-L4, a benchmark that addresses key limitations of current REC corpora.** Ref-L4 contains 4–6× more annotations, categories, expression length, and vocabulary than existing benchmarks (Table 3, Section 3.2). This fills a genuine gap: existing benchmarks are saturated (top models exceed 90% accuracy) and do not stress-test LMMs on long, diverse descriptions.

- **Comprehensive evaluation with scale-aware and per-category protocols.** The paper evaluates 24 models using Acc₀.₅, Acc₀.₇₅, Acc₀.₉, and mAcc, broken down by instance size (small/medium/large) and across 365 categories (Tables 4, 5; Figure 3). This reveals that even top models like CogVLM-Grounding perform poorly on certain common categories, providing actionable diagnostic information.

## Weaknesses

### Fatal
None.

### Major
- **The labeling error rate analysis lacks sufficient methodological transparency, yet these rates are foundational to the paper's first contribution.** The paper reports error rates of 14%, 24%, and 5% based on "manual examination" (lines 19, 58) but provides no details about the annotation protocol: number of annotators, annotation guidelines, inter-annotator agreement, or how disagreements were resolved. The error types are listed (typos, misalignment, inaccurate bounding boxes) but the judgment criteria are unspecified. While the paper references a section `sec:label_error` that was stripped by parsing, the presented paper does not establish that these rates are reliable rather than idiosyncratic. This matters because the cleaned benchmarks are released as a contribution — the community cannot assess how conservative or aggressive the cleaning was. The paper should at minimum describe the annotation process and report agreement statistics.

- **No human performance baseline on Ref-L4, making model scores hard to interpret.** The top model (CogVLM-Grounding) achieves 81.70% Acc₀.₅ and 66.09% mAcc, while GPT-4V achieves only 9.91% Acc₀.₅. Without human accuracy on a representative sample of Ref-L4, it is unclear whether the benchmark is genuinely challenging but solvable, or whether the long GPT-4V-generated expressions introduce ambiguity that makes the task ill-posed. For a new benchmark designed to replace existing ones, a human baseline is standard and important for calibration.

- **The quality and uniqueness of Ref-L4's long referring expressions are asserted but not systematically validated.** The paper states that in Step-3, human reviewers ensure each expression "uniquely describes the instance and is factual, accurate, and harmless" (line 145). However, no data is provided on what fraction of GPT-4V-generated expressions were rejected or modified during review, how often expressions were ambiguous across distractors, or whether the 24.2-word average descriptions function as referring expressions (uniquely identifying a target) rather than as general scene captions. The paper would benefit from a systematic analysis of expression ambiguity.

### Minor
- **GPT-4V's strikingly low performance (9.91% Acc₀.₅) is not discussed.** Since GPT-4V was used to generate the expressions, this raises natural questions: is the low score due to a suboptimal evaluation prompt, GPT-4V's architectural limitations for precise localization, or a genuine property of the benchmark? The paper should address this to help readers interpret the benchmark's difficulty.

- **The filtering criteria for Objects365 image selection (e.g., dimensions >800px, >10 categories, >20 instances) are presented without rationale** (line 139). While these choices are defensible, the paper does not discuss how they affect benchmark composition or whether they introduce bias toward particular scene types.

- **No limitations section.** The paper does not discuss limitations of Ref-L4 — e.g., reliance on GPT-4V for expression generation (which may carry its own biases), the restriction to Objects365 and COCO image domains, or the fact that most evaluated models were not trained on Objects365-style images, which could confound the "harder benchmark" interpretation with an "out-of-distribution" effect.

### Trivial
- None.

## Nice-to-Haves

- A human performance baseline on a 500–1000 sample subset of Ref-L4, which would calibrate the results.
- A random-sample validation study where human annotators judge whether each expression uniquely identifies its target among distractors, with reported agreement rates.
- Spearman rank correlation showing whether Ref-L4 produces different relative model rankings than RefCOCO/+/g, to support the claim that it measures something distinct.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that prompts are "described only in an appendix we cannot see"** — removed per instruction that the parser strips appendices; the prompts exist in the original submission.
- **Criticism that the paper doesn't "discuss whether instances from Objects365 are 'unique' in the sense of being distinguishable"** — the paper states that instances were "excluded if difficult to describe uniquely" (line 139), partially addressing this.
- **Criticism that the vocabulary/POS analysis is "shallow"** — this is an opinion about depth of analysis, not a factual weakness of the paper.
- **Criticism that the paper "does not analyze whether the expressions actually *require* spatial reasoning"** — this asks the paper to do more than it set out to do; the benchmark is designed for REC evaluation, not for attributing difficulty to reasoning types.
- **Comments about the paper needing to "explicitly separate" error correction from the harder benchmark contribution** — this is a framing suggestion, not a weakness; the paper already presents them as sequential contributions.

## Novel Insights

The reviews converge on a coherent picture: the paper makes a genuinely useful contribution (cleaned benchmarks, a large-scale challenging benchmark, broad model evaluation) but the evidentiary bar for two key aspects — the labeling error analysis methodology and the validity of the long expressions as referring expressions — is not fully met. The most important insight is that these are fixable gaps, not structural flaws. Neither reviewer disputes the existence of labeling errors or the value of a harder benchmark; rather, they seek stronger guarantees that the numbers are reliable and that the benchmark measures what it claims to measure. Separately, the GPT-4V performance anomaly (9.91% on expressions it helped generate) is an interesting puzzle that the paper passes over without comment — addressing it could sharpen the paper's diagnostic value considerably.

## Suggestions

1. **Provide annotation methodology for the error rate analysis.** Describe how many annotators were involved, the annotation guidelines, what constitutes each error type, and report inter-annotator agreement (e.g., Cohen's κ). If a third party adjudicated disagreements, state this. Even a brief paragraph would substantially increase trust.

2. **Add a human performance baseline on a 500–1000 sample subset of Ref-L4.** Report human Acc₀.₅ and mAcc on this subset using a standard bounding-box selection interface. This will calibrate the model results and demonstrate that the benchmark is solvable by humans.

3. **Provide statistics on the expression review process in Step-3.** Report what fraction of GPT-4V-generated expressions were accepted as-is, what fraction required modifications, and what fraction were rejected entirely. Include examples of ambiguous expressions that were caught and fixed.

4. **Discuss GPT-4V's low score.** Even a brief analysis — e.g., whether the evaluation prompt was the same format as the generation prompt, whether this is a known limitation of GPT-4V for dense localization, or whether GPT-4V struggles with its own generated text due to distribution shift — would help readers interpret the results.

5. **Add a limitations section.** Discuss the reliance on GPT-4V, the domain scope (COCO + Objects365), potential bias in the filtering criteria, and whether the benchmark's difficulty partly reflects distribution shift rather than inherent complexity.

## Score and Decision

The paper addresses a real need, makes concrete contributions (cleaned benchmarks, Ref-L4, broad model evaluation), and is clearly written. The main weaknesses — insufficient methodological detail for the error analysis, no human baseline, and unvalidated expression quality — are fixable with additional analysis and transparency rather than structural rework. The paper would be strengthened by addressing these points but makes a solid contribution even as-is.

**Originality**: 7/10 — identifying errors in existing benchmarks and building a harder benchmark is valuable, though the individual components (error analysis, larger dataset, model evaluation) are established practices.

**Importance**: 8/10 — REC evaluation needs updated benchmarks; existing ones are saturated.

**Claims well supported**: 6/10 — the error rate claims need stronger methodology; the Ref-L4 evaluation is well-executed.

**Soundness**: 7/10 — generally sound, with the noted caveats.

**Clarity**: 8/10 — well-structured and readable.

**Value**: 8/10 — cleaned benchmarks and Ref-L4 are practically useful resources.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>