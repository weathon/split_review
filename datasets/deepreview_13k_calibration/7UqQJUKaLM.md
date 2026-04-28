# xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The continuous advancement of large language models (LLMs) has brought increasing attention to the critical issue of developing fair and reliable methods for evaluating their performance. Particularly, the emergence of cheating phenomena, such as test set leakage and prompt format overfitting, poses significant challenges to the reliable evaluation of LLMs. As evaluation frameworks commonly use Regular Expression (RegEx) for answer extraction, models may adjust their responses to fit formats easily handled by RegEx. Nevertheless, the key answer extraction module based on RegEx frequently suffers from extraction errors. Furthermore, recent studies proposing fine-tuned LLM as judge models for automated evaluation face challenges in terms of generalization ability and fairness. This paper comprehensively analyzes the entire LLM evaluation chain and demonstrates that optimizing the key answer extraction module improves extraction accuracy and enhances evaluation reliability. Our findings suggest that improving the key answer extraction module can lead to higher judgment accuracy and improved evaluation efficiency compared to the judge models. To address these issues, we propose xFinder, a novel evaluator for answer extraction and matching in LLM evaluation. As part of this process, we create a specialized dataset, the \textbf{K}ey \textbf{A}nswer \textbf{F}inder (KAF) dataset, to ensure effective model training and evaluation. Generalization tests and real-world evaluations show that the smallest xFinder model, with only 500 million parameters, achieves an average extraction accuracy of 93.42\%. In contrast, RegEx accuracy in the best evaluation framework is 74.38\%. The final judgment accuracy of xFinder reaches 97.61\%, outperforming existing evaluation frameworks and judge models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel evaluator for answer extraction and matching in LLM evaluation. The main idea is to first construct a large-scale LLM response evaluation dataset, and then train (small) LLMs on it. This paper conducts an extensive evaluation of multiple tasks with comparison with multiple LLM-based evaluators.

### Strengths
1 A large dataset that can be used for further LLM-based evaluation.
2 A new model that can be used for more reliable evaluation.

### Weaknesses
To be perfectly honest, I am not an expert in LLM-based evaluation. But to me, the main contribution is the construction of a dataset that can help train LLM evaluators, with the help of other LLMs (e.g GPT-4). Thus the novelty of the proposed model is less convincing as it does not provide any new architecture. Training LLMs on evaluation data as evaluators have also been explored in previous research, such as [1] and its subsequent work. Could the authors explain more on its novelty? For example, in terms of training process, and model architectures, how does the xFinder differ from previous work that trains LLMs on evaluation data? Also, would it possible to prompt GPT-4 or other very big LLM using ICL with the constructed data, and how would it perform?

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces xFinder, a novel evaluator designed for answer extraction and matching in the context of LLM evaluation. The study identifies the limitations of current answer extraction modules, particularly those based on RegEx, in handling inconsistencies in model response formats. To address these issues, the authors propose xFinder to enhance extraction accuracy and evaluation reliability. The authors developed a dataset called the Key Answer Finder (KAF) dataset to train xFinder. Experimental results demonstrate that xFinder significantly outperforms existing frameworks and model-based evaluators in terms of extraction accuracy and evaluation efficiency.

### Strengths
The identified challenges in LLM response extraction and matching are realistic and merit attention.

The paper proposes a novel method to improve answer extraction modules, addressing limitations in existing approaches.

The paper is well-structured, with a clear progression from problem definition to methodology and experimental analysis.

### Weaknesses
Although the KAF dataset is used to validate xFinder’s performance, the paper lacks a comprehensive exploration of the model’s generalizability to entirely different datasets and error types.

The paper does not include sufficient experimental analysis on the impact of xFinder on final evaluation outcomes, such as a comparison between using xFinder and other extraction methods in terms of evaluation results.

There is a lack of detailed analysis of the KAF dataset’s quality, such as inter-annotator agreement metrics.

### Questions
see weaknesses

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
The paper introduces xFinder, a tool designed to enhance the accuracy of evaluating large language models by improving key answer extraction and matching. It identifies flaws in current methods like test set leakage and RegEx limitations, proposes a new dataset (KAF) for training, and shows xFinder outperforms traditional and other automated judge models in extraction and judgment accuracy, thus contributing to more reliable LLM evaluations.

### Strengths
- The significance of accurate answer extraction in evaluations is often underestimated, yet it critically impacts results. This study rightly emphasizes this aspect.
- xFinder demonstrates strong performance in accuracy over conventional RegEx frameworks.
- Both the model and its dataset are immediately usable for enhancing the reliability of LLM assessments.
- The paper effectively outlines the problems in current evaluation methods and introduces a well-structured solution.

### Weaknesses
 - The techniques may not be applicable to responses where the answer is not a short, extractable phrase.
- Although the results are promising, I suspect the technique might be replaced by stronger LLMs used as judges with improved prompting techniques in the near future, which could also generalize better for longer responses. The results in Table 3 are good, showing that even GPT-4 as a judge does not perform as well as xFinder. Therefore, I believe xFinder remains useful at this moment for tasks that have a similar distribution to its training data. It will also be interesting to discuss the combination of xFinder and other techniques.

### Questions
What is the prompt you used for GPT-4 as Judge (CoT)?

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
5

### Summary
The paper proposes a training dataset KAF for key answer extraction and the correspondingly trained models, xFinder. The motivation lies in improving the extraction of answers in LLM responses for more reliable evaluation. The authors create KAF based on various LLMs, different evaluation tasks, and widely used prompting techniques, i.e., CoT and few-shot prompting. Based on the comprehensive experiments in the paper, xFinder outperforms RegX and other LLM-based methods in answer extraction.

### Strengths
The paper is solid enough on all claims with its comprehensive experiments. The proposed KAF dataset is suitable for future research on developing more reliable evaluation systems. The xFinder models are more efficient and reliable than current LLM-based methods. In all, the paper did a good engineering research on using LLMs to better find the answers from their own responses.

### Weaknesses
- **Missing Related Work**: The work [1] is also highly related to this work, especially for the Judgement Accuracy part. It holds a similar idea by comparing different evaluation methods, including LLM-based ones, in directly evaluating open-question answering.

- **Annotation Agreement**: Human rechecking is one of the significant parts of the data generation pipeline. What are the annotation agreements between annotators? It's crucial to understand the level of consistency in human judgments, especially given the subjective nature of key answer extraction. Without a clear metric of inter-annotator agreement (e.g., Cohen's Kappa), the reliability of the KAF dataset is questionable.

- **Human/Case Study**: Except for those numbers in the experiment tables, it is important to do the case study on the output of xFinders. For example, **How and Why is xFinder better**, **Is it worth using xFinder other than RegX or other LLM-based methods?**, **Summarize the failure modes of those inferior methods and how xFinder could perform better in these cases.**, etc. The paper needs to provide concrete examples of where xFinder excels and where other methods falter, going beyond aggregate performance metrics.

- **Writing**: I recommend adding more content about experimental settings, such as evaluation metrics, baseline models, etc, to the main text. There are too many staff in the Appendix. Things could be clearly explained in the main text for better reading.

### Questions
- **Why does the key extraction task need to have ``short text`` and ``alphabet option`` categories, as the former could be transformed into the latter?**

- **Does the order of the xticks in the bump charts affect the comparison between ``alphabet option`` and ``short text``?**

- **What is the trade-off between xFinder and simply adding one or more regular expression patterns in RegX?**: It is known to us that LLMs are good at learning patterns and following instructions, which could have further enhancements as the models' reasoning capabilities are further enhanced. xFinder indeed makes good improvements, but where do they come from? We must be sure that xFinder (or future work) helps answer extraction better than RegX, such as finding answers from those nasty answer patterns. After all, it is easy to write RegX patterns nowadays by simply prompting GPT-4 and LLM-based methods are still inefficient compared to lexical methods.

### Soundness
4

### Presentation
3

### Contribution
4
