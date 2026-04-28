# Retrieval Augmented Thought Process for Private Data Handling in Healthcare

- Decision: Reject
- Avg Score: 4.20
- Scores: 6, 3, 3, 3, 6

## Abstract
Large Language Models (LLMs) have demonstrated the strong potential to assist both clinicians and the general public with their extensive medical knowledge. However, their application in healthcare is constrained due to concerns about the privacy of data used in training, which prevents the integration of private and personal information because of security and ethical issues. Moreover, if their capabilities can be enhanced with information retrieval to access up-to-date knowledge, the current integration of LLMs with Information retrieval lacks robustness to imperfect retrieval, which can hinder their effectiveness and even reduce overall performance. In this work, we address this challenge by introducing the Retrieval-Augmented Thought Process (RATP). Given access to external knowledge, RATP formulates the thought generation of LLMs as a multiple-step decision process. To optimise such a thought process, RATP leverages Monte-Carlo Tree Search and learns a proxy reward function that permits cost-efficient inference. On a private dataset of electronic medical records, deliberately excluded from any LLM training set, RATP achieves 35% additional accuracy compared to in-context retrieval-augmented generation for the question-answering task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Large Language Models (LLMs) two major challenges in healthcare such as:
1. Privacy concerns with sensitive medical data
2. Difficulty in reliably accessing and using external knowledge

RATP addresses these by formulating thought generation as a markov decision process where states are reasoning graphs and actions are combinations of thoughts with retrieved documents. The privacy challenge is addressed by keeping sensitive data separate from LLM training, using only frozen inference with retrieved chunks. For retrieval integration, RATP treats documents as potential thoughts in the state space, allowing MCTS to optimize the document selection and reasoning paths, unlike standard RAG which uses fixed retrieval.

The paper shows strong results on benchmarks against their baselines.

### Strengths
The paper is well written, it improves upon ToT by unifying document retrieval and thought generation in a single MDP framework, allowing for dynamic graph expansion rather than fixed-tree exploration. The method requires no LLM fine-tuning, preserving privacy and allows easy deployment. The method scales across different LLMs. The papers shows strong improvements against baselines experiments.

### Weaknesses
My main concerns with the paper is that it doesn’t compare against strong methods that have been established in the literature such as ReACT [1] or DSP [2] with the only one being ToT. Compared to ToT, how does it compare on LLM calls, total input + output tokens, and time?  The evaluation of retrieval quality is incomplete - there's no analysis of whether MCTS truly finds optimal documents or just compensates for poor retrieval through more reasoning. Does the RAG baseline incorporate Chain of Thought?

### Questions
1. How does the method compare to ToT in terms of computational costs such as  LLM calls, total input + output tokens, and total time to answer a question?
2. How does the method compare to methods such as ReACT or DSP?
3. The RAG baseline implementation lacks clarity - was chain-of-thought prompting used? How much of RATP's improvement comes from better reasoning versus better retrieval?
4. How does RATP's document selection compare to retrieval metrics (precision@k, recall@k)? Is MCTS actually finding better documents or just processing more of them?

### Soundness
2

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
The authors addressed privacy data leakage in language model training and inference. They proposed a novel retrieval-augmented thought process that formulates multi-step thought generation as a Markov Decision Process, effectively solving it using Monte Carlo Tree Search. They evaluated the proposed method and baselines on two biomedical and two open-domain QA tasks, demonstrating the effectiveness of their approach.

### Strengths
+ The authors propose a novel approach that integrates RAG and MCTS into a single framework.

### Weaknesses
 + The experimental results are not sufficient to demonstrate the effectiveness of the proposed method. 
For instance, S. Soni and K. Roberts [1] showed that they achieved an EM accuracy of 70.56 on emrQA using the training dataset and ClinicalBERT. 
Since one of the proposed reward models requires the training data, the authors should include additional baselines that utilize the training data of each dataset.
Furthermore, X. Zhang et al. [2] proposed a pipeline that improves SLM performance by incorporating medical contexts from LLMs in privacy-restricted scenarios. 
Including such baselines would strengthen the authors' contribution.

+ The authors do not conduct any privacy analysis. 
Although they used a frozen LLM, the reward model was trained on a privacy-sensitive dataset, which methods like the model inversion attack [3] could extract training data. 
The authors should include a privacy analysis of the generated output, as done in [2].

+ The strength of the proposed method is unclear. 
Based on the results in Table 9, this approach does not appear to generalize well to open-domain QA datasets. 
Additionally, it is not specifically designed for the biomedical domain. 
For example, the authors could more carefully design the self-critic prompt to incorporate essential domain knowledge for each biomedical task. 
Another concern is the computational efficiency of the proposed method. 
While MCTS is effective for complex reasoning tasks, it is known to be computationally costly. 
I suggest that the authors include an efficiency analysis to compare the performance gains against the computational cost.

### Questions
+ Is $p_{doc}$ a predefined constant? If so, this should be clarified in line 205. Additionally, the pseudocode in the Appendix should be moved to the main article to improve understanding of the expansion phase.

+ Is there a reason why some of the methods listed in Table 2 are not included as baselines?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents the Retrieval-Augmented Thought Process (RATP), an approach designed to enhance large language models (LLMs) in healthcare by allowing them to interact with external knowledge sources while maintaining data privacy. RATP leverages Monte-Carlo Tree Search (MCTS) to support LLM decision-making in a multi-step reasoning framework, specifically addressing privacy concerns with private datasets excluded from LLM training. The approach yields substantial accuracy improvements over baseline retrieval-augmented generation (RAG) methods, notably achieving a 35% gain in accuracy on question-answering tasks over EMR datasets.

### Strengths
1. **Novelty**: The authors introduce RATP, which combines retrieval with a thought process through MCTS, enhancing LLM reasoning and robustness to imperfect retrievals.
2. **Focusing on Healthcare problem**: The RATP addresses privacy concerns which is highly relevant in the healthcare domain. By avoiding the use of sensitive data in training, the approach enhances the applicability of LLMs in handling sensitive healthcare information safely and efficiently.
3. Empirical Results: RATP demonstrates significant improvements in accuracy (35%) over standard retrieval-augmented generation methods on private datasets, underscoring its utility in healthcare QA task

### Weaknesses
1. **Privacy Concerns Still Existing**: While the training-free method mitigates some privacy risks by excluding sensitive data from training, it limits applicability to proprietary or on-premise LLM setups. Additionally, it raises questions about whether training-free alone is sufficient to address all privacy concerns, as data handling during inference still poses potential risks. The paper does not sufficiently address potential vulnerabilities during the retrieval and inference stages, such as data breaches or unauthorized access to the retrieved EMR chunks. The reliance on a standard information retrieval model like Contriever, without additional privacy safeguards, could expose patient data during the retrieval process.
2. **Appropriateness of Experimental Setup**: The experimental setup for emrQA raises questions about the feasibility of accurately retrieving the "**oracle**" EMR. Since emrQA queries are designed to be answered directly from specific patient records, it is unclear how the system reliably identifies and retrieves the relevant EMR document (oracle) to support accurate answers. This critical detail is not fully explained in the paper, complicating understanding of the retrieval process and the model's effectiveness in real-world scenarios. The description of dividing EMRs into 100-word chunks and using Contriever for retrieval lacks sufficient detail on how the system ensures that the most relevant chunk is retrieved, especially given the variability in EMR length and content. The paper does not address how the system handles cases where the answer spans multiple chunks or when the retrieved chunk does not contain the complete answer.
3. **High Inference Cost**: The RATP framework involves a multi-step thought generation process using Monte-Carlo Tree Search, which increases inference time and computational cost. Given the linear increase in LLM queries with the number of thought steps, extensive thought processes can become financially and temporally demanding, particularly in real-time applications. The paper lacks a detailed analysis of the computational resources required for RATP, including memory usage and processing time, which are critical for practical deployment. The absence of a comparison of inference costs with baseline methods makes it difficult to assess the practical viability of the approach.

### Questions
1. There appears to be an inconsistency in Figure 3 regarding document selection. In the "Expansion" step, there is no arrow indicating that \( I_4 \) is selected, yet it is included in the prompt for generating \( \phi_{10} \). This raises questions about how \( I_4 \) was chosen for the prompt without a connecting arrow in the illustration. Clarification on this selection process and whether \( I_4 \) should indeed be part of the prompt would improve the figure’s accuracy and help clarify the decision-making flow in the MCTS process.
2. As mentioned in the weaknesses, it would be beneficial to include a comparison of inference costs. Given the high computational demands of the multi-step thought process, a detailed analysis of inference costs compared to other methods would provide valuable insights into the efficiency of the RATP approach.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework, Retrieval-Augmented Thought Process (RATP), designed to integrate external information retrieval with LLMs to safely and effectively use private medical data. It addresses challenges in privacy, reasoning, and robustness when LLMs access sensitive information for healthcare applications.

### Strengths
This paper take the privacy question in healthcare into consideration, which is very critical in the healthcare domain,  and propose corresponding  methods to enhances the interaction between LLMs and private data.

The experimental results comparing to proposed baselines looks promising in the EHR QA datasets.

### Weaknesses
1. Incremental Contribution:
While the paper addresses several critical issues in the healthcare domain—such as privacy, hallucination, and reasoning—it relies heavily on existing approaches, including RAG, multi-step thinking paths, and scoring systems, without introducing fundamentally new ideas. The core mechanism of using MCTS for planning, while effective, is not a novel contribution in itself, and its application to this specific problem appears to be a straightforward adaptation of existing techniques.

2. Ambiguity in Baseline Models:
The authors mention using "LLM" as a baseline but fail to specify which LLM or group of LLMs they experimented with. This lack of clarity makes it difficult for readers to accurately assess the reproducibility and comparability of their results. The absence of specific model details, such as the model size, architecture, and training data, makes it challenging to understand the performance characteristics of the baseline.

3. Lack of Comparison with Simpler Methods:
The paper does not compare the proposed method with simpler and widely adopted reasoning frameworks, such as Chain of Thought (CoT) with or without self-consistency. Including such comparisons would have provided better insights into the benefits of using the proposed Monte Carlo Tree Search (MCTS) framework. Without a direct comparison to CoT, it's unclear if the added complexity of MCTS provides a significant advantage over simpler, more established methods.

3. High Computational Cost:
Although the use of MCTS improves the reasoning capacity of the LLM, the computational cost is likely much higher than that of simpler baselines. A detailed comparison of computational overhead, including the number of LLM queries and time or resource consumption, would strengthen the evaluation and help justify the trade-off between performance and efficiency. The paper lacks a quantitative analysis of the computational resources required by MCTS compared to simpler methods, making it difficult to assess its practical applicability.

4. Insufficient Coverage of Related Work:
The related work section lacks coverage of recent advancements in Medical LLMs and privacy in healthcare. Here are some works are notably missing:

Medical LLMs: 
Li et al. (2023): ChatDoctor: A Medical Chat Model Fine-Tuned on a Large Language Model (LLaMA) Using Medical Domain Knowledge
Zhang et al. (2023): AlpaCare: Instruction-Tuned Large Language Models for Medical Applications
Kim et al. (2024): Health-LLM: Large Language Models for Health Prediction via Wearable Sensors

Health-domian privacy:  
Zhang et al. (2022): Enhancing Small Medical Learners with Privacy-Preserving Contextual Prompting

Including these references would provide a more comprehensive understanding of related work in the healthcare domain, particularly concerning privacy and medical LLMs.

### Questions
1. Could you clarity what LLM indicates in the paper.

2. Could you compare with simple baselines such as COT with or without self-consistency.

3. Could you should the effectiveness of your model across basemodel family and size?

4. Could you show the computational cost comparison comparing to baselines?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describe a novel method to to expand LLM knowledge using recursive thought process that includes retrieving relevant documents. This method is extremely useful in the scenarios where private data is needed to answer a question.

### Strengths
According to the authors the method greatly increases the performance over the tested dataset.

### Weaknesses
 - I think the paper is written in too abstract and over formulated manner, a concrete step-by-step walkthrough example of the process would be very useful to better understand  the process. 

- What is the reason that RAG underperforms LLM in some cases, it is especially peculiar when we know the answers requires private data. Is the retrieval wrong? Does the model has issue utilizing the retrieved data? An analsys of the reason for failure would be useful and can contribute to the understanding of why your method is successful

- Figure 4 seems to be missing the MCTS oracle #LLM queries line, generally this figure is hard to read to the fact it has two y values, splitting the figure and adding the missing line would be useful

- For easier understanding of the method cost I think total tokens used would be easier to understand. Can total tokens per method be added to the analsys?

### Questions
None

### Soundness
3

### Presentation
2

### Contribution
2
