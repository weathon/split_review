Now I'll produce the final consolidated review.

## Summary

LongHalQA introduces a benchmark (~6,485 multiple-choice questions) for evaluating long-context hallucinations in MLLMs, built via an automated pipeline (LongHallGen) using GPT-4V to generate image descriptions and conversations, detect hallucinations, and construct two task formats: hallucination discrimination (detect + explain hallucinations) and hallucination completion (select the non-hallucinatory continuation). The paper evaluates ten MLLMs and reports findings including that Chain-of-Thought degrades performance on long-context discrimination tasks.

---

## Strengths

- **Unified discriminative and generative evaluation in MCQ format, eliminating LLM evaluators at evaluation time.** The completion task transforms generative hallucination evaluation into a multiple-choice format, avoiding the cost and instability of LLM-as-judge approaches (Section 3.1, lines 48–50). The paper validates this by showing that MCQ-based rankings are broadly consistent with free-form generation rankings (Tab. 4/9: Qwen2-VL-72B #1 in both, LLaVA-1.6-34B #2 in both, Fuyu-8B #9 in both), while being dramatically faster (Fig. 7/4).

- **Text substantially longer and more diverse than existing hallucination benchmarks.** LongHalQA's image-level descriptions average 130 words and multi-round conversations average 189 words, compared to ~80 words in prior generative benchmarks. The benchmark also covers ~4K object names versus the fixed 80 COCO categories in POPE/CIEM (Section 3.2, line 101).

- **Novel finding that Chain-of-Thought degrades performance on long-context hallucination discrimination.** Tab. 8 (Section 5.4) shows that CoT, previously shown to mitigate hallucinations on short queries, causes most MLLMs to drop on long-context discrimination (e.g., LLaVA-1.6-34B drops 11.84 points in mc-ACC). This is a non-obvious empirical finding.

- **12-category hallucination taxonomy extending beyond object existence/attributes.** The taxonomy (Tab. 1) includes under-explored types such as Text/Sign Meaning (H8), Environment (H9), Background (H10), Time (H11), and Weather (H12), including complex logic-level hallucinations (Section 3.2, lines 96–98).

- **LongHallGen pipeline is a reproducible methodology for future benchmark construction.** The pipeline (Section 4, lines 108–151) details image collection/filtering from VisualGenome/Objects365, GPT-4V-based generation, hallucination checking (self-check + GroundingDINO verification + manual revision), and MCQ construction.

---

## Weaknesses

### Major

- **Insufficient independent validation of the benchmark's ground truth against GPT-4V's internal hallucination patterns.** The benchmark construction pipeline (Section 4) relies on GPT-4V to: (a) generate long texts, (b) self-check those texts for hallucinations, (c) produce hallucination-explanation pairs, and (d) formulate questions and answer options. GroundingDINO provides some external object-level verification, and human revision is mentioned as "optional" (line 151), but no systematic human validation study is conducted on the final benchmark data. The paper acknowledges (line 240–241) that GPT-4o's strong performance "suggests GPT's potential capability of self-correction for hallucinations, given that the LongHalQA is primarily based on hallucination data from GPT." This concern is not resolved. For a benchmark that claims to measure hallucination relative to ground-truth image content (rather than alignment with GPT-4V's hallucination patterns), independent human validation on even a 200–500 sample subset would dramatically strengthen the contribution.

- **Validation of the MCQ format as a proxy for generative evaluation is underpowered.** Section 6 (lines 308–340) compares MCQ accuracy with free-form generation accuracy on only 400 total samples (200 per condition). The rankings show notable discrepancies (LLaVA 1.6-7B ranks #5 in MCQ but #3 in free-form; MiniCPM-V2 ranks #4 in MCQ but #5 in free-form). No statistical tests are reported, and the absolute accuracy values differ substantially (e.g., LLaVA 1.5-7B: 36.08% MCQ vs 52.50% free-form). The claim that rankings are "largely consistent" overstates what the data support.

- **No comparison with existing hallucination benchmarks.** The paper never evaluates the same models on POPE, CHAIR, AMBER, or other established benchmarks, so the reader cannot determine whether LongHalQA captures a distinct or complementary signal. For a new benchmark claiming to address limitations of prior work, showing that model rankings on LongHalQA diverge from existing benchmarks would establish its distinctiveness empirically.

### Minor

- **"Long-context" framing is oversold for ~21% of the data.** Object-level descriptions average only 14 words (line 101), which is shorter than existing generative benchmarks (~80 words). The remaining 79% (image-level descriptions at 130 words and conversations at 189 words) is genuinely long, but the abstract and framing imply the entire benchmark is long-context. Disaggregating results and claims by text length would be more accurate.

- **"LLM-free" in the abstract is imprecise.** The paper clarifies (line 23) that the benchmark avoids LLM evaluators *at evaluation time*, but the abstract's "LLM-free hallucination benchmark" (line 4) could mislead readers into thinking the construction is also LLM-independent. Rephrasing to "LLM-evaluator-free" would be more accurate.

- **No statistical significance measures reported.** The paper presents all results as point estimates without confidence intervals or significance tests. Given that several model comparisons differ by just a few percentage points (Tab. 1 overall results: Qwen2-VL-72B at 55.55 vs LLaVA-1.6-34B at 53.47), it is unclear which differences are reliable.

- **No human baseline.** Reporting human accuracy on a subset of the benchmark would calibrate how difficult the task actually is, especially given that some models perform near the 25% random baseline.

- **CoT analysis oversimplifies exceptions.** Tab. 8 shows that Qwen2-VL-72B improves on long-context binary accuracy by +6.34 with CoT, and several small models also see average improvements (LLaVA-1.5-7B +1.2, LLaVA-1.5-13B +1.45). The paper's claim that CoT "degrades the performance of most MLLMs" (line 25) is true for most but the exceptions are notable and deserve more discussion.

- **Per-image variance not reported.** With 1,200 images generating 6,485 questions, some images contribute many samples. Without clustering standard errors or reporting per-image variance, the results could be dominated by a small number of images.

### Trivial

- The paper refers to "LongHalOA" (typo) in the Section 6 header (line 308).

---

## Nice-to-Haves

- A human validation study on 200–500 samples to establish ground truth independently of GPT-4V.
- Correlation analysis of model rankings on LongHalQA vs. POPE, CHAIR, and other benchmarks to establish distinctiveness.
- Disaggregated analysis by text length (object-level vs. image-level vs. conversation), especially since Fig. 4 (Tab. 3 binary results) shows dramatic accuracy drops from object-level to longer contexts — this could be the paper's most important finding.
- Deeper discussion of data contamination given that many MLLMs may have been trained on VisualGenome/Objects365 validation images.

---

## Removed Points

These points were flagged during the merge process and are reproduced here for transparency only; they should not be relied upon as valid criticisms.

- **"GPT-4V is the sole source of ground truth" (Harsh Critic).** The pipeline also uses GroundingDINO for tool-based verification and manual revision (line 116). The critic's characterization is an overstatement.
- **Missing prompt templates in the main paper.** Per instruction, appendix sections are stripped from all papers by the parser; these exist in the original submission.
- **Asymmetric MCQ structure (1 correct / 3 incorrect) is a weakness.** This is a standard MCQ design with a clear 25% random baseline. It does not constitute a flaw.
- **"LLM-free" as a fatal framing issue.** The paper clarifies in context that this refers to evaluation, not construction. It is a minor imprecision, not a structural flaw.
- **Generic concerns about "could be measuring a proxy" or "confounders not controlled."** These are area-of-concern sweeps rather than specific identified problems anchored to paper content.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem," "targeted an interesting question") have been removed as superficial.

---

## Novel Insights

The two reviews present a tension that is informative: the Harsh Critic's most forceful claim — that the benchmark is "a study of alignment with GPT-4V's hallucination patterns" — is partially countered by the paper's use of GroundingDINO object detection and manual revision as independent checks. However, neither reviewer fully explored what this actually means for interpretation of results. If the benchmark primarily measures alignment with GPT-4V's hallucination style, then the finding that Qwen2-VL-72B outperforms GPT-4o on the completion task (61.50 vs 56.15) becomes *more* interesting: it suggests Qwen2-VL-72B is better at avoiding hallucinations that *GPT-4V itself produces*, which is a non-trivial capability. Conversely, the finding that smaller models with RLHF (MiniCPM-V2, Qwen2-VL-2B) outperform larger ones suggests that training intervention matters more than model scale for hallucination robustness, which is a valuable signal regardless of GPT-4V dependency. The real missed opportunity is that neither the paper nor the reviews tackle the question at the level of *which hallucination types* are most contaminated by GPT-4V's own biases — object hallucination (H1) could be independently verified by GroundingDINO, while environment/weather hallucinations (H9–H12) cannot. A per-type validity analysis would be far more impactful than a blanket circularity concern.

---

## Suggestions

1. **Conduct a human validation study on 300–500 samples** to establish: (a) whether the hallucinatory text actually contains a hallucination relative to the image, and (b) whether the designated correct answer is uniquely correct. Report per-hallucination-type agreement.
2. **Evaluate the same model suite on POPE, CHAIR, or AMBER** and report rank correlations. This is essential for a benchmark paper to demonstrate that LongHalQA captures something distinct.
3. **Disaggregate all results by text length** (object-level vs. image-level vs. conversation). The dramatic accuracy drops in Tab. 3 (binary answers) are the paper's most striking finding and should be the centerpiece.
4. **Report confidence intervals or bootstrapped standard errors** for all main results, especially the MCQ-vs-generative comparison.
5. **Reframe "LLM-free" to "LLM-evaluator-free"** throughout the paper, and clearly qualify that the long-context claim applies primarily to image-level descriptions and conversations, not object-level descriptions.
6. **Provide the full prompt templates** (in the appendix or supplementary) to make LongHallGen reproducible.

---

## Score and Decision

**Score:** 5.0

**Decision:** Reject

**Rationale:** LongHalQA addresses a genuine gap — existing hallucination benchmarks use short, simple queries or costly LLM evaluators — and the paper's empirical findings about long-context hallucination (especially the CoT degradation and the dramatic accuracy drops from short to long text) are interesting and non-obvious. However, as a benchmark paper at a top venue, the validation is incomplete in three critical ways that together justify rejection: (1) the heavy GPT-4V dependency is not resolved by independent human validation or a systematic analysis of which hallucination types are externally verifiable; (2) the central claim that MCQ format faithfully captures generative capability rests on only 400 samples with notable ranking discrepancies and no statistical tests; (3) the paper provides no comparison to existing benchmarks, making it impossible for the community to calibrate what LongHalQA adds. These are addressable weaknesses, and a revised version with human validation, benchmark comparisons, and stronger statistical grounding could be a strong paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>