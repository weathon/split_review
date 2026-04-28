# Enhancing Language Model Agents using Diversity of Thoughts

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 5, 6, 8

## Abstract
A popular approach to building agents using Language Models (LMs) involves iteratively prompting the LM, reflecting on its outputs, and updating the input prompts until the desired task is achieved. However, our analysis reveals two key shortcomings in the existing methods: $(i)$ limited exploration of the decision space due to repetitive reflections, which result in redundant inputs, and $(ii)$ an inability to leverage insights from previously solved tasks. To address these issues, we introduce DoT (Diversity of Thoughts), a novel framework that a) explicitly reduces redundant reflections to enhance decision-space exploration, and b) incorporates a task-agnostic memory component to enable knowledge retrieval from previously solved tasks—unlike current approaches that operate in isolation for each task. Through extensive experiments on a suite of programming benchmarks (HumanEval, MBPP, and LeetCodeHardGym) using a variety of LMs, DoT demonstrates up to a $\textbf{10}$% improvement in Pass@1 while maintaining cost-effectiveness. Furthermore, DoT is modular by design. For instance, when the diverse reflection module of DoT is integrated with existing methods like Tree of Thoughts (ToT), we observe a significant $\textbf{13}$% improvement on Game of 24 (one of the main benchmarks of ToT), highlighting the broad applicability and impact of our contributions across various reasoning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Motivated by the observation of repetitive reflections, this paper proposes a method to improve the diversity of generated reasoning by incorporating task-agnostic memory and diversity of thoughts (DoT) prompting (on top of reflexion). The experiment results show clear improvement with various LLMs.

### Strengths
1. The method is well-motivated. 
2. I appreciate the analysis and results in the Introduction to showcase the repetitive reasoning generation with existing methods, i.e., LATS, which is insightful and provides evidence.
3. The paper is well-written and easy to follow.
4. The results seem promising.

### Weaknesses
1. I am still unsure if diverse reflections can be guaranteed if prompting the Mdr agent with "Ensure your reflections are accurate and leverage previous reflections to avoid repetition. Aim for diversity in your explanations while prioritising the correctness of your hints.". Can you provide empirical evidence or analysis demonstrating how your prompting approach leads to diverse reflections?  For example, you could include metrics quantifying the diversity of generated reflections compared to baseline methods. You can also explain the reason behind it.
To me, it is more like a magic prompt. Can you explain why this simple prompt works? 
2. The whole framework is built on reflection, with Msr replaced by Mdr. Given my first comment and considering that utilizing memory to improve response diversity is widely explored, the contribution of DoT is limited.

### Questions
1. Line 700 has un-referred figure

### Soundness
2

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
4

### Summary
This paper proposes Diversity of Thought (DoT), a method that enhances LLM reasoning through diverse reflections. The paper first identifies two limitations of existing methods: (1) limited exploration due to repetitive reflections, and (2) inability to reuse knowledge from similar tasks. To address these, DoT reduces repetitive reflections and incorporates a task-agnostic memory. Experiments on three programming benchmarks and the Game of 24 demonstrate improvements of DoT compared to baselines.

### Strengths
- The paper examines tasks requiring complex reasoning and proposes solutions to enhance LLMs' reasoning capabilities. Experiments show that DoT and DoT-bank outperform baselines across various benchmarks.
- The paper provides some analysis, e.g. quantifying the redundancy of reflections generated using existing methods, to motivate the proposed method.

### Weaknesses
 - The proposed method is motivated by two observed limitations of existing methods: lack of exploration and inability to leverage cross-task knowledge. While the first limitation is analyzed and discussed in Table 1, the second lacks supporting analysis. Therefore, adding a task-agnostic memory component to DoT appears somewhat disconnected from the paper’s discussion. Although intuitively it makes sense to reuse insights from previously solved tasks, whether it is useful in practice remains unclear. The authors need to provide more evidence to justify this proposed solution in order to create a more coherent story for the paper.
- For the Reflexion baseline, is the number of reflections set to 1? If so, this may not be a fair comparison, as DoT uses many more reflections. A better comparison would be to Reflexion with k sampled reflections. This would more accurately indicate whether the proposed diverse reflection generation method (one-shot or iterative) is effective.
- DoT-bank requires building a memory bank, and its size scales with the number of failed tasks using DoT based on Algorithm 1. Therefore, the reported cost of DoT-Bank is misleading, as it does not include the cost of building the memory bank. Also, for the DoT-Bank results in all tables, is the memory bank used for every task or only for failed tasks? 
- The choice of models used for different tasks seems arbitrary. Why are different models used across tasks? For example, why does HumanEval use Sonnet 3.5 and Llama-3.1, while LeetCodeHardGym only uses Sonnet 3.5? Additionally, why does GPT-3.5 have a different setting in Table 5 compared to other models in Table 4?
- For incorporating DoT into ToT, is the only difference that ToT samples k thoughts in parallel, while ToT+Diversity samples k thoughts in one shot?

### Questions
- L700 Figure reference is missing 
- The paper uses Reflexion as a key baseline, but other similar self-reflection methods, e.g. [1], should also be cited.
- Several citation formats are not proper, e.g. some \citet, and \citep are misused, e..g L41, L105, L350, etc. 
- How is the cost of the Llama-3.1 model calculated?

[1] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback

### Soundness
2

### Presentation
2

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
This paper introduces DoT (Diversity of Thoughts), a novel framework for improving language model agents's iterative reasoning tasks by addressing two key limitations in existing approaches: 1: redundant reflections that lead to inefficient exploration of the decision space, and 2:the inability to leverage insights across different tasks. The framework consists of a diverse-reflections model that reduces redundancy in reasoning paths and a task-agnostic memory bank that enables knowledge transfer between tasks. Through extensive experiments on programming benchmarks (HumanEval, MBPP, and LeetCodeHardGym) using various language models, DoT demonstrates up to 10% improvement in Pass@1 while maintaining cost-effectiveness compared to existing methods like LATS, and when integrated with Tree of Thoughts (ToT), its diverse reflection module improved performance by 13% on the Game of 24 benchmark.

### Strengths
The paper identifies and addresses concrete limitations in existing approaches (redundant reflections and isolated task solving) with a practical solution that shows consistent improvements across different models and benchmarks. The proposed modifications are simple to implement yet effective.

### Weaknesses
1:The paper's two main components (Diverse-Reflection and Memory Bank) appear to be independent modules without a strong theoretical connection or necessity to be combined. This suggests the work is more of an engineering effort combining separate improvements rather than a cohesive theoretical advancement. The lack of comprehensive ablation studies makes it unclear which component truly drives the performance gains.

2: The paper's positioning around efficiency improvement over LATS is problematic because LATS and similar resource-intensive methods primarily aim to maximize accuracy, not efficiency. The experimental validation has several limitations: improvements are incremental (2-10%), test sets are relatively small, and no statistical significance testing is reported to validate that improvements are meaningful rather than random variation.

3: The paper lacks detailed analysis of why and how diversity in reflections leads to better results. There's insufficient discussion about the reliability of one-shot sampling for generating diverse reflections and potential failure modes. Also, key technical details about the memory bank implementation and retrieval mechanism are not fully explained, including specifics about how "relevant trajectories" are defined and retrieved and how the diversity in reflection generation is ensured; all of these make reproduction challenging.

4: The evaluation focuses mainly on programming tasks with visible or synthetic unit tests, limiting the method's demonstrated applicability to domains where clear evaluation metrics are available. This leaves questions about generalizability to broader reasoning tasks.

### Questions
How is cost calculated for different model types (especially for Llama models where costs are in GPU hours rather than API calls)? Why is the cost difference between iterative and one-shot sampling surprisingly small in Table 10?

What specific mechanism is used for retrieving "relevant trajectories" from the memory bank? How is relevance defined and measured?

While the method reduces LLM inference calls by avoiding redundancy, does it require more tokens per call due to longer context? Can you provide a quantitative analysis of average input/output token lengths compared to baselines?

What's the effect of varying k in k diverse-reflections? How reliable is the one-shot prompt approach, and what's the sensitivity to the number of retrieved trajectories?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents an iterative prompting method for LLMs that aims to improve responses by repeatedly reflecting on its previous outputs similar to the recent Reflexion method. The key advance here over the Reflexion method is to encourage diversity in the outputs. The method also incorporates a task-agnostic memory component to enable knowledge retrieval from previously solved tasks.

### Strengths
The paper is well laid out and clearly describes the method and justification for it. The method is general and can be widely applied as well as supporting integration with other orthogonal approaches (the example being tree of thoughts). The experiments are varied and well chosen with appropriate choice of base LLMs and tasks. The results show a consistent and clear improvement over other recent SoTA methods: Reflexion, LATS and ToT (where appropriate).

I am particularly impressed with the modular nature of DoT and its generality.

### Weaknesses
The weaknesses are, in my opinion, minor. The following things came to mind:
* The description of retrieval of previous trajectories could be a bit clearer, as could the experiment which produces the results in Table 9.
* I am not sure that the t-SNE evaluation in Figure 4 is as robust as it could be. It may show that DoT produces more diverse self-reflections then LATS but as the embedding is done separately for the two sets of reflections it isn't entirely clear that this is the case. I would suggest embedding the two methods together and showing that the DoT reflections are more dispersed within the same space (maybe that is what was done but it isn't clear to me).
* There are lots of results and space is at a premium but things do get less clear towards the end of these, perhaps partly due to the formatting.

### Questions
It isn't clear how an evaluator can be an LLM. Is the LLM asked to produce a numeric score? Or is there space for a textual evaluation?

When you say that MB trajectories are picked based on cosine-similarity, do you mean that the K most similar are chosen? Is there a risk that there isn't much diversity in these retrieved trajectories? Or am I missing something?

### Soundness
3

### Presentation
3

### Contribution
4
