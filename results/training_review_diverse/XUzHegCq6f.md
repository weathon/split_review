Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper proposes Polyak Parameter Ensemble (PPE), a method that constructs a parameter-level ensemble by maintaining a running weighted average of model parameters at each epoch interval during training of a single model. The authors apply PPE primarily to knowledge graph embedding models (DistMult, ComplEx, QMult) on link prediction and multi-hop reasoning tasks, and also include a CIFAR-10 image classification experiment. The claimed advantage is improved generalization with zero additional cost at test time — the same memory and latency as a single model.

## Strengths

- **Cost-free ensemble at test time.** PPE requires no architectural changes, no extra training, and produces a single set of parameters at test time. This is a genuinely practical advantage over prediction-level ensembles (e.g., Bagging, Snapshot Ensembles) that multiply test-time memory and latency. The paper clearly articulates this advantage (Section 1) and verifies that no runtime overhead was detected in practice (Section 5).

- **Consistent improvements across KGE models and datasets.** The experimental results (Tables 4–6) show that PPE consistently improves MRR and Hits@N over the final-epoch baseline for DistMult, ComplEx, and QMult on FB15K-237, YAGO3-10, NELL-995 variants, UMLS, KINSHIP, Mutagenesis, and Carcinogenesis. The effect holds across multiple KGE model families and a diverse set of dataset sizes and domains.

- **Benefits scale with model capacity.** Table 8 demonstrates that the improvement from PPE becomes more pronounced as the embedding dimension \(d\) grows, with the method outperforming the baseline on 81 out of 96 scores for \(d \geq 32\). This scaling behavior is a useful finding for practitioners working with large embeddings.

- **Clean experimental design isolating the averaging effect.** By fixing the cutoff epoch \(j=200\) across all datasets and not using validation-loss feedback (line 135), the authors ensure the observed improvements come from the averaging mechanism itself rather than from implicit early stopping or validation-set leakage. This makes the ablation cleaner.

## Weaknesses

### Fatal
None. The results are not fabricated or fundamentally invalid — the core finding (epoch-level averaging improves over the final checkpoint) is reproducible in principle.

### Major

- **Missing comparison to the most relevant baselines: SWA and standard Polyak averaging.** The paper compares PPE only to the final-epoch checkpoint, not to Stochastic Weight Averaging (Izmailov et al., 2018, cited at line 36) or to standard mini-batch-level Polyak averaging over the same training trajectory. Since PPE with uniform weights is explicitly described as "applying the Polyak averaging technique at each epoch interval" (lines 10, 90), the novel claim must be that epoch-level granularity and/or exponential weighting provides benefit over these existing approaches. Without direct experimental comparison under an identical compute budget, the paper cannot support this claim — the observed improvements may be obtainable with simpler, well-known averaging schedules. This is the most significant gap in the paper.

- **The fixed cutoff epoch \(j=200\) is not ablated and may be problematic.** The paper sets \(j=200\) for all datasets, even those trained for only 200 total epochs (line 133: \(N \in \{200, 250\}\)). For \(N=200\), this means the averaging window is the very last epoch or less — effectively no averaging at all — yet results are still reported as improved. For \(N=250\), the window is 50 epochs. No ablation is provided to show how performance varies with \(j\), and no justification is given for choosing 200 over any other value. This makes it difficult to assess whether the method is robust or relies on a carefully tuned hyperparameter.

- **Single-run results reported without variance.** All results in Tables 4, 5, 7, and 8 appear to come from single runs with no standard deviations, confidence intervals, or multi-seed statistics. For a method whose stated advantage includes "more stable training" (line 13), stability across runs is directly relevant. The 10-fold cross-validation on Mutagenesis and Carcinogenesis (Table 6) is a partial exception but covers only two small datasets. The field norm for KGE (Ruffinelli et al., 2020, whose setup the paper follows) often uses single runs, but the paper's own claims about stability make the lack of variance reporting more consequential here.

### Minor

- **CIFAR-10 experiment is under-reported.** The image classification experiment is presented only as a qualitative figure (Figure 1) with no model architecture, no training hyperparameters, no quantitative test accuracy, and no comparison to a non-PPE baseline in the text. This does not constitute a reproducible experimental result and weakens the claim that PPE "generalizes across tasks."

- **Theoretical justification does not match the experimental setup.** The derivation in Section 3 uses \(T=2, N=2\) with equal weights from epoch 1 onward to argue that averaging reduces the influence of later noisy updates. But the experiments use a cutoff \(j=200\), where epochs 1–200 receive zero weight. The paper does not reconcile this discrepancy. The theory as presented motivates full-trajectory averaging; what is actually evaluated is late-stage averaging.

- **Limited exploration of the exponential growth rate \(\lambda\).** Only \(\lambda \in \{1.0, 1.1\}\) are tested (line 133). The paper proposes exponential weight growth as a mechanism but provides almost no analysis of how \(\lambda\) affects performance or guidance on how to set it.

- **Memory overhead of maintaining a running parameter average is not discussed.** The paper claims "no additional computational cost" but maintaining a running average requires storing a second copy of all parameters in memory (the same cost as SWA). This is worth acknowledging, even if the cost is modest relative to prediction-level ensembles.

- **Minor inconsistencies.** The Introduction claims benefits dissipate at \(d \leq 4\) (line 21), but the Discussion states they dissipate for \(d < 16\) (line 195). The abstract claims "11 benchmark datasets" but only 10 are clearly identifiable in the main paper (UMLS, KINSHIP, NELL-995 h25, NELL-995 h50, NELL-995 h100, FB15K-237, YAGO3-10, Mutagenesis, Carcinogenesis, CIFAR-10), and results for NELL-995 h100 are not presented in the main tables.

### Trivial
- No pseudocode/algorithm box is provided, which would improve reproducibility of the running-average update procedure.
- The title phrase "Exponential Parameter Growth" could be misinterpreted as referring to the number of parameters growing rather than the ensemble weights.

## Nice-to-Haves

- An ablation of the cutoff epoch \(j\) (e.g., \(j \in \{0, 50, 100, 150, 200\}\)) would directly address the gap between theory and practice.
- Reporting multi-seed statistics (mean and std over 3–5 seeds) for the main results would strengthen the stability claims.
- A discussion of how the exponential weights are normalized in practice (the paper states \(\sum \alpha_i = 1\) but exponential growth requires re-normalization) would improve clarity.

## Removed Points

- **Criticism that SWA/Polyak are "absent from the discussion."** This is partially incorrect: Izmailov et al. (2018) is cited at line 36, and the paper explicitly connects PPE to Polyak averaging multiple times (lines 10, 21, 90). The core concern (missing experimental comparison) is preserved in Major weaknesses; the incorrect claim of total absence is removed.
- **Criticism about training set scores being reported as a weakness.** The paper explicitly states the rationale for reporting training scores ("to detect possible impacts on the training performance," line 157). This is a design choice, not an error.
- **Generic formatting/style nitpicks.** Removed per instructions.

## Novel Insights

The most interesting observation is the scaling behavior: PPE's benefit grows with embedding dimension \(d\) and essentially vanishes for small \(d\). This suggests that the method is compensating for optimizer noise that scales with model capacity — a plausible mechanism worth investigating further. However, the paper does not provide a theoretical account of why this scaling occurs, so this remains an observation rather than a developed insight. Beyond this, the reviews do not surface a genuinely novel insight beyond the paper's own contributions.

## Suggestions

1. **Add experimental comparisons to SWA and mini-batch Polyak averaging** under the same training budget. This is the single highest-impact change: it would clarify whether the epoch-level granularity or the exponential weighting (as opposed to the general concept of parameter averaging) is responsible for the gains reported.
2. **Run an ablation on the cutoff epoch \(j\)** to show how performance depends on the averaging window length and to reconcile the theory with the experiments.
3. **Report the CIFAR-10 experiment with full quantitative results** (architecture, hyperparameters, final test accuracy with and without PPE, and ideally multiple seeds).
4. **Add multi-seed standard deviations** for at least the three largest datasets (FB15K-237, YAGO3-10, NELL-995 h50) to support the stability claim.
5. **Include a pseudocode algorithm** showing exactly when and how the running average is updated, and clarify the weight normalization procedure for the exponential case.

## Score and Decision

The paper proposes a simple, practical technique and provides consistent empirical evidence that it improves KGE link prediction over the final-epoch baseline. The method's main strength — cost-free test-time ensemble — is real and well-articulated. However, the experimental evaluation has a critical gap: the most natural baselines (SWA, standard Polyak averaging) are absent, and without them the claim of novelty or superiority cannot be evaluated. Combined with the unablated cutoff epoch, single-run results, and under-reported CIFAR-10 experiment, the contribution as presented is not yet convincingly established as new or practically superior to existing averaging techniques. The paper would need the suggested comparisons to reach the bar for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>