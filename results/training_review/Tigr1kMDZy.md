Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies why language models reproduce incorrect information from few-shot demonstrations. Using the logit lens to decode intermediate representations, the authors discover "overthinking": for incorrect demonstrations, decoding from middle layers yields *higher* accuracy than the final layer, with accuracy diverging from the correct-demonstration trajectory at a "critical layer." They identify "false induction heads"—attention heads in late layers that attend to and copy false labels from similar past demonstrations—and show that ablating just 5 such heads (≈1% of all heads) reduces the accuracy gap between correct and incorrect prompts by 38.9% on average across 14 datasets and generalizes beyond the toy dataset used for head discovery.

## Strengths

- **Discovery of a genuine and practically important phenomenon**: The paper demonstrates "overthinking" for incorrect demonstrations across 11 models (GPT-J, GPT2-XL, GPT-NeoX-20B, multiple Pythia sizes, Llama2-7B) and 14 datasets, showing that early-exiting at or before the critical layer outperforms the full model on nearly all datasets. The phenomenon is robust to model scale (410M–20B), instruction tuning, and prompt variations (permuted, random, half-correct labels).

- **Causal identification of specific model components**: The paper defines three properties (label-attending, class-sensitive, label-promoting) and a prefix-matching (PM) score to locate false induction heads. The ablation study is genuinely causal: removing 5 heads discovered on a single toy dataset (Unnatural) reduces the accuracy gap by 38.9% on all 14 real-world tasks, with negligible degradation on correct prompts. Random-head ablation provides a clean control.

- **Top-down mechanistic analysis at a practical scale**: Unlike most mechanistic interpretability work focused on synthetic toy tasks and low-level circuits, this paper studies realistic text classification benchmarks and operates at the level of layers and attention heads. This enables scaling to larger models and more practical settings, with findings that have already inspired follow-up work (Belrose et al. 2023 on tuned lens and prompt injection detection).

- **Robustness across architectures and training regimes**: Overthinking appears in both older models (GPT-2) and modern Chinchilla-optimal models (Llama2-7B), in both pretrained and instruction-tuned variants, and across model sizes spanning two orders of magnitude. This breadth rules out artifacts of a specific training recipe or model family.

- **Controlled experiments ruling out trivial explanations**: The semantically-unrelated-labels control (replacing "Positive"/"Negative" with "A"/"B") shows that overthinking depends on the ground-truth relation of labels, not just relabeling. The ablation isolating attention heads from MLPs shows the effect is specific to attention.

## Weaknesses

### Fatal

None.

### Major

- **The "false induction head" terminology overclaims the mechanistic depth achieved.** The paper draws an analogy to induction heads (Olsson et al., 2022), which perform a specific prefix-matching computation. However, the heads identified here are only shown to be (1) label-attending, (2) class-sensitive (attend more to labels from inputs of the same class), and (3) label-promoting. None of these properties establishes the **prefix-matching induction mechanism**—the heads could simply be generic label-copying heads that attend to labels in context based on class similarity, without performing any prefix-matching computation. The "prefix-matching score" measures class-conditional label attention, not induction in the Olsson et al. sense. This does **not** undermine the core causal finding (these heads contribute to false context-following), but the naming and framing overstate the mechanistic understanding achieved.

- **The logit lens is used without validation on the specific models and layers studied.** The paper relies heavily on the logit lens to measure layerwise accuracy and define the overthinking phenomenon. While the paper discusses the logit lens compared to probing (Section 6) and cites follow-up work using the tuned lens (Belrose et al., 2023) on BLOOM-560M, it does **not** validate that the logit lens predictions at intermediate layers are faithful for the main models studied (GPT-J, GPT2-XL, Pythia, Llama2-7B). The tuned-lens validation by Belrose et al. covers a different model (BLOOM-560M), not the paper's own model zoo. **However**, this is **not** a fatal flaw: the paper's overthinking claim is also supported by direct ablations (zeroing out late layers/attention heads improves accuracy), which do not depend on the logit lens. The logit lens concern primarily affects the *layerwise accuracy curves* as measurements of model processing, not the existence of overthinking as an intervention-verified phenomenon.

### Minor

- **The ablation evidence does not fully establish that false induction heads *cause overthinking* specifically (as opposed to generally harming performance on incorrect prompts).** The paper reports that ablating the 5 heads reduces the final-layer accuracy gap by 38.9%. While the paper states it compares "layerwise performance" (line 224), the headline result and the main ablation table appear to focus on final-layer accuracy. To mechanistically link these heads to the *monotonic accuracy decrease after the critical layer* that defines overthinking, one would want to see that ablating them shifts the entire layerwise accuracy curve (especially the post-critical-layer decline), not just improves final accuracy. The current evidence is consistent with the heads contributing to false imitation in general, but less specific to the layerwise trajectory.

- **The critical layer identification is informal and reported without variance.** The paper defines the critical layer as "the layer at which the accuracy gap first reaches half of its final value" (footnote) but does not report these values systematically across all model-dataset pairs with variance estimates. While the qualitative pattern (divergence at similar layers across datasets) is visually clear, the analysis would be strengthened by a table of critical layers with confidence intervals.

- **The false induction heads are identified on the Unnatural dataset but only their ablation (not their PM scores) is verified on other datasets.** The paper shows that ablating these heads generalizes to all 14 datasets, which is strong evidence of causal relevance. But the PM scores themselves are not computed on the target datasets to verify that the same heads exhibit label-attending/class-sensitive behavior on those tasks. While the ablation result speaks for itself, the mechanistic claim would be stronger with cross-dataset PM score validation.

- **The "true prefix" overthinking (benefiting from early exiting even with correct demonstrations) is acknowledged but not analyzed.** The paper finds that GPT2-XL sometimes benefits from early exiting even with correct demonstrations, which suggests overthinking may not be exclusively a false-imitation phenomenon. The paper notes this but does not investigate whether the same false induction heads are responsible or whether a different mechanism is at play. This leaves the framing somewhat incomplete.

### Trivial

- The attention-vs-MLP ablation comparison (Table `new-ablations-main-table`) is reported for GPT-J only. Extending to other models would strengthen the claim that attention heads specifically cause overthinking.

## Nice-to-Haves

- Test false induction heads on non-classification tasks (e.g., code generation with buggy examples). The paper motivates the problem with code completion but evaluates only on text classification.
- Use mean ablation or resampling ablation instead of zero-ablation, as the paper itself acknowledges in the limitations. This would address the off-distribution concern.
- Directly test whether the model "knows" the correct answer before the critical layer (e.g., via probing for the correct label in early-layer representations). The paper frames the problem as "knowing vs. saying" but does not test the "knowing" part directly.

## Removed Points

These points were factually incorrect, reflected reviewer misunderstandings, or were scope creep:

- **"The ablation is evaluated on final-layer accuracy alone, not on the layerwise trajectory"** — The paper explicitly states it evaluates "layerwise performance" (line 224). The 38.9% gap reduction is a summary statistic of the final-layer improvement, but the analysis includes layerwise comparison.
- **"No statistical test" for false-label-promoting scores** — The paper reports mean and standard deviation for 100 random sets (−0.04 ± 0.41) versus the 5 selected heads (6.5). The 5 heads are ~16 standard deviations above the random baseline; the evidence is overwhelming without a formal test.
- **"The paper never directly tests whether the model 'knows' the right answer"** — This is scope creep. The "knowing vs. saying" is a motivating intuition, not a claim the paper sets out to prove.
- **Permuted labels are "structurally unnatural"** — The paper tests multiple variants (random labels, half-correct labels) and these all show similar overthinking. Demanding a specific "mostly right annotator" scenario is scope creep.
- **Pure formatting/style nitpicks** — Removed per instructions.
- **Missing appendix content** — The parser strips appendix figures; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent insight from the reviews is the tension between the logit-lens-measured phenomenon and the intervention-based evidence. The paper's overthinking claim rests on two independent pillars: (1) logit lens decoding shows accuracy decreasing after the critical layer, and (2) actually ablating late layers/heads improves accuracy. The fact that both methods converge on the same conclusion—despite the logit lens being potentially unreliable at intermediate layers—strengthens the core claim considerably, though the paper does not frame this convergence explicitly. This suggests a general methodological lesson: phenomena observed via the logit lens should be corroborated by actual interventions before being treated as established.

## Suggestions

1. **Temper the "false induction head" terminology.** The heads are causally important and well-characterized, but calling them "false induction heads" invites unnecessary scrutiny about whether they implement the induction mechanism. "False-copying heads" or "label-copying heads" would be more precise and avoid overclaiming mechanistic depth.

2. **Add a validation experiment for the logit lens** on at least one of the main models (e.g., GPT-J), comparing logit lens predictions to either trained probes or the tuned lens from Belrose et al. on the same model and layers. This would address the most serious methodological concern.

3. **Report critical layers systematically** in a table with per-dataset values and variance across prompts, to support the claim that divergence occurs at the same layers across datasets.

4. **Show the layerwise ablation curves** for false induction heads more prominently. The paper states it compares layerwise performance—showing these curves in the main paper would directly address the concern about whether the heads specifically flatten the post-critical-layer accuracy decline.

5. **Extend the attention-vs-MLP ablation** to at least one additional model beyond GPT-J to strengthen the claim that attention heads (and not MLPs) are the primary locus of overthinking.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>