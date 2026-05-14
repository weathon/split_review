Now I have a complete picture. Let me synthesize the final review.

---

## Summary

This paper proposes SADRE, a density ratio estimation (DRE)-based Bayesian optimization method that incorporates semi-supervised classifiers—specifically label propagation and label spreading—to address an over-exploitation problem where supervised classifiers in methods like BORE and LFBO concentrate probability mass too narrowly on known good regions. The method handles two scenarios: one where unlabeled points are sampled from a truncated multivariate normal around labeled points, and one where a fixed-size pool is available. Empirical results on synthetic benchmarks, Tabular Benchmarks, NATS-Bench, and a 64D MNIST task show consistent improvement over BORE, LFBO, and GP-based BO.

## Strengths

- **Concrete identification and visualization of over-exploitation (Figure 1):** The paper clearly defines "over-exploitation" as distinct from general classification overconfidence—namely, that a small number of points receive high class probabilities for the class of interest, concentrating acquisition in narrow regions. Figure 1 provides visual evidence across iterations showing that MLP-based BORE/LFBO assign high probability to small regions while SADRE with label propagation/spreading spreads probability more broadly across the search space.

- **Consistent empirical improvement across diverse benchmarks:** SADRE with either label propagation or label spreading outperforms BORE, LFBO, and GP-based BO across synthetic functions (Beale, Branin, Bukin6, Six-hump camel), Tabular Benchmarks (Naval, Parkinsons, Slice), NATS-Bench (CIFAR-10, CIFAR-100, ImageNet-16-120), and the 64D MNIST task (Figures 3–7). The improvement holds in both the sampling scenario and the pool-based scenario.

- **Clean algorithm specification handling two practical scenarios:** Algorithm 1 is well-specified and the method naturally covers both the case where unlabeled points must be actively sampled and the case where a fixed-size pool is given (common in HPO/NAS). The inductive model (Eq. 7) enables querying unseen points after transductive label propagation.

- **Technically sound integration of well-established components:** The paper correctly adapts the DRE-BO framework (BORE/LFBO) by replacing the supervised classifier with graph-based semi-supervised classifiers, using standard label propagation and label spreading algorithms with an entropy-based adaptive β learning scheme.

## Weaknesses

### Major

- **Weak justification for why semi-supervised learning addresses over-exploitation:** While Figure 1 visually shows that SSL classifiers produce broader probability distributions, the paper does not explain the mechanism by which unlabeled data resolves the over-exploitation problem. The cluster assumption (Assumption 1) is invoked, but the connection between that assumption and the optimization task is not made rigorous. As the human reviewers of this paper noted, the synthetic benchmarks sample X from uniform distributions where there is no cluster structure correlated with Y, making it unclear why unlabeled points should carry information about the classification boundary. The empirical results are positive, but without a clearer mechanism, the reader cannot determine whether the gains come from SSL or simply from the graph-based smoothness prior serving as an exploration bonus.

- **The unlabeled point sampling strategy lacks principled grounding:** When a fixed pool is not available, the method samples unlabeled points from truncated multivariate normal distributions centered at each labeled point (Section 4.2). The paper invokes the cluster assumption to justify this, but the connection is tenuous: the cluster assumption refers to the natural data distribution P(X), not an artificially constructed distribution. The sampling strategy is a reasonable heuristic—placing unlabeled points near labeled ones so the graph-based classifier can propagate labels through high-density regions—but the paper does not empirically validate whether alternative sampling distributions (uniform, Sobol', Halton, which are mentioned in the Discussion) perform worse, nor does it discuss when this heuristic might fail. The sensitivity analysis for different sampling distributions is deferred to an appendix.

- **The cluster assumption may not hold in the experimental settings:** In the synthetic benchmarks, inputs are sampled uniformly from bounded search spaces, and in the tabular/NAS benchmarks, candidate points are effectively on a grid. In these settings, proximity in X-space carries no inherent information about similarity in Y. The 64D MNIST task is a partial exception (digit images may lie on a low-dimensional manifold), but as noted by human reviewers, the target function (sum of three-digit numbers) is not smooth in pixel space (e.g., "099" and "100" are nearby in pixels but far in function value). This undermines the core premise that the cluster assumption holds in the tested domains.

### Minor

- **64D MNIST benchmark dimensionality is unexplained:** The paper titles the task "64D Minimum Multi-Digit MNIST Search" but describes concatenating three MNIST images (28×28 each), which yields 2,352 dimensions. How the input reaches 64D is never explained. The validity of this benchmark as a BO testbed is also questionable given that proximity in pixel space does not correlate well with the target function.

- **No comparison against simpler fixes for classifier overconfidence:** The paper argues that supervised classifiers in DRE-BO suffer from over-exploitation, but does not test whether simpler remedies—temperature scaling, stronger regularization, or ensemble methods applied to the supervised classifier in BORE/LFBO—would achieve similar gains. This weakens the claim that semi-supervised learning is specifically needed rather than any method that produces less confident classifiers.

### Trivial

- The threshold ratio ζ is used in the Introduction before being formally defined in Section 3, which can confuse readers unfamiliar with DRE-BO.

- Σ, u, and l for the truncated normal sampling distribution (Eq. 8) are described as "set as an identity matrix" and "determined by a search space" respectively, but no guidance is given on how to set bounds for arbitrary search spaces.

## Nice-to-Haves

- A direct ablation comparing SADRE against BORE with the same graph-based classifier but without unlabeled points would isolate the contribution of unlabeled data from the classifier architecture change.

- Quantitative exploration diagnostics (e.g., distance between consecutive query points, number of distinct local optima visited) would strengthen the claim that SADRE promotes exploration rather than just providing a different inductive bias.

- Extending the method to LFBO-style utility functions beyond the probability of improvement (e.g., expected improvement) by imputing unknown y values for unlabeled points—the paper acknowledges this difficulty in the Discussion but does not attempt a solution.

- Theoretical analysis of whether the semi-supervised acquisition function preserves the connection to the probability of improvement that BORE/LFBO enjoy.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **Harsh Critic Point 3 (insufficient experimental details):** The critic complained that baseline classifier choices and experimental configurations are "relegated to an appendix that is not provided." The original submission includes these appendices; they were stripped by the parser. This is not an author error. **REMOVED under hard rule about appendix stripping.**

2. **Harsh Critic Point 3 (unfair comparison / missing ablation with BORE+SSL):** The critic demanded comparison against "BORE that uses the same graph-based pseudo-labeling." This is essentially asking the authors to ablate away their entire contribution—BORE with label propagation IS SADRE. The fair comparison is SADRE vs. standard BORE/LFBO with their intended supervised classifiers. **REMOVED as a strawman weakness.**

3. **Harsh Critic Point 5 (missing ablations in appendix):** The critic complained that ablations on β learning, flat-landscape heuristic, pool subsetting, and number of unlabeled points are "relegated to an appendix that could not be examined." These exist in the original submission. The main text does present Figure 8 (threshold ratios) and Figure 9 (pool sampling times). **REMOVED under hard rule about appendix stripping.**

4. **Harsh Critic concern about GP outperformance being "suspicious":** The critic suggested that SADRE outperforming GP on some synthetic functions "raises suspicion about the GP setup." But DRE-based methods outperforming GP-EI on certain functions is well-documented in the BORE/LFBO literature. The paper uses standard GP configurations. **REMOVED as factually unsupported skepticism.**

5. **Harsh Critic concern about "how L-BFGS-B is applied to a discrete pool":** The acquisition function π(x) is a continuous function defined over the continuous input space X. L-BFGS-B optimizes this continuous function; the pool is simply a set of possible inputs. There is no contradiction. **REMOVED as a misunderstanding of the method.**

6. **Strength Finder "addressed an important problem":** This is generic and superficial. **REMOVED.**

7. **Strength Finder "thorough ablation analyses":** Most ablations are in the (parser-stripped) appendices. The main text has Figures 8 and 9 but the bulk is deferred. This strength is overstated given what is verifiable in the main text. **REMOVED as partially unverifiable.**

8. **Harsh Critic complaint about Section 2 missing prior work combining SSL with BO:** The instructions state "DO NOT mention missing related works, as you do not have external sources to confirm their existence." **REMOVED.**

9. **Harsh Critic complaint about typos, grammar, formatting, or parser artifacts:** The instructions state to remove all such criticisms. **REMOVED.**

## Novel Insights

The paper's most interesting observation is that the over-exploitation problem in DRE-based BO is structurally different from standard classifier overconfidence: it is not about individual points receiving high probabilities, but about probability mass concentrating on a small region of the search space. Figure 1 convincingly illustrates this distinction across iterations, showing that supervised MLP classifiers in BORE/LFBO progressively narrow their high-probability region to one or two points while SSL classifiers maintain broader support. This framing—that the acquisition function should identify all regions satisfying the density ratio condition rather than collapsing to a single point—is a useful conceptual contribution even if the mechanistic explanation for why SSL achieves this remains incomplete.

## Suggestions

- Strengthen the motivation by explaining the mechanism: why does adding unlabeled points to a graph-based classifier produce a less concentrated acquisition function? The current explanation ("dilutes confidence") is intuitive but informal. A more precise argument—perhaps analyzing how the label propagation update distributes probability mass across graph components—would substantially improve the paper.

- Address the cluster assumption mismatch: either restrict the claimed applicability to settings where the assumption plausibly holds, or demonstrate experimentally that the method still helps even when the assumption is violated (e.g., on the synthetic benchmarks where X is uniform).

- Clarify the 64D MNIST setup: explain the dimensionality reduction pipeline (e.g., PCA, downsampling) and justify why proximity in the reduced space correlates with the target function.

- Add a simple baseline: BORE/LFBO with a calibrated/regularized classifier (e.g., temperature scaling or label smoothing) to test whether the gains come from SSL specifically or just from reducing classifier overconfidence.

## Score and Decision

### Calibration Anchors

| Path | Paper | Avg Human Score | Comparison |
|------|-------|----------------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iMnd6c5bAa.md` | Same paper (DRE-BO-SSL) | 3.67 (3, 3, 5) | Exact match — human reviewers flagged the same justification/motivation gaps |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CY9f6G89Rv.md` | TSBO (Semi-supervised BO) | 5.33 (6, 5, 5) | Stronger paper — more novel teacher-student framework, better ablations, clearer motivation. Our paper is weaker on motivation/justification. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OOxotBmGol.md` | LLAMBO (LLM-enhanced BO) | 8.00 (8, 8, 8, 8) | Much stronger — extensive experiments, clear motivation, novel integration. Our paper is substantially weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EXGahWDp1E.md` | Semi-supervised BNN optimization | 4.25 (5, 3, 3, 6) | Similar quality tier — interesting idea with justification gaps |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/M8XUdsjxQM.md` | CEPBO (high-dim BO) | 3.50 (3, 3, 5, 3) | Similar quality — heuristic method with limited theoretical grounding |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/562B7aLi5X.md` | Binary Losses for DRE | 6.40 (6, 6, 6, 6, 8) | Stronger — provides theoretical characterization. Different sub-area. |

### Score Justification

The paper presents a reasonable idea—using semi-supervised classifiers in DRE-based BO—with consistent empirical results across multiple benchmarks. However, it shares the fundamental weaknesses identified by human reviewers of this exact paper: the mechanism linking SSL to the resolution of over-exploitation is not explained, the sampling strategy is heuristic with tenuous connection to the cluster assumption, and the cluster assumption itself is unlikely to hold in several of the tested domains. These are not fatal errors (the empirical results are real and the method works), but they prevent the paper from being a strong, well-justified contribution.

Compared to TSBO (5.33), which offers a more principled teacher-student framework with uncertainty quantification, SADRE is simpler but also less well-motivated. Compared to the same paper's human reviews (3.67), I find the harsh critic's review was overly harsh on several fronts (appendix stripping, unfair comparison demands), so a slight upward adjustment is warranted. The paper is closer to the 4.25 semi-supervised BNN paper in quality tier: an interesting idea with real empirical gains but insufficient theoretical or mechanistic grounding.

**Score: 4.0**

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>