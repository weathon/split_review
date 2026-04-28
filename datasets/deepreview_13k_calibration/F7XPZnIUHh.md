# Adversarial Learning of Decomposed Representations for Treatment Effect Estimation

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 5, 5, 3

## Abstract
Estimating the Individual-level Treatment Effect (ITE) from observational data is an important issue both theoretically and practically. Including all the pre-treatment covariates for prediction is unnecessary and may aggravate the issue of data unbalance.
While the confounders (C) are necessary, there are some covariates that only affect the treatment (instrumental variables, I), and some only affect the outcome (adjustment variables, A). Theoretical analyses show that including extra information in I may increase the variance lower bound and hence should be discarded. To facilitate the decomposed representation learning for the ITE estimation, we provide a rigorous definition of  {I, C, A} in terms of the causal graph and prove that such decomposition is identifiable from observational data. Under the guidance of such theoretical justification, we propose an effective ADR algorithm to learn the decomposed representations and simultaneously estimate the treatment effect by introducing adversarial modules to constrain the independence and conditional independence relations. Our proposed algorithm can be applied to both categorical and numerical treatments and the disentanglement is assured by both theoretical analyses and empirical results. Experimental results on both synthetic and real data show that the ADR Algorithm is advantageous compared to the state-of-the-art methods. Theoretical analyses also provide a path to further explore the issue of decomposed representation learning for ITE estimation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduced a new decomposed representation learning method for conditional average treatment effect (CATE) estimation. It is based on a theoretic property that all the covariates in the valid adjustment set can be either instrumental variables, adjustment variables, confounders, or background noise variables, and that this this decomposition is identifiable from the observational distribution. The paper then develops an adversarial learning technique to decompose the covariates into three categories of instrumental variables, adjustment variables, and confounders. The authors compare their method, namely, adversarial learning of decomposed representations (ADR), with the existing representation learning baselines for CATE estimation on several synthetic and semi-synthetic benchmarks.

### Strengths
The paper is clearly written and well-structured. I found the theoretic results of the paper regarding the decomposition of the insightful and important for representation learning for CATE. For example, I appreciate that the authors provided formal identification guarantees for the decomposed representation, i.e., Prop. 3.1 and Theorem 3.2. Also, the experimental results on decomposing, i.e., Figures 3-5, are very informative.

### Weaknesses
There are several issues in this paper:
  1. Error in derivations. I spotted two issues. First, Theorem 3.2 claims that $\mathbf{C}$ is a valid set $\mathbf{X}’$ in the definition of the instrumental variables. On the other hand, by looking at the example in Fig. 1 (b), $\mathbf{C} = \varnothing$, but $X_2 \notindependent Y \mid T$. Second, there seems to be an erroneous statement in the proof of Prop. 3.2, that the equality in the expectation $\mathbb{E} (T \mid A(X) ) = \mathbb{E}(T)$ implies the independence, $T \independent A(X)$, which is not true, if $T$ is continuous. Specifically, there could be inequalities wrt. to higher moments. Those two issues are further very important for the correct implementation of the ADR.
2. Novelty. The implementation of the decomposed representation learning with adversarial representations, namely, ADR, was already proposed in [1], and this work is not even mentioned in the related work or included as a baseline. Therefore, the paper has only a marginal contribution.
3. Implementation and tuning. Some details are missing on the implementation of the baselines, e.g., the dimensionalities of the representations.  Also, the authors did not provide any details on how to choose the dimensionalities of the decomposed representations in their method, which is a very important issue in practice, e.g., for the IHDP benchmark. Therefore, it is impossible to say, whether the empirical evaluation was fair.

### Questions
See the section on weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the disentanglement of instrumental variables (I), adjustment variables (A), and confounders (C) (distinguished according to their dependence on the treatment and outcome variables) from covariates for causal effect inference.
They provide an identifiable definition of these variables and a method based on adversarial training in which two discriminators predict the treatment and outcome variables from A and I, respectively, and the representation extractors for A and I counter them.

### Strengths
* Since the representation balancing for CATE estimation is pointed out as not capturing the whole CATE estimation errors in literature, representation decomposition is a promising direction as a response.
* In this context, the first identifiable formulation of representation decomposition through an adversarial formulation would be a very mainline approach.
* A simulation-based experiment clearly illustrates its superiority in disentanglement performance compared to some existing methods.

### Weaknesses
1. The aim is not clear. The disentanglement itself seems to be the aim, and it is not clear how it contributes to the accuracy of the CATE (see Question 1).
1. The design of the loss function is somewhat heuristic and a logical explanation or guarantee is insufficient (see Question 2).
1. The adversarial joint objective is not in a convex-concave formulation, which means there is no guarantee of convergence. Intuitively, it seems very unstable.
    * Are there any existing studies of such a formulation that *maximizes* the loss function such as the MSE?
    * While maximizing the MSE by the adversary is easily accomplished by making the predictions infinity, it seems to be difficult to predict it accurately.
    * It may be helpful to show realistic convergence using a learning curve.

### Questions
1. What is the purpose of the decomposition? The original purpose was to combine weighting only w.r.t. the confounders in DR-CFR, in my understanding. Confounder variables should be limited to necessary ones to alleviate the estimation variance due to extreme weights. The proposed method does not use weighting and thus I am confused about its aim.
    1. A possible reason for the above question is to limit the input, i.e., excluding instrumental variables from the input of the predictor, as suggested in Thm 3.1. Although, Thm 3.1 is only about the variance lower bound and I am not sure if that is dominant or critical in the estimation error. Does excluding I(x) from the input of the predictor really have a decisive impact? Any theory about the whole risk bound of the proposed method, or an ablation experiment on the "with-I(x) model" $f_{C\cup A\cup I\cup T \to Y}$ instead of $f_{C\cup A\cup T \to Y}$ might provide empirical evidence.
1. Why $L_A$ does not include the accuracy of $f_{C\cup A\cup I \to Y}$? A(x) is input to $f_{C\cup A\cup I \to Y}$, but the gradient for the connection is stopped. Does not this have any negative impact on the whole design of the optimization procedure?

Minors:

* P4 Theorem 3.2 stats -> states
* P4 Hassanpour & Greiner (2020). -> [Hassanpour & Greiner (2020)].

=== EDIT after reading the reponse===

I would like to keep rating because I think the current structure is insufficient in the following points, although I recognize a certain value in that they newly define the I/C/A definitions and derive a principled method.
My concerns are summarized two-fold (and not solved yet).

1. Motivation: the existing decomposition-based methods are weighting-based methods, whereas the proposed method is not, and does not perform full bias removal at the loss function level (thus, e.g., not guaranteed to be consistent when misspecified). Therefore, it does not seem appropriate to position this as this research stream.
- Rather, it should be positioned in the stream of simple modeling methods, such as T-Learner, which is not organized and written as such, and thus lacks a motivation argument to claim value in that context.
- Also, when viewed simply as a SOTA CATE estimation method, it lacks sufficient statistically significant results.

2. Soundness: the method is considered as a heuristic alternate update and not formalized as a joint objective; thus the optimization can be unstable (maybe it does not converge).
- Unlike GANs, it is not formalized as a zero-sum game that provides some convergence guarantee.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses efficient estimation of Conditional Average Treatment Effects (CATE), working primarily in the case where the covariate set is high-dimensional and contains different kinds of pre-treatment covariates (e.g., confounders, IVs, variables only affecting the outcome).

### Strengths
See below for a contextual discussion of strengths and perceived weaknesses.

### Weaknesses
In my view, this paper strikes me as overall well-written and motivated (albeit somewhat heavy on notation which could limit its broader impact). The assumptions used in the paper are standard for observational inference (which I view as a strength of the paper). The point that variance bounds are affected by pre-treatment covariate number and that distinguishing between kinds of pre-treatment estimation variance bounds in an effort to improve the bound is intriguing, as is the notion that we can distinguish between pre-treatment covariates of different types in an identified manner. 

My main comments concern the ability of readers to evaluate the contribution of the paper in view of the literature. For example, what is the relationship between the work on semiparametric efficiency bounds in effect estimation with some of discussion here. The literature on, e.g., semi-parametric efficiency is often focused on ATE (as opposed to CATE estimation as here), but even a discussion of the efficiency of the approach here for the ATE vs. in that setting would be most informative for this reviewer. 

On a related note, the paper could further improve its contribution by evaluating observational ATE recovery against some of the most commonly used methods for that (e.g., doubly robust methods and something simple like inverse propensity score weighting). If readers can see that the proposals here by improving observational CATEs also improve observational ATEs (which have extremely broad applicability in existing applied work, much more than observational CATEs), the paper's contribution would be enhanced. 

On another note, the decomposition of I(X), C(X), and A(X) would be extremely useful in practice. However, one limitation is that in any given experiment, we cannot know/validate for sure (and if there is good a priori reason to suspect a covariate is an I, C, or A adjustment could proceed directly with that knowledge). Nevertheless, if the authors could obtain a case (perhaps from, e.g., the biological context where biophysical relations are approximately known) where the decomposition provides useful information to the investigator, I would think the contribution would also be improved. By the way, it would be very convincing if the approach here was somehow better than using a priori knowledge of the decomposition directly. 

A few small comments: 

(1) Not to sound pedantic, but the writing at the sentence/paragraph level is somewhat stronger than across sections. For example, there is much discussion of the variance bound in the theory section, but this emphasis disappears later on. The paper can sometimes feel disjointed (as if separate contributions are fused). 

(2) I would edit the "Algorithm 1" text to remove the reference to (I believe) the specific optimizer Adam. Optimizers will come and go with time and presumably, the contribution here is more general, and other optimizers would work as well in principle.

### Questions
One question concerns whether the authors intend investigators to actually examine the inferred decomposition of X, or whether the motivation is mainly or exclusively efficient CATE estimation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Post-rebuttal update**: I maintain my score but add my final reply to the author(s).

*On Thm 3.1* It seems the quotation agrees with my understanding, and I guess the "their" does not refer to $\hat\theta_n$. All in all, do you agree that this result is not essential for the method? If so, I still suggest moving it to the Appendix. Otherwise, you should explain its importance together with clearer writing.

*On Def 3.1* I believe we agree that there are admissible sets diff from yours and might provide better finite sample performance. So you need to admit and explain this, particularly because your defs of I, C, A are diff from usual.

I still do not agree this method is theoretically guaranteed in a strict sense. You may want to explain in what sense you mean it.

**End update**

As for the problem of treatment effect estimation under unconfoundedness, the paper proposes to decompose the observed covariates into three disjoint sets, roughly corresponding to the usual concepts of instrumental, confounding, and adjustment variables. The variables are defined in graphical terms, and then reduced to independence relationships, by Theorem 3.2. An adversarial learning approach is proposed to induce the independence. Experiments show the benefits of the method.

### Strengths
The separation of covariates into three disjoint sets using Def 3.1 is an interesting idea.

The main theoretical results seem correct (proofs not checked, but I have my own (rough) proofs and cannot come up with counterexamples).

Experiments show the representations are practically decomposed, and the ablation study shows the usefulness of the theoretical ideas.

### Weaknesses
 **Some problematic theoretical developments and discussions**

*Th 3.1* (variance lower bound). The statement seems incorrect or has typo(s). For CATE, the bound should depend on the value of x, but your eq of V takes expectation on X. Moreover, for consistent estimators, V should depend on n, and V → 0 as n → inf, but your V is a constant wrt n. The authors' explanation of asymptotic variance does not address the core issue that the bound should be a function of x, not a constant. The variance of a CATE estimator, even asymptotically, is conditional on x, and this is not captured in the current formulation. Furthermore, the provided reference does not justify the specific form of the bound presented in the paper. Anyway, I don’t see this result has a strong relationship to the method (or else I will give a lower score), you could remove this result if you cannot fix it.

*Def 3.1* deviates from standard notions in the literature and also has practical limitations. For example, 

- in your Fig 1a, if there is an X4 that is a parent of both X1 and X2, this is usually understood as a confounder and can improve the precision of estimation, but is excluded from your approach. The authors' justification that  $P(Y|X_2, X_3, do(t))=P(Y|X_2, X_3, X_4, do(t))$ does not address the point that including $X_4$ can reduce variance in finite samples, even if it does not introduce bias. This is a crucial point that the authors need to acknowledge and discuss.
- your Fig 1b is actually the “M-bias” case (see model 7 [here](https://ftp.cs.ucla.edu/pub/stat_ser/r493.pdf)). X1 and X3 both satisfy the backdoor criteria and could be understood as confounders. Here, besides X3, both X1 and X2, which are excluded from your approach, could possibly improve the precision (though X2 alone is a bad control). The authors' claim that there are no unblocked back-door paths is incorrect. The path T-X1-X2-X3-Y is a backdoor path that is blocked by conditioning on X2. Thus, X1 and X3 are indeed confounders, and the authors need to address this discrepancy with standard causal inference literature.

I suggest being clear that the definition is nonstandard, discussing and comparing it to usual notions (possibly in the Appendix). In particular, you should mention there are possible variables in your IVs that are good to add as controls. 

See Questions for more comments.

**The method is theoretically motivated but *not* theoretically guaranteed.** 

Prop 3.2 seems correct but the learning approach is not sufficient. Taking (i), I agree that independence means larger L_A than dependence, but, there can be many different functions A that give the independence. Worse, some A could take a confounder but “cleverly” through away the dependence on T. Similar comments apply to (ii). The authors' response does not address this concern. The core issue is that maximizing the loss function does not guarantee that the learned representations will capture the desired causal structure. There is no mechanism to prevent the adversarial learning from finding trivial solutions that satisfy the independence criteria without actually disentangling the causal variables. Could your theory rule out these concerns?

The ADR algorithm does not precisely enforce the required independence or even the approach in Prop 3.2, because L_A, L_C, L_I contain both prediction and adversarial terms, so the ADR is a trade-off but not a direct implementation of the theory. Moreover, training the losses together with hyper-parameters adds yet another layer of trade-off.

I suggest weakening the claims on this contribution.

### Questions
I will read the rebuttal and revised paper and raise my score to 6 if the issues/questions in Weaknesses are addressed. Some further points are as below.

Prop 3.1 (i) I think we can say “either…or…” which is stronger than simply “or.” Also, it is safer to say “X \indep T and X \indep Y” which is weaker than the joint independence and seems enough. 

It is confusing to only stress C in the last statement of Th 3.2. In fact, A may also be sufficient, as in your Fig 1b.

The comments below Th 3.2 are confusing. It is an identification because the 3 sets of variables are determined by the observable joint distribution, through the conditional independence requirements. In fact, the definition of I/C/A implicitly assumes graphical structures, and you reduce the graphical structure to independence by *causal Markov and faithfulness assumptions*. Indeed, these *are* the “further assumptions” you also use.

Add experiments that directly evaluate identification and decomposition. Actually, Fig 3 and 5 show the method does not fully identify and decompose the covariates. Thus, it is meaningful to examine this more closely. For example, we could build several datasets with only one I, C, A respectively, and plot the learned I, C, A against the truth.

As to identifiable representation, the recent advance in using deep identifiable model (e.g., [1]) to estimate treatment effect (e.g., [2, 3]) is worth discussing in the related work. 

[1] Khemakhem, Ilyes, et al. "Variational autoencoders and nonlinear ICA: A unifying framework." International Conference on Artificial Intelligence and Statistics. PMLR, 2020.

[2] Wu, Pengzhou Abel, and Kenji Fukumizu. "beta-Intact-VAE: Identifying and Estimating Causal Effects under Limited Overlap." International Conference on Learning Representations (2022).

[3] Ma, Wenao, et al. "Treatment Outcome Prediction for Intracerebral Hemorrhage via Generative Prognostic Model with Imaging and Tabular Data." International Conference on Medical Image Computing and Computer-Assisted Intervention., 2023.

Minor (did not affect the score):

It is bad to use the abbreviation ITE for the Individual-level Treatment Effect. Maybe you could use “ILTE” instead. Actually, “ITE” in your paper refers to both ILTE/CATE and eq1, which is the correct definition of ITE.

"Adjustment variables" usually mean the set of variables conditional on which the confounding is removed. Only in some ML papers do adjustment variables refer to those variables that affect Y but not T. This is another often-seen misnomer in the ML community.

The \mathcal(L) in Prop 3.2 should be a typo.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The main contributions of this paper are the ADR algorithm for decomposed representations in ITE estimation, a precise definition of variables decomposition, and theoretical analysis showing the benefits of this decomposition approach, including the variance lower bound of the CATE estimand. The ADR algorithm demonstrates its effectiveness through empirical validation and can be applied to a variety of treatment data types.

### Strengths
(1)The paper introduces the concept of $\mathbf{I, C, A}$ based on causal graphs and proves that this decomposition can be identified from observational data. 

(2) A novel ADR algorithm is proposed, leveraging adversarial modules to ensure independence and conditional independence relations. 

(3) This ADR algorithm is applicable to both categorical and numerical treatments and is supported by both theory and empirical results.

### Weaknesses
 **Presentation**: There are many unclear statements. For example, `The ITE refers to $Y_i(t) − Y_i(0)$.' why do not write it as $Y_i(1) − Y_i(0)$? Eq.(1) is only presented for a binary treatment. How to define ITE or CATE for other types of treatments?


**Novelty**: The use of decomposed representation for identifying adjustment sets in causal inference has been previously explored in the literature. This paper likely builds upon existing methods and concepts while potentially introducing novel insights or improvements. In essence, several conclusions in the article may have already been substantiated. Additionally, the manuscript does not reference the literature that employs sufficient dimension reduction for learning the adjustment set.

**Contribution**: The conclusion in Theorem 3.2 has been proved by previous work[1,2], and both works also allow latent variables. So, the developed ADR can be regarded as a restricted version of the implementation of these two works. Therefore, the contributions of the work is not high enough for ICLR. 

[1] Entner D, Hoyer P, Spirtes P. Data-driven covariate selection for nonparametric estimation of causal effects[C]//Artificial intelligence and statistics. PMLR, 2013: 256-264. 

[2] Cheng D, Li J, Liu L, et al. Local search for efficient causal effect estimation[J]. IEEE Transactions on Knowledge & Data Engineering, 2022 (01): 1-14.

### Questions
Q1, `To deal with the issue, the common practice is to introduce pre-treatment covariates such that {Y (t)|x} =d {Y |t, x} (ignorability assumption).' Is it correct? If there are only pre-treatment covariates, it implies that there are no descendants of both $T$ and $Y$ in the set of covariates. How can we ensure $ignorability$ hold?

Q2, Eq.(2): `E[Y(t)|x]=E[Y(t)|x,T =t]=E[Y|x,T =t]', Can we really transform the potential outcome prediction problem into a supervised learning problem? 


Q3. For the causal DAG in Fig. 1 (b),  does ADR also apply when $X_1$ is an unobserved variable.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
