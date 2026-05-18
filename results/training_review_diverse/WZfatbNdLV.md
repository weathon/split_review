Now I have a thorough understanding of the paper and can verify each claim against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper proposes TrASPr, a multi-transformer architecture for tissue-specific splicing prediction, and BOS, a Bayesian optimization framework that uses TrASPr as an oracle to design RNA sequences with desired splicing outcomes. TrASPr centers four pretrained transformers on the four splice sites of a cassette exon, combines their representations with genomic features (intron/exon length, conservation, tissue type), and is trained on GTEx and mouse (MGP) data. The paper reports strong predictive performance (Pearson r=0.81 on GTEx PSI prediction), validates predictions against ENCODE RBP knockdown and Daam1 minigene reporter assays, and shows BOS achieves 30.3% valid candidate sequences under edit-distance constraints versus ~4% for baselines.

## Strengths

- **TrASPr achieves strong predictive performance on tissue-specific splicing tasks.** On the MGP dPSI dataset, TrASPr consistently outperforms the AE+MLP feature-based model from Jha et al. (2017) on AUPRC across multiple tissue pairs (Table 1, Figure 3). The advantage is demonstrated under the same train/test splits used by prior work, providing a fair within-methodology comparison.

- **Experimental validation against orthogonal biological data.** TrASPr is tested against ENCODE RBP knockdown experiments (3 RBPs, 2 cell lines), correctly predicting the direction of splicing change for over 50% of targets (p=0.0001, Figure 4c). It also correctly predicts 7/9 mutations in the Daam1 minigene reporter assay (p=0.0012, Figure 5a). These tests go beyond simple held-out metrics and probe whether the model captures real regulatory mechanisms.

- **Ablation studies convincingly justify the architectural choices.** Table 2 shows that removing pretraining (noPre) severely degrades regression metrics, removing side features (noFeat) degrades prediction values, and replacing the transformers with bidirectional LSTMs (wLSTM) causes dramatic performance loss across all metrics. This substantiates the claim that each component — pretraining on splice sites, transformer attention, and side features — contributes meaningfully.

- **Careful handling of data leakage and long-range context.** The paper hides entire chromosomes for testing and applies similarity filters to avoid leakage from paralogs/orthologs (Section 2). The four-transformer design allows the model to handle variable-length regulatory regions that can span far beyond the fixed 10 Kb window of prior CNN models like Pangolin and SpliceAI.

## Weaknesses

### Fatal

None.

### Major

- **The Pangolin comparison (Section 4.1, Figure 2) is unreliable and should not be used to support a state-of-the-art claim.** Pangolin was designed to predict "splice usage" from a 10 Kb window, not the PSI of a specific cassette exon. The paper feeds it only the splice sites of each cassette exon and averages two scores — a procedure validated nowhere in the Pangolin paper. The reported gap (0.81 vs 0.17) is so large that it demands a fair comparison, and the current one does not provide it. The paper is transparent about the adaptation, but the result is nonetheless misleading when presented as evidence of state-of-the-art performance. **The authors should either drop this comparison or replace it with a properly matched baseline (e.g., train a SpliceAI-style model on the same data and task).** The AE+MLP comparison (MGP data) provides independent support for TrASPr's value and should be foregrounded instead.

- **Data leakage concern in the AE+MLP comparison (Section 4.1, Table 1).** When applying a stricter filtering criterion, TrASPr's performance degrades while AE+MLP's improves. The paper explains this by noting that filtered events had labels correlated with similar training samples, giving TrASPr an advantage that AE+MLP (using predefined features) could not exploit. This explanation is reasonable but the paper provides no quantitative support — no histogram of sequence identity between train and test, no characterization of the 2,354 additionally excluded events. Without this analysis, the concern that TrASPr is partially memorizing local sequence patterns rather than learning generalizable regulatory rules remains unresolved. **The authors should report the distribution of max sequence identity between train and test under both filter levels.**

### Minor

- **BOS evaluation is circular and provides no evidence of biological validity (Section 4.4).** As the paper acknowledges ("we assume the Oracle is correct and only assess the ability to efficiently generate candidate sequences"), BOS uses TrASPr as its oracle and then evaluates against TrASPr's own predictions. The comparison to random mutation and genetic algorithm measures only optimization efficiency against this oracle, not whether the designed sequences would produce the intended splicing changes in a biological system. The paper's framing of BOS as a co-equal contribution alongside TrASPr is overstated; it is an in silico proof-of-concept awaiting experimental validation. The authors should scale back BOS claims and explicitly call for experimental testing.

- **Unspecified weight sharing among the four transformers (Section 3.1.2).** The paper describes "a matching pre-trained transformer T^i" for each of the four splice-site regions but never states whether these four transformers share weights (same pretrained checkpoint, fine-tuned jointly) or are entirely separate instances. This affects both model size and the interpretation of fine-tuning dynamics. The notation T^i and the phrase "utilizing several Transformers each focused on a specific region" suggests separate instances, but this should be stated explicitly.

- **BOS VAE training details are absent.** The paper states the VAE uses a "6 layer Transformer encoder and 6 layer Transformer decoder" (Section 3.2) but provides no information about latent dimensionality, training epochs, batch size, learning rate, tokenization scheme for the VAE, or how variable-length sequences are handled (the paper notes sequences can span "many kilo-bases" but each transformer processes 400-base windows). These details are necessary for reproducibility.

- **ENCODE RBP KD correlation is modest.** The reported Pearson r for dPSI effects is 0.34 (p=0.0192), and approximately half of the negative-direction cases (decreased inclusion after KD) are predicted as "no change" (Figure 4c). The paper describes this as "performed well," which overstates the evidence. This does not undermine the contribution but should be characterized more accurately.

### Trivial

- **Daam1 region 11 blind spot.** Both minigene misses occur in the same region (region 11), suggesting a systematic blind spot rather than random noise. The paper notes this but does not offer a potential explanation. Worth investigating but does not affect the core results.

## Nice-to-Haves

- An ablation comparing TrASPr's splice-site pretraining against a generic RNA language model pretrained on the same data would strengthen the claim that the pretraining strategy is specialized and beneficial.
- For BOS, an analysis of which known RBP regulatory motifs (from ATtRACT or RBPDB) appear in the mutated regions would improve the biological plausibility of the designs without requiring wet-lab validation.
- A histogram of max sequence identity between training and test sets under both filter levels would cleanly resolve the data leakage concern.

## Removed Points

- The reviewer's concern that "the AE+MLP model's improvement under stricter filtering... is a red flag that the 'standard' filter may be too permissive" is noted but retained as a Major weakness (it is a legitimate concern, though the paper provides a reasonable explanation). What is removed: the framing of this as definitively indicating leakage, since the paper's counter-explanation is coherent.
- The reviewer's framing that "the Pangolin benchmark inflates TrASPr's reported advantage and misleads readers about the field's baseline" is accurate and retained. However, the suggestion to "drop this comparison entirely" is softened to a Major weakness rather than a fatal flaw, since the AE+MLP comparison provides independent support.
- The reviewer's request for "experimental validation of BOS-designed sequences (even a single minigene assay)" is moved to Nice-to-Haves; it would strengthen the paper but is a scope expansion, not a flaw in what was demonstrated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective absent from the paper itself.

## Suggestions

1. **Replace or properly qualify the Pangolin comparison.** Either drop it entirely and rely on the AE+MLP comparison plus ablation studies, or add a properly trained SpliceAI-style model on the same task as a baseline.
2. **Quantify the data leakage concern.** Report a histogram of max percent sequence identity between training and test events under both "standard" and "stringent" filtering to show whether the additionally excluded events are enriched for near-duplicates.
3. **Clarify the TrASPr architecture.** State explicitly whether the four transformers share weights or are separate instances, and specify the actual genomic span of the four 400-base windows.
4. **Add BOS VAE training details.** Report latent dimensionality, training epochs, batch size, and how variable-length sequences are handled.
5. **Reframe BOS as an in silico proof-of-concept** rather than a co-equal contribution, and add an explicit call for experimental validation in the discussion.
6. **Tone down the characterization of the ENCODE results** (r=0.34) to match the evidence.

## Score and Decision

The paper makes a genuine contribution with TrASPr — a well-motivated architecture for tissue-specific splicing prediction, supported by ablation studies and multiple validation datasets. The BOS component is interesting but preliminary and circularly evaluated. The Pangolin comparison is the main weakness that inflates the claimed contribution, but it is not the only evidence of TrASPr's value. The data leakage concern is plausible but the paper provides a reasonable (if unquantified) explanation. With revisions to the Pangolin comparison, BOS framing, and reproducibility details, this would be a solid contribution to the splicing code literature.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>