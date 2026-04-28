# Enhancing Graph Of Thought: Enhancing Prompts with LLM Rationales and Dynamic Temperature Control

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
We introduce Enhancing Graph Of Thoughts (EGOT), a method designed to enhance the performance of large language models (LLMs) on complex reasoning tasks. EGOT automates the process of generating accurate responses using given data and a base prompt. The process consists of several steps: It obtain an initial response from the answering node using the base prompt. Evaluation node evaluates the response and generates reasoning for it, utilizing the score's probabilities to enhance evaluation accuracy. The reasoning from both the answering node and the evaluation node is aggregated to identify the problem in the response. This aggregated reasoning is incorporated into the base prompt to obtain an enhanced response. These steps are organized in a graph architecture, where the final leaf nodes are merged to produce a final response. As the graph descends, the temperature is lowered using Cosine Annealing and scoring, to explore diverse responses with earlier nodes and to focus on precise responses with later nodes. The minimum temperature in Cosine Annealing is adjusted based on scoring, ensuring that nodes with low scores continue to explore diverse responses, while those with high scores confirm accurate responses. In sorting 256 elements using GPT-4o mini, EGOT performs 88.31\% accuracy, respectively, GoT (Graph Of Thought) performance has 84.37\%. In the frozen lake problem using GPT-4o, EGOT averages 0.55 jumps or falls into the hole, while TOT (Tree Of Thoughts) averages 0.89.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces EGoT, an architecture for enhancing large language model (LLM) performance by dynamically generating prompts and answers using a base prompt. It utilizes cosine annealing for temperature control to refine answer confidence and log probabilities to improve accuracy without needing additional training or examples. EGoT demonstrates consistent, high-quality output across tasks by continuously appending rationale steps and focusing on diverse yet accurate responses.

### Strengths
- The use of rationale-driven approaches is well-motivated, and experiments show EGoT achieving higher performance in tasks like number sorting and frozen lake.
- Example use cases effectively illustrate the mechanism’s function, though additional examples of negative rationales would enhance understanding.

### Weaknesses
 - It would be beneficial to include cases where EGoT fails and scenarios where the gap between EGoT and EGoT* is more pronounced.
- Experiments were limited to GPT-4o models. Findings might differ from other model types.
- How the aggregate rationale node functions is unclear. How effectively can LLMs aggregate rationales?

### Questions
- Given that EGoT requires three times the resources compared to other mechanisms, for which tasks does this approach offer an advantage, and in which cases might it be less suitable?
- Is there any rationale behind selecting these specific experimental setups—document merging, number sorting, and frozen lake?

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
3

### Summary
The paper present an architecture for prompt engineering based on Graph of Thoughts, aimed at supporting LLM reasoning for complex reasoning tasks. It is evaluated on the frozen lake problem.

### Strengths
Addressing advanced methods for prompting LLMs is valuable.
The proposed method starts from a reasonable basis.

### Weaknesses
The paper present an architecture for prompt engineering based on Graph of Thoughts, aimed at supporting LLM reasoning for complex reasoning tasks. It is evaluated on the frozen lake problem.


 3


 2


 3


 Addressing advanced methods for prompting LLMs is valuable.
The proposed method starts from a reasonable basis.


 The paper should be enhanced to resolve readability issues and exemplification of the steps in their workflow, e.g., the nested steps are not explained following a clear workflow, and are not associated with the claimed approach for dynamic temperature control. I acknowledge that the authors provided some context to understand their results, and took several steps to improve the narrative of the paper.


 Can you provide a clear workflow and an example of a concrete prompt on a real world reasoning problem?
Can you formalise the steps used in the method?
Can you experiment with the method on existing LLMs?
I acknowledge that the authors made efforts to clarify the workflow and broadened the set of tested LLMs.


 ['No ethics review needed.']


 6


 3


 Yes

### Questions
Can you provide a clear workflow and an example of a concrete prompt on a real world reasoning problem?
Can you formalise the steps used in the method?
Can you experiment with the method on existing LLMs?
I acknowledge that the authors made efforts to clarify the workflow and broadened the set of tested LLMs.

### Soundness
3

### Presentation
2

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
This paper proposes Enhancing Graph of Thoughts (EGOT) to improve the performance of LLM on reasoning tasks. They design a flow within each node to answer the question with rationales, evaluate the answer with rationales, and consolidate the answer and evaluation rationales as inputs to the child nodes. They also introduce temperature control with cosine annealing to explore answer space at earlier nodes and refine the promising answers at later nodes. They report that the proposed methodology shows better performance on number sorting and frozen lake tasks compared to baselines including CoT, ToT, and GoT.

### Strengths
1. This paper goes beyond the evaluation scoring used in ToT and GoT for pruning and ranking; instead, they also leverage LLMs to provide rationales for the answers and evaluation scores to help the model refine the answers.

2. This paper introduces temperature control with cosine annealing to balance between exploration and exploitation.

3. This paper demonstrates the effectiveness of EGoT on an additional reasoning task, Frozen Lake problem, which has not been explored in any of baselines including CoT, ToT, and GoT.

### Weaknesses
1. The paper formulates the methodology with a graph architecture, but it does not hold certain characteristics of a graph similar to Graph of Thoughts (GoT). First, figure 1 starts with Method Node as root and section 2.2 says “heuristic methods are requested from LLM and utilized”, but it’s not clearly illustrated in the example use case (section 3.3), hence making the interaction between Method Node and other nodes confusing. Second, based on the section 3.3 example use case, the methodology starts with 3 nodes and there are no interaction between child nodes either from the same parent or different parents until the very end. Given these observations, it seems like 3 Tree of Thoughts with aggregation at the last layer. It would be good to explain more clearly on this front.

2. Some settings mentioned in the paper seem arbitrary without thorough explanation. First, for the evaluation score, the authors run evaluation once more with a temperature of 1 if the probability is lower than a threshold and different scores have different thresholds. Without looking at the specific evaluation prompt, it is not clear why we select a scale of 0-100 instead of 0-10 or 0-5. Since the evaluation requires more accuracy and lower diversity, it it not clear why we set a temperature of 1 to re-run the evaluation instead of relying on the scores generated with a temperature of 0. Could you provide justifications for these choices? Are they based on any experiment results?

3. In section 4, the authors state that “for GoT, instead of evaluating the best performing node, they select the one with medium score value, with the goal of comparing only structural performance, as solving problems with evaluation metrics is not considered to be a structural advantage.” However, it may not be convincing as EGoT also takes advantage of LLM evaluation with rationales instead of structure changes only; it may not be a fair comparison to only select the medium for GoT. Furthermore, the claim that selecting the median node is equivalent to random selection needs more justification, as an LLM might not always identify the first response as the best one. It would be beneficial to provide baseline numbers following the complete GoT pipeline and share quantitative results to support this claim.

### Questions
1. It would be good to add the prompts used for each task and each node to appendix

2. In section 3.3, the illustrated case branches each node in depth 0 into 2 child nodes, but after depth 0, each parent node only generates 1 child node. What's the criteria to determine how many child nodes to be generated.

3. In section 3.1.1, the authors state that if the child gives the same answer as the parent, a questions is only asked once more, since it cannot be determined whether it’s the correct answer. It would be good to validate if the score or confidence level produced by the evaluation node could determine if one more run is needed.

4. Curious to understand the cost compared to other baselines.

### Soundness
2

### Presentation
1

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
This paper introduces a dynamic an approach of enhancing prompts with dynamic temperature control. The steps are organized in a tree-like structure, where there is an answering, an evaluation and an aggregate rationale component in each node and each node passes the information to the child nodes. The authors evaluate this approach evaluate a range of closed and open LLMs on tasks and compare with other relevant methods from the literature.

### Strengths
- The authors borrow ideas from other methods from the literature and combine them in a good way
- They use a dynamic temperature which initially allows for more exploration when the model has less confidence and decreases as the model gains more confidence of its answers
- They show that this method is improving on some common benchmarks using GPT4o/GPT4o mini
- This is a method that doesn't require fine-tuning which can be resource intensive and time consuming
- The paper is well-written and comprehensible

### Weaknesses
 - This method is only evaluated with GPT4o. It would be important to see how other models are performing like Llama or Mistral. 
- I think for this method the bottleneck is the model's self-evaluation and answering. For self-evaluation If it assigning incorrect scores and rationales, then the performance will also be bad no matter what method you use. In such a case it may even yield in worse performance than some of the methods you presented. For answering, you already provided the chess example. The best way around it is to fine-tune with well curated examples.
- For the most part these ideas are not novel. We've seen these ideas in papers like ToT,  $T^{2}oT$, GoT, SC, Self-Evaluation

### Questions
- From your benchmarking, I see that by fixing the temperature (EGoT*) the accuracy is sometimes very similar to dynamic temperature (EGoT). Would that indicate that for those instances dynamic temperature has no effect?
- Is there an established set of benchmarks for evaluating these methods? For example in the GoT paper I see that they also evaluate on sorting and document and merging tasks as you do, but they also evaluate on keyword counting and document merging and they don't evaluate on the frozen lake
- Minor mistakes:
Use “Prompt engineering” instead of “Prompted engineering”
"As a result, no architectures cannot find a move that captures the opponent’s piece". Do you mean $\textbf{"can find"}$?
- In your figure 2 it's hard for me to follow the coordinates. Would it be possible to make each cell look more distinct and add a x,y axis ticks?

### Soundness
3

### Presentation
3

### Contribution
3
