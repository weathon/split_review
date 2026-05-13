# Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Multimodal Large Language Models (MLLMs) exhibit promising advancements across various tasks, yet they still encounter significant trustworthiness issues. 
Prior studies apply Split Conformal Prediction (SCP) in language modeling to construct prediction sets with statistical guarantees. 
However, these methods typically rely on internal model logits or are restricted to multiple-choice settings, which hampers their generalizability and adaptability in dynamic, open-ended environments. 
In this paper, we introduce \textit{TRON}, a \textbf{t}wo-step framework for \textbf{r}isk c\textbf{o}ntrol and assessme\textbf{n}t, applicable to any MLLM that supports sampling in both open-ended and closed-ended scenarios. 
\textit{TRON} comprises two main components: (1) a novel conformal score to \textbf{sample} response sets of minimum size, and (2) a nonconformity score to \textbf{identify} high-quality responses based on self-consistency theory, controlling the error rates by two specific risk levels. 
Furthermore, we investigate semantic redundancy in prediction sets within open-ended contexts for the first time, leading to a promising evaluation metric for MLLMs based on average set size.
Our comprehensive experiments across four Video Question-Answering (VideoQA) datasets utilizing eight MLLMs show that \textit{TRON} achieves desired error rates bounded by two user-specified risk levels. Additionally, deduplicated prediction sets maintain adaptiveness while being more efficient and stable for risk assessment under different risk levels.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a two step risk control based framework extending split conformal prediction method for open ended and multimodal (videoQA) tasks. The method applies a conformal score to calibrate the minimum number of responses (samples) needed to ensure coverage. This score defines the prediction set’s error rate at a risk level alpha. It then refines the set using frequency or semantic similarity to identify high quality responses controlled by another risk parameter beta. The overall risk is bounded by a function of alpha and beta to provide statistical consistency guarantees using calibration, sampling and refinement steps. The paper builds upon multiple conformal risk control based methods and addresses the shortcomings with this two step method (to maintain smaller average prediction set size (APSS))  with lower risk thresholds) and applying them to multimodal videoQA setting.

### Strengths
- The paper's two-step risk control methodology addresses general shortcoming of the conformal prediction method and provides statistical guarantees for error rates, increasing the reliability of MLLM responses.
- Since open ended tasks are more challenging due to large number of possible generation, this method (two step approach, use of semantic similarity) seems to dynamically adapt well to provide flexible prediction set sizes for complex and generic generative scenarios (although we need more experimental validation). Error stays within bounds even after filtering step (bounded by alpha + beta - alpha.beta)
- As shown is Figure 3, deduplication of the semantically similar responses helps with more stable error rates and smaller prediction sets. Experiments suggest that semantic diversity can create smaller, more efficient prediction sets (lower APSS) without compromising on accuracy (EER stays within limits).

### Weaknesses
 - Authors already mention under limitations that guarantees are not conditional to individual data points but marginal over the test set. With this limitation, it may still be a bottleneck where risk compliance guarantees are needed for critical applications requiring more stringent guarantees and/or compliance requirements. The marginal coverage guarantee, while statistically sound across the entire test set, does not ensure that each individual prediction set achieves the desired coverage rate. This is a significant limitation for applications where reliability is needed on a per-instance basis.
- more open-ended evaluations and experiments on the open-ended datasets would have shed more light on the strengths and weaknesses of the methods (like Fig 4b). This is a key innovative strength of the method to address open-ended tasks (unlike MCQ) and adoption of this method will depend heavily on understand the strengths of this method in more open-ended generation tasks. The paper's focus on video question answering, while relevant, does not fully explore the potential of the proposed method in more diverse open-ended generation scenarios. The experiments should include a wider range of tasks to better demonstrate the general applicability and robustness of the approach.

### Questions
- Do you foresee any major modifications needed for TRON to control risk in scenarios involving distribution shifts, where calibration and test distributions differ?
- Would it be feasible to incorporate dynamic adjustments to prediction set sizes based on task difficulty or user preferences in real time? Are there challenges with balancing efficiency and robustness in such a dynamic setting?
- Could access to model internals like logits help improve TRON's performance?
- Could reliance on frequency-based nonconformity scores lead to biases in the types of responses included in the prediction set, especially in cases where the model’s sampling is limited?
- Have you observed any variance in EER across different model architectures or response generation and sampling methods (for example, cases where EER can go outside the bounds set by alpha and beta)
- How easy is it to generalize this approach beyond VideoQA to other open-ended tasks? Are there any major limitations or requirements for generalization?

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
3

### Summary
The authors propose a two-step framework, TRON, for assessing and controlling risk in MLLMs, specifically targeting VideoQA tasks. The framework consists of: (1) Sampling Step: This step involves calibrating a conformal score that defines the minimum number of response samples needed to ensure the inclusion of acceptable responses within a certain risk level. (2) Identification Step: In this phase, a nonconformity score based on self-consistency theory identifies high-quality responses within the candidate set. This score accounts for model uncertainty by estimating reliability via response frequency, introducing another risk level to statistically control errors.

The authors carry sufficient experiments on four VideoQA datasets with eight MLLMs and demonstrate that TRON achieves desired error rates within the specified risk bounds. The study further highlights TRON’s adaptability and stability through deduplicated prediction sets that provide more efficient and robust uncertainty estimation across various risk levels.

The authors address limitations in existing SCP methods, which either modify outputs to ensure factuality, rely on internal token sequence logits, or restrict applications to multiple-choice settings. This new approach is versatile, applicable to both open-ended and closed-ended VideoQA tasks, and operates independently of internal model outputs.

### Strengths
1. TRON’s two-step approach combines conformal scores and self-consistency theory to establish a flexible and robust risk assessment framework for MLLMs, particularly in open-ended scenarios, where traditional SCP methods fall short.
2. The paper presents extensive experiments across four VideoQA datasets and eight MLLMs, showcasing TRON's effectiveness and consistency in different VideoQA tasks.
3. By avoiding reliance on model logits, TRON is adaptable for API-restricted MLLMs, expanding its usability in various practical applications.

### Weaknesses
I raise the concern that although TRON is evaluated on diverse datasets, it primarily focuses on VideoQA tasks. Could it be tested on additional multimodal tasks to enhance the generalizability of its risk management capabilities?

### Questions
1. How does TRON handle outliers in response sampling that may disproportionately affect the frequency-based confidence scoring?
2. Could TRON’s conformal score be further adapted to dynamically adjust the sampling size based on real-time uncertainty measurements?

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
The paper deals with risk control and assessment for MLLMs. To address the issues of existing work relying on the internal model logits and working in the multiple-choice setting, the authors propose a TRON, a two-step framework for MLLMs supporting sampling for both open-ended and close-ended scenarios. TRON allows controlling error rates by sampling response sets of minimum size and identifying high-quality responses using self-consistency theory. The experiments on VideoQA demonstrate the efficacy on eight MLLMs.

### Strengths
- The paper is easy to follow and understand.
- The proposed method extends SCP to open-ended scenarios by estimating the confidence from frequency.

### Weaknesses
 - The confidence estimation in Step 2 relies on the prediction of another model(e.g. DeBERTa-large-mnli). Then it should be at least discussed on the reliability as the semantic classifier. Otherwise, it makes the identification of risk control less convincing.

- It is unclear how the silence percentage is conducted on the audio, and how the conclusion ‘introduce audio modality enhances the confidence level’ (Line371-372) is made. It is shown in Fig. 4 that increasing SPs leads to higher APSS. Also, introducing audio modality seems to only improve VideoLLaMA with SP <50%.   

- It seems that the proposed method is general to LLMs as well. How does the proposed method work for LLMs for both open-ended and close-ended scenarios? The paper claims this advantage but shows no experimental results. This would make the paper more impactful.

- How is the proposed method compared with existing methods for LLMs on such as MCQA? Such a comparison would make the paper more comprehensive.

### Questions
- It seems that the best practice of the ratio of the calibration and test set is model-dependent. Is there any insight on the ratio selection when applied to different MLLMs?

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
The paper presents **TRON**, a two-step framework designed for **risk control and assessment** in multimodal large language models (MLLMs), particularly for **Video Question Answering (VideoQA)** tasks. Addressing challenges in dynamic and open-ended environments, TRON leverages **Split Conformal Prediction (SCP)**, introducing a **conformal score** for sampling response sets and a **nonconformity score** for identifying high-quality responses. Through experiments on several VideoQA datasets, TRON demonstrates the ability to achieve desired error rates across various **user-specified risk levels**. It is also noted for exploring the concept of **semantic redundancy** in prediction sets as an evaluation metric, an area not previously investigated in open-ended contexts.

### Strengths
1. **Innovative Framework**: The introduction of TRON, a two-step risk control and assessment framework, contributes significantly to the field of MLLM evaluation in both open-ended and closed-ended VideoQA tasks. Its flexibility in applying conformal prediction in open-ended contexts is commendable.

2. **Novel Conformal and Nonconformity Scores**: The paper proposes a unique conformal score for setting the minimum sample size in open-ended tasks and a nonconformity score based on self-consistency theory. These scores provide a rigorous approach to risk control.

3. **Addressing Uncertainty with Redundancy Analysis**: The evaluation of **semantic redundancy** in open-ended settings introduces a new angle to uncertainty measurement, providing a promising metric that complements traditional accuracy.

4. **Comprehensive Experimental Evaluation**: The experiments span multiple datasets, risk levels, and different types of MLLMs, offering a thorough assessment of TRON’s effectiveness in diverse conditions.

### Weaknesses
1. **Limited Discussion of Practicality and Adaptability**: While TRON provides theoretical guarantees, the practical aspects, such as computational overhead and applicability in real-world scenarios, could be discussed in greater depth. Specifically, the paper lacks a detailed analysis of the time complexity associated with generating multiple responses and evaluating their reliability using the proposed conformal and nonconformity scores. This is crucial for assessing its feasibility in real-time applications or when dealing with large-scale datasets. Furthermore, the paper does not address the potential challenges in adapting TRON to different types of MLLMs or tasks beyond VideoQA, such as image captioning or multimodal dialogue systems, which might require adjustments to the scoring mechanisms or sampling strategies.

2. **Insufficient Baseline Comparisons**: The paper lacks a comparison with other standard risk control methods or frameworks that may be relevant, particularly in closed-ended settings or previous SCP applications in MLLMs. For instance, the paper does not compare TRON against simpler, heuristic-based risk control methods, such as thresholding based on model confidence scores or ensemble-based approaches, which could serve as a baseline for evaluating the added value of the proposed conformal prediction framework. Additionally, the paper does not discuss how TRON compares to existing applications of Split Conformal Prediction (SCP) in other domains, which could provide insights into its novelty and potential limitations.

3. **Complexity in Method Presentation**: Some sections of the methodology, particularly the derivation of the conformal and nonconformity scores, lack clarity, which could challenge readers unfamiliar with SCP. The paper does not provide a step-by-step explanation of how the conformal score is derived from the loss function, nor does it clearly articulate the assumptions underlying the nonconformity score based on self-consistency theory. This lack of detailed explanation makes it difficult to fully understand the theoretical underpinnings of TRON and to replicate the results. Furthermore, the paper could benefit from a more intuitive explanation of how the proposed scores relate to the underlying uncertainty in the model's predictions.

4. **Inconsistent Evaluation Details**: Although the experiments are extensive, details on some evaluation metrics, like APSS and their implications for different risk levels, could be better explained. The paper does not provide a clear explanation of how APSS is calculated for open-ended tasks, especially when prediction sets can have varying sizes and semantic content. The choice of models and how each metric was applied in open-ended versus closed-ended settings was also not consistently clarified. For example, it is unclear if the same evaluation protocol was used for all datasets and models, and how the semantic redundancy metric is integrated into the overall evaluation process.

### Questions
1. **What is the expected computational impact** of using TRON in large-scale applications or real-time risk assessment tasks? Could you provide a more detailed explanation or metrics regarding the processing time required for each step?

2. **Baseline Method Comparison**: Have you considered comparing TRON with simpler risk control baselines? For instance, would a heuristic-based risk control method suffice for certain types of tasks in closed-ended VideoQA? If not, could you clarify how TRON performs specifically better in such cases?

3. **Semantic Redundancy in Open-Ended Tasks**: How does the semantic redundancy analysis handle responses that may be lexically distinct but only partially semantically equivalent? Could this approach potentially overlook responses with subtle but important semantic differences?

4. **Alternative Conformal and Nonconformity Scoring Methods**: Could the proposed conformal and nonconformity scores be further enhanced by alternative methods, such as clustering-based or confidence-based approaches beyond self-consistency theory? If so, what would be the implications for TRON’s current framework?

5. **Additional Real-World Validation**: Have there been any attempts to validate TRON in real-world or industry-specific VideoQA tasks, possibly in collaboration with industry partners? If so, could you share any preliminary insights on its practical performance and potential adaptations? If not, do you plan to include such validation in future work?

### Soundness
3

### Presentation
2

### Contribution
3
