Now I have sufficient calibration data. Let me construct the final review.

## Summary

This paper introduces Wanda (Pruning by **We**ights **a**n**d** **a**ctivations), a simple pruning method for LLMs that computes weight importance as the product of weight magnitude and the L2 norm of the corresponding input activation, evaluated per output neuron. The method requires no retraining or weight update — just a single forward pass with a small calibration set. Experiments on LLaMA and LLaMA-2 (7B–70B) across unstructured, 4:8, and 2:4 sparsities show that Wanda dramatically outperforms magnitude pruning and is competitive with SparseGPT while being over 200× faster.

## Strengths

- **Simple yet principled pruning metric.** The proposed score $|\mathbf{W}_{ij}| \cdot \|\mathbf{X}_j\|_2$ directly addresses the known issue of emergent large-magnitude features in LLMs (Section 2). The connection to OBD/OBS is explicitly shown via a clean reduction (Equation 3). This is not an ad-hoc heuristic — it arises as a diagonal approximation of the second-order pruning metric used by SparseGPT.

- **No weight update, yet competitive with SparseGPT.** Despite modifying no remaining weights, Wanda matches SparseGPT on both perplexity and zero-shot accuracy across nearly all model sizes and sparsity configurations (Tables 2 and 3). For example, on LLaMA-65B at 50% sparsity, Wanda achieves 4.57 perplexity (identical to SparseGPT) and 66.67% zero-shot accuracy (vs. 66.30% for SparseGPT). This demonstrates that exact sparse subnetworks exist in pretrained LLMs.

- **Dramatic speed advantage.** Pruning LLaMA-65B takes 5.6 seconds with Wanda versus 1353.4 seconds for SparseGPT — a >240× speedup (Table 4). This is practically significant for iterative pruning or sparse training settings.

- **Insightful ablation disentangling metric vs. grouping.** Table 6 systematically varies both the pruning metric and the comparison group, revealing that the per-output comparison group is critical. Strikingly, even magnitude pruning benefits enormously from choosing the right comparison group (perplexity drops from 17.29 for layer-wise to 8.86 for per-input grouping), showing the paper's main insight about comparison granularity is a general principle for LLM pruning.

- **Robustness to scarce calibration data.** Figure 1 shows Wanda maintains perplexity of 7.66 even with a single calibration sample, while SparseGPT degrades sharply. This robustness stems from simpler estimation of input norms versus full Hessian inverses.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core contribution. The paper's central claims are well-supported.

### Minor

- **Unsupported claim about image classifiers (Section 3).** The paper states: *"we conduct additional experiments on pruning image classifiers. However, we do not observe similar trend in image classification models, suggesting that our observations regarding pruning per output might be unique to LLMs."* No data, figure, table, model name, dataset, sparsity level, or metric is provided to support this claim. The paper hedges ("might be unique"), but stating that experiments *were conducted* without showing any evidence is a presentation gap. This is easy to fix by either adding the results or removing the sentence.

- **Fine-tuning experiments limited to LLaMA-7B.** The fine-tuning study (Table 8) is only conducted on LLaMA-7B. Replicating on at least one larger model (e.g., LLaMA-13B or LLaMA-2-13B) would strengthen the conclusion that fine-tuning can reliably close the gap to the dense model at scale.

- **No variance reporting for the main results.** All perplexity and accuracy numbers in Tables 2 and 3 are reported as single values without variance across different calibration draws. While the method is deterministic given fixed calibration data, a brief study (e.g., 5 random draws of 128 sequences from C4) would quantify sensitivity to the specific calibration sample.

### Trivial

- The paper mentions Wanda can be "seen as a renaissance of OBD" (Section 3, Remark). The connection is more of a loose analogy than a derivation — the paper already hedges appropriately ("can be seen as"), so this is a minor presentational point, not a flaw.

## Nice-to-Haves

- A brief qualitative analysis of *why* per-output grouping helps (e.g., showing that output neurons have widely varying parameter norms, and per-output pruning avoids destroying entire outputs) would deepen insight.
- The image classifier data, if it exists, should be included.
- Applying Wanda to newer model families (e.g., Llama 3, Mistral) would show the method is not tied to a specific architecture.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Strength Finder's claim that "even magnitude pruning benefits drastically from per-output grouping (perplexity 8.86 vs 17.29)"* — the 8.86 value is actually for **per-input** (input, 1) grouping, not per-output. Per-output gives 13.41 for magnitude pruning. The broader point (comparison granularity matters greatly) still holds; the specific grouping is misattributed.
- *Harsh Critic's note about "OBD connection is a loose analogy"* — the paper already uses hedging language ("can be seen as") and provides the exact mathematical reduction from SparseGPT's metric to Wanda's metric. The criticism does not identify a genuine problem.
- *Various formatting/style nitpicks* — parser artifacts, not author errors.
- *Missing related works* — cannot be verified without external sources.
- *Missing appendix/proofs* — parser-stripped sections.

## Novel Insights

The reviews collectively surface one insight that goes beyond the paper's own contributions: the ablation in Table 6 reveals that comparison granularity — **how weights are grouped for pruning decisions** — may be as important as the pruning metric itself. The fact that even magnitude pruning, a decades-old method, can be rescued from a perplexity of 17.29 down to 8.86 simply by choosing per-input grouping (input, 1) is a non-obvious finding. This suggests that much of the prior literature on pruning may have conflated metric design with grouping strategy, and that future work should treat comparison granularity as a first-class design axis rather than an afterthought. This is a concrete, actionable insight for the pruning community.

## Suggestions

1. **Add the claimed image classifier results** or remove the unsupported sentence from Section 3. A small table showing per-output vs. per-layer pruning for e.g., ResNet-50 on ImageNet at comparable sparsities would suffice.
2. **Report variance** for at least one representative setting (e.g., LLaMA-7B at 50% sparsity with 5 different 128-sample draws from C4) to quantify calibration sensitivity.
3. **Extend fine-tuning experiments** to at least one larger model (13B or 30B) to confirm the trend holds at scale.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/.../f4gF6AIHRy.md` (DiSF) | 8.00 | Very strong paper with thorough experiments, but limited to ≤1.1B models. Wanda tests up to 70B, giving it wider practical scope. Comparable quality. |
| `/home/.../OfjIlbelrT.md` (FlexPrefill) | 8.00 | Unanimous 8s — extremely polished. Wanda is similarly solid but has minor missing-evidence issues (image classifier claim). Slightly below this anchor. |
| `/home/.../ngmEcEer8a.md` (Layer Pruning) | 6.50 | Good empirical study, but simpler contribution. Wanda has both a novel method and more thorough evaluation. Clearly stronger. |
| `/home/.../ldJXXxPE0L.md` (Cost of Scaling Down) | 6.00 | Analysis paper with modest novelty. Wanda proposes a new method with practical impact. Stronger. |
| `/home/.../wV9iMiyQcc.md` (RotPruner) | 5.33 | Requires rotation + retraining, overhead concerns. Wanda is simpler, cleaner, and more practical. Stronger. |
| `/home/.../0Ag8FQ5Rr3.md` (Super Weight) | 4.60 | Interesting observation but marginal improvements. Wanda is a more complete, impactful contribution. Significantly stronger. |
| `/home/.../IU4L7wiwxw.md` (PGZ) | 4.50 | Writing issues, marginal gains over SparseGPT. Wanda is much cleaner and more convincingly demonstrated. Significantly stronger. |

### Assessment

The paper presents a clean, well-motivated pruning method with a strong empirical evaluation across models up to 70B, multiple sparsity formats, and two evaluation axes. The central claims — that the product of weight magnitude and activation norm with per-output grouping is an effective pruning metric, and that sparse subnetworks exist exactly in pretrained LLMs — are convincingly supported. The method's simplicity and speed are genuine practical advantages. The only notable weakness is an unsupported claim about image classifiers, which is peripheral to the main contribution. Overall, this is clearly an accept-quality paper.

**Originality:** Good — the metric itself is a novel combination of existing ideas, applied insightfully to LLMs. The per-output grouping finding is non-obvious.

**Importance:** High — LLM compression is a critical problem, and Wanda's simplicity makes it immediately useful as a baseline and practical tool.

**Claims supported:** Well-supported for the LLM claims. One minor unsupported claim about image classifiers.

**Soundness:** Strong — appropriate baselines, careful ablations, thorough evaluation across model sizes.

**Clarity:** Very good — well-written, clear motivation with the two-weight example, helpful PyTorch pseudocode.

**Value to community:** High — already influential as a NeurIPS publication.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>