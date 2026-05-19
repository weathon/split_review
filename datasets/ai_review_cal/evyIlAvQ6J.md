- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 3
I have now thoroughly verified all claims against the paper. Here is my consolidated final review.

---

## Summary

The paper introduces the **Flow Tree**, a novel data structure that captures the dynamics of a group of navigation trajectories by encoding decision divergences through time. It is presented as a discrete, directional adaptation of the Reeb graph: nodes correspond to points where trajectories diverge, and edge weights encode subgroup sizes. The paper demonstrates the Flow Tree on a human VR navigation dataset (100 participants, 72 start–goal pairs), using it for (1) predicting path difficulty from tree features/embeddings/shapes, (2) dynamically predicting individual success as a trajectory progresses, and (3) hypothesis testing between groups of successful vs. unsuccessful navigators.

## Strengths

- **Clear formal definition and construction (Section 3.1, Definition 2, Figure 2):** The Flow Tree is precisely defined as an attributed tree built from a collection of trajectories, with nodes at decision splits and edge weights encoding subgroup fractions. Complexity bounds are provided (Proposition 1: O(N·M) time, O(M) space). This makes the method reproducible and distinguishable from prior static approaches (heat maps, path-length summaries).

- **Predictive advantage for path difficulty over static baselines (Figure 4E):** Flow Tree features achieve the lowest RMSE (0.201) compared to static features (0.227) and heat maps (0.219) using 5-fold cross-validation across 72 paths. Flow Tree features also show strong correlations with success rate (e.g., average branching factor r=−0.647), and the directionality advantage (e.g., N→Y vs. Y→N) is a genuinely novel capability that static metrics cannot capture.

- **Three complementary analysis frameworks (Sections 3.2, 4.3–4.5):** The paper provides features, graph embeddings (graph2vec), and shape-based (permutation-class) representations of Flow Trees, along with a metric-space hypothesis-testing framework using Fréchet means and permutation tests. This breadth demonstrates the versatility of the tool across different analytical paradigms.

- **Formal complexity analysis (Proposition 1):** Worst-case time O(N·M) and space O(M) are derived, grounding the method's computational practicality explicitly.

## Weaknesses

### Fatal
None.

### Major
- **Dynamic prediction experiment lacks baseline comparisons (Section 4.4, Figure 5).** The paper reports that AUC rises from 0.6 after the first split to 0.81 after three splits, but provides no comparison to any alternative predictor. Reasonable baselines would include: (a) using the overall path success rate as a static predictor, (b) conditioning on the current location only (ignoring the tree's hierarchical grouping), or (c) a simple belief-update model based on observed correct/incorrect turns. Without such baselines, it is unclear whether the Flow Tree's tree structure adds value beyond what any method would achieve by conditioning on more steps. This weakens the claim that "a trajectory through the Flow Tree is predictive of that individual's success" as a distinct contribution of the tree structure itself.

### Minor
- **Hypothesis-test group size imbalance not controlled (Section 4.5).** The paper states: "Assume the number of individuals in each group are the same to not inherently bias the complexity of the tree." However, participants are split by average accuracy, which will almost certainly yield unequal group sizes. No subsampling, matching, or adjustment procedure is described. If one group is larger, its Flow Trees will naturally have more splits due to sampling alone, inflating the test statistic. The assumption is stated but not validated or enforced.

- **Handling of incomplete / unsuccessful trajectories is not specified (Section 3.1, Definition 2).** Definition 2 says "consider M trajectories going from A to B," but it is ambiguous whether this includes trajectories that never reach B (e.g., timed out, took wrong turns). This affects both the tree structure and the edge-weight interpretation. The dynamic prediction experiment (Section 4.4) uses "successful and unsuccessful trajectories" as training labels, which suggests unsuccessful trajectories exist, but their role in Flow Tree construction is not clarified.

- **Number of trajectories per start–goal pair is not reported.** The paper states that 100 participants each attempt 48 of the 72 possible paths (Section 4.1). This means some paths likely have far fewer than 100 trajectories. The distribution is not given, and no analysis checks whether predictive performance degrades on sparsely sampled paths. This is relevant for assessing the reliability of the Flow Trees used throughout.

- **Unsupported generalization claims in the conclusion (Section 5).** The paper claims Flow Trees are "broadly applicable across spatial navigation datasets… also to abstract graph spaces, like the internet or Wikipedia." This is not tested — only one discrete-maze VR dataset is used. While speculation about future applications is acceptable, the phrasing reads as a validated finding.

### Trivial
None.

## Nice-to-Haves

- Add a baseline to the dynamic prediction experiment (see Major weakness). A simple one: at each node, predict success using the overall success rate of all trajectories reaching that node, ignoring the tree's hierarchical grouping. This isolates whether the tree structure adds predictive information beyond location-conditioned rates.
- Analyze sensitivity to the "no merge" design choice. When trajectories reconverge, the Flow Tree treats them as permanently separate branches. A controlled comparison (e.g., artificially merging branches that reconverge within a small number of steps) would help bound the impact.
- Report the runtime of the shape-distance computation for the 72×72 distance matrix, which would clarify practical feasibility.

## Removed Points

These points were identified in the reviewer inputs but are removed (with justification):

- **Data leakage in path-difficulty regression (Harsh Critic Point 1).** *Reason for removal:* This criticism misunderstands the experimental setup. The regression is across 72 paths (one Flow Tree per path, one success rate per path). 5-fold cross-validation is applied across **paths**, not across trajectories within a path. Each path appears in only one fold. The Flow Tree for path X is built from path X's trajectories, and path X appears in either the training or test set — never both. There is no cross-contamination. Both Flow Tree features and baseline features are computed per-path in the same way, so the comparison is fair. This criticism is not a valid weakness.

- **Missing related work on trajectory aggregation trees.** *Reason for removal:* Per the review guidelines, missing related works are not to be mentioned, as the reviewer cannot verify their existence or relevance without external sources.

- **Reproducibility nitpicks about undisclosed hyperparameters and implementation details (e.g., split criterion at reconvergence).** *Reason for removal:* The paper provides a definition of Flow Tree construction (Section 3.1) and pseudocode-equivalent prose. Specific implementation details like "whether a node is created only when the next step differs" are reasonable to clarify but not essential for reproduction given the clarity of the construction. Per guidelines, trivial implementation details are removed.

- **Formatting / style nitpicks.** *Reason for removal:* Parser artifacts do not reflect the original submission.

- **Criticism that "Flow Trees cannot be independently verified."** *Reason for removal:* The paper states code will be made public. Per hard rules, this does not constitute a valid weakness.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest evidence (the path-difficulty regression, Figure 4) is also its most straightforward claim, while the most novel experiment (dynamic prediction, Figure 5) is the one where the evaluation is weakest. The reviewers converge on the value of the Flow Tree as a *descriptive* tool (visualization, hypothesis testing), but diverge on whether the *predictive* claims are sufficiently supported. The missing baseline in the dynamic experiment is a gap that neither the overly harsh (who fatally condemned the regression experiment on incorrect grounds) nor the strength finder (who uncritically accepted the dynamic predictions) fully addressed with the right level of severity.

## Suggestions

1. **Add baselines to the dynamic prediction experiment (Section 4.4).** At minimum, compare to a location-only prediction (success rate of all trajectories passing through the same node, without tree structure) and the overall path success rate. This would isolate the value added by the tree's hierarchical grouping.
2. **Address the group-size confound in the hypothesis test (Section 4.5).** Subsample the larger group to match the smaller one's size before computing Flow Trees, or use a resampling procedure that keeps group sizes fixed. Report results with and without this control.
3. **Clarify whether incomplete trajectories are included in Flow Tree construction (Section 3.1, Definition 2).** State explicitly whether "M trajectories going from A to B" includes only successful trajectories, and if unsuccessful ones are included, describe how they are handled at leaf nodes.
4. **Report the distribution of trajectory counts per start–goal pair.** Include a histogram or summary statistics. If some paths have fewer than ~20 trajectories, flag the potential for noisy Flow Trees and check whether predictive performance degrades on those paths.
