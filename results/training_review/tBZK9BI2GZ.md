I now have all the information needed. Let me compile the final consolidated review.

## Summary

The paper introduces the concept of *Cognition and Perception (C&P) knowledge conflicts* — inconsistencies between an MLLM's VQA answer (cognitive) and its OCR output (perceptual) for the same text in document images. It systematically measures these conflicts across five MLLMs (including GPT-4o and Qwen-VL-Max) on six document understanding datasets, finding that even GPT-4o achieves only 68.6% C&P consistency and open-source models fall below 20%. To mitigate the problem, the authors propose *Multimodal Knowledge Consistency Fine-tuning*, a three-stage training approach (Perception Consistency → Cognition Consistency → C&P Connector) that improves C&P consistency by 34–43 absolute points across three open-source models while generally maintaining or improving task accuracy.

## Strengths

1. **First systematic measurement of cross-task inconsistency in document MLLMs**: The paper provides a clear, reproducible methodology for constructing paired (VQA, OCR) queries from existing benchmarks and defines a formal C&P consistency metric (Eq. 1–2). The evaluation across 5 models × 6 datasets reveals that even GPT-4o and Qwen-VL-Max exhibit substantial inconsistencies (31.4% and 20.0% conflict rates respectively, Table 2), establishing the practical significance of the problem.

2. **The proposed fine-tuning method yields large, consistent improvements**: Across all three open-source models (Qwen-VL-Chat, InternVL2-2B, InternVL2-8B) and all six datasets, C&P consistency rises by 34–43 absolute percentage points (Table 3). The gains are consistent across architectures and model sizes, demonstrating general applicability.

3. **Task performance does not degrade and often improves**: Table 5 shows that the method improves or maintains cognitive task metrics (ANLS, F1, accuracy) while dramatically improving perceptual (OCR) performance (e.g., Qwen-VL-Chat OCR ANLS on DocVQA from 22.7% to 74.2%). This addresses the practical concern that consistency gains might come at the cost of raw task accuracy.

4. **Informative ablation study**: The ablation (Table 4) transparently quantifies each component's contribution, showing that the Perception Consistency task provides the largest individual gain (14.79%), while the Cognition Consistency and C&P Connector tasks contribute smaller but non-trivial improvements (0.44% and 1.06%). The paper acknowledges the perception task's dominance, lending credibility to the analysis.

## Weaknesses

### Fatal
None.

### Major

1. **The conceptual claim of a novel "knowledge conflict" is oversold relative to the evidence.** The paper defines C&P conflicts as mismatches between cognitive (VQA) and perceptual (OCR) outputs. However, the ablation shows that the Perception Consistency task accounts for ~42% of the total gain, and the paper itself notes that "the perception consistency task demonstrates the largest gain, likely due to the limited perception capabilities of open-source MLLMs" (Section 5.3). While the reviewer's claim that the improvement is "almost entirely driven by fixing broken perception" is factually overstated — the non-perception components (Cognition Consistency + C&P Connector) still improve C&P consistency from 19.41% to 39.45% even without any perception training — the framing of a distinct "knowledge conflict" between two separable knowledge systems (K_C and K_P) is never independently validated. The paper does not demonstrate a scenario where perception is accurate but cognition conflicts (the genuine "conflict" scenario), nor does it measure K_C and K_P independently of the model's outputs. The contribution would be more honestly framed as improving cross-task consistency in document MLLMs rather than introducing a new category of knowledge conflict.

2. **Evaluation lacks a held-out generalization test.** The method is trained and evaluated on the same six datasets. With Stage 1 using 2,189k training samples, there is a risk that the model memorizes query patterns rather than genuinely improving cross-task consistency. No out-of-distribution evaluation is performed on a held-out document understanding dataset (e.g., SROIE, CORD) or on a different visual domain. The paper acknowledges this focus on document understanding in the conclusion but does not provide any generalization test.

3. **No comparison to simpler baselines.** The paper does not compare its three-stage method against a single-stage perception-only fine-tuning baseline (e.g., supervised fine-tuning on OCR data without any consistency or connector tasks). Such a baseline would directly test whether the complexity of the three-stage approach is justified over a simpler alternative. The ablation partially addresses this, but an independent baseline with equivalent training data would strengthen the claims.

### Minor

1. **Extent and representativeness of evaluation data filtering is not reported.** Section 2.3 describes keyword-based filtering (removing yes/no, comparison questions) and filtering due to OCR annotation mismatches, but the paper does not report how many samples were removed per dataset, nor does it analyze whether the remaining subset is representative of the full dataset. If filtering systematically removes harder cases (e.g., multi-word answers, reasoning-heavy questions), the reported consistency numbers may be inflated. Table 1 reports final evaluation counts but not the original dataset sizes or filtering ratios.

2. **No analysis of the perception-correct-but-cognition-wrong scenario.** The paper's framing implies a genuine conflict between two knowledge systems, but it never analyzes how often perception is correct while cognition produces a conflicting answer (the scenario that would most directly support the "knowledge conflict" framing over the simpler "poor OCR" interpretation). A 2×2 confusion matrix (perception correct/wrong × cognition correct/wrong) for each model before and after fine-tuning would clarify the nature of the conflicts being resolved.

3. **The C&P Connector contributes minimal improvement (1.06%)** and is structurally similar to the perception consistency task (both are two-option verification questions about bounding boxes). The paper's claim that it "creates a bridge between cognitive and perceptual knowledge" is not strongly supported by the marginal gain.

4. **Cognitive and perceptual task consistency metrics (C and P in Table 3) saturate at 98–99% after fine-tuning.** While these measure self-consistency (whether the model agrees with its own answers), not raw task accuracy, the near-ceiling levels suggest the validation query patterns may be memorized. The paper does not discuss whether these high numbers would generalize to novel validation query templates.

### Trivial
None beyond normal presentation preferences.

## Nice-to-Haves

- A perception-only fine-tuning baseline to contextualize the three-stage method's benefit.
- Out-of-distribution evaluation on a held-out document understanding dataset.
- Reporting the number of QA pairs filtered out per dataset during evaluation sample construction.
- A 2×2 confusion matrix (perception accuracy × cognition accuracy) showing what fraction of conflicts arise from each failure mode.
- Qualitative error taxonomy for persistent errors after fine-tuning.

## Removed Points

- The claim that "the C&P consistency improvement is almost entirely driven by fixing broken perception" — This is factually inaccurate. Without any perception training (Row 1 of ablation, Cog+Conn only), C&P consistency rises from 19.41% to 39.45%, recovering more than half of the total gain (~20 out of ~35 points). The perception task contributes the largest single component (~15 points), but the improvement is not "almost entirely" driven by perception.
- The criticism that the Doral/Doraf example is "indistinguishable from a standard hallucination" — The paper explicitly distinguishes its focus from hallucination research (line 35): hallucination research examines conflicts within a single output modality, while this work examines conflicts between two outputs (OCR and VQA) for the same ground truth. Whether one finds this distinction persuasive is a matter of framing, not factual error.
- The request for comparison against LRV-Instruction and VIGC — These are general hallucination mitigation methods designed for different problem settings. The paper's method targets a specific cross-task inconsistency not addressed by these methods. A fair comparison would require adapting them to the C&P consistency setting, which is beyond the paper's stated scope.
- Comments about missing related work on object hallucination (Pope et al., Gunjal et al., Zhou et al.) — The paper already discusses hallucination in its Related Work section with appropriate citations.
- The speculation that the "cognitive/perceptual task consistency near-ceiling suggests the model has memorized validation query patterns" — This conflates the GV-style self-consistency metric (does the model validate its own answer?) with standard task accuracy. The C and P metrics in Table 3 are inherently about self-consistency within the GV framework and are expected to be high after fine-tuning. The actual task performance (Table 5) shows realistic, non-ceiling numbers.
- Dataset variation analysis requests — The paper's speculation about DeepForm's layout is acknowledged as speculation, not a rigorous claim.

## Novel Insights

None beyond the paper's own contributions. The existing reviews largely converge on the same assessment: the paper tackles a real and measurable problem with an effective method, but oversells the conceptual novelty of "knowledge conflicts" versus the more straightforward interpretation of improving cross-task consistency in document understanding.

## Suggestions

1. **Reframe the contribution.** The paper's strongest contribution is not a fundamentally new category of knowledge conflict, but rather (a) a systematic framework for measuring cross-task (OCR vs. VQA) inconsistency in document MLLMs, and (b) an effective fine-tuning method for improving this consistency. Reframing the paper around "measuring and mitigating cross-task inconsistency" rather than "a novel form of knowledge conflict" would align the claims with the evidence and strengthen the paper.

2. **Add a perception-only baseline.** Fine-tune models on only the perception consistency data (Stage 1 data alone) and measure C&P consistency improvement. This would directly test whether the three-stage structure is necessary.

3. **Add a held-out evaluation.** Test on at least one document understanding dataset not seen in training (e.g., SROIE, CORD) to demonstrate generalization.

4. **Report filtering statistics and analyze representativeness.** Show how many samples were filtered per dataset and compare the filtered subset to the original on dimensions like answer length and question type.

5. **Add a 2×2 error analysis.** Show, for each model before and after fine-tuning, how often perception is correct/wrong crossed with cognition correct/wrong. This would reveal what fraction of C&P conflicts arise from each failure mode and directly address the concern that the problem is "just poor OCR."

## Score and Decision

The paper makes a real empirical contribution — a systematic cross-task consistency benchmark for document MLLMs and an effective mitigation method with large, reproducible gains. However, the conceptual framing is oversold, the evaluation lacks some standard baselines and held-out testing, and several analyses that would substantiate the "knowledge conflict" narrative are missing. These are addressable weaknesses, and the core empirical findings are valuable.

**Originality**: Moderate. The problem framing has conceptual novelty but is more incremental than claimed. The method adapts the Generator-Validator framework to the document understanding setting.

**Quality**: Good. The experiments are extensive (5 models, 6 datasets, 3 open-source fine-tuned models). The ablation study is informative. Missing baselines and held-out evaluation lower the rigor.

**Clarity**: Good. The paper is well-written and the problem definition is clear.

**Significance**: High for the document understanding community. The finding that even GPT-4o exhibits 31% cross-task inconsistency is practically important, and the mitigation method provides a useful tool.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>