Now let me write the final consolidated review.

## Summary

SigMap proposes a multimodal foundation model for wireless localization with two innovations: (1) a **cycle-adaptive masking** strategy for self-supervised pre-training that dynamically disrupts periodic patterns in CSI to prevent shortcut learning, and (2) a **map-as-prompt** framework that encodes 3D building geometry via Delaunay triangulation and a GCN, then injects the result as a soft prompt token into a frozen Transformer backbone for parameter-efficient cross-scenario adaptation. The model is evaluated on DeepMIMO and WAIR-D datasets against OMP, CNN, SWiT, and LWLM baselines.

## Strengths

- **Cycle-adaptive masking demonstrably outperforms fixed masking strategies.** Table 3 provides clean causal evidence: adaptive masking achieves 0.673m MAE versus 0.770m (grid) and 0.753m (strip), a 10.6–12.6% reduction. The core idea — that periodic CSI patterns let standard MAE models exploit local shortcuts — is well-motivated and supported by the experiment.

- **Map-as-prompt framework with cleanly isolated geographic contribution.** The GNN-based encoding of 3D building geometry into a soft prompt token (Algorithm 1) is architecturally novel for this domain. Table 4 provides a clean three-way ablation: 3-D map (1.564m MAE) → 2-D bird's-eye (1.692m, +8%) → no map (2.275m, +45% relative to 3-D). The large jump from no-map to 2-D confirms that topological/LoS constraints are the primary driver, which the paper correctly acknowledges.

- **Strong zero-shot generalization with parameter efficiency.** On unseen DeepMIMO O2, SIGMAP (w/ map) achieves 1.026m MAE vs. LWLM's 2.213m (53.6% improvement); on WAIR-D, 1.880m vs. 3.375m (44.3% improvement). Fine-tuning updates only 0.085M parameters (≈0.7% of total) and completes in 30 minutes (Table 5). This demonstrates genuine practical value for real-world deployment where labeled data is scarce.

- **Systematic multi-BS fusion with interpretable attention.** The attention-based fusion mechanism (Eqs. 9–10) dynamically weights contributions from each base station. Table 2 shows multi-BS SIGMAP (w/ map) achieves 0.673m MAE and 84.5% CDF@1m, improving on the no-map variant by 14.7%, indicating the fusion mechanism effectively leverages geographic prompts.

## Weaknesses

### Major

1. **Headline claims conflate method contribution with map modality.** The paper's central SOTA claim ("outperforming the best baseline by 34.4%") compares SIGMAP (w/ map) against LWLM, which does not use map information. The fair comparison — SIGMAP (w/o map) vs. LWLM — shows only a 4.5% improvement in single-BS MAE (2.275 vs. 2.382 m, Table 1). While the paper does provide both (w/ map) and (w/o map) results, the narrative framing does not cleanly separate the two contributions. The reader cannot tell from the headline whether the cycle-adaptive masking + Transformer backbone is itself competitive, or whether all gains come from the map modality. The paper needs to either (a) include baselines that also use map information, or (b) clearly separate claims into "method improvement" and "multimodal fusion improvement."

2. **Missing directly relevant SSL baselines.** The related work section discusses CrowdBERT (Han et al., 2024), WirelessGPT (Yang et al., 2025), and signal-guided masked autoencoders (Wang et al., 2025) — the most directly comparable SSL-based approaches. None appear in the experimental section. Only LWLM, SWiT, CNN, and OMP are compared. Excluding these while claiming SOTA creates a gap between narrative and evidence. The paper should either include them or explain why they cannot be compared (e.g., incompatible task setup).

3. **No variance or uncertainty reported for any result.** The paper states results are "averaged over 5 independent runs" (line 239) but no table reports standard deviations or confidence intervals. This is critical because the small margins between SIGMAP (w/o map) and LWLM (~4.5% MAE in single-BS) may not be statistically significant. Without variance information, the quantitative comparison is incomplete.

4. **NLoS-aware attention mechanism (Eq. 11) appears first in the results section** without being described in the methodology (Section 3). Equation (11) is introduced at line 248 as the "key advantage" of the method, but this attention variant over LoS/NLoS path embeddings is never mentioned in Section 3. If it is part of the model architecture, it must be described in the methodology; if it is a post-hoc analysis tool, it should be presented as such.

### Minor

5. **Cycle-adaptive masking is under-specified.** The mask Equation (6) depends on a detected periodicity shift `d_final`, but the paper does not describe how `d_final` is computed. The text mentions "computing row-wise cross-correlation" and "detect dominant periodicities" but no algorithm, formal definition, or critical hyperparameters (e.g., what counts as "dominant") are given. This component is the first named contribution and is not reproducible as written.

6. **Numerical inconsistencies.** (a) WAIR-D Scenario-2 MAE: Table at line 336 reports 1.880m, but line 340 says 1.580m. These differ by 19%. (b) Parameter efficiency: line 340 says "0.4% of parameters" while line 352 says "0.7%" (0.085M/11.730M ≈ 0.72%, confirming the latter). (c) The generalization table is referred to as "Table 4.5" (line 317), an apparent section-label leak. These inconsistencies undermine confidence in reporting precision.

7. **Strip masking achieves lower RMSE than adaptive masking, creating an undisclosed trade-off.** Table 3 shows strip-masking achieves RMSE = 0.972m vs. adaptive's 1.099m, meaning strip produces smaller worst-case errors. The paper claims adaptive masking yields "the best trade-off" without discussing this trade-off or explaining why adaptive's RMSE is worse.

8. **Generalization evaluation uses an incomplete baseline set.** Only LWLM and SIGMAP (w/o map) are compared on the generalization tasks (Section 4.5). SWiT (the contrastive learning method) and CNN from the main tables are dropped without explanation. It is also unclear whether LWLM was pre-trained on the same data and fine-tuned on the same 100 samples.

### Trivial

9. **The phrase "existing self-supervised approaches employ generic masking strategies that ignore inherent cyclic patterns"** (Section 1.1) implicitly claims no prior work addresses signal periodicity. This should be verified against the cited LWM, CrowdBERT, and signal-guided MAE papers, which may have their own periodicity handling.
10. **"Table 4.5"** label leak (line 317) is a minor formatting issue.

## Nice-to-Haves

- **Provide a clear algorithm for periodicity detection** (how `d_final` is computed). Even a simple algorithm (e.g., compute autocorrelation along frequency axis, pick lag with maximum response outside a neighborhood) would suffice to make the contribution reproducible.
- **Include standard deviations or error bars** for all main results.
- **Discuss why the 2-D bird's-eye map retains most of the benefit** — the current discussion acknowledges it but could go deeper on why vertical detail matters so little for this task and dataset. This could strengthen the contribution by clarifying when 3D maps are genuinely needed vs. when 2D is sufficient.
- **Clarify the generalization protocol for baselines**: were they pre-trained on the same data and fine-tuned on the same 100 samples?
- The single-pooled prompt token is a notable design choice. A brief discussion of why this was chosen over multi-token or per-building prompts would help readers assess the design space.

## Removed Points

These points were considered but removed from the main weaknesses:

- *"3D Delaunay triangulation over thousands of vertices could be computationally prohibitive"* — speculative; no evidence in the paper that this is actually a bottleneck, and the fine-tuning time (30 min) reported in Table 5 suggests it is not.
- *"2-D vs 3-D finding undermines the paper's emphasis on 3D geometric richness"* — the paper already acknowledges this finding honestly (line 301: "most of the topological benefit is retained even without vertical detail") and frames it constructively as an "immediate upgrade path."
- *"GlobalMeanPool into a single prompt token limits expressivity"* — this is a design choice that could be discussed, but the critic's specific concern about occlusion awareness is speculative. Moved to Nice-to-Haves.
- *Strengths that are generic or superficial* (e.g., "the problem is important") from the Strength Finder have been dropped. Only evidence-grounded strengths are retained above.

## Novel Insights

The most interesting finding not fully emphasized by the paper is that the 2-D bird's-eye map achieves 92% of the performance improvement of the full 3-D mesh (MAE 1.692 vs. 1.564m), while being dramatically simpler to obtain (street-level photographs could suffice). This suggests that the primary value of geometric prompts is not in fine-grained 3D structure but in coarse topological constraints (which buildings block which lines of sight). This insight could redirect future work toward cheaper-to-acquire map representations rather than expensive 3D meshes — a practical implication the paper touches on but could amplify.

## Suggestions

1. **Disentangle the two contributions clearly** in both narrative and results. Present SIGMAP (w/o map) vs. all baselines as the evaluation of the method architecture and pre-training strategy, and frame the map prompt as a separate multimodal fusion contribution.
2. **Specify the periodicity detection algorithm** for `d_final`. Provide pseudocode or a clear formal description.
3. **Resolve the numerical inconsistencies** — particularly the 1.580 vs. 1.880 WAIR-D MAE mismatch.
4. **Add standard deviations** to all tables, or at minimum a note on statistical significance for the comparisons with small margins.
5. **Either include the SSL baselines** cited in related work or explain why they cannot be compared.
6. **Move the NLoS-aware attention (Eq. 11) to Section 3** if it is part of the model architecture, and describe its role clearly.

## Score and Decision

**Calibration procedure:**

*Round 1 (bracketing)* — Searched the human-review corpus across five score bands. Strong reject anchors (score < 2.5): papers with incoherent contributions or fatal evaluation issues. Weak anchors (2.5–4.5): communications/sensing papers with solid ideas but significant gaps in evaluation or presentation (e.g., *Variational Diffusion Channel Decoding* at 3.00, *WiFi Mesh Regression* at 4.00). Middle anchors (4.5–6.1): papers with clear contributions but nontrivial weaknesses (e.g., *Lightweight Pre-trained Transformers for RS Timeseries* at 4.75, *SensorLLM* at 5.50). Strong anchors (6.0–7.5): well-supported papers with minor weaknesses (e.g., *Differentiable Wireless Simulation* at 7.00). Top anchors (7.5+): outstanding papers. Initial bracket: [3.5, 5.5].

*Round 2 (narrowing)* — Searched inside (3.0, 5.0) and (4.5, 6.5). Compared against *Presto* (4.75): both papers have domain-specific SSL, incomplete baseline comparisons, and limited performance gains over simpler methods — similar in scope and severity of issues. Compared against *SensorLLM* (5.50): SensorLLM has more fundamental questions about architectural necessity; SigMap's contributions are better justified but have more reporting issues (numerical inconsistencies, under-specified components). Round-2 bracket: [4.0, 5.0].

*Anchors consulted:* 
1. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/YHDY5uXOSN.md` — avg 3.00, wireless communication paper with presentation gaps and missing baselines → SigMap is notably stronger (clearer contributions, better evaluation) 
2. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/q3WzT2mrhB.md` — avg 4.00, WiFi mesh estimation with incomplete evaluation → SigMap is slightly stronger 
3. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Iip7rt9UL3.md` — avg 4.75, Presto remote sensing SSL with missing baselines and small gains → SigMap is comparable  
4. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/cDd7kg9mkP.md` — avg 5.50, SensorLLM with clarity about architectural value → SigMap has better-justified contributions but more reporting issues → slightly weaker
5. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9TClCDZXeh.md` — avg 7.00, Wi-GATr wireless simulation with strong evaluation → SigMap is notably weaker (incomplete baselines, under-specified method)

The paper's core ideas are genuinely novel for the domain (cycle-adaptive masking, map-as-prompt) and the ablation studies cleanly isolate each contribution. However, the evaluation has clear gaps: the headline claim conflates two separate contributions, relevant SSL baselines are absent, no variance is reported, and critical method components (periodicity detection, NLoS attention) are under-specified or misplaced. These are fixable issues, but in the current form the evidence does not fully support the stated claims. Score is positioned at the lower end of the round-2 bracket, comparable to Presto (4.75) but lower due to the numerical inconsistencies.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>