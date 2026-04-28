# Out-of-Variable Generalisation for Discriminative Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5

## Abstract
The ability of an agent to do well in new environments is a critical aspect of intelligence. In machine learning, this ability is known as $\textit{strong}$ or $\textit{out-of-distribution}$ generalization. However, merely considering differences in distributions is inadequate for fully capturing differences between learning environments. In the present paper, we investigate $\textit{out-of-variable}$ generalization, which pertains to an agent's generalization capabilities concerning environments with variables that were never jointly observed before. This skill closely reflects the process of animate learning: we, too, explore Nature by probing, observing, and measuring proper $\textit{subsets}$ of variables at any given time. Mathematically, $\textit{oov}$ generalization requires the efficient re-use of past marginal information, i.e., information over subsets of previously observed variables. We study this problem, focusing on prediction tasks across environments that contain overlapping, yet distinct, sets of causes. We show that after fitting a classifier, the residual distribution in one environment reveals the partial derivative of the true generating function with respect to the unobserved causal parent in that environment. We leverage this information and propose a method that exhibits non-trivial out-of-variable generalization performance when facing an overlapping, yet distinct, set of causal predictors. Code: https://github.com/syguo96/Out-of-Variable-Generalization

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates out-of-variable generalization, namely the ability for a predictive model to generalize to target domains in which the agent has never seen the joint variables in the target domain in a single source domain before. Under certain assumptions as well as when these assumptions don't fully hold, the paper shows that the error residual distribution in an environment provides information on the unobserved causal parent variable in this environment, and they use this information to derive an algorithm that performs OOV generalization with source and target domains that have overlapping sets of causal factors.

### Strengths
**Originality**
- As far as I know, though the problem the paper addresses is well-known as a significant problem, the paper provides several theoretical results, mathematical derivations, and supports these with simple empirical results that are novel.

**Quality**
- The quality of the paper is high. It addresses a high-value problem in a principled fashion, shows how certain assumptions help obtain certain results and how and in which cases these assumptions can be bypasses while maintain approximately accurate results, and evaluates these cases in terms of loss accuracy as well as sample complexity of its approach versus baseline approaches.
- The paper openly highlights limitations in its work, such as assumptions made for theorems to hold, and proposes prospective future work in multiple avenues. This refreshingly is (1) included at all and (2) doesn't seem like a mere afterthought.

**Clarity**
- The paper is mostly clear in its explanation of motivation, preliminaries, approach, baseline usage, results, and limitations.
- The paper does a great job providing simple, clear real-world examples to elucidate the problem and applications of the various theorems included in multiple cases.

**Significance**
- The significance of the problem the paper addresses is high and the problem is ubiquitous. The approach is promising and can be applied in many real-world settings through Monte-Carlo sampling or similar methods. The paper shows that their approach can perform relatively well in "few"-shot settings though this depends on the number of variables involved and the complexity of the problem.

From what I can tell, this is excellent work that I hope motivates further addressing this *out-of-variable* generalization problem by the research and applied AI community. My only reservation is my limited knowledge on the understanding of and state-of-the-art theoretical and applied approaches addressing this problem.

### Weaknesses
 - Referring to Figure 1, in the first paragraph in page 3, the claim "it would seem all but impossible...(orange box)" could be better explained. Specifically, it's unclear why the inability to observe $Y$ in the target domain makes the problem 'all but impossible' without further context. The argument relies on the idea that without observing the joint distribution of all causal factors in the target domain, it's difficult to infer the effect of the unobserved variable. However, this could be made more explicit by detailing the specific challenges in estimating the conditional distribution $P(Z|X)$ when $Y$ is unobserved, especially in the context of potential confounding effects.
- In Figure 1, it is unclear whether "With $Y$ not observed in the target domain" is an assumption made or is somehow indicated in the diagram or earlier in the paper. Eventually I realized that it's an assumption made, but the illustration Figure 1a alone isn't enough to show this assumption. This ambiguity may clear for some or compound for some later in Section 3. The diagram could be improved by visually distinguishing between observed and unobserved variables, perhaps using dashed lines or different colors for the unobserved $Y$ in the target domain. This would immediately clarify that the absence of $Y$ is a key assumption of the problem setup, rather than a consequence of the data generating process itself.

### Questions
- The abstract states "merely considering differences in data distributions is inadequate for fully capturing differences between learning environments." Doesn't out-of-variable technically fall under out-of-distribution, so shouldn't this be adequate? Perhaps more specificity is needed here.
- The abstract states "Mathematically, out-of-variable generalization requires the efficient re-use of past marginal information..." Why does it require efficient re-use? Could it work with "non-efficient" or inefficient re-use?
- On page 2, should "modal" be "model?"
- On page 6, do you mean "parentheses" instead of "brackets" between Eq (9) and Eq (10)?
- Why is the joint predictor considered an oracle predictor if MomentLearn outperforms it?
- Could you explain why MomentLearn is reliably more sample efficient than the oracle predictor for "few"-shot prediction?

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
This paper describes the out-of-variable OOV problem, which in its simplest form, aims to learn a predictor Y = f_t(X2, X3) given an OOV predictor Y = f_s(X1, X2) and a dataset (X2, X3), but without any instance of (X2, X3, Y). The authors describe the setting in which this is possible and develops an algorithm. The key observation is that the third moment of the residue Y - f_s(X1,X2) contains information about X3 that is least polluted by the noise.

### Strengths
- The key observation/discovery is clever, and the algorithm is straight-forward to use.
- The writing is clear, clean, and well-referenced. The examples also made things concrete and easy to follow.
- The rigor and simplicity of the work can act as a foundation to build OOV research.

### Weaknesses
 - The main weakness is the applicability of the method. The authors only showed results for proof-of-concept, not for real-world usage. 
- It is unclear how one could identify whether the assumptions are satisfied given a dataset.
- It is unclear how bad the predictor would be if the assumptions are not satisfied.
- It is not yet clear what realistic problem can be well modeled by OOV generalization.

### Questions
Intro:
- It seems OOV fits very well the frame of missing-not-at-random and covariate-dependent missingness. Could the authors comment on that?

Section 2:
- Theorem 2 is slightly confusing for me at first glance because I thought PA_Y by definition includes all parents of Y (so x1,x2, x3 in the example) and not just those in the target environment (x2, x3). It may be helpful to clarify.

Section 3:
As I am trying to get a sense of the restriction and applicability of the approach, I was wondering the following questions: 
- How does the method fair with the oracle as the magnitude of the noise increases? 
- What if the noise is not gaussian but more heavy tailed? 
- Does the performance degrade or improve with increasing number of variables? 
- I assume Theorem 3 does not apply to discrete variables because of the violation of differentiability; is that right?

Section 4:
- Can include missing-not-at-random imputation and covariate-missing imputation as two more baseline models (a search in Google scholar using the two key phrases yields some methods).
- It would be really interesting if the authors could find some real-world datasets, create source and target environments by sub-setting the columns, and see how the method performs.
- Figure 3: I don’t quite understand the figure. It would be helpful to define OOV loss, be explicit about the number of samples on the y-axis being (x2,x3,y) or (x1,x2,y) or something else. I also don’t understand why relative loss is zero means the method is on par with the oracle predictor. Why not just show how the fine-tuning error compares with oracle training, which seems easier to interpret? Anyway, I am overall a bit confused about the figure, so my questions may not make sense.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work investigates out-of-variable (OOV) generalization, which is a sub-problem to OOD generalization, and refers to scenarios where an agent needs to generalize to environments containing variables that were never jointly observed before. The paper shows that if the source and target environments contain some overlapping variables (and under certain conditions), information from the predictor in the source environment can improve predictions in the target environment. More specifically,  the moments of the residual distribution from the optimal classifier in the source environment can be used to calculate the generating function with respect to the unobserved variable in the target domain.

Based on this observation, the paper proposes a practical algorithm for OOV prediction, evaluates its performance, and compares it against the marginal predictor and imputed predictor, as well as an Oracle predictor.

### Strengths
The paper proposes a new and important problem-setting - OOV generalization, which can occur in real-world situations, on its own or alongside OOD aspects. The work also provides an extensive study of the identification problems of various variants of OOV scenarios, including theoretical proofs and examples. 

In addition, the paper proposes a practical algorithm to solve several OOV scenarios that achieves non-trivial OOV transfer on synthetic data.

The ideas presented in the paper are novel and the conclusion that information from source domains can be used for prediction in the target domain in this setting is important, and can potentially have a broad impact on future research in the field.

### Weaknesses
The main limitation of the paper is that the proposed approach was tested on only synthetic data, and was not validated using more challenging datasets. While the synthetic data allows for controlled experiments, it does not fully capture the complexities of real-world scenarios where the underlying data distributions are often more intricate and noisy. The absence of validation on established benchmark datasets limits the generalizability of the findings and raises questions about the practical applicability of the proposed algorithm.

In addition, the extension of OOV in multi-environments is mentioned mainly in the appendix and the algorithm was not tested empirically for that extension. This lack of empirical validation for the multi-environment setting is a significant gap, as it is unclear how the proposed method would perform in more complex scenarios with multiple source and target environments. The theoretical framework is presented, but without empirical support, it is difficult to assess the robustness and effectiveness of the approach in such settings.

### Questions
I would like to ask the following questions:

1. For future work, is there a more complicated/realistic dataset to validate the algorithm?
2. Is it possible to compare the algorithm to state-of-the-art marginal or causal methods such as Mejia et al. (2021) or Janzing (2018)? To validate if Vapnik’s principle holds and whether the proposed approach indeed improves results due to solving a less general problem.
3. Theorem 3 connects all moments of the residual distribution to the partial derivatives with respect to the unique variable of the target environment. If additional moments were to be calculated as part of the proposed algorithm, would it improve results (for the general function case)? 
4. In general, since the paper's main claim is that in the real world, it is likely to encounter both aspects of OOD and OOV - How simple is it to combine state-of-the-art  OOD methods with the proposed approach? I cannot imagine at the moment a straightforward way to do that.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces out-of-variable (OOV) generalization, which is an the ability to generalize in environments with variables that have never been jointly observed before. OOV is an issue in settings where different variables (e.g. diagnostic tests) are available for different environments (e.g. different patients). The paper investigates challenges for common approaches when faced with the OOV problem, and proposes an OOV predictor that leverage moments of the error distribution. The work contributes to theoretical understandings of OOV and offers a proof-of-concept for a predictor capable of non-trivial OOV transfer.

### Strengths
- The paper formally studies a new perspective on generalization.
- The methods employed in the paper are sound.

### Weaknesses
 - The paper does not demonstrate the practical applicability of the concept of OOV generalization, and the setting feels a bit contrived. Also it seems like OOV generalization can be thought of just a case of OOD generalization--if we think about all the variables together as the input, the OOV generalization is just a case of OOD generalization (e.g. covariate shift) where some inputs have clear signal from some features and other inputs have clear signal from other features. 
- It would be helpful to include more intuitive discussion throughout the paper providing more analysis on the sections. For example, more discussion on the assumptions of the settings/theorems would be helpful, and it's not clear exactly under what assumptions the proposed predictor is appropriate.

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
