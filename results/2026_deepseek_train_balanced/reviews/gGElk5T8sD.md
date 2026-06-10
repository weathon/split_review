## Summary

The paper proposes Self-Lengthen, an iterative training framework that enables open-source LLMs to generate long texts without external data or proprietary models. The framework alternates between a Generator (producing initial responses) and an Extender (expanding responses via a two-stage process), using self-generated outputs as training data. Applied to Qwen2-7B-Instruct and LLaMA3.1-8B-Instruct, the method achieves output length growth from ~1,000 to ~8,000 words over three macro-iterations.

## Strengths

- **Novel self-contained iterative paradigm.** Unlike Suri (requires high-quality human-written text) or LongWriter (requires GPT-4), Self-Lengthen needs only seed instructions and an open-source instruct model. Table 1 directly contrasts these resource requirements, making the contribution clear.

- **Two-stage extension mechanism with a non-trivial design choice.** The method splits extension into two stages (lines 136-145): first extending only the first half, then using the first two-thirds of the extended half as in-context demonstration for extending the remainder. The deliberate 1/3 truncation to avoid abrupt transitions is a well-motivated practical technique that addresses the bottleneck of single-shot extension limits.

- **Length-bias sampling with distributional evidence.** The cubic-decay sampling formula (Equation, lines 176-179) demonstrably accelerates iteration. Figure 7 directly compares length and score distributions with and without this technique, showing accelerated length growth without quality degradation.

- **General-task performance is preserved.** The paper reports (line 234) that MMLU and AlignBench performance remains nearly equivalent after long-generation fine-tuning, with a noted improvement on AlignBench for the LLaMA model. This addresses the common concern about specialized fine-tuning harming general capabilities.

- **Consistent length doubling quantified across iterations.** Figure 7 shows steady growth from ~1,000 to ~8,000 words over three macro-iterations using violin plots (distributional evidence, not point estimates). Each iteration roughly doubles output length, directly validating the central mechanism.

## Weaknesses

### Fatal

None.

### Major

- **Very small human evaluation for comparative claims.** The data-level human evaluation uses only 15 query-response pairs per method (line 208). With ~3-4 methods, this is 45-60 total samples. No confidence intervals, significance tests, or inter-annotator agreement are reported. The abstract and introduction claim Self-Lengthen "consistently achieves better long-text generation capabilities compared to instruction backtranslation and behavior imitation," but the human evidence supporting this comparative claim is far too thin. The model-level evaluation (main results table) appears to rely entirely on GPT-4o-based judgments — there is no human evaluation of the fine-tuned models' outputs.

- **Ad-hoc, non-standard benchmark.** The evaluation benchmark is constructed from undisclosed "online logs" with prompts rewritten by GPT-4o (lines 222-223). No standardized long-generation benchmark (LongBench, HELLOBench, or any published evaluation set) is used. This makes it difficult for readers to situate results relative to known work or assess whether the benchmark systematically favors the proposed method. The total size, domain coverage, and selection methodology are not reported in the available text.

### Minor

- **GPT-4o evaluation confound.** GPT-4o is used for both benchmark construction (prompt rewriting) and evaluation (quality scoring, pairwise win-rates). The human evaluation is too small to independently validate the GPT-4o judgments. While the method does not train on GPT-4o outputs (mitigating the stronger form of circularity), LLM-as-judge evaluation is known to exhibit systematic preferences. The paper does not discuss this limitation, include agreement analysis with a different judge model, or report correlation between GPT-4o scores and human judgments.

- **Baseline comparison fairness.** The paper adds length constraints to the original Suri and LongWriter queries (line 230) to "ensure a fair comparison." The proposed method was trained to follow length constraints; the baselines were not. This modification could advantage the proposed method. The paper should evaluate baselines on their original query formats as a separate condition and discuss any differences.

- **Missing implementation details.** The extend prompt is referenced as `prompt_{EXT}` (lines 103-104, 181) but never shown verbatim. Training hyperparameters (learning rate, batch size, optimizer, GPU hardware, training time) are not reported. These are important for reproducibility and for assessing the practical cost of the method.

- **No computational cost analysis.** Iterative training with two models and repeated extension is more expensive than a single SFT pass. The paper does not quantify training time, GPU requirements, or inference overhead relative to baselines.

### Trivial

None.

## Nice-to-Haves

- Evaluate on at least one standardized benchmark (e.g., LongBench generation tasks or HELLOBench) to complement the ad-hoc benchmark and enable external comparison.
- Include failure case analysis by query type or domain — the paper reports only average scores.
- Justify the choice of three macro-iterations and three micro-iterations (is this from a sweep, or could more iterations cause quality degradation?).
- The style-adjustment experiment (lines 263-271) is interesting but preliminary; deeper analysis would strengthen it.

## Removed Points

These are flagged for removal; treat them with caution.

- Criticism that the benchmark is "never named or described": the paper describes the construction process (lines 222-223). The benchmark name (LaTeX `\benchname`) and statistics table are stripped by the parser — removed per the rule about content stripped by the parser existing in the original submission.
- Criticism that Suri subset selection (3,000 samples) is not justified: the paper states "randomly selected," a standard sampling justification — removed as overly picky.
- Criticism of "no human assessment at all for model-level evaluation": factually incorrect — the paper does include a human evaluation, though it is small. Removed on factual grounds.
- Criticism about missing discussion of model collapse from self-training: speculative concern about a risk not demonstrated in the paper's 3-iteration setup, and the paper reports maintained quality scores. Removed as insufficiently grounded in the paper.
- Strength Finder's generic claims ("important problem," "interesting question"): removed per instructions about generic/superficial strengths.
- Several "Strengthening the Paper" suggestions from the Harsh Critic are folded into the Nice-to-Haves section rather than listed as separate weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Expand the human evaluation to at least 50-100 samples per method with inter-annotator agreement reporting, so the comparative claims are properly supported.
2. Include at least one standardized long-generation benchmark, or release the full benchmark with detailed documentation of its construction, size, and domain coverage.
3. Report the extend prompt verbatim and provide training hyperparameters (learning rate, batch size, optimizer, GPU hardware, training steps).
4. Evaluate baselines on their original query formats (without added length constraints) as a separate condition, and discuss any differences.
5. Include agreement analysis between GPT-4o judge scores and human judgments, or add a second judge model.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>