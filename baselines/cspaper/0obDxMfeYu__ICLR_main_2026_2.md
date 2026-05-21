---
job_id: 0c040590-61f4-45e0-8165-bf4697553d92
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0obDxMfeYu.pdf
paper: A Median Perspective on Unlabeled Data for Out-of-Distribution Detection
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on out-of-distribution detection, robust learning with unlabeled data, and accompanying theoretical analysis.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, method, theory, experiments, results, and conclusion. While I have significant concerns about the rigor and support for several claims, these issues do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions to automated reviewers, or other suspicious content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies OOD detection in the setting where one has labeled in-distribution data and unlabeled “wild” data consisting of a mixture of InD and OOD samples. The proposed method, Medix, first computes gradients of a classifier trained on InD data, then greedily removes samples from the wild set based on how much their removal makes the element-wise median of wild gradients closer to the average InD gradient, and finally trains a binary OOD detector on labeled InD data plus the extracted candidate outliers. The paper also presents bounds on inlier and outlier misclassification rates for the filtering stage and reports experiments on CIFAR-10/100 with several standard OOD datasets.

## Strengths
1. The paper targets an important and practically relevant setting, namely OOD detection with mixed unlabeled wild data rather than a clean auxiliary OOD dataset. This is a meaningful problem formulation and is more realistic than the standard OE-style assumption of access to a purely OOD auxiliary pool.

2. The filtering idea is intuitive and reasonably well motivated. The discussion around **Equation (4)** makes the intended objective explicit, namely selecting a subset whose gradient median aligns with the InD reference gradient. Even though I have reservations about the exact formulation and the greedy solver, the core idea is easy to grasp.

3. The paper does make a genuine effort to provide a theoretical account of the filtering stage, which is better than many purely heuristic OOD papers. In particular, **Theorem 4.1** and **Theorem 4.2** try to separate concentration, contamination, and separation effects, and the high-level message is coherent: median-based filtering should be robust when contamination is not too large and gradients of InD points concentrate.

4. The empirical evaluation in the main paper is broad in terms of benchmark coverage. **Table 1** and **Table 2** include a large set of standard OOD baselines, both methods trained only on InD data and methods using auxiliary or wild data. This breadth is useful for understanding where the method sits in the current landscape.

5. The headline empirical performance is strong on the reported CIFAR benchmarks. In **Table 1**, Medix reports very low average FPR95 and high AUROC on CIFAR-10, outperforming WOODS and OE-style baselines. In **Table 2**, the gains on CIFAR-100 are smaller but still mostly favorable, especially on TEXTURES and LSUN-C. If these results are robust, they suggest the approach is competitive.

6. The toy visualization in **Figure 2** is helpful for communicating the intended behavior of the filtering stage. The panel showing selected black points mostly overlapping with the red OOD cluster does support the claim that the greedy median-based procedure can isolate obvious far-away outliers in a simple low-dimensional setting.

## Weaknesses
1. The paper’s main empirical claim, “outperforms existing methods across the board” from the abstract and introduction, is overstated relative to the evidence in the main paper. Looking at **Table 1**, Medix is indeed strong, but the row formatting is confusing and the “(Ours)” row reports tiny upward arrows that are not explained clearly, making it hard to tell what exactly is being compared. In **Table 2**, the average FPR95 gain over WOODS is only from 6.74 to 5.42, which is modest, and on SVHN the difference is 0.17 versus 0.16, essentially negligible. This matters because the paper repeatedly frames the empirical evidence as a decisive across-the-board win, while the main-table evidence supports a more measured conclusion: strong results, yes, but not a clean knockout everywhere.

2. The algorithmic formulation around **Equation (4)** and **Algorithm 1** is not sufficiently well specified, and some notation is inconsistent enough to affect reproducibility. In **Equation (4)**, the optimization defines $\mathcal{S}_{\text{in}}^{*}=\arg\min_{\mathcal{S}'\subseteq\mathcal{S}_{\text{wild}}}\|\bar{\nabla}_{\text{in}}-\mathrm{EWM}(G_{\mathcal{S}})\|$, but the subset variable switches between $\mathcal{S}'$, $\mathcal{S}$, and $\mathcal{S}_{*}$ inside the definition of $G_{\mathcal{S}}$. This is not just cosmetic, because the whole method depends on what subset is being optimized over. Similarly, **Algorithm 1** uses $\hat{\nabla}_{\mathrm{in}}$ while the text defines $\bar{\nabla}_{\mathrm{in}}$, line 2 uses “while $t \le T$ or $|\delta_{\max}|>\epsilon$” where one would expect an “and” or a more careful stopping condition, and line 3 adds previously selected $\mathcal{I}_k$ before recomputing all $\delta_i$, which makes the ordering harder to parse. For a method paper, this level of ambiguity in the core procedure is a real problem.

3. The computational story of the greedy filter is not convincing in the main paper. The procedure described on **Pages 4–5** appears to require, at each iteration, leave-one-out recomputation of the element-wise median after removing every candidate point. Naively, this is expensive, especially with high-dimensional gradients. Yet the main paper does not provide a complexity analysis, an approximation trick, or any serious accounting of how this scales beyond CIFAR-sized settings. This matters because the method’s practicality depends heavily on whether the filtering stage is tractable. The appendix profiling suggests nontrivial runtimes, but the main paper itself gives the reader little basis to judge whether this is a practical method or a costly proof-of-concept.

4. The method relies on pseudo-label gradients for unlabeled wild samples, but the treatment of pseudo-label quality is underdeveloped in the main paper. In **Section 3.1**, the gradient for a wild sample is $\nabla \ell(f_{\phi_{\mathcal{S}_{\text{in}}}}(\tilde{x}_i), \hat{y}_{\tilde{x}_i})$, where $\hat{y}_{\tilde{x}_i}$ is the model’s predicted label. This creates a circular dependence: the same InD classifier used to define the reference gradient also assigns labels to potentially OOD samples, which may be arbitrarily wrong. The paper claims robustness to noisy labels later, but that evidence is outside the main paper. In the main text, there is no clear analysis of how mistaken pseudo-labels alter the gradient distribution or whether the proposed filtering criterion remains stable under severe misclassification. Since OOD examples are precisely where one expects wrong labels and odd gradients, this omission weakens the scientific story.

5. The theory is presented as a major pillar, but in its current form it does not tightly support the actual algorithm used in experiments. **Theorem 4.1** and **Theorem 4.2** bound the performance of an “EWM filtering rule” or an optimal subset $\mathcal{S}_{\mathrm{in}}^*$ defined by **Equation (4)**. However, the experiments use the greedy leave-one-out approximation in **Algorithm 1**, and the paper provides no theorem connecting the greedy algorithm to the optimum of **Equation (4)**, no approximation guarantee, and no monotonicity proof for the chosen stopping criterion. This gap matters a lot: the theorems are about an idealized object, while the experiments are about a heuristic. Without a link between them, the theoretical guarantees do not really certify the implemented method.

6. There are mathematical inconsistencies and likely errors in the theoretical statements and derivations. The displayed formula for **Theorem 4.2** on **Page 6** appears malformed: the braces do not match, and the concentration and contamination terms are not properly closed. More importantly, the contamination term for outlier error, $\frac{1-\pi}{2\pi}$, is problematic as an upper-bound component on a quantity in $[0,1]$, since it exceeds 1 whenever $\pi<1/3$. An upper bound larger than 1 is not automatically false, but it becomes nearly vacuous in the low-contamination regime where OOD detection is often most relevant. The text still presents the theorem as providing “rigorous theoretical assurance,” which is much stronger than what such a loose bound justifies.

7. The proof details in Appendix C raise additional concerns about correctness and consistency. For example, in the proof of **Theorem C.1**, equation numbering and substitutions are muddled: after deriving a bound involving $2d\exp(-\epsilon^2/(2\sigma^2)) + \sqrt{\log(1/\delta)/(2m_{\mathrm{in}})}$, the manuscript jumps in **Eq. (22)** directly to an expression that already includes both $\frac{1}{m_{\mathrm{in}}}$ and the contamination term $\frac{\pi}{2(1-\pi)}$, even though the contamination term has not been derived in Step 1. Later, the swapping argument defines $\mathrm{ERR}_{\text{in}}$ in terms of $m_\varepsilon - m^*_{\text{in}}$, but $m_\varepsilon$ itself counts both OOD points and bad inliers, which makes the interpretation of the error variable murky. These are not minor typos, because they obscure where the final stated bound actually comes from.

8. The assumptions underlying the theorems are stronger than the paper acknowledges, and the empirical justification is too weak. **Remark 4.3** uses **Figure 4a** and **Figure 4b** to argue that gradient coordinates are sub-Gaussian because one histogram looks bell-shaped and one Q-Q plot approximately follows a diagonal. This is not a convincing validation of the assumption. First, the figure appears to visualize only a single coordinate or a small slice, while the theory needs coordinate-wise assumptions across high-dimensional gradients. Second, approximate Gaussianity in one empirical marginal on one dataset does not justify the i.i.d. gradient-coordinate assumptions used in the proofs. The paper leans quite heavily on “mild assumptions,” but they are not mild for deep-network gradients.

9. The motivating evidence in **Figure 1** is weaker than the surrounding text suggests. The text claims a “clear and monotonic increase” in the $L_2$ deviation as more OOD samples are added, and that the stopping criterion is inspired by this. Visually, the curve is increasing overall, but it is not cleanly monotone, and the link from this synthetic addition experiment to the stopping rule in **Algorithm 1** is not theoretically justified. This matters because the stopping rule is central to preventing over-pruning of InD samples, yet it is supported mainly by heuristic intuition.

10. The qualitative evidence in **Figure 2** is too easy to be persuasive. The OOD cluster is far from the three InD Gaussian blobs, centered around approximately $(20, 2\sqrt{3})$, which makes the filtering problem almost trivial in 2D. The reported 12.5% extraction error sounds decent, but in a setting with such large geometric separation, I would expect many standard heuristics to succeed. As a result, **Figure 2** is good for intuition but does not really provide meaningful evidence for the hard regime the method is supposed to address.

11. The experimental protocol raises comparability issues. On **Page 7**, the paper states that CIFAR is split in half, with 25,000 images used to train $\phi_{\mathcal{S}_{\text{in}}}$ and the remaining images used to construct the wild mixture. But several InD-only baselines in **Table 1** and **Table 2** appear to use the standard full training set or a different training setup, and the paper itself later attributes some InD accuracy differences to this mismatch. This makes direct performance comparisons less clean than presented, because some methods are not operating under identical data budgets or supervision configurations.

12. Hyperparameter selection is potentially problematic as described in the main paper. **Section 5.2** says that $\epsilon$ and $k$ are selected from candidate sets “with the objective of maximizing OOD performance,” but it does not specify what validation data is used for this tuning. In an OOD paper, this detail is crucial. If OOD test datasets or statistics from them informed selection, that would be leakage; if a separate validation split was used, that needs to be stated clearly. The current description is vague enough to undermine confidence in the reported numbers.

13. The detector-training objective in **Equation (5)** is underspecified and somewhat confusing. The paper first writes the loss using indicator functions, then says a differentiable sigmoid-based surrogate is used, and finally says the InD risk from **Equation (2)** is incorporated into a unified optimization. However, the exact surrogate loss, the weighting, and the optimization objective are not all defined in one place in mathematically precise form. For example, is the binary detector trained with logistic loss on top of frozen features, jointly fine-tuned end-to-end, or with some multi-task objective mixing the multiclass and binary terms? **Section 5.2** gives some implementation hints, but the objective itself should be explicitly stated in the method section.

14. The related-work positioning is thinner than it should be for this particular problem setting. The paper does cite WOODS and Du et al. (2024a), which are indeed central, but the broader literature on leveraging mixed unlabeled data for open-set or OOD detection is discussed somewhat selectively. Given that the claimed contribution is a new filtering mechanism for mixed unlabeled data, the paper should do a sharper job explaining exactly what prior filtering-based or unlabeled-mixture approaches cannot do, and where the median statistic changes the picture in a substantive rather than incremental way.

15. The paper repeatedly suggests that the main contribution is the filtering stage, but the empirical section does not isolate that claim well enough in the main paper. Since stage 2 follows Du et al. (2024a), the key scientific question is whether median-based filtering materially improves the quality of extracted candidate outliers compared with other plausible gradient-based or threshold-based filters. The main paper lacks a direct apples-to-apples ablation replacing the median criterion with simpler alternatives while holding stage 2 fixed. Without that, it is difficult to attribute the gains specifically to the advocated median perspective.

## Questions
1. Please clarify the exact optimization objective actually used to train the final detector. In **Equation (5)** the objective is written in terms of indicator losses, while **Section 5.2** mentions a sigmoid surrogate and a weighted combination with the InD classification loss. It would increase my confidence substantially if the rebuttal provided the explicit final loss in mathematical form, including whether $f_\phi$ and $g_\theta$ are jointly updated or whether only the added binary head is trained.

2. What validation protocol was used to choose $\epsilon$ and $k$ in **Section 5.2**? The paper currently says these are selected to maximize OOD performance, but it does not identify the validation set or explain whether that tuning is done separately for each InD-OOD pair. A precise answer here is important, because any use of the test OOD sets for tuning would materially weaken the empirical claims.

3. Can the authors provide a clean connection between the guarantees in **Theorem 4.1 / 4.2** and the greedy procedure in **Algorithm 1**? Even a weaker proposition, such as monotonic improvement of the objective under some condition, or an approximation guarantee relative to **Equation (4)**, would help. Right now the theory seems to apply to an ideal subset selector rather than the implemented algorithm.

4. In **Equation (4)** and **Algorithm 1**, please cleanly define the subset variables and stopping rule. In particular, should the while-loop use “and” rather than “or”? Also, what happens when all $\delta_i$ are negative, or when the top-$k$ removal increases the objective? Clarifying these edge cases would help reproducibility.

5. The contamination term in **Theorem 4.2**, $\frac{1-\pi}{2\pi}$, becomes large when $\pi$ is small. Is this the intended bound, and if so, how should readers interpret it in the low-contamination regime? If there is a typo or a looser-than-necessary derivation, correcting that would increase my trust in the theory.

6. The paper uses the penultimate-layer weights for gradient computation on **Page 7**. Did the authors test whether the method is sensitive to the choice of layer? Since the method depends crucially on gradient geometry, a brief main-paper ablation on layer choice would be quite informative.

7. Since the main claim is about the filtering stage, can the authors report, in the main paper, a direct comparison of extracted-outlier purity/recall against one or two alternative filters under the same detector-training stage? For example, compare Medix filtering against a simpler gradient-distance threshold or an entropy-based pseudo-label filter. This would better isolate where the gains come from.

8. In **Figure 1**, the text claims monotonic behavior that motivates the stopping criterion. Could the authors quantify this more systematically across datasets rather than presenting a single motivating example? If the stopping rule is robust across settings, a concise table or plot in the main paper would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are apparent from the submission. The work focuses on methodological improvements for OOD detection on standard vision benchmarks, and the paper does not involve sensitive human-subject experimentation or obviously harmful deployment claims beyond the usual concerns associated with reliability methods.

## Soundness Rating
2: fair. The paper has a plausible core idea and nontrivial experimentation, but the technical claims are not supported as cleanly as presented. In particular, the mismatch between theorems and the implemented greedy algorithm, ambiguity in the optimization details, and several proof-level issues reduce confidence in the soundness of the central claims.

## Presentation Rating
2: fair. The paper is readable at a high level, but the presentation is not careful enough for a method whose contribution depends on precise algorithmic and theoretical details. Notation inconsistencies, under-specified objectives, unclear table formatting, and several mathematical slips make the presentation weaker than it should be.

## Contribution Rating
2: fair. The problem setting is important and the method is interesting, but the actual incremental contribution beyond prior wild-data OOD pipelines is not yet convincingly established, and the main-paper evidence does not isolate the median-based filtering contribution strongly enough.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and addresses an important setting, and the reported benchmark numbers are strong enough that I would not be shocked to see it make it through. However, in its current form, the gap between theory and algorithm, the ambiguities in the method description, the under-specified hyperparameter selection protocol, and the proof-level issues make me lean negative for ICLR main track.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main technical concerns, although I have not fully re-derived every proof detail end-to-end.