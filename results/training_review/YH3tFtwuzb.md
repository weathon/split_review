Now I have all the information I need to produce the final consolidated review.

## Summary

This paper studies differentially private fine-tuning of large pre-trained models by training only the bias terms (DP-BiTFiT). The core insight is that bias gradients have a uniquely simple computation graph that makes the per-example gradient clipping overhead independent of the feature dimension \(T\) — a property that no weight-training DP method (including LoRA, Adapter, full fine-tuning) possesses. The paper provides a systematic complexity analysis (the first of its kind for DP PEFT methods), demonstrates 2–30× speedup and 2–8× memory reduction over DP full fine-tuning across language and vision benchmarks, and shows competitive accuracy (matching or exceeding prior DP methods on GLUE, E2E, CIFAR, and CelebA) while training only ~0.1% of parameters.

## Strengths

1. **First systematic complexity analysis of DP for PEFT methods (Table 2).** The paper rigorously separates time and space costs for weight vs. bias training under DP, covering Opacus, GhostClip, MixGhostClip, LoRA, and Adapter for the first time. This analysis reveals that only bias training has DP overhead independent of feature dimension \(T\), which is a genuinely novel analytical contribution that was missing from prior DP and non-DP PEFT literature (including the original BiTFiT paper).

2. **Compelling and thorough efficiency experiments.** Figures 2–4 directly measure memory, throughput, and batch-size scaling with both feature dimension and model size across multiple architectures (RoBERTa, GPT2, ResNet, ViT). The results convincingly demonstrate that DP-BiTFiT's efficiency advantage grows with data dimensionality — e.g., at \(T=512\) in text tasks, DP-BiTFiT uses <4GB memory vs. >16GB for DP full fine-tuning (Fig. 3).

3. **Competitive accuracy with extreme parameter efficiency.** Across text classification (Table 1), NLG (Table 3), and image classification (Tables 4–5), DP-BiTFiT matches or approaches SOTA while training only ~0.1% of parameters. Notably, it outperforms DP full fine-tuning on GPT2-large BLEU (65.21 vs. 64.64 at \(\epsilon=8\)) and on CIFAR100 with ViT-large (91.2% vs. 90.1% at \(\epsilon=2\)).

4. **Model-agnostic design with simple implementation.** DP-BiTFiT works on any network architecture (BERT, RoBERTa, GPT2, ViT, ResNet, etc.) without architectural modifications, and requires essentially one line of code change — a practical advantage for adoption.

5. **Identified scaling pattern (Remark 1).** The observation that the accuracy gap between BiTFiT and full fine-tuning (both DP and non-DP) shrinks with model size — from 1.4% to 0.1% on QNLI, from -3.06 to +0.57 BLEU on GPT2 — is an interesting empirical finding not highlighted in prior work.

## Weaknesses

### Fatal
None.

### Major

1. **Accuracy comparisons rely on prior-published numbers without controlled re-evaluation.** The DP full fine-tuning results in Table 1 are cited from Li et al. 2021, and DP LoRA/Adapter/Compacter results from Yu et al. 2021, without being re-run in a unified environment with matched hyperparameters, privacy accounting, and tuning budgets. While the paper states it uses "the same setup as Li et al. 2021," small differences in learning rate schedules, batch sizes, or privacy accounting could shift relative rankings. The claim that DP-BiTFiT "matches the state-of-the-art accuracy" would be substantially strengthened by a head-to-head re-implementation of all baselines in a single codebase. This does not invalidate the paper's core claims but weakens the primary accuracy assertion.

2. **The long-sequence / high-resolution use case is claimed but not demonstrated with actual fine-tuning.** The paper repeatedly motivates DP-BiTFiT's advantage on document-level texts (\(T\approx 20000\)) and high-resolution images (1024×1024), and states in the abstract that it "enables us to conduct DP fine-tuning on language and vision tasks with long-sequence texts and high-resolution images." However, the scaling plots only go up to \(T\approx 1000\) (text) and \(\sqrt{T}\approx 512\) (images), and no downstream accuracy task is conducted at these extreme scales. The paper says "We expect to observe greater efficiency advantage" — this is speculation, not evidence. A single experiment on a long-document benchmark (e.g., a subset of Long-Range Arena or IMDB full reviews) or a high-resolution vision dataset (e.g., CelebA-HQ 1024×1024) would directly support this central claim.

### Minor

3. **DP-BiTFiT-Add is only evaluated on ResNet18.** The add-bias variant for bias-free architectures (e.g., LLAMA, convolutional layers with BatchNorm) is tested only on ResNet18 for CelebA. The paper mentions LLAMA2-7B parameter counts but provides no accuracy results on any large language model or other bias-free architecture. The claim that this variant is broadly applicable remains unsubstantiated beyond a single small-scale experiment.

4. **No analysis of why DP-BiTFiT outperforms DP full fine-tuning on GPT2-large BLEU (and on ViT-large CIFAR100).** The paper observes this interesting reversal (smaller models show a gap in favor of full fine-tuning, larger models show BiTFiT ahead) but offers no mechanistic explanation. Possible reasons (e.g., reduced overfitting under DP due to the low data/parameter ratio, lower variance of bias gradients after clipping, optimization benefits) are not discussed. An ablation or analysis would deepen understanding.

5. **The vision results on CelebA with ResNet18 show a 1.5% accuracy gap** (DP-BiTFiT 86.87% vs. DP full 88.38% for multi-label) that is not discussed in relation to the scaling pattern (Remark 1). Since ResNet18 is a smaller model, this is consistent with the identified pattern, but the paper does not make this connection explicitly or discuss whether this gap is expected to shrink on larger vision models.

### Trivial

6. **"Book-Keeping(full)" column in Table 2 is never defined.** This term appears only in the table header with no explanation in the main text or caption.

7. **The 2–30× speedup and 2–8× memory reduction ranges in the abstract are very wide**, spanning nearly two orders of magnitude for speedup. While the paper correctly specifies "compared to DP full fine-tuning," the concrete experiments show more modest gains (e.g., 1.2–2× throughput improvements in practice), making the upper bound appear to come from an optimistic extrapolation.

## Nice-to-Haves
- A controlled re-evaluation of DP full fine-tuning and DP LoRA/Adapter under the same codebase, privacy accountant, and hyperparameter search for at least 2–3 tasks (e.g., SST2, QQP, CIFAR10) with standard errors.
- A study of sensitivity to clipping threshold \(R\) for bias vs. weight gradients, since bias gradients likely have different norm distributions.
- Per-layer gradient norm visualizations comparing bias vs. weight gradients under DP to build intuition for why bias-only training works well.
- A small-scale experiment combining BiTFiT with LoRA (as mentioned in the Discussion section).

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Abstract "2–30× faster, 2–8× less memory" without baseline**: The abstract clearly states "than DP full fine-tuning" — the reviewer missed this.
- **Novelty paragraph should cite codebase versions**: A minor presentation nitpick about citation formatting; not a substantive weakness.
- **Section 2 omits bias gradients for conv/norm layers**: The paper explicitly states this is deferred to the appendix — standard practice.
- **QQP example is "anecdotal"**: It is clearly presented as a concrete example/illustration, not a systematic study.
- **1.5× speedup claim conflates complexity with runtime**: The paper says "complexity analysis indicates" — this is correctly framed as a theoretical complexity claim, with empirical results reported separately.
- **Table 1 standard columns mix sources**: Source attribution is clear from column headers and surrounding text.
- **"Applied on top of last-layer training" is ambiguous**: The paper explicitly states which parameters are trained (biases + last-layer weights) and provides parameter counts.
- **Discussion paragraph is speculative**: This is standard future-work language; no experiments are promised.
- **Section 2 "omits" conv/norm bias gradient derivation**: Paper explicitly says derivation is in the appendix.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a controlled re-evaluation of baselines.** For at least 2–3 tasks, re-run DP full fine-tuning and DP LoRA with the exact same training pipeline, privacy accountant, and hyperparameter search budget as DP-BiTFiT. Report with standard errors. This single change would substantially strengthen the accuracy claims.

2. **Either add a long-sequence or high-resolution fine-tuning experiment, or temper the corresponding claims.** A single experiment on a benchmark with \(T > 2000\) (e.g., IMDB full reviews or a Long-Range Arena subset) or resolution > 512×512 (CelebA-HQ 1024×1024) would convert a speculative claim into a demonstrated one.

3. **Discuss the GPT2-large/ViT-large outperformance observation.** Provide a brief mechanistic hypothesis (e.g., reduced overfitting, lower gradient variance) to help readers understand when bias-only training is beneficial.

4. **Define "Book-Keeping" in Table 2's caption or the surrounding text.**

5. **Tighten the efficiency claim ranges** in the abstract to reflect the empirically observed range more accurately.

## Score and Decision

The paper makes a solid, well-motivated contribution. Its core contribution — the recognition and rigorous analysis that bias-gradient DP overhead is independent of feature dimension — is correctly identified and convincingly demonstrated. The efficiency gains are substantial and empirically validated across multiple architectures. Accuracy is competitive. The weaknesses are genuine but fixable: the baseline comparison relies on numbers from prior work rather than controlled re-evaluation, and the long-sequence/high-resolution capability is claimed but not experimentally demonstrated. Neither issue invalidates the core contribution but both prevent the paper from being definitive.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>