Now I have enough calibration. Let me finalize my assessment.

**Calibration analysis:**

The paper under review sits most naturally between:
- **"Determine-Then-Ensemble" (7.50, Accept)**: Similar LLM ensembling topic, but the paper under review has stronger theoretical foundations (Bayesian optimality, closed-form advantage gaps, finite-sample guarantees) vs. this paper's more empirical approach. However, that paper has more practical impact. Comparable quality.
- **"Balancing Act: DMoA" (6.25, Accept)**: Also LLM ensembles, but much weaker theoretical grounding. The paper under review is clearly stronger.
- **"SpecFuse" (5.33, Reject)**: LLM ensemble but purely empirical. The paper under review has substantially stronger contributions.
- **"Rethinking Reward Modeling" (8.00, Accept)**: Deep theoretical analysis of BT model in LLMs, comparable theoretical depth. Slightly stronger overall due to more comprehensive experiments (12,000 setups).

Round 1 bracket: 6.5–7.5. Round 2 narrows to **7.0**.

The OW-L/OW-I equivalence is unexplained but non-fatal (the methods diverge across other ensembles). The core theoretical contributions (Theorems 1–3, Corollaries 1–2) are clean and novel. The empirical gains are modest on the featured ensemble but the paper shows consistent improvement across 16 ensemble configurations.

---

## Summary
This paper proposes Optimal Weight (OW) and Inverse Surprising Popularity (ISP) for aggregating answers from multiple LLMs. OW is proven Bayesian-optimal among all aggregation functions under conditional independence (Theorem 1), while ISP leverages only second-order correlation information—no ground-truth labels needed—and provably outperforms majority voting (Theorem 2). Two unsupervised pipelines (OW-L, OW-I) estimate optimal weights from second-order information. Validation spans simulated data, UltraFeedback, MMLU, and a healthcare dataset ARMMAN.

## Strengths
- **Strong theoretical core**: Theorem 1 proves OW is Bayesian-optimal among *all* aggregation functions (not just linear ones). Theorem 2 provides closed-form advantage gap expressions: $\mathbb{E}[\text{Adv}_{ISP}(s^*)] \geq \mathbb{E}[\text{Adv}_{MV}(s^*)] \geq \mathbb{E}[\text{Adv}_{SP}(s^*)]$, with ISP's advantage over MV scaling as $\Theta(1/K)$. Theorem 3 extends to finite samples. These are clean, well-presented results.
- **Novel ISP algorithm**: The "inverse surprising popularity" construction—evaluating conditional probabilities under counterfactual answers rather than actual ones—is a creative adaptation of surprising popularity for the LLM setting where systematic biases are weaker. The key advantage: ISP requires no ground-truth labels, only second-order correlation data.
- **Information-theoretic justification for Bradley-Terry** (Corollary 1): For $K=2$, optimal weights reduce to inverse-logistic weighting $\omega_i \propto \sigma^{-1}(x_i)$, providing a principled explanation for the BT model ubiquitous in RLHF practice.
- **Insightful negative result on SP** (lines 138-148): The explanation that LLM agents lack the systematic biases of human crowds, making SP worse than MV, is a genuine contribution to understanding when surprising popularity works.
- **Comprehensive evaluation design**: 16 model ensembles from 4 families (GPT, Qwen, Llama, Phi), tested across simulated data, UltraFeedback, MMLU, and ARMMAN. OW-L outperforms MV in 97.92% of ensemble cases with absolute gains up to 14.20%.

## Weaknesses

### Fatal
None.

### Major
- **Unexplained identical performance of OW-L and OW-I on the main-table ensemble**: In Tables 3 and 4, OW-L and OW-I show identical accuracy on all three datasets (73.66%, 90.37%, 85.78%) and identical per-question discrepancy counts (2545/1727, 1821/659, 264/195). These are conceptually different methods—OW-L learns accuracies via ERM over second-order statistics (Eq. 7), while OW-I uses ISP predictions as pseudo ground-truth. The paper provides no explanation. Critically, across all 16 ensembles, OW-L outperforms MV in 97.92% of cases while OW-I does so in only 85.83%, so the methods clearly differ in general. But the complete bit-identical equivalence on the featured ensemble deserves discussion—either a structural reason exists (worth stating) or the authors should identify the numerical cause.

### Minor
- **Modest absolute gains on the featured ensemble**: The improvements over MV for the four-strong-model ensemble are 1.45% (UltraFeedback), 1.05% (MMLU), and 0.54% (ARMMAN). While statistically significant (t-statistics of 12.53, 23.39, 3.22) and while the paper reports gains up to 14.20% across all 16 ensembles, the main text focuses on a case where Single Best (91.02% on MMLU) outperforms all proposed methods (90.37%). Briefly discussing when aggregation over a single strong model is worthwhile would strengthen the paper.
- **Only one ensemble detailed in main text**: Tables 3 and 4 report only the four-strong-model ensemble; all 16 ensembles are in Appendix F.4. The summary statistics (e.g., "97.92% of cases") are not independently verifiable from the main text alone. A compact summary figure showing OW-L's improvement over MV across all 16 ensembles would strengthen the empirical claims.
- **No comparison with practical weighted baselines**: The paper compares against MV and SP but not against weighted voting with weights proportional to model size/benchmark scores, or learned ensemble weights from a held-out labeled set. Even an oracle-weighted baseline would help contextualize the gains.

### Trivial
- **Binary-only intuition for ISP**: The motivation (lines 152-169) is presented entirely for $K=2$; the jump to the general-$K$ formula in Eq. 5 is non-trivial. A brief remark bridging the two would improve readability.

## Nice-to-Haves
- Analyzing ensemble diversity (within-family vs. across-family) and its effect on aggregation quality, since conditional independence is more plausible across families.
- Brief discussion of computational/sample complexity as N grows (experiments use N=4).
- Reporting conditional accuracy gain on the disagreement subset (52%, 31%, 47% of questions) to clarify where aggregation helps most.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's concern about "modest absolute gains" as a fundamental issue: the paper reports gains across 16 ensembles ranging from 0.54% to 14.20%, with OW-L beating MV in 97.92% of cases. The modest gains on the featured ensemble are a minor presentation issue, not a fundamental flaw.
- Concerns about random shuffling losing information: the paper addresses this in Appendix B.1 and acknowledges it's standard practice.
- Scalability concern with O(N²K²) parameters: the paper uses N=4 and K∈{2,4}, the practical range for LLM ensembles. This is a nice-to-have, not a weakness.
- Questions about positional biases of smaller models: the paper explicitly acknowledges this assumption (line 51).
- Harsh critic's note about the binary intuition gap for ISP: verified as a minor readability issue, not a substantive flaw.

## Novel Insights
The paper's most genuinely novel insight is the demonstration that surprising popularity—designed for human crowds with systematic biases—is provably *worse* than majority voting for LLM agents, and that the remedy is to invert the conditioning direction. The resulting ISP algorithm and its closed-form advantage gap ($\Theta(1/K)$ over MV) provide a principled framework for unsupervised LLM aggregation. The information-theoretic justification for the Bradley-Terry model (Corollary 1) connects aggregation theory to LLM post-training practice in a way that hasn't been established before.

## Suggestions
- Explain why OW-L and OW-I produce identical predictions on the four-strong-model ensemble. If both estimation procedures converge to the same accuracy ordering under the conditional independence model, stating this would strengthen the paper.
- Add a compact figure showing OW-L's improvement over MV across all 16 ensembles in the main text.
- Briefly discuss when aggregation is most valuable relative to simply using the single best model (especially relevant for MMLU where Single Best outperforms all proposed methods).

## Reporting

**All retrieved anchors across rounds:**

Round 1:
- `8QTpYC4smR.md` — avg 1.00 — Systematic review of LLMs (unrelated, strong reject)
- `5kMwiMnUip.md` — avg 1.40 — Jailbreaking LLMs (unrelated)
- `Uj0h13lVrR.md` — avg 1.00 — GFlowNets (unrelated)
- `nSDOkm0SKo.md` — avg 1.00 — Financial markets (unrelated)
- `ff5srKUefm.md` — avg 3.00 — Entropy voting in capsules (tangentially related, rejected)
- `z3DMFpaP6m.md` — avg 3.00 — Information emergence in LLMs (tangentially related)
- `ujNe7sybJu.md` — avg 2.50 — Video summarization with MoE (tangentially related)
- `k7pnwqrpKB.md` — avg 2.50 — Deep bootstrap aggregation (tangentially related)
- `lhLQpS33YL.md` — avg 5.33 — **SpecFuse: LLM ensemble via segment prediction** (topical, rejected, paper under review is stronger)
- `8HQS1X2AK4.md` — avg 5.33 — Test-time alignment via hypothesis reweighting (somewhat related)
- `LyNsMNNLjY.md` — avg 4.25 — LLM routing with benchmarks (related, rejected)
- `kF3tNnhkvX.md` — avg 4.60 — Language model merging in iterative preference learning (related, rejected)
- `Dl6nkKKvlX.md` — avg 6.25 — **Balancing Act: DMoA LLM ensembles** (highly relevant, accepted, paper under review has stronger theory)
- `yaOe2xBcLC.md` — avg 6.00 — NoVo: Norm voting for hallucinations (related, accepted)
- `Fs9EabmQrJ.md` — avg 6.67 — EmbedLLM: compact representations (related, accepted)
- `tbx3u2oZAu.md` — avg 6.00 — Theory for token-level RAG harmonization (similar theoretical flavor, accepted)
- `rfdblE10qm.md` — avg 8.00 — **Rethinking Reward Modeling / BT model** (highly relevant theory, paper under review is slightly below)
- `f4gF6AIHRy.md` — avg 8.00 — Dimensional collapse in pre-training (less relevant)
- `WbWtOYIzIK.md` — avg 8.00 — Knowledge cards for LLMs (less relevant)
- `OOxotBmGol.md` — avg 8.00 — LLMs for Bayesian optimization (less relevant)

Round 2:
- `jJXZvPe5z0.md` — avg 6.67 — Convergence of no-regret dynamics in IR games (similar theoretical style)
- `0oWGVvC6oq.md` — avg 6.50 — Regret-information trade-off (similar theoretical depth)
- `LqTz13JS2P.md` — avg 7.25 — Generalized principal-agent with learning agent (similar theory rigor)
- `NO6Tv6QcDs.md` — avg 6.50 — Limits to scalable evaluation with LLMs (relevant negative result)
- `36L7W3ri4U.md` — avg 7.00 — Beating PoA in potential games (similar proof style)
- `AEFVa6VMu1.md` — avg 7.50 — Approximation algorithms with predictions (similar theory level)
- `i9Vs5NGDpk.md` — avg 7.50 — Sketched ridge ensembles (similar ensemble theory)
- `XOnya9gSdF.md` — avg 7.50 — Multi-label classification with macro-at-k metrics (similar algorithmic contribution)
- `FDnZFpHmU4.md` — avg 7.50 — **Determine-Then-Ensemble / UniTE** (highly relevant LLM ensemble, paper under review has stronger theory)
- `uSz2K30RRd.md` — avg 7.33 — Weighted point cloud embedding (similar optimization theory)

**Round-1 bracket**: 6.5–7.5 (the paper clearly sits above the 5-6 range rejected papers and the 6.25 accepted ensemble paper, but slightly below the 8.00 BT reward paper)

**Round 2 narrowing**: The paper is comparable to "Determine-Then-Ensemble" (7.50) which has less theory but similar practical impact, and above "Balancing Act" (6.25) which has weaker theoretical grounding. Final score: **7.0**.

The OW-L/OW-I equivalence is an unexplained concern but does not undermine the core theoretical contributions (Theorems 1-3, ISP algorithm). The modest gains on the featured ensemble are offset by consistent improvement across 16 ensemble configurations (up to 14.20%, beating MV in 97.92% of cases). The paper makes a genuine contribution to information aggregation theory applied to LLMs.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>