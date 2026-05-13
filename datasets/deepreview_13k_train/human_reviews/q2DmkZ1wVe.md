# CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark

- Decision: Accept
- Scores: 6, 5, 5, 8

## Abstract
While Large Language Models (LLMs) excel in question-answering (QA) tasks, their real reasoning abilities on multiple evidence retrieval and integration on Multi-hop QA tasks remain less explored. Firstly, LLMs sometimes generate answers that rely on internal memory rather than retrieving evidence and reasoning in the given context, which brings concerns about the evaluation quality of real reasoning abilities. Although previous counterfactual QA benchmarks can separate the internal memory of LLMs, they focus solely on final QA performance, which is insufficient for reporting LLMs' real reasoning abilities. Because LLMs are expected to engage in intricate reasoning processes that involve evidence retrieval and answering a series of sub-questions from given passages. Moreover, current factual Multi-hop QA (MHQA) benchmarks are annotated on open-source corpora such as Wikipedia, although useful for multi-step reasoning evaluation, they show limitations due to the potential data contamination in LLMs' pre-training stage. To address these issues, we introduce a Step-wise \textbf{Co}unter\textbf{f}a\textbf{c}tu\textbf{a}l benchmark (CofCA), a novel evaluation benchmark consisting of factual data and counterfactual data that reveals LLMs' real reasoning abilities on multi-step reasoning and reasoning chain evaluation. Our experimental results reveal a significant performance gap of several LLMs between Wikipedia-based factual data and counterfactual data, deeming data contamination issues in existing benchmarks. Moreover, we observe that LLMs usually bypass the correct reasoning chain, showing an inflated multi-step reasoning performance. We believe that our CofCA benchmark will enhance and facilitate the evaluations of trustworthy LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a new dataset, CofCA for evaluating LLM’s counterfactual multi-hop reasoning ability, which focuses on both final answer evaluation and reasoning step evaluation. The dataset construction involves 2 steps, 1) the sampled Wikipedia paragraphs are sent to GPT-4 for entity replacement and paraphrase, and then back-translation is done to further modify the paragraphsm and then these paragraphs are manually checked 2) GPT-4 is then used to generate QA pairs based on the newly generate paragraphs. Here GPT-4 is asked to generate both overall multi-hop QA pair and subquestion answer pairs, and the resulting data is also manually verified. 
The authors then conducted experiments on both newly generated data and HotpotQA, 2WikiHop and Musique, using both closed-sourced models and open-source models. The results show that all LLMs suffer significant performance drop on counterfactual questions and the joint performance which considers both final answer and reasoning process correctness can be even worse, exposing the weakness of current LLMs.

### Strengths
1. CofCA could be a valueable resource for studying LLM’s true reasoning ability. Due to its counterfactual nature, the LLMs can no longer use their internal knowledge for finding reasoning shortcut, hence the model have to reason over provided context. Also, the annotation of intermediate sub question answer pairs can also enable examination of the reasoning process. 

2. The experiments and analysis are very thorough. The results show a clear trend of performance vs question complexity and the analysis on the reasoning process further exposes the weaknesses of the SOTA LLMs.

### Weaknesses
My main concern is the scale of the passages set when constructing the data. For previous datasets such as. HotpotQA and 2WikiHop, they usually construct questions using multiple passages to ensure that the answer have to be deducted from multiple pieces of evidence. However, it seems that for CofCA, the questions are generate using only a single passage? If this is the case, how can you make sure the generated multi-hop QA pairs are fully grounded to the passage?

### Questions
See weaknesses

### Soundness
3

### Presentation
3

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
The paper introduces CofCA, an evaluation benchmark for multi-hop reasoning abilities of LLMs over counterfactual data. CofCA is created by (1) LLMs alter Wikipedia passages by replacing keywords with counterfactual information, and (2) LLMs generate multi-hop questions over the modified passages. Both steps are manually verified by human annotators, and the benchmark includes 900 multi-hop questions from 300 passages. Experimental results show a gap between performance on the counterfactual CofCA and existing multi-hop QA datasets. Additionally, the paper shows that the low performance is due to reasoning failures.

### Strengths
- A counterfactual multi-hop benchmark can be helpful to understand the ability of LLMs to perform multi-hop reasoning. The benchmark will be publicly available in addition to the annotation guidelines and implementation details.

- The paper features extensive quantitative analysis examining the effect of the annotation pipeline and the performance of sub-questions amongst others.

### Weaknesses
 - Given the examples presented in the paper, I was not fully convinced about several aspects of the collected data. Mainly, how do you ensure that the counterfactual information does not contradict real-world facts? In the example shown in Figure 1d, no such coach exists that serves the Chinese national basketball team and was born in 1997. If counterfactuals contradict real-world facts, a performance degradation is expected. Also, both examples in the main paper seem to have shortcuts, e.g., there is only one position in the example in Fig.1, and only one designer in the example in Fig. 2. This could lead to models answering correctly without performing multi-hop reasoning.

- Qualitative analysis - the analysis presented in Section 5 did not fully address the concerns above, and is limited to 20 correct/incorrect questions with GPT-4. A more thorough analysis regarding the quality of the generated data is needed, specifically examining contradiction and shortcuts. This analysis should verify that the main claims of the paper (multi-hop QA is more challenging on counterfactual information) are supported. For example, an error analysis comparing different error categories (reasoning failures, evidence retrieval errors, contradictions) between factual and counterfactual questions could reveal whether the performance gap is due to reasoning failures or contradictions with pre-existing knowledge.

- Presentation - the presentation in several parts of the paper was a bit hard to follow. For example, in Fig.1, the text is very small and there is an error (the bottom-right box the question is about the coach and the answer is Point Guard). In Tab.2, the ‘Whole data property’ is not the sum of the other columns (I assume this is due to the factual questions sampled from other datasets?). The main results in Section 4.2 require comparing between information presented in different tables (Tables 3 and 4). Table 8 is referenced before Table 7 but presented afterwards.

### Questions
See weaknesses, mainly:
- Does the counterfactual information contradicts real-world facts? If so, isn't some degradation in performance expected? 
- How often are shortcuts in the collected examples? 
- What qualitative analysis did you consider that might strengthen the main claims of the paper?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new dataset called CofCA, designed to effectively assess LLMs' capability in counterfactual multi-hop question answering. The authors generate the dataset by starting with Wikipedia passages and applying techniques such as entity replacement and back-translation to create question-answer pairs. The models are then evaluated at both the final-answer level and the sub-question level. To ensure the quality of the dataset, the authors perform thorough quality checks and include human-in-the-loop validation throughout the dataset construction process.

### Strengths
1. The paper is well-written and easy to follow, presenting the content in a clear and accessible manner.

2. The authors demonstrate an awareness of the limitations of using Exact Match (EM) and F1 scores when evaluating the output of large language models (LLMs). To address this, they introduce an additional Partial Match metric, which helps mitigate the issue and provides a more nuanced evaluation.

### Weaknesses
1. One major drawback of the paper is that, while it claims to assess LLMs' true reasoning abilities, it primarily reports the accuracy of different sub-questions without fully addressing whether the models are capable of reasoning holistically. For a more comprehensive evaluation of reasoning abilities, other factors should also be considered, such as whether the model is able to effectively decompose the problem into meaningful or correct sub-questions, rather than treating them as isolated tasks. The paper does not delve into the quality of the generated sub-questions themselves, such as whether they are logically connected and contribute to the final answer in a meaningful way. It's possible that a model could achieve high sub-question accuracy by simply memorizing patterns without true reasoning.

2. The quality of the dataset is also in question. Currently, the correctness and informativeness of the dataset are evaluated using GPT-4. However, as the paper itself shows, GPT-4 struggles to correctly answer these questions, which suggests that it may not be fully reliable for assessing the quality of the dataset. This raises concerns about the robustness of the dataset validation process. Furthermore, relying on a single model for validation introduces potential biases and may not capture the full spectrum of potential errors or ambiguities within the dataset. The paper should explore alternative validation methods or involve multiple models and human annotators to ensure higher dataset quality.

3. There is further concern about ensuring that the generated questions are non-trivial. As shown in Table 9, the prompt generates the multi-hop questions and the sub-questions, along with their answers, simultaneously. This raises a natural concern that the generated multi-hop questions may either be independent of these sub-questions or follow a single pattern (e.g., q1->q2->q3), leading to a lack of diversity in question structure. The paper does not address or discuss this potential limitation. The simultaneous generation of questions and sub-questions could result in a dataset where the multi-hop questions are artificially constructed to fit the pre-determined sub-questions, rather than reflecting genuine multi-hop reasoning challenges.

4. When benchmarking models, the paper lacks evaluation on more recent and advanced models, such as GPT-4 Turbo, GPT-4O, and Claude series, as well as newer open-source models like LLaMA 3 or Deepseek. Including these models would provide a more up-to-date and comprehensive analysis of the current state-of-the-art in LLMs. The absence of these evaluations limits the generalizability of the findings and leaves open the question of how these newer models would perform on the proposed dataset.

### Questions
1. Could you provide a more intuitive explanation for the **JOINT COMPUTATION** metric mentioned in Appendix B? An example or simplified breakdown might help readers understand its significance and how it is calculated in practical terms. This would not only make technical details more accessible but also allow readers to better appreciate its role in evaluating model performance.

### Soundness
3

### Presentation
3

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
The paper is designed to evaluate large language models (LLMs) on multi-hop counterfactual reasoning abilities. CofCA generates counterfactual contexts that LLMs likely haven’t encountered during pre-training, and ask questions based on the counterfactual contexts.  It also emphasizes sub-question evaluation for each reasoning step. 

The evaluation in this paper reveals that models like GPT-4 show inflated scores in standard QA due to these contamination issues, while performance drops on CofCA due to its reasoning on counterfactual contexts, highlighting the gap between LLM memory and genuine reasoning.

### Strengths
1. CofCA minimizes data contamination by creating a cleaner benchmark for evaluating LLM reasoning.

2. The diverse counterfactual and factual datasets allow researchers to observe performance discrepancies, adding depth to LLM evaluation.

3. The constructed dataset is clearly different from existing counterfactual QA benchmarks, including distentQA and IfQA. The multi-hop challenge lacks of enough study in counterfactual setting.

### Weaknesses
1. More open-source LLMs should be evaluated on the benchmark, like llama-3 or 13B-level models.

2. OpenAI o1 was evaluated in the paper, it shows using long reasoning-chains could help a lot on this reasoning tasks, and more insights on comparing o1 reasoning with 4o reasoning could be insightful.

### Questions
As given in the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
