# Arctic-SnowCoder: Demystifying High-Quality Data in Code Pretraining

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Recent studies have been increasingly demonstrating that high-quality data is crucial for effective pretraining of language models. However, the precise definition of ``high-quality'' remains underexplored. Focusing on the code domain, we introduce \ours-1.3B, a data-efficient base code model pretrained on 555B tokens through three phases of progressively refined data:
(1) \emph{general pretraining} with 500B standard-quality code tokens, preprocessed through basic filtering, deduplication, and decontamination,
(2) \emph{continued pretraining} with 50B high-quality tokens, selected from phase one by a BERT-style quality annotator trained to distinguish good code from random data, using positive examples drawn from high-quality code files, along with instruction data from \magicoder and \scins,
and (3) \emph{enhanced pretraining} with 5B synthetic data created by \llamathreeone-70B using phase two data as seeds, adapting the \magicoder approach for pretraining. 
Despite being trained on a limited dataset, \ours achieves state-of-the-art performance on \bigcodebench{}, a coding benchmark focusing on practical and challenging programming tasks, compared to similarly sized models trained on no more than 1T tokens, outperforming \phims-1.5-1.3B by 36\%.
Across all evaluated benchmarks, \ours-1.3B beats \starcoderbase-3B pretrained on 1T tokens.
Additionally, it matches the performance of leading small base code models trained on trillions of tokens.
For example, \ours-1.3B surpasses \starcodertwo-3B, pretrained on over 3.3T tokens, on \humanevalp, a benchmark that evaluates function-level code generation, and remains competitive on \bigcodebench{}. Our evaluation presents a comprehensive analysis justifying various design choices for \ours. Most importantly, we find that the key to high-quality data is its alignment with the distribution of downstream applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Arctic-SnowCoder-1.3B, a small code model trained on 555B tokens through a meticulously designed three-phase pretraining process. The first phase involves general pretraining with 500B tokens of standard-quality code, filtered and deduplicated. The second phase refines this with 50B tokens of high-quality code, identified using a BERT-based quality annotator trained on positive examples from curated open-source repositories and instruction datasets. In the final phase, 5B tokens of synthetic data are generated using Llama-3.1-70B, seeded from the high-quality data to further enhance model performance. The model achieves state-of-the-art results on BigCodeBench, significantly outperforming larger models on practical and challenging programming benchmarks such as HumanEval+ and MBPP+. The paper highlights the importance of progressively improving data quality and aligning it with downstream tasks, offering comprehensive evaluations, ablation studies, and practical insights into optimal pretraining strategies, such as learning rate schedules and data repetition, to maximize the efficiency of smaller language models in code generation tasks.

### Strengths
Arctic-SnowCoder demonstrates remarkable strengths among small size model, particularly in achieving state-of-the-art results on BigCodeBench with a 36% performance improvement over Phi-1.5-1.3B, despite using only 555B tokens compared to models trained on trillions of tokens. Arctic-SnowCoder-1.3B outperforms StarCoderBase-3B across all benchmarks and surpasses StarCoder2-3B, trained on over 3.3T tokens, on HumanEval+ with a score of 28.0 compared to 27.4. The model also achieves competitive results on MBPP+ (42.9) and EvoEval (18.0), showing that it can match or exceed the performance of larger models like StableCode-3B and Granite-Code-Base-3B, which are trained on 1.3T and 4.5T tokens, respectively. These results, combined with thorough ablation studies, highlight the effectiveness of its three-phase pretraining strategy, focusing on high-quality and synthetic data, while providing concrete evidence of its efficiency and superior performance in practical and complex coding tasks.

### Weaknesses
While the synthetic data significantly boosts performance, as seen in the 36% improvement over Phi-1.5-1.3B on BigCodeBench, an overreliance on synthetic data risks skewing the model’s understanding of practical coding tasks. Specifically, the synthetic data generation process, while aiming for higher quality, might inadvertently introduce biases or patterns that do not accurately reflect the diversity and nuances of real-world code. Additionally, the performance on HumanEval+ (28.0) and MBPP+ (42.9), although impressive, shows only incremental improvements over models like StarCoder2-3B (27.4 on HumanEval+ and 49.2 on MBPP+), indicating room for optimization in handling more complex or diverse programming tasks. The quality annotator, trained on specific curated datasets, could introduce biases that may not adequately represent broader coding practices, potentially limiting its effectiveness across all programming domains. For instance, if the curated datasets over-represent certain coding styles or paradigms, the annotator might favor these, leading to a model that performs well on specific benchmarks but struggles with more varied real-world code. 

The paper’s approach to handling repo-level data in the general pretraining phase is insightful but has room for further exploration. The authors compare two methods: grouping files by repository names and by language before repository. They conclude that partitioning by language yields better results, as evidenced by improved scores on HumanEval+ (17.1 vs. 12.8), MBPP+ (33.9 vs. 30.7), and EvoEval (7.4 vs. 7.0). This method ensures that training documents are more focused and homogenous, which likely aids the model in learning language-specific patterns effectively. However, this method might overlook the potential benefits of cross-language learning, especially in multi-language projects where inter-language interactions are critical. For example, many real-world projects involve multiple languages, and a model trained solely on language-specific groupings might struggle with tasks that require understanding the interplay between different languages. Future work could explore hybrid approaches that maintain language-specific grouping but occasionally incorporate multi-language contexts to enhance the model’s ability to handle real-world, polyglot codebases. Additionally, more granular investigations into the impact of repository size and the diversity of code snippets within a repository could provide deeper insights into optimizing repo-level data grouping for enhanced model performance. For instance, it would be beneficial to analyze how the model performs when trained on repositories with varying sizes and code complexity. 

In addition, my concern is that the paper presents compelling results among small language models, particularly with its strong performance on benchmarks like BigCodeBench and HumanEval+. However, the underlying reasons for achieving such high performance despite the relatively small training dataset (555B tokens) are not fully unpacked. While the authors attribute the success to the progressive refinement of data quality and the use of synthetic data, the detailed mechanisms by which these factors translate into superior model performance remain somewhat opaque. For example, it is unclear how the quality annotator's specific features contribute to the model's improved learning, and what specific characteristics of the synthetic data make it more effective than the original high-quality data. 

Finally, I suggest evaluating the model on the CodeMMLU benchmark, which could provide a broader assessment of the model’s capabilities across a diverse set of coding tasks, thereby offering more comprehensive insights into its strengths and potential areas for improvement.

### Questions
1) Could you provide more detailed analysis or ablation studies on how the quality annotator specifically improves the model’s learning? What are the key features or patterns it identifies that contribute most to the performance boost?

2) How does the synthetic data generated by Llama-3.1-70B differ in quality or characteristics from the high-quality tokens selected by the annotator? Could you provide examples or metrics that highlight these differences?

3) Your results suggest that grouping by language before repository improves performance. Could you elaborate on why this approach works better? Have you considered any hybrid methods that combine cross-language learning with language-specific training?

4) Given the success of Arctic-SnowCoder-1.3B with 555B tokens, how do you envision scaling this approach for larger models or different domains? Are there diminishing returns or unique challenges you anticipate?

5) The paper focuses on benchmarks like BigCodeBench and HumanEval+. How do you ensure these benchmarks reflect real-world programming challenges? Have you considered any additional metrics or benchmarks that might better capture practical coding scenarios?

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
The authors emphasize the critical role of high-quality data in the effective pretraining of language models, particularly within the code domain, while noting that the precise definition of "high-quality" remains inadequately explored. To address this, they introduce Arctic-SnowCoder-1.3B, a data-efficient base code model pretrained on 555 billion tokens through three phases of progressively refined data. The first phase involves general pretraining with 500 billion standard-quality code tokens, processed through basic filtering, deduplication, and decontamination. The second phase continues with 50 billion high-quality tokens, selected from the first phase by a BERT-style quality annotator trained to distinguish good code from random data, using high-quality code files and instruction data from Magicoder and StarCoder2-Instruct. The final phase employs 5 billion synthetic tokens generated by Llama-3.1-70B, using phase two data as seeds and adapting the Magicoder approach for pretraining. Despite the limited dataset, Arctic-SnowCoder achieves state-of-the-art performance on BigCodeBench, outperforming similarly sized models trained on up to 1 trillion tokens, including a 36% improvement over Phi-1.5-1.3B. Across various benchmarks, Arctic-SnowCoder-1.3B performs better than StarCoderBase-3B pretrained on 1 trillion tokens and matches the performance of leading small base code models trained on trillions of tokens.

### Strengths
+ Important Area.

The authors address a critical aspect of language model development—high-quality data in the code domain—which is essential for improving model performance and applicability. 



+ Good Performance on BigCodeBench

Arctic-SnowCoder-1.3B demonstrates good results, achieving state-of-the-art performance on BigCodeBench and surpassing similarly sized models trained on up to 1 trillion tokens, including a notable 36% improvement over Phi-1.5-1.3B.

### Weaknesses
1. Limited Novelty: While the use of a data annotator to extract high-quality data for pretraining is a valuable approach, it is not entirely novel. Similar methodologies have been employed, such as using GPT-4 as a data annotator. This raises questions about the uniqueness of the authors' contributions.

2. Missing Baselines: The evaluation would benefit from the inclusion of additional baselines, such as OpenAI's GPT models. Comparing or discussing these established models would provide a more comprehensive context for assessing Arctic-SnowCoder's performance and highlight its relative strengths and weaknesses.

3. Lower than Phi-1.5-1.3B on HumanEval+ MBPP+ and EvoEval: Despite achieving strong performance on BigCodeBench, Arctic-SnowCoder-1.3B underperforms compared to Phi-1.5-1.3B on more general code generation tasks, such as HumanEval+, MBPP+, and EvoEval. Interestingly, Phi-1.5-1.3B achieved better results with less training data, which suggests that Arctic-SnowCoder's specialized pretraining on high-quality code tokens may not necessarily translate into better generalization across a broader range of benchmarks.

### Questions
The authors address a critical aspect of language model development—high-quality data in the code domain—which is essential for improving model performance and applicability. For the experiments, Arctic-SnowCoder-1.3B demonstrates good results, achieving state-of-the-art performance on BigCodeBench and surpassing similarly sized models trained on up to 1 trillion tokens, including a notable 36% improvement over Phi-1.5-1.3B.

However, I have three concerns:

1. Limited Novelty: While the use of a data annotator to extract high-quality data for pretraining is a valuable approach, it is not entirely novel. Similar methodologies have been employed, such as using GPT-4 as a data annotator. This raises questions about the uniqueness of the authors' contributions.

2. Missing Baselines: The evaluation would benefit from the inclusion of additional baselines, such as OpenAI's GPT models. Comparing or discussing these established models would provide a more comprehensive context for assessing Arctic-SnowCoder's performance and highlight its relative strengths and weaknesses.

3. Lower than Phi-1.5-1.3B on HumanEval+ MBPP+ and EvoEval: Despite achieving strong performance on BigCodeBench, Arctic-SnowCoder-1.3B underperforms compared to Phi-1.5-1.3B on more general code generation tasks, such as HumanEval+, MBPP+, and EvoEval. Interestingly, Phi-1.5-1.3B achieved better results with less training data, which suggests that Arctic-SnowCoder's specialized pretraining on high-quality code tokens may not necessarily translate into better generalization across a broader range of benchmarks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a  method that includes three different pre-training phases, combined with iterative improvements to the quality of training data. It presents a code model—Arctic-SnowCoder-1.3B—which demonstrates competitive performance compared to current small code models, while significantly reducing the number of tokens used. The paper also provides guidelines for repo-level data grouping, learning rate scheduling, and emphasizes the importance of high-quality data.

### Strengths
1. This paper proposes a method for improving the performance of pre-training models by focusing on multi-stage data quality enhancement. It introduces a high-performing code model with low token usage. 
2. Additionally, the paper analyzestraining strategies, including emphasizing the preparation of training data files and the characteristics of learning rate scheduling.

### Weaknesses
This paper primarily focuses on techniques for enhancing and filtering the quality of code training data, with a key emphasis on how high-quality, filtered data improves model performance. However, an important question arises: could this improvement come at a cost, such as reduced generalization ability on non-target domain tasks?

Additionally, the paper should review some existing techniques for improving training data quality and, where appropriate, include comparative analyses to demonstrate the advantages of the proposed method.

### Questions
There are some questions after reviewing the paper:
1. In line 190,  "increase the Python mix ratio to approximately 50% while keeping the proportions of the other languages unchanged.", why is Python set as the primary language data, and how can it be adjusted for other languages?
2. In line 295,  "We can observe that the second approach, which we finally adopt in general pretraining, performs significantly better than the first one.", could you further explain the reason behind this conclusion?
3. In line 351, "the key to high-quality data is essentially the alignment with downstream application distributions.", what is the difference between alignment and fine-tuning of pre-trained models? And what are the advantages of the method proposed compared to fine-tuning techniques?

### Soundness
2

### Presentation
2

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
The authors provide practical findings through pretraining a small code language model (Code LM), which achieves SOTA performance on representative coding benchmarks like HumanEval, MBPP, and BigCodeBench, among the Code LMs with similar sizes.

### Strengths
The authors documented various valuable practices of pretraining Code LMs from scratch, which can inspire future work in this direction:
- Training a BERT-based classifier to annotate code quality, which is very efficient compared to any LLMs-as-Judges approaches.
- Using re-warmup as the learning rate schedule is quite novel.
-  While previous studies [1] suggest that deduplicating the data will result in better model performance, training on the repeated high-quality code data can further improve the coding capabilities.

The authors also shared a few interesting findings:
- "Textbook" is not all you need, so improving "educational value" in the training data may not be optimal.
- Re-warmup performs much better than other conventional schedules, such as linear and constant.
- When the number of high-quality tokens is limited to 50B, the setup of 12.5B with four repetitions could be more optimal.

[1] Lee, K., Ippolito, D., Nystrom, A., Zhang, C., Eck, D., Callison-Burch, C., & Carlini, N. (2022, May). Deduplicating Training Data Makes Language Models Better. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 8424-8445).

### Weaknesses
There are a few weaknesses in this paper:
- The current evaluations are Python-only, and the evaluation on multilingual (programming languages) code generation may share more interesting findings. Specifically, the paper does not explore how the pretraining strategies generalize to other languages with different syntax and semantics, such as Java or C++. This limits the scope of the findings and leaves open the question of whether the observed improvements are specific to Python or more broadly applicable. The absence of multilingual evaluation is a significant gap that should be addressed to demonstrate the robustness of the proposed approach.
- The authors only study the 1.3B models, which is considered a bit small. While I understand that pretraining LMs is very costly, is it possible for the authors to provide more motivation for studying the ~1B models? While the authors mention the cost of pretraining, a more detailed justification for focusing on this specific model size is needed. For example, they could discuss the trade-offs between model size and computational resources, or perhaps explore the performance of smaller models in relation to the 1.3B model to better understand the scaling behavior of their approach. Without this, the choice of model size seems somewhat arbitrary.
- It is most likely that the data cannot be opened due to legal constraints.

### Questions
1. Regarding the openness of this work, will the authors consider making the data pipeline and models publicly available? This will greatly help future studies on Code LM pretraining.
2. Regarding the evaluation, can the authors provide some explanations as to why BigCodeBench results are omitted in most of the tables?
3. Can the authors share more insights on how current setups documented in the paper can be generalized to larger Code LMs (e.g., 10B+)?

### Soundness
3

### Presentation
3

### Contribution
2
