Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper introduces a neural network-based framework for computing continuous optimal transport (OT) plans with general cost functionals, going beyond standard Euclidean costs. The core theoretical contribution is a maximin reformulation (Theorem 1) that subsumes prior classic and weak OT formulations, paired with a duality-gap error bound (Theorem 3) that avoids convexity assumptions on the dual potential. Two practical instantiations are presented: a class-guided functional for dataset transfer (preserving class structure across domains) and a pair-guided functional for supervised image-to-image translation. On the dataset transfer task (FMNIST→MNIST), the method achieves 83.22% accuracy with only 10 labeled target samples per class, dramatically outperforming unsupervised baselines (~10%, i.e., random chance).

## Strengths

- **Generic maximin reformulation unifying prior OT frameworks**: Theorem 1 derives a saddle-point formulation for general cost functionals $\mathcal{F}$ that automatically reduces to known formulations for classic OT and weak OT when the cost functional is specialized. This provides a genuine theoretical unification, and the paper explicitly traces these connections (Section 4, "Relation to prior works").

- **Class-guided functional solves dataset transfer, a previously unsolved problem for continuous OT**: With only 10 labeled target samples per class, the method achieves 83.22% accuracy on FMNIST→MNIST (Table 1), far exceeding all baselines — including label-using ones like OTDD (10.28%) and SinkhornLpL1 (10.67%). This demonstrates a new capability for continuous OT to incorporate side information like class labels.

- **Error analysis that removes restrictive assumptions on the dual potential**: Unlike prior work \citep{fan2023neural, rout2022generative, makkuva2020optimal} that requires convexity of the dual potential $\hat{v}$, Theorem 3 provides a duality-gap bound requiring only strong convexity of the cost functional $\mathcal{F}$. This is a genuinely differentiability-free assumption on the dual side.

- **Convexity and lower semi-continuity of proposed functionals are established**: Theorem 4 proves that $\mathcal{F}_{\text{G}}$ is convex, lower semi-continuous, and $*$-separably increasing, ensuring the saddle-point approach is valid for the class-guided case.

- **Practical Monte Carlo estimator for the energy distance term**: Proposition 1 provides a concrete estimator $\widehat{\Delta\mathcal{E}^2}$ enabling stochastic optimization with labeled batches, detailed in Algorithm 2.

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice gap: strong convexity assumption in Theorem 3 is not satisfied by either example functional.** The error analysis (Theorem 3) requires $\mathcal{F}$ to be $\beta$-strongly convex in a metric $\rho$ on $\Pi(\mathbb{P})$. However, (a) the class-guided functional $\mathcal{F}_{\text{G}}$ (Eq. 6) is a sum of energy distances — convex but not established to be strongly convex in any standard metric on $\Pi(\mathbb{P})$; (b) the pair-guided functional $\mathcal{F}_{\text{S}}$ (Eq. 8) is linear in $\pi$, hence not strongly convex at all. The paper acknowledges on line 151 that "to apply our duality gap analysis, the strong convexity of $\mathcal{F}$ is required," but nowhere checks this condition for the examples. Consequently, the theoretical error bound is decoupled from the practical algorithms being validated. To repair this, the authors would need to either (i) prove strong convexity holds for $\mathcal{F}_{\text{G}}$ under appropriate conditions (e.g., with a regularizer), (ii) relax Theorem 3 to work under convexity alone, or (iii) clearly state the bound applies only to future functionals that satisfy the condition and not to the paper's own examples.

- **Insufficient quantitative evaluation for the paired image translation task.** For the pair-guided functional $\mathcal{F}_{\text{S}}$, the paper reports results on three datasets (Comic-Faces-V1, Edges-to-Shoes, CelebAMask-HQ) but provides only qualitative visual comparisons for the first two and a single FID of 21.1 for CelebAMask-HQ — without reporting FID (or any other metric) for the baselines (Pix2Pix, RMSE regression, NOT) on any of these datasets. The baselines section on line 292-293 lists Pix2Pix and RMSE regression, but their quantitative performance is never reported. The claim of "competitive quality" on line 297 is not verifiable without quantitative comparisons. For a well-established benchmark task with standard evaluation protocols, this omission significantly weakens the empirical contribution.

### Minor

- **Key condition "separably $*$-increasing" in Theorem 1 is undefined in the main text.** This term appears in the statement of the paper's central theorem (line 111) and is invoked again in Theorem 4 (line 197) to certify $\mathcal{F}_{\text{G}}$, but is never defined or explained in the main body. The remark that "one can eliminate this restriction by taking the advantage of the minimax theorems" (line 109) is too cryptic to serve as a substitute. A reader cannot assess whether the classic OT cost, weak OT costs, or the two proposed functionals satisfy the condition without consulting external references. While a definition may appear in the appendix (stripped by the parser), the main paper should at minimum state the definition and discuss whether the examples satisfy it, since this is the core theoretical claim.

- **Theorem 2's logical inference is slightly oversimplified.** Theorem 2 states: if $v^*$ is an optimal potential and $T^*$ is a stochastic OT map, then $T^* \in \arg\inf_T \mathcal{L}(v^*, T)$. The paper then claims "by solving (5) and obtaining an optimal saddle point $(v^*, T^*)$, one gets a stochastic OT map." This direction — that any $T$ minimizing $\mathcal{L}(v^*, \cdot)$ is an OT map — is the converse of what Theorem 2 proves and requires additional justification. The paper does hint at a resolution on line 129 ("To ensure that all the solutions are OT maps, one may consider adding strictly convex regularizers") but does not develop this point. Clarifying the logical structure would improve rigor.

- **Reproducibility details for class-guided experiments are sparse.** For the pair-guided experiments, the paper specifies architectures (U2Net, ResNet discriminator). For the class-guided experiments (the paper's primary empirical contribution), no architecture details, hyperparameters, or sensitivity analysis (e.g., how accuracy changes with the number of labeled samples) are provided. The code repository URL is mentioned (line 228) but the path is cut off in the extracted text. Adding standard experimental details would improve reproducibility.

### Trivial

- The logical flow of Theorem 2 to the claim about obtaining OT maps from saddle points could be more precise. The nuance about strictly convex regularizers on line 129 is mentioned parenthetically but deserves a clearer treatment.

## Nice-to-Haves

- For the paired translation task, it would be informative to report FID (and ideally LPIPS or similar perceptual metrics) for all baselines on all three datasets, so the "competitive quality" claim can be quantitatively verified.
- A sensitivity analysis of the class-guided method to the number of labeled target samples (e.g., varying from 1 to 50 per class) would strengthen the practical contribution.
- The paper could explicitly state whether $\mathcal{F}_{\text{G}}$ or $\mathcal{F}_{\text{S}}$ satisfies the strong convexity condition of Theorem 3, perhaps after adding a small strongly convex regularizer, and if not, acknowledge that the error bound applies only to future $\mathcal{F}$'s that do meet the condition.

## Removed Points

The following criticisms from the original reviews are removed with justification:

- **"Comparison against unsupervised baselines is methodologically improper"** — Removed. The paper is transparent about the label usage (line 281: "Other baselines lack the capability to use label information"), includes proper semi-supervised/label-using baselines (OTDD, SinkhornLpL1) in the same tables, and the comparison to unsupervised methods serves to demonstrate that the task is unsolvable without label information. The framing is appropriate, not misleading.

- **"Missing Algorithm \ref{algorithm-gnot}"** — Removed. The parser strips appendix content from all papers; this algorithm exists in the original submission.

- **"Notation issue with $\Pi(\mathbb{P})$ in Theorem 3"** — Removed. The reviewer claims the object of interest is $\Pi(\mathbb{P},\mathbb{Q})$ but $\Pi(\mathbb{P},\mathbb{Q}) \subset \Pi(\mathbb{P})$, so the metric on $\Pi(\mathbb{P})$ is well-defined for both $\pi_{\hat{T}}$ and $\pi^*$.

- **"Estimator derivation should be sketched"** — Removed. The estimator is explicitly given in Proposition 1 (Eq. \ref{estimator-energy}).

- **"Typos, formatting, style nitpicks"** — Removed per instructions (these are parser artifacts, not author errors).

- **"Missing related works"** — Removed per instructions (cannot verify existence of missing references without external sources).

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important tension: the paper aims to provide a *generic* theoretical framework for general OT (Theorem 1, Theorem 3), yet the two practical instantiations both fail to satisfy a key condition (strong convexity) required by the error analysis. This suggests that the real value of this work may lie not in the generic theory but in the specific class-guided functional and its empirical success on dataset transfer — a problem that prior continuous OT methods could not address. The mismatch between the generality the paper claims and the conditions its examples actually meet is the central unresolved issue.

## Suggestions

1. Define "separably $*$-increasing" in the main text, or at minimum explain why the condition is mild enough that it can be eliminated via minimax theorems, and verify it explicitly for $\mathcal{F}_{\text{G}}$ and $\mathcal{F}_{\text{S}}$.
2. Address the strong convexity gap: either prove that $\mathcal{F}_{\text{G}}$ (or a regularized version) is strongly convex, relax Theorem 3 to convexity-only (possibly with a weaker bound), or honestly state that the bound does not apply to the paper's examples.
3. Add a quantitative comparison table for the paired translation experiments reporting FID (and ideally LPIPS) for all baselines on all three datasets.
4. Include key experimental details for the class-guided experiments: architectures, hyperparameters, and a sensitivity analysis w.r.t. the number of labeled target samples.

## Score and Decision

The paper makes a genuine contribution — a unified neural framework for general OT cost functionals — and the dataset transfer results are compelling. However, the combination of (a) a major theory-practice gap where the central error bound is not verified for either example functional, and (b) substantially incomplete quantitative evaluation for the paired translation task, prevents the contribution from being fully convincing. These weaknesses are addressable but require non-trivial additional work.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>