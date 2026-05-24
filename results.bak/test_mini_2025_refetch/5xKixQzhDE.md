Now I have sufficient calibration data. Let me write the consolidated review.

## Summary

This paper proposes Hyperparameter-Calibrated Dataset Condensation (HCDC), a method that learns a synthetic validation dataset such that validation-performance rankings of models with different hyperparameters are preserved when replacing the original dataset with the condensed one. The key idea is to match *hypergradients* (gradients of the validation loss w.r.t. hyperparameters) computed on the condensed and original datasets, using implicit differentiation and Neumann-series Hessian approximation for efficiency. Experiments on image (CIFAR-10/100 with NAS-Bench-201) and graph (Cora, Citeseer, Ogbn-arxiv, Reddit) benchmarks show that HCDC dramatically improves Spearman rank correlations over coreset and standard condensation baselines, and accelerates off-the-shelf NAS algorithms.

## Strengths

1. **Novel and well-motivated problem formulation.** Reframing dataset condensation for hyperparameter ranking preservation (rather than single-architecture generalization) is a genuine contribution. The paper clearly motivates why existing condensation methods fail at this task (negative correlations, Table 1) and provides a principled alternative.

2. **Strong empirical results on image data.** Table 1 shows HCDC achieves Spearman correlations of 0.74 (CIFAR-10) and 0.63 (CIFAR-100), while all eight baselines (coreset and standard condensation methods) produce negative or near-zero correlations. The selected-architecture test performance (92.9%, 72.4%) is close to the oracle optimum (93.5%, 72.9%).

3. **Consistent gains on graph data across multiple compression ratios.** Table 2 reports that HCDC attains correlations of 0.80–0.90 on Cora, Citeseer, Ogbn-arxiv, and Reddit using only 0.9%–5.2% of the original nodes, consistently outperforming GCond by 0.1–0.2 correlation points. The improvements hold across all four datasets and all three compression ratios, with narrow confidence intervals.

4. **Theoretical connection between hypergradient alignment and ranking preservation.** Theorem 1 formally links hypergradient alignment (Definition 2) to hyperparameter calibration (Definition 1) on a connected compact set, providing a principled justification for the HCDC objective beyond heuristic gradient matching.

5. **Demonstrated acceleration of NAS.** Figure 4 shows that GraphNAS on HCDC-condensed graphs reaches ~71.8% accuracy by 140 seconds, while the same algorithm on the original graph only reaches ~70.5%. This directly supports the claim of faster hyperparameter/architecture search.

6. **Efficient implementation.** The use of IFT with Neumann-series inverse Hessian approximation (Lorraine et al., 2020) provides constant-memory hypergradient computation, making the algorithm tractable for practical model sizes.

## Weaknesses

### Major

1. **Missing specification of which SDC method generates the fixed synthetic training set.** The paper repeatedly states that the synthetic training set $\mathcal{S}^{\text{train}}$ is "predetermined by any standard dataset condensation (SDC) algorithm" (Section 5.1, Algorithm 1 input), but the experiments never state which specific method is used. The experimental section lists DC, DSA, DM, KIP, and TM as baselines, but does not say which one produces the training set for HCDC. This is essential for reproducibility — different SDC methods produce training sets of very different quality, which directly affects HCDC's results.

2. **Table 3 (NAS speed-up on images) has empty HCDC and Original columns.** The parsed text shows the HCDC and Original columns contain no numerical values for DARTS-PT or REINFORCE. The text claims "the test performance of the selected architecture on the HCDC condensed dataset is consistently higher" without presenting the numbers. If this is not a parser artifact, it is a serious omission; if it is an artifact, the paper should be checked for completeness before publication.

### Minor

3. **Baseline comparison conflates the "learned validation set" effect with the "hypergradient alignment" effect.** Baselines (DC, DSA, DM, etc.) randomly split their condensed training data to obtain a validation set, while HCDC learns a separate synthetic validation set via hypergradient matching. Because the baselines have no mechanism to produce a separate validation set, the comparison is asymmetric. An ablation that adds a learned validation set to a baseline (e.g., applying the same hypergradient-matching loss on top of a fixed DC training set) would isolate the contribution of the objective from the extra learnable parameters. The paper's framing of HCDC as a *complement* to any SDC method (Figure 1) partly addresses this concern, but the claim that "HCDC is much better at preserving the performance ranking" (Section 7) would be strengthened by the ablation.

4. **Theoretical justification is incomplete in the main text.** Theorem 1 claims equivalence between hypergradient alignment and hyperparameter calibration on a connected compact set, but the proof is deferred to the appendix (which is stripped by the parser). The sketch in Section 4 uses a first-order Taylor expansion and states the implication is "straightforward," but a more detailed sketch of the integration argument (or the required smoothness assumptions) would help the reader evaluate the claim without consulting the appendix.

5. **Figure 2 caption contains conflicting descriptions.** The paper includes three different captions for Figure 2: one says "darker red indicating better performance" (line 244), another says the same (line 259), and a third says "lighter shades refer to better performance" (line 261). Additionally, the correlation values listed in the Figure 2 table (HCDC: +0.074) differ by a factor of 10 from Table 1 (HCDC: 0.74 ± 0.21), which may indicate a parsing issue but should be verified.

### Trivial

6. **Algorithm 1's Line 7 is ambiguous.** The pseudocode updates $\lambda$ (the hyperparameter being searched over) in the inner loop, which could confuse readers. The surrounding text clarifies that this is part of the extended-space trajectory construction (Appendix H), but the pseudocode does not distinguish the original discrete set $\Lambda$ from the continuous relaxation used for trajectory generation. A comment or reformatting would help.

7. **"CIFAR-100 or CIFAR-100" typo in Section 7** (line 242) — the text says both datasets are "CIFAR-100" when one should be CIFAR-10.

## Nice-to-Haves

- A computational cost comparison (wall-clock time for condensation + search) between HCDC and standard condensation methods. The paper emphasizes speed-up during search but does not report the cost of the HCDC condensation phase itself. If HCDC condensation takes e.g. 5× longer but yields 10× faster search, the trade-off is favorable, but the reader cannot judge.
- Adding error bars to the "Whole Graph Perf." column in Table 2 for consistency (the column already has them — 83.8 ± 0.4 — but they are only reported once per dataset rather than per compression ratio).

## Removed Points

- **Criticism about missing related work**: Removed per instructions (cannot verify existence of unlisted works).
- **Criticism about "unfair comparison because baselines don't learn a validation set" as a fatal flaw**: Downgraded from fatal to minor. HCDC is explicitly designed to learn a validation set; baselines are training-set condensation methods with no mechanism for this. The paper frames HCDC as a complement to SDC methods, so the comparison is appropriate in context. However, an ablation isolating the hypergradient objective from the extra parameters would strengthen the paper, which is noted in the Minor weaknesses.
- **Criticism about missing appendix/proofs**: Removed per instructions — the parser strips these sections from all papers.
- **Generic "reproducibility" concerns about undisclosed hyperparameters**: Removed as nitpicks.
- **Strength Finder's generic strengths** (e.g., "important problem," "timely topic"): Removed as too generic or conflicting with verified weaknesses.

## Novel Insights

The HCDC approach reveals an important insight that goes beyond the paper's own contributions: hyperparameter ranking preservation during dataset condensation can be formulated as a *bilevel optimization over a bilevel optimization*, and the natural resolution is to match first-order derivatives of the inner objective with respect to the outer variable. This contrasts sharply with standard condensation methods (DC, DSA, MTT) that match training-loss gradients w.r.t. model parameters — a fundamentally different quantity. The observation that standard methods can produce *negative* correlation (Table 1), while even a simple random coreset sometimes beats them, strongly suggests that the conventional condensation objective inadvertently destroys the hyperparameter information that HPO needs. This reframes much of the dataset condensation literature: methods optimized for single-architecture test accuracy may be actively harmful for downstream HPO, and a separate validation-oriented condensation objective is necessary.

## Suggestions

1. **Specify which SDC method generates $\mathcal{S}^{\text{train}}$** in each experiment (images and graphs), and report its hyperparameters.
2. **Add an ablation** comparing HCDC against a baseline that also learns a validation set (e.g., adding the hypergradient-matching objective on top of a fixed DC training set). This would cleanly isolate the effect of the hypergradient objective from the effect of having additional learnable parameters.
3. **Fill in Table 3** with HCDC and Original columns' numerical values for DARTS-PT and REINFORCE, or explain why they are absent.
4. **Add a brief sketch of the Theorem 1 proof** in the main text (even 3-4 lines showing the integration argument), and explicitly acknowledge that the finite-sample optimization only approximately satisfies the alignment condition.
5. **Resolve the Figure 2 caption** inconsistency and verify the correlation values match Table 1.
6. **Clarify Algorithm 1** by adding a comment that Line 7 generates HPO trajectories (Appendix H) and does not directly optimize the hyperparameters.

## Score and Decision

**Calibration details.** Round 1 bracketing placed the paper between the weak anchor band (scores 1.5–3.4, papers on unrelated HPO topics) and the strong anchor band (scores 7.75–8.0, data selection theory and pretrained model tuning). The most relevant anchors are in the middle band (3.5–7.5): four dataset condensation papers scored 3.8–5.75 (all rejected) and two accepted posters at 6.5 and 7.0. Round 2 refined within (4.5, 8.0) using queries for dataset condensation with cross-architecture/NAS evaluation, retrieving additional anchors: AutoUAD (6.0, accepted), Lossless Distillation (7.0, accepted poster), GIFT (6.5, accepted poster). Comparing against these: HCDC has a more novel problem formulation than the 5.0–5.75 rejected anchors and comparable novelty to the accepted ones, but its presentation issues (missing Table 3 data, unspecified SDC method, caption inconsistency) place it slightly below the GIFT (6.5) and Lossless Distillation (7.0) anchors, which are more polished. The paper sits between the best rejected anchors (5.75) and the accepted poster anchors (6.5), closer to the latter.

**Final score: 6.0.** The paper makes a genuine, well-motivated contribution to dataset condensation by reframing the problem for hyperparameter search. The empirical results are strong and consistent across two domains. The main issues are presentation completeness (missing specification of the SDC method, empty cells in Table 3, caption inconsistency) rather than fundamental flaws in the approach. These are addressable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>