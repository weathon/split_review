# How language models extrapolate outside the training data: A Case study in Textualized Gridworld

- Decision: Reject
- Scores: 5, 3, 5, 5, 8

## Abstract
Language models' ability to extrapolate learned behaviors to novel, more complex environments beyond their training scope is highly unknown. This study introduces a path planning task in a textualized Gridworld to probe language models' extrapolation capabilities. We show that conventional approaches, including next-token prediction and Chain of Thought (CoT) fine-tuning, fail to extrapolate in larger, unseen environments. Inspired by human cognition and dual-process theory, we propose \textit{cognitive maps for path planning}—a novel CoT framework that simulates human-like mental representations. Our experiments show that cognitive maps not only enhance extrapolation to unseen environments but also exhibit human-like characteristics through structured mental simulation and rapid adaptation. Our finding that these cognitive maps require specialized training schemes and cannot be induced through simple prompting opens up important questions about developing general-purpose cognitive maps in language models. Our comparison with exploration-based methods further illuminates the complementary strengths of offline planning and online exploration

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study LMs ability to solve path finding  in synthetic GridWorld problems. They propose fine-tuning an LM to first produce path search traces (called cognitive map) then produce the path. These traces are obtained by running two different algorithms (called forward and backward) on these grids. They compare their method to CoT prompting for extrapolation to larger grids.

### Strengths
- The paper is written clearly
- The results are strong on the task: their backward version with markings of dead ends (Table-1 last column) generalizes to larger grids

### Weaknesses
 - The **cognitive maps** have too much emphasis yet we see only a single synthetic task. How these maps related to how humans solve this task? Is there any experiment with humans to show similarity— eye gazing, asking them how they arrived at their solutions? I saw some references in the paper but did not find a strong discussion of it.
- The fine-tuning of rule based solved cognitive maps is not an ecologically valid comparison to humans, as humans are not trained with such intermediate maps but they could come up with themselves.  
- The experiments start too late on Page 7, you could move most of  3.3 to appendix.
- The method is not novel as fine-tuning with intermediate structures or CoTs  do exist in the literature. The structure of CoT and how they constructed is different but specific to this task.

### Questions
I think this paper is well written but it over presents its relations to human cognition. I will increase my score if authors could provide a way to address these weaknesses in the revision.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates language models' extrapolation abilities in novel environments using a textualized Gridworld path-planning task. By introducing cognitive maps inspired by dual-process theory, the study demonstrates enhanced planning capabilities in language models over traditional Chain of Thought (CoT) approaches, particularly in extrapolated, larger environments.

### Strengths
1. Innovative approach using cognitive maps to emulate human-like System 2 reasoning in language models.
2. Rigorous experimental design testing multiple configurations of cognitive map construction (forward, backward) and planning tasks.
3. Experimental results demonstrate significant performance improvements.

### Weaknesses
I feel like the experiments can only prove that "cognitive maps" is a good method for the navigation task in Gridworld, but cannot support the claim that it is helpful for generalization.

The generalization ability of LLMs comes from large-scale pretraining on diverse tasks so that the models learn the underlying rules behind them and can generalize to unseen tasks. In this sense, evidences given by **training**  (or say, overfitting) a language model on a very specific domain seems not so convincing. 

Specifically, training the model with cognitive map provides extra supervision signals, so the performance increase is reasonable on such a small dataset in a restricted domain, but it is unclear whether the conclusion will still hold when scaling up.

### Questions
Even for a proof-of-concept paper, some experimental results somehow demonstrating the scalability of the method would be better, e.g., providing results on different tasks / environments.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces a path planning task in a textualized Gridworld, which requires a simulation process to obtain human-like cognition. 
They show that conventional approaches such as end2end generation and COT fail to generalize to larger environment. In stead, they design a  cognitive maps based approach to mimic human thinking process to enhance model planning abilities in extrapolated environments. Experiments show that their method can enable model to better generalize to larger sizes with better results.

### Strengths
- The task is clearly defined, the process is detailed, and the experiments show effectiveness of their proposed method;
- The motivation is clear and writing is explicit, with precise language, well-organized structure, and clear communication of ideas;
- The analysis is fairly thorough.

### Weaknesses
 - My primary concern is that "extrapolation" or "generalizability" extends beyond simply increasing the grid size. Rather than merely expanding the grid, it would be more insightful to evaluate model performance on grids that differ in structure or complexity from the training set; for example, by introducing obstacles, loops, or varying path lengths, which would more thoroughly test the model's ability to generalize beyond the training distribution.
- The baselines used are relatively simple. Incorporating stronger methods, such as [1] or Tree of Thoughts for planning construction, would better support claims about the model's effectiveness. Additionally, clarifying why the proposed cognitive map approach outperforms previous planning methods would strengthen the argument; specifically, a more detailed analysis of the limitations of end-to-end generation and COT in this task, and how the cognitive map addresses these limitations, would be beneficial. The current explanation lacks sufficient depth to fully justify the choice of the proposed method.
- The test set lacks diversity, raising questions about the model's generalization capabilities and its applicability to real-world scenarios. The fact that performance reaches 1 on small grid sizes suggests that the model might be memorizing solutions for simpler cases, rather than truly generalizing. This lack of diversity limits the conclusions that can be drawn about the model's robustness and its ability to handle unseen scenarios.

### Questions
- I didn't find these details in the paper: how was the training set constructed? How did you obtain the cognitive map of training samples?  What are its statistics (e.g., lengths of inputs, outputs, and plans)?
- From Figure 2, it appears that the cognitive map traverses the entire search tree. Could this cause issues with length if the grid size is large?
- In the results shown in Table 1, performance reaches 1 when the grid size is small. Does this suggest that limited diversity may be an issue, allowing the model to solve test samples simply by memorizing the training samples?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work aims to test whether LLMs are capable of planning on out-of-distribution (extrapolated) data, and proposes a new method for fine-tuning LLMs to more effectively plan and generalize to new data. The authors propose to use a textualized gridworld as the domain of study, and OOD generalization is tested by training models on (N x N) grids and testing on (A x B) grids, where A and B may be greater than N. They test two task varients, offline and online planning, where in the first a model outputs an entire plan in one shot, and in the latter a model iteratively outputs a single action, then feedback from the environment is appended to the context, then the model produces another action, and so on. Their method consists of three stages where the LLM chains actions to and from the goal. The authors test a few variants on this method and compare to two baselines, one being a simpler CoT prompt. They fine-tune LLMs with data in their cognitive maps format, and find that with 500-1000 training steps the LLMs reach peak performance. Their method vastly exceeds the performance of their baselines in OOD generalization.

### Strengths
- Paper is well-motivated, and the question of whether in-context planning extrapolates to new data is compelling.
- Task seems appropriate for studying how algorithms succeed/fail to extrapolate.
- Problem formulation is thorough and described well
- A number of experiment details and different analyses provided in the Appendix.

### Weaknesses
 - The authors make strong claims about "simulation" in reasoning, but do not sufficiently describe what this means or provide concrete justifications for their claims. E.g.
	- "The model [o1]’s success is attributed to its ability to conduct ”internal simulation” before providing an answer." I haven't seen any work making this claim, and none is cited here.
	- "These observations collectively imply that cognitive maps tap into a form of simulative reasoning that is fundamentally different from the sequential logic typically employed in CoT." I'm not sure how these results support this claim, or what "simulative reasoning" or "sequential logic" mean. 
- The authors' description of OpenAI's o1 model seems off in my reading, along with the interpretation of results. To my understanding, o1 is not "a tree-searching augmented LLM capable of internal simulation before planning". The OpenAI o1 blog post [1] specifies that the model uses a (seemingly more or less traditional) CoT that is merely hidden from the user, and even gives examples of these chains. Perhaps there's something I'm missing here.
- For the authors' claim that this "emphasize[s] the need for cognitive map-regarded training", it is unclear to me what this approach would be like for real-world domains and applications.
- Missing citations, in particular [2] seems highly relevant since it tests planning and cognitive map representations in LLMs, and similarly finds that current LLMs struggle to do planning in-context. However, the models they test seem to fare much better than these authors' baselines. Another related work not cited is [3].
- The explanation of the Cognitive Map method (Section 4) wasn't very clear to me, and figures 1 & 2 didn't help me much.
	- Fig. 1 - It's not obvious to me what the takeaways are or how to map this to the main theory/methods. The only clear takeaway I see is showing extrapolation to larger grids. The grid with the shaded area (bottom-middle) seems intended to emphasize "no cognitive map / no simulative reasoning" but it looks like it could mean partial vs. full observability or something else.
	- Fig. 2 - I'm not sure whether the "cognitive map" spoken by the agent is distinct, or in a different text format, from the steps printed in the "Output" panel. The numbers mentioned in the caption aren't shown in the figure. The figure could also reference the optimal vs. reachable plan distinction mentioned in the caption.

### Questions
- What does "simulative reasoning" mean, and how is it different from "sequential logic" as in traditional CoT?
- What evidence is there that OpenAI-o1 does "tree search" or "internal simulation" different from traditional CoT?
- How does this work relate to [2], and what accounts for differences between the authors' results compared to [2]?
- How might the authors see their methods being used at scale and/or with real-world domains? Would "cognitive map-regarded training" be applicable to general-purpose LLMs like o1 and Claude, or would it only be used in a domain-specific fine-tuning stage?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates the generalisation & extrapolation of LLMs in a controlled setting and proposes a new method for better extrapolation in the controlled setting. Specifically, the authors investigate whether and how LLMs generalise in the task of path planning. To this end the paper uses a textual grid-world of varying sizes. The authors train the models on grid sizes of 10x10 and then evaluate the models on grid sizes up to 20x20. Direct Answer and CoT produce poor results barely generalising beyond 10x10. The author's method of `cognitive maps' shows strong performance and generalisation to the grid sizes up to 20x20. Interestingly zero-/ and few-shot prompting elicits very poor performance except for models such as o1 (however, still lower than the author's approach). Finally, the author's detail their experiments and results in detail.

### Strengths
Strengths:
1. Great analysis of extrapolation ability of LLMs.
2. Detailed experiments and results
3. Strong and impressive results on the controlled task of grid-world navigation.

### Weaknesses
Weaknesses:
1. Focus on one control task, it would be interesting to do additional experiments of the like done in `Physics of Language Models' https://physics.allen-zhu.com/
2. Question of how to apply to tasks beyond the specific control task?

### Questions
Question:
1. How would you cognitive map method generalise to other approaches?
2. Comparison to previous work: How does this work compare to approaches like: Act-Re (which has a fine-tuning mechanism), or StateAct, (which proposes a `state-tracking')?

### Soundness
3

### Presentation
3

### Contribution
3
