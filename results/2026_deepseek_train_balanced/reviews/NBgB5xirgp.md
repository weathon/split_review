## Summary

DualFocus introduces a two-perspective framework for MLLMs: (1) a "macro" pathway that processes the full image, (2) a "micro" pathway that localizes a question-relevant sub-region, crops and zooms into it, and answers using both views, and (3) a PPL-based selection mechanism that dynamically picks between the two answers. The method is evaluated on LLaVA-1.5 (7B, 13B) and Qwen-VL-Chat across SEED, MMBench, GQA, and TextVQA, showing consistent improvements (+1.2 to +4.2). A 143k curated VG dataset is introduced to train the box-prediction + dual-answer regime.

## Strengths

- **Clean, well-motivated architecture that resolves the resolution trade-off.** Unlike uniform high-resolution models (Monkey, OtterHD) that gain detail but lose global context, DualFocus first scans globally, then zooms into relevant sub-regions. Table 1 confirms this empirically: DualFocus improves both global benchmarks (SEED, MMBench) *and* detail-oriented benchmarks (GQA, TextVQA) across all tested configurations.

- **Consistent gains across two model families and two sizes.** Every entry in Table 1 (3 configurations × 4 benchmarks = 12 entries) shows a positive delta. This rules out architecture-specific or coincidental improvement. The gains replicate from LLaVA-1.5 7B (+2.7/+2.3/+2.1/+3.8) to 13B (+2.8/+3.0/+4.2/+4.2) to Qwen-VL-Chat (+1.2/+2.6/+4.0/+2.2).

- **Ablation cleanly separates training data effects from inference pathway effects.** Table 3 (tab:component) decomposes the gains: training on VG data alone (macro-only) yields +0.5/+0.4; adding the micro pathway yields +1.5/+3.1 over baseline; adding PPL selection yields +2.7/+3.8. This isolates the contribution of the zoom-and-select mechanism from the extra training data.

- **Demonstrated hallucination reduction.** POPE results (Table 4) show consistent improvements across all three splits (adversarial, popular, random) on both accuracy and F1 (+1.8 to +2.4). This is a plausible and valuable secondary benefit of grounding answers in localized regions.

- **Fine-grained analysis confirms detail gains without global loss.** Figure 3 breakdown shows Text Understanding +12.9 and Instance Attributes +4.3 under the micro pathway, while global sub-tasks (Instance Counting −0.4, Scene Understanding +0.7) are essentially unaffected — micro focuses detail without harming holistic understanding.

## Weaknesses

### Fatal
None.

### Major

- **Box prediction quality is never reported, leaving the core localization mechanism unvalidated.** The paper trains the model to predict bounding box coordinates (lines 101–106), and the entire micro pathway depends on whether these predicted boxes correctly localize the question-relevant region. Yet no metric — IoU, accuracy@threshold, or even qualitative statistics — is reported anywhere. The ablation (Table 3) partially mitigates this by showing the micro pathway adds value beyond training-data alone (+1.0 SEED, +2.7 TextVQA over macro-only), but without box metrics the reader cannot tell whether the model is actually learning to localize or whether gains arise from the extra visual tokens and richer prompting in the micro pathway. This is the single most important piece of missing evidence for the claimed mechanism.

### Minor

- **The claimed "degradation on global tasks" motivating PPL selection is not supported by the reported numbers.** The paper states (lines 163–166) that micro answers "degrade" on global comprehension tasks, motivating PPL-based selection. However, Table 3 shows the micro pathway *alone* outperforms the macro pathway on *both* SEED (67.7 vs. 66.7) and TextVQA (61.3 vs. 58.6). The fine-grained analysis (Figure 3) further shows micro is essentially flat on global sub-tasks (−0.4 Instance Counting, +0.7 Scene Understanding) — not degraded. The PPL selection still works (micro + PPL > micro alone), but the stated motivation is overdrawn. The paper should either retract the "degradation" claim or provide the per-task breakdown that substantiates it.

- **GQA$^{*}$ protocol clarity.** The paper converts GQA to a multiple-choice format (GQA$^{*}$, line 196) but does not explicitly state which baselines in Tables 1–2 were re-evaluated under this modified protocol versus taken from original publications. The evidence suggests re-evaluation (LLaVA-1.5's published GQA ≈62.0 vs. the GQA$^{*}$ score of 67.2), and Table 2 uses "—" for models that could not be re-run. However, the text should state this clearly to avoid any ambiguity, especially since the format change to multiple-choice inflates absolute scores and changes task difficulty.

- **Training data overlap with evaluation benchmarks is not discussed.** The 143k VG-derived training data may share images with GQA (which is built on VG images) and potentially TextVQA. Since GQA$^{*}$ is a key benchmark where DualFocus shows large gains (+4.2 on LLaVA-1.5 13B), any image-level overlap should be quantified and discussed to rule out data leakage inflating results.

- **Information asymmetry between pathways is not controlled.** The micro pathway receives the full image *plus* the zoomed sub-image *plus* the predicted box coordinates *plus* two rounds of prompts — strictly more conditioning information than the macro pathway. The PPL comparison (which selects the lower-PPL answer) could be biased toward micro simply because extra conditioning lowers perplexity, independent of zoom quality. An ablation controlling for this (e.g., macro with dummy coordinates) would strengthen the analysis.

### Trivial

- The −0.4 on Instance Counting (Figure 3) is not discussed; a brief speculation would be helpful.
- The related work section (lines 43–50) includes a broad survey of LLMs and MLLMs that is not tightly scoped to the paper's contribution.

## Nice-to-Haves

- **Computational cost.** DualFocus runs two full inference pathways (macro and micro), each requiring visual encoding of the image (and the micro pathway encodes two images). This doubles or more the inference cost versus standard single-pass MLLMs. Acknowledging this overhead would give readers a more complete picture.
- **Statistics on when PPL selects macro vs. micro.** A breakdown of selection frequency by task type would directly evidence the claimed "dynamic switching" behavior.

## Removed Points

These points were flagged by reviewers but removed or demoted after verification against the paper:

1. **GQA mixing of scores is "uninterpretable"** — Removed as factually inaccurate. Baseline LLaVA-1.5 GQA$^{*}$ (67.2) differs from its published GQA (~62.0), confirming re-evaluation. Table 2 uses "—" for models not re-run. The protocol could be clearer, but the concern about mixing is not borne out.
2. **"Cross-entropy loss on coordinate tokens conflates token-level and coordinate-level error"** — This is standard practice in grounded MLLMs (Shikra, KOSMOS-2). Not a meaningful weakness.
3. **InstructBLIP's GQA listed as "—" when it has a published score** — The published score is under the original open-ended protocol, not GQA$^{*}$. Listing "—" is correct.
4. **PPL distribution figure not quantitatively discussed** — Figures are stripped in the parsed text; they exist in the original submission. Not an author error.
5. **Missing standard deviations / statistical significance** — Not standard practice for these benchmarks; reporting conventions in the field are single-run.
6. **Formatting/style nitpicks** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews does surface one useful observation: the PPL-guided selection mechanism works even though the stated motivation (micro degrades on global tasks) is not quantitatively supported by the ablation — suggesting the PPL gain may come from other factors (e.g., PPL as a general confidence signal) rather than from a specific macro/micro specialization.

## Suggestions

1. **Report box prediction quality** (IoU@0.5 or accuracy at a threshold) for the predicted bounding boxes on a held-out set. Include an analysis of whether answer correctness correlates with box accuracy.
2. **Clarify the GQA$^{*}$ protocol** in the main text: explicitly state that all baselines with numeric GQA$^{*}$ entries in Tables 1–2 were re-evaluated under the same multiple-choice format.
3. **Quantify training/evaluation data overlap** between the VG-derived training data and GQA/TextVQA evaluation sets, and discuss the potential impact.
4. **Correct or substantiate the "degradation on global tasks" claim.** Either show per-question PPL distributions that demonstrate degradation on specific global sub-tasks, or revise the motivation to reflect what the data actually shows.
5. **Add a control experiment** comparing the full micro pathway against a variant that receives the same conditioning (box coordinates, two rounds) but without the zoomed sub-image, to isolate the zoom contribution.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>