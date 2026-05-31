Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes xLSTM-Mixer, a multivariate time series forecasting model that combines three stages: (1) a shared linear forecast (NLinear) applied independently per variate (time mixing), (2) refinement by sLSTM blocks that stride over variates as tokens (joint mixing of time and variate information), and (3) multi-view mixing that reconciles forecasts from the original and reversed latent embeddings. The method is motivated by the recent resurgence of recurrent models (xLSTM) and draws on mixing strategies from MLP-Mixer and TSMixer. On four standard long-term forecasting benchmarks (Weather, Electricity, Traffic, ETT), the paper reports best results in 18/28 MSE settings and 22/28 MAE settings against 12 baselines, with an ablation study confirming the contribution of each component.

## Strengths

- **Novel multi-view mixing mechanism.** The idea of processing both the original and reversed latent embedding through the same sLSTM stack (weight-sharing) is a clean architectural contribution. The ablation confirms this component improves performance beyond what the sLSTM alone provides, and the weight-tying provides regularization without extra parameters. (Section 3.3, ablation discussion lines 274–279)

- **Systematic ablation evidence.** The paper evaluates ten variants with different combinations of the four key components (time mixing, sLSTM, initial token, multi-view mixing) across two datasets and four horizons. The ablation text reports specific percentage degradations (e.g., "removing the time mixing increases MAE by 3.4% on ETTm1 at length 96"), confirming that all components contribute and that the full configuration is best. (Section 4.2, lines 257–279)

- **Well-motivated variate-order sLSTM processing.** Processing variates as tokens in the sLSTM (rather than time steps) is a deliberate design choice that yields linear scaling in the number of variates — a concrete advantage over quadratic-attention Transformers. The robustness analysis (Figure 5) shows that this design also handles longer lookback windows better than Transformer baselines, supporting the efficiency and scaling claims. (Section 3.2, lines 154–161; Section 4.2, lines 309–313)

- **Interpretability analysis of learned initial tokens.** The qualitative inspection of the learned embedding token $\eta$ (Figure 4) shows that it captures dataset-specific seasonal patterns, providing transparency into the model's internal representations. This goes beyond aggregate metrics and aids understanding. (Section 4.2, lines 288–293)

- **Comprehensive robustness and sensitivity analysis.** The paper tests sensitivity to the hidden dimension (Figure 5) and lookback length (Figure 6), showing consistent improvements with larger capacity and longer context. The lookback analysis includes error bars and comparison to transformer baselines, demonstrating stability. (Section 4.2, lines 305–313)

## Weaknesses

### Fatal
None.

### Major

- **Baseline result provenance is not documented.** The paper lists 12 baselines and reports results in a 28-setting comparison, but the only explicit source note is "[a] Taken from \citet{wuTimesNetTemporal2DVariation2022}" for TimesNet. For the remaining 11 baselines (including xLSTMTime, TimeMixer, iTransformer, PatchTST, etc.), the paper does not state whether these numbers were obtained through a unified re-evaluation with identical lookback length, normalization, and evaluation code, or taken from disparate original papers. The paper states it "follow[s] the established benchmark procedure" of prior work, but this does not clarify the provenance. Since the headline claim ("consistently achieves state-of-the-art") depends on this comparison, the lack of provenance documentation undermines confidence in whether the reported margins reflect genuine architectural superiority or differences in evaluation protocol. This is the most significant barrier to acceptance. (Lines 211–240, Table 2)

### Minor

- **Lookback length is not stated in the main experiment.** Table 2 reports results averaged over prediction horizons {96, 192, 336, 720} but does not specify the lookback length used. The qualitative comparison (line 252) mentions lookback=96 for Figure 1, and the robustness analysis tests varying lookback lengths, but the main table — the paper's central evidence — omits this information. Since models like PatchTST and iTransformer are sensitive to lookback length, this omission reduces reproducibility. (Table 2 caption, lines 223–240)

- **No variance or confidence intervals in the main results.** The primary comparison table (Table 2) reports only point estimates (MSE, MAE) without standard deviations or multi-seed averages. Several wins may be small (e.g., the paper itself notes less competitive performance on Traffic and ETTh2), and without variance information it is impossible to assess whether the reported differences are meaningful. While single-run reporting is common in this literature, the paper's strongest claims would benefit from variance estimates. (Table 2)

- **The multi-view reversal operation could be described more precisely.** The paper states the reversed embedding reverses "the order of the latent dimensions including the representation of $\eta$." This is interpretable as reversing the D-dimensional token vectors (which is how most readers will understand "latent dimensions"), but the description would benefit from a brief clarifying phrase (e.g., "each token's D-dimensional embedding vector is reversed component-wise") to eliminate any ambiguity for implementers. (Section 3.3, lines 169–180)

- **Computational cost relative to baselines is not discussed.** The paper motivates the approach partly by noting the quadratic cost of attention, but never reports runtime, parameter counts, or FLOPs comparisons against the baselines. Given that inference efficiency is part of the stated motivation, this is a notable omission. (Sections 1 and 3)

### Trivial
- The claim that Transformers "typically require large datasets to train successfully" (line 31) is an overgeneralization — many transformer-based forecasting models train effectively on small datasets like ETT — but this is a throwaway line in the introduction and does not affect the paper's contributions.

## Nice-to-Haves

- **Add a second dataset to the hidden-dimension sensitivity analysis** (Figure 5, currently only on Electricity) to check whether the observed trend generalizes.
- **Report parameter counts and wall-clock time** for xLSTM-Mixer vs. the main baselines, especially given the efficiency motivation.
- **The initial token visualization (Figure 4)** is qualitatively interesting but adds limited evidence beyond what the ablation already quantifies. Could be moved to appendix to free space for the ablation table.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"sLSTM does not really jointly mix time and variate — temporal info is only from NLinear."** The sLSTM processes variates as tokens, where each token contains the full time series representation (through the up-projection). The hidden-state recurrence mixes information across variates, and the temporal information is embedded in each token's dimensions. The wording "jointly mix time and variate" is a fair characterization of the overall architecture, not a misleading claim about the sLSTM alone. **Removed** (overstated criticism).

- **"Ambiguity about whether initial token is prepended before or after up-projection."** The paper states $\eta$ is "prepended to each encoded time series $\bm{x}^\text{up}$" (line 163), which unambiguously means after the up-projection. **Removed** (factually incorrect criticism).

- **"Incorrect grouping of TCN, N-BEATS, N-HiTS as joint mixing."** The paper lists these as examples of methods that use joint mixing, in the context of a general discussion about channel independence vs. mixing. This classification is defensible for multivariate implementations and is not central to the paper's contribution. **Removed** (nitpick).

- **"Ablation table not shown in main text."** The table is included via `\include`; it is present in the original submission. The parser strips included content. The paper discusses ablation results in detail (lines 274–279). **Removed** (parser artifact).

- **"Ambiguity about whether this means reversing variate order or hidden dimensions."** The paper says "the order of the *latent dimensions*" (line 170), which specifically refers to the dimensions within each embedding vector, not the variate order. **Removed** (sufficiently clear; only a minor phrasing improvement needed, retained as Minor weakness above).

- **"Initial token visualization (Figure 5) doesn't quantitatively show $\eta$ improves performance beyond ablation."** The figure is presented as qualitative interpretation ("dataset-specific patterns"), not as quantitative evidence. The quantitative evidence is in the ablation. **Removed** (scope-creep).

## Novel Insights

None beyond the paper's own contributions. The reviews converge on a clear pattern: the paper has a well-designed architecture with convincing ablation evidence, but the presentation of the main empirical comparison has documentation gaps that prevent full confidence in the SOTA claim. This is a tension between the paper's careful internal validation (ablation) and its less careful external validation (baseline provenance).

## Suggestions

1. **Document the baseline evaluation protocol.** The single most important improvement: clarify for all 12 baselines whether results were obtained from a unified re-evaluation or cited from prior work. If re-evaluated, describe the protocol (lookback length, codebase, seed count). If cited, clearly label each baseline's source in the table. A small, internally consistent comparison (even on a subset of datasets) would substantially strengthen the SOTA claim.

2. **State the lookback length in the main table caption.** This is a one-line fix (e.g., "All models use a lookback length of 96").

3. **Add variance information.** Report mean and standard deviation over at least 3 seeds for the main results, or at minimum for the datasets where margins are small (Traffic, ETTh2).

4. **Clarify the multi-view reversal.** Add a brief phrase specifying that the D-dimensional embedding vectors are reversed component-wise.

5. **Add a brief runtime or parameter count comparison** to support the efficiency motivation.

6. **Present a compact summary of the ablation table inline** (e.g., a 2×2 table of average ranks or relative MSE changes) so readers can see it without parsing the full table.

## Score and Decision

**Scoring calibration.** Round 1 bracketing: weak anchors (scores 2.5–3.25) correspond to papers with fundamental flaws; strong anchors (scores 7.5–8.0) correspond to exceptionally polished papers with formal proofs or extreme efficiency. The paper clearly sits in the middle bracket (3.5–7.5). Within this, the most comparable anchors are:

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| UniTST | cuFnNExmdq.md | 5.00 | R1 | Similar TS forecasting paper with unified attention; had missing controlled ablation. xLSTM-Mixer has stronger ablation but similar baseline documentation gaps. |
| LRAM | T1pUS4GZZq.md | 5.75 | R1 | Uses xLSTM for decision-making; had missing convergence evidence. Comparable in using xLSTM but different domain. |
| GRformer | lmShn57DRD.md | 4.00 | R1 | Graph-augmented PatchTST; had an unfair baseline comparison (L=96 vs L=336). xLSTM-Mixer is clearly stronger than this. |
| FACTS | dmCGjPFVhF.md | 6.00 | R1/R3 | SSM with formal proofs; had routing linearization gap. xLSTM-Mixer has stronger empirical breadth but lacks formal theory. |
| UniTS | v9Sfo2hMJl.md | 5.67 | R2 | Hybrid forecasting model; had 2.19% hybrid gain issue. Comparable architecture/ablation quality but different central issue. |
| TimeMixer | 7oLshfEIC2.md | 5.67 | R3 | MLP-based multiscale mixing; reported best on all 8 datasets. Stronger empirical results but similar type of contribution. |
| ShuffleMTM | aWkAKucZMR.md | 5.50 | R3 | Self-supervised masking for TS; had novel mechanism but similar evaluative level. |

Round-1 bracket: 4.0–7.5. Round-2/3 narrowing placed the paper between UniTS (5.67) and GRformer (4.00), with closest comparables being TimeMixer (5.67) and ShuffleMTM (5.50). The paper's strongest evidence is the ablation study and the multi-view mixing mechanism; its weakest point is the undocumented baseline provenance, which is a genuine barrier but fixable. I position the paper slightly below TimeMixer (5.67) due to the more complete SOTA coverage in that paper, and slightly above ShuffleMTM (5.50) due to the more thorough ablation and robustness analysis.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>