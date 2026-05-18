Now I have a complete picture. Let me write the final consolidated review.

## Summary

The paper proposes **RedGrape**, a method for federated long-tailed learning that re-balances the classifier in a decentralized manner during local training. The key ideas are (i) constructing a local balanced dataset from local real data supplemented by global gradient prototypes for missing classes, and (ii) introducing a supplementary classifier to allow the main classifier to be re-balanced without causing optimization conflicts. The method is evaluated on long-tailed MNIST, CIFAR-10, and CIFAR-100, consistently outperforming baselines including the prior SOTA CReFF.

## Strengths

1. **Addresses a key limitation of prior SOTA by leveraging local real data rather than server-side pseudo features.** The paper correctly identifies that CReFF's server-side pseudo features are low-quality and highly similar per class (Section 1, paragraph 3), leading to a sub-optimal classifier. RedGrape instead uses abundant real data stored on clients, supplemented by global gradient prototypes, to form local balanced datasets for classifier re-balancing (Section 3.3.1, Eq. 9–12). This design choice is validated by ablation in Section 5.1 (Figure 3), where removing local real data (T=∞) degrades performance.

2. **Formalizes and resolves the contradictory optimization goal from local classifier re-balancing.** The paper introduces a supplementary classifier Ŵ alongside the main classifier W to decouple instance-balanced training from classifier re-balancing (Section 3.2, Eq. 3–4). The necessity is empirically demonstrated in Section 5.2 (Figure 4): removing the supplementary classifier ("Ours w/o Extra Classifier") leads to significantly worse performance, confirming that the two-stream architecture is critical for avoiding bad local optima.

3. **Mixed gradient re-balancing handles missing classes without requiring a global balanced dataset.** When a client lacks samples for a class, the method substitutes the global gradient prototype of that class (Eq. 10–12). This allows each client to re-balance even when local data is non-i.i.d. and missing classes. The effectiveness is supported by consistent superiority across multiple imbalance ratios (IR 10, 50, 100) in Tables 1 and 2.

4. **Consistent SOTA performance across diverse settings.** The method outperforms all baselines (FedAvg, Fed-Focal Loss, Ratio Loss, CLIMB, CReFF) on MNIST-LT, CIFAR-10-LT, and CIFAR-100-LT under both full and partial client participation, at multiple imbalance ratios. Improvements are often large (e.g., >5 points on CIFAR-10-LT IR 100). Faster convergence is demonstrated in Figure 2.

5. **Practicality: no extra server-side auxiliary data or server-side training overhead.** Unlike Ratio Loss (requires auxiliary dataset on server) and CReFF (requires optimizing pseudo features on server), RedGrape only uses standard gradient aggregation on the server and leverages data already present on clients.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Imprecise theoretical framing.** Section 3.2 frames the optimization as a Lagrange multiplier problem (Eq. 4→Eq. 6), but the algorithm uses a fixed λ hyperparameter rather than updating λ as a Lagrange multiplier. This is more accurately described as the penalty method. However, the derivation from Eq. (6) to the actual algorithm (Eq. 13) is mathematically sound: the term \(\min_{W_P} L(W_P;P,\mathcal{D}^{bal})\) does not depend on \(W\), so its gradient is 0, and the remaining gradient is exactly \(g_{\text{local}} + \lambda g_{\text{bal}}\). The reviewer's claim that "the algorithm does not attempt to solve this constrained problem" is incorrect — the algorithm does follow from Eq. (6). The issue is purely presentational: the paper should frame this as a penalty method rather than invoking Lagrange multipliers, which would be more precise.

2. **Staleness of global gradient prototypes is not analyzed.** The global gradient prototypes are computed on the model from two rounds ago (\(W^{t-2}\)). Gradients depend on the current model's predictions and can change as training progresses. While the paper partially addresses this through gradient normalization (Eq. 13) to prevent stale prototypes from dominating in scale, it provides no analysis of directional staleness — e.g., measuring cosine similarity between \(g^{\text{pro}}_{W^{t-2},c}\) and the true gradient at round \(t\), or comparing with prototypes computed on the current round. The paper would be strengthened by such an analysis, especially to characterize settings where staleness might cause issues (e.g., more aggressive non-i.i.d. shifts or larger numbers of local epochs).

3. **No comparison with FEDIC.** FEDIC (Shang et al., 2022a) is discussed in related work but not included as a baseline. While the paper notes FEDIC requires an auxiliary balanced dataset (making it less practical), a comparison would help contextualize RedGrape's performance against the full landscape. The authors should either add the comparison or explicitly justify its exclusion.

4. **Privacy implications of gradient prototypes are not discussed.** Sending per-class gradient prototypes from each client reveals which classes the client possesses (or at least aggregate gradient information per class). This is a meaningful privacy leak that the paper does not address, especially given that the method criticizes Ratio Loss for requiring an impractical auxiliary dataset. The communication overhead (one vector per class per sampled client) should also be reported.

5. **The claim about instance-balanced encoder training is slightly over-stated.** The paper argues that the supplementary classifier enables the encoder to be trained under an instance-balanced paradigm. This is mostly true — the encoder's gradients come from instance-balanced batches (Eq. 7). However, since \(W\)'s updates include the re-balancing gradient, there is an indirect second-order effect on the encoder through the shared representation in subsequent steps. An ablation measuring representation quality (e.g., linear probe on frozen features) would strengthen this claim, though the claim as stated is reasonable and the indirect effect is minor.

### Trivial
- The paper reports standard deviation over only 3 seeds. Acceptable for this setting, but 5+ would be more robust for stochastic FL.
- The MNIST-LT results are less informative due to the simplicity of the task; the CIFAR experiments are the main evidence.

## Nice-to-Haves
- An ablation isolating the role of global gradient prototypes vs. local real data individually (beyond the T=∞ condition which removes only local data, not prototypes).
- Testing under more extreme non-i.i.d. settings (e.g., Dir(α=0.1)) to verify gradient prototypes remain useful under stronger distribution shifts.
- Quantifying the number of communication rounds saved by the faster convergence (Figure 2).

## Removed Points
The following criticisms from the harsh reviewer were removed after cross-checking against the paper:

- **"λ is reported as 0, which is inconsistent with the algorithm"** — Removed. The text states "λ is fixed as 0," but the ablation study in Section 5.1 (Figure 3) definitively proves λ > 0: varying the threshold T produces different results, and T=∞ (removing local real data) degrades performance. If λ=0, the re-balancing term in Eq. (13) would vanish entirely and changing T would have no effect. The "0" is confirmed to be a PDF parsing artifact (likely a decimal was stripped). Similarly, the ablation in Section 5.2 (Figure 4) describes "Ours w/o Extra Classifier" as still applying re-balancing via Eq. (13), which requires λ > 0.

- **"The algorithm does not attempt to solve the constrained problem / no minimization over W_P"** — Removed. The term \(\min_{W_P} L(W_P;P,\mathcal{D}^{bal})\) does not depend on the optimization variables \((P,W,\widehat{W})\), so its gradient is 0 and it correctly drops out of the gradient computation. The derivation from Eq. (6) to Eq. (13) is mathematically valid.

- **"The penalty term is never explicitly instantiated"** — Removed. The penalty term's role is to add the balanced-dataset gradient to the W update, which is exactly what the algorithm does via \(g_{\text{bal}}\) in Eq. (13).

- Various pure formatting/style nitpicks removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the general tension between theoretically principled framing and practical heuristic design in FL optimization, but this is a well-known trade-off rather than a novel observation.

## Suggestions

1. Reframe the optimization in Section 3.2 as a penalty method rather than Lagrange multipliers to align the theoretical narrative with the actual algorithm.
2. Add an analysis of gradient prototype staleness (e.g., cosine similarity between stale and current gradients across rounds) to characterize when the approximation is valid.
3. Include an ablation that measures representation quality (e.g., linear probe on frozen features) to directly support the claim that the encoder learns balanced representations.
4. Acknowledge and discuss the privacy implications of sharing per-class gradient prototypes, and report the communication overhead.
5. Correct the reported λ value (which is clearly a parsing artifact) and include a sensitivity analysis over λ in the final version.

## Score and Decision

The paper tackles an important problem and presents a well-designed method with consistently strong empirical results. The core ideas — decentralized classifier re-balancing using local real data plus gradient prototypes, and the two-stream classifier architecture — are novel and validated by careful ablations. The weaknesses (imprecise theoretical framing, unanalyzed prototype staleness, missing FEDIC comparison, privacy discussion) are all addressable and do not undermine the core contribution. The most concerning reviewer criticism (λ=0) is definitively a PDF parsing artifact, as confirmed by the paper's own ablation studies that require λ>0.

This is a solid paper that makes a clear empirical contribution to federated long-tailed learning.

MY FINAL SCORE: <pineapple>7</pineapple>
MY FINAL DECISION: <orange>Accept</orange>