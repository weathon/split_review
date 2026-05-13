# Feature Responsiveness Scores: Model-Agnostic Explanations for Recourse

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Machine learning models are often used to automate or support decisions in applications such as lending and hiring. 
In such settings, consumer protection rules mandate that we provide a list of ``principal reasons'' to consumers who receive adverse decisions.
In practice, lenders and employers identify principal reasons by returning the top-scoring features from a \emph{feature attribution} method.
In this work, we study how such practices align with one of the underlying goals of consumer protection -- \emph{recourse} -- i.e., educating individuals on how they can attain a desired outcome.
We show that standard attribution methods can mislead individuals by highlighting \emph{reasons without recourse} -- i.e., by presenting consumers with features that cannot be changed to achieve recourse.
We propose to address these issues by scoring features on the basis of \emph{responsiveness} -- i.e., the probability that an individual can attain a desired outcome by changing a specific feature.
We develop efficient methods to compute responsiveness scores for any model and any dataset under complex actionability constraints.
We present an extensive empirical study on the responsiveness of explanations in lending, and demonstrate how responsiveness scores can be used to construct feature-highlighting explanations that lead to recourse and to mitigate harm by flagging instances with fixed predictions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the limitations of feature attribution methods in decision-making scenarios where regulations mandate that individuals are informed of the principal reasons for adverse decisions. Existing methods often highlight important features without considering whether those features can actually be changed to achieve a desired outcome, thereby failing to provide actionable recourse.
The authors propose a new method for scoring feature responsiveness, which evaluates the likelihood that changing a particular feature can lead to a favorable model outcome.  The authors conducted an empirical study in consumer finance, demonstrating that their responsiveness-based approach more accurately identifies features that offer actionable recourse, flagging instances where standard methods provide “reasons without recourse.” They also release a Python library to support the implementation of feature responsiveness.

### Strengths
1. The paper effectively highlights a critical shortcoming in the use of feature attribution methods for generating explanations. By demonstrating that standard methods often provide non-actionable reasons, the authors reveal a key limitation that could undermine the intended goals of explainability and consumer protection in high-stakes applications.

2. The introduction of responsiveness scores offers a novel/nuanced approach to measuring "actionability." These scores help flag instances where individuals cannot achieve recourse, thereby preventing the issuance of misleading explanations and enhancing the practical value of model explanations.

### Weaknesses
(1) While I find the concept of feature responsiveness quite interesting, the contributions of this paper appear marginal, particularly in light of the work [1]. This paper draws upon existing ideas introduced in [1], such as the notions of reachable sets and action sets, which are used for recourse verification there (i.e., determining if an individual can achieve recourse through actions in the feature space). In [1], the approach returns a binary output: 1 if there exists an action that achieves recourse (feasible) and 0 if no such action exists (infeasible). In contrast, this work provides a probabilistic measure by assessing the fraction of actions on a feature that leads to recourse. Although the responsiveness score method offers a more nuanced probabilistic view, the framework in [1] could also be adapted to identify unresponsive features effectively. For example, the experiment of Table 3 (Recourse feasibility....) is similar to Table 2 in [1].

To improve the contributions, I would like to see this work go beyond identifying unresponsive features or "actionability" of features to leveraging the responsive score to produce better explanations. For example, can we leverage this responsiveness score to produce feature attribution methods that return more actionable features? Or when finding recourse (or counterfactual explanations) can we leverage the responsiveness score to find more actionable recourses? 

(2) Generally, I also believe your method can go beyond checking the responsiveness of top-k features from a feature attribution method. You can also extend this to various recourse generation methods, counterfactual explanations, or any feature explainability methods.

(3) I challenge the assumption that feature attribution methods should necessarily provide actionable recourse. Attribution methods and recourse methods are fundamentally different types of explanations, each with distinct purposes and applications. While feature attribution methods are designed to identify and communicate the features that most strongly influence a model’s prediction, they are not inherently designed to satisfy an "actionability axiom". This distinction is important because blending the goals of feature attribution and recourse may lead to confusion and misaligned expectations. The paper might benefit from a brief discussion on this but I don't think the premise of "feature attribution method should be able to provide recourse" needs to be true. 


(4) The definition of responsive score as a probability is a bit confusing as there is no random variable or distribution. It might be more precise to define the responsive score as a fraction or proportion. To accurately define responsive score as a probability you would need to properly characterize your sample space, probability measure, and events.

What if two features are individually irresponsive, but when considered together can be responsive (and can provide a recourse)?  

(5) The responsiveness score does not consider the ease or difficulty of implementing certain actions, which is a crucial factor from the user's perspective. For instance, actions that are relatively easy to undertake, such as increasing a credit score by 2 points, should carry more weight than more challenging actions, increasing a credit score by 20 points. A weighted version of the responsiveness score, which factors in the feasibility or effort required for each action, could offer a more user-centric measure. This might better capture "user responsiveness" rather than a uniformly distributed action space.  For instance, what do you do when a feature is continuous and unbounded (e.g., income feature)? 

  
minor --
Increase the text font size of Figure 1 for clarity.

### Questions
Address questions in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a new concept within interpretability of ML models, focusing on explanations for recourse. Even though the approach is specially proposed, developed and discussed within the context of lending, I believe it has general applicability for a broader set of problems. Basically, instead of considering shapley values or other concepts to assign a contribution/importance to some input feature, it concentrates instead on assessing sensitivities of the forecasts to changes in the features. These features that could be changed are seen as recourse. While the idea is very simple, and could be seen as a simple sensitivity measure, I believe it can be a very understandable and powerful approach to convey information that would support interpretability much better than Shapley values, for many applications.

### Strengths
I clearly agree with the starting point of the paper, aiming to focus on another view of interpretability, where for a number of applications, only features that are actionable are relevant, while one would be interested in seeing how different outcomes may be if values for these features would change (even slightly). It is crucial to go away from thinking that Shapley values (and other similar approaches) are the go-to approach to bring interpretability to ML. Here, the approach is described in a rigorous and pedagogical manner. The concepts and main measure proposed (in Definition 4) are simple yet powerful. The methodological contribution is sound, original and valuable. Personally, I enjoyed reading the paper and it made me think about a lot of potential use cases and extensions.

### Weaknesses
In my view the only weakness of the paper is that it only concentrates on a given application area, while it could have been interesting to consider the ideas and concepts in the paper in a more general framework.

### Questions
I do not have any specific point or question to the authors.
Possibly, if they could try to discuss their approach in a more general context (i.e., envisaging what could be done for other application areas) at various stages of the paper, it could make it stronger.

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
4

### Summary
This work studies feature attribution and its relationship to recourse. It demonstrates that many feature attribution techniques do not highlight features that can lead to recourse, i.e. these methods do not identify features that if an individual were to change them, the model. prediction would be different. This work then addresses this issue by proposing a way to score features on the basis of responsiveness – i.e., the probability that an individual can attain a desired outcome by changing a specific feature. The paper presents efficient methods to compute such scores and demonstrates via experiments that their proposes responsiveness scores highlight features that can lead to recourse.

### Strengths
1) I believe this paper aims to address a very important problem with current feature attribution methods, that is, the features these methods identify as important are rarely those that can be modified/changed so that a different prediction may occur. 

2) I believe the idea of action and reachable sets is an interesting one and I appreciate the authors trying to make these notions precise via theory.

3. The paper performs numerous experiments to demonstrate their result

### Weaknesses
1) I don't particularly think this work is very novel. There has been numerous works that propose counterfactual feature attribution methods, i.e. those that identify important features as the ones that, when changed, lead to a different prediction. Are these not pretty much responsiveness scores in the language of this paper. I advise the authors to take a look at these papers and address how their proposed notion of responsiveness is different than the notions proposes in the following works

https://proceedings.mlr.press/v162/dutta22a/dutta22a.pdf
https://arxiv.org/abs/2409.20427
https://arxiv.org/pdf/1912.03277

The beginning of the 3rd page of the first paper [Dutta et al 2022] in fact list many works that focus on develop feature importance scores that identify important features as those when changed, lead to a different prediction

2) How are the actionable sets defined exactly? To be correct the only way to properly understand model behavior is to see how its predictions change while modifying features such that the new feature vector x' still comes from the same distribution that the original feature vector comes from. This is because the model was trained on samples from this distribution and so to evaluate how it performs on samples that may not make sense does not make sense to me. Is the reachable set trying to capture all "feasible" ways that we can change the feature vector? How do identify this reachable set?

3) Overall I have concerns on the novelty and limited impact of this work. These ideas have been explored in numerous works and whats outlined in the paper seems to only apply to simple settings with discrete features where its clear what the reachable set is.

### Questions
What is line 96 saying? 
- "By highlighting features that can be changed to consumers who could not attain a different outcome
- I thought current methods fail to identify features that are actionable, i.e. those that could be changed to achieve a different, hopefully desirable outcome? I am not sure what this line is saying.

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
The authors propose feature responsiveness scores to highlight the features that can be changed to receive a better model outcome and assess how feature attribution methods can inflict harm by providing users with reasons without recourse.

### Strengths
The authors propose a novel way of looking at actionability. 
The authors perform comprehensive experiments using three datasets and explainability methods and avail their code.

### Weaknesses
 **Weaknesses and questions**

- There are endogenous and exogenous actionable features. When defining the actionability constraints (e.g., from the way authors define them - table 2 for example), it’s non-trivial to fully capture the relationship between features, especially in a way that reflects varied real-world scenarios. The action set and reachability set might not accurately capture these dynamics. For example, by making age immutable, a user is limited to recourse that doesn’t involve age changing (e.g. figure 2), and in some settings, e.g., education and age, if an individual changes from education:1 to education:3, age changes as well. As a result, the formulation of the responsiveness score might be limited.
- While some features are not actionable, they could be highly predictive and ethical. For example in predicting who is admitted to a K1 class, age is a very predictive feature despite being a sensitive attribute and not being actionable. Similarly, disability is a very predictive feature in predicting eligibility for the Paralympics despite being a sensitive attribute and not being actionable. So although the feature might not be actionable and not eligible for actionable recourse recommendations, if methods like LIME and SHAP attach a high feature attribution score to it, it’s not a negative thing. I think the responsiveness score is context-dependent and the proposed formulation could be stronger with some way of filtering instances where the score is most informative or applicable.
- The reliance on the computation of the responsive score on the reachable set is very limiting. This is because 1) The decision-maker has to define the reachability set based on the action set (which might be limited by the training data manifold and is susceptible to breaking causality and the relationship between features). 2) It’s hard to compute the responsiveness score in cases where features are continuous and sampling might introduce bias that's propagated and exacerbated in the explanation. 3) For methods like LIME or SHAP where the objective is to get a sense of the most important features among a set of features or determine the value of features to the model, defining an action set or individualized recourse might be out of scope. 
- The formulation of actionability and subsequently responsiveness score such that the number of features changed = number of actions taken is rarely the case in real-world settings. For example, while a student might be required to get at least a grade A in class w and at least a grade B in class z, one action might lead to the achievement of both grades (features).
- In addition to the quantitative results (tables and numbers ), it might be helpful to add more qualitative results as well. For example, on page 9, lines 467 to 468, the authors briefly do this.

**Minor  or other observations**

- I think it might be interesting to further investigate the responsiveness score at an individual or instance level. I imagine that in a real-world setting, the responsiveness score might be limited by what actions different individuals have access to, varied user preferences and strengths/circumstances (potentially captured by individual costs), and so on.
- Additionally, in several recourse methods, several alternative sets of actions, e.g., with different costs, or diverse actionable features, are returned, where e.g., in some instances, the least costly is chosen. 
How well or easily is the responsiveness score scalable to this setting? Additionally, how do authors determine sufficient alternatives recourse as cutoff in that case, for example would it be dependent on diversity of the features recommended in recommended varied recourse, or number of alternative recourse, etc?
- Given the dependence on a manual action set definition, the responsiveness score is susceptible to biases and replication or reproducibility challenges. 
- The figures and tables communicate what the authors want to convey. However, the text font is very small. Authors could find ways to increase the font to improve the readability of the figures and tables. 
- Given that only users that have received a negative outcome get recourse, would it be computationally cheaper to more generally bound the reachability set, since the action set is more general -specific to the training set-?
- How does a change in training data distribution affect the feature responsiveness score? 
- The reachability set and responsiveness scores are more likely to leak significant information about the model than the local explanation tools like SHAP and LIME.

### Questions
The questions are integrated with the context in the weakness section. Authors should please respond to the questions added in the sub-section "weaknesses and questions"

### Soundness
3

### Presentation
3

### Contribution
2
