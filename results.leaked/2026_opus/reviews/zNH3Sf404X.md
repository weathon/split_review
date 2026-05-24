Based on my analysis of the paper and verification against the reviews, I'll now write the consolidated review.

## Summary
The paper introduces a semi-supervised learning framework for detecting illicit Bitcoin flows within CoinJoin Shared Send Mixer (SSM) transactions. It contributes (i) a 163M-transaction CoinJoin dataset with SSU complexity classification, (ii) the integration of KeyLinker address clustering and Shared Send Untangling complexity metrics into a feature pipeline, and (iii) a pseudo-labeling scheme reaching F1 ≈ 0.84 with XGBoost. The framing thesis is that data quality (via feature engineering) matters more than data quantity for SSL effectiveness.

## Strengths
- **Substantial dataset contribution.** Table 1 documents 163.4M CoinJoin transactions, 1.15B total transactions, 1.37B addresses, plus SSU complexity counts (Simple 99.1M, Separable 24.2M, Ambiguous 10.5M, Time-limit 5.4M, Regular 24.3M) integrated from WalletExplorer, Elliptic++, MBAL, and Kaggle datasets with manual conflict resolution. This corpus size and the explicit SSU stratification appear to exceed prior CoinJoin-specific resources and is the paper's most defensible contribution.
- **Consistent ablation pattern across configurations.** Across all three classifiers in both Tables 2 and 3, adding OTC features either fails to improve or actively reduces F1 relative to "Default+REUSE+CS+SSU", which provides directional support for the qualitative claim that OTC-clustered labels are noisier than KeyLinker-clustered ones.
- **Principled handling of imbalance.** Section 5.3 explicitly avoids SMOTE/ADASYN on the grounds that pseudo-labeling subsequently introduces new positive examples; combined with class-weighted loss, this is a coherent design choice for the 12% positive rate setting.
- **Encoding mixing complexity as features.** Section 4 formally defines `t → t_sim` with κ(t) ∈ {regular, simple, separable, ambiguous, time-limit} and feeds the SSU class into the model, going beyond standard UTXO-statistic features.

## Weaknesses

### Fatal
None. The paper's issues are serious but not unambiguously fatal given what is on the page.

### Major
- **Central "proof" claim is contradicted by the paper's own numbers.** Contribution (3) and the abstract claim SSL guided by quality features outperforms supervised baselines and "proves" that quality drives performance. But the best SSL XGBoost in Table 3 is F1 = 0.845 vs. supervised XGBoost in Table 2 at F1 = 0.844 — a 0.001 difference. Section 6.3 itself concedes "the semi-supervised phase did not produce dramatic metric gains." All inter-feature-set comparisons that ground the OTC-vs-KeyLinker thesis sit within 0.001–0.005 F1, and no standard deviations from the stated 5-fold CV, no confidence intervals, and no significance tests are reported. The narrative as written is not supported at the resolution the tables provide.
- **The "quality-aware" pseudo-labeling mechanism is not directly tested.** Section 5.2 lays out a principle for prioritizing SSU Simple/Separable transactions and KeyLinker-clustered addresses, but Section 5.3 and 6.3 describe a generic top-fraction-by-confidence rule with the observation that high-confidence samples "are disproportionately found in the more tractable SSU complexity classes." That is a passive consequence, not an active selection mechanism. The experiments vary the *feature set* (with vs. without OTC), not the *pseudo-label selection rule*. The paper's titular claim cannot be isolated from these ablations.
- **Label-propagation rule introduces an unaddressed leakage risk.** Section 4 explicitly states `A ~ A' ⇒ Tag(A) = Tag(A')`. The classification uses a stratified random 80/10/10 split over 4.6M labeled CoinJoin transactions (Section 5.3) with no mention that clusters (KeyLinker, CS, or OTC) are kept disjoint across splits. If clusters span splits, correlated label assignments inflate test metrics, and tighter clusters (e.g., KeyLinker) benefit more — which mechanically aligns with the paper's conclusion. Given that the entire "OTC noisy / KeyLinker good" claim rests on F1 differences of 0.003, ruling out cluster leakage is structurally necessary before that claim can be made.
- **No prior-art baseline on the new dataset.** The related work in Section 3 cites Nerurkar (2022) at 92%, Rathore et al. (2022) at 97%, Alarab et al. (2020), CENSor (Lee et al., 2024), and metapath GNNs (Song & Gu, 2023). None is reproduced on the proposed dataset. The proposed framework is compared only against itself (XGBoost vs. CatBoost vs. RF on the authors' features). The 0.84 F1 is therefore not anchored against any externally proposed method.

### Minor
- **Novelty framing.** The Introduction lists "KeyLinker address clustering and Shared Send Untangling (SSU) complexity metrics" as contributions of this paper, but Sections 2.3 and 5.1 cite Smolenkova & Yanovich (2025) for KeyLinker and Larionov & Yanovich (2023) for SSU. The actual original contribution is integrating these into a pipeline and producing the dataset; the framing inflates novelty.
- **"Extreme class imbalance" vs. 12% positives.** Section 6 reports illicit CoinJoin at ~12% — moderate imbalance routinely handled by class weighting, which the paper uses. The abstract's "extreme class imbalance" overstates the problem.
- **Pseudo-labeling procedure under-specified.** Section 5.3 describes selecting "the top fraction of samples on both sides of the decision boundary" but does not specify number of rounds, retention fraction, positive/negative balance, or stopping criterion. Given the headline effect sizes are very small, these details matter.
- **Conflict-resolution rule.** Section 4's tag-propagation rule does not specify what happens when two clustered addresses carry conflicting external tags (e.g., mixer vs. exchange). Section 5.1 mentions "manually resolved" conflicts; the rule is not formalized.

### Trivial
- The bolded "best results" rows in Tables 2 and 3 are inconsistent across models, making it hard to identify which row is "the" headline result for each classifier without close inspection.

## Nice-to-Haves
- A direct ablation that holds the feature set fixed and varies only the pseudo-labeling rule (vanilla confidence-top-k vs. confidence-top-k restricted to SSU Simple/Separable vs. restricted to KeyLinker-clustered addresses), with seeds/folds standard deviations reported. This would actually isolate the quality-aware SSL claim.
- A label-level analysis: quantify the disagreement rate between OTC-clustered addresses' propagated tags and ground-truth tags vs. the same for KeyLinker, independently of downstream F1. This would provide a sharper evidentiary basis for the "data quality" thesis than 0.003 F1 differences.
- Reproduce one or two prior-art methods (Rathore-style decision tree, gradient-boosted feature baselines from Alarab et al., or a GNN approach) on the new dataset to anchor the 0.84 figure.
- Re-run with cluster-disjoint train/val/test splits to confirm the OTC-vs-KeyLinker conclusion is not an artifact of label propagation across splits.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Identical checkmark patterns with different metric values in Tables 2 and 3" (harsh critic).** The last three rows of each XGBoost block in Table 2 all appear to have all five feature columns checked but different F1s (0.821, 0.842, 0.840). On verification, this is almost certainly a parsing artifact of the PDF→text conversion — the original LaTeX likely uses different subsets that the table-extraction tool collapsed to "all checked." Per the guidance, formatting/parser artifacts are not author errors.
- **"Recall improvements without operating-point analysis" (harsh critic).** The +0.03 recall / −0.04 precision trade-off discussion is a standard textual summary; demanding precision-recall curves for an applied paper of this scope is a nice-to-have rather than a substantive flaw.
- **Strength: "explicit problem formulation incorporating untangling complexity classes" (Strength Finder).** Already captured under "Encoding mixing complexity as features"; merged to avoid double-counting.
- **Strength: "demonstration that SSL with quality-focused features outperforms SSL with noisy features"** (Strength Finder). The supporting evidence (0.845 → 0.836 F1 in Table 3) is within the same magnitude as the noise concerns raised under the major weaknesses, so this strength conflicts with a verified weakness. Demoted.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel artifact is the dataset itself (163M CoinJoin transactions with SSU complexity classes labeled). The "quality-aware SSL" framing, by contrast, is a research direction the paper points toward but does not isolate experimentally.

## Suggestions
- Reframe the paper around the dataset, with detailed label provenance, splits designed to avoid cluster leakage, and reproduced prior-art baselines on the new corpus. Position the SSL pipeline as a starting baseline for users, not as "proof" of a general principle.
- Add cluster-disjoint train/val/test partitioning given the explicit `A ~ A' ⇒ Tag(A) = Tag(A')` propagation rule, and report results both ways so readers can see how much leakage contributed.
- Replace the "proof"/"Crucially, we prove" language in contribution (3) and the abstract with weaker, evidence-appropriate phrasing; report mean ± std across folds/seeds for every feature-set row.
- Run a direct pseudo-labeling-rule ablation (hold features fixed; vary the rule) to isolate the actual mechanism the paper is named after.
- Re-evaluate whether two of the three "novel features" should be presented as integrations of prior work (Smolenkova & Yanovich 2025; Larionov & Yanovich 2023) rather than as contributions of this paper.

## Axis Assessment
- **Originality:** Moderate. The dataset is novel and substantial; the methodology repackages existing components (KeyLinker, SSU, standard pseudo-labeling, off-the-shelf ensembles).
- **Importance of question:** High. Detecting illicit flows through Bitcoin mixers is a real forensic problem with limited reliable labels.
- **Claim support:** Weak. The central "quality drives SSL" claim is undermined by Section 6.3's own admission and by sub-0.005 F1 effect sizes without variance estimates.
- **Soundness of experiments:** Mixed. Ablations are systematic but cannot test what the paper claims to test, label propagation interacts with random splits in an unaddressed way, and there are no external baselines.
- **Clarity:** Acceptable. The dataset, features, and pipeline are described clearly enough to follow; the pseudo-labeling procedure is under-specified.
- **Value to community:** Real but depends on the dataset actually being released as promised. The methodological story as currently written contributes less.

## Calibration Anchors

Round 1 — Bracketing:
- `q7Xi4yZYcH.md` (avg 3.00, weak band) — Ethereum GNN anomaly detection, rejected. Comparable applied-blockchain ML scope; the paper under review is stronger due to dataset breadth.
- `aXSxSu3fvg.md` (avg 3.00, weak band) — SSL with heuristic early stopping; orthogonal topic.
- `yM7rw8Bo1f.md` (avg 4.25, middle band) — FE-GNN Ethereum account classification; most directly comparable: applied blockchain ML with empirical contributions, criticized for incremental novelty and no significance tests.
- `X8RTdxzqJQ.md` (avg 4.80, middle band) — Two-sample testing as SSL; methodological, not topical.
- `dpnPOXoqVQ.md` (avg 4.75, middle band) — SSL meta additive model; methodological.
- `6yXAKleluj.md` (avg 4.00, middle band) — Ethereum transaction anomaly TRW-GCN; comparable applied blockchain scope, weaker execution than the paper under review.
- `IGzaH538fz.md`, `KbetDM33YG.md`, `P7KIGdgW8S.md`, `uKZdlihDDn.md` (avg ≥7.6, strong band) — Theoretical GNN/diffusion papers; not topically comparable; clearly stronger contributions than the paper under review.

Round-1 bracket: between **3.5 and 5.0**, anchored most tightly on FE-GNN (4.25) and the Ethereum anomaly papers (3.00, 4.00).

Round 2 — Narrowing:
- `1ymGFnxfVB.md` (avg 4.75) — LJ-Bench ontology benchmark; different domain, similar reviewer concerns.
- `nwjgeFGbAF.md` (avg 5.25) — Better Call Graphs malware FCG dataset; close comparator (dataset-centric paper) but has reproduced baselines, which the paper under review lacks.
- `y9tQNJ2n1y.md` (avg 5.25) — CASE-Bench safety benchmark; different domain.
- `ZXO7iURZfW.md` (avg 5.25) — AutoFE by prompting; methodological feature engineering paper.
- `cNThpik3Jz.md` (avg 4.50) — LLMs as data scientists; benchmark paper.
- `0bjIoHD45G.md` (avg 4.20) — Tabular Fourier + implicit categorical features; methodological.
- `TXjYOslkUh.md` (avg 4.50) — Distribution-shift-aware feature transformation; methodological.

The paper under review is closest in profile to FE-GNN (4.25) and BCG (5.25) but materially weaker than BCG because BCG runs prior-art baselines on the proposed dataset while the paper under review does not. The paper under review's methodological overclaiming (calling sub-0.005 F1 differences "proof") and unaddressed label-leakage risk pull it below FE-GNN, whose main issue was just incremental novelty.

Final placement: ~**3.5**, between the 3.00 anchors (clear rejects with incomplete or unsupported empirical work) and the 4.00–4.25 anchors (rejected but reasonable applied blockchain ML papers). The dataset effort prevents a lower score; the overclaimed thesis and missing baselines prevent landing at 4.0+.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>