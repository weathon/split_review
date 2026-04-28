# MetaTool: Facilitating Large Language Models to Master Tools with Meta-task Augmentation

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
\begin{quote}
Utilizing tools with Large Language Models (LLMs) is essential for grounding AI agents in real-world applications. The prevailing approach involves few-shot prompting with demonstrations or fine-tuning with expert annotations. However, mere in-context demonstrations may fail to cover sufficient knowledge for complex tools and tasks. Training on solution paths is also hindered by the high cost of expert annotations and generalizing to new tools. A core challenge of generalizable tool use lies in understanding the ``meta'', or fundamental natures of tools that are transferable across tasks, such as causality and constraints. In this paper, we present \textit{MetaTool}, a novel tool learning methodology designed to generalize across any reusable toolset. Our approach incorporates a self-supervised augmentation technique derived from a series of meta-tasks. This involves predicting masked elements in the tool execution process. The self-supervised procedure enables scalable generation of high-quality QA data, which is handy for supervising tool understanding. By incorporating meta-task data into task-oriented training, our method significantly enhances the performance of open-source LLMs, achieving results comparable to ChatGPT in both tool-based planning and chatting scenarios. Through large-scale instruction tuning, the MetaTool model demonstrates impressive zero-shot generalizability on new tasks.
\end{quote}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to achieve generalizable tool learning by additionally training models on meta-reasoning QA tasks. The meta-reasoning data are constructed by asking questions about the tool-using process in multiple directions, including action effect, decision-making, reversion, action input boundary, etc. Experiment results show improved tool learning performance on tasks including SAW, BW, LOG, Toolbench and BFCL.

### Strengths
1. A novel meta-learning approach for tool learning showing improved tool-learning results.
2. The ablation study verifies the effectiveness of each meta-task.

### Weaknesses
1. In lines 224-226, "In order to maintain the general ability of the model in the first stage, only the parameters of the query and value projection layers of the Transformer are updated instead of full-parameter training." This constraint might also affect learning ability and make comparisons unfair. Results ensuring similar settings will make results more convincing.

2. The "LLaMA3-solution" baselines are updated fewer times (10k*3) compared with other models ((10k + 10k)*3). It would be fairer to test both training with more steps and using more solution data to ensure similar update steps.

3. Lack of 2-stage results on ToolBench and BFCL benchmarks, nor LLaMA3-8B-inst results on BFCL. Would be better to explain the setup more clearly.

4. Authors used the early stop to prevent overfitting, which also creates the possibility for larger variance due to the arbitrary selection of epoch numbers. Any more comprehensive results to eliminate this hyperparameter selection?

### Questions
See weaknesses

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
4

### Summary
This paper proposes MetaTool, a novel approach for training Large Language Models (LLMs) to use tools effectively. The authors argue that current methods, which rely on demonstrations or expert annotations, need to be revised in generalizing to complex tools and tasks. MetaTool addresses this by introducing a set of self-supervised meta-tasks that focus on the fundamental nature of tools, such as causality and constraints. These meta-tasks are used to generate high-quality training data without human annotation. Through extensive experiments, MetaTool demonstrates superior performance to other LLMs on tool-oriented tasks, achieving results comparable to ChatGPT, and exhibits impressive generalization capabilities on new tasks.

### Strengths
This is a paper with good methodology and solid experiments.

The paper tackles the crucial challenge of enabling LLMs to effectively use tools, a capability essential for expanding their real-world applicability.

The paper demonstrates a good understanding of related LLMs and tool learning work, with a comprehensive list of references.

 The experimental setup and evaluation metrics are well-defined, the ablation studies are comprehensive, and the results demonstrate a clear improvement over baselines trained solely on solution data.

The tool-oriented scenario is an interesting setup. This is a new environment to evaluate LLMs' tool-using capability.

### Weaknesses
This paper has several weaknesses regarding the writing and the experiment results.

The idea of using self-supervised tasks to improve tool understanding is not entirely new. The authors themselves acknowledge that previous works like Toolformer and TALM have explored similar approaches. The main difference in MetaTool seems to be the specific set of meta-tasks proposed, but their novelty and contribution need further justification. Specifically, the paper does not adequately distinguish its approach from existing methods that also leverage self-supervision for tool learning, making it difficult to assess the true advancement of MetaTool.

The problem formulation and definition are clear. However, I am also curious about the real-world scenarios of these six settings. Are there any specific rationales behind why we should apply this causal inference mechanism to tool use? The paper would benefit from a more thorough discussion of the practical relevance and applicability of the proposed meta-tasks in real-world tool-use scenarios.

The paper lacks a comprehensive comparison with a wider range of state-of-the-art tool-learning models, including those employing self-supervised learning. This limitation makes it difficult to claim that MetaTool significantly improves over existing approaches [1]. There are more baselines on the Berkeley Function-Calling Leaderboard to compare with. Some of them are trained from LLaMA-3.1-8B as well. The absence of a detailed comparison against other self-supervised methods and models on the BFCL limits the ability to contextualize the performance of MetaTool.

From what I can read through this paper, the self-play and tree search lack implementation details. This is an interesting way of generating synthetic data. However, the authors did not explain that clearly. For example, the method section should describe using the ReAct to generate thought-tool-input tuples instead of the experiment section.

Some claims or writings in this paper are contradictory or confusing.

The analogy to BERT isn't that pertinent to me. We are still training the LLMs under an autoregressive objective with LLaMA-3-8B. The model is trained on an augmented/generated dataset using BERT's 'masking' process but is not trained to predict what is missing in the context.

What is the model version of ChatGPT? What about GPT-4 and Claude-2? The authors should specify the model versions more clearly.

It will be helpful if the authors add $\uparrow$ and $\downarrow$ to show which directions of the metrics are better.

Line 225 ... are updated instead of full-parameter training. Which part of the training requires full-parameter training? Isn't this model trained using QLoRA?

The tables and figures are organized confusingly. Table 3 is for tool-augmented scenarios but is placed in Section 3.1. Figure 4 is for tool-oriented scenarios, but the authors separate Section 3.3 for result analysis (only for the results in Section 3.1).

All the tables and figures should have hyperlinks.

### Questions
Typo

Line 146: Bert $\rightarrow$ BERT 

Line 208: ',' should follow the math formula

Line 256: BlocksWolrd $\rightarrow$ BlocksWorld

Line 334: ChaGPT $\rightarrow$ ChatGPT 

Line 363: ReACT $\rightarrow$ ReAct 

[1] Devlin, J. (2018). BERT: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.

[2] OpenAI (2022). Introducing ChatGPT. https://openai.com/index/chatgpt.

[3] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., \& Cao, Y. ReAct: Synergizing Reasoning and Acting in Language Models. In The Eleventh International Conference on Learning Representations.

Clarification

Line 352: Two evaluation metrics are designed based on ChatGPT: (1) Pass Rate, calculated
by the proportion of instructions successfully completed within a limited budget; (2)Win Rate,
measured by asking a ChatGPT evaluator to select its preference for two solution paths.

Question: What does 'based on ChatGPT' mean? If you use the Pass Rate, it is an automatic evaluation that does not require ChatGPT.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MetaTool, a new way to help large language models (LLMs) better understand and use tools. Instead of relying on traditional methods, like giving examples in prompts or using labeled training data, MetaTool focuses on self-supervised learning through meta-tasks. The idea is to teach models the basics of how tools work, like understanding cause and effect, what actions are allowed, and what outcomes to expect. They introduce six meta-tasks—Effect, Decision-making, Reversion, Input Boundary, Output Boundary, and Counterfact—that cover these foundational ideas. MetaTool shows impressive results across different tool-based tasks and even competes well against models like ChatGPT in both planning and chat scenarios.

### Strengths
+ The approach is unique because it emphasizes a general, task-independent understanding of tools. MetaTool's focus on foundational tool knowledge is different from the usual heavy reliance on labeled data, allowing the model to handle more situations with less specific training.

+ The experiments are thorough, covering both scenarios where the model has to use a tool in sequence (like planning) and where it’s just one part of a conversation or task. MetaTool consistently performs well across the board, and the ablation study is detailed, showing which parts of the model contribute the most to performance.

+ The explanation of the meta-tasks is clear and easy to follow. Each task seems thoughtfully designed to address different aspects of tool use, and the visuals in the paper, like the figures comparing MetaTool with other methods, really help make the results easy to understand.

### Weaknesses
 - While the benchmarks are solid, some of them are in simulated environments. This setup might not fully reflect the unpredictability of real-world situations, so testing MetaTool in live, dynamic environments could strengthen the case for its broader applicability.

- The self-supervised meta-task setup is definitely innovative, but it might be tricky for people who want to apply it to new tools or unique domains without more support. Offering some guidance or a framework for adding new tools could make MetaTool easier to use widely.

- Although MetaTool performs well against strong baselines, it would be interesting to see it compared to other recent multi-task or hierarchical learning approaches, which also aim to improve model generalization. This would give a better sense of where MetaTool stands in terms of scalability and flexibility.

### Questions
+ Could MetaTool work with tools in more dynamic, unpredictable domains, like finance or autonomous driving, where tool results might vary or need to adapt in real-time?

+ The paper mentions that MetaTool’s data generation is efficient, but how does this scale up if we’re working with very large toolsets? What’s the computational cost?

+ Do the authors plan to add more meta-tasks or tweak existing ones to improve model understanding? Would expanding to include tasks around probabilistic reasoning or continuous learning help MetaTool become even more generalizable?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MetaTool, a methodology for improving how large language models (LLMs) learn to use tools. Instead of relying solely on few-shot prompting or supervised fine-tuning with expert annotations, the authors propose a self-supervised approach based on meta-tasks that capture fundamental aspects of tool usage. The method generates training data by predicting masked elements in tool execution processes, enabling LLMs to develop a deeper understanding of tool functionality, causality, and constraints. The approach demonstrates improvements in both tool-based planning and chatting scenarios, achieving performance comparable to ChatGPT while using much smaller models.

### Strengths
- The data generation process is scalable: The paper uses self-supervised techniques to generate training data for tool use via a list of meta-tasks without requiring expert annotations. The meta-task framework allows for the automatic generation of diverse training examples that cover various aspects of tool understanding.

- Reasonable Meta-Task Design: The six meta-tasks (Effect, Decision-making, Reversion, Input Boundary, Output Boundary, and Counterfact) are well-designed to capture different aspects of tool understanding and/or action execution, which seems generalizable.

- Good empirical results: The experimental results show decent performance gains, with MetaTool achieving comparable results to ChatGPT while using much smaller models (8B parameters). Also ablation study on tool-oriented tasks showcase the effectiveness of meta-tasks generation even in the absence of “solution” data. Ablation study in ToolBench and BFCL validate the effectiveness of this data generation approach.

### Weaknesses
 - Lack of clarity regarding “solution data”: It feels like the author didn’t fully introduce and define these -concepts and brought them up abruptly in line 227. And in the evaluation section, it is a little unclear what data each baselines were trained on. It would be helpful if the authors could define different types of data in the experiment setup and use a consistent notation across the entire paper.

- Lake of details about the “meta-task generation”: it would be good to replace figure 4 with a qualitative example of metatasks generated for real-world benchmarks (e.g., ToolBench, BFCL). Also I’d appreciate the authors providing the actual prompt used for metaset construction, specifically about L199-201 “For large toolsets and diverse task scenarios that are hard to enumerate, we incorporate LLMs with self-play or tree search techniques to reduce redundant trials..."

### Questions
- The authors mentioned, “we modify the context into a more informative state in such scenarios by prompting LLMs s ∗ n = LLM(s ′ n , an, t), which is trivial for most language models.” Will the complexity of this generated instruction have an impact on the model performance? It would be helpful to see a few qualitative examples of this "context generation" (e.g., prompt input, output).

### Soundness
3

### Presentation
2

### Contribution
2
