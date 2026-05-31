## Summary

This paper presents a semi-supervised learning (SSL) framework for detecting illicit Bitcoin Shared Send Mixer (CoinJoin) transactions. It contributes (1) a comprehensive dataset of 163 million CoinJoin transactions over Bitcoin's full history, (2) two novel domain-specific forensic features — KeyLinker (address clustering via cryptographic key reuse) and SSU complexity metrics — and (3) an empirical demonstration that quality-focused pseudo-labeling outperforms volume-focused pseudo-labeling, establishing a "quality over quantity" principle for SSL in blockchain forensics.

---

## Strengths

- **Large-scale, practically valuable dataset.** With 1.15 billion total transactions and 163 million CoinJoin transactions, this is the most comprehensive historical Bitcoin forensics dataset described in the academic literature. The integration of multiple off-chain label sources (WalletExplorer, Elliptic++, MBAL, Kaggle) and careful deduplication represents substantial engineering effort with real utility for the field.

- **Empirically supported quality-over-quantity thesis.** The ablation across Table 2 (supervised) consistently shows that adding OTC features degrades all models (e.g., XGBoost F1 drops from 0.844 to 0.841 when OTC is added, and to 0.821 when SSU is also included with OTC). This pattern holds across all three model families, providing reasonable multi-model evidence for the central claim that heuristic noise matters.

- **Domain-motivated feature engineering.** KeyLinker's grounding in cryptographic public-key reuse (rather than behavioral inference) makes it a genuinely higher-fidelity clustering signal compared to the behavioral OTC heuristic. The SSU complexity classification provides a principled, computationally-motivated taxonomy of transaction tractability that is well-suited to guide pseudo-label quality filtering.

---

## Weaknesses

### Fatal
None.

### Major

1. **SSL improvements over supervised baselines are negligible, undermining the central SSL claim.** The abstract prominently reports "F1-score: 0.84" for the SSL framework, but the best supervised XGBoost also achieves F1 = 0.845 (Table 2) while the best SSL XGBoost achieves F1 = 0.845 (Table 3). The paper itself acknowledges "the semi-supervised phase did not produce dramatic metric gains" and that pseudo-labeling yields only "+0.03 recall" gains offset by "-0.04 to -0.05 precision" reductions. The paper's framing that "SSL effectively leverages unlabeled data" is not substantiated by the numbers; at best, SSL preserves performance parity while slightly shifting the precision-recall tradeoff.

2. **Critical ambiguity and apparent duplication in reported experimental results.** Tables 2 and 3 contain rows where all five feature flags are shown as checked (✓ ✓ ✓ ✓ ✓) for multiple consecutive entries in each model block. In Table 3, the last two rows for CatBoost (both 0.874/0.788/0.829/0.966), XGBoost (both 0.890/0.787/0.836/0.967), and RandomForest (both 0.872/0.768/0.817/0.960) are identical. This suggests either a rendering failure that stripped feature distinguishers, or that the same results were reported twice. This ambiguity makes it impossible to fully reconstruct which feature combinations were tested and whether the reported best results correspond to the high-quality feature subsets as claimed.

3. **No external baseline comparison for the core classification task.** The paper benchmarks only internal feature ablations. It does not compare against prior CoinJoin/mixing-service detection methods (e.g., Rathore et al. 2022 reporting 97% detection, or Lin et al. 2022 reporting 87% accuracy), making it impossible to assess whether the proposed features and framework represent genuine progress over the state of the art.

4. **The pseudo-labeling mechanism is standard and underspecified.** The SSL method is described as "top fraction of samples on both sides of the decision boundary" but the exact fraction, the number of iterations, and the selection criterion for stopping are not specified. No comparison with alternative SSL techniques (e.g., self-training with consistency regularization, label propagation on the transaction graph, GNN-based SSL which is directly applicable here) is provided. For an ML venue, a single-iteration top-confidence pseudo-labeling scheme without alternative SSL baselines is insufficient to make claims about SSL methodology.

### Minor

1. The "quality over quantity" thesis, while empirically supported by ablations, lacks any theoretical grounding or analysis of pseudo-label accuracy. The paper asserts that OTC introduces "noise" but does not measure the noise level (e.g., by evaluating pseudo-label accuracy on a held-out labeled subset), so the mechanism is inferred from downstream F1 rather than demonstrated directly.

2. The 12% illicit rate in the labeled set is noted but it is unclear whether this reflects the true prior in unlabeled CoinJoin transactions, potentially affecting how well precision-recall metrics on the labeled test set reflect real-world deployment performance.

### Trivial

- The paper's claim to "prove" in the abstract is stronger than what is demonstrated; "empirically show" would be more accurate.

---

## Nice-to-Haves

- A pseudo-label accuracy analysis (comparing pseudo-labels to ground truth on a held-out labeled portion of the unlabeled pool) would directly substantiate the "quality" claims about OTC vs. KeyLinker, rather than inferring it only from downstream test F1.
- Including a comparison with at least one graph-based SSL baseline (e.g., label propagation on the Bitcoin transaction graph) would strengthen the methodological positioning at an ML venue.
- Reporting confidence intervals or standard deviations across cross-validation folds would improve statistical rigor given the marginal SSL improvement claims.

---

## Novel Insights

The paper's most genuinely novel observation is that the SSU transaction-complexity taxonomy (simple, separable, ambiguous, time-limited) can serve as an intrinsic data-quality signal for filtering pseudo-labels — i.e., that the computational tractability of untangling a CoinJoin transaction is predictive of the reliability of its inferred label. This insight, that domain-specific structural complexity serves as a proxy for labeling difficulty, is a useful contribution to applied SSL in adversarial settings. However, the empirical support for this specific mechanism is entangled with the KeyLinker effect, and the two are never disentangled to show each feature group's independent contribution to SSL quality.

---

## Suggestions

- Separately ablate the pseudo-labeling quality filters: run pseudo-labeling using (a) only SSU-based filtering, (b) only KeyLinker-based filtering, and (c) standard confidence-threshold-only filtering, to isolate which quality signal drives the benefit.
- Fix the duplicate rows in Tables 2 and 3 and clearly annotate what feature combination each row represents, including the specific KeyLinker vs. no-KeyLinker distinction within the OTC rows.
- Report pseudo-label noise estimates: apply the trained classifier to a withheld labeled subset, generate pseudo-labels, and report how OTC vs. KeyLinker-filtered pseudo-labels differ in accuracy from the ground-truth labels.

---

## Score and Decision

The paper addresses a real problem with a large-scale dataset and provides clear empirical evidence that feature quality matters for pseudo-labeling. However, the SSL performance gains over supervised baselines are effectively zero, the experimental tables contain unresolved duplicate/ambiguous entries, the SSL methodology is standard with no comparison to alternatives, and there is no external benchmark comparison. For an ML venue like ICLR, the ML methodological contribution is thin, and the empirical demonstration of the central SSL claim is too weak relative to the framing.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>