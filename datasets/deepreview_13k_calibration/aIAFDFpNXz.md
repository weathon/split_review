# Cradle: Empowering Foundation Agents towards General Computer Control

- Decision: Reject
- Avg Score: 6.50
- Scores: 5, 5, 8, 8

## Abstract
\label{sec:abstract}
Despite the success in specific scenarios, existing foundation agents still struggle to generalize across various virtual scenarios, mainly due to the dramatically different encapsulations of environments with manually designed observation and action spaces.
To handle this issue, we propose the \textbf{General Computer Control} (GCC) setting to restrict foundation agents to interact with software through the most unified and standardized interface, \ie using screenshots as input and keyboard and mouse actions as output. 
We introduce \projname, a modular and flexible LMM-powered framework, as a preliminary attempt towards GCC. Enhanced by six key modules: Information Gathering, Self-Reflection, Task Inference, Skill Curation, Action Planning, and Memory, \projname is able to understand input screenshots and output executable code for low-level keyboard and mouse control after high-level planning, so that \projname can interact with any software and complete long-horizon complex tasks without relying on any built-in APIs.
Experimental results show that \projname exhibits remarkable generalizability and impressive performance across four previously unexplored commercial video games, five software applications, and a comprehensive benchmark, OSWorld. To our best knowledge, \projname is the first to enable foundation agents to follow the main storyline and complete 40-minute-long real missions in the complex AAA game Red Dead Redemption 2 (RDR2). 
\projname can also create a city of a thousand people in Cities:~Skylines, farm and harvest parsnips in Stardew Valley, and trade and bargain with a maximal weekly total profit of 87\% in Dealer's Life 2. \projname can not only operate daily software, like Chrome, Outlook, and Feishu, but also edit images and videos using Meitu and CapCut. 
With a unified interface to interact with any software, \projname greatly extends the reach of foundation agents by enabling the easy conversion of any software, especially complex games, into benchmarks to evaluate agents' various abilities and facilitate further data collection, thus paving the way for generalist agents.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes General Computer Control (GCC) setting in a pursuit to build foundation agents that can master ANY computer task via the universal human-style interface by receiving input from screens and audio and outputting keyboard and mouse actions. The solution approach backed by LMM is broken into 6 modules - 1) information gathering 2) self-reflection 3) task inference 4) skill curation 5) action planning. and 6) memory. Each of the module is challenging and having it's own pros & cons and it is good to see a pipeline stitched in the paper, whose efficacy is further demonstrated in different categories of tasks. Overall, this is a good systems paper with limited novelty and contribution in the representation learning space.

### Strengths
The system architecture is well thought of. It uses LMMs to generate code functions as semantic-level skills, which encapsulate lower-level keyboard and mouse control.

Codebase has been shared and the appendix is extensive with figures and supporting material, case studies. Hard work has been put, but mostly on the engineering side.

The usage in software tasks is something fresh, although tech is a join of off the shelf SOTA.

Formulation / design of the template prompts is good with example and format. This seems to be in line with Robogen [https://github.com/Genesis-Embodied-AI/RoboGen] philosophy.

### Weaknesses
To establish the approach firmly, it is recommended that the authors start the paper with clear input & output example. Fig 15 comes later in Appendix, but is cumbersome to fit in front. The system architecture at front part of paper is too much information right at front, without diving in the actual technical challenges. I think a higher level pipeline [input, output, objective] should have been shown and then specific details on sub-objectives and I/O.

Episodic Memory - there is a lot of important recent work, specifically in egocentric video - FPS. What novelty is bought here is not clear as this is one of the driving factors of success of downstream task [in lieu of earlier skill learning]. The paper does not adequately address how the episodic memory module leverages or differs from existing approaches in egocentric video processing, especially given its importance for downstream task performance.

Reasoning is also handled by LMM as it is, thereby giving credit to the LMM paper, instead of this paper. At least some sort of improvement LMM++ was expected. The paper relies heavily on the reasoning capabilities of the underlying LMM without demonstrating any novel enhancements or modifications to the LMM itself. This raises concerns about the actual contribution of the paper beyond simply applying an existing model.

Not sure if the approach is generalization to different domains and how much depends on perception part? More errors there -> more errors downstream. The paper does not sufficiently explore the limitations of the approach in different domains, particularly concerning the robustness of the perception module. The potential for compounding errors due to perception inaccuracies is a significant concern that needs to be addressed.

### Questions
In terms of action planning, whether PDDLstream could have been explored?

If the pipeline so heavily depends on LMM, then if LMM become very superb in near future as encompassing the architecture internally, then the pipeline might not be needed and go towards dissolution.

How would have Deep RL fared under this scenario with game related rewards?

Is there any LMM query prompting level innovation like chain of thought incorporation

The metrics of evaluation vary per dataset / game / software category. How can this be generalized to reduce human input?

What mathematics and philosophy is behind the fact that this chain of 6 modules will work perfectly, and not any other combination?

Were there any robust human user studies done domain and demography nostic?

I was wondering how will it work for CAPTCHA task?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an LLM powered system/framework for solving tasks by direct observation of screen state (i.e. from pixels) and direct manipulation of computer controls such as  mouse and keyboard. The system comprises of 6 high level modules and the authors demonstrate performance on a range of difficult tasks including open-world game playing and UI navigation on a benchmark of typical computer use/productivity tasks. The novelty lies in the development of a particular framework to use pretrained VLM based controller (as opposed to a model learned from scratch) to perform control from pixels (as opposed to a tailored representation of the state of the world).


Note:
I've updated score after the author rebuttal/clarification.

### Strengths
I do applaud the immense amount of effort that has been put into this work and a big strength of this work is the evaluation across a wide variety of task types that include game and non-game settings. The results presented also seem to be relatively strong. The primary contribution is an exploration of what ingredients are needed to get an LMM like GPT-4o to complete a range of tasks when limited to input via pixels and output via keyboard and mouse actions (vs api's provided by these software) in a similar manner to the way a human would control these systems. The system also has to some degree infer what actions it can take in the world and how to do so which is also challenging to do.

### Weaknesses
I think my primary concerns are around the presentation of the work, overall I found it quite hard to extract takeaways about the design of the system and to understand the experiment results from the *main body of the paper*. This is partly because of the scope of the work and the evaluation scenarios, but I think more could be done to bring the main arguments and results into the body of the paper rather than in the appendices (and the appendices are quite long). Overall I'd encourage the authors to consider more what are they key things they would want a reader to takeaway from the paper (and potentially apply to future systems).

Some specific examples of the challenges I had:
- Its quite hard to understand the design/implementation of the 6 modules in Cradle. Aside from high level descriptions of the *purpose* of the module little information is presented about how they function in the main text. I think parts of the *general implementation* that is currently in the appendix need to move to the main body.
- It is hard to understand the critical differences and similarities between this framework and that used in other systems including ones cited such as, Describe, Explain, Plan and Select, Jarvis-1, etc. Is it the addition of external tools to prompt VLM perception of the scene, or a particular component that you would say is the main advancement in the design of such systems.
- Clearer discussion of the bootstrapping ) the system requires to get started in the various scenarios would be helpful to discuss upfront (e.g. initial skills, and domain information provided in the prompts for each component). It seems like there is quite a bit of upfront work to get Cradle working in a new domain. These are listed in one of the appendices, but some guiding principles/base requirements would be useful for readers to know.  Quantitatively the authors could for example present the number of low-level and composite skills provided for each scenario and the number of generated skills to complete the task successfully.
- A clearer presentation of the quantitative task performance before diving into qualitative analysis of the many different behaviors would make it easier to follow:
	- The paper focuses a fair amount on the results from RDR2, but could better contextualize the tasks themselves (e.g. their difficulty) and the behavior of the system when performing them e.g. how many different discrete actions need to be executed to complete each task—does following an NPC only require executing a single *follow* action (that is my impression after reading the appendix).
	- What is the success rate of the system on RDR2 out of the 5 runs? Do they all compete successfully? 
- The baseline comparisons in section 4.1. do not seem all that useful/informative to me. It is not clear what is being 'ablated' compared to Cradle (GPT-4o) in Table 3. While i think the goal was to try and benchmark in some way against an existing system. I think it would be better to focus on ablations of the different parts of the system itself such as in 4.2. My understanding from reading this section is that the main difference in the Reflextion-like is the lack of "Task Inference" stage, but looking at the ablations in the next section, ablating Task Inference had relatively low impact compared to the other components? Am i understanding this correctly?
- The ablations in 4.2 could be expanded to at least one non-game scenario tasks. The authors present the system as one that **generalizes across multiple domains** and it would be useful for readers to know what elements of the system are most helpful for enabling that generalization or indeed if non-video game domains need the same set of components as video game domains. I'd encourage the authors to run the ablations over the OSWorld benchmark or a benchmark like WebArena (which has wider adoption) that enables automatic evaluation
	- Another ablation that I think would make this a stronger paper is a version of Cradle where the LLM doesn't have access to tools such as Grounding DINO, SAM and others. Is that they key ingredient to make systems like this effective.
- Some of the figures and tables are hard to understand
	- Table 1: What are the units for *"Farm Clearup (Grids Num)"*  and *"Avg Haggling (Count)"*? 
	- Table 1: When you use the plus or minus sign, is that reflecting the range in both directions? Cities Skylines Human population is 415+-416, which would imply some player had -1 population? This table might be clearer if it indicated the min and max separately.
	- Table 4: I think this should be be "Figure" 4. I do find it hard to read, what do the shaded areas represent? They seem to overlap a fair amount, how should we interpret this?
	- Figure 6 is quite busy, the annotations look like the data points being plotted, I don't know if the chart is helped by the connecting lines. It might be more helpful to see average number (and std-dev) of steps per task rather than cumulative steps to allow readers to better understand performance on hard vs difficult tasks. The top half of the figure (the two maps) isn't all that helpful and could give you back space to bring in more information about the system.

I am open to increasing my score, particularly if the authors can help articulate what the main things they think the community should learn/takeaway from this paper (other than the existence of the system)

**Smaller nitpicks (does not affect the score)**

L094: "We managed to prove that commercial software is out-of-box testbeds under our framework." — Not very clear what this sentence means.

### Questions
Are the authors proposing the GCC (General Computer Control) setting as a contribution/novel aspect of this work? Could the authors clarify how the proposed GCC differs from the general approach to learning control from pixels *Human-level control through deep reinforcement learning* [Mnih et al 2016]?
- How is a 'step' defined in the context of the games/cradle? Is one step=one action selected by cradle? How many mouse/keyboard interactions can happen in one step?
- In table 1 are the humans limited in the amount of time they get to spend to complete the tasks?
- How customized do the prompts for each module in Cradle need to be for each domain it is applied to? Is there anything that can be shared across multiple domain without heavy customization?
- What happens to visual information/screenshots during the summarization process into episodic memory?
- In appendix H.4 how is "visual prompting" different from the information gathering used in other scenarios? If the augmented screenshot is not fe d to the information gathering modules, where does it go?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces CRADLE, a modular framework utilizing large multimodal models (LMMs) for general computer control (GCC). The authors evaluate its capabilities on both video games and software applications, illustrating the system's adaptability across various domains. This presents an interesting contribution to the conference and offers valuable insights for advancing agent-based control systems.
The framework is composed of six distinct modules: information gathering, self-reflection, task inference, skill curation, action planning, and memory.

### Strengths
This framework demonstrates considerable complexity, with extensive evaluations across video games and diverse software applications. The use of a standard action space is particularly effective, allowing the framework to generalize across applications with minimal adaptation.

The system's performance is noteworthy; however, it's somewhat unclear to what extent this success is attributable to the baseline human players' lack of expertise in the evaluated games, as they had limited practice compared to the agent, which was afforded many trial steps.

The ablation study, examining each module’s contribution, provides valuable insights.

### Weaknesses
While the evaluations are extensive, the number of runs and human participants remains relatively small to achieve robust statistical significance. Given the complexity and resources required for such evaluations, the authors might consider acknowledging this limitation explicitly in the paper.

While the evaluations are extensive, the number of runs and human participants remains relatively small to achieve robust statistical significance. Given the complexity and resources required for such evaluations, the authors might consider acknowledging this limitation explicitly in the paper.



### Questions
Line 1197: Could the authors clarify the specific visual prompting techniques employed, particularly the extent of manual curation involved? Greater transparency here would help assess the generalizability of the framework.

Were task-specific prompts manually written, or were they generated—at least partially—by LMMs? If generated, what iterative methods were employed to refine these prompts?

Can the authors elaborate on the design rationale for each module, discussing why each module was considered necessary and the factors underlying their inclusion, rather than directly presenting each module?

For novel tasks, how much time and expertise are required to develop prompts and input videos for CRADLE to generalize effectively? An exploration of these requirements could provide a clearer picture of the framework's adaptability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an LLM-powered agent designed to interact with various virtual environments, processing screenshots as inputs and executing actions through mouse and keyboard controls, encapsulated within functions generated by the underlying language model. The agent is composed of several modules, including self-reflection, memory, and action planning. The authors demonstrate the agent's versatility across a wide range of environments, from complex, long-duration open-world action games to planning and decision-making games, as well as everyday software applications like web browsers and image and video editing tools.

### Strengths
This paper presents a well-designed framework that effectively leverages LLMs to build generalized agents capable of performing tasks across diverse domains. The agent's modular design makes it easier to extend or modify specific functionalities for different tasks and environments.

By translating language-based capabilities into embodied actions (using mouse and keyboard inputs), the paper showcases an innovative approach to applying LLMs in environments that require physical interaction without relying on a constrained, manually crafted action space.

The paper includes a comprehensive benchmark covering a variety of tasks, along with a thorough and detailed evaluation. The appendix is also highly informative, providing extensive details on every aspect of the system.

The agent's demonstrated ability to perform tasks in widely-used applications like web browsers and media-editing software suggests strong potential for real-world applications and scalability to more practical, non-gaming environments.

### Weaknesses
In several parts of the paper, the authors attribute the agent’s poor performance on certain tasks to the limited OCR and visual capabilities of the underlying LLM. However, no formal evaluation of these limitations is presented in the main paper. While Appendix E5 briefly discusses GPT-4's perception limitations, it lacks a systematic analysis or quantifiable assessment. The absence of a dedicated evaluation makes it difficult to ascertain the precise nature and extent of these limitations, hindering a complete understanding of the agent's performance bottlenecks. For example, it is unclear how the agent's performance degrades with varying levels of visual complexity or occlusion, and how this impacts its ability to complete tasks.

The visual perception issues are understandable in scenarios with low visibility, such as in the game RDR, but are less justified in standard software applications. When discussing CRADLE's performance on these applications, the authors cite difficulties in recognizing button states and locations due to non-standardized layouts of some tools used, stating that “lacking prior knowledge by GPT-4 leads to the failure of task inference and selecting the correct skills.” This reliance on prior layout familiarity poses a limitation to the agent’s ability to generalize, in my opinion. Ideally, the agent should identify interactive elements based on general characteristics, rather than relying on previously encountered layouts, which undermines its robustness in unfamiliar software environments. The agent's inability to generalize from known to unknown UI elements suggests a fundamental limitation in its perception and interaction model. For instance, the agent should be able to identify a button as an interactive element even if it has never seen that specific button before, based on its visual characteristics and context, rather than relying on memorized layouts.

### Questions
I only have a general question about how the authors propose to address the issues with impaired visual capability. Specifically, in situations like the one cited below as it seems that even if the agent can recognize every object in the scene, it would still struggle due to a lack of "attention" or focus.

> L359: “Additionally, indoor tasks like Search for Supplies are also challenging due to GPT4-o’s limited spatial perception, which finds it difficult to locate target objects and ends up circling aimlessly around the house. Moreover, the room contains numerous interactive items unrelated to the task, resulting in much more steps for the agent to complete the task.”

### Soundness
4

### Presentation
4

### Contribution
4
