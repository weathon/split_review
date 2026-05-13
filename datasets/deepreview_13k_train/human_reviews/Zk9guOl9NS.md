# What Makes Large Language Models Reason in (Multi-Turn) Code Generation?

- Decision: Accept
- Scores: 8, 5, 8

## Abstract
Prompting techniques such as chain-of-thought have established themselves as a popular vehicle for improving the outputs of large language models (LLMs).
For code generation, however, their exact mechanics and efficacy are under-explored.
We thus investigate the effects of a wide range of prompting strategies with a focus on automatic re-prompting over multiple turns and computational requirements.
After systematically decomposing reasoning, instruction, and execution feedback prompts, we conduct an extensive grid search on the competitive programming benchmarks CodeContests and TACO for multiple LLM families and sizes (Llama 3.0 and 3.1, 8B, 70B, 405B, and GPT-4o).
Our study reveals strategies that consistently improve performance across all models with small and large sampling budgets.
We then show how finetuning with such an optimal configuration allows models to internalize the induced reasoning process and obtain improvements in performance and scalability for multi-turn code generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the effects of varied prompting techniques, including chain-of-thought (CoT), reasoning, and execution feedback prompts, on the performance of large language models (LLMs) in multi-turn code generation. It focuses on understanding the mechanics and efficacy of these prompts on complex programming tasks using benchmarks like CodeContests and TACO across models of different sizes (e.g., Llama 3.0/3.1, GPT-4o). Unlike simpler code generation tasks, competitive coding demands algorithmic reasoning and has not been widely explored with unified evaluation metrics for multi-turn code generation. 

Key contributions include:

1. **Framework for Multi-Turn Code Generation**: The paper establishes a unified framework that enables a mix of single-turn and multi-turn prompting techniques, incorporating reasoning, instruction, and feedback prompts. This approach aims to build robust baselines for multi-turn performance and to measure trade-offs between sampling budgets and model capabilities.

2. **Experimental Insights**: The authors’ extensive grid search reveals that combining reasoning and instruction prompts significantly enhances single-turn model performance, especially for larger models and more difficult tasks. However, for multi-turn settings, while combining with CoT prompts boosts performance, using multi-turn alone has limited benefits and can even reduce performance at higher sample budgets due to less diverse outputs.

3. **Internalized CoT**: The study adapts the RFT, which allows models to internalize multi-turn CoT reasoning during training. RFT-trained models demonstrate improved performance and reasoning abilities in the absence of CoT prompts at inference, showing promise for scaling up multi-turn code generation capabilities.

4. **Exploration-Exploitation Dynamics**: The analysis indicates that detailed feedback can induce exploitative behavior in models, which is beneficial for simpler problems but counterproductive for complex ones where diversity in code generation is critical. This highlights the need for feedback strategies that balance between exploiting known solutions and exploring new ones, particularly in high-difficulty settings.

In conclusion, this work underscores that multi-turn code generation is not inherently beneficial without adaptive strategies like CoT prompts and RFT. The findings advocate for tailored prompting configurations based on problem difficulty and suggest that further advancements in multi-turn code generation could benefit real-world applications such as repository-level LLM agents capable of reasoning, self-repair, and complex interaction with environments.

### Strengths
**Originality**:  
This work provides a unique contribution by systematically exploring multi-turn code generation for large language models (LLMs) through diverse prompt configurations, including **chain-of-thought (CoT)**, **reasoning prompts**, and **execution feedback**. While prior work has explored CoT and single-turn code generation, this paper’s emphasis on **multi-turn prompting in competitive programming benchmarks** addresses an under-explored area. The study’s integration of multi-turn CoT with finely tuned execution feedback as a **comprehensive prompting framework** offers an original approach to improve model reasoning in multi-turn contexts. Additionally, the use of **Rejection Sampling Fine-tuning (RFT)** to internalize CoT reasoning across turns is a creative and impactful extension, enabling models to generalize reasoning capabilities without prompting at inference time.

**Quality**:  
The paper demonstrates high quality in its rigorous experimental design and breadth of evaluations. Through an extensive **grid search** of prompt combinations, the authors provide a robust dataset for comparing single-turn and multi-turn settings across a **variety of model architectures and sizes** (Llama 3.0/3.1, GPT-4o). The benchmarks, CodeContests and TACO, are well-chosen for evaluating competitive coding capabilities, allowing the paper to contribute valuable insights for LLM applications in algorithmic and complex reasoning tasks. Methodologically, the work includes detailed ablations, sensitivity analyses, and cross-model comparisons, ensuring that the findings are well-supported and generalizable.

**Clarity**:
The paper is well-structured, clearly outlining the motivation, objectives, and experimental setup. The **framework for prompt deconstruction** is presented systematically, with visual aids like **Figure 1** that clarify the operational structure of single- and multi-turn code generation. Each type of prompt (reasoning, instruction, feedback) is explained with appropriate examples, making the framework comprehensible for readers. The authors’ discussion on **exploration-exploitation dynamics** and performance limitations in multi-turn settings enhances clarity by contextualizing how feedback granularity impacts model behavior. Additionally, the conclusions are tied back to the primary research questions, reinforcing the relevance of the findings.

**Significance**:  
The study makes significant strides in understanding and advancing multi-turn reasoning for code generation in LLMs. By introducing a unified prompting framework and evaluating its efficacy in algorithmically demanding benchmarks, the paper sets a strong foundation for future research in **multi-turn, reasoning-heavy applications** for LLMs. The RFT approach has implications beyond competitive programming, as it suggests that **prompted reasoning behaviors can be internalized** within the model, potentially reducing computational costs for other complex, multi-step tasks. Given the trend toward **LLM-based agents** capable of autonomous decision-making, this paper’s insights into adaptive CoT, feedback prompting, and exploration-exploitation trade-offs are timely and have high applicability.

**Conclusion**:
In summary, this paper’s originality in multi-turn prompting, its methodological rigor, clarity, and significance make it a valuable contribution to the field of LLM code generation. The findings not only enhance understanding of CoT in multi-turn settings but also provide practical strategies for optimizing reasoning in LLMs, making this work highly relevant for both researchers and practitioners.

### Weaknesses
 While the paper makes significant contributions to the understanding of multi-turn code generation in LLMs, there are a few areas where improvements could be made to strengthen the study further.

**1. Limited Scope of Multi-Turn Framework**
The paper’s framework, while well-designed for competitive programming benchmarks, focuses primarily on **chain-style multi-turn code generation**. This approach limits the exploration of more complex **tree-structured trajectories** or **backtracking mechanisms** that could better emulate real-world multi-turn interactions in agent-based LLM applications. Exploring additional trajectory structures—such as decision-tree-style paths where LLMs could backtrack or revise earlier steps—would add depth to the study and provide insights into more adaptive reasoning scenarios. Extending the framework to incorporate these structures could lead to a more comprehensive understanding of multi-turn reasoning dynamics. For instance, the current framework does not account for scenarios where an LLM might need to revisit a previous step due to a later error, a common occurrence in debugging or complex problem-solving.

**2. Potential Bias in Rejection Sampling Fine-Tuning (RFT)**
Although Rejection Sampling Fine-Tuning (RFT) is a compelling method for embedding reasoning behavior, the paper’s reliance on **correctly generated trajectories** may introduce a bias toward successful patterns, potentially limiting the model’s adaptability to a broader range of problem-solving approaches. By focusing only on “successful” reasoning patterns, the model may overfit to specific prompt types or problem formats. Future work could consider **diversifying the fine-tuning data** to include not only correct but also nearly correct attempts with varied prompts, allowing models to learn from a broader array of problem-solving paths. For example, the model might not learn to recover from a suboptimal initial step if it is only trained on trajectories that were correct from the start.

**3. Dependence on High-Resource Settings**
The paper’s approach requires considerable **computational resources** due to the grid search over a large set of prompt combinations and the use of multi-turn, CoT, and feedback prompts across different model sizes. This may limit the practical application of the findings for research groups or practitioners with restricted compute budgets. Introducing methods for **adaptive prompt selection** that can identify effective prompt configurations more efficiently (e.g., meta-learning approaches) could make the approach more accessible and scalable, especially for real-world applications where computational resources may be constrained. The current methodology does not offer a clear path for researchers with limited resources to replicate or build upon these findings.

**4. Limited Discussion of Prompt Failure Modes**
The paper could benefit from a more detailed **analysis of prompt failure modes**, particularly in cases where certain prompt combinations degrade performance in multi-turn settings. While the paper briefly notes that CoT may harm performance by obstructing LLM context or encouraging suboptimal plans, it lacks a thorough exploration of specific cases where multi-turn CoT and feedback combinations lead to failure. A more in-depth examination of these failure patterns, especially for challenging tasks, would provide actionable insights into optimizing prompt configurations and mitigating these issues in future iterations. For instance, it would be useful to know if certain reasoning prompts consistently lead to dead ends or if specific feedback prompts cause the model to get stuck in a loop.

### Questions
1. Diversity in Rejection Sampling Fine-Tuning: The paper fine-tunes the model on correctly generated trajectories. Given the potential for this approach to bias the model towards successful solutions, would the authors consider including near-correct or diverse trajectories to introduce a broader range of reasoning paths? This could enhance the model’s adaptability to different problem-solving strategies.
2. Adaptive Prompt Selection for Reducing Computational Requirements: The extensive grid search across prompt types and model configurations is resource-intensive. Have the authors explored adaptive or meta-learning techniques to streamline prompt selection, reducing computational demands while still achieving optimal prompt configurations? Such techniques could make the framework more accessible for settings with limited computational resources.
3. Detailed Analysis of Prompt Failure Modes: The paper mentions that certain CoT prompt configurations may degrade performance, particularly in multi-turn settings with higher sample budgets. Could the authors provide a more granular analysis of these failure modes? Understanding specific prompt combinations or scenarios where performance degrades could guide practitioners in avoiding ineffective configurations.
4. Balancing Exploration and Exploitation in Feedback Prompts: The study notes that finer-grained feedback prompts may encourage exploitative behavior in models, potentially limiting performance on complex tasks. Have the authors considered any strategies for adjusting the feedback granularity dynamically based on task difficulty or performance? This could help achieve a balance between exploration and exploitation for more challenging problems.
5. Transferability of the Findings to Other LLM Architectures: The paper experiments primarily with the Llama series and GPT-4o models. To what extent do the authors believe that the findings, especially related to prompt configurations and RFT, would transfer to other LLM architectures with different pretraining characteristics? For instance, would models with fewer parameters or more domain-specific training exhibit similar responses to the same prompting strategies?
6. Future Directions for Enhancing Multi-Turn Reasoning in LLMs: Given the current results, what specific directions do the authors see as most promising for advancing multi-turn reasoning capabilities? Are there any particular technical approaches, benchmarks, or modifications to current LLM architectures that the authors believe could improve multi-turn performance on reasoning-heavy tasks?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper evaluates various prompting strategies in single-turn and multi-turn code generation settings. For single-turn generation, it explores chain-of-thought (CoT) prompting, dividing it into reasoning prompts and instruction prompts. In multi-turn generation, the paper investigates multiple error feedback strategies. The evaluation covers the CodeContests and TACO benchmarks, focusing on Llama models and GPT-4o. The authors also fine-tune the models on multi-turn CoT data to internalize reasoning within the LLMs.

### Strengths
-	The paper brings together the evaluation of a wide range of prompting strategies in both single turn and multi-turn for multiple models on a challenging code dataset.
-	Extensive set of experiments with an extensive grid search
-	Interesting idea of splitting the CoT prompts into reasoning, instruction, and feedback so that we can understand what strategies work best for different model sizes and problem difficulties. 
-	Multi-turn code generation findings reinforce insights from previous papers --- just multi-turn is not sufficient but combining with CoT might improve performance. 
-	Fine-tuning on multi-turn CoT data is a novel approach that shows promising results.

### Weaknesses
 - **Limited novelty**: There is substantial existing research on CoT and self-repair in the code domain, which somewhat limits the paper's originality.

- COT-Retry prompts seem like an arbitrary combination of prompts. Why this particular combination? The paper lacks any chain of thought prompting specific to reasoning about why the test failed or how to fix the test.


- For additive reasoning prompts experiment in table 6, what happens if each sample uses a different COT prompt?


Some of the details are missing/not clear that gives me less confidence on the results:

1.	**Baseline for Fine-Tuning**: There should be a baseline that fine-tunes on problem-solution pairs (without CoT data). This would help clarify whether RFT fine-tuning offers benefits beyond simple fine-tuning.

2.	**Clarity on CoT and Multi-Turn CoT**: Tables 1 and 2 could more clearly explain CoT and multi-turn CoT strategies. Are they different across models? Are they also different across sample sizes?

3.	**Another baseline for table 8**: How does table 8 results compare to just resampling from the base model? Is feedback even playing a role in these multi-turn settings?

4.	**Explain Figure 6**: Why does the multi-turn CoT differ from the base model at max_turns=1? Shouldn’t they be identical if CoT-Retry doesn’t apply CoT in the first turn?

5.	**Misinterpretation of results**: Some results are misinterpreted in the text. For instance, Figure 4 uses different axes across charts, making it difficult to interpret trends accurately. . Also, we cannot  say that 1% to 2% is better than 30% to 40% or other way around.

### Questions
Please answer the questions in the weakness section.

### Soundness
2

### Presentation
2

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
This paper investigates the effects of various prompting strategies on large language models (LLMs) for code generation tasks, focusing on multi-turn interactions and computational requirements. The authors conduct a comprehensive study using competitive programming benchmarks (CodeContests and TACO) across multiple LLM families and sizes. They explore single-turn vs. multi-turn code generation, chain-of-thought (CoT) prompting techniques, execution feedback in multi-turn settings, and the impact of model size and problem difficulty on prompting effectiveness. The study also examines fine-tuning models on multi-turn CoT data.

### Strengths
1.Comprehensive evaluation of CoT prompting strategies across different model sizes and benchmarks. I found the negative results that Reasoning prompts not additive interesting.

2.Usage of pass n@k metric for fairer comparison between single-turn and multi-turn approaches.

3.Thorough analysis of the impact of different error-feedback granularities.

4.Investigation of fine-tuning on multi-turn CoT data and its effects on model behavior, showing effectiveness to internalize CoT steps for LLMs.

### Weaknesses
1.Although this work has solid empirical evaluations and good presentations, the novelty is a bit limited by combining existing works together, including CoT strategies, error-feedback granularities, and Pass n@k. The core contribution is primarily a prompt engineering effort combined with the evaluation of existing LLM capabilities in code generation. While valuable, this doesn't represent a significant theoretical or methodological advancement in the field. As for the RFT part, although I think it is a novel method used here, I would like to see more details on it to explain it clearly, with details on how it is finetuned with.

2.Limited theoretical analysis of why certain prompting strategies work better than others. Although the authors presented solid empirical results on the prompting strategies ablation, I will still wonder why it works. Plus, since there is no best CoT for every case, i still think cases can be categorized into a bunch of properties, would it be better to have a task analysis model first, to decide which CoT to be applied based on these properties? I would be happy to see the answer to it.

3.Potential overfitting concerns with fine-tuning on multi-turn CoT data generated from the same benchmark used for evaluation, since currently the training process is not clearly described, i keep this as a doubt and look forward to the authors' response.

4.Figure presentations: I found some figures in the appendix not using vector figures, which are in low-resolution, starting from line 1100 and after. And some figures don't have proper captions, starting from line 1524 and after. The typesetting in the appendix should also be reorganized to avoid large blank pages. In a word, I think the good presentation in the main text should be kept as well in the appendix for a good ICLR paper.

### Questions
1.How well do the findings generalize to other types of code generation tasks beyond competitive programming? Are there more complicated benchmarks available to evaluate?

2.How large finetuning dataset is required to train a sufficient model that internalized the CoT? Need more finetuning details.

3.How does the finetuned model perform on unseen code generation tasks?

### Soundness
4

### Presentation
3

### Contribution
2
