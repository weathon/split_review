# AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
Autonomy via agents based on large language models (LLMs) that can carry out personalized yet standardized tasks presents a significant opportunity to drive human efficiency. There is an emerging need and interest in automating web tasks  (e.g., booking a hotel for a given date within a budget). Being a practical use case itself, the web agent also serves as an important proof-of-concept example for various agent grounding scenarios, with its success promising advancements in many future applications. Meanwhile, much prior research focuses on handcrafting their web agent strategies (e.g., agent's prompting templates, reflective workflow, role-play and multi-agent systems, search or sampling methods, etc.) and the corresponding in-context examples. However, these custom strategies often struggle with generalizability across all potential real-world applications. On the other hand, there has been limited study on the misalignment between a web agent's observation and action representation, and the data on which the agent's underlying LLM has been pre-trained. This discrepancy is especially notable when LLMs are primarily trained for language completion rather than tasks involving embodied navigation actions and symbolic web elements. In our study, we enhance an LLM-based web agent by simply refining its observation and action space, aligning these more closely with the LLM's capabilities. This approach enables our base agent to significantly outperform previous methods on a wide variety of web tasks. Specifically, on WebArena, a benchmark featuring general-purpose web interaction tasks, our agent \codename surpasses the previous state-of-the-art and concurrent work by 9.8 (+29.4\%) and 5.9 (+15.8\%) absolute points respectively, and boosts the success rate by 26.6 points (+161\%) over similar plain web agents with its observation and action space alignment. We achieve this without using in-context examples, new agent roles, online feedback or search strategies. \codename's simple design highlights LLMs' impressive zero-shot performance on web tasks, and underlines the critical role of carefully tuning observation and action spaces for LLM-based agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work focuses on developing a simple generalized framework for LLM-based web agents, allowing them to leverage the strengths of LLMs to get complete web tasks. This framework focuses on aligning LLMs to the web domain and hence converts the problem to that of finding alignments/mappings in observation and action space between web domain and LLMs. As part of that, for action space alignment, they reduce actions to simple set of actions and add few additional "planning" related actions to the set. For observation space alignment, they propose to simplify the web page representation and also focus on selective representation of history for tracking. They show impressive results of the impact of these strategies on WebArena benchmark while also providing ablations to understand the impact of each of the recommended change. Finally, they show how this simple baseline agent can be promisingly combined with existing strategies.

### Strengths
The following are the major strengths of the paper:
-  They have focused on the first principles of building a domain-specific agent, i.e., a web agent and hence utilized domain-knowledge to optimized how LLMs can be used in the best way for this domain.
- The ablations presented are very well presented allowing the reader to understand the impact of each of the changes proposed in the paper.

### Weaknesses
 - The results are shown on WebArena which is a simulated environment. It would be more realistic to see how it performs on WebVoyager which is more realistic in terms of how web behaves.
- The tree representations used for planning needs better explanation. I have to honest that I couldn't grasp it as well as I would want to. While I understand it in principle, presenting it with a more detailed example, even if in Appendix, might help someone like me look into the details of it.
- While the methodology/process presented in this paper of "optimizing/aligning LLMs to the domains when designing agents" is very important and valuable, it is worth noting that the specific proposed changes themselves (understandably) don't generalize to other domains beyond web.
- Minor typo in title of Sec 5 (not a weakness obviously but would be good to fix in the final version).

### Questions
- I would be curious to see how the agent performs on other benchmarks, especially WebVoyager. This is especially valuable benchmark as besides being more realistic, it will help answer my next question.
- The ideas presented in this work are extremely similar to another concurrent work on building a WebVoyager SOTA web agent, Agent-E. There is almost a one-to-one mapping between the proposed changes (both action and observational space) in AgentOccam and Agent-E. 
i. The simplifying of action space in AgentOccam is close to the selection of "primitive actions" in Agent-E.
ii. The Planning tree in AgentOccam is close in principle to "hierarchical planning" in Agent-E.
iii. Simplifying Web Page observation in AgentOccam is same in principle to the idea behind "DOM distillation" in Agent-E.
iv. Selective replaying of observation history in AgentOccam is similar in principle to "change observation" in Agent-E.
And both agents are SOTA on different benchmarks, AgentOccam on WebArena and Agent-E on WebVoyager, and hence would be good to have a detailed comparison, both quantitative and qualitative, between them.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new method for improving LLM-based web agents. The contributions are mainly two folds:

1. Improve alignment between the action and observation space of the web agent and the data on which the LLM has been pre-trained. The authors propose heuristics to: a. Simplify the actions available to the agent and b. Better clean and format the web page observation input for the LLM.

2. New actions and improvement for planning. The authors introduce new `branch` and `prune` actions for altering the plan, as well as prune the web elements included in the historical context.

The authors conduct experiments with WebArena, a web agent benchmark that includes simulation environments across 5 websites.

- The proposed method obtains significant improvement over the base agent design from the original WebArena.
- The proposed method also outperforms the SOTA method on WebArena by 6 points. (Note that the base model is not the same)
- Through ablations, both the action/observation alignment and improvement in planning contribute to the overall bump in performance, with the most gain coming from the action/observation simplification.
- The proposed method can also be combined with another method though the improvement depends on specific agent design. In Step, the proposed method brings improvement compared with Step, though it does not bring further improvement to AgentOccam. When combined with an LLM judge, the authors observe further improvement over AgentOccam.

### Strengths
- The overall experiment results are positive, and new SOTA performance was obtained on the WebArena benchmark.
- The proposed design is simple yet effective, so it should be rather easy to be applied.
- The experiment on WebArena is extensive, with a comparison of multiple base models and ablations to show improvement of individual components.

### Weaknesses
 - The main contribution, and also the main source of improvement, is the simplification of action and observation space. A natural question would be how well these simplifications could be generalized across websites and tasks. Although WebArena contains multiple tasks, it still only contains five websites. To further verify the effectiveness of the proposed method, I would suggest including experiments on other datasets, e.g., Mind2Web, which has more websites.

- Similarly, the alignment could potentially be LLM-dependent. The paper only conducted experiments with GPT-4; it would be better if it could be shown that the method could generalize to different LLMs, which potentially have seen different mixes and formats of training data.

- How to properly represent webpage observation and select the action space has been studied by a few works, both for web agents and web IE, in the past (1) (or, in general, all papers on web agents have touched on this topic). It is appreciated that the authors find a new representation that works very well, but the technical novelty is a bit limited, especially for conferences like ICLR.

1. Zhou Y, Sheng Y, Vo N, Edmonds N, Tata S. Simplified DOM Trees for Transferable Attribute Extraction from the Web.

### Questions
1. Are there experiments on more datasets to show the effectiveness of the proposed heuristic beyond WebArena?

2. Are there experiments with other LLMs.

3. If possible, it would be better to include results using the same base LLM. It is okay to report SOTA on the best LLM available. But for fair comparison and a better understanding of the contribution of the proposed method, it would be very helpful to include results using the same LLM as the baselines.

4. I recommend swapping Figure 5 and Table 10 for the ablation results. The numbers in the table is easier to consume.

### Soundness
3

### Presentation
3

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
This paper proposes a new pathway to improve the performance of LLM-based web agents. Compared with previous works on web agents, it mainly focuses on optimizing the action space and observation space, rather than designing reasoning/planning/memory modules for more complex inferences. The performance on WebArena shows the effectiveness of AgentOccam on web tasks.

### Strengths
Pros:
- The perspective to improve the capability of web agents is great, which it dives into the action space and observation space. It is a common pathway that may take effect in not only web tasks but also other tasks with complex actions and observations.
- I think the action optimization is inspired, especially for abstracting and generating new actions. From my perspective, it is similar to the tool learning problem and can be effective.
- The improvement in performances seems great, where it demonstrates a huge improvement on WebArena.

### Weaknesses
Cons:
- The author claims to solve the generalizability across all real-world applications in the abstract. However, the method section seems to just illustrate how to deal with the specific web environment. There are too many 'specifically' and 'in particular' in sections 4.1 and 4.2. This raises concerns about the practical applicability of the proposed optimizations beyond web-based tasks. For instance, while the paper discusses merging and reshaping elements based on their roles in a webpage's DOM, it remains unclear how these operations would be defined or implemented in non-web environments. Does it mean I need to design different merges manually, where the method is just providing a guide or strategy to conduct the manual process? I think an ideal optimization is to conduct the optimization automatically, even by prompting LLMs. Providing concrete examples of how this approach could be applied to other domains, or discussing any limitations in generalizability would strengthen the paper.
- The lack of a general method to automatically conduct the alignment, especially for the action space, is a significant limitation. The current approach appears to rely heavily on manual design and heuristics, which may not be scalable or adaptable to new, unseen tasks or environments. A more automated approach, perhaps leveraging techniques from reinforcement learning or meta-learning, could potentially enhance the agent's ability to dynamically adjust its action and observation spaces.
- I'm confused about the part 'Replaying Observation History Selectively', could you please demonstrate with more details? I think this is an information retrieval process, but I'm aware of how to get relevant information. You may provide a step-by-step example of how the selective replay process works on a sample task. This would help clarify the information retrieval aspect that I'm unsure about. Additionally, you might show more details on how the relevance of information is determined and how this process differs from or improves upon standard information retrieval techniques. Specifically, how does the agent determine which past observations are most relevant to the current step, and what criteria are used to filter or prioritize information from the observation history?

### Questions
Please see the cons. Please point out if I have any misunderstandings, and I'm willing to improve my rating if the author could greatly address my concerns.

### Soundness
2

### Presentation
2

### Contribution
2
