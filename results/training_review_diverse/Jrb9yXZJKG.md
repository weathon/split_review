Now I have all the information needed to cross-check each claim against the paper. Let me produce the consolidated review.

---

## Summary

This paper introduces CAD-Editor, the first system for text-based CAD editing. The authors formulate the task as a sequence-to-sequence problem using LLMs (Llama-3-8B-Instruct), generate a large-scale synthetic training dataset (92k examples) by combining design-variation models (SkexGen, Hnc-CAD) with GPT-4o multi-level captioning, and then further fine-tune on a small selective dataset curated by D-CLIP or human feedback. Experiments show CAD-Editor achieves 91.4% valid ratio and 0.21 D-CLIP score, substantially outperforming GPT-4o prompting baselines, while maintaining generation quality comparable to dedicated CAD generation models.

## Strengths

1. **First formulation of text-based CAD editing as a seq2seq problem with LLMs.** The paper identifies and formalizes a genuinely under-explored task, defines a CAD sequence representation suited for LLM processing (variable-length, textual tokens for categorical and numerical variables), and demonstrates that a pre-trained LLM can be adapted for this purpose. (Sections 1, 3.1)

2. **Practical synthetic data pipeline leveraging complementary existing models.** The authors combine design-variation models (for generating paired CAD models) with MLLMs + multi-level captioning (for producing textual instructions) in a systematic way. The multi-level captioning strategy (describe images → identify differences → compress) is shown to improve data quality over naive captioning in both qualitative (Figure 9) and quantitative (Table 2) ablations. (Section 3.2)

3. **Selective dataset fine-tuning demonstrably improves instruction alignment.** The key observation — sampling an initially fine-tuned model multiple times yields at least one good result — is operationalized via D-CLIP feedback (DCF) or human feedback (HF). Both methods improve D-CLIP scores (from 0.17 to 0.22 with DCF, 0.24 with HF), showing the approach works even without expensive human annotation at scale. Importantly, HF improves D-CLIP *without* using D-CLIP for selection, providing convergent evidence. (Section 3.3, Table 2)

4. **Comprehensive evaluation with multiple metrics and human assessment.** The paper reports Valid Ratio, D-CLIP, COV, MMD, JSD, and a human evaluation by five crowd workers per sample. CAD-Editor achieves 91.4% valid ratio (vs. GPT-4o 3-shot at 67.1%) and a human eval success rate of 31.1% (vs. GPT-4o 3-shot at 13.1%), demonstrating real improvement over prompting-only baselines. (Section 4.2, Table 1)

5. **Ablation studies isolating contributions of multi-level captioning and selective data.** Each component is ablated quantitatively, confirming their individual contributions. (Section 4.3, Table 2)

## Weaknesses

### Fatal

None.

### Major

1. **Test set is constructed from the same synthetic pipeline as training data, with no validation on human-written instructions.** The 2000-example test set is produced by the same design-variation models and GPT-4o captioning pipeline (Section 3.2), then manually verified for correctness. The distribution thus closely matches the training distribution. The paper acknowledges this limitation in the conclusion, but the concern goes beyond a caveat: the benchmark can only capture edits that GPT-4o can derive from visual differences between rendered CAD images. Genuine user instructions could involve functional edits ("strengthen this bracket"), material changes, or other requests outside this distribution. Without even a small set of human-written instructions (e.g., 50–100) to validate transfer, it is unclear how well CAD-Editor would perform under realistic conditions. The human evaluation does include crowd workers judging output quality, but the *instructions themselves* remain synthetic — this limits the strength of the benchmark claim. This is the single most impactful weakness in the paper.

### Minor

2. **D-CLIP is used both for selection (DCF) and evaluation, and the paper does not discuss this.** The DCF variant selects training examples by ranking model outputs with D-CLIP, and the same metric is reported as evidence of improvement in Tables 1 and 2. While the evaluation is on a held-out test set (which mitigates direct circularity), the potential for D-CLIP-selected training data to inflate D-CLIP evaluation scores is not discussed. Importantly, the HF results (which improve D-CLIP without using it for selection) partially address this concern, but the paper would benefit from an explicit discussion and, ideally, a comparison of DCF vs. HF D-CLIP scores on a subset of the test set that was held out from all selection processes.

3. **No analysis of failure modes from the human evaluation.** The human eval shows 31.1% success for CAD-Editor, meaning ~69% of outputs fail on alignment or quality. The paper does not categorize common failure types (e.g., wrong shape type, position error, invalid geometry, no change). A brief breakdown would significantly improve understanding of where the approach stands and what the next bottlenecks are.

4. **Multi-level captioning ablation is performed on a 10k-example subset.** The paper acknowledges computational constraints (Section 4.3), and the improvement is clear on this subset. Nevertheless, confirming the benefit holds at the full 92k scale would strengthen the claim.

5. **Missing reproducibility details on the selective dataset.** The paper does not report how many triplets were collected via DCF or HF, nor how many samples per input were drawn from the initial model. These details are needed for reproducibility.

### Trivial

None.

## Nice-to-Haves

- A small-scale validation set (50–100 examples) of human-written editing instructions paired with real CAD models, with human ratings of CAD-Editor's outputs. This would directly address the most significant limitation of the paper.
- A breakdown of why 8.6% of CAD-Editor outputs are invalid (broken curves? invalid extrusions?).
- Rough estimates of API costs for the GPT-4o-based pipeline to help readers gauge practical accessibility.
- Reporting test-set filtering statistics: how many candidate examples were rejected during manual verification, and what was the inter-annotator agreement on the manual examination?

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Criticism: CAD-Editor comparison to SkexGen/Hnc-CAD is unfair.** *Reason for removal:* The paper explicitly states in the Table 1 caption that "SkexGen and Hnc-CAD are unable to handle text-based editing, so only their generation quality is compared." The comparison is scoped to generation quality metrics (COV, MMD, JSD) — which these models *are* designed for — and the paper does not claim CAD-Editor competes with them on their own terms. This is not a weakness.

- **Criticism: "The paper's strongest quantitative claim (instruction alignment via D-CLIP) is partially confounded by using the same metric for selection and evaluation" as a Fatal/Major issue.** *Reason for downgrade:* The criticism is valid as a concern, but the HF results (0.24 D-CLIP without using D-CLIP for selection) provide convergent evidence that the improvement is real, not an artifact. This reduces the severity from a structural flaw to a methodological gap that can be addressed with additional analysis. Retained as a Minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel synthesis that the paper itself misses — they largely confirm and qualify the paper's own framing.

## Suggestions

1. **Add a human-instruction validation set.** Collect 50–100 text editing instructions from designers (or even non-experts) paired with real CAD models from the DeepCAD test set. Have the same humans rate CAD-Editor's outputs (without additional fine-tuning). Report the success rate. This single addition would substantially increase confidence that the synthetic training distribution transfers to realistic input and would strengthen the benchmark claim.

2. **Explicitly address the D-CLIP confound.** Add a brief discussion in Section 4.3 noting that D-CLIP is used both for DCF selection and evaluation, that the evaluation is on a held-out test set, and that the convergent HF results (which improve D-CLIP without using it) suggest the improvement is genuine. Optionally report D-CLIP scores for DCF and HF variants on a subset of the test set never used in any selection.

3. **Report selective dataset statistics and failure mode analysis.** Include the number of triplets collected per method (DCF, HF), samples per input, and a categorization of common failure modes observed in the human evaluation (e.g., wrong geometry, position error, invalid command sequence, no change).

4. **Full-scale captioning ablation.** If resources permit, validate that the multi-level captioning benefit holds at the full 92k scale rather than only on the 10k subset.

## Score and Decision

This paper makes a genuine contribution by introducing a new task, building a practical synthetic data pipeline, and demonstrating a working system. The weaknesses are real but addressable — the most significant is the lack of validation on human-written instructions. The paper's core claims (that LLMs can be fine-tuned on synthetic CAD-editing data to follow textual instructions) are supported by the evidence. The D-CLIP confound is partially addressed by the convergent HF results. I recommend acceptance conditional on addressing the major and minor weaknesses, particularly the human-instruction validation and the selective dataset documentation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>