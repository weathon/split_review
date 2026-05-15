## Summary

The paper proposes HiRA (Hadamard High-Rank Adaptation), a PEFT method that replaces LoRA's low-rank product ΔW=AB with a Hadamard product ΔW=W₀⊙(AB), where W₀ is the frozen pre-trained weight. Because the rank of a Hadamard product can be as large as the product of the ranks of the two factors, HiRA yields update matrices with empirically much higher rank than LoRA (thousands vs. 32) while keeping the same number of trainable parameters. The method is cleanly formulated, merges into the original weights for inference like LoRA, and shows consistent improvements over LoRA, DoRA, and MoRA on commonsense reasoning (Table 1) and dialogue generation (Table 2).

---

## Strengths

- **Novel and conceptually clean formulation.** HiRA modifies LoRA by simply replacing matrix multiplication with a Hadamard product with the frozen pre-trained weight. The idea is elegant, has a clear rank-theoretic motivation (Section 4.2), and inherits LoRA's key practical benefits (mergeability, no inference overhead). The observation that R=ones recovers LoRA as a special case (Section 4.3) correctly contextualizes the contribution.

- **Empirical evidence of higher-rank updates.** Figures 1 and 7 show that HiRA's update matrices have orders-of-magnitude higher rank than LoRA's (e.g., average ~2837 vs. 32) and also exceed MoRA's, directly supporting the paper's central motivation. Figure 4 further shows that HiRA's singular-value distribution more closely resembles full fine-tuning than LoRA's, and Figure 5 shows it avoids the excessively large singular values that LoRA/MoRA exhibit.

- **Consistent performance gains on commonsense reasoning and dialogue.** On commonsense reasoning (Table 1), HiRA with r=32 achieves 86.72% on Llama-3-8B, outperforming DoRA (85.20%) and LoRA (84.63%). On ConvAI2 dialogue (Table 2), HiRA achieves 47.80 average vs. DoRA's 46.62. These gains hold across both Llama-2-7B and Llama-3-8B, demonstrating robustness.

- **Systematic ablation studies.** The paper validates key design choices: (a) Table 4 shows that using W₀ as the fixed matrix R significantly outperforms a random R (HiRA_rand), confirming the pre-trained weights provide useful structure; (b) Figure 6 shows monotonic improvement with increasing r; (c) Table 5 analyzes placement across transformer components; (d) Table 6 explores combining HiRA with LoRA.

- **Practical deployability.** Section 4.4 shows that HiRA can merge update parameters into W₀ for inference (no latency overhead) and recover original parameters via elementwise division — a concrete advantage over MoRA, whose compression/decompression mappings make clean merging difficult.

---

## Weaknesses

### Fatal
None.

### Major

- **The LoRA baseline on Llama-2-7B mathematical reasoning (Table 3) is implausibly low and undermines the math claims.** LoRA achieves only 15.16% on GSM8K with Llama-2-7B, while the same method gets 65.89% on Llama-3-8B under the same setup. HiRA achieves 46.85% on the same Llama-2-7B model — a 31.69 pp improvement. The paper uses "the identical training setup to (Liu et al., 2024)," making it difficult to attribute this gap to a known limitation of LoRA. Without an explanation or verification of this baseline, the mathematical reasoning results cannot be taken at face value. This issue is specific to the Llama-2-7B math results; the commonsense reasoning and dialogue results (where LoRA baselines appear reasonable) are not affected.

### Minor

- **No variance or significance reported on any main result (Tables 1, 2, 3), despite 5 random seeds being used.** Several margins are small (e.g., HiRA vs. DoRA on Llama-3-8B commonsense: 86.72% vs. 85.20%, a 1.52 pp difference). Without standard deviations or significance tests, the reader cannot assess whether these differences are within noise. Adding error bars or significance measures would substantially strengthen the paper.

- **Rank computation threshold is not specified for Figures 1 and 7.** The rank of a matrix in numerical computation must be determined by counting singular values above a cutoff. Figure 4 specifies a threshold of 0.005, but Figures 1 and 7 (which present the headline "2837 vs. 32" claim) do not. This makes the central empirical claim about rank not fully reproducible. The authors should specify the threshold used for all rank figures and show robustness to threshold choice.

- **Theorem 1 does not provide a comparative guarantee against LoRA.** The theorem bounds HiRA's approximation error as σ_{r+1}(Ē ⊘ W₀) ‖W₀‖₂, while citing a known bound for LoRA of σ_{r+1}(Ē). The paper does not relate these two bounds — it neither proves nor empirically shows that σ_{r+1}(Ē ⊘ W₀)‖W₀‖₂ < σ_{r+1}(Ē) under reasonable conditions. As presented, the theorem is a correct re-expression of the problem but does not formally demonstrate that HiRA is more expressive. The qualitative discussion in Section 4.6 is reasonable, but the theorem's role as a "theoretical justification" is overstated.

- **Gradient analysis (Section 4.7) shows a structural difference but does not establish a practical benefit.** The derivation correctly shows that HiRA's gradients involve W₀ while LoRA's do not. However, involvement of W₀ could equally cause optimization instability (e.g., if W₀ has large/small entries). The claim that this "leverages information" to improve adaptation is asserted without supporting evidence.

### Trivial
None.

---

## Nice-to-Haves

- Include a full fine-tuning baseline on at least one task (e.g., GSM8K with Llama-3-8B) to contextualize the PEFT results against an upper bound.
- Plot full singular value spectra for a few layers (not just counts above a threshold) to show whether HiRA's high rank reflects genuine signal or noise-floor singular values.
- In Table 4 (choice of R), include the natural baseline R = ones (i.e., vanilla LoRA) to directly compare using W₀ vs. using no information.
- Ablate R with a random matrix that preserves W₀'s singular value distribution (not just uniform random) to separate the effect of having a fixed structured matrix vs. specifically W₀.
- Report actual trainable parameter counts for each baseline in a table rather than describing them as "comparable."

---

## Removed Points

These points were flagged by input reviewers but are removed from the main review. Treat with caution if using them to evaluate the paper.

- *"The claim of being 'first to apply Hadamard product to PEFT of LLMs' is not verified here."* — The paper makes a plausibility claim and this is not a substantive weakness; reviewers do not have complete knowledge of all related work.
- *Strength Finder's claim that "gains are statistically significant."* — Factually incorrect; the paper does not report statistical significance. Removed from strengths.
- *General reproducibility nitpicks about undisclosed training details.* — The paper provides standard implementation details consistent with prior work (DoRA setup).
- *Formatting-related observations from the harsh critic's section-by-section notes.* — These are observations, not actionable weaknesses.
- *Criticisms about missing appendix content or missing references.* — The submission format strips these; they exist in the original.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on HiRA that the paper itself does not already articulate. The observation that the method's rank benefit comes from the Hadamard product's product-of-ranks upper bound (vs. multiplication's min-of-ranks bound) is clean and well-explained in the paper itself.

---

## Suggestions

1. **Fix the LoRA math baseline or clarify what caused the 15.16% result.** Re-run the Llama-2-7B math experiment and report whether the low value reproduces. If it does, explain the discrepancy (e.g., training for only 2 epochs may not be sufficient for LoRA on this setup). If it does not, correct the table.
2. **Add standard deviations to Tables 1, 2, and 3.** With 5 seeds available, this is a simple and high-impact fix.
3. **Specify the singular-value cutoff for Figures 1 and 7, and show robustness to threshold choice** (e.g., a table or plot showing rank vs. threshold from 1e-1 to 1e-5).
4. **Either strengthen or de-emphasize Theorem 1.** Either add an empirical comparison of the two bounds (σ_{r+1}(Ē ⊘ W₀)‖W₀‖₂ vs. σ_{r+1}(Ē)) across layers, or reframe the theorem as a structural observation rather than a comparative guarantee.

---

## Score and Decision

The paper presents a genuinely novel and conceptually clean PEFT method. The HiRA formulation is elegant, practically appealing (mergeable, no inference overhead), and supported by credible results on commonsense reasoning and dialogue tasks. The ablations are thorough and validate the design choices.

However, the mathematical reasoning claims are undermined by a LoRA baseline (15.16% on GSM8K with Llama-2-7B) that appears anomalously low, and the absence of variance reporting makes it difficult to assess whether smaller margins are significant. The theoretical framing (Theorem 1) is also weaker than claimed. The core idea has merit, but the experimental evidence needs strengthening before the paper's conclusions can be fully trusted.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>