Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper identifies and addresses a model collapse phenomenon in DCCA-based multi-view representation learning, where performance degrades sharply during training. The authors propose NR-DCCA, a noise regularization method that enforces a Correlation Invariant Property (CIP) — the idea that correlation with random noise should be invariant under the learned transformation. They prove that CIP is equivalent to full-rank weight matrices for a linear transformation (Theorem 1), and argue that forcing this property in deep networks prevents the weight matrices from becoming low-rank, which they hypothesize is the root cause of collapse. The paper also introduces a synthetic data generation framework with controlled "common rate" between views. Experiments on synthetic data and three real-world datasets (PolyMnist, CUB, Caltech) show NR-DCCA outperforming DCCA variants.

## Strengths

1. **Novel problem identification:** The paper is the first to identify and systematically analyze model collapse in DCCA-based methods. The observation that DCCA's representations can be full-rank while its weight matrices become low-rank (Section 4, ReLU example, Figure 1 eigenvalue decay) goes beyond prior literature (Andrew et al., De Bie) that only examined representation rank. This is a genuinely useful insight for the MVRL community.

2. **Simple and intuitive method with strong synthetic evidence:** The noise regularization approach is straightforward and well-motivated. On synthetic data, Figure 3(a) convincingly shows that NR-DCCA maintains stable accuracy across training epochs while DCCA, DCCAE, and DCCA_PRIVATE all collapse. This is the most compelling evidence in the paper — it directly demonstrates both the collapse phenomenon and the proposed remedy on controlled data.

3. **Synthetic benchmark framework:** The "God Embedding" construction with controllable common rate (Definition 1) is a practical contribution that could benefit the broader MVRL community by enabling controlled evaluation of how well methods handle varying degrees of shared vs. view-specific information.

4. **Generalizable approach:** The paper demonstrates that the NR approach can be applied to DGCCA (Deep Generalized CCA) in addition to DCCA, which suggests broader applicability beyond the specific architecture tested.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical justification does not extend to deep nonlinear networks.** Theorem 1 is correctly stated and proven for a single linear square matrix $W_k$: CIP $\iff$ $W_k$ is full-rank. However, the paper then applies this reasoning to deep neural networks $f_k$ composed of multiple nonlinear layers (often with non-square weight matrices). The claim that "by forcing $f_k$ to possess CIP... the NR approach constrains the weight matrices to be full-rank and less redundant" (line 232) is never justified for the composition case. For a nonlinear $f_k$, $\zeta_k = 0$ does not imply that any individual internal weight matrix is full-rank — it only constrains the input-output behavior on two specific sets (data $X_k$ and noise $A_k$). The paper provides no bridge from this compositional constraint to the rank of internal weight matrices. This is a structural gap between the theoretical claims and the actual setting of DCCA.

2. **Evidence of model collapse on real-world datasets is weak.** On synthetic data, the paper shows learning curves (Figure 3a) that directly demonstrate performance degradation over time. On real-world datasets (PolyMnist, CUB, Caltech), however, only static bar plots of final F1 scores are presented (Figure 4). Without seeing performance over training epochs, the reader cannot determine whether DCCA actually collapsed during training on these datasets, or whether NR-DCCA prevented collapse — only that the final scores differ. The paper acknowledges that "DCCA-based methods exhibit varying degrees of collapse on various datasets" (line 376), but the reader has no way to verify this or assess the training dynamics from the presented evidence.

### Minor

3. **Missing experimental details for reproducibility.** The paper does not report: (a) the number of training epochs for real-world experiments, (b) whether all methods received the same training budget, (c) the hyperparameter $\alpha$ values used per dataset or the tuning procedure, (d) learning rate and optimizer settings, or (e) whether results are averaged over multiple random seeds (as opposed to just 5-fold CV). Without these details, the real-world results cannot be reproduced or properly assessed.

4. **Potential confound in synthetic benchmark.** The synthetic data defines downstream tasks as functions of the full "God Embedding" $G$ ($T_j = \psi_j(G)$), while each view observes only a partial slice of $G$. Theorem 2 shows that full-rank weight matrices (CIP) lead to low reconstruction loss. This creates a possible coupling: methods that preserve view-specific information (and thus achieve lower reconstruction loss) may also do better on tasks that depend on the full $G$ — independent of whether they prevent collapse. The paper does not control for this by, e.g., testing downstream tasks that depend only on the common information across views. That said, this concern is somewhat mitigated by the fact that DCCAE (which explicitly optimizes reconstruction) still underperforms NR-DCCA on this benchmark, suggesting the advantage is not purely reconstruction-driven.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis for the hyperparameter $\alpha$ across a range (e.g., 0.01, 0.1, 1, 10) on synthetic data would strengthen claims of robustness and provide practical guidance.
- Learning curves (performance vs. epoch) for at least one real-world dataset would substantially strengthen the main claim.
- A clearer definition of the NESum metric used in Figure 3(c) should be provided in the main text.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Insufficient experimental detail on real-world datasets" — the harsh critic's version mentions number of epochs, same epochs for all methods, early stopping. The paper does not state these. KEEP (moved to Minor weakness #3 above, as it is legitimate).
- *"The paper does not discuss failure cases" — this is a general area sweep, not a specific identified problem. REMOVED.
- *"The paper does not include comparison to Linear CCA on real data" — the paper's bar plots include Linear CCA (it's one of the baselines in the real-world experiments). This is factually wrong. REMOVED.
- *"The synthetic data framework may advantage the proposed method" — the harsh critic argued that methods with reconstruction loss are favored. However, DCCAE explicitly optimizes reconstruction loss and still underperforms NR-DCCA, which undercuts this criticism. KEPT as Minor #4 with the counterargument included.
- *Strength Finder claims about "theoretical proof linking CIP to full-rank weight matrices" being a core strength — this is retained in Strengths but qualified in Weaknesses #1.
- *Strength Finder claim that NR-DCCA "effectively prevents collapse on both synthetic and real datasets" — the synthetic evidence is strong. The real evidence is weak (no learning curves). Kept as a qualified strength.
- *"Code availability not mentioned" — REMOVED per hard rules (do not question availability of cited resources).
- *"Include non-CCA deep MVRL method as baseline" — this is scope creep. The paper explicitly focuses on DCCA-based methods. REMOVED.
- *"Missing related works" — REMOVED per hard rules.
- *"Training details for real datasets must be reported" — KEPT as Minor #3.

## Novel Insights

The two reviews largely converge on the paper's strengths (novel problem identification, simple and plausible method, strong synthetic evidence) and weaknesses (theory does not extend to deep networks as claimed, insufficient real-world training dynamics evidence). The harsh critic also raised a useful point about a potential confound in the synthetic benchmark (conflating reconstruction with collapse prevention), though this concern is partially mitigated by DCCAE's weaker performance despite its explicit reconstruction objective. The most important insight that emerges from synthesizing both reviews is that the paper's central claim — that NR prevents collapse by keeping weight matrices full-rank — rests on a theoretical result (Theorem 1) that is correctly proven for linear transformations but not established for the deep nonlinear setting where it is applied. Closing this gap (or honestly retreating to a heuristic justification) and providing real-world learning curves would transform this from a promising-but-incomplete paper to a strong contribution.

## Suggestions

1. **Provide learning curves** for at least one real-world dataset (F1/R2 vs. epoch) to directly demonstrate both collapse and its prevention.
2. **Clarify the scope of the theory.** Either provide an argument for how CIP in deep networks connects to rank of internal weights, or explicitly present Theorem 1 as motivation for a heuristic approach.
3. **Report all experimental details** (epochs, learning rate, optimizer, $\alpha$ values per dataset, number of random seeds) for reproducibility.
4. **Add an $\alpha$ sensitivity analysis** on synthetic data to guide practical usage.
5. **Show results of NR applied to DGCCA** on real data to substantiate the claim of generalizability.

## Score and Decision

**Round 1 bracketing:** After the first calibration pass, I considered anchors from three bands: weak (2.4–3.0 — multi-view clustering papers with significant flaws), middle (4.0–7.0 — including a 4.0 sparse CCA paper, 5.0 multi-view causal discovery, 5.5 neural regression collapse, 7.0 robust multi-view clustering), and strong (8.0+ — topically dissimilar papers). The paper clearly falls in the middle band.

**Round 1 bracket:** [4.0, 5.5].

**Round 2 narrowing:** I retrieved anchors within [4.5, 6.5] and [3.5, 5.5]. The closest comparators are: the Sparse CCA paper (4.00, Reject) — this paper has stronger problem novelty but weaker experiments; the "Geometric properties of neural multivariate regression" paper (5.50, Reject) — this has cleaner experiments but more expected findings; the "Explaining Grokking" paper (4.67, Accept) — similar structure of incomplete theory with interesting conceptual contribution; and the "Multi-View Causal Discovery" paper (5.00, Reject) — split opinions on a solid theoretical contribution with some practical gaps.

**Final score setting:** The paper under review is stronger than the Sparse CCA paper (4.00) due to its genuinely novel problem identification and effective method. It is comparable to the Multi-View Causal Discovery paper (5.00) — both have clear contributions undermined by evidential gaps. It is weaker than the Neural Regression Collapse paper (5.50) because that paper's experiments are more thorough even though its findings are more expected. The paper also sits slightly above the Grokking paper (4.67) because the method directly addresses a real deployment problem. **Score: 5.0. Decision: Reject** — the core idea is promising and the synthetic evidence is strong, but the theoretical gap for deep networks and the lack of learning curves on real data mean the central claims are not adequately supported in the current form. The paper would benefit from a major revision cycle.

**Calibration anchors used:**
- `/home/wg25r/review_agent/human_reviews_2026/bU8tRjuanU.md` (avg 2.40, Round 1 weak) — Low-rank attention MVC paper; notably weaker than the paper under review.
- `/home/wg25r/review_agent/human_reviews_2026/3AyriKQDTd.md` (avg 3.00, Round 1 weak) — Modality gap paper; similar structure of identifying a phenomenon but weaker contribution.
- `/home/wg25r/review_agent/human_reviews_2026/3Zkyc6x6Uk.md` (avg 4.00, Rounds 1+2 middle) — Sparse CCA paper; less novel problem, similar level of experimental gaps.
- `/home/wg25r/review_agent/human_reviews_2026/wnFbqvUJ6D.md` (avg 5.00, Rounds 1+2 middle) — Multi-view causal discovery; solid theory but practical concerns; similar overall quality.
- `/home/wg25r/review_agent/human_reviews_2026/ZN1wygYhTZ.md` (avg 4.50, Round 2 middle) — Residual cross-view MVC; comparable experimental thoroughness.
- `/home/wg25r/review_agent/human_reviews_2026/XK5C6pE1ki.md` (avg 5.50, Round 2 middle) — Neural regression collapse; cleaner experiments, more expected findings; slightly stronger than this paper.
- `/home/wg25r/review_agent/human_reviews_2026/sLX5P7FTfT.md` (avg 4.67, Round 2 middle) — Grokking/IB explanation; similar incomplete theory but interesting conceptual contribution.
- `/home/wg25r/review_agent/human_reviews_2026/a4S1nQay3b.md` (avg 7.00, Round 1 middle) — Robust multi-view clustering; significantly stronger experiments and theoretical grounding.
- `/home/wg25r/review_agent/human_reviews_2026/M4t2JUMlfI.md` (avg 6.50, Round 1 middle) — Neural collapse in multi-task learning; stronger theory and experiments.
- `/home/wg25r/review_agent/human_reviews_2026/3YKeB9R1g9.md` (avg 8.00, Round 1 strong) — Scaling with collapse (LLM training); topically dissimilar, far stronger.
- `/home/wg25r/review_agent/human_reviews_2026/kI27Niy4xY.md` (avg 8.00, Round 1 strong) — Text-to-3D stitching; topically dissimilar, far stronger.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>