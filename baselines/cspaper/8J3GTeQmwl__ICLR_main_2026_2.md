---
job_id: e981761b-d384-4fcd-aadd-fda45b0bf2f4
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 8J3GTeQmwl.pdf
paper: Graphon Cross-Validation: Assessing Models on Network Data
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies model selection and cross-validation for graph-based probabilistic models, with theoretical analysis and empirical evaluation on network learning tasks.

## Minimum Quality
Pass ✅. The submission includes the required scientific components, namely abstract, introduction with positioning to prior work, methodology, theoretical analysis, experiments, quantitative results, and conclusion. While there are notable clarity and rigor issues, I do not see a desk-reject-level fatal flaw such as obvious data leakage, non-English content, or entirely unsupported central claims.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes a graphon cross-validation procedure, called CV-imputation, for tuning hyperparameters and selecting among graphon estimation methods on network data. The key idea is to hold out edge pairs, replace them in the training graph with Bernoulli imputed values of mean $\theta$, and then affine-transform the resulting estimator back to a predictor of the original probability matrix. The paper provides an asymptotic result claiming that the proposed validation score is parallel to the true estimation loss, and presents simulation and real-network experiments comparing the method mainly against edge cross-validation (ECV).

## Strengths
1. The paper addresses a real and nontrivial problem. Hyperparameter tuning and model selection for graphon estimators are genuinely awkward because naive cross-validation assumptions do not fit network data, and the paper targets that issue directly.

2. The proposed procedure is simple to state and potentially useful in practice. The construction in **Equation (4)**, followed by the affine correction in **Equation (6)**, gives a concrete recipe that can be plugged into multiple estimators, and the empirical section indeed applies it across NS, USVT, SAS, and ICE rather than building a method specialized to one estimator.

3. The method is computationally appealing relative to matrix-completion-based ECV. The discussion in **Section 3** and the runtime comparisons in **Figure 3** support the claim that avoiding per-fold matrix completion can substantially reduce overhead. In **Figure 3**, the gap is especially visible for SAS and USVT as $n$ increases, and for the larger settings the ECV curves rise much more sharply than CV-imputation. Even though the asymptotic cost discussion is somewhat informal, the empirical trend is clear.

4. The simulations are reasonably broad in estimator coverage. **Table 1** compares four estimation families under four graphon designs, and this breadth is a plus. The table also shows that the proposed tuning often improves over default hyperparameter choices, which is an important practical message independent of the head-to-head comparison against ECV.

5. The paper includes an attempt at theoretical justification instead of relying purely on heuristics. Theorem 1 is not fully satisfying to me, but it at least tries to formalize what quantity the validation score is estimating and how the discrepancy scales with $n$ and $K$.

6. Some of the visual diagnostics are useful. **Figure 4** is particularly helpful because it directly plots standardized CV score against standardized MSE as a function of the tuning parameter for NS. This is much more informative than only reporting selected hyperparameters, because it lets the reader inspect whether the criterion is shape-aligned with the target loss.

## Weaknesses
1. The central theoretical assumption, **Condition 1** on Page 4, is doing almost all of the heavy lifting, but it is too abstract and insufficiently justified in the main paper. The condition requires
\[
P\!\left(\left|\frac{Q_K(M)}{K^{-\alpha}}\right|\ge \delta_0\right)\le \varepsilon,
\]
uniformly for large $K$, where
\[
Q_K(M)=\sup_{1\le k\le K}\frac{1}{n(n-1)}\|\hat{\mathbf P}(M|\mathbf A)-\hat{\mathbf P}_k(M)\|_F^2.
\]
This is essentially an assumption that the split-and-impute estimator remains close to the full-sample estimator at a polynomial rate. But for a model-selection paper, this is precisely the nontrivial part. The theorem then says the CV score tracks the true loss provided this optimism bias behaves well. That makes the result conditional on a property that is not established for the estimators used in the experiments, except for a brief Erdős-Rényi remark. So the theory is more of an abstract meta-theorem than a validation of the proposed procedure for graphon estimators of actual interest. This matters because the paper repeatedly presents the approach as “theoretically sound” and “model-agnostic”, while the main theorem only transfers the burden to an estimator-dependent assumption.

2. There is a notable mismatch between the claimed generality and the actual assumptions. Early in **Section 2**, the paper assumes independent Bernoulli edges with
\[
a_{ij}\stackrel{\mathrm{ind}}{\sim}\mathrm{Ber}(p_{ij}), \quad p_{ij}=f(\mu_i,\mu_j),
\]
and later the whole logic of Lemma 1 and the validation score relies on conditional edge independence. Yet in the conclusion on **Page 10**, the paper suggests extension to broader models such as latent-space networks and generalized sparse graphons. That may be plausible, but within the main paper there is no formal argument establishing when the affine correction in **Equation (6)** remains valid outside the exact setup of **Equations (1)-(2)**. This overreach matters because readers may interpret the method as more broadly justified than it currently is.

3. The exposition around the math has several imprecisions that make the core mechanism harder to trust than necessary. A few examples:
   - On **Page 4**, immediately after **Equation (5)**, the text says “where $\mathbf A^{[-k]}$ is the one’s vector”, which is clearly a notation error and presumably should refer to $\mathbf 1$. This is minor in isolation, but it appears in the middle of the key derivation.
   - In **Lemma 1** on **Page 3**, the phrasing “the value of any entry in $\mathbf A^{[-k]}$ is mutually independent of the node connectivity for node pairs in the validation set” is vague. The actual needed statement is conditional independence between training entries and validation entries given $\mathbf P$, not some generic independence from “node connectivity.”
   - **Equation (6)** rescales an estimated matrix by $(1-w_k)^{-1}$. For large $K$, $w_k\approx 1/K$ so this is benign, but the paper does not discuss how this correction affects finite-sample variance, nor how often truncation to $[0,1]$ is needed. Since the score in **Equation (7)** is computed after truncation, while the theorem seems to concern the untruncated affine transformation, that gap should be addressed explicitly.

4. The empirical claims are stronger than the evidence in some places. In **Table 1** on Page 6, the paper states that CV-imputation “consistently selects models with smaller MSE values compared to those chosen by ECV for all five methods and all synthetic datasets.” Even setting aside the “five methods” typo, the practical significance of some improvements is tiny. For example, NS on Graphon 4 is $1.05 \pm 0.06$ versus $1.06 \pm 0.10$, SAS differences are often very small, and ICE improvements are modest. There is no statistical significance analysis, no paired comparison, and no discussion of when differences are meaningful versus noise-level. The table supports “often better” much more comfortably than “consistently superior” in a substantive sense.

5. Some results in **Table 1** also raise questions about the paper’s narrative and deserve analysis that is missing. For Graphon 3, **Default NS** achieves $0.74 \pm 0.04$, which is actually slightly better than **CV-imputation (NS)** at $0.79 \pm 0.07$. That does not invalidate the method, but it directly contradicts the surrounding prose that tuning is uniformly helpful and should have been discussed. If the default hyperparameter is already near-optimal for certain sparse designs, that is interesting and relevant. Instead, the paper smooths over this inconsistency.

6. The comparison set is narrower than it should be for a paper centered on cross-validation for networks. The main baseline is ECV from Li et al. (2020a), which is relevant, but the broader literature on network cross-validation and tuning is not adequately reflected in either the positioning or the experiments. This makes it difficult to judge whether the contribution is a substantial advance in network model selection or mainly an efficient alternative to one specific baseline. Because the paper sells itself as a general graphon cross-validation framework, the empirical comparison would be stronger if it included additional network CV strategies or at least a more careful discussion of what alternatives are excluded and why.

7. The “rank consistency” claim based on **Figure 4** is overstated. **Figure 4** indeed shows that the red CV-imputation curve often resembles the black MSE curve more closely as $n$ grows, which is encouraging. But the figure is only for NS, only for a coarse grid of $M\in\{0.5,1,\dots,5\}$, and the curves sometimes look fairly step-like and flat near the optimum. A claim like “CV-imputation maintains rank consistency in model selection for any given estimation approach” goes beyond what this figure demonstrates. At most, the displayed evidence suggests improving agreement in these simulated settings.

8. The real-data evaluation has several methodological weaknesses.
   - In **Section 6.1** on Pages 8-9, the paper uses a future time window as testing data for the COVID co-occurrence graph and then interprets a high-scoring predicted drug link as medically suggestive. That is an interesting anecdote, but it is very far from validation of scientific usefulness. Co-occurrence is not causal interaction, and the discussion risks overstating what the model output means.
   - In **Section 6.2**, the paper samples $10\%$ of node pairs as testing data for large networks and reports AUC in **Table 2**. However, the exact protocol is underspecified. Are methods refit after removing those edges? How is this external test split kept separate from the internal CV used for tuning? Is the 10% sample balanced across positive and negative edges, or simply uniform over all pairs? For sparse networks, the latter yields a huge class imbalance, and AUC can hide that. These details matter for interpreting the reported gains.

9. The computational-efficiency discussion is directionally plausible but still somewhat hand-wavy. In **Section 3**, the paper gives complexity as
\[
O\big(|\mathcal M|\cdot (K C_{\text{estim}}(n)+n^2)\big),
\]
while ECV is
\[
O\big(|\mathcal M|\cdot (K C_{\text{estim}}(n)+K T_{\text{mc}}(n))\big).
\]
This is fine at a high level, but the argument “existing graphon estimation methods usually have $C_{\text{estim}} > n^2$” is too informal, and the comparison depends materially on the implementation of matrix completion and on the estimator. The empirical runtime plots in **Figure 3** are useful, but they are limited to relatively small synthetic graphs up to $n=200$, which is not exactly the regime where asymptotic runtime claims are most compelling. The larger real graphs in **Table 2** help, but there the candidate estimator set is reduced, which complicates apples-to-apples interpretation.

10. The presentation is uneven and occasionally careless in ways that reduce confidence. There are multiple writing issues and small inconsistencies, for example “implemtation issues” on **Page 5**, the duplicated Li et al. (2020a)/(2020b) reference entry on **Page 11**, and the statement on **Page 6** referring to “all five estimation methods” although only four are listed in the experimental setup. None of these is fatal, but together they give the paper a somewhat not-fully-polished feel, especially for a paper whose contribution is methodological subtlety rather than a large empirical benchmark.

## Questions
1. Theorem 1 depends crucially on **Condition 1**. Can the authors provide, in the main paper’s setting, at least one nontrivial rate derivation for an estimator actually used in the experiments, such as NS, SAS, USVT, or ICE? Even a proposition under simplified regularity assumptions would substantially increase my confidence that the theorem is more than an abstract wrapper.

2. In **Equation (6)**, the estimator is corrected by
\[
\hat{\mathbf P}_k(M)=\frac{\hat{\mathbf P}(M|\mathbf A^{[-k]})-w_k\theta \mathbf 1\mathbf 1^\top}{1-w_k}.
\]
How sensitive are the final selected models to the choice of $\theta$? The paper says this is discussed in the supplement, but a concise summary in the main text would help. In particular, is there any principled choice such as the observed edge density, and what happens when $\theta$ is badly misspecified?

3. How often does truncation of $\hat p_{ij}^{[k]}(M)$ to $[0,1]$ occur in practice for each estimator, and does Theorem 1 still apply after truncation? If not, can the authors explain why the discrepancy is negligible?

4. For the large-network experiments in **Section 6.2** and **Table 2**, please clarify the evaluation protocol in detail:
   - Is the external 10% test set sampled uniformly over all node pairs?
   - Are hyperparameters tuned only on the remaining 90% graph?
   - Are all reported AUCs computed on the same held-out pairs across methods within a replicate?
   - What is the positive-edge rate in the test pairs for each dataset?

5. The paper claims broad model-agnosticity. Could the authors clarify the precise boundary of applicability? For example, which parts of the procedure fail if edges are dependent conditional on latent variables, or if one moves to directed/weighted graphs?

6. In **Table 1**, some gains over ECV are very small, and in at least one case default NS appears better than tuned NS on Graphon 3. Can the authors provide paired statistical comparisons or a deeper analysis of when tuning helps most versus when it does not?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper does not raise major ethics issues requiring formal review. The COVID drug-repurposing case study on **Pages 8-9** should be interpreted cautiously, but this is better framed as a presentation issue than an ethics-review trigger based on the current manuscript.

## Soundness Rating
3: good. The method is plausible and supported by useful experiments, but the main theorem relies on a strong estimator-dependent assumption that is not instantiated for the principal methods studied, and some empirical protocols need clearer specification.

## Presentation Rating
2: fair. The paper is readable overall and the figures help, but the exposition has several imprecisions, a few notation/writing errors, and some claims are stated more strongly than the presented evidence supports.

## Contribution Rating
3: good. The paper addresses an important problem and proposes a practical, estimator-agnostic tuning mechanism with credible computational advantages, though the novelty and validation feel more incremental than fully definitive.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles an important problem and offers a practically useful idea with decent empirical support, especially on computational efficiency. I am positive overall, but only narrowly, because the theoretical guarantee is heavily assumption-driven, the positioning against broader related work is not fully convincing, and several claims in the empirical section are overstated relative to the evidence.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. The paper is close enough to the threshold that stronger clarification on Condition 1, the evaluation protocol, and the exact scope of applicability could materially strengthen the case.