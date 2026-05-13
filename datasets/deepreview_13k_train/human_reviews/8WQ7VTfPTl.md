# Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors

- Decision: Accept
- Scores: 6, 6, 6, 6, 8

## Abstract
Large language models (LLMs) have achieved remarkable performance across many tasks, yet aligning them with desired behaviors remains challenging. Activation intervention has emerged as an effective and economical method to modify the behavior of LLMs. Despite considerable interest in this area, current intervention methods exclusively employ a fixed steering vector to modify model activations, lacking adaptability to diverse input semantics. To address this limitation, we propose \textbf{Semantics-Adaptive Dynamic Intervention (\sadi)}, a novel method that constructs a dynamic steering vector to intervene model activations at inference time. More specifically, \sadi utilizes activation differences in contrastive pairs to precisely identify critical elements of an LLM (i.e., attention heads, hidden states, and neurons) for targeted intervention. During inference, \sadi dynamically steers model behavior by scaling element-wise activations based on the directions of input semantics. Experimental results show that \sadi outperforms established baselines by substantial margins, improving task performance without training. \sadi's cost-effectiveness and generalizability across various LLM backbones and tasks highlight its potential as a versatile alignment technique.
In addition, we release the code to foster research along this line

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel Semantics-Adaptive Dynamic Intervention (SADI) technique for Large Language Models (LLMs). Unlike conventional methods using fixed steering vectors, SADI adapts dynamically to the semantic context of inputs, modifying the model’s internal activations accordingly. Using activation differences from contrastive pairs, SADI identifies key elements (attention heads, hidden states, and neurons) of the model for targeted intervention. Experimental results show that SADI outperforms traditional intervention methods across various models, including LLAMA2-7B-CHAT, BLOOMZ-7B, MISTRAL-7B, and FALCON-7B-INSTRUCT, without requiring additional training. SADI’s cost-effectiveness and adaptability across languages and tasks highlight its potential as a versatile alignment technique​.

### Strengths
1. The paper is well-written, and the methodology is clearly presented.
2. SADI achieves substantial performance improvements across various benchmarks, often outperforming baseline methods by significant margins without additional training.

### Weaknesses
1. The paper lacks sufficient detail regarding the construction of contrastive pairs, including the specific number of examples used. Additionally, an ablation study on how the number of contrastive examples affects SADI’s performance would provide valuable insights into the robustness and scalability of the method. Specifically, the paper does not detail the criteria for selecting contrastive pairs, such as whether they are semantically similar or dissimilar, or if they are generated using a specific method. This lack of clarity makes it difficult to assess the generalizability of the approach. Furthermore, the absence of an ablation study on the number of contrastive pairs leaves open questions about the method's sensitivity to the size of the contrastive dataset. It is unclear if the performance gains saturate with more examples, or if there is a risk of overfitting with too many contrastive pairs.
2. The experiments are limited to models up to 7B parameters, leaving the effectiveness of SADI on larger models (e.g., 13B, 30B, or more) untested. This is a significant limitation, as the behavior of LLMs can change drastically with scale. It is not clear if the observed performance gains on smaller models would translate to larger models, which are often more complex and have different emergent properties. The paper should include experiments on larger models to demonstrate the scalability of SADI.

### Questions
1. In the experiments, are the questions ($x_i$) used for contrastive pair construction sourced directly from the task datasets (in-distribution), or do they include any out-of-distribution samples?
2. Could you provide a qualitative example illustrating how SADI’s input-adaptive mechanism offers semantic adaptability compared to traditional fixed-vector approaches? This would clarify the practical benefits of SADI’s dynamic intervention.
3. Could the authors provide further analysis on why SADI-HIDDEN shows lower performance on certain tasks? Exploring underlying causes for these variations could provide deeper insights.

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
5

### Summary
This work proposes an approach to dynamically steer model hidden states by adapting to the semantic contexts of inputs during inference time. Extensive experiments across various tasks, LLMs backbones, and languages show the effectiveness.

### Strengths
- Figures and tables are clear and easy to read.
- The method is explained in detail with clear mathematical formulations, pseudocode and a clear visual representation.
- The experimental evaluation is extensive across multiple model architectures, languages, and tasks, accompanied by various ablation studies.

### Weaknesses
 - While the paper mentions the "linear representation hypothesis," it does not provide theoretical guarantees or formal analysis of why the method works. The paper lacks a rigorous justification for why adapting the steering vector based on the semantic content of the activations should lead to improved performance. It is unclear how the element-wise intervention, specifically the mask $M$, is theoretically grounded in the linear representation hypothesis.
- Based on Figure 2, the performance is very sensitive to the two hyper-parameters, but this paper doesn't provide clear guidelines for selecting these parameters in practice. The paper does not offer a principled approach for determining the optimal values of the intervention strength $\delta$ and the number of key elements $K$. The lack of a clear methodology for hyperparameter selection makes the method less practical for real-world applications, as users would need to conduct extensive and potentially costly grid searches.
- The work lacks a critical comparison of computational efficiency across methods. While SADI is claimed to be "cost-effective,” no concrete metrics (inference time, memory usage, computational overhead) are provided to compare against other baselines. The paper only claims that the steering vector introduces negligible memory overhead without providing any quantitative analysis. Furthermore, the claim that the Adaptive Steering step has a time complexity of $O(1)$ is misleading, as the computation of the mask $M$ and the element-wise multiplication are not accounted for in this analysis.

### Questions
See weaknesses.

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
The paper proposes a new LLM intervention approach that aims to steer model behavior while adapting to the semantic contexts of inputs.  Unlike prior intervention approaches with fixed steering vectors, this paper proposes to dynamically change the steering vector based on test inputs. The paper presents extensive experiments and ablations to demonstrate the effectiveness of the approach across multiple common setups in the community.

### Strengths
- The paper is mostly well written with clear and logically coherent organization.
- The method is new and easy to implement.
-  The experiments and ablations are thorough.

### Weaknesses
My primary concern is that the paper places a strong emphasis on **what** the method achieves but does not sufficiently explore **why** it works and why certain design choices are more preferable, beyond what is shown by hyperparameter sweeping. 

While the results across various tasks and model families suggest that the method is generally effective, there is a notable lack of in-depth analysis (particularly in Sections 5 and 6), to elucidate the underlying reasons for its success. Furthermore, the results presented in Figure 2 indicate that the approach may require extensive hyperparameter tuning, as consistent setups across different datasets are not apparent.

Specifically, it would be great to delve into the following aspects:

(1) The experiments indicate that using attention heads yields superior results compared to using hidden states. However, the relationship between these components and the "steering behavior" remains unclear. A more detailed analysis of **why** attention heads (instead of hidden states) might contribute more effectively to the method's success would be valuable.

(2) The rationale behind selecting negative pairs is not entirely clear. For instance, why is a "blank space" used as an incorrect answer (L286)? Similarly, the choice of a "randomly chosen incorrect answer" for multiple-choice tasks may raise concerns of not being representative and can introduce high variance based on the selected samples. What defines a "good" negative answer and how it impacts the method remains under-explored.

### Questions
See above.

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
3

### Summary
This paper introduces an innovative method named SADI, designed to provide a dynamic vector to intervene model activations at inference time in LLMs. Specifically, SADI leverages activation differences in contrastive pairs to identify and target critical units for effective intervention. The effectiveness of this method is demonstrated in experiments using multiple popular LLMs on multiple tasks.

### Strengths
1. SADI is a general steering method applicable to a wide range of LLMs. Through extensive experiments with four model backbones over eleven diverse tasks, SADI has  proven to significantly enhance model performance, surpassing baseline methods by substantial margins. Detailed analysis demonstrates that interventions targeting attention heads consistently yields significant performance improvements across various tasks, validating the effectiveness of this dynamic steering approach.

2. This paper has a  clear structure and highlights the key points. Specifically, the Method section provides a detailed procedure of the proposed method. And in the Experiment section, they outline the experimental setup and objectives.  This makes it easy for readers to understand the core idea of this work. Besides, the author promises to release the code.

### Weaknesses
1.  In the Related Work Section, the author mentioned that the difference between SADI and these "fixed steering vector" works is that SADI takes "input semantics" into account. However, according to Algorithm 1, SADI uses the steering vectors obtained by the mean difference of activation of all positive and negative samples in the test set, which is also "fixed" to some extent. Besides, in the paper, the author said “CAA uses the mean difference in the activations at the position of the answer letter between all the positive and negative prompts to construct a fixed steering vector to shift activations.” From this angle, the changes made by SADI are actually very small. **So what is the essential difference between SADI and these related works? Why is SADI effective?**

2. For SADI, what is the relationship between the dataset used in "Difference Extraction" step and the dataset used in "Adaptive Steering" step? Are they from datasets on the same task? Or from datasets on different tasks? Or from the same dataset? What is the rationale for doing so? How to explain it?  I think these questions concern the effectiveness of SADI.

3. This paper lacks guidance on selection of hyperparameters. SADI introduces the hyperparameters, but there seems no way to perceive which hyperparameters is optimal when solving a new dataset from Experiment section. Without such a principle, SADI may be left in the shade compared with similar methods. 

4. No prominent improvement with SADI using SFT. In Table 1, SADI+SFT only performs 90.97 over SFT by 0.06. The author needs add more reasons why this issue occurs in the paper.

### Questions
As shown in Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the Semantics-Adaptive Dynamic Intervention (SADI) method for improving Large Language Models' performance on downstream tasks with a dynamic intervention mechanism. The method is shown to be effective through extensive experiments and requires only a small dataset. However, it is unclear for how to address the potential imbalance of positive and negative examples in real-world datasets, which could affect the method's applicability.

### Strengths
1. The paper introduces a novel approach called Semantics-Adaptive Dynamic Intervention (SADI) designed to modify the behavior of Large Language Models (LLMs) with the aim of enhancing their performance on downstream tasks through the intervention.
2. In contrast to prior research that necessitated fixed intervention masks for each task, this study introduces a dynamic intervention mechanism that autonomously adapts to a variety of downstream tasks.
3. The authors have conducted an extensive series of experiments to demonstrate the efficacy of their proposed method.
4. The ablation studies provided by the author are thorough and indicate that the SADI method does not demand an extensive dataset. Remarkably, approximately 150 examples are sufficient to achieve commendable performance with SADI.

### Weaknesses
1. As discussed in Section 3.2, the dataset T is structured such that each entry includes a single positive example and one negative example. In real-world scenarios, however, the prevalence of negative examples typically surpasses that of positive examples. In cases where negative examples are more abundant, the methodology for selecting which negative examples to include in the construction of each instance within dataset T is not clear. Guidance on this selection process would be beneficial. Specifically, the paper does not address the potential impact of using different types of negative examples (e.g., semantically similar vs. random negatives) on the intervention's effectiveness. The lack of clarity on how to handle an abundance of negative examples and the absence of a discussion on the quality of negative examples raises concerns about the practical applicability of the method in diverse real-world scenarios.

### Questions
Please refer to the Weakness Section.

### Soundness
4

### Presentation
3

### Contribution
4
