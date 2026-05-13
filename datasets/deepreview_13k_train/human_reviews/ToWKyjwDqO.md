# Direct Judgement Preference Optimization

- Decision: Reject
- Scores: 3, 3, 8, 6

## Abstract
Auto-evaluation is crucial for assessing response quality and offering feedback for model development. Recent studies have explored training large language models (LLMs) as generative judges to evaluate and critique other models' outputs.
In this work, we investigate the idea of learning from both positive and negative data with preference optimization to enhance the evaluation capabilities of LLM judges across an array of different use cases.
We achieve this by employing three approaches to collect the preference pairs for different use cases, each aimed at improving our generative judge from a different perspective. 
Our comprehensive study over a wide range of benchmarks demonstrates the effectiveness of our method.
In particular, our generative judge achieves the best performance on 10 out of 13 benchmarks, outperforming strong baselines like GPT-4o and specialized judge models.
Further analysis show that our judge model robustly counters inherent biases such as position and length bias, flexibly adapts to any evaluation protocol specified by practitioners, and provides helpful language feedback for improving downstream generator models.\footnote{The code and our judge models will be released for research purposes.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper "Direct Judgement Preference Optimization" improves large language models (LLMs) used as generative judges by introducing Direct Preference Optimization (DPO), which enhances evaluation by learning from both positive and negative examples. The authors train models on pairwise comparison, single ratings, and classification tasks using a mix of human and synthetic data, including Chain-of-Thought (CoT) critiques and response deduction. Their models outperform baselines like GPT-4o across 13 benchmarks, mitigate biases, and adapt to various evaluation protocols, offering more robust and flexible performance while also providing valuable feedback for improving other models.

### Strengths
**Diverse Evaluation Tasks**: The paper proposes a comprehensive evaluation framework, including pairwise comparisons, single ratings, and binary classification. This makes the model adaptable to different evaluation needs​.

**Model Performance**: The paper demonstrates that their judge models outperform existing baselines, such as GPT-4o and specialized judge models, across multiple benchmarks, including pairwise comparison, single rating, and classification tasks​.

**Bias Mitigation**: The model robustly counters common biases, such as position and length bias, offering improved generalization across evaluation protocols.

### Weaknesses
 **Content organization **: The organization of this paper could be further improved, for example, structurize some long paragraphs.


**Design philosophy**: The paper could be strengthened by providing a more detailed explanation of the design philosophy, including the rationale for including each component, their individual functions and relationships, and how they relate to the background presented in Section 2. An ablation study or discussion of the impact of removing individual components would also be valuable.

### Questions
See the Weaknesses.


The authors could enhance the paper by clarifying the relationship between Direct Judgement Preference Optimization and Direct Preference Optimization, highlighting key similarities and differences. Additionally, they could more explicitly state the main takeaways of the paper and explain how their use of three types of data for DPO differs from and improves upon the original DPO approach.

What are the takeaway messages of this paper? It seems like the authors use three types of data for DPO rather one type in the original DPO?

### Soundness
3

### Presentation
3

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
This paper curates the preference data to train an LLM as an evaluation judge using DPO, and demonstrates the effectiveness of the trained models in different sizes (e.g., 8B, 12B, 70B) on three types of evaluation tasks (e.g., pairwise comparison, single rating and classification). The contribution lies in the method of creating preference data for three evaluation tasks using a collection of labeled data from diverse data sources (annotated by humans or other models).

### Strengths
**Originality v.s. Significance**: This paper proposes to process existing annotated data into the preference data format, and train an LLM as a judge using DPO on the curated data. It’s a straightforward application of DPO to the task of training an LLM for evaluation. The novelty lies in the way of constructing preference data from existing labeled datasets for three evaluation tasks — but see the novelty concerns in the weakness section below. The technical novelty is weak, compared to the significance of releasing a good evaluation model to the community. However, I don’t find the statement of releasing the model checkpoints and the curated data from the paper. It’d be better to clarify this explicitly. 

**Quality**: Extensive experiments and analyses have been conducted on seven pairwise comparison benchmarks, four single rating benchmarks, and two classification benchmarks.

### Weaknesses
 **Novelty of data curation**: As the main contribution of this paper is data curation, it’s better to clarify the difference between this work and existing studies on data curation for LLM evaluation. The key differences are still unclear even after reading the description in Lines 136-150. From Table 1, existing studies have explored the three evaluation tasks (Vu et al., 2024), and have used both SFT and DPO (Want et al, 2024c). This paper seems incremental to combine what has been done in existing studies at a larger scale of training data. Specifically, the paper does not clearly articulate how the preference data is constructed for each of the three evaluation tasks. For instance, how are the positive and negative examples selected for the pairwise comparison task? Are they based on human annotations, or model-generated outputs? If the latter, what is the process for ensuring the correctness of the preference data? The paper also lacks details on the specific prompts used to elicit the desired behavior from the LLMs, which is crucial for reproducibility and understanding the model's capabilities. Furthermore, the paper does not discuss the potential biases introduced by the data curation process itself. For example, if the preference data is derived from existing datasets, it may inherit the biases present in those datasets, which could affect the fairness and reliability of the evaluation model.

**Presentation**: It’s hard to interpret the results and the evaluation with other baseline models (see details in the question section below). The tables and figures are far away from their corresponding text descriptions, making it hard to read them at the same time. The paper also lacks a clear explanation of the evaluation metrics used for each task. For example, while accuracy is mentioned for classification, the specific metrics used for pairwise comparison and single rating tasks are not clearly defined. This makes it difficult to compare the results with other studies and to assess the true performance of the proposed model. The lack of detailed information on the evaluation setup, such as the specific hardware and software used, further hinders the reproducibility of the results.

### Questions
1. In Line 315, what do you mean by evaluating models trained for single ratings on classification? How do you use a model trained for single ratings to evaluate classification tasks?
2. In Line 314, “All baselines are evaluated only on the tasks they are trained for”.  Can you report which tasks these baselines are trained for? How can you get the results for the tasks that these baselines are not trained for in Table 1 & 2? Do you get the baseline models’ results from their papers or run the baseline models by yourself? Do you test your models on those benchmarks without further fine-tuning your models on the benchmark data at all?
3. In Table 5, what are the 6 types of biases? And How do you measure these biases? I understand the position bias can be measured by the consistency of choosing responses even if the order is swapped. But what about the other biases?
4. Line 464 claims that “we plot the average performance across all three evaluation tasks when removing each training task”, but Fig 4 may miss the SFT+DPO w/o CoT critique.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores enhancing large language models (LLMs) as generative judges for evaluating model responses and generating critiques. It introduces direct preference optimization (DPO) using diverse human and synthetic judgments to improve evaluation across pairwise, single ratings, and binary classification tasks. The trained models, especially the 8B parameter model, outperform strong baselines and specialized judge models, showing robust performance and adaptability across various benchmarks.

### Strengths
1. The problem of automated evaluation is important and well studied in recent years. Thus, the work is well motivated.
2. Use of DPO using positive and negative pairs to improve LLM eval is novel. Response deduction is also a nice idea.
3. The framework is comprehensive -- works on 3 eval setttings -- Single Rating, Pairwise Comparison, and Classification.
4. Comprehensive eval on seven pairwise comparison benchmarks, four single rating evaluation benchmarks, and two classification benchmarks. The results are convincingly better compared to our SOTA models and even gpt4o.
5. Bias evaluation results, ablations, flexible prompting strategies, downstream model improvements -- are all nice additions in the paper.

### Weaknesses
1. It will be interesting to see how easy vs hard negatives can help. Given the current way of generating negatives, it is unclear if they were hard enough and if a mix of easier and hard negatives could help improve further.
2. Choice of 70%:15%:15% for DCoT, DStd and DDed sounds somewhat arbitrary. Can you provide further reasoning behind this?
3. Broadly a comparison to evaluation systems with multiple models is not expected as such, but still it will be nice to compare and check how does your method works compared to methods like reconcile.

Typos:
1. citep vs citet should be used properly. E.g. line 41 should have "GPT-4 (OpenAI, 2023)" and not "GPT-4 OpenAI (2023)".
2. Notations M_t vs M_{teacher} or M'_{teacher} do not match between Section 3 and Fig. 2. Same for student model.

### Questions
1. Is it possible to quantify hardness of negatives and does that correlate with evaluation accuracy?
2. Choice of 70%:15%:15% for DCoT, DStd and DDed sounds somewhat arbitrary. Can you provide further reasoning behind this?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper explores the use of preference learning algorithms (DPO) to enhance the evaluation/critique capabilities of LLMs. By relying on human-annotated judgment scores to automatically assess the quality of model-generated critiques, they are classified into chosen or rejected categories, facilitating the preference learning. Additionally, the authors designed three training methods: Chain of Thought (CoT), standard judgment, and response deduction to optimize the model, achieving impressive experimental results on 13 benchmarks, covering pairwise, point-wise, and binary classification evaluation protocols.

### Strengths
* This paper thoroughly analyzes the contribution of three different training examples to enhancing model evaluation and reflection capabilities: CoT, standard judgment, and response deduction. 
* The authors conducted extensive testing on 13 benchmarks covering three types of evaluation protocols: pairwise, pointwise, and classification, with experimental results demonstrating superiority over existing baselines. 
* The proposed method maintains good reliability in terms of bias in LLM-as-a-judge.

### Weaknesses
### 1. Some Prior Works Need to Be Discussed

Using preference learning for optimization sounds impressive, but some prior work have already utilized preference learning to enhance the evaluation/critique capabilities of LLMs, such as CriticGPT  [1] and Themis [2]. 

1. CriticGPT employs a standard RLHF workflow to improve the evaluation/critique capabilities of LLM in the code generation task, relying heavily on cost human annotations. 

2. Similarly, Themis also utilizes DPO to enhance the evaluation capabilities of language models. Themis also automatically construct the preference data by checking if the model's judgment scores are consistent to human-annotated judgment scores. In terms of motivation and implementation details, there is not much difference between this paper and Themis. Of course, the authors introduce three different preference examples to enhance the capabilities of LLMs. 

However, from my perspective, these two works need to be carefully compared and analyzed in this paper. Although the authors can compare the Themis with proposed method (CriticGPT is a closed-sourced model), I do not recommend doing so because I believe there may be numerous variables that could affect the experimental results, such as the size of the dataset and the optimization techniques (Themis re-designs the DPO loss).

Beyond above comments, this paper, Themis, and CriticGPT heavily rely on human-annotated judgment labels to automatically construct preference datasets. Therefore, the scalability of these methods is limited. I hope to receive some detailed discussion and analysis from the authors on this aspect.



### 2. Flexibility of Evaluation Critiera

Similar to models in the Prometheus family, the current model's input includes an additional evaluation protocol except for the user query and the evaluated response. Therefore, during real-world evaluation setting, additional craft of evaluation criteria is required, as demonstrated in lines 328-329. Although Section 5.4 demonstrates that the impact of the crafted evaluation protocol on evaluation is limited, both this paper and Prometheus-like models require the input of an evaluation protocol (no matter the human-annotated or automatically generated by GPT-4). Therefore, when performing evaluation in real-world scenarios, this severely limits the scalability of the method because it may require additional supervision of humans and advanced models (From my perspective).

### 3. Coarse-grained Evaluation Aspects

As demonstrated in Section 4.2 (line 231 tp line 234), the evaluation aspects for building training dataare general quality, like facuality, helpfulness, safety, etc, which is limited and coarse-grained, compared to previous works like Auto-J and Prometheus.
For example, Auto-J introduces 58 tasks and corresponding fine-grained evaluation criteria. Prometheus generate the score-rubrics-like customized evaluation criteria for specific user queries.

### 4. Without the evaluation of  textual critques quality (Chain-of-Thought)
This paper only evaluate the quality of judgment scores, while neglect the evaluation of textual critique quality (the quality of chain-of-thought). Previous works have demonstrated that even if the judgment score is consistent with human-annotated, their chain-of-thought may contains several flaws [3]. This will introduce numerous bias and drawbacks for application of the fine-tuned critique model in some important reseach fields, like the self-improvement of LLMs.

### Questions
1. This paper, Themis, and CriticGPT heavily rely on human-annotated judgment labels to automatically construct preference datasets. Therefore, the scalability of these methods is limited. 

2.  When performing evaluation in real-world scenarios, requiring the input of evaluation criteria limits the scalability of the method because it may require additional supervision of humans and advanced models.

I hope to receive some detailed discussion and analysis from the authors on these aspects.

### Soundness
3

### Presentation
3

### Contribution
3
