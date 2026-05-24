Now I have all the evidence. Let me produce the final consolidated review.

## Summary

This paper proposes WASI (Weight-Activation Subspace Iteration), a method that jointly compresses both weight matrices and activation maps of transformers into low-rank subspaces during fine-tuning. The key idea is that the parameter subspace is stable across training iterations, enabling cheap subspace iteration rather than repeated SVD. Experiments on ViT, SwinT, and TinyLlama show memory reductions up to 62× and FLOPs reductions up to 2×, with ≈1.4× speedup on a Raspberry Pi 5.

## Strengths

1. **Joint compression of weights and activations is novel and well-motivated.** The paper correctly identifies that prior work (ASI, SVD-LLM) compresses only one of weights or activations, while WASI addresses both simultaneously. The unified framework with a controlled information-loss threshold (ε) is a principled design that gives practitioners a tunable accuracy-efficiency knob.

2. **Strong empirical evidence across multiple architectures and datasets.** Results span ViT (CIFAR-10), SwinT (five datasets), and TinyLlama (BoolQ), showing WASI consistently matches or exceeds vanilla accuracy while cutting memory by up to 62× (SwinT) and 953× activation memory / 30× weight memory (TinyLlama). The evaluation breadth supports the claim that the method is not tied to a single architecture.

3. **Real-world on-device validation is a genuine strength.** The Raspberry Pi 5 experiment (Sec. 4.4, Fig. 8) demonstrates that WASI achieves ≈1.4× faster training and inference per iteration than vanilla training at ε=0.9 (where accuracy matches vanilla). This is direct evidence of practical usefulness on exactly the kind of hardware the method targets — rare in the subspace/low-rank literature.

4. **WSI is shown to be more efficient than repeated full SVD.** Figure 3b validates that subspace iteration (WSI) requires 1.36× fewer FLOPs than recomputing SVD at every iteration for the same accuracy, and outperforms SVD at equal FLOPs by ≈35% in accuracy. This directly supports the practical benefit of the subspace reuse hypothesis.

## Weaknesses

### Major

1. **The central hypothesis of weight subspace stability is insufficiently validated.** The paper claims that "the intrinsic subspace remains relatively stable" during fine-tuning (Sec. 3.3), but the only direct evidence is Fig. 3a, which shows that singular *values* (and thus the *rank* K_i) remain stable across epochs. Rank stability does **not** imply that the subspace itself (the span of the singular vectors) is stationary — the singular vectors could rotate substantially while the rank stays fixed. A rotating subspace would cause the subspace iteration (Algorithm 1) to diverge from the true subspace over time. The paper does not measure principal angles, cosine similarity between subspaces, or the per-iteration approximation error of the subspace-iterate against the true weight matrix. This is a gap in the methodological foundation. (Sec. 3.3, Sec. 4.2, Fig. 3a)

2. **The gap between theoretical FLOPs reduction and practical speedup is not analyzed.** The paper claims up to 2× FLOPs reduction, yet the Raspberry Pi 5 speedup is only ≈1.4× — and that is at ε=0.9 (the *least* aggressive compression). For more aggressive compressions (ε=0.4–0.7), the speedup is larger but the accuracy gap is also larger. The paper does not discuss the causes of this gap (overhead of subspace iteration/decomposition, memory access patterns, inability to exploit low-rank structure on CPU), making the theoretical FLOPs numbers somewhat disconnected from practical benefit. This directly affects the credibility of the deployment claim. (Sec. 3.4, Sec. 4.4)

### Minor

3. **Limited generality claim with thin evidence on language models.** The TinyLlama experiment (Sec. 4.3) is informative but limited: only the last 5 layers are fine-tuned, ε=0.1 is extremely aggressive and not swept, and memory/FLOPs savings are reported only for the fine-tuned layers (not the full model). The accuracy difference (<0.5%) is within likely noise, making the "no accuracy loss" claim optimistic. A sweep over ε with more layers unfrozen would provide stronger evidence of generality.

4. **The dynamic programming improvement for activation rank selection lacks ablation.** The paper claims to improve ASI with a DP strategy that reduces search cost from exponential to linear (Sec. 3.3), but no experiment compares this against the original ASI's brute-force or grid-search approach. Without this comparison, the value of the claimed improvement is unsubstantiated.

5. **Accuracy numbers are reported without error bars or confidence intervals.** Given that differences between methods can be small (e.g., <1%), multiple runs with statistical significance reporting would strengthen the paper's claims, particularly for the TinyLlama experiment where the accuracy difference is marginal.

6. **The conclusion overreaches when claiming WASI's principles "apply broadly to any neural network trained with backpropagation."** The method explicitly assumes linear layers with low-rank weight matrices and stable subspaces — properties validated only for transformers. This claim should be qualified.

### Trivial

7. Notation for compressed gradients (Eq. 8–11) is only defined in the appendix, not the main text. A brief explanation in the main body would improve readability.
8. The description of ASI (Nguyen et al., 2025) in Sec. 2 as using "a perplexity-based heuristic" should be clarified against the original ASI's rank selection approach to avoid mischaracterization.

## Nice-to-Haves

- **A LoRA baseline comparison** would clarify WASI's positioning. While the paper reasonably scopes out LoRA because it does not compress the architecture or reduce inference cost, a comparison would highlight WASI's advantages (inference efficiency, joint compression) vs. LoRA's strengths (simplicity, wide adoption). This is not a required comparison but would strengthen the paper.
- **Direct measurement of subspace similarity** (principal angles between singular vector subspaces across iterations) would definitively validate the weight subspace stability claim.
- **A combined baseline** (naïve SVD weight compression + fixed-rank activation compression, without subspace iteration) would isolate the benefit of subspace iteration over a straightforward combination.

## Removed Points

These points from the inputs were removed for the following reasons:

- **"Insufficient validation of central hypothesis" as described by the critic →** This point is retained above as Major weakness #1, but reformulated to accurately reflect what the paper does and does not show. The critic's framing ("fatal" / "methodological gap that could be fixed") was too severe — the paper's empirical results (Fig. 3b) show WSI works well despite the validation gap, and prior work on subspace stability is cited.
- **"Incomplete baseline comparison (LoRA, subnetwork methods)" →** The paper explicitly scopes comparisons to methods that also compress the architecture (Sec. 4.1: "directly comparable baselines"). LoRA does not compress the architecture or reduce inference cost — it is a different category of method. Subnetwork methods (Lin et al., Quelennec et al.) are designed for CNNs, not transformers. The critic's demand is scope creep. The LoRA comparison is moved to Nice-to-Haves.
- **"Unclear adaptation of SVD-LLM" →** The paper points to Appendix A.4 for details on how SVD-LLM was adapted to vision transformers. Per the review rules, weaknesses about missing appendix content are removed (the parser strips appendices; they exist in the original submission).
- **"The statement 'ASI requires access to a downstream dataset' is confusing" →** The paper says "ESPACE... requires access to a downstream dataset" (line 31), not ASI. The critic misread the text. This is factually wrong and removed.
- **"Fig. 3b 35% improvement seems implausible" →** The claim compares WSI vs. full SVD at *equal FLOPs* — the subspace iteration spends its FLOP budget on training iterations rather than SVD recomputation, so the comparison is sensible. The implausibility claim reflects a misunderstanding of the comparison setup.
- **"Related Work: ASI mischaracterization" →** The paper's description of ASI's rank selection approach is a characterization that may or may not be accurate; without direct access to the ASI paper, I cannot verify this. The point is moved to Trivial (#8) as a clarification request.
- **Pure style/formatting nitpicks** about figure labels and variable definitions → Removed as formatting artifacts.
- **"Code reproducibility: license/snapshot" →** Per the rules, nitpicks about reproducibility for large artifacts are removed.

## Novel Insights

None beyond the paper's own contributions. The two input reviews largely reinforce each other: the harsh critic identifies genuine gaps (subspace stability evidence, speedup gap analysis) and the strength finder correctly identifies the paper's genuine contributions (joint compression, on-device validation). The main novel observation from combining the two is that the paper's core weakness is *not* that its method fails, but that its theoretical foundation (subspace stability for weights) is asserted from evidence that only shows rank stability — yet the method empirically works. This suggests the method may be more robust than the theoretical justification admits, which is an interesting position for future work.

## Suggestions

1. **Directly measure weight subspace stability** by computing principal angles between singular vector subspaces at successive iterations for a few representative layers. Show that the angle remains small (e.g., <5°). This single experiment would resolve the most serious weakness.
2. **Add an analysis of the FLOPs-to-speedup gap** on Raspberry Pi 5: profile where time is spent (subspace iteration overhead, memory bandwidth, matrix multiplication), and discuss why the 2× FLOPs reduction yields only 1.4× speedup.
3. **Add error bars** (at least 3 runs) for key experiments, particularly where accuracy differences are small.
4. **Sweep ε on the TinyLlama experiment** (e.g., 0.1, 0.3, 0.5) and report overall model savings, not just savings for tuned layers.
5. **Ablate the dynamic programming rank selection** against the original ASI brute-force approach on at least one dataset.
6. **Tone down the overreach** in the conclusion: qualify "any neural network trained with backpropagation" to "transformer-based models and similarly structured architectures with linear layers."

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "subspace iteration low-rank training transformer fine-tuning on-device memory reduction" with score cutoffs.

- *Weak band (score < 3.5):* DASP (3.00), PESO (3.00), GALE (3.33) — all rejected, primarily for insufficient novelty or validation gaps.
- *Middle band (3.5–7.5):* CERSA (4.50), LoRAct (4.00), nlgQsugmGw (4.00), vQcyqsGJDw (5.00). CERSA is the closest topical anchor (SVD-based subspace PEFT with similar subspace stability concern) and scored 4.50/reject.
- *Strong band (> 7.5):* Polar Express (8.00), Transducing LMs (8.00) — completely different topics, not useful anchors.

**Round 1 bracket: [4.0, 5.5]** — The paper is clearly stronger than papers scoring ≤3.33 (GALE, PESO) due to its on-device validation and broader evaluation, but has methodological gaps that place it below papers scoring ≥5.5 (WSVD at 5.50, which was accepted).

**Round 2 (Narrowing):** Two queries targeting the [4.0, 6.0] range for topically similar papers.

- BALF (5.33, Reject) — activation-aware factorization, fine-tuning-free compression. Thorough method but missing large-scale validation.
- LANCE (4.50, Reject) — on-device activation compression via one-shot HOSVD. Shares subspace stability concerns with WASI. LANCE lacks on-device deployment results; WASI has them.
- ALS-ActLR (5.00, Reject) — activation-aware low-rank compression.
- TuzsCiHocG (5.00, Reject) — SVD-based LLM compression with rank allocation.

Comparing against these anchors: WASI is stronger than LANCE (4.50) because it has actual on-device results and covers weight+activation compression, not just activations. WASI is comparable to CERSA (4.50) — both have subspace stability gaps, but WASI's scope (joint weight+activation, on-device deployment) is broader. WASI sits slightly below BALF (5.33) because BALF has more rigorous theoretical backing, though they address different problems.

**Final score: 5.0** — This reflects the paper's genuine contributions and on-device validation while acknowledging the methodological gap in subspace stability validation and the missing analysis of the speedup gap. The paper is not fatally flawed but needs strengthening in these areas before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>