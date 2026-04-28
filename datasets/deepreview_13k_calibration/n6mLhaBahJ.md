# HAZARD Challenge: Embodied Decision Making in Dynamically Changing Environments

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
Recent advances in high-fidelity virtual environments serve as one of the major driving forces for building intelligent embodied agents to perceive, reason and interact with the physical world. Typically, these environments remain unchanged unless agents interact with them. However, in real-world scenarios, agents might also face dynamically changing environments characterized by unexpected events and need to rapidly take action accordingly. To remedy this gap, we propose a new simulated embodied benchmark, called  \BENCHMARKNAME, specifically designed to assess the decision-making abilities of embodied agents in dynamic situations. \BENCHMARKNAME consists of three unexpected disaster scenarios, including fire~\fireemoji, flood~\floodemoji, and wind~\windemoji, and specifically supports the utilization of large language models (LLMs) to assist common sense reasoning and decision-making. This benchmark enables us to evaluate autonomous agents' decision-making capabilities across various pipelines, including reinforcement learning (RL), rule-based, and search-based methods in dynamically changing environments. As a first step toward addressing this challenge using large language models, we further develop an LLM-based agent and perform an in-depth analysis of its promise and challenge of solving these challenging tasks.
\BENCHMARKNAME is available at \url{https://vis-www.cs.umass.edu/hazard/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new benchmark, ‘HAZARD’, to evaluate an agent's ability to complete a task in environments with changing dynamics. Specifically, the proposed environments simulate three different unexpected disaster scenarios:  fire, flood, and wind. The three disaster scenarios are simulated based on the ThreeDWorld platform. In addition, the authors evaluate several baselines, including an LLM-based approach, on the newly proposed benchmark. The experimental results show that the LLM-based approach outperforms other methods in most of the tasks.

### Strengths
Originality and Significance:    
The reviewer found the proposed environments interesting. The environment could be valuable in two folds: (1) It evaluates an agent’s capability to adapt to changing dynamics, which is an important capability of an embodied agent. (2) The simulated three hazard scenarios could foster future research on rescuing embodied agents. 
 

Quality:   
The paper is technically sound. The proposed environments and LLM-based policy are thoroughly evaluated. 


Clarity:    
The paper is generally well-organized and easy to follow.

### Weaknesses
1. It seems that the hazard’s effect on the functionality of the embodied agents is not simulated. For instance, how does the fire and high temperature affect the functionality of the agent? Similarly, in the flood scenario, is the agent affected by the buoyancy force and drag force? The reviewer found the simulation of damage to the agents is an important piece of a realistic simulator.   

2. How would the proposed approach address a partially broken embodied agent? Would approaches similar to Zeng [1] work?  

3. The reviewer found the baselines in the experimental section somewhat weak. Comparing existing works, such as Landi [2] for embodied AI on changing environments could make the experimental section more convincing.   

4. Could you elaborate why the MCTS-based method outperforms other baselines in terms of fire step and flood step?

### Questions
Please see the above section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new virtual environment for embodied agents from the perspective of dynamic environmental change in the real world, focusing on unexpected disaster scenarios, including fires, floods, and winds. A benchmark HAZARD is developed to evaluate embodied agents making decisions in dynamically changing environments. Further qualitative results on HAZARD the challenges of dynamic environments to existing baseline agents. Notably, the limitations of reasoning and responding to dynamically changing environments for LLM-based agents are analyzed.

### Strengths
- This work simulates new scenarios of dynamic unexpected disasters for embodied agents. Based on the simplified physical model, the scenes achieve a good balance between realistic physical properties and real-time simulation
- This work provides a new simulated embodied benchmark HAZARD to save valuable items in unexpected disaster scenarios to assess the performance of agents in dynamic simulations. The new benchmark will promote the study and enhancement of the performance of embodied agents in dynamic scenarios
- Under the HAZARD benchmark, the quantitative results on a range of baselines, including LLM-based agents, provide a base performance of all baseline methods in dynamic environments.
- The paper proposes to focus on the ability of embodied agents to respond quickly to environmentally driven changes, and reveal the strengths and limitations of LLMs-based agents based on the results, where the performance of the LLMs-based approach is limited by the dynamic environment.
- The paper is well written and easy to follow with its detailed documentation and open source code.

### Weaknesses
 - The rendering quality and motion effects of the simulated scene are still somewhat different from reality, which may result in some perceptually based agents using camera images that will lead to domain gaps. Specifically, the lack of fine-grained particle effects for fire and the simplified fluid dynamics could impact the performance of agents trained on real-world data or those relying on precise visual cues. The visual fidelity, while a balance with simulation speed, might limit the transferability of learned policies to real-world scenarios.
- The current scenario exhibits a limited scale. While the paper mentions the ability to add assets, the process of creating diverse and complex disaster scenes efficiently is unclear. It's not apparent how the system handles the assignment of attributes to different disaster scenes, such as varying fire intensities or flood levels, and if there are tools or methods to automate or streamline this process beyond manual configuration. The lack of a scalable scene generation process could limit the benchmark's applicability.
- The proposed LLM pipeline has to input the same task description at each step to perform sequential decisions, which is not efficient. This approach of re-prompting the LLM with the full task description at each step raises concerns about computational overhead and potential redundancy. The method does not leverage the sequential nature of the task to maintain a consistent context, which could lead to inefficiencies in both computation and reasoning.
- The mission objectives of the benchmarks are relatively simple, focusing on the task of object rescue, and the benchmarks can be expanded further in terms of mission complexity. The current benchmark primarily focuses on object retrieval, overlooking other crucial aspects of disaster response, such as navigation through complex environments, interaction with dynamic elements (e.g., opening doors, operating machinery), and collaborative tasks involving multiple agents. This limited scope might not fully capture the complexities of real-world disaster scenarios.

### Questions
See Weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new simulated benchmark for interactive agents that focuses on dynamic changes in the environment, caused by fire, flooding or strong winds, which the agent needs to react to dynamically. It provides a simulator, a set of 100 scenes for each of the three tasks (split between train and test) and a language interface that allows LLM-based agents to interact with the environment. Evaluations of LLM and non-LLM agents show that the common-sense reasoning in LLMs is beneficial, but they lack ability to react to dynamic environment changes.

### Strengths
The simulator is an interesting step towards testing agents' abilities in scenarios where the environment is dynamically changing and these changes are uncontrollable by the agent. This seems like a scenario of practical relevance for search-and-rescue applications.

The physics of the fire / flood / wind, albeit simplistic, seem sufficient for meaningful yet systematic changes to occur in the environments. The visual rendering of the effects is sufficiently realistic judging from the photos provided.

It is nice that the benchmark supports language-based descriptions and interaction out of the box to facilitate research on higher level reasoning systems while removing the burden of low-level control and perception if not desired.

Further, the procedural environment generation allows for the creation and evaluation of diverse scenes, so that overfitting to a few environments is prevented.

### Weaknesses
While I like the text-based interface, it also seems like a weakness of the benchmark that it seems primarily designed to evaluate the high-level reasoning capabilities of agents, rather than the potentially more challenging low-level manipulation aspects of these tasks. To put differently, would there be any difference if the benchmark wasn't implemented with a nice graphics pipeline but instead as a fully text-based game a la nethack? My understanding is that at least the main LLM planner method would work without change.

I do acknowledge that the authors try to provide versions of the benchmark that require visual perception of the environment. It would be nice though if a similar array of different options was provided on the action representation side. The current benchmark only supports very high-level actions. It is further unclear whether the RL policy that the authors compare to has all the same privileged observation and action primitive access that the LLM planner has. A fair comparison would be good here.

There is some information that is missing from the paper (see questions below). The paper does provide some videos on their website, but the videos "with agent" did not load for me, which makes it hard to judge how fast the environment changes with respect to the speed of the agent, and thus how challenging the tasks are.

While the current split of train:test is reasonable, it would be nice to investigate certain axis of generalization for the different agents more systematically. E.g. one could specifically test generalization to larger rooms or to new objects etc.

Finally, as acknowledged by the authors, the agent currently has no way of *influencing* the dynamics of the environment, e.g. by putting out the fires instead of working around them. It would be good to add such capabilities to more holistically evaluate disaster responses, but I acknowledge that this is challenging and the lack thereof does not invalidate the contributions of this submission.

### Questions
- is the robot agent itself incurring damages as it moves eg through fire / water?

- is there a way to generate training demonstrations, e.g. for an imitation learning pipeline?

- what simulation speed does the current simulator support? can it be run on headless servers & with multiple workers in parallel? this is important for understanding whether it can support RL workflows.


# Post-Rebuttal Comments

Thank you for answering my review. I appreciate the adaptations to the benchmark, in particular taking environment effects on the agent into account and supporting generalization evaluations.
Overall, I support acceptance of the paper. I also skimmed through the other reviews and the rebuttal seems to at least in part address the concerns of the reviewer that voted "marginally below acceptance", so I will increase my score to accept.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper builds a novel embodied AI environment, addressing the dynamically changing environments. They also provide an API to employ large language models (LLMs) for action selection.

### Strengths
The ability to detect changes and adapt to changes in dynamically changing environments is key to intelligent agents. It is good to see people start to develop environments to address such challenges. The authors also provide support for LLMs to perform action selection.

### Weaknesses
see questions

### Questions
I am curious about how hard are the three environments. Also, which decision-making approaches do you think will dominate in the HAZARD challenge?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
