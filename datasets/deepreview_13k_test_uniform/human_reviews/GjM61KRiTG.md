# Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Fine-tuning large language models (LLMs)  on human preferences, typically through reinforcement learning from human feedback (RLHF), has proven successful in enhancing their capabilities.  However, ensuring the safety of LLMs during the fine-tuning remains a critical concern, and mitigating the potential conflicts in  safety and helpfulness  is costly in RLHF.  To address this issue, we propose a supervised learning framework called \textit{{\oursfull} ({\ours})}, which re-parameterizes a joint RLHF objective of both safety and helpfulness into a single supervised learning objective. In the supervised optimization, a labeling function is used to capture global preferences ranking to balance both safety and helpfulness. To  evaluate \textit{{\ours}}, we  develop a benchmark  including comprehensive discriminative and generative tasks for helpfulness and harmlessness. The results indicate that our method significantly outperforms existing approaches in both safety and helpfulness. Moreover, \textit{{\ours}} eliminates the need for human prompting and annotation in LLM fine-tuning while achieving the same level of safety as methods that heavily rely on human labor, with less than 10\% of the computational resources. The training recipes and models will be released.

\textcolor{red}{Warning: This paper contains offensive or harmful content.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Bi-Factorial Preference Optimization (BFPO) to address the limitations in balancing the helpfulness and safety. Specifically, this paper converts the multi objective RLHF into a modified direct preference alignment, while considering the factor of safety. Through experiments on several alignment datasets including helpfulness and safety, this paper demonstrates the effectiveness of the proposed method.

### Strengths
1. This paper converts the multi-objective RLHF objective into a direct preference alignment paradigm that balances the safety and helpfulness.
2. Derived from existing findings, this paper used the global reward and safety label functions to effectively fine-tune the model towards safety and helpfulness via a supervised learning form. Though the notations part of the method is not clear enough, the theoretical part is mostly correct.
3. The experiments include various datasets to demonstrate the effectiveness of the proposed method in improving the model's safety and helpfulness.

### Weaknesses
1. This paper overclaims that it does not need human annotations. However, the preference datasets used for BFPO still need the annotations. You can't claim it does not need it only because these datasets are publicly available. Otherwise, nearly all methods can claim they don't need any annotations since there likely existed a prepared dataset before. I hope the authors can revise this part.
2. My major concern is about the writing and annotations of the method section. There are many annotations are not well explained and even confusing. For example, Eq. 5 should have more details instead of citing two papers. L347 is also confusing, $\theta$ is the param of the model, what do you mean be softmax it? How do you define the action space? Also, the term of buffered training is confusing, I don't see the connection between it with buffering in RL. It seems like it just sampled two batches from safety and helpfulness datasets.
3. Question: Why don't the authors adopt LoRA or other existing PEFT methods? Freezing the selected layers of LLM for fine-tuning may be not fair for baseline methods, and often need more validation in the experiments. I hope the authors can validate BFPO with LoRA.
4. Question: what's the difference between your label function and the reward model (including helpfulness and safety) used in Llama? Llama uses piecewise function, and should have similar impacts on training the LLM?

### Questions
See the weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a supervised learning framework called Bi-Factorial Preference Optimization (BFPO) for enhancing both the safety and helpfulness of large language models (LLMs). By re-parameterizing the multi-objective reinforcement learning from human feedback (RLHF) approach, BFPO integrates the objectives of safety and helpfulness into a single supervised learning objective. In addition, this paper establishes a benchmark based on existing datasets. The experiments demonstrate a superior balance over safety and helpfulness.

### Strengths
1. This paper proposes an interesting method to fine tune LLM directly on the preference datasets to balance helpfulness and safety. In addition, the justification and theorems provide a solid foundation.

2. Experimental results show superior performance. In the experiment of table 1, results demonstrate better balance between safety and helpfulness.

### Weaknesses
1. The ablation experiments are incomplete. (1) The significant hyperparameter \alpha in the learning objective is only tested in two scenarios: '\alpha=0 only' and '\alpha=0 & no buffer'. However, the setup of \alpha's values in section [3.4 ILLUSTRATIVE EXAMPLES](row 350, \alpha=0.5) and section [4.2 ALIGNMENT WITH BFPO OBJECTIVE](row 394, \alpha=-0.5) differ entirely. This inconsistency prevents a clear understanding of \alpha's true role. (2) The authors do not explore the impact of different values of the hyperparameter \tau, which is also present in BFPO loss function, on the final results.

### Questions
Since two hyperparameters, \tau and \alpha, are included in the loss BFPO, could you conduct experiments with a wider range of values for them to test their impact on the final results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel supervised optimization approach, BFPO, which balances the safety and helpfulness of a large language model by introducing a labeling function. The effectiveness of the proposed method is demonstrated by the evaluation of  constructed benchmark datasets.

### Strengths
1. The proposed Bi-Factorial Preference Optimization (BFPO) method presents a novel approach to balancing safety and helpfulness in the alignment of LLMs. The authors offer a fresh perspective on addressing these often conflicting objectives by integrating direct optimization with multi-objective reinforcement learning principles.
2. BFPO performs well on constructed benchmark datasets and can alleviate the need for manual labeling in LLM fine-tuning.

### Weaknesses
1. Limited Real-World Applicability: The experiments are conducted on a synthetic dataset, which may not reflect real-world complexities. The authors should include experiments on more diverse datasets or practical scenarios to demonstrate the robustness and applicability of BFPO in real-world situations.
2. The paper presentation needs to be improved.

### Questions
1. Could you elaborate on how your method performs in more complex, real-world scenarios beyond the synthetic dataset used in your experiments? What steps would you take to validate the effectiveness of BFPO in such cases?
2. Could you provide more detailed information on the safety and helpfulness labels used in your dataset? How do you ensure the consistency and reliability of these labels?
3. In Section 3, "Equation (7)"  there is no mention of "g(x,y)".
4. While BFPO eliminates human prompting and labeling to some extent, the ability to capture subtle differences in complex human preferences remains questionable.
5. In Table 1 of the experimental results, why does Alpaca perform better for DPO than BFPO?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper propose Bi-Factorial Preference Optimization (BFPO) to learn a single objective of both safety and helpfulness. Specifically, the authors introduce a novel label function that scores preference in terms of both safety and helpfulness, and theoretically prove that solving a supervised optimization problem with the label function is equivalent to solving the multi-objective RLHF with a combination of the rewards of safety and helpfulness. Experimental result shows that BFPO achieves the highest harmlessness score and the best balance between helpfulness and harmlessness.

### Strengths
1. This paper propose a novel approach to align LLMs in terms of both harmlessness and helpfulness, which is essential for AI safety.
2. The proposed label function is theoretically equivalent to the multi-objective RLHF, possessing several properties that offer flexibility when constructing algorithms.
3. The authors conduct extensive experiments to strengthen the soundness of BFPO.

### Weaknesses
1. Some notations are inconsistence or not defined clearly, causing confusions in comprehend Sec. 2 and 3. For example, the reward function is written as $r(x,y)$ in some cases while $r(y|x)$ in others. Similarly, there are $g(x,y)$ and $g(y|x)$. Also, in eq 10 and 11, $y\succ \pi$ is not clearly defined in the main paper. The authors could choose one consistent notation (e.g., $r(y|x)$) and use it throughout the paper, and add a notation table to clarify the meaning of each symbol, including $y\succ \pi$.

### Questions
1. Appendix B.4 only shows that the relationship between $B_1$ and $B_3$ is $B_3(B_1-1)=1$. The authors could include an ablation study or sensitivity analysis to show how the change of these two hyperparameters affect models' performance? 

Typo:
line 222: We remain neutral toward the harmful but unhelpful responses like (c) -> (d)
line 223: ... and we hate the harmful yet exhaustive (helpful) responses like (d) -> (c)

### Soundness
4

### Presentation
3

### Contribution
3
