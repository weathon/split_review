# CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation

- Decision: Accept
- Scores: 6, 5, 5, 8

## Abstract
In this work, we address the cooperation problem among large language model (LLM) based embodied agents, where agents must cooperate to achieve a common goal.
Previous methods often execute actions extemporaneously and incoherently, without long-term  strategic and cooperative planning, leading to redundant steps, failures, and even serious repercussions in complex tasks like search-and-rescue missions where discussion and cooperative plan are crucial. 
To solve this issue, we propose Cooperative Plan Optimization (CaPo) to enhance the cooperation efficiency of LLM-based embodied agents. Inspired by human cooperation schemes, CaPo improves cooperation efficiency with two  phases: 1) meta-plan generation, and 2) progress-adaptive meta-plan and execution. 
In the first phase, all agents analyze the task, discuss, and cooperatively create a meta-plan that decomposes the task into subtasks with detailed steps, ensuring a long-term strategic and coherent plan for efficient coordination. 
In the second phase, agents execute tasks according to the meta-plan and dynamically adjust it based on their latest progress (e.g., discovering a target object) through multi-turn discussions. 
This progress-based adaptation eliminates redundant actions, improving the overall cooperation efficiency of agents. Experimental results on the ThreeDworld Multi-Agent Transport and Communicative Watch-And-Help tasks demonstrate CaPo's much higher task completion rate and efficiency compared with  state-of-the-arts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduced Cooperative Plan Optimization into the CoELA framework to improve embodied multi-agent cooperation. A new meta-plan mechanism ensures agents can form and follow a long-term strategic and coherent plan for efficient coordination. Multi-turn discussions following pre-defined templates among agents are triggered whenever new progress is made to adapt the meta plan to progress. The experiments on two embodied multi-agent cooperation benchmarks demonstrate the proposed method achieves better performance than sota.

### Strengths
- Introducing a meta-plan mechanism to ensure agents can form and follow a long-term strategic and coherent plan can improve the coordination's efficiency.

- The paper is clearly written and well-organized.

- The ablation study and qualitative analysis provides valuable insights.

### Weaknesses
 - Since the paper reuses 1) a perception module, 2) a memory module, 3) a communication module, and 7) an execution module from the CoELA paper, it may be better to put the discussion of these modules into the preliminary sections rather than in the method section to make this paper's contribution more clear.

- The contribution is limited since the only improvement is achieved by introducing a pre-defined communication protocol by prompting into an existing CoELA framework.

- The paper uses the same formalization and experiments set up as prior work CoELA, which is not a bad thing. For the main results in Table 1, the column with RHP*, RHP, and LLAMA-2 CoELA is identical as reported in the CoELA paper but with no appropriate notation. In the meantime, only the CoELA baseline's results are changed to use GPT-3.5 backbones instead of the GPT-4 used in the original paper, which also causes a major performance drop (avg. 71 -> 52; 85->72) compared to the reported results in the original paper. Results with gpt-4 are reported as original in Table 2 and Appendix Table 5, where the performance gain is down to 4 points rather than 13 points. Why the results are organized as such needs further clarification.

- One of the interesting settings of the CoELA paper is that they formalized communication as a step that also comes with a cost so the agents need to balance the cost and gain of communication. They make the findings that it's not effective yet for LLM-based agents to communicate spontaneously, which may be part of the motivation for this paper. In this paper, however, it's not specifically discussed whether this costly communication is still employed, and if so, some analysis around the communication cost and corresponding efficiency achieved may provide valuable insights for the community.

- Is the progress-adaptive planning module always triggered whenever there is new progress? How many rounds of meta-plan updates are there on average and how many steps would be used to conduct this meta-plan discussion? Is the communication module also needed after the progress-adaptive planning module makes the update to share it with the others? What happens if two agents make new progress at the same time and all want to be the meta-plan designer? What will happen if agents can't reach a consensus? Will they just have no communication afterward or try to communicate again after how many steps or stuck at arguing every few steps?

- Minor typos:
  - L70: typo, 'sever' -> 'several'

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Cooperative Plan Optimization (CaPo) to improve cooperation among LLM-based embodied agents. Existing methods lack strategic planning, leading to inefficiency and failures in complex cooperative tasks. CaPo enhances cooperation through two phases: meta-plan generation and progress-adaptive execution. In the first phase, agents collaboratively analyze the task and create a strategic plan with detailed steps. In the second phase, agents execute and adjust the plan dynamically based on real-time progress, supported by ongoing multi-turn discussions. This progress-based adaptation prevents redundant actions and boosts overall task efficiency. Empirical experiments on the ThreeDworld Multi-Agent Transport and Communicative Watch-And-Help tasks demonstrate CaPo’s superiority in task completion and efficiency.

### Strengths
1. The paper is well-written and easy to follow. The figures and illustrative examples help demonstrate the effectiveness of the proposed progress-adaptive meta-plan.
2. The related work section is sufficiently comprehensive, providing a clear context for the study.
3. Complex ablation studies on each module of CaPo, the effect of agent number, and convergence analysis.

### Weaknesses
1. This work appears to be a straightforward extension of CoELA, with minimal innovation beyond basic prompt engineering for the meta-plan module. The problem setting and agent framework largely mirror those of CoELA. For instance, as noted in Section 4.1, the CaPo agent comprises seven modules: 1) perception, 2) memory, 3) communication, 4) cooperative planning, 5) progress-adaptive planning, 6) plan parsing, and 7) execution. The CoELA agent already includes five of these, lacking only the cooperative planning and progress-adaptive planning modules, while these 2 modules can be easily implemented by prompting LLM.
2. The authors limited their experiments to the TDW-MAT and C-WAH testbeds, which are already used in CoELA. To demonstrate the broader effectiveness of their method, it would be beneficial to include experiments in new and varied environments.
3. The process of updating the meta-plan relies on broadcasting communication among agents, which incurs significant communication costs.

### Questions
1. Can the authors elaborate further on their contributions compared to CoELA? The current presentation does not sufficiently highlight the novelty of this work.
2. Would the authors consider conducting additional experiments in different environments to better demonstrate the generalizability and effectiveness of their method?
3. Is it possible to reduce the communication cost by replacing the broadcasting communication mechanism with a different network design?
4. In Figure 8, the authors claim that consensus is typically reached within 3 rounds. However, over 20% of trials still fail to reach consensus after 3 rounds. Is setting the discussion budget to 3 rounds a reasonable choice given this observation?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the Cooperative Plan Optimization (CaPo) framework, which aims to enhance the long-term planning cooperation efficiency among Large Language Model (LLM)-based embodied agents. CaPo includes two-phase: meta-plan generation and progress-adaptive meta-plan and execution. Experimental results on the TDW-MAT and C-WAH tasks demonstrate CaPo's significant improvement over state-of-the-art methods.

### Strengths
The paper introduces a novel two-phase planning approach, Cooperative Plan Optimization (CaPo), which addresses the limitations of single-step planning in CoELA. This approach demonstrates its effectiveness through experiments on the TDW-MAT and C-WAH environments.

### Weaknesses
The main content of the article appears to be an extension of CoELA[1], enhancing its single-step planning approach by incorporating multi-turn discussions after the execution phase. Meanwhile, several works, for example, [2,3] have already demonstrated multiple rounds of discussions in various contexts, so the novelty and significance of this article's contribution seem somewhat lacking.

Additionally, I confess that I am not familiar with ThreeDworld Multi-Agent Transport (TDW-MAT) task, and the Communicative Watch-And-Help (C-WAH) task, so I am not quite clear on how to assess their complexity. However, for works [4,5,6] based on Minecraft, which typically evaluates dozens or even hundreds of tasks. I am cautiously skeptical about whether considering only 6 or 10 target tasks in food and stuff settings is sufficient to thoroughly validate the capabilities of the proposed framework. How the complexity of TDW-MAT and C-WAH tasks compares to Minecraft tasks? Whether you have plans to evaluate on a larger set of tasks in future work?

In the ablation study, the paper mentions the impact of the number of agents, but the game appears to only contain two players, Alice and Bod. I'm confused about the number of agents. Please clarify how you tested different numbers of agents if the main experiments only used two.

### Questions
In the ablation study, the paper mentions the impact of the number of agents, but the game appears to only contain two players, Alice and Bod. I'm confused about the number of agents. Please clarify how you tested different numbers of agents if the main experiments only used two.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a method called CaPo, which uses LLM agents having multi-turn conversations with each other to create meta-plans (a collection of subtasks for solving the overarching problem that are assigned to each agent). Not only does it precompute these tasks, it dynamically adjusts them over time as agents perceive new information or interact with objects in ways that impact the preexisting plan. By testing on realistic simulators emulating embodied household tasks, the authors show the efficacy of the approach compared to conventional LLM approaches and classical symbolic planners.

### Strengths
The authors did a nice job ablating the different modular components of their agent architecture. Oftentimes in the LLM agent literature plans are either made in a single-turn or an agent just refines what to do in its own mind, but introducing multi-turn group communication seems like an effective strategy if one has enough of a communication budget. The architecture itself seems highly reproducible, the benchmarks are challenging, and the impact of which LLM underlies communication is thoughtfully examined.

### Weaknesses
The experiments could benefit more from being evaluated on real humans collaborating with LLM agents on tasks such as Watch and Help. If the ultimate goal of this line of work is to build embodied agents that help humans, understanding how real humans complete the task differently with different agents is key. Extra evaluations could show the same efficiency metrics but also metrics indicating which agents human preferred playing with. If CaPo is very verbose when making plans, humans may not prefer interacting with it despite the efficiency gains compared to a method like CoELA. It would be interesting to dissect this. 

Moreover, an analysis of the runtime cost of CaPo would be nice to see. If a multi-round discussion is needed to reformulate a plan every time new information is discovered, how long does this take? How long can prompts end up being for the LLMs (how large does the memory grow as well) and does the duration of an episode/memory size impact planner quality?

### Questions
What is the standard error for the metrics shown in Table 1? 

What is the runtime of this method at each turn? Can it be run in real-time with humans and how does planner quality change as a function of time?

Nice to have - what are results from playing this method with humans compared to other baselines? What do humans prefer?

### Soundness
4

### Presentation
4

### Contribution
3
