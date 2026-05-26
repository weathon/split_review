Now I have a thorough understanding of the paper. Let me produce the final consolidated review, applying the filtering rules against both the harsh critic's points and the strength finder's claims.

## Summary

This paper identifies three fundamental limitations of static supervised causal learning (SCL) — fragility to distribution shifts, failure in compositional generalization, and poor synthetic-to-real transfer — and proposes Test-Time Training for SCL (TTT-SCL), a framework that dynamically generates a customized training set aligned with each test instance. The Alignment of Distribution (AD) metric, combined with sparsity constraints, enables search over causal graphs to construct test-aligned training data. The instantiation TACTIC achieves strong empirical results, including a substantial improvement on the real-world Sachs dataset (78.9 AUROC vs. 62.3 for the best static SCL baseline) and on pseudo-real SynTReN data.

## Strengths

- **Systematic empirical diagnosis of static SCL limitations.** Section 3 and Figure 2 provide controlled experiments across 6 synthetic settings demonstrating that distribution shifts (graph, mechanism, noise) and compositional generalization failures degrade SCL performance by 3–58 AUROC points. Table 1 further documents the synthetic-to-real gap (AVICI drops from 97.8 on RFF_G to 62.3 on Sachs). This evidence is concrete and directly supports the paper's motivation.

- **Novel TTT-SCL framework with a principled alignment objective.** The AD metric (Eq. 3) operationalizes distributional alignment as a likelihood-based score, and the sparsity penalty (Eq. 4–5) enforces causal minimality. The framework is cleanly formalized and conceptually distinct from prior static-diversity SCL approaches.

- **TACTIC achieves strong results on real-world and pseudo-real data.** In Table 2, TACTIC (Notears) reaches 78.9 AUROC on Sachs vs. 67.1 for PC and 62.3 for AVICI, and 80.1 on SynTReN vs. 65.4 for AVICI. These are large, meaningful improvements on the most challenging scenarios, directly delivering on the paper's central claim.

- **Ablation confirms sparsity is necessary.** Table 3 shows that removing the sparsity penalty (λ=0) causes consistent AUROC drops across all settings (e.g., Sachs: 78.9→63.5, Chebyshev_G: 83.0→69.7), validating the theoretical argument that AD alone yields degenerate dense solutions.

- **Stage-wise analysis demonstrates the two-stage pipeline's value.** Table 4 shows that the final SCL prediction consistently improves over both the seed graph and the highest-scoring graph from the search, empirically justifying the design choice of training an SCL model rather than stopping at the best-scoring graph.

## Weaknesses

### Fatal
None.

### Major
None. The remaining concerns are addressable and do not threaten the paper's core conclusions.

### Minor

1. **Real-world evaluation in the main text is limited to a single small dataset.** Only Sachs (11 variables, one ground-truth graph) appears as a real-world benchmark in the main paper. While Appendix G (present in the original submission) reports results on bnlearn graphs (Asia, Cancer, Earthquake, Survey), the main text would benefit from at least one additional real-world result or a summary of those appendix results. Relatedly, **no standard deviations are reported for TACTIC on Sachs and Syntren** in Table 2 (e.g., TACTIC (Notears) Sachs: 78.9, Syntren: 80.1 — both without variance), making it impossible to assess the stability of these key results.

2. **No sensitivity analysis for the sparsity weight λ.** The ablation removes sparsity entirely (λ=0), which is informative, but the paper does not explore how different λ values affect performance. Since λ directly trades off distributional alignment against causal minimality, a brief sensitivity study (e.g., across one order of magnitude) would strengthen confidence that the chosen λ is not brittle.

3. **The stochastic search procedure is underspecified in the main text.** The acceptance mechanism is described as "accepted with probability proportional to its score," while Figure 3 shows α = min[1, score(G^{k+1})/score(G^k)] — a Metropolis-Hastings-style rule that is not identical to "probability proportional to score." The number of refinement iterations, burn-in, thinning, and how the set of K=200 graphs is sampled from the chain are not stated. These details matter for reproducibility and for understanding search quality.

4. **The explanation for why the SCL model outperforms the highest-scoring graph is thin.** The paper states that the SCL model "learns more accurate causal relationships" from the generated training data (Table 4 discussion), but does not analyze *how* the supervised model improves over the score-based search. A brief diagnostic (e.g., does the SCL model correct systematic edge-type errors? does ensembling over multiple generated graphs help?) would strengthen the contribution.

5. **The "Component-mixed" condition description could be more precise.** The paper states it "contains all individual components … seen in isolation during training, but crucially excludes the specific combinations present in the test instances." It would be clearer to specify, for each test setting, exactly which (mechanism, graph, noise) combinations are included in the training set and which are withheld.

### Trivial
None.

## Nice-to-Haves

- A brief runtime/scalability discussion in the main text (the paper references Appendix F for complexity analysis, but a one-sentence summary of the per-test cost would help readers gauge practicality).
- A more detailed comparison with test-time adaptation methods from general ML (the paper notes TTT-SCL is the first in SCL, but could draw sharper contrasts with parameter-adaptation approaches vs. its data-generation approach).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"AD metric is underspecified / not reproducible."** The critic claims the paper does not define how p(X_i|f_i^k) is computed. The paper states "While there are many ways to implement AD as discussed in Appendix A" — the appendix (present in the original submission) contains the implementation details. Per the meta-instructions: "REMOVE weaknesses about missing appendix … the parser strips those sections from all papers; they exist in the original submission."

2. **"Computational cost is not addressed."** The paper explicitly states: "Complexity analysis and runtime variation with the number of nodes are detailed in Appendix F." The claim that cost is unaddressed is factually incorrect.

3. **"Evidence for compositional generalization failure is not sufficiently strong."** The paper shows consistent 3–11 AUROC drops across all 6 settings in Figure 2 (e.g., RFF_G_97.8: 100→91, Chebyshev_G_62.3: 93→83). This is systematic evidence supporting the claim. The critic's framing of "moderately lower" and "far from a failure" is a matter of interpretation, not a concrete flaw in the paper.

4. **"AVICI still outperforms TACTIC on RFF_G."** The paper explicitly acknowledges this: "The pre-trained AVICI (scm-v0) model achieves optimal performance on the RFF_G datasets, as it was explicitly trained on this distribution. TACTIC's performance on RFF_G is slightly lower but remains strong." This is an expected limitation, not a weakness.

5. **"Comparison with NOTEARS would be informative"** — NOTEARS results are already listed separately in Table 2 (e.g., 80.5 on RFF_G, 82.0 on Linear_U). The critic appears to have misread the table.

6. **"The acceptance mechanism may be problematic with negative scores."** The joint score = AD(G) − λ·Sparsity(G). Since AD is a log-likelihood averaging sum of log probabilities (typically negative) and λ·Sparsity is non-negative, scores are generally negative, making the ratio of two negative scores positive and well-defined for the α = min(1, ratio) rule. While edge cases with mixed signs could arise, this is a subtle technical point that does not clearly undermine the method as presented.

7. **"Reliance on appendix for AD details is not acceptable."** Per the meta-instructions, appendix deferral for implementation details is standard practice; the parser strips appendix content from all papers. This is not a valid criticism of the submission as originally written.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's merits (novel TTT-SCL framework, strong empirical results on real-world data) and identify minor presentation and evaluation gaps, but do not surface fundamentally new observations about the work.

## Suggestions

- Add standard deviations for TACTIC on Sachs and Syntren (Table 2), and consider including a summary of the bnlearn appendix results in the main text.
- Include a brief sensitivity analysis for λ (e.g., ± one order of magnitude around the chosen value) to demonstrate robustness.
- Clarify the acceptance mechanism: reconcile the "probability proportional to its score" description with the Metropolis-Hastings ratio shown in Figure 3, and specify the number of iterations and how K=200 graphs are collected.
- Expand the discussion in Section 4.4 with a brief diagnostic of how the SCL model improves over the highest-scoring graph.

## Score and Decision

The paper makes a genuine contribution: it identifies real limitations in the static SCL paradigm, proposes a principled test-time training framework with a tractable alignment objective, and demonstrates substantial empirical gains on the most challenging real-world and pseudo-real benchmarks. The weaknesses are minor and addressable — none threaten the core claims or results.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>