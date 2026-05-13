# Key-Graph Transformer for Image Restoration

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
While it is crucial to capture global information for effective image restoration (IR), integrating such cues into transformer-based methods becomes computationally expensive, especially with high input resolution. Furthermore, the self-attention mechanism in transformers is prone to considering unnecessary global cues from unrelated objects or regions, introducing computational inefficiencies. 
In response to these challenges, we introduce the Key-Graph Transformer (KGT) in this paper. 
Specifically, KGT views patch features as graph nodes. The proposed Key-Graph Constructor efficiently forms a sparse yet representative Key-Graph by selectively connecting essential nodes instead of all the nodes.
Then the proposed Key-Graph Attention is conducted under the guidance of the Key-Graph only among selected nodes with linear computational complexity within each window.
Extensive experiments across 6 IR tasks confirm the proposed KGT's state-of-the-art performance, showcasing advancements both quantitatively and qualitatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the K-Graph Transformer (KGT) for image restoration. The proposed KGT addresses the computational challenges of transformer-based methods by creating a sparse K-Graph that connects only essential nodes, improving efficiency.

### Strengths
A novel Key-Graph Transformer was proposed to conduct the self-attention operation only among these selected nodes with linear computational complexity for image restoration.
Extensive experiments were conducted to verify the effectiveness of the proposed KGT.

### Weaknesses
On the image deblurring task, the authors should provide more results of comparison with current state-of-the-art works. 
The authors should explain why the KGT, which is built upon the structure of SwinIR, possesses more than double the model parameters of SwinIR (25.82M vs. 11.75M). Are the proposed K-Graph Constructor and K-Graph Attention Block really computationally efficient?
The authors should also provide a comparison between their proposed KGT and some representative state-of-the-art methods in terms of latency.

### Questions
It is suggested that that the authors consider discussing the differences and similarities with KiT[1] in the literature review part. 
In the demosaicking and denoising tasks, it is recommended to include the appropriate citation information in the corresponding table or context. In addition, in the denoising task, the number of model parameters for Xformer is 25.23M, as stated in the corresponding paper.
In the supplementary material, Is there a misquotation in subsection 3.1? Fig.?? should refer to Fig. 7? Furthermore, the authors mentioned that the training contains two phases in single-image motion deblurring task, which seems to be an uncommon training setup.
Reference:
[1] Lee, Hunsang, et al. "KNN local attention for image restoration." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach, the Key-Graph Transformer (KGT), which selectively choose top-K nodes, and then the chosen nodes undergo processing by all the successive K-Graph transformer layers. The computational complexity of the method can be significantly reduced from quadratic to linear when compared to conventional attention operations. Extensive experimental results show that the proposed KGT achieves state-of-the-art performance on several tasks.

### Strengths
1. This article proposes a novel approach where image features within a specified window are considered as nodes in a graph. For each node, a subset of k remaining nodes is chosen to establish connections, and subsequently, a self-attention operation is performed only among these selected nodes.

2. High algorithm efficiency can be achieved by calculating attention only among the k selected nodes, rather than considering all nodes. This approach significantly reduces the computational complexity from quadratic to linear, in comparison to conventional attention operations.

### Weaknesses
1. The paper mentions that compared with traditional self-attention, the time complexity of this method significantly slows down from quadratic to linear. Therefore, it is more prudent to add a chart comparing the convergence speed of various methods to the paper. Specifically, the paper should include a comparison of training time per epoch, or time to reach a specific performance threshold, for both the proposed KGT and the baseline methods. This would provide a more concrete understanding of the practical benefits of the reduced computational complexity.

2. None of the references in the full text are cited, which makes it very inconvenient to view the documents mentioned in the text. This lack of citations makes it difficult to verify the claims made in the paper and to understand the context of the proposed method in relation to existing work.

### Questions
1. I am uncertain about the usage of "KK". Upon examining the model diagram, I only observe the notation "K" being used, which raises doubts about the origin or meaning of "KK".

2. Please provide a detailed description of the model architecture, including the number of blocks in each layer.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a K-Graph Transformer (KGT) for image restoration.  The K-Graph Attention Block is proposed within each KGT layer to conduct the self-attention operation only among these selected nodes with linear computational complexity.

### Strengths
+ The technique of this work is somewhat appealing, because K-Graph Attention has low computing cost and high scalability.

+ The experimental evaluation and discussion are adequate, and the results convincingly support the main claims.

+ The paper is well-organized and clearly written.

### Weaknesses
- The author should discuss with relevant methods. Chen et al. [1] proposed a top-k strategy to selectively choose the most relevant tokens for image restoration (e.g., deraining).

Ref[1]: Learning A Sparse Transformer Network for Effective Image Deraining, CVPR2023.

- The limitations of the proposed method should be discussed.

### Questions
See the above Weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This proposes a graph based method to capture strong neighborhood cues from images and make them amenable to be fed to a transformer based model. The Q to K projection is used to reduce projection dimension (implicitly) which is learned through a similarity based adjacency matrix formulation. Overall, this is an interesting idea, but how to learn the neighborhood term 'K' needs more looking into since it can be changed from training to inference time.

### Strengths
The idea is good and the way to implement it using existing techniques works. The primary challenge of implementing the Key-Graph-Attention block has been implemented by three different techniques. The experiments do show that the method improves the SOTA performance for Image Restoration and other related tasks.

Originality: I think the idea is original and novel.
Clarity: the idea has been developed clearly and important terms in the process have been defined / clarified as necessary. 
Quality: I believe the experiment reporting quality could have been improved. 
Significance: The method is novel, and the experiment results are strong. This work can be useful for other applications as well.

### Weaknesses
The ablation studies were a bit hard to follow. For the randomly sampled strategy, it is not clear whether the value of K is selected once and then training is performed, or is it sampled per batch / epoch? This lack of clarity makes it difficult to assess the robustness of the method. Furthermore, the description of the inference phase, where 'K is set to desired value for both sets', is vague. The term 'desired value' is not defined, leaving the reader to guess how this value is chosen and what impact different choices might have on the final results. For Fig 4, the red and yellow circles are becoming bigger in size from left to right. The meaning of this visual cue is not explained in the text making the figure hard to interpret. What is the X axis, is it K at inference time? The figure caption and the main text should clearly explain what the circle size represents and the meaning of the x-axis. 

For the comparative experiments, it is not clear whether the methods were independently implemented, or their results obtained from the papers. If the results are taken directly from the papers, then it should be explicitly stated, and the reader should be directed to the original papers for details about the experimental setup. If the methods were independently implemented, then a more detailed discussion of the parameter selection for these methods is needed. Without knowing how the baselines were implemented, it is difficult to judge the validity of the comparison.

### Questions
Please improve the overall experimentation reporting. Segregate the datasets, methods and their implementations and the tasks and create a more cohesive experimentation reporting. This will definitely help this paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
