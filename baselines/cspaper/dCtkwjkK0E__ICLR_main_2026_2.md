---
job_id: b968ca15-f89f-4d74-8f37-03fcc6e40dca
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: dCtkwjkK0E.pdf
paper: Active Learning for Flow Matching Model in Shape Design: A Perspective from Continuous Condition Dataset
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about active learning for generative models, specifically flow matching, and includes theoretical and empirical ML components that fit ICLR topics.

## Minimum Quality
Pass ✅. The paper contains the expected major components, including abstract, introduction, methodology, experiments/results, and conclusion. While there are serious concerns about correctness, novelty, and clarity, these issues do not rise to the level of an automatic desk rejection based on the provided text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to reviewers, or other manipulative content in the paper text.

# Expected Review Outcome:
## Summary
This paper studies pool-based active learning for conditional flow matching models in continuous-label shape design problems. The core idea is a piecewise-linear analysis of conditional flow matching, from which the authors derive two query strategies, one intended to improve diversity and another intended to improve accuracy, plus a weighted hybrid strategy to trade off between the two objectives. Experiments are reported on one synthetic dataset and three shape-design datasets, comparing the proposed strategies against several active learning baselines.

## Strengths
The paper raises an interesting and underexplored question, namely active learning tailored to generative models rather than using generative models to help discriminative active learning. That framing is relevant, and the emphasis on continuous-condition datasets is a meaningful setting where standard classification-style active learning heuristics are not an obvious fit.

The paper also has a reasonably clear high-level intuition: repeated data near existing labels may help generative diversity under a condition, whereas broader label-space coverage may improve conditional accuracy. Even though I am not convinced by the formal development, the central intuition is easy to follow and could be useful as a starting point for future work.

The experiments cover multiple datasets beyond a toy problem, including airfoil, flying wing, and starship-like shape generation tasks. It is good to see the authors try to evaluate both diversity and accuracy separately rather than compressing everything into a single metric.

Some figures help communicate the intended intuition. In particular, **Figure 1** is useful for understanding the authors’ proposed diversity argument in the 1D-label case: panels (a) through (d) visually explain why adding a sample at an existing endpoint label is claimed to increase the number of possible interpolated outputs, whereas adding a point between labels may reduce the number of combinations available at a fixed condition. Likewise, **Figure 2** gives an intuitive picture of how different query rules bias selection in data space versus label space, which at least makes the intended behavioral differences between coreset, committee, \(Q_D\), and \(Q_A\) easier to parse.

The paper includes qualitative generations on the synthetic and shape datasets. **Figures 5, 6, and 8** do suggest that the authors are trying to compare diversity-oriented and accuracy-oriented acquisition behaviors in a visually interpretable way, which is appropriate for a generative design paper.

## Weaknesses
I have substantial concerns about the technical foundation, the mathematical correctness of the core claims, and the strength of the empirical evidence. At present, the paper reads more like an interesting but very preliminary hypothesis paper than a solid ICLR main-track contribution.

1. **The central theoretical assumptions are extremely strong and insufficiently justified, and much of the method depends entirely on them.**  
   The whole framework in **Section 2.2, Pages 3 to 4** assumes that the trained conditional flow matching network behaves as a continuous piecewise-linear interpolator in label space, and that when a condition \(\mathbf{c}^*\) is not in the dataset, the vector field satisfies the exact affine relation in **Equation (2)**:
   \[
   \mathbf{u}_t(\mathbf{x}', a_0\mathbf{c}_0 + \cdots + a_d\mathbf{c}_d)
   =
   a_0 \mathbf{u}_t(\mathbf{x}', \mathbf{c}_0) + \cdots + a_d \mathbf{u}_t(\mathbf{x}', \mathbf{c}_d).
   \]
   This is not a benign modeling simplification, it is essentially the entire engine of the later conclusions. But the paper does not establish when this relation should hold for the actual trained networks used in experiments. The argument appeals loosely to CPWL networks and “condensation” phenomena, but CPWL with respect to network input does not automatically imply the exact simplex-wise barycentric interpolation structure used here, especially for a deep network jointly conditioned on \((\mathbf{x}, t, \mathbf{c})\). A ReLU or LeakyReLU network is piecewise affine in its input, yes, but that does not mean the partition of the condition space forms the convex-hull interpolation geometry the paper assumes, nor that the output at \(\mathbf{c}^*\) must be the barycentric interpolation of outputs at nearby dataset labels. This gap is not cosmetic, it directly affects the validity of **Eq. (3), Eq. (5), Eq. (6)**, and the diversity/accuracy trade-off claim.

2. **The mathematical derivation around Equations (1) to (3) is unclear and appears to overstate what follows from closed-form flow matching.**  
   On **Page 3**, **Equation (1)** defines
   \[
   \mathbf{u}_t(\mathbf{x}', \mathbf{c}_0)=\frac{\sum_i p_{t,i}\mathbf{e}_{t,i}}{\sum_i p_{t,i}},
   \]
   where \(\mathbf{x}_i\) are said to be the data with label \(\mathbf{c}_0\). Then **Equation (2)** is imposed as an interpolation assumption across conditions, and **Equation (3)** concludes that generated samples belong to
   \[
   \{\mathbf{x}^* \mid \mathbf{x}^* = a_0\mathbf{x}_i + a_1\mathbf{x}_j + \cdots + a_d\mathbf{x}_k\}.
   \]
   This step is much too fast. Even if the velocity field were affine in the condition, it does not immediately follow that the terminal samples are exactly convex combinations of training examples in the very concrete set-valued form in **Eq. (3)**. The paper itself later admits in the appendix that the vector fields are “not exactly the same” but claims the final generated results are consistent because of different noise schedules. That is a major leap. In a flow model, matching a family of vector fields only approximately is not enough to conclude exact equivalence of reachable sample sets. The paper needs a rigorous argument about the induced ODE solution map, not a hand-wavy identification between field interpolation and output interpolation.

3. **Lemma 1 is not proved rigorously, and parts of the appendix are mathematically inconsistent.**  
   In **Appendix A, Pages 11 to 12**, the proof of **Lemma 1** is problematic. A few concrete issues:
   - The loss is written as \(\sum \|\mathbf{u}_t(\mathbf{x}_t,\mathbf{c}) - [(1-t)\mathbf{x}_0 + t\mathbf{x}_1])\|^2\), which does not look like the standard flow-matching target. Usually the target velocity under linear interpolation is \(\mathbf{x}_1 - \mathbf{x}_0\), not the path point itself.
   - In **Eq. (12)**, the density \(p_{t,i}\) is defined with a covariance-like term \(|\Sigma_t|^{-1/2}\), but \(\Sigma_t\) is never defined in the main text or the appendix.
   - The indexing is inconsistent across **Eqs. (15) to (19)**, with \(i,j,k,l\) and counts \(m,n,o\) introduced somewhat informally, and the notation for the condition dimension \(d\) is overloaded.
   - The proof concludes that because two vector fields are “not exactly the same” but have “consistent” final generated results, the lemma follows. That is not a proof. The equality of terminal distributions or terminal supports needs to be established, not asserted.
   Given that **Lemma 1** is used to justify **Equation (3)** and the core diversity argument, this is a serious soundness issue.

4. **Lemma 2 and Equation (5) rely on hidden assumptions that are not established, and the derivation is incomplete.**  
   On **Page 5**, **Equation (5)** states
   \[
   |f(\mathbf{x}^*)-\mathbf{c}^*| \le K \max \|\mathbf{c}_i - \mathbf{c}_j\|^2.
   \]
   The appendix proof on **Pages 12 to 13** assumes the existence of an inverse function \(f^{-1}\) on each convex hull, a bounded Hessian \(H_{f^{-1}}\), and a linear interpolation error formula. This is a lot of structure. In shape design, the map from shape to performance is typically many-to-one or at least non-invertible globally, and the paper does not justify why local invertibility should hold on the relevant regions. More importantly, the main text presents the bound as if it were a property of the model, but it is really a property that would require strong regularity assumptions on the unknown data-generating inverse map. If these assumptions fail, **\(Q_A\)** loses its theoretical basis. This matters because **Equation (6)** is sold as “intuitive” and theoretically grounded by **Eq. (5)**, but the proof does not robustly support that claim.

5. **The query strategies are underspecified and partly non-operational as written.**  
   The formulation of **\(Q_D\)** in **Equation (4), Page 4** contains several ambiguous pieces:
   - What exactly is \(\Delta \textit{entropy}\) for one candidate point? Since entropy depends on the partitioning of label space into clusters, how are clusters formed online, what threshold is used, and how sensitive is the result to this threshold?
   - The paper says this entropy is “classification entropy” after partitioning labels into clusters, but the labels are continuous. The induced discretization scheme is therefore crucial, yet no precise algorithm is given in the main paper.
   - For unlabeled pool data, labels are predicted by an RBF network, but the architecture, training procedure, and uncertainty quality of this predictor are not specified in enough detail. Since both **Eq. (4)** and **Eq. (6)** depend directly on predicted labels, the method quality may depend more on the surrogate regressor than on the proposed flow-matching theory.
   - In **Equation (7)**, \(Q_{\text{hybrid}}=\omega Q_D + (1-\omega)Q_A\) is not mathematically well-defined as written, because \(Q_D\) and \(Q_A\) are \(\arg\max\)-style selection rules, not scalar quantities. I can infer that the authors likely mean a weighted combination of the scoring functions before the \(\arg\max\), but that is not what the equation says.
   These are not tiny notation issues, they affect reproducibility and even the meaning of the method.

6. **There is a mismatch between the theoretical story and the actual experimental setup.**  
   The theory is explicitly about “closed-form flow matching models” and piecewise-linear interpolation behavior, but the experimental model in **Section 3.1, Page 7** is a generic 8-layer fully connected network trained for 4,000,000 steps. The paper does not demonstrate that this trained model satisfies the assumptions in **Section 2.2**, nor does it test any consequence of the theory directly. If the theory only applies in a special closed-form regime, while the experiments are done on standard neural flow matching, the bridge between theory and practice is missing. Right now the paper asks the reader to accept a fairly strong analytical abstraction, then evaluate a heuristic inspired by that abstraction, without checking whether the abstraction is descriptively valid for the learned models.

7. **The empirical evaluation is suggestive but not strong enough to support the paper’s broad claims.**  
   The paper claims in the abstract and conclusion that the proposed strategies “outperform” active learning methods designed for discriminative models, but the evidence is thinner than that wording suggests.
   - There are no result tables in the main paper, only plots. That is acceptable in principle, but here it makes it harder to judge exact margins, variance, and consistency across rounds and datasets.
   - In **Figure 4, Pages 7 to 8**, the diversity and accuracy trajectories are shown across four datasets, but there are no confidence intervals, no repeated-trial statistics, and no indication of variability across random initial pools. Since the initial round is random and subsequent acquisition is path-dependent, variance matters a lot in active learning.
   - The baselines are limited. The committee baseline is built from SVR, Random Forest, XGBoost, and RBF, which is reasonable as a generic regressor committee, but the paper does not compare against stronger continuous-output active learning methods tailored to regression beyond this small set, nor does it compare against simple density-aware label-space coverage heuristics that would be quite close to the proposed \(Q_A\).
   - The “anchor” method is said to work on predefined anchor conditions, but the description is brief and it is not fully clear that it is tuned comparably.
   - Most importantly, because the proposed methods do not depend on the trained flow model at all, a fair question is whether the gains simply come from choosing better label-space coverage under an RBF proxy, not from anything specifically tied to flow matching.
   This weakens the claim that the paper has established active learning principles specifically for flow matching models.

8. **The evaluation metrics are insufficiently justified for the claims being made.**  
   On **Page 6**, diversity is defined as the average pairwise Euclidean distance between generated samples integrated over label space, and accuracy is the integrated MSE between the condition and the simulated or analytically obtained label of generated samples. A few issues:
   - Average pairwise Euclidean distance is a crude proxy for diversity. A model can inflate this metric by producing spread-out but poor-quality or off-manifold samples. The paper even notes on **Page 4** that **Eq. (3)** is an upper bound on diversity because generation probabilities are ignored. That should make one very cautious about using a support-size-like story plus pairwise distance as the main diversity metric.
   - The paper does not explain how the integrals in **Eqs. (8) and (9)** are approximated in practice, over what label grids, or whether the approximation is comparable across datasets with different label dimensions.
   - For shape generation tasks, it would be useful to report additional metrics tied to realism or validity of the generated geometry, not just label error and pairwise shape spread.
   These choices do not invalidate the experiments, but they make the empirical story much less convincing than the paper suggests.

9. **The figures are not always aligned with the claims they are supposed to support.**  
   **Figure 3** is used to argue that \(Q_D\) yields the highest diversity and \(Q_A\) the lowest on the synthetic dataset. Visually, the difference is plausible, but the figure is qualitative and limited to condition 0.5. If this figure is meant to support a general diversity claim, it is too narrow. More broadly, **Figure 2** is an intuition figure built from a 2D Gaussian toy construction; it helps illustrate differences in selected points, but it does not validate the piecewise-linear flow-matching theory. In other words, the paper often uses intuitive visuals where stronger quantitative evidence is needed.
   
10. **Presentation and notation issues are frequent enough to impede careful reading.**  
   There are many places where the writing becomes hard to parse, for example on **Page 3**: “when condition \(\mathbf{c}_0\) in the labels of the dataset”, or the repeated confusion between \(k\) and \(d\) in **Equation (2)**. The notation for labeled and unlabeled sets in **Section 2.1** is also awkward, with both bold uppercase collections and bold lowercase elements introduced inconsistently. This may sound minor, but in a theory-heavy paper these inconsistencies make it much harder to verify what is actually being claimed.

11. **The contribution is more incremental and heuristic than the paper’s framing suggests.**  
   Stripped to its practical core, \(Q_A\) is essentially label-space coreset selection using predicted labels, which the paper itself acknowledges on **Page 5**. \(Q_D\) combines preference for labels close to existing labels, more balanced label clusters, and feature-space novelty. That is a reasonable heuristic, but the jump from these heuristics to a claimed “theoretical characterization” of flow-matching generalization feels overstated. If the paper positioned itself more modestly as a pilot heuristic motivated by a simplified model, I would be more sympathetic.

## Questions
1. The main technical question is about **Equation (2)** and the piecewise-linear interpolation assumption in **Section 2.2**. Can the authors provide direct empirical evidence, on the trained models used in **Section 3**, that \(\mathbf{u}_t(\mathbf{x}',\mathbf{c})\) behaves approximately affinely with respect to \(\mathbf{c}\) within local simplices of label space? For example, measure
   \[
   \left\|
   \mathbf{u}_t(\mathbf{x}',\mathbf{c}^*)
   -
   \sum_{i=0}^d a_i \mathbf{u}_t(\mathbf{x}',\mathbf{c}_i)
   \right\|
   \]
   on held-out local tuples \((\mathbf{c}_0,\dots,\mathbf{c}_d,\mathbf{c}^*)\). If this approximation fails, the theoretical narrative becomes hard to maintain.

2. Please clarify the exact operational form of the hybrid strategy in **Equation (7)**. Do you combine the scalar acquisition scores underlying \(Q_D\) and \(Q_A\), then apply \(\arg\max\), or do something else? As written, the equation combines query operators rather than scores.

3. For **\(Q_D\)** in **Equation (4)**, please give a fully specified algorithm in the rebuttal: how are continuous labels clustered, how is the threshold chosen, how is \(\Delta\)entropy computed for each candidate, and how sensitive are results to those choices?

4. Can the authors provide repeated-run statistics, such as mean and standard deviation over multiple random initial pools, for the results in **Figure 4**? This would substantially increase confidence because active learning curves are often unstable.

5. Since both proposed methods depend on predicted labels from an RBF network, how sensitive are results to the label predictor? Replacing RBF with another regressor, or reporting predictor accuracy on a held-out set, would help establish whether the gains are due to the proposed acquisition logic rather than a specific surrogate.

6. For **Lemma 2**, what assumptions are actually intended on the map \(f\) and \(f^{-1}\)? Is local invertibility assumed in every simplex of label space? If so, please state these assumptions clearly in the main paper. As written, the theorem appears stronger than the proof supports.

7. If there are no tables in the main paper by design, I strongly recommend adding at least one compact quantitative summary table in revision, reporting final diversity/accuracy values, gains over baselines, and variability. The current figure-only presentation makes it too easy to over-read noisy trends.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The application domain is shape design with simulation-generated labels, and the paper does not present obvious privacy, fairness, or human-subject issues.

## Soundness Rating
2: fair. The paper has an interesting intuition and some empirical support, but the core mathematical claims are not established convincingly, and several derivations and assumptions are too shaky to support the strength of the stated conclusions.

## Presentation Rating
2: fair. The paper is readable at a high level, and some figures are helpful, but the notation, equations, and methodological details are often unclear or underspecified.

## Contribution Rating
2: fair. The topic is relevant and the pilot-study angle is interesting, but the current combination of strong claims, fragile theory, and limited empirical rigor makes the overall contribution fall short of ICLR main-track standards.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper asks a worthwhile question and contains some promising intuitions, but there are too many substantive issues in the current version, especially around the validity of the theoretical framework and the precision of the method specification. I see this as closer to a promising early-stage idea than a publishable ICLR main-track paper.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main reasons for my score are the mismatch between the strength of the paper’s claims and the actual level of theoretical and empirical support provided.