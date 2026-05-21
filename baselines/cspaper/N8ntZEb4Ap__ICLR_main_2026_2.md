---
job_id: cd9ce716-b8df-4c1f-9a38-872298e1a572
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: N8ntZEb4Ap.pdf
paper: AutoNFS: Automatic Neural Feature Selection
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within general machine learning, specifically feature selection for tabular learning, differentiable optimization, and interpretability of learned representations.

## Minimum Quality
Pass ✅. The paper includes the expected core components, namely abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion, and it presents a complete empirical study. While I have substantial concerns about novelty, positioning, and some methodological claims, these are review-level issues rather than desk-reject defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes AutoNFS, a differentiable feature selection method for tabular data that combines a masking network based on Gumbel-Sigmoid sampling with a downstream task network trained end-to-end. The method uses a sparsity penalty to automatically determine a global feature subset, and is evaluated on OpenML-style benchmark datasets under three corruption scenarios as well as on metagenomic datasets.

## Strengths
The paper addresses a practically relevant problem. In many feature selection pipelines, the number of selected features is indeed treated as an external hyperparameter, and reducing this manual tuning burden is useful.

The method is simple and easy to understand at a high level. The core architecture in **Figure 1** communicates the intended data flow clearly: a masking network outputs feature-selection logits, these are sampled through a Gumbel-Sigmoid relaxation, and the resulting mask is applied before the task network. Even though the mathematical exposition has some issues that I discuss below, the conceptual idea of coupling a global mask learner with a predictor is straightforward and implementable.

The empirical study is reasonably broad in terms of tasks. The paper covers both classification and regression, synthetic corruption scenarios, and a real biological application. This breadth is a positive aspect, even if I have concerns about what exactly the experiments establish.

Some results are competitive. In the benchmark tables, AutoNFS does perform well on average. For example, in **Table 4** (corrupted features), AutoNFS has the best mean rank of 2.1, and in **Table 3** and **Table 5** it also attains the strongest average rank among the listed methods. This suggests the method is at least a viable practical baseline for this benchmark setup.

The feature-count reduction is substantial. The right half of **Table 1** shows that the method often selects far fewer features than the original dimensionality, sometimes dramatically so, and **Table 2** reports an average reduction from 535 to 41 features on the metagenomic datasets. This practical sparsification is meaningful if the predictive performance is preserved.

The computational-scaling experiment is a potentially useful addition. **Figure 4(a)** shows a flatter scaling curve for AutoNFS than for the compared selectors, and **Figure 4(b)** summarizes this with a fitted exponent near zero. Even though I think the claim of "nearly constant computational overhead regardless of input dimensionality" is overstated, the experiments do indicate favorable scaling relative to several classical baselines.

## Weaknesses
1. **The claimed methodological novelty is limited, and the paper does not sufficiently separate itself from prior differentiable gating-based feature selection methods.**  
   The core recipe, namely learning feature-wise stochastic gates with a sparsity-inducing regularizer and training jointly with a predictor, is already very close to prior differentiable feature selection approaches discussed by the paper itself, especially Hard-Concrete/$L_0$ regularization and stochastic gates in **Section 2** (**Pages 2-3**). What remains here is mainly the use of a global mask parameterized through a learnable embedding and a Gumbel-Sigmoid relaxation, plus a simple cardinality penalty. The paper repeatedly frames this as a major departure from prior work, for example in the abstract and **Section 1**, but the technical differences are not articulated sharply enough.  
   This matters because at ICLR the bar is not just "works reasonably well", but whether the paper advances the state of the art conceptually or empirically in a way that is well distinguished from existing approaches. Right now, the paper feels much closer to a repackaging or simplification of known relaxed-gate feature-selection ideas than to a clearly new method.

2. **The central claim that the method "automatically determines the minimal set of features essential to solve a given downstream task" is too strong for what is actually optimized.**  
   In **Page 4**, the objective is
   \[
   \mathcal{L}_{\text{total}}=\mathcal{L}_{\text{task}}+\lambda \mathcal{L}_{\text{select}}, \quad
   \mathcal{L}_{\text{select}}=\frac{1}{D}\sum_{j=1}^D m_j.
   \]
   This objective encourages sparsity, but it does not establish minimality in any formal sense. It is only a regularized trade-off objective, and its solution depends on \(\lambda\), optimization dynamics, annealing, initialization, model capacity, and feature redundancy. There is no theorem, no identifiability argument, and no empirical protocol showing that the returned subset is minimal rather than merely sparse enough under one chosen regularization weight.  
   This matters because "minimal sufficient subset" is one of the paper's central selling points, repeated in the abstract, **Page 2**, and **Section 5**. Without stronger support, the paper should tone this down to "learns a sparse subset" or "automatically balances accuracy and sparsity".

3. **The mathematical specification of the Gumbel-Sigmoid sampler is questionable or at least under-specified.**  
   In **Section 3.2** (**Page 3**), the paper defines
   \[
   \text{GS}(w_i;\tau)=\sigma\left(\frac{w_i+g_i}{\tau}\right), \quad g_i\sim -\log(-\log u), \, u\sim \mathrm{Uniform}(0,1).
   \]
   This uses a single standard Gumbel perturbation added to a logit and then passed through a sigmoid. For Bernoulli/relaxed-Bernoulli sampling, a standard formulation typically involves either logistic noise or the difference of two Gumbels. If the authors intentionally use a one-Gumbel variant, they need to justify that this induces the intended relaxed Bernoulli behavior and not merely an ad hoc noisy gate.  
   This is not a cosmetic issue. The entire method rests on the distributional semantics of the gate sampler. If the sampling relaxation is mis-specified, then the claimed connection to Gumbel-Sigmoid / Concrete-style feature selection becomes shaky, and the optimization behavior may not match the interpretation offered in the text.

4. **Several details of the optimization objective and training protocol are missing or inconsistent, which reduces reproducibility and makes some claims difficult to verify from the main paper alone.**  
   For instance, in **Algorithm 1** (**Page 5**), the classification loss is written explicitly as
   \[
   \mathcal{L}_{\mathrm{task}}=-\sum_{i=1}^B \sum_{c=1}^C y_{i,c}\log(\hat y_{i,c}),
   \]
   but the paper also claims to handle regression. There is no regression-specific pseudocode in the main paper, nor any complete training specification for that case. Also, the main paper says "we experimentally verified that using a constant value \(\lambda=1\) gives satisfactory results across datasets" (**Page 4**), whereas the appendix later discusses tuning behavior and shows a sensitivity plot in **Figure 6**. The interaction between this claimed universality of \(\lambda=1\) and the visible sensitivity to \(\lambda\) is not well reconciled.  
   Similarly, the exact discretization used at inference is a fixed threshold \(\sigma(w_i)>0.5\) in **Section 3.5** (**Page 5**), but training optimizes expected soft masks with noise. There is no discussion of train-test mismatch induced by replacing stochastic soft masks with deterministic thresholded masks.

5. **The complexity claim is overstated, and the evidence shown in the paper does not justify the broad wording.**  
   The paper claims "nearly constant computational overhead regardless of input dimensionality" in the abstract and repeatedly in **Sections 1 and 3**. However, the model still outputs a \(D\)-dimensional logit vector and multiplies a \(D\)-dimensional mask with each input. At minimum, there is an unavoidable \(O(D)\) dependence in producing and applying the mask, unless \(D\) is somehow bypassed, which it is not.  
   **Figure 4(a)** and **Figure 4(b)** only show an empirical fit over a finite range of dimensionalities against selected baselines. A fitted exponent of \(\alpha \approx 0.08\) is not the same as dimension-independent complexity. The paper should present this as favorable empirical scaling under the tested implementation and hardware setup, not as a nearly constant-overhead property of the algorithm itself. This distinction matters because the current wording reads like an algorithmic claim.

6. **The empirical comparisons are not fully convincing as evidence of superiority over modern neural feature-selection approaches.**  
   The compared methods in the main benchmark are mostly classical selectors or older neural sparsity baselines. The paper does mention some related neural approaches in **Section 2**, but the experimental section does not convincingly position AutoNFS against the strongest directly comparable differentiable gate-based selectors in the main paper. Since the method is essentially another member of that family, this omission weakens the empirical case for contribution.  
   This matters especially because the paper's main empirical message is "consistently outperforms both classical and neural FS methods" from the abstract. To justify that strong statement, the baseline set must be beyond dispute.

7. **The presentation of aggregate benchmark results hides effect sizes and variability.**  
   **Figure 2** only reports average ranks across the three corruption types. Average ranking is useful as a summary, but it can obscure the magnitude and consistency of gains. Looking into **Tables 3-5**, the story is more mixed than the figure suggests. For example, in **Table 3**, AutoNFS is indeed best on average rank, but on some datasets the gain over strong baselines is very small, and on some datasets it is not the best raw score. In **Table 5**, the mean-rank advantage is also present, but again several dataset-wise results are essentially tied.  
   This matters because the strong language in the main text, especially "consistently outperforms" on **Pages 1-2 and 7**, overstates what the tables actually show. The paper would be stronger if it reported mean and standard deviation across runs in the main tables, along with statistical testing or at least paired win/tie/loss counts.

8. **The metagenomic experiment is interesting, but the interpretation is too optimistic and the evidence is mixed.**  
   **Table 2** shows a positive average change, but several datasets deteriorate noticeably after selection. For MLP, examples include KeohaneDM_2020 (0.469 to 0.344), JieZ_2017 (0.693 to 0.612), ThomasAM_2018a (0.733 to 0.567), and YuJ_2015 (0.653 to 0.417). For RF, there are also substantial drops, such as NielsenHB_2014 (0.711 to 0.634), LiJ_2017 (0.561 to 0.432), and HanniganGD_2017 (0.817 to 0.533).  
   Yet the text on **Page 7** says AutoNFS "maintains predictive performance on downstream tasks while drastically reducing feature dimensionality" and that the representation usefulness is independent of downstream classifier. That conclusion is too broad relative to the table. The average improves slightly, but the per-dataset instability is real and should be discussed. This matters for biological applications, where robustness across studies is often more important than a small average uplift.

9. **The evidence for interpretability is fairly weak and somewhat circular.**  
   The MNIST visualizations in **Figures 7 and 8** are intuitive, but they do not establish much beyond the fact that the model tends to pick central image pixels and those pixels have higher class-conditional entropy. For a handwritten-digit dataset, that is not surprising. More importantly, these figures are in the appendix and disconnected from the core tabular feature-selection claims.  
   Even within the main paper, **Figure 3(b)** is used to argue that the selected set "cannot be further reduced without affecting predictive performance" (**Page 7**). But the plotted quantity is the average drop when removing one selected feature, not a proof of irreducibility of the whole subset. In redundant feature spaces, every selected feature could individually appear useful while the subset is still not minimal. So the interpretation is too strong.

10. **Some exposition is sloppy enough to hurt confidence.**  
   There are multiple small but telling issues: inconsistent naming between "target network" and "task network", several grammatical problems, a typo "Mutual Informatio" in **Page 9**, duplicate references in the bibliography, and occasional overclaims not matched by evidence. None of these individually is fatal, but together they make the paper read less carefully checked than one would hope for an ICLR submission.  
   More importantly, the main paper pushes key details into the appendix, while the main text itself leaves critical questions unresolved, especially around baseline fairness, exact hyperparameter selection, and the theoretical meaning of the learned mask.

## Questions
1. The core sampler in **Section 3.2** uses
   \[
   m_i=\sigma\left(\frac{w_i+g_i}{\tau}\right), \quad g_i\sim \mathrm{Gumbel}(0,1).
   \]
   Can the authors justify this formulation carefully? In particular, how does this correspond to a relaxed Bernoulli gate rather than simply injecting one-sided Gumbel noise into logits? A concise derivation or correction here would materially affect my confidence in the method.

2. The paper repeatedly claims that AutoNFS finds the "minimal" sufficient feature set. What precise notion of minimality is intended? If this is only an empirical shorthand for sparsity induced by \(\lambda \sum_j m_j\), please revise the claims. If the authors believe a stronger statement is justified, please provide either theory or much more targeted empirical evidence.

3. How exactly were hyperparameters chosen for AutoNFS and for all baselines on the main benchmark? In particular, was the same search budget used across methods, and was model selection performed on a validation split only? Clearer detail on this would improve trust in the reported advantages.

4. For the metagenomic study in **Table 2**, can the authors provide variability across runs and discuss the datasets where AutoNFS significantly hurts performance? The current average-only interpretation is too smooth relative to the per-dataset results.

5. The complexity discussion around **Figure 4** should distinguish empirical runtime scaling from algorithmic complexity. Can the authors clarify what exactly was measured, on what hardware, with what implementation details, and whether the observed near-flat exponent persists when the masking network output layer and mask application cost are isolated?

6. Why is the final hard-selection rule fixed at \(\sigma(w_i) > 0.5\) in **Section 3.5**? Was this threshold validated empirically, and how sensitive are the selected subsets and scores to this choice?

7. The benchmark figures focus on average rank. Could the authors provide statistical significance analysis, paired win/tie/loss counts, or confidence intervals in the main paper, especially for **Tables 3-5**? This would help determine whether the observed gains are meaningful or mostly marginal.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The metagenomic application is biomedical in flavor, but the paper does not describe deployment on human subjects, release of sensitive data, or a direct clinical use claim requiring ethics escalation based on the provided text.

## Soundness Rating
2: fair. The overall approach is plausible and empirically evaluated, but some core methodological claims are overstated, the sampling formulation needs clarification, and the evidence does not fully support the strongest conclusions.

## Presentation Rating
2: fair. The paper is readable at a high level and figures such as **Figure 1** and **Figure 4** help convey the method and experiments, but the exposition is uneven, several technical points are under-specified, and the claims are often stronger than what the figures and tables actually demonstrate.

## Contribution Rating
1: poor. The paper tackles an important practical problem, but the incremental nature relative to prior differentiable gating methods, together with incomplete positioning and overclaimed conclusions, makes the overall contribution below the bar I would expect for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is technically plausible and practically motivated, and the experiments suggest it may be a useful baseline. However, the contribution is too incremental, the novelty and complexity claims are overstated, and several central interpretations, especially around minimality and the gating formulation, are not supported strongly enough for acceptance in the current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main methodological claims, equations, figures, and results tables carefully.