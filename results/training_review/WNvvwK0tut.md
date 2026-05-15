Now I have thoroughly analyzed the paper and all reviews. Let me construct the authoritative final review.

## Summary

This paper presents a comprehensive study of masked diffusion models (MDMs) for language modeling at scale, establishing the first scaling law for MDMs, proposing unsupervised classifier-free guidance, and evaluating MDMs up to 1.1B parameters on language understanding, conditional generation, reverse curse, and temporal robustness tasks. The central claim is that MDMs are a competitive alternative to autoregressive models (ARMs).

## Strengths

- **First scaling law for MDMs with comparable scaling rate.** The IsoFLOP analysis (Section 3) demonstrates that MDMs exhibit a power-law scaling exponent similar to ARMs, with a constant compute gap of ~16× that is notably smaller than the 64× gap reported for continuous diffusion models. This is the first such analysis for MDMs and directly supports their scalability.

- **Unsupervised classifier-free guidance that works without paired data.** The paper proposes a simple formulation (Eq. 10) that replaces the unconditional distribution with a dummy-conditioned distribution, exploiting the fact that MDMs pretrained on unlabeled text model joint distributions. Table 1 shows unsupervised CFG improves accuracy on all eight zero-shot benchmarks (e.g., +7.2 on OpenBookQA, +4.99 on LAMBADA) despite using no paired data.

- **Competitive zero-shot language understanding across multiple benchmarks.** A 1.1B MDM outperforms the larger 1.5B GPT-2 on 4/8 tasks (BoolQ, OpenBookQA, RACE, LAMBADA) as shown in Table 3. Against same-sized ARMs pretrained on the same data with the same FLOPs, MDMs win on 4/8 tasks (Table 2).

- **Demonstrates bidirectional reasoning on the reverse curse.** On the reverse curse dataset (Table 6), a 1.1B MDM achieves 92% accuracy on reverse Description→Name, where cited results for GPT-3 (175B) and Llama-2 (13B) show 0%. This provides evidence that MDMs handle bidirectional relationships substantially better than standard ARMs.

- **Flexible quality-efficiency trade-off in conditional generation.** On MT-Bench (Table 5), a 1.1B MDM at 128 sampling steps (1.56 score, 396s) closely matches a same-sized ARM (1.57, 555s) while being ~1.4× faster. At 256 steps (1.60, 780s), it surpasses the ARM in quality.

- **Evidence of robustness to temporal distribution shift.** On FineWeb 2024 data (Table 7), a 220M MDM achieves lower perplexity (24.06) than an equally-sized ARM (27.01) despite both being trained on SlimPajama (2023), suggesting MDMs are more robust to temporal shifts.

## Weaknesses

### Fatal
None.

### Major

- **Per-task selection of likelihood evaluation method inflates reported results.** The paper (Section 5) uses chain-rule likelihood for OpenBookQA and PIQA but Monte Carlo estimation for ARC-Easy, Hellaswag, RACE, and SIQA, selecting whichever method gives higher accuracy per task. This post-hoc selection is not pre-specified, and no single consistent evaluation method is reported alongside it. The CFG scale parameter (w) for these results is also not reported; if it was tuned per task, the problem compounds. This weakens the reliability of the claimed superiority in zero-shot comparisons.

- **Reverse curse comparison may not be apples-to-apples.** The MDM is fine-tuned on the reverse curse training set (as stated in Section 7.1: "We fine-tune MDMs on these statements"). The GPT-3 and Llama-2 results are sourced from Berglund et al. and Lv et al., but the paper does not clarify whether those prior evaluations also involved fine-tuning on the same training statements or were zero-shot/few-shot. If the reference ARMs were not fine-tuned, the comparison is asymmetric and the claim "breaks the reverse curse encountered by much larger ARMs" is overstated. The paper should either confirm the protocols matched or provide a controlled experiment where an ARM is fine-tuned under identical conditions.

- **Scaling law compares mismatched loss quantities without validation.** The MDM loss (Eq. 5) is an upper bound on negative log-likelihood, while the ARM loss is exact cross-entropy. These are plotted on the same axis (Fig. 2) and used to derive the "constant compute gap of 16×." The paper does not assess how tight the MDM bound is or compute actual NLL for MDMs. If the bound is loose, the absolute gap could differ. The scaling rate (power-law exponent) is less affected, but the claimed 16× gap lacks direct support.

### Minor

- **Unsupervised CFG mechanism is underspecified.** The paper replaces the unconditional distribution with a dummy mask sequence vm (Eq. 10) but does not analyze whether the model's behavior on all-mask condition inputs is actually equivalent to unconditional inference. The empirical results (Table 1) indirectly validate the approach, but an analysis (e.g., comparing model predictions under all-mask condition vs. a held-out unconditional evaluation) would strengthen the claim.

- **Temporal degradation experiment confounded by training compute.** The 220M MDM required 16× more computation than the 220M ARM to reach similar validation loss (noted in Section 7.2). The robustness advantage could partly come from more training rather than the architecture itself. An ablation matching training steps (not validation loss) would be informative.

- **GPT-2 comparison confounded by training data.** The 1.1B MDM is trained on SlimPajama while GPT-2 (1.5B) was trained on WebText. The paper does not control for the training data confound when claiming superiority on 4/8 tasks.

- **CFG scale not reported for zero-shot results.** While the CFG scale is reported for the reverse curse (0.8, Table 6) and the CFG ablation (searched in {0.4, 0.6, 0.8, 1}), it is not disclosed for the zero-shot understanding results in Tables 1–3.

### Trivial
None beyond presentation issues attributable to PDF parsing artifacts.

## Nice-to-Haves
- An ablation comparing unsupervised CFG to an actual unconditional model (trained without any condition) to validate the all-mask condition approximation.
- Compute actual NLL (via importance sampling) for MDMs at several scales to verify the 16× compute gap is not an artifact of the loss bound.
- A controlled reverse curse experiment where an ARM is fine-tuned on the same training data under identical conditions.

## Removed Points

These points were removed from the harsh critic's review and are included here only for completeness. They should be treated with caution.

- **"Conditional generation trade-off claim not supported"** — REMOVED as factually incorrect. The critic claimed "the only MDM configuration that is 1.4x faster (64 steps, 204s) achieves score 1.40, substantially lower than ARM's 1.57." However, the 128-step MDM (396s) is also ~1.4× faster than ARM (555s) with score 1.56 vs 1.57 — a difference of 0.01 that reasonably supports "matches the performance." The critic overlooked this configuration.
- **"Scaling law fits use only a few compute budgets, narrow range"** — REMOVED as a generic complaint. The range covers 6×10^18 to 10^20 FLOPs (two orders of magnitude), consistent with the Chinchilla scaling law methodology. 
- **"MDM FLOPs calculation may need different factor than 6"** — REMOVED as unsubstantiated speculation. The paper uses the standard formula and both models use similar transformer blocks; the critic provides no evidence the factor differs.
- **"Variable-length training could disadvantage ARM baseline"** — REMOVED because the critic themselves acknowledges ARMs "likely do not need it," and the paper applies variable-length training only to MDMs (which need it), not to ARMs.
- **"Temporal degradation: training more steps could explain robustness"** — MOVED to Minor (was listed as a more severe criticism by the critic). The paper explicitly acknowledges the compute difference ("it is worth noting that MDMs require 16× more computation"), so this is a noted confound rather than an oversight.
- **"Missing comparison with continuous diffusion language models"** — REMOVED per instructions (not about missing related works, but the critic noted it as a "missed opportunity" which is beyond scope).
- **"Abstract and Introduction set unrealistic expectations"** — REMOVED as a subjective framing critique that does not identify a factual error.
- **"FLOPs calculation factor of 6 might not apply"** — Already removed above.
- Several pure formatting/style nitpicks removed.

## Novel Insights

The most interesting observation that emerges across the reviews is the finding that MDMs and ARMs show **complementary strengths** across zero-shot tasks (Section 5): the datasets where MDMs outperform ARMs are consistent across both the SlimPajama comparison (Table 2) and the GPT-2 comparison (Table 3). MDMs excel on BoolQ, OpenBookQA, RACE, and LAMBADA, while ARMs excel on ARC-Easy, Hellaswag, PIQA, and SIQA. This suggests the two architectures may capture different types of linguistic structure, pointing toward a deeper architectural insight: the bidirectional nature of MDMs may inherently favor tasks requiring full context integration (e.g., reading comprehension, yes/no questions), while the left-to-right inductive bias of ARMs may better suit tasks involving local commonsense reasoning and next-event prediction. This complementarity, if reproducible at larger scales, could guide model selection for specific task families and potentially inspire hybrid approaches.

## Suggestions

1. **Clarify the reverse curse evaluation protocol.** Explicitly state whether Berglund et al. and Lv et al. also fine-tuned their models on the training statements. If yes, provide a citation to confirm; if no, either run a controlled ARM fine-tuning experiment or rephrase the claim to acknowledge the asymmetric evaluation. This is the most actionable fix and would substantially strengthen the paper's headline contribution.

2. **Report results under a single likelihood evaluation method** (either chain rule or Monte Carlo) as the primary metric, and present per-task selection as a secondary analysis. Report the CFG scale(s) used for zero-shot results.

3. **Acknowledge the loss-bound limitation in the scaling law** and discuss how the gap might differ if true NLL were used. Even a small-scale validation of bound tightness would add credibility.

4. **Include an ablation controlling for training compute in the temporal degradation experiment** (e.g., compare MDM at 1× steps against ARM at 1× and 16× steps) to disentangle architectural robustness from training quantity effects.

## Score and Decision

**Originality:** 7/10 — First scaling law for MDMs and unsupervised CFG are novel contributions; individual components build on existing work.  
**Importance of research question:** 8/10 — Whether diffusion models can scale competitively with ARMs is a timely and impactful question.  
**Claims supported:** 6/10 — Core claims are directionally supported, but the reverse curse comparison, likelihood evaluation protocol, and scaling law quantification all have gaps that weaken the support.  
**Soundness of experiments:** 6/10 — Experiments are broad and well-motivated, but confounds in the reverse curse comparison, likelihood selection, and temporal degradation limit soundness.  
**Clarity of writing:** 7/10 — Well-structured and generally clear, though the CFG mechanism could benefit from more implementation detail.  
**Value to community:** 7/10 — The scaling law, CFG method, and empirical results will be useful to researchers working on discrete diffusion models.

The paper makes genuine, novel contributions — particularly the scaling law analysis and the unsupervised CFG formulation — and provides the most extensive evaluation of MDMs at scale to date. However, several claims are weakened by methodological concerns that the authors can address in revision. The paper does not contain any fatal flaws; the weaknesses are addressable.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>