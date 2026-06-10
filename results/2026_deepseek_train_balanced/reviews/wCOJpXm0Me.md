**Final Review**

## Summary
This empirical analysis paper proposes the Alignment Hypothesis: the cosine similarity between an image and its class-label text embedding in a pretrained CLIP model predicts final DG accuracy even after source fine-tuning. The authors compare this to the Image Similarity Hypothesis (perceptual similarity to pretraining data), finding alignment to be more predictive. Using this insight, they split five DomainBed datasets into In-Pretraining (IP) and Out-of-Pretraining (OOP) subsets and benchmark ten DG methods. The key finding is that all methods perform well on IP data (sometimes beating an oracle) but struggle on OOP data, with recent methods offering little improvement over older methods on the OOP subset.

## Strengths
1. **The IP/OOP diagnostic framework is a practical and conceptually clean tool.** Splitting evaluation data by pretraining alignment reveals an important asymmetry that standard leaderboard aggregation obscures: CLIPood achieves 84.7% on DomainBed-IP but drops to 57.1% on DomainBed-OOP, while MIRO+MPA matches it on OOP (57.2%) despite being 2% worse overall. This reframes leaderboard progress and is a genuinely useful lens for the community. The release of these splits is a concrete contribution.

2. **DG methods outperforming an oracle on IP data but failing badly on OOP data is a striking diagnostic finding.** On three of five IP datasets (DomainNet, OfficeHome, PACS), the best DG method exceeds a target-trained oracle, while on TerraIncognita-OOP the best method scores only 24.9% versus an oracle of 83.2% (Table 1, lines 194–218). This asymmetry provides strong evidence that current methods exploit pretraining alignment rather than learning genuinely generalizable features.

3. **Systematic data cleaning addresses known confounds.** The paper identifies and removes mislabeled samples at low AlignmentScores (e.g., VLCS loses 12.41%) and OCR-based shortcuts at high AlignmentScores (Table lines 109–124). This methodological care ensures the IP/OOP split reflects alignment differences rather than label noise.

## Weaknesses

### Major

1. **The central comparison between the Alignment Hypothesis and the Image Similarity Hypothesis lacks quantitative rigor.** The paper's key theoretical claim — that AlignmentScore predicts DG performance "significantly more strongly" than PerceptualSimilarityScore (line 81) — rests entirely on visual inspection of binned-accuracy plots in Figure 2 using a single method (VL2V-SD). No correlation coefficient (Pearson, Spearman), R², binned AUC, or any other quantitative measure is reported for either hypothesis. The PerceptualSimilarity plot in Figure 2b also shows a visible positive trend, so the reader cannot assess whether the difference is large, moderate, or marginal. For an empirical analysis paper whose contributions are diagnostic rather than a new method, this is a significant evidential gap.

2. **The same backbone is used for both defining the IP/OOP splits and for initializing/training all DG methods.** The paper states this explicitly (line 93: "we use the same backbone both for splitting the datasets into IP and OOP subsets and for training DG methods") but does not discuss why this is appropriate or what limitations it imposes. The OOP samples are, by construction, those where the backbone's image-text alignment is weak. From such a starting point, any method initialized with that backbone would be expected to struggle on those samples. This conflates "hard for this backbone" with "hard for DG methods generally." Decoupling the splitting backbone from the training backbone would substantially strengthen the diagnostic interpretation.

3. **The Alignment Hypothesis is verified using only a single DG method (VL2V-SD).** The comparison between AlignmentScore and PerceptualSimilarityScore in Figure 2 (lines 70, 81) is conducted solely on VL2V-SD. Different DG methods have different mechanisms — MIRO regularizes feature representations toward the pretrained model, SWAD averages weights, CLIPood regularizes both weights and outputs. It is plausible that the Alignment Hypothesis holds more strongly for some methods than others. Without testing at least ERM and one other method (e.g., MIRO or CLIPood), the claim that this is a general property of DG methods is unsupported.

### Minor

1. **No statistical uncertainty is reported for any experimental result.** Table 1 shows only point estimates with no standard deviations, confidence intervals, or seed information. The DomainBed protocol standardly reports results averaged over multiple seeds. Without error bars, the reader cannot assess whether differences the paper discusses — e.g., CLIPood 57.1% vs MIRO+MPA 57.2% on OOP, or MPA outperforming ERM by 6% on OOP — are meaningful or within noise.

2. **The 0.21 threshold for IP/OOP splitting is subjective and data-dependent.** The threshold is selected "based on the trends observed in Figure 2(a) ... as this is the point where performance begins to improve significantly" (line 129). This is a post-hoc choice based on VL2V-SD's performance curve. Different thresholds would change which samples are IP vs OOP, potentially shifting findings. The paper acknowledges this subjectivity but provides no sensitivity analysis.

3. **Class distribution shifts between IP and OOP are noted but not controlled for.** The paper shows (Figure 8, line 132) that TerraIncognita's class distribution differs substantially between IP and OOP subsets. This means OOP performance gaps could partly reflect class imbalance rather than alignment difficulty. The paper acknowledges this but does not analyze or control for it.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis of the IP/OOP threshold (e.g., 0.18 vs 0.24) to show how robust the findings are.
- Verification of the Alignment Hypothesis on at least one additional method (ERM, MIRO, or CLIPood) beyond VL2V-SD.
- Per-method correlation analysis between AlignmentScore and accuracy, to see if the relationship holds similarly across different DG algorithms.

## Removed Points
These points were flagged during review but removed per filtering rules:
- **Missing Figure 1 (retrieval):** The paper references `\fig{retrieval}` but the figure is absent from the parsed text. This is a parser artifact — the figure exists in the original submission. Removed per hard rule about parser/stripping artifacts.
- **"Data cleaning not systematic, no inter-annotator agreement":** The paper uses a reasonable automated approach (sampling 100 instances per alignment interval, counting mislabeling fraction). Demanding inter-annotator agreement for this type of analysis is disproportionate.
- **"Hyperparameters may have been tuned on the full evaluation set":** This is speculative; the paper follows standard DomainBed protocol using recommended hyperparameters. No concrete evidence of a confound.
- **Strength Finder's claim that the Alignment vs Image Similarity comparison is a "clean, controlled comparison":** This overstates the evidence — the comparison is purely visual with no quantitative measure. The underlying observation (Alignment predicts better than perceptual similarity) is real but the strength claim as phrased was inflated relative to the evidence.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Quantify the comparison.** Report Spearman correlation (or binned AUC) between AlignmentScore/PerceptualSimilarityScore and accuracy, for at least 2–3 methods. This is the minimum to make the central claim credible.
2. **Decouple the splitting backbone from the training backbone.** Define IP/OOP splits using one backbone (e.g., OpenCLIP-ViT-L/14 or DinoV2) and evaluate methods initialized from a different backbone (e.g., OpenCLIP-ViT-B/16). If findings replicate, they would be substantially more convincing.
3. **Report multi-seed results with standard deviations** following standard DomainBed protocol.
4. **Add a sensitivity analysis for the 0.21 threshold** to show how split composition and results change with different thresholds.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>