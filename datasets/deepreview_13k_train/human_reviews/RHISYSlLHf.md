# Upcycling Instruction Tuning from Dense to Mixture-of-Experts via Parameter Merging

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Mixture-of-Experts (MoE) shines brightly in large language models (LLMs) and demonstrates outstanding performance in plentiful natural language processing tasks. However, existing methods transforming LLMs from dense to MoE face significant data requirements and typically rely on large-scale post-training.
In this paper, we propose Upcycling Instruction Tuning (UpIT), a data-efficient approach for tuning a dense pre-trained model into a MoE instruction model.
Specifically, we first point out that intermediate checkpoints during instruction tuning of the dense model are naturally suitable for specialized experts, and then propose an expert expansion stage to flexibly achieve models with flexible numbers of experts, where genetic algorithm and parameter merging are introduced to ensure sufficient diversity of new extended experts.
To ensure that each specialized expert in the MoE model works as expected, we select a small amount of seed data that each expert excels to pre-optimize the router.
Extensive experiments with various data scales and upcycling settings demonstrate the outstanding performance and data efficiency of UpIT, as well as stable improvement in expert or data scaling. Further analysis reveals the importance of ensuring expert diversity in upcycling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose the Upcycling Instruction Tuning (UpIT) method to transform a pre-trained dense model into an MoE instruction tuned model. A primary concern in the standard upcycling approach is how to promote diversity among the experts at the initialization stage to improve results. UpIT achieves this by saving a series of intermediate checkpoints at fixed intervals during the fine-tuning of the dense pre-trained model. These checkpoints are used as initializations for the expert weights, followed by the curation of expert-specific data subsets to pre-optimize routing weights. The final step involves merging all expert models and routing vectors to form the MoE model, which is then fine-tuned on the entire instruction dataset.

The proposed method is implemented for Llama 2 7B and Sheared Llama 2.7B. The authors present the results for different amount of training data, number of Experts, LoRA vs full model training. They also conduct ablation studies on the checkpoint selection, parameter merging, and data selection strategies for router initialization.

### Strengths
- The paper is generally well-written, providing a clear explanation of the UpIT method.
- Introducing MoEs at the fine-tuning stage with limited training data is significant and impactful.
- The ablation experiments offer valuable insights into the method's effectiveness.

### Weaknesses
 - **Expert Diversity:** While the UpIT method enhances expert diversity at initialization, Figure 2's motivation could be more robust. The way the motivation is provided in this figure suggests that different checkpoints excel at different benchmarks. I am wondering to what extend this argument is correct. For example on Factual knowledge, checkpoints saved at 0.25 and 1.5 Epochs have merely identical performance for the MMLU and ARC-e tasks. It also appears that the performance of the model does not improve much across these benchmarks over the fine-tuning stage to indicate the model is focusing on some tasks more than others over the course of training. A stronger case could be made if task interference led to performance drops of some tasks over other tasks during training, suggesting earlier checkpoints might be better for initializing experts whose associated tasks are dominated by other tasks over time.
 
- **Checkpointing Mechanism:** Given its centrality to UpIT, distinguishing the impact of initialization strategy from routing initialization and data selection is crucial. Table 2 suggests that much of the performance gain stems from router initialization. It would be beneficial to assess the effect of the proposed router initialization on other upcycling methods, such as naive upcycling via cloning with noise.

- **Expert Expansion:** The ablation study in Table 2 indicates that the DARE-based expert expansion algorithm does not significantly outperform simply saving more checkpoints. This aspect may not be a substantial contribution to the work.

### Questions
**Routing Distributions:** I find the routing distributions to different experts shown in Fig 5 hard to explain. To my understanding, there is no explicit mechanism during the initialization and MoE training stages that would encourage such an extreme specialization effect. The checkpoints saved at different steps are not specifically task conditional and in practice a vast majority of the samples coming from different benchmarks would be fine across different checkpoints. It is also unlikely that the acquired subsets in $D_s$ are purely task-specific samples. Can the authors provide insight into why this pattern appears?

### Soundness
2

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
This paper proposes UpIT, which aims to initialize MoE more data efficiently. The paper observes the optimal downstream tasks' performance usually happens in different training steps, so they use the checkpoints in different steps to initialize the experts. Furthermore, UpIT also uses model merging to create more experts and create expert-specific data to initialize routers.

### Strengths
The performance of UpIT is better than several baselines on LLaMA2, and the method scale with more data.

### Weaknesses
1. The paper claims the method is data-efficient. However, it is unclear how many samples each method uses during training in Table 1.

2. In Table 2, what would be the results of not using intermediate checkpoints to initialize MoE?

3. The proposed approach contains 3 main components (as shown in Table 2). What is the most important component that contributes to the final performance?

4. Also, UpIT is highly related to "Specialized Upcycling" as the training requires curated expert data. However, none of the baselines belong to specialized upcycling.

5. In line 258, "merging all the expert models" is confusing with the term model "merging" (parameter merging), and in line 258, it seems more like concatenation.

6. The contents in Figure 1 are very small.

7. In Sec 3.1, it would be great to explain the mechanism of each baseline.

8. In lines 8-10 of Algorithm 3, how to choose which bucket to append the data?

9. The idea of using model merging to expand experts is interesting, but the performance improvement is marginal according to Table 2.

### Questions
Please refer to Weakness.

### Soundness
2

### Presentation
2

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
Based on the pilot experiment, which showed that different checkpoints during instruction tuning are inherently suitable for creating specialized experts, they proposed a method that leverages intermediate dense checkpoints for model upcycling. Additionally, to address the issue of routers being randomly initialized after upcycling—leading to token misallocation in the early post-training stage—they introduced a data selection strategy to curate expert-specific datasets tailored to each expert model and pre-optimize additional routing vectors to enhance differentiation among experts. They demonstrated the effectiveness of their methods on various benchmarks, outperforming other upcycling baselines in LoRA-based and FFN-based upcycling settings.

### Strengths
1. The writing is clear, and they provide sufficient supplementary information to help readers easily understand the algorithm.
2. Their findings from the pilot experiment somewhat support their motivation for using the intermediate checkpoints.
3. They demonstrated the effectiveness of their methods on several benchmarks.

### Weaknesses
1. Looking at Figure 2, it appears that, across intervals, there is not much difference in performance for certain benchmarks. Therefore, the authors' claim that checkpoints saved at regular intervals can be considered specialized experts seems somewhat exaggerated. Specifically, the y-axis scale in Figure 2 makes it difficult to discern meaningful performance variations between checkpoints for some tasks; a more granular analysis, perhaps with separate plots or a different visualization, would be beneficial to support the claim of specialization. The lack of clear performance deltas raises concerns about the actual diversity of the 'experts' being created.
2. It is unclear whether the same pattern would be observed with datasets other than the training dataset used in the paper. In other words, it needs to be verified if using checkpoints from different intervals for upcycling generalizes well across a variety of datasets. The reliance on a single dataset for demonstrating the specialization of intermediate checkpoints limits the generalizability of the findings. It is crucial to assess whether the observed performance variations are consistent across diverse datasets, or if they are specific to the dataset used in the experiments. The absence of such validation raises concerns about the robustness of the proposed method.
3. In addition to explaining how they select checkpoints when the number of saved checkpoints exceeds the required number of experts, studying the impact of saving checkpoints at different intervals during dense model training could further enhance the robustness of the proposed method. The paper does not explore the impact of checkpoint saving frequency on the quality of the resulting experts. The current approach of saving checkpoints at regular intervals might not be optimal, and a more systematic investigation of different saving intervals could reveal more effective strategies for expert preparation. This could involve varying the intervals based on training progress or other criteria, which could lead to more diverse and effective experts.

### Questions
1. Regarding the expert preparation process, how do we determine the appropriate interval for saving checkpoints? Is this solely based on heuristic methods?
2. In the expert expansion process, the two models with the greatest discrepancy are selected for merging. In this case, wouldn't this mostly result in the selection of checkpoints from the early and late stages of training?
3. How is the similarity between the two experts calculated?
4. During the training of the dense model, the training data was randomly sampled. What would happen if this approach was not used?

### Soundness
2

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
This paper introduces "Upcycling Instruction Tuning" (UpIT), a novel and data-efficient method for converting dense pre-trained language models into a Mixture-of-Experts (MoE) model. UpIT leverages intermediate checkpoints from the dense model’s instruction-tuning phase to create specialized "experts" and employs a genetic algorithm for expert expansion to maintain diversity and flexibility in expert numbers. Additionally, it uses a router initialization step to optimize the model’s token routing, allowing each expert to excel in designated tasks. Compared to traditional methods, UpIT significantly reduces data requirements while improving performance, scalability, and stability in MoE models across various natural language processing benchmarks. The paper’s extensive experiments validate UpIT's effectiveness, particularly in low-data scenarios and when scaling expert counts, highlighting the importance of expert diversity for efficient model upcycling.

### Strengths
1. The paper is well-organized and clearly written, which is very easy to follow.
2. The proposed method is reasonable: by specializing a few experts and further merging and mutating into new ones.
3. The authors provided comprehensive experiments.

### Weaknesses
 **Ablation Study on Hyperparameters m and n in Algorithm 2**: The lack of an ablation study comparing values of m and n (step 1 in Algorithm 2) leaves an important gap in understanding how to control expert diversity and scalability in expert merging. This comparison is likely critical, as it would shed light on the trade-offs involved in selecting these hyperparameters, such as the extent of expert specialization versus computational efficiency. Providing guidance on optimal values for different model sizes and data conditions would greatly assist practitioners in fine-tuning their model configurations.



### Questions
1. **Specialized Expert Preparation and Data Distributions**: How can we ensure that the preparation of specialized experts (step 2 in Algorithm 1) effectively captures diverse expertise, especially when data distribution is varied? While Figure 3 only considers different scales of training data, it would be insightful to evaluate how experts perform with data that varies not only in size but also in domain or content distribution. Would experts trained on domain-specific or contextually diverse subsets offer improved performance or encounter challenges in maintaining consistent expertise?

2. **Forgetting Issues in Expert Specialization**: When specializing the dense model into distinct experts using diverse datasets, some experts may experience different levels of forgetting, particularly for knowledge outside their specialized domain. Would it be beneficial to retain a copy of the original dense model throughout the expert expansion process to mitigate potential knowledge loss? Retaining this copy might help rebalance the model’s general knowledge base, especially if certain experts regress on commonly shared tasks.

### Soundness
3

### Presentation
3

### Contribution
3
