# Why Solving Multi-agent Path Finding with Large Language Models has not Succeeded Yet

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
With the explosive influence caused by the success of large language models (LLM) like ChatGPT and GPT-4, there has been an extensive amount of recent work showing that foundation models can be used to solve a large variety of tasks. However, there is very limited work that shares insights on multi-agent planning. Multi-agent planning is different from other domains by combining the difficulty of multi-agent coordination and planning, and making it hard to leverage external tools to facilitate the reasoning needed. In this paper, we focus on the problem of multi-agent path finding (MAPF), which is also known as multi-robot route planning, and study the performance of solving MAPF with LLMs. We first show the motivating success on an empty room map without obstacles, then the failure to plan on the harder room map and maze map of the standard MAPF benchmark. We present our position on why directly solving MAPF with LLMs has not been successful yet, and we use various experiments to support our hypothesis. Based on our results, we discussed how researchers with different backgrounds could help with this problem from different perspectives.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the use of LLMs for solving multi-agent path-finding problems(MAPF), focusing on moving multiple agents from start to goal locations without collisions. The study explores whether LLMs, without additional training or heuristic guidance, can effectively generate valid paths for agents in different MAPF scenarios, including simple and complex environments. 
Experiments reveal that while LLMs can solve straightforward MAPF cases with limited obstacles, they struggle with more challenging environments, often failing to generate collision-free solutions. The paper identifies three primary reasons for LLMs’ limitations in MAPF: lack of advanced reasoning, context length limitations, and difficulty understanding spatial map information. Based on these findings, the authors suggest directions for future work to address these limitations and improve LLMs' MAPF performance.

### Strengths
Firstly, the paper is well-structured, and it clearly explains why LLMs may be suitable candidates for MAPF due to their reasoning capabilities and large contextual understanding. It conducts experiments on various MAPF benchmark maps, evaluating LLMs’ performance in different scenarios and identifying specific failure points. The paper’s breakdown of LLM limitations, such as reasoning and spatial understanding, provides useful insights for future improvements in LLM-based MAPF solutions. Different prompt styles and input representations (e.g., text-only, multimodal) are compared, contributing valuable insights into how prompt structure affects LLM performance.

### Weaknesses
The paper does not compare the LLM-based approach with traditional MAPF algorithms (e.g., heuristic search, SAT, or reinforcement learning). Including baseline comparisons would provide a better understanding of how LLMs perform relative to established methods.
It also lacks visualizations of agent paths and collision instances, which would improve clarity and provide a more intuitive understanding of LLM performance. Success metrics focus on whether a solution is collision-free, with limited emphasis on solution quality (e.g., path optimality or efficiency). Detailed metrics would offer a clearer picture of LLMs’ efficacy in generating high-quality paths.

### Questions
The authors can consider including baseline methods like heuristic search or SAT-based MAPF algorithms for comparison. Such comparisons would clarify whether LLMs bring any unique advantage to MAPF. Besides, they can evaluate the generated paths for metrics like makespan, and path length. Including these metrics could highlight the quality of LLM-generated solutions relative to optimal or near-optimal paths.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the feasibility of using large language models (LLMs) for solving the Multi-Agent Path Finding (MAPF) problem. While LLMs have demonstrated success in various fields, this study examines their limitations in handling MAPF due to issues with reasoning capabilities, context length limits, and obstacle comprehension. Experiments on standard MAPF benchmarks show that LLMs perform well on simple scenarios but struggle as problem complexity increases. The authors conclude that current LLMs are insufficient for MAPF without additional improvements or hybrid systems integrating traditional path-planning methods.

### Strengths
- This paper addresses a unique application of LLMs to multi-agent coordination, specifically MAPF.
- The paper identifies general limitations of LLMs in multi-agent coordination tasks, with some illustrative failure cases.
- The discussion outlines the general challenges of using LLMs in MAPF and suggests broad areas for improvement.

### Weaknesses
 - Given that these problems are well-addressed by analytical methods, could the authors elaborate on the concrete advantages of using LLMs for MAPF compared to existing analytical methods?
- As the findings primarily reiterate known LLM challenges (e.g., context limitations and reasoning issues) without introducing MAPF-specific insights or innovations. The relevance to MAPF needs to be clarified. The authors are suggested to highlight any MAPF-specific challenges or insights they discovered.
- The experiments are restricted to simple cases that may not generalize to real-world MAPF tasks, which undermines the strength of the study’s conclusions.
- The chosen prompt design lacks justification as the best approach for MAPF. Without alternative prompting methods or tuning strategies, it is unclear if the observed limitations are universal or specific to this setup.

### Questions
1. How do you justify that the proposed prompt method is the best approach and that its failure indicates no other prompting method can address the MAPF problem? How do you ensure the conclusions are generalizable beyond this specific scenario and prompt?
2. Given that the insights are common LLM limitations, not specific to MAPF, what is the unique benefit of this research? Are there distinct challenges in MAPF that differ from general LLM challenges, making any of the observations particularly relevant?
3. Why use LLMs for MAPF or even SAPF? The necessity is unclear, as these problems can be well-addressed using traditional analytical methods.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the challenge of multi-agent pathfinding using large language models (LLMs). The authors demonstrate that while LLMs have proven effective for single-agent planning and, to a certain extent, for multi-agent pathfinding in relatively simple environments, current LLM capabilities are inadequate for planning in more complex settings.

### Strengths
- This paper effectively highlights the current limitations of LLMs in multi-agent pathfinding (MAPF) domains through experiments conducted across environments of varying complexity.
- The authors provide an analysis of potential reasons behind LLMs’ challenges in effective planning.
- This work could serve as a valuable reference for future research directions in MAPF with LLMs.

### Weaknesses
 - The paper only addresses the limitations of LLMs in centralized planning paradigms. The authors claim to use the history of the agents as input in the prompts. Due to this, the context window limit is reached quite quickly when the number of agents is high. But since the environment is Markov, shouldn’t it be able to decide actions for the agents just based on their current states?
- The methods used to demonstrate the limitations of LLMs are relatively straightforward. Including comparisons to more advanced modular architectures, such as those incorporating memory modules and decentralized planners (e.g., [1, 2, 3]), would have strengthened the analysis—even though surpassing state-of-the-art classical planners is not the primary objective of the paper.
- Overall, the paper feels more akin to a research proposal than a definitive study; it identifies key challenges and proposes future research directions but lacks extensive experimental results demonstrating effective solutions.
- The authors suggest three possible reasons for LLMs' shortcomings in MAPF: reasoning limitations, context length constraints, and difficulty understanding obstacle locations. However, these challenges should also arise in single-agent scenarios, where the agent must similarly reason and interpret obstacles, yet LLMs perform well in those cases. Could the authors provide further insights by comparing single-agent and multi-agent tasks?

### Questions
There are some serious concerns that I have pointed out in the previous section

## Limitations:

The methods used to obtain plans with LLMs are quite simple. It would have been better to have some more sophisticated methods (used in prior literature) to compare and show their failure modes. Just using LLMs for planning might not be a reasonable approach and probably that’s why many of the recent papers come up with more sophisticated methods (different roles with LLMs, decentralization, etc.)

### Soundness
2

### Presentation
2

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
This is a paper that attempts to show that LLMs are not yet a viable option for solving multi-agent path finding (MAPF).  The authors describe a method for prompting an LLM for a solution, checking the output for collisions, and iteratively re-prompting the LLM until a solution is found or until a max number of iterations is reached.  They show that LLMs can solve MAPF problems when the planning problem is simple (such as single agent problems in an empty room with no obstacles) and that the capabilities of LLMs as MAPF solvers break down as the problem becomes more complex (multiple agents and more complex obstacle scenarios). They then discuss three possible causes of the poor performance (LLM’s reasoning capabilities, context length limits, and map “understanding”).

### Strengths
LLMs are indeed experiencing a surge of popularity in a huge spectrum of applications.  Any work that contributes to understanding their limitations is important.

### Weaknesses
1. While it’s true that their method didn’t work well, the authors do not present enough evidence to justify saying “LLMs do not yet work for MAPF” (which is the main claim of the paper).  
2. Experimental results are given in Tables 1-4 without sufficient explanation of the methods.  Would recommend a more concise problem statement in the paper (not appendix) that gives specifics of the scenarios, prompts, LLM outputs, and the collision checker.
3. The justification for why the SBS method the authors describe in the paragraph starting on line 207 is not clear.  Other than providing a method to keep the context length shorter, it’s not apparent why this is a good approach.
4. Many claims are made with little to substantiate them:
a. Line 041: previous work “barely covers multi-agent planning” (Chen2023b and Agashe 2023)
b. Line 047-049: Disagree on the list of previous methods.  It should also include LLMs (Chen et al 2023b)
c. Broad claims about LLMs are made in the section on Understanding Obstacle Locations that do not seem supported by the single example presented.
d. The authors claim (line 428) that the current workflow does not include any tool use, but they use an external collision checker (with little or no description of the checker).
e. The claim made on line 363 “people barely provide any such information online since people have common knowledge of what to do with a map” seems unfounded and there is nothing to support it.
5. There are significant grammar issues throughout.  Some examples:
a. (Line 323) “However, recent studies have shown that long models like GPT4- turbo-128K are not a model whose capacity in 8K length also works when given a 128K-tokens input.”
b. And (line 371) “which is killed by using much more total number of steps than it should”
6. In lines 102-103 the authors say “we hope LLMs can be an alternative model to the current MAPF RL based models without additional training”.  However, they have previously stated that in their formulation, this didn’t work.  At this point, it’s better to say what you observed than what you had hoped for.
7. The authors state on line 201 “It is unclear how well LLMs can solve MAPF problems,” but the main claim of the paper is that they aren’t good at it.
8. In Figure 4, the goal of Agent 1 is (3,1) and the goal of Agent 2 is (2,0), however, Agent 1 ends up at (0,1) and Agent 2 ends up at (0,3). These are not at the goals, and in fact, Agent 2 has moved further away from the goal, so it’s not clear why this is a “validated solution”, except for the fact that they did not collide.  
9. It seems intuitive and not scientifically interesting that success rate drops as the size of the problem grows (Lines 424-426).  
10. The formatting of references seems non-standard.

### Questions
1.  Would comparing to a wider range of baseline methods (other than just 0S and SBS) help substantiate the claim that LLMs are not good for MAPF problems?     
2.  Under Methods: “Following common practices of LLMs” what exactly are these?
3.  The authors mention giving the LLM “stepwise local information” what exactly does this mean?  (I assume it is related to the context window size issue?)
4.  The authors only give the LLM information to solve the “next step” and keep re-prompting until the LLM provides a solution with no conflicts.  How does this affect the global optimality of the solution?
5.  Is there any additional reasoning/evidence for why the SBS method is advantageous (other than the context window length)?  Are there any downsides to the SBS method?  
6.  What is meant by "validated solution" in Figure 4?  The agents do not reach the goals specified in the figure.

### Soundness
2

### Presentation
2

### Contribution
2
