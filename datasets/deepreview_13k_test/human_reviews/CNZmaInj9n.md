# Exploring Unified Perspective For Fast Shapley Value Estimation

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Shapley values have emerged as a widely accepted and trustworthy tool, grounded in theoretical axioms, for addressing challenges posed by black-box models like deep neural networks. However, computing Shapley values encounters exponential complexity in the number of features. Various approaches, including ApproSemivalue, KernelSHAP, and FastSHAP, have been explored to expedite the computation. We analyze the consistency of existing works and conclude that stochastic estimators can be unified as the linear transformation of importance sampling of feature subsets. Based on this, we investigate the possibility of designing simple amortized estimators and propose a straightforward and efficient one, SimSHAP, by eliminating redundant techniques. Extensive experiments conducted on tabular and image datasets validate the effectiveness of our SimSHAP, which significantly accelerates the computation of accurate Shapley values.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents three main contributions. First, the paper shows that existing stochastic estimators for Shapley values (semivalue, random order value, least squares value) can all be written in the form of an affine transformation of a weighted average of the values of sampled subsets. In this unified formulation, each estimator is uniquely defined by the sampling distribution for subsets, the weights in the average, and the parameters of the affine transformation. Second, the authors show that the FastSHAP objective can be viewed as minimizing the distance to estimated Shapley values under a specific metric space, noting that one can generalize this idea to define other amortized estimators by choosing other metric spaces. Then, the authors choose a particular choice of stochastic estimator (which they call Sim-Semivalue) and metric space (Euclidean) to propose SimSHAP, a new amortized Shapley estimator.

### Strengths
1. The unified perspectives on stochastic Shapley estimators and objectives for amortized Shapley estimators is clarifying, to my knowledge novel, and potentially quite impactful (e.g. by stimulating further progress on proposing better estimators).
2. SimSHAP seems to reach comparable performance to FastSHAP with slightly faster inference time, given FastSHAP computes an additional normalization step that SimSHAP does not.

### Weaknesses
1. The proposed SimSHAP seems insufficiently motivated. Why did the authors make the specific choices for the stochastic estimator and metric space that they did? 
2. It is not clear from the experiments if there are any performance benefits from SimSHAP beyond faster inference.

Other notes:
1. It would be helpful if the authors were a bit more explicit about notation, e.g. explicitly defining $\mathbf{J}$ in the definition of the least squares value transformation $\mathbf{T}$ and $\mathbf{1}^{\mathbf{S}}$ in the definition of the least squares value.
2. The insertion curve seems to have two green curves but no blue curve. There might be a plotting bug somewhere?

### Questions
1. Why did the authors design SimSHAP the way they did? 
2. What are the reasons for using SimSHAP over FastSHAP? Is the primary benefit of SimSHAP faster inference time, or are there other benefits? Also, can the authors explain why SimSHAP outperforms FastSHAP specifically in the deletion AUC for CIFAR-10 and if there is a generalizable takeaway there? 
3. What do the authors mean by "That’s mostly because of the requirement of number of mask is larger for SimSHAP" when explaining why SimSHAP training is slower than FastSHAP training in Section 4.2.4 (speed evaluation)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the efficient approximation of Shapley coefficients in the context of local feature importance for machine learning predictors. After reviewing the different approaches that approximate these intractable coefficients (exponential in dimension), the authors propose a generalization of previous approaches and a different way of computing them (employing the "LS value" distribution in the context of what they define as unified amortized estimators. They compare their results in approximation quality for tabular data, and for deletion and insertion analysis for image data, showing reasonable results, whereas the running time at inference is order of magnitude faster.

### Strengths
* This paper studies an important problem, with the increasing popularity of Shapley values to explain machine learning predictors (with high dimensional features).

* The paper provides a nice introduction of current approximation techniques, and their proposed variations (while not radically innovative) are simple and intuitive.

* The numerical results support their method, and seems adequate.

### Weaknesses
* Some typos and unclear passages makes the paper harder to read at times (see below).

* The demonstrations of benefits are all empirical, and there is no guarantee that their proposed SimSHAP provides faster approximations than other alternatives.

### Questions
* Why did the authors define $f:\mathcal X \to \mathcal Y$ in Sect 2.1 if this is not used in the rest of the paper? Note that the fact that $f(x_S) = v(S)$ was never made.

* The authors do a good job at commenting on related works for approximation of Shapley values, due to their complexity. However, there is no mentioning to works that provide tractable, exact or finite-sample approximate, computations of these values in cases where distributional assumptions are made: 

i) [Chen, Jianbo, et al. "L-shapley and c-shapley: Efficient model interpretation for structured data." arXiv preprint arXiv:1808.02610 (2018).]

ii) [Teneggi, Jacopo et al. "Fast hierarchical games for image explanations." IEEE Transactions on Pattern Analysis and Machine Intelligence 45.4 (2022): 4494-4503]

The authors should comment on these because, in these cases, approximations are not needed, and thus Shapley coefficients admit provably more efficient computations. Naturally, if these properties of the data are not met, the approximation strategies that the authors describe do provide useful estimation tools.

* In sec 2.3, the authors first define their Unified Stochastic Estimator and then show that it is a generalization of other schemes. However, their Definition 2 reads "Most existing stochastic estimators can be unified.." which sounds like a claim to be proven, not a definition. Indeed, this is shown/proven immediately after in the form of running text. I think the authors should consider re-organizing this Definition + Remarks as Definition + Theorem, which states the strict generalization.

* I find the AUC results reported in table 3 a bit unsatisfying: the standard error (i presume?) are at the same or larger order of magnitude than the means! This makes these comparisons have very little meaning.

* On the other hand, the improvement in inference speed is massive, and the authors wait until the end, in section 4.2.4, to showcase this. This is the greatest benefit of the method, and the authors should consider stressing this throughout the text more.

* I'm confused as to how the ground truth Shapley values are computed for the experiments in Fig 2: some of the datasets have up to 96 features, which would results in completely prohibitory computation (around 10^28 flops). Even if these are computed w.r.t. some reference surrogate approximation (as I believe the authors explain in the Implementation Details), how are these surrogate trained? don't they need the ground truth values?

Minor: 
* I think that to say that "Deep learning techniques have revolutionized various industries due to their learning capability by universal approximation theorem" is a stretch. Many methods provide universal approximation. The reasons for deep learning becoming so popular are others and more diverse.

* After Definition 1, the authors write "*However, machine learning models are not cooperative games and the complexity of Eq. (1) grows exponentially with the data dimension d*". How is "*machine learning models are not cooperative games*" relevant to "*the complexity of Eq. (1) grows exponentially with the data dimension d*" exactly?

* "the optimization object L in Eq. (5) need[s] to be approximated"

* There is an $\arg\min_\eta$ missing in the right-most term in Eq(5),

* capaicity -> capacity

* in equation 14, remove " \to Shapley values" as this reads as "tends to", which is not what the authors meant pressumably.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work considers the topic of efficient Shapley value estimation and presents two contributions. The first is that several current Shapley value estimators can be understood via a shared perspective of a linear transformation of expectations of feature subsets. The second is that amortized Shapley value estimation can be viewed via comparison to the true Shapley values in a chosen metric space, which enables the development of a new approach, SimSHAP. Under this method, we simply calculate the similarity to estimated Shapley values, and this is competitive with an existing amortized method (FastSHAP).

### Strengths
Efficient Shapley value estimation is an interesting topic that is in need of improved methods, particularly ones that leverage amortization to provide faster solutions than stochastic estimators. This work provides a new perspective on existing stochastic estimators, although it does appear to derive any practical insights or algorithms from this perspective. It then provides another new perspective on amortized methods, and the authors use this to propose SimSHAP. SimSHAP is simple and competitive with FastSHAP.

### Weaknesses
About the main methodological contributions:

- The main contribution of this paper is SimSHAP, which involves training a Shapley value estimation model by comparing to estimated values for each gradient step. While there is a lot of build-up to this proposal, this idea has been explored by at least two other works [1, 2], so the novelty is limited. These works are not cited, and I'm not sure there's much methodological innovation on top of them.

- Regarding the unified perspective in Section 2.3, it seems like this view is clearly apparent for the semivalue-based estimator and does not add much here. After reading the paper closely, I'm not sure it's correct for the least squares estimator. Previous work by Covert & Lee (2021) showed a similar derivation from the KKT conditions, and the analytic solution involves two terms that are estimated: one that resembles the importance sampling term, and one that resembles the transform term (see their section 3.2). In this work, it looks like the transform term $T$ is assumed to be known, which does not correspond to KernelSHAP but rather an alternative version from that work called "unbiased KernelSHAP." Are the authors perhaps analyzing that version rather than the original one? Note that the original one cannot be calculated without a sufficient number of samples due to invertibility issues (the authors here manage to use a very small number in their experiments, suggesting the unbiased version), and that the original one is not provably unbiased (whereas the authors claim zero bias here in eq. 14).

- Regarding the unified view of amortized estimators, it is true that you can compare to the true Shapley values with any properly defined metric and learn the correct function. It is therefore not surprising that you can use the l2 distance. The authors might have been more careful about showing why it's okay to train on inexact values from the least squares estimator, because these training targets will be very noisy. What is the impact of this noise during training? Also, note again that [1, 2] have already explored this approach.

- Regarding the unified view of amortized estimators, I'm not sure the proposed view of FastSHAP is correct. For the unnumbered equation defining $\mathcal{L}(\theta)$ in Section 2.3, there are two equations and I'm not able to see whether they are mathematically equivalent. The authors should consider adding this derivation, either here or in the appendix. Furthermore, the expression for $\phi_x$ is not equal to the Shapley values, because it isn't the solution from the KKT conditions and doesn't incorporate the constraint. Currently, I do not see how this perspective is correct, and it doesn't seem helpful to view the FastSHAP loss as comparing to the true values under a complicated metric: it misses the main point of the FastSHAP loss, which is that it bypasses the need for the ground truth. This perspective is also not necessary to understand that comparing to the ground truth using l2 distance should work.

- Related to the above point, I'm not sure the entries for FastSHAP in Table 2 are correct.

[1] Schwarzenberg et al, "Efficient Explanations from Empirical Explainers" (2021)

[2] Chuang et al, "CoRTX: Contrastive Framework for Real-time Explanation" (2023)

About the experiments:

- In Figure 2, SimSHAP does not appear to outperform FastSHAP. In fact it's noticeably worse for the census dataset. Why is that, and can it be made more accurate?

- The results in Table 3 appear to contradict those in Figure 4. How can SimSHAP have the best AUC when its curves are far from the best?

About the writing, which could be significantly improved:

- The description of related work is incorrect in several places. In the introduction, "semivalue" and "least squares value" are not estimation methods, they are classes of game-theoretic solution concepts, and their mathematical perspectives are used to develop estimation methods (e.g., fitting a weighted least squares model with an approximate version of the least squares objective). Also in the introduction, model-specific methods do not "reduce computation cost by merging or pruning redundant feature combinations," this is not true for TreeSHAP, LinearSHAP or DeepSHAP. It is also not true that "the exact differences among these algorithms remain unclear," the differences seem very clear, as they are described in this work. The gap in missing work seems to be that the fastest solutions either are not general enough (TreeSHAP) or accurate enough (FastSHAP), although this work does not appear to solve the latter problem.

- The "large numeral law" is not common terminology, it may be better to call this the "law of large numbers" as it is typically called (see [wikipedia](https://en.wikipedia.org/wiki/Law_of_large_numbers)). Also, the LLN does not imply an approximation error of $\mathcal{O}(1/\sqrt{M})$, it only implies convergence of the sample mean to the expectation. For the error rate, it might be better to cite a probabilistic error bound like Chebyshev's inequality.

- For proposition 1, it would be helpful to refer to a proof. Or even better, because this is a known result, the authors might refer to one of the works that originally showed it to be true, for example Charnes et al 1988.

- In eq. 8 regarding FastSHAP, the authors' notation neglects to show the input $x$ in the cooperative game $v(S)$. It may be difficult for readers to follow what $v(S)$ represents. It would also help to give a specific example of how $v(S)$ is defined in Section 2.1, because no equation is currently provided.

- Regarding the additive efficient normalization, there are parts where FastSHAP is described as "biased" or that its predictions need to be rectified. The current description could be confusing to many readers, because it suggests that the loss is somehow incorrect, but that's not quite true. For example, you could write that the weighted least squares loss does not encourage the correct optimal value unless the predictions satisfy the efficiency constraint, which can be enforced by applying the normalization to the predictions.

- There are small typos throughout the paper, for example "remarkbly" on page 3 and "minimizaion" on page 4. The paper could be more thoroughly proofread. 

- Overall, the paper's structure is extremely similar to the FastSHAP paper, to the point that the authors have replicated all the main text experiments, many of the supplementary experiments, and have nearly copied some of the writing. It would be helpful to either acknowledge this similarity, or deviate from it more significantly.

### Questions
Several questions are mentioned in the weaknesses section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
