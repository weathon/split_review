---
job_id: 47256af1-30b7-47cb-bc3c-5bd5f81ec788
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: H1s6SBhzlg.pdf
paper: Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within general machine learning, probabilistic aggregation, learning theory, and LLM-based decision making, with applications to language and healthcare.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion; while I have substantial concerns about assumptions, empirical support, and some mathematical/expository details, these are review-level issues rather than clear desk-reject defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies answer aggregation for multiple LLM agents and argues that majority voting is suboptimal because it ignores agent heterogeneity and cross-agent information. The authors propose two aggregation rules, Optimal Weight (OW), which uses agents’ accuracies as first-order information, and Inverse Surprising Popularity (ISP), which uses conditional answer correlations as second-order information; they provide theoretical claims under a symmetrized generative model and evaluate the methods on simulated data, UltraFeedback, MMLU, and ARMMAN.

## Strengths
The paper tackles a relevant problem. Aggregating multiple LLM outputs is common in practice, and a principled treatment of when and how one can beat majority voting is useful for the ICLR community.

The first-order result is clean in the paper’s stylized model. Under the assumptions stated in Section 3 and Assumption 1, the derivation behind **Theorem 1** is intuitive: after random label shuffling and conditional independence, the posterior reduces to a weighted vote with weights proportional to $\sigma_K^{-1}(x_i)$. Even though the setup is restrictive, the resulting rule is simple and interpretable.

I also appreciate that the paper does not stop at a purely supervised-oracle result. The move from OW to second-order aggregation and then to unsupervised estimation procedures OW-L / OW-I in **Section 5.2** is a sensible attempt to bridge theory and practice.

The synthetic experiments are directionally aligned with the theory. In **Table 2** on Page 8, ISP consistently beats MV and SP across $K\in\{2,4,6,8,10\}$, and the OW oracle is best overall, matching the theoretical narrative. The fact that ISP is very close to OPT for larger $K$ in that table is an interesting sanity check of the proposed formulation, at least under the simulated assumptions.

The appendix figure **Figure 1** on Page 24 is helpful. It visualizes the shrinking ISP-MV gap as $K$ increases, which directly corresponds to the scaling discussion after **Theorem 2**. This is one of the clearer places where the paper’s theorem and empirical evidence line up.

The per-model-family performance plot in **Figure 2** on Page 26 is also useful as contextual evidence that the chosen LLM pools are genuinely heterogeneous across datasets. That figure supports the basic premise that equal-weight majority voting may be leaving performance on the table when model quality differs substantially.

The real-data results are not huge, but they are at least consistently reported and sometimes nontrivial. In **Table 3** on Page 10, the proposed methods beat MV on all three reported datasets for the selected strong-model ensemble. The wider ensemble sweep in **Tables 5–7** also provides more breadth than a single cherry-picked setting.

## Weaknesses
1. **The main theoretical setup is much narrower than the paper’s practical claims, and the gap is not just cosmetic.**  
   The whole analysis rests on a very specific symmetrized noise model after random label shuffling, namely **Proposition 1** on Page 3 plus **Assumption 1** on Page 4. In particular, for each agent $i$, conditional on the true label, all incorrect options are equiprobable:
   \[
   \mathbb{P}(A_i=s_k\mid S^*=s_j)=\frac{1-x_i}{K-1}, \quad k\neq j.
   \]
   This is a strong structural assumption, not merely a harmless normalization. It excludes systematic distractor preferences, semantic confusions, and option-dependent biases, all of which are common in multiple-choice QA and especially in preference tasks where the two options are not exchangeable in any semantic sense. The paper acknowledges random shuffling, but shuffling labels does not make all wrong answers equally likely in the underlying decision process. It only removes positional asymmetry, not semantic asymmetry. Because **Theorem 1** and **Theorem 2** depend critically on this structure, the claimed “Bayesian optimality” and “provable improvement over MV” are much less general than the framing suggests.

2. **The random-shuffling reduction is overused as if it were innocuous, but the paper does not establish that it preserves the practically relevant information structure in the settings tested.**  
   Section 2 argues that random label shuffling is “standard practice” and, under certain circumstances, can be without information loss. But in the main text, the practical justification is much weaker than needed. The key assumption is that model outputs are unaffected by option order, stated on Page 3. For real LLMs this is at best approximate. The appendix remark that answer frequencies are near-uniform after shuffling is not enough, because equal marginal frequencies do not imply invariance of the full conditional response behavior under permutation. This matters because the entire derivation of **Proposition 1**, then **Theorem 1**, then the second-order calculations, all rely on the post-shuffle model being the right object. In short, the paper treats a mathematically convenient symmetrization as a faithful model of LLM behavior, but gives little convincing evidence in the main paper that this is justified.

3. **The empirical story for OW is substantially weaker than the framing implies, because OW itself is never actually evaluated on real data in the regime the paper claims to care about.**  
   The abstract and introduction heavily emphasize OW as a Bayesian-optimal first-order aggregator, but on real datasets the paper cannot use true accuracies and instead evaluates only heuristics, OW-L and OW-I. This is admitted on Page 2 and again in Section 5.2. That would be fine if the estimation methods were themselves well-founded, but they are presented as heuristics with limited analysis. So the paper’s strongest theorem supports a method that is not directly applicable in the main empirical setting, while the empirically used variants do not inherit the same guarantees. This weakens the scientific payoff of the first-order theory.

4. **Equation (7) and the OW-L estimation procedure are under-specified and appear statistically ill-posed or at least non-identifiable up to important ambiguities.**  
   In **Equation (7)** on Page 9, the authors propose
   \[
   \widehat{x}_{1},...,\widehat{x}_{N}=\arg\min_{x_1,\ldots,x_N}\sum_{i,j,k,l}\Big(\mathbb{P}(A_i=s_k\mid A_j=s_l)[x_1,\ldots,x_N]-\widehat{\mathbb{P}}(A_i=s_k\mid A_j=s_l)\Big)^2.
   \]
   Several issues matter here. First, this optimization is nonconvex in the $x_i$ and no algorithmic details are given in the main paper, even though the procedure is central to the best-performing practical method. Second, the paper does not discuss identifiability or local minima, despite fitting latent accuracies solely from pairwise conditional frequencies. Third, the expanded formula in Appendix F.2 appears to contain a typo in the same-label case, using $(1-x_j)(1-x_j)$ where symmetry strongly suggests $(1-x_i)(1-x_j)$. If that typo reflects the implemented objective, the estimator is simply wrong; if it is only a writing error, the presentation is still too sloppy for a core component. Either way, the lack of a careful treatment of Equation (7) is a serious weakness.

5. **The mathematical exposition has several correctness/clarity issues that make it harder to trust the proofs at face value.**  
   A few examples:
   - In **Equation (1)** on Page 4, MV is written as a weighted rule with $w_i=1/N$, which is harmless, but the introduction of weights there muddies the distinction from OW rather than clarifying it.
   - In Section 4.2, just before **Equation (4)** on Page 6, the line
     \[
     \mathbb{P}(A_i=s_2\mid A_j=s_1)=\mathbb{P}(A_i=s_2\mid A_j=s_1)\le \mathbb{P}(A_i=s_2\mid A_j=s_2)=\mathbb{P}(A_i=s_1\mid A_j=s_1)
     \]
     is oddly written and partly tautological, and the reference to “humans” in the surrounding explanation is out of place in a paper about LLM agents.
   - In **Proposition 2** / Appendix D.4, the indexing is sloppy. For example, “for all $i\in[K]$” should be over agents, not labels. There is also a displayed inequality ending up as $\beta_i \ge \sum_{j\neq i}\beta_i$, which should presumably be $\beta_i \ge \sum_{j\neq i}\beta_j$. This is not a tiny typo because it occurs in the central argument comparing OW to the best single agent.
   - In **Algorithm 3** on Page 18, line 4 says $\arg\max_{eS}$, clearly a notation error.

   None of these alone kills the paper, but together they create an unfortunate pattern: the proofs may be basically salvageable, yet the manuscript does not read like the mathematics has been fully stress-tested.

6. **Theorem 2 proves a statement about expected advantage, not accuracy, but the paper often slides rhetorically from one to the other.**  
   On Page 7, **Theorem 2** establishes
   \[
   \mathbb{E}[Adv_{ISP}(s^*)]\ge \mathbb{E}[Adv_{MV}(s^*)]\ge \mathbb{E}[Adv_{SP}(s^*)].
   \]
   This is not the same as proving that ISP has higher accuracy than MV for finite $N$. The text says ISP “outperforms” MV “in expectation”, but later discussion often reads much stronger, as if this settled practical superiority of the decision rule itself. Since the prediction is $\arg\max_s Adv(s)$, the link between larger expected advantage of the true label and higher classification accuracy is not straightforward without additional arguments on concentration or ordering probabilities. The paper gestures at this informally, but that is weaker than the headline claim suggests.

7. **The finite-sample analysis in Theorem 3 is not fully convincing as written.**  
   The theorem on Page 8 states that for every question, with probability at least $1-\delta$,
   \[
   \mathbb{E}[\widehat{Adv}_{ISP}(s^*)-Adv_{MV}(s^*)] \gtrsim \text{population gap} - \widetilde{\mathcal O}\!\left(\sqrt{\frac{1}{M}\log\frac{1}{\delta}}\right).
   \]
   But the proof sketch in Appendix E.4 mixes expectations over the target question with concentration over the dataset used to estimate $\widehat{\mathbb P}$, while also using leave-one-out arguments somewhat informally. The theorem statement itself is hard to parse because it is a high-probability statement about an expectation conditioned on estimated quantities from the same sample. I am not claiming the result is false, but the current presentation is too loose for a technical theorem meant to support the practical method.

8. **The experimental comparison is too narrow relative to current multi-LLM aggregation practice.**  
   The paper mainly compares against MV, SP, and the single best model. That is not enough. There are many natural baselines that sit between plain majority voting and the proposed method, even within the paper’s own assumptions: weighted voting using proxy confidences, self-consistency-style ranking, Dawid-Skene style annotator aggregation, EM-style worker-ability estimation, and modern multi-LLM answer-selection methods based on confidence or judging. Since the paper’s real contribution is practical aggregation without labels, the lack of stronger unsupervised or weakly supervised baselines is a major omission. As written, outperforming MV is useful but not sufficient to establish that ISP/OW-L are the right tools for practitioners.

9. **The results tables are encouraging but not strong enough to support some of the bolder claims.**  
   Consider **Table 3** on Page 10. The gains over MV are modest: +1.45 points on UltraFeedback, +1.05 on MMLU, and +0.54 on ARMMAN for OW-L/OW-I. On MMLU, the proposed methods are still below the “Single Best” oracle baseline, 90.37% vs 91.02%, so the text about extending model capability boundaries should be toned down. The paper does acknowledge that Single Best is an oracle, which is fair, but some of the prose in Section 5.4 overstates what the table actually demonstrates. Similarly, **Table 4** reports discrepancy counts and then uses t-statistics, but the appropriateness of a t-test for paired binary correctness outcomes is questionable; a McNemar test would be much more natural here.

10. **The presentation of real-data experiments leaves open important questions about evaluation protocol and possible leakage-like effects.**  
    OW-L estimates accuracies from the same unlabeled dataset on which final aggregation is reported. ISP also estimates conditional probabilities from the same dataset and applies them back to those same examples. In an unsupervised setting this is not “label leakage” in the usual sense, but it can still inflate apparent gains because the estimated correlation structure is evaluated in-sample rather than on a separate held-out set of questions. This is especially relevant when the method exploits stable dataset-level agreement patterns. The paper should report a train/test split over questions for estimating second-order statistics versus evaluating final aggregation accuracy. Without that, the reported real-world gains are harder to interpret as out-of-sample improvements.

11. **The paper does not sufficiently analyze why OW-L and OW-I are often numerically identical in the headline results.**  
    In **Table 3**, OW-L and OW-I are exactly the same on all three datasets. In many rows of **Tables 5–7**, they are also identical or nearly identical. That is surprising because the two procedures are conceptually different: one fits latent accuracies from conditional probabilities via Equation (7), the other bootstraps from ISP pseudo-labels. If they always collapse to the same ranking, that suggests either the problem is effectively one-dimensional in these experiments, or one of the implementations may be reducing to the other. The paper does not investigate this, and it should.

12. **The figure-based evidence is somewhat mixed and, in one case, undermines parts of the framing.**  
    As noted above, **Figure 1** is a good sanity check for the synthetic theorem. But **Figure 2** on Page 26 also reveals something important that the paper does not fully grapple with: model rankings vary a lot across datasets, and the spread within a family can be very large. This supports the heterogeneity premise, yes, but it also suggests that any global per-model weight may be too crude. If GPT-4o is much stronger on MMLU while gaps compress on ARMMAN, then prompt- or domain-specific weighting may matter more than the paper’s static aggregation framework. The figure therefore partly supports a limitation of the proposed approach, not just its motivation.

13. **The relation to prior literature is incomplete in the practical aggregation space.**  
    The related work on human information aggregation is fairly broad, but the LLM-aggregation comparison is thinner than it should be. The paper discusses majority voting, debate, confidence-based aggregation, and diversity-oriented ensembles, but omits several highly relevant recent methods for multi-LLM answer selection and compound inference that would provide stronger empirical context. This matters because the practical novelty claim hinges on whether higher-order aggregation adds something beyond already explored confidence- or judge-based ensemble methods.

14. **The healthcare application raises responsible-use questions that are not discussed enough in the main paper.**  
    The ARMMAN task concerns predicting dropout risk for pregnant and postpartum women. Even though the paper presents it as a benchmark-style evaluation, any framing around “predicting human behavior” in maternal health deserves a clearer discussion of potential bias, deployment safeguards, and the consequences of false positives/false negatives. The current main text mostly treats it as another dataset, which is too light for such a sensitive domain.

## Questions
1. For **Theorem 1**, can the authors clearly state which parts rely only on uniform prior over labels after shuffling, and which parts rely on the stronger assumption that all wrong labels are equiprobable? A concise derivation showing where this symmetry enters the posterior would help assess how far the result generalizes.

2. For **Equation (7)**, please clarify the optimization problem in full detail:
   - what is the feasible set for each $x_i$, presumably $x_i\in[1/K,1]$,
   - what optimizer is used,
   - whether the objective is identifiable up to multiple optima,
   - and whether the expanded expression in Appendix F.2 contains a typo in the same-label term.  
   This point materially affects my confidence because OW-L is one of the strongest empirical methods.

3. Can the authors provide an out-of-sample evaluation where second-order statistics or fitted accuracies are estimated on one subset of questions and aggregation is evaluated on a disjoint held-out subset? This would substantially increase confidence that the reported gains over MV are not partly in-sample fitting artifacts.

4. Please justify more carefully the use of expected advantage in **Theorem 2** as evidence of better aggregation accuracy. Is there a formal result connecting larger $\mathbb{E}[Adv(s^*)]$ to a higher probability that $s^*$ attains the maximal advantage? If not, the wording in the main text should be narrowed.

5. Why are OW-L and OW-I exactly equal in **Table 3**, and so often equal in **Tables 5–7**? Is this expected theoretically, or is it a consequence of the specific datasets/ensembles? A short diagnostic analysis would be helpful.

6. Could the authors compare against stronger unsupervised aggregation baselines, not just MV and SP? Even simple annotator-model baselines such as Dawid-Skene or EM-based worker aggregation, or confidence/judge-based multi-LLM selectors, would make the empirical case much more convincing.

7. On the real datasets, especially ARMMAN, did the authors consider calibration across subgroups or any fairness-sensitive error analysis? For a healthcare application, even a brief discussion of harms and deployment limitations would improve the paper.

## Flag For Ethics Review
- Yes, Discrimination / bias / fairness concerns  
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)  

## Details Of Ethics Concerns
The main concern is the ARMMAN application in **Sections 5.3 and 5.4**. The task predicts disengagement risk for pregnant and postpartum women in a maternal health program, which is a high-stakes setting. Even if the paper only evaluates offline prediction, deployment of such a system could affect who receives outreach, support, or intervention. The main paper does not discuss subgroup bias, calibration, differential error rates, or the consequences of misclassification. It would also be useful to clarify whether the underlying data usage and prompting setup are consistent with the dataset’s governance constraints and intended use.

## Soundness Rating
2: fair. The core ideas are plausible and some theoretical derivations are interesting, but the main guarantees rely on restrictive assumptions, the practical estimator behind OW-L is under-specified, and several mathematical/expository issues reduce confidence.

## Presentation Rating
2: fair. The paper is readable overall, but the notation and proof exposition contain enough ambiguities and apparent typos that they materially affect trust and clarity.

## Contribution Rating
2: fair. The problem is important and the information-aggregation framing is interesting, but the practical novelty is not fully established against stronger baselines, and the empirical/theoretical bridge is weaker than the paper suggests.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
This is a thoughtful paper with a real problem and some appealing ideas, but I do not think the current version clears the bar yet. The theory is built on a stylized symmetric model that is much narrower than the practical framing, the strongest practical method is insufficiently specified, the empirical comparison is too limited, and several technical presentation issues need cleanup. With a stronger out-of-sample protocol, more serious baselines, and tighter treatment of Equation (7) and the theorem claims, I could imagine this moving up.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the technical and empirical narrative with care, though some proof details would benefit from author clarification.