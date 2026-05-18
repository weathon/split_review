Now I have enough information to produce the final consolidated review. Let me write it.

## Summary

The paper tackles the problem of implicit subpopulation imbalance — where classes are balanced but hidden subpopulations within classes are imbalanced and unlabeled. The authors propose SHE (Scatter and HarmonizE), which discovers latent subpopulations by maximizing interaction information (between inputs, labels, and subpopulation assignments) and then achieves subpopulation-balanced predictions through a LogSumExp operation over subpopulation-specific heads. The method is evaluated on COCO, CIFAR-100, tieredImageNet, and spurious-correlation benchmarks, consistently outperforming strong baselines.

## Strengths

1. **Well-motivated problem formulation with clear distinctions from prior work.** The paper explicitly defines implicit subpopulation imbalance and distinguishes it from class imbalance and spurious correlations (Table 1), highlighting why existing class-level calibration methods cannot address this setting. This provides a clear motivation for the proposed approach.

2. **Principled theoretical framework connecting data partition to prediction ability.** The paper introduces optimal data partition via interaction information (Definition 3.1) and proves that minimizing the proposed empirical risk (Eq. 1) asymptotically aligns with maximizing the interaction information (Theorem 3.3). Theorem 3.4 further shows that the LogSumExp operation yields subpopulation-balanced predictions. This provides a principled foundation beyond heuristic clustering.

3. **Consistent and substantial empirical gains across diverse benchmarks.** SHE achieves the best results on all main benchmarks (Table 2): 1.72% gain on COCO, 1.35–1.53% on CIFAR-100 across three imbalance ratios, and 1.42% on tieredImageNet over the best baseline. These gains are consistent and supported by standard deviations.

4. **Balanced improvement across subpopulation splits on COCO.** Table 3 shows SHE improves the minority (Few) split by 4.42% over the best baseline while also achieving the best results on Many and Medium splits. This demonstrates that SHE enhances tail subpopulations without degrading head performance, a critical requirement for real-world deployment.

5. **Extensive ablation and analysis.** The paper ablates the number of subpopulations \(K\) (Fig. 4a), the diversity term \(\beta\) (Fig. 4b), the entropy term (Table 5), and the optimization approach for \(V\) (Fig. 4c). Each component is shown to contribute positively, and the method is robust to hyperparameter choices.

6. **Versatility across richer imbalance contexts.** SHE extends to combined class and subpopulation imbalance (Table 4 left) and to spurious-correlation benchmarks (Table 4 right), showing the method is not narrowly tailored to one setting.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap between the theoretical analysis and the actual algorithm.** The theoretical framework (Definition 3.1, Theorem 3.3) is developed around an *optimal data partition* defined as a *hard* mapping \(\nu: (x,y) \to S\) with an indicator function in Eq. (1). The practical algorithm, however, replaces the indicator with a *soft* assignment matrix \(V\) (Eq. 2), introduces a diversity regularization term \(\text{Div}(\cdot)\) not derived from the theory, and employs a multi-head architecture. The paper does not discuss whether the theoretical guarantees (consistency with interaction information maximization, convergence rates) carry over to the soft-assignment variant actually evaluated. The NMI tracking (Fig. 3) provides empirical support but does not close this gap. As a result, the theory serves as motivation rather than a formal substantiation of the method's success.

2. **Incomplete evaluation of the core claim — protecting minority subpopulations — on CIFAR-100 and tieredImageNet.** The paper's stated goal is subpopulation-balanced predictions that improve performance on minority subpopulations. Per-split (Many/Medium/Few) analysis is only provided for COCO (Table 3). On CIFAR-100 and tieredImageNet, only overall top-1 accuracy is reported. While a balanced test set ensures a fair aggregate, it does not reveal whether the improvements come specifically from better handling of minority subpopulations, from a general lift, or (in the worst case) from sacrificing the smallest groups. Given the paper's own emphasis on per-split analysis (Fig. 1d), this omission is significant on two of the three main benchmarks.

### Minor

1. **Method is underspecified for reproduction from the main text.** Several implementation details are not fully described: (a) how the subpopulation-weight matrix \(V\) is initialized and optimized (jointly with the model or via alternating updates?); (b) how the empirical conditional entropy \(\hat{H}_{\mathcal{D}}(Y|V)\) is computed in practice with soft assignments and in a mini-batch setting; (c) the definition of subpopulations on COCO under the ALT-protocol is referenced but not explained — the reader cannot tell what constitutes a subpopulation on COCO. While an appendix likely contains these details (stripped by the parser), the main text should be self-contained enough for an informed reader to evaluate the method's design.

2. **The claimed problem novelty relative to spurious-correlation methods is nuanced and not fully demonstrated.** Table 1 contrasts subpopulation imbalance with spurious correlations, and the paper argues that methods designed for spurious correlations (e.g., LfF, JTT, EIIL, ARL, GRASP, MaskTune) assume ERM models rely on spuriously correlated attributes. However, many of these baselines are designed precisely to handle group imbalance without group labels, and the paper does not provide a mechanistic analysis showing *why* they underperform on the constructed benchmarks or *why* SHE succeeds specifically because it avoids that assumption. The empirical gains over these baselines are modest (1–2% absolute on most settings), and without deeper analysis the problem-framing distinction, while valid, is less sharp than claimed.

3. **Conceptual tension in the diversity regularization.** The diversity term \(\text{Div}(x)\) encourages disagreement between subpopulation-specific heads on each sample, which is at odds with the goal that each head should specialize to a coherent subpopulation (and thus agree on samples from that subpopulation). The ablation shows it helps marginally (\(\beta=0\) still outperforms ERM), but the tension is not discussed.

4. **Fine-tuning gains from pre-trained models are small.** Table 6 shows SHE consistently outperforms baselines when fine-tuning CLIP, ALIGN, and AltCLIP, but the absolute gains over ERM are 0.5–1.5% and the gap between methods is compressed. This setting does not strongly demonstrate SHE's advantages over alternatives.

5. **Statistical significance is not established.** Several reported standard deviations are large relative to the gains (e.g., the critic notes COCO ERM 78.76±1.54 vs. SHE 79.48±1.28). A paired test or discussion of significance would strengthen the empirical claims.

### Trivial
None.

## Nice-to-Haves

- Per-subpopulation confusion matrices or NMI breakdowns on CIFAR-100 subclasses (beyond the simple 2D toy and Waterbird) would strengthen the subpopulation discovery claims.
- A variant of SHE that conditions the model-based \(V\) on both features and labels (e.g., a small MLP on \([\psi(x), \text{one-hot } y]\)) would more directly test whether the interaction-information framing drives the success.
- Explicit discussion of the trade-off between the diversity term and head specialization.

## Removed Points

- **"The overall improvement on COCO is driven almost entirely by the Few split, possibly with slight sacrifices on Many/Medium"** — Removed because the paper explicitly states (line 159) that SHE achieves *best results on Many-split and Medium-split*, directly contradicting the claim of sacrifices. The paper acknowledges no such trade-off exists on these splits.
- **"More challenging test for NMI needed"** — Moved to Nice-to-Haves. This asks for an additional experiment that would strengthen but does not invalidate existing evidence.
- **Various formatting/style observations** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily affirm the paper's stated contributions while identifying a theory-algorithm gap and an evaluation scope limitation.

## Suggestions

1. **Bridge the theory-practice gap.** Either (a) derive the soft-assignment objective (Eq. 2) as a variational bound or relaxation of the hard-partition interaction information objective, or (b) explicitly characterize under what conditions the soft-assignment variant inherits the theoretical guarantees, and discuss whether the diversity term can be seen as a penalty that encourages the relaxation to approach a hard partition.

2. **Report per-subpopulation accuracy on CIFAR-100 and tieredImageNet.** Provide the same Many/Medium/Few split analysis (or worst-subpopulation accuracy) on these datasets. This directly addresses whether the claimed minority-protection benefit generalizes beyond COCO.

3. **Add an oracle-subpopulation baseline.** Compare SHE against a version where subpopulation assignments come from ground-truth labels (e.g., CIFAR-100 subclasses). This quantifies the gap between the learned partition and the ideal one, calibrating expectations for the theory.

4. **Provide implementation details for \(V\) and \(\hat{H}(Y|V)\) in the main text or a clearly referenced appendix section.** Specify optimization schedule (joint vs. alternating), initialization, learning rate, and the mini-batch estimator for the empirical conditional entropy with soft assignments.

5. **Add a brief discussion of the conceptual role of the diversity term** in relation to head specialization and the theoretical partition objective, clarifying why disagreement helps rather than hurts subpopulation discovery.

## Score and Decision

The paper addresses a relevant and under-explored problem with a novel method that is theoretically motivated and empirically validated across diverse settings. The consistent improvements over strong baselines, the per-split gains on COCO, and the thorough ablation studies represent a genuine contribution. The major weaknesses — the theory-algorithm disconnect and the incomplete per-subpopulation evaluation on CIFAR-100/tieredImageNet — are significant but addressable in a revision and do not invalidate the paper's core empirical findings. The paper delivers on its central claim: SHE consistently improves subpopulation-imbalanced learning across multiple benchmarks.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>