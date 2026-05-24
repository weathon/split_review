Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper defines and systematically evaluates **Cognition and Perception (C&P) knowledge conflicts** in MLLMs — inconsistencies between what a model "sees" (its OCR/perceptual output) and what it "says" (its VQA/cognitive output) on document understanding tasks. Evaluating five MLLMs across six datasets, the authors find that even GPT-4o achieves only 68.6% C&P consistency, with open-source models below 20%. To mitigate this, they propose a three-stage fine-tuning method (Perception Consistency, Cognition Consistency, and a C&P Connector) that improves C&P consistency by 34–43 percentage points across three open-source MLLMs while generally maintaining or improving original task performance.

## Strengths

1. **Novel problem definition with clear formalization.** Section 2.1 formally defines C&P knowledge conflicts using the criterion \(y_C \subseteq y_P\), providing an operationally clean way to measure cross-task consistency. This distinguishes the work from prior hallucination research (which examines conflicts *within* a single modality) by targeting conflicts *between* perception and cognition.

2. **Large, consistent improvements across multiple models and datasets.** Table 3 shows that the proposed method raises C&P consistency from 19.41% → 54.24% for Qwen-VL-Chat, 12.09% → 49.94% for InternVL2-2b, and 16.87% → 60.03% for InternVL2-8b — absolute gains of 34–43 percentage points across all three open-source MLLMs. These improvements hold across all six individual datasets (Table 2).

3. **Comprehensive evaluation covering diverse document types.** Six datasets span Document QA (DocVQA), Information Extraction (DeepForm, KLC, FUNSD), Chart QA (ChartQA), and Table QA (WTQ), demonstrating that the conflict and its mitigation generalize across different document formats and task types.

4. **Ablation study validates each component's contribution.** Table 4 isolates each fine-tuning stage: removing Perception Consistency drops average C&P consistency by 14.79% (39.45% → 54.24%), while removing the C&P Connector drops it by 1.06%, confirming each component contributes to the overall effect.

## Weaknesses

### Fatal
None.

### Major

1. **No out-of-distribution / held-out evaluation.** The method is trained on the training splits of all six datasets and evaluated on their test splits. There is no experiment holding out one or more datasets entirely to test whether the method learns generalizable consistency behavior rather than dataset-specific patterns (e.g., quirks of a particular OCR engine's bounding-box distributions or question templates). The paper mentions a limitation only about "focus solely on document understanding" (Conclusion), but this is a narrower concern: even within document understanding, generalization across datasets is not tested. For a method that claims to mitigate a general problem, within-distribution evidence is necessary but not sufficient.

2. **Closed-source evaluation uses a protocol inconsistent with open-source evaluation.** For GPT-4o and Qwen-VL-Max, the perceptual query is posed by drawing a red bounding box on the image (Set-of-Mark prompting) because the models' bounding-box input formats are not publicly documented. Open-source models receive structured bounding-box input in their native format. This means the closed-source models face a fundamentally different perceptual task — interpreting a visual marker rather than receiving structured spatial coordinates — which likely depresses their measured C&P consistency. The paper acknowledges this difference (Section 3.3), but the abstract and introduction highlight the closed-source numbers (68.6%, 79.98%) as motivating evidence without sufficient caveat. The core fine-tuning experiments use only open-source models with consistent protocols, so this does not invalidate the main results, but the motivating comparisons are weaker than claimed.

3. **Massive training data imbalance across stages is not controlled in ablation.** Stage 1 (Perception Consistency) uses 2,189k samples, while Stage 2 (Cognition Consistency) uses 176k and Stage 3 uses 146k. The paper notes that Stage 1 uses "all text and their corresponding bounding boxes from the entire image, resulting in M ≫ N" (Section 5). In the ablation (Table 4), removing Perception Consistency causes a 14.79% drop, while removing Cognition Consistency causes only a 0.44% drop. These differences are at least partially attributable to the order-of-magnitude larger training budget for Stage 1 rather than to an inherent primacy of perceptual over cognitive consistency. The paper attributes the dominant Perception Consistency effect to "limited perception capabilities of open-source MLLMs" (Section 6.3), but this confound is not addressed.

### Minor

1. **The C&P Connector contributes only 1.06% on average.** In the ablation (Table 4, rows 3 vs. 4), the full method (54.24%) barely outperforms the variant without the Connector (53.18%), and on three of six datasets (DeepForm, KLC, WTQ) the variant *without* the Connector performs better. The paper acknowledges this small gain (Section 6.3) but the narrative emphasis on "connecting cognitive and perceptual knowledge" as a key contribution is disproportionate to the empirical support. The evidence better supports a reframing centered on the Perception Consistency task as the primary driver.

2. **Evaluation data construction introduces potential selection bias.** The construction process (Section 3.3) filters out QA pairs whose answer does not appear in third-party OCR annotations — both because the question type is non-locatable (comparisons, yes/no) and because OCR engines may miss text. The paper reports this filtering but does not characterize the filtered-out cases (e.g., what fraction are removed per dataset, whether they involve systematically harder examples like small/rotated text). If the filter disproportionately removes cases where perception is difficult, the evaluation set over-represents easy examples, potentially overestimating consistency for all models. This does not invalidate relative comparisons but the absolute numbers (e.g., 68.6% for GPT-4o) should be interpreted with this caveat.

3. **No confidence intervals or variance estimates.** All fine-tuning results are reported as single-run point estimates without multiple seeds or statistical tests. Given that the C&P Connector gain is only 1.06%, the difference could be within run-to-run noise.

4. **Minor numerical inconsistency.** The introduction (line 34) states GPT-4o achieves "69.60%" consistency, but both the abstract (line 11) and Table 1 report 68.60%. This appears to be a typo in the introduction.

### Trivial
- The templates (Temp_CV, Temp_PV, TempQ_Conn, TempR_Conn) are referenced but their exact wording is not provided; including them (e.g., in an appendix) would improve reproducibility.
- Some cognitive task declines on InternVL models (DocVQA: −2.4%, ChartQA: −1.0 to −2.1%) are mentioned but not analyzed (e.g., whether declines concentrate on complex questions).

## Nice-to-Haves
- **Leave-one-out evaluation.** Training on five datasets and testing on the held-out sixth would directly test generalization and strongly strengthen the claims.
- **Per-sample analysis of C&P Connector mechanism.** Categorizing samples into (both correct, both wrong, cognitive-right/perceptual-wrong, cognitive-wrong/perceptual-right) before and after fine-tuning would clarify what the Connector actually resolves, beyond aggregate consistency.
- **Controlled ablation balancing training data quantity.** Subsampling Stage 1 to match Stage 2's size in the ablation would disentangle task design from data quantity.
- **Analysis of perceptual task failure modes.** Understanding *why* baseline OCR is so low (e.g., 13.9% for InternVL2-2b on DocVQA) — whether the model reads wrong regions or cannot read at all — would clarify whether C&P conflicts primarily stem from perception failures or genuine cross-task misalignment.

## Removed Points
- **"Baseline OCR is broken, undermining the narrative"** — The critic claims that very low baseline OCR performance (e.g., 13.9% for InternVL2-2b) means the conflict is "partially because perception is simply broken." This misunderstands the paper's framing: C&P conflicts are defined as a *consistency* gap between two model outputs, regardless of whether either output is correct. The paper's own Table 5 reports these baselines transparently. A low perceptual accuracy does not "undermine" the concept of cross-task inconsistency; it simply documents one reason why consistency is low.
- **"The 'first to identify' claim should be tempered"** — The paper already hedges with "To the best of our knowledge" and distinguishes C&P conflicts from hallucination work (which examines conflicts *within* cognition or perception, not *between* them). This is a reasonable claim.
- **"Pure formatting/style nitpicks"** and **"Typos/spelling/grammar"** — These are parser artifacts or minor issues not relevant to evaluation.
- **"Missing related works"** — Cannot be verified without external sources.
- **"Reproducibility: hyperparameters not fully disclosed"** — The paper states learning rate (1e-5), batch size (128), 1 epoch, 8 A100 GPUs, and that other hyperparameters remain at default. This is adequate for the field's standards.
- **"Missing appendix"** — The parser strips appendix content; it exists in the original submission.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the paper's authors have not already considered or addressed to some degree.

## Suggestions
1. **Add a leave-one-dataset-out evaluation** to demonstrate that the method learns generalizable consistency behavior rather than dataset-specific patterns. With six datasets available, holding out one for testing is straightforward and would significantly strengthen the generalization claims.
2. **Reframe the contribution** to better match the evidence: the primary driver is the Perception Consistency task (which is largely about improving the model's ability to read text from bounding boxes). The C&P Connector should be presented as a small additive component rather than the centerpiece of "connecting" the two knowledge types.
3. **Add confidence intervals** (e.g., 3 random seeds) for all fine-tuning results, especially given the 1.06% Connector gain that could be within noise.
4. **Provide the exact templates** (Temp_CV, Temp_PV, TempQ_Conn, TempR_Conn) in the paper or supplement for reproducibility.
5. **Characterize the filtered-out data** in the evaluation construction to establish how selection bias may affect absolute consistency numbers.

## Score and Decision

**Score: 6.5** — The paper identifies a meaningful problem, evaluates it systematically, and presents a method with large empirical improvements. The main weaknesses (no OOD generalization test, closed-source evaluation inconsistency, ablation confound from data imbalance) are substantive but not fatal. The within-distribution results are strong and the contribution is clearly scoped. With the addition of a held-out evaluation and more careful framing, this would be a stronger paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>