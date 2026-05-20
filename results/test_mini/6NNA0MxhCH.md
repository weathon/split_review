Now I have sufficient context from both the paper and anchors. Let me compose the final consolidated review.

## Summary

This paper investigates how transformer language models produce answer-choice symbols (e.g., "A" or "B") in formatted multiple-choice question answering (MCQA). Using vocabulary projection and activation patching across Olmo-7B-SFT and Llama2-13B-Chat on HellaSwag, MMLU, and a synthetic Colors dataset, the authors localize answer-symbol production to a single middle layer (layer 21 for Olmo, layers 15–21 for Llama2), show that later layers increase symbol probability via a sparse set (~8) of specialized attention heads, and find that poorly-performing checkpoints cannot separate answer symbol tokens in vocabulary space. The paper also introduces a synthetic Colors task that disentangles formatted MCQA ability from dataset-specific knowledge, and identifies a two-stage processing strategy for out-of-distribution answer symbols.

## Strengths

- **Consistent localization across datasets and architectures**: Activation patching identifies the same middle-layer causal region (layer 21 for Olmo) across HellaSwag, MMLU, and the synthetic Colors task, and the pattern replicates in a different model family (Llama2-13B-Chat, layers 15–21). This cross-task, cross-architecture consistency is a genuine finding that goes beyond single-dataset analyses.

- **Methodological triangulation via vocabulary projection + activation patching**: The paper demonstrates that these two techniques reveal complementary aspects — activation patching localizes causal mechanisms before hidden states are projectable to the vocabulary space, while vocabulary projection shows how relevant information appears in probability space over remaining layers (§4, Figs. 2–4). This pairing strengthens the causal interpretation.

- **Discovery of symbol-specialized attention heads**: The fine-grained head-level analysis (Fig. 6) shows that of the ~8 causally relevant attention heads, some consistently promote a specific symbol (e.g., always "A" or always "B"), some promote whichever symbol is correct, and some activate only for one symbol. This is more nuanced than prior work on "correct letter heads" (Lieberum et al., 2023) and provides a concrete mechanistic hypothesis about how the model implements answer selection.

- **Synthetic task and training dynamics**: The Colors task isolates the formatted MCQA ability from factual knowledge. The finding that this ability emerges between 350B and 1T training tokens for Olmo v1.7 — even while harder dataset performance remains poor — cleanly separates the learning of symbol binding from the learning of factual content.

- **Evidence for two-stage OOD processing**: For C/D symbols, Olmo first assigns probability to the expected A/B symbols before abruptly switching at layer 30 (Figs. 2, 4). This provides a concrete explanation for why some models struggle with unusual answer formats.

## Weaknesses

### Major

- **Activation patching confounds answer-symbol identity with answer content/position.** The core causal experiment (§4.1) patches hidden states between `AB_Acorrect` and `AB_Bcorrect` — prompts where the correct answer changes from position A to position B, and the associated answer *text* also changes. The patched hidden state thus encodes not only which symbol (A vs. B) is correct but also which answer content is correct and which position the correct content occupies. Consequently, the causal effect cannot be uniquely attributed to symbol identity. This limits the specificity of the headline claim that "a single middle layer ... is responsible for answer selection." The OOD (C/D) experiments partially address this concern by showing a different mechanism when symbols change, but without a control that disentangles symbol identity from position/content (e.g., patching between prompts where the same symbol is correct at the same position but with different answer text), the core causal attribution remains less specific than claimed.

- **Limited model generality vs. overclaimed scope.** Only 2 of the 8+ tested models pass the consistency criterion and are analyzed. The paper's title ("Understanding How LMs Answer Multiple Choice Questions") and abstract frame the contribution broadly, but the evidence comes from two instruction-tuned/aligned models (Olmo-7B-SFT, Llama2-13B-Chat). The paper is transparent about which models pass the criterion, but the gap between the sweeping framing and the narrow empirical base is notable. Moreover, the finding that Llama2's critical region spans ~6 layers while Olmo's is concentrated at a single layer shows that the mechanism is *not* uniform across the two studied models, further undercutting blanket generalizations.

- **The "attention heads dominate" claim is based on vocabulary projection, not causal importance.** Section 6 states that "attention heads generally dominate the distribution" based on projected probabilities of function outputs. However, vocabulary projection does not measure causal importance — an MLP could be critical even if its projected probability is low, if it provides a small residual update that redirects the trajectory. The paper's own activation patching results (Fig. 4) show comparable causal effects for MLPs and MHSA at several layers, contradicting the "domination" narrative. This claim should be re-framed as a vocabulary-projection observation, not a causal conclusion.

### Minor

- **No analysis of attention patterns for identified heads.** The paper identifies heads that "specialize" in promoting specific symbols (Fig. 6) but does not examine *where* these heads attend. Earlier work (Lieberum et al.) found "correct letter heads" that attend to the symbol's token position in the prompt. Without attention pattern analysis, it is unclear whether the identified heads work by copying the symbol from earlier positions, by attending to answer content, or via some other mechanism. This leaves the mechanistic explanation incomplete.

- **No confidence intervals or error bars on activation patching curves.** Many plots (e.g., Figs. 3, 4) show averages over instances without measures of variance. Given that the number of correct predictions and the patching effect size vary across instances, the reliability of these averages is unclear.

- **The vocabulary-projection comparison for poorly-performing models uses only one weak checkpoint (350B).** While the contrast between the 350B and 1T/2T checkpoints (Fig. 7) is clean, the claim that an "inability to separate answer symbol tokens in vocabulary space ... is a property of poorly-performing models" rests on a single observation point. This is suggestive but not conclusive.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- **Attention pattern analysis for identified heads:** Showing where the symbol-specialized heads attend (e.g., to the earlier token position of that letter, to the answer content, or to the question) would substantially deepen the mechanistic account and connect to prior work on "correct letter heads."
- **A control activation-patching experiment** that varies position while holding answer content fixed (or vice versa) to disentangle symbol identity from position.
- **Test on additional models** that could plausibly pass the consistency criterion (e.g., Llama3-8B-Instruct, Mistral-7B-Instruct, larger Olmo variants) to strengthen generality claims.
- **Error bars / confidence intervals** on averaged activation patching and vocabulary projection plots.

## Removed Points

These points from the reviews were removed as factually incorrect, scope-creep, or otherwise invalid:

1. **"Colors task does not convincingly isolate formatted MCQA from simple copying"** — REMOVED because the paper *does* show that the same layer 21 is causally important for Colors via activation patching (Fig. 4b, cited in §5: "layer 21 also plays a key causal role in the promotion of answer symbol tokens for Colors"). The claim that "no evidence" exists is factually wrong.
2. **"The paper does not report performance on other datasets at those checkpoints"** — REMOVED as scope-creep. The paper's goal in §7 is to analyze the synthetic Colors task specifically; the contribution is demonstrating that the task isolates MCQA ability, not that it predicts performance on all other datasets.
3. **"350B checkpoint analysis rests on a single observation"** — WEAKENED to minor. The paper compares one weak checkpoint (350B) against two strong ones (1T, 2T). This is sufficient for a suggestive finding but not for a general property claim; it has already been moved to the Minor weaknesses section with appropriate framing.
4. **Various demands to investigate "why" the two-stage OOD process occurs, test non-letter symbols, study incorrect predictions, etc.** — Moved to Nice-to-Haves as they address questions beyond the paper's stated scope.
5. **Formatting/style complaints** — Removed per instructions (parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The reviewers did not identify a novel perspective that the authors themselves had missed. The only cross-cutting observation is that the activation-patching confound (symbol identity vs. position) is a general concern for any study using patching between different-format prompts where both the symbol and the underlying correct answer change simultaneously — this methodological point is implicit in the reviewer critique but is not developed into a concrete insight.

## Suggestions

1. **Address the activation-patching confound head-on.** The most impactful fix would be to add a control experiment: patch between two prompt conditions where the *same* answer symbol is correct at the *same* position but the answer text differs (or where different answer positions map to the same symbol). This would disentangle symbol identity from position/content and sharpen the core causal claim. Even acknowledging this as a limitation and showing that the current results are consistent with a symbol-binding interpretation (but not uniquely so) would substantially strengthen the paper.

2. **Re-frame scope claims.** The title and abstract should qualify that the findings are about how *performant* models (specifically Olmo-7B-SFT and Llama2-13B-Chat) produce answer *symbols* in formatted MCQA, and that the broader claim about "how LMs answer multiple choice questions" overstates the evidence.

3. **Re-frame the "attention heads dominate" claim** (Section 6) from a causal claim to an observation about vocabulary-projection probability. Acknowledge that activation patching shows comparable MLP and MHSA effects and that the two measures capture different quantities.

4. **Add attention-pattern analysis** for the identified heads to show whether they attend to the symbol's token position, the answer content, or other parts of the prompt. This would connect the work to existing findings on "correct letter heads" and strengthen the mechanistic interpretation.

5. **Include statistical measures of variance** (error bars, confidence intervals) on averaged plots (activation patching and vocabulary projection) where feasible.

## Score and Decision

I calibrated my score by comparing the paper under review against the following anchor papers from the human-review corpus:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Retrieval Head (EytBpUGB1Z) | 8.0 | Much stronger: studied across 4 model families at multiple scales with clean, well-supported claims. The present paper is narrower in scope and model coverage. |
| Activation Patching Best Practices (Hf17y6u9BC) | 6.67 | Stronger on methodological rigor and systematic experimentation; the present paper has a more interesting research question but weaker execution on the core causal experiment. |
| Controllable Context Sensitivity (Igm9bbkzHC) | 6.75 | Stronger: clean experimental design, multiple model families, clear causal findings. Present paper is comparable in ambition but has a confound in the central experiment. |
| Which Attention Heads Matter for ICL (KadOFOsUpQ) | 4.60 | Comparable in structure but the present paper has cleaner methodology and more consistent findings. However, both suffer from overclaiming relative to the evidence. |
| Llamas Think in English (fSbPwHjdDG) | 3.00 | Weaker: limited task, poor presentation, methodological concerns. The present paper is substantially more rigorous and has clearer contributions. |
| Neural Networks Decoded (PoB6QGAM38) | 3.00 | Weaker: vague claims, no rigorous experiments. The present paper has concrete findings and clear methodology. |
| Mechanistic basis of abrupt learning (aN4Jf6Cx69) | 4.50 | Comparable: polarizing reviews, genuine insights but with methodological limitations. Present paper has cleaner presentation and more directly actionable findings. |

The paper has genuine contributions (consistent layer localization, symbol-specialized heads, synthetic task design, training dynamics analysis) but is held back by: (1) a confound in the core activation-patching experiment that limits the specificity of the headline causal claim, (2) a scope overclaim given only 2 performant models are analyzed, and (3) a claim about attention heads "dominating" that is not supported by causal evidence. The weaknesses are addressable but non-trivial. Relative to the anchors, the paper falls below the strong accept range (≥6.5) but above reject-quality papers (≤4). I assign it a score of 5.5, reflecting a paper with clear contributions that needs substantial revision to reach its full potential.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>