Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper challenges the standard cross-device FL paradigm where each selected cohort participates in only one communication round with the server. It proposes SPPM-AS (Stochastic Proximal Point Method with Arbitrary Sampling), a framework that allows a cohort to perform multiple local communication rounds per global iteration. The key finding is that increasing the number of local communication rounds \(K\) can reduce total communication cost by up to 74% compared to FedAvg/LocalGD on convex logistic regression, with even larger gains (94.87%) under hierarchical FL structures. The paper provides a convergence theory for strongly convex objectives under arbitrary sampling, introduces stratified sampling with variance reduction guarantees, and gives practical hyperparameter guidance.

## Strengths

1. **Novel and practically relevant finding**: The paper empirically demonstrates that increasing local communication rounds within a cohort (beyond the conventional single round) reduces total communication cost to reach a target accuracy. This directly challenges a widely held design assumption in cross-device FL. The effect is shown across multiple datasets (a6a, mushrooms, ijcnn1, a9a) and is especially pronounced at large learning rates (Figures 1 and 4).

2. **Clean algorithmic framework with convergence theory**: SPPM-AS is a principled generalization of the stochastic proximal point method to arbitrary client sampling distributions. Theorem 1 provides a non-asymptotic convergence bound for strongly convex objectives without requiring smoothness, covering nice, block, and stratified sampling as special cases. The theory correctly captures the trade-off between convergence speed and neighborhood size governed by \(\gamma\) and the sampling distribution.

3. **Stratified sampling with provable variance reduction**: Lemma 1 bounds the noise variance of stratified sampling in terms of intra-cluster gradient deviations, and Lemma 2 shows that optimal stratified sampling achieves a smaller convergence neighborhood than nice sampling. The experimental comparison in Figure 2 validates the theoretical advantage. This is a technically clean contribution.

4. **Extension to hierarchical FL with larger gains**: The hierarchical FL experiments (Section 3.5) show a 94.87% communication cost reduction when local-to-hub cost is low and hub-to-server cost is high — the practically relevant scenario for edge-cloud architectures. This strengthens the practical value of the approach.

## Weaknesses

### Fatal
None.

### Major

1. **Neural network experiments are too thin to support the claimed generality**. The non-convex experiments use only one dataset (FEMNIST) and one architecture (CNN). The paper's title and abstract claim general results for "cross-device FL," but the DL evidence consists of a single figure showing qualitative trends (optimal \(K\) increases with \(\gamma\)). No quantified communication cost reduction is reported for the neural setting. Given that the theoretical analysis is limited to strongly convex objectives, the empirical burden on the non-convex side should be *higher*, not lower. This limits the paper's scope more than the authors acknowledge.

2. **Missing comparison to FedProx**. The paper claims SPPM-AS "generalizes" FedProx (line 189) and mentions FedProx in the title of the appendix (sec:Avg-SPPM-baselines), yet the experimental comparison is limited to MB-GD and MB-LocalGD. FedProx is the most natural baseline given the proximal point formulation. Without showing that SPPM-AS with suitable \(K\) outperforms a well-tuned FedProx, the claim that the framework "surpasses existing state-of-the-art cross-device algorithms" (line 58) is unsupported. This is a significant empirical gap.

### Minor

3. **Cost model inconsistency in the standard FL setting**. The paper defines total cost as \(TK\) (Section 1, line 50). In the hierarchical setting, the correct formula \((c_1 K + c_2)T\) is used (line 382). However, for the standard (base) setting, the paper sets \(c_1=1, c_2=0\) — effectively assuming global communication is free. If global rounds are counted at the same cost as local rounds (i.e., \(c_1=c_2=1\)), the total cost would be \((K+1)T\) for SPPM-AS versus \(2T\) for LocalGD, changing the 74.36% figure to approximately 72%. The qualitative finding is robust, but the paper should clarify the cost model and state whether global rounds are included or excluded and why.

4. **Theory does not directly model the role of \(K\)**. Theorem 1 assumes exact proximal steps, while experiments use inexact iterative solvers (CG, BFGS, Adam). The paper references an inexact formulation in the appendix (line 186), which partially addresses this, but the main theorem does not connect \(K\) (number of local communication rounds) to the accuracy of the proximal solve. A bound of the form \(\mathbb{E}\|x_{t+1} - x_*\|^2 \leq \text{contraction} + \text{error}(K)\) would unify the theory and experiments. As presented, the theoretical contribution and the main empirical finding are somewhat decoupled.

5. **Stratified sampling requires sharing gradient information for K-means clustering** (line 324), but privacy implications are not discussed. For a cross-device FL paper, this omission is worth noting — clustering gradient information may leak data properties that the FL setting aims to protect.

### Trivial
None.

## Nice-to-Haves

- A comparison to FedProx (and ideally SCAFFOLD) under a consistent communication cost budget would substantially strengthen the empirical evaluation.
- Additional non-convex benchmarks (e.g., CIFAR-100 with ResNet or Shakespeare with an RNN) would broaden the empirical support.
- A brief explicit mapping showing how SPPM-AS with particular choices of solver and sampling recovers FedProx and FedAvg as special cases would ground the "generalization" claim more concretely.
- The paper could re-center its main claim around the hierarchical FL setting, where the cost model is most realistic and the gains are largest.

## Removed Points

- **Critic's point about cost model being a "structural flaw"** — downgraded from fatal/major to minor. The inconsistency is real but the qualitative finding is robust (the corrected 72% vs 74% does not change the paper's message), and the hierarchical setting uses the correct cost model.
- **Critic's point that theory "never acknowledges" the inexact prox issue** — removed as factually incomplete. The paper explicitly states on line 186: "we present in \cref{sec:fedavg-sppm} the lemma of the inexact formulation for SPPM-AS." The analysis exists in the appendix (stripped by parser). The criticism is downgraded to a minor point about the main text presentation.
- **Critic's "one step travels far" discussion being unnovel** — this is a pedagogical exposition, not a claimed contribution. Not a weakness.
- **Strength Finder's generic strengths about "addressing an important problem"** — these were not present; the strengths listed were specific and grounded. No removal needed.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest theoretical result (exact-prox convergence with arbitrarily large \(\gamma\)) and its strongest empirical result (communication cost reduction via increased \(K\)) operate on different planes. The exact-prox theory shows that one can converge in a single global iteration with a large enough \(\gamma\), essentially solving the proximal problem perfectly. The experiments show that solving the prox *approximately* with \(K\) local rounds creates a trade-off where larger \(K\) (more accurate prox) reduces the number of global iterations needed. Connecting these two — showing theoretically how \(K\) controls inexactness and what the optimal \(K(\gamma)\) is — would transform the paper from an empirical observation with separate theory into a tightly unified contribution.

## Suggestions

1. Clarify the cost model: explicitly state whether global rounds are included in the base setting or not, and justify why.
2. Add a FedProx baseline comparison — this is the single highest-leverage addition.
3. Expand non-convex experiments to at least one additional dataset/architecture, and report quantified communication cost reduction percentages for the neural setting.
4. Move the inexact proximal analysis from the appendix into the main text, or at minimum add a brief statement connecting \(K\) to the accuracy of the proximal solve.

## Score and Decision

The paper identifies a genuinely useful and surprisingly under-explored direction in cross-device FL, provides a clean algorithmic framework with theoretical backing, and shows compelling results on convex problems. However, the experimental evaluation is too narrow to fully support the claimed generality, and the missing FedProx comparison is a notable gap. The paper is a solid contribution but needs substantial revision before it is publication-ready.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>