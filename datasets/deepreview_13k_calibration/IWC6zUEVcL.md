# Towards Evaluating Generalist Agents: An Automated Benchmark in Open World

- Decision: Reject
- Avg Score: 4.00
- Scores: 1, 6, 3, 6

## Abstract
Evaluating generalist agents presents significant challenges due to their wide-ranging abilities and the limitations of current benchmarks in assessing true generalization. We introduce the \textbf{M}ine\textbf{C}raft \textbf{U}niverse (\textbf{MCU}), a fully automated benchmarking framework set within the open-world game \emph{Minecraft}. MCU dynamically generates and evaluates a broad spectrum of tasks, offering three core components: \textcolor{black}{1) a task generation mechanism that provides high degrees of freedom and variability,} 2) an ever-expanding set of over \textbf{3K} composable atomic tasks, and 3) a general evaluation framework that supports open-ended task assessment. By integrating large language models (LLMs), MCU dynamically creates diverse environments for each evaluation, fostering agent generalization. The framework uses a vision-language model (VLM) to automatically generate evaluation criteria, achieving over 90\% agreement with human ratings across multi-dimensional assessments, which demonstrates that MCU is a scalable and explainable solution for evaluating generalist agents. Additionally, we show that while state-of-the-art foundational models perform well on specific tasks, they often struggle with increased task diversity and difficulty.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces MineCraft Universe (MCU), an automated benchmarking framework for evaluating so-called generalist AI agents within Minecraft. MCU consists of three components: a dynamic task generation mechanism, a set of over 3,000 composable atomic tasks, and an evaluation framework supporting open-ended task assessment. The framework evaluates agents across six key dimensions: task progress, action control, material usage, task efficiency, error recognition, and creative attempts. The automated evaluation pipeline can assess open-ended tasks without explicit end states and shows reasonable concordance with human assessments across different dimensions. The authors evaluated VPT, STEVE-1, and GROOT using their framework.

### Strengths
1. **Originality.** The paper includes a creative use of LLMs and VLMs for both task generation and evaluation.

2. **Quality.** The empirical validation showing higher agreement between automated and human evaluation is good. 

3. **Clarity.** I could get the general gist of what the paper is doing.

4. **Significance.** Minecraft is a very interesting and popular domain of study.

### Weaknesses
1. **Lack of code.** The paper does not include anonymized code, which is highly unusual for a D&B paper. This omission significantly hinders the ability to reproduce the results and thoroughly evaluate the proposed framework.

2. **Generally unclear writing.** The paper suffers from several instances of unclear writing, making it difficult to understand the methodology and results. For instance, the statement "We hire 20 people with expertise in the field of Minecraft, and annotate 1 hour of data" is ambiguous. It is unclear whether each person annotates one hour of data or if the total annotation time is one hour. Similarly, the claim "These trajectories exhibit highly similar poses for many steps, thereby increasing the evaluative complexity" lacks a clear explanation of why this is the case.

3. **Incorrect or unclear claims about prior work.** The paper makes several claims about prior work that are either inaccurate or lack sufficient support. For example, the assertion that BEDD does not include a comprehensive evaluation of capabilities is a mischaracterization of the work. BEDD, in fact, introduces a decomposed evaluation framework that allows for comparisons along subgoals and other characteristics. Furthermore, the claim that tasks require long-horizon planning, which reduces composability, is not well-explained. In Minecraft, long-horizon tasks are often considered compositions of simpler tasks, so this claim needs further clarification. The paper also mentions that some prior work fine-tunes foundation models for Minecraft but does not explain why these were not studied or are considered insufficiently general.

4. **Results presentation lacking.** The figures lack error bars, making it difficult to assess the statistical significance of the results. Additionally, the content of Figure 4 is unclear. It is not specified whether it represents an aggregate of all evaluations or specific examples. The large gaps in some evaluations raise questions about the reported Kendall's tau value.

5. **Unclear benefit of use of LLMs.** The paper states that LLMs can "autonomously generate tailored criteria for each task" based on the 6 high-level criteria. However, it does not explain why this is desirable or whether the criteria would be consistent across trials. It is unclear if there is a fixed set of factors for each high-level criterion.

6. **Contradictory evaluation?** The evaluation methodology is described inconsistently. In one section, the paper mentions evaluation options like "a is better," "b is better," "tie," and "both are bad." In another section, it describes scoring intervals as "very poor, poor, fair, good, and excellent." It is unclear which method is used or if both are employed.

7. **Overclaims without evidence.** The paper claims that the evaluation offers "outstanding performance and profound insights" (lines 359-361) without providing sufficient evidence to support these claims.

### Questions
1. Line 330: where do the human gameplay videos come from? This is never specified.

2. 4.2.2 essentially shows the same finding as BASALT: compositional tasks that require creativity and/or deep knowledge of Minecraft are still difficult. Could the others clarify how this finding is different? 

3. Could the authors clarify why the task definition is tool independent? In Minecraft, it would be meaningful to mine dirt with a diamond shovel over a wooden pickaxe. The former would be more efficient and would require traversing more of the tech tree. So I don't think that this task definition makes too much sense.

4. What are the difficulty settings that get introduced? I don't understand how this is systematically implemented.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the MineCraft Universe (MCU), an automated benchmarking framework designed to evaluate generalist agents within the open-world environment of Minecraft. The MCU framework aims to push boundaries in evaluating agent generalization capabilities by generating over 3000 atomic tasks that vary across difficulty levels and integrate compositional complexity. Key features include the dynamic generation of tasks using large language models (LLMs), verification mechanisms for solvability, and a vision-language model-based (VLM) evaluation system that assesses multi-dimensional performance metrics. Experiments reveal that existing generalist agents, while proficient in certain tasks, struggle with more complex and creative tasks. The paper argues for MCU’s contribution to developing robust generalist agents that can generalize and interact effectively in open-world scenarios.

### Strengths
- Comprehensive Benchmarking Framework: MCU introduces a robust benchmarking approach for testing generalist agents. Its combination of task generation, verification, and evaluation creates a solid foundation for assessing performance in open-ended environments.
- Task Diversity and Complexity: The framework’s extensive task library and compositional complexity promote intra- and inter-task generalization, enabling a nuanced understanding of agent adaptability and scalability.
- Evaluation Consistency with Human Judgment: The paper demonstrates that the automated VLM-based evaluations align closely with human assessments, enhancing MCU’s credibility as a scalable, automated benchmark.
- Real-World Relevance: By leveraging Minecraft's open-ended nature and unpredictability, MCU provides a realistic environment that tests generalist agents' adaptability and robustness in dynamic, real-world scenarios.

### Weaknesses
 - Missing important references on data generations for agent benchmarking. The atomic task composition approaches for task generation have been explored in previous works like CRAB: Cross-environment Agent Benchmark for Multimodal Language Model Agents
- Limited Validation with State-of-the-Art Agents: While MCU's evaluation was conducted on several agents, the majority of tested models (e.g., VPT, STEVE-1) represent early-stage developments in generalist AI. The framework’s effectiveness in evaluating more recent, advanced models and agents is uncertain. The selection of agents seems to be limited to those with publicly available implementations, potentially overlooking more sophisticated, albeit less accessible, models.
- Reliance on Minecraft-Specific Dynamics: Although Minecraft provides a useful testbed, the heavy reliance on its specific mechanics may limit generalizability. Results might be biased toward models fine-tuned for Minecraft’s environmental patterns, rather than broader real-world adaptability. The use of Minecraft's block-based world and discrete action space may not translate well to continuous control problems or environments with different physics.
- Insufficient Analysis of Evaluation Metrics: While multi-dimensional evaluation is emphasized, more in-depth analysis of how each metric (e.g., error recognition, creative attempts) impacts generalization performance across task types would clarify MCU's potential in training versus evaluating. The paper lacks a detailed breakdown of how each metric contributes to the overall assessment of agent performance, and how these metrics correlate with each other.

### Questions
- What criteria were used for selecting the 3000 atomic tasks, and how representative are they of a wide range of real-world agent challenges?
- Could the MCU framework be adapted to test agents in other open-world environments, or is it largely Minecraft-specific?
- How well does MCU handle highly complex, multi-step tasks that may require advanced planning or problem-solving strategies?

Minor
- Line 49 Missing citation
- Table 1: Missing space between Benchmark names and citations

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
This paper presents a new agent evaluation benchmark based on the minecraft environment.

### Strengths
- **New incremental improvement over existing benchmarks**: As shown in Table 1 and Figure 2, the proposed benchmark brings clear improvement over [Minedojo](https://github.com/MineDojo/MineDojo), by introducing open-ended tasks, simulation on real game playing, and various difficulty level. The pipeline with automatic task generation and automatic evaluation is also a nice contribution. I believe the engineering efforts could be non-trivial, if reproducible.

### Weaknesses
 - **Overclaims**: I am concerned about potential overclaims made by the authors. I suggest the authors to adjust the tone for more truthful/precise/rigorous presentation. For example:
    - The evaluation environment relies solely on Minecraft. I suggest the authors to explicitly add Minecraft in the title or reflect the ''Open World'' is a simulated one. Additionally, is `generalist agents` well defined and well captured by this specific environment in the paper? I lean towards **no**. As I see it, a more precise description might be `open-ended embodied agents`. I recommend the authors to take a look at [Hughes et al., 2024](https://arxiv.org/abs/2406.04268), where open-endedness is precisely defined. If the authors really want to use ''generalist'', it would be more convincing to include multiple different or realistic environments beyond a single game, like [Gato](https://deepmind.google/discover/blog/a-generalist-agent/) / [AgentBench](https://github.com/THUDM/AgentBench) / [VisualAgentBench](https://github.com/THUDM/VisualAgentBench) / [CRAB](https://github.com/camel-ai/crab) / [SWE-Bench-M](https://www.swebench.com/multimodal.html).
- **Experimentation**:
    - Are all the agents evaluated pre-trained open-source models? Can one use API-based agents (e.g., gemini, gpt) with MCU?
    - How easy can people use the proposed benchmark? Could the author provide code to illustrate? How long does it take for a full evaluation and how much resources would cost?
    - Would you provide a more detailed and clear description for the human rating system in both the main text and appendix?
    - How robust is the evaluation? For example, can the authors try different LLM judges and see if there are any qualitative differences?
- **Writing**: Please improve the writing clarity. I find the paper sometimes hard to follow. (Minor note: many citations (e.g., line 49), section ref (e.g., line 148) and marks (you should use `' instead of "" in latex) are not in the correct format.) Please also consider adding a section on limitations.


I am concerning about the reproducibility of this work and the veracity of the claims. I am happy to raise my score if the authors can make concrete efforts to address the concerns.

### Questions
Please see the weaknesses part.

I am concerning about the reproducibility of this work and the veracity of the claims. I am happy to raise my score if the authors can make concrete efforts to address the concerns.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the MineCraft Universe (MCU), which includes (1) over 3,000 atomic tasks (goals) meant to test basic skills in Minecraft, (2) an LLM-based approach to generating initial states from which the tasks should be executed (aka scene generation), and (3) a VLM-based approach to evaluate whether an agent has successfully completed a task. The goal of this new benchmark is to enable better evaluation of generalist agents that can accomplish a wide variety of goals in Minecraft.

### Strengths
1. Minecraft is an excellent domain in which to test the capabilities of generalist agents, and this is an area that should be of increasing importance over the next few years.
2. The VLM evaluator is a significant contribution: earlier benchmarks in Minecraft were often limited to what could be evaluated with programmatic rewards (e.g. MineRL Diamond), or required expensive human evaluation that limited adoption (e.g. MineRL BASALT).
3. The authors have taken steps to increase the quality of their instruction set, beyond that of e.g. MineDojo.
4. There are evaluations of existing Minecraft agents.

### Weaknesses
## Evaluation

The significance of the paper depends on claims like:

1.  The VLM evaluator provides a robust enough signal that it is useful for evaluating agent performance, and it is better than other comparably cheap evaluation signals in the literature.
2.  The suite of atomic tasks / instructions forms a better training or evaluation set for generalist agents than other benchmarks in the literature.
3.  It is important that the initial state distribution for an individual atomic task is diverse. (This is needed to justify the utility of the LLM scene generation.)

The paper provides decent evidence for claim (1) in Tables 2 + 3, and maybe Figure 4 too, though it would be nice if it also provided interrater agreement (e.g. taking one human’s labels as ground truth, how well does a different human rater perform), to assess how close the VLM is to human performance.

However, I think the justification for claims (2) and (3) are lacking. For claim (2), the obvious comparison is to MineDojo. Figure 2 presents some flaws with the MineDojo instructions, but it isn’t clear whether this is a major problem – perhaps it is sufficient to use an LLM to automatically filter the MineDojo instructions to remove duplicates and only keep ones at a certain difficulty level. To provide better justification for claim (2), the authors could:

*   Cluster the tasks in MineDojo vs MCU, and qualitatively compare the clusters to argue for the benefit of MCU – for example, perhaps when restricting to tasks that are of the appropriate difficulty level, MCU has much larger diversity.
*   Build a pipeline to filter MineDojo instructions for appropriate quality, and show that the number of such instructions is much lower than present in MCU. (It would be important to validate the pipeline, though this could be relatively simple, e.g. reporting ten randomly sampled rejected MineDojo instructions in the paper, and arguing that they are indeed problematic.)

The paper doesn’t present any evidence for claim (3). To fix this, the authors could:

*   Run evaluations of existing Minecraft agents with (a) a single initial state for each task, and (b) the full initial state distribution for each task. Ideally, we would see qualitatively different conclusions with (b) than with (a), demonstrating that the initial state distribution reveals additional information not present when using a single initial state.
*   Finetune a Minecraft agent on a suite of tasks with (a) a single initial state for each task, and (b) the full initial state distribution for each task. Ideally, we would see that (b) produces a much more robust agent.

It would also be good to evaluate the verification pipeline from Mineflayer – for example by reporting what fraction of LLM-generated scenes are rejected by Mineflayer, and using human review to estimate what fraction of those are false positives (i.e. the scenes were possible, but Mineflayer was unable to accomplish the task). However this is less important than the above evaluations.

## Presentation

There are many key details that are necessary to understand and evaluate the paper that are not present, such as:

1.  Details on how the 3,000+ atomic tasks were collected, and what quality control was done to ensure these tasks are of high quality. (Particularly important since the authors claim this as a benefit over MineDojo.)
2.  An explanation of the Mineflayer verification pipeline. My understanding is that Mineflayer is a programmatic bot, whereas the atomic tasks are written in natural language, so how do you provide the atomic task as an input to Mineflayer to verify that the task is possible?
3.  How VPT was evaluated on MCU – to my knowledge, VPT does not take natural language instructions as an input, so it is unclear to me how the task was communicated to VPT. (Perhaps the task was _not_ communicated to VPT, and instead the VPT model was placed in the environment and we simply see if it happens to solve the task in the course of acting – if so, this should be explicitly stated in the main text.)
4.  Prompts for the LLM scene generation and VLM evaluation.

Of course, the paper has many components and so there is not enough space to provide full detail about all the components – but the information should still be present in an appendix. I looked through the appendices and didn’t see any of this information, though I might have missed it.

## Significance

Due to the weaknesses in evaluation and presentation mentioned above, it was hard to evaluate how significant the contributions in this paper are.

The authors emphasize that the atomic tasks evaluate basic skills rather than more long-horizon, agentic tasks. It is unclear to me that this is the right focus – it seems possible that with moderately high-level action spaces (as opposed to raw keyboard / mouse inputs), a frontier vision-language model finetuned for Minecraft would saturate this benchmark in the near future. Of course, the benchmark may still be interesting for the development of agents with more low-level action spaces even after that point, as a proxy for real world tasks that require this (e.g. robotics).

Overall I feel very conflicted about this paper. There has clearly been a lot of good work put into it, and some clear contributions such as the VLM evaluator, but I found it difficult enough to assess what was done and how useful it was that I’m recommending a borderline reject.

## Simple fixes

Figure 4: This figure would be much easier to interpret if the x-axis were sorted in order of increasing human scores. (This would allow the reader to easily check that the VLM scores are also increasing on average.)

Line 150: soverability → solvability

Line 267: Add a citation for Mineflayer

Line 373: Specify in more detail which model you use as VPT(bc) – there are several in [Baker et al 2022](https://arxiv.org/pdf/2206.11795). Is it the VPT foundation model finetuned on earlygame_keyword, or on contractor_house, or both, or something else entirely?

Line 507: The Guss et al citation is for the MineRL Diamond competition; the correct citation for MineRL BASALT is [Shah et al 2021](https://arxiv.org/abs/2107.01969).

Line 1182: Malformed figure reference

### Questions
1. How does the automatic verification pipeline with Mineflayer work? In particular, given one of your over 3,000 atomic tasks, and an LLM-generated initial state configuration, how do you create a Mineflayer bot that can solve the task (assuming it is possible)?
2. Can you say more, ideally with quantitative evaluations, about why the set of atomic tasks in MCU is better than the tasks in MineDojo?
3. How did you collect the atomic tasks in MCU? How did you ensure their quality?
4. How do you provide task instructions to the VPT(bc) and VPT(rl) methods?
5. Why doesn’t Table 4 report numbers for VPT(rl)?
6. What is the interrater agreement for human evaluations?

### Soundness
2

### Presentation
2

### Contribution
2
