# Efficient In-Context Visual Learning with Trident Block and Cross Blocks

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Visual prompt-based large vision models exhibit remarkable performance in a range of vision tasks. However, visual prompting large vision models are computationally intensive and resource-demanding due to their large parameter sizes and the complexity of processing visual prompts, resulting in inefficiencies in speed and memory usage. To tackle these challenges, we propose the Efficient Painter model, which leverages a novel context-aggregated attention based trident block to alleviate cross-task gaps and reduce memory and computation overhead. Furthermore, we introduce a cross-blocks feature union module to capture global contextual information at different levels and speed up training. This architecture mitigates training costs and memory requirements during inference. Our model strikes a balance between speed and memory efficiency, achieving a 19$\times$ reduction in FLOPs. Moreover, our model is 9$\times$ smaller in model size and runs 4.1$\times$ and 27$\times$ faster during training and inference, respectively. Comprehensive experiments demonstrate that our design effectively processes additional visual prompts and outperforms baseline methods on standard benchmarks like \textit{SIDD} and \textit{LoL} in zero-shot settings, improving performance by 0.4\% and 1.2\% respectively.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose an efficient large vision model (LVM) called Efficient Painter, designed to reduce memory and computational demands for visual tasks. Key contributions include a context-aggregated attention (CAA) mechanism that allows dynamic context processing with lower resource usage and a cross-block feature union (CBFU) module that improves multi-level global context processing, effectively speeding up training. The authors report significant reductions in memory consumption and substantial speed improvements during inference.

### Strengths
If understood correctly, the Efficient Painter model demonstrates substantial reductions in computational load and memory usage compared to its baselines. There appears to be a meaningful architectural novelty, especially in the design of the CAA and CBFU components, which seem well thought out and targeted toward efficiency.

### Weaknesses
The paper’s writing quality is quite limited, making it difficult to follow and understand key ideas, especially in the introduction, motivation, and experimental sections. The paper is filled with confusing sentences, which need substantial improvement for clarity and readability.

Moreover, the paper appears unfinished, with placeholders such as "NaN" in the result tables, which is especially noticeable in Table 5. The experimental results are presented in a messy and confusing manner, further detracting from the paper's overall quality. The lack of clear baselines and the inconsistent reporting of results make it hard to assess the true contributions of the proposed method. For example, it's unclear why certain baseline models were chosen and why some results are missing.

### Questions
In its current state, I don’t believe this paper meets the standards for publication and would require significant revisions to be considered.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper aims to address the computational inefficiencies and slow speeds resulting from the large number of parameters and complex prompt processing in visual promoting large vision models. The paper proposes a context-aggregate attention based on the trident block and a cross-blocks feature union. Compared to previous models, it is 9× smaller in model size and runs 4.1× and 27× faster during training and inference, respectively.

### Strengths
+ From the experimental results, the architecture of this paper shows certain improvements in computational efficiency and speed.
+ The designed architecture can be applied to multiple tasks, including denoising and low-light enhancement tasks.

### Weaknesses
 - There are grammar issues in the writing, such as in the related work on the second page, ‘Traditional approaches such as DeiT, and MobileViT  leverage knowledge distillation or architectural downsize fail to enhance 
actual inference speed or throughput.’
- Lack of innovation. The core contribution of this article is a lightweight architecture, but many of the operations that affect parameter changes are existing methods, such as integrating existing DWConv or reducing the dimension of queries. The paper does not sufficiently demonstrate a novel approach to parameter reduction beyond standard techniques.
- Non-standard use of abbreviations in the writing.

### Questions
1. What is the innovation in this article? In addition to existing dimension reduction methods, what is the innovative dimension reduction strategy proposed in this article?
2. From the description in Section 4.2 on the fourth page and Figure 3, The CAA module primarily computes attention weights for different channel features and enhances the response of important features. It then accumulates and stacks important features from different channels. How are deep connections established between different channels? More prominently observed in the current design is feature aggregation rather than the establishment of correlations.
3. The mention of aligning channel attention mechanisms on lines 204-205 can reduce computational costs. The related reasons need to be further elaborated with specificity.
4. The article mentions that in the design of sub-modules, smaller dimensions are used to reduce the parameter count. This is indeed a simple and effective strategy, but further experiments and analysis are needed for the core innovative operations that can reduce the parameters.
5. Please avoid using abbreviations for the first occurrence whenever possible.
6. In lines 310-316 on page six, it is explained that aligning the channels of the sub-decoder can alleviate gradient explosions. Please provide specific reasons why this operation is believed to mitigate gradient explosions.
7. The alpha and beta variables used in section 4.4 are not clearly elucidated regarding the numerical selection strategy. Experimental analysis of the parameters chosen is lacking.

### Soundness
3

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
While Visual prompt-based large vision models exhibit remarkable performance in a range of vision tasks, visual prompting large vision models are computationally intensive and resource-demanding due to their large parameter sizes and the complexity of processing visual prompts. In light of this view, the authors propose the Efficient Painter model, leveraging a novel context-aggregated attention-based trident
block to alleviate cross-task gaps and reduce memory and computation overhead.

### Strengths
1 The authors propose the Efficient Painter model which is faster and more memory-inefficient than Painter [Ref1].
2 The authors present ideas clearly, making the paper easy to follow.

### Weaknesses
1 The CAA passes the feature from the previous head to the next head. This will make heads can't run in parallel leading to increasing running time. Could you prove the effectiveness of this design compared to running them in parallel? More discussion should be added.

2 In CAA, the authors use a smaller dimension for Q and K. Could authors apply the same idea to ViT of Painter and check whether it can get similar results with fewer parameters? This actually challenges the novelty/efficiency of this proposed method, if setting the dimensions of Q, K to a lower dimension to ViT of Painter can reach similar results, then the proposed CAA might be a insufficient design.

3 The specialized models in Table 5 are outdated. The authors should compare the proposed model with the newest best-specialized methods.

4 Could authors evaluate the proposed model with other datasets (for generality), not only the datasets in Painter [Ref1]?

5 Why are the results of Painter (Efficient-ViT-M5) all NA in Table 5? Table 5 is extremely incomplete in this case, it becomes really hard to evaluate the performance across different methods systematically. I understand that  the benchmark might be hard to build, however, when reporting related performance, the relative results should be reported for completeness.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper mainly focuses on visual in-context learning, specifically the previous work Painter. The authors point out that the previous in-context visual learning methods require unaffordable computational resources. To this end, the authors propose a more efficient network structure specifically designed for visual in-context learning, which can alleviate cross-task gaps and reduce memory and computation overhead.

### Strengths
1. The method is clearly explained.
2. The idea of reducing computational complexity for visual in-context learning is interesting and practical.

### Weaknesses
1. I am not sure how the proposed CAA is implemented. It seems the information is sequentially propagated between different attention heads.
2. It seems the proposed method may be overly complex. To achieve the goal of better efficiency, the authors rebuild almost all basic modules in the original Painter. While there are several ablation studies showing the efficacy of these designs, these experiments only focus on the high-level design. It is still not clear if it is necessary to build the modules the same as in L266 and L306.
3. I am not sure why the authors have to include the Painter+EViT with all NaN restuls in Tab.5?
4. I wonder if the author can compare the proposed method with methods such as distillation and pruning?
5. It would be better if the authors can test the proposed methods on different in-context learning tasks. For example, use MAE-VQGAN [1] for segmentation, detection and colorization.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
