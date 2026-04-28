# Contextualized Policy Recovery: Modeling and Interpreting Medical Decisions with Adaptive Imitation Learning

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Interpretable policy learning seeks to estimate intelligible decision policies from observed actions; however, existing models force a tradeoff between accuracy and interpretability, limiting data-driven interpretations of human decision-making processes. 
Fundamentally, existing approaches are burdened by this tradeoff because they represent the underlying decision process as a universal policy, when in fact human decisions are dynamic and can change drastically under different contexts. 
Thus, we develop Contextualized Policy Recovery (CPR), which re-frames the problem of modeling complex decision processes as a multi-task learning problem, where each context poses a unique task and complex decision policies can be constructed piece-wise from many simple context-specific policies.
CPR models each context-specific policy as a linear map, and generates new policy models \textit{on-demand} as contexts are updated with new observations.
We provide two flavors of the CPR framework: one focusing on exact local interpretability, and one retaining full global interpretability.
We assess CPR through studies on simulated and real data, achieving state-of-the-art performance on predicting antibiotic prescription in intensive care units ($+22\%$ AUROC vs. previous SOTA) and predicting MRI prescription for Alzheimer's patients ($+7.7\%$ AUROC vs. previous SOTA).
With this improvement, CPR closes the accuracy gap between interpretable and black-box methods, allowing high-resolution exploration and analysis of context-specific decision models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes "contextual" policy recovery, a new interpretable method for parametrizing policies for imitation learning to mitigate the interpretability x accuracy tradeoff. The parametrization uses interpretable policy functions for $\pi_\theta(a_t \mid x_t)$ such as a linear class and summarizes historical patient context through the parametrization of this policy class i.e., $\theta = g(x_{1:t-1}, a_{1:t-1})$. The authors demonstrate that this parametrization improves over current imitation learning baselines in terms of the accuracy/interpretability tradeoff. Empirical evaluation in MIMIC (and ICU healthcare dataset for antibiotics treatment) and ADNI MRI scan data for cognitive disorder diagnosis suggests improved tradeoffs. Authors have tried to exhaustively interpret the results from both datasets.

### Strengths
1. Interpretability of learned offline RL policies is crucial for safety of implementation in applications such as healthcare. Authors are trying to improve the accuracy interpretability tradeoff by proposing a new parametrization of the policy class.

2. The paper is well motivated and the presentation makes the contributions clear

3. Detailed empirical evaluation of healthcare data, which seems like the main application area of interest, is presented. 

4. I think Figure 7 is the most informative in terms of understanding how contextualized policy recovery helps without needing significant domain expertise.

### Weaknesses
1. While the contribution is simple and easy to understand, I believe the contribution is a bit incremental than one would like. The core idea of using a context-dependent parameterization of a policy class, while intuitive, lacks significant novelty in the broader context of representation learning and policy parameterization techniques. The paper does not adequately demonstrate how this approach fundamentally differs from existing methods that also incorporate historical context into policy learning, such as those using recurrent neural networks or attention mechanisms. A more rigorous comparison to these methods, highlighting the specific advantages of the proposed parameterization, is needed to justify the claim of a significant contribution.

2. I think its a strong assumption to make that imitation learning is the best thing to do in MIMIC and ADNI datasets. Healthcare biases in EHR data are fairly well-reported [1], although one might hypothesize it is less so for ICU data. Without clear discussion of why this is a reasonable choice, the relevance and applicability diminishes a bit, in my view. The paper does not sufficiently address the potential for learned policies to perpetuate or even amplify existing biases present in the training data. The authors should provide a more detailed discussion of the limitations of imitation learning in these contexts and how the proposed method mitigates or exacerbates these issues. A critical analysis of the potential negative consequences of deploying such a policy in real-world healthcare settings is necessary.

3. It is quite challenging for me to validate each of the interpretations of the emprical evaluation presented in the paper (beyond simple interpretation like expected values of the learned co-efficients at a very coarse level). A much better empirical evaluation would have been to ask clinicians specific questions about the learned policies and reported the summary statistics on those. I understand that this is challenging to do in generality, but even annotations from one to two clinicians would suffice. At this point because of the depth of emphasis on interpreting the policies, and my lack of clinical background, I am not able to asses most of the empirical evaluation. The paper relies heavily on qualitative interpretations of the learned policies, which are difficult to validate without domain expertise. The lack of quantitative metrics that directly measure the interpretability of the learned policies makes it challenging to objectively assess the method's effectiveness in this regard. The authors should consider incorporating metrics that quantify the degree to which the learned policies align with established clinical guidelines or expert opinions.

4. I am not sure the simulations in 4.2 really add much insight.

### Questions
1. Do the authors have a clinician on the team who assisted with these interpretations?

2. Why haven't authors re-created and reproduced their own results for MIMIC Antibiotics for AUPRC and Brier Score?

3. Why use MIMIC-II when we're already in a world with updated version of MIMIC-IV with a larger number of patients.

4. I don't clearly understand the ADNI MRI task. What is the goal and what is the desired outcome? Can the authors add more context in whether these cognitive impairment rating decisions tend to be accurate in the data?

5. I would suggest adding additional empirical evaluation in more traditional imitation learning tasks to show utility without requiring significant domain knowledge to interpret all results. 

6. I would also consider improving the empirical evaluation altogether. Suppose clinicians given you some domain constraints that need to be satisfied (e.g., antibiotics dose should not exceed a certain amount, although this is not the exact decision point here). Can the authors demonstrate that using contextualized policy learning more easily satisfies such constraints (without explicitly adding them) compared to existing baselines and RNN/LSTM parametrizations of the policy class? I think this would add some interesting evaluation than is currently presented in the paper.

---- Updates based on author responses--------------------------------
Thank you for the comments and for clarifying my concerns. It sounds like the authors claim is that this kind of imitation learning is useful to uncover biases in healthcare data. If that is the case, my recommendation is that the motivation needs to be updated to reflect what the contribution is. 

I still don't know why use MIMIC-III over MIMIC-IV

I also don't believe methods like LIME can actually provide real interpretability of treatment policies in a way that's actionable to clinicians. 

I do believe adding more clinician annotations will make the study interesting and the empirical evaluation more credible. 

Based on the author responses, I have improved the score.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is concerned with learning interpretable policies from data. Different from prior work, it frames the problem as learning context-specific interpretable policies. The paper claims that instead of a global interpretable policy, having multiple contextualized interpretable policies results in an improved tradeoff between accuracy and interpretability. Each context-specific policy is called interpretable because it induces a linear mapping from observations to actions. On the other hand, these interpretable policies are parameterized by contexts, which can be generated from historical data using black-box models. The paper’s claims were validated by two experiments on medical domains. One of them concerns interpreting MRI prescriptions. The other one is about predicting antibiotic prescriptions.

### Strengths
With the growing use of machine learning methods in high-stakes real-world applications, questions posing the interpretability of machine learning methods have become a serious concern in the field. This paper tries to improve the tradeoff between interpretability and accuracy by proposing contextualized policy recovery. AUROC improvements in the accuracy compared to SOTA interpretable policy learning methods are promising. It is also good that the authors focus their experimental results and discussion on two real-world medical problems that intrigue researchers and practitioners.

### Weaknesses
I am not convinced by the originality and significance of the proposed approach. On the one hand, the proposed approach comes with remarkable performance, almost matching those of non-interpretable black-box counterparts. On the other hand, it deems itself as being as interpretable as previous interpretable policies. Reasoning dictates that there should be no free lunch. Looking deeper into the proposed contextualized policy recovery (CPR), I see it as a grey box rather than a glass box. It is a glass box only for the current context, which is good. However, all the past information, including previous contexts and actions, is hidden inside a non-interpretable black-box context encoder. I think that this jeopardizes the interpretability of the envisioned medical applications. To put things into context, given the same context at time t, different action probabilities can be recommended based on the history-dependent parameterization. Ideally, we want to understand which contexts and actions in the past caused this difference. However, if the context encoder is black-box, it sheds no light on why this difference happened. I think that this is a big obstacle to interpretability.

The experiments mainly involve applying CPR to medical datasets and interpreting the resulting context-specific decision models. In line with the main premise of CPR, decision functions change under different contexts. I am confused about the interpretation of the heterogeneity of the decision policies. For instance, for the MIMIC antibiotics dataset, it is concluded that the main driver of heterogeneity is “prior antibiotic prescription”. Is it a conclusion that CPR reached? This should be the case if CPR produces interpretable policies. However, it does not seem to be the case since prior antibiotic prescription (which is an action taken in the past) is mapped to a context by a black-box context encoder.

### Questions
The experiments mainly involve applying CPR to medical datasets and interpreting the resulting context-specific decision models. In line with the main premise of CPR, decision functions change under different contexts. I am confused about the interpretation of the heterogeneity of the decision policies. For instance, for the MIMIC antibiotics dataset, it is concluded that the main driver of heterogeneity is “prior antibiotic prescription”. Is it a conclusion that CPR reached? This should be the case if CPR produces interpretable policies. However, it does not seem to be the case since prior antibiotic prescription (which is an action taken in the past) is mapped to a context by a black-box context encoder.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed an interpretable behavior cloning method for a partially observed MDP, the Contextualized Policy Recovery. It reframes the problem of policy learning as a multi-task learning of context-specific policies. A time-varying and context-dependent policy linearly maps the patient symptoms to treatment. The context updates with new symptoms and treatments. Effectively CPR is learning a linear behavior cloning plicy whose model parameters adapt to history information, with the history affecting the model parameters instead of the input, thus retaining interpretability. Experiments with a simulator show that CPR can converge to the true decision model parameters. On two behavior cloning tasks with real medical data, it matches the performance of black-box models in terms of recovering best treatments.

### Strengths
1. proposed a novel approach to interpretable behavior cloning
2. Thorough experimentation and analyses

### Weaknesses
1. the interpretability is only retained for the current observation in the logistic regression but not for history values, nor the dynamics (how the values progress across time), both of which can be more important than some of the current values in real-world problems. Indeed the authors did mention that 'CPR assumes that a physician places the highest importance on the most current patient information when deciding an action', but this however contradicts their own problem setting of the partially observable environment in which 'the action probability ... is a function of ... current and past patient symptoms, as well as past actions'. So it seems to me either limited interpretability in POMDPs (without interpreting history), or interpretability assuming the current observation is most important to and suffice to interpret the action (which is no longer an unconstrained POMDP). I'm not so convinced how valuable either is.
2. the authors appear to be using behavior cloning and imitation learning interchangeably.
3. since patients with missing observation values were excluded, it's hard to say how well the model can make use of historical information, i.e., the environment was not partially observable enough.
4. (minor) typo in Eq. 1 $P_w(\theta|c)$

### Questions
1. how did you realize the stochasticity around $\theta$ suggested in Eq. 1 if it's parameterized only by an RNN?
2. why all the experimented environments have a binary action space? It'd be good to see how the interpretability and accuracy generalize to multi-class predictions with a linear model.
3. as the weights of the regression model are parametrized by an RNN, there is inductive bias between consecutive timesteps. So I would envisage it's possible that e.g. a feature is found to be important at a certain step not least because it was important at the previous step, but not that it's actually still important (or its current importance being exaggerated). Would you think this should be a problem and why?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor
