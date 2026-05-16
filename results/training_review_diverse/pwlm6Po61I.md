Now I have a thorough understanding of the paper. Let me produce the final review.

## Summary

This paper investigates whether large language models (LLMs) can process and understand images when those images are converted into Scalable Vector Graphics (SVG)—an XML-based textual format. The authors evaluate GPT-4 (and fine-tuned Vicuna) on three categories of tasks: visual reasoning (Sort-of-Clevr), out-of-distribution image classification (MNIST/Colored-MNIST), and visual prompting (generating transformed SVG images). The core claim is that LLMs, despite never being trained on visual data, can perform these tasks competitively when images are represented as SVG code, suggesting latent visual understanding abilities.

## Strengths

- **Systematic exploration across multiple vision task categories.** The paper evaluates SVG-as-bridge on discriminative (reasoning, classification) and generative (visual prompting) tasks, providing a broader empirical scope than prior qualitative demonstrations (Bubeck et al., 2023). This coverage is valuable as an exploratory study mapping what SVG-mediated LLM processing can and cannot do.

- **Demonstrates SVG-mediated robustness to distribution shifts in controlled settings.** The fine-tuning comparison (Vicuna+SVG vs. ConvNeXt+pixels on MNIST→Colored-MNIST) shows that Vicuna trained on SVG-based MNIST achieves substantially higher accuracy on color-shifted test sets (95.7% CMNIST-A, 92.9% CMNIST-B) than ConvNeXt trained on pixel-based MNIST (74.8%, 74.4%). This controlled comparison (both models fine-tuned on MNIST, same test conditions) provides meaningful evidence that SVG representations may help models focus on shape over color.

- **In-context learning with SVG enables few-shot classification improvement.** GPT-4 improves from 75.3% (zero-shot) to 79.3% (one-shot) on Mini-MNIST, demonstrating that even a single SVG example helps the LLM adapt to a visual classification task—a finding distinct from the fine-tuning experiments.

- **Quantitative and qualitative results on visual prompting (Table 3).** The paper reports color-aware mIOU across six transformation tasks, showing that GPT-4 can produce coherent SVG output for shape/color/size transformations, with qualitative examples in Figures 4 and 5.

## Weaknesses

### Major

- **The Sort-of-Clevr "visual reasoning" task primarily tests text-based coordinate arithmetic, not visual understanding.** The SVG representation of Sort-of-Clevr images embeds explicit numeric coordinates, shapes, and colors as structured XML. Questions like "what is the shape of the object closest to the gray object?" can be solved by parsing coordinate values and computing distances—a pure text-manipulation task at which LLMs are known to excel. The paper acknowledges this obliquely ("the best-case scenario might be when images have the locations of certain shapes embedded in their XML code") but nonetheless frames the results as evidence of "visual understanding." This mismatch between the claim and what the task actually tests is the paper's central weakness: the strongest quantitative results do not require visual interpretation in any meaningful sense.

- **Uncontrolled comparisons undermine attribution of the main results.** The claim that GPT-4+SVG "surpasses a model explicitly trained for this task" (the Relation Network on Sort-of-Clevr) compares a ~1.7T-parameter zero-shot LLM processing structured XML with small trained vision models (CNN+MLP, Relation Networks) processing pixels. Everything differs—model scale, architecture, training data, input modality—so the comparison cannot isolate whether SVG is a good visual representation, or whether the LLM's general reasoning abilities (applied to any structured text) drive performance. Similarly, the OOD comparison (Vicuna+SVG vs. ConvNeXt+pixels) confounds representation format with model architecture. A controlled ablation (e.g., the same LLM with SVG vs. a flattened coordinate list, or a vision model trained on SVG-rendered PNGs) is needed to attribute performance to SVG's structural properties.

### Minor

- **Small sample sizes with no uncertainty quantification.** The visual reasoning experiment uses only 120 examples; Mini-MNIST classification uses 100 images; visual prompting uses 100 examples per task. No confidence intervals, error bars, or significance tests are reported anywhere. For the headline claim that GPT-CoT (89%) "surpasses" the Relation Network (81%) on Sort-of-Clevr, the confidence interval around 89% accuracy on 120 samples is roughly ±5–6 percentage points—meaning the two results may not be significantly different. This is a reproducible-evidence concern given the strength of the claims.

- **LLaVa is listed as an evaluated method but its results are absent.** The methods description (Section 3.1) states that LLaVa is among the zero-shot LLMs analyzed, but neither Table 1 nor the discussion reports LLaVa's accuracy. The reader is left wondering whether it was omitted due to cost, poor performance, or an error—this should be transparent.

- **Human evaluation procedure is underspecified.** The paper states that LLM outputs were "summarized post human evaluation to determine the final accuracy" but provides no details: number of annotators, handling of formatting mismatches, resolution of ambiguous answers, or inter-annotator agreement. Given that LLM outputs can be verbose or miss formatting expectations, this matters for reproducibility.

- **The "distribution shift" framing does not apply cleanly to zero-shot LLMs.** The paper tests GPT-4 under shape/color "distribution shifts" on Sort-of-Clevr and frames the observation that "the LLM does not suffer much" as evidence of robustness. But since GPT-4 is not trained on the original distribution, the concept of distribution shift is not meaningful in the same way as for trained models. The LLM is simply presented with new SVG text—this tests generality of instruction-following, not OOD robustness. The fine-tuning experiments (Vicuna/ConvNeXt) are properly framed as OOD; the GPT-4 results should be reframed.

- **The GPT-4 (Mini-MNIST, 100 images) and Vicuna/ConvNeXt (full MNIST test set) rows in Table 2 are on different test sets.** While the table separates these visually, the presentation invites implicit cross-row comparisons that are not apples-to-apples. The 4% ICL improvement is on a 100-image sample, making its generalizability unclear.

### Trivial

None.

## Nice-to-Haves

- A controlled ablation comparing GPT-4+SVG to GPT-4 with a flattened coordinate list (shapes without names) or a simple text representation of object positions would directly address whether SVG's *structure* matters or whether the results just reflect numerical reasoning from coordinates.
- Testing whether increasing the number of in-context examples further improves classification performance would strengthen the ICL claims.
- Reporting bootstrap confidence intervals for all quantitative results would dramatically improve interpretability without requiring more data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing Vicuna fine-tuning details / MNIST conversion quality.** The paper states these are in the supplementary materials, which were stripped by the parser. Per meta-review policy, missing appendix content is not a valid weakness.
- **"Limitations undermine the broader claim."** Having clearly stated limitations is a strength of the paper, not a weakness. A paper should not be penalized for being transparent about its scope.
- **"No discussion of SVG fidelity / lossiness before Limitations."** The related work section discusses SVG properties, and the Limitations section covers this—standard placement.
- **"Visual prompting lacks quantitative errors for style/content extrapolation."** This section is explicitly qualitative, which is legitimate for exploratory work. The paper does not frame it as a controlled experiment.
- **Demands for additional tasks/datasets beyond the paper's stated scope.** The paper's depth-oriented exploratory approach across 3 task families is defensible; requiring broader coverage would be scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension that the paper does not fully resolve: the Sort-of-Clevr results likely reflect the LLM's text-based arithmetic reasoning on explicit coordinate data rather than any form of visual understanding, but the paper's framing obscures this distinction. The most novel observation from the reviews is that the "distribution shift" framing is misleading for zero-shot LLMs—a point that the paper itself does not address.

## Suggestions

1. **Reframe the Sort-of-Clevr results.** Acknowledge directly that the task tests structured-text reasoning on coordinate data, not visual understanding. Add a controlled ablation (e.g., shuffled coordinates, removed shape names) to isolate which aspects of SVG drive performance.
2. **Add uncertainty quantification.** Bootstrap confidence intervals on all reported accuracies would give readers an honest picture of the evidence strength, especially given the small sample sizes.
3. **Report LLaVa results or explain their omission.** The current presentation is incomplete.
4. **Separate the GPT-4 and fine-tuning results more clearly** in Table 2, and avoid claims of "distribution shift robustness" for zero-shot models.
5. **Specify the human evaluation protocol** (number of annotators, handling of ambiguous outputs) in the main text.

## Score and Decision

The paper asks a legitimate and interesting question—can LLMs process images via SVG?—but the experimental evidence does not convincingly support the conclusions drawn from it. The Sort-of-Clevr results, which form the paper's strongest quantitative claim, are better explained by text-based coordinate arithmetic than by visual understanding. The uncontrolled comparisons prevent attribution of performance to SVG's properties. The small sample sizes without uncertainty quantification further weaken the quantitative claims. The paper's value lies primarily in its exploratory scope and the OOD fine-tuning experiment (Vicuna+SVG vs. ConvNeXt+pixels), which is the cleanest controlled comparison in the paper.

The contribution is real but falls short of what is needed to support the paper's framing. The paper would benefit from a redesigned evaluation that disentangles confounds, adds uncertainty estimates, and tempers its claims to match the evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>