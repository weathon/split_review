Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper presents TrASPr, a multi-Transformer architecture for tissue-specific splicing prediction (PSI/dPSI), and BOS, a Bayesian optimization algorithm for designing RNA sequences with desired splicing outcomes. TrASPr uses four pre-trained Transformers centered on each splice site of a cassette exon, combined with hand-crafted features, and is evaluated on GTEx, MGP, ENCODE RBP knockdown, and Daam1 minigene data. BOS uses TrASPr as an oracle within a latent-space Bayesian optimization framework to mutate sequences under edit-distance constraints.

## Strengths

1. **Well-motivated architecture with validated design choices.** The multi-Transformer design (four Transformers, one per splice site region) is a principled response to the biological structure of splicing regulation. The ablation study (Table 2) quantitatively confirms that removing pretraining (noPre), features (noFeat), or replacing Transformers with LSTMs (wLSTM) degrades performance, providing solid evidence that the architectural choices matter.

2. **Strong performance on dPSI prediction against a relevant feature-based baseline.** On the MGP dataset, TrASPr significantly outperforms the AE+MLP model (Jha et al., 2017) in AUPRC for both differentially included and excluded events (Figure 3, Table 1), using the same train/test splits. This comparison is apples-to-apples and represents a genuine improvement over a curated-feature approach.

3. **Independent experimental validation on held-out perturbation data.** TrASPr correctly predicts the direction of splicing changes for RBP knockdowns in ENCODE data (>50% direction accuracy, p=0.0001) and 7/9 mutations in Daam1 minigene reporter assays (p=0.0012) — both independent, biologically grounded evaluations that go beyond simple held-out prediction.

4. **BOS generates biologically interpretable mutations.** The BOS algorithm preferentially mutates core splice sites and known RBP regulatory motifs (TIA1, PTBP1, QKI) rather than neutral regions (Section 4.4, Figures 5b–5c), suggesting the generated sequences are realistic and biologically plausible.

5. **Formulation of a new constrained splicing design problem.** The paper explicitly defines the optimization task with Levenshtein distance and tissue-specific outcome constraints (Equation 1), framing a practical biomedical problem (ASO targeting, prime editing) that is novel and potentially impactful.

## Weaknesses

### Fatal
None.

### Major

1. **Pangolin comparison is uncharitable and likely not apples-to-apples.** The paper reports TrASPr achieving Pearson 0.81 vs. Pangolin's 0.17 on GTEx PSI prediction — an extraordinarily large gap that far exceeds any reasonable model improvement. The paper adapts Pangolin by feeding splice site predictions and averaging, but this adaptation is **not validated**. Pangolin was designed to predict splice usage at individual genomic positions from a 10kb window, not to quantify cassette exon inclusion. The paper's own explanation — that the large gap "might be because... relevant sequence context is outside the 10kb window" — acknowledges the mismatch. Without showing that Pangolin can be fairly applied to this task or comparing on Pangolin's own evaluation protocol (tissue-specific splice usage prediction), the claim that TrASPr achieves "state-of-the-art" PSI prediction is not convincingly supported. This weakness is partially mitigated by the paper's other evidence (MGP comparisons, RBP KD, Daam1) but the headline SOTA claim rests heavily on this comparison.

2. **BOS evaluation is circular and does not demonstrate RNA design.** The paper acknowledges this limitation explicitly ("Note that here we assume the Oracle is correct and only assess the ability to efficiently generate candidate sequences," Section 4.4), which is commendable. However, this means BOS is evaluated entirely against the same model (TrASPr) that it uses as an oracle. The baselines (random mutation, genetic algorithm) are also evaluated against the same oracle, so the comparisons are internally consistent but tell us nothing about whether the designed sequences would produce the desired splicing outcome in vivo. The paper frames BOS as a sequence design method (abstract: "we demonstrate BOS can more effectively mutate a given sequence"), but the actual contribution is an algorithm that optimizes a model's predictions. Without wet-lab validation or at minimum validation against held-out experimental ground truth (e.g., the Daam1 data), the design claim is premature.

### Minor

1. **Data leakage concern on MGP under strict filtering.** When stricter filtering is applied to remove test exons similar to training exons, TrASPr's performance degrades while AE+MLP improves (Section 4.1). The paper explains this as TrASPr benefiting from correlated labels in similar samples while AE+MLP, using predefined features, does not. However, this pattern is consistent with TrASPr exploiting non-causal correlations rather than learning generalizable regulatory principles. The paper presents the standard filtering as primary and mentions the stricter result only in passing, but this pattern warrants deeper investigation and a clearer statement of what it implies about generalization.

2. **Missing implementation details hinder reproducibility.** Several architecture and training details are underspecified: (a) the value of k in "mask the surrounding k tokens" is never given; (b) whether the four Transformers T¹…T⁴ share weights or are separate is ambiguous from the phrase "matching pre-trained transformer"; (c) the VAE latent dimensionality and KL regularization are not specified; (d) how continuous PSI/dPSI targets are binned for cross-entropy loss is not described (the paper states cross-entropy "performed better than regression" without showing the comparison); (e) no code, model weights, or data are mentioned for release. These gaps make independent verification difficult.

3. **RBP KD results are modest.** The dPSI correlation of 0.34 (p=0.0192) is weak, and the model misses roughly half of negative-direction cases (Figure 4c). The paper reports "over 50%" direction accuracy — this is statistically significant but not strong. Precision and recall are not reported. The systematic failure on both negative-direction Daam1 mutations in region 11 (Figure 5a) suggests the model has a blind spot for repressive elements in that region that goes unexplained.

4. **BOS baselines are weak.** The genetic algorithm baseline is taken from Sample et al. (2019), originally designed for 5' UTR design, not splicing. A more relevant baseline would be a simple VAE with random latent sampling, or direct evolutionary search on the sequence. Additionally, the success threshold (dPSI > 0.2) is arbitrary with no sensitivity analysis.

### Trivial

- The paper states "over 50%" correctly called changes for RBP KD without reporting the exact number or precision/recall.
- The constraint Ψ ≥ 0.05 for non-target tissues is stated without justification or sensitivity analysis; the paper's justification ("prevents destroying splicing") is reasonable but a sensitivity check would strengthen it.

## Nice-to-Haves

- Analysis of the VAE's reconstruction accuracy (perplexity, sequence-level reconstruction rate) and latent space quality, since BOS depends on the decoder's ability to produce meaningful sequences.
- Quantitative comparison to MT-Splice or a discussion of why it is not comparable.
- Sensitivity analysis on the BOS constraint parameters (Ψ ≥ 0.05, τ = 30).
- Post-hoc in silico validation of BOS using the Daam1 minigene data: would BOS-designed mutations in region 11 produce the experimentally observed decreased inclusion?

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing table values (Table 1, Table 2 content not visible):** Parser issue — figures/tables embedded as images in the PDF are not extracted in the plain text. The original submission contains them. Removed per "missing appendix/sections" rule.
- **"Code and data not released" characterization as fatal flaw:** This is a valid concern but not fatal in isolation; moved to Minor #2.
- **"Explicit comparison to MT-Splice" demand:** The paper compares against the most relevant baselines (Pangolin, AE+MLP) and discusses MT-Splice as related work. Demanding additional baselines beyond what the paper's scope warrants.
- **"The 0.05 constraint is arbitrary and biologically unmotivated":** The paper provides a reasonable justification. This is a minor point, subsumed under Trivial.
- **"The paper should analyze VAE reconstruction accuracy":** A reasonable suggestion but not a weakness — moved to Nice-to-Haves.
- **Generic formatting/style nitpicks from the harsh critic:** Removed per formatting rules.
- **"BOS should be compared to a simple VAE with random latent sampling":** A valid suggestion but the comparison to random mutation and GA is sufficient for a first presentation; moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews identify structural evaluation gaps (particularly the Pangolin comparison and BOS circularity) that are noted by the authors themselves to varying degrees, but do not introduce new technical insights about the method.

## Suggestions

1. **Fix the Pangolin comparison.** Either validate the adaptation (e.g., show that Pangolin's averaged splice-site predictions correlate reasonably with ground-truth PSI on a subset), or drop the SOTA claim and instead use a fairer baseline (e.g., retrain SpliceAI or Pangolin on the same cassette-exon task). Alternatively, reframe the comparison as "TrASPr achieves stronger PSI prediction than the best available alternative adapted to this task, with caveats."

2. **Reframe BOS explicitly.** Rename the contribution from "RNA sequence design" to "model-based optimization of splicing outcomes" or add a limitations subsection that prominently states that BOS optimizes TrASPr's predictions and has not been experimentally validated. The abstract and introduction should match this more cautious framing.

3. **Address the strict-filtering MGP result.** Either show that TrASPr's advantage holds under stricter filtering with a different explanation, or add an explicit discussion of what the degradation implies about the model's learning biases.

4. **Release code and pretrained models.** As a computational paper whose contributions are architectural, this is essential for community impact and verifiability.

5. **Report confidence intervals / error bars** for main results (at minimum the PSI correlations and ablation metrics) based on multiple train/test splits or bootstrap resampling.

## Score and Decision

The paper introduces interesting methodology — the multi-Transformer architecture for splicing is well-motivated and the ablation study confirms its value. The independent validation on RBP KD and Daam1 data is a genuine strength. However, two structural issues prevent the paper from making its case convincingly. First, the headline claim of state-of-the-art PSI prediction rests on a Pangolin comparison that is likely not apples-to-apples, overstating the result. Second, the BOS "design" contribution is evaluated circularly and its framing exceeds what the evidence supports. These are not fatal — the underlying methodology has merit — but they require substantial revision to the claims and evaluation. The missing implementation details further weaken verifiability.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>