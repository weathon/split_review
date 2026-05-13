# Can Watermarks be Used to Detect LLM IP Infringement For Free?

- Decision: Accept
- Scores: 6, 6, 5, 6, 6

## Abstract
The powerful capabilities of LLMs stem from their rich training data and high-quality labeled datasets, making the training of strong LLMs a resource-intensive process, which elevates the importance of IP protection for such LLMs. Compared to gathering high-quality labeled data, directly sampling outputs from these fully trained LLMs as training data presents a more cost-effective approach. This practice—where a suspect model is fine-tuned using high-quality data derived from these LLMs, thereby gaining capabilities similar to the target model—can be seen as a form of IP infringement against the original LLM. In recent years, LLM watermarks have been proposed and used to detect whether a text is AI-generated. Intuitively, if data sampled from a watermarked LLM is used for training, the resulting model would also be influenced by this watermark. This raises the question: can we directly use such watermarks to detect IP infringement of LLMs? In this paper, we explore the potential of LLM watermarks for detecting model infringement. We find that there are two issues with direct detection: (1) The queries used to sample output from the suspect LLM have a significant impact on detectability. (2) The watermark that is easily learned by LLMs exhibits instability regarding the watermark's hash key during detection. To address these issues, we propose LIDet, a detection method that leverages available anchor LLMs to select suitable queries for sampling from the suspect LLM. Additionally, it adapts the detection threshold to mitigate detection failures caused by different hash keys. To demonstrate the effectiveness of this approach, we construct a challenging model set containing multiple suspect LLMs on which direct detection methods struggle to yield effective results. Our method achieves over 90\% accuracy in distinguishing between infringing and clean models, demonstrating the feasibility of using LLM watermarks to detect LLM IP infringement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose LIDet, a novel method designed to detect whether an LLM has been fine-tuned using the outputs of another LLM, potentially causing IP infringement. The approach assumes that the source LLM’s generated outputs are watermarked and that a suspect model is fine-tuned on them.  Based on this and assuming that the suspect model has learned this watermarked distribution of data, the method uses a set of anchor LLMs to select appropriate queries for sampling from the suspect model. It then detects watermarks in the suspect's generated text using an adaptive threshold based on z-scores. The authors evaluate the method with different models and datasets, proposing an analysis and ablation study of LIDet based on different watermarking methods.

### Strengths
•	The authors propose an evaluation of the method with data from different domains.

•	The authors evaluate the performance of the detection method with different watermarking techniques.

•	The authors propose a clear and precise problem statement and threat model.

### Weaknesses
•	The paper lacks in the comparison of LIDet with other methods in the state of the art.

•	The Results section (4.2) does not provide sufficient details on the performance of the different anchor models considered in LIDet.

•	The authors do not propose an evaluation of the method using different combinations of original and suspect models. 


**Comments.**

1.	In the related works, the authors cite the work in [1] which proposes another method to detect LLM watermarks from the suspect model tuned with watermarked texts. The authors did not propose a comparison of LIDet with this method, even though it attempts to solve the same type of problem. Although the threat model is slightly different, the author could have proposed a comparison with [1] in Table 3 when the Query for Detection follows the same distribution as the Query for Training, i.e., i.i.d. detection queries as considered in [1].

2.	In the first step of the detection method, the authors propose to sample a set anchor LLMs $\theta_{\rm anchor}^M$ used to help select the proper queries to sample the suspect LLM. As presented in the paper, the set of anchor models presents the same model architectures as the source model, however, there is no discussion on how to select the right set of anchor models, nor is there any insight into which anchor model contributes the most to the selection of the final set of queries. The paper does not present any ablation on the number of anchor models or on the type of model architectures.

3.	In addition to that, the authors considered only the scenario where Llama2 and Llama3 models are used as source and anchor models, but not as suspect models. There is no analysis of LIDet's performance when the suspect and source models are derived from the same base model. Similarly, the authors did not provide any analysis of the method using different model architectures as source models, e.g. Mistral.

### Questions
•	Do you think LIDet performs better than [1]? Could you provide a comparison of the two methods?

•	Should the set of anchor models always contain the same source model architecture?

•	Do you think the suspect model's dimension (number of parameters) could affect the performance of the method?

•	Do you think there is a correlation between the detectability of the watermarks and the domain of the datasets considered in the queries used to train the suspect model?

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
2

### Summary
This paper studies the problem of Model IP infringement for LLMs. The authors propose to use different anchor LLMs to select query samples that are more likely to contain more diverse and evenly distributed tokens, which are useful for later detection. Furthermore, for the detection phase, it uses dynamic thresholding for the z-score-based detection methods. The empirical results show the significant detection performance compared to the baselines.

### Strengths
1. The structure of the paper is good that, it first empirically identifies the vulnerabilities of existing watermarking scheme for text or models.
2. The empirical performance is strong.

### Weaknesses
1. The evaluation settings rather limited and only contains two domains and also did not consider the fact that, if the target domain is a mixture of multiple domains (e.g., math and code). The paper can benefit from a more comprehensive evaluations that mixes multiple domains. 
2. The threat model is still unclear to me. Even though the different types of downstream applications exist, the the source model trainer should still have some general understanding about the high-level domains that are involved in the training set. Therefore, even for the vanilla approach, generating some possible responses from each of these high-level domains is a possible (and potentially stronger) baseline.

### Questions
As the paper is mostly an empirical paper, I would suggest making the evaluations more comprehensive. The detailed suggestions for comprehensive evaluations are listed in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To distinguish the AI-generated texts from human-produced ones, watermarking is added over generated texts, by using green-and-red list and adding bias to the logits of different tokens. In this paper, the authors exploit this text watermark to detect whether a new model $M_a$ is finetuned over the texts generated from a well-trained model $M_b$. Ideally, if $M_a$ is totally trained over the texts generated from $M_b$, the outputs of $M_a$ satisfy the same bias as $M_b$, so that the detector can detect the output of $M_a$ to determine whether the IP of $M_b$ is violated or not. However, in the realistic situation, there exist the domain mismatch and green ratio mismatch between $M_a$ and $M_b$, which leads to the failure of the detection. The authors proposed a new method called LIDet to detect whether $M_a$ is finetuned over the $M_b$-generated data.

### Strengths
1.	Clear definition of threat model to show the capability of stealer and detector.
2.	Scrutiny the reasons on the attenuation of watermark detection: domain mismatch and green ratio mismatch.

### Weaknesses
Lack of adaptive attack: The authors only assume that the stealer will directly finetune $M_a$ over the queried data, and fail to exploit the adaptive attack. For instance, if the stealer knows the queried data including the watermark, he/she could modify the queried texts to remove the watermark. By this way, the finetuned model $M_a$ may not learn the bias. From another perspective, the stealer can even finetune the $M_a$ without the data from $M_b$, but mimic the same bias as $M_b$ to increase the FPR of LIDet. This mimicry attack is a significant concern, as a sophisticated adversary could potentially train a model to exhibit the same statistical biases as the watermarked model without actually using its data. This could involve analyzing the token distributions of the victim model's output and training a new model to replicate these distributions, thus circumventing the detection mechanism. The feasibility and resource requirements of such an attack are not sufficiently addressed, and it is unclear how robust the proposed detection method is against this type of sophisticated mimicry.

### Questions
NA

### Soundness
2

### Presentation
2

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
This paper investigates using watermarks in large language models (LLMs) to detect intellectual property (IP) infringement. It identifies two key issues with direct watermark detection: the impact of sampling queries on detectability and the instability of watermark hash keys. To address these, the authors propose LIDet, a method that selects suitable sampling queries and adapts detection thresholds. Experimental results show LIDet achieves over 90% accuracy in distinguishing between infringing and clean models, demonstrating its effectiveness for detecting LLM IP infringement.

### Strengths
1. The paper is well-written, with clear logic and organization that makes it easy to follow.
2. The experimental results appear promising, demonstrating the proposed method's effectiveness in distinguishing between infringing and clean models.

### Weaknesses
1. Evaluation of Time/Computational Costs: The experimental section lacks an assessment of the time and computational costs involved. It should evaluate the number of queries required for effective detection, as this is crucial for understanding the practicality of the proposed method. Specifically, the paper should analyze the relationship between the number of queries, the number of tokens per query, and the resulting detection accuracy. This analysis should consider the trade-off between detection performance and computational overhead, providing a clear picture of the resource requirements for real-world deployment.
2. Transferability of the Approach: The paper does not adequately address how the proposed method, LIDet, can be applied to other models. Clarifying the conditions under which the method retains its effectiveness across different architectures would strengthen the contribution of the work. The paper should investigate the sensitivity of LIDet to variations in model architecture, such as the number of layers, attention mechanisms, and embedding dimensions. Furthermore, it should explore whether the method requires retraining or fine-tuning when applied to a new model, and if so, what the computational costs are.

### Questions
(1) Please evaluate the number of queries required for effective detection and present the results obtained using varying numbers of queries.

(2) It is recommended to conduct experiments using models other than Mistral-Instruct-7b as the base model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes using watermarking to detect IP infringement in large language models (LLMs). The proposed method, LIDet, improves detection accuracy by addressing domain mismatch and watermark stability through adaptive thresholding and optimized query selection based on token entropy and generalizability. Experiments show that LIDet achieves high reliability in distinguishing between infringing and non-infringing models, enhancing LLM protection.

### Strengths
The proposed approach in this paper leverages watermarking as a novel method to detect IP infringement in large language models (LLMs), providing a robust layer of protection against unauthorized replication. The proposed detection method, LIDet, tackles key challenges such as domain mismatch and stability issues through adaptive thresholding and a targeted query selection strategy. By focusing on token entropy and cross-model generalizability, the proposed query strategy ensures more reliable detection, reducing false positives and achieving high accuracy across various settings.

### Weaknesses
The paper could benefit from further exploration of the impact of watermarking on overall model performance, including metrics such as perplexity, BLEU scores, or human evaluations to assess any trade-offs in output quality and diversity. Specifically, the analysis should consider how the introduction of watermarks affects the model's ability to generate coherent and contextually relevant text, and whether the watermarking process introduces any biases or limitations in the generated content. Additionally, while candidate queries are selected for high token entropy and cross-model generalizability to ensure that infringing models retain watermark patterns, the detection reliability may vary if infringing models do not fully absorb specific watermarked phrases. This is particularly concerning if the infringing model is trained on a relatively small amount of watermarked data, or if the watermarking scheme is not robust enough to withstand fine-tuning or other model modifications. Testing detection on models trained with varying amounts of watermarked data, and with different fine-tuning strategies, could clarify this absorption. Lastly, the “anchor LLM” method aims to reduce false positives by selecting queries with favorable green ratios and entropy, but there is still a risk that unwatermarked models could unintentionally exceed detection thresholds. This risk is heightened by the fact that natural language can exhibit statistical patterns that might coincidentally align with the watermarking scheme. Analyzing the false positive rate across a broader set of non-infringing models, under various conditions and across diverse datasets, would provide a more comprehensive understanding of the method’s specificity, and would help to determine the practical applicability of the proposed approach.

### Questions
1. If two models are trained on overlapping open-source datasets, will the false positive rate significantly increase? Shared data could lead to misclassification of non-infringing models as infringing ones.
2. How does watermarking affect the model’s performance—does it enhance or degrade output quality? It’s essential to evaluate whether watermarks could unintentionally reduce the overall effectiveness of the model's generation capabilities.
3. How can candidate queries effectively ensure that the infringing model has learned specific watermark phrases? If the infringing model has not learned the intended watermarked phrases, can these queries reliably retrieve them?
4. How can we ensure that the responses retrieved through queries are indeed related to the watermark? Some models may unintentionally produce watermarked phrases simply through regular training, which could lead to inadvertent misclassifications.

### Soundness
3

### Presentation
3

### Contribution
3
