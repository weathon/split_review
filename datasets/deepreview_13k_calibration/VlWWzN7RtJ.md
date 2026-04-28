# iMotion-LLM: Motion Prediction Instruction Tuning

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 6, 3, 3, 3

## Abstract
We introduce {\papernameAbbrev}: a  Multimodal Large Language Models (LLMs) with trajectory prediction, tailored to guide interactive multi-agent scenarios. Different from conventional motion prediction approaches, {\papernameAbbrev} capitalizes on textual instructions as key inputs for generating contextually relevant trajectories. By enriching the real-world driving scenarios in the Waymo Open Dataset with textual motion instructions, we created InstructWaymo. Leveraging this dataset, {\papernameAbbrev} integrates a pretrained LLM, fine-tuned with LoRA, to translate scene features into the LLM input space.
iMotion-LLM offers significant advantages over conventional motion prediction models. First, it can generate trajectories that align with the provided instructions if it is a feasible direction. Second, when given an infeasible direction, it can reject the instruction, thereby enhancing safety.  
These findings act as milestones in empowering autonomous navigation systems to interpret and predict the dynamics of multi-agent environments, laying the groundwork for future advancements in this field.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents an advanced multimodal large language model designed for autonomous driving, capable of forecasting vehicle trajectories by synthesizing textual instructions with environmental data. By integrating a pretrained LLM with trajectory prediction frameworks, iMotion-LLM is adept at producing diverse and viable future pathways that align precisely with specified driving directives. To facilitate this capability, the authors introduce InstructWaymo, a novel data augmentation method that infuses the Waymo Open Motion Dataset with textual driving commands, thereby augmenting the model’s proficiency in instruction adherence.

### Strengths
- Introduces an innovative task, Text-Guided Intention Trajectory Prediction, which adds a new dimension to autonomous driving by combining language-based instructions with trajectory forecasting.
- Proposes InstructWaymo, a unique data augmentation technique that enriches the Waymo Open Motion Dataset with textual driving commands, making trajectory prediction more adaptable and interactive.
- Demonstrates an application of large language models in trajectory prediction, creatively bridging LLMs with multimodal inputs for real-time, instruction-following models.

### Weaknesses
- More experiments are needed. The paper only considered the GameFormer model as the motion prediction model. It will be interesting to add more models as baseline motion predictors. E.g., Add instruction guidance to the MTR [1] that has strong performance in motion prediction task. 
- In table 4, the baseline GameFormer without guided instruction is always better than iMotion-LLM (even considering actual scenario instruction). It seems the generalizability of the instruction-based model becomes worse. 
- In the main results, the OF/INF drops a lot after adding feasibility detection, which means the feasibility detector could reject more feasible instructions. 


[1] Shi, Shaoshuai, et al. "Motion transformer with global intention localization and local movement refinement." Advances in Neural Information Processing Systems 35 (2022): 6531-6543.

### Questions
Please see the concerns in the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an instruction-following car trajectory forecasting model, introducing metrics to measure instruction adherence. It presents a data augmentation technique that generates templated text descriptions of car trajectories. Additionally, it proposes an architecture involving a large language model (LLM) designed to interpret these augmented trajectories and encode them for trajectory forecasting purposes.

### Strengths
- The integration of language instructions with trajectory forecasting is an interesting approach that could enhance the interpretability of prediction models.
- The proposed data augmentation technique offers a systematic way to generate text descriptions from trajectories, potentially enriching the training data.

### Weaknesses
*Lack of Clear Motivation*: The paper claims advantages such as enhancing safety and the ability to anticipate and adapt to potential hazards. However, it does not demonstrate how the proposed method contributes to these areas.
The motivations provided could be achieved with existing multi-modal trajectory forecasting models. While the paper propose a novel approach, this novelty does not seem to contribute to its motivations.

*Overly Restrictive Data Augmentation*: The rule-based approach relies on absolute directions and speed changes, which may not generalize well to complex or curvy roads where "going straight" involves turning.
The categories used do not align with common driver decisions, such as lane changes, limiting the applicability of the method for general scenes and interpretability.

*Questionable Feasibility Parameters*: The feasibility conditions (e.g., minimum and maximum speed changes, maximum range of 60 meters) are hard to interpret and seem arbitrary.The method for lane association to assess feasible directions is not clearly explained.

*Lack of Comparison with Baselines and Ablations*: The proposed architecture is complex, involving multiple components and customized inputs/outputs, but lacks clear justification for its design. However, it shows weak ablation studies to justify the numerous design choices. There is only one comparison with GameFormer on the core application and two ablations in table 2.(a). One ablation is keeping the GameFormer architecture but adds a conditioning on instructions, the other is the proposed approach without the feasibility detection. The results are mixed without a clear best choice between these three ablations. The proposed approach shows a significant degradation of instruction following recall on actual scenario and other feasible scenario (bad) while showing a lower compliance to infeasible instructions (good). It is unclear if the actual scenario instruction following to infeasible instruction following ratio shows a significant gain because it is 4x smaller than the unconditionned GameFormer baseline.
Two other baseline models are used (MTR and MotionLM) but using different metrics (minADE and minFDE) that are not core to the paper (all three baseline outperform the proposed approach on these metrics).  

*Rigid and Arbitrary Metrics*: The diversity and instruction-following metrics are based on rigid categorizations, which may not generalize across diverse road scenarios. Related works on measuring multi-modality and diversity in trajectory predictions are not adequately discussed to assess the novelty of the proposed metrics. The metric definitions uses thresholds that match exactly the instruction generation and might not be useful as a novel metric proposition for other methods that do not rely on these instructions.

*Misleading or Inaccurate Claims*: The statement that previous prediction models lack comprehension of different driving behaviors is inaccurate, as many models are designed to capture diversity and consider various driving scenarios.
Some design choices and their justifications are unclear or unjustified within the context of the paper.

### Questions
- Can you provide concrete evidence or examples of how your method specifically contributes to enhancing safety and hazard anticipation compared to existing models or give a different motivation for why this work is important that I have missed?
- How does your rule-based data augmentation handle complex road scenarios, such as curvy roads or lane changes? Have you tested its effectiveness in these contexts?
- Could you clarify the feasibility conditions used in your method, such as the minimum and maximum speed changes and the maximum range? How were these parameters determined, and are they empirically justified?
- Why did you choose to freeze the motion prediction model during training? Have you conducted any ablation studies to assess the impact of this choice on your model's performance?
- Have you considered or compared your instruction construction method to other baselines, such as using an LLM or VLM to generate text descriptions from input trajectories or from renderings of the scene and trajectory? Given that the generated instructions are templated and do not resemble human-generated descriptions, how do you assess their effectiveness? Would incorporating more natural language generation techniques improve performance?
- Can you discuss how your diversity and instruction-following metrics compare to existing metrics in trajectory prediction research? How do they contribute to assessing the novelty and relevance of your approach? Instruction following could be compared to maneuver aware prediction or CVAE approaches given the conditioning class. Many diversity metrics from the literature could be used, could you justify why they are not suitable in your approach?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel task called Text-Guided Intention Trajectory Prediction for the trajectory prediction model to predict future trajectories based on human intention input. To establish the methodology and baseline, the paper introduces several contributions, such as Waymo dataset augmentation, novel model design for language and scene fusion, and extensive validation on the benchmarks.

### Strengths
The paper introduces a novel task that incorporates human intention into the prediction model, which is of sufficient impact on the discussion on safety-critical scenarios in autonomous driving. To serve with this topic, the author augments scenario descriptions to the Waymo dataset and also enhances the previous proposed models to incorporate scene descriptions. The author also proposes relevant evaluation metrics to measure the controllability of such proposed model.
The paper is overall well-written and easy to follow.

### Weaknesses
1. Language-conditioned trajectory prediction and generation has evolved in years and there are many previous works that the authors to compete in terms of the performance, such as Trafficgen: Learning to generate diverse and realistic traffic scenarios [ICRA 2023], Language Conditioned Traffic Generation [CoRL 2023], etc. The authors should have discussed about their model design choices compared to the previous literature.
2. Although mentioned in their introduction, the discussion of safety-critical scenarios is limited in the main paper. I feel like it is a very important topic since the incorporation of human intention should be measured or evaluated with the compatibility to prevent danger in real-world cases. I suggest the authors to follow RiskBench: A Scenario-based Risk Identification Benchmark [ICRA 2024] paper to at least have some discussions on how the current model could benefit risk localization and anticipation in traffic scenario.

### Questions
1. Can the authors post some of the failure cases analysis where the prediction model 1) failed to obey human intention 2) failed to understand traffic scenarios (in crowded scenario)? 
2. Could you explain how you measure the quality of the augmented scenario descriptions of Waymo dataset?
3. It would be beneficial to see the performance variations when training with different ratios of the training data (i.e., 20%, 50%, 80%) to see the effectiveness of language augmentations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents iMotion-LLM, a multimodal large language model (LLM) integrated with trajectory prediction to enhance interactive motion prediction for autonomous driving. iMotion-LLM incorporates a pretrained LLM fine-tuned via LoRA to generate trajectory predictions based on textual instructions, utilizing a new augmented dataset, InstructWaymo, derived from the Waymo Open Motion Dataset (WOMD). Through conditional language prompts, iMotion-LLM aims to generate more diverse and instruction-compliant trajectories while filtering out infeasible scenarios to improve driving safety.

### Strengths
1. **Interesting Technical Approach**: The concept of making motion prediction models promptable through natural language is interesting. The authors made an integration of LLMs into the domain of trajectory prediction, expanding the scope of traditional motion prediction models/tasks.

2. **Contribution of New Metrics**: The introduction of new metrics such as Instruction Following Recall (IFR) and Direction Variety Score (DVS) is valuable, as they address the consistency between instructions and generated actions, as well as the diversity of predictions. These metrics could provide good value for future work on language-conditioned motion prediction/planning.

3. **One Insightful Experimental Result**: The experiments in Table 2, showcase interesting findings, namely feasibility detection can lower instruction adherence when instructions are infeasible.

4. **Clear Illustrations**: The paper includes well-designed figures and tables that support the understanding of the proposed method.

### Weaknesses
1. **Poor Writing and Structure**: The paper suffers from poor organization and writing quality, which significantly impacts clarity. The overall flow and logic are difficult to follow. A structured rewrite, with a stronger focus on motivation and high-level contributions, would improve readability. 
   - The abstraction and introduction lack structure and logic. Among all examples, the most obvious one is that, evaluation metrics are introduced even before the proposed model itself, leading to a confusing narrative. 
   - The methodology sections (Sections 3, 4, and 5) are even harder to follow. For example, the beginning of Section 3 contains too many details, making the paper more like a technical report rather than a scientific paper. After reading, it still remains unclear what constitutes an “instruction” in the context of this paper. For example, is it limited to one word as in the categories listed in Table 1? A full list or a representative list of actual used instructions would be helpful. The authors should describe the design principles and structures, and leave details to the appendix. 
   - Besides, numerous unexplained terms appear abruptly. For example, the definition of “caption” on line 212 causes a lot of confusion, and the reviewer only finds an implicit definition of it later in Line 306. 
   - In Section 4, a large portion of the text is describing another paper, namely GameFormer, which shows excessive detail and unclear focus. I know the proposed method is based on the structure of GameFormer, but this description should be condensed in one paragraph, instead of half a page.

2. **Unclear Motivation for Instruction-Conditioned Prediction**: The paper appears to aim at addressing instruction-conditioned prediction, yet the introduction focuses instead on prediction diversity. The authors do not clearly present the motivation, insights, or advantages of condition-based prediction. Later, the authors suggest that conditioning motion prediction offers benefits such as (1) enhancing prediction diversity and (2) generating challenging, novel traffic scenarios. However, these points are not convincingly substantiated:
   - How the proposed method achieves diverse predictions is unclear. Simply enumerating possible language instructions to prompt the model seems neither meaningful nor efficient.
   - Generating realistic traffic scenes requires multi-agent modeling and interaction, whereas the proposed method generates predictions for only a single agent at a time, which limits the model's ability to simulate complex multi-agent scenarios realistically.

Additionally, the motivation and contributions of this work are introduced late and somewhat buried (line 312). A revision to clarify and emphasize true contributions would greatly improve the paper’s coherence and impact. The current writing and presentation make it challenging for reviewers to fully appreciate the technical contributions of this work.

3. **Experiment Design Concerns**: Several issues in the experimental setup raise questions about the validity of the findings:
   - Customized Data Split: The use of a custom data split with only 2,311 samples from Waymo raises concerns about statistical confidence. Justification for not using the full dataset, possibly due to computational constraints, and how these 2,311 samples are selected, would be helpful.
   - Baseline Evaluation: In Table 2(a), the evaluation for GameFormer on instruction-following and diversity metrics is unclear. Since GameFormer does not take instructions as input, how is its instruction-following performance assessed? Are predictions generated without instructions and then compared against the instructions? If so, further explanation on the significance of this baseline would be helpful.
   - Unclear Baseline Descriptions: Again in Table 2(a), the baseline of conditional GameFormer lacks sufficient descriptions. How GameFormer is conditioned on discrete directions, by using ground truth directions as additional inputs? More transparency is needed to understand how these comparisons are made.
   - Incorrect Naming in Tables: In Table 2(a), the last two rows have identical method names. Besides, in one table, we observe multiple methods are labelled as 'ours', which could be confusing.
   - Incomparable evaluation: Tables 3 and 4 use different data for evaluation (test set VS. customized val subset), which undermines comparability. I understand this metrics are used to get a sense of SOTA methods's performance, but using different data split could hinder that purpose. A better solution could be use SOTA methods' checkpoints and evaluate them on your customized data split

### Questions
see the weakness section

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work provides a text-guided trajectory "prediction" model which can generate future trajectories corresponding to the input language prompt and the history of a real driving scene. It first provides a tool, InstructWaymo, to add language which summarizes the future trajectory modals for Waymo Open Motion Dataset (WOMD) scenarios. With these labels, an LLM can be fine-tuned to make future trajectory generation following the modal ordered in language. Experiments show that language conditions are somehow followed by the trajectory generation model, while language explanations and feasibility are given at the same time as the output of the LLM. The authors also claim that the fine-tuned LLM can be generalized to other datasets.

### Strengths
1. The idea of classifying motion data in WOMD according to the future motion modal, and attaching the classified labels onto the WOMD, is interesting, and I believe it would make the motion dataset more useful for diverse downstream tasks.
2. The tool, InstructWaymo, seems to be useful for motion dataset users needing language modal input.
3. The proposed metrics, IFR and DVS, are interesting, as they provide additional angle focusing on the diversity of predictions, which is long ignored in previous works.

### Weaknesses
1. The most significant concern of me is: the authors claim this is a "text-guided trajectory prediction" work, but how can guidance and prediction exist at the same time? In trajectory predictions, we aim to analyze the history trajectory and propose *all possible* future trajectories, to help a safe planning. When a specific text prompt is involved, a future modal is specified so the prediction is no longer covering more modals. I would suggest the authors considering topics like "simulator" or "scene generator", which I believe would be more accurate and more significant.
2. If prediction is considered the topic for this work, results in Tab. 3 and Tab. 4 seem not supporting a positive effect of the proposed method. Without instructions, there seems not to be any metric improvement. While metrics do improve with instruction, it is noticeable that the instructions contain future trajectory modal information, which involves severe information leak. So these improvements seem ambiguous to me. I would suggest that if the authors continue to claim their method as a prediction model, metric improvements might have to be achieved with careful model designs, to prove the benefit of the proposed language model.
3. Some examples provided in Fig. 1 and Fig. 5 seem not to be correct to my common knowledge:
i) Fig. 1, U-turn, it should be rejected because right U-turn is certainly not permitted in traffic scenes going on the right side. It has nothing to do with whether there is a lane on the right.
ii) Fig. 1, AS and Other feasible direction, their narratives do not correspond, especially on Agent-2 and the Stop Sign's positions.
iii) Fig. 5, Stationary, I don't see strong reasons to reject it, nor do I feel that the reasons provided ban the car from stopping.
These make the figures confusing. My advice is to pick some clearer cases to avoid misunderstandings.
4. A full example of InstructWaymo can be provided as a figure / table to show its contents more clearly and to avoid bulk texts.
5. I hope the authors can clarify on the reason for measuring IFR for INF, and why IFR for INF is the lower the better. Why to test the model's prediction ability with INF instruction during inference, which has no ground-truth in the training stage?
6. On presentations: generally the paper might need to be thoroughly revised to provide a clearer logic on what it is focusing on and what significant improvement it achieves. For example, Fig. 3 should be improved for the streamline and the look. Currently, it looks a little bit messy at the first glance. Various colors mix together, and those purple dotted lines look overwhelming. I would suggest to re-organize this figure to better present the pipeline.
7. Typo: Line 460, it should be "baseline", not "basline".

### Questions
Please see the Weaknesses part for details. Thanks for your reading.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
To adress the issue of mode collapse (the predicted paths are not diverse enough and mainly focus on one driving behavior) in multi-modal trajectory prediction, the author's proposes a novel task *Text-Guided Intention Trajectory Prediction*. The authors raise InstructWaymo to augment WOMD with instruction categories for this task and propose iMotion-LLM to handle this task. Further, the authors introduce two evaluation metrics: Instruction Following Recall (IFR) and Direction Variety Score (DVS), to measure the model’s ability to follow instructions and the diversity of predicted modalities across different directional categories.

### Strengths
1. It is valuable to study the diversity of predicted modes in multimodal trajectory prediction task.
2. The method (Fig.3) is techincally sound.
3. The experiments are well discussed.

### Weaknesses
1. Lack of concrete task definition. As this paper proposes and studies about a novel task *Text-Guided Intention Trajectory Prediction*, it is very important to give a mathematical definition of this task with clear explanations. For example, the format of the instruction is not clearly stated for a prediction. The lack of task definition makes the paper difficult to follow.
2. The application of this task in real world is not clear. It is confusing how the input instructions can be acquired in the test phase in real-world applications such as autonomous driving. Further, the necessity of such input instructions for trajectory prediction in autonomous driving is also not clear, although I suggest that the instructions can be useful for planning and simulation.
3. Evaluation metrics. For IFR, it is diffucult to follow since the format of the input instruction is not clear. For DVS, it is not the case that greater diversity means better prediction results. Although DVS can evaluate the diversity of predictions, it does not reveal the accuracy of each prediction. 
4. Some statements are not supported by evidence or references. For example, "Although previous models can predict multi-modality trajectories, the predicted paths are not diverse enough and mainly focus on one driving behavior" in L48.

### Questions
1. The motion behaviors are categorized to directions, speeds and accelarations, which are symbols and numerical values. I have a question that although LLMs can describe these categories with natural language, can it be a better choice to use primitives or meta-programs (like a tuple of [dir: 0-7, speed: 0-4, acc: 0-8]) as a descriptor, which can be much more easier and intuitive. Why or why not?

### Soundness
3

### Presentation
2

### Contribution
2
