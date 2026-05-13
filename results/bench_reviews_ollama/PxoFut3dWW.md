## Summary
The paper introduces Wanda, a pruning method for LLMs that scores weights by the product of weight magnitude and the L2 norm of the corresponding input activations, compared on a per-output basis. It requires no weight update or second-order information and runs in a single forward pass, yet matches SparseGPT at 50% unstructured sparsity on LLaMA/LLaMA-2 (7B–65B) while computing the metric ~150–300× faster.

## Strengths
- **Activation-aware metric closes most of the gap to SparseGPT without weight updates** (Table 2): on LLaMA-7B at 50% sparsity, Wanda 7.26 vs SparseGPT 7.22 vs magnitude 17.29; parity holds up to 65B (4.57 vs 4.57). This is the central empirical claim and it is supported.
- **Per-output comparison group is a clean, separable finding** (Table 6/5): even plain magnitude pruning improves from 17.29 → 8.86 PPL when grouped (input,1), showing the grouping axis is an independent contribution from the metric.
- **Metric computation is dramatically cheaper than SparseGPT** (Table 4: 0.54s vs 203s on 7B; 5.6s vs 1353s on 65B), making Wanda a practical drop-in baseline.
- **Robustness to calibration size** (Fig. 2/4): a single calibration sample yields PPL 7.66, while SparseGPT degrades to 8.02 — a genuinely surprising property that distinguishes Wanda from second-order methods.
- **Honest reporting**: 2:4 cases where SparseGPT wins on smaller models are not hidden, and the weight-update ablation (Table 7) is included.

## Weaknesses

### Fatal
None.

### Major
- **"Competitive with SparseGPT" framing is asymmetric for structured 2:4 sparsity on small models** — On LLaMA-7B 2:4: Wanda 11.53 PPL vs SparseGPT 11.00; LLaMA-2-7B: 11.02 vs 10.17; zero-shot accuracy shows similar gaps (~2 points). Since 2:4 is the regime that delivers actual tensor-core speedups (per §5.3), the headline framing should track this asymmetry rather than be calibrated to the 50%-unstructured result.
- **Generality of the central claim rests on a single model family** — All language-modeling results use LLaMA/LLaMA-2. Since the motivation hinges on emergent outlier features (an empirical, family-sensitive phenomenon), demonstrating Wanda on at least one non-LLaMA family would substantially strengthen claims like "exact sparse subnetworks exist for LLMs."

### Minor
- **The OBD reduction in Eq. 6 is presented with a "diagonal approximation" equality** — Replacing diag((X^TX)^{-1}) with (diag(X^TX))^{-1} is only tight when X^TX is near-diagonal, which is the opposite of the outlier-correlation regime that motivates the method. Framing this as motivation rather than derivation would be more honest.
- **Per-output grouping is shown to help but not explained** — The grouping is arguably the more surprising empirical finding than the metric itself, yet Section 5 only restates it. A per-neuron analysis of ||X_j|| distributions, or a direct measurement of how grouping interacts with outlier columns, would convert a curiosity into a deeper contribution.
- **Only WikiText PPL is reported in the main tables** — Since calibration is drawn from C4, C4 PPL is the natural cross-domain check; its omission is a small but conspicuous gap.
- **Fine-tuning comparison is one-sided** — §6 shows LoRA recovers some gap for Wanda, but does not report SparseGPT after the same fine-tuning, leaving open whether Wanda's "no weight update" advantage survives post-hoc adaptation.

### Trivial
- End-to-end speedup (1.24× on 7B) vs kernel-level (1.6×) gap could be acknowledged explicitly as prototype-level rather than deployment-ready.
- The aside that image classifiers do not benefit from per-output grouping is highlighted as "intriguing" but the supporting numbers are deferred; one concrete number in the main text would help.

## Nice-to-Haves
- Higher sparsity sweeps (60/70/80%) for Wanda vs SparseGPT in the main tables.
- Mask-overlap analysis between Wanda and SparseGPT to clarify whether they identify the same subnetwork.
- A minimal Wanda + weight-update variant for 2:4 to close the small-model gap (Table 7 already hints at this).
- Non-uniform per-layer sparsity allocations combined with Wanda's metric.
- Direct measurement of how often Wanda preserves weights connected to outlier channels relative to magnitude pruning, closing the motivational loop.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- "Uniform sparsity is a choice not a finding" — Reasonable as a nice-to-have but not a real weakness; uniform allocation is the standard baseline used in SparseGPT comparisons, and the paper does not claim non-uniformity is solved.
- "LoRA r=8 on Q/V only is thin" — Standard fine-tuning recipe in this literature; criticizing it as insufficient is scope creep.
- "Reproducibility / availability" concerns: none flagged; nothing to remove here.

## Novel Insights
None beyond the paper's own contributions. The most genuinely novel observation — that even plain magnitude pruning becomes competitive when grouped per-output — is the paper's own.

## Suggestions
- Soften the "competitive with SparseGPT" claim in the abstract/intro to specifically reference 50% unstructured, and add a one-clause acknowledgment of the 2:4 gap on 7B models.
- Add at least one non-LLaMA family (e.g., OPT, Falcon, or Mistral) at 50% unstructured + 2:4.
- Reframe Eq. 6 as "motivation via diagonal approximation" rather than an equivalence chain.
- Report C4 (and optionally PTB) perplexity alongside WikiText.
- Add an analysis section explaining *why* per-output grouping helps (distribution of ||X_j||, outlier channel localization, or per-neuron sparsity balance).
- Include SparseGPT-after-LoRA in the fine-tuning comparison.

---

**Overall assessment.** Originality: moderate — the metric is simple but combines magnitude and activation norms in a way that proves surprisingly effective; the per-output grouping finding is the more original contribution. Importance: high — LLM pruning is a deployment-relevant problem and a strong, training-free baseline has real practical value. Soundness of claims: well-supported for 50% unstructured on LLaMA; partially supported (with honest reporting) for 2:4 and only on one model family. Experiments: thorough on LLaMA-family but narrow in family coverage. Clarity: good. Value to community: high — the method is trivial to implement and reproduce, and will function as a baseline for subsequent pruning work. The flaws are bounded and addressable; none undermines the core claim.

## Score and Decision
MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>