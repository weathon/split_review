# ConDS: Context Distribution Shift for Robust In-Context Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
In-context Learning (ICL) is a popular approach to filling Large Language Models (LLMs) with the context without fine-tuning. ICL works by feeding the test input along with the context information selected from the candidate dataset as examples of explaining the target task and getting the answer. In real-world applications, noisy samples are easily to be included in the datasets, so it is unavoidable that the candidate set might contain noise caused by human or measurement errors. The effectiveness of ICL is highly dependent on the quality of the selected ICL samples. Thus the noise in the candidate set can severely mislead the query answer and degrade the ICL performance. However, the noise ICL problem is largely overlooked. To tackle this challenge, in this paper, we propose Context Distribution Shift (ConDS), which iteratively revises the distribution of the candidate dataset so that the retrieved ICL samples are emphasized to improve the robustness of ICL. Specifically, we first identify the informative samples based on the retriever ranking score and the feedback from the LLMs, and then augment the identified informative samples. A subsampling strategy is also adopted to emphasize the importance of informative samples and decrease the size of noisy samples. Thus, ICL's reliability can be improved by reducing the catastrophic impact of noisy samples on almost all test queries to a small percentage. Our ConDS can be easily combined with existing off-the-shelf and fine-tuned retrievers. An analysis is also provided to reveal the relationship between ConDS and retrievers. Experimental results show that ConDS outperforms baselines on various tasks under the influence of noise by a large margin of 8.12\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes **ConDS (Context Distribution Shift)** to enhance the robustness of **In-Context Learning (ICL)** when dealing with noisy samples. The core idea is to modify the distribution of the candidate sample set to amplify informative samples and reduce the impact of misleading samples. The ConDS method primarily consists of the following steps: 1. Identifying Informative Samples: Using feedback from large language models (LLMs) and ranking scores from retrievers to identify information-rich samples within the candidate set. 2. Enhancing Informative Samples: Amplifying Informative samples by duplicating or paraphrasing them, thereby increasing their presence in the candidate set. 3. Subsampling: Conducting subsampling on the enhanced candidate set to control its size and further increase the probability of selecting Informative samples. The paper validates the effectiveness of the ConDS method through experiments on various text classification tasks, with results indicating that ConDS improves ICL performance in the presence of noisy samples. Additionally, the paper analyzes the effectiveness of combining ConDS with different retrievers, and finds that ConDS can be effectively combined with various retrievers.

### Strengths
1. The paper addresses the impact of noisy samples in In-Context Learning (ICL), which is a practical and important issue.
2. The experiment results seem promising. Experimental results show that the ConDS method achieves performance recovery across various text classification tasks, consistently outperforming pure retrieval baselines, in both off-the-shelf and fine-tuned retrievers setting.
3. The paper conducts extensive experiments to validate the effectiveness of the ConDS method, providing detailed analyses of the impact of different parameters.

### Weaknesses
1. **Lack of comparison with other denoising methods**: The paper would benefit from comparing ConDS with other dataset denoising methods.
2. **Insufficient explanations in some places**:  
   - The definitions of "informative samples" and "misleading samples" are vague, lacking a thorough discussion regarding their relationships with clean and noisy samples.
   - The authors introduce the mixed score and assert that it enhances the retriever's ability to select clean samples. However, there is no experimental evidence provided to support this claim. It would be beneficial for the authors to design experiments comparing the impacts of different scoring mechanisms (e.g., using only retriever ranking scores, only sampling probabilities, and using mixed scores) on ICL performance to validate the effectiveness of the mixed score.
3. **Lack of discussion on mathematical assumptions**:  The conditions for applying the hypergeometric distribution in line 273 may need more discussion. ConDS utilizes enhancement and subsampling to modify the size and distribution of the candidate sample set, which does not strictly meet the conditions for sampling without replacement. Furthermore, the retriever does not make binary decisions but instead ranks and selects samples based on scores.
4. **Lack of case studies**:  The paper would benefit from the inclusion of case studies that illustrate the application and effectiveness of the ConDS method in experiment datasets.
5. **Lacks results of larger and more advanced LLMs**:  The experimental conclusions do not encompass larger or more advanced language models. Given that models with varying parameter sizes and training methodologies may yield different ICL results, it would be valuable for the authors to conduct further experiments involving these models to provide a more comprehensive evaluation.

### Questions
1. **Alternative indicators for sample selection**:  Besides LLM answer consistency, what other methods can guide the selection of samples? Have you validated the effectiveness of any other indicators in this context?
2. **Limitations observed in figure 4d**:  In Figure 4d, there are nearly 500 test queries where the clean sample ratio is 0 after applying ConDS. Does this indicate some limitations of the ConDS method? How do you plan to address and overcome these limitations in future work?

Other questions please see above weakness for reference.

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
The paper studies in-context learning (ICL) where the pool of examples includes noisy examples. To address this challenge, the paper proposes ConDS, which focuses on improving ICL robustness. ConDS identifies clean and informative samples based on the validation set, and then removes noisy examples that contribute to negative performance. Experimental results on nine datasets show ConDS's robustness on noisy ICL examples.

### Strengths
The strengths of the paper are outlined below:

- S1)  The paper examines the robustness of ICL, offering new insight for various LLM-based applications.
- S2) ConDS significantly outperforms competing baselines in noisy conditions.
- S3) The motivation is clear, and the paper is easy to follow.

### Weaknesses
The weaknesses of the paper are outlined below:

-  W1) I have some concerns regarding the methodology. ConDS relies on the validation set to classify examples as clean or noisy. However, since the validation set itself may contain noise, this could lead to inaccurate predictions. How do the authors ensure that the feedback from the validation set is reliable?

- W2) The experimental setup and results are unconvincing. The default noise ratio is set to $p=0.6$, which results in the majority of the pool being noisy. In this scenario, it would be reasonable to conduct zero-shot inference using advanced LLMs, such as LLaMA-3, and disregard the noisy pool entirely. However, the authors only test smaller, outdated models like GPT-Neo-2.7B, which do not provide meaningful insights into zero-shot performance. Could the authors present zero-shot results for more advanced models of various sizes?

- W2) ConDS seems to be an extension of PromptPG, which may limit its broader applicability (although ConDS can be combined with other retrievers, its performance is suboptimal). Could the authors elaborate on the unique contributions of this work?

### Questions
Some additional questions/comments are outlined below:

- Q1) Could you further clarify the differences between Sections 3.1 and 3.2? In Section 3.1, you utilize a paraphrasing model, while in Section 3.2, you employ a fine-tuned retriever to define $E_{shift}$. Is this correct and how do the two approaches compare in terms of performance?

- Q2) The paraphrasing model is a T5 model trained on ChatGPT responses. Could you augment the baselines with this model and achieve better performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ConDS, an approach designed to filter noisy in-context examples from a candidate set using LLM feedback—in this case, the prediction of the LLM on a held-out split of the candidate set—to distinguish between noisy and non-noisy examples. The method is straightforward and effective, demonstrating notable improvements over the strongest baseline, PromptPG, evaluated in this study. 

However, it is worth noting that the paper does not address why existing LLM feedback-based filtering methods, which employ similar entropy/perplexity based feedback mechanisms, cannot be directly applied in noisy settings.

### Strengths
1. Demonstrates a significant performance improvement over baselines in noisy settings, showing proposed approach's effectiveness in filtering noisy in-context examples.
2. An additional strength lies in the static approach's simplicity, as it can be seamlessly applied to any in-context pipeline with minimal modifications.

### Weaknesses
1. There is lack of clarity in contextualizing this work against prior studies on filtering in-context demonstrations. Although these existing methods operate in non-noisy settings, many rely on LLM feedback [1,2,3], often in the form of entropy or perplexity, similar to ConDS. Clarifying why such methods are not discussed would be beneficial. [3] originally is applied to find the best order of the prompt but it can potentially be used to provide the weighting of each in-context example in the noisy setting.

2. UDR [4], mentioned in related work, also fine-tunes a retriever based on LLM feedback, yet it is unclear why training a UDR-style model on feedback is not included. Specifically, it is not clear why the retriever cannot be directly fine-tuned using LLM feedback, as UDR does, instead of using ConDS as a post-processing step. This is especially relevant since PromptPG also requires retriever training on the target task.

### Questions
**Questions and Comments**

1. Consider ConE: ConE [3] appears to be applicable for re-weighting the candidate set $C^{\text{train}}$ based on the informativeness of retrieved examples, as different prompts of in-context examples would have higher perplexity. ConDS and ConE share similarities in this respect, but there is no discussion on these parallels.
2. Comparing PromptPG + ConDS with UDR: Based on Lemma 1, how does the combination of PromptPG + ConDS differ from training a UDR-style model on the target task? Since PromptPG + ConDS also requires retriever training on the target task, it would seem that a UDR-like method, which incorporates LLM feedback directly into the retriever's fine-tuning, would serve as a useful baseline.
3. Noise Ratio in Figure 5(a): Why is the maximum noise ratio capped at 0.6? It would be insightful to know if ConDS can filter noise effectively at even higher noise levels, which may align with noisy samples in the validation split of $C^{\text{train}}$.
4. Definition of SCORE($\cdot$): It is not specified what SCORE($\cdot$) represents. Are these similarity scores from the retriever?
5. Static Augmentation with ConDS: Are there results on applying ConDS to PromptPG in the static augmentation scenario? I am assuming that all other values in Table 2 are from the static setting.
6. The term ‘augmentation time’ is confusing, as it actually refers to the number of augmentations after upsampling. Consider renaming it to ‘augmentation size’ or an equivalent term for clarity.

**Typos**
- Line 131: "concatination" → "concatenation"
- Line 533: "as followings" → "as follows"
- Algorithm 1, Lines L6 and L7: Should $q_i$ be $x_i$?

**References**

[1] Demystifying Prompts in Language Models via Perplexity Estimation (Gonen et al., EMNLP Findings 2023)

[2] Revisiting Demonstration Selection Strategies in In-Context Learning (Peng et al., ACL 2024)

[3] Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity (Lu et al., ACL 2022)

[4] Unified Demonstration Retriever for In-Context Learning (Li et al., ACL 2023)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ConDS to handle noisy ICL examples which could be misleading and result in degraded ICL performance. ConDS tackles this by adjusting the distribution of the candidate pool —identifying clean, informative examples through retriever scores and LLM feedback, then boosting them while downplaying noisy ones. The paper also mathematically proved that this process is equivalent to dynamically fine-tuning a retriever. Rather than developing a new retriever, ConDS enhances the data for existing retrievers like BM25, KNN, and fine-tuned ones like PromptPG. The paper’s experiments show ConDS improves performance significantly—by about 8.12%—across various tasks like sentiment analysis and topic classification, particularly in noisy conditions. The key takeaway is ConDS boosts ICL’s reliability by ensuring cleaner samples are used during learning.

### Strengths
The paper introduces a practical approach to improve ICL run-time robustness by adaptively adjusting the distribution of the demonstration pool. This approach is not limited to the choice of example retriever, i.e. off-the-shelf and fine-tuned retrievers can both be integrated, making the system flexible. It also shows overall promising results on several benchmarks (8.1% average performance boost), and especially in noisy data environments.

### Weaknesses
Although the paper recognize a real-world problem - contamination in ICL example pool and developed a practical mitigation strategy, it is still somewhat incremental and I am questionable about it's generalizability. There are lots of other real-world complexities that have not been considered.
1. The datasets assessed here are not very challenging, mostly classification. It's uncertain how this behaves on more challenging use-cases such as text2sql, RAG, plus the binary signal used to distinguish between noisy / informative examples can be hard to generalize on other tasks.
2.  The inference model used here is a fairly out-dated model GPT-neo-2.7B., and whether such method will still be effective towards a more powerful llm is unclear.
3. The "training" stage is not very scalable as the pool size increases and the queries are long.
4. The definition of noise: looking at the noise example provided, the labels are completely irrelevant with the ground truths. In real world scenario, noise can be more nuanced and there lacks of discussion how to handle borderline cases (e.g. when examples are ambiguous)

### Questions
1. Have you tested the transferability across other tasks?
2. How would this approach over-penalize borderline examples that may actually hold some useful contextual information? In complex tasks such as function calling, code generation, maybe the label contents do not match exactly with ground truth, but the formatting can be useful? Also what would happen when the query is challenging and hard to achieve good performance by adding :relevant good examples and those good examples are marked as "problematic" ones?
3. The paper mentions using simple duplication or paraphrasing for augmenting clean examples. Although it might not be the focus of this paper - have you considered other augmentation methods such as adversarial example generation, i.e. adding noise to $x_i^{k}$ in the retrieved example (not $y_i^k$), to not only reduce noise examples but enhance the quality of the informative examples?
4. Regarding scalability, any profiling of training time regarding dataset size and LLM size?

### Soundness
2

### Presentation
2

### Contribution
2
