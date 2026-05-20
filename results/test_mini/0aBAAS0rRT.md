Now I have all the verification I need. Let me write the final consolidated review.

## Summary

The paper proposes SigMap, a wireless localization foundation model with two key components: (1) a cycle-adaptive masking strategy for self-supervised pre-training that dynamically adjusts masking to disrupt periodic shortcuts in CSI, and (2) a map-conditioned prompt tuning framework that encodes 3D geographic information into lightweight soft prompts for parameter-efficient cross-scenario adaptation. Experiments on DeepMIMO and WAIR-D benchmarks show consistent improvements over baselines for single-BS and multi-BS localization.

## Strengths

1. **Cycle-adaptive masking is a well-motivated and effective innovation.** The idea of detecting periodicity in CSI via cross-correlation and generating masks that prevent simple interpolation-based reconstruction directly addresses a real limitation of standard masked autoencoding for periodic signals. Table 3 confirms that adaptive masking achieves 0.673 m MAE vs. 0.770 m (grid-only) and 0.753 m (strip-only) in the multi-BS setting.

2. **Geographic prompt tuning is elegantly designed and clearly beneficial.** Encoding 3D building meshes and BS positions into soft prompts via a GNN (Algorithm 1) and prepending them to the frozen transformer is a clean, parameter-efficient approach. Table 1 shows a 31% MAE reduction from prompts (1.564 m vs. 2.275 m without map) with only 0.085 M trainable parameters (0.7% of total), and Table 5 reports 30-minute fine-tuning.

3. **Systematic ablation isolates each contribution.** Tables 3 and 4 independently evaluate masking strategy and map modality. This makes the evidence for each claimed contribution transparent and separable — a strength over papers that only report end-to-end gains.

4. **Cross-scenario generalization results are impressive.** On the unseen DeepMIMO O2 scenario, SigMap achieves 1.026 m MAE, outperforming LWLM by 53.2%, and on WAIR-D Scenario-2 achieves 1.880 m MAE, outperforming LWLM by 44.3% — while updating only 0.4% of parameters. These results demonstrate genuine practical value.

## Weaknesses

### Major

1. **"Zero-shot" claim in abstract contradicts the actual few-shot experimental setup.** The abstract and Section 1.2 claim "strong zero-shot generalization in unseen environments." However, Section 4.5 explicitly states: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario) … This few-shot learning setup." Fine-tuning ~100 labeled target samples is few-shot, not zero-shot. True zero-shot evaluation (no target-domain labels at all) is not presented. This is a structural claim mismatch. The paper itself uses the correct terminology ("few-shot") in the body, making the abstract's "zero-shot" an overclaim that would mislead readers. The authors should either conduct genuine zero-shot experiments or revise the claim consistently.

2. **Numerical inconsistency between text and table.** Section 4.5 states: "SIGMAP reaches … 1.580 m on WAIR-D Scenario-2" but Table 4.5 shows 1.880 m for SIGMAP (w/ map) on WAIR-D Scenario-2 (line 348). This is a factual error that undermines trust in the reported numbers. One of these values is wrong and must be corrected.

3. **No measures of variability reported despite claiming "averaged over 5 independent runs."** No standard deviations, confidence intervals, or individual run values appear in any table (Tables 1–4.5). Many reported margins are modest (e.g., 0.673 vs. 0.789 MAE in Table 2; 0.770 vs. 0.753 vs. 0.673 in Table 3). Without variance estimates, the reader cannot assess whether differences are statistically reliable or within run-to-run noise. This is a significant evidential gap.

### Minor

4. **RMSE inconsistency in the masking ablation is not discussed.** Table 3 shows that strip-masking achieves RMSE of 0.972 m, which is *lower* (better) than adaptive masking's 1.099 m. The paper concludes adaptive masking is "best" based on MAE and CDF@1m but does not acknowledge or explain why RMSE — which penalizes large errors — is worse. This suggests adaptive masking may increase outlier errors, a hypothesis worth investigating. The omission weakens the narrative that adaptive masking is unambiguously superior.

5. **Missing comparisons with directly relevant self-supervised localization methods.** The introduction cites CrowdBERT (Han et al., 2024) and signal-guided MAEs (Wang et al., 2025) as related SSL-based localization approaches, yet neither is included in the baseline comparisons. The paper compares against OMP, CNN, SWiT, and LWLM, but without the most directly relevant prior work, the claim of "state-of-the-art performance" is incompletely supported. At minimum, the paper should explain why these methods were not included (e.g., unavailability of code/data).

6. **NLoS-aware attention mechanism (Eq. 11) is introduced but never separately ablated.** This mechanism appears in Section 4.2 alongside results but is never evaluated on its own. Without ablation, its contribution to the reported gains is unknown — the improvement could come entirely from masking and prompt tuning.

7. **All experiments are on simulated data.** DeepMIMO and WAIR-D are ray-traced simulations. The paper frames itself as targeting practical deployment but does not evaluate on real-world CSI, where hardware impairments, dynamic obstacles, and imperfect maps are significant challenges. This is a limitation that should be explicitly discussed (the paper has no limitations section).

### Trivial

8. The radar chart in Figure 5 has a metric labeled "oss_scenario" — likely a typo for "cross_scenario" or similar.

## Nice-to-Haves

- Compare full fine-tuning of the backbone against prompt tuning to substantiate the parameter-efficiency claim beyond raw parameter count.
- Include qualitative error maps showing when map prompts help or fail.
- Report computational overhead of ray-tracing for map generation, since the method relies on 3D maps that may not always be available.
- Discuss scenarios where 3D maps are incomplete, inaccurate, or outdated.

## Removed Points

These points from the reviewers are removed with justification:

- **"Pre-train typo in Table 5" (Harsh Critic):** The term "Pre-train" is a standard abbreviation for "pre-training." Not a typo.
- **"Cycle-adaptive masking underspecified, no algorithm for periodicity detection" (Harsh Critic):** While the description could be more detailed, Algorithm 1 is provided for geographic prompt generation, and Eq. (6) defines the mask pattern. The periodicity detection via cross-correlation is described in prose (Section 3.3). An explicit pseudocode would be a nice addition but is not missing to the point of being a weakness.
- **"Missing appendix content" (Harsh Critic):** The appendix is stripped by the PDF parser; the original submission contains it. This is an artifact of the review format, not an author omission.
- **"Weakness about unfair comparison where asymmetry favors baseline" (from rules):** Not applicable — the baselines are not disadvantaged.
- **"Strengths about 'zero-shot generalization'" (Strength Finder):** This strength is removed because it is factually inaccurate — the experiments are few-shot, not zero-shot, as discussed in Weakness 1.
- **"Strength about 'importance of the problem'" (from rules):** Generic strength. The paper's actual methodological strengths are concrete enough that generic framing adds nothing.
- **"Strength about 'addressed an important problem'" (from rules):** Generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful observation about the RMSE/MAE trade-off in the masking ablation that the paper itself overlooked, and the reviewer notes that geographic prompt tuning retains most of its benefit even with 2-D maps (suggesting height information contributes less than claimed). Neither contradicts the paper's contribution but both point to nuances the authors should address.

## Suggestions

1. **Fix the zero-shot/few-shot inconsistency immediately.** Either add a genuine zero-shot evaluation (no target-domain fine-tuning) or change all instances of "zero-shot" to "few-shot" / "few-shot adaptation." This is the single most important correction.
2. **Resolve the text/table numerical discrepancy for WAIR-D (1.580 vs. 1.880) and check all other numbers for consistency.**
3. **Add standard deviations (or other variance measures) to all tables reporting averages over 5 runs.** Without these, the headline comparisons cannot be properly assessed.
4. **Acknowledge and discuss the RMSE behavior in Table 3.** Explain why adaptive masking produces worse RMSE than strip-masking despite better MAE.
5. **Add a limitations paragraph** covering simulated-only evaluation, map availability/quality assumptions, and the scope of claimed generalization.
6. **Include the most relevant self-supervised baselines** (CrowdBERT, signal-guided MAE) or provide a clear rationale for their exclusion.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|--------------------------|
| v6byS5Dypp.md (EMind) | 3.33 | R1 | Weaker — electromagnetic signals foundation model with less targeted evaluation |
| YY40r8c9U0.md (CAT) | 3.00 | R1 | Weaker — channel equalization, different task |
| D4CH3hCNdb.md (FGNO) | 3.00 | R1 | Weaker — time-series SSL |
| MUnHOkaEFC.md (Open-Set RFFI) | 3.33 | R1 | Weaker — different wireless task |
| **3AbyfpQgR2.md (AEMP)** | **5.33** | **R1/R2** | **Most similar — self-supervised CSI localization. SigMap has stronger methodology but has claim inflation and numerical errors that AEMP does not. SigMap is slightly weaker overall.** |
| N5gNhO2OPB.md (PRLS-RFF) | 4.00 | R1 | Weaker — RF fingerprinting, narrower scope |
| DmCof7cMTc.md (GRF-LLM) | 4.00 | R1 | Weaker — channel modeling, not localization |
| 0izu8IWJ5z.md (nGRF) | 4.00 | R1 | Weaker — channel estimation |
| **RKDkqkkZ5m.md (TS-DDAE)** | **4.67** | **R2** | **Wireless signal pre-training. SigMap has stronger novelty but TS-DDAE has fewer claim inconsistencies. SigMap is slightly stronger.** |
| RXaoGgjrFs.md (SlotFM) | 6.00 | R2 | Different domain (accelerometers); less relevant |
| kkBOIsrCXh.md (NavFoM) | 8.00 | R1 | Much stronger — full embodied navigation foundation model |
| oBXfPyi47m.md (Efficient RL) | 8.00 | R1 | Much stronger — RL with extensive offline data |

**Round 1 bracket:** Between 3.5 and 7.5, narrowing to 4–6 based on the most similar anchor (AEMP at 5.33).

**Round 2 narrowing:** SigMap is stronger than TS-DDAE (4.67) in methodological novelty and evaluation breadth, but weaker than AEMP (5.33) due to the zero-shot claim mismatch and numerical error — issues that AEMP does not have. This places SigMap between the two, at approximately 5.0.

**Final score:** 5.0. The core methodology is solid and the results support the technical contributions, but the claim inflation ("zero-shot" vs. actual few-shot setup), the numerical inconsistency, and the lack of variability reporting are substantive flaws that must be corrected before the paper meets the acceptance bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>