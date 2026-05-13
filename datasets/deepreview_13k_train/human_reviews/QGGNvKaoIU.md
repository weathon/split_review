# Model-agnostic meta-learners for estimating heterogeneous treatment effects over time

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Estimating heterogeneous treatment effects (HTEs) over time is crucial in many disciplines such as personalized medicine. For example, electronic health records are commonly collected over several time periods and then used to personalize treatment decisions. Existing works for this task have mostly focused on \emph{model-based} learners (i.e., learners that adapt specific machine-learning models). In contrast, model-agnostic learners -- so-called \emph{meta-learners} -- are largely unexplored. In our paper, we propose several meta-learners that are model-agnostic and thus can be used in combination with arbitrary machine learning models (e.g., transformers) to estimate HTEs over time. Here, our focus is on learners that can be obtained via weighted pseudo-outcome regressions, which allows for efficient estimation by targeting the treatment effect directly. We then provide a comprehensive theoretical analysis that characterizes the different learners and that allows us to offer insights into when specific learners are preferable. Finally, we confirm our theoretical insights through numerical experiments. In sum, while meta-learners are already state-of-the-art for the static setting, we are the first to propose a comprehensive set of meta-learners for estimating HTEs in the time-varying setting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes model-agnostic meta-learners to estimate temporal HTE. Specifically, authors address the main challenges of temproal HTE estimation from a unified view. They theoretically analyze when specific learners are preferable over others. They derive inverse variance weights to stabilize the loss of the DR-learner.

### Strengths
1. Authors provided a comprehensive related works section.
2. The problem setting is clear and overall reasonable. 
3. The theoretical analysis is good and comprehensive, although I can't fully check the correctness.
4. The empirical validation is comprehensive too.

### Weaknesses
1. I suggest authors explain their motivation in detail. I believe the current version "Despite the fact that meta-learners are often considered state-of-the-art in the static setting, similar learners for the time-series setting are missing."  is not enough. How exactly meta-learners benefit or fit the time-varying setting? I think the reason: "meta-learners are SOTA under static setting" is not convincing. 

2.  The caption of Figure 1 can be more specific. I suggest authors add some explanation for the edges, for example, why X(t-2) has a direct causal influence on X(t+1)? What is the practical meaning of such causal path?

3. I think some important concepts are not clearly defined. For example, does response surfaces equal response functions? I presume they are the same estimands.

4. I understand the PI-RA-learner, which can be seen as the estimator version of Eq 5. However, can authors explain the pseudo-outcomes (Eq. 8) in detail? When At = at or bt, why the time index of history info (H) is t+1 rather than t?

5. The contribution of methodology may be thin, since I believe IPW estimator for heterogeneous treatment effects or counterfactual outcomes estimation is already proposed by Papadogeorgou et al (2022). 《Causal inference with spatio-temporal data: estimating the effects of airstrikes on insurgent violence in iraq.》 Journal of the Royal Statistical Society
Series B: Statistical Methodology, 84(5):1969–1999.

6. In eq.9, authors define the propensity scores in the time-varying setting. My concerns are about the implementation details about this propensity score. To be specific, the action (treatment) sequence Al, is a high-dimensional variable. So how do authors employ history info Hl to model the probability distribution of this high-dimensional variable? Please clarify my concerns.

7. In the experiment section, I understand authors try to emphasize that their proposed estimators do not rely on any specific model architecture. However, to implement an estimator, one have to choose a network, and I believe different network architectures can have diverse performances. In addition, there may be a best model (e.g. Transformer or Mamba). So I think the contribution of "MODEL-AGNOSTIC" may not be appropriate. 

8. BTW, it seems that authors do not discuss the computation efficiency. I suggest authors add this section in the main text or Appendix.

### Questions
Please refer to "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors study the problem of estimating heterogeneous treatment effects in a time-dependent setting, where the treatment and measured covariates can change at each discrete step of a pre-specified time interval. The authors consider several possible meta-learning strategies for conditional average potential outcome (CAPO) and conditional average treatment effect (CATE) estimation which can be combined with any machine learning estimate of a base nuisance function, and they provide a theoretical analysis of the asymptotic error rate of each method. Based on the limitations of the initially proposed meta-learners, they propose the inverse variance weighted doubly robust learner to reduce instabilities that may arise due to low data availability. Finally, they confirm their theoretical findings and insights on both synthetic and real data.

### Strengths
The problem under study is of high practical relevance. While there has been a great proliferation of data availability in recent years, most of it is observational in nature, and collecting data from strict randomized controlled trials is still expensive. Methods that can take advantage of such data are critical. The time-varying aspect of the problem is also a natural feature of observational data collected "in the wild," making the problem setting even more relevant.
 
The presentation of the technical results is excellent. I am not an expert on causal inference, and the bare statement of one of the main results of the paper (Theorems 1) is highly technical in nature. However, the authors provide helpful interpretations of their results which make the value of the theorem clear. This clarity of exposition can be seen in many other places in the paper:

- An explanation for the lack of equality in equation (3) (failure to adjust for post-treatment confounders).
- An explanation for the constant variance assumption in Theorem 2. I had planned to add a question about this assumption to my review, but the authors addressed it immediately.
- Insight on the weighting mechanism of the proposed inverse variance weighted doubly-robust learner (lines 413-419), especially showing the connection to the simpler but more familiar binary treatment and static (not time-varying) settings.
- Intuition for which methods should be expected to perform best on which synthetic datasets and why.

These additional remarks and insights make the results of the paper far more accessible than they would be otherwise.

The results themselves are also strong. The authors give a theoretical analysis of the asymptotic behavior of each of the studied methods and discuss the implications for when each method should be preferred in practice. They then confirm their theory with synthetic datasets whose qualitative differences mimic some of the possible variation one could encounter when applying these methods in practice. Finally, they also obtain improved performance on real world healthcare data, which is the primary motivating example for the problem under study.

### Weaknesses
While the intuitions that the authors have already provided are greatly appreciated, additional context for some of the quantities used in the paper would be helpful for a non-expert audience. For instance, additional explanation of the nuisance functions in an appendix would be helpful. It would be beneficial to provide more detail on the specific forms these nuisance functions take, and how their estimation impacts the overall performance of the proposed meta-learners. For example, discussing the bias-variance trade-off associated with different estimation strategies for these functions would be valuable. Specific examples of the rate functions used in Theorem 1 for some particular settings would also make the theorem easier to parse. It would be helpful to see how these rates translate into concrete bounds on the estimation error for different choices of base learners, such as linear regression, random forests, or neural networks. Furthermore, it would be beneficial to discuss the practical implications of these rates, such as how they affect the required sample size for achieving a desired level of accuracy.

### Questions
1. What is the precise definition for a regression estimator to admit a particular rate in Assumption 3?

2. The real-world experiment reports RMSE on predicted normalized blood pressure. What is the normalization, and should the results of the proposed method be considered "good" or "bad" in absolute terms (not just relative to the other methods, over which it clearly obtains improvement)? It would be helpful to include an analysis of this sort to indicate where there is still room for future work.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies treatment effect estimation from observational data over a period of time. The observed data contains a (time-varying) covariate, treatment, and outcome at each time point. The proposed methods contain a set of meta-learners designed to be used with any machine learning algorithm as base learners. The meta-learners are specifically designed for four types of confounding adjustment, namely history adjustment, regression adjustment, propensity adjustment, and doubly robust adjustment. In other words, the paper extends existing adjustment methods under the static setting into the dynamic setting. The theoretical bound between each of the proposed estimators and the true effect is given under assumptions that are commonly used in treatment effect estimation. In the experiment section, the paper studied Transformer as one type of learner under one synthetic and the MIMICIII dataset.

### Strengths
This paper's strength is that it provides a good organisation of the existing learners and discusses the meta-learners and their estimation bounds. Although the technique used to prove the bound is not novel, it is nice to see the combination of existing techniques to provide bounds for each of the meta-learner.

### Weaknesses
1. One key weakness is that the experiment section is weak. Currently, the content has only one synthetic dataset and one real-world dataset, and the compared methods only include the meta-learners proposed in this paper. Only one instantiation is experimentally studied for the meta-learners proposed in this paper. I think there should at least be some existing state-of-the-art comparison included, and there should also be other instantiations even for a "proof-of-demonstration" experiment section, especially since ICLR has a tradition of valuing comprehensive experiments.

2. The later sections of the paper are not as well-written as the earlier ones. The latter sections seem rushed, and many sentences are incorrect. For example, "Here, we section outline..." should be this section outline; "proof-of-demonstration" should be proof-of-concept; Making things worse, the paper ended abruptly at section 7. There is not even a conclusion paragraph at the end of the paper.

### Questions
1. One strength claimed by the author is that the proposed learners can be used with "arbitrary machine learning models", and the title also emphasises "model-agnostic meta-learners". However, this is not supported by the empirical evaluation at all. I suggest the authors back up their claim with evidence. Also, some comparisons with different machine-learning models are essential for readers to understand the proposed meta-learner better. In its current form, the paper feels very unfinished. 

2. I think the paper is relatively well-written until section 7. Unfortunately, the rest of the paper seems very rushed, and the content is limited. In the only instantiation using a Transformer, the authors emphasized that the Transformer has not been optimized for the treatment effect estimation and then use quite a bit of space to give the details of their architecture. I think the space can be better used if more experiment results can be presented. The detailed architecture of Transformer can be in the supplementary. 

3. The discussion of results should also be enhanced. Currently, there is only a very brief description of the results of the experiment. There should at least be discussion of the results that can be linked back to the theoretical analysis. For example, in the theorem, it has been shown that the PI-HA learner is asymptotically biased. Still, in the real-world dataset, there are two occasions that PI-HA performs the best and by a significant margin. In fact, except for the IVW-DR-learner, other proposed meta-learners seldom perform better than the PI-HA learner despite the fact that PI-HA is biased while the others are not.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors compare different causal metalearners estimating treatment outcomes over time. They also propose a novel variant of the temporal DR-Learner based on inverse-variance weights. These learners are described and then compared based on a transformer architecture.

### Strengths
The presented metalearners are a novel framework for thinking about these models and, as such, this work constitutes an important contribution to the literature. Given the popularity of metalearners in the static setting, these will certainly have wide applicability. Moreover, given the fast evolution in research on time series modeling, having these model-agnostic metalearners will be very valuable. The presented experiments clearly show the benefits of different approaches, with results corresponding to the hypotheses suggested in the theoretical analysis.

### Weaknesses
1. Several points are not entirely clear to me (possibly due to some misunderstandings):
- If I understand correctly, the challenge of time-varying confounding is different compared to previous work (e.g., CRN). In my opinion, this needs to be stressed more and explained in more detail. Specifically, the paper should clarify how the proposed approach addresses confounding arising from future covariates, which are not accounted for in methods like CRN. The distinction between adjusting for past confounders and the unique challenge of post-treatment confounders needs to be more explicit.

- Some parts of the methodology are not entirely clear (see questions).

- The notation is not always clear to me (see questions).


2. There is no conclusion, or a discussion of limitations and possible directions for future work.

### Questions
- I am not sure whether I understand the implications of eq. 3. The authors claim that other methods, such as CRN and CT, do not correctly adjust for this bias. However, as they build an unbiased representation iteratively in each step (based on $\bar{H}_t$), it seems to me that future covariates get added correctly, and no bias should exist?

- Do the learners with different estimands (e.g., nuisance parameters) use separate models for each, or are they built in a multitask framework? While a multitask framework is sensible for transformers, it does not apply to time series models generally.

- Do you use sample splitting in the experiments? 

- Having CAPO as $\mu$ and CATE as $\tau$ would be more clear in my opinion, though I leave this up to the authors. Later, $\mu$ and $\delta$ are also introduced, though they seemingly refer to similar estimands. What is the reasoning behind this notation? 

- The RA-Learner is much more complex than its static variant, where only the final term in Eq. 8 is present. Some intuition here would be appreciated.

___

**Minor points:**
- Line 290: "major different" -> difference

### Soundness
4

### Presentation
3

### Contribution
3
