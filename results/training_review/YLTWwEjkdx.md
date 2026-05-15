Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper investigates redundancy across three Transformer module granularities—entire Blocks, MLP layers, and Attention layers—using a cosine-similarity-based importance metric. The central finding is that Attention layers are far more redundant than Blocks or MLP layers across Llama-2, Llama-3, and Mistral model families, with results such as Llama-2-70B retaining 71.5 vs. 73.9 average performance after dropping 40 of 80 attention layers. The paper also traces attention importance scores across MAP-Neo-7B checkpoints, showing the redundancy is consistent throughout training, and proposes Attention Drop and Joint Layer Drop as training-free pruning methods.

## Strengths

- **Empirical breadth across model scales and families**: The paper tests Block, MLP, and Attention dropping on Llama-2 (7B/13B/70B), Llama-3 (8B/70B), and Mistral-7B—eight model configurations—on a consistent set of eight benchmarks (Tables 1, 4). This systematic documentation of *which* components are redundant and to what degree is a useful empirical contribution. The finding that attention layers can be removed far more aggressively than blocks or MLPs holds across all tested models.

- **Training-stage analysis (MAP-Neo-7B checkpoints)**: Using continuous checkpoints released by MAP-Neo-7B, the paper shows that attention layers maintain consistently lower importance scores than MLP and block modules throughout pretraining (Figure 6). This is the most novel contribution—it suggests the redundancy is an inherent architectural property rather than a post-training artifact.

- **Concrete efficiency measurements**: The paper provides measured KV-cache reductions (e.g., Llama-2-13B from 52GB to 26GB) and wall-clock speedups (up to 1.48× for Llama-2-70B, Table 4), giving practitioners actionable data about the practical benefits of attention-layer pruning. The SDR metric (γ) provides a clean way to compare efficiency–performance trade-offs across methods.

- **Cross-calibration-dataset validation**: Importance scores are computed using C4, CodeAlpaca-20k, MathInstruct, and LIMA (Figures 2, 3), showing the redundancy pattern is not an artifact of a single calibration distribution.

## Weaknesses

### Fatal
None.

### Major

1. **The similarity-based metric is not validated against alternatives, and the evaluation lacks a random-dropping control.** The paper uses score = 1 − CosineSim(x, y) to rank module importance. For a residual block where y = x + f(x), if the residual f(x) is small in norm, y ≈ x regardless of whether f(x) is functionally critical—cosine similarity cannot distinguish "this layer contributes nothing" from "this layer makes a small-magnitude but essential correction." The paper never validates this metric by comparing its rankings to gradient-based importance, loss-impact analysis, or—most critically—by showing that dropping low-score attention layers outperforms dropping the *same number of random* attention layers. Figure 3 plots "random guessing" as a task-level reference line, not a random-dropping curve. Without this control, it is unclear whether the metric is selecting genuinely redundant layers or whether all attention layers (or a random subset) could be dropped with similar results. While the absolute results (e.g., 71.5 after dropping 40/80 attention layers) are still informative, the claim that the metric *identifies* redundancy is unsupported.

2. **Evaluation is limited to short-context, non-attention-intensive tasks.** The eight benchmarks (ARC-C, BoolQ, HellaSwag, MMLU, OBQA, PIQA, RTE, WinoGrande) all involve single sentences or short paragraphs with limited-length dependencies. None require long-range context, document-level reasoning, multi-hop synthesis over long inputs, or the complex attention patterns that motivate the Transformer architecture. The abstract and introduction frame the finding as general ("a large portion of these layers...can be pruned without degrading performance"), but the experimental design does not support claims about attention redundancy in settings where attention should matter most. Adding at least one long-context evaluation (e.g., a summarization task or long-document QA) is necessary to assess whether the finding holds outside the short-context regime.

### Minor

1. **No comparison to existing structured pruning methods.** The paper evaluates Block Drop, MLP Drop, and Attention Drop solely against each other. Block Drop is essentially ShortGPT's method (which the paper cites), so the paper implicitly compares against this baseline—but does not benchmark against LLM-Pruner, SliceGPT, or other structured pruning approaches. Without such comparisons, the practical value of Attention Drop relative to the state of the art is unclear. The paper's contribution is primarily analytical (discovering which components are redundant), so this weakness is not fatal, but it limits the paper's claims about method effectiveness.

2. **Speed measurements mix precision across model comparisons.** For Llama-2-70B, 4-bit quantization is used to fit on a single GPU, while other models use 16-bit precision (Section 5). This makes speedup comparisons across models inequitable, since quantization and attention pruning are interacting factors. The paper notes this is "orthogonal" but does not isolate the Attention Drop contribution from the quantization effect.

3. **SDR definition (γ) uses ambiguous language.** Line 168 defines ΔAvg. as "percentage change in average performance," but the actual computation uses absolute point differences (e.g., 73.9 − 71.5 = 2.4), not relative percentages. The numbers are reproducible when interpreted this way, but the definition should be clarified. Similarly, the abstract reports "2.4% performance drop" for Llama-2-70B, which is actually 2.4 absolute points (≈3.25% relative)—this loose phrasing could mislead readers.

### Trivial

- The paper does not discuss calibration dataset size, variance across samples, or stability of the importance-score ranking. This could affect reproducibility for practitioners.
- MLP Drop's inherently limited speedup (1.04–1.08×) is presented as a weakness of the method rather than a necessary consequence of MLPs being parameter-heavy. A brief acknowledgment of this asymmetry would improve exposition.

## Nice-to-Haves

- A random-dropping *attention layer* baseline (not task-level random guessing) would substantially strengthen the claim that the metric selects meaningfully redundant layers.
- A small fine-tuning-after-pruning experiment (even limited to one model) would connect the work to community standards for structured pruning.
- Visualizing attention maps before/after dropping to check whether remaining layers compensate for removed ones.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The central claim is invalidated by the metric"** — Overstated. The empirical results (actual performance after dropping) do not depend on the metric being theoretically ideal. The paper demonstrates *that* attention layers can be dropped; the metric is the selection mechanism, but the raw outcomes are independently meaningful.
- **"Joint Layer Drop is a trivial combination"** — The paper frames it as a natural extension, not a radical invention. The observation that it outperforms single-type dropping at high sparsity is still useful.
- **"Cherry-picking MMLU for the 90% claim"** — The paper explicitly says "on the MMLU task" (line 502), so this is honest reporting, not cherry-picking.
- **"No discussion of calibration dataset size/variance"** — This is a standard detail that could be added but is not a substantive flaw.
- **"The 48.4% speedup / 2.4% drop phrasing is 'inaccurate'"** — The speedup is correct (1.48× = 48% faster). The "2.4%" is ambiguous (points vs. percent), but this is a minor presentation issue, not factual error.

## Novel Insights

The most genuinely novel observation from the reviews is the tension between the paper's short-context evaluation and its general claim about attention redundancy. Several reviewers noted that the tasks tested (ARC-C, BoolQ, HellaSwag, etc.) may not exercise attention mechanisms in the ways that motivate Transformer architectures. This raises an interesting question: is the paper discovering a fundamental property of attention layers, or merely that simple benchmarks don't require much attention? The training-stage analysis (Figure 6) partially addresses this by showing the pattern is consistent throughout pretraining, but without long-context evaluations, the generalization remains unproven. A productive follow-up would be to check whether the same attention layers are redundant on long-context tasks, and if redundancy varies by layer depth in those settings.

## Suggestions

1. **Add a random-dropping attention-layer baseline.** Compare performance after dropping the same number of attention layers selected by the similarity metric vs. randomly selected. This distinguishes redundancy *detection* from redundancy *existence*.
2. **Add at least one long-context evaluation** (e.g., QMSum, NarrativeQA, or a long-context variant of an existing task) to probe attention requirements.
3. **Validate the metric** by correlating cosine-similarity rankings with at least one alternative importance measure (e.g., gradient magnitude or loss change on held-out data) on a subset of models.
4. **Clarify the SDR and percentage-drop language** to distinguish absolute points from relative percentages.
5. **Separate the quantization and pruning speedups** for the 70B model to isolate the Attention Drop contribution.

## Score and Decision

**Originality**: Moderate — the core finding (attention redundancy) is somewhat anticipated by prior work on layer dropping (ShortGPT, Gromov et al.), but the systematic comparison across three granularities and the training-stage trace provide new insights.  
**Importance of research question**: High — understanding which components are redundant has direct implications for efficient architecture design.  
**Claims supported**: Partially — the central claim about attention redundancy is supported for short-context tasks across multiple model families, but the metric is unvalidated and the scope is narrower than claimed.  
**Soundness of experiments**: Adequate but incomplete — missing random-dropping baseline, no long-context tasks, no comparison to existing pruning methods.  
**Clarity of writing**: Good — well-structured and generally clear.  
**Value to community**: Moderate — practitioners will find the efficiency numbers useful, and the training-stage analysis is a genuine contribution to understanding attention behavior.

The paper has a real empirical contribution (documenting attention layer redundancy across model families and training stages) but is limited by an unvalidated selection metric, a short-context-only evaluation, and missing baselines. These are addressable in a major revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>