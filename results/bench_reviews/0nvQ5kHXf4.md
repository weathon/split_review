Now I have enough context. Let me write the consolidated review.

## Summary

WASI (Weight-Activation Subspace Iteration) proposes a unified framework that jointly compresses both model weights and activation maps into stable low-rank subspaces during transformer fine-tuning. By reusing SVD-computed subspaces across iterations via subspace iteration (avoiding expensive recomputation), and by coupling weight subspace iteration (WSI) with activation subspace iteration (ASI), WASI achieves up to 62× memory reduction, ~2× FLOP reduction, and ~1.4× wall-clock speedup on a Raspberry Pi 5 while maintaining accuracy close to vanilla training. The paper evaluates on ViT, SwinT, and TinyLlama across multiple vision and language tasks, and includes real on-device timing on three edge devices.

## Strengths

- **Joint compression of weights and activations in a single training framework.** Unlike prior work that compresses either weights (SVD-LLM) or activations (AMC, ASI) separately, WASI handles both simultaneously, addressing the two dominant memory bottlenecks in backpropagation. The forward/backward pass derivations in the low-rank space (Eq. 8–11, Appendix A.1) are clearly laid out and reproducible.

- **Real on-device validation across multiple edge devices.** WASI is evaluated on Raspberry Pi 5, Jetson Orin, and Jetson Nano (Table 3, Fig. 8), with consistent speedups over vanilla training. The inclusion of energy measurements on Jetson Orin (Table 4, ~33–34% energy reduction) strengthens the practical deployability claim beyond what most related work provides.

- **Extensive empirical scope.** Experiments span three model families (ViT, SwinT, TinyLlama), five vision datasets (CIFAR-10/100, CUB, Flowers, Pets), and BoolQ for LLM fine-tuning. The SwinT experiments (Fig. 6) are particularly valuable because 4D activation maps are explicitly addressed (Appendix A.4), a limitation of SVD-LLM that WASI overcomes.

- **Principled control of accuracy-efficiency trade-off via explained variance.** The ε threshold provides interpretable control over the compression-accuracy trade-off, and the dynamic-programming rank selection (Appendix A.2) replaces the exponential search of prior work with a linear-time procedure.

## Weaknesses

### Major

1. **The core assumption — subspace stability — is only indirectly validated.** The paper claims that "the intrinsic subspace remains relatively stable after each training iteration" (Section 3.3). The direct evidence provided is **rank stability** (Fig. 3a: singular values remain stable across epochs for one layer `W_6` on Pets). Rank stability does not imply subspace (basis vector) stability — the left/right singular subspaces `L_i`, `R_i` could rotate while maintaining the same singular values. The WSI vs. full SVD comparison (Fig. 3b) is a joint test of both the stability assumption and the subspace-iteration approximation, conflating the two. A direct measure (e.g., principal angles between subspaces at consecutive iterations) is needed to cleanly validate the premise. While WSI empirically works (Fig. 3b), the paper's rhetorical framing relies on this assumption being true, and the evidence for it is weaker than claimed.

2. **Main accuracy-efficiency results lack multi-seed statistics.** The core comparison plots (Figs. 5, 6, Table 1) report single runs. Accuracy differences between WASI at ε=0.9 and vanilla training are often small (e.g., 96.24% vs. 97.32% in Table 1). Appendix B.2 provides multi-seed results for ViT on Pets and reports minimal variance, but this covers only one dataset-model combination. Without error bars on the main figures, it is unclear whether the observed small accuracy gaps are systematic or within noise. Given that the paper's central claim is that WASI "maintains accuracy comparable to vanilla training," this weakens the evidence.

### Minor

3. **LoRA is not included as a direct standalone baseline.** The paper compares against SVD-LLM (which uses LoRA-style adapters with rank=8) but not against standard LoRA fine-tuning. While the paper explains in Section 2 why LoRA differs in scope (does not reduce inference cost, adds memory during training from co-existing frozen weights and adapters), a direct comparison would help position WASI's advantages over the most widely-used parameter-efficient method. This is not fatal — the paper's related work discussion is clear about the differences — but it would strengthen the empirical positioning.

4. **The FLOP/speedup analysis in Fig. 2 assumes uniform ranks across layers.** Section 3.4 acknowledges this simplification ("For simplicity, we assume that the same optimal rank is applied"). Since actual ranks vary per layer and per mode, the figures are illustrative rather than empirical. The authors should clarify this in the caption.

5. **The on-device speedup (1.4×) is modest relative to the FLOP reduction (up to 2×).** The paper attributes this to overhead from subspace iteration itself but does not provide a runtime breakdown showing where the gap comes from. A decomposition of training time (WSI, ASI, forward pass, backward pass) for WASI vs. vanilla on the Raspberry Pi 5 experiment would clarify the practical efficiency picture.

### Trivial

6. Some figures (e.g., Fig. 1, Fig. 8) appear duplicated in the paper (parser artifact). The content is present; this does not affect evaluation.

## Nice-to-Haves

- A direct subspace similarity metric (principal angles or Frobenius norm difference of basis vectors across consecutive iterations) would cleanly validate the core assumption.
- Extending the TinyLlama experiment to more layers and a higher ε value would strengthen the generality claim for LLMs.
- Reporting multi-seed variability for at least the main CIFAR-10 ViT results would address the confidence concern definitively.

## Removed Points

The following points from the reviewer inputs are removed with justification:

- **"The first method for efficient model-activation-decomposition-aware training is overstated"** — The paper carefully frames this as a specific technical contribution (joint activation+weight decomposition during training), not a sweeping novelty claim. The phrasing is acceptable.
- **"SVD-LLM hyperparameters may not be optimal for vision tasks"** — The paper follows the SVD-LLM paper's own settings. This is standard practice. A sweep would be nice but not required.
- **"Missing appendix content / proofs"** — The appendix exists in the original submission; parser stripping is not the authors' fault.
- **Formatting nitpicks and typo claims** — Parser artifacts, not author errors.
- **Claims about "not yet released" code or models** — The paper cites a GitHub repository and commits to open-sourcing; questioning availability violates the hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself misses about its own work. The main insight the reviewers add is that the subspace stability assumption could be validated more directly — this is a methodological suggestion, not a novel observation about the paper's findings.

## Suggestions

1. Add a direct subspace stability measure (principal angles between `R_i^{(t-1)}` and `R_i^{(t)}` across epochs for multiple layers) to Section 4.2 to directly validate the core assumption.
2. Report mean and standard deviation over 3 seeds for the main accuracy-efficiency figures (at least Table 1 and the CIFAR-10 / Pets results).
3. Include a runtime breakdown table (time spent on WSI, ASI, forward pass, backward pass) for the Raspberry Pi 5 experiment.
4. Clarify in the Fig. 2 caption that the uniform-rank assumption is for illustration.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `f3KD7jfSWY.md` (CERSA) | 4.50 (Reject) | Similar subspace/SVD-based PEFT approach; WASI has stronger on-device evaluation, joint weight+activation compression, but shares similar subspace-stability assumption concerns. WASI is stronger. |
| `QD4DL0OUmZ.md` (LoRAct) | 4.00 (Reject) | Activation compression only; WASI is more comprehensive (weights + activations, training + inference, on-device timing) and better validated. WASI is stronger. |
| `bR32fsXLbf.md` (DASP) | 3.00 (Reject) | Subspace-based fine-tuning with methodological issues and missing baselines; WASI's experiments are more thorough and its claims more measured. WASI is stronger. |
| `xEcUIn81Fp.md` (Subspace paper) | 4.00 (Reject) | Empirical study of subspace properties; limited practical contribution. WASI has concrete deployment value. WASI is stronger. |
| `TkHjRwbMNl.md` (Trion) | 5.60 (Accept Poster) | Efficient low-rank optimization with DCT-based projection; similar tier of contribution — practical method with some methodological open questions but clear empirical value. WASI is comparable. |
| `VVruwk9404.md` (CR-Net) | 6.50 (Accept Poster) | Low-rank pre-training with very strong large-scale experiments; scale of validation exceeds WASI. WASI is weaker. |
| `vBJKZ19XGY.md` (MLRA) | 6.00 (Accept Poster) | Strong architectural contribution with clear speedup and validation; WASI's contribution is comparable in practical value but less clean in novelty story. WASI is slightly weaker. |

The paper sits above the rejected subspace/PEFT papers (3.0–4.5) due to its stronger empirical validation and practical on-device experiments. It is comparable to accepted methods in the 5.5–6.0 range like Trion, but slightly weaker than CR-Net or MLRA because: (a) the core subspace stability assumption is not rigorously validated, (b) the main results lack confidence intervals, and (c) the LLM validation is limited. These are addressable weaknesses that do not invalidate the paper's contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>