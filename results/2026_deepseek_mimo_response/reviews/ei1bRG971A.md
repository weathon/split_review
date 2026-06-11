Now I have enough calibration data. Let me finalize the review.

**Calibration Analysis:**
- Round 1 bracket: 5.0 to 6.5 (DND is clearly better than rejected papers at 4.5-5.0 but has issues preventing it from matching accepted papers at 6.33-6.50)
- Round 2 anchors narrowed to ~5.75-6.5, with DND landing at ~6.0

**Anchor comparisons:**
- DND vs. Stutter (4.50, rejected): DND is clearly superior — broader evaluation (4 models up to 30B vs. Pythia up to 1B), post-training capability, no inference inefficiency problem, comprehensive ablations.
- DND vs. LazyLLM (5.00, rejected): DND is stronger — adds computation to selected tokens (vs. just pruning), more thorough evaluation, mechanism-level analysis.
- DND vs. CoTFormer (5.75, accepted): Comparable quality. CoTFormer has a more elegant architectural insight but smaller evaluation. DND has broader evaluation but weaker loss formulation explanation.
- DND vs. Learning How Hard to Think (6.50, accepted): DND has broader benchmark evaluation but "Learning How Hard to Think" has cleaner methodological claims and adaptive allocation framework.
- DND vs. RouteLLM (6.33, accepted): Different domains but RouteLLM's routing mechanism is clearer and its claims are better supported.

DND is positioned clearly above the rejected papers (4.50-5.00) and roughly comparable to CoTFormer (5.75), with the missing 100% baseline and loss formulation confusion pulling it below the accepted 6.33+ range.

## Summary
This paper proposes Dynamic Nested Depth (DND), a post-training method that improves LLM performance by dynamically selecting "critical" tokens via a learned router and reprocessing them through the same transformer layer. The router uses a sigmoid-based score compared against an adaptively controlled threshold, with two training strategies (router controlling loss and threshold control scheme) to ensure stable, discriminative token selection. Evaluated on three dense models (Qwen3-1.7B, Llama3.2-1B, Gemma3-1B) and one MoE model (Qwen3-30B-A3B), it reports +0.87% to +2.61% average improvements with ~6% extra FLOPs and ~7-8% throughput reduction.

## Strengths
- **Broad and consistent evaluation across diverse models and benchmarks**: Tables 1 and 2 demonstrate improvements across 4 models (Qwen3-1.7B, Llama3.2-1B, Gemma3-1B, Qwen3-30B-A3B) spanning 17+ benchmarks covering general knowledge, math, STEM, coding, and agent tasks. No individual benchmark shows regression on the MoE model, and dense models show pronounced gains on reasoning-heavy tasks (BBH +5.02, GPQA +5.80 for Qwen3-1.7B).
- **Token selection analysis validates the core mechanism**: Figures 4a and 4b provide direct quantitative evidence that DND's router preferentially selects high-entropy (uncertain) tokens (Pearson r=0.3359) and that nested reprocessing significantly reduces their logit entropy (Pearson r=-0.5811). This goes beyond aggregate benchmark numbers to demonstrate the mechanism works as designed.
- **Comprehensive ablation isolating each component's contribution**: Table 4 systematically varies router control, threshold control, selection ratio, and layer range, showing RC+TC yields +1.88 over baseline versus ~1.0 with either alone, demonstrating complementarity of the two training strategies.
- **Practical efficiency with minimal overhead**: Table 3 shows 91.6–93.1% throughput retention on a single H100 GPU with only 0.03M extra parameters and ~6% FLOPs increase, making DND deployable in practice.
- **Well-designed threshold control mechanism with clear visual evidence**: Figures 5 and 6a provide clear evidence that the dual-mechanism design (buffer proportional control + EMA synchronization) is necessary and effective at stabilizing selection ratios.

## Weaknesses

### Fatal
None.

### Major
- **Missing 100% selection (uniform recurrence) baseline** — Table 4 varies selection ratio at 10%, 20%, and 30%, but never includes 100% (reprocessing all tokens through the same layer). Without this baseline, the paper cannot distinguish between (a) the selection mechanism itself driving gains by focusing compute on hard tokens, vs. (b) any form of extra recurrence helping, with selection merely saving FLOPs. This directly affects whether the paper's core thesis — that *selective* reprocessing is superior to alternatives — is validated versus the contribution being primarily an efficiency optimization over uniform recurrence.

- **Ambiguous training setup comparison** — Section 4.2 states "the same learning rate applied" and "all parameters set as trainable" but does not explicitly confirm whether baseline SFT and DND SFT use identical training data, identical number of training steps, and identical total compute budgets. Because the DND model has an extra forward pass (~6% more FLOPs per step), if the number of training steps is held constant, DND effectively sees ~6% more compute than the baseline. This ambiguity matters for interpreting the improvements in Tables 1 and 2.

### Minor
- **Score Dispersion Loss description contradicts its mathematical effect** — Equation 6 normalizes routing scores by their sum and then minimizes negative entropy, which pushes normalized scores toward uniformity (all equal). This is the opposite of "dispersing" scores to create diversity. Meanwhile, Equation 7 (MSE toward 0.5) also pushes toward moderate uniformity. The described "push-pull dynamic" is therefore misleading — both losses push in the same direction (moderate uniformity), functioning more as regularization against score collapse than as dispersion. The empirical effect is positive (Table 4: RC helps +0.87), but the explanation of *why* it works appears incorrect. A more accurate framing would better serve the paper.

- **Positional embeddings in nested pass unspecified** — Equation 3 introduces new positional embeddings $\mathbf{E}_{\text{pos}}^i$ for the packed sequence but never specifies what these are (original token positions? Learned embeddings for compact sequence?). This affects how self-attention operates during the nested pass and is needed for reproducibility.

- **No statistical significance reporting** — All results are single-run numbers. The headline improvements for dense models (+1.88 to +2.61) are modest, and on smaller benchmarks like GPQA-Diamond (~198 examples) and BBH (~600 examples), sampling variance matters. For the MoE model, the average improvement of +0.87 could plausibly be within noise on some individual benchmarks. Error bars or multiple seeds would strengthen confidence.

### Trivial
None.

## Nice-to-Haves
- Discussion of why DND helps less on MoE models (+0.87 vs. +1.88–2.61 on dense). MoE already has routing mechanisms; acknowledging this redundancy would refine positioning.
- MOR as a comparison point in Table 1 (discussed in §2.2 but not empirically compared).
- Total training compute comparison showing DND's training cost is also modest.
- The qualitative example in Figure 7b is interesting but limited to a single QA instance.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Nitpicks about formatting, typos, or parser artifacts — these are not present in the original paper.
- Missing related works — cannot verify from the paper alone.
- The harsh critic's note about ITT being "dismissed" — the paper does compare ITT in Table 1 and explains the mismatch, which is a reasonable treatment.

## Novel Insights
The token selection analysis (Figures 4a/4b) reveals a genuinely informative pattern: the router selects tokens proportional to their logit entropy (uncertainty), and nested reprocessing subsequently reduces that entropy. The hierarchical selection visualization (Figure 7b) — where shallower layers select essential nouns and deeper layers select abstract mathematical expressions and key verbs — provides interpretable evidence that DND's depth allocation is semantically meaningful rather than arbitrary.

## Suggestions
- Add a 100% selection ratio row to Table 4 to validate that selection (not just extra computation) drives the gains.
- Clarify the loss formulation: either correct the description to "preventing score collapse / regularization" or modify the loss to genuinely encourage dispersion on raw sigmoid scores.
- Specify positional embeddings in Equation 3 for reproducibility.
- Confirm identical training data, steps, and compute between baseline SFT and DND SFT.
- Report error bars or multiple seeds, at minimum on the smaller benchmarks.

## Score and Decision

**Round 1 anchors (bracketing):**
- FiRST (3.00, weak): Layer skipping for latency reduction, rejected. DND is more comprehensive.
- EfficientSkip (2.50, weak): Dense-to-sparse conversion, rejected. Less related.
- Stutter (4.50, middle-low): Selective additional layers for hard tokens, rejected. Very similar concept but DND is clearly better (broader eval, post-training, no inference inefficiency).
- LazyLLM (5.00, middle-low): Dynamic token pruning, rejected. DND goes further (reprocesses tokens vs. just pruning).
- CoTFormer (5.75, middle): Chain-of-thought architecture with adaptive computation, accepted. Comparable quality to DND.
- Learning How Hard to Think (6.50, upper-middle): Adaptive computation allocation, accepted. Cleaner claims but different scope.
- RouteLLM (6.33, upper-middle): Router between LLMs, accepted. Different domain.
- MoE++ (8.00, strong): Zero-computation experts in MoE. Much stronger.

**Round 2 anchors (narrowing):**
- Understanding In-Context Learning (5.50, lower-middle): Analysis paper, less comparable.
- Looking Beyond Top-1 (6.40, upper-middle): Analytical understanding paper, rejected despite high score.
- LazyLLM (5.00): Same as above.
- RouteLLM (6.33): Same as above.
- Learning How Hard to Think (6.50): Same as above.
- GraphRouter (6.50, upper-middle): LLM selection framework, accepted.
- CoreInfer (6.25, upper-middle): Adaptive sparse activation, rejected despite score.

**Bracket**: DND sits clearly above rejected papers at 4.5-5.0 (Stutter, LazyLLM) and comparable to CoTFormer (5.75), but below accepted papers at 6.33+ (RouteLLM, Learning How Hard to Think) due to the missing 100% baseline and loss formulation issues. The broad evaluation and token-level analysis are genuine strengths that prevent scoring below 5.5.

**Final score: 6.0** — DND is a solid empirical contribution with broad evaluation and practical efficiency, but the missing uniform-recurrence baseline and loss formulation confusion prevent it from reaching the quality of accepted papers in the 6.33+ range. The method likely works, but the evidence as presented doesn't fully validate the core thesis that *selection* drives the gains.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>