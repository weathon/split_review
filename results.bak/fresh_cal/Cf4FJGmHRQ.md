Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

The paper proposes PAC-FNO, a frequency-domain neural operator module that attaches to pre-trained image classifiers to handle both low-resolution inputs and natural input variations (fog, brightness, spatter, saturate) with a single model. The key innovations are: (1) removing the low-pass filter from standard FNO blocks to retain high-frequency information (AC-FNO block), (2) stacking AC-FNO blocks in a parallel rather than serial structure to increase capacity, and (3) a two-stage training algorithm that first harmonizes the PAC-FNO module with the backbone at the target resolution before fine-tuning on low resolutions. Experiments on four backbones and seven datasets show consistent improvements over resize-based, super-resolution, and FNO baselines at low resolutions, while maintaining competitive accuracy at the target resolution.

## Strengths

- **Novel architectural design with clear motivation.** Removing the low-pass filter from the FNO block (creating the AC-FNO block) is well-motivated by the observation that high-frequency information is critical for fine-grained visual recognition (Section 3.1). The parallel configuration (n × m blocks) demonstrably outperforms a serial configuration with the same total number of blocks, as shown in Figure 6, where the parallel structure drops only 22.9% under fog at 224 vs. 39.3% for serial.

- **Comprehensive evaluation across diverse conditions.** The paper evaluates four backbone architectures (ResNet-18, Inception-V3, ViT-B16, ConvNeXt-Tiny) on seven datasets including ImageNet-1k, four fine-grained datasets, and ImageNet-C/P corruptions. Tables 1–3 show PAC-FNO consistently achieves the best or near-best accuracy at almost every low resolution (28–128), often beating the next-best method by nontrivial margins — e.g., ConvNeXt-Tiny at 32×32 on ImageNet-1k: PAC-FNO 63.2% vs. UNO 62.9% vs. Fine-tune 62.3%.

- **Two-stage training algorithm is justified by ablation.** Figure 7 demonstrates that both stages are necessary: training only the second stage (direct multi-resolution fine-tuning without first-stage harmonization) leads to severe accuracy degradation (~50% at resolution 224), while the full two-stage algorithm maintains ~70%. This supports the claim that the two-stage procedure is essential for stability.

- **Generalization to unseen resolutions is demonstrated.** Table 4 shows that PAC-FNO trained on only {32, 224} still achieves meaningful accuracy on unseen intermediate resolutions (e.g., 55.5% at 48×48), validating the resolution-invariance property inherited from the FNO framework.

## Weaknesses

### Fatal

None.

### Major

- **The PAC-FNO configuration (n,m) is not reported for the main experimental tables, harming reproducibility.** The sensitivity study (Figure 8) finds that n=1,m=2 is optimal for ResNet-18 on ImageNet-1k, but states that the optimal configuration "show[s] differences depending on the backbone models and datasets" (line 500). However, Tables 1, 2, and 3 never specify which (n,m) was used for each backbone/dataset. Since the performance varies substantially with configuration (Figure 8), readers cannot reproduce the reported results or assess whether the configuration was chosen to maximize PAC-FNO's advantage. The authors should state the (n,m) used for every table entry, or at minimum report that the same configuration was used throughout and state what it was.

- **The training protocol for FNO baselines (FNO, UNO, A-FNO) is ambiguously described, raising questions about fairness.** The paper states these are "trained by our proposed training method for fair comparison" (line 202). The proposed training method is the two-stage algorithm, which the ablation study (Figure 7) confirms is specifically designed for PAC-FNO — "Second stage only" (training directly on low and target resolutions without the first stage) degrades target resolution accuracy severely. If the two-stage algorithm was applied to vanilla FNO architectures that were not designed for it, this could systematically disadvantage them. The paper needs to clarify exactly what "trained by our proposed training method" means for the FNO baselines (same two-stage algorithm, or just the same multi-resolution data and loss?), and ideally include an alternative baseline trained with a more natural protocol for those architectures.

### Minor

- **Extraordinary gains on fine-grained datasets lack supporting analysis.** On Oxford-IIIT Pets at 28×28, PAC-FNO achieves 73.4% vs. the next-best baseline (DRPN) at 41.5% — a 31.9 percentage-point gap (Table 2). Similar large gaps appear on Flowers (74.1% vs. 64.5% DRPN) and Food-101 (74.9% vs. 54.8% DRPN). The paper attributes this to retaining high-frequency components, which is a plausible explanation, but the paper provides no additional analysis (e.g., frequency response visualization, per-class breakdown, or an ablation that compares AC-FNO with a controlled low-pass variant) to verify that the improvement indeed comes from high-frequency preservation rather than dataset bias or other artifacts. This would substantially strengthen the central claim.

- **Target-resolution accuracy degradation is acknowledged for some settings but not fully discussed.** PAC-FNO is slightly below Fine-tune at 224×224 on several corruption types (Table 3: Fog: 62.8 vs. 63.0; Brightness: 74.7 vs. 75.7; Spatter: 64.0 vs. 64.6) and on Oxford-Pets clean (91.7 vs. 93.8). The paper acknowledges this for ImageNet-1k (line 384) and Food-101 (lines 392–393) but not consistently. A multi-objective framing (e.g., Pareto frontier across resolutions) would better characterize the trade-off.

- **Training hyperparameters are not reported.** No learning rate, batch size, number of epochs, optimizer, weight decay, or data augmentation strategy is given for any experiment. While some details may appear in supplementary material stripped by the PDF parser, the paper as provided cannot be reproduced from the information it contains.

- **The stopping criterion for the first training stage is vague.** The paper defines "well harmonized" as "the performance of the model combining PAC-FNO and the pre-trained backbone model is similar to that of a pre-trained model at the target resolution" (footnote, line 167), but does not specify how "similar" is quantified (e.g., threshold in accuracy difference) or the maximum number of epochs.

- **No inference cost analysis is provided.** The paper claims PAC-FNO has only 1–13% of the backbone's parameters (line 175), but no FLOPs or throughput (images/sec) comparison is given. Since PAC-FNO adds frequency transforms and parallel blocks before the backbone, the practical latency impact matters for deployment.

### Trivial

- The abstract claims "improves performance... by up to 77.1%" but this number is not traced to any specific table or baseline in the paper (the only "77.1" in the paper is FNO's accuracy at 112 on ViT-B16 in Table 1). The authors should state which comparison this refers to.

## Nice-to-Haves

- **Ablate the low-pass filter directly.** The paper motivates removing the low-pass filter by citing the accuracy-generalization trade-off (Wang et al., 2020), but never includes an ablation comparing AC-FNO with a variant that uses a controlled low-pass filter in the same parallel structure. Such an ablation would directly test whether the improvements come from retaining high frequencies.

- **Analyze what PAC-FNO learns on fine-grained datasets.** Visualizations of the learned frequency-domain filters, the effective receptive field, or a comparison of which classes improve most would help explain the dramatic gains on fine-grained datasets.

## Removed Points

These points were raised by reviewers but are excluded from the main weakness list for the reasons stated:

1. **"No error bars or standard deviations reported"** — This is a generic criticism applicable to most image classification papers using standard benchmarks; single-run evaluation is the norm in this setting. Removed as a noise point.

2. **"Bold column headers in tables not explained"** — The bold 224/299 columns are clearly the target resolutions described in Section 4 (line 212). This is a formatting choice, not a substantive issue. Removed as a formatting nitpick.

3. **"No evaluation on combined degradations"** — This is factually incorrect. Table 3 evaluates each corruption (Fog, Brightness, Spatter, Saturate) across multiple resolutions (24, 32, 54, 64, 112, 128, 224), i.e., combined low-resolution + corruption. The critic misread the table. Removed as factually wrong.

4. **"FNO baselines are likely being forced into a harmful training protocol"** — The critic asserts this as a structural flaw, but the paper's phrasing ("trained by our proposed training method") is ambiguous: it could refer to the multi-resolution data setup (which would be fair) or the two-stage algorithm (which would be unfair). The critic's framing as a definitive fatal flaw overstates what can be determined from the paper as written. This is reframed as the Major weakness above rather than a fatal flaw because the ambiguity goes both ways. The core concern about missing clarification is retained.

5. **"The paper does not report what training procedure was used for Fine-tune and the super-resolution baselines"** — The paper does describe Fine-tune (line 199–200: "fine-tuning the pre-trained classification model with the resized images"). Removed as the paper addressed this.

6. **Generic strengths from Strength Finder** — "Consistent improvements across multiple backbone architectures and seven datasets" is retained as a supporting strength since it's verifiable from tables. "Sensitivity studies confirm parallel configuration is beneficial" is merged into the general evaluation strengths. Surface-level strengths about the problem being important are dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new perspective that the paper itself does not already provide.

## Suggestions

1. **Report the (n,m) configuration for every experiment in the main tables**, either directly in table captions, a footnote, or a dedicated column. If the configuration varies per backbone/dataset, justify the choice.
2. **Clarify the training protocol for FNO baselines.** State explicitly whether the two-stage algorithm was applied to FNO, UNO, and A-FNO, and whether alternative training protocols (e.g., standard single-stage multi-resolution training) were considered. Include a baseline trained without the two-stage procedure to disentangle architectural gains from training procedure gains.
3. **Add analysis for the fine-grained gains.** At minimum, compare PAC-FNO with a variant that re-introduces a controlled low-pass filter in the parallel structure, and/or visualize the frequency response of learned filters to demonstrate that high-frequency information is retained.
4. **Report training hyperparameters** (learning rate, optimizer, epochs, batch size) for all experiments. Specify the stopping criterion for the first training stage (e.g., fixed number of epochs or accuracy convergence threshold).
5. **Include a brief inference cost comparison** (FLOPs or throughput) between PAC-FNO+backbone vs. resize-and-feed to contextualize the computational overhead.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>