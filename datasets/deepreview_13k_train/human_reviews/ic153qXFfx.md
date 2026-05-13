# MMMT-IF: A Challenging Multimodal Multi-Turn Instruction Following Benchmark

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
Evaluating instruction following capabilities for multimodal, multi-turn dialogue is challenging. With potentially multiple instructions in the input model context, the task is time-consuming for human raters and we show LLM based judges are biased towards answers from the same model. 
We propose MMMT-IF, an image based multi-turn Q$\&$A evaluation set with added global instructions between questions, constraining the answer format.
This challenges models to retrieve instructions dispersed across long dialogues and reason under instruction constraints.
All instructions are objectively verifiable through code execution.
We introduce the Programmatic Instruction Following ($\operatorname{PIF}$) metric to measure the fraction of the instructions that are correctly followed while performing a reasoning task.
The $\operatorname{PIF-N-K}$ set of metrics further evaluates robustness by measuring the fraction of samples in a corpus where, for each sample, at least K out of N generated model responses achieve a $\operatorname{PIF}$ score of one.
The $\operatorname{PIF}$ metric aligns with human instruction following ratings, showing 60 percent correlation.
Experiments show Gemini 1.5 Pro, GPT-4o, and Claude 3.5 Sonnet, have a $\operatorname{PIF}$ metric that drops from 0.81 on average at turn 1 across the models, to 0.64 at turn 20.
Across all turns, when each response is repeated 4 times ($\operatorname{PIF-4-4}$), GPT-4o and Gemini successfully follow all instructions only $11\%$ of the time.
When all the instructions are also appended to the end of the model input context, the $\operatorname{PIF}$ metric improves by 22.3 points on average, showing that the challenge with the task lies not only in following the instructions, but also in retrieving the instructions spread out in the model context. 
We plan to open source the MMMT-IF dataset and metric computation code.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MMMT-IF (Multimodal Multi-Turn Instruction Following), a new benchmark for evaluating instruction following capabilities in multimodal conversational AI systems. The key contribution lies in how it extends an existing MMDU by incorporating multiple instructions that constrain response formats across conversation turns. The paper also introduces PIF metric to assess how many instructions are correctly followed during a reasoning task. The paper showed that PIF metric is aligned with human rating.

### Strengths
- The paper proposes two new metrics to measure the instruction following capability through program execution.
- The paper identified a significant performance drop when the number of given instructions increases.

### Weaknesses
 - The novelty and technical contributions are somehow limited. For example, the MMMT-IF dataset is mostly an augmentation of previous MMDU dataset. The paper also lacks of providing more in-depth and insightful findings.
- Evaluated models are limited to proprietary LLMs. More open-sourced LLMs, such as LLaMA, should also be compared.
- The paper writing is not clear. For example, it would be helpful if the authors can show an example on how they extend the MMDU dataset.

### Questions
- It would be more interesting if the authors could provide more analysis on the model size’s effect on long-term instruction-following.

### Soundness
2

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
3

### Summary
This paper introduces MMMT-IF, a multi-turn, image-based multimodal question-answering (QA) dataset designed to test models on retrieving and following instructions over extended dialogues. The benchmark challenges models to not only locate relevant instructions within long conversations but also reason effectively within the constraints of these instructions. To accurately evaluate model performance, MMMT-IF includes a metric called Programmatic Instruction Following (PIF), along with a variant, PIF-N-K, which allows for a nuanced assessment of how well models adhere to instructions. Every instruction in this dataset is verifiable through code, ensuring an objective measure of a model’s instruction-following ability. Through this benchmark, the authors demonstrate that even advanced models like Gemini-1.5-Pro and GPT-4o struggle with two key areas: reliably extracting instructions from dialogues and providing high-quality answers consistently. These challenges highlight key areas for improvement in current state-of-the-art models.

### Strengths
(1) This benchmark focuses on long-form multimodal dialogue QA, with conversations extending up to 20 turns. This challenging task demands the ability to understand lengthy contexts—up to 20k tokens—and helps uncover specific issues in state-of-the-art models, such as difficulties in retrieving relevant instructions or providing consistent, high-quality answers.

(2) In addition to relying on automatic evaluation, the benchmark includes human evaluation results, with a correlation score of 0.60 between human assessments and model performance, suggesting that the PIF metric is reasonably effective in measuring models’ instruction-following abilities.

(3) The benchmark also provides an in-depth analysis of potential biases in automatic evaluations, revealing that when a model acts as the evaluator, it tends to favor its own outputs. This insight helps validate the reliability of the evaluation results by accounting for potential self-assessment biases in models.

### Weaknesses
 (1) The paper does not clearly explain how instructions are verified through code execution. Even with examples provided in the appendix, it is unclear what specific code is executed to verify each instruction. A more detailed explanation is needed, ideally with concrete examples demonstrating how instructions are translated into executable code. Additionally, the paper should define the concept of an "instruction" more clearly, as the current explanation leaves the exact meaning ambiguous.

(2) Although the paper includes detailed statistics about the dataset, it would be beneficial to include a short, complete example directly in the main text rather than in the appendix. Additionally, while the appendix briefly summarizes related work, the differences between multi-turn instruction following and related datasets like MMDU are not sufficiently explained in the main text. A clear summary of MMDU, including its main ideas and dataset characteristics, would help clarify MMMT-IF’s unique contributions. Moreover, it lacks the details of how MMDU is changed and modified to generate this proposed dataset.

(3) Expanding the evaluation to include more open-source models, such as Qwen2-VL and InternVL-2, would provide a more comprehensive assessment of model performance on the MMMT-IF benchmark. Testing open-source models also enables additional types of analysis, such as examining attention weights, which can give insights into how different models interpret and follow instructions. Currently, it only incldues analysis like needles in a haystack and sampling robustness. More in-depth analysis about the potential reason why it fails on specific cases can be done. Including a diverse set of models—spanning both interleaved and non-interleaved multimodal architectures—could reveal distinct challenges faced by different model types. While context length may pose a limitation, evaluating various open-source models could better highlight the difficulties inherent in multi-turn, multimodal instruction following, providing stronger evidence for the problem’s complexity.

### Questions
Could you provide more details on the human evaluation process and how the correlation with model performance is calculated? Specifically, what type of correlation metric is used (e.g., Pearson, Spearman) for these calculations? Additionally, it would be helpful to know the inter-annotator agreement statistics. While the paper indicates that human performance significantly outpaces model performance, more information on the evaluation protocol and inter-annotator correlation scores would provide a clearer understanding of the reliability and consistency of the human evaluations.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
It introduces MMMT-IF, a challenging benchmark for evaluating multimodal, multi-turn instruction-following in AI models. This dataset extends existing multimodal benchmarks by adding global instructions that models must retrieve and follow across multiple dialogue turns, which enhances the complexity of the task. The authors propose two metrics: Programmatic Instruction Following (PIF), which measures how well models adhere to given instructions, and PIF-N-K, which tests the robustness of models by evaluating their performance across multiple response samples.

The results indicate significant challenges for models, such as Gemini 1.5 Pro, GPT-4o, and Claude 3.5 Sonnet, especially as the number of instructions or the length of the conversation increases. Human evaluations align moderately well with the PIF metric, suggesting its effectiveness in assessing instruction adherence. The study highlights that the primary difficulty lies not in following instructions per se but in retrieving and reasoning over them across long contexts.

### Strengths
1. MMMT-IF effectively extends the scope of existing datasets by incorporating multi-turn, multimodal challenges, making it more relevant for real-world dialogue tasks where instructions are dispersed throughout interactions.

2. The PIF and PIF-N-K metrics provide a clear and objective way to evaluate models' instruction-following capabilities, verified through code execution. This adds reliability to the evaluation process and reduces human bias.

3. The study sheds light on how current AI models struggle with retrieving and reasoning over instructions in long contexts. This insight is valuable for researchers focusing on improving the long-context reasoning capabilities of language models.

### Weaknesses
1. The task's high difficulty might limit its immediate usability for current models, as evidenced by significant drops in PIF scores across all tested models. This suggests that the benchmark may be too challenging for some real-world applications or standard models.

2, Implementing and evaluating models with the MMMT-IF dataset and PIF metrics can be computationally demanding, potentially hindering researchers with limited resources.

3. The need for models to follow specific and potentially complex instructions could lead to overfitting on tasks within the benchmark rather than promoting generalizable improvements in instruction-following capabilities.

### Questions
1. How well does the PIF metric scale with larger datasets or models? Are there limitations in applying this to more extensive, real-world data?

2. Can the MMMT-IF benchmark be adapted or simplified for single-modality tasks, or is it strictly limited to multimodal, multi-turn settings?

3. How does the complexity of individual instructions impact model performance? Would simplifying or categorizing instructions lead to better insights?

4. What are the potential improvements or training adjustments needed for models to better handle instruction retrieval and adherence?

5. How do specific architectural features (e.g., memory modules, context window size) influence model performance on the MMMT-IF benchmark?

### Soundness
3

### Presentation
3

### Contribution
4
