Now I have a clear picture of the calibration. Let me compose the final review.

**Round 1 bracket:** Between 4.5 (stronger than SubZero/SubTrack-Grad) and 7.0 (weaker than AdaRankGrad). The narrowest plausible range is 5.0–6.5.

**Round 2 narrowing:** The paper is stronger than SubTrack-Grad (4.75) and TinyTrain (5.25) — it has more novel methodology and a cleaner contribution. But it is weaker than Adapprox (6.40) and AdaRankGrad (7.00), which have more thorough experiments, theoretical grounding, and fewer evaluation gaps. WASI sits between LoRAM (6.20, accept) and TinyTrain (5.25, reject). I place it at **5.5** — a borderline paper with real contributions but evaluation gaps that need addressing.

Now let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None

### Major
...

### Minor
...

### Trivial
...

## Nice-to-Haves
...

## Removed Points
...keep details

## Novel Insights
...

## Suggestions
...

## Score and Decision## Summary

This paper proposes WASI (Weight-Activation Subspace Iteration), a method that jointly compresses both weight matrices and activation maps into low-rank subspaces during fine-tuning, leveraging the observation that these subspaces remain stable across training iterations. The key idea is to use subspace iteration (rather than costly repeated SVD) to maintain the low-rank decomposition of weights (WSI) combined with activation compression (ASI), enabling transformer fine-tuning with up to 62× memory reduction and measured speedup on a Raspberry Pi 5.

## Strengths

1. **Novel joint weight–activation subspace iteration for transformers.** WASI is the first method to simultaneously apply subspace iteration to both weights and activations in a unified low-rank training framework. The stability assumption (Section 3.3) is empirically verified in Figure 3a, showing layer ranks remaining nearly constant across 40 epochs. This goes beyond prior work (ASI compresses only activations; SVD-LLM addresses only weights) and is a genuine algorithmic contribution.

2. **Impressive memory savings with real hardware validation.** On SwinT (Section 4.3, Figure 6), WASI achieves up to 62× training memory reduction and 1.5× FLOPs reduction while matching vanilla accuracy at ε=0.9. Critically, the paper includes an on-device latency experiment on a Raspberry Pi 5 (Figure 8), where WASI achieves roughly 1.4× wall-clock speedup over vanilla training — direct evidence of real-world applicability, which is rare in this literature.

3. **Reasonable breadth across architectures and tasks.** WASI is evaluated on ViT, SwinT, and TinyLlama (decoder-only) across five image classification datasets (CIFAR-10/100, CUB, Flowers, Pets) plus BoolQ for language. This shows the method generalizes beyond the vision transformers it was primarily designed for.

4. **Theoretical efficiency analysis.** Section 3.4 and Figure 2 derive closed-form expressions for compression rates and speedup ratios as functions of rank, demonstrating that WASI's gains grow with model size — a desirable property for over-parameterized models in on-device learning.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by direct experimental evidence, and no criticism in the reviews invalidates the main results when verified against the paper.

### Minor

1. **No ablation isolating weight compression (WSI) from activation compression.** The paper compares WASI vs. ASI (activation-only), revealing the value of adding weight compression to activation compression. However, there is no WSI-only baseline. Without this, it is unclear how much of the benefit comes from the novel weight-side compression vs. the already-known activation compression (ASI), and whether the interaction between the two is synergistic or additive. This is an easily fixable gap that would strengthen the paper's scientific rigor.

2. **No variance reporting or statistical significance.** All experimental results are reported as single runs without error bars or multiple seeds. Fine-tuning with low-rank approximations involves randomness from subspace initialization and iteration dynamics, so reporting variance is important for assessing robustness — especially when accuracy differences between WASI and vanilla are sometimes small (e.g., TinyLlama, Figure 7).

3. **Headline memory reduction claim (62×) lacks scope qualification in abstract and conclusion.** The paper explicitly states in Section 4.1 that memory is measured "focusing on linear layers within multi-perceptron blocks for fair comparison with previous methods." Yet the abstract and conclusion state "reducing memory usage by up to 62×" without this caveat. For a practitioner evaluating on-device feasibility, the total memory footprint (including embeddings, attention projections, layer norms, optimizer states) is what matters. The abstract should clearly communicate the measurement scope.

4. **TinyLlama experiment is too limited to convincingly demonstrate generality to language models.** Only the last 5 layers are fine-tuned at a single aggressive compression level (ε=0.1), achieving accuracies around 64–66% on BoolQ. This setting is far from how LLMs are typically fine-tuned, and the absolute accuracy is well below SOTA. While the *relative* comparison to vanilla is valid, a more extensive study (more layers, higher ε values, larger datasets) would substantially strengthen the generality claim.

5. **Stability of weight subspaces verified only on one layer of one model.** Figure 3a validates the rank-stability assumption only for layer W6 of ViT on the Pets dataset. While the paper's premise depends on this stability holding broadly, no evidence is provided for other layers, other models (SwinT, TinyLlama), or other datasets. The stability analysis should be extended to at least a representative set of layers across models.

6. **WSI vs. SVD comparison (Figure 3b) needs clearer interpretation.** The claim "WSI achieves 35% higher accuracy at same FLOPs" is because, at a given FLOP budget, the full SVD baseline operates at a lower effective rank (same FLOPs but lower rank → lower accuracy). This is not a flaw, but the comparison would benefit from an explicit explanation that the x-axis (FLOPs) conflates different rank strategies.

### Trivial
None.

## Nice-to-Haves

- **Comparison of training memory with LoRA or other PEFT methods.** The paper discusses LoRA's drawbacks qualitatively (Section 2) but does not provide a quantitative memory comparison. A simple bar chart showing peak memory of WASI vs. LoRA vs. vanilla would help practitioners situate the method.
- **Analysis of the overhead of subspace iteration and rank selection.** The subspace iteration (Algorithm 1) and the DP-based rank selection (Appendix A.2) have non-trivial costs that are not separately measured from the overall training time.
- **On-device latency for more than one model.** Only ViT on CIFAR-10 is tested on the Raspberry Pi 5. Testing SwinT or TinyLlama on-device would strengthen the deployment claim.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:
1. **Missing on-device learning baselines (subnetwork training, dynamic subnetworks).** The paper explicitly scopes to *low-rank decomposition* methods (Section 2: "compact model design, quantization, sparsification, and knowledge distillation also fall outside the scope of this work—low-rank decomposition"). Subnetwork training methods are a different paradigm. Criticizing their absence is scope creep.
2. **SVD-LLM adaptation not described.** The paper points to Appendix A.4 for this detail, which was stripped by the PDF parser. The parser-removed appendix cannot be held against the paper.
3. **"First method" phrasing is overwrought.** A style/stylistic nitpick that does not affect scientific merit.
4. **Notation concerns in Algorithm 1.** The dimensions check out when traced through (the reviewer acknowledged "it is not a fatal error"). The derivation is self-consistent.
5. **No comparison to LoRA in training memory.** Raised elsewhere and moved to Nice-to-Haves; not a core weakness.
6. **The claim "underlying principles apply broadly to any neural network" is unsupported.** This is a standard forward-looking statement common in conclusion sections, not a central claim.

## Novel Insights

None beyond the paper's own contributions. The reviews surface some gaps in the evaluation (missing ablation, missing error bars, ambiguous scope of the headline memory number) but do not identify novel connections or reinterpretations of the method that the authors themselves missed.

## Suggestions

1. **Add a WSI-only ablation** to all main experiments (Figures 5 and 6). This would directly isolate the contribution of the weight-side compression and demonstrate whether the combination is indeed better than either component alone.
2. **Run all main experiments with at least 3 random seeds** and report mean ± std. This is essential for assessing robustness, especially given the small accuracy deltas in some settings.
3. **Clarify the scope of the 62× memory claim** in the abstract and conclusion. Add a sentence such as "measured on MLP linear layers, which dominate training memory in transformer models" to avoid misleading readers.
4. **Extend the stability analysis** (Figure 3a) to at least 3–4 layers spanning different depths and across 2 models (e.g., ViT and SwinT) to validate the core assumption more broadly.
5. **Provide a more convincing LLM experiment** by fine-tuning more layers of TinyLlama at multiple ε values, or by using a standard PEFT benchmark setup.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review/.../igGeaxOiFM.md (HoLoRA) | 3.00 | 1 | Much weaker — purely incremental LoRA variant with no on-device experiments |
| /home/wg25r/split_review/.../04RLVxDvig.md (NanoMoE) | 3.00 | 1 | Much weaker — limited experimental validation |
| /home/wg25r/split_review/.../ZTvUT49JjL.md (Implicit Bias in MF) | 3.40 | 1 | Much weaker — theoretical analysis with limited practical validation |
| /home/wg25r/split_review/.../49ti6LOUw5.md (UnoLoRA) | 3.00 | 1 | Much weaker — incremental multi-task LoRA |
| /home/wg25r/split_review/.../LvNROciCne.md (AdaRankGrad) | 7.00 | 1,2 | Stronger — has theoretical proofs, more comprehensive experiments, multiple seeds |
| /home/wg25r/split_review/.../s7DkcgpRxL.md (LoRAM) | 6.20 | 1 | Stronger in scale (70B models) but weaker in novelty (pruning+LoRA). WASI has more novel methodology but narrower scope |
| /home/wg25r/split_review/.../FK6T0U4Mg1.md (SubZero) | 4.25 | 1 | Weaker — limited novelty (combination of existing ideas), narrower experiments, no hardware validation |
| /home/wg25r/split_review/.../cgCKm5DOnu.md (ROSA) | 6.00 | 1 | Comparably strong — clean method with thorough experiments. WASI has weaker evaluation rigor (no error bars, no ablation) |
| /home/wg25r/split_review/.../TwJrTz9cRS.md (HiRA) | 8.00 | 1 | Much stronger — comprehensive with strong results across many tasks |
| /home/wg25r/split_review/.../Tzh6xAJSll.md (Scaling Laws) | 7.60 | 1 | Much stronger — rigorous theoretical and empirical contribution |
| /home/wg25r/split_review/.../d8w0pmvXbZ.md (Stability Proxies) | 8.00 | 1 | Much stronger — well-designed study with clear practical value |
| /home/wg25r/split_review/.../E4Fk3YuG56.md (Cut Cross-Entropy) | 8.50 | 1 | Much stronger — impactful engineering contribution with thorough baselines |
| /home/wg25r/split_review/.../KxGGZag9gW.md (EigenLoRA) | 5.00 | 2 | Slightly weaker — less thorough evaluation, narrower scope |
| /home/wg25r/split_review/.../nR0n4R1Ck2.md (SubTrack-Grad) | 4.75 | 2 | Weaker — missing memory reporting, unclear advantages over GaLore |
| /home/wg25r/split_review/.../xNdE7RiRyP.md (TinyTrain) | 5.25 | 2 | Similar — both have on-device experiments and evaluation gaps. WASI has stronger novelty but less comprehensive edge analysis |
| /home/wg25r/split_review/.../mzkpLkd1S8.md (Nullspace ViT) | 5.25 | 2 | Similar score range but different topic — robustness augmentation, not comparable |
| /home/wg25r/split_review/.../5btFIv2PNb.md (LoR-VP) | 6.33 | 2 | Stronger — cleaner evaluation, more architectures tested |
| /home/wg25r/split_review/.../cWGCkd7mCp.md (Sine-Activated LR) | 7.00 | 2 | Stronger — theoretical contribution with thorough empirical validation |
| /home/wg25r/split_review/.../RtzxJLPxGk.md (Adapprox) | 6.40 | 2 | Stronger — more thorough experiments, better coverage of practical tradeoffs |

**Round 1 bracket:** [4.5, 7.0] based on comparison to anchors scoring 3.0–3.4 (weaker) and 7.0–8.5 (stronger). The paper is clearly stronger than papers scoring in the 3s but has evaluation gaps that prevent it from reaching the 7+ level.

**Round 2 narrowing:** Compared against 5–6.4 range anchors, WASI sits above SubTrack-Grad (4.75) and TinyTrain (5.25) due to stronger novelty and an on-device experiment. It is below Adapprox (6.40) and LoR-VP (6.33), which have more thorough experiments. Comparable to LoRAM (6.20) in overall contribution quality but WASI's evaluation is less rigorous (no error bars, no ablation, limited LLM experiment).

**Final score determination:** 5.5 — The paper proposes a genuinely novel combination of techniques (joint weight-activation subspace iteration) with promising empirical results including rare on-device hardware validation. However, several evaluation gaps (no WSI-only ablation, no error bars, ambiguous scope of headline memory number, limited TinyLlama experiment, single-layer stability validation) prevent the evidence from being fully convincing. These are all addressable with revisions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>