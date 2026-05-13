# No Free Lunch: Retrieval-Augmented Generation Undermines Fairness in LLMs, Even for Vigilant Users

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the fairness implications of Retrieval-Augmented Generation (RAG) in LLMs. While RAG effectively reduces hallucinations and improves performance, the study shows it can compromise fairness even with bias-censored datasets. Through analyzing three levels of user awareness (uncensored, partially censored, and fully censored datasets), researchers found that RAG-based models generate biased outputs without changing parameters of LLMs. The findings highlight limitations in current fairness alignment strategies and call for new safeguards.

### Strengths
1. Important topic: This study examined a critical concern about how RAG approaches can affect LLM alignment, particularly regarding fairness implications.
2. Comprehensive Analysis: The study provided a well-structured evaluation across different scenarios, considering various levels of user awareness and types of dataset censorship.

### Weaknesses
1. Limited contribution: While the paper thoroughly analyzes how RAG can compromise LLM fairness, it offers minimal practical solutions, only briefly suggesting mitigation strategies in its conclusion.
2. Ambiguous scope: The paper examined RAG's impact on LLM fairness, distinguishing between supposedly 'prominent' biases (race-ethnicity, sexual orientation) and 'less conspicuous' ones (religion, age). However, this classification lacks systematic supporting evidence. The paper arbitrarily categorizes 11 types of bias without justifying why certain biases are considered more prominent than others. For instance, the classification of religious bias as less conspicuous than racial or sexual orientation bias remains unsupported. This arbitrary categorization undermines the study's comprehensiveness.
3. Unconvincing Analysis: In Section 4.3, the paper identified that RAG data with biases in one category can trigger biases in another category. While this finding is significant, it lacks in-depth analysis of potential underlying mechanisms. Specifically, the paper does not explore the specific types of cross-category bias propagation or the conditions under which they occur. In Section 4.4, The paper argued that RAG with censored datasets compromises LLM alignment by promoting positive responses where the LLM previously refused biased queries. However, this argument has two key weaknesses: It oversimplifies appropriate LLM responses to biased content, assuming rejection is the only valid response rather than acknowledging possibilities for nuanced explanatory responses that address bias without outright refusal. Secondly, the analysis relies on intuitive speculation rather than detailed experimental evidence demonstrating the specific mechanisms by which censored data leads to this shift in LLM behavior.

### Questions
In Section 4.1's Question-Answering Task evaluation (line 268), the authors' assumption that 'refusals equal unbiased outcomes' is oversimplified. LLMs can respond to biased questions with nuanced explanatory answers rather than simple refusals as "i do not know", making this binary classification inadequate for measuring bias.

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
The authors explore the relationship between RAG and generation fairness under three conditions: (a) uncensored corpora, (b) partially censored corpora, and (c) fully censored corpora.  They test their hypotheses under several tasks, fairness metrics, and models.  The results demonstrate that, under all conditions, RAG can degrade fairness compared to non-RAG models.  

**Given that both RAG and Data-Centric AI are current methods for addressing multiple concerns with LLMs, this is an important area of study.**

### Strengths
* **Clear hypotheses.** The authors very clearly specify their hypotheses across reasonable experimental conditions.  This allows for the construction of appropriate experiments and testing. 
* **Metrics are well-motivated and operationalized.** The authors use established and clear metrics for unfairness, covering a variety of different operationalizations, depending on the task. 
* **Well-motivated.** The research is salient given the current movement toward RAG using (safe) LLMs that may be degraded through corpora. 
* **Good experiments.** The experiments are solid and thorough.  All of these results are clearly analyzed and put into context.

### Weaknesses
 * **Statistical testing.** The hypotheses and experiments are very clear and amenable to proper hypothesis testing.  This would make it easier to understand the robustness of these results. Please consult texts on significance testing ("Empirical Methods for Artificial Intelligence"), including corrections for multiple comparisons.  It is unclear what statistical tests should be used given the nature of the data and experimental design.  For example, the frequency-based metrics may require non-parametric tests, while the toxicity scores may require other tests.  It is important to clarify the nature of the data, and the statistical tests used to analyze it. 
* **Implications.** The observations in the experiments are interesting and deserve some treatment of next steps.  There's a short sentence in the conclusion alluding to the need for future work on fairness but it would be good to explore this more.  The current discussion is too high-level and does not delve into the specific mechanisms by which RAG might degrade fairness or how these mechanisms might be mitigated.  
* **Related work.** There is related work on the difficulty of data-driven approaches to fairness that is worth drawing connections to.   There are several here,
   * Esther Rolf, Theodora T Worledge, Benjamin Recht, and Michael Jordan. Representation matters: assessing the importance of subgroup allocations in training data. In Marina Meila and Tong Zhang, editors, Proceedings of the 38th international conference on machine learning, volume 139 of Proceedings of Machine Learning Research, 9040--9051, PMLR, 18--24 Jul 2021.
   * Meera A. Desai, Irene V. Pasquetto, Abigail Z. Jacobs, and Dallas Card. An archival perspective on pretraining data. Patterns, 5(4):100966, 2024.
   * Fernando Diaz and Michael Madaio. Scaling laws do not scale. In Proceedings of the 2024 aaai/acm conference on ai, ethics, and society, 2024.
   * Nithya Sambasivan, Erin Arnesen, Ben Hutchinson, Tulsee Doshi, and Vinodkumar Prabhakaran. Re-imagining algorithmic fairness in india and beyond. In Proceedings of the 2021 acm conference on fairness, accountability, and transparency, FAccT '21, 315--328, New York, NY, USA, 2021. , Association for Computing Machinery.

### Questions
* Were statisical significance tests conducted to test the hypotheses?  And, if so, do they correct for multiple comparisons?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an empirical study about user awareness of fairness regarding RAGs, showing that retrieval can introduce biases even with unbiased datasets. The study uses a three-level threat model based on user awareness of fairness, examining uncensored, partially censored, and fully censored datasets. Experiments reveal that RAG can degrade fairness without fine-tuning, underscoring limitations in current alignment methods and the need for new fairness safeguards.

### Strengths
- The paper proposes a novel insight into RAG fairness and highlights the potential for RAG to introduce biases (even in supposedly unbiased systems).

- The threat model is well-structured.

- The experimental setup is clear and robust. The paper adopts various benchmarks to assess the fairness of RAG comprehensively.

### Weaknesses
 - The paper does not provide detailed qualitative samples to support the argument, which is especially important for the generation task. The Perspective API can assign low toxicity scores to repeated meaningless sentences or high scores to correct answers containing specific toxic words. 

- The evaluation focuses on the fairness side but neglects the retrieval efficacy. The paper suggests a trade-off between retrieval/accuracy and fairness, but it has not been studied in the experiments.

- The paper tends to focus more on high-level implications rather than providing an in-depth analysis of the underlying mechanisms of why and where RAG introduces biases.

- The definitions of "uncensored," "partially censored," and "fully censored" datasets are somewhat vague. How were the datasets selected and processed for each level of censorship, and how do you ensure consistency across these levels?

### Questions
- Can you provide more detailed examples or case studies of the biases that were introduced by RAG, particularly in the context of fully censored datasets?

- How were the datasets selected and processed for each level of censorship, and how do you ensure consistency across these levels?

- How do you propose integrating the suggested mitigation strategies into existing LLMs without affecting their performance in other areas?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The author conducted an experimental analysis on the fairness risks introduced in LLMs when human users with three different levels of fairness awareness and use RAG with uncensored data, partially censored data, and fully censored data.

### Strengths
RAG significantly impacts the performance of LLMs. The paper’s motivation on the potential bias of RAG is encouraging

The authors have thoughtfully considered varying levels of fairness awareness among human users, which is presented clearly.

The experiments are conducted across a range of tasks, including classification, question answering, and generation tasks, which is a positive aspect of the study.

### Weaknesses
1.  The works [1][2][3]  share similar objectives and are worth to be discussed.

[1] Wu, X., Li, S., Wu, H. T., Tao, Z., & Fang, Y. (2024). Does RAG Introduce Unfairness in LLMs? Evaluating Fairness in Retrieval-Augmented Generation Systems. arXiv preprint arXiv:2409.19804.

[2] Dai, S., Xu, C., Xu, S., Pang, L., Dong, Z., & Xu, J. (2024, August). Bias and unfairness in information retrieval systems: New challenges in the llm era. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp. 6437-6447).

[3] Dai, S., Xu, C., Xu, S., Pang, L., Dong, Z., & Xu, J. (2024). Unifying Bias and Unfairness in Information Retrieval: A Survey of Challenges and Opportunities with Large Language Models. arXiv preprint arXiv:2404.11457.

2. The experimental description is not convincing enough in demonstrating that "RAG leads to unfairness in LLMs," as it lacks the necessary results, i.e., the introduction of RAG in Fig. 3 not only leads to a decrease in fairness, but also a decrease in accuracy, which means that the data quality is lower. Does it mean that the degradation of fairness comes from the data itself rather than RAG?  along with other experimental weakness listed in the Questions
3. In the discussion section, the authors aim to analyze existing strategies cannot mitigate the bias arising from RAG. However, they use an unfairness rate of 1.0. I believe it would be more convincing to use an unfairness rate of 0.0, as this would better support the authors' argument that “retrieval-augmented generation undermines fairness” rather than suggesting that “low-quality data undermines fairness.”
4. Lack of some analysis on how to mitigate the author's claim unfairness issue from RAG effectively

### Questions
1. The statistical disparity and other indicators in the table 1 are more accurate if they are formed by subtraction instead of equality, reflecting a value instead of true or false. In addition, there are upward arrows in the table to indicate the direction of the value. And the symbols in the table lack annotations, such as S, T, U, $f_{\theta}$, etc.
2. The second sub-table in Fig. 2 seems to be different with a non-monotonic relationship with the unfairness rate? Is there any reason? It seems wrong to claim "The results consistently indicate" in the text. In addition, Line 318-344 mentions findings from Figs. 2 and the first two sub-figures in Fig. 3, but the vertical coordinates of Figs. 2 and the first two sub-figures in Fig. 3 are not consistent.
3. The introduction of RAG in Fig. 3 not only leads to a decrease in fairness, but also a decrease in accuracy, which means that the data quality is lower. Does it mean that the degradation of fairness comes from the data itself rather than RAG?
4. Regarding that the Llama series performs better than GPT on the Holistic dataset, the article says that it "might stem from their inability to properly understand the questions". Is there any further experimental data to support this?
5. In "FULLY CENSORED DATASETS", the experimental results shown in Figure 8 cannot well reflect the bias caused by RAG. A more reasonable way is to show the proportion of biased answers under all known answers, rather than count. In addition, the proportion of correct answers also needs to be shown to show the advantages of RAG.
6. Why can the summarizer alleviate the reduction in fairness to a certain extent? The specific reasons are not analyzed
7. Will different RAG construction methods produce different results? [4] 

[4]Shrestha, R., Zou, Y., Chen, Q., Li, Z., Xie, Y., & Deng, S. (2024). FairRAG: Fair human generation via fair retrieval augmentation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 11996-12005).

### Soundness
2

### Presentation
3

### Contribution
1
