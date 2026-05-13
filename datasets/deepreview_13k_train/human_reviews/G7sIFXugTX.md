# Enhancing Software Agents with Monte Carlo Tree Search and Hindsight Feedback

- Decision: Accept
- Scores: 3, 5, 5, 3

## Abstract
Software engineers operating in complex and dynamic environments must continuously adapt to evolving requirements, learn iteratively from experience, and reconsider their approaches based on new insights. However, current large language model (LLM)-based software agents often follow linear, sequential processes that prevent backtracking and exploration of alternative solutions, limiting their ability to adapt their strategies when initial approaches prove ineffective. To address these challenges, we propose SWE-Search, a multi-agent framework that integrates Monte Carlo Tree Search (MCTS) with a self-improvement mechanism to enhance software agents' performance on repository-level software tasks. SWE-Search extends traditional MCTS by incorporating a hybrid value function that leverages LLMs for both numerical value estimation and qualitative evaluation. This enables self-feedback loops where agents iteratively refine their strategies based on both quantitative numerical evaluations and qualitative natural language assessments of pursued trajectories. The framework includes a SWE-Agent for adaptive exploration, a Value Agent for iterative feedback, and a Discriminator Agent that facilitates multi-agent debate for collaborative decision-making. Applied to the SWE-bench benchmark, our approach demonstrates a 23% relative improvement in performance across five models compared to standard open-source agents without MCTS. Our analysis reveals how performance scales with increased search depth and identifies key factors that facilitate effective self-evaluation in software agents. This work highlights the potential of self-evaluation driven search techniques to enhance agent reasoning and planning in complex, dynamic software engineering environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Large language models have been used to automate repository-level tasks in software engineering. Current models used rigid, hand-crafted rules for decision making in these tasks. However, these constraints can cause these software agents to be less adaptable to long-horizon tasks. This paper proposes SWE-search, a framework incorporating multiple agents and Monte Carlo tree search (MCTS) to perform these software tasks. This framework consists of a search agent to perform exploration over software actions, a value agent for self-learning feedback and a discriminator agent for deciding on actions. The paper also includes empirical comparisons of the proposed approach against currently used software agents.

### Strengths
**Originality:** The three types of agents being trained for the framework are based on pre-existing models. However, novelty arises in the way they are combined to form a automated SE framework.

**Significance:** The use of LLMs for automating SE tasks is already pretty widespread. Significantly improving on the current SOTA would further increase their adoption into more use cases.

**Clarity:** The idea presented was clearly laid and explained well.

**Quality:** The problem is well-motivated and plainly laid out. The intuition behind the proposed framework is conceptually simple and the way the multiple agents in the framework are used is sound and reasonable. The experimental design was sound and the baselines against which their approach was compared were sensible. I appreciated the demonstration for the importance of state information in Sec 4.2.

### Weaknesses
There are however a few concerns that need to be addressed.

1. There were a number of (I think) formatting issues. This resulted in some the equations not making sense.
    - the arguments in the value function on line 193 do not make sense
    - the expected cumulative reward on line 196 also does not make sense.
    - $O$ is never defined

2. Section 3 was very confusing:
    - $t$ is used to refer several different things. In 3.1 it is a state and later it is used to define time step. In section 3.1.1, $t$ is used to refer to action type.
    - In 3.1.1, actions, states and action-types seem to be used interchangeably. I can't tell if the action-types are the states or actions. Fig 1 suggests they are the states in the search tree so why not call them that in all instances?
    - $T$ is not defined on line 190.

3. In Sec 4, I'm not exactly sure what the moatless-adapted baselines entails. I read after under the impression that they are the models using the moatless tools with the strict search restrictions.

4. There is no Table 3. There is, however, a Figure 3 that is a table that is never referenced but the values do not align with the descriptions of Table 3.

5. MCTS is stochastic algorithm. As such the evaluations should be performed using more than one random seed on the evaluation set. This would provide the expected performance wrt solve rate, computation, etc. Most importantly, it would provide some measure of significance testing to see if the results support the claims made by authors about the performance gains of SWE.

### Questions
1. Line 181: Typo in "including"

2. In Equation 1, why is value function not dependent on the context space?

3. In Equation 2, in search and RL, a balance between emphasizing the importance of long-term and short-term rewards is made using a discount factor. The $early\textunderscore depth\textunderscore bonus$ and $late\textunderscore depth\textunderscore penalty$ appear to be an attempt to handcraft this balance. Why not just use discounting?

4. Lines 411-415: I do not understand what that segment is trying to say.

### Soundness
2

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
3

### Summary
The authors propose a new agentic system for software development applications based on frontier models and MCTS. They show that this leads to a performance improvement relative to a separate baseline model across several different LLM engines.

### Strengths
- The topic is very relevant and timely.
- An improvement on the problem tackled here has incredible potential.
- MCTS is a good approach to take for this kind of problem, and finding a good way to integrate it has been thought about a lot, so this work is quite useful to the community.
- This approach is modular enough that it could feasibly be integrated effectively with other approaches, leading to rich future work.

### Weaknesses
 - I think the Brown M&M here is really the citation used for MCTS. MCTS was absolutely not proposed for the first time in Silver et al.'s seminal work (Silver even cites the original paper), and using that here hints that this work is very unpolished. But this citation is just one of the symptoms of a greater problem: this paper is poorly written to the point that it reads more like an advertisement than a technical, scientific paper (lines 346-348 are a good example, but the issues are throughout and I'm not confident this can be solved without a full rewrite). While clarity is often overlooked, I'm not sure the rest of the paper is of the exceptional standards needed to justify getting away with it.
- There are serious typos in a few places (e.g., the paragraph at 92 or all the missing parentheses around citations). I think the work needs---at a bare minimum---a full run-through to correct all these.
- The primary area listed here is wrong. The taxonomy here refers to autonomy and planning in the robotics domain. This work has nothing to do with that.
- The paper only mentions its tested on SWE-Bench Lite later on. That should be clarified in the abstract or, at least, in the introduction. That seems like a big difference to me here.
- There's only a single baseline here (Moatless). I would have expected, say, three different baselines. The multiple LLMs here serve the role of something similar to random seeds in demonstrating that the results aren't a statistical fluke.
- The performance improvement with the baseline seems quite incremental despite all the additional complexity.
- "general value functions" are a particular concept in RL research. The authors need to change that term out.
- SWE-Bench really is not a comprehensive benchmark and should not be said to be one. Not that it's a bad benchmark here, but you should remove the statement saying it is.
- It would be good to swap out the lines in Figure 4(b) and the bars in 5(a) with different styles to make the paper more friendly to both colorblind readers and black and white printouts.

### Questions
Please respond to the above when possible as well.

- What is the exact data flow here? There are a few modules, but how do they actually connect together? The text is quite sparse on that and seems to instead focus on describing only the virtues of their approach.
- What's the change in cost here? How much more expensive is this approach compared to other ones? I would like to see something like Table 1 but with USD API costs.
- Is that doing significantly better on SWE-Bench than the norm? A quick look says no (but they look like contemporary works, so I won't hold it against you, and it is optional to address this question). Would this naturally integrate with some of those approaches?
- Line 479-481 seems highly significant at first glance. Is there a reason that isn't a bigger topic in the paper?
- Can you give more details on the difference between your work and the Alibaba system? Is that contemporaneous work?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes the use of MCTS and LLM self-evaluation to improve the performance of software agents. The agent achieves a strong 23% relative improvement on top of moatless-tools across the SWE-bench lite benchmark with a variety of different foundation models, and shows good results for test-time compute scaling with more environment steps.

### Strengths
- Very well-motivated and natural extension to coding agents
- Clear theoretical presentation of the RL/MCTS setting used
- Strong improvements across a wide variety of foundation models on the SWE Bench lite benchmark
- Promising results for scaling inference time compute with more environment steps

### Weaknesses
 - Line 14: Unclear that the best software agents have “rigid processes”. Indeed, the meatless-tools framework that the authors use has a flexible choice of tools at every single timestep already. I agree with the author's justification that some search is necessary, but this claim should be more accurate.
- Completely unclear what value or reward function that value agent is optimizing in Section 3.1.2. I cannot find a definition for the value in the main paper. Appendix G is also unclear, hard to see why the value function would return values like 40, or 75 in the main paper in Figure 4. There needs to be far more analysis/ablations and justification of this design choice.
- Table 1 has no error bars or confidence intervals, which makes it hard to judge statistical significance.
- Experimental evaluation is limited to the lite dataset with a single agent (moatless-tools), it would strengthen the paper to show improvements on the full benchmark as well with other base SWE agents
- Unclear what prompts are used for the discriminator agent at the end, in general, the paper does not have enough details for full reproducibility
- Comparison to other SWE agents is missing.

Minor: 
- The presentation is overly abstract and general until far later in the paper. It would be helpful for the authors to ground their initial theoretical presentation with concrete SWE examples from the start.
- Inconsistent use of \citep and \cite in the paper, please move in-text cites to \citep

### Questions
- How specific to the moatless-tools agent is the author’s algorithm? While the results on SWE-Bench are impressive, since then other agents have achieved 43% performance on the lite benchmark. (I recognize these agents may have been submitted after the author's results, but some comment on generality is needed)
- A natural baseline for scaling inference time compute would be pass@n and compute matching. Does the MCTS agent beat this simple baseline?

### Soundness
3

### Presentation
2

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
This paper introduces SWE-search, a multi-agent framework that integrates Monte Carlo Tree Search (MCTS) with self-improvement mechanisms to enhance the performance of LLM-based software agents in dynamic repository-level tasks. The motivation is to  enable agents to iteratively refine their strategies using both numerical and qualitative feedback. By facilitating multi-agent debates, SWE-search optimizes the selection of solutions for complex problems through diverse perspectives. In experiments, the authors demonstrate the effeciveness of SWE-search by comparing it with a baseline called Moatless-adapted.

### Strengths
1. The motivation of this paper is clear, in the sense that software development is a non-linear process by its nature. The authors elaborate how their method mimic human work patterns in real world, which makes sense to me. 

2. The idea of using MCTS to search for better solutions is novel.

### Weaknesses
1. The problem is not well-defined. Software development includes various kinds of tasks such as requirement analysis, architecture design, code generation from scratch, patching, debuging, testing, etc. The problem formulation part does not indicate which types of problems they are trying to sovle. In the experiment part, it seems that SWE-search aims to address issues in existing code bases. But it is still unclear how this problem is formulated as a sequential decision making problem. For example, in line 206, the authors describe the action space A_t as "a set of actions corresponding to type t". What EXACTLY are these actions? code generation? code repair? Overall, the problem formulation seems to be a general MDP-like formulation, with littel connections to software development tasks. 

2. It is unclear how the value agent evaluate actions. It makes sense to me that the feedback is divided into an utility value and a piece of explanation. However, I doubt whether a normal LLM could provide accruate values to the SWE agent. Recall that in reinforcement learning, a value function is crucial to policy learning, and learning the value function is a very hard task. In software development, the value function should provide comprehensive testing results for given code and requirement list. Given the high-level descriptions in this paper, I am not convinced that a normal LLM could provide accurate feedback. 

3. It is unclear how the MCTS runs. The authors only describe a way  to compute UCT in equation 3. However, many key information is missing, For example, what are the solutions we are searching for? What are the nodes (states) and edges (actions) in the context of software tasks? How to perform a node expansion? 

4. Lack of justification of the Discriminator agent. Intuitively, if the value agent is accurate and the search algorithm works well, we would not need a multi-agent debate process. 

5. Lack of baselines. Since the contributions of this paper mainly lie in the multi-agent framework, including the MCTS search, it is necessary to compare with existing Agent-level framework such as MetaGPT, ChatDev and GPT-Engineer. However, the authors only compare SWE-search with moatless-adapted.

### Questions
Please respond to the questions in the Weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
