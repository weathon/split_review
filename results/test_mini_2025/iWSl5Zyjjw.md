Now I have all the information needed to write the final consolidated review. Let me compile it.

## Summary
2-3 sentence summary of the paper's contribution.

The paper identifies and quantifies Mamba's limited length extrapolation capability, attributing it to a restricted effective receptive field (ERF) tied to the sum of Δ_t values exceeding training-length bounds. To address this, the authors propose DeciMamba, a token-decimation strategy that uses Δ_t as an importance score to discard unimportant tokens before the S6 layer, enabling extrapolation to much longer sequences (up to 128K on passkey retrieval from 2K training) without full retraining and with a ~2× inference speedup.

## Strengths

- **Novel diagnosis of Mamba's length extrapolation failure via the Mamba Mean Distance metric.** The paper introduces a quantitative measure (Eq. 8) that concretely demonstrates that Mamba's effective context utilization collapses as evaluation length exceeds training length (Fig. 5). The analytical link connecting the product of transition matrices to exp(A·ΣΔ_k) (Eq. 9) provides a clean, mechanistic explanation for why the ERF is bounded — this goes beyond anecdotal observation.

- **Δ_t-based token decimation is a simple, well-motivated, and demonstrably effective solution.** The method is grounded in the recurrent dynamics of Mamba (Eq. 10): Δ_t naturally controls how much each token affects the hidden state. The evidence is strong and multi-faceted: on Passkey Retrieval (Fig. 1, right), Mamba-130M fails above 16K while DeciMamba maintains near-perfect accuracy up to 128K; on LongBench (Table 1), DeciMamba improves the 2.8B model's TriviaQA score from 3.93 to 12.61 (220% gain). Ablations (Fig. 7) confirm Δ_t-based pooling outperforms random and max-norm alternatives.

- **Inference speed improvement alongside context extension.** Table 3 reports that DeciMamba-130M is ~2× faster than the baseline Mamba at every context length (e.g., 0.31s vs. 0.69s at 32K). This is a practical advantage that distinguishes DeciMamba from most context-extension methods, which typically add overhead.

- **Comprehensive evaluation across multiple challenging tasks.** The paper tests DeciMamba on LongBench (16 tasks, zero-shot), Passkey Retrieval (up to 128K), Document Retrieval (up to 160 documents), Multi-Document QA, and PG-19 language modeling (both zero-shot and fine-tuned). The consistent pattern of improvement across diverse settings makes the contribution robust.

- **Zero-shot generalization is demonstrated with larger models.** DeciMamba improves perplexity on PG-19 for 1.4B and 2.8B models with no additional training (Fig. 6, right) and boosts zero-shot LongBench scores (Table 1). This shows the Δ_t importance signal transfers from pretrained weights without any task-specific tuning.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence presented.

### Minor

- **Ambiguity in the "no need to re-train the model" claim.** Section 4 states: "we propose embedding a filtering mechanism within the pre-trained Mamba layers, **with no need to re-train the model**." This is accurate for the zero-shot experiments (LongBench, PG-19 zero-shot). However, the passkey retrieval, document retrieval, and PG-19 fine-tuning experiments all involve training with DeciMamba enabled. The paper does distinguish these settings in the experiment descriptions, but the framing in Section 4 is broader than what the zero-shot results alone cover. The authors should clarify that DeciMamba can be applied (a) zero-shot to pre-trained models or (b) integrated during training for larger gains, rather than implying no training is ever needed.

- **No variance or confidence intervals reported.** Tables 1, 2, and 3 report only point estimates. Given the variability inherent in LLM evaluations — especially for LongBench tasks where some scores are very low (e.g., TREC at 0.5) — it is difficult to assess whether reported improvements are statistically stable. This is a standard concern in the field but worth noting.

- **Hyperparameter sensitivity acknowledged but practical guidance limited.** The ablation in Fig. 7 (left) shows that the choice of first decimating layer critically affects passkey retrieval (success drops from ~1.0 at layer 12 to ~0.55 at layer 20), and the method introduces β, L_base, and layer-selection hyperparameters. While the paper provides ablations, it does not offer practical heuristics for selecting these hyperparameters for a new model or task without running ablations.

### Trivial
None.

## Nice-to-Haves

- A comparison with a simple baseline that is directly applicable to Mamba (e.g., truncating to the last L_train tokens, or scaling Δ_t values uniformly) would strengthen the positioning of DeciMamba's specific design choices.
- Reporting the computational cost of the Δ_t computation and top-P selection (even though it is claimed to be negligible) would be useful for practitioners.

## Removed Points

These points were raised by reviewers but are removed from the main review for the reasons stated below:

1. **"Hyperparameter selection for zero-shot LongBench experiments is not adequately specified"** — This criticism questions whether hyperparameters were tuned on LongBench data. The paper states hyperparameter details are in Appendix C (which is stripped by the parser, per parsing pipeline rules). The ablation studies in the main paper (Fig. 7) and the explicit reference to Appendix C for hyperparameter selection strategy make this concern speculative rather than grounded in what is on the page. **Reason: Removed per "REMOVE weaknesses about missing appendix" rule and "A weakness only counts as fundamental if it is verifiable from the paper as written — not from speculation" rule.**

2. **"The extrapolation claim is undercut by zero-shot PG-19 results showing Mamba itself extrapolates"** — The paper's Fig. 6 (right) shows that Mamba-1.4B and Mamba-2.8B have some extrapolation but degrade sharply after ~30K, while DeciMamba remains flat. The paper does not claim Mamba has zero extrapolation ability; it claims limited ERF, which is consistent with the data. The honest presentation of baseline performance is a strength, not a weakness. **Reason: Removed as factually consistent with the paper's claims — the criticism misreads the paper's characterization.**

3. **"Missing comparison with other context-extension methods"** — The paper explicitly scopes itself as focusing on Mamba-specific context extension (Sec. 2), and claims to be the first such method for Mamba. Comparing with Transformer-specific methods (LongLora, Landmark Attention) would be scope creep. The suggested "simple windowed SSM or depth-based interpolation of Δ_t" are not established baselines in the literature. **Reason: Scope creep / the criticisms demand methods outside the paper's stated scope.**

4. **"The paper does not compare against any Mamba-specific prior work"** — The paper explicitly claims to be the first context-extension method for Mamba. If concurrent work exists (e.g., MambaExtend), it is not the paper's fault for not comparing against unreleased concurrent work. **Reason: Cannot penalize for not comparing against concurrent work.**

5. **Strongth Finder's generic or sycophantic strengths** (e.g., "addressed an important problem," "well-written") — Removed as generic/superficial. Only strengths grounded in specific evidence are retained.

## Novel Insights

The reviews surface an interesting tension that the paper itself does not fully explore: DeciMamba's method applies Δ_t-based decimation at inference time (pre-fill phase only) and also works during training, but the paper does not disambiguate how much of the gain in the training-based experiments comes from the architectural inductive bias of decimation vs. the simple fact that training with shorter effective sequences (due to decimation) allows the model to attend better to remaining tokens. The observation that Mamba-2.8B already has non-trivial zero-shot extrapolation (Fig. 6 right) while Mamba-130M collapses (Fig. 6 left) suggests the ERF limitation is itself scale-dependent — larger Mamba models may learn more robust Δ_t distributions that generalize better, and DeciMamba's benefit may be most critical for smaller models. This scaling property is acknowledged in the data but not discussed as a finding.

## Suggestions

1. Clarify the "no retraining" framing in Section 4: distinguish between (a) plug-and-play zero-shot application to any pre-trained Mamba and (b) training with DeciMamba as a component. Use separate terminology for each regime.
2. Add error bars or confidence intervals to the key tables (at least Table 1 and 2) to increase confidence in the reported improvements.
3. Provide a brief practical guide for setting β, L_base, and decimation-layer choice as a function of model size and target context length.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Sparse Mamba | vOfDGYGVyj.md | 2.50 | 1 (weak) | Different problem (controllability in SSMs), far weaker empirical support |
| Multimodal Instruction Tuning with Hybrid SSMs | cagNCwQEEN.md | 3.40 | 1 (weak) | Different domain (multimodal), weaker |
| Mamba-HMIL | 0yVP49SDg0.md | 3.25 | 1 (weak) | Medical imaging domain, weaker |
| **MambaExtend** | **LgzRo1RpLS.md** | **6.25** | **1 (middle), 2** | **Most directly comparable — same problem, accepted as poster. DeciMamba has more comprehensive evaluation, novel ERF analysis, and inference speedup, making it stronger.** |
| Samba | bIlnpVM4bc.md | 6.67 | 1 (middle), 2 | Different contribution (new hybrid architecture trained at scale); DeciMamba is less architecturally ambitious but has cleaner analysis |
| Mamba (original) | AL1fq05o7H.md | 6.25 | 1 (middle), 2 | Original architecture paper, rejected due to one low score. DeciMamba is more focused and has stronger empirical support for its specific claims |
| Unleashing Mamba in VLMs | 0A6f1b66pE.md | 4.60 | 1 (middle) | Vision-language domain, withdrawn, weaker |
| Compressed Context Memory | 64kSvC4iPg.md | 5.75 | 2 | Different problem (KV compression for Transformers), accepted as poster. DeciMamba has stronger results for its problem |
| Learning Mamba as Continual Learner | 1TXDtnDIsV.md | 4.67 | 2 | Different problem (continual learning), rejected |
| Scaling Laws of RoPE-based Extrapolation | JO7k0SJ5V6.md | 8.00 | 1 (strong) | Different architecture (Transformer RoPE), requires different evaluation standard |
| Unlocking State-Tracking | UvTo3tVBk2.md | 8.00 | 1 (strong) | Different problem (negative eigenvalues in LRNNs), oral-level contribution |

**Round 1 bracket:** 5.0–7.0 (clearly above weak anchors <3.5, clearly below strong anchors >7.5 which address different problems or require architectural/training advances at a different scale).

**Round 2 narrowing:** Compared to MambaExtend (6.25, accepted as poster) — the most directly comparable paper — DeciMamba offers: (a) a more thorough analysis of the problem (Mamba Mean Distance, ΣΔ_t divergence), (b) more comprehensive evaluation (LongBench with 16 tasks vs. MambaExtend's limited Pile/PG-19, plus Document Retrieval and QA), (c) an inference speed advantage (~2×), and (d) both zero-shot and training-based results. MambaExtend's main advantage is cleaner scope (purely training-free calibration of Δ_t scaling). DeciMamba is stronger empirically. The Samba paper (6.67) involved a new hybrid architecture trained at 3.8B scale — a different and more ambitious contribution type.

DeciMamba sits between MambaExtend (6.25) and Samba (6.67) in quality — stronger empirical package than MambaExtend but not as architecturally novel as Samba. The minor clarity issues around the "no retraining" claim and missing variance reporting prevent it from reaching the 7+ range.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>