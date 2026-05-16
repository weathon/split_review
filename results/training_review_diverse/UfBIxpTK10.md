Now I have thoroughly read the paper and verified claims. Let me produce the final consolidated review.

## Summary

This paper tackles the problem of generalization in blind molecular docking. It makes three contributions: (1) **DockGen**, a new benchmark using ECOD domain classification that rigorously tests generalization to unseen binding domains and reveals that existing ML docking methods severely underperform when faced with novel pockets; (2) **DiffDock-L**, a scaled model integrating additional MOAD training data, larger architectures, and a van der Mer (vdM) synthetic data augmentation strategy, setting new SOTA on DockGen (22.6% vs. 7.1%); and (3) **Confidence Bootstrapping**, a self-training method that uses a confidence model's feedback to fine-tune a diffusion model on target protein clusters using only binding knowledge (no ground-truth poses), improving success from 9.8% to 24.0% on the DockGen-clusters subset.

## Strengths

1. **DockGen benchmark meaningfully exposes generalization failures.** The paper demonstrates that existing benchmarks (PDBBind) suffer from pocket similarity contamination even with low global sequence similarity (Figure 1-A shows 22% sequence identity yet nearly identical pockets). By building splits on ECOD domain classification and sourcing a held-out test set from Binding MOAD (179 ECOD clusters unseen in PDBBind), the paper convincingly shows that all prior ML methods drop dramatically: DiffDock (10 samples) falls from 35.0% on PDBBind to 7.1% on DockGen-full (Table 1). This is a valuable community resource.

2. **Scaling analysis with DiffDock-L demonstrates that data, model size, and synthetic augmentations can narrow the generalization gap.** The systematic investigation (Section 4.1, Figure 3) shows gains from adding ∼52% more training data, increasing the score model from 4M to 30M parameters, and incorporating vdM synthetic complexes. The resulting DiffDock-L surpasses the best search-based method (GNINA exhaustivity 64: 17.5%) at 22.6% on DockGen-full (Table 1), supporting the claim that scaling can substantially improve generalization.

3. **Confidence Bootstrapping is a novel and well-motivated self-training paradigm for diffusion models.** The idea of using confidence feedback from a separate model to update early diffusion steps is conceptually novel and grounded in a connection to Monte Carlo tree-search / RL (Section 3.2). The empirical result on DockGen-clusters — raising DiffDock-S from 9.8% to 24.0% success — demonstrates real practical value for adapting to new protein domains without requiring structural data, and the per-cluster analysis (Figure 4) shows consistent improvements across most clusters.

## Weaknesses

### Fatal
None.

### Major

1. **Confidence Bootstrapping lacks controlled baselines and ablations.** The method is compared only to standard DiffDock and search-based tools, with no comparison to simpler self-training alternatives — e.g., retraining on generated poses *without* confidence weighting, using a hard confidence threshold, or uniform weighting of all generated samples. Without these baselines, the observed improvement cannot be cleanly attributed to the specific mechanism of confidence-weighted, time-differentiated bootstrapping rather than to the generic effect of any fine-tuning on additional domain-specific data (even noisy). Furthermore, the key design choice of using different λ(t) and λ′(t) schedules to target early diffusion steps is not ablated. The paper states (line 138) that different schedules "direct the bootstrapping feedback principally to update the initial steps," but no experiment compares this to using identical schedules. This is a significant evidential gap: the paper's core method may be no more than a noisy self-training scheme, and the claimed exploitation of the multi-resolution structure is not empirically demonstrated.

2. **Confidence model is fixed and its calibration is unexamined.** The formalization (lines 129-136) only updates θ (the generator), not φ (the confidence model). This means the generator could overfit to the potentially flawed preferences of an out-of-distribution confidence model as it moves away from the original training distribution. The paper provides no analysis of whether the confidence model's scores remain calibrated or even correlate with RMSD on the target clusters *before* bootstrapping. If the confidence model is systematically wrong on the new cluster, bootstrapping could drive the generator toward incorrect solutions.

### Minor

1. **The λ(t)/λ′(t) schedules are not specified.** While the paper correctly formalizes the use of separate weighting functions (lines 131-133, line 138), it never specifies the actual schedules used in experiments. This under-specification harms reproducibility and makes it impossible to verify the claimed mechanism of targeting early diffusion steps. Readers cannot tell whether this design choice is critical to the method's success or a minor detail.

2. **No statistical significance or variance is reported for any metric.** The DockGen test set contains 189 complexes; the clusters subset has 85 complexes. Per-cluster analysis (Figure 4) involves clusters that may contain as few as 6-10 complexes each, where a single correct/failed prediction shifts percentages by >10 points. The paper reports only "two fine-tuning runs per cluster" with averaged results but no error bars, confidence intervals, or significance tests. This does not invalidate the results but substantially weakens the reliability of the numerical comparisons.

3. **The scaling analysis confounds three interventions.** The improvement from 7.1% to 22.6% (DiffDock-L) simultaneously increases data (+52% from MOAD), model size (20M→30M parameters), and adds vdM synthetic augmentations. While Figure 3 likely shows multiple configurations (based on the caption mentioning "different colors"), the text (line 162) only qualitatively states "some improvements" from vdM. A controlled ablation isolating each factor's contribution (e.g., 30M model with and without vdM, or 20M model with and without additional MOAD data) would substantially strengthen the analysis. The paper's stated goal of "analyzing the scaling laws" is only partially fulfilled without these disentangled comparisons.

4. **Failure cases are acknowledged but not analyzed.** Three of the eight test clusters show no improvement from bootstrapping (line 177). The paper does not discuss why — whether due to poor initial generator, insufficient binding data, wrong pocket regions, or confidence model failure. Understanding these failures would strengthen the method's credibility and guide future improvements.

5. **Computational budget is under-reported.** The paper does not specify the total number of diffusion rollouts per bootstrapping iteration, the buffer size, or the number of SGD steps per iteration. This information is important for reproducibility and for practitioners evaluating the method's cost.

### Trivial

- The vdM augmentation section does not report how many synthetic complexes were generated or whether adding them degrades performance on the standard PDBBind test set.
- The caption note "† more details in Section 4" (Table 1) references a section whose content may have been partially lost in parsing.
- Line 162 has a stray "}." artifact: "The vdM augmentation strategy also seems to provide some improvements when scaling to larger model sizes.}."

## Nice-to-Haves

- A cross-cluster generalization experiment (fine-tune on one set of clusters, test on a disjoint set) would strengthen the "unseen domains" narrative, though the current per-cluster evaluation is valid for the paper's stated setting of fine-tuning with binding-only data.
- Reporting how vdM synthetic data affects performance on the standard PDBBind test set would help calibrate concerns about potential degradation.
- An analysis of whether confidence scores correlate with RMSD on target clusters before bootstrapping would clarify whether the confidence model's feedback signal is trustworthy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about "domain adaptation, not generalization to unseen domains" (Harsh Critic Point 1).** The paper's claim (lines 19-20, 185) is about fine-tuning "on classes of proteins where binding structural data is not available." The experiment fine-tunes on complexes from target clusters *without using their structural data* (only binding knowledge) and tests on held-out complexes from the same cluster. This is exactly what the claim describes: the model is adapted to a previously unseen domain using only binding data, not crystal structures. The critic's expectation of zero-shot cross-cluster generalization is a *stronger* claim than what the paper makes. The experimental setup is appropriate for the stated contribution. A clarified framing would help, but this is not a structural flaw.

- **"The method is expensive (one model per cluster)."** The paper explicitly addresses this (lines 121-122): "docking screens are usually run on a very large number of complexes... using a restricted set of proteins. Therefore, any time that one would spend fine-tuning... would be largely amortized." This is a reasonable mitigating argument.

- **"The paper does not describe how the models are aggregated."** Line 165 says "fine-tune a model on each protein domain cluster," which clearly indicates separate models.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add ablated baselines for Confidence Bootstrapping.** At minimum, compare against (a) self-training with uniform weighting of generated poses (no confidence weighting), and (b) self-training with hard thresholding on confidence (keep only top-k poses above a fixed score). This would isolate whether the specific mechanism of exponential confidence weighting matters.

2. **Ablate the λ(t)/λ'(t) design.** Compare the full method against a version where λ(t) = λ'(t) for all t. This directly tests whether the multi-resolution targeting is responsible for the improvement.

3. **Report the actual λ(t)/λ'(t) schedules used in experiments** to ensure reproducibility.

4. **Add error bars or confidence intervals** for all main metrics, especially the per-cluster results in Figure 4.

5. **Provide a controlled decomposition of the scaling analysis** showing the effect of each intervention (data only, vdM only, model size only) in at least a 2×2 comparison.

6. **Discuss the three failing clusters** — analyze whether failure correlates with cluster size, initial confidence scores, or specific domain properties.

## Score and Decision

The paper makes three distinct contributions, each with value to the community. The DockGen benchmark is well-constructed and exposes a genuine limitation of existing evaluations. The scaling analysis, while not fully decomposed, demonstrates useful trends. Confidence Bootstrapping is a novel idea with promising empirical results. However, the core method lacks the controlled baselines and ablations needed to definitively attribute the improvement to its stated mechanism. The paper as a whole has enough independent merit — particularly the benchmark and the scaling analysis — to warrant acceptance, but the Confidence Bootstrapping contribution requires significant strengthening to fully support its claims. With revisions addressing the ablations and baselines, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>