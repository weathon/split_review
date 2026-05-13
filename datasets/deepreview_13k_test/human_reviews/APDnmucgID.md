# Relative Preference Optimization: Enhancing LLM Alignment through Contrasting Responses across Identical and Diverse Prompts

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
In the field of large language models (LLMs), aligning models with the diverse preferences of users is a critical challenge. Direct Preference Optimization (DPO) has played a key role in this area. It works by using pairs of preferences derived from the same prompts, and it functions without needing an additional reward model. However, DPO does not fully reflect the complex nature of human learning, which often involves understanding contrasting responses to not only identical but also similar questions. To overcome this shortfall, we propose Relative Preference Optimization (RPO). RPO is designed to discern between more and less preferred responses derived from both identical and related prompts. It introduces a contrastive weighting mechanism, enabling the tuning of LLMs using a broader range of preference data, including both paired and unpaired sets. This approach expands the learning capabilities of the model, allowing it to leverage insights from a more varied set of prompts. Through empirical tests, including dialogue and summarization tasks, and evaluations using the AlpacaEval2.0 leaderboard, RPO has demonstrated a superior ability to align LLMs with user preferences and to improve their adaptability during the training process. %

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors proposed new preference optimization methods to improve the performance of preference learning on various tasks. They explained that the current state-of-the-art methods cannot fully reflect the complex nature of human learning. To overcome this challenge, they proposed Relative Preference Optimization (RPO) to discern between more and less preferred responses derived from identical and related prompts. They showed that RPO outperforms DPO, KTO, and IPO on dialogue, summarization, and general evaluation benchmarks.

### Strengths
The authors explored one of the important problems of direct preference optimization methods, and it's interesting. Another advantage of this paper is the comprehensive experiment and theory used to satisfy their hypothesis.

### Weaknesses
I would appreciate that if the authors could clarify the following points:

- The results show that RPO outperforms other methods. I looked at the implantation they put in Appendix G and understood the main difference between RPO loss and DPO loss is the weight matrix. I am wondering how the authors can describe if a policy model has knowledge about the difference between the response of prompt i and j (assume prompt i is a reasoning question, and prompt j is a usual question that asks about the weather) will have a better performance?

- The Experiment section shows that the authors didn't explore the hyperparameters for other methods. To the best of my knowledge for the authors, direct methods like DPO, IPO, and KTO have a different performance on different hyper-parameters like Batch-Size, Beta, Regularization terms in IPO etc. Also, they didn't use beta=0.01 for DPO, which is the best hyper-parameter for this method. So, I suggest the authors compare their methods with the best DPO, KTO, and IPO hyperparameters. 

- With respect to the comprehensive experiments, it seems the authors didn't report the scores for all models. For example, the experiments on Summarization are on the Mistral model, but for Anthropic-HH, it is on LLaMA (7B, 13B) and Mistral. Also, for other benchmarks, they didn't report the score for other methods. For example, on Open LLM  Leaderboard benchmarks, they just compared with KTO; another comparison method can be DRO [1]. I am confused as to why the authors used the Binarized Capybara Dataset because Ultrafeedback_binarized [2] is available, and they could use this dataset.

- New methods like SimPO and CPO are better choices for comparison. I encourage the authors to compare the proposed method with these algorithms, too.

- Using new models like LLaMA-3 can improve the experiment section.

---
[1] DRO:  https://arxiv.org/abs/2405.19107

[2] Ultrafeedback_binarized: https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized

### Questions
All the points are mentioned in the Weakness section.

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
4

### Summary
The Relative Preference Optimization (RPO) method presents a novel approach to aligning preferences that significantly improves data efficiency and effectiveness.

### Strengths
The proposed RPO method introduces an innovative approach to preference alignment, showcasing enhanced data efficiency and effectiveness. By integrating a contrastive weighting mechanism, RPO significantly broadens the learning capabilities of language models, allowing them to process a wider range of preference data. The experimental results across various tasks, such as dialogue, summarization, and general evaluation benchmarks, highlight RPO's superior adaptability and effectiveness in optimizing language model performance according to user preferences.

### Weaknesses
The paper states that "DPO does not fully reflect the complex nature of human learning, which often involves understanding contrasting responses to not only identical but also similar questions." However, there appears to be a lack of explicit experimentation or detailed discussion in the manuscript to substantiate this claim. It would be beneficial for the authors to provide empirical evidence or theoretical elaboration to support this assertion, which would strengthen the argument for RPO's advantages over existing methods like DPO.

### Questions
- How long does the embedding preprocessing step take?
- In my understanding, RPO utilizes a loss function similar to DPO's, augmented with a data reweighting mechanism. Could this mechanism be integrated with other approaches such as IPO, KTO, or SimPO? If so, what would the potential benefits or challenges be in combining these methodologies?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Relative Preference Optimization (RPO), an enhancement to the Direct Preference Optimization (DPO) method for aligning large language models (LLMs) with user preferences. RPO extends DPO by considering both identical and related prompts, and it uses a contrastive weighting mechanism to handle a broader range of preference data. Experiments demonstrate that RPO outperforms baseline methods on dialogue, summarization, and general evaluation benchmarks.

### Strengths
1. RPO addresses a limitation of DPO by incorporating both identical and related prompts, thereby expanding the model's ability to learn from a more diverse set of data.

2. The paper is well-written and clearly explains the methodology and experimental results, making it easy for readers to understand the contributions and their implications.

### Weaknesses
1. The approach of using sentence embeddings to assess semantic similarity may not be sensitive to token-level differences. This could be a significant drawback in domains like code and mathematics, where even minor differences in tokens of prompts can lead to entirely different or even contradictory answers.

2. The proposed RPO may be seen as a form of data augmentation, where different question answer pairs are combined during the training process to generate more data pairs to improve model performance. This augmentation approach is common in traditional data augmentation fields.

3. The experiments could be further strengthened. For instance, it would be interesting to see if using the model being trained to compute sentence similarity would yield better results. Additionally, the paper should explore whether this simple method provides any benefits for larger models, such as 13B or more capable ones, to fully validate its effectiveness across different scales.

### Questions
Please refer to the Weaknesses.

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
4

### Summary
The paper introducs Relative Preference Optimization (RPO), a novel method to enhance the alignment of LLMs with human preferences. RPO considers preferences across both identical and semantically related prompts and employs a contrast matrix to discern preferences between preferred responses via a contrastive weighting mechanism. So RPO enhancs model training with a broader range of data. Empirical tests on dialogue and summarization tasks showed that RPO outperforms existing methods like DPO, IPO, and KTO, especially in adapting to varied contexts.

### Strengths
- Extends beyond traditional methods by considering semantically related prompts.
- RPO is adaptable to both paired and unpaired data scenarios, making it a flexible tool for different types of preference data.

### Weaknesses
- RPO relies heavily on the semantic similarity of prompts to establish contrastive pairs. This approach might limit its effectiveness in contexts where prompts lack clear semantic relationships, especially in diverse general-purpose task datasets. As a result, the probability of relevant prompts appearing within a mini-batch is relatively low, and it is rather difficult to screen out sample pairs of high $\omega$ within a mini-batch. Related to Question 1.
- As an article submitted to ICLR, both the scientific problems distilled in the article and its methodologies are rather deficient in terms of inspiration and theoretical contributions.

### Questions
1. It seems that the performance improvement of this method relative to DPO mainly stems from the combination of additional weighted training samples within the mini-batch, which expands the scale of the training data. Could you please count the proportion of samples with omega > 0.5 in the Anthropic-HH training set under different configurations of batch size?

2. If we construct new sample pairs of relative prompts (i.e. high $\omega$ values) based on the entire dataset and then add them to the original dataset according to the ratio obtained from Question 1, could DPO produce comparable or even better result?

### Soundness
3

### Presentation
3

### Contribution
2
