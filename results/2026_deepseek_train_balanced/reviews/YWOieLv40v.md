Now I'll produce the final consolidated review.

## Summary

This paper proposes analyzing GNN expressiveness through multi-order interaction strengths $J^{(m)}$, empirically observes that GNN-learned interaction distributions deviate sharply from data distributions (unlike CNNs), attributes this to inductive bias from graph construction (KNN/FC), and introduces ISGR—a rewiring method that dynamically adjusts the KNN parameter $K$ based on which interaction order increases most during training. The core claims are that GNNs suffer from a "representation bottleneck" defined by failing to reach the optimal interaction distribution $J^{(m)*}$, and that ISGR alleviates this bottleneck.

## Strengths

- **Empirical observation that GNNs' learned interaction distributions deviate from data distributions, unlike CNNs.** Figures 1 and 3 show that EGNN and Molformer's $J^{(m)}$ is nearly independent of $J_D^{(m)}$, while ResNet and MLP-Mixer track their data distributions closely (lines 97–100, 190–192). This is a concrete, cross-architecture comparison not made in prior work.

- **Specific mechanistic link between the KNN parameter $K$ and the peak interaction order.** The paper notes that with $K=8$, "the number of nearest neighbors $K$... is equivalent to the order that has the highest strength in $J^{(m)}$ of EGNN" (line 100). This ties a graph construction hyperparameter directly to the observed bias.

- **Extension of multi-order interaction analysis to node-level tasks.** Equation 2 defines a node-level interaction metric $I_i^{(m)}(j)$ using a norm-based formulation, adapting the graph-level framework to tasks like force prediction (lines 44–51).

- **ISGR uses a training-time signal to estimate the optimal interaction order.** Rather than requiring domain knowledge or auxiliary OOD subgraph losses, ISGR monitors which order's interaction strength increases most during training and adjusts graph topology accordingly (lines 149–151). The concept is principled and avoids known pitfalls of OOD-based interaction losses.

- **Critical re-examination of prior theoretical work (Deng et al., 2021).** Section 6.1 identifies a flaw in the claim that $F^{(m)}$ determines $|\Delta W^{(m)}(i,j)|$, arguing that $\partial\Delta f(i,j,S)/\partial W$ varies with contextual complexity and architecture (lines 170–174).

## Weaknesses

### Major

- **Proposition 1 is stated without proof or derivation, and is arguably tautological.** The proposition (line 71) asserts that any GNN whose $J^{(m)}$ differs from $J^{(m)*}$ (the interaction strength of the global-minimum solution) must converge to a strictly higher loss. No proof, sketch, or justification is given—the surrounding text says only "Intuitively, we declare in Prop.4)." Moreover, the "representation bottleneck" is defined (line 73) as *failing to reach $J^{(m)*}$*, where $J^{(m)*}$ is itself defined as the interaction strength of the globally optimal model. Under this framing, any suboptimal model exhibits a "bottleneck" by construction, which adds no explanatory or predictive power beyond stating that the model is not optimal. The paper needs an independently measurable notion of the optimal interaction order—grounded in the task, not in the model's own loss—for the concept to carry weight. This weakens the central theoretical framing of the paper.

- **ISGR algorithm is under-specified to the point of being non-reproducible.** The method (lines 144–151) requires: (a) computing multi-order interaction strengths $I^{(m)}(i,j)$ for all node pairs across multiple orders $m$, which involves enumerating or sampling subgraphs; (b) a threshold $\bar{J}$ for triggering rewiring; (c) an update interval $\Delta e$. None of these are specified with concrete values or guided by any analysis. Crucially, there is **no discussion of how $I^{(m)}(i,j)$ is tractably computed**—the expectation over subgraphs of size $m$ is combinatorial, yet no sampling strategy, number of samples, or approximation scheme is provided. The computational overhead of computing interaction strengths during training is never discussed, which is especially concerning for scientific applications with large systems. The paper also does not analyze whether ISGR converges to a stable $K$ or oscillates.

- **No ablation studies, sensitivity analysis, or statistical rigor in the experimental evaluation.** The main results (Table 1) are embedded as a parser-illegible image, but the deeper problem is the absence of any ablation that isolates the effect of ISGR. There is no comparison to: a fixed-KNN baseline without rewiring, random graph rewiring at the same rate, or ISGR with a fixed $K$ schedule. The hyperparameters $\bar{J}$ and $\Delta e$ have no sensitivity study. No standard deviations or significance tests are reported for baseline methods (only the ISGR row shows $\pm$ values in the extractable text). For a paper whose central deliverable is a new rewiring method, the lack of controlled experiments makes it impossible to attribute any observed improvement to the interaction-strength-based heuristic versus random graph perturbation.

### Minor

- **The CNN/GNN comparison conflates two different phenomena.** The paper claims GNNs are "more affected by inductive bias than visual tasks" (line 192), but CNNs' $J^{(m)}$ tracks $J_D^{(m)}$ largely because image data *is* locally structured—the inductive bias of small kernels happens to align with the data. The paper itself notes CNNs are "bound to low-order interactions" (line 181), which is itself an inductive-bias effect. So the comparison shows that the *type* of inductive bias differs, not necessarily that GNNs are *more* constrained. The framing overstates the contrast.

- **Empirical scope is narrow relative to the title's generality.** Only two GNN architectures (EGNN, Molformer) are tested, on small-molecule datasets (QM7, QM8, ISO17 with ~7–23 atoms) and an N-body simulation. The paper acknowledges this (line 201) but frames it as a future direction rather than a constraint on the conclusions. Claims about "GNNs' representation bottleneck" broadly cannot be supported by evidence from two architectures on molecular-scale systems.

### Trivial

None.

## Nice-to-Haves

- A computational cost analysis comparing ISGR's training-time overhead against baselines would substantiate the method's practicality.
- Reporting whether ISGR converges to a stable $K$ over training would strengthen the claim that $J^{(m)}$ "gradually approximates" $J^{(m)*}$.
- ISGR could be tested on a larger system (e.g., >100 particles) to demonstrate its applicability beyond small molecules.

## Removed Points

- **"Table 1 is illegible / results not presented in verifiable form" (Harsh Critic, point 2):** Partially a parser artifact—the table exists as an image in the original PDF, and the ISGR row is extractable with values. The substantive version of this criticism (missing ablation/sensitivity/statistical detail) is retained in the Major weaknesses above.
- **"Proposition 1 is unsubstantiated" framing as fatal:** The weakness is real and retained as Major, but not Fatal—the paper's empirical observations (GNNs' $J^{(m)}$ deviates from $J_D^{(m)}$, ISGR improves performance) do not depend entirely on the proposition's validity.
- **Strength 1 from Strength Finder ("Formal definition via Proposition 1"):** Conflicts with the verified weakness that Proposition 1 is unproven and tautological. The "definition" is precisely what is problematic; removed per the rule that when a strength and weakness disagree, the weakness wins.
- **"Missing related works":** Per the hard rule, I cannot assert missing related works without external sources.
- **Formatting/style nitpicks, garbled OCR artifacts, missing appendix references:** Removed per hard rules—these are parser/formatting issues, not author errors.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews does not reveal a pattern or oversight that the paper itself does not surface.

## Suggestions

1. **Remove or substantiate Proposition 1.** Either provide a genuine proof (or sketch) connecting $J^{(m)}$ mismatch to suboptimal loss, or drop the proposition and reframe the paper as an empirical characterization of GNN inductive bias—the empirical findings stand on their own.

2. **Specify the ISGR algorithm completely.** Provide concrete values (or a reasonable range) for $\bar{J}$ and $\Delta e$, describe the sampling strategy used to compute $I^{(m)}(i,j)$ tractably (Monte Carlo? how many samples?), and report wall-clock overhead versus baselines.

3. **Add controlled ablations.** At minimum: (a) fixed KNN without any rewiring, (b) random K perturbation at the same rate, (c) ISGR with different $\bar{J}$ thresholds. This would isolate whether the interaction-strength heuristic drives improvement.

4. **Scale back the claims to match the evidence.** Replace "we prove" (line 16) and references to a general "GNNs' representation bottleneck" with language scoped to geometric GNNs on small scientific systems. The paper would be stronger as a well-scoped empirical study.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>