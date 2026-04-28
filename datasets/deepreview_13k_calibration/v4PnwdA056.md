# DEAN: Deactivating the Coupled Neurons to Mitigate Fairness-Privacy Conflicts in Large Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Ensuring awareness of fairness and privacy in Large Language Models (LLMs) is critical. Interestingly, we discover a counter-intuitive trade-off phenomenon that enhancing an LLM's privacy awareness through Supervised Fine-Tuning (SFT) methods significantly decreases its fairness awareness with thousands of samples. To address this issue, inspired by the information theory, we introduce a training-free method to \textbf{DEA}ctivate the fairness and privacy coupled \textbf{N}eurons (\textbf{DEAN}), which theoretically and empirically decrease the mutual information between fairness and privacy awareness. Extensive experimental results demonstrate that DEAN eliminates the trade-off phenomenon and significantly improves LLMs' fairness and privacy awareness simultaneously, \eg improving Qwen-2-7B-Instruct's fairness awareness by 12.2\% and privacy awareness by 14.0\%.
More crucially, DEAN remains robust and effective with limited annotated data or even when only malicious fine-tuning data is available, whereas SFT methods may fail to perform properly in such scenarios. We hope this study provides valuable insights into concurrently addressing fairness and privacy concerns in LLMs and can be integrated into comprehensive frameworks to develop more ethical and responsible AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an approach to improve privacy and fairness simultaneously by deactivating the neurons that react to both objectives.

### Strengths
- The paper studies an interesting problem of the tradeoff between privacy and fairness in fine-tuning.
- As a mitigation, the paper further proposes a training-free method.

### Weaknesses
 - Theorem 1: The theoretical model assumes that they share the same activation on certain representations, abstracted through a single random variable $Z$. This is a strong assumption as the activation values for both privacy and fairness data might correlate but almost unlikely to lead to the same value. Does the same theoretical result hold if one consider the model that considered two different yet correlated representations $Z_1$ and $Z_2$ respectively for privacy and fairness data, i.e., $I(Z_1;Z_2)>0$?

- Proposition 1: The proposition statement seems problematic. In inequality (2), the terms inside mutual information is an expectation, which has no randomness.

- The paper discusses an interesting finding yet it will be great to further examine this finding in different setups. E.g., is it possible to improve privacy and fairness simultaneously by simply balancing the ratio between privacy and fairness data? How do privacy and fairness vary with different number of samples in SFT?

### Questions
See above.

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
3

### Summary
The paper proposes new methods to deactivate fairness and privacy neurons, improving fairness awareness compared to Supervised Fine-tuning methods such as Full Finetuning (FFT) and LoRA.

### Strengths
1. The paper investigates an interesting phenomenon in supervised fine-tuning methods, where their approach enhances the LLM's privacy awareness but decreases fairness awareness.

2. The presentation is well done.

### Weaknesses
1. The baseline is somewhat confusing. Why don’t the authors use privacy-related and fairness-related methods? The baseline methods mentioned in this paper do not seem to provide fairness and privacy analysis. There are many privacy-enhanced algorithms, such as DP-LoRA [1]. Do these algorithms also exhibit this phenomenon?

2. Identifying the related neurons seems time-consuming. Can the authors provide an efficiency comparison with other methods? The proposed method, DEAN, appears to generate masks that decouple fairness and privacy-related neurons and then apply the mask to the weights. However, it is unclear when the masking occurs.

3. The definitions of fairness and privacy differ somewhat from what I know in related fields. For example, how do these methods guarantee privacy and fairness (typically, in my field, we use differential privacy and group fairness definitions)? What are the formal definitions of privacy and fairness here, and how is effectiveness measured?

4. There is inconsistency in the notations. For instance, in line 208, $D_f$ and $D_p$ represent the fairness and privacy-related datasets, but in line 215 and Alg. 1, $D_b$ becomes fairness related and $D_f$ becomes privacy related dataset.

5. The theory part is too simplistic just like an inequality application.

### Questions
Refers to the weakness and questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
It addresses the challenge of balancing fairness and privacy in large language models (LLMs). The authors observe a trade-off where enhancing privacy awareness in LLMs through standard supervised fine-tuning (SFT) often diminishes fairness awareness, and vice versa. To mitigate this conflict, the paper introduces a novel, training-free method called DEAN (DEActivate the fairness and privacy coupled Neurons). Inspired by information theory, DEAN identifies and deactivates neurons that are coupled to both fairness and privacy awareness, thereby reducing mutual information between these representations. Experimental results demonstrate that DEAN effectively eliminates the fairness-privacy trade-off, achieving significant improvements in both areas, such as a 12.2% increase in fairness and a 14.0% increase in privacy awareness for the Qwen-2-7B-Instruct model. Additionally, DEAN shows robustness even with limited annotated data or when fine-tuning data is potentially biased. The authors suggest that DEAN could be integrated into broader frameworks to develop more ethical and responsible AI systems.

### Strengths
The authors introduce DEAN, a training-free method based on information theory that decouples fairness and privacy without needing extra fine-tuning, making it both effective and easy to understand.
The experiments show DEAN’s strong performance across multiple models and challenging scenarios, with noticeable improvements in fairness and privacy. It’s also robust in cases where data is limited or biased, making it practical for real-world situations where high-quality data can be hard to come by.
The paper is clearly structured, with straightforward explanations of the problem, DEAN’s approach, and helpful illustrations. The step-by-step breakdown makes it easy to follow and replicate.
By addressing both fairness and privacy at the same time, DEAN is a valuable tool for LLMs in sensitive areas. Its training-free design means it can be widely applied and easily integrated into existing frameworks without high computational costs.

### Weaknesses
While the paper compares DEAN with several fine-tuning methods, it lacks a detailed performance analysis against other advanced fairness and privacy protection techniques. Including such comparisons would help clarify DEAN’s relative strengths and weaknesses.
·  The paper relies on mutual information and HSIC to identify neurons coupled with fairness and privacy, but the accuracy of this method depends heavily on the quality and representativeness of the dataset. Limited or biased datasets could lead to inaccurate identification, potentially affecting DEAN’s effectiveness.
·  The paper uses a simple, threshold-based binary classification to identify neurons associated with fairness or privacy. This approach may miss neurons that contribute to multiple tasks or whose importance varies by context. A more refined scoring system could better capture these nuanced roles, improving DEAN’s accuracy in targeting the most relevant neurons.
Directly deactivating coupled neurons may unintentionally disrupt other important model functions, as these neurons could also contribute to additional tasks. To minimize this risk, the authors might consider techniques like partial suppression or dynamic weight adjustments, which would allow DEAN to address the fairness-privacy conflict without sacrificing the model’s general performance.
As a security topic, privacy is 0 or 1. Editing neurons may be applicable to other issues, such as hallucination, but it is unsuitable for privacy. The authors cannot give theoretical guarantees that their method will not leak private information. Moreover, from the neuron analysis view, compared with previous work, I cannot see any novelty except a simple theorem.

### Questions
The paper uses the Hilbert-Schmidt Independence Criterion (HSIC) to estimate mutual information. Does it provide a detailed explanation of the parameter choices for HSIC? How might variations in these parameters affect the identification of neurons coupled with fairness and privacy?


Does directly deactivating coupled neurons lead to information loss? Is there a significant impact on model performance from this approach? Has the paper explored alternative deactivation methods, such as partial suppression or weight scaling, to further reduce any negative effects on overall model performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an approach called DEAN that aims to mitigate the conflict between fairness and privacy-consciousness in large language models (LLMs) by de-activating coupled fairness and privacy neurons. It is found that enhancing privacy awareness through traditional fine-tuning methods leads to a decrease in fairness and vice versa. DEAN utilizes information theory to reduce the interplay between fairness and privacy, thereby enhancing the independence of the two. The authors conducted experiments using DEAN on several models (e.g., Qwen2-7B-Instruct, Llama2, etc.) as well as on three datasets with different dimensions.

### Strengths
1. The proposed method can simultaneously improve the model's awareness of fairness and privacy protection by identifying and de-activating, without sacrificing the overall performance of the model. While traditional fine-tuning methods usually require a large amount of computational resources, especially in resource-poor scenarios, DEAN does not require additional training, which is highly efficient and innovative, and provides a new way of thinking for model optimization under resource-constrained conditions.
2. The authors tested the DEAN approach on several LLMs of different sizes and architectures (e.g., Qwen2, Vicuna, Llama2, etc.) to ensure its broad applicability and reliability. By using different types of datasets such as Beavertails, Salad-bench and Alpaca, the authors were able to evaluate the performance of DEAN in terms of fairness and privacy preservation, and to examine its effectiveness for modeling different data environments and task requirements.
3. The paper uses several charts to visualize the effects of DEAN, for example, to show the conflict between fairness and privacy, the performance of DEAN on different models, and so on. The table also lists the fairness and privacy enhancement of each model, which makes the experimental results more intuitive and convincing.

### Weaknesses
1. The de-activation operation may have side effects on other features of the model, such as affecting generation fluency or multitasking ability. Although the article evaluates the impact of DEAN on the overall performance of the model through several benchmarks (e.g., HellaSwag, Race, MMLU) in Table 3, generation fluency and multitasking capabilities were not specifically tested. It is recommended that the authors provide more specific assessments of generative fluency and multitasking, possibly through more specific generative tasks or benchmarks (e.g., generative coherence or cross-task accuracy metrics), to better understand the potential impact of DEAN on model performance.
2. Although the importance scoring mechanism is simple and efficient, the lack of comparative analysis with other neuron selection methods may affect the optimal performance of DEAN. It is recommended that the authors further experiment with other neuron selection methods, e.g., using clustering algorithms (e.g., K-means or DBSCAN) to cluster neuron activation patterns and group neurons belonging to sensitive feature mappings into the same group; and using interpretive methods, such as SHAP or LIME (Local Interpretable Model-agnostic Explanations), to compute the contribution of each neuron in the fairness and privacy tasks. The authors can consult relevant paper references to compare the effects of different selection strategies on the de-activation effect to confirm whether the choice of importance scores is optimal. This will help to understand the differences in the performance of different methods in decoupling operations and may further enhance the performance of DEAN.
3. The experiments mainly focused on generative tasks and lacked tests on common task types such as classification, question and answer, and sentiment analysis. May limit the effectiveness of DEAN in real-world applications. It is recommended to test on a wider range of task types (e.g., classification, Q&A, sentiment analysis), and it is recommended to use publicly available benchmark datasets, such as IMDB, SQuAD (Q&A), and AG News (Classification), to help assess the fairness and privacy-preserving ability of DEAN more comprehensively. Despite the challenges of obtaining real data, data from real-world scenarios can better model DEAN's performance in real-world applications.

### Questions
1. See weakness 1.
2. Did the authors consider other, more precise methods of neuron selection? Why did they ultimately choose this mechanism based on importance scores? Were other selection mechanisms tried and their effects compared?

### Soundness
3

### Presentation
3

### Contribution
2
