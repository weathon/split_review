# MISR: Measuring Instrumental Self-Reasoning in Frontier Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 8, 5, 3

## Abstract
We propose a suite of tasks to evaluate the instrumental self-reasoning ability of large language model (LLM) agents.
Instrumental self-reasoning ability could improve adaptability and enable self-modification, but it could also pose significant risks, such as enabling deceptive alignment.
Prior work has only evaluated self-reasoning in non-agentic settings or in limited domains.
In this paper, we propose evaluations for instrumental self-reasoning ability in agentic tasks in a wide range of scenarios, including self-modification, knowledge seeking, and opaque self-reasoning.
We evaluate agents built using state-of-the-art LLMs, including commercial and open source systems.
We find that instrumental self-reasoning ability emerges only in the most capable frontier models and that it is highly context-dependent. No model passes the the most difficult versions of our evaluations, hence our evaluation can be used to measure increases in instrumental self-reasoning ability in future models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a benchmark suite called MISR which is composed of various evaluations regarding LLMs ability to modify configuration files to improve on a give task, identify issues with a given tool, knowledge seeking, deceptive / social reasoning and a monitoring task. 

The objective of the benchmark is to identify progress on self-reasoning abilities of LLMs.

### Strengths
I generally liked the discussion in the paper. Discussion on self-reasoning is important and relates to other fields like Theory of Mind, human-AI etc. which are topical. I agree that self-reasoning is going to be very important for autonomous agents and the paper makes an effort in that direction.

### Weaknesses
While I like the direction of the paper, I'm not convinced that the evaluations correspond to self-evaluation. (I'm hoping for some discussion with the author to clarify) : 

Parts that may not be "self-reasoning" : 

- Discuss why is Tool Improvement part of self-reasoning. In this case LLM is acting as a verifier / checker of an external system. I feel access to deceptive tools is a second-order concern for current LLMs (i.e. LLMs should be aware of when tools are deceptive), but even that doesn't seem to be self-reflection. 
- Similarly, why is embedded social reasoning an aspect of "self-reasoning" - which is designed (lines 189 - 191) for devising strategies in social contexts. This is more like opponent modeling / or modeling other agents and responding accordingly. If, the discussion were to be about whether the LLM can self-reason on if its allowed to be deceptive etc. - that may be more in line with paper's goal, but the current section 3.4 seems to be not related to self-reasoning. 
- Knowledge Seeking - the objective seems to be whether the LLM knows about the environment (which is different from knowing about its own abilities). Are the authors not differentiating between an agent & the environment where it lives? For example, a human knowing about their own abilities is closer to self-reason than them knowing about how government of a certain country functions (like knowing about Linux shell env). As in line 182; do the authors not provide information about the environment and expect LLM to browse through shell configuration files to gather the information about the environment?

Self-Modification is more in line with "self-reasoning" but is taken from a prior work as acknowledged by the authors. I don't think this should be counted towards this paper's contributions (as I believe the authors would agree). Regardless, while in spirit the section 3.1 seems more aligned, can the authors discuss : 
-  Do the agents provide information about the configuration files that impacts the task as part of the input prompt? If not, then why is it reasonable for the LLM to be able to guess presence of an arbitrary configuration file for the task. 

Generally, I feel that there are interesting evaluations but not necessarily in line with the central theme of "self-reasoning". 

The other (minor) concern I have is the lack of some human baseline. For instance, would humans be able to guess that  for improving acceleration they have to update a "config.yaml" somewhere in the file system? Some evaluation / discussion on the fact that there is enough information in the input prompt for an LLM / human to be able to achieve the task should be helpful. 

Finally, it seems that some of the tasks in the evaluation category are repetitive as the authors acknowledge (tool improvement checks for errors in python code; self modification looks for updating some config) - can the authors discuss why multiple variations of the same task is helpful? What would be other applications areas (such as beyond changing config files)?

### Questions
Please see "Weaknesses" section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MISR (Measuring Instrumental Self-Reasoning in Frontier Models), a comprehensive suite of evaluations for instrumental self-reasoning abilities in LLM agents. The authors motivate the importance behind evaluating the self-reasoning capabilities of frontier models and design several tasks and evaluation measures toward understanding the quality of self-reasoning. An abundance of results are provided, showcasing that some frontier models can perform this type of reasoning but all models struggle at the most difficult task level. The authors conclude by noting more future work is needed to improve LLM self-reasoning capability, and making this self-reasoning capability transparent to mitigate risks.

### Strengths
Strengths:
+ This work studies an important area of research: evaluating self-reasoning capabilities of LLMs 
+ The paper contains several well-designed tasks and measures for evaluating self-reasoning abilities of LLMs. As state-of-the-art LLMs perform poorly in this suite, this suite can be used as a testbed to test these complex reasoning abilities.

### Weaknesses
Weaknesses:
- Many of the specific details regarding the prompt and task design are found in the appendix. It would be beneficial to move some of this material in the main paper to improve readability. For example, the precise wording of prompts, the specific constraints imposed on the models, and the detailed setup for each task are crucial for understanding the experimental methodology. Without these details readily available in the main text, it is difficult to fully assess the validity and replicability of the results.
- Could you expand on how the results in the Opaque Reasoning Section relate to Figures 2 and 3? It's unclear how the opaque reasoning evaluation, which seems to involve a separate monitoring model and evasion strategies, fits into the overall framework presented in Figures 2 and 3, which appear to focus on task performance and reasoning steps. The connection between these different evaluation approaches needs to be clarified.
- Is there a larger takeaway or recommendation toward future LLM research that these results imply? Does poor current self-reasoning capabilities mean that a human should be in the loop to ensure better LLM performance? The paper concludes by noting more future work is needed, but it would be helpful to have a more concrete discussion of the implications of these findings for the development and deployment of LLMs. Specifically, what are the practical implications of the observed limitations in self-reasoning?

### Questions
- Could you address the specific weaknesses above?
- The authors mention that this work evaluates self-reasoning in agentic settings. Could the authors provide a description of what they mean by "agentic" and whether they feel these results translate to embodied agents (e.g., robots)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a suite of tasks to evaluate potentially dangerous self-reasoning capabilities in frontier models. These tasks measure capabilities such as self modification, tool improvement and knowledge seeking. Their work builds on the UK AI Safety Institute’s “Inspect” framework, and involves having an LLM agent execute bash commands in a container to solve tasks with implicit self-reasoning challenges.

### Strengths
1. This work is highly relevant, and research along these lines will be crucially important as frontier models continue to progress. The authors have identified an important area to investigate and are thinking along good lines.
2. The writing is concise and informative.
3. I like the thorough results in appendix, and a detailed run-through of the prompts used is helpful for understanding exactly what's going on.

### Weaknesses
1. I am concerned as to how novel this work is given Phuong et al’s “Evaluating Frontier Models for Dangerous Capabilities”. The “self modification” task is not novel, whilst “tool improvement” is better but seems slightly unnecessary given the suite of tasks in Phuong et al’s “self-proliferation” section. I would appreciate a more detailed comparison between your tasks and theirs, particularly for the "tool improvement" tasks, explaining how you contribute beyond existing evaluations.
2. The relevance of the “knowledge seeking” task to instrumental self-reasoning seems slightly tenuous. The prompts ask models to explore the environment, and the dangerous behavior is then whether they do explore the environment? Could you please clarify how the knowledge seeking tasks specifically evaluate instrumental self-reasoning rather than simple instruction following.
3. I would like to see confidence intervals on the bar charts.
4. I think that “our evaluations significantly improve upon prior work” and “our results have strong implications for AI safety and development” are overclaims here. I would like to hear a defense as to how this work “significantly” improves upon the highly detailed Phuong paper mentioned above.

### Questions
Please respond to the weaknesses highlighted above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work evaluates the instrumental self-reasoning abilities of several mainstream cutting-edge LLMs in agentic scenarios through five different perspectives on a task that needs to reveal implicit goals, and conducts large-scale experimental analysis. The experimental results show that only the most advanced current LLMs demonstrate some performance in this ability, and none of the LLMs passed the most difficult tasks. The authors believe that these results can draw attention to this capability of LLMs, thereby contributing to AI safety and development.

### Strengths
The work designed a large number of tasks and conducted extensive experiments, the results of which seem to be highly credible and reproducible. At the same time, the author organized these tasks into a benchmark that can be used to evaluate the instrumental self-reasoning ability of subsequent LLMs.

Additionally, researching the instrumental self-reasoning ability of LLMs is a very interesting issue, as it can demonstrate whether LLMs are capable of adjusting their settings through reasoning to perform different tasks in a targeted manner.

### Weaknesses
In terms of writing, the overall structure of this work resembles a technical report. It lacks the completeness and rigor expected of an academic work and does not clearly demonstrate its positioning within the current field or the significance of the research. For instance, it does not highlight the advantages of instrumental self-reasoning compared to self-correction [1] or self-improvement through introspection [2].

In terms of experiments, this work lacks detailed experimental setup information, including task quantity, task sources, and the motivation behind designing these tasks. Additionally, the paper lacks details on the settings for the LLM, such as temperature and seed.

In terms of novelty, I do not see much improvement compared to the instrumental self-reasoning evaluation part of the work [3] cited by the author themselves (the specific experimental task format design as well). The author also mentioned that their focus is on agentic scenarios, which were lacking in previous work. However, I do not believe that [3] lacks this aspect. In fact, this capability itself needs to be demonstrated in agentic scenarios.

### Questions
See the **Weaknesses** section.

### Soundness
3

### Presentation
2

### Contribution
2
