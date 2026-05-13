# BALCONI: BALancing CONtext  and Internal Knowledge For Training Flexible LLMs

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
The faithfulness to the context is significant for large language models (LLMs)  in tasks such as Retrieval-Augmented Generation (RAG) or Information Extraction. However, LLMs can exhibit a "stubborn" reliance on their internal knowledge, which leads to failure in maintaining faithfulness to the context. Ideally, a model should leverage the given context if the user instruction requires to, yet remain correctness based on internal knowledge when the instruction does not provide the context. Considering such scenarios, we propose a balanced benchmark, FaithfulBench, to evaluate the faithfulness of LLMs, together with internal knowledge correctness in LLMs and evaluate whether the improvement in faithfulness would affect internal knowledge. Extensive experiments show that LLMs  can be unfaithful to the context to some extent and in the Multi-choice QA, we observe an obvious negative correlation between faithfulness and internal knowledge correctness across different LLMs. Then based on the analysis of faithfulness enhancement methods, we find that instruction tuning using counterfactual data can significantly improve the model's context faithfulness, but compromise the model's internal knowledge. To address such a issue, we propose a straightforward yet effective approach BALCONI training  by training with mixup data of factual requests, context requests, and NoAns (I cannot tell the answer from the context) requests. Experiments on our benchmark and a context-based machine translation task demonstrate that BALCONI can achieve a well-balanced effect in improving the balanced faithfulness and internal knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces FaithfulBench, a benchmark designed to evaluate the faithfulness of large language models (LLMs) and assess how improvements in faithfulness might impact internal knowledge accuracy within LLMs. Extensive experiments show that 1) LLMs exhibit unfaithful to the context to some extent; 2) there is a clear negative correlation between faithfulness and internal knowledge accuracy across different LLMs in multiple-choice QA tasks; 3) instruction tuning with counterfactual data can significantly improve the model's context faithfulness but compromise the model's internal knowledge. Based on "BALCONI training", training with mix-up data of factual requests, context requests, and NoAns requests can achieve a well-balanced effect in improving balanced faithfulness and internal knowledge.

### Strengths
1. This paper presents FaithfulBench, encompassing the tasks of Openbook QA and Multi-choice QA based on the NaturalQuestions and TriviaQA datasets. Experimental results show that all models exhibit a degree of stubbornness to their internal knowledge, and there exists a significant negative correlation between faithfulness and internal knowledge correctness in multi-choice QA.
2. This paper compares different previous methods in improving faithfulness and finds that t tuning the model on counterfactual data can enhance model faithfulness to the relevant context but hinder the model’s correctness in internal knowledge.
3. This paper proposes BALCONI training, tuning the model using mix-up data of factual requests, context requests, and NoAns requests, whose effectiveness has been proven in experiments.

### Weaknesses
1. While the paper presents a dataset focused on faithfulness, the data is generated via LLMs, which may introduce hallucinations during the dataset generation process and affect the evaluation results. It would be better if the authors could introduce some methods to guarantee the data quality and add human evaluation on (a subset of) data.
2. The models employed in the paper are somewhat outdated. For instance, Mistral 7B, which was introduced over a year ago, has since seen newer versions. Updating the experiments with the latest, more advanced models could potentially alter the results and observations.

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies whether models can be flexible as to using the given context versus its parametric knowledge. In particular, they study whether models can handle 1) **context requests**: when the user asks the model to answer based on context, overriding any parametric knowledge, 2) **factual requests**: absent such an instruction, the model should answer based on its parametric knowledge, and 3) **NoAns requests**: when the context does not contain an answer, the model should say so.

To test this they create FaithfulBench, where context requests are created by synthetically revising passages accompanying factual questions, so that they support new, counterfactual answers. They find that no model is strong in all three categories. In general, models with more internal knowledge are less faithful to the contextual knowledge. Only instruction-tuning on data from one of the three categories will improve performance in that category, but at the detriment of others. Thus the authors propose BALCONI training, which basically means tuning the model on all three types of requests at once. They show that this achieves strong performance on both FaithfulBench and a new benchmark they design for context-based machine translation.

### Strengths
This paper formalizes three scenarios that models should excel at, in order to flexibly adapt to contextual vs. parametric knowledge. They show some of the tradeoffs that come with tuning the model with only one scenario in mind.

### Weaknesses
 - There is a missing baseline: instead of tuning a model on each of the three request types (i.e., SFT-F, SFT-NoAns, and SFT-C baselines), which trades off with performance on the other request types, what if you give *in-context* examples corresponding to the desired request type? For instance, if the user wants the model to use context instead of parametric knowledge, then simply provide some in-context examples from the "context requests" category. This will likely teach the model in-context to rely solely on contextual knowledge, without compromising its ability to use parametric knowledge on other requests.
- The findings of the paper are generally unsurprising. Analysis of when models rely on contextual vs. parametric knowledge is well-studied, and BALCONI essentially boils down to training on all of the request types that the model will be evaluated on. Here is some related work about knowledge conflicts that aren't cited — 

Rich Knowledge Sources Bring Complex Knowledge Conflicts: Recalibrating Models to Reflect Conflicting Evidence (https://arxiv.org/abs/2210.13701)
Knowledge Conflicts for LLMs: A Survey (https://arxiv.org/abs/2403.08319)
Resolving Knowledge Conflicts in Large Language Models (https://arxiv.org/abs/2310.00935)
Understanding the Interplay between Parametric and Contextual Knowledge for Large Language Models (https://arxiv.org/abs/2410.08414)

### Questions
- For TriviaQA, it looks like special care was taken to ensure the counterfactual passage makes sense and doesn't contain internal conflicts. Was this also done for Natural Questions?
- L. 196: the text states that three options are given to the human annotator, but I only see two listed (the factual one and the counterfactual one). What is the third option?
- What hyperparameter do you use for the context-aware decoding baseline?

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
3

### Summary
This paper introduces FaithfulBench, a benchmark to assess how well LLMs balance reliance on contextual information versus their internal knowledge. The authors propose the BALCONI training method by fine-tuning with mixup data of factual requests, context requests, and NoAns (I cannot tell the answer from the context) requests, to enhance models' ability to use context appropriately without compromising internal knowledge accuracy. Experiments show BALCONI improves performance on FaithfulBench and context-based machine translation, demonstrating a better balance between context faithfulness and internal knowledge.

### Strengths
- The motivation of the paper is reasonable, and the evaluation is comprehensive, taking three types into account simultaneously.
- The paper is easy-to-follow and well-organized.

### Weaknesses
 - In 3.1 you mentioned "replacing the answer in the context with a counterfactual answer to create a counterfactual context". However, according to [1], it seems that the context generated by directly replacing the answer is difficult for LLM to be convincing.
- How much does the order of the options in a multiple-choice question affect the LLM's decision? I think it is necessary to shuffle the options for evaluation.

### Questions
- Since FaithfulBench covers three different types of requests evaluation, it’s intuitive and seemingly feasible to fine-tune by mixing different types of training data. Have you analyzed the impact of different mixing ratios, identifying which type of improvement is most resistant to change and which type is more easily modified through training?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In addressing tasks similar to RAG, this work discusses the trade-off between leveraging internal knowledge and contextual information in models. The paper initially introduces "FaithfulBench" to evaluate the factuality of LLMs when faced with such common scenarios. Subsequent analysis confirms the existence of this tension in specific contexts, revealing that instruction fine-tuning does not achieve a balance between internal knowledge and the context. Based on these findings, the authors propose the BALCONI algorithm, which mixes various types of requests to balance the use of internal knowledge and contextual information.

### Strengths
1. This work presents the tradeoff between the utilization of internal knowledge and context information.
2. This work proposes a benchmark for the evaluation of model behavior of this tradeoff.
3. This work proposes to mix different kinds of prompts for balancing this trade-off.

### Weaknesses
1. There are some suspicions about the core statements in this work, detailed in Question 3~5.
2. The baseline used in this work seems too weak to me. As mentioned in Question 5, I suspect there is potential overfitting due to the limited data size and large training epoch.
3. The central idea of the proposed approach (mixing different demonstrations of different model behaviors to adjust model behavior in terms of faithfulness) has been somewhat familiar to the community (like http://arxiv.org/abs/2312.07000, http://arxiv.org/abs/2311.09677). Even though this works focus on the model behavior under the scenario of RAG, I believe some important analysis can be further supplemented, as mentioned in Question 7.

### Questions
1. Line 256, can the author further explain why to use "factual request in the training set"? Why is this a necessary operation for "measuring the knowledge change"?
2. How the responses are determined to be "not answering" in NoAns requests of OpenbookQA?
3. Line 298~300, it's to an extent a reasonable result that GPT-4-turbo performs better in Factual requests than Context requests. If GPT-4-turbo is not a single parametric model and has its own context when you send the request to their API, this result may stem. However, as for the NoAns request, we observe different trends for GPT-4-turbo in OpenbookQA and Multi-choice QA. GPT-4-turbo performs much better in the latter case than in the first case. In line 306, the author states this may be the result of the hint of option in Multi-choice QA. So, what if we add a hint to the OpenbookQA requests, may the results change?
4. I somehow suspect the strong statement in Lines 317~319 concluded from the limited observations in Table 1. For the potential reason mentioned in Question 3, the close-source model requested from API may have their own context or prompt processing techniques which may not be suitable for analysis. So, when only considering the three open-source models, I don't think there is a clear conflict between Context/Factual/NoAns requests. In contrast, I find Mistral-7B-Inst-v0.1 generally performs better. Can the author provide a comparison across open-source models of different sizes in the same family, like Qwen or Llama3 for a more controlled analysis?
5. Is the x-axis coordinate of Figure 5 the epoch number? In line 405, the author infers the tension between performance on different prompts from Figure 5. However, in the first two epoch (if the the number in x-axis stands for epoch), I observed all metrics improved in the first two epochs. While there could be the possibility that there is a Pareto frontier between different kinds of prompts, it seems to me that there is actually some kind of overfitting to the request distribution in this experiment setting. Can the author provide further analysis of this trade-off?
6. What's the meaning of the y-axis in Figure 3?
7. How exactly the different requests are mixed (like the ratio of different requests) in BALCONI? What's more, I believe it can be meaningful to investigate how the ratio influences the model behavior and performance (with SFT-F/C/NoAns as an extreme case).

### Soundness
3

### Presentation
2

### Contribution
3
