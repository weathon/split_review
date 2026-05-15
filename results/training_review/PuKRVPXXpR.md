Here is the final consolidated review.

---

## Summary

This paper proposes ResTran, a simple transformation \(X_G = X L_b^{-1/2}\) that converts a graph-with-features problem into a standard vector representation, after which any off-the-shelf vector ML method (SVM, VAE, etc.) can be applied. The paper provides theoretical justification connecting this transformation to effective resistance, a \(k\)-means objective, and spectral clustering (including a claimed ratio-cut equivalence, Theorem 8). Empirically, ResTran + simple classifiers substantially outperforms GCN, GAT, and SGC on heterophilous graph benchmarks (e.g., Wisconsin: 77.4% vs. GCN's 60.3%).

## Strengths

1. **Novel ratio-cut / \(k\)-means spectral connection.** Theorem 8 establishes an equivalence between the relaxed ratio cut objective and relaxed \(k\)-means on the transformed coordinates \(L_b^{-1/2}\mathbf{e}_i\). Prior work (Dhillon et al., 2004) only covered normalized cut; extending this to ratio cut is a genuine theoretical step forward, provided the proof is correct.

2. **Strong empirical evidence against basic GNNs on heterophilous data.** On datasets where homophily is low (Wisconsin, Cornell, Texas, Chameleon, Squirrel, Actor), ResTran + SVM or ResTran + a simple NN beats GCN, GAT, and SGC by margins exceeding 10–17 points (Table 3). This directly supports the claim that the approach is more robust to homophily bias than standard GNN architectures.

3. **Clean intra-component resistance preservation (Proposition 5).** Within a given connected component, distances under \(L_b^{-1/2}\) equal the original effective resistance. This gives a principled guarantee that the transformation does not distort distances inside components, grounding the "resistance" intuition mathematically.

4. **Principled inter-component separation control (Proposition 6).** The paper provides an explicit condition \(b > \sqrt{2}n_1/\lambda_{K+1}\) ensuring cross-component distances exceed within-component distances, giving users a theoretically grounded knob for tuning the graph-structural bias.

5. **Improved over both graph-only and feature-only representations.** Table 1 shows ResTran outperforms both graph-only spectral clustering and feature-only spectral clustering on all tested datasets (e.g., Cora: 76.8% vs. 38.4% graph-only and 71.3% feature-only), confirming that the transformation meaningfully integrates both sources of information.

6. **Practical computational complexity.** The paper adopts a Krylov subspace approximation to compute \(X_G\) in \(O(r f m)\) rather than \(O(n^3)\), with \(r < 100\), making the method scalable. The approach is simpler than most GNN architectures.

## Weaknesses

### Fatal

None. The paper's core claims — that ResTran provides a simple vector representation combining graph and feature information, has theoretical grounding, and is more robust to homophily bias than established GNNs — are supported by evidence.

### Major

None. The identified issues are addressable with additional experiments and clarifications rather than invalidating the paper's contribution.

### Minor

1. **Missing comparison with heterophily-aware GNNs.** The paper compares against GCN, GAT, and SGC — all basic architectures that predate heterophily-specific designs. Methods such as H2GCN, LINKX, ACM-GCN, and CPGNN explicitly target heterophilous graphs. Including them would clarify whether ResTran's advantage is unique to the comparison against simple GNNs or holds against the broader state of the art. Without these baselines, the headline claim "more robust to the homophilous bias than established GNN methods" rests on a narrow comparison set.

2. **The "balancing" claim in Section 4.1 is imprecisely phrased.** The paper states that ResTran "balances homophily and heterophily." However, the eigenvalue analysis shows that the transformation \(L_b^{-1/2}\) maps small Laplacian eigenvalues (homophily) to large weights \(\lambda_i^{-1/2}\) and large eigenvalues (heterophily) to small weights \(\lambda_j^{-1/2}\). This is a low-pass filtering effect — homophily is amplified while heterophily is attenuated, not balanced. The paper's actual argument is more nuanced (ResTran does not *ignore* heterophilous information the way stacked GNNs do, because the transformation is applied only once), but the wording "balances" invites misinterpretation. Clarifying the distinction between "applies a single weak low-pass filter" vs. "stacks multiple low-pass filters (GNNs)" would more accurately describe the claimed advantage.

3. **The graph-with-features extension (Section 4.2.2) is heuristic, not rigorous.** The paper calls replacing \(I\) with \(X\) in the objective a "natural extension," and acknowledges this is not a formal equivalence. The featureless case (Theorem 8) has a rigorous connection to ratio cut; the feature case inherits no such guarantee. While this is an honest limitation, it means the theoretical justification is incomplete for the setting the method actually targets (graphs with features).

4. **No variance or significance reported.** The paper averages over 10 random splits but does not report standard deviations or confidence intervals for Tables 2 and 3. This makes it impossible to assess whether observed gaps (e.g., 77.4% vs. 60.3%) are statistically reliable or could overlap across runs.

5. **The choice of VAT and AAVE as NN backends for ResTran is not well motivated.** The paper says these are "early and simple models," but it is not clear why these specific models were chosen over a basic MLP or other standard architectures. Without ablations on the downstream model, it is hard to separate the contribution of ResTran from the choice of classifier.

### Trivial

- Figure 1 is a bitmap image and is essentially unreadable in the text. A higher-quality or vector rendering would help.
- The paper would benefit from stating the condition in Proposition 6 more clearly in terms of when the user should set \(b\).

## Nice-to-Haves

- **Ablation on the shift parameter \(b\).** The theory (Proposition 6) gives a threshold for \(b\), but there is no experiment showing how performance varies with \(b\) on homophilous vs. heterophilous datasets. Such an ablation would strengthen the practical guidance.
- **Synthetic experiments with controlled homophily levels.** Testing on synthetic graphs with tunable homophily ratios (e.g., the contextual stochastic block model) would directly validate the claim about robustness to homophily bias without confounding from real-world dataset idiosyncrasies.
- **A frequency-response plot comparing ResTran's effective spectral filter with GCN's filter** would make the "once vs. stacked" argument visually clear and would address the concern about low-pass filtering definitively.

## Removed Points

The following criticisms from the harsh reviewer are removed as they are either factually incorrect, misread the paper, or reflect knowledge gaps:

- **Critical Issue 1** (that the theoretical justification is invalid because \(L_b^{-1/2}\) is a low-pass filter and the claim contradicts the method's behavior): The paper explicitly states it "favors homophilous assumption but does not ignore heterophilous assumption." The paper never claims ResTran amplifies heterophily more than homophily. The distinction is between a single application of \(L_b^{-1/2}\) vs. stacked GNN layers that progressively suppress high frequencies. The critic attacks a stronger claim than the paper actually makes. Verified against the paper at lines 198–200: "Our ResTran can be seen as favoring the homophilous assumption but, at the same time, not ignoring the heterophilous assumption."

- **Critical Issue 2** (that Theorem 8 is almost certainly incorrect): The critic argues that "nullspace eigenvectors are not used in ratio cut," which is incorrect for the \(K\)-way ratio cut with \(K\) components — the relaxed ratio cut uses the \(K\) smallest eigenvectors of \(L\), which include the nullspace (component indicators) when multiple components exist. Theorem 8's claim is that under condition \(n_1 b > \lambda_{K+1}^{-1}\), the top-\(K\) eigenspace of \(L_b^{-1/2}\) equals the bottom-\(K\) eigenspace of \(L\). Since Proposition 3 shows \(L\) and \(L_b^{-1/2}\) share eigenvectors, this is a self-consistent claim. The critic's reasoning about eigenvalue ordering mismatch reflects a misunderstanding of how spectral clustering handles multiple components. While the proof cannot be inspected (stripped by parser), the claim is not obviously flawed as presented.

- **Strawman about "non-standard 5% split"**: The 5% label split is a standard setting in GNN literature (e.g., many papers use 5–10% labels). 20 labels per class is common for small citation networks but not universal. This is a typical experimental choice, not a flaw.

- **Claim that "no statistical significance or variance is reported"**: This is partially true but the paper does report averages over 10 random splits. Reporting variance is standard practice and this is kept as a minor weakness above, but the critic's framing as a "concern" implying overfitting is too strong.

- **Criticism about Section 4.2.2 being a "non sequitur"**: The paper explicitly calls this a "natural extension" (line 241) and does not claim a rigorous equivalence for the feature case. The critic overstates the paper's claim. However, the underlying observation that the feature case lacks formal justification is valid and is retained as a minor weakness.

- **Complaint about VAT/AAVE choice being "ad hoc"**: The paper explains these are "early and simple models" used to avoid sophistication. This is a reasonable design choice for a method that claims to work with any vector-based ML. Retained as a minor note rather than a major flaw.

- **Missing appendix / proof criticisms**: The parser stripped appendix content; these are not author errors.

## Novel Insights

The most interesting observation emerging from intersecting the reviews is the tension between ResTran's simplicity-based framing and the theoretical apparatus used to justify it. The paper argues that GNNs' architectural bias toward homophily is inherent and therefore the remedy should be to bypass GNN architectures entirely, yet the method's own theoretical justification leans on spectral graph theory that is equally connected to GNN filter design. Understanding precisely *how much* heterophilous information survives a single \(L_b^{-1/2}\) transformation relative to a single GCN layer — and whether the advantage is simply the absence of repeated filtering rather than any fundamental spectral property — would sharpen the contribution. The paper's framing of "mixing" or "balancing" would benefit from replacing those qualitative descriptions with precise spectral bandwidth comparisons (ResTran vs. 1-layer GCN vs. 2-layer GCN).

## Suggestions

1. **Replace "balances" with a more precise characterization.** The paper should clearly state that ResTran is a *single* low-pass filter (applied once), while GNNs apply repeated low-pass filtering through stacked layers. The advantage is not "balancing" but "shallower filtering" — the method preserves more high-frequency content simply because it does not stack filters.

2. **Add comparisons with heterophily-aware GNNs** (H2GCN, LINKX, or ACM-GCN) on the same datasets and splits to substantiate the claim of robustness.

3. **Report standard deviations** for Tables 2 and 3 over the 10 random splits.

4. **Include an ablation on \(b\)** to show how the shift parameter affects performance across datasets with varying homophily levels.

5. **Provide the proof of Theorem 8** (in an appendix or supplement) so reviewers and readers can verify the claim.

6. **Clarify in Section 4.2.2** that the extension to graph-with-features is heuristic/analogical, not a proven equivalence, and briefly discuss what would be needed to bridge the gap (e.g., a variant of the \(k\)-means objective with feature-aware weights).

## Score and Decision

The paper proposes a clean alternative to GNNs with a simple transformation, provides non-trivial theoretical connections (ratio-cut / \(k\)-means equivalence), and demonstrates strong empirical results against standard GNN baselines on heterophilous graphs. The main weaknesses — missing heterophily-aware baselines, imprecise wording about "balancing," heuristic feature extension — are addressable and do not invalidate the core contribution. The paper would benefit from the suggested additions but is already a solid contribution presenting a genuinely different approach to graph learning.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>