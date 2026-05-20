Now I have everything I need. Let me write the consolidated review.

---

## Summary

This paper identifies three critical out-of-distribution generalization failures in static supervised causal learning (SCL)—fragility under distribution shifts, compositional generalization failure, and a synthetic-to-real performance gap—and proposes TTT-SCL, a framework that dynamically generates causally aligned training data at test time. The method, TACTIC, uses a proposed Alignment of Distribution (AD) metric with a sparsity penalty to guide stochastic graph search, generating customized training sets per test instance. Experiments across synthetic, pseudo-real (SynTREn), and real-world (Sachs) datasets show TACTIC substantially outperforming both traditional causal discovery methods and the strongest SCL baseline (AVICI), notably improving AUROC on Sachs from 62.3 to 78.9.

## Strengths

- **Systematic diagnosis of SCL limitations with controlled experiments (Figure 2, Table 1).** The paper empirically demonstrates three distinct OOD failure modes of static SCL: (1) fragility when test distributions shift in mechanism, graph, or noise (e.g., RFF_G AUROC drops from 97.8 to 42 under mechanism shift), (2) compositional generalization failure even when all individual components are seen during training, and (3) dramatic synthetic-to-real gap (AVICI scm-v0 achieves 97.8 on RFF_G but only 62.3 on Sachs). This is a well-executed, evidence-rich motivation that goes beyond hand-waving about distribution shift.

- **Novel TTT-SCL framework with a practical instantiation (TACTIC) that demonstrates strong empirical performance.** The idea of generating test-aligned training data via distributional alignment (AD) combined with sparsity is conceptually clean and well-motivated. Table 2 shows TACTIC (Notears) achieves SOTA or competitive AUROC across all datasets: 91.8 on RFF_G, 86.3 on Linear_U, 83.0 on Chebyshev_G, 78.9 on Sachs, and 80.1 on SynTREn—consistently outperforming AVICI on non-RFF distributions. The stage-wise analysis (Table 4) convincingly demonstrates that the SCL training phase adds value beyond the highest-scoring graph found during search (e.g., Chebyshev_G improves from 75.8 → 83.0).

- **Well-designed ablation studies that validate design choices.** The sparsity ablation (Table 3) shows consistent degradation when λ=0 (e.g., Chebyshev_G drops from 83.0 to 69.7), confirming that sparsity prevents degenerate dense solutions. The seed initialization comparison (random vs. NOTEARS) demonstrates the method is robust to initialization quality while benefiting from better seeds.

- **Comprehensive baseline comparison across paradigms.** The paper compares against 8 diverse methods spanning constraint-based (PC), score-based (GES, NOTEARS), function-based (RESIT, SCORE, NoGAM), and SCL (AVICI) approaches, evaluated across synthetic, pseudo-real, and real data.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The AD metric's regression model class is deferred entirely to the appendix (Section 4.1).** The main text states that AD is computed via likelihood under a fitted mechanism \(f_i^k\) from SIM, and notes "as discussed in Appendix A," but never specifies whether the regression uses linear models, GAMs, neural networks, or kernel regression—nor the noise model assumed for the likelihood. While this is presumably in the stripped appendix, the AD metric is the central mechanism connecting candidate graphs to test data; without knowing the model class in the main text, the reader cannot assess whether AD reliably captures distributional alignment or whether the results might depend on fortuitous regressor-data matches. The authors should state the regression class and noise assumption explicitly in Section 4.1.

- **Only one real-world dataset (Sachs, 11 nodes) is evaluated, with no reported standard deviation for that result (Table 2).** The Sachs result (78.9 for TACTIC Notears) is a single number, whereas synthetic results include standard deviations from multiple runs. For a paper whose central claim is bridging the synthetic-to-real gap, one real dataset with a single evaluation is thin evidence. The SynTREn pseudo-real data and the bnlearn benchmarks (Appendix G, not visible) partially mitigate this, but stronger real-world validation would substantially strengthen the contribution.

- **The stochastic search procedure (Section 4.2) is described at a high level without key algorithmic details in the main text.** The paper mentions "propose local modifications… while maintaining the DAG constraint" and acceptance "with probability proportional to its score" (or ratio-based as shown in Figure 3), but does not specify: how DAG-ness is enforced during proposals, the number of refinement iterations, whether there is a burn-in period, or the handling of negative scores in the ratio acceptance rule. The acceptance rule \(\min(1, \text{score}(G_{k+1})/\text{score}(G_k))\) is unusual when scores can be negative (AD is a log-likelihood; sparsity subtracts further). These details matter for reproducibility and for understanding whether the search is efficient or essentially random walk. The appendix (Appendix F) is cited for complexity analysis but not visible.

- **Missing ablation: training the SCL model on only the single highest-scoring graph.** Table 4 shows the SCL model trained on the K=200 generated graphs outperforms the single highest-score graph found during search. But this leaves open whether the improvement comes from (a) the ensemble of multiple graphs providing richer training data, or (b) the SCL model architecture acting as a post-processor that could achieve similar gains from just the best graph with data augmentation. An ablation using only the best graph (with/without sampling multiple datasets from it) would cleanly separate these effects.

### Trivial

- The conclusion states "Our theoretical and empirical results underscore the effectiveness of AD and necessity of sparsity." No theoretical results (theorems, lemmas, proofs) appear in the main text. If the theoretical analysis is in the stripped appendix, this is fine; if not, the claim should be revised to "analytical and empirical" or similar.

- The value of λ (sparsity penalty weight) is not reported in the main text for the main experiments, making exact reproduction difficult without the appendix.

## Nice-to-Haves

- An evaluation on at least one additional real-world dataset with multiple random seeds would strengthen the central synthetic-to-real claim.
- An analysis of sensitivity to the seed graph initialization quality beyond the random-vs-NOTEARS binary comparison (e.g., using a deliberately degraded seed).
- Discussion of computational cost relative to baselines—how does TACTIC's test-time generation + training compare to AVICI's single forward pass in wall-clock time?

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The AD metric and the regression model are critically underspecified — this is fatal."** Removed as fatal; demoted to Minor. The paper explicitly cites Appendix A for implementation details, and per policy, stripped-appendix content is assumed to exist. The concern is valid but not fatal—the main text omission is addressable.

- **"False claim of theoretical results damages credibility — misrepresentation."** Removed as a major concern; demoted to Trivial. This is most likely a wording issue where "theoretical" was used loosely to mean "analytical" or refers to content in the stripped appendix. There is no evidence of intentional misrepresentation.

- **"The acceptance rule is problematic because AD values can be negative — unnormalized and unstable."** Removed as a standalone major weakness. While a valid technical observation, this is an implementation detail that can be trivially fixed (e.g., exponentiating scores or using a temperature parameter). The paper's appendix may already address this. Demoted to part of the Minor search-procedure point.

- **"AVICI vs PC comparison on Sachs ignores that AVICI was trained on different dimensionality/scale."** Removed. The paper uses this comparison to motivate the synthetic-to-real gap, which is a legitimate and well-understood observation in the field. The point about dimensionality mismatch is speculative and does not undermine the core claim.

- **"The Component-mixed condition description is vague; exact construction not given."** Removed. The description in Section 3.1 is sufficient for understanding the experimental design at a conceptual level. Detailed construction is appropriately in the appendix (Appendix B, cited).

- **"No comparison against other SCL methods (Ke et al., 2022; Zhang et al., 2025)."** Removed. The paper already compares against 8 diverse baselines including the strongest publicly available SCL model (AVICI scm-v0). Adding every SCL variant is scope creep; the current baseline set is more than adequate.

- **"Training hyperparameters (epochs, batch size, learning rate) not reported."** Removed per policy—these are standard appendix-level details.

- **"L0 norm is non-differentiable; should discuss LASSO-type relaxations."** Removed. The search is stochastic (not gradient-based), so differentiability is irrelevant. The L0 norm is the natural choice for counting edges.

- **Strength Finder: "This paper addressed an important problem" / "targeted an interesting question."** Generic framing removed. The concrete strengths retained above capture the actual evidence.

## Novel Insights

The paper's key insight—that similarity between a candidate causal graph and the true (unknown) graph can be measured indirectly through distributional alignment of their induced data distributions—is genuinely clever and well-operationalized. The AD metric elegantly sidesteps the chicken-and-egg problem of needing the true graph to evaluate candidate graphs: by regressing mechanisms from the test data under each candidate's parent sets and evaluating likelihood, it provides a self-contained signal for graph quality. The finding that this signal, combined with sparsity and followed by SCL training on the generated data, substantially outperforms both the seed graph and the highest-scoring search graph (Table 4) suggests that SCL models can extract structural information beyond what the score function alone captures—a practically significant observation.

## Suggestions

- Move the regression model class and noise assumption for AD computation from Appendix A into Section 4.1, even if just as a single sentence (e.g., "We use linear regression with Gaussian homoscedastic noise" or whatever the actual choice is).
- Add an ablation where the SCL model is trained on data generated from only the single highest-scoring graph (with multiple dataset samples) to isolate the ensemble effect.
- Run TACTIC with multiple seeds on Sachs and report standard deviation to match the reporting standard used for synthetic datasets.
- Clarify in Section 4.2 how negative scores are handled in the acceptance ratio, or switch to an exponential/Boltzmann-style acceptance.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison to paper under review |
|------|-----------|-------|----------------------------------|
| lQYi2zeDyh (Demystifying amortized CD) | 5.00 | R1 | Weaker: bivariate only, synthetic-only, analysis not method |
| ZXs3pkmrRG (TICL - Test-time interventional CD) | 5.50 | R2 | Similar concept (TTT for CD) but narrower scope, less novelty, worse evaluation |
| x3F8oPxKV2 (Zero-shot causal models) | 6.25 | R2 | Stronger technical novelty but weaker evaluation; comparable overall quality |
| zwMfg9PfPs (Out-of-variable generalization) | 6.75 | R1 | Stronger: has theoretical contributions + algorithm; accepted |

**Round 1 bracket:** 5.0–7.0 based on comparison with lQYi2zeDyh (5.00, weaker on all dimensions) and zwMfg9PfPs (6.75, stronger due to theoretical depth).

**Round 2 narrowing:** The closest comparator is ZXs3pkmrRG (TICL, 5.50), which also proposes test-time training for causal discovery but was rejected due to novelty concerns (characterized as "trivial combination" of existing methods), presentation issues, and narrower evaluation. The paper under review has clearer novelty (AD metric is original), better-motivated problem (three systematic OOD failure demonstrations), stronger empirical evaluation (synthetic + pseudo-real + real vs. bnlearn semi-synthetic), and cleaner presentation. It is clearly better than 5.50.

The x3F8oPxKV2 anchor (6.25, rejected) has a more technically sophisticated method (amortized FiP) but suffers from limited evaluation, scaling issues, and reproducibility concerns. The paper under review has a simpler method but much more thorough empirical validation and ablation. These papers are of comparable overall quality, with the paper under review having a slight edge in empirical rigor.

**Final score: 6.0.** The paper makes a clear, well-motivated contribution with a novel framework and strong experimental results. The weaknesses (AD specification in appendix, single real dataset, search procedure details, missing ablation) are all addressable and none threaten the core claims. The score reflects that the paper is competitive with accepted work in the 6.0–7.0 range but lacks the theoretical depth or large-scale real-world validation that would push it higher.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>