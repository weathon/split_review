# VeSX: A Framework Featured by Verification, Self-Correction and In-context Learning for Web Automation Tasks

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 5, 6, 3, 3

## Abstract
While large language models have achieved remarkable success in tasks such as reasoning and question answering, applying LLMs to interactive tasks like web automation remains challenging. In web automation, existing planning-execution workflow often faces limitations due to the infeasible subtasks. We propose VeSX, a framework designed to enhance subtask feasibility through verification, self-correction, and in-context learning. VeSX introduces three key improvements: (1) subgoal-guided verification, which verifies the execution results of subtasks based on the preset subgoals; (2) hierarchical self-correction, which combines reflection and replanning, targeting to self-correct mistakes in both planning and execution phases; (3) exemplar bank, which improves in-context learning by partitioning execution trajectories and heuristically generating metadata for exemplars. We evaluate VeSX on WebArena benchmark and achieve the state-of-the-art average success rate of 0.34, which significantly outperforms existing methods without human guidance on all five scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
VeSX is a framework for interactive web automation tasks using LLMs that focuses on improving sub-task feasibility, a common issue for planning based methods that initially break down tasks into multiple steps before execution. To improve sub-goal feasibility, VeSX introduces three components: sub-goal guided verification, which verifies either with the model itself or external methods if the sub-task is feasible. The second is a hierarchical self-correction method that takes place when verification fails during planning as well as during execution. Hierarchical self-correction uses reflection to correct verification errors, and replans if necessary. Lastly, VeSX uses an exemplar bank for in-context learning for both planning and execution. Unlike previous uses of in-context learning, the VeSX exemplar bank does not use full trajectories, instead sampling from existing trajectories to build the examples. For evaluation, VeSX uses 5 scenarios from the WebArena benchmark.

### Strengths
- Identifies key weaknesses in current methods for web automation
- Method tries to account for different types of failures through the dual verification system and self-correction
- Notable observations as part of method:
    - A) It is easier to verify then come up verification for different goals 
    - B) Having the LLM output expected results as part of reflection 
- Exemplar bank: I think this is one of the strongest contributions since it is very different than existing work in particular using parts of trajectories instead of full trajectories.

### Weaknesses
 - Presentation:
    - I am a bit confused about the overall workflow. It would be helpful to have it written in an algorithm. 
    - It would also be helpful to see more examples 
- Extra Time and Cost:
    - How much extra time and tokens does it take for this method compared to others (if available for other methods)? If these other methods also had access to more compute, they might also have higher performance. 
- Original of exemplars: Are the exemplars produced from questions in the benchmark? Are those questions included in the final results? This could also lead to an unfair comparison. 
- One stated advantage of the approach is that human guidance is not needed. Is any human guidance used to design the prompts for the different steps? Is the exemplar bank used as in-context examples for all of the different steps?

### Questions
In addition the ones listed in the weaknesses:
- How many total tasks are there for each scenario? 
- Out of the 60 sampled tasks for each scenario, how many exemplars were produced? 
- After re-planning is done or self-correction, does the process start from the beginning again? Is there a limit to the number of times self-correction or reflection is allowed? Is this the same as in other papers?

### Soundness
3

### Presentation
2

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
The paper presents VeSX, a framework for enhancing large language models (LLMs) in web automation tasks by introducing verification, self-correction, and in-context learning. VeSX aims to tackle the common challenges in web automation workflows, such as subtask infeasibility and data scarcity, by implementing three key components: subgoal-guided verification, which checks the accuracy of each subtask; hierarchical self-correction, allowing the model to reflect and replan when errors occur; and an exemplar bank for in-context learning, storing structured examples that improve decision-making. Evaluated on the WebArena benchmark, VeSX achieved a state-of-the-art success rate of 34% across multiple scenarios without human guidance, demonstrating its potential to improve accuracy and reliability in complex, multi-step web interactions.

### Strengths
- The web automation task is interesting and worth exploring.
- The proposed self-reflection approach seems to have great improvement in performance, highlighting its potential to enhance task success and reliability in complex, interactive environments.

### Weaknesses
 - The novelty is limited. Compared to previous work on web automation, the paper integrates self-reflection and retrieval-augmentation components, both of which have been widely explored. The paper also lacks discussions on relevant works on reflection and retrieval augmentation.
- The writing needs to be improved, especially in explaining the main components and their novelty.
    * Section 2.1 Overview is empty
    * Clearly indicate success rates as percentages by adding the percentage sign (e.g., 34% instead of just 34)
    * It will be better to put short descriptions in the captions for terms in the table (‘Shop’, ‘CMS’, ‘Red’, ‘Git’, ‘Map’).
    * Adding example prompts would provide readers with a practical understanding of the pipeline.
- Figures need to be significantly improved:
    * ‘orders’ rather than ‘oreders’ in the teaser figure.
    * Miss left bracket for ‘click sorted by]’. Is ‘click [sorted by]’ and ‘click [sortby]’ the same operation?
    * the texts frequently touch or cross the boundaries of the icons.
    * Some figures are blurry and difficult to interpret. (e.g. In Figure 2, it is not clear what the four boxes below the environment represent.)
    * The figure captions should be refined to clearly describe each major component.

### Questions
How does VeSX distinguish itself from approaches like Tree of Thought (which leverages branching and self-verification of reasoning steps), Reflexion (which incorporates self-reflection mechanisms), and various retrieval-augmented frameworks?

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
The authors present a solution to automating web tasks such as checking on shopping orders. The solution leverages LLMs that break down the task into subtasks, executes those subtasks in the browser, verifies the subgoals are accomplished, can self corrects and replan if necessary, and leverages in context examples retrieved from an exemplar bank created by the authors. Experimental results show the authors' superior approach compared to the literature on WebArena, a popular benchmark in the literature.

### Strengths
Summary: 
- Solves a relevant problem
- Adopts a solution that is based on the latest technology
- Beats the state of the art with their experimental results on a well-known benchmark from the literature

Details: 
The problem of automating web tasks is difficult and very relevant in this age of enterprise productivity. Many tasks are quite repetitive and could benefit from automation but the diversity of browsers and apps and tasks makes it challenging for automated systems. 

LLMs have proven beneficial and the paper not only leverages them but also tests GPT-4o which is one of the newest and less costly models compared to others from the literature. 

The proposed framework introduces three key components to the LLM pipeline: 1) sub-goal verification, 2) self-correction and 3) exemplar bank. Each of these components are not particularly original but combining them into a single framework and applying this framework to the web task automation leads to state of the art of results.

### Weaknesses
Summary:
- Limited experimental results and analysis including missing computational cost analysis, error analysis especially when linked to the various contributed components in their framework
- Typing and grammar mistakes

Details:
The experimental results show that the proposed approach (including individual components) do improve the state of the art on the web arena benchmark. The authors compare to other approaches from the literature and do an ablation study on the components they proposed. However, the experimental analysis is still missing some key results that could help the community understand and evaluate this approach better. Notable, the authors perform multiple LLM calls during their pipeline. Quantifying the computational cost (whether with number of calls per input or some other metrics) would help evaluate the approach and compare to other in the literature. Furthermore, the authors do not analyze what errors benefited more from what components in their pipelines. What types of errors needed replanning, which were addressed with reflection only, why did some of the verifications fail, etc. Finally, the authors perform an end to end evaluation but do not evaluate each component individually on intrinsic metrics; e.g., how often was the reflection component able to correct an error that is within its scope, etc.

### Questions
NA

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
4

### Summary
This paper presents VeSX, a framework for web automation that integrates verification, self-correction, and in-context learning mechanisms.

### Strengths
1. The exemplar bank's approach of breaking down trajectories into smaller, reusable components is innovative and practically valuable for reducing context length while maintaining effectiveness.
2. The ablation studies are comprehensive and help validate the contribution of each component.
3. The design of local reflection and global reflection are interesting.

### Weaknesses
1. The literature review on LLM-based agents appears incomplete, missing several relevant recent works
2. About "subgoal-based verification," process supervision is a well-studied research direction[1]. This paper's key difference lies in the hierarchical verification mechanism. However， to prove the effectiveness of hierarchical verification，more comparison experiments and discussions should be made。
3. Although the authors don't use ground-truth labels, their exemplar construction process still utilizes tasks from the target domain. While this doesn't constitute supervision in the traditional sense, it does provide the model with domain-specific information that zero-shot baselines may not have access to, potentially creating an unfair comparison if the baselines are purely zero-shot.

### Questions
See Weaknesses. Further:

1. Could the authors clarify whether the 60 sampled tasks used for creating exemplars overlap with the test set? If so, how do they address potential data leakage concerns?
2. How does the system handle cases where the verification phase produces false positives or false negatives? Is there any analysis of the verification accuracy?
3. How scalable is the exemplar bank approach as the number of tasks and domains increases? Is there a strategy for managing the growing size of the exemplar bank?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents VeSX, a framework designed to enhance web automation tasks by improving the subtask feasibility of Large Language Models (LLMs). It addresses the challenges of error-prone workflows by introducing three key components: (1) Subgoal-Guided Verification, which ensures that subtasks are completed correctly by generating subgoals during the planning phase and verifying the execution results against those subgoals, (2) Hierarchical Self-Correction, which adds layers of error correction during both the planning and execution phases. If mistakes occur, the model first reflects on its actions, and if needed, replans the task, (3) Exemplar Bank for In-Context Learning, which uses stored examples of previous tasks to help the model learn from experience and improve performance on future tasks.

### Strengths
Originality: The paper presents VeSX, a framework that introduces a combination of verification, self-correction, and in-context learning for web automation tasks. The approach is notable for its hierarchical self-correction mechanism, which allows the model to reflect on errors and replan, addressing potential common challenges.

Quality: The idea proposed in this paper is straightforward and clear. The overall structure is clear, despite some minor confusion. 

Clarity: Key concepts such as subgoal-guided verification and hierarchical self-correction are explained straightforwardly, and the diagrams effectively support the explanations.

Significance: VeSX addresses a common issue in web automation—handling subtask failures and error correction. Its ability to autonomously verify and correct errors while using in-context learning is a useful enhancement.

### Weaknesses
While the paper proposes an interesting framework for web automation, the technical contribution feels somewhat limited. The system is more focused on practical application rather than introducing a novel method or algorithm. Additionally, there is no follow-up evaluation of the entire system under real-world conditions. It would be beneficial to see both quantitative and qualitative analyses of VeSX in real-world usage scenarios to better understand its performance in practical settings. E.g., a statistical evaluation or user study focusing on whether this system truly works for real-world tasks would significantly strengthen the paper. A field study or feedback from real users would also provide practical insights into how the system performs in dynamic, unstructured environments.

The concept of "self-correction" is promising, but the evaluation of this feature is not comprehensive enough. Although the paper includes an ablation study, a more detailed analysis of the self-correction mechanism is necessary to demonstrate its effectiveness. For example, breaking down how self-correction functions in different failure cases or assessing the time and resource costs associated with error correction would provide deeper insights into the feature’s utility. 

The paper does not address what happens if the system or specific components fail. While self-correction is included, there is no discussion of how the system handles scenarios where self-correction or verification mechanisms fail. For real-world applications, understanding the system’s resilience and fallback options is crucial. Including an analysis of fail-safe protocols would enhance the system’s reliability and robustness.

### Questions
How would the system perform in a real-world scenario with unstructured tasks and environments? Have you considered conducting a user study or statistical analysis to test its practical application and effectiveness?

While you provide an ablation study, could you expand on the evaluation of the self-correction feature? How does it handle various failure cases, and what are the associated costs (in terms of time, resources, etc.) for error correction?

Beyond its application focus, do you see any potential for extending the technical contributions of VeSX? For example, could the subgoal-guided verification or hierarchical self-correction be applied in other domains?

PS: content under Section 2.1 Overview is missing.

### Soundness
2

### Presentation
1

### Contribution
2
