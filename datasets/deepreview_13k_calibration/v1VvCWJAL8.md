# Towards Characterizing Domain Counterfactuals for Invertible Latent Causal Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Answering counterfactual queries has important applications such as explainability, robustness, and fairness but is challenging when the causal variables are unobserved and the observations are non-linear mixtures of these latent variables, such as pixels in images.
One approach is to recover the latent Structural Causal Model (SCM), which may be infeasible in practice due to requiring strong assumptions, \eg linearity of the causal mechanisms or perfect atomic interventions.
Meanwhile, more practical ML-based approaches using na\"ive domain translation models to generate counterfactual samples lack theoretical grounding and may construct invalid counterfactuals.
In this work, we strive to strike a balance between practicality and theoretical guarantees by analyzing a specific type of causal query called \emph{domain counterfactuals}, which hypothesizes what a sample would have looked like if it had been generated in a different domain (or environment).
We show that recovering the latent SCM is unnecessary for estimating domain counterfactuals, thereby sidestepping some of the theoretic challenges.
By assuming invertibility and sparsity of intervention, we prove domain counterfactual estimation error can be bounded by a data fit term and intervention sparsity term.
Building upon our theoretical results, we develop a theoretically grounded practical algorithm that simplifies the modeling process to generative model estimation under autoregressive and shared parameter constraints that enforce intervention sparsity.
Finally, we show an improvement in counterfactual estimation over baseline methods through extensive simulated and image-based experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on the problem of domain counterfactuals in the context of latent causal models and proposes a practical yet theoretically grounded approach to address this problem, aiming to improve the estimation of domain counterfactuals while making minimal assumptions about the true model and available data.  Experiments on extensive simulated and image-based data show the advantages of domain counterfactual estimation both theoretically and practically.

### Strengths
The problem setting, which revolves around domain counterfactual estimation, is a novel and highly intriguing area of research. I believe it has the potential to make a valuable contribution to the research community.

---------

My main concerns are as follows:

1) I am experiencing confusion regarding domain counterfactual equivalence. While I agree that it may not be necessary to fully identify the true latent causal model for domain counterfactual estimation, I would appreciate a more intuitive explanation of Theorem 1 and its implications. For instance, it would be helpful to know which specific aspects of the true latent causal model need to be identified to enable domain counterfactual estimation. This could include considerations like the identifiability of latent noise variables, the size of the intervention set, or any other relevant factors. 

2) How should we precisely define the size of the intervention set, denoted as 'k'? In discussions about interventions or the number of variables subject to intervention, there is usually a reference to a latent causal model where no interventions have occurred. How do we accurately establish this reference latent causal model?

3) One of the main contributions, in my view, pertains to the definition of the canonical domain counterfactual model. However, this definition might appear somewhat stringent, particularly with its requirement that only the last variables be intervened. Even though it's surprising that any Invertible Latent Domain (ILD) model can be transformed into an equivalent canonical ILD, could you provide some real-world applications to illustrate and justify the relevance and utility of the canonical domain counterfactual model?

4) It appears that in order to enhance domain counterfactual estimation, one needs to have prior knowledge of the intervention sparsity, denoted as 'k.' However, in practical scenarios, obtaining this information can be challenging. While the experiments do offer some insights and analysis regarding the mismatch of sparsity between generative and inference models, could you provide further justification or reasoning for the selection of the appropriate value for 'k'?


I would be willing to increase my rating if these concerns are addressed.

### Weaknesses
My main concerns are as follows:

1) I am experiencing confusion regarding domain counterfactual equivalence. While I agree that it may not be necessary to fully identify the true latent causal model for domain counterfactual estimation, I would appreciate a more intuitive explanation of Theorem 1 and its implications. For instance, it would be helpful to know which specific aspects of the true latent causal model need to be identified to enable domain counterfactual estimation. This could include considerations like the identifiability of latent noise variables, the size of the intervention set, or the specific forms of the structural equations, and how these interact to guarantee counterfactual equivalence. A more detailed discussion of what aspects of the latent causal model are irrelevant for counterfactual equivalence would also be beneficial.

2) How should we precisely define the size of the intervention set, denoted as 'k'? In discussions about interventions or the number of variables subject to intervention, there is usually a reference to a latent causal model where no interventions have occurred. How do we accurately establish this reference latent causal model? Specifically, how do we determine which latent variables are considered 'intervened' when comparing across different domains, and what criteria are used to decide if a change in the structural equation constitutes an intervention, especially when the underlying causal mechanisms are unknown?

3) One of the main contributions, in my view, pertains to the definition of the canonical domain counterfactual model. However, this definition might appear somewhat stringent, particularly with its requirement that only the last variables be intervened. Even though it's surprising that any Invertible Latent Domain (ILD) model can be transformed into an equivalent canonical ILD, could you provide some real-world applications to illustrate and justify the relevance and utility of the canonical domain counterfactual model? It would be helpful to see concrete examples where this canonical form simplifies analysis or leads to more efficient computation, and how it relates to practical scenarios where interventions might not naturally occur in the last variables.

4) It appears that in order to enhance domain counterfactual estimation, one needs to have prior knowledge of the intervention sparsity, denoted as 'k.' However, in practical scenarios, obtaining this information can be challenging. While the experiments do offer some insights and analysis regarding the mismatch of sparsity between generative and inference models, could you provide further justification or reasoning for the selection of the appropriate value for 'k'? Specifically, what are the practical implications of overestimating or underestimating 'k', and how does this affect the accuracy and reliability of the counterfactual estimates? What strategies can be used to determine a reasonable value for 'k' when the true intervention structure is unknown?

### Questions
See above

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
UPDATE: I thank the authors for their reply, and am happy to see that the case I described was in fact covered by the theory. I have raised my score accordingly.

This paper considers the problem of making counterfactual predictions, in a multi-domain setting of latent causal models: In each domain, the latent variables form an SCM, the observed variables are computed from the latent ones by a deterministic function that is shared by all domains, and the counterfactual query asks, given observed data from one domain, what that data would have been had it been generated in another domain.

### Strengths
The paper is clearly structured, guiding the reader through the theoretical setup.

Compared to existing similar work, this paper provides a significant and novel contribution, both in terms of theoretical results and their application in an algorithm.

### Weaknesses
I have a concern that there might be an unstated assumption; see my main question below.

The text could benefit from more proofreading.

### Questions
One thing that is unclear to me about the problem setting is the following. Suppose $g = Id$, for some domains $f_d = Id$, and for others $f_d = -Id$. Then in all domains, the observed variables are independently distributed as standard normals. (The same would be true for variations where e.g. each domain flips the signs of a subset of the variables.) For a given counterfactual query, how can your method know whether to predict according to $x_{d'} = x_d$, or according to $x_{d'} = -x_d$? There is no signal in the available data to determine this. Is there an (implicit?) assumption somewhere to rule out cases like this?

Other comments / questions:

* Abstract, "all non-intervened variables have non-intervened ancestors": I suggest "... have no intervened ancestors". The current sentence can be interpreted as "have some intervened ancestors".

* Paragraph before C1-4, "Given our assumption ... distribution equivalence": This is apparently without assumptions (1) and (2), which were stated in the preceding sentence. Please make clearer in the text that you're now considering assuming *only* (3).

* In corollary 3, "Prop. 8" should refer to definition 8.

* Section 3.3: "establish on" should be something else. These sentences should emphasize that you'll now be assuming continuity of $f$ and $g$ (so remove "the" and rewrite). In corollary 5, no requirement of continuity is currently stated, but I think it is needed. Also, just above the corollary, what do you mean with "and not ill-defined"?

### Soundness
3 good

### Presentation
3 good

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
**Post rebuttal update** I maintain my score (and uncertainty) but add my final reply to the author(s). Overall, I think both the original submission and the rebuttal revision are too clustered; the submission has many defs and results, and the revision adds more. 

*Generalized causal mechanisms*

I still cannot understand. I have no problems with “reordering wlog”, however, if there exists a non-invertible subsystem $s$ in an invertible SCM (now Def 1), the reordering only changes the labels of the input nodes of $s$, not the *functional form* of $s$. Did I miss anything? Do you change the functional form of $s$ via $g$? But $g$ is invertible, I do not think we can change the invertibility of $s$ via $g$.

*Rosenblatt transformation*

I still hold my original view. To be clear, I use $J$ to denote the univariate CDFs with fixed conditional values. For a sample $\mathcal{D}$, we have

$$u_2=J_2(x_2):=F_2(x_2|x_1),$$

but, for another sample $\mathcal{D}’$, we have

$$u_2’=J_2’(x_2'):=F_2(x_2'|x_1’).$$

$J_i \neq J_i'$ except for $i=1$.

Or, we say there does not exist a single set of invertible CDFs for all possible values of RV X.

**End update**

This work considers the situation that different domains have the same causal graph but different structural causal functions; the “intervention” in this paper is the “*domain difference of causal mechanisms*”, and the “counterfactual” is the “*domain adaptation of observations*” under a pre-defined domain difference. More specifically, the “intervention” means changing a structural function (from one domain to another) but leaving any other things untouched, and the “counterfactual” means simply the new observation generated by the “intervention”.

An Invertible Latent Domain Causal Model (ILD) is a set of SCMs whose structural functions are invertible and autoregressive plus an Invertible Observation Function which connects the latent and observable. The equivalence class of ILDs is characterized, and it is proved that, for any CLDs, there exist equivalent “canonical forms” whose domain difference is described by the last k structural functions under the topological ordering. Based on this, the paper makes the point that “if we know the number k of different structural functions between the domains, then we can improve the performance”.

There are experimental supports for the effectiveness of the above idea.

### Strengths
It is an interesting idea to see the difference between domains as invertible transformations.

The theoretical analysis seems serious (but it is quite impossible to check the proof in detail as a conference submission). 

If a real-world situation satisfies the theoretical setting, then it is possible to largely reduce the complexity of finding domain differences.

### Weaknesses
 *The idea of “intervention” and “counterfactual” in this paper is nonstandard and confusing*. As standard concepts in causal inference, an “intervention” roughly means setting a variable to a specific value but leaving any other things untouched, and “counterfactual” means imagining an intervention with the *past values* of exogenous variables untouched. In the above, *the structural functions are unchanged*. However, as indicated in my summary, the “intervention” and “counterfactual” in this paper refer to totally different things, in particular, the “counterfactual” does *not* consider the past values of exogenous variables which are the gist of “counterfactual”. Explanations regarding these are necessary, and I strongly suggest *not* using the terms “intervention” and “counterfactual” in this paper. The paper should clearly define what is meant by a “soft intervention” and how it relates to the standard notion of intervention in causal inference. The current explanation is insufficient and needs to be more precise, especially regarding how it differs from a *do*-intervention. Additionally, the paper should clarify how the proposed “counterfactual” relates to the standard counterfactual, particularly concerning the preservation of past exogenous variable values. The lack of clarity on these points makes it difficult to assess the validity and relevance of the proposed framework. 

*The “generalized causal mechanisms” in Prop 2 are only a subclass of “invertible SCMs”*. There is no formal definition of “invertible SCMs” in this paper; I think the definition should be like: writing the whole system of SCMs as X=f(\epsilon) and function f is invertible. In the proof of Prop 2, it assumed that each $\hat{f}^{(j)}$ is invertible. But this is not implied by the general concept/definition of “invertible SCMs” I mentioned above, because there is no guarantee that the *subsystem* involving only $z_{<j}$ is invertible; information from other variables might be needed to invert the whole system, and missing any piece of information might render the subsystems non-invertible. Hereafter, I name this class of models *“invertible autoregressive SCM (IASCM)“*. The core issue is that the invertibility of the overall function $f$ does not guarantee the invertibility of its subsystems $\hat{f}^{(j)}$ when only considering $z_{<j}$. The paper needs to address this by either providing a proof or explicitly stating the assumption that the subsystems are invertible, which is a stronger condition than the invertibility of the overall SCM. The current argument relies on a reordering of nodes, but it's unclear how this reordering can transform a non-invertible subsystem into an invertible one. This needs further clarification and justification.

*The claim on the generality of the model class (Prop 1) seems problematic*. First, here the model class is IASCM. In the proof of Prop 1, the Rosenblatt transformation should be constructed for a fixed *sample point* of p(X), because each conditional CDF F_j should depend on fixed x_{<j}. Thus, we need a Rosenblatt transformation for each sample point, and we cannot construct the F_p and F_q for the whole distributions p(X) and q(\epsilon). The paper's argument that the Rosenblatt transformation can be applied to the entire distribution is incorrect. The transformation is defined for a specific sample point, where the conditional CDFs are evaluated with fixed values of $x_{<j}$. The paper needs to clarify how the Rosenblatt transformation can be used to construct a single invertible function for the entire distribution, rather than a transformation that is specific to each sample point. The current explanation does not adequately address this issue, and it is a crucial point for the validity of the proposed framework.

I have spent 3 hours to get around the confusion in the listed Weaknesses, and I can only skim the rest of the paper and ask some questions as below. *I will read the rebuttal and the revised paper again and update my review accordingly*.

### Questions
*Do we have any ideas on the identifiability of the model*? This is an important question because we discuss causality. Although the theory in the paper converts IASCMs on a set of domains into an easy-to-deal-with form that is the canonical ILD. There are no discussions on the identifiability of canonical ILDs, that is, when we really try to learn the canonical ILDs, can we identify the single eq class of canonical ILDs, which contains the true one? The practical application of the proposed idea depends critically on this question. 

*How can we understand if a practical dataset satisfies the theoretical setting*? Both high-level discussions and examples are highly desirable. For example, for MNIST datasets, how can we understand that the observable (image) is related to the latent by an injective mapping? Why the latent variables in different domains are related by invertible mappings? And in the end, what are the latent variables? Note that I do not require any precise claims on the causal structure (it is latent anyway), but even reasonable “guesses” would be very helpful.

I think the 2nd equality of eq2 is also by definition?

In Def 3, point 3, I am not sure Gaussian exogenous noises are without loss of generality, any references and/or reasonings?

Shared observation function g should be explained right after Def 3.

The claim of “both counterfactually and distributionally equivalent” in Theorem 2 looks strange to me. Can’t we prove that counterfactual equivalence implies distributional equivalence?

There is a related work [1] that is worth mentioning; it also considers invertible causal mechanisms, shared function between domains, and transferability between domains. See Sec 2.3, 2.4 and 3.1 in that paper.

[1] Wu, Pengzhou, and Kenji Fukumizu. "Causal mosaic: Cause-effect inference via nonlinear ICA and ensemble method." International Conference on Artificial Intelligence and Statistics. PMLR, 2020.

Minor

There are two different defs of autoregressive functions, at the end of page 1 and in Def 1. Def 1 seems to be correct.

In Prop 2, generalize → generalized

In Corollary 3, you mentioned “Prop 8”, but I think it should be just Def 8.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on domain counterfactuals: *What a sample would have looked like if it had been generated in a different environment*.
It provides a characterization of *domain counterfactually equivalent* models. They show that sparsity of domain interventions as an inductive bias can help reduce the search space and generate more accurate counterfactuals.

### Strengths
The problem that this work considers has practical significance, e.g., in combining datasets in domains where data collection is expensive.

### Weaknesses
 * I think the writing and structure of the paper can be improved. A large fraction of space is used for many theorems, some of which are not that important. I suggest moving these theorems to the appendix and only keeping Theorem 2 in section 3.2. Furthermore, the simulated experiments look very contrived to me. The data generation mechanism used for creating data in these experiments is too simplistic. It consists of linear transformations followed by a leaky relu (I had to dig into a very long appendix to find this). The model also seems to have knowledge of the precise form of data generation mechanism (linear + relu), and only fits that form.
To me, the interesting experiments come in section 5.2. However, I can't find an explanation of how sparsity is enforced in these experiments. It is unclear whether the sparsity is enforced during training or only during inference, and what specific mechanisms are used to achieve this sparsity. For example, are they using L1 regularization, or are they using a hard thresholding approach? The lack of clarity makes it difficult to assess the validity of the experimental results. Furthermore, the experiments in 5.2 lack sufficient detail regarding the architecture of the VAE used, and the specific choices of hyperparameters. 
In summary, I think authors can restructure the paper to provide more room for experiments in 5.2., and explain the methodology in detail.

### Questions
* How does one set the number of intervention (k)?
* If we don't have the right k, or if the form of the ILD is not precisely known, how off could be our counterfactual estimates? Do we have identifiability in this case?
* How does this work compare with a prior line of work in using sparsity for identifiable representations, e.g., [Synergies between Disentanglement and Sparsity: Generalization and Identifiability in Multi-Task Learning](https://proceedings.mlr.press/v202/lachapelle23a.html) or [On the Identifiability of Nonlinear ICA: Sparsity and Beyond](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6801fa3fd290229efc490ee0cf1c5687-Abstract-Conference.html), just to name a few?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
