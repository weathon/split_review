# AVG-LLaVA: A Large Multimodal Model with Adaptive Visual Granularity

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Recently, when dealing with high-resolution images, dominant large multimodal models (LMMs) usually divide them into multiple local images and one global image, which will lead to a large number of visual tokens. In this work, we introduce AVG-LLaVA, an LMM that can adaptively select the appropriate visual granularity based on the input image and instruction. This approach not only reduces the number of visual tokens and speeds up inference, but also improves the overall model performance. Specifically, we introduce the following modules based on LLaVA-NeXT: (a) a visual granularity scaler that includes multiple pooling layers to obtain visual tokens with different granularities; (b) a visual granularity router, which includes a Transformer layer, an MLP layer, and a voter layer, used to select the appropriate visual granularity based on the image and instruction. Furthermore, we propose RGLF, a novel training paradigm that aims at aligning the granularity predicted by the router with the preferences of the LMM, without the need for additional manually annotated data. Extensive experiments and analysis show that AVG-LLaVA achieves superior performance across 11 benchmarks, as well as significantly reduces the number of visual tokens and speeds up inference (e.g., an 85.3\% reduction in visual tokens and a 2.53$\times$ increase in inference speed on the AI2D benchmark).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents AVG-LLaVA, a large multimodal model capable of adaptively selecting the appropriate visual granularity based on input images and instructions, aiming to enhance model performance and reduce the number of visual tokens to expedite inference. AVG-LLaVA extends LLaVA-NeXT with the addition of a visual granularity scaler and a visual granularity router, along with a novel training paradigm called RGLF, which aligns the router's predicted probabilities of multiple granularities with the preferences of the LMM through a ranking loss.

### Strengths
1. The paper introduces a novel approach to handle high-res images by adaptively selecting the appropriate granularity based on the input image and instruction. Also, it conducted experiments to develop the appropriate tuning practice (the training state 3 & 4) to unlock the potential of the new paradigm.
2. On multiple benchmarks, AVG-LLaVA demonstrates its efficacy. It can achieve better results compared to LLaVA-NeXT while consumes much less computations.

### Weaknesses
1. The training paradigm is complex. It incorporates two additional training stages, each requires extensive computation costs. The additional training cost may hinder this approach from being widely adopted. The paper does not provide a detailed breakdown of the computational cost for each stage, making it difficult to assess the practical feasibility of the method.
2. The framework is not thoroughly investigates and the ablation study is not sufficient (see Questions).


### Questions
1. It's well known than finetuning VLMs on instruction tuning corpora with multiple epochs will typically improve the performance on benchmarks. The authors need to prove that the improvement cannot be simply attributed to 3x tuning epochs (corresponding to stage 2 to 4).
2. Achieving better performance with fewer visual tokens is not a usual case. Would you please include more qualitative & quantitative examples & analysis and discuss under which circumstances the VLM can achieve this?
3. The AVG-LLaVA framework can be easily extended to perform patch-wise granularity selection (for example, select different granularity for different patches). Would that be helpful to save more visual tokens under text-rich scenarios (the current AVG-LLaVA did not save much visual tokens for TextVQA and ChartQA). 
4. Recently, Qwen2-VL proposed to use native dynamic resolution visual encoders (no patchify) to generate visual embeddings. It would be beneficial to show that AVG-LLaVA also works for that kind of visual encoders.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a model that dynamically adjusts the granularity of visual tokens based on input images and instructions. This adaptive mechanism improves both efficiency and performance in multimodal tasks, reducing token usage and speeding up inference. The authors propose a novel training method, Ranking Granularity to Align LMM Feedback (RGLF), and test the model across 11 benchmarks. While the approach optimizes efficiency, concerns remain regarding scalability and performance trade-offs on certain tasks. The work offers promising advancements in multimodal learning.

### Strengths
The paper introduces a visual granularity scaler and router, which adaptively selects the appropriate granularity for visual tokens based on the input image and instructions. This adaptive selection mechanism is a significant advancement over static high-resolution LMMs, potentially improving both efficiency and accuracy in multimodal tasks.

### Weaknesses
1.	Lack of novelty: The motivation of this paper is highly similar to Matryoshka model, which also employs hierarchical token merging for visual token reduction, akin to token pruning in this paper. It seems that the difference is that the authors design an router to allocate weights to several granularities, which is incremental in terms of novelty.
2.	Insufficient experiments: This paper does not fully explore alternative approaches for granularity selection, such as task-specific fine-tuning or manual selection for certain tasks that might further improve performance.
3.	While the model's adaptive granularity selection is a strength, the architecture of the visual granularity router (involving multiple pooling layers, Transformer layers, and a voter layer) adds significant complexity and a substantial computational cost.
4.	The performance improvement is not superior across all benchmarks. For example, in GQA and ScienceQA, the proposed method underperforms slightly compared to some baselines, raising concerns about whether token reduction is always beneficial.
5.	Repeated Training Data: The training data for Stages 2, 3, and 4 are identical. Therefore, it is unclear whether the performance improvement is due to repeated training, akin to training for three epochs.
6.	Performance on OCR Tasks: As shown in Table 5, the visual tokens for OCR tasks are almost entirely retained, rendering the filter ineffective. The improvement in OCR tasks may primarily stem from repeated training.

### Questions
1.	The ablation study in Section 4.5 suggests a strong reliance on instruction tokens for granularity selection. Could the model's robustness be affected in situations where instructions are ambiguous or noisy? This is more important to the industry from my perspective.
2.	The benchmarks used are well-known public datasets. However, has the model been evaluated in real-world scenarios with less curated, noisier data? This would test its robustness in a more practical context.
3.	Training Cost: Provide details of the training costs associated with each of the four training stages.
4.	Comparative Experiment: Conduct a comparative experiment by training LLaVA-Next with repeated SFT data two or three times and present the detailed results.

### Soundness
3

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
5

### Summary
This work aims to enhance the LMM LLAVA-NeXT through improved visual granularity selection. 
To achieve this, we introduce AVG-LLAVA, which consists of a visual granularity scaler, 
a visual granularity router, and the RGLF training paradigm. 
Experiments have been conducted to validate the effectiveness of the proposed method.

### Strengths
1. The research focus  is intriguing, particularly the aspects of visual granularity selection and the Ranking Granularity to Align LMM Feedback.

2. Experimental results demonstrate its effectiveness.

### Weaknesses
1. The training pipeline has become more complicated, moving from original two stages to four, which increases the training overhead despite the performance improvements.

2. I think the description of the main contributions is not well-articulated; it should better to include an algorithm, especially the Visual Granularity Router.

3. It would be beneficial to provide direct, rigorous evidence for the selection of granularity to illustrate the proposed method.

4. Providing visual examples that highlight the need for granularity, such as attention maps of visual tokens in the LLM, would be advantageous.

5. In Table 3, for ChartQA, the token per grid is 99.1%, while the speed is 0.97x without any increment.

### Questions
It should better to provide total token numbers of each method in main performance comparsion for each method.

### Soundness
3

### Presentation
2

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
The authors propose an adaptive visual granularity mechanism dubbed AVG-LLaVA.  Based on this assumption, they employ the visual granularity scaler to generate visual tokens with various granularities, and the visual granularity router to select the appropriate visual granularity. Besides, the paper introduces a training paradigm RGLF to enhance the router.  Comprehensive experiments are performed on various visual benchmarks to validate the effectiveness of the method.

### Strengths
1. The motivation is novel, and different prompts require information at different visual granularities. And the manuscript is explicit and well-organized.
2. The authors solve the problem of training the router in VLM directly and utilize the ranking loss to supervise, which is impressive.
3. Experimental validation is sufficient. The authors conduct comprehensive experiments on various tasks and show improvements, to validate the effectiveness of the method.

### Weaknesses
1. The method lacks novelty. (1) the multiple pooling operation in visual granularity scaler is very common, like the most classic SPPNet [1]. Specifically, the visual granularity scaler uses a series of max pooling operations with kernel sizes of 1x2 and 2x1, which are very similar to the pooling operations used in SPPNet. The only difference is the specific kernel sizes used, but the overall concept of using multiple pooling operations to extract multi-scale features is the same. (2) the router operation has been proposed for many years, and the current implementation, using a transformer layer followed by an MLP and a voter, is a standard approach for routing mechanisms. The combination of these components does not represent a significant departure from existing methods.
2. Although the method sounds simple, the overall pipeline is complex. The stage 2 and 3 cost more training resources and time, where the vision encoder and LLM both are trained. The need to train the vision encoder and LLM in stages 2 and 3 significantly increases the computational burden and makes the method less practical for resource-constrained environments. This multi-stage training approach also introduces additional complexity in terms of hyperparameter tuning and management.

### Questions
1. Is it convenient to list their accuracy in Table 3 for further comparison? Besides, I want to know the absolute value of its actual speed.
2. I would like to see a visualization of actual token clipping, such as the image in Figure 1, and what the router results would be for different prompts.

### Soundness
3

### Presentation
3

### Contribution
2
