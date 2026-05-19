- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper establishes the first scaling law for masked diffusion models (MDMs), demonstrating a scaling rate comparable to autoregressive models (ARMs) with a constant compute gap of ~16× (smaller than the 64× factor reported for continuous diffusion models). The authors propose unsupervised classifier-free guidance (CFG), a theoretically grounded technique that leverages the MDM's probabilistic formulation to boost performance without paired data. Empirically, a 1.1B MDM outperforms the larger 1.5B GPT-2 on 4/8 zero-shot benchmarks, matches a same-sized ARM in conditional generation while being 1.4× faster, and most strikingly breaks the reverse curse where GPT-3 (175B) and Llama-2 (13B) achieve 0% accuracy.

## Strengths

1. **First scaling law for MDMs (Section 3).** Using IsoFLOP analysis across compute budgets from 6×10¹⁸ to 10²⁰ FLOPs, the paper shows MDM validation loss follows a power law with a rate comparable to ARMs (Fig. 2a). The optimal parameter size of MDMs is approximately half that of ARMs at equal compute (Fig. 2b). The 16× compute gap versus ARMs is smaller than the 64× gap reported for continuous diffusion models (Gulrajani et al., 2024).

2. **Unsupervised CFG (Section 4).** The paper introduces a novel formulation (Eq. 7) that replaces the unconditional distribution in standard CFG with a dummy-masked conditional distribution, enabling guidance without paired data. This is theoretically justified through the MDM's conditional distribution property (Eq. 3 → Eq. 8). Table 1 shows unsupervised CFG improves the 220M MDM on all eight zero-shot benchmarks (e.g., LAMBADA from 36.00 to 40.99, OpenBookQA from 27.00 to 34.20).

3. **Breaking the reverse curse (Section 7.1, Table 7).** A 1.1B MDM achieves 92% accuracy on reverse DescriptionToName queries and 37% on reverse NameToDescription with BLEU 67, where GPT-3 (175B) and Llama-2 (13B) both score 0% on reverse tasks. This is the paper's most striking and well-supported result — the MDM architecture's bidirectional attention directly addresses a known ARM limitation.

4. **Competitive zero-shot language understanding (Section 5, Tables 2–3).** The 1.1B MDM outperforms the larger 1.5B GPT-2 on 4/8 benchmarks (BoolQ, OpenBookQA, RACE, LAMBADA). In controlled comparisons on SlimPajama, MDMs at equal FLOPs match ARMs (4/8 tasks), and with 16× more FLOPs (as suggested by the scaling law), surpass ARMs on all eight tasks.

5. **Flexible quality–efficiency trade-off in conditional generation (Section 6, Table 6).** The 1.1B MDM matches ARM quality (1.56 vs 1.57) while being 1.4× faster (396s vs 555s), or surpasses ARM quality (1.60) at 1.4× slower speed (780s). This trade-off is not available to ARMs with KV-cache, where faster decoding means lower quality is fixed.

6. **Robustness to temporal data shift (Section 7.2, Table 8).** Despite slightly worse perplexity on the training distribution (SlimPajama: 18.02 vs 17.34), the MDM achieves lower perplexity on 2024 FineWeb data (24.06/24.01 vs 27.01/26.93), demonstrating less sensitivity to distributional drift.

## Weaknesses

### Fatal
None.

### Major

- **Training FLOPs for the 1.1B ARM in the conditional generation comparison are not reported.** Section 6 states both the ARM and MDM are "pre-trained as described in Sec. 4 with 1.1B parameters each" and that the MDM's pre-training time is extended by 16×, but the ARM's actual training FLOPs are never stated. The scaling law section (Sec. 4) only specifies compute budgets up to 10²⁰ FLOPs for the IsoFLOP analysis, not for 1.1B models. Without knowing whether the 1.1B ARM was trained to Chinchilla-optimal tokens or was undertrained, the claim that the MDM "matches the performance ... while being 1.4× faster" is difficult to fully evaluate. This is a documentation gap that the authors should fill in the rebuttal.

### Minor

- **The scaling-law (validation-loss) results and downstream task performance are not directly connected.** The scaling law shows MDMs need ~16× more FLOPs to match ARM validation loss, yet Table 2 shows MDMs at *equal* FLOPs already match ARMs on 4/8 zero-shot tasks. The paper does not discuss why validation loss and task accuracy diverge in this way. This is not a contradiction (validation loss and downstream accuracy are known to imperfectly correlate), but the paper would be strengthened by explicitly acknowledging this and discussing how the scaling law relates to task-level capabilities.

- **The temporal degradation experiment (Table 8) confounds model architecture with unequal training compute.** The paper acknowledges this ("MDMs require 16 times more computation to reach this performance level") but the robustness claim would be substantially stronger with an ARM trained for ~16× more FLOPs. As it stands, the MDM's lower perplexity on FineWeb 2024 could partly reflect its heavier training rather than an inherent architectural advantage for distribution shift.

- **The unsupervised CFG vs. standard CFG comparison in conditional generation (Table 5) lacks error characterization.** The reported scores (1.53 standard vs. 1.60 unsupervised) are single values without variance, confidence intervals, or significance testing. The difference is small, and it is also a comparison of different fine-tuning protocols (unsupervised CFG fine-tunes only the conditional distribution; standard CFG fine-tunes both conditional and unconditional — an unequal training budget). While the paper's claim that unsupervised CFG "leverages large-scale unpaired data" is plausible, the experimental support is thinner than desirable for a central methodological contribution.

- **The IsoFLOP analysis spans a relatively narrow compute range (6×10¹⁸ to 10²⁰ FLOPs, ~16.7×).** Scaling laws in prior work (Kaplan et al., Chinchilla) typically cover 2–3 orders of magnitude. The power-law exponent estimates would be more reliable with a wider range. The paper should acknowledge this limitation explicitly.

### Trivial
None.

## Nice-to-Haves

- Including standard errors or confidence intervals for zero-shot accuracy and MT-Bench scores would help readers assess the significance of observed differences.
- A brief discussion of failure cases or sensitivity of unsupervised CFG to the dummy mask length or CFG scale would improve reproducibility.
- Controlling for training compute in the temporal degradation experiment (training an ARM for ~16× more FLOPs) would strengthen the robustness claim from suggestive to conclusive.

## Removed Points

**Weaknesses removed (with justification):**

1. *"The reverse curse result is on a narrow synthetic task and may not generalize."* — Removed (scope creep). The paper uses the exact benchmark from the original reverse curse paper (Berglund et al., 2023). That the task is synthetic and diagnostic is the entire point; it is the standard evaluation for this phenomenon. Asking for additional naturalistic tests is a reasonable future direction, not a weakness of the presented results.

2. *"The scaling-law/downstream tension undermines the core narrative."* — Demoted from "Critical Issues" to Minor (see Weaknesses above). The paper never claims validation loss perfectly predicts task performance. The scaling law is used to *motivate* training MDMs longer; the downstream experiments then show that with that extra compute, MDMs perform well. This is internally consistent.

3. *"The comparison with GPT-2 is not controlled because GPT-2 was trained on different data."* — Removed. The paper explicitly acknowledges this ("its FLOPs are unknown" in the table caption) and uses GPT-2 only as a literature anchor. The controlled comparison is in Table 2 (both models trained on SlimPajama).

4. *"Formatting/parser artifacts in Section 5"* and *"truncated sentences in Sec. 6."* — Removed per instructions (parser errors, not author errors).

5. *"No discussion of the CFG scale used in Table 1."* — The paper says "we use the rescaled conditional distribution defined in Eq. (6)" for the zero-shot experiments. While the scale parameter isn't explicitly stated here, this is a minor omission; the CFG-scale search is fully described for the MT-Bench experiments.

6. *"Missing appendix, proofs, or references."* — Removed per instructions (parser strips these sections).

**Strengths removed (with justification):**

None — all strengths identified by the Strength Finder are concrete, specific to this paper, and grounded in evidence.

## Novel Insights

The most interesting observation that emerges from synthesizing the reviews is the **mismatch between the scaling-law hierarchy (validation loss) and the downstream task hierarchy (accuracy)**. The scaling law says MDMs need ~16× more FLOPs to match ARM validation loss; yet at equal FLOPs, MDMs already match or beat ARMs on half of the zero-shot benchmarks (Table 2). This decoupling suggests that the 16× gap is a property of the training loss surface (which ARMs optimize more directly for next-token prediction), not a predictor of the models' relative ability to extract useful features for downstream tasks. The paper's reverse curse and temporal robustness results further support that the validation-loss gap may overstate the practical gap. A productive future direction would be to study whether bidirectional architectures inherently achieve better feature efficiency per unit of training loss — an idea that the paper's data supports but does not explicitly articulate.

## Suggestions

1. **Report training FLOPs for the 1.1B ARM** used in the conditional generation comparison (Table 6). This is the single most important missing detail.

2. **Add a brief discussion** connecting the scaling-law findings to the downstream results — explicitly noting that validation loss and task accuracy are not perfectly correlated, and that the 16× gap should be interpreted as a training-dynamics finding rather than a hard lower bound on performance.

3. **Run the temporal degradation experiment with equal-compute models** (e.g., an ARM trained for ~16× more tokens to match the MDM's validation loss) to disentangle whether the MDM's robustness is architectural or a byproduct of heavier training.
