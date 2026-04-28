# Improving Autonomous AI Agents with Reflective Tree Search and Self-Learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Autonomous agents have demonstrated significant potential in automating complex multistep decision-making tasks. However, even state-of-the-art vision-language models (VLMs), such as GPT-4o, still fall short of human-level performance, particularly in intricate web environments and long-horizon planning tasks. To address these limitations, we introduce Reflective Monte Carlo Tree Search (R-MCTS), a novel test-time algorithm designed to enhance the ability of AI agents, e.g., powered by GPT-4o, to explore decision space on the fly.
R-MCTS extends traditional MCTS by 1) incorporating contrastive reflection, allowing agents to learn from past interactions and dynamically improve their search efficiency; and 2) using multi-agent debate to provide reliable state evaluation. Moreover, we improve the agent's performance by fine-tuning GPT-4o through self-learning, using R-MCTS generated tree traversals without any human-provided labels. On the challenging VisualWebArena benchmark, our GPT-4o-based R-MCTS agent achieves a 6% to 30% relative improvement across various tasks compared to the previous state-of-the-art. Additionally, we show that the knowledge gained from test-time search can be effectively transferred back to GPT-4o via fine-tuning. The fine-tuned GPT-4o matches 97\% of R-MCTS's performance while reducing compute usage by a factor of four at test time. Furthermore, qualitative results reveal that the fine-tuned GPT-4o model demonstrates the ability to explore the environment, evaluate a state, and backtrack to viable ones when it detects that the current state cannot lead to success. Moreover, our work demonstrates the compute scaling properties in both training - data collection with R-MCTS - and testing time. These results suggest a promising research direction to enhance VLMs' reasoning and planning capabilities for agentic applications via test-time search and self-learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides an overview of MCTS based methods for improved test-time (i.e. inference-time) algorithms for Visual Language Models and tested on the VisualWebArena benchmark for complex web environments. This benchmark is particularly important as it poses a substantial challenge, as VLMs have been shown to often fall short of human-level performance in such tasks, hence any progress in this space is important. The most performant variation of the search algorithm studied in this paper is R-MCTS, which leverages the well known benefits of the traditional Monte Carlo Tree Search (MCTS) algorithm, popular method for improving decision-making in long-horizon tasks with a large action space. Although MCTS has been used in other contacts with a learned world model, this paper is using the WebArena simulator to expand tree nodes. None of the results use the VLM or some other learned model for transitions. VLM is only used for policy and value functions.

R-MCTS extends traditional MCTS by incorporating contrastive reflection and utilizing multi-agent debate. Contrastive reflection allows agents to learn from past interactions and dynamically improve their search efficiency. Perhaps the most impactful design choice is the Memorization of reflection. Reflection embeddings are stored in a vector database and, during inference, relevant reflections are retrieved from the database and appended to the agent's current context, enabling it to learn from past mistakes and improve future task executions. On the other hand, Multi-Agent Debate prompts multiple VLMs to generate individual value estimates, which are then aggregated to produce a final estimate. This approach aims to provide a more holistic view of the current state and encourage stronger reasoning through collaborative/adversarial incentives.

Experiments performed on the VisualWebArena (VWA) benchmark, which evaluates multimodal agents' performance across various web navigation tasks, demonstrated the effectiveness of R-MCTS, with significant performance boosts over alternative search methods.
Moreover, the authors demonstrate that the search trajectories can be effectively transferred back to base models via fine-tuning, resulting in improved performance without requiring search augmentation at test time.

### Strengths
Building agents that are capable of solving complex web navigation using methodologies that are as general as possible will prove to be among the most impactful contributions in the field of AI. The authors are doing a good job to emphasize this and they provide an important contribution in this area, properly aligned with many findings that emphasize the strong VLM capabilities in inference time reasoning and planning.Additionally, the authors demonstrated how easily integrated concepts drawn from human dialogue can be used to improve generic methods. They did this by pinpointing two intuitive modifications to MCTS: contrastive reflection and debating.The boost in performance with the proposed methods is also quite significant, raising the bar on the type of capabilities that can be achieved with the use of LLMs, while also demonstrating the strong potential of scaling up these methods (e.g. longer search horizons, more inference time computations). Lastly, I will point out that the paper is overall well contextualized with respect to the current literature on agentic LLM frameworks, search-based methods for LLMs/VLMs and other inference time algorithms. I would also like to applaud the contributions to SFT-based experiments and emphasizing the importance of generating quality synthetic data, given the cost and logistical challenges associated with human data collection

### Weaknesses
I will perhaps start with what I believe is one of the most important limitations of the work: the use of agent-environment interactions to generate and expand new nodes in the search tree. Unless there is something that I am missing, the search algorithm is based on Alpha-Zero and not Mu-Zero, which essentially means that the results rely heavily on access to a simulator at test time. This should be stated explicitly and the experimental work should be adjusted to account for this rather important detail. In particular, neither ReAct,  nor TreeOfThought (albeit it could be adapted to use the simulator) are presented as a way to enhance agent performance by using an exact simulator. It should be very clear for each of the methods in the experimental section whether the method uses the simulator and if so, to what extent (e.g. how many transitions). Note that I am a strong proponent of using a simulator when available and I also think this should be clarified as a distinct paradigm from a method similar to MuZero, which is fully devoted to a simulator, and hence much more generalizable. At the same time, having access to ground truth transitions can indeed make a huge difference in terms of access to important information, hence empirical results should be presented in a way that makes this use much more transparent. Note that many results in Reinforcement Learning, where agents similarly have access to a simulator, will always report results as functions of “episodes” or “epochs”, both of which are essentially reporting the amount of simulated interactions that an agent has access to. As such, comparing an agent such as ReAct that (AFAICT) doesn’t have access to these simulated transitions, or even another search agent for which readers have no clear understanding of how it works, can be quite misleading.

Figure 1 (left) should be explained much more clearly and that should be done in the captions of the Figure, given that the figure is placed in on the first page. It is great that the reader is given the impact of the work as early as possible. I personally struggled to understand the result both when I first saw it on the first page and after I reached the experimental section and the Figure was explained. First, if the number of tokens for ReAct is not something that can be controlled, then the plot in Figure 1 (a) needs another baseline, e.g. MCTS, Search-Agent. As it stands, the result is stating that the more an agent has access to a simulator to learn about possible trajectories, the better the performance - but I imagine the authors want a stronger message. Similarly, for the Figure on the right side, the plot now discusses actions allowed and “unseen” success rate, which once again seems quite selective and there is no clear message takeaway message. Do you want to convey the fact that SFT on search trajectories allows the model to learn the shortest path?

I would also like to raise concerns about the improvement step, which is essentially doubling down on the advantage of using a simulator by storing embeddings of reflections. This is akin to Replay buffers in Reinforcement Learning. Once again, this seems to be essential to your method, but there is no reason why this improvement step cannot be applied for the other search methods.

Given my take on the main results (i.e. Figure 1) and my comments on the simulator, I would encourage the authors to be more explicit about the significance of the work. As it stands, the message is mostly centered around R-MCTS_{MAD} improving SoTA on VWA, but focus should be given to agents that can utilize the simulator. Obvious candidates for these agents include algorithms like BFS, DFS, and MCTS, and the additional components the authors propose should then be clearly justified and ablated, especially when they can be applied independent of the search method. Note that the same I argument can be made for the multi-agent value function. 

For experiments, perhaps testing more than two underlying models is necessary to better understand the phenomenon of search for VWA, albeit it is understandable if this incurs costs that are too high for their corresponding institution/s. Additionally, empirical results should be much more explicit on the number of simulations that were used in each case. Even for results on SFT where the number of simulations is perhaps irrelevant at test time, it should be clear how many simulations were necessary to build the datasets used for SFT.

I noticed that there is a very clear emphasis on the number of tokens used by either of the methods. I wonder if the authors considered Best-on-N (i.e. generate many candidate trajectories without any search) as a baseline, and if so, why was it not included in the studies? To my point on scaling results such as those presented in Figure 1a, it is important to acknowledge that, as we increase the number of available tokens, there are things simpler than MCTS that could be done and search should only be justified when the performance gap is significant. Additionally, why can’t we increase the size of the search tree for ToT, Search-Agents, MCTS, to match the token consumption of R-MCTS? 

Lastly, as far as novelty is concerned, I stand by my take that the paper is a very interesting study of search methods when a simulator for VWA is provided to the agent and the R-MCTS algorithm is a simple twist to the very popular MCTS. The modifications themselves, whether contrastive reflections, multi-agent debates, or self learning, are, as the authors already made clear, existing concepts with straightforward incorporation with MCTS on VLMs.

### Questions
Since my stance on the paper is strongly grounded on my understanding that the trees for the search algorithms are built with full access to the VMA simulators, I would love if the authors are more descriptive on how experiments were conducted. For context, my assumption is based on the description of the MCTS algorithm in the Appendix, where $\mathcal{T}$ is used to expand new nodes.

### Soundness
3

### Presentation
3

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
The paper presents a novel algorithm improving the capabilities of VLM agents in long-horizon exploration tasks via a combination of MCTS, and value function estimation by reflection and multi-agent debate. The authors show strong results in the VisualWebArena benchmark as well as showing these behaviors can be distilled back into GPT-4o to improve its base performance.

### Strengths
- Well-written and clearly presented paper
- Strong motivation in improving VLM agents in long-horizon tasks
- Novel contrastive reflection proposal that enables a VLM to in-context learn from errors in value estimation
- Thorough ablations over two different value function constructions and individual components of the algorithm 
- Informative analysis of the types of errors the agent makes in Section 5.3.

### Weaknesses
 - Missing relevant multi-step exploration baselines including Reflexion [1] and Intelligent Go-Explore [2]
- The baselines in the main evaluation are not fairly evaluated with equal compute, e.g. does R-MCTS beat ReAct’s 7-shot performance in Table 2? What about ToT’s 2-shot performance? This makes it impossible to evaluate the paper’s contribution. Equally for the self-learning results, would fine-tuning on the best-of-n ReAct trajectories deliver similar improvements in base performance? I would raise my score if the authors could show positive results for this.
- Evaluation is limited to the VisualWebArena benchmark, focusing solely on web navigation tasks. Other VLM domains could include video games, etc.

Minor: 
- Line 11: clarify what kind of autonomous agents, the authors clearly mean foundation model based rather than traditional RL
- MCTS should be attributed to Coulom et al. 2006

### Questions
- Why not also fine-tune GPT-4o instead of the in-context contrastive reflection approach?
- Does the proposed algorithm beat the baselines with equal compute? 
- What is the impact of the size of the reflection database on value accuracy?

### Soundness
2

### Presentation
4

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
The authors propose to improve autonomous AI agents with reflective tree search and self-learning. The authors introduce Reflective Monte Carlo Tree Search (R-MCTS), a test-time algorithm to explore decision space on the fly, with contrastive reflection and multi-agent debate. The authors fine-tune GPT-4o through self-learning, using tree traversals generated by R-MCTS, without any human-provided labels. The authors conduct experiments with VisualWebArena benchmark.

### Strengths
Reflective Monte Carlo Tree Search (R-MCTS) for test-time exploration of decision space
fine-tuning GPT-4o through self-learning

### Weaknesses
A fundamental issue is: 
Given that no LLMs are perfect, so that the data generated  and the evaluations conducted by LLMs are likely not fully reliable, although the algorithm may improve the performance.
It is desirable or a must to collect reliable training data and feedback for a healthy learning system.

### Questions
Why it is valid to
self-generate data from an imperfect LLM,
self-reflect with an imperfect LLM, and
fine-tune an imperfect LLM from data generated by itself?
Is this based on some sound principle?
Although the algorithm may improve the performance, what is the drawbacks and limitations of a learning system trained with data not fully reliable?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a variation of MCTS that exploit the reasoning capabilities of VLMs and that can also be fine tuned.

### Strengths
1. Incorporating VLMs reasoning capabilities into MCTS is a novel idea with great potential.
2. The proposed methodology has been extensively evaluated on a challenging benchmark and significantly outperforms the baselines.
3. Improvements of the benchmark with optimizations that will useful for future works.

### Weaknesses
1. The presentation of the paper makes it hard to follow. For example, in the second paragraph of Section 3.1 the authors say that the mult-agent debate state estimation was introduced in Section 2.3 but in that section they say that the methodology will be described in the next section.
2. The methodology seems to be specifically tailored for the web navigation task, and it is potentially unlikely to generalize to different tasks. A clearer explanation and a better contextualization would improve the clarity of the paper.

### Questions
1. Why is the methodology only evaluated in web? Is it because it requires access to the model of the environment to run the MCTS?
2. Can you please better explain how the simulation step carried out in the algorithm? In vanilla MCTS, it is carried out with random rollout. Is it different in the proposed methodology?
2. In Table 2, you show the results for several search methodology with a different amount of tokens? Would it be possible to have a comparison with a fixed computational budget? I think it would be a more fair comparison with the baselines.
3. I wasn't able to understand what the values in Training column from Table 3 means, can you clarify?

### Soundness
2

### Presentation
2

### Contribution
2
