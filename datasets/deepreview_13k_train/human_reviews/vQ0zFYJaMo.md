# Your Task May Vary: A Systematic Understanding of Alignment and Safety Degradation when Fine-tuning LLMs

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Through supervised fine-tuning or reinforcement learning with human feedback, large language models can achieve a certain level of safety alignment during instruction fine-tuning. However, these *safety guardrails* are often fragile, as models can easily generate harmful content after downstream fine-tuning. Although various methods have been proposed to mitigate this, our paper shifts focus to the durability of safety guardrails, beginning with their formation in the upstream alignment stages. The central question we explore is: *Can we construct more durable safety guardrails for specific downstream tasks to ensure models remain safe after fine-tuning?* Our experiments demonstrate that the durability of these safety guardrails is closely tied to the similarity between upstream and downstream datasets: higher similarity results in more fragile guardrails after fine-tuning, whereas lower similarity results in more durable guardrails. This finding highlights the importance of dataset diversity and privacy in upstream alignment data. Ensuring the diversity of the alignment dataset, which allows downstream datasets to be less similar to it, enhances the guardrail durability for fine-tuning. Maintaining its privacy prevents the exposure of alignment data that adversaries could exploit. Thus, we advocate for a dual strategy: prioritizing both the privacy and diversity of upstream alignment datasets to fortify safety guardrails against potential threats, ensuring long-term model robustness in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors study the relationships between data diversity across different training stages of LLMs and its impact on the ability to weaken safety guardrails. The authors perform experiments on llama 3 architecture and conclude that 1) keeping the training data private may reduce the ability of an attacker to jailbreak the models, 2) higher diversity may also reduce the attacker's ability to jailbreak the models.

### Strengths
- Originality: the paper studies the impact of dataset similarity across multiple stages of training as a possible aspect that could impact the effectiveness of safety guardrails in fine-tuning. I don't know other papers focusing on this aspect.
- Clarity: the paper is clear and well written, with nice diagrams that illustrate the concepts easily. 
- Quality: several empirical aspects limit the scope and validity of the analysis
- Significance: the paper is extremely relevant for the community.  

- The proposed procedure is interesting and could potentially be very useful if the authors demonstrated the generalisability of its assumptions (see weaknesses)

### Weaknesses
 - The conclusion that better safety can be achieved by obscurity about the training data, although very practical, is not a typical recommendation the security community would make. 
- The generalizability of the paper's conclusions is unclear, since the work focuses on very restricted model architectures. The claims need further empirical evidence, it could be good if the authors could include in the rebuttal. Both to study the phenomenon for different architectures and model sizes 
- It is unclear if the conclusions drawn depend on the choice of the jailbreaks. Indeed, an extensive suite of multiple jailbreak benchmarks should be used in order to draw solid conclusions. Furthermore, one would also need to present some adaptive forms of jailbreak generation that do account for the differences in training between models. While even this would not guarantee the absolute generalizability of the conclusions (which would remain a core limitation), it would make a much stronger empirical point. 
- the statements also only hold for the considered guardrails, and it's unclear how well they generalise to other forms of guardrails. 

### Questions
- Could the authors consider using data contamination detection procedures in order to reduce the conjecturality about section 3.1?

### Soundness
2

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
This paper investigates how to make LLMs' safety guardrails more durable after downstream fine-tuning. The authors find that safety guardrails are more fragile when the upstream and downstream datasets are similar but more durable when they are dissimilar and diverse.

### Strengths
1. This paper provides a new insight about the fragility of safety guardrails, which stems from the high similarity between upstream and downstream tasks.
2. Instead of using constraint loss functions, this paper proposes a new direction: data-based approach for fine-tuning attacks.

### Weaknesses
1. The real-world applicability of the findings is questionable. In the experiments, the authors have access to the complete downstream data, yet the safety improvement is modest. According to Table 2, the GPT score is about 0.1 - 0.4 lower than random selection, and the GPT ASR is around 5% lower. This gap is likely to be smaller in real-world scenarios, where downstream data from attackers are not accessible. Furthermore, the study does not address the scenario where an attacker might strategically craft fine-tuning data to maximize the erosion of safety guardrails, which is a more realistic threat model.
2. The paper concludes that low-similarity datasets are more diverse than high-similarity ones, which is intuitively understandable and not a particularly novel or interesting insight. Moreover, the paper does not provide new methods or insights on how to obtain a more diverse safety-alignment dataset. The connection between dataset similarity and diversity, while plausible, lacks rigorous justification. The paper does not explore alternative metrics for diversity or similarity, which could offer a more nuanced understanding of the observed phenomena.
3. The authors should include constraint loss based baselines in their experiments to better demonstrate the effectiveness of data similarity in defending against fine-tuning attacks. Without comparing against established constraint-based methods, it is difficult to assess the practical value of the proposed data-centric approach. The paper also lacks a discussion on the computational cost associated with the proposed method, especially when dealing with large datasets.

### Questions
In table 1, the clustering algorithm is k-means. As we know k-means contains some randomness, are the results in table 1 the average of several runs?

### Soundness
3

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
The paper studies how upstream datasets affect the durability of safety guardrails during downstream fine-tuning in large language models.  The authors conjecture that safety guardrails are more durable when the upstream dataset is more diverse and less similar than the downstream dataset, which is verified using the LLAMA2-7B-CHAT model under various datasets.

### Strengths
The paper shows that a malicious actor can exploit the similarity of upstream and downstream datasets to weaken the safety guardrails. Hence, it is crucial to protect the privacy and improve the diversity of the upstream dataset. This is a meaningful observation with important real-world implications for improving LLM safety.

### Weaknesses
The observation regarding how improving the privacy and diversity of the upstream dataset can help with safety is somewhat expected and has already been recognized in the literature to a great extent. The metrics of similarity and diversity used in the paper are both adapted from recent work. For example, it was observed in He et al. (2024) that selecting benign examples that are most similar to known harmful data can improve the attack success rate significantly. The idea of protecting the privacy of training data to hinder adversarial manipulation is also well known in security and adversarial machine learning communities. 

The evaluation is far from being comprehensive. In addition to the several limitations already mentioned in the paper, including using a single LLM architecture of fixed size, one important weakness is that when evaluating the impact of similarity between upstream and downstream tasks, only the cluster of list-format data is considered. Further, the paper does not consider any defense against downstream fine-tuning attacks. It is unclear if similar results or new insights can be obtained when considering other clusters of similar data or downstream tasks with some defense applied.

### Questions
In Section 4.2, the paper shows that low-similarity data is more diverse than high-similarity data. Why is this always the case? The diversity only concerns the upstream data, while the similarity measure involves both the upstream and downstream datasets.

### Soundness
2

### Presentation
3

### Contribution
2
