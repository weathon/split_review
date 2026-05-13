# MultiTrust: Enhancing Safety and Trustworthiness of Large Language Models from Multiple Perspectives

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Large Language Models (LLMs) have shown impressive performance across various tasks, yet they still face significant safety and trustworthiness challenges, such as robustness, fairness, and truthfulness. Addressing these challenges is critical for the reliable deployment of LLMs. Directly fine-tuning LLMs to enhance safety can degrade their performance and is challenging to balance across multiple safety perspectives due to the forgetting phenomenon. In this paper, we propose MultiTrust, a novel and scalable framework designed to enhance LLM safety from multiple safety perspectives. In particular, MultiTrust first generates challenging training data through adversarial optimizations, focusing on LLMs trustworthiness perspectives, such as robustness, fairness, and safety. MultiTrust then separately train safety auxiliary models for each perspective using supervised fine-tuning and Direct Preference Optimization (DPO). MultiTrust augments a base model with these safety auxiliary models on the fly through dynamic routing and logit ensembling, significantly boosting the performance across different trustworthiness metrics for the base model while preserving its helpfulness. Notably, MultiTrust introduces an effective perplexity-based inference-time router to seamlessly integrate these safety auxiliary models by averaging the logit outputs of the selected safety auxiliary model and the base model, which enhances the stability of the final performance. Moreover, MultiTrust's flexible design allows for the augmentation with new safety auxiliary models for different perspectives without necessitating additional training or adaptation. Extensive experimental results show that MultiTrust, which trains a series of 7B safety auxiliary models, significantly improves the trustworthiness of the base LLM across different sizes (7B and 13B). For instance, MultiTrust increased the average performance of Llama2-13B from 35.54% to 51.14%, and Vicuna-13B from 29.91% to 52.82%, outperforming models with similar and even larger sizes across different perspectives. These results underscore the effectiveness and scalability of MultiTrust in enhancing the safety and reliability of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on improving the safety and trustworthiness of LLMs. While directly fine-tuning LLMs can enhance safety, it often leads to forgetting issues and difficulty in optimizing multiple perspectives simultaneously. To tackle this, the authors propose MultiTrust, which trains auxiliary safety models for each perspective separately and incorporates a perplexity-based inference-time router to combine one of their logits with that of the base model. In this way, without optimizing the parameters of the base model, MultiTrust can not only improve safety of LLMs but also preserve their original capabilities.

### Strengths
•	The proposed framework includes a list of data generation methods for each perspective. Experiments show that with the help of auxiliary models, the base models can largely improve their trustworthiness while maintaining general performance.
•	For comparison, the authors compare auxiliary model fine-tuning with a mixed-dataset or continuous training strategy, finding that training auxiliary models separately is more effective.
•	From Tables 4 and 5, it is interesting that different perspectives have interactions and mutual influence, and the data used to enhance robustness spans a broad range of domains.

### Weaknesses
•	Since MultiTrust trains auxiliary models for each perspective, it is essential to compare it with other methods optimized for specific perspectives (as written in Introduction). Table 1 only presents the performance of a set of baseline models.
•	In Section 3.2, the authors use PPL to select the optimal safety model, but no explanation or supporting evidence is provided for this choice. It is unclear why perplexity would be a good indicator of which auxiliary model is most appropriate for a given input, especially since perplexity is typically used to evaluate language model fit, not necessarily safety or trustworthiness.
•	MultiTrust relies on the logits from base and auxiliary models, which restricts its applicability to classification tasks. And it would be better to report scores for each auxiliary model across specific perspectives to allow for direct comparison with MultiTrust. The current presentation makes it difficult to assess the individual contributions of each auxiliary model and whether the ensembling approach is truly beneficial compared to simply using the best performing auxiliary model for each perspective.

### Questions
•	In Table 2, Fine_sep on Truth performs slightly lower than Llama2-7B, yet the truthfulness auxiliary model improves the base model’s performance on Truth compared to other model sizes. Is this trend consistent across different model sizes?
•	The training details are missing. In Line 249, the authors state that DPO is trained for 1000 steps. Given the high risk of overfitting in DPO, what batch size is used?

### Soundness
3

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
The paper introduces MultiTrust, a framework to enhance the safety and trustworthiness of large language models (LLMs) from multiple safety perspectives, including robustness, fairness, and truthfulness. MultiTrust employs adversarial training data generation, safety auxiliary models, and a perplexity-based routing mechanism to dynamically align base LLMs with specialized safety models, improving their performance across these safety perspectives without sacrificing general task performance. Experimental results show significant trustworthiness improvements, especially in enhancing robustness and fairness while maintaining scalability.

### Strengths
1. The paper is written clearly and is easy to follow. The overview figure of MultiTrust is particularly effective in visually clarifying the framework’s components and workflow.
2. The authors conduct a comprehensive evaluation of MultiTrust across various base models and benchmarks. The analysis includes detailed empirical observations that provide valuable insights into how MultiTrust performs across different trustworthiness perspectives. 
3. The paper offers a novel multi-perspective approach to LLM safety enhancement. By introducing an inference-time routing mechanism to dynamically align models with appropriate safety auxiliary models, MultiTrust can address multiple safety concerns in parallel—a significant innovation that moves beyond the conventional focus on isolated safety aspects. This modular integration offers a flexible and scalable solution that is well-suited for real-world applications demanding high standards of trustworthiness.

### Weaknesses
1. The technical novelty and the specific application scenario for MultiTrust are not sufficiently clear. While combining synthetic data generation with an inference-time routing mechanism is effective, both elements have been established previously. The framework may thus appear as a relatively straightforward combination of existing approaches without introducing substantial innovation in either area.

2. The selection of empirical results in the main text, such as the slight accuracy reductions in ARC and MMLU for Vicuna-7B and Llama2-13B, is not fully representative. Table 1 shows non-negligible performance degradation in general helpfulness benchmarks for other data points, which may suggest that MultiTrust has more notable limitations in maintaining helpfulness across benchmarks than the highlighted examples imply.

3. MultiTrust requires more data and increased computational resources, and thus the observed performance improvements over the base models are not unexpected given these added resources. The experiments presented do not sufficiently demonstrate that the routing mechanism offers a definitive advantage over simpler strategies like ensembling, model merging, or other approaches for multi-task learning.

4. The paper claims scalability for MultiTrust in the abstract and introduction, but this aspect is not thoroughly explained or validated in later sections.

### Questions
1. In the paper, the authors mention using only the first two iterations of data collected by the GRATH method for the Truthfulness dataset. Could the authors elaborate on why only these initial iterations were used? Additionally, is the Truthfulness dataset treated differently from the datasets used for Adversarial Robustness and Fairness? 
2. The paper mentions five types of word-level perturbations used to construct the adversarial robustness dataset: typo-based, embedding-similarity, context-aware, knowledge-guided, and semantic-optimization-based perturbations. Could the authors provide specific examples from the constructed dataset to illustrate these perturbations and clarify how each type was applied in practice? 
3. The parameter 𝛾 plays a crucial role in balancing the influence of the base model and the safety auxiliary models, yet the specific value used is not clearly stated. Could the authors detail how 𝛾 was selected in your experiments and discuss its impact on model performance?

4. In Table 1, while it’s stated that the impact on model helpfulness is minimal, there are cases of notable accuracy drops, such as Llama-2-13B on HellaSwag (82.14% to 78.44%) and Vicuna-7B on Winogrande (72.38% to 68.90%). Could the authors provide further explanation on how these decreases align with the claim of minimal impact, and perhaps discuss the trade-offs involved in these cases?

5. It would be helpful to include MultiTrust in the comparative analysis shown in Table 2. If my understanding is correct, the models under ${\text{FT}}_{\text{sep}}$ do not utilize any routing mechanism. Comparing these with MultiTrust could provide a clearer view of the routing mechanism’s benefits.

6. Adding comparisons with other multi-task learning methods would be beneficial. 

I would be happy to engage with the authors to help improve the presentation of the method and evaluation during the discussion phase, but my concerns are not insignificant. Clarifications would need to resolve my questions in order for my score to improve.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes MultiTrust, a  framework aimed at enhancing the safety and trustworthiness of LLMs by addressing critical challenges such as robustness, fairness, and truthfulness. MultiTrust introduces a solution by generating challenging training data through adversarial optimizations and training specialized safety auxiliary models for each safety perspective.

### Strengths
1. MultiTrust addresses safety and trustworthiness from multiple angles—robustness, fairness, and truthfulness—which is a holistic approach not commonly found in other frameworks.
2. This paper is well-written and
3. This paper is easy to understand.

### Weaknesses
1. The author overestimate their findings, since selection made by evaluating the perplexity of the input with each model and choosing the model that minimizes it does not guarantee overall benign performance or helpfulness of the models. The perplexity metric, while useful for assessing model fit to training data, does not directly correlate with safety or helpfulness. A model could achieve low perplexity on adversarial inputs by simply memorizing patterns, without actually exhibiting robust or safe behavior. This approach might also favor models that are overfit to the training data, potentially reducing their generalization capabilities on unseen, genuinely adversarial examples.
2. The effectiveness of the first stage heavily relies on the quality and representativeness of the adversarial dataset. Biases in data collection can lead to biased model behaviour. Lack of dataset ablation study. The paper does not provide sufficient detail on the specific types of adversarial examples used, nor does it justify the choice of perturbation strategies. Without a clear understanding of the adversarial data distribution, it is difficult to assess the generalizability of the proposed method. Furthermore, the lack of an ablation study makes it impossible to determine which types of adversarial examples are most effective in improving model safety.
3. The experiment that elevated the average performance score of Llama2-13B from 35.54% to 51.14% and Vicuna-13B from 29.91% to 52.82% lacks credibility if conducted in isolation. To enhance the reliability of these findings, it is essential to incorporate additional experiments and comparisons with other models, different architecture or different in size. The reported performance gains are substantial, but without comparisons to other state-of-the-art safety training techniques, it's hard to determine if these improvements are truly significant or simply due to the specific experimental setup. The lack of experiments with different model sizes and architectures further limits the generalizability of the findings.
4. Parameters involved in the formulas, such as β in DPO and γ in the alignment process, may require careful tuning. But the methodology section have not discussed the impact of the selection of these parameters. The paper does not provide any justification for the chosen values of β and γ, nor does it explore the sensitivity of the results to these parameters. Without such analysis, it is difficult to assess the robustness of the proposed method to different hyperparameter settings.

### Questions
1. You indicates that certain model behaviors developed for one perspective can enhance performance in others. But is that also happened to SFT?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces MultiTrust, a framework designed to enhance the safety and trustworthiness of large language models (LLMs) across multiple safety dimensions, specifically robustness, fairness, and truthfulness. MultiTrust addresses the challenge of balancing these safety perspectives without degrading model performance, a common issue with sequential fine-tuning approaches.

### Strengths
* Comprehensive Safety Perspective Coverage: MultiTrust addresses robustness, fairness, and truthfulness, which are critical for LLM deployment, particularly in sensitive or safety-critical environments.

* Good Trade-offs: MultiTrust improves trustworthiness without substantially compromising general model performance

### Weaknesses
 * Data Dependency: The effectiveness of MultiTrust is strongly influenced by the quality and diversity of the generated datasets.

* Efficiency: For each base model, dataset construction and fine-tuning must be repeated, and even minor changes in the base model architecture may impact auxiliary model performance.

* Scalability: Integrating auxiliary models adds inference overhead, particularly as the number of safety perspectives increases.

### Questions
1. Given that adversarial robustness relies on standard datasets (SST-2, QQP, NLI) and established construction methods, how effectively can the auxiliary model generalize if the adversarial prompts differ significantly from these distributions?

2. How adaptable are the auxiliary models to incremental updates of the base model, such as those from continual learning? Additionally, are there strategies to reduce the need for repeated dataset construction and fine-tuning when applying MultiTrust to similar base models?

3. Could the authors provide an analysis of the inference overhead introduced by incorporating auxiliary models?

4. As the number of integrated safety perspectives grows, how to reduce the inference overhead associated with the auxiliary models?

### Soundness
3

### Presentation
3

### Contribution
2
