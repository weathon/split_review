# Towards Federated RLHF with Aggregated Client Preference for LLMs

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Reinforcement learning with human feedback (RLHF) fine-tunes a pretrained large language model (LLM) using user preference data, enabling it to generate content aligned with human preferences. However, due to privacy concerns, users may be reluctant to share sensitive preference data. To address this, we propose utilizing Federated Learning (FL) techniques, allowing large-scale preference collection from diverse real-world users without requiring them to transmit data to a central server. Our federated RLHF methods (i.e., FedBis and FedBiscuit) encode each client’s preferences into binary selectors and aggregate them to capture common preferences. In particular, FedBiscuit overcomes key challenges, such as preference heterogeneity and reward hacking, through innovative solutions like grouping clients with similar preferences to reduce heterogeneity and using multiple binary selectors to enhance LLM output quality. To evaluate the performance of the proposed methods, we establish the first federated RLHF benchmark with a heterogeneous human preference dataset. Experimental results show that by integrating the LLM with aggregated client preferences, FedBis and FedBiscuit significantly enhance the professionalism and readability of the generated content.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Reinforcement learning with human feedback (RLHF) is a good way to fine-tune a pretrained large language model (LLM) to generate content aligned with human preferences. This paper proposes to use federated learning technique to aggregate different model information from users to enhance RLHF ability of LLM. Concretely, the proposed federated RLHF methods encode each client’s preferences into binary selectors and aggregate them to capture common preferences. This method overcomes key challenges like preference heterogeneity and reward hacking to enhance LLM output quality. Experiments on two LLM benchmarks demonstrate the effectiveness of the proposed federated RLHF algorithm.

### Strengths
(1)	This paper provides a novel federated learning-based reinforcement learning method to enhance the output ability of LLM. To the best of my knowledge, this is the first time to employ federated learning technique to enable diverse user collection for RLHF.

(2)	The organization of this paper is clear and easy to follow. In particular, Figure 2 clearly depicts the outline of the proposed FedBis model.

(3)	The algorithm design in Section 5.1 is practical and new to me. Besides, the key component of the algorithm (i.e. training a binary selector and aggregating different selectors to the LLM server) effectively incorporates federated learning idea into the design of RLHF model.

(4)	The experimental results on summarization and question-answering dataset validate the advantages of the proposed algorithm over existing methods.

### Weaknesses
(1)	The experimental results in Section 7 are not extensive enough. This paper conducts experiments on two NLP tasks, summarization and question-answering, and more experiments on other tasks should be complemented, like few-shot learning, synthetic, code completion, multi-needle retrieval. The choice of datasets is also limited, and it is unclear if the proposed method can generalize to other types of datasets with different characteristics, such as those with more complex structures or longer sequences.

(2)	I admire the proposed FL-based reinforcement learning method, but it will be more readable and more concise to summarize the contents in Section 5.1 Algorithm Design into a pseudocode (i.e. shown in an Algorithm). The current description is somewhat verbose and difficult to follow, making it hard to grasp the core steps of the algorithm.

(3)	Lines 70-77 in Introduction is about the limitation of preference heterogeneity and reward hacking, and such limitation appears (in detail) once again in lines 224-237 of methodology. It suffices to mention such limitation once in one paper, or at least, not to emphasize it twice (e.g. not use bold to highlight it).

(4)	Section 6 is about the details of the experimental datasets, and will be better to defer it to Section 7 Experiments.

(5)	It will be better to use \begin{small} or other writing skill, to make Eq.(2) and Eq.(4) shown in one line.

(6)	Lines 237,294, 471, isolated word

(7)	Line 268, fix ". $\phi _{u}$"

### Questions
It may not be easy to add more experimental results in the rebuttal period. But can the proposed method also enhance RLHF ability of LLM in other NLP tasks like few-shot learning, synthetic, code completion, multi-needle retrieval?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper deals with privacy preservation through applying federated learning to employing user preferneces to fine-tune a common LLM. The synergy of reinforcement learning, large language model, and federated learning appears apealing to me. The paper presents nicely with an intuitive comparison between standard and fedrated RLHF, making the problem easy to follow.

### Strengths
- The paper deals with an important research problem.
- The paper is generally well orgnaised and presente, and easy to follow.
- The authors proposed a sound solution to the research problem, showing advantages over baselines.

### Weaknesses
 - The challenged identifiied on Page 2 seems univeral and apply to many federated learning scenarios, not specified to this paper's research context. Therefore, although the overall problem setting seems to be new, the key research problem to tackle remains conventional.
- To deal with excessive comptuation overhad and preference heterogeneity seem to be a common issue that has been addressed by various previous efforts. The clustering approach to addressing the key issue does not appear novel to me.
- The cons of appplying the federated learning approach might be discussed for readers to better understand the trade-off.

### Questions
What are the unique challenges posed by employing federated learning to RLHF?
How RLHF impact the challenges and solution design presented in the paper?
What is the motivation behind the binary selector? what are the alternatives and why binary selectior, in particular, is chosen to be part of the solution?

### Soundness
3

### Presentation
4

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
This paper leverages federated learning into reinforcement learning with human feedback (RLHF) and proposes two federated-based RLHP methdos (FedBis and FedBiscui) to fine-tune large language models using user preference while preserving data privacy. The methods employ binary selectors to aggregate client preferences without requiring direct data sharing. FedBiscuit extends the functionality of FedBis by addressing preference heterogeneity and mitigating reward hacking. Experiments demonstrate that FedBis and FedBiscui perform better on Summarization task and QA task.

### Strengths
1、Generally, this paper is well-written with clear explanations of the methodologies and results. 

2、The proposed FedBis and FedBiscui demonstrate good performance on several benchmarks, suggesting good-quality research and implementation.

3、This paper addresses the heterogeneity issue, an important issue in all fields of federated learning related research.

### Weaknesses
1、It would be better to include experiments that explore the sensitivity of the hyperparameters, particularly the number of clusters $U$, which is a crucial or even central parameter in the FedBiscuit method. However, the current results only present cases for $U=3$ and $U=5$, providing limited insights from these two configurations. Specifically, the paper lacks a systematic analysis of how different values of $U$ impact the performance and convergence of the model. It is unclear whether the chosen values are optimal or if there is a principled way to select $U$ for different datasets or tasks. A more thorough investigation, including a wider range of $U$ values and a discussion of the trade-offs involved, is needed.

2、The authors should further explain why FedBiscuit with $U=3$ performs better in some cases while $U=5$ yields superior results in others. Since FedBiscuit addresses the heterogeneity issue, and as noted in existing federated learning literature, particularly in cluster-based federated learning approaches, the number of clusters is a key factor. Understanding the impact of different cluster sizes on the method’s effectiveness would be valuable. The paper does not provide sufficient insight into the conditions under which each configuration is preferable. A more detailed analysis of how the number of clusters interacts with the data distribution and the specific characteristics of the tasks is necessary to make informed decisions about the choice of $U$.

3、The additional complexity introduced by clustering and the use of multiple selectors in FedBiscuit may still pose scalability challenges, particularly in real-world applications with thousands of clients. It would be helpful to provide more analysis on the scalability of the approach, especially under varying numbers of clients and communication costs. This would shed light on the method’s feasibility for large-scale deployment. The paper lacks a detailed discussion of the computational overhead associated with the clustering and selector aggregation processes, and how these costs scale with the number of clients and the size of the model. A more thorough analysis, including empirical evaluations of the method's performance under different communication constraints, is needed to assess its practicality for large-scale federated learning scenarios.

### Questions
Please see weaknesses.

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
2

### Summary
This paper proposes a federated RLHF method specially designed for large-scale preference collection, which encodes each client’s preferences into binary selectors and aggregates them to capture common preferences. An enhanced method is also introduced, which overcomes the challenges of preference heterogeneity and reward hacking by grouping similar clients and leveraging multiple binary selectors to improve LLM output quality. The authors also established a novel federated RLHF benchmark for evaluation. Experimental results show the superiority of the proposed model.

### Strengths
-The workload is impressive, every part is introduced in detail.

-The idea of training binary selectors to encode client’s preferences is novel.

-The two proposed methods are reasonable and both have many details in addressing the issues faced by traditional method.

### Weaknesses
-Computation overhead. This method involves additional training of binary selectors, which are pre-trained LLMs. Although the authors apply LoRA to reduce the computation cost, the time and computation overhead of fine-tuning LLM selectors are still not negligible, which limits its application scenario. The overhead is particularly concerning given that each client needs to train these selectors, potentially requiring significant resources even with LoRA. The paper does not provide a clear breakdown of the computational costs associated with training these selectors on different hardware configurations, making it difficult to assess the practical feasibility of the approach.

-The experiments need supplements: In the section of performance analysis on different binary selectors, the experiments applied three base model with both different model structure and parameter size. To make the results more convincing, the effect of model type and model size should be explored separately. The current experimental setup conflates the effects of model architecture and parameter count, making it hard to isolate the impact of each factor on the performance of the binary selectors. A more controlled experiment would vary only one of these factors at a time.

### Questions
-Is there any data available on the training time or memory footprint of the entire training process?

-Given that LoRA configuration also has an impact on performance, can the authors provide the detailed information about the LoRA configuration used in their experiments?

### Soundness
3

### Presentation
3

### Contribution
3
