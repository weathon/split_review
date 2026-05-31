Now let me synthesize the review carefully.

## Summary

This paper studies how the scale (measurement variance) of variables can cause score-based structure learning algorithms to prefer incorrect DAGs. It extends prior work (Loh & Bühlmann 2014; Reisach et al. 2021) by providing theoretical conditions for d-dimensional chains/forks/colliders (Propositions 2–6), showing that the problem persists under non-linear dependencies through the equivalence of log-likelihood and MMSE under Gaussian noise (Propositions 7–10), and empirically demonstrating the effect for NOTEARS, DAG-GNN, GraN-DAG, and GES on synthetic and real-world data.

## Strengths

1. **Extension of scale-sensitivity theory to d-dimensional atomic structures.** Propositions 2–6 provide explicit conditions under which the MMSE is lower for the wrong DAG (reversed chain, fork, collider, additional edge) for d-dimensional chains, forks, and colliders. This moves beyond the prior 2-node results and gives practitioners concrete conditions to reason about when scale can mislead structure learning.

2. **Extension to log-likelihood based losses (BIC, ELBO).** Propositions 7–10 prove that under Gaussian noise, log-likelihood, BIC, and ELBO reduce to the MMSE and are therefore similarly susceptible to scaling. This is a stronger conclusion than prior work (which focused only on least squares) and is consistent with the empirical finding that DAG-GNN (ELBO) and GES (BIC) are impaired by scaling.

3. **Systematic multi-algorithm, multi-setting empirical validation.** The paper tests four distinct learners (NOTEARS, DAG-GNN, GraN-DAG, GES) across linear/non-linear dependencies, 3/10-variable chains/forks/colliders, random 10-node DAGs, and one real-world dataset, with repeated trials. The "100% of cases" failure rate for NT/DG/GND under the tested conditions (10–30 repetitions) is a striking demonstration that the phenomenon is not algorithm-specific or a rare edge case. The ablation showing the problem persists even when assumption (A1) is violated (Section 4 Q3) meaningfully extends the empirical scope beyond the atomic structures used in the theory.

4. **Clear practical motivation.** The medical example (Figure 1) concretely illustrates that choosing the wrong DAG can flip a treatment decision (0.49 vs. 0.51 threshold), grounding the technical results in real-world stakes.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical scope substantially narrower than the paper's framing.** The title ("Learning Large DAGs is Harder than you Think") and abstract claim "conditions under which square-based losses are minimal for wrong DAGs in d-dimensional cases." In practice, Propositions 2–6 are proven only for chains, forks, and colliders. The attempt to generalize via Remark 1 ("each DAG can be decomposed into subgraphs fulfilling (A1)") is not rigorous: overlapping roles (a node being both a fork and a collider) are explicitly excluded despite being the typical case in real graphs. The paper's own Limitations section acknowledges this, but the main text, title, and abstract frame the contribution more broadly, which risks over-interpretation by practitioners. The gap between the framing and the actual theoretical scope is large enough that it needs to be addressed.

2. **Insufficient statistical rigor in experimental reporting.** The paper repeatedly reports "100% of the cases" for NT, DG, and GND but provides no confidence intervals, standard deviations, or effect sizes. While 10–30 repetitions all showing the same result is suggestive of a deterministic effect, the absence of any variance reporting means the reader cannot assess the stability of the results across different scaling magnitudes or random seeds. Scaling factors are not reported, so the sensitivity (e.g., smallest factor that causes a flip) is unknown. The non-linear experiments test only a single function (cosine), leaving the generality of the non-linear extension unclear. These gaps weaken the evidential weight of otherwise consistent experiments.

3. **Undiscussed tension with prior work on standardization.** Reisach et al. (2021) showed that NOTEARS exploits variance ordering and that standardization *reduces* performance because it removes the sorting signal. The present paper argues that scale causes wrong DAGs and suggests standardization (as part of SRL) as a remedy. The paper briefly cites Reisach et al. but does not address this apparent contradiction: if standardization helps here but hurts in Reisach et al.'s setting, the practical recommendation is ambiguous. A practitioner needs to know when standardization is beneficial and when it might backfire. This omission substantially limits the practical actionability of the paper's message.

### Minor

1. **SRL is acknowledged as limited but this limits its practical value.** The proposed Scale Robust Loss requires knowing which nodes have no parents, which is circular in structure learning. The paper is upfront about this limitation ("SRL can only be used for discrete structure learners"), but this means the paper's proposed remedy is not applicable to the continuous optimization methods (NOTEARS, DAG-GNN, GraN-DAG) that are the main focus of the experiments. The section reads more as a suggestion than a solution.

2. **Limited real-world validation.** Only one real-world dataset (Sachs et al., 11 variables) is used, and the evaluation protocol (use the original SL prediction as pseudo-ground-truth, then scale and check for changes) is a sensitivity check rather than a validation that the original prediction was correct. While a reasonable approach given the lack of known ground truth, the empirical claim of real-world relevance would be strengthened with additional datasets.

3. **The non-linear theoretical result does not provide conditions for wrong DAGs.** Proposition 7 shows equivalence of MMSE and log-likelihood under Gaussian noise for potentially non-linear functions, but the paper explicitly notes (line 130) that "it is not trivial to derive conditions under which the optimum of the log-likelihood render a wrong DAG without additional assumptions." The non-linear experiments are thus empirical only. The framing ("show that scale can impair performance... if relations among variables are non-linear") is accurate, but the theoretical extension for non-linearity is thinner than the linear case.

### Trivial
None.

## Nice-to-Haves
- Reporting scaling factor magnitudes and sensitivity analysis (smallest factor causing a flip).
- Testing constraint-based algorithms (e.g., PC, FCI) as a control to confirm they are unaffected, since they are scale-invariant by design.
- Additional non-linear functions (e.g., sine, polynomial) to broaden the evidence.

## Removed Points
These points from the reviewers are removed with justification:

1. *"No detail on default hyperparameters or implementations"* — The harsh critic noted this as a reproducibility concern, but implementation details for standard algorithms (NT, GES, DAG-GNN, GraN-DAG) are well-known and the paper refers to the appendix for further details. This is a standard level of description for a paper of this type.

2. *"Section 2.1 (A1) is very restrictive"* — The paper explicitly acknowledges this assumption, tests its violation empirically in Q3, and discusses it in the Limitations section. The restriction is stated transparently.

3. *"Proposition 5 (MEC) is particularly sweeping"* — The critic questions whether it holds for arbitrary MEC members that may not decompose cleanly. Without being able to verify the appendix proof, this speculation about incomplete decomposition should not be elevated to a confirmed weakness.

4. *"The 100% match... without variance estimates or details on scaling factor magnitude, it is hard to assess how robust the result is"* — This is covered in the Major weakness about experimental rigor above, but the specific claim about "hard to assess" is weakened by the fact that 30/30 or 10/10 is a statistically meaningful result for a deterministic phenomenon.

5. *Strength Finder strengths about "generalization to d-dimensional structures" and "impactful medical example"* — These are genuine strengths; I have incorporated them above.

6. *Strength Finder: "Systematic multi-algorithm, multi-setting experiments"* — This is kept as a strength above.

7. *Various nitpicks about missing appendix content* — The parser strips appendix content from all papers; these existed in the original submission.

## Novel Insights

The most interesting observation that emerges from the reviews is the asymmetric behavior of GES (and GES with SRL) compared to the continuous optimization methods (NT, DAG-GNN, GraN-DAG). GES is substantially more robust to scaling in the complex DAG experiments (~20% affected vs. 100%), and SRL further improves it for atomic structures. This suggests that the greedy search strategy may implicitly regularize against scale-driven errors, and that the discrete vs. continuous optimization distinction could be as important as the loss function choice for scale robustness. This insight goes beyond the paper's own emphasis and points toward a deeper investigation of how optimization strategy interacts with scale sensitivity.

## Suggestions

1. **Scope the theoretical claims honestly in the abstract/title.** Replace "Learning Large DAGs" with something like "Learning DAGs from Scaled Data" and acknowledge upfront that the theoretical conditions are proven for chains, forks, and colliders.
2. **Add error bars, confidence intervals, or standard deviations** to the key experimental results, even if only in the appendix. At minimum, show how the effect varies with scaling factor magnitude.
3. **Add a paragraph addressing the Reisach et al. tension.** Discuss conditions under which standardization helps vs. hurts, perhaps noting that it depends on whether the variance ordering is causally meaningful or arbitrary.
4. **Expand the non-linear experiments** to at least one additional function beyond cosine.
5. **Report scaling factors** used in the experiments so the results are reproducible and interpretable.

## Score and Decision

**Round 1 bracket:** After reading the paper, I estimated it sits between score 4 and 7 based on initial comparison with the three retrieved bands (weak anchors at ~3.0, middle at ~4.5–5.0, strong at 8.0). The paper clearly exceeds the weak band (papers that were rejected with fundamental issues) but falls far short of the strong band (8+ papers on different topics).

**Round 2 narrowing:** Reading four papers in the 4.5–5.3 range:
- ψDAG (4.67, Reject): Proposed a new algorithm but had weak theory and non-existent code. This paper is **stronger** — its core empirical finding is clearly demonstrated and reproducible.
- Progressive Acyclicity (5.00, Reject): Identified an optimization issue with a heuristic fix. Similar level — both papers identify a real problem with limited solution, but this paper has better theoretical grounding.
- Moment Matters (5.00, Reject): Theorem + method paper. **Comparable** — both have clear theoretical contributions limited by strong assumptions.
- Score-based Greedy Search (5.33, Accept): Novel algorithm with identifiability guarantees. This paper is **weaker** — its contribution is more of a cautionary finding than a new method, and it addresses a gap in understanding rather than proposing a deployable solution.

The paper under review sits near the upper end of this band. Its contribution — demonstrating that scale deterministically misleads score-based structure learning, with theoretical conditions for d-dimensional atomic structures — is genuine and well-supported empirically despite the noted gaps. However, the overclaiming in the framing and the experimental rigor issues prevent it from being a clear accept.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>