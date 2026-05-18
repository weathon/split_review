Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes using query-key dot products (QK-score) and attention weights from specific "select-and-copy" attention heads, rather than the model's final output logits, to improve multiple-choice QA. The method is evaluated across models from 7B to 70B parameters on several MCQA benchmarks and a synthetic dataset. A key finding is that certain heads (e.g., (14,24), (14,20) in LLaMA2-7B) are consistently good across datasets and can even be identified without labeled data via an attention-diversity heuristic.

## Strengths

1. **Unsupervised identification of universal select-and-copy heads.** The paper shows that robust heads can be found *without* a labeled validation set by scoring heads on attention to option tokens and variability across options (Section "Finding best heads without validation labels"). These heads (e.g., (14,24), (14,20)) appear in the top 10–20 across real and synthetic datasets. This goes beyond prior work (e.g., Lieberum et al. 2023) that relied on validation labels or specific option tokens, and it directly addresses the practical utility of the method.

2. **Near-perfect accuracy on a synthetic format test provides strong evidence for the core claim.** The QK-score achieves ~60% absolute improvement over baseline on the Simple Synthetic Dataset (SSD), reaching close to perfect accuracy (Section 5.4, Fig. 9). This is compelling evidence that the method extracts knowledge the model possesses but cannot express via standard MCQA logits, directly validating the paper's central thesis.

3. **Causal evidence via zero-ablation.** Ablating the top 10 select-and-copy heads (identified by attention to EOL tokens) causes accuracy to drop below random on several datasets, while ablating random heads from the same middle layers does not (Fig. 7). This provides mechanistic evidence that these heads are causally responsible for MCQA performance. The control (random heads from the same layers, aggregated over 5 runs) is reasonable and strengthens the causal claim beyond a mere correlation.

## Weaknesses

### Fatal
None.

### Major
None. The issues below are real but addressable and do not invalidate the paper's core contributions.

### Minor

1. **The QK-score's mechanistic justification is thin.** The paper motivates stripping RoPE from the QK-score by saying they want to avoid positional effects (lines 84–88, 117). This is a reasonable intuition, but it is not supported by an analysis showing that the unrotated dot product actually isolates semantic content or that alternative formulations (e.g., using the actual pre-softmax logits with RoPE, or applying other forms of position-removal) would not work equally well or better. Since the QK-score is the central metric of the method, a deeper investigation (e.g., an ablation comparing QK-score against the actual pre-softmax attention logits) would substantially strengthen the paper. The empirical success partially compensates, but the gap between the mechanistic narrative ("attention as select-and-copy") and the actual computation used remains.

2. **The PriDe comparison is conducted on a modified dataset that disadvantages PriDe.** All datasets are modified to include two extra options ("E. None of the above," "F. I don't know") that are never correct (line 151). The paper acknowledges that PriDe "is not robust for additional uncertain options" (line 190) and still claims QK-score "outperforms PriDe." This is not a flaw in the proposed method, but the comparison is not on equal footing. The paper's main claims do not depend on beating PriDe, but presenting this comparison without a corresponding evaluation on the original 4-option format (where PriDe was designed to operate) somewhat overstates the advantage.

3. **Head selection on a small validation set without statistical characterization.** The method selects a single best head from ~1000+ candidates using only 5% of each dataset (~700 examples for MMLU) as validation (lines 152, 171). No variance estimates, confidence intervals, or controls for selection bias are reported. For the dataset-specific results (as opposed to the universal-head results in the analysis section), one cannot fully rule out that some of the reported gain is due to lucky selection. The universal-head analysis (Section 6) partially mitigates this by showing that certain heads work across datasets, but the dataset-specific results remain uncharacterized. Reporting bootstrap intervals or comparing against a calibration-based selection procedure would strengthen confidence.

4. **Limited analysis of failure cases on knowledge-intensive tasks.** On MMLU, the QK-score underperforms the baseline for several large models (LLaMA3-70B, LLaMA3-70B chat, LLaMA2-70B — see Table 1). The paper offers a one-sentence speculation ("questions from it are oriented on general knowledge while our method by design focuses more on the semantic relations," line 193) but does not analyze why the method fails here. Understanding this failure mode would be valuable for assessing the method's scope and could inform improvements.

### Trivial

1. **Abstract understates max improvement.** The abstract claims "up to 16% gain for LLaMA2-7B and up to 10% for larger models," but the body reports a 27% gain on LLaMA3-8B for HellaSwag (line 193). The abstract should either include this case or be more precise about which model families are covered.

2. **Ablation scatter plot lacks interpretability without a "worst-heads" baseline.** The current ablation compares against random heads from the same layers (Fig. 7), which is reasonable, but including a comparison to the *worst* heads (lowest-attention to options) would make the causal story sharper and eliminate any ambiguity about whether the effect is simply "any head matters."

## Nice-to-Haves

- Evaluate on the original 4-option datasets (without E/F) to provide a clean comparison with PriDe on its intended setting.
- Include prompt templates for each dataset in the appendix for reproducibility.
- Add a simple analysis of why QK-score struggles on MMLU for large models — e.g., does head behavior differ between knowledge-retrieval questions and reasoning questions?

## Removed Points

These are points from the reviewers that were removed with brief justification:

- **"The QK-score lacks any theoretical or empirical reason"** — The paper *does* provide a reason (mitigating position effects, lines 84–88). Stripped because factually inaccurate. The retained weakness (Minor #1) captures the real issue (insufficient depth, not absence).
- **"The claim 'nearly perfect accuracy' is imprecise because it's only true for certain heads"** — The abstract refers to the method's performance using selected heads, which is standard. Stripped as strawman.
- **"Missing related works"** — Stripped per instructions: cannot verify existence of omitted works.
- **"Code and data availability are not mentioned"** — Stripped per instructions (reproducibility nitpick).
- **"Missing appendix / appendix details"** — Stripped per instructions (parser strips these; they exist in original).
- **"Prompt templates not specified"** — Moved to Nice-to-Haves; the paper describes the format generally.
- **"Synthetic dataset description is sketchy"** — The paper describes the dataset clearly at line 149 (word-matching task, 2500 examples, random-word distractors). Stripped as factually inaccurate.
- **"The comparison with random heads from middle layers is insufficient; worst heads would be better"** — Random heads from the *same* layers is a reasonable control; included as a trivial suggestion rather than a weakness.
- **Strength Finder's generic strengths** — All three strengths from the Strength Finder were concrete and specific; none were removed.

## Novel Insights

The two reviewers' perspectives, when combined, reveal an interesting tension: the harsh critic identifies methodological gaps in the QK-score's justification and the PriDe comparison, while the strength finder highlights the paper's strongest evidence (causal ablation, synthetic-data validation, unsupervised head discovery). The key novel insight from synthesizing these views is that the paper's strongest contribution is not the QK-score *per se* (which is an engineering choice that could be refined) but rather the discovery of *universal* select-and-copy heads that can be identified without labels and causally affect MCQA performance. The QK-score is best understood as one instantiation of a more general insight — that internal head signals can outperform output logits — and the paper would benefit from framing it this way rather than as a principled derivation from the attention mechanism.

## Suggestions

1. **For the QK-score:** Conduct an ablation comparing QK-score (without RoPE) against the actual pre-softmax attention logits (with RoPE) on a subset of models/datasets. This would clarify whether stripping positional information is indeed beneficial and would ground the central metric more firmly.
2. **For the PriDe comparison:** Add results on the original 4-option versions of the datasets (without E/F). This would provide a cleaner comparison and would demonstrate that the method's advantage holds in the standard MCQA setting.
3. **For head selection:** Provide bootstrap confidence intervals or variance estimates for the dataset-specific results. Alternatively, de-emphasize dataset-specific selection and foreground the universal-head results (which are already more robust).
4. **Add a failure-mode analysis for MMLU on large models.** A simple breakdown (e.g., by category within MMLU) could reveal where the QK-score helps vs. hurts and would sharpen the paper's scope claims.
5. **Make the abstract consistent with the observed max gains across all tested models.**

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>