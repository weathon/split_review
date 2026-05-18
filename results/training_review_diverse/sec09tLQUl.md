I have the full paper from the initial read. Now I'll construct the final consolidated review by carefully cross-referencing each claim against the paper's actual content.

---

## Summary

This paper studies the connection between memorization and poor generalization for minority groups in spurious-correlation settings. Through a neuron-flipping analysis (adapted from Maini et al., 2023), it shows that minority-group examples require fewer neurons to flip their prediction and that dropping those neurons improves worst-group accuracy. It then proposes FairDropout, an example-tied dropout method that allocates "memorizing neurons" to individual examples during training and drops these at test time, aiming to redirect memorization into droppable slots. The method is evaluated on five datasets (CelebA, Waterbirds, MetaShift, MultiNLI, MIMIC-CXR) from the subpopulation shift benchmark, improving over ERM on all five and achieving competitive/state-of-the-art results on MultiNLI and MIMIC-CXR, all without requiring group annotations.

## Strengths

- **Novel empirical analysis linking memorization to poor minority-group generalization in the spurious-correlation setting.** Figures 2 and 3 provide concrete evidence: (a) minority-group examples require far fewer neurons to flip their prediction than majority-group examples; (b) those neurons have less impact on training worst-group accuracy; (c) dropping those neurons improves test worst-group accuracy for ~75% of minority-group examples. This mechanistic insight is new in this context and goes beyond simply restating the known worst-group accuracy gap.

- **FairDropout improves upon ERM on all five datasets without requiring group annotations.** As shown in Table 1, FairDropout outperforms ERM on CelebA (75.6 vs. 67.2), Waterbirds (87.3 vs. 84.0), MetaShift (85.9 vs. 78.6), MultiNLI (70.3 vs. 63.6), and MIMIC-CXR (70.6 vs. 68.0). This is a genuine improvement operating in a more challenging setting than methods that require group annotations.

- **Competitive or state-of-the-art results on MultiNLI and MIMIC-CXR.** FairDropout achieves 70.3 ± 2.4 on MultiNLI (beating all compared methods) and 70.6 ± 0.6 on MIMIC-CXR (beating or tying all methods), suggesting particular value in text and medical domains where group annotations are expensive.

- **Cross-domain validation.** The evaluation spans five datasets across three modalities (vision, NLP, medical imaging), demonstrating that the approach generalizes beyond a single domain or benchmark.

## Weaknesses

### Fatal
None.

### Major

- **The central mechanism claim — that FairDropout works by redirecting memorization into the allocated neurons — is not directly verified.** Section 3.2 elegantly identifies the *actual* neurons that flip minority-group predictions when removed, and shows dropping them helps. FairDropout (Section 3.3) then randomly allocates "memorizing neurons" during training, *hypothesizing* that the network will steer memorization into those slots. The paper does **not** provide an experiment showing that, after training with FairDropout, the randomly allocated neurons are indeed the ones that flip predictions when removed (e.g., by running the Section 3.2 analysis on FairDropout-trained models). Without this link, the motivating analysis and the method are disconnected: FairDropout could be working simply as a structured regularizer, and the "redirecting memorization" story remains unsubstantiated. The Limitations section (line 197–199) acknowledges this as a hypothesis "outside the scope of this paper," but the main text presents it more assertively, creating a gap between framing and evidence.

- **No comparison to standard dropout.** Standard (Bernoulli) dropout is the most natural baseline for any dropout variant. FairDropout drops neurons at test time; standard dropout drops neurons stochastically during training and keeps all at test — different mechanisms, but the comparison is essential to determine whether the example-tied allocation drives the gains or simply any structured regularization would help. The paper includes many baselines (GroupDRO, DFR, JTT, Resample, CBLoss, etc.) but omits standard dropout entirely. If standard dropout at comparable effective drop rates achieves similar worst-group accuracy improvements, FairDropout's distinctive contribution is substantially weakened. This omission undermines the paper's ability to argue for the value of its specific design.

### Minor

- **No ablation on the core hyperparameters \(p_{\text{gen}}\) and \(p_{\text{mem}}\).** These control how many neurons are designated as memorizing and how often each example gets one — the very mechanism the paper claims is central. The warm-up experiment uses \(p_{\text{mem}}=p_{\text{gen}}=0.2\), and the full benchmark says these were tuned along with learning rate and weight decay, but no sensitivity analysis is reported. The reader cannot assess how robust the method is, whether performance degrades gracefully as these deviate from optimal values, or whether the optimal ratios differ meaningfully across datasets.

- **The Section 3.2 analysis has clarity issues that limit reproducibility.** Equation 1 references notation (\(\Delta \Omega_B\)) that does not appear in the equation itself. The sequential neuron removal procedure is described only in one dense paragraph, making it difficult to determine exactly how the set of "memorizing neurons" is identified and how overlapping sets are handled when different examples require dropping different neurons (relevant for Figure 3's claim about "75% of cases").

- **Ambiguity in the FairDropout allocation description.** The text states "each sample is allocated a memorizing neuron uniformly with probability \(p_{\text{mem}}\)" and also "every example allocates the same fixed number of memorizing neurons." These are in tension: the former implies stochastic allocation (some examples get none), the latter implies deterministic allocation. The paper also says "each image allocates only one memorizing neuron" in a figure caption. This needs clarification.

### Trivial
None beyond what is already captured in Minor.

## Nice-to-Haves

- A comparison to the original example-tied dropout from Maini et al. (2023) on the same spurious-correlation benchmarks would help establish whether the shift from the label-noise setting introduces new challenges or benefits.
- An analysis of why FairDropout underperforms DFR and several other methods on Waterbirds, beyond the brief speculation about transfer learning.
- Reporting training time or memory overhead compared to ERM would substantiate the scaling claim more concretely.
- An investigation (perhaps in a figure) of the correlation between worst-class accuracy (used for tuning) and worst-group accuracy (used for final evaluation) to validate the tuning proxy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The scaling claim is unsupported."** The paper demonstrates scaling to ResNet-50 and BERT with architectural descriptions (placement after residual blocks for ResNet-50; added linear layer before classifier head for BERT). The experimental results confirm that the method works at this scale. The reviewer's complaint about not identifying "technical obstacles" expects the paper to justify the difficulty of scaling, which is secondary to demonstrating that scaling succeeds. **Justification:** The criticism is a matter of framing preference — the paper shows scaling works, which is sufficient.

- **"Claims of being 'first' are too strong."** Without external literature verification, I cannot confirm or deny this claim. Per instructions, I must not manufacture missing related-work criticisms. **Justification:** Requires external knowledge I do not have.

- **"Figure 1 is not new."** It shows the known worst-group accuracy gap, which the paper uses as setup for the memorization analysis (the novel part). **Justification:** This is contextual framing, not a claimed novel finding.

- **"The Waterbirds explanation is just speculation."** The paper offers a plausible hypothesis citing Izmailov et al. (2022). A deeper analysis would strengthen the paper, but the offered explanation is reasonable. **Justification:** Moved to Nice-to-Haves.

- **"Missing reproducibility details (epochs, batch size, LR schedule)."** The paper explicitly states it uses the subpopulation shift benchmark library (Yang et al., 2023), which standardizes the training protocol. FairDropout-specific hyperparameters are described and tuned. **Justification:** Reproducibility concerns addressed by reference to the benchmark library.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Verify the mechanism.** Run the neuron-flipping analysis (Section 3.2) on models trained *with* FairDropout to check whether the randomly allocated "memorizing" neurons are indeed the ones that flip minority-group predictions. This single experiment would bridge the disconnect between motivation and method.
2. **Add standard dropout as a baseline.** Compare FairDropout against standard (Bernoulli) dropout with matched effective drop rates at test time, to determine whether the example-tied allocation is responsible for the gains.
3. **Add an ablation study** on \(p_{\text{gen}}\) and \(p_{\text{mem}}\) on at least CelebA, including extreme cases (\(p_{\text{mem}}=0\), \(p_{\text{gen}}=1\) recovers ERM), to characterize sensitivity.
4. **Clarify the allocation rule.** Resolve the ambiguity between "probability \(p_{\text{mem}}\)" and "same fixed number" — specify explicitly whether every example always receives the same number of memorizing neurons or whether allocation is stochastic.

---

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>