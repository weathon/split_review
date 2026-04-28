# From Layers to States: A State Space Model Perspective to Deep Neural Network Layer Dynamics

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6

## Abstract
The depth of neural networks is a critical factor for their capability, with deeper models often demonstrating superior performance. Motivated by this, significant efforts have been made to enhance layer aggregation - reusing information from previous layers to better extract features at the current layer, to improve the representational power of deep neural networks. However, previous works have primarily addressed this problem from a discrete-state perspective which is not suitable as the number of network layers grows. This paper novelly treats the outputs from layers as states of a continuous process and considers leveraging the state space model (SSM) to design the aggregation of layers in very deep neural networks. Moreover, inspired by its advancements in modeling long sequences,  the Selective State Space Models (S6) is employed to design a new module called Selective State Space Model Layer Aggregation (S6LA). This module aims to combine traditional CNN or transformer architectures within a sequential framework, enhancing the representational capabilities of state-of-the-art vision networks. Extensive experiments show that S6LA delivers substantial improvements in both image classification and detection tasks, highlighting the potential of integrating SSMs with contemporary deep learning techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a new module named Selective State Space Model Layer Aggregation (S6LA), designed to integrate traditional CNN or transformer architectures into a sequential framework for improving the representational power of advanced vision networks. The paper shows results on image classification and detection and segmentation benchmarks.

### Strengths
Overall the paper seems to be structured.

### Weaknesses
The main issue of the paper is that it is not written with enough clarity and often sidetracks from the main points making it hard to understand the main point. Unfortunately, the lack of clarity in the paper makes it hard to judge the work itself. The idea pitched forward in the paper might be interesting but in its current form, it's remotely comprehensible. I would suggest that the author(s) go over the paper and rewrite it in as simple and clear as possible. Also, please go over the mathematical notation and polish it more. Moreover, please pay attention to the citations to back up the claims. For example, lines 230-234, does not contain any citation or mathematical grounds for the claims made there. Similarly, line 95-96 is cryptic. Moreover, the captions of the figures should also indicate what is happening in the figure (this goes for all the figures included in the paper). I believe that once the paper writing is majorly polished and refined, it may have a higher chance of getting through.

### Questions
What kind of results does the table 4 contains? Does it use Mask RCNN 1x schedule, 3x schedule (from implementation details it seems like it is 1x schedule but then why is 3x schedule not included)?
In fig. 6 and fig 7, Can the author(s) please comment or write in the caption how the qualitative results for the proposed technique are better than the competition?

### Soundness
2

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
3

### Summary
The paper proposes a novel layer aggregation method S6LA that treats the outputs from layers as states of a continuous process and utilizes selective state space models architecture for layer aggregation. The paper reformulates two different layer aggregation processes with the proposed S6LA for ConvNet and Transformer-based backbones. The experiments are conducted on two tasks image classification
and detection on ImageNet, MS COCO 2017 datasets.

### Strengths
1. The paper is well-written and well-organized.
2. The idea of utilizing a selective state space-based model for seamless layer aggregation with continuous layer output is novel and interesting. The different integration formulation using the proposed S6LA for different backbones(ConvNet and Tranformer) is reasonable.
3. The quantitative results in the experiment sections show the proposed method's effectiveness over baseline methods.

### Weaknesses
1. The pipeline figure (Figure 3) for the Transformer-based approach can be improved so it will be easier for the reader to follow. For example, the naming labels in Figure 3 should be more aligned with what's in the paper along with some pipeline walkthrough captions.
2. Selective State Space models are known for slow training due to their nature of backpropagation through time (even with parallel scans). Will this affect the transformer and ConvNet backbone's parallelization training compared to the baseline methods that are Transformer or ConvNet-based?

### Questions
I have a question about transformer-based S6LA integration.

In the paper, equations 15, 18, 19, and Figure 3, $X^{t−1}_{input}$ go through the attention block, add & norm, and split into two parts: the cls embedding goes through the S6LA, image embeddings add with the product of itself with hidden state, and the final output is the concatenated cls embedding and image embedding.

1. Can you provide a clarification that with the S6LA integration, are the MLP blocks excluded from the original Transformer block?

2. If yes, can you clarify the reason for excluding?

3. If no, how it fits into the pipeline detailed in equations 15, 18, 19, and Figure 3? 

4. (I am assuming Linear Projection in Figure 3 means MLP block in the Not Exlcuded case) Since in the traditional transformer-based methods,  after attention and add & norm, cls embedding is also fed into the MLP layer along with image embeddings. From Figure 3, the proposed method seems to exclude cls embedding from MLP layers. Can you clarify the reason and potential impact on layer aggregation if this is the case?

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
4

### Summary
The central idea is to treat various layer outputs as continuous states within a state space model (SSM) and introduce the Selective State Space Model Layer Aggregation (S6LA). The outputs from different layers are fed to the state space model as sequential inputs. This approach aims to enhance the representational power of neural networks by aggregating information across layers in a continuous manner, motivated by advancements in SSM for sequence modeling. Experimental results show that S6LA performs well in comparison to standard convolutional and transformer-based layer aggregation techniques in image classification and object detection tasks.

### Strengths
* The approach is novel, application of state space models to layer aggregation in deep neural networks is an interesting concept. 
* S6LA demonstrates notable improvements in classification and detection tasks, especially when compared to existing layer aggregation methods.
* The S6LA module is compatible with both CNN and transformer architectures.
* The paper includes extensive experiments on benchmark datasets, showing consistent gains in accuracy.
* The ablation experiments are detailed and well positioned to study the effect different design elements in the approach.

### Weaknesses
 * Introducing state space models to layer aggregation may increase computational complexity, can the authors add run time comparisons of their and competing methods?
* Authors criticize the RealFormer and EA-transformer approaches for high memory consumption. What is the memory consumption of proposed architecture? It will be good to clarify and compare the memory consumption.
* SSM models can be unstable in training, do authors observe any unstable training behaviour with the proposed SSM based block?

### Questions
* How does the computational cost of S6LA compare to simpler aggregation techniques, and are the improvements in accuracy justified by this cost?
* The concatenation vs. multiplication of X and h variables seem to have a lot of impact on final performance. Can the authors motivate why different fusion mechanisms are needed for different architecture families i.e., CNN vs ViTs?

### Soundness
3

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
This paper proposes a novel layer aggregation strategy based on the recent S6 block. Two different implementations are conducted for CNN and Transformer architectures. Detailed experiments are delivered on both classification and object detection tasks. The proposed strategy achieves almost the best improvement among current layer aggregation strategies.

### Strengths
The proposed layer aggregation based on the S6 block is delicate and achieves significant improvement on various tasks and model architectures. This paper is easy to understand, and the proposed method is easy to follow.

### Weaknesses
1. The main problem for me is the different designs between the transformer and CNN. There is a lack of valid explanation here as to why the transformer needs a multiplication strategy while CNN requires an additive one. The only reason given in Lines 301-302 from the input perspective is not convincing enough. Specifically, the justification for using element-wise multiplication in the Transformer and concatenation followed by a linear layer in the CNN is unclear. The authors should provide a more detailed analysis of how these operations affect information flow and feature interaction within each architecture. Furthermore, the performance of CNN with a multiplication format of S6LA (used in the transformer) is missing here, which would provide a more complete picture of the design choices.

2. The authors claim that Kaiming normal initialization is crucial for the initial hidden state and will verify this point in the ablation study. However, no relevant experiments are found in the main paper. This is a critical omission, as the choice of initialization can significantly impact the training dynamics and final performance of the model. The absence of this ablation study makes it difficult to assess the true contribution of the proposed method.

3. The impact of S6LA on model efficiency is needed, including detailed inference and training FPS and memory occupation. Without this information, it's hard to evaluate the practical applicability of the proposed method, especially in resource-constrained environments. The trade-off between performance gains and computational costs needs to be clearly quantified.

4. Some minor errors. The authors may consider replacing the "th" with a subscript, such as the one in Line 164. Besides, from 0 to t-1, there are a total of t layers instead of t+1, as stated in Line 167.

### Questions
Could the authors also report the performance improvement on the ADE20K dataset?

### Soundness
3

### Presentation
2

### Contribution
3
