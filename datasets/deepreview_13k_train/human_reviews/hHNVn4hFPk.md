# Compress then Serve: Serving Thousands of LoRA Adapters with Little Overhead

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Fine-tuning large language models (LLMs) with low-rank adaptations (LoRAs) has become common practice, often yielding numerous copies of the same LLM differing only in their LoRA updates. This paradigm presents challenges for systems that serve real-time responses to queries that each involve a different LoRA. Prior works optimize the design of such systems but still require continuous loading and offloading of LoRAs, as it is infeasible to store thousands of LoRAs in GPU memory. To mitigate this issue, we investigate the efficacy of model compression when serving LoRAs. We propose a method for joint compression of LoRAs into a shared basis paired with LoRA-specific scaling matrices. We extend our algorithm to learn clusters of LoRAs that are more amenable to joint compression, allowing it to scale gracefully to large LoRA collections.
Our experiments with up to 500 LoRAs demonstrate that compressed LoRAs preserve performance while offering major throughput gains in realistic serving scenarios with over a thousand LoRAs, maintaining 80\% of the throughput of serving a \emph{single} LoRA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method to accelerate multi-LoRA serving by jointly compressing multiple LoRAs together. They use a method that shares a basis and then rescales the basis to represent different LoRA adapters. They also extend their method to group clusters of LoRAs together which are more amenable to joint compression, and leverage an alternating assignment algorithm to optimize the cluster assignments and compressed LoRA representations. This method allows for storing a large number of LoRAs more compactly in memory, and also serving these adapters with significantly lower costs than existing LoRA serving systems.

### Strengths
- They present a novel joint compression approach for multi-LoRA serving that compresses together LoRAs using a joint diagonalization method (which projects groups of LoRAs onto a shared basis)
- They propose a clustering-based approach that groups together similar LoRAs (which are more amenable to shared basis compression) and then alternates cluster assignment with joint compression. This is necessary for compressing large numbers of LoRAs together without significant accuracy degradation. 
- They provide theoretical error bounds on the reconstruction error from their method
- They also provide comprehensive evaluation for their method

### Weaknesses
 - This approach relies on having well-clustered LoRA adapters for high attainable compression
- For multiple users who want to use LoRA-as-a-service, it seems unlikely that they would want the accuracy of their fine-tuned model to be dependent on the other LoRAs that are included in the batch (or to have the behavior of their model be influenced by the other LoRAs that their adapter is grouped with).
- For the throughput improvements, this work relies on the assumption that the LoRAs that are used together are consistent for throughput benefits (as if there are changes in terms of which LoRAs are being used heavily with a dynamic workload, then the throughput benefits would be more limited). Have the authors considered evaluating their method under dynamic workloads in order to assess whether the throughput benefits are comparable, or considered the implications of how their method could be applied in such a scenario?
  - For edge deployment (with one base model and many downstream task adapters), this approach would help significantly in terms of memory savings; however, for these applications there would be no throughput / latency benefits.
- Are there any privacy concerns with this type of approach? It would be useful if the authors could provide an analysis of privacy implications of their joint compression approach (specifically, whether it is possible for joint compression to leak any information).
  - Do the authors have any ablation for the following: given the base model with adapter A for task T_A which has been jointly compressed with adapter B for task T_B, does the base model with adapter A now inadvertently perform better on task T_B, or does it maintain its "independence" in the sense that the compressed A adapter hasn't been leaked information from adapter B?
- I didn't understand the connection to LoRA merging at the end of Section 4, and how this supports the claims of the paper. Intuitively, I don't think that averaging adapters is actually a desired property (since it means that each adapter that you add in would bias the other adapters to be more similar to the added adapter). It would be helpful if the authors could clarify in the rebuttal what the intended implications are with the LoRA merging comparison.
- One minor point is that I found the evaluation hard to follow - this may be because there are multiple moving parts (number of LoRAs, rank, number of clusters, different "full" / "diagonal" variants of their method) which makes it hard to present results.

### Questions
- Are there any privacy concerns with this type of approach? It would be useful if the authors could provide an analysis of privacy implications of their joint compression approach (specifically, whether it is possible for joint compression to leak any information).
  - Do the authors have any ablation for the following: given the base model with adapter A for task T_A which has been jointly compressed with adapter B for task T_B, does the base model with adapter A now inadvertently perform better on task T_B, or does it maintain its "independence" in the sense that the compressed A adapter hasn't been leaked information from adapter B?
- I didn't understand the connection to LoRA merging at the end of Section 4, and how this supports the claims of the paper. Intuitively, I don't think that averaging adapters is actually a desired property (since it means that each adapter that you add in would bias the other adapters to be more similar to the added adapter). It would be helpful if the authors could clarify in the rebuttal what the intended implications are with the LoRA merging comparison.
- One minor point is that I found the evaluation hard to follow - this may be because there are multiple moving parts (number of LoRAs, rank, number of clusters, different "full" / "diagonal" variants of their method) which makes it hard to present results.

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
3

### Summary
This paper presents a method for compressing low-rank adaptations (LoRAs), which is a common technique used in parameter-efficient fine-tuning. The main idea is to jointly diagonalize the set of LoRA matrices, which allows sharing parameters across multiple LoRAs and reducing the overall number of parameters. The authors also propose a clustering algorithm to improve reconstruction error by grouping similar LoRAs together. They evaluate their approach on a variety of natural instruction tasks and demonstrate that their compression techniques preserve the performance of the original LoRAs while maintaining high throughput when serving over 1000 LoRAs.

### Strengths
● The proposed joint diagonalization method is well-motivated and theoretically justified. 
● The clustering algorithm helps improve the compression efficiency. 
● Experimental results show that the proposed method can achieve high throughput while preserving performance.

### Weaknesses
1. The paper mentions that F-LoRA and S-LoRA are related methods, but it doesn't explicitly compare them with the proposed joint diagonalization method. Including a comparison with these and other state-of-the-art methods could highlight the advantages and disadvantages of the proposed method relative to existing solutions.

2. There are some doubts about the specific experimental results, as the model's performance improvement is not clearly addressed. The compression used here is lossy and cannot fully restore the original model's performance. Furthermore, there is a lack of comparative experiments to demonstrate whether the model's performance after compression maintains its efficacy or accuracy compared to the original. These aspects require more detailed data and experimental results for support.

### Questions
To fully understand the computational requirements of the proposed method, it's essential to evaluate several factors including the complexity of the algorithms used, the types and sizes of the datasets involved, and the specific hardware configurations required.

Regarding latency and resource usage:
- Latency: The method's impact on latency should be assessed by comparing the time it takes to process tasks with and without the use of the proposed method. This will reveal if there's an increase in processing time or if the method helps reduce delays typically associated with computation.
- Resource Usage: Analyzing resource usage involves looking at how much CPU and GPU time is required, the memory footprint, and whether the method optimizes or increases the demand on these resources. Additionally, it would be beneficial to compare the resource consumption with that of other existing methods to determine its efficiency.

For a comprehensive evaluation, you might consider setting up experiments that measure these metrics under controlled conditions, ensuring you can directly observe the impacts and effectively compare them with other techniques.

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
This paper addresses the pressing challenge of efficiently serving a large number of low-rank adaptation (LoRA) adapters in real-time systems. The authors propose a novel Joint Diagonalization (JD) method that combines multiple LoRA adapters' weights into shared matrices, significantly reducing the storage and computational overhead required for inference. The experimental results demonstrate that this approach maintains model performance while enhancing throughput, particularly in scenarios involving thousands of adapters.

### Strengths
- The paper tackles a critical and timely issue in deploying large-scale machine learning models, particularly in real-time applications. The need to serve numerous LoRA adapters efficiently is a relevant concern in the field.
- The proposed JD method is a novel approach that leverages shared matrices to compress multiple LoRA adapters effectively. This innovation contributes significantly to the field of model compression and efficiency.
- The authors provide solid experimental evidence supporting their claims. The results illustrate that the proposed method effectively retains performance while significantly improving throughput, which is crucial for practical implementations.
- The introduction of a clustering strategy to handle LoRA adapters with varying ranks demonstrates a thoughtful extension of the core methodology, allowing for greater flexibility and scalability in real-world applications.

### Weaknesses
 - The experimental section of the paper utilizes a uniform rank for the LoRA method across all fine-tuning tasks, demonstrating that this approach can achieve lower reconstruction loss. However, in current multi-LoRA deployment systems, the required rank values often vary significantly across different tasks. When there is a substantial disparity in the rank values of different LoRA modules, the method presented in this paper may be less effective. Although it is feasible to stratify LoRA parameters of varying ranks into different groups using clustering methods, the advantages of doing so may be limited. Specifically, the paper does not address the scenario where a few LoRAs have very high ranks while the majority have low ranks, which could lead to inefficient compression if high-rank LoRAs dominate the shared matrices.
- Several efficient fine-tuning methods with shared parameters have been proposed to reduce the parameter count in LoRA. For instance, VeRA [1] suggests fine-tuning a large language model by sharing global static parameters while setting local scaling variables. In a multi-LoRA deployment environment, VeRA naturally incorporates shared parameters and does not require additional computation to extract these shared parameters from different LoRAs. Using VeRA for fine-tuning eliminates the need for an additional computational process for shared parameter extraction, while also avoiding the introduction of errors. Furthermore, VeRA supports LoRAs with varying rank values without relying on clustering methods. In contrast, the JD method may introduce some reconstruction errors and necessitate additional computations, lacking a clear advantage. The paper should also consider methods like adapter fusion, which directly combines parameters, and compare against them.
- The experiments conducted in the paper utilize only the Mistral-7B-Instruct-v0 base model, which does not sufficiently demonstrate the applicability of the proposed method to other base models, such as those in the Llama series. Additionally, the experiments do not account for larger-scale models (e.g., 13B and 70B), which leaves unverified the effectiveness of the method in the context of large-scale models. The paper should include results on a variety of model sizes and architectures to show the generalizability of the method, as the performance could be impacted by the model's architecture and scale.
- The clustering methodology described lacks specific details. The paper mentions the use of clustering algorithms like k-means but does not elaborate on how different LoRA parameters are clustered or how the number of clusters is determined. Providing more detailed information on these aspects would significantly enhance the clarity and rigor of the methodology. For example, it is unclear if the clustering is performed on the flattened LoRA matrices or on some other representation, and how the distance metric is chosen for clustering.

### Questions
- The experimental section of the paper reports training LoRA on 500 distinct types of tasks. However, it is currently unclear what the primary categories of these tasks are and whether there is a high degree of task similarity. If there is a high similarity among the tasks, it is hypothesized that the resulting LoRA parameters may also be more similar, potentially leading to lower reconstruction loss. It would be beneficial to explore whether this is the case and to discuss how the reconstruction loss might compare when tasks are less related or entirely dissimilar.
- The paper introduces two distinct methods, JD-Full and JD-Diag. It is crucial to analyze under what scenarios each method is more suitable. Are there experimental comparisons that indicate which method achieves lower reconstruction loss in scenarios with higher ranks or with a larger number of clusters? Providing such analysis would significantly enhance the understanding of when and where each method is most effective.
- Regarding Figure 2, data is only presented for 0-100 and 500 LoRA instances, with other quantities left unfilled. It would be valuable to understand if there are any trends or patterns that emerge with different numbers of LoRA instances. Clarifying this would provide a more comprehensive understanding of the relationship between the number of LoRA instances and the associated outcomes.

### Soundness
4

### Presentation
4

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
This work proposes a new approach to compress multiple LoRAs together to reduce the frequent CPU-GPU swapping when serving multiple LoRAs with the same base model (like S-LoRA). The essential technique is an SVD-like compression algorithm that decomposes multiple LoRAs simultaneously. To further support more LoRAs, a clustering-based approach is devised, which groups LoRAs into different clusters and apply the SVD-like compression within each group. The authors trained 500 LoRAs across different tasks to evaluate the effectiveness, including the task performance (in terms of validation metrics) and serving efficiency (in terms of serving throughputs).

### Strengths
This work studies a timely and important problem. How to serve multiple LoRAs more efficiently can help us move towards better personalization of foundation models. The authors made extensive efforts to train LoRAs over 500 tasks, which, from my humble opinion, may be valuable to the community.

### Weaknesses
Despite the significance in the studied topic and the self-trained LoRAs, the technical depth of this work seems rather shallow. There are many important experiments lacking, and the authors should go deeper in when is each proposed technique suitable and effective. Please see questions below.

1. To motivate this work, I suggest the author conduct a detailed breakdown to show how much time (and ratio to end-to-end inference) is taken to load the LoRAs.

2. There lacks the time cost about the compression in the experiments. Besides, there are no discussions or experiments demonstrating how much the memory reduction is after applying compression. Please add experiments to show the compression time as well as the memory usage before and after compression, under different numbers of LoRAs.

3. After applying the compression, the computation also differs. It would be nice to see how this approach affects the computation cost of LoRAs (e.g., via a detailed breakdown of the inference time).

4. In addition to the tradeoff between task performance and reconstruction error (Figure 3), I believe showing the tradeoff between task performance and serving efficiency is more essential to practical uses. In other words, when compressing more LoRAs together, we could achieve better serving efficiency, while the task performance goes down. An in-depth study would be nice to have.

5. Based on the experimental results, it is hard to tell which approximation (i.e., JD-Full and JD-Diag) is better and how the number of clusters should be configured. It would be better to conclude a few takeaways to improve the practicality of the proposed techniques.

6. As an extension, I would like to see discussions about how this work could apply to larger models. In particular, when the base model is larger (e.g., over 100B), the portion of memory consumption of LoRAs should be smaller. Then, how would the effectiveness of this work becomes?

7. Minor comment: Punica (https://arxiv.org/abs/2310.18547), another work about multi-LoRA serving, is not mentioned.

### Questions
1. To motivate this work, I suggest the author conduct a detailed breakdown to show how much time (and ratio to end-to-end inference) is taken to load the LoRAs. 

2. There lacks the time cost about the compression in the experiments. Besides, there are no discussions or experiments demonstrating how much the memory reduction is after applying compression. Please add experiments to show the compression time as well as the memory usage before and after compression, under different numbers of LoRAs.

3. After applying the compression, the computation also differs. It would be nice to see how this approach affects the computation cost of LoRAs (e.g., via a detailed breakdown of the inference time).

4. In addition to the tradeoff between task performance and reconstruction error (Figure 3), I believe showing the tradeoff between task performance and serving efficiency is more essential to practical uses. In other words, when compressing more LoRAs together, we could achieve better serving efficiency, while the task performance goes down. An in-depth study would be nice to have.

5. Based on the experimental results, it is hard to tell which approximation (i.e., JD-Full and JD-Diag) is better and how the number of clusters should be configured. It would be better to conclude a few takeaways to improve the practicality of the proposed techniques.

6. As an extension, I would like to see discussions about how this work could apply to larger models. In particular, when the base model is larger (e.g., over 100B), the portion of memory consumption of LoRAs should be smaller. Then, how would the effectiveness of this work becomes?

7. Minor comment: Punica (https://arxiv.org/abs/2310.18547), another work about multi-LoRA serving, is not mentioned.

### Soundness
2

### Presentation
3

### Contribution
2
