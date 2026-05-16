Now I have all the information I need. Let me compose the final review.

## Summary

This paper identifies three "discordances" between LoRA and privacy-preserving federated learning (FL) — aggregation interference from the semi-quadratic low-rank structure, noise amplification under DP-SGD, and sensitivity to the scaling factor α. To resolve these, the authors propose FFA (Federated Freeze-A LoRA), which freezes the randomly initialized A matrix and trains only the zero-initialized B matrix. The solution is simple, principled, and halves communication costs. Empirical results on RoBERTa (GLUE tasks) and LLaMA-7B (GSM-8K) show FFA consistently outperforms vanilla LoRA across privacy levels, data heterogeneity regimes, and rank budgets.

## Strengths

1. **Clear problem diagnosis with mathematical grounding.** The paper provides explicit mathematical derivations for each of the three discordances (Eq. 4 for aggregation interference, the product-of-noise-terms analysis for DP amplification, and the α-sensitivity discussion). This goes beyond prior work that simply applied LoRA to FL without analyzing root causes.

2. **Simple, principled solution that genuinely addresses the identified problems.** FFA eliminates the aggregation error (Eq. 5 shows exact equivalence to ideal model-averaging), reduces DP noise to a linear term, and removes α-sensitivity (Theorem 1 shows equivalence to LoRA with α → ∞). The solution is both theoretically motivated and practically elegant.

3. **Consistent empirical advantage across diverse experimental conditions.** Tables 1, exp_iid_noniid, roberta_no_DP, and exp_rank_DP span multiple GLUE tasks, three privacy levels (ε ∈ {1,3,6}), three data heterogeneity levels (i.i.d., mild, severe), multiple ranks (r ∈ {2,4,8,16}), and two model families (RoBERTa-Large and LLaMA-7B). FFA outperforms LoRA in the large majority of comparisons, often substantially (e.g., MNLI-matched ε=6: 78.81% vs 39.46%). The results are reported with means and stds over 20 runs.

4. **Computational and communication efficiency.** FFA halves the number of trainable parameters compared to LoRA (Table 3), yielding a direct practical advantage for federated fine-tuning of large models. This benefit is independent of any performance improvements.

## Weaknesses

### Fatal

None.

### Major

1. **Different learning rate ranges for LoRA and FFA are not justified.** The main DP experiments (Table 1) search η ∈ {0.01, 0.02, 0.05, 0.1} for LoRA but η ∈ {0.1, 0.2, 0.5, 1.0} for FFA — an order of magnitude shift with no overlap. The paper provides no justification for why LoRA was not tested at larger rates, nor does it report whether a preliminary search informed this choice. Because different parameterizations (FFA trains one matrix vs. LoRA's two) naturally have different optimal LR scales, the concern is not that different LRs were used per se, but that the paper provides no controlled experiment or scaling argument to establish that the comparison is fair. The dramatic gap on MNLI (39.46% vs 78.81%) could partly reflect LoRA being under-tuned. This is the most significant weakness and weakens confidence in the central empirical claim. *The non-DP ablation experiments partially mitigate this concern by showing FFA advantages in settings where LR ranges are not discussed (and thus likely shared), but the main DP results table should be held to a higher standard of controlled comparison.*

### Minor

2. **Noise amplification analysis (Discordance 2) uses a simplified parameter-level description that omits the η-scaling of the cross-term.** The paper writes the parameters after a DP-SGD update as W₀ + (B + ξ_B)(A + ξ_A), where ξ_B, ξ_A represent noise. This is a legitimate shorthand for the net effect on parameters after an update (ξ = η·gradient_noise). However, the synthetic verification (Figure 1) directly computes the Frobenius norm of the product term ξ_Bξ_A without clarifying whether this is η²-scaled or unscaled, and it compares only this cross-term against full fine-tuning's noise rather than the total noise affecting LoRA. The core insight — that LoRA's semi-quadratic structure creates noise cross-terms absent in linear parameterizations — remains valid, but the analysis is imprecise and the synthetic verification is incomplete. This does not undermine the paper's main claims, since the empirical results stand independently of this theoretical motivation.

3. **The LLaMA-7B experiment is under-reported.** Only a single accuracy number is given (17.12% vs 15.68%) with no details on communication rounds, number of clients, learning rate, data splits, or variance. The computer vision experiment is mentioned in a single sentence without quantitative results. These experiments would be more persuasive with standard experimental detail.

4. **No ablation comparing freezing A vs. freezing B.** The paper freezes the randomly initialized A matrix and trains the zero-initialized B matrix. It does not test the symmetric configuration (freeze B, train A), which would help isolate whether the benefit comes from the specific choice of which matrix is frozen or simply from reducing the number of trainable parameters (and thus noise dimensions). Since zero vs. random initialization is a confound, this ablation would strengthen the paper's analysis of *why* FFA works.

5. **Non-DP ablation experiments do not specify learning rates.** Tables exp_iid_noniid and roberta_no_DP report "best accuracy" but do not state the LR range used. This makes it harder to assess whether the different-LR concern from the DP experiments extends to these tables as well.

### Trivial

- Line 247 has a dangling reference ("\ref{thm_alpha}.") that appears to be a formatting artifact.
- The α-ablation and initialization-ablation sections are very brief and appear to reference results or tables in an appendix that is not present in the main text.

## Nice-to-Haves

- **Privacy composition accounting**: The paper uses Opacus's accountant with the total step count and sampling rate, but in an FL setting with 3 clients doing 10 local steps each over 1000 rounds, the total number of steps is 30,000 (per-client) × 3 (clients) = 90,000. The paper should clarify whether the reported ε refers to per-client privacy or the global guarantee (the text states the stronger setting where each client's update is DP, which would make the reported ε a per-client guarantee).
- **Additional baselines**: While the paper focuses on improving LoRA specifically (which is a defensible scope choice), comparison with other PEFT methods in the DP+FL setting (e.g., adapters, prompt-tuning) would broaden the contribution.

## Removed Points

These points were flagged by reviewers but removed per evaluation guidelines (see meta-reviewer instructions):
- *"Theorem 1 is stated without proof (deferred to appendix)"* — Removed per rule: the appendix exists in the original submission; the parser strips it.
- *"The α-table is not visible in the extracted text (likely in appendix)"* — Removed per rule: appendix content is stripped by the parser; this is not an author error.
- *"FFA uses α=8 'for consistency' but claims it doesn't rely on α — inconsistent"* — Removed: the paper explicitly acknowledges this is for consistency only and that α is not needed for FFA. There is no inconsistency.
- *"Missing comparison with other PEFT methods (adapters, prompt tuning)"* — Removed per rule: the paper scopes itself to improving LoRA. Demanding coverage of other PEFT families is scope creep.
- *"Missing reproducibility details (seeds, client sampling, clipping threshold search)"* — Seeds: standard practice not to list 20 seeds explicitly; client sampling: 3-client cross-silo setting described (all clients used); clipping threshold: grid search over {2,5,10} stated.
- *"The σ=0.99 example for SST-2 needs justification"* — The paper provides the parameters (1000 rounds, 10 local steps, B=200, ε=6, δ=1e-5) and uses Opacus to compute σ. This is standard practice.
- *"The paper's claim about 'best results on fine-tuning LLaMA with GSM-8K' is unverifiable"* — This qualifier ("to the best of our knowledge") is standard academic phrasing; it does not constitute a verifiable claim.
- *"Client-drift argument doesn't formally connect to convergence"* — This is a research paper with theoretical intuition, not a formal convergence analysis paper. The illustrative example is appropriate for the paper's scope.

## Novel Insights

The key insight that emerges from the reviews is that FFA's advantage likely stems from a confluence of factors beyond any single discordance: (1) eliminating the aggregation cross-term, (2) reducing the number of noise-injection dimensions in DP (from 2rk to d·r), (3) removing α as a tunable source of variance. The reviews do not surface an alternative explanation for FFA's consistent empirical advantage — the LR concern suggests the *magnitude* might be overstated but does not explain away the directional consistency across 6 tasks × 4 privacy levels × 4 ranks × the LLaMA experiment. The noise-amplification analysis is the weakest link theoretically, but the empirical results are robust enough to support the paper's practical claims regardless of whether that specific channel is significant.

## Suggestions

1. **Run a controlled LR experiment**: Fix the same learning rate for both methods (e.g., η = 0.1) on at least one task under DP and report results. If this is not possible, provide a principled scaling argument (e.g., η_FFA / η_LoRA ≈ α/r · ‖A‖) that justifies the different ranges.
2. **Clarify the noise analysis**: Explicitly state the η-scaling of the ξ terms when modeling the effect of DP-SGD noise on parameters. The synthetic verification should either compare total noise in LoRA (including all three noise-containing terms) against full fine-tuning, or be presented as an illustrative scaling-law comparison rather than a precise quantitative one.
3. **Expand LLaMA and CV experiments**: Report means and variances, training hyperparameters, and data splits. Even a single additional metric (e.g., perplexity on GSM-8K) would strengthen this section.
4. **Add the freeze-B ablation**: Test FFA-B (freeze B, train A) on at least one task to disentangle the effect of which matrix is frozen from the effect of reducing parameter count.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>