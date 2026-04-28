# Machine Reinforced Perturbation on Drifted Human Logical Reasoning

- Decision: Reject
- Avg Score: 5.17
- Scores: 3, 6, 6, 5, 5, 6

## Abstract
Using deep neural networks as computational models to simulate cognitive process can provide key insights into human behavioral dynamics. This enables synthetic data generation to test hypotheses for neuroscience and guides adaptive interventions for cognitive regulation. Challenges arise when environments are highly dynamic, obscuring stimulus-behavior relationships. However, the majority of current research focuses on simulating human cognitive behaviors under ideal conditions, neglecting the influence of environmental disturbances. We propose ReactiveAgent, integrating drift-diffusion with deep reinforcement learning to simulate granular effects of dynamic environmental stimuli on human logical reasoning process. This framework is built and evaluated upon our contributed large dataset of 21,157 logical responses of humans under various dynamic stimuli. Quantitatively, the framework improves cognition modelling by considering temporal effect of environmental stimuli on logical reasoning and captures both subject-specific and stimuli-specific behavioural differences. Qualitatively, it captures general trends in human logical reasoning under stress, better than baselines. Our approach is extensible to examining diverse environmental influences on cognitive behaviors. Overall, it demonstrates a powerful, data-driven methodology to simulate, align with, and understand the vagaries of human logical reasoning in dynamic contexts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to discover a model capturing how time pressure affects logical reasoning by predicting answers and reaction times by humans in a mathematical logical reasoning problem. The authors introduce a hybrid model combining task-driven deep learning, deep RL, and a classic cognitive model (DDM) designed to capture the dynamics of decision-making under uncertainty. The authors demonstrate that this model attains higher quantitative scores than some other approaches. The authors also introduce a dataset consisting of 44 subjects performing this task. They also argue that the approach is interpretable, permitting interrogation of the classic cognitive model's components.

### Strengths
The work is well motivated, as predicting human behavior in complex reasoning problems is an important and exciting application of AI.

The hybrid data-driven approach seems promising for this type of task. Particularly given the constraints of the dataset, using features learned from a model trained on a task, adapting them based on behavior, and incorporating a classic model with an interrogatable form seems like a good approach for this problem. 

The open-sourcing of the dataset is a very positive contribution.

### Weaknesses
The approach appears to quantitatively outperform others to which they compare it, although it is unclear how these baselines are motivated -- what drives the choices in Table 1? 

Furthermore, the improvement is hard to interpret. The mean score of 0.2999 is better than for the other models. However, the standard deviation and lower/upper bounds of the range are quite large, and it's not clear if this difference is significant. This is also the case for the quantitative results per figure.

It also would be helpful to see what scores look like at chance. I realize there is no "chance" for RTs, but recommend performing a permutation test (randomly permute choices with respect to input problems) and report the scores. Otherwise, it's not clear what magnitude of improvement the current method gives (and it's not clear how strong the baselines are, or whether the data is sufficient here to support a data-driven approach at all). 

Is there a classic cognitive modeling approach that has been typically applied to this problem, or is there one suggested by the heuristics that have been documented? I realize the DDM is part of this, but it seems that can't be applied naively absent the LSTM/DRL/SVM components. This would also be helpful for assessing the contribution.

Model seems a bit complex, and it's not clear the extent to which each component is justified or what each component is uniquely responsible for. For example, there are multiple stages that adapt the model to the data (SVM+DRL).

Model ablations are performed, but they are incomplete. For example, it also appears there is no ablation that includes giving all the information that was used to train the LSTM to the SVM model -- the numbers were given, but not what the correct answer is. This is important because it's possible the additional information conferred by the LSTM is having information about what the target is going to be. Another ablation might use the output logits of the LSTM rather than the feature layer, as it seems likely that the answer and the certainty about it would have a lot of the information relevant to predicting reaction time, whereas "features" implies it something about the stimuli.

These ablations also have confusing numbers -- how are digits/strings getting 81% accuracy and F1 score of 0?

44 subjects is not a huge dataset as it relates to this type of analysis, and with 4 conditions, that is 11 per group. It is also a cognitively complex task which would presumably demonstrate real individual variability, making larger numbers even more important. I'm skeptical this dataset is sufficiently large to support a data driven approach at all. This could be demonstrated by outperforming a pure cognitive model baseline, or with some careful permutation tests. but with only data-driven baselines, it's unclear what the model is picking up on.

Presentation of the task, model, and results are very unclear. In particular, it was very difficult to figure out the architecture, and several design choices are unclear. Even after referencing the figure in the appendix, I'm unclear on why an LSTM was used, and what corresponds to the sequence dimension (trials? computation time? time within trial?). Also was not clear some of the task details -- are subjects informed of the task structure, or do they learn it from feedback? How are numbers sampled -- is the probabilty of true/false 50/50? Also had difficult parsing the text on how the progress bar related to the agents score.

missing axis labels -- e.g. what are the x + y axes in fig 6? fig 9?

interpretability -- these seem like behavioral features that all could have been measured in a pure data driven approach.

### Questions
Questions inline above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a novel hybrid approach for modeling of human cognitive process by incorporating the drift-diffusion model (DDM) with RL agent. The authors evaluate their idea on the task with modular arithmetic. The proposed approach extracts features using a pre-trained LSTM model on synthetic data, after that SVM model is used to predict response time and correctness of the response. On top of that, they train an RL agent that extracts visual information using CNN model and obtains reward from a DDM model.

### Strengths
1. The authors provide an open dataset for future investigation and research.
2. The authors introduce a novel method for incorporating RL into modeling human reasoning.
3. The authors provide a variety of baseline models that were used in experiments.

### Weaknesses
1. The entire problem applied only to modular arithmetic which might not exactly be a full baseline for the method. In general, extending to more tasks would highlight the method's applicability and generalization. 
2. No connection to learning user state? LSTM models are great tools for learning underlying user states as shown in DKT [https://stanford.edu/~cpiech/bio/papers/deepKnowledgeTracing.pdf]. I would expect to see also some of the user information fed directly to the model rather than just using it as a proxy.
3. Is the model really interpretable? I still have doubts that by adding RL agent and LSTM (Which both are not interpretable) we can give an assessment of cognitive behavior.  The entire section 5.6 does not provide insight into human/agent decisions. I would suggest adding more discussion of the effect of LSTM and RL agents on casual connection.

### Questions
1. Does the neuron in LSTM refer to the size of the hidden state?
1.1 Does line 352 refer to the last layer of LSTM or the hidden state size?
1.2 I would suggest replacing training loss/accuracy with Validation loss /accuracy. Since 100% accuracy might also refer to overfitting for LSTM in this scenario. 
2. In line 947, the agent should output 2 instead of 3? 26 mod 4 is 2.
3. Does the model generalize on tasks of different lengths i.e. can we model 4360==870mod(6)? I do understand that it would be hard for the person to answer such a problem in real-time, but it might be beneficial for model performance.
4. What exactly meant "the block number." on line 1007?
5. How does including question id in training SVM affect the performance of the model? I'm not sure that I correctly understand the point of adding question id as a feature since it might cause a common leak problem, which just makes SVM remember the mapping between feature id and the correctness/time response of the user. 
6. How does dataset size affect the performance of the model? 
8. Why can't we add user features to lstm for training and output user features for better representation? I.e why can't we directly train lstm on user data?
9. Does the model take into account that with time users get more familiar with the problem and their response time also changes?
10. Can you clarify general level splitting? Is it performed in Time base Sequence Train-Test split? [https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
11. I would argue about interpretability since the approach requires a "black-box" LSTM model. Same as with RL agent, it can not be directly interpretable since it is basically an MLP trained with PPO without any constraints. It would be interesting to see more discussion on inpreterability of such an approach. 
12. Typo: For time pressurem, line 1039
13. Could authors clarify action space for the hybrid model and the total final estimation of time? What is the output of the hybrid model i.e last layer of MLP?
14. Whate are R_p and S_p on line 1147
15. How does long-term evaluation of user prediction and time?

Comments:
1. I would refer here to [https://arxiv.org/pdf/2207.02098] as seen in Table 2, LSTM tends to fail at Modular Arithmetic since it corresponds to DCF grammar.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenges of using deep learning to simulate cognitive processes in the context of dynamic environments, where environmental disturbances are often neglected or ideal conditions assumed. Specifically, the paper presents a dataset capturing human logical reasoning in response to temporally variable environmental stimuli and formulates ReactiveAgent to simulate such phenomena at fine granularity. The work improves modeling of human logical reasoning under stress and is extensible to analyze other environmentally-influenced cognitive behaviors.

### Strengths
+ The paper addresses an important gap in current approaches to computationally model human cognitive behaviors, namely the ability to analyze nuances of how dynamic environmental factors impact human cognition.
+ The paper uniquely builds upon the benefits of DDM and DRL to develop a more flexible and interpretable cognitive modeling approach.
+ Experiments are sound, with reasonable metrics selected to assess performance. Ablation studies are comprehensive to verify each portion of the framework. Alignment of predicted with actual human response times is high vs. baseline methods.

### Weaknesses
The paper focuses on a single math arithmetic task to demonstrate the efficacy of the proposed framework. This is reasonable and gives good results, but a second setting would be helpful to demonstrate the generalizability of the approach. 

Please see additional considerations in the questions below.

### Questions
Questions
* Table 1 Clarification: For response time predictions represented in Table 1, was this done on a per-individual basis or per-group basis? Additionally, did predictions capture absolute response time or the difference between baseline and time-pressured response time? Baseline measurement is discussed in the main and supplementary texts but it appears unclear here. If predictions capture raw response times would perceived task difficulty and mental fatigue/attention not be confounders? 
* For the curated dataset, how was the validity of responses assessed? Specifically, what determined whether a response time sample was valid/invalid?
* What is the rationale for using MAPE versus correlation to assess alignment between predicted and real response times?
* How does the accuracy of the logical reasoning agent impact the efficacy of the proposed framework at modeling human performance?
* How would one extend ReactiveAgent to model human cognitive performance in more than one task at once?

Suggestions
* Figure 1: The name of the method, ReactiveAgent, is not mentioned. It could help to increase the font size of the label for each of the four stages or move the labels to under the rectangular bounding boxes.
* [Minor] Line 97-98: “proposed” is in past tense vs. present tense for the following two contribution bullet points.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present ReactiveAgent which is an interesting computational framework designed to simulate the impact of dynamic environmental stimuli, such as time pressure, on human logical reasoning processes. They integrate the drift-diffusion model with deep reinforcement learning in order to model the effect of dynamic stimuli on evidence accumulation during decision-making tasks. ReactiveAgent is evaluated on a dataset of 21157 human responses to math tasks under various time-pressure conditions which is claimed to demonstrate improved accuracy, interpretability, and efficiency compared to baseline models. The authors discuss how the framework has potential to provide insights into human cognitive behaviors under stress and that this work could contribute to the development of adaptive interventions and neuroscience research.

### Strengths
1. Open-source dataset with 21,157 logical reasoning responses from humans
2. Shows better simulation accuracy in predicting human response times compared to several baseline models, meaning the framework captures the effects of dynamic stimuli on cognitive processes more accurately
3. The framework is flexible and could be adapted to study other types of environmental influences on cognitive behaviors beyond time pressure, suggesting it could be applied broadly in cognitive science research
4. Includes comprehensive ablation studies that evaluate the importance of each component in their framework, like the math logical reasoning agent and the integration of the DDM into the DRL agent

### Weaknesses
1. While the introduction outlines the methodology and objectives of the study, it lacks a compelling explanation of why this research is significant and what specific impact it could have on the field of cognitive modeling or neuroscience. The only mentions of potential impact are generic statements about providing key insights into human behavioral dynamics and informing the design of feedback mechanisms to augment cognition. This vagueness makes it difficult to understand the broader implications or novelty of the work.

---- [Abstract] Using deep neural networks as computational models to simulate cognitive process can provide key insights into human behavioral dynamics. 

---- [Intro] ...the effects of environmental dynamics (e.g., stress (Cheng (2017)) and feedback (Costa et al. (2019))) on cognitive performance could elucidate behavioral responses to tasks (Cheng (2017)) and inform the design of feedback mechanisms to augment cognition

**Recommendation for Improvement**: The authors should clearly articulate the specific contributions and potential impact of their work. This could involve highlighting how their hybrid framework advances current modeling techniques, addresses existing limitations, or opens new avenues for research. Providing concrete examples of applications or how this model could influence future studies would strengthen the paper's significance

2. The core of the paper is the integration of the drift-diffusion model with deep reinforcement learning to simulate the impact of dynamic stimuli on human logical reasoning. However, the paper does not provide enough analysis of how the modulations introduced by the DRL agent align with established cognitive mechanisms or theories of human reasoning under stress. There is a gap in demonstrating that the DRL agent's modulation of evidence accumulation trajectories corresponds to known patterns of human cognitive processing under time pressure.

**Recommendation for Improvement**: The authors should conduct a deeper analysis comparing the DRL-induced modulations with empirical data or established theories on human cognitive mechanisms under stress. Including discussing how the DRL agent's behavior mirrors or diverges from human cognitive strategies under time pressure would provide good insights.

3. The study exclusively focuses on time pressure as the external stimulus affecting cognitive performance. While time pressure is a significant stressor, cognitive stress can also arise from factors like multitasking, uncertainty, or social pressures. The paper does not explore whether the proposed framework can generalize to other forms of cognitive stress or external stimuli.

**Recommendation for Improvement**: To improve the generalizability of the framework, the authors should consider incorporating other types of cognitive stress into their experiments or at least discuss how the model might be adapted for different stressors. This could involve designing tasks that introduce emotional distractions or require multitasking, and then evaluating the model's performance under these new conditions.

4. Figure 2 top row is hard to interpret. Please create a more interpretable graph.

5. This study uses a math arithmetic task to assess human logical reasoning under time pressure. Relying on a single type of task may limit the applicability of the results to other domains of cognitive function. Different cognitive tasks engage various neural circuits and cognitive processes, so a model that performs well in math reasoning may not necessarily translate to language comprehension, spatial navigation, or memory tasks.

**Recommendation for Improvement**: The authors should evaluate their framework on perhaps 1 additional cognitive task to demonstrate its robustness and general applicability. If extending the study to additional tasks is not feasible within the current timeline, the authors should acknowledge this limitation and propose it as an avenue for future research.

6. consider incorporating qualitative analyses or case studies could improve the evaluation in the main text or appendix. For example, examining specific instances where the model successfully predicts human behavior under stress or fails to do so could demonstrate the underlying mechanisms. Including discussions on how the model's behavior aligns with psychological theories of stress and decision-making would improve this work.

### Questions
1. Can you provide a clearer explanation of why your work is important and what specific impact it could have on cognitive modeling or neuroscience?
2. How does the DRL agent's modulation of the evidence accumulation process align with known human cognitive mechanisms under stress? can you provide more analysis or evidence supporting this alignment?
3. Can your framework be tested on other cognitive tasks besides math reasoning to demonstrate its robustness? Do you have plans to evaluate it on tasks involving memory, language comprehension, or spatial reasoning?
4. Have you considered potential confounding factors like individual differences in stress tolerance, math proficiency, or fatigue? Discussing how these might affect your results would strengthen the validity of your findings.
5. What are your plans for future work? Do you intend to test your model with different tasks or incorporate other forms of stimuli?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes to model the effects of stress-inducing stimuli on human response time in a mathematical reasoning task. The task consist of a math problem (answering whether two number are equivalent modulo a third), and the stimulus is a progress bar creating time pressure. The authors collect a large dataset of human response times under various applications of this stimulus, and train and evaluate their proposed model on it.

The model consists of SVMs predicting response time and choice under perfect conditions (no stimulus) from an embedding of the math task. A drift diffusion model (DDM) is then used to predict response time under the stimulus from this. The DDM’s evidence accumulation rate is modulated by an RL policy conditioned on the stimulus. The RL policy is trained to steer the DDM such that it replicated the response rates observed in the training data.

The proposed model is compared to a large set of baselines. The authors also find that use of the DDM in predicting the response time is instrumental.

### Strengths
The paper tackles an important problem: reasoning and choice under time pressure. The model it contributes can unlock new insights into human behavior in these conditions, and could potentially be used to create new interventions to mitigate the effects of these stimuli.

I appreciate that this paper moves away from ideal conditions and towards dynamic environmental stimuli. I also like that the task considered is simple but realistic. In this light, the participant data that was collected is certainly valuable.

The experiments presented appear rigorous (although I sometimes miss statistical significance tests) and are well-documented in the main paper and in the extensive appendices.

### Weaknesses
What I am missing is a more explicit hypothesis regarding how the stimulus considered here affects human choice, and to see that hypothesis reflected in the modelling decisions. Right now the paper reads very much like a statistical modelling paper, which arranges a number of existing elements into a new ML model that achieves better performance than baselines, but does not uncover any significant insight into human cognition.

Further, Table 3 suggests that the proposed model’s performance is within error of a standard Transformer model (line 1386). Why was this baseline not included in the main text? Is there any reason why it is not an equally good model?

Finally, the model is evaluated on only one task. This is acknowledged by authors, and I do understand that this is common practice in the field. Nevertheless, it limits the evidence we have for the proposed model.

### Questions
For the pure DRL agent, wouldn’t the problem it is solving be more accurately described as a contextual bandit problem? The actions it takes (predicting perturbation to baseline response time) do not appear to affect the next state (the next math problem), unless I am missing something?

In section A.6.4, it is unclear to me how exactly the action affects the rate of evidence accumulation. I do not see the action $a$ in any of the formulas there.

Is the difference in MAPE between the Hybrid DRL and Pure DRL agents statistically significant?

You found that the block number influenced users’ performance, and therefore included the question ID as an additional feature for response time and choice prediction. Why was this important? Does it help to model (implicitly) things like participants tiring out (hence slipping attention) or learning the task (hence decreasing response time)?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduce "ReactiveAgent," a hybrid framework integrating deep reinforcement learning (DRL) with the drift-diffusion model (DDM) to simulate the impact of dynamic environmental stimuli on human logical reasoning. The model aims to provide a more granular simulation of human cognition under dynamic conditions, particularly under time pressure.

 ReactiveAgent leverages a large dataset of human logical responses and demonstrates improved accuracy and interpretability compared to existing cognitive models.


The paper addresses the challenge of modeling human cognitive behavior under dynamic environmental stimuli. While existing research typically focuses on modeling cognition under ideal conditions, this work aims to simulate how environmental factors (like time pressure and stress) affect human logical reasoning.

### Strengths
The authors contributed a large dataset of human logical reasoning responses under dynamic stimuli. Open sourcing the dataset would allow future researchers to leverage the data for other cognitive studies

Better Performance: ReactiveAgent achieves lower Mean Average Percentage Error (MAPE) compared to baseline models

Faster Training: Hybrid approach converges ~10x faster than pure DRL

Better Interpretability: Can generate and analyze trajectories of time pressure effects

Captures Group Differences: Successfully models different responses across experimental groups

### Weaknesses
1.Single Task Limitation: The evaluation is based solely on a math arithmetic task, which may limit the generalizability of the conclusions. Cognitive processes vary significantly across different types of tasks, and more diverse tasks would help in validating whether ReactiveAgent's approach is broadly applicable to human cognition beyond arithmetic reasoning.

2. Complexity of Model Components: The integration of multiple components (LSTM, DRL, DDM, etc.) adds considerable complexity to the framework. While the paper strives to explain these interactions, there is still a risk that such complexity may lead to challenges in replicability or practical implementation.

### Questions
How well does the proposed framework generalize to other types of cognitive tasks beyond the arithmetic task presented? Could the authors provide further clarification or potentially some preliminary experiments to address generalizability?

How sensitive is the framework to the hyperparameter choices, particularly those in the DRL agent and the drift-diffusion model?

### Soundness
3

### Presentation
3

### Contribution
2
