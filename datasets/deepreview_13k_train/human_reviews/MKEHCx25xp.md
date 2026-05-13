# WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
We introduce WildBench, an automated evaluation framework designed to benchmark large language models (LLMs) using challenging, real-world user queries. 
\wildbench{} consists of 1,024 examples carefully selected from over one million human-chatbot conversation logs. 
For automated evaluation with \wildbench, we have developed two metrics, WB-Reward and WB-Score, which are computable using advanced LLMs such as GPT-4-turbo. 
\wildbench{} evaluation uses task-specific checklists to evaluate model outputs systematically and provides structured explanations that justify the scores and comparisons, resulting in more reliable and interpretable automatic judgments. 
WB-Reward employs fine-grained pairwise comparisons between model responses, generating five potential outcomes: much better, slightly better, slightly worse, much worse, or a tie. 
Unlike previous evaluations that employed a single baseline model, we selected three baseline models at varying performance levels to ensure a comprehensive pairwise evaluation. 
Additionally, we propose a simple method to mitigate length bias by converting outcomes of ``slightly better/worse'' to ``tie'' if the winner's response exceeds the loser's by more than $K$ characters.
WB-Score evaluates the quality of model outputs individually, making it a fast and cost-efficient evaluation metric. 
\wildbench{} results demonstrate a strong correlation with the human-voted Elo ratings from Chatbot Arena on hard tasks. Specifically, WB-Reward achieves a Pearson correlation of 0.98 with top-ranking models. Additionally, WB-Score reaches 0.95, surpassing both ArenaHard's 0.91 and AlpacaEval2.0's 0.89 for length-controlled win rates, as well as the 0.87 for regular win rates.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces WILDBENCH, a novel benchmarking framework designed to evaluate large language models (LLMs) using challenging, real-world user queries. It consists of 1,024 examples selected from over one million human-chatbot conversation logs. The framework employs two evaluation metrics, WB-Reward and WB-Score, to provide reliable and interpretable assessments of LLM performance. By using task-specific checklists and a dynamic update mechanism, WILDBENCH aims to reflect real user interactions and mitigate data leakage concerns. The results demonstrate a strong correlation with human judgment, surpassing existing benchmarks and offering a more accurate reflection of LLM capabilities.

### Strengths
1. **Real-World Evaluation**: utilizes real user queries to provide a more reliable assessment of LLM performance. This approach is more cost-effective than human evaluations and offers greater authenticity compared to traditional machine evaluations.

2. **Robust Evaluation Metrics**: introduces WB-Reward and WB-Score, which enhance accuracy through the use of checklists and a CoT-style evaluation process. These metrics effectively mitigate length bias, ensuring fairer comparisons.

3. **Dynamic Updates and Data Leakage Prevention**: update regularly, reflecting new user interactions and preventing data leakage, which enhances the benchmark's relevance and security.

### Weaknesses
1. **Cost Comparison**: The paper does not provide a detailed comparison of the llm api costs between WILDBENCH and previous evaluation methods, which could help in understanding its efficiency.

2. **Cheaper Version with Consistency Check**: Offer a cheaper version of the benchmark, such as using 30% of the samples, and verify it's the consistency and reliability with the full evaluation results.

### Questions
See weakness part.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper carefully picked out data from WildChat to construct an evaluation benchmark with in-the-wild user queries. 

This paper proposes two kinds of evaluation strategies, namely, checklists and structured analysis, to encourage more detailed and fine-grained evaluation.

This paper proposes two primary metrics for both pairwise and pointwise evaluation and further mitigates the bias towards longer outputs.

### Strengths
- The first benchmark for LLM evaluation with in-the-wild user queries.
- A bunch of tricks for a more accurate and debiased evaluation:
    - pairwise + pointwise
    - checklist-based
    - multiple baseline models for pairwise evaluation.
    - structured analysis before concluding the rewards.
    - mitigating the length bias with a margin term $K$ for ties, which is customizable according to the users’ needs.
- Interesting experimental findings such as the re-evaluated performance of LLaMA3-Inst-8B-SimPO.

### Weaknesses
 - The novelty of this work is quite limited despite its richness of evaluation and wild data construction practices.
- The handling of length penalty in this work is a bit crude, because sometimes a longer response is indeed better. Performing uniform processing directly at the entire dataset level fails to take into account the specific situations of each sample.
- The experimental findings offer limited novelty compared to existing benchmarks like AlpacaEval and Chatbot Arena. The comparative performance among different models remains largely consistent with previous evaluations. Additionally, this work lacks sufficient analysis from the perspective of "wildness" in the data. It fails to address a crucial question: What unique insights emerge when introducing "wildness" into the evaluation process?

### Questions
In the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors introduced WildBench, a benchmarking framework for evaluating large language models (LLMs), using 1,024 complex tasks selected from real user conversation. These tasks reflect the natural distribution of real user tasks and are diverse, allowing for a more realistic evaluation of model capabilities. The framework incorporates detailed checklists to ensure objective evaluation. Experiments show that WildBench has a high correlation with human-voted Elo rankings from Chatbot Arena, outperforming other existing automated evaluation frameworks.

### Strengths
1. WildBench establishes a comprehensive evaluation pipeline, creating a task set from real user queries that is both well-distributed and diverse, enabling a more comprehensive evaluation. Additionally, WildBench can update over time to accommodate emerging task distributions, reducing some potential risks of data leakage.
2. Experimental results show that WildBench has a high correlation with the Elo scores from Chatbot Arena, which is considered a fair evaluation. However, the human cost is lower than Chatbot Arena, and WildBench provides two evaluation metrics, offering researchers diverse options for assessing LLM performance.
3. The evaluation incorporates task-specific checklists and considers length penalties, further reducing the negative impact of "LLM as a judge."

### Weaknesses
1. Although multi-turn conversation evaluation is a highlight of WildBench, the authors did not conduct much analysis from this perspective, which is unfortunate. Specifically, there's a lack of investigation into how performance varies with different input context lengths, which is crucial for understanding the benchmark's ability to evaluate models on complex, multi-turn exchanges. This limits the understanding of how different models handle the increasing complexity of longer conversations.

2. The task quality filtering method is not detailed enough or may have some inadequacies, which could lead to inaccurate evaluations of performance differences between specific models. The filtering criteria, particularly for multi-turn conversations, need more clarity. Additionally, the analysis of the overall correlation with Chatbot Arena may not reflect the performance differences of specific models between the two leaderboards (e.g., the differences between Yi-Large and Yi-1.5-34B-Chat on WildBench and Chatbot Arena). It's unclear if the benchmark can reliably differentiate between models with similar overall performance but different strengths in specific areas.

3. The test set includes multi-turn data, and the publicly available history conversation, when used for training models, still provides some assistance in answering the final question, which means there is still a certain risk of data leakage in the dataset. The lack of specific details on how the multi-turn data was anonymized and how potential leakage was mitigated makes it difficult to assess the robustness of the benchmark.

### Questions
1. WildBench's feature of updating its task set over time is valuable. However, since the baseline models are fixed, have the authors considered whether the current baseline models can effectively evaluate models with updated training data and more advanced performance, as both the models and task sets evolve over a long period?
2. The responses in the history conversation come from earlier versions of ChatGPT-3.5 and GPT-4, which may introduce bias. For example, the history conversation may contain factual errors caused by hallucinations from ChatGPT-3.5 and GPT-4, which could conflict with the prior knowledge of the evaluated models, leading to inaccurate evaluations of model capabilities. Have any measures been taken to filter out such issues?
3. For multi-turn conversation filtering, besides limiting the number of turns and applying single-turn filtering rules, is there additional task theme consistency checking? Even with fewer turns, multiple themes might still be present, affecting task focus and coherence. There is also a potential issue where a task might consist of multiple relatively simple questions across different domains, making the overall difficulty appear higher and bypassing the difficulty filtering. However, the final question itself might be low in difficulty and easy to answer, affecting the overall benchmark difficulty.
4. The provided anonymous link is not accessible.

### Soundness
3

### Presentation
3

### Contribution
3
