- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
## Summary

This paper presents Ditto, a framework that enables quantization-aware secure inference of Transformer models using multi-party computation (MPC). The key contributions are: (1) incorporating MPC-friendly static dyadic quantization (with dyadic scaling factors that map to cheap bit-shifts) and quantization-aware distillation to retain model utility, and (2) novel MPC primitives (UpCast/DownCast) that perform the type conversions between different fixed-point representations and rings, which are essential for mixed-precision quantized computation. The framework builds on SPU with dynamic ring support and automatic type-insertion in the computation DAG. Experiments on BERT and GPT2 models show 1.4–4.4× speedups over MPCFormer and PUMA with generally small utility degradation on GLUE tasks, though GPT2 perplexity shows non-trivial increase.

---

## Strengths

- **Novel type-conversion MPC primitives (Algorithm 1)**: The UpCast protocol converts shares between different rings (e.g., ℓ=32 to ℓ=64) with 3ℓ+ℓ′ bits communicated in 3 rounds, while DownCast is purely local (right-shift + modulo). These primitives directly enable mixed-precision quantized secure inference, which prior MPC frameworks could not support. The communication complexity is clearly stated and verified against the protocol steps.

- **Quantifiable end-to-end speedups over state-of-the-art**: Figure 4 and Table 3 show that Ditto achieves 3.14–4.40× speedup over MPCFormer (Quad) and 1.44–2.35× over PUMA across BERT and GPT2 variants. The communication-vs-runtime scatter plots consistently show Ditto in the bottom-left corner. Speedup factors are reported against multiple baselines and across varying input lengths.

- **Clean ablation isolating component contributions**: Table 4 separates the effect of quantization alone (1.41–1.56× speedup over vanilla) from quantization + GeLU approximation (1.74–2.09×), providing direct evidence for how each component contributes to overall efficiency.

- **Static dyadic quantization design explicitly bridges ML-MPC gap**: Section 4.2.1 identifies the two cross-domain gaps (dynamic quantization is expensive in MPC; type conversions are difficult in MPC) and proposes concrete solutions. Using dyadic scales (1/2^f) that map to cheap truncation shifts is a well-motivated design choice grounded in the constraints of MPC.

- **Practical system contribution with dynamic ring support**: The framework extends SPU to support multi-ring computation with automatic type-conversion insertion in the computation DAG (Figure 3), making the system deployable on models loaded from HuggingFace. This engineering contribution is substantial and addresses a real limitation of prior MPC frameworks.

---

## Weaknesses

### Fatal

None.

### Major

1. **UpCast protocol relies on an unverified range assumption.** The core optimization trick in Algorithm 1 (lines 261–264) assumes the input x lies in [-2^{ℓ-2}, 2^{ℓ-2}-1] so that after adding a bias of 2^{ℓ-2}, the MSB is guaranteed to be 0 and the wrap-detection reduces to a single AND operation. The paper describes this as a "positive heuristic trick" and provides a toy ℓ=8 example, but offers **no verification—either analytical or empirical—that this range actually holds** for the quantized values in the evaluated Transformer models. If the assumption fails in practice (e.g., due to outlier activations, accumulated rounding errors, or the fixed-point encoding itself), the UpCast protocol would produce incorrect results, and a more expensive correct protocol would be needed. Since the UpCast protocol is one of the paper's two main MPC primitives and directly underpins the efficiency claims, the authors must either (a) prove that the range is always satisfied given their quantization design and model architectures, (b) provide empirical evidence across all layers and inputs, or (c) characterize the failure cases and their impact. *Severity*: this is a real gap, but it is not fatal — the assumption is mild (for ℓ=32, it covers values in [-2^30, 2^30-1], i.e., ~99.9% of the signed 32-bit range) and likely holds in practice; however, the paper must substantiate this.

### Minor

2. **GPT2 utility degradation is understated.** The abstract and introduction claim "negligible utility degradation," but GPT2-base perplexity increases from 12.25 to 13.78 (a 12.5% relative increase) and GPT2-medium from 10.60 to 11.35 (~7% relative increase) under Quad approximation (Table 1). These are noticeable degradations in language modeling quality. The paper's discussion of utility loss (line 338) focuses on Bert tasks and CoLA but does not address the systematic perplexity increase on GPT2. The results are reported transparently, but the "negligible" characterization in the high-level claims should be calibrated against these GPT2 numbers, or the degradation should be explicitly contextualized (e.g., "acceptable for the target deployment scenario because...").

3. **Network setting for efficiency results is not disclosed.** The experimental setup (lines 313–315) describes both LAN (5Gbps, 0.4ms RTT) and WAN (400Mbps, 40ms RTT) environments, but the main efficiency results (Figure 4, Table 3) never specify which setting was used. Reported runtimes are uninterpretable without this context, as the communication vs. computation tradeoffs differ dramatically between LAN and WAN. For instance, the fact that communication reduction (e.g., 3.00× for Bert-base length 32) exceeds runtime reduction (1.76×) is consistent with communication-dominated settings (WAN), but the paper never confirms this.

4. **Missing reproducibility details.** The paper does not provide: (a) the per-layer quantization scales (fractional bits f for each layer), (b) distillation hyperparameters (learning rate, number of epochs, teacher/student architectures, loss weighting), or (c) the choice of 18 fractional bits for FXP64_18 (why 18 rather than 16 or 20?). While the paper states code will be open-sourced, these details are necessary for evaluation during review.

5. **The 18 fractional bits for FXP64_18 is unexplained.** Section 4.2.2 specifies FXP32_8 for linear and FXP64_18 for non-linear layers, but the rationale for 18 fractional bits (vs. 16 or 20) is not provided. Since the precision bits differ by exactly 10 (= 18 − 8), this may relate to the downcast shift, but the connection is not clarified.

### Trivial

- Table 3's speedup row labels "×" as "against PUMA" only in the caption, but the row itself just says "3.00×" — it would be clearer to include the reference baseline in the table.
- The Discussion section heading is present (line 466) but appears empty — if content existed in the original submission, this is a formatting artifact.

---

## Nice-to-Haves

- A comparison with SecureQ8 (discussed in related work) would strengthen the claim of being "first" to enable quantization-aware secure inference, even if the comparison is approximate or qualitative.
- Breaking down runtime into computation, communication, and idle time would help attribute where the speedup comes from and reconcile the LAN/WAN ambiguity.
- A brief security argument sketch for the UpCast protocol (showing that no information about the shares is leaked beyond the opened masked value y) would improve confidence, even for a systems paper.
- Standard deviations or multiple-run statistics for utility numbers would help assess whether the GPT2 degradation is statistically significant.

---

## Removed Points

- *"Pseudocode conflates different sharing types"* — The algorithm clearly separates 2-out-of-2 sharing (twoshare) from 3-out-of-3 RSS (share) using distinct notation. This is not an actual confusion.
- *"Round count analysis misses PRF rounds"* — PRF generation in Step 4 is non-interactive (parties use pre-shared PRF keys), so the 3-round claim is correct as stated.
- *"GeLU approximation borrowed from MPCFormer should be explicitly noted"* — The paper already says "Inspired by [MPCFormer]" (line 180). This criticism reflects a failure to read the existing text.
- *"Missing Discussion section"* — The Discussion heading is present but empty; this is almost certainly a parser artifact that stripped the content. Per the hard rules, parser-removed content cannot be cited as a weakness.
- *"Missing security proof sketch"* — The paper is a systems/empirical paper operating in a well-established 3PC security model (semi-honest, honest-majority). A formal security proof is not standard for such papers and was not claimed.
- *"MPCFormer run on CPU is unfair if others use GPU"* — The paper states *all* experiments use the same CPU setup (one AMD Ryzen CPU, line 313). The reviewer's speculation about GPU acceleration is unfounded.
- *"The toy example may not generalize to all linear layers"* — The toy example (Figure 1) is explicitly illustrative (it shows the scaling/clipping overhead problem) and the paper never claims exact proportions hold for every layer.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the UpCast heuristic assumption and the paper's correctness claims, but this is a weakness in need of fixing rather than a novel observation.

---

## Suggestions

1. **Address the UpCast range assumption directly.** This is the single most important issue. The authors should either (a) provide a formal proof that under their fixed-point quantization with FXP32_8 and FXP64_18, all intermediate values stay within [-2^{ℓ-2}, 2^{ℓ-2}-1], or (b) instrument the plaintext models to empirically verify that the range holds for all layers across representative inputs (report min/max values per layer), or (c) describe a fallback protocol that works correctly without the assumption and quantify its overhead.

2. **Specify which network setting (LAN or WAN) the reported efficiency numbers correspond to** in the captions of Figure 4 and Table 3. If both settings were tested, report both or clearly explain the choice.

3. **Calibrate the "negligible" utility claim.** Qualify the abstract/introduction statement to acknowledge the GPT2 perplexity increase (~7–12.5% relative), and add a brief discussion of why this level of degradation is acceptable (or not) for the intended deployment scenarios.

4. **Provide missing experimental details** in the main text or appendix: per-layer quantization bitwidths, distillation hyperparameters, and justification for the 18 fractional bits in FXP64_18.

5. **Clarify the MPCFormer runtime comparison.** MPCFormer's runtimes in Table 3 are notably high (e.g., 124s vs. PUMA's 43s for Bert-base, length 128) — a brief note on why MPCFormer's runtime is substantially worse than even the vanilla baseline would help readers interpret the speedup numbers.

---
