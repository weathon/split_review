# Motion Inversion for Video Customization

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 5

## Abstract
In this work, we present a novel approach for motion customization in video generation, addressing the widespread gap in the exploration of motion representation within video generative models. Recognizing the unique challenges posed by the spatiotemporal nature of video, our method introduces \textbf{Motion Embeddings}, a set of explicit, temporally coherent embeddings derived from a given video. These embeddings are designed to integrate seamlessly with the temporal transformer modules of video diffusion models, modulating self-attention computations across frames without compromising spatial integrity. Our approach provides a compact and efficient solution to motion representation, utilizing two types of embeddings: a Motion Query-Key Embedding to modulate the temporal attention map and a Motion Value Embedding to modulate the attention values. Additionally, we introduce an inference strategy that excludes spatial dimensions from the Motion Query-Key Embedding and applies a differential operation to the Motion Value Embedding, both designed to debias appearance and ensure the embeddings focus solely on motion. Our contributions include the introduction of a tailored motion embedding for customization tasks and a demonstration of the practical advantages and effectiveness of our method through extensive experiments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a motion customization method for video diffusion models. Specifically, it introduces two types of motion embeddings to capture the global relationships between frames and the spatial movements between frames. The former excludes spatial dimensions to effectively disentangle the temporal dynamics from the spatial information. Qualitative and quantitative comparisons, along with ablations, reveal the effectiveness of this method.

### Strengths
Method:

The method appears pretty solid, it is logical and intuitive. Disentangling the spatial from the temporal, and learning the temporal dynamics using motion key-query and motion-value embeddings in attention is a good way to approach the problem.

Experiments

There are qualitative results, and quantitative comparisons with various metrics - there could be some changes in this part, elaborated more in the weaknesses.

Paper writing

The paper is well written and easy to understand.

### Weaknesses
Experiments

I would really like to see more qualitative results. The results provided in the paper and supplementary are extremely limited, which raises questions on whether the method works well only on a small set of videos.

Additionally, I wonder why there are no comparisons with Tune-A-Video. It'll be great if these comparisons can be provided. 

There are also no comparisons with other motion customization methods such as AnimateDiff, MotionMaster, etc - is that because those methods require a specific motion module to be trained?

Method

One clarification - I assume the method is still zero-shot? Are the motion embeddings pre-trained on any videos, or is it all done using just the source video (from scratch)?

### Questions
Please answer the questions in the weaknesses.

In addition, I have another (open-ended) question: How dependent is the performance of the method on the backbone foundational model? I understand that the results would naturally improve as stronger backbones are used, but I want to understand if something like Tune-A-Video + strong backbone model would be equivalent to this method + strong backbone model? 

Are most of the limitations stated in line 83-92 because of the method or the backbone? 

I am happy to revise my score if all my concerns are resolved!

Post rebuttal comment: I have increased my score based on the authors rebuttal.

### Soundness
3

### Presentation
4

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
This paper proposes motion embeddings for model control. The main idea is to adjust the temporal attentions with the features extracted from the source guidance video. Specifically, this paper proposes a 1D motion Q-K embedding to add to the Q and K features to guide the global motions. Moreover, a 2D motion V embedding with differencing pre-processing is proposed to add to the V features to guide the local motions. The experimental results show that motion embeddings can be trained to effectively guide the motion of the output video without being influenced by the appearance of the source video.

### Strengths
**Originality**: the idea of combining 1D motion Q-K embeddings and 2D motion V embeddings is novel to me. The idea of using 1D to remove the spatial information is not new as in DMT. The idea of using differencing operations is also not new as in DMT. However, combining the two kinds of embeddings for two-level global and local motion control is interesting.

**Quality**: The experimental results generally show that the proposed method is effective and show superior performance over the other state-of-the-art methods in CVPR 24 and ECCV 24. From the videos in the supplementary materials, the performance of the proposed method is satisfying. And the effectiveness of each component has been verified by the ablation study.

### Weaknesses
As for **clarify**, though the selection of the 1D and 2D embeddings has been studied in the ablation study, generally speaking, it is still hard to understand why the QK should use 1D embeddings and why the V should use 2D embeddings. There lacks some intuitive explanation on why we should use such settings. Specifically, while the ablation study demonstrates the effectiveness of the chosen embedding dimensions, it does not provide a clear explanation of the underlying mechanisms. For instance, the 1D embedding for QK might be effective at capturing global motion, but the exact nature of this representation and why it is superior to a 2D representation for QK is not clear. Similarly, the 2D embedding for V is stated to capture local motion, but the specific spatial patterns it learns and how these patterns contribute to the final result are not well-defined. The lack of interpretability of these learned embeddings makes it difficult to fully understand the method's behavior and potential limitations.

Another **unclear part** is that, 2D embeddings use differencing operations to debias the appearance. However, from Eq. (5), only features with $j>1$ are debiased. When $j=1$, the original features with appearance information are used. Why not debiasing the first feature, for example, differencing $j=1$ with $j=L$?

### Questions
**Questions**

1.	Could the authors provide an intuitive explanation on why we should use 1D and 2D for QK and V, respectively?
2.	Why not differencing the first 2D embedding? 
3.	Why the frames of the output video are less than the source video. For example, supp\results\teaser\4.mp4 (1 seconds) and 4_source.mp4 (2 seconds)

**Small issues**

Line 191, $F$ should be $\mathbf{F}$

Line 320: `Diffusion Motion Transfer - CVPR24 (DMT) (Yatim et al., 2023), Video Motion Customization - CVPR24 (VMC) (Jeong et al., 2023)`
As DMT and VMC have been accepted to CVPR, the reference should be correspondingly updated to Yatim et al., 2024, Jeong et al., 2024

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
This paper introduces a novel method for motion customization in video generation, addressing the underexplored challenge of motion representation in video generative models. The proposed approach leverages Motion Embeddings—temporally coherent representations derived from video data—to enhance the motion modeling in video diffusion models without compromising spatial integrity. The paper presents two key components: the Motion Query-Key Embedding, which modulates the temporal attention map, and the Motion Value Embedding, which adjusts the attention values. Additionally, the paper proposes an inference strategy that removes spatial dependencies and focuses the embeddings purely on motion. Through extensive experiments, the method demonstrates its ability to effectively customize motion within videos while maintaining efficiency and spatial consistency.

### Strengths
1. Superiority against sota baselines, where evaluation is done both quantitatively and qualitatively.
2. Novel task
3. Clarity of the presentation and writing
3. Novelty in introducing the motion embedding concept
4. Easy to follow the paper

### Weaknesses
1. I understand the main method composed of two part; (1)What they optimize and (2)How they optimize.
In terms of the optimization target (1), there exists technical contribution. But in terms of the loss calculation (2), they either use the standard denoising loss, or the VMC/MotionDirector [1,2] loss.
If my understanding above is right, I think the paper should claim more on optimizing the motion embeddings are so important and superior than other options (temporal attention / temporal lora).

2. Finetuning temporal attn would directly hurt the model's original prior but training temporal lora would avoid this problem. Thus, the paper should show theoretical understanding / empirical insights that their eq(3) is superior to temporal lora optimization.

3. L260 ~ L264 need more explanation. What is is trying to achieve from the modulation? If the goal is to achieve appearance debiasing, why would it work? Is this modulation ablated in the paper?

4. In Figure 4 and in the paper in general, what does "excluding spatial dimensions" mean? Do the authors refer to "optimizing temporal attn related parameters instead of self attn related parameters? In Figure 4 left, what are the authors visualizing in the middle? Attention maps of the same module in the t2v unet? And how did they visualize them (e.g. PCA)?

5. In Fig 4 right, what do the authors mean by "differential"? If they mean residuals across frame-axis? If so, using different phrase would be more appropriate.

6. In quantitative evaluation, for computing temporal consistency, clip is not the optimal choice. Referencing metrics from V-bench [3] would increase the value of the paper.

### Questions
Please address the Weakness section

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
5

### Summary
This work introduces Motion Embeddings, a method for enhancing motion customization in video generation. The approach proposes a motion representation with two types of embeddings: Motion Query-Key Embedding for temporal attention modulation and Motion Value Embedding for adjusting attention values. An inference strategy is also proposed to focus exclusively on motion by excluding spatial dimensions and using a differential operation.

### Strengths
1. The proposed techniques for motion representation are clear and reasonable.

2. The experiments are comprehensive, featuring a variety of qualitative and quantitative results.

3. The paper is well-written and easy to understand.

### Weaknesses
1. The primary concern is that the proposed method's effectiveness has already been demonstrated in previous works, such as MotionDirector [1]. For instance, MotionDirector employs motion LoRA in the temporal layer for motion representation, which essentially involves adding weights to the Q, K, and V projectors (Wq, Wk, and Wv in Eq. 3). This paper introduces learnable embeddings added to the input features in Eq. 3. While these two embedding approaches are not identical, their functionality appears similar, thus limiting the novelty of the contribution.

2. The interpretability of the learned embeddings is insufficiently addressed. Although the paper claims improved interpretability, no convincing evidence is provided. For instance, could the authors visualize the learned QK embeddings to determine if the attention maps exhibit meaningful patterns? Alternatively, are the learned V embeddings interpretable in any discernible way? The paper should provide a more thorough analysis of the learned embeddings, demonstrating a clear connection between the learned representations and the motion characteristics they are intended to capture. The current analysis lacks the depth needed to establish a significant improvement in interpretability beyond simply following motion.

### Questions
1. The paper claims to utilize 1-D QK embeddings for global motion and 2-D V embeddings for spatially varying movements. Could the authors provide results demonstrating their effectiveness when these embeddings function independently?

2. The proposed method targets temporal attention, while the base models decompose attention into separate spatial and temporal components. It would be more compelling to demonstrate the effectiveness of this technique within full attention architectures, where spatial and temporal attention are integrated into a single attention mechanism (e.g., Open-Sora [1]).

[1] Open-Sora: Democratizing Efficient Video Production for All, Zheng et al., 2024.

### Soundness
2

### Presentation
3

### Contribution
1
