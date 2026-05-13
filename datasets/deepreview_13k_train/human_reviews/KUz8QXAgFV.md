# Bridging Autoregressive and Masked Modeling for Enhanced Visual Representation Learning

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Autoregressive models have demonstrated superior performance in natural language processing due to their ability to handle large-scale training and generating ability. However, their potential in computer vision has not been fully explored due to some key challenges they still face. Currently, masked modeling methods such as MAE are dominant in this field. By analyzing autoregressive and masked modeling methods in a probabilistic way, we find that they can complement each other. Based on this, we propose a general formulation and modeling framework that combines the benefits of both, named \textbf{G}enerative \textbf{V}isual \textbf{P}retraining (GVP). Our unified probabilistic framework allows for different training strategies, including masked modeling and autoregressive modeling, to be realized simultaneously. Our framework can be adapted for various downstream tasks and outperform existing methods in several benchmarks, including linear probing, fine-tuning and transfer learning. This work provides a promising direction for future research in generative masked visual representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work explores self-supervised training of visual representations with transformers models based on autoregressive and masked modelling objectives. At training time, content and query tokens and their attention masks are set up to represent a random permutation of input tokens that are predicted K at time via the query tokens. 

The work claims the obtained representations outperform existing methods in linear-probing, finetune in ImageNet-1K and transfer-learning to 9 downstream tasks. It compares against MIM and AR approaches as well as both when using discrete and pixel space for input and outputs.

### Strengths
The presented idea of how to extend pretraining to capture both AR and MIM setup is simple, if it overperforms existing methods or its inference flexibility can be shown to be usable to new setups, I would consider it to be a valuable contribution. IMO as it currently stands it is misleading (see weaknesses).

It’s good to see the evaluation against many existing methods and cover both pixel and discrete space.

### Weaknesses
The presented method appears to cost at least 2x to train to alternative methods (due to processing tokens once for content and once for query). By failing to present and discuss compute cost, the comparison with existing works in the main text does not provide sufficient evidence to claim outperforming them. Besides compute the memory requirements also change and may make this method less interesting than existing approaches.

Given the above and that the methods don't differ so much in representation accuracy, it begs the question on why the extra complexity. This work provides little discussion/results/ideas on how the added sampling flexibility can be use downstream and it reads more like: "here is another (more complex) way to obtain very similar image representations".

### Questions
What is the training cost of the presented method vs existing methods?

What is the source for the numbers in table 1? How were hyper parameters tuned for those?

Is the added flexibility, on how these networks can be sampled, usable for downstream tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper found that autoregressive modeling and masked modeling can complement each other for visual representation learning. The authors proposed a general framework that combines both methods. Experiments on several vision benchmarks show that this framework performs better than previous methods.

### Strengths
This paper demonstrates something interesting to me. It proposed a general framework for autoregressive modeling and masked modeling paradigms, which may help to better formulate the problem. In doing so, it also revealed a difference lies in the sequential dependency of autoregressive modeling and independence assumption of masked modeling, which I think may serve as a useful starting point to study generative visual pre-training.

### Weaknesses
While the innovation is good, I found some perspectives of the paper are not sound enough to convey true insights. Details are listed below.

1.	The motivation is not clearly illustrated. The paper claimed that “autoregressive models and masked modeling can complement each other” in Paragraph 3 of the introduction. However, I’m not aware of why “naturally generate sequences based on a specific masking pattern” is a good property. In fact, as the authors have stated, predicting autoregressively is not a natural choice in computer vision. Then, what’s the benefit of combining autoregressive models?

2.	The design of two-stream attention is not well motivated. Previous methods like MAE use one-stream attention. The proposed framework does not put a restriction on the two-stream attention mechanism. What is the purpose of introducing two-stream attention? On the other hand, two-stream attention is not well presented. What’s the differences between content stream and query stream? Why the causal masks are different for these two streams?

3.	Lack of ablation studies. Two ablation studies in the paper (patch ordering, analysis on auto-regressivity) both demonstrated that fixed pattern is not helpful for representation learning. However, these properties are consistent with masked modeling, but instead is not possessed by autoregressive modeling. As I have mentioned in Weakness 1, these experiments still do not tell us exactly what is the benefit of using autoregressive models. 
The main results show that the general framework performs better. Ablation studies should be responsible for telling why the performance is better. In order to do this, the authors need rigorous comparison experiments, especially with masked modeling paradigm. For example, experiments can begin with a pure masked modeling version (no grouping, no causal masks, no two-stream attention), and gradually add these modifications step by step to show what is key factor that contributes to the performance gain.

### Questions
1.	Notation is chaotic.

*	Equation (2) , $x$ is of different styles and inconsistent subscripts. Notation $m$ is not introduced.

*	Page 6, Section 4.2, Para 2, Line 4, $M$ is not introduced.

2.	What is the group segmentation distribution during training?

3.	Do you have the results on COCO detection task?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores the idea from XL-net (generalized auto-regressive modeling) in NLP that can efficiently implement arbitrary ordering to self-supervised visual representation learning (which is currently dominated by the idea of masked modeling). The paper provides a perspective that bridges the two type of modeling methods (all using visible data to predict hidden ones), and borrows the idea from XL-net to get the best of two worlds. Experiments are conducted on both pixel input/output, and tokenized input/output, and some improvements are shown (in Table 1). Analysis is mainly on the claim that iGPT is too restricted in using a fixed ordering (random ordering helps), and on how to do sequential prediction in groups.

### Strengths
+ The clear write-up that bridges the gap between masked modeling and autoregressive modeling is solid and very easy to follow.
+ I appreciate the effort of applying the idea from XL-net to see the effect. Even further, the work explored different inputs/outputs, different ways to evaluate the representation (linear vs. fine-tune), etc, which I highly appreciate.

### Weaknesses
 - I understand computation could be a problem, but would like to see more solid comparisons. E.g., the main table (Table 1) used a pre-training epoch of 200. At this stage, it is unclear whether the pre-training is just worse in upper bound, or it is just some pre-training converges faster. Plus, it would be much more fair to me if the comparison is done based on the "overall compute" or "overall data" spent on pre-training, rather than simply put number of epochs there. For example, the default number of epochs used in MAE is 800-ep, this is when the model has sufficiently converged. And even then, from 800 to 1600 there is still notable improvements in the final table. Comparing with MAE at 200-epoch is not the fair-most comparison.  
- (minor) I think Eq 3 has a typo that z should be greater or equal to m, instead of t.

### Questions
- Is there a planned code release? I guess from XL-net it is fine but would be great to promote open-sourcing here.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method called "Generative Visual Pretraining (GVP)" aimed at exploring the potential of autoregressive models in the field of computer vision. Autoregressive models have demonstrated remarkable performance in natural language processing, but they have not been fully explored in computer vision, thus there are still some key challenges. 

By probabilistically analyzing the methods of autoregressive and autoencoding mask modeling, it is found that the two can complement each other. Based on this, a general formula and modeling framework are proposed to combine the advantages of both methods, named "Generative Visual Pretraining (GVP)". Their unified probability framework allows for the simultaneous implementation of different training strategies, including mask modeling and autoregressive modeling. Their framework can adapt to various downstream tasks and outperforms existing methods in multiple benchmark tests, including linear probing, fine-tuning, and transfer learning.

### Strengths
Comprehensive Framework: The paper proposes a unified probabilistic framework that combines autoregressive modeling and masked modeling methods, enabling them to simultaneously implement different training strategies, including masked modeling and autoregressive modeling.

Performance Improvement in Tasks: The authors validate the effectiveness of their framework in multiple benchmark tests, including linear detection, fine-tuning, and transfer learning. They demonstrate that the framework outperforms existing methods in these tasks.

Flexible Generation Capability: Due to the integration of the advantages of autoregressive and masked modeling methods, the framework can provide improved classification ability and flexible generation capability.

Mathematical Analysis: The article analyzes the relationship between current autoencoding methods and autoregressive methods from a probabilistic perspective, and proposes a group-based autoregressive probability framework that allows modeling and flexible adjustment of task complexity in any order while modeling strong dependencies between tokens.

### Weaknesses
The author introduces a new framework that performs well in multiple benchmark tests. However, the paper lacks an in-depth discussion of the framework's semantic effectiveness in visual multi-object scenes. Although the author validates the effectiveness of the segmentation task ADE20K, there is insufficient validation on other detection and segmentation tasks. This limits the applicability of the method in real visual scenarios.

Furthermore, the method is not compared with last year's SAIM paper[1]. SAIM and RandSAC are contemporaneous works that explore self-supervised approaches using autoregressive methods. The autoregressive self-supervised method has also shown good performance on downstream tasks. As far as I know, RandSAC has explored group-level reasoning. How can we demonstrate the advantages of this paper's method compared to SAIM's patch-based autoregressive and RandSAC's segment-based approaches? Is it possible that your method is just a combination of these two methods?

Additionally, this article does not describe the efficiency of the method. We need to know if the method significantly delays training time, thereby reducing training efficiency. Moreover, the author uses a large batch size, which may be to obtain better performance. However, I hope the author can provide a more detailed analysis of this design choice.

### Questions
The current paper does not provide results for the multi-object visual scene detection task on COCO. It is recommended to include experimental results for downstream validation tasks related to object detection.

Please explain why only the mixed results perform the best in the autoregressive analysis. How do the fixed length and random approaches based on p2d and d2d perform?

Please provide the inference time and training time.

Is the GPU usage higher for this method compared to the RandSAC and SAIM methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
