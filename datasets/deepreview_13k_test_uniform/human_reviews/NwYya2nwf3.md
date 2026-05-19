# ExpertZIP: A Progressive Fusion Framework for Mixture-of-Experts Model Optimization through Huffman Tree Structures

- Decision: Reject
- Scores: 6, 3, 5, 6, 6

## Abstract
Mixture-of-Experts (MoE) models have gained attention as a novel approach to developing large language models (LLMs), praised for their ability to enhance performance by utilizing multiple experts. However, while increasing the number of experts in these models can yield performance gains, it also introduces significant trade-offs, such as substantial memory overhead and increased inference time, limiting their scalability and practical deployment. In this work, we conduct a thorough analysis of expert utilization and identify inefficiency: many experts are underutilized, leading to suboptimal resource allocation with limited improvement. To address this issue, we propose ExpertZIP, a progressive framework for MoE models that leverages a Huffman tree-based expert fusion technique. This progressive approach systematically merges underutilized experts step by step, ensuring their essential contributions are maintained while drastically reducing memory usage and computational demands. Our approach yields a 17.23x reduction in model size and a 4.84x improvement in inference time, with only a 1.18\% decrease in average accuracy compared to the original 64-expert Switch Transformer model. Moreover, it demonstrates a 6.47\% increase in accuracy relative to models with an equivalent number of experts. These results demonstrate that our optimized framework provides performance on par with larger models, offering an efficient solution for resource-constrained and real-time applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to optimize Mixture-of-Experts (MoE) models by reducing the number of experts through a progressive fusion technique based on Huffman tree structures. The authors claim that their method, ExpertZIP, addresses the inefficiency of underutilized experts in MoE models, leading to significant reductions in model size and inference time while maintaining performance. The paper reports a 17.23x reduction in model size and a 4.84x improvement in inference time with only a 1.18% decrease in average accuracy compared to the original 64-expert model. The approach is evaluated on classification and summarization tasks, demonstrating its effectiveness and efficiency, which is especially suitable for resource-constrained and real-time applications.

### Strengths
1. The use of Huffman tree structures for expert fusion in MoE models is a creative solution to address the problem of underutilized experts.
2. The paper demonstrates substantial improvements in model size and inference time, which are critical for deploying large language models in practical applications.
3. The authors provide extensive experimental results to validate their approach, including comparisons with original MoE models and other fusion strategies.
4. ExpertZIP shows consistent performance across a variety of NLP tasks, indicating its broad applicability.

### Weaknesses
1. The paper could provide more details on the complexity of implementing the ExpertZIP framework, especially for readers who may not be familiar with Huffman trees.
2. More SOTA MoE models could be tested to prove the robustness of the ExpertZIP framework, such as DeepseekMoE.

### Questions
1. The Switch Transformer appears to select only the top 1 expert for each input, which suggests that the computational complexity during inference is already minimized. Given that your work primarily compresses the number of experts, why is the inference latency reduced? 
2. What are the implications of ExpertZIP on the interpretability of MoE models, given that some experts are merged? 
3. How does ExpertZIP compare to other model compression techniques, particularly those focusing on pruning or quantization?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a progressive expert fusion framework for MoE models which employs a Huffman tree-based technique. The Huffman tree is widely-used for lossless data compression. The authors merges underutilized experts step by step based on the utilization frequency within the MoE model. The paper claims a 17.23x model size reduction and a 4.84x inference time improvement with only 1.18% decrease in average accuracy compared to the original model.

### Strengths
The paper shows a visualization of expert selection imbalance across different layers in the MoE model.

### Weaknesses
Since the main idea of the paper is proposed a new expert fusion strategy, it's better to add a comparison with other expert fusion strategies in the experimental section.

### Questions
If there is no retraining, how will the expert fusion strategy based on utilization frequency perform?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work examines inefficiencies in Mixture-of-Experts (MoE) models, where many experts remain underutilized, leading to excessive memory and computation costs that limit scalability. To address this, the authors introduce **ExpertZIP**, a framework that progressively merges underused experts using a Huffman tree-based approach, retaining essential contributions while significantly reducing model size and enhancing inference speed.

### Strengths
- The topic of expert inefficiency in Mixture-of-Experts models is intriguing, with the findings on expert underutilization providing valuable insights.

- The proposed method demonstrates efficiency gains, optimizing resource usage while preserving model performance.

- The authors also showcase the effectiveness of post-training, which complements and enhances the MoE compression pipeline.

### Weaknesses
- While the authors show promising results in Switch-Transformers, these gains might largely stem from redundancy within the Switch-Transformer architecture itself. The performance on Mixtral, however, is less competitive; in Table 5, performance degrades by more than 10% even after a few fine-tuning steps, indicating that this method may not be as effective on more recent models like Switch-Transformers.

- Although the proposed approach introduces some novel ideas, comparisons with relevant works are limited. Specifically, comparisons with expert pruning methods (e.g., [1, 2]) are lacking; pruned models have also been shown to maintain performance effectively.

- Additionally, exploring other fusion techniques, such as OT-Fusion, would strengthen the analysis. A comparison with alternative fusion methods would better contextualize the benefits and limitations of the proposed approach.



[1] Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models  
[2] Demystifying the Compression of Mixture-of-Experts Through a Unified Framework

### Questions
- How about the performance of ExpertZIP on most recent MoE models and complex tasks? Does it maintain the performance? 

- Can you compare ExpertZIP with other compression techniques?

### Soundness
2

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
4

### Summary
This paper has found that many experts in the MoE model are rarely activated across different applications and those less frequently used experts contribute significant information the overall performance of MoE.  Therefore, this paper proposed ExpertZIP,  which merges less frequently used experts by a weight combination strategy rather than discard them. In this paper, Huffman tree is applied to identify and merge the least significant experts，and repeat this merging process until the desired number of experts is achieved.  ExpertZIP could significantly reduce the memory size and reference time of the MoE model with a very small performance loss.

### Strengths
It is a well written paper. The weakness of MoE is clearly described and the method prosed in this paper sounds good as the ExpertZIP has  gained a 17.23x reduction in model size and 4.84x improvement in reference speed with a very small accuracy drop.

### Weaknesses
For summarization tasks, this paper takes the ROUGE-l as the accuracy.  The importance of a word in the reference  summary should be taken into consideration.   Here is a simple example of considering the importance of words in the reference summary.

Let's assume the reference summary contains N words, among which M words are more important, M < N.  We call these M words IMPORTANT words and set the weight of these IMPORTANT words to 2/(N+M), and set the weight of the remaining (N-M) words to 1/(N+M).  In most cases, M = 1.   

Therefore, when ExpertZIP takes a summarization task and generates a summary with one IMPORTANT word missed （assume the reference summary includes only 2 words and one of them is the IMPORTANT word）.  In this case, the accuracy of ExpertZIP should be 1/3 rather than 1/2.

### Questions
In Fig.5, why did the ExpertZIP performance better at 2 Experts than at 4 and 8 Experts?  Could you please provide an analysis or explanation for this counterintuitive result?  or try more experiments to get more accurate results in the future.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a three-step pipeline to reduce the number of parameters and improve the inference time of popular MoE models, such as Switch Transformer and Mixtral 8x7B. First, it groups underutilized experts, then merges them using frequency-weighted averaging, and finally fine-tunes the model to recover accuracy.

### Strengths
- The analysis of expert utilization across different benchmarks strongly motivates this work.
- The figures clearly demonstrate the logical flow and effectively illustrate the main idea.

### Weaknesses
- The authors did not compare their method to existing baselines. Could the authors consider referencing [1] and [2]? The former performs expert merging on the Switch Transformer, and the latter prunes experts based on activation frequency.
- The authors did not clearly specify the model in the abstract and introduction, which may lead to confusion about the reported improvements, as different models may yield varying results.

[1] Li et al. Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy, ICLR 2024.\
[2] He et al. Demystifying the Compression of Mixture-of-Experts Through a Unified Framework, 2024.

### Questions
- For each task benchmark, is the fine-tuning process independent? More specifically, is the model evaluated on CoLA and SST-2 have exactly the same parameters? It seems that there are two models, one is fine-tuned on CoLA, and the other is fine-tuned on SST-2.
- Could the authors provide the time cost for fine-tuning and the accuracy after fusing without fine-tuning?
- Could the authors provide more details on the reasons for the decreased inference cost? Is it due to modifying the original router strategy from top-k to top-1 and then fine-tuning the model accordingly? Or is the cost reduction primarily due to time saved by loading experts into GPU memory?
- Could the authors specify which MoE model you use to analyze in Fig. 3?
- Could the authors explicitly compare the proposed method's performance and efficiency gains against the results reported in [1] and [2], highlighting any key differences in approach or outcomes?
- Could the authors add a description regarding the adopted MoE model architecture in the introduction and abstract sections?

### Soundness
2

### Presentation
3

### Contribution
2
