Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes HiRA (Hadamard High-Rank Adaptation), a PEFT method that computes the update matrix as the Hadamard product of the frozen pretrained weight \(W_0\) and a low-rank matrix \(AB\) (i.e., \(\Delta W = W_0 \odot (AB)\)). Because \(\text{Rank}(W_0 \odot AB) \leq \text{Rank}(W_0) \times \text{Rank}(AB)\), this can yield a much higher-rank update than LoRA (which is bounded by \(r\)) while keeping the same number of trainable parameters. Experiments on commonsense reasoning, dialogue generation, and mathematical reasoning show HiRA consistently outperforming LoRA, DoRA, and MoRA. The paper also provides an upper bound on the approximation error and analyzes how the gradient interacts with \(W_0\).

## Strengths

- **Empirically demonstrated high-rank updates with parameter efficiency.** Figures 1 and 7 show HiRA achieves an average update-matrix rank of ~2837 compared to LoRA's 32, using the same number of trainable parameters. This directly validates the central architectural claim.

- **Consistent performance gains across diverse tasks.** On commonsense reasoning (Table 1), HiRA with \(r=32\) achieves 86.72% on Llama-3-8B, outperforming DoRA (85.20%). On mathematical reasoning (Table 3, Llama-3-8B), HiRA reaches 70.81% vs. LoRA's 65.89% and MoRA's 67.98%. On dialogue generation (Table 2), HiRA surpasses all baselines on every metric. These results are consistent across two model families and three task types.

- **Ablation studies that inform design choices.** Table 4 shows that replacing \(W_0\) with a random fixed matrix (HiRA\(_{\text{rand}}\)) degrades performance, confirming that the pretrained weights contribute substantively. Figure 6 shows monotonic improvement as \(r\) increases. Section 6.6 combines HiRA with LoRA and shows the HiRA component contributes more per parameter than the LoRA component. These ablations give a nuanced picture of how the method works.

- **Inference overhead identical to LoRA.** Section 4.4 explains that the merged weights \(W' = W_0 + W_0 \odot (AB)\) form a single matrix, and the original \(W_0\) can be recovered via element-wise division by \(AB+1\). This enables fast task switching without additional compute at inference time.

## Weaknesses

### Fatal

None.

### Major

1. **The HiRA\(_{\text{rand}}\) ablation (Table 4) undermines the paper's central narrative that high rank drives improvement.**  
   A random matrix from uniform \([0,1]\) is full-rank with high probability, so HiRA\(_{\text{rand}}\) also achieves high rank. Yet it significantly underperforms HiRA (which uses \(W_0\)). This strongly suggests that the *specific content* of \(W_0\) — the inductive bias from the pretrained weights — is at least as important as the rank increase. The paper's motivation (Section 3, Figure 2) shows that increasing LoRA's rank improves performance, which is consistent with rank mattering, but that does not isolate rank as the mechanism behind HiRA's gains. The paper would need an ablation that varies rank while holding the "informativeness" of \(R\) constant (e.g., using a different pretrained matrix as \(R\)) to support the causal claim. As is, the evidence is equally consistent with "HiRA works because \(W_0\) provides a good prior for scaling the low-rank update" — a different and less emphasized narrative. This does not invalidate the method's empirical success, but it means the paper's framing is overclaimed relative to the evidence.  
   *Severity justification: This concerns the paper's core interpretation of why the method works, not whether it works. The method itself remains empirically validated.*

2. **The anomalously large gain on Llama-2-7B mathematical reasoning requires explanation.**  
   On GSM8K, HiRA achieves 46.85% while LoRA achieves 15.16% — a gap of 31.69 percentage points. DoRA (22.59%) and MoRA (31.08%) are also well below typical reported ranges for Llama-2-7B on GSM8K. The paper follows the "identical training setup" of Liu et al. (2024) and uses only 2 epochs, but does not verify that its baseline implementations reproduce expected numbers from the literature or from that reference. The paper also does not comment on why this gap is so much larger than the gaps on the other two tasks (where HiRA's advantage over LoRA is ~3–5 points). If the gap is genuine, it is extraordinary and deserves analysis; if it is due to a configuration issue (e.g., undertuned baselines), the reported advantage may be inflated. Without resolution, the reader cannot assess the reliability of this result.  
   *Severity justification: A result this far outside normal ranges demands explanation. The paper provides none.*

### Minor

1. **Theorem 1 does not provide a meaningful superiority guarantee over LoRA.**  
   The theorem bounds HiRA's approximation error by \(\sigma_{r+1}(\overline{E} \oslash W_0) \|W_0\|_2\). LoRA's standard bound is \(\sigma_{r+1}(\overline{E})\). Since these involve different matrices, the theorem does not establish that HiRA's bound is tighter — it simply expresses the bound in terms of a different object. The paper's own discussion acknowledges this limitation ("\(W_0\) serves a dual role: it confines and facilitates the adaptation"). The theorem is mathematically correct but does not advance the paper's narrative about superior expressiveness relative to LoRA. It would be more informative as a remark rather than a highlighted contribution.

2. **No variance information reported for any result.**  
   The paper states that HiRA is evaluated over 5 runs, but Tables 1–3 report only point estimates without standard deviations or confidence intervals. For a method where improvements are sometimes modest (e.g., +1.5% on Llama-3-8B commonsense reasoning), the reader cannot assess whether differences are statistically reliable. This is standard practice to report in PEFT papers and is necessary for the reader to evaluate the strength of the evidence.

3. **Rank computation methodology for Figure 7 is unspecified.**  
   Figure 4 uses a threshold of 0.005 for counting singular values. It is unclear whether the same threshold is used for computing the "average rank" in Figure 7, or whether a different numerical rank criterion (e.g., tolerance-based SVD truncation) is applied. This should be specified.

### Trivial

- The paper mentions recovery of \(W_0\) by element-wise division by \(AB+1\), noting that no entry of \(AB\) may equal \(-1\). This minor numerical concern could be addressed with a small damping term but is not discussed.

## Nice-to-Haves

- A discussion of peak memory usage during training: HiRA may need to materialize the full \(d \times k\) matrix \(W_0 \odot (AB)\) during the forward pass, whereas LoRA only materializes the low-rank factors. While the computational complexity is equivalent (\(O(drk)\)), the memory footprint may differ.

## Removed Points

These points were raised by reviewers but are removed per the review guidelines:

- **Request for comparison with FourierFT / Kronecker methods.** Removed: the instruction says "DO NOT mention missing related works" as external verification is not available. The paper's baseline selection (LoRA, DoRA, MoRA, Prompt Tuning, P-tuning) is defensible for its class.
- **Criticism that the "first to apply Hadamard product" framing is diminished.** Removed: this is a subjective framing preference, not a factual error. The paper provides empirical evidence for the approach regardless of how the novelty is phrased.
- **Suggestion about adding confidence intervals.** Moved to Minor (point 2 above) — the concern is valid but is already accounted for as missing variance information.
- **Criticism about the -1 division issue being undiscussed.** Downgraded to Trivial — it is a minor numerical edge case, not a structural concern.
- **Request for a deconfounding ablation that varies rank while holding \(W_0\) constant.** This is a reasonable suggestion for strengthening the paper. It is reflected in Major weakness #1 (the narrative issue) but the specific experimental design is a suggestion, not a required fix for acceptance.
- **"Memory overhead discussion" suggestion retained as Nice-to-Have** — it is a reasonable suggestion but not required for the paper's core claims.

## Novel Insights

The HiRA\(_{\text{rand}}\) ablation reveals something genuinely interesting beyond the paper's own framing: the Hadamard product with \(W_0\) is effective because \(W_0\) is not just any high-rank matrix but a *pretrained* one with latent structure that aligns well with the gradient signal. The gradient analysis in Section 4.7 shows that \(W_0\) modulates the gradient element-wise, which means adaptation concentrates on entries where \(W_0\) already has large magnitudes — effectively a learned importance weighting. This suggests that the method's real strength may be an implicit form of parameter-space regularization or importance-aware updating, rather than rank expansion per se. This mechanism is under-analyzed in the paper and could be a fruitful direction for future work.

## Suggestions

1. **Deconfound rank from the source of \(R\).** Add an ablation where \(R\) is a different fixed high-rank matrix that is also informative (e.g., a pretrained weight from a different layer, or a different pretrained model's weight). If HiRA still outperforms LoRA, the rank hypothesis gains support. If it does not, reframe the contribution: the method works because \(W_0\) provides a structured prior, and high rank is a side effect rather than the primary mechanism.

2. **Verify baseline fidelity for the Llama-2-7B math results.** Report what numbers the same experimental setup produces for each baseline and whether they match those reported in (Liu et al., 2024) or other published work. If they do not match, explain the discrepancy. Report individual seed results for at least the math reasoning task.

3. **Report means ± standard deviations** for all main results (Tables 1–3), or state if only single runs were performed and why.

4. **Specify the rank computation methodology** for Figure 7 (threshold, SVD tolerance, or numerical rank criterion) and justify the choice.

5. **Demote Theorem 1** from a highlighted theoretical contribution to a remark or observation, unless a meaningful comparison to LoRA's bound can be added (e.g., a condition under which HiRA's bound is strictly tighter).

## Score and Decision

**Originality:** High. The Hadamard-product formulation for PEFT is novel and the connection to high-rank updates is clean.

**Importance:** Moderate–High. PEFT is an active area and methods that improve upon LoRA without increasing inference cost are valuable.

**Claims well-supported:** Partially. The empirical results broadly support effectiveness; but the central "rank is the driver" narrative is not well-supported by the evidence (the HiRA\(_{\text{rand}}\) ablation points to a different mechanism). The anomalously large math gap needs explanation. Theorem 1 is not as supportive as claimed.

**Soundness:** Moderate. The experimental design is reasonable but missing error bars and the unexplained math gap weaken confidence.

**Clarity:** Good. The paper is well-structured and the method is clearly explained.

**Value:** Moderate. The method is simple, effective, and practically useful. The empirical results are promising but the current evidential base needs strengthening.

The paper proposes a simple, effective, and practical PEFT method. The core concern is not that the method fails — it clearly works across tasks — but that the paper's narrative about *why* it works is overclaimed relative to the evidence, and one unusually large result lacks explanation. These are fixable in revision. The contribution is genuine and the method is likely to be useful to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>