Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces CAD-Editor, the first model for text-based CAD editing. It formulates the task as sequence-to-sequence prediction using an LLM (LLaMA-3-8B) backbone, where the input is a concatenation of a textual instruction and a CAD command sequence, and the output is an edited CAD sequence. To overcome the absence of naturally occurring data, the authors construct a synthetic training set (92k examples) by combining design-variation generation models (SkexGen, Hnc-CAD) with GPT-4o multi-level captioning, followed by a selective-data refinement stage (via D-CLIP or human feedback) using the model's own high-quality outputs. CAD-Editor achieves a 91.4% valid ratio, 0.21 D-CLIP score, and 31.1% human evaluation success rate, substantially outperforming GPT-4o prompting baselines.

## Strengths

- **Novel task formulation as sequence-to-sequence for text-controlled CAD editing.** The paper defines text-based CAD editing as predicting an edited CAD sequence from the concatenation of a textual instruction and the original CAD sequence (Sec. 3.1). The tailored CAD sequence representation (variable-length, textual tokens for both categorical and numerical variables) is a practical design that enables LLMs to process CAD commands. This formulation directly addresses the lack of user control in prior design-variation generation work (SkexGen, Hnc-CAD).

- **Synthetic data pipeline that productively combines complementary existing models.** The paper constructs a large paired dataset by using SkexGen and Hnc-CAD to produce CAD model pairs and GPT-4o with multi-level captioning to generate textual editing instructions (Sec. 3.2). The multi-level captioning strategy (describe → identify differences → compress) empirically improves quality over naive captioning, as shown in the ablation on the 10k subset (Table 2: CAD-Editor-mini w/MLC vs. w/BC shows higher COV, lower MMD/JSD, better D-CLIP, and higher Valid Ratio).

- **Selective-data refinement demonstrably improves instruction alignment.** The two-stage fine-tuning pipeline (Sec. 3.3) samples multiple outputs from the initially fine-tuned model and selects the best ones via D-CLIP (DCF) or human feedback (HF). The ablation on the 10k subset shows D-CLIP improving from 0.16 (w/o) to 0.26 (w/DCF) and 0.28 (w/HF), validating that this refinement step meaningfully improves text-to-CAD alignment.

- **Consistent quantitative and qualitative superiority over GPT-4o baselines.** CAD-Editor achieves a 91.4% valid ratio (vs. 24.5% and 23.3% for GPT-4o), D-CLIP of 0.21 (vs. −0.65 and −0.01), and a human evaluation score of 31.1% (vs. 2.5% and 9.2%). Qualitative results (Figures 4–8) illustrate diverse and controlled edits including deletion, addition, local/global changes, and iterative editing, corroborating the quantitative advantages.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation is conducted entirely on machine-generated instructions, not human-written natural language.** The test set instructions are produced by GPT-4o (following the same pipeline as training data) and then human-verified for correctness (Sec. 4.1). While the instructions are accurate descriptions of the CAD pair differences, they carry GPT-4o's phrasing biases and vocabulary, which closely match the training distribution. The human evaluation (Sec. 4.2) also uses these same machine-generated instructions. The paper's framing promises "text-based editing" broadly — implying arbitrary natural language — yet never exposes the model to organically human-written instructions. The Conclusion acknowledges the limitation for generalization ("our method's ability to generalize to new edits... is limited by the ability of GPT-4o to generate instructions") but does not address the fact that even the evaluation itself remains within GPT-4o's language distribution. This means the reported D-CLIP (0.21) and Human Eval (31.1%) may overestimate performance on real user language. For a paper introducing a new task, this is a reasonable starting point, but the claims of generality are currently unsupported.

### Minor

- **No failure analysis for the 69% of outputs rated unsuccessful by humans.** The human evaluation reports a 31.1% success rate — far better than GPT-4o baselines but still meaning that roughly two thirds of outputs are unsatisfactory. The paper does not categorize or analyze common failure modes (e.g., instruction misinterpretation, wrong shape/location, quality issues). Such analysis would clarify where the model's weaknesses lie and is important for guiding future work on this new task.

- **Ablation of selective data is only on a 10k subset, not the full 92k model.** Table 2 compares CAD-Editor-mini variants (trained on a 10k subset). The full model (Table 1) is only reported as the final CAD-Editor (D-CLIP 0.21). Without a full-model ablation that removes the selective-data stage, the reader cannot directly attribute how much of the final improvement comes from the selective-data refinement vs. simply having more (92k) synthetic data. Adding one training run to isolate this would cleanly separate the two contributions.

- **D-CLIP is used both as a selection criterion (for building the selective dataset) and as an evaluation metric.** The model is fine-tuned to maximize D-CLIP via selective data selection, and D-CLIP is then reported as a measure of text-CAD alignment. This creates a potential bias. The paper acknowledges "better metrics may be needed" but does not discuss this circularity. The presence of human evaluation and point-cloud metrics partly mitigates the concern, but D-CLIP scores should be interpreted with caution.

- **Missing details about the selective dataset.** The paper does not report the size of $\mathcal{D}_{\text{selective}}$, how many samples per input were generated for selection, or whether the same test set examples could appear in the selective data (data leakage risk). These details are needed for reproducibility.

- **No quantitative evaluation of captioning quality.** The multi-level captioning strategy is a key component of data generation (Sec. 3.2), but there is no human evaluation of whether the generated instructions correctly describe the change between CAD pairs. A simple audit on a sample of captions would quantify the noise injected into the synthetic training set.

### Trivial
None.

## Nice-to-Haves

- **A small test set (50–100 examples) with human-written instructions** (e.g., crowdsourced from non-experts) would directly address the core concern about evaluation generality and turn the paper's contribution from "editing with machine-generated descriptions" to "editing with natural language."
- **A failure analysis categorizing the 69% unsuccessful outputs** into types (instruction misinterpretation, wrong shape/location, quality failure, etc.) would strengthen the paper's contribution to the community and guide future work.
- **Reporting the proportion of CAD pairs discarded at each filtering stage** (cosine similarity thresholds, sequence-level filtering) would help assess data quality.

## Removed Points

These points were flagged by the reviewers but are removed after cross-checking against the paper:

- *"GPT-4o three-shot baseline uses training-set instructions (GPT-4o outputs) as in-context examples, which is unfair."* — This is a reasonable baseline: it shows that even when GPT-4o is given its own generated examples as demonstrations, it still cannot perform the task. If anything, this strengthens the authors' results. Removed as not a valid weakness.

- *"Potential data leakage from test set construction — test CAD pairs generated by same variation models as training data."* — The test set is sampled from the DeepCAD *test* split, and training data uses models from the training split. Base CAD shapes are held out. This is standard practice and not a genuine leakage concern. Removed as speculative.

- *"Paper overstates the 31.1% human evaluation result in abstract/conclusion."* — The paper reports the 31.1% number transparently and contextualizes it against GPT-4o baselines (2.5%, 9.2%). The abstract states "demonstrate the advantage," which is factually true. The framing is acceptable for a first-task paper. The *lack of failure analysis* is retained as a Minor weakness; the "overstating" framing is removed.

- *Strength Finder: "Strong quantitative and human-evaluation results demonstrate superiority over baselines."* — Kept, but contextualized with the 31.1% caveat in the main strengths section.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same set of observations: the method is sound and the results are meaningful for a new task, but the evaluation's reliance on synthetic (GPT-4o-generated) instructions limits the generality of the claims. The most productive direction for improvement — testing on human-written instructions — is identified by both the harsh critic and the strength finder's implicit scope analysis.

## Suggestions

1. **Most impactful single addition:** Construct a small test set (50–100 examples) with instructions written by humans (not GPT-4o), and report CAD-Editor's performance on it. Even if the score is lower, this would establish a realistic baseline and honestly characterize the gap between synthetic and human language.

2. **Add a full-model ablation** (CAD-Editor without the selective-data stage on the full 92k dataset) to Table 1, so readers can directly see the contribution of the selective-data refinement independent of dataset scale.

3. **Include a failure analysis section** that categorizes the 69% unsuccessful human-evaluation outputs. This would clarify where the model breaks and provide concrete guidance for future work.

4. **Report the size of $\mathcal{D}_{\text{selective}}$** and the number of samples generated per input example during the selection process.

## Score and Decision

This is a paper that introduces a genuinely new and important task with a practical, well-engineered approach. The contribution — task formulation, synthetic data pipeline, two-stage fine-tuning strategy, and the first benchmark — is solid. The main weakness is that the evaluation is entirely within the distribution of GPT-4o-generated instructions, leaving the claim of general "text-based editing" partially unsupported. For a first paper on a new task, this is a reasonable starting point, and the method clearly outperforms GPT-4o baselines by a wide margin. The missing failure analysis and incomplete ablation are addressable gaps. The paper would benefit from additional experiments but its core contributions are real.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>