Now let me synthesize the final review.

**Round 1 bracket:** I bracketed SigMap between weak anchors (scores 2-3, clearly not relevant/"foundation model" papers in other domains that were rejected) and strong anchors (scores 7.5+, completely different topics like LLM alignment). The relevant comparison band was clearly the middle range (3.5-7.5).

**Round 2 narrowing:** Within the 4.5-6.5 range, I compared against EM-GANSim (6.0, Reject — wireless EM simulation, similar missing-baseline issues), URLOST (6.4, Accept — representation learning with MAE, similar technical novelty), and WiMTR (4.0, Reject — WiFi CSI processing). SigMap is clearly stronger than WiMTR (4.0) but has more significant overclaiming issues than EM-GANSim (6.0). SigMap's zero-shot overclaim and undefined NLoS-attention mechanism are more serious than EM-GANSim's missing comparisons. I place SigMap at **5.0**, between WiMTR (4.0) and EM-GANSim (6.0).

Here is the final review:

---

## Summary

SigMap proposes a foundation model for wireless localization with two innovations: (1) cycle-adaptive masked modeling that dynamically adjusts masking patterns based on CSI periodicity to avoid shortcut learning during pre-training, and (2) a "map-as-prompt" framework that encodes 3D geographic information via a GNN into lightweight soft prompts for parameter-efficient cross-scenario fine-tuning. The model is evaluated on simulated ray-tracing benchmarks (DeepMIMO, WAIR-D) for single-BS and multi-BS localization, showing consistent improvements over OMP, CNN, SWiT, and LWLM baselines.

## Strengths

- **Cycle-adaptive masking directly addresses a genuine domain-specific failure mode.** The paper identifies that standard masked autoencoding on periodic CSI data allows the model to exploit periodicity as a reconstruction shortcut. The proposed adaptive masking (Table 3) outperforms grid and strip masking on MAE (0.673 vs 0.770/0.753) and CDF@1m (84.5% vs 80.3%/75.3%), validating that disrupting periodic shortcuts forces more meaningful representation learning. This is a concrete, motivated technical contribution.

- **Geographic prompt tuning yields consistent and non-trivial gains across all settings.** The map-conditioned prompts improve single-BS MAE from 2.275 m (w/o map) to 1.564 m (w/ map) and multi-BS MAE from 0.789 m to 0.673 m. The improvement persists on unseen environments (DeepMIMO O2: 1.026 m vs 1.282 m; WAIR-D: 1.880 m vs 2.578 m), supporting the claim of effective cross-scenario adaptation.

- **Parameter efficiency is well-documented and practically relevant.** Fine-tuning updates only 0.085 M parameters (0.7% of 11.73 M total), completing 1000 epochs in 30 minutes, with inference at 0.83 ms/sample. These numbers (Table 5) support the practical deployability argument.

- **Informative ablation on map modalities.** The comparison of 3D mesh (1.564 m), 2D birdview (1.692 m), and no-map (2.275 m) in Table 4 provides practical insight into where the gains come from, honestly noting that most of the topological benefit is retained without vertical detail.

## Weaknesses

### Major

- **"Zero-shot generalization" is claimed but not evaluated.** The abstract states the model "exhibits strong zero-shot generalization in unseen environments," and Section 1.2 lists "strong zero-shot generalization" as a core contribution. However, Section 4.5 explicitly describes a few-shot setup: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)." No experiment anywhere tests the model with zero labeled samples from the target scenario. This is a mismatch between the headline claim and the actual evidence that would mislead readers about the model's capabilities. The paper itself calls it a "few-shot learning setup" (line 317), making this a clear internal inconsistency.

- **The NLoS-aware attention mechanism (Eq. 11) is introduced without any definition.** Equation (11) appears abruptly in Section 4.2 as "the key advantage" enabling the model to differentiate between direct and reflected paths. The variables $\mathbf{o}_s^{(i)}$, $\phi(\cdot)$, and $\mathbf{W}_{\text{NLoS}}$ are never defined. This mechanism is not described in the methodology section (Section 3), not mentioned in the framework overview (Section 3.1), and is absent from the contributions list. It is unclear whether this is part of SigMap or an independent explanatory device. If it is part of the model, it belongs in the method section; if not, the claim that it explains SigMap's advantage is unsupported.

- **Several SSL-based localization methods cited as related work are omitted from comparisons.** The paper mentions CrowdBERT (Han et al., 2024) and signal-guided masked autoencoders (Wang et al., 2025) as "SSL-based frameworks target[ing] localization more directly" (lines 26-27) and criticizes them for being "confined to specific configurations." Yet neither appears in any comparison table. While SWiT and LWLM are reasonable SSL baselines, the paper claims to address limitations of these specific cited methods without demonstrating improvement over them. This creates an evidential gap.

### Minor

- **Numerical error in the generalization results.** Line 340 states "1.580 m on WAIR-D Scenario-2," but Table 4.5 (line 336) shows 1.880 m for SIGMAP (w/ map) on that scenario. The 44.3% improvement figure is consistent with 1.880 m, not 1.580 m.

- **Parameter-efficiency inconsistency.** Section 4.5 claims "updating only 0.4% of parameters," while Section 4.6 and Table 5 indicate 0.7% (0.085 M / 11.73 M). These differ without explanation.

- **RMSE anomaly in cycle-adaptive masking ablation (Table 3).** Adaptive masking achieves better MAE (0.673) and CDF@1m (84.5%) than strip-masking (0.753, 75.3%), but *worse* RMSE (1.099 vs. 0.972). The paper claims adaptive masking "yields the best trade-off" without discussing this degradation or explaining why it occurs.

- **Evaluation is entirely on simulated ray-tracing data.** All results use DeepMIMO and WAIR-D simulations. For a paper framing its contribution as a "foundation model" with claims of generalizability, the absence of any real-world CSI validation limits the strength of the claims. The paper does not meaningfully acknowledge the simulation-to-reality gap.

### Trivial

- None.

## Nice-to-Haves

- A proper zero-shot experiment (no fine-tuning at all) would either validate or allow removal of the overstated claim in the abstract.
- Reporting standard deviations for the 5-run averages would help assess significance, especially where margins are narrow (e.g., multi-BS CDF@1m: SIGMAP w/o map 77.5% vs. LWLM 75.6%).
- Explaining why strip-masking achieves better RMSE than adaptive masking would strengthen confidence in the approach.
- Providing the transformer backbone specifications (layers, heads, hidden dimension) in the main text rather than deferring entirely to the appendix would aid readability.

## Removed Points

- *"Map-as-prompt contribution is mostly from 2D, not 3D"* — The paper openly reports this ablation (Table 4) showing 2D birdview (1.692 m) vs. 3D mesh (1.564 m) and honestly states "most of the topological benefit is retained even without vertical detail." This is transparent reporting, not a weakness.
- *"Inconsistency in contributions count (two vs. three)"* — A formatting issue, as the abstract highlights "two key innovations" while Section 1.2 lists three, with the third being a property of the approach. This is a presentational choice, not a substantive flaw.
- *"Zero-shot vs. few-shot in generalization table"* — The table itself is labeled as generalization with "minimal fine-tuning," and Section 4.5 honestly calls it a "few-shot learning setup." The problem is specifically that the abstract and contributions section use "zero-shot" language inconsistent with the evaluation.
- *Speculative methodological concerns about Delaunay triangulation over building vertices and base stations* — Not supported by evidence of actual performance degradation.
- *Missing architecture details (transformer dimensions)* — The paper explicitly defers to Appendix B, which is standard practice. The appendix is stripped by the parser.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Remove or substantiate the "zero-shot" claim.** Either add a proper zero-shot experiment (freeze the backbone, evaluate with no target-domain fine-tuning at all) or consistently replace "zero-shot" with "few-shot" throughout the abstract and contributions section. The experiment as presented already supports a strong few-shot generalization claim; overselling it as zero-shot weakens the paper's credibility.
2. **Define Eq. 11 or remove it.** If the NLoS-aware attention mechanism is part of the model, it must be specified in Section 3 with all variables defined. If it is illustrative, remove it to avoid confusion.
3. **Add comparisons with CrowdBERT and Wang et al. (2025).** These are the closest related SSL-based localization methods the paper critiques; their absence from the comparison tables undermines the claim of improvement.
4. **Correct the numerical error** (1.580 → 1.880 on WAIR-D) and reconcile the parameter-efficiency percentages (0.4% vs. 0.7%).
5. **Discuss the RMSE anomaly** in the cycle-adaptive masking ablation (Table 3) to explain why adaptive masking degrades RMSE relative to strip-masking despite improving MAE and CDF@1m.

## Score and Decision

**Round 1 bracketing:** SigMap sits above weak-domain "foundation model" papers scoring 2-3 (PowerGPT, NormWear) and well below strong papers scoring 7.5+ on unrelated topics (LLM alignment). The relevant comparison band is the middle range (3.5-7.5), anchored by Wi-GATr (7.0, Accept) and EM-GANSim (6.0, Reject) in the wireless domain.

**Round 2 narrowing:** Compared against EM-GANSim (6.0), URLOST (6.4), Information Flow in SSL (6.0), and WiMTR (4.0). SigMap is clearly stronger than WiMTR (4.0) which has limited novelty in CSI processing, but has more significant overclaiming and presentation issues than EM-GANSim (6.0), which was rejected. The zero-shot overclaim and undefined Eq. 11 are substantive issues that prevent the paper from reaching the EM-GANSim tier. Score is positioned between these anchors at **5.0**.

**Calibration Anchors:**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| XhdckVyXKg.md (NormWear - wearable foundation model) | 3.0 | 1 | Weaker: less clear technical novelty, broader scope |
| ntSP0bzr8Y.md (PowerGPT - power systems foundation model) | 3.0 | 1 | Weaker: less targeted contribution |
| 9TClCDZXeh.md (Wi-GATr - wireless geometric transformer) | 7.0 | 1 | Stronger: real-world validation, clearer presentation |
| 29JDZxRgPZ.md (EM-GANSim - EM simulation GAN) | 6.0 | 1,2 | Stronger by a modest margin: similar issues but no overclaiming |
| MBBRHDuiwM.md (URLOST - unsup. rep. learning) | 6.4 | 2 | Stronger: cleaner claims, better presentation |
| WfjJOEfAf7.md (Info Flow in SSL) | 6.0 | 2 | Stronger: theoretical contribution despite being reject |
| NRY0QAvGNT.md (AddressVLM - geo-localization) | 5.75 | 2 | Comparable: similar missing-baseline issues |
| q3Wz2TmrhB.md (WiMTR - WiFi mesh regression) | 4.0 | 2 | Weaker: limited novelty in CSI processing |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>