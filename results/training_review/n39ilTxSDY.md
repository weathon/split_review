Now I have all the information needed. Let me produce the final consolidated review.

## Summary

Ditto presents the first framework for quantization-aware secure Transformer inference under MPC. The key idea is a co-design of static dyadic quantization (power-of-two scales) with novel type-conversion MPC primitives (UpCast/DownCast) that enable mixed-precision computation across different rings. The paper demonstrates 3.14–4.40× speedup over MPCFormer and 1.44–2.35× speedup over PUMA on Bert and GPT2 models with negligible accuracy degradation.

## Strengths
- **Co-design of MPC-friendly static dyadic quantization and type-conversion primitives.** The paper identifies a genuine gap: plaintext quantization techniques use dynamic operations (min/max/clip) that are expensive in MPC. By adopting static dyadic quantization (power-of-two scales) and designing UpCast/DownCast protocols (Section 4.3.1), the framework enables quantization-aware secure inference that prior work could not support. The upcast protocol (Algorithm 1) is a non-trivial contribution for handling ring conversion in RSS.
- **Significant and well-documented efficiency gains.** End-to-end experiments (Section 5.2, Figure 2, Table 2) show Ditto achieves 3.14–4.40× speedup over MPCFormer and 1.44–2.35× speedup over PUMA across Bert-base, Bert-large, GPT2-base, and GPT2-medium models, in both LAN and WAN settings. Communication size reductions of 2.37–3.43× over PUMA are reported. These are substantial improvements.
- **Comprehensive evaluation across models, tasks, and settings.** The paper evaluates on 4 GLUE tasks (RTE, CoLA, QQP, QNLI) and Wikitext-103, with two model families (Bert, GPT2) at two scales each, under two network environments (LAN, WAN), with varying sequence lengths, and includes an ablation study separating the effects of quantization and approximation.
- **Practical system engineering.** The dynamic ring support and automatic type conversion compiler integration (Section 4.3.2) extends the SPU framework to handle mixed-precision secure computation without manual type management, making the framework deployable.

## Weaknesses

### Major
- **DownCast protocol is presented as exact local computation without acknowledging the known truncation error in RSS.** The paper claims (line 207–208) that downcast "suffices" as a local right-shift of each share followed by modulo. In 2-out-of-3 RSS, the secret is $x = x_0 + x_1 + x_2 \mod 2^\ell$, and locally right-shifting each share does **not** produce the same result as right-shifting the true secret value: carry bits from the lower $k$ bits of the three shares are lost, introducing a small error (bounded by at most ~3 in the integer domain). The paper cites ABY3 and mixed-ab-circuit-20 for truncation, both of which use protocols with communication for exact results. The paper does not acknowledge this approximation, analyze its impact on model accuracy, or justify why the error is acceptable. Given that the empirical accuracy results hold up, the issue is not necessarily fatal — probabilistic truncation with small errors is standard practice in MPC-based ML — but the current description is misleading and leaves a gap between claimed correctness and actual behavior.

- **The upcast protocol's "positive heuristic trick" relies on an unverified range assumption.** The optimization (lines 261–264) assumes the input $x$ lies in $[-2^{\ell-2}, 2^{\ell-2}-1]$. A bias $2^{\ell-2}$ is added to ensure the masked value's MSB is zero, enabling a cheap wrap computation. The paper provides no experimental validation that this range holds after layer-wise quantization and non-linear computations, nor any failure analysis for when it is violated. While the assumption is plausible for well-quantized networks, the lack of verification or fallback mechanism weakens the claim of correctness.

### Minor
- **No isolated cost breakdown for the type conversion primitives themselves.** The paper reports end-to-end efficiency gains but does not separately measure the communication/runtime cost of the UpCast and DownCast operations in isolation, nor compare them against standard truncation protocols (e.g., ABY3's probabilistic truncation). This makes it difficult to attribute the speedups specifically to the novel primitives vs. the quantization itself.
- **No discussion of whether the DownCast error accumulates across layers.** Since downcast operations are invoked throughout the network (e.g., after every LayerNorm), even a small per-operation error could compound. The paper does not analyze this. The good end-to-end accuracy suggests the effect is small, but a layer-wise precision/error analysis would strengthen the work.

### Trivial
- None.

## Nice-to-Haves
- Reporting confidence intervals or multiple seeds for utility results on smaller datasets (RTE, CoLA) would help establish that accuracy differences are not within noise.
- A brief security argument (even informal, semi-honest) for the UpCast protocol would improve completeness, though it is not strictly required for this type of venue.

## Removed Points
- **"Downcast is 'fundamentally incorrect' / would make the method not work at all"** — This overstates the issue. Local truncation introduces a small statistical error that is standard practice in MPC for ML. The paper's empirical results validate that the method functions correctly. The real weakness is the lack of acknowledgment/analysis of this approximation, not that the protocol is "incorrect" or that the paper's claims are invalidated.
- **"No comparison against SecureQ8"** — SecureQ8 targets int8 quantization for CNNs, not Transformers, and as the paper correctly notes (line 75), its quantization does not extend to ciphertexts which remain over a uniform large ring. Direct comparison is not meaningful; the paper's discussion of how Ditto overcomes SecureQ8's limitations is sufficient.
- **"No security proof for upcast"** — Formal security proofs are not standard for systems/ML papers at venues like ICLR/NeurIPS. The paper describes the security model (semi-honest, honest-majority) and provides communication analysis, which is adequate.
- **"No confidence intervals"** — Single-run evaluation is the norm in this line of work (MPCFormer, PUMA, etc.).
- **"Discussion section is stripped"** — Parser artifact; not the authors' error.
- **Missing related works** — Cannot be independently verified; per instructions, not included.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a genuine technical gap (the DownCast local-truncation approximation) that the paper should have discussed, but they do not introduce otherwise unavailable insights about the method.

## Suggestions
1. **Acknowledge and analyze the DownCast approximation.** Replace the claim that local right-shift "suffices" with a precise description: explain that this is a probabilistic truncation with a bounded error (cite ABY3), characterize the error bound, and show empirically or analytically that it does not affect model accuracy.
2. **Validate the upcast range assumption empirically.** Provide a brief analysis (e.g., trace activation ranges for a few layers across the evaluated models) showing that inputs to upcast operations indeed fall within $[-2^{\ell-2}, 2^{\ell-2}-1]$, or provide a fallback protocol when the assumption is violated.
3. **Report the isolated cost of type conversions.** A table showing communication/runtime of UpCast and DownCast vs. standard ABY3 truncation would help readers understand the source of efficiency gains.

## Score and Decision

**Score**: 6.0

**Decision**: Weak Accept

The paper addresses a timely and important problem with a well-motivated co-design approach. The efficiency gains over strong baselines (MPCFormer, PUMA) are substantial and well-documented across multiple models and settings. However, the paper has a non-trivial presentation gap regarding the DownCast protocol: the claim that local right-shift "suffices" for exact truncation in RSS is technically incorrect, though the empirical results suggest the method works in practice (as probabilistic truncation is standard in this domain). This does not invalidate the core contribution — the static dyadic quantization + upcast protocol + compiler integration — but it needs to be honestly discussed. With clarifications and an error analysis, the paper would be solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>