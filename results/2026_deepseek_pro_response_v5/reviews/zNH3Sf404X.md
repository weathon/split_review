Now let me finalize the review. Let me compile all anchor comparisons and write the final review.

## Round 1 Bracket

Based on the Round 1 anchors:
- **Strong reject (≤2.5)**: Papers at 1.0–1.8 — clearly flawed or incomplete papers (e.g., superficial LLM-based stock prediction, poorly executed financial forecasting). The paper under review is substantially better than these.
- **Weak reject (2.5–4.5)**: FE-GNN (4.25), Temporal-Spatial GCN (4.0), EGLNN (3.5) — blockchain ML papers with incremental methods, missing baselines, or weak evaluations. Our paper is stronger than these due to dataset scale and systematic ablation.
- **Middle (4.5–6.1)**: BlockFound (5.75), Better Call Graphs (5.25), Data Poisoning (5.50) — papers with genuine contributions but notable limitations. Our paper falls in this range.
- **Middle-high (6.0–7.5)**: SSL theory papers (6.5–7.0) — our paper lacks the theoretical depth of these.
- **Strong accept (7.5+)**: Papers with strong theory and comprehensive evaluation (8.0) — our paper is clearly below these.

**Round 1 Bracket: 4.0–5.5**

## Round 2 Narrowing

Focused on 3.5–5.5 range. Additional anchors: FE-GNN (4.25), Probabilistic GCN (4.0), S2MAM (4.75), DIPS pseudo-labeling (5.00), Two-sample testing SSL (4.80).

After comparing against these:
- Our paper is **better than** FE-GNN (4.25): larger dataset, more systematic ablation, broader model comparison
- Our paper is **comparable to or slightly below** DIPS (5.00): DIPS has a cleaner methodology and more honest framing, but our paper has a larger-scale empirical contribution  
- Our paper is **comparable to** BCG (5.25): both are dataset-heavy papers with empirical evaluation; BCG has cleaner claims, our paper has more comprehensive experiments but also overclaiming

Final assessment: the paper's central SSL outperformance claim is not supported by its own results — this is a significant weakness that prevents acceptance. However, the dataset contribution and feature ablation experiments have genuine value. Score: **4.5**.

---

## Summary
This paper presents a large-scale dataset of Bitcoin CoinJoin transactions (1.15B total, 163M CoinJoin, 4.6M labeled) and evaluates feature engineering for illicit transaction detection using supervised and semi-supervised learning. The authors compare five feature groups (DEFAULT, REUSE/KeyLinker, CS, OTC, SSU) across XGBoost, CatBoost, and Random Forest in both supervised and SSL settings. The strongest empirical result is the consistent finding that One-Time Change (OTC) features degrade detection performance despite their broad coverage, while higher-fidelity features like KeyLinker and SSU improve it. However, the paper's claim that the SSL framework "outperforms" supervised baselines is not supported by the results.

## Strengths
- **Comprehensive feature ablation across three model families**: Tables 2 and 3 present a systematic evaluation of seven feature combinations across XGBoost, CatBoost, and Random Forest, cleanly isolating each feature group's marginal contribution in both supervised and semi-supervised settings.
- **Robust, cross-setting evidence that OTC features are harmful**: The finding that OTC degrades performance holds consistently across all three model types and both learning paradigms. In supervised XGBoost, adding OTC to Default+REUSE+CS drops F1 from 0.844 to 0.841 (Table 2); in SSL XGBoost the same addition drops F1 from 0.839 to 0.836 (Table 3). The same degradation appears for CatBoost and Random Forest.
- **Large-scale, transparently documented dataset**: Table 1 provides detailed accounting of dataset composition — 1.15B total transactions, 163.4M CoinJoin transactions, 4.6M labeled — with breakdowns by SSU complexity class and heuristic coverage. The dataset spans full Bitcoin history through block 882,421 (February 2025), and the authors commit to public release (line 199).

## Weaknesses

### Major
- **Central claim of SSL "outperforming" supervised baselines is not supported by the results.** The best supervised XGBoost achieves F1=0.844 (Default+REUSE+CS, Table 2); the best SSL XGBoost achieves F1=0.845 (Default+REUSE+CS+SSU, Table 3). These are effectively identical. When comparing the same feature set (Default+REUSE+CS) across settings, SSL _degrades_ performance (0.839 vs. 0.844). The introduction claims "a semi-supervised learning framework outperforms supervised baselines" (line 29), but the evidence shows at best parity. Section 6.3 partially acknowledges this ("did not produce dramatic metric gains"), but the framing throughout the paper remains misleading. This undermines contribution #3 as stated.

### Minor
- **The "data quality over data quantity" thesis is tested only at the feature level, not the data level.** The experiments demonstrate that higher-fidelity features (KeyLinker, SSU) outperform noisier ones (OTC) when applied to the same dataset. This is a feature-quality comparison, not a test of whether a smaller volume of high-quality data beats a larger volume of low-quality data. The paper's title and conclusion ("models trained on strategically expanded high-quality data outperform those trained on larger, noisier datasets," line 331) promise a comparison the experiments do not directly deliver. No experiment varies training set size while holding quality fixed, or vice versa.
- **"Novel features" claim is overstated.** The paper describes KeyLinker (Smolenkova & Yanovich, 2025) and SSU metrics (Larionov & Yanovich, 2023) as "novel, high-fidelity features" (line 9), but both techniques are prior published work. The novelty lies in their _application_ as features in an ML pipeline on this dataset, not in the feature extraction methods themselves.
- **Pseudo-labeling selects for easy examples without discussing the circularity.** Sections 5.2 and 6.3 state that pseudo-labels are preferentially drawn from SSU Simple and Separable classes — the transactions easiest to classify. The supervised classifier already handles these well, so pseudo-labeling augments training with redundant easy examples rather than informative hard ones. This selection bias plausibly explains the null SSL result, but the paper never discusses the limitation.
- **Pseudo-labeling procedure lacks basic reproducibility details.** The paper states only that "the top fraction of samples" is selected while "adjusting the share of positives and negatives" (Section 5.2). No specific fraction, batch size, number of iterations, final count of pseudo-labeled examples, or pseudo-label accuracy estimate is reported.
- **No standard deviations or confidence intervals reported.** Tables 2 and 3 present single-point metrics despite using 5-fold cross-validation, making it impossible to assess whether small differences (e.g., F1=0.844 vs. 0.845) are statistically meaningful.
- **Feature group mapping is underspecified.** Section 5.1 describes four feature groups (UTXO attributes, transaction values, address-level behavior, specialized attributes, lines 201–202) but never maps them to the abbreviations used in Tables 2–3 (DEFAULT, REUSE, CS, OTC, SSU). The reader must infer what DEFAULT contains and how REUSE/CS/OTC/SSU correspond to the described groups.

### Trivial
- **Possible miscitation in related work.** Lee et al. (2024) is cited for the CENSor hypergraph-based illicit transaction detection model (line 137), but the bibliographic entry describes an NFT rarity analysis study on the BAYC collection (line 379–381). If this is the intended reference it appears irrelevant; if not, the citation may be incorrect.

## Nice-to-Haves
- A label-scarcity experiment (e.g., training on 1%, 5%, 10% of labels and showing SSL recovery toward the supervised baseline) would more directly test whether SSL addresses the label-scarcity problem stated in the introduction.
- Reporting pseudo-label accuracy on the test set and the number of pseudo-labeled examples added would strengthen the SSL contribution.
- Comparison against at least one published method from the related work section (e.g., the 8-feature decision tree approach of Rathore et al. 2022) would contextualize results, even if on different data.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **HC: Duplicate rows in Table 3 are a formatting error** — REMOVED. The duplicate rows (lines 307–309, 316–317, 324–325) are parser artifacts from the PDF extraction process, not errors in the original paper. The instruction explicitly states that formatting/parser artifacts should not be held against the paper.
- **HC: Irrelevant Lee et al. (2024) reference is a parser artifact** — RETAINED as trivial. While the reference mismatch exists in the extracted text, the instruction to treat all cited references as existing and real means this is noted as a minor bibliographic inconsistency, not a substantive flaw.
- **SF: "Honest empirical self-assessment"** — REMOVED as a standalone strength. While Section 6.3 does acknowledge limited SSL gains, this candor is undercut by the abstract and introduction's stronger claims of SSL outperformance. The tension between the abstract's claims and Section 6.3's candor makes "honesty" an inconsistent characterization.
- **SF: "Formal problem definition with precise mathematical notation"** — REMOVED. The notation in Section 4 (lines 148–165) is standard for a machine learning paper and does not rise to the level of a notable strength; most empirical ML papers include a comparable problem formulation.
- **HC: Lee et al. (2024) being about NFT not blockchain forensics** — RETAINED as trivial (see above).

## Novel Insights
The paper's most instructive finding — consistent across three model types and two learning paradigms — is that the One-Time Change heuristic, despite covering 472.3M addresses (Table 1), is a net negative for illicit CoinJoin transaction detection. This is practically significant because OTC is widely used in blockchain analytics and is often assumed helpful; the paper provides systematic evidence to the contrary. This finding has implications beyond the paper's specific framework for anyone building blockchain forensic feature pipelines.

## Suggestions
- Reframe the SSL contribution honestly: the paper shows that quality-guided SSL _matches_ supervised performance while being more selective about which unlabeled data to use — a defensible and interesting finding that does not require claiming "outperformance."
- Add a label-scarcity experiment to actually test whether SSL helps when labels are scarce, which is the motivation stated in the introduction.
- Specify the exact composition of each feature group abbreviation (DEFAULT, REUSE, CS, OTC, SSU) with a clear mapping table to the four feature groups described in Section 5.1.
- Report variance estimates (standard deviations across CV folds) for all metrics in Tables 2–3.
- Discuss the circularity in pseudo-label selection (easy examples reinforcing existing model strengths) as a limitation.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| LLM Stock Prediction | ICwdNpmu2d | 1.50 | R1 | Paper is substantially stronger |
| FE-GNN (Ethereum GNN) | yM7rw8Bo1f | 4.25 | R1/R2 | Paper has larger dataset, more systematic ablation |
| Temporal-Spatial GCN | 6yXAKleluj | 4.00 | R1/R2 | Paper is stronger methodologically |
| EGLNN | k9KKFhwNwg | 3.50 | R1 | Paper is clearly stronger |
| BlockFound | LPXfOxe0zF | 5.75 | R1 | More sophisticated methodology (foundation model); paper is weaker |
| Better Call Graphs | nwjgeFGbAF | 5.25 | R1 | Comparable dataset contribution; paper has more experiments but overclaims |
| Data Poisoning Defense | rK0YJwL69S | 5.50 | R1 | Paper is weaker (less methodological depth) |
| S2MAM (SSL theory) | dpnPOXoqVQ | 4.75 | R2 | Different type; paper has larger empirical scope |
| DIPS (Pseudo-labeling) | eSO9quCgmz | 5.00 | R2 | Comparable level; DIPS has cleaner framing |
| OOD Unlabeled Data | Bo6GpQ3B9a | 7.00 | R1 | Paper is clearly weaker (no theory) |
| MPU AI-Text Detection | 5Lp6qU9hzV | 6.50 | R1 | Paper is weaker |
| FixMatch Theory | 25kAzqzTrz | 8.00 | R1 | Paper is substantially weaker |

**Round 1 bracket**: 4.0–5.5  
**Round 2 narrowing**: The paper is closest to FE-GNN (4.25) and DIPS (5.00). It has a stronger dataset than FE-GNN but weaker methodological framing than DIPS. The unsupported SSL outperformance claim is the decisive factor pulling the score below the 5.0 threshold. **Final score: 4.5.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>