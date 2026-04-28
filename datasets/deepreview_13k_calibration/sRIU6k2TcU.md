# Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Agents powered by large language models have shown remarkable abilities in solving complex tasks. However, most agent systems remain reactive, limiting their effectiveness in scenarios requiring foresight and autonomous decision-making. In this paper, we tackle the challenge of developing proactive agents capable of anticipating and initiating tasks without explicit human instructions.
We propose a novel data-driven approach for this problem. Firstly, we collect real-world human activities to generate proactive task predictions. These predictions are then labeled by human annotators as either accepted or rejected. The labeled data is used to train a reward model that simulates human judgment and serves as an automatic evaluator of the proactiveness of LLM agents.
Building on this, we develop a comprehensive data generation pipeline to create a diverse dataset, \ourdata, containing \datasetsize events. 
Finally, we demonstrate that fine-tuning models with the proposed \ourdata can significantly elicit the proactiveness of LLM agents.
Experimental results show that our fine-tuned model achieves an F1-Score of \agentperf in proactively offering assistance, outperforming all open-source and close-source models.
These results highlight the potential of our method in creating more proactive and effective agent systems, paving the way for future advancements in human-agent collaboration.
\footnote{Our code and data are available at~\repourl.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the limitations of reactive agent systems by introducing a proactive approach to LLM agents. The authors develop a data-driven method where real-world human activities are collected to generate task predictions, which are then labeled as accepted or rejected by human annotators. These labels train a reward model that simulates human judgment, enabling the agent to anticipate and initiate actions without explicit instructions. The authors create ProactiveBench, a dataset of 6,790 events, and show that fine-tuning agents with this dataset significantly enhances their proactive capabilities. It marks a promising step forward in human-agent collaboration.

### Strengths
I really appreciate the concept of proactive agents, as it addresses a crucial challenge in the planning field: actions should have long-term impacts—a factor often overlooked in prior research. This approach could inspire future agent research to prioritize anticipating future outcomes before choosing actions in the current step. I'm also impressed by the model's performance on ProActiveBench, where it significantly outperforms the GPT series models.

### Weaknesses
The main weaknesses lie in several points:

First, the training process for the proactive agent is not fully explained, particularly regarding the type of annotations used. Besides, while the introduction mentions human-annotated data, it may also cover some portions potentially synthesized automatically. It’s unclear what instructions human annotators followed, how annotation quality was ensured, and how quality control was managed for automatically generated data. Specifically, the paper lacks detail on the annotation process, such as the specific guidelines given to annotators, the number of annotators per data point, and the method used to resolve disagreements. The paper should specify the exact criteria used to determine if a proposed task is 'accepted' or 'rejected' by the annotators, as this is crucial for the reward model's training. Furthermore, it is unclear how the automatically generated data is validated and integrated into the training process, and what measures are taken to prevent the model from learning biases from this synthetic data.

Additionally, the process of maintaining environment state requires further detail. Since this involves using GPT models to generate new states, it raises questions about the accuracy and reliability of GPT in simulating these states. More clarification here would be valuable. The paper does not specify how the GPT model is prompted to generate these states, what level of detail is included in the state representation, and how the model ensures that the generated states are consistent with the previous states. The potential for the GPT model to introduce inconsistencies or unrealistic state transitions needs to be addressed. The paper should also clarify how the generated states are validated, and what measures are taken to ensure the simulated environment is a realistic representation of the real-world scenarios the agent is expected to operate in.

I also have concerns about the comprehensiveness of the tested baselines. For instance, the GPT-based baselines might not fully leverage GPT's potential. Incorporating more chain-of-thought reasoning could lead to more grounded and reliable action predictions, similar to a world model that simulates multiple steps ahead. It would also be insightful to see a comparison showing performance without any proactive agents as a benchmark. The paper should explore more sophisticated prompting techniques for the GPT baselines, such as few-shot learning with demonstrations of successful proactive behaviors. A comparison with a purely reactive agent, which only responds to immediate user actions without any proactive planning, would provide a clearer understanding of the benefits of the proposed proactive approach. The current baselines do not fully explore the potential of existing models, and a more thorough comparison is needed.

Additionally, the evaluation relies heavily on an in-house test set, raising questions about the broader applicability of the proactive agent approach. A more comprehensive evaluation, possibly across varied scenarios, would help clarify its generalizability and robustness.

### Questions
See above. I may also suggest incorporating more examples in the method part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a proactive agent framework designed to predict human intentions based on real-world-inspired environmental observations. To support this, the authors introduce ProactiveBench, a benchmark dataset containing 6,790 events across coding, writing, and daily life activities, capturing user behaviors such as keyboard and mouse inputs, clipboard content, and browser activity.

The data generation process integrates three components: a proactive agent, a user agent, and an environment simulation to emulate realistic interactions. Leveraging human-annotated data, the authors train a reward model that simulates human judgment, achieving 91.8% consistency with human evaluations.

To further enhance the capability to proactively predict human intentions, the authors fine-tuned the LLaMA-3.1-8B and Qwen2-7B. Among these, Qwen2-7B-Proactive achieved the highest accuracy and F1-scores in anticipating user intentions, outperforming both open-source and closed-source baselines.

### Strengths
* The paper presents a well-structured framework for proactive agents, supported by robust experimental design.
* The creation of ProactiveBench provides a comprehensive benchmark dataset that will be highly valuable for future research in proactive language models and user-agent interaction studies.
* The paper employs reinforcement learning to simulate the user agent and model user preferences, enabling a realistic and dynamic approach to assess agent behaviors and refine their decision-making processes.

### Weaknesses
 * This paper lacks sufficient detail in sections such as *Section 3.3: Environment Gym* and *Section 4.1: Reward Model Assessment*, which hinders a full understanding of the framework and evaluation process.
* The paper does not adequately discuss current research on real-world proactive agents or clarify how this work differs from existing approaches.
* The experimental analysis is limited, and the ablation study section is somewhat misleading.

### Questions
* It's unclear whether the environment gym relies on an interactive simulator or is simply text-based.
* The four stages used to describe the environment gym setup seem redundant and could be streamlined for clarity.
* More information is needed on the dataset used for reward model assessment, particularly whether the test data is out-of-domain or in-domain.
* The paper lacks information on the human annotators involved in determining the agreement ratio in the reward model assessment. It is better to provide details on their demographics or annotation guidelines.
* In Proactive Agent Evaluation, it is unclear why Qwen2-7B outperforms LLaMA-3.1-8B despite having fewer parameters. Additionally, the performance gains from fine-tuning on Qwen-7B appear relatively small, which should be further discussed.
* The term *ablation study* seems somewhat misleading here, as this section primarily compares public models in different settings rather than systematically removing or modifying components. Furthermore, it is unclear why the *Predict Multiple Tasks* setting improves overall performance, and additional explanation would be helpful.

### Soundness
2

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
The paper provides a novel approach towards building proactive LLMs. To this end, the authors propose a data collection pipeline on three different types of tasks (coding, writing, daily life). The data pipeline uses Activity Watcher to collect human data (clicks, clipboard, etc.) on these different tasks.

GPT-4o is used to synthetically generate more events and create "ProactiveBench" dataset. They train a reward model to simulate human judgement from some human annotations and create an automatic evaluator of proactiveness. The results show that this reward model is better aligned in comparison to existing LLMs (LLaMa, GPT-4o). 

They fine-tune two models (LLaMA, Qwen) on their Proactive Bench training set and show that this strategy leads to better proactiveness against baselines - measured in terms of precision, recall, accuracy, False-Alarm and F1-Score against the test set. Qwen2-7B based LLM fine-tuned on ProactiveBench achieves 66.47% F1 score, in comparison to 64.60% from GPT-4o. 

They also perform ablation studies where they allow LLMs to output multiple candidates, and a dummy feedback  from their reward model to improve on its prediction - both strategies lead to some improvement in F1.

### Strengths
- The authors attempt to improve on a novel perspective and quality of LLM agents - proactiveness. The way they model this quality is also simple yet interesting - using rewards from user agents. They build a benchmark around this and show effectiveness of their approach towards building proactive agents.
- The design of the reward model and human judgement collection is thorough - they include all possible scenarios and the logic is sound.
- The additional metrics for the agreement ratio are interesting and help provide a better understanding of the performance of various reward models.
- The authors show improved performance against both open-source and closed-source models, when the LLMs are fine-tuned on their ProactiveBench dataset.
- The figures are really good, and they help with the understanding of the approach. The paper is more or less clear (see weaknesses - clarifications).

### Weaknesses
 **General Weaknesses**
- GPT-4o already achieves 64.60% F1, while the author's best F1 score is 66.47%, which is a ~2% relative improvement. The test set (233 events) is not big enough for this difference to be statistically significant. Would be nice to have some discussion on why the authors feel that this improvement will have an impact on future research in this area, considering the fact LLMs keep getting better by the day.
- The experiment is performed against their reward-tuned model, and their own fine-tuned proactive agent, both on subsets of ProactiveBench (please correct me if I am wrong). This casts a doubt on whether actual users will benefit from the approach. Ideally, there should have been some user studies to support this, possibly with unseen events/scenarios.
- The authors do not discuss why they think Qwen performs better than LLaMa and GPT-4o.

**Limitations**
- The authors do not discuss the resource consumption for LLMs when they are proactively predicting tasks on existing systems. A good reason why most LLM agents today are reactive could be because of this issue - it is not possible to have an 7B parameter model constantly running on-device for proactive response generation.
- The authors discuss this in the limitations section - but the gym / agents are in a toy-setting with limited task types. The authors do not perform any real-user evaluations i.e. actually integrating the proactive agent into a system and getting an actual user to evaluate how helpful or disruptive the agent is.

**Missing clarifications/data**:
- Table 4: Can the proactive agents also be used with multiple candidates and with RM? If yes, then this table should contain results for those too.
-  The paragraph describing the human annotation in Section 3.5 could use improvement: 
    - It is not clear what is the "cosine distance" computed against.
    - It is also not clear what "consistency rate" means or how is it measured.
    - What is the annotator agreement on train set?
- How is the GPT-4o explanation for the user judgement used downstream? Is this actually used?
- Section 3.4 - "it first updates its memory with the event" - what kind of memory mechanism is being used?
- Section 4.1 - Setting - How is the LLaMa 3.1 8B-Instruct trained? Are all the layers unfrozen during the training?
- Line 356 - "The temperature is set to 0 during testing." Which temperature? The one used for decoding? This line disrupts the flow of the reading, might be better placed elsewhere.
- Minor:
    - Not sure if I missed this: would be nice to have a well-defined description for what events and scenarios mean.
    - Would be nice to have examples of failure modes (showing scenarios, events, states, predictions), even if in Appendix, for different LLMs in comparison to authors' fine-tuned variant to clarify the differences.

### Questions
- They use GPT-4o for almost the entirety of the pipeline, except for initial user-data, and initial human judgement collection. 
	- How do they ensure that the created scenarios/events and states make logical sense, if they are doing it at scale?

- Not relevant to the paper's strengths/weaknesses: What are the authors' thoughts on being able to tune reactiveness and proactivness? Each user and/or task may have different preferences, is there a straight forward way to control this?

- Line 408 - "In short, while most models can assist when needed, they still frequently offer unnecessary help, even when instructed to provide only essential assistance."
	- Do the authors have any thoughts on how this can be prevented in the future?

- How many events are collected in real-world events? How much is synthetically generated?

- How long are the context windows for the events i.e how many events are used for a single prediction?

- To clarify, the judgement is the only thing that is done from humans? And actions are produced by GPT-4o?

### Soundness
3

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
This paper develops proactive agents—agents capable of initiating tasks without explicit human instructions by simply observing the environmental state and historical actions. This direction is important as it represents a shift from reactive to proactive agents, a very useful characteristic for future agents. 

To train such a proactive agent, the authors propose a data synthesis framework. They utilize GPT-4o to construct a text-based simulation environment called Environment Gym. This 'gym' functions as a sandbox that employs GPT-4o to generate new environmental states whenever agents perform actions. Additionally, the authors prompt GPT-4o to predict proactive actions through a proactive agent module and simulate user interactions to determine whether to accept the predicted actions.

Through this data pipeline, combined with some minor human annotations, the authors curated 1,760 data entries, using 120 of them for testing. The trained proactive agent demonstrates a clear performance improvement over the vanilla LLaMA-3.1-8B model and GPT-4o, which, while notable, is not entirely surprising.

### Strengths
1.  The concept of creating proactive agents is important yet less explored in the field. This paper represents a significant early step in that direction. While proactive conversational models are not entirely new, applying this approach to the realm of agents should be regarded as a noteworthy contribution to the field.

2. The curated benchmark and the proposed proactive agent prompts will serve as valuable resources for the community.

### Weaknesses
One major weakness I identified is the text-based simulation environments. In the current implementation, all environmental changes and updates are managed by GPT-4o. This raises concerns about whether LLMs can accurately reflect true environmental changes. Additionally, this reliance on LLMs could potentially make the benchmark too easy, as they may only be capable of predicting changes that they fully understand and are familiar with, which are also easily solvable by other LLMs. 

After reviewing the entire paper and appendix, I still find myself unclear about the specifics of the dataset. Including some statistics and examples in the main text would be very helpful.

As stated in the introduction, the main contributions of this paper are the data pipeline and the proactive agent. However, the method used for creating this agent is just simple fine-tuning. Without comparison with strong baselines, it's really hard to assess the true effectiveness of the proposed data pipeline.  I understand the difficulty of finding baselines for new problems, but the current evaluation results are not very convincing.

### Questions
Would it be possible to turn text-based simulation into a real interactive environment? 

Can you propose more baselines or analyses to demonstrate the effectiveness of the proposed agent?

### Soundness
2

### Presentation
3

### Contribution
2
