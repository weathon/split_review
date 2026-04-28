# Hallucination Detox: Sensitive Neuron Dropout (SeND) for Large Language Model Training

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
As large language models (LLMs)  are  increasingly deployed across various industries, concerns regarding their reliability, particularly due to hallucinations—outputs that are factually inaccurate or irrelevant to user input—have grown. Our research investigates the relationship between the training process and the emergence of hallucinations  to address a key gap in existing research that focuses primarily on post hoc detection and mitigation strategies. Using models from the Pythia suite (70M–12B parameters) and several hallucination detection metrics, we analyze hallucination trends throughout training and explore LLM internal dynamics. We introduce \textbf{Sensitivity Dropout ( SenD)}, a novel training protocol designed to mitigate hallucinations by reducing variance during training.  SenD  achieves this by deterministically dropping embedding indices with significant variability, referred to as Sensitive Embedding Indices. In addition, we develop an unsupervised hallucination detection metric, Efficient EigenScore (EES), which approximates the traditional EigenScore in 2x speed. This efficient metric is integrated into our protocol, allowing  SenD  to be both computationally scalable and effective at reducing hallucinations. Our empirical evaluation demonstrates that our approach improves LLM reliability at test time by up to 40\% compared to normal training while also providing an efficient method to improve factual accuracy when adapting LLMs to Wikipedia, Medical, and  LegalBench domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Sensitive Neuron Dropout (SeND), a novel training protocol aimed at reducing hallucinations in large language models (LLMs) by minimizing variance during training. Unlike existing post-hoc hallucination mitigation methods, SeND operates during training, specifically targeting neurons—referred to as Sensitive Neurons—that exhibit high variability across training epochs. By selectively dropping these neurons, SeND helps stabilize model outputs, thereby enhancing factual confidence and reducing the likelihood of confabulations, which are hallucinations where models inconsistently produce factually correct and incorrect responses.

### Strengths
1. Innovative Approach: Introduces SeND, a new training method, and EES, an efficient hallucination detection metric.
2. Robust Evaluation: Demonstrates SeND’s effectiveness across multiple models and datasets.
3. Computational Efficiency: EES is scalable, supporting application in large LLMs without adding significant computational costs.
4. Clear Methodology: The paper clearly explains the theoretical background and provides step-by-step details for SeND implementation.

### Weaknesses
1. While the paper introduces Efficient EigenScore (EES) as an approximation of the EigenScore metric for hallucination detection, it largely focuses on a single metric. Expanding the scope of metrics could provide a more comprehensive understanding of SeND’s performance. For instance, incorporating metrics like Semantic Entropy or FactScore alongside EES would allow a nuanced evaluation of hallucinations across different aspects of factuality and consistency. Specifically, the paper lacks a clear justification for why EES is sufficient to capture the multifaceted nature of hallucinations, especially given that it primarily focuses on the variance of hidden representations. A more thorough analysis should explore how EES correlates with other established hallucination metrics, providing a stronger basis for its use as a proxy for overall hallucination reduction.
2. The paper’s experimental setup lacks an ablation study on SeND’s dropout parameters, such as the percentage of neurons dropped and the interval for identifying sensitive neurons. This omission makes it difficult to assess the robustness of the chosen parameters and whether the reported results are optimal. The paper should include a detailed analysis of how different dropout rates and sensitivity thresholds affect the performance of SeND, including the trade-offs between hallucination reduction and potential loss of model capacity. Furthermore, the paper does not explore the impact of varying the frequency at which sensitive neurons are identified and dropped, which could significantly affect the training dynamics.
3. Although the paper tests SeND on the Pythia model series, this restricts its applicability to similar architectures. Testing SeND on diverse LLM architectures, such as LLaMA, would better establish its generalizability across model types with varying parameters and configurations. The paper should investigate how SeND performs on models with different architectural features, such as varying layer sizes, attention mechanisms, and activation functions. This is crucial to determine if the method is universally applicable or if it requires architecture-specific tuning.

### Questions
1. What guided the specific selection of neuron dropout parameters (e.g., dropout percentage, sensitivity threshold)? Could the authors provide insights into how the dropout parameters for SeND were chosen? Was there an empirical process for selecting these values, and did the team explore different configurations to determine the optimal settings? 
2. What impact do Sensitive Neurons have on downstream tasks, especially when a high percentage is dropped?
3. Can the authors share any qualitative examples of how SeND changes model outputs? Including specific examples of model outputs before and after training with SeND, particularly for hallucination-prone prompts, would help illustrate the model’s qualitative improvements.

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
In this paper, the authors are attempting to solve the hallucination problem called confabulations where the LLM generates different responses given the same or similar inputs. Specifically, the authors propose two main contributions including the triaining protocal named Sensitive Neuron Dropout (SeND) and the enhanced unsupervised hallucination detection metric namd Efficient EigenScore (EES).
In SeND, a novel training protocol, aimed at alleviating the phenomenon of hallucinations in large language models (LLMs) by reducing the variance during the training process. This method reduces the variance of illusions and enhances the factual certainty of the model by deterministically discarding neurons with significant variability on the dataset (known as sensitive neurons) as a regularization technique. The developed an unsupervised hallucinations detection metric EES that is twice as fast as traditional EigenScore while minimizing its impact on accuracy. This efficient metric is integrated into the SeND protocol, making SeND computationally scalable and effective in reducing illusions. In the experiments, the study demonstrated that its method improved the reliability of LLMs during testing, increasing reliability by up to 40% compared to normal training, and providing an effective approach to improve real-world accuracy when adapted to fields such as Wikipedia and medical datasets.

### Strengths
● Innovation: This study proposes a new training protocol, SeND, which may have a significant impact on the reliability and security of LLMs, making it an important research area.
● Practical application: Empirical evaluations on Wikipedia and medical datasets have demonstrated the potential of SeND in improving factual accuracy, which is particularly important for applications in high-risk industries.
● Computational efficiency: The development of EES has significantly improved the computational efficiency of hallucination detection, which is particularly important for large models and datasets.
● Paper writing: This paper has a smooth writing structure and clear logical expression, allowing readers to quickly understand the relationship between this paper and previous related works.

### Weaknesses
● Lack of discussion on other training stages. The authors assume that the existing research that focuses primarily on post hoc detection and mitigation strategies. However, the training stages in current works mainly contain three import paradigms including pre-training, continue pretraining and SFT. All of them may produce the hallucination phenomenon, and thus the discussion about other two training stages should be considered. Specifically, the paper does not address how the proposed Sensitive Neuron Dropout (SeND) method would interact with or potentially mitigate hallucinations during the initial pre-training phase, where the model learns fundamental language representations. The absence of this discussion limits the scope of the work, as pre-training is a critical stage where many biases and inconsistencies can be introduced, leading to later hallucinations.
● To evaluate the OSCILLATORY BEHAVIOUR, the authors use the two tasks including self-consistency and summarization, the other important metrics (e.g., PPL) or tasks (e.g. QA) should be considered. The evaluation of oscillatory behavior is limited by the choice of tasks. Self-consistency and summarization, while relevant, do not fully capture the nuances of hallucination across different types of language understanding. For example, question answering (QA) tasks, which require precise factual recall, could reveal different aspects of the oscillatory behavior of hallucinations. Furthermore, the inclusion of perplexity (PPL) as a metric would provide insights into the model's confidence in its predictions, which is crucial for understanding the underlying causes of hallucinations.
● Mismach parameters size between SENSITIVE NEURONS discussion and main experiments. In experiments settings, the range of paramerts' size of LLMs is from 70M to 12B. However, the theoretical analysis and experimental results of SENSIIVE NEURON are conducted using the Pythia 1B model in the main body (Sec. 3), and there is concern about the lack of generalization of the SeND to larger scales model. The analysis of sensitive neurons is primarily conducted on a 1B parameter model, while the experiments involve models ranging from 70M to 12B parameters. This discrepancy raises concerns about the generalizability of the findings. The behavior of sensitive neurons might vary significantly across different model sizes and architectures, and it is not clear whether the conclusions drawn from the 1B model will hold for larger models. This lack of consistency between the analysis and the experiments weakens the claims about the effectiveness of SeND across different scales.
● The effectiveness of SeND experiment is weak. Firstly, the authors only select two datasets (general domain and medical domain), and the effectiveness of this method needs to be proven on more authoritative hallucination benchmarks. In addition, as shown in Fig. 4, the FT method is not too weak compared to the SeND, and thus more datasets are needed to prove the effectiveness of the method. The experimental evaluation of SeND is limited by the choice of datasets. While the general and medical domains are relevant, the lack of evaluation on more established hallucination benchmarks limits the generalizability of the results. The fact that the fine-tuning (FT) method performs comparably to SeND in some cases, as shown in Figure 4, suggests that the improvements achieved by SeND might not be substantial enough to justify its complexity. More diverse and challenging datasets are needed to demonstrate the clear superiority of SeND over existing methods.

### Questions
See the Weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel training protocol called Sensitive Neuron Dropout (SeND) to address hallucinations in Large Language Models (LLMs). The work presents three main contributions: (1) empirical validation of oscillatory hallucination behavior during training, (2) development of SeND for reducing hallucination variance during training, and (3) introduction of Efficient EigenScore (EES), a computationally efficient approximation of EigenScore for hallucination detection. While the theoretical framework is interesting, the empirical validation relies heavily on proxy metrics and limited evaluation data, making it difficult to assess the real-world impact on hallucination reduction.

### Strengths
The paper proposes a novel approach tackling hallucinations during training rather than post-hoc, representing a interesting shift in addressing this critical challenge.
The foundation is solid, with clear mathematical derivations for both SeND and EES.
The development of EES shows practical value by providing a computationally efficient approximation for hallucination detection with demonstrated speedup.

### Weaknesses
The empirical evaluation is severely limited with only 100 test datapoints and lacks validation on more than one established hallucination benchmarks, like HaluEval, raising concerns about result reliability. 
The work relies heavily on EES as a proxy metric without sufficient evidence that improvements in EES correlate with actual reduction in model hallucinations.

### Questions
1. Could the authors provide results on a significantly larger test set beyond 100 datapoints?
2. What is the correlation between EES improvements and actual hallucination reduction as measured by standard benchmarks?
3. How does SeND compare to other hallucination reduction methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper empirically validates the oscillatory nature of hallucinations during the training process of LLMs, despite being discovered by previous work. Subsequently, this paper introduces Sensitive Neuron Dropout (SeND), a training-time method for hallucination reduction, and  Efficient EigenScore (EES), a more efficient hallucination detection metric.

### Strengths
1. Different from existing post-hoc detection and mitigation strategies, this paper focuses on the relationship between the training process and the emergence of hallucinations, trying to provide interpretation from a relatively new perspective.
2.  Before introducing the specific method, this paper conducts motivational experiments, consolidating the rationale of the method.

### Weaknesses
1. Despite focusing on hallucination, this paper does not test on any hallucination dataset and metrics directly, but utilizes some indicative alternatives. This reduces the credibility of the results.
2. Despite the claims of reduced hallucination, it's unclear whether this technique would hinder the performance of models. Specifically, performance should be evaluated on standard benchmarks such as GSM8K, MATH, MBPP, and HumanEval, not just training loss. The impact on reasoning tasks is particularly important to assess.
3. For LLMs, it's rare to train models for several epochs to prevent overfiting and catastrophic forgetting, while it seems that this method can only be used for multi-epoch training settings. The method's applicability to single-epoch or few-epoch training scenarios needs clarification.
4. Xsum is not suitable to evaluate hallucination of LLM, and Rouge1 score is a bit out-of-date/ineffective to evaluate the performance of LLMs. More contemporary metrics and datasets should be considered.
5. The writing for "Sec. 1.2 Related Work" is quite strange. Here, the 2nd and 4th paragraphs focus on motivation and implementation details instead of the comparison with peer methods.
6. In Sec. 2.2, I observed that generally, the metrics change positively with the increase of LLM sizes, inconsistent with the observations of authors. Could you please provide further explanation?
7. The number of models and datasets is too small (i.e., only 1) to validate the robustness of the method. The lack of diversity in model architectures and training data limits the generalizability of the findings.
8. There is a lack of baseline and performance comparison with post-hoc solutions. A comparison with existing methods like RAG is necessary to contextualize the contribution.

### Questions
1. For line 227, the meaning of H needs to be further explained.
2. For line 229, a citation is needed to support the claim.
3. Based on my understanding, Sensitive Neurons refers to specific indices, rather than neurons. This name could be misleading.
4. For line 284, the details of removing operation are unclear.

### Soundness
1

### Presentation
2

### Contribution
1
