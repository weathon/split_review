# EXAGREE: Towards Explanation Agreement in Explainable Machine Learning

- Decision: Reject
- Scores: 3, 1, 3, 1

## Abstract
Explanations in machine learning are critical for trust, transparency, and fairness. Yet, complex disagreements among these explanations limit the reliability and applicability of machine learning models, especially in high-stakes environments. We formalize four fundamental ranking-based explanation disagreement problems and introduce a novel framework, EXplanation AGREEment (EXAGREE), to bridge diverse interpretations in explainable machine learning, particularly from stakeholder-centered perspectives. Our approach leverages a Rashomon set for attribution predictions and then optimizes within this set to identify Stakeholder-Aligned Explanation Models (SAEMs) that minimize disagreement with diverse stakeholder needs while maintaining predictive performance.  Rigorous empirical analysis on synthetic and real-world datasets demonstrates that EXAGREE reduces explanation disagreement and improves fairness across subgroups in various domains. EXAGREE not only provides researchers with a new direction for studying explanation disagreement problems but also offers data scientists a tool for making better-informed decisions in practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper titled "EXAGREE: Towards Explanation Agreement in Explainable Machine Learning" addresses the challenge of explanation disagreement in machine learning. Explanation disagreement, where model explanations diverge based on methods, models, or stakeholder expectations, hampers trust and transparency in high-stakes environments. The authors propose a framework called EXplanation AGREEment (EXAGREE) that utilizes a Rashomon set—multiple models with similarly good predictive performance—to align explanations with diverse stakeholder expectations. By optimizing within this set, EXAGREE identifies Stakeholder-Aligned Explanation Models (SAEMs) that reduce disagreement while preserving predictive accuracy.

The authors formalize four types of explanation disagreement: stakeholder, model, explanation method, and ground truth disagreements. EXAGREE addresses these by introducing a two-stage process: Rashomon set sampling, followed by SAEM identification. Empirical analyses demonstrate that EXAGREE reduces explanation disagreements and improves fairness across datasets, positioning it as a potentially valuable tool for practitioners aiming to enhance trust and fairness in machine learning applications​.

### Strengths
- The paper addresses a critical challenge faced by researchers and practitioners: how to proceed when even explainable AI tools disagree on feature importance. Additionally, it incorporates model and stakeholder rankings, making the approach quite comprehensive.
- The paper tackles its proposed problem by integrating methodologies from several different areas, including the XAI literature as well as general AI methods for optimization challenges.
- The insight to make the process end-to-end differentiable is both creative and practically useful.
In the appendix, the authors demonstrate the impact of the choice of $\epsilon$ on the Rashomon set, which serves as a valuable methodological sensitivity analysis.
- The empirical results test their methods across a variety of settings: 6 OpenXAI datasets, both synthetic and empirical; and 2 pre-trained models (logistic regression and artificial neural networks).

### Weaknesses
The paper integrates several methods and techniques to address the explainability disagreement issue; however, it can feel somewhat dry and lacks the depth and technical details that would enable readers to fully appreciate the contributions and identify strengths and weaknesses. Technical jargon used to describe the methodology needs precise definitions, mathematical arguments should be clearly defined and explained, and additional background information would offer useful entry points for readers. Most of the following points align with this suggestion. This lack of precise definitions also contributes to my limited confidence in the recommendations, as it made it challenging to fully assess the work's potential impact.
- The loss functions for $L_{sparsity}$ and $L_{diversity}$ are not defined clearly in the paper or the appendix.
- Precise mathematical definitions of what a mask is and how it is derived are essential for readers to understand the methodology in depth, as this concept is central to the approach. Without a clear definition of how these masks are generated and what their mathematical properties are, it's difficult to assess the validity of the optimization process. For instance, are these masks binary, continuous, or something else? How does the mask relate to the model's parameters, and how does it affect the attribution? The paper should include a formal definition of the mask, including its dimensionality, constraints, and relationship to the model's architecture.
- Consider adding a sentence or footnote to define core terms in your algorithm, as these abstract concepts can vary in meaning:
    - "attribution set", "model representations", "model characterizations", "end-to-end optimization".
    - For instance, in the sentence "Training a Differentiable Mask-based Model to Attribution Network (DMAN) that maps feature attributions from model characterizations for use in the next stage," it would be helpful to clarify precisely what “model characterizations” entail. Are these model weights, activations, or something else? How are they extracted and processed? A concrete definition is needed to understand the input to the DMAN. Also, in Equation 4, where $f_{DMAN}^*$ is defined as the optimal surrogate model in the Rashomon set that describes feature attributions, it appears to be the loss between $f_{DMAN}$ and a set comprising ${\text{masks}, \text{attributions}}$. Minimizing the output to such abstractly defined elements would benefit from more clarity. What is the precise mathematical form of this loss? How are masks and attributions combined in the loss calculation?
- It would be helpful to include insights or references for the result in row 196. Why is faithfulness proportional to agreement? Is this a theoretical result, an empirical finding from the paper, or something else? If it is a theoretical result, a proof or a reference to a proof is needed. If it is an empirical finding, more details about the experimental setup and the data used to derive this conclusion are needed.
- Figure 1 provides few entry points for readers and doesn’t seem to aid in understanding at its current placement. Consider either removing it or adding more descriptive captions to clarify each step (similar to Figure 2, which includes more context). Suggestions include captions for the rankings, lightbulb, etc. Additionally, why are stakeholders grouped together in the first half but not in the second half?
- Figure 2 is clear, but it seems to appear too early in the paper. Moving it to the end of Section 3 might make it more helpful, as readers would have more context to interpret it.
- Is the fairness improvement an explicit objective of the EXAGREE model? If so, please explain the rationale and mechanism. If it’s an outcome of the empirical analysis, please clarify this in the paper, as empirical results may not generalize across all applications. If fairness is not an explicit objective, then the paper should be careful not to overstate the fairness results, and should provide a more detailed analysis of why fairness is improved in the experiments.
- In row 276, in the explanation of the "Ranking Supervision and Correlation Metric," it would be beneficial to provide more context and motivation for this metric and how it fits in the big picture of your methodology before defining it. Why is Spearman's rank correlation chosen over other correlation metrics? What are the specific advantages of using it in this context? How does it relate to the overall goal of explanation agreement?

### Questions
Specific suggestions (please feel free to disregard these if I’ve misunderstood something):
- Typo in row 480: “Rashomon” is misspelled.
- Possible typo or confusion in row 340: “We utilized two pre-trained models,” but immediately afterward, three model types are mentioned.
- Readability suggestion: Consider defining $f_{diffsort}$ (f_{diffsort}) as $f_{\text{diffsort}}$ (f_{\text{diffsort}}) for readability and saving space in equations?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper addresses the problem of explanation disagreement (or explanatory multiplicity), where (post-hoc) explanations of a given machine learning model conflicts with one another. The authors propose a new framework called EXAGREE to find a model, stakeholder-aligned explanation model (SAEM), that provides explanations (feature attribution rankings) in accordance with stakeholder desiderata.

### Strengths
The technical framework of end-to-end optimization problem which involves constructing the Rashomon set, DMAN, sorting networks and multi-heads architecture is interesting.

### Weaknesses
However, this paper should be rejected because:
(1) it is built on weak understanding of explainability
(2) there is a weak connection between "explanation disagreement" and the solution
(3) has questionable experiment design and metrics without sufficient justification
(4) it is unrefined

My biggest concern is that the paper uses local explanatory models (i.e. LIME, Integrated Gradients) to generate global (model-level) explanations. In Section 2.3, the authors mention that they have adapted feature attribution methods for local explanations "by averaging feature attributions across all instances to obtain global attributions." These methods were not designed to be used this way. Although SHAP does have functionality to provide model-level feature attribution, it takes an average of the **absolute** attribution across instances.

My impression of the paper's proposed solution, EXAGREE, is that it attempts to address "explanation disagreement" by finding a model that aligns with stakeholder expectations (i.e., based on domain knowledge) through examining its post-hoc explanation. There is one critical assumption here: the post-hoc explanation is faithful to model behavior --- something we cannot take for granted (see e.g. [Adebayo et al. (2019)](https://arxiv.org/abs/1810.03292)). Besides, I don't think the solution addresses the problem of "explanation disagreement", but is rather a model-selection tool using post-hoc explanations. I see that there are two cases of "explanation disagreement" (both of which is mentioned in the paper):
1. Models with similar performance give different explanations (explanation method fixed)
2. Explanation methods provide different explanations for one model (model fixed)
EXAGREE addresses 1 to an extent but not 2 --- the paper does not make this clear. The authors seem to suggest that the "stakeholder centric" approach can address complex disagreements (Section 2.2). But I don't see how it addresses case 2.

Moreover, I am not convinced that "higher agreement between rankings implies greater faithfulness". Bad actors might want explanations that hide the discriminatory nature of their models, hence want features to be ranked a certain way. In fact, several works have highlighted that explainability methods are prone to manipulation:  [Slack et al. (2020)](https://arxiv.org/abs/1911.02508), [Aivodji et al. (2019)](https://proceedings.mlr.press/v97/aivodji19a.html), [Goethals et al. (2023)](https://arxiv.org/abs/2306.13885). Explainability methods are tools to gain insight into a model (to potentially build trust) not project our desired belief upon the model.

As a result, the metrics, which are based on an unsubstantiated assumption that agreement $\implies$ faithfulness, and the empirical results fall short of achieving the goals outlined in the introduction: to identify models "that provide fair faithful and trustworthy explanations."

The experimental design uses the "ground truth" explanation, the coefficients of the LR model, as "stakeholder needs." It is inappropriate to compare this to the explanations of the ANN model. I do not understand why we would want ANN model explanations to agree with LR explanations. Note that this is quite different from what [Agarwal et al. (2022)](https://arxiv.org/abs/2206.11104) did in their experiments. The experiment setup in general is quite confusing.

In line 463, the discussion regards explanation methods as "stakeholders". I question whether it is appropriate to frame it this way as it is difficult to imagine a stakeholder wanting rankings "like LIME".

Furthermore, the paper in its current state does not seem refined. The authors introduce the problem of explanatory multiplicity but do not make an effort to elaborate on how and why it hinders trust in the model (what about the explanation method?). Also, figures 1 and 2 are not helpful in improving the readers' understanding of the EXAGREE process. Figure 1 is especially confusing regarding what it is meant to portray.

### Questions
- Section 2.3 describing the metrics should be integrated into the experiment section.
- Is $\psi$ fixed in the optimization problem?
- Line 233-4 "which allows us to transform single attribution values into ranges" -> how? (I know its in the appendix right now, should be in the main body)
	- And why is this an important point to raise?
- Line 469-472: I don't quite understand the significance of this "crucial insight."
- Experiments: what is the $k$ value? I can't seem to find this parameter.
- Neither the discussion nor the figure caption explain what is going on in the figures, what it means and its significance.
- Is there code to reproduce the results?

Nitpicks
- The remarks should be paragraphs. If the authors want to emphasize on a point, the remarks should be more concise.
- 2.3 Evaluation Matrices -> Metrics
- Might want to switch to active voice on some of the sentences

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper begins with an implicit premise that there exists an ideal model explanation for a given set of model predictions. Given this kind of explanation obtained from an oracle, the paper presents an algorithm to select a model from a Rashomon set of models that matches the expected explanations. The paper terms this as an SAEM (stakeholder aligned explanation model). "Explanation model" here does not seem to refer to an explanation method, but a predictive model (one picked from the existing Rashomon set) that best matches the explanations desired by a stakeholder.

### Strengths
The scientific contribution presented in the paper is valid and interesting. The proposed method has the means to create machine learning models that can produce explanations that match an arbitrary ideal. The paper presents a new, model-agnostic method to accomplish this, which would be a meaningful and important contribution to the field.

### Weaknesses
The paper’s formalization of four types of disagreements lacks sufficient motivation and clarity, especially in comparison to the foundational work it draws from. For example, the classification of "model disagreement" as a type of "explanation disagreement" is unclear - different models that produce the same predictions can indeed have different internal mechanisms of doing so - in this case explanations should disagree and illuminate this fact rather than obscure it. This notion aligns with the concept of Rashomon sets, where multiple models with similar predictive performance can have significantly different decision boundaries. I encourage the authors to clarify their rationale for categorizing model disagreement within the explanation disagreement framework and to elaborate on how their approach handles cases where differing explanations for similar predictions might reveal essential model behaviors rather than obscure them. There is no "model disagreement" problem.

The paper's contributions then are better studied and understood in the context of a related line of inquiry about adversarial attacks and explanation fairwashing, such as Slack et al (https://doi.org/10.1145/3375627.3375830). The primary problem addressed appears to involve modifying the explanations produced by a Rashomon set of models to align with a predefined set of explanations from an external oracle. This connection is effectively illustrated, though not explicitly addressed, in Table 1, where metrics such as FA, RA, SRA, and others are reported for the ANN model. Notably, the original OpenXAI benchmark (Agarwal et al.: https://dl.acm.org/doi/10.5555/3600270.3601418) does not provide ground truth for ANNs. What this paper does (I think) is use the LR coefficients as ground-truths to measure metrics such as FA, RA, SRA, etc against a **different** model - an ANN! I recommend the authors clarify their novel approach to calculating these metrics for the ANN model and discuss the ethical implications of aligning ANN explanations with LR model coefficients.

Finally, the paper’s entire framing around "explanation agreement" (motivated in Section 2) could be made clearer. Rather than resolving "model disagreement," the proposed SAEM approach seems to modify model explanations without altering predictive accuracy, which could be viewed as a form of adversarial attack on explanations. I encourage the authors to address how this approach contrasts with adversarial manipulations of explanations (if at all), discuss potential connections to explanation fairwashing, and consider any ethical implications that arise from intentionally adjusting explanations while maintaining predictive outputs. What is presented in this paper as an SAEM to resolve the apparent "model disagreement" class of explanation disagreement problems is essentially a means to make the FIS score for the ANN model to match the coefficients from the LR model trained on the same data - this is an adversarial attack.

### Questions
It would be good for the paper to define terms such as "explanation model" before using them (it is possible that I've misunderstood this term in my review). There seem to be other consistency errors that could elevate the writing and clarity. For example, Table 1 has a model class and explanation method in columns 1 and 2, under the common heading method. However the last row has "decision trees" listed as an explanation method (my understanding is this should be a model - in which case what is the explanation method used?).

The figures 1 and 2 were similarly unclear to me - the symbols used were not explained (what do the curved arrows represent? what is the lightbulb? what do the question-mark and check-mark mean respectively?) and did not help with my understanding. These could be omitted entirely in my opinion without any impact on the papers clarity.

Most critically though, perhaps the paper needs to dispel the notion of promoting a nebulous notion of "explanation agreement", as motivated in section 2, and recognise the algorithm for what it does - produce models that can maintain predictive accuracy while generating explanations that can match different ones. The paper is thus not resolving "model disagreement", but introducing an adversarial attack that maintains predictions and modifies explanations.

To reiterate, I think the method is good and the contributions are interesting and valuable, but I think the framing of "explanation agreement" can be replaced with a "adversarial manipulations of explanations" to clarify the writing.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes to address the problem of explanation disagreement across different models (of same performance on a dataset, called a Rashomon set), and across different explanation techniques. The authors say that disagreement between explanations hurts reliability of the model if and when deployed in high-stakes environment. They propose EXAGREE where they talk about 4 avenues of such disagreement, and propose an approach that **apparently** addresses the problem.

### Strengths
The problem that the paper focuses on is interesting and the paper does a good job at disentangling the four scenarios of explanation disagreement. 

Originality and Significance (of the problem): High
Quality and Clarity: Poor

### Weaknesses
## Review

### summary:
 The paper proposes to address the problem of explanation disagreement across different models (of same performance on a dataset, called a Rashomon set), and across different explanation techniques. The authors say that disagreement between explanations hurts reliability of the model if and when deployed in high-stakes environment. They propose EXAGREE where they talk about 4 avenues of such disagreement, and propose an approach that **apparently** addresses the problem.

### soundness:
 1

### presentation:
 1

### contribution:
 1

### strengths:
 The problem that the paper focuses on is interesting and the paper does a good job at disentangling the four scenarios of explanation disagreement. 

Originality and Significance (of the problem): High
Quality and Clarity: Poor

### weaknesses:
 The paper has a lot of weakness in my opinion and I delineate them as follows. You do not need to address all of them in the rebuttal, I have marked points that are major weakness, you can focus on them. 

1. Starting with Figure 1 on Page 1 -- totally unclear. How does the right side of the figure indicate agreement while the left does not? (this figure is not crucial to understand the paper, but I am just making a point of why the paper is so unclearly written and you do not need to address this point in the rebuttal, there are many more important problems. )

2. [Major] In Section 2 (Preliminaries), there are several mistakes in the formulation:

**a)** M* is not defined in Eq. 1. I assume what you mean is the optimal model by M* (the model with the best performance on the data). 

**b)** a_1, a_2,...,a_p are not defined as features.  

**c)** In Equation 1, I think the sign should be >= instead of <= (the loss of the other models will be higher than M* (assuming M* refers to optimal model)

**d)** Why is $\epsilon$ multiplied by L(M*), usually similar performing models are supposed to be an absolute threshold, not relative to the loss of the original model. 

3. [Most Major] In Section 2.1, you mention 4 axes of explanation disagreement. I am with you on the model and method disagreement, but what does stakeholder and ground truth disagreement mean? 

**a)** In Stakeholder disagreement you mention "Different stakeholders in S might prefer different rankings". Why would that ever happen? Do these stakeholders want something that is not real and want fake explanations that aligns with their mental expectations of what a model should care about? What is an example of such stakeholders wanting something different from reality? Your current example of a data scientist wanting statistical significance and domain expert valuing different features **does not** answer this. Does wanting statistical significance and valuing different features amount to wanting different ranking of features (this also assumes that these rankings won't be same in the first place)? And even if they want different rankings, should a technique be optimized to suit their demands and provide fake explanations? 

**b)** In ground truth disagreement you mention "ground truth interpretations (i think you mean explanations) from interpretable models can conflict with post-hoc explanations" -- yeah this is obvious, but does it matter? If I have an interpretable model, why do I care what a post-hoc technique says, I will never ever use that for such a model? Why would one do that? 

**c)** In the primary objective of the paper you write: "identify a well-performing model that minimizes disagreement (or maximizes agreement) between model explanations and stakeholder expectations. " -- where stakeholder expectation is either something we should not give them because it is fake or something I do not understand. Your rebuttal will help me understand if it is the latter (a solid convincing example is required). 

5. Section 2.3, I think the title of that subsection should be "Evaluation Metrics" and not "Evaluation Matrices". Anyway, in that section you mention two metrics: faithfulness assessment and fairness assessment. In faithful assessment you give a further breakdown in several metrics -- however, most of these metrics seems highly correlated, for e.g., the attribution values directly affect the ranking, so FA, RA, RC, SA, SRA, PRA should have extreme correlation (when you consider the attribution values with its sign). Can you measure this please? If they are highly correlated, then that is effectively one metric and not six. If they are not correlated, can you explain why that is not the case (except the case where you consider the absolute values, its obvious then). 

6. You have used the word "mask" in line 256, without defining, what does it mean? Also in line 259 what does the phrase "bridging the gap between models in Rashomon set and their feature attributions mean" mean? each model in the Rashomon set (or any model for that matter) has a feature attribution (produced by any technique), what is the gap between them -- they don't even lie in the same space, one is in the weight space and other is in the explanation space (they have different dimensionality). 

7. [Major] You have this complicated (and not at all well explained) pipeline of computing SAEM which is basically the models that have the highest agreement with stakeholder requirements. Please tell me why do you need this pipeline? You have the models that are trained on that dataset, you can use that to compute the set of the models that are best performing (according to some threshold $\epsilon$), and then compute the explanations of these models using whatever method you like, and then just give those models to the stakeholders with whom they have the highest agreement. What is the job of the models like DMAN, you are just using that to predict the model that will have the highest agreement (is that a correct understanding of the model's job?), but you don't need that you have the ground truth and you even say this in lines 268-269. 

8. [Major] The above were the problems with the problem setup, now coming to the experiment section. 
**a)** In table 1 you mention k= 0.25, what does k stand for? You have used k and l in Section 2.1 without ever defining them. For the same reason, I do not comprehend what does the k in caption of Figure 3 stand for. 

**b)** Why is SAEM technique bolded in Tables 1 and 2. The standard practice in ML papers to the bold the best performing method, but your technique, and this is misleading. 

**c)** If SAEM selects the models with the highest agreement with the stakeholder, why is it not the best for LR in Table 1 and 2? (especially in Table 2, it is pretty behind techniques that are not optimized for agreement, which alludes to the case that explanation disagreement might not even show up in actual experiments?)  

**d**) how is FIS_LR computed? Is this not just the feature importance and since you are using ground-truth explanations from pre-trained LR, this should have 100% agreement and should be the best 8 number of times (currently in Table 1 it is best 0 times)?

### Questions
I have listed all the questions in the weakness section, the authors can focus on the major problems if they like.

### Soundness
1

### Presentation
1

### Contribution
1
