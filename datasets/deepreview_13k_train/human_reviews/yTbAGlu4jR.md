# Learning Identifiable Balanced Prognostic Score for Treatment Effect Estimation Under Limited Overlap

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Understanding individual-level treatment effects is a fundamental and crucial problem in causal inference. In this paper, our objective is to tackle the issue of limited overlap, where certain covariates only exist in a single treatment group. We demonstrate that, under weak conditions, it is possible to simultaneously recover identifiable balanced prognostic scores and balancing scores. By leveraging these scores, we relax the requirement of overlapping conditions in a latent space, enabling us to generalize beyond overlapped regions. This approach also allows us to handle out-of-distribution treatments with no overlap. Additionally, our approach is adaptable to various tasks, including both binary and structured treatment settings. Empirical results on different benchmarks demonstrate that our method achieves state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the paper, the authors tackle an important problem in causal inference: estimating individual-level treatment effects when there is limited overlap in covariates across treatment groups. To be specific, traditional causal inference methods require substantial overlap in covariates between different treatment groups to accurately estimate treatment effects. The paper focuses on cases where this condition is not met, which is challenging for existing methods. The authors propose a solution that allows for the estimation of treatment effects when covariate overlap is insufficient. They achieve this by recovering two types of scores:
   - **Balanced Prognostic Score**: Reflects the expected outcome of an individual without treatment.
   - **Balancing Score**: Indicates the probability of an individual receiving a particular treatment, given their covariates.

The Disentangled Identifiable vaRiational autoEncoder (DIRE) is introduced as a key technical tool. It is a model that disentangles the factors of variation in the data while maintaining identifiable features. Besides, the paper presents theoretical arguments for how the balanced prognostic score effectively manages the issue of limited overlap, and how it can adapt to scenarios where there is zero overlap, addressing out-of-distribution treatments.

Finally, the authors conduct extensive experiments that benchmark their method against others, especially in scenarios with binary treatments and in complex situations where traditional methods may fail due to limited covariate overlap.

### Strengths
1. The paper tackles the critical issue of non-overlap in causal inference, a problem that, if unaddressed, renders many causal analyses ineffective. By confronting this problem head-on, the research addresses a fundamental bottleneck in causal methodology, ensuring that the insights drawn from such analyses are both valid and applicable in more realistic scenarios where perfect overlap is not present. 

2. The authors have conducted an extensive array of simulation studies to showcase the performance of their proposed method. These simulations are critical for demonstrating the method's effectiveness across a variety of conditions and benchmarks. 

3. The paper excels in its articulate presentation. It defines the problem of estimating individual-level treatment effects in scenarios with non-overlapping covariates succinctly. The proposed method, including the innovative use of the Disentangled Identifiable vaRiational autoEncoder (DIRE), is described with a clarity that ensures readers are able to grasp both the significance and the application of the research.

4. The theoretical underpinnings of the paper are robust and effectively illuminate the concepts behind the methodology. The theoretical sections can support the practical aspects of the proposed method but also enhance the reader's comprehension of why the method works.

### Weaknesses
 1. On page 3, the author elucidates the concepts of non-overlapping and limited overlapping with clarity. Yet, in the experimental analysis, specifically in Q2, when introducing a 'degree' of non-overlapping, the definition remains ambiguous. It is crucial for the reader to understand the extent to which this method can effectively operate within various levels of non-overlap. Could the author provide a more detailed explanation? Additionally, the experiment study (Q2) suggests that the proposed "DIRE" method's performance is unaffected by the degree of non-overlapping. This assertion underscores the robustness of the method, but it warrants a deeper explanation to substantiate such a claim.

 2. Section 4.3 discusses the integration of an 'ELBO decomposition trick' into the method, which contributes to the final loss function. The specific advantages of incorporating this technique, particularly in the context of addressing limited overlap issues, have not been fully articulated. What incremental value does this approach provide, and how does it interact with the other components of the loss function, namely the prognostic score-based and balancing score-based losses? If the loss function were simplified to include only these two components, how might that impact the method's performance?

 3. In section 5.4, the paper navigates the complex terrain of structured treatment settings. An elucidation of the inherent challenges within such settings would greatly benefit the reader. Does this term imply a scenario with a multitude of treatments amongst which certain structural patterns are discernible? If so, to the best of my knowledge, two interesting studies can be noted: one from the Journal of Machine Learning Research (JMLR) in 2023: "Learning Optimal Group-structured Individualized Treatment Rules with Many Treatments", and another from the Neural Information Processing Systems (NIPS) conference in 2022: "Learning Individualized Treatment Rules with Many Treatments: A Supervised Clustering Approach Using Adaptive Fusion". Both papers address situations of limited overlap amid an array of many treatments, focusing primarily on the refinement of individualized treatment rules. However, there appears to be a difference in their approaches compared to the one presented in this paper. Could the author expound on the distinctions and potential synergies between these methodologies and the current approach under discussion?

### Questions
1. On page 3, the author elucidates the concepts of non-overlapping and limited overlapping with clarity. Yet, in the experimental analysis, specifically in Q2, when introducing a 'degree' of non-overlapping, the definition remains ambiguous. It is crucial for the reader to understand the extent to which this method can effectively operate within various levels of non-overlap. Could the author provide a more detailed explanation? Additionally, the experiment study (Q2) suggests that the proposed "DIRE" method's performance is unaffected by the degree of non-overlapping. This assertion underscores the robustness of the method, but it warrants a deeper explanation to substantiate such a claim.

2. Section 4.3 discusses the integration of an 'ELBO decomposition trick' into the method, which contributes to the final loss function. The specific advantages of incorporating this technique, particularly in the context of addressing limited overlap issues, have not been fully articulated. What incremental value does this approach provide, and how does it interact with the other components of the loss function, namely the prognostic score-based and balancing score-based losses? If the loss function were simplified to include only these two components, how might that impact the method's performance?

3. In section 5.4, the paper navigates the complex terrain of structured treatment settings. An elucidation of the inherent challenges within such settings would greatly benefit the reader. Does this term imply a scenario with a multitude of treatments amongst which certain structural patterns are discernible? If so, to the best of my knowledge, two interesting studies can be noted: one from the Journal of Machine Learning Research (JMLR) in 2023: "Learning Optimal Group-structured Individualized Treatment Rules with Many Treatments", and another from the Neural Information Processing Systems (NIPS) conference in 2022: "Learning Individualized Treatment Rules with Many Treatments: A Supervised Clustering Approach Using Adaptive Fusion". Both papers address situations of limited overlap amid an array of many treatments, focusing primarily on the refinement of individualized treatment rules. However, there appears to be a difference in their approaches compared to the one presented in this paper. Could the author expound on the distinctions and potential synergies between these methodologies and the current approach under discussion?

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the identifiability of treatment effects under limited overlap, but with latent adjustments, confounders, and instruments. Under a general causal graph model, the authors show that overlapping conditions can be sustantially relaxed, and treatment effects can extend to non-overlapping regions. Experiments also show that the proposed method achieves superior performance compared with competing methods in various benchmarks.

### Strengths
1. Significance and contribution.

Treatment effect estimation beyond overlap is an important problem. This paper contributes to this literature by proposing a model that enables treatment effect generalization and methods to achieve so. 

2. Quality and clarity.

This paper is clearly written, with discussions from time to time that address possible confusions. The experiments are thorough and provide concrete support to the technical part.

### Weaknesses
Discussion on the model

The identifiability of treatment effects relies crucially on the model. While some part such as outcome DGP is discussed so that readers understand they are weaker than existing literature, assumption 4.3 and 4.4 for treatment and prognostic score may need more justification. Specifically, assumption 4.3, which posits that the balancing score is a sufficient statistic for treatment assignment, needs further elaboration. It's not immediately clear why this assumption holds in the context of the proposed latent variable model, especially given the potential for complex interactions between observed covariates and latent confounders. Similarly, assumption 4.4, which parameterizes the outcome as a function of a prognostic score, needs more justification. While the authors mention it generalizes a previous assumption, the specific form of the generalization and its implications for identifiability need to be more thoroughly explained. The assumption that the outcome itself can serve as a sufficient statistic for the outcome, and the subsequent generalization to n-dimensional prognostic scores, requires more detailed explanation of its theoretical underpinnings and practical implications.

### Questions
1. I don't really get why a bPGS can always be derived based on a PGS (right after Proposition 1). Can you provide more discussion?

2. Besides justifying the model assumptions, is there a way to verify this model is reasonable given a dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigated the challenge of estimating treatment effects when there's limited overlap. They emphasized that overlap need not be present in the covariate space; instead, it suffices for overlap to exist within a latent representation. To address this, they introduced a disentangled identifiable Variational Autoencoder that effectively separates adjustment, instrumental, and confounder variables. Their experiments demonstrated that their approach outperforms other baseline methods, showcasing its superior performance.

### Strengths
They attempted to acquire a disentangled representation, effectively segregating confounders, instrumental variables, and adjustment variables. The results from their experiments unequivocally demonstrate a notable improvement in performance.
They used the idea from chen et al. 2018 to achieve a disentangled representation.

### Weaknesses
I wish I could see the results for a simple VAE without ELBO decomposition, to see how much improvement could happen. it is not clear to me how much this improvement is coming from elbo decomposition.

I find the decoder structure in Figure 1 unclear. It's not evident to me whether we are reconstructing observed variables from latent variables, or if we need to supply T and Y as signals to the model.

Equation 12's inference factorization isn't immediately clear to me. It would be greatly appreciated if the authors could provide an explanation in the appendix.

There are some assumptions mentioned, such as the injective nature of certain functions. Were these assumptions followed in the implementation, or were they primarily included for mathematical purposes?

Is it necessary to include a z4 in the model?

In section 5.3, I assumed we would observe a drop in performance in other methods while your method maintained a constant performance. However, this doesn't appear to be the case, and varying the level of limited overlap doesn't seem to affect the performance of other methods.

### Questions
Questions:
1. I find the decoder structure in Figure 1 unclear. It's not evident to me whether we are reconstructing observed variables from latent variables, or if we need to supply T and Y as signals to the model.
2. Equation 12's inference factorization isn't immediately clear to me. It would be greatly appreciated if the authors could provide an explanation in the appendix.
3. There are some assumptions mentioned, such as the injective nature of certain functions. Were these assumptions followed in the implementation, or were they primarily included for mathematical purposes?
4. Is it necessary to include a z4 in the model?
5. Was there any hyperparameter to balance the contribution of different losses to the final loss?
6. In section 5.3, I assumed we would observe a drop in performance in other methods while your method maintained a constant performance. However, this doesn't appear to be the case, and varying the level of limited overlap doesn't seem to affect the performance of other methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Post-rebuttal update**: 
I am sorry, but I have to say most main claims of the paper still look a mess to me. I maintain my score but add my final reply to the author(s).

Markov condition. "This update on assumption will not impact the fundamental methodology of our proof." I am dubious. Could you highlight how this assumption is used in the proof?

Injective is unrealistic. I do not understand what you mean by "their dimensions can be hyperparameterized". Anyway, could you show that, for function g, dim(image) ≥ dim(domain)?

Assum 4.2. My concern was just that the second equality seems trivially satisfied. Then, why it is an assumption?

**End update**


The paper proposes a new identifiable VAE to disentangle and identify the instrumental variable, hidden confounder, and prognostic score. Theoretical analysis and experimental results are provided.

### Strengths
Using identifiable VAE, and more generally deep identifiable models, to estimate causal effect is a promising recent direction.

It is interesting to see the potential of identifiable VAE to handle zero overlap.

Experiments show favorable performance regarding estimation accuracy.

### Weaknesses
 *Impossible/unrealistic theoretical assumptions, and (almost) assume the main results*

Most importantly, Theorem 1 result 1 directly assumes the 3 hidden variables are identified up to injective mappings, but this is what we want to prove! For example, this is the major goal of the theoretical analysis in the Intact-VAE paper. Moreover, the 2nd independence assumption (through mutual information) violates the Markov condition; Z3 and Y are related through the path Z3-T-Y. Any violations of Markov condition are dubious without detailed justification.

In Prop 2, g maps three variables to a variable. Then, injectivity is impossible unless the domain of g is in fact a 1-dim manifold embedded in the 3-dim space. Similarly, assuming functions K4-K7 are injective is unrealistic.

*Insufficient experimental evidence, particularly for identification and zero overlap*

The experiments only examine the ATE error and PEHE, without touching on identification. In Fig 3, there are no legends for the x-axis, but the tendency of the proposed method is no better than others.


In Sec 5.3, the claim “even in the in-sample scenario, β-Intact-VAE struggles to generate a balanced prognostic score in the presence of instruments” is unconvincing. You only show your method has lower errors, but the reason might be, for example, that your method has better fitting capacity. Moreover, the claim “The performance of DR-CFR diminishes as the limited overlapping level becomes more severe” is also unconvincing, the differences are very small and in the range of error bars.

*The claim of handling zero overlap is not theoretically supported.*

But the claims in the Abstract and contributions make readers think the opposite. The statement “since DIRE also generalizes its identification capability to the out-sample setting, …” at the end of Sec 5.2 is also read as if there are theoretical supports.

*No support for the identification of balancing score*. In fact, after it is claimed in the Abstract and contributions, the only place this is mentioned is at the end of Sec 4 “we predict the treatment using the identifiable balancing score”; again, a blank claim.

*Discrepancy between the theory and method*

If the theory works, there is no need to use the “ELBO decomposition trick” and to add L_{prognostic score} and L_{balancing score}. In general, any departure of practical choices and the theory should be discussed and/or supported by experiments.

*Writing is very unclear and sloppy*

The theoretical assumptions and statements are not clear and/or not discussed clearly.

- Assum 4.1, the “circle-plus” symbol is used without introduction. I assume it means “concatenate the dimensions together”.
- Assum 4.2, I assume p in eq3 means p(Z1, Z2), but, if j_t is just a general function, what is the difference between the two sides of the 2nd equality? I don’t think “the second equality is obtained through backdoor criterion” is a meaningful explanation. Also, the symbol j_t is used without introduction (though I know you are following the previous work.)
- Assum 4.4 comes from nowhere. We need the discussion of its causal meaning, or, if it is a technical assumption, why it should hold in practice should be discussed. For example, rank conditions are usually critical for identification, so we care what is n here?
- I cannot understand Prop 1. There is a “where j =” clause, but j is even not mentioned before! (I assume it is not j_t in eq4). And I cannot understand why it means “we can always derive a balanced prognostic score”.
- In Theorem 1, p_{theta} is used before introduction.
- Symbol p is overloaded, meaning either prognostic score or probability.

The major (unrealistic) assumptions, as I mentioned in the first weakness, are not listed formally as in Assumption 4.1 etc, but are mentioned in the pass in the theorems. This is very sloppy writing.

Figure 3 is not mentioned in the main text.

### Questions
Please address the issues/questions raised in the Weaknesses.

My general suggestion is that, don’t take hidden confounding lightly! Causal effect identification and estimation under hidden confounding is an extremely hard problem. I do not want to over-generalize, but I have not seen a single conference paper that rigorously addresses this problem under non-standard settings. I refer to standard settings as, for example, IVs, proxy variables, balancing scores, prognostic scores (but usually not combinations of them), and, in general, those studied in the causal inference literature and published at Biometrika, Econometrica, Journal of Econometrics, Journal of the American Statistical Association, Journal of the Royal Statistical Society Series B, Annal of Statistics, etc. If you check the Intact-VAE paper, which is your main reference, you will find it indeed refers to those journals a lot.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
