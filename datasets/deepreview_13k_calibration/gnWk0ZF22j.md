# Customized Procedure Planning in Instructional Videos

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Generating customized procedures for task planning in instructional videos poses a unique challenge for vision-language models. In this paper, we introduce Customized Procedure Planning in Instructional Videos, a novel task that focuses on generating a sequence of detailed action steps for task completion based on user requirements and the task's initial visual state. Existing methods often neglect customization and user directions, limiting their real-world applicability. The absence of instructional video datasets with step-level state and video-specific action plan annotations has hindered progress in this domain. To address these challenges, we introduce the Customized Procedure Planner (CPP) framework, a causal, open-vocabulary model that leverages a LlaVA-based approach to predict procedural plans based on a task's initial visual state and user directions. To overcome the data limitation, we employ a weakly-supervised approach, using the strong vision-language model GEMINI and the large language model (LLM) GPT-4 to create detailed  video-specific action plans from the benchmark instructional video datasets (COIN, CrossTask), producing pseudo-labels for training. Discussing the limitations of the existing procedure planning evaluation metrics in an open-vocabulary setting, we propose novel automatic LLM-based metrics with few-shot in-context learning to evaluate the customization and planning capabilities of our model, setting a strong baseline. Additionally, we implement an LLM-based objective function to enhance model training for improved customization. Extensive experiments, including human evaluations, demonstrate the effectiveness of our approach, establishing a strong baseline for future research in customized procedure planning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the issue of generating customized procedures for task planning in instructional videos. Existing methods face challenges like overlooking customization and lacking proper datasets. The contributions are significant. It presents a novel setting for customized procedure planning, emphasizing user - specific needs. The Customized Procedure Planner (CPP) framework is proposed, which utilizes LlaVa - based models and is trained with pseudo - labels generated through a weakly - supervised approach. New evaluation metrics are introduced to assess planning and customization quality. Experimental results on CrossTask and COIN datasets show CPP's superiority over baselines like GPT - 4o. The integration of customization loss further enhances performance. Overall, this research lays a strong foundation for future work in customized procedure planning.

### Strengths
1. The paper shows a novel task and CPP framework, using models creatively for generating customized procedures for task planning.

2.It is well-written and clear. The introduction motivates the problem, and the technical approach is detailed.

### Weaknesses
1. The CPP model is trained and evaluated on a specific set of instructional video tasks (mostly related to cooking and DIY activities in the used datasets). It is unclear how well the model would generalize to other types of tasks or domains that have different characteristics and action requirements. For instance, tasks involving complex mechanical assembly, abstract problem-solving, or highly specialized procedures might present significant challenges due to differences in action granularity, visual complexity, and the nature of the required reasoning.

2. The process of creating pseudo - labels using GPT - 4o and GEMINI might introduce some biases or inaccuracies. The reliance on large language models for generating customization details, while efficient, could lead to a homogenization of the generated plans, potentially overlooking the diversity of user needs and preferences. Additionally, the inherent biases present in the training data of these models could be inadvertently transferred to the pseudo-labels, affecting the overall performance and fairness of the CPP model.

3. The interpretation of the "relevance score" for customization quality assessment could be more straightforward. The rubric used to measure customization is somewhat subjective, and it might not be clear how different users would rate the relevance of a plan. The lack of a clear, objective definition for 'relevance' makes it difficult to compare the model's performance across different user groups or tasks. A more rigorous definition, perhaps incorporating specific criteria or user-defined parameters, would be beneficial.

4. The human evaluation seems to focus mainly on validating the model's performance rather than exploring potential areas for improvement. A more in - depth qualitative analysis of the human feedback could uncover additional insights into the strengths and weaknesses of the CPP model and guide further refinements. The current evaluation does not delve into the reasons behind user ratings, which limits the ability to identify specific areas where the model struggles or excels.

### Questions
See details in 'Weakness' section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduce a new task called customized procedure planning (CCP) as an extension to the task of procedure planning in instructional videos. This task generates action plans in natural languages conditioned on user-specific requirements and task objectives, utilizing a weakly supervised approach to overcome the lack of detailed customization annotations in existing datasets. The authors propose a training method, leveraging Large Language Models (LLMs) like GPT-4 for generating pseudo-labels and for enhancing customization through a novel objective function. The paper also introduces new LLM-based metrics to evaluate open-vocabulary, user-specific plans.

### Strengths
1. The introduction of CPPIV is a valuable extension of traditional procedure planning tasks, addressing the limitations of existing models that do not output natural language plan. 

2. The development of LLM-based metrics to evaluate open-vocabulary plan customization and quality is innovative.

### Weaknesses
1. While the new metrics are interesting, the reliance on LLM-based evaluation could be perceived as less interpretable and overly dependent on the LLM’s performance and biases.

2. Rather than simply framing this task as catering to user-specific needs, the primary distinction lies in how the goal is represented. Traditional procedure planning approaches are goal-oriented, often defining the goal using a single image. In contrast, this approach defines the goal using an Objective along with specific Conditions, providing a more nuanced and customizable representation.

3. The paper does not thoroughly address the potential limitations and biases introduced by pseudo-labeling, especially given that human-annotated datasets remain scarce.

4. The results on CrossTask and COIN are also somewhat difficult to interpret. Since these datasets lack ground truth action plans expressed in natural language, the evaluation relies on pseudo-labels generated by LLMs. This introduces a challenge: comparing model outputs, which are also generated by LLMs, against pseudo-labels from the same or similar models raises questions about the objectivity and robustness of the evaluation process.

### Questions
Could you elaborate on the potential biases introduced by using GPT-4 and GEMINI for pseudo-labeling and how they may affect the quality of the generated plans? How does the model handle cases where the user-specified conditions conflict with one another or with the task objective?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
To address the potential challenges of lacking details in action steps in procedure planning in videos, the authors propose Customized Procedure Planner (CPP) framework to predict detailed action steps. They also used foundation models to create detailed action labels for benchmark dataset COIN and CrossTask. They also propose automated LLM-based metrics to evaluate the proposed models, therefore setting baselines.

### Strengths
-The authors pinpoint the problem of lacking detailed action steps in textual form that could distinguish the completion of task in procedure planning. 

-To address this problem, they proposed the CPP framework and leveraged foundation models to train the model with pseudo action labels. The experiments in work is extensive.

### Weaknesses
 -The authors failed to advocate the gravity and scientific significance of the problem (e.g. lack of detailed action steps or user requirements) that they were trying to solve.

-It seems that both are achievable just expanding the input/output spaces of previous tasks.

-The proposed framework lacks novelty. It is a combination of foundation models, designed to solve a very specific task.

-The authors only compare their proposed model with two foundation model baselines.

-Using foundation models to do the evaluation are not robust because the definition of task success is not based on ground-truth.

### Questions
-How is user requirements and detailed action steps fundamentally different from previous task instruction and action outputs? Can I view them as merely adding more detail to the data in the same modality?

-What solving this task matter? Can you prove or is there evidence that it might have impact other fields (e.g. in real world robotics?)

-Have you tried other combination of foundation models to solve your task?

-How should you reproduce your experiment results since commercial foundation model outputs are not reproducible?

-Why choose COIN and CrossTask datasets? There are more recent datasets (e.g. Ego4D).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates a more practical formulation of PPIV that considers user directions, called customized procedure planning in instructional videos.To overcome data limitations, the authors built a novel pipeline to collect customizations from existing PPIV datasets. Finally, a Customized Procedure Planner (CPP) framework (based on Llava) with a customization loss is proposed.

### Strengths
1.  The article investigate an interesting problem, extend conventional procedure planning to open-vocabulary, varied, and detailed instructional plans.
2. The authors propose a weakly supervised training approach that addresses the lack of customization annotations for CPPIV model training.

### Weaknesses
1.  This paper builds a pipeline for generating Customized Plans. The authors need to provide more examples and statistical results to demonstrate the effectiveness of the generated plans. Additionally, most of the keywords provided as examples in the manuscript are materials used in the production process, which does not quite align with the notion of customization.
2. In the data collection pipeline, does the VLM input include a Generic Plan? The prompt in Figure 2 does not seem to contain this information. Does the VLM model have such capabilities or knowledge?
3. In this task, the ground truth (GT) usually consists of gerund phrases, while the model generates full sentences. Could adding related prompts to constrain the model's output improve performance?
4. The authors should provide more examples to demonstrate the effectiveness of the proposed model and modules outlined in the text, Instead of just using numerical results.
5. The impact of the Customization Loss is marginal.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
