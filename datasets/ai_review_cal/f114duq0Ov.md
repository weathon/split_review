- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3
Now I have a thorough understanding of the paper and the reviewer inputs. Let me construct the final consolidated review.

---

## Summary

This paper proposes M³-Impute, a mask-guided representation learning method for missing value imputation. It builds on the bipartite graph framework of Grape and introduces three components: (1) a refined initialization that uses observed values and mask information to initialize sample node embeddings, (2) a Feature Correlation Unit (FRU) with learnable soft masking over feature similarities that respects missingness, and (3) a Sample Correlation Unit (SRU) with mutual sample masking and irrelevant feature masking to model sample correlations conditioned on missingness and the target feature. Experiments on 8 datasets under MCAR show the method achieves best or second-best MAE in all cases, with competitive runtime.

## Strengths

1. **Refined initialization that incorporates missingness improves over prior bipartite-graph initialization.** The proposed initialization (Eq. 1) uses the mask vector and observed feature values to initialize sample embeddings, rather than all-one vectors as in Grape. The ablation study (Table 2, "Init Only" vs. Grape) shows this single change yields lower MAE on 7 of 8 datasets (e.g., Yacht: 1.43 vs. 1.46, Energy: 1.35 vs. 1.36, Concrete: 0.74 vs. 0.75). This is a clean, well-motivated improvement.

2. **FRU and SRU provide small but consistent additive improvements on several datasets.** The full model outperforms the "Init Only" variant on 5 of 8 datasets (Yacht: 1.33 vs. 1.43, Housing: 0.59 vs. 0.63, Concrete: 0.71 vs. 0.74, Energy: 1.31 vs. 1.35). While the gains are modest, they demonstrate that the masking schemes provide additional value beyond the initialization.

3. **Competitive runtime.** Table 3 shows GPU inference under 1 second for all eight datasets, with CPU times comparable to Grape (e.g., Yacht: 0.05s CPU; Housing: 0.14s CPU). This is important for practical deployment.

4. **Robustness to hyperparameters and missing ratios.** The method shows stable performance across peer sizes 1–20, epsilon values spanning multiple orders of magnitude (Table 4), and missing ratios from 10%–70% (Figure 2). These experiments support practical usability.

## Weaknesses

### Fatal
None. The paper has a coherent methodology and positive results; no flaw invalidates the core claims entirely.

### Major

1. **The headline quantitative claim is not fully supported by the presented evidence.** The abstract states that the method achieves "20 best and 4 second-best MAE scores on average under three different missingness settings" across 25 datasets. However, the experimental section shows results only for MCAR on 8 datasets (Table 1). The MAR and MNAR results are described in a single unsupported sentence (Section 4.2, line 189): "We observe that M³-Impute consistently outperforms all the baselines under all the eight datasets and achieves an even larger margin in the improvement compared to the case with MCAR setting." No numerical tables, figures, or summary statistics accompany this claim. While the paper may have conducted these experiments, the results of the other 17 datasets and the MAR/MNAR settings are not present in the manuscript, making the "20 best and 4 second-best" claim unverifiable from what is presented.

### Minor

2. **The ablation study shows that the novel FRU and SRU components contribute marginal improvement beyond the refined initialization.** In Table 2, the "Init Only" variant (which only changes the embedding initialization) already achieves competitive results. Adding FRU or SRU individually yields improvements of at most 0.01–0.03 MAE on most datasets. On Wine, Kin8nm, and Power, all variants produce essentially identical scores. The full model does outperform Init Only on several datasets (Yacht: 1.33 vs. 1.43; Housing: 0.59 vs. 0.63; Concrete: 0.71 vs. 0.74), but the gains from the masking schemes themselves are small. The paper frames FRU and SRU as the main novelties, but the evidence suggests the initialization change accounts for most of the improvement over Grape.

3. **No statistical significance testing is reported.** Several comparisons show differences within or near the reported standard deviations (e.g., Energy: M³-Impute 1.31±0.01 vs. HyperImpute 1.32±0.02; Power: 0.99±0.00 vs. Grape 1.00±0.00; Wine: 0.60±0.00 vs. Grape 0.60±0.00). Without significance tests or effect-size analysis, it is unclear whether the small reported improvements reflect genuine advantages or noise from the five random runs.

4. **The missing-ratio robustness analysis (Figure 2) covers only 4 of the 8 datasets** (Yacht, Concrete, Energy, Housing). The other four (Wine, Naval, Kin8nm, Power) are omitted without explanation. While the included datasets show favorable results, the omission weakens the robustness claim.

5. **Baseline coverage omits generative diffusion methods cited in the related work.** The paper cites `diffusion_impute_tabular` and `stable_diffusion` in Section 2 but does not compare against them. While the paper already includes 10 strong baselines (including GAIN, MIWAE, Grape, HyperImpute), the omission of methods from the same family that the paper itself references is a gap.

### Trivial

6. **MAE scores in Table 1 are "enlarged by 10 times"** — this scaling convention is stated in the table caption but is unconventional and could confuse readers. Raw MAE or clearer labeling would be preferable.

7. **The paper notes that Kin8nm and Naval are cases where the method does not lead (or underperforms),** but provides no systematic analysis of when M³-Impute fails. A limitations section discussing failure modes (e.g., datasets with independent features as in Kin8nm) would strengthen the paper.

## Nice-to-Haves

- **Hard-mask vs. soft-mask ablation for FRU.** The paper uses a learned soft mask (σ₁ applied to m_s) but does not compare against a hard mask that uses m_s directly. This experiment would directly validate whether the learnable soft mask is necessary.
- **FRU and SRU applied to a fixed GNN baseline** (e.g., Grape's embeddings) without the modified initialization. This would isolate the contribution of FRU/SRU from that of the initialization unit, which the current ablation confounds.
- **Statistical significance analysis** (e.g., paired tests across datasets or runs) to calibrate whether the small MAE differences are robust.
- **Real-world missing data benchmarks** — while synthetic masks are standard, a dataset with naturally occurring missingness would strengthen practical relevance.

## Removed Points

(Appearing here flagged for reference, removed per filtering rules.)

- **"The paper's central quantitative claim is unsupported by the presented experimental results"** — Partially retained as Weakness #1 but downgraded from "fatal" to "major" since the MCAR evidence on 8 datasets is valid and the claim could be verified if the data exists in a supplementary appendix (which the parser may have stripped). The criticism is about main-paper presentation, not a fatal error.

- **"No code or reproducibility details beyond hyperparameters"** — Removed per hard rules on reproducibility nitpicks. The paper provides key hyperparameters (learning rate, epochs, embedding dimension, architecture details).

- **"GRAPE characterization as not explicitly encoding missingness is somewhat unfair"** — Removed. The paper's characterization is reasonable; GRAPE uses edge presence/absence which is an implicit encoding.

- **"No comparison on datasets with naturally occurring missing values"** — Removed as scope creep. The standard experimental protocol in this area uses synthetic masks.

- **Strength Finder Strength 4 ("State-of-the-art performance across 25 datasets under three missingness mechanisms")** — Removed because it conflicts with verified Weakness #1 (the evidence for this claim is insufficiently presented).

- **Strength Finder's generic praise about problem importance** — Removed as generic/superficial (not specific to this paper's contribution).

- **Criticisms about missing justification for specific design choices (the adaptive α activation, the choice of epsilon vs. learnable placeholder)** — These are reasonable questions but are design analysis, not flaws. Moved to nice-to-have territory.

## Novel Insights

The most notable observation from the reviews is the disconnect between the paper's framing and its evidence: the refined initialization — a relatively simple idea — appears to drive most of the performance gains, while the more complex FRU and SRU masking schemes provide small additive benefits. This suggests that the paper's core contribution could be told more honestly as "a simple initialization change yields meaningful gains over Grape, and two more complex masking modules can squeeze additional small improvements." The current framing overstates the role of the masking schemes.

## Suggestions

1. **Present the MAR and MNAR results** in full (either in the main paper or by clearly referencing an appendix) so the "20 best and 4 second-best" claim can be verified. If the data supports it, the claim is meaningful; if not, adjust the claim accordingly.
2. **Add a targeted ablation** where FRU and SRU are applied on top of Grape's original (all-one) initialization. This would isolate the contribution of the masking schemes from the initialization and either strengthen or clarify the paper's claims.
3. **Add statistical significance tests** (e.g., paired t-tests or Wilcoxon signed-rank tests across the 5 runs) to demonstrate that the small MAE differences are robust.
4. **Add the missing-ratio results for all 8 datasets** to Figure 2, or explain why the omitted datasets were excluded.
5. **Consider a simpler narrative**: frame the refined initialization as a primary contribution and FRU/SRU as supplementary refinements, which better matches the evidence.
