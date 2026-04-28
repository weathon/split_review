# Mathematical Justification of Hard Negative Mining via Isometric Approximation Theorem

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 3, 8

## Abstract
In deep metric learning, the Triplet Loss has emerged as a popular method to learn many computer vision and natural language processing tasks such as facial recognition, object detection, and visual-semantic embeddings. One issue that plagues the Triplet Loss is network collapse, an undesirable phenomenon where the network projects the embeddings of all data onto a single point. 
Researchers predominately solve this problem by using triplet mining strategies. 
While hard negative mining is the most effective of these strategies, existing formulations lack strong theoretical justification for their empirical success.
In this paper, we utilize the mathematical theory of isometric approximation to show an equivalence between the Triplet Loss sampled by hard negative mining and an optimization problem that minimizes a Hausdorff-like distance between the neural network and its ideal counterpart function. This provides the theoretical justifications for hard negative mining's empirical efficacy.
In addition, our novel application of the isometric approximation theorem provides the groundwork for future forms of hard negative mining that avoid network collapse. 
Our theory can also be extended to analyze other Euclidean space-based metric learning methods like Ladder Loss or Contrastive Learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors attempt to analyse the network collapse phenomenon associated with hard negative mining for triplet loss. Such network collapse is not omnipresent and vary depending on the task at hand. The authors attempt to explain this phenomena by drawing a equivalence between the hard negative-mining triplet loss and the Hausdorff-like distance metric by using isometric approximation. Such approximations help to establish a relationship between the network collapse and the batch size or the dimension of the embedding, which provide insights into using different batch size or embedding dimensions for different variety of tasks across a number of tasks (such as person re-identification). Therefore the authors have provided theoretical insights as to why such collapsing happens for learning a distance metric with hard negative sampling, and ways to overcome them by performing experiments across different datasets and different backbones.

### Strengths
The connection between network collapse with the batch size or embedding dimensions; using isometric approximation is novel and interesting.

The authors have provided a detailed analysis of their proposed approximation between the hard negative-mining triplet loss and the Hausdorff-like distance metric along with detailed proofs in the appendix.

The authors have provided a substantial number of experiments across different datasets and different network backbones to show the effectiveness of their proposed work.

### Weaknesses
The major weakness of the paper is only showing the effectiveness of their proposed method for hard negative mining strategies for learning the distance metric. There have a considerable number of new sampling strategies which improve upon hard negative mining, especially aimed to tackle the slow convergence rate and the network collapsing phenomena. A different variety of loss functions have also been developed  to tackle the above mentioned issues. Therefore the impact of this paper is limited by the choice of the single "hard mining strategy". The methods in [A, B, C, D] aim to reduce the dependency of the batch size or the size of the embedding. A similar study has also been conducted in [E]. These methods need not always provide any theoretical explanations (which is a big plus for this paper), but they attempt to solve and tackle similar issue (network collapse). So it will be interesting if such equivalence can be drawn with such methods, which is missing in the paper.

### Questions
(1) Will such approximation hold true for any other sampling strategy or loss functions as mentioned in the Weakness section?

(2) In [A], the authors experiment with learnable $\beta$'s. Can the authors more some insights as to what would happen if $\alpha$ is also learned, instead of keeping it fixed.

(3) Have the authors done any experiments on face recognition datasets similar to [B, C]? It will be interesting to see if the proposed explanations hold true for experiments on face recognition too.

[A] Wu, Chao-Yuan, et al. "Sampling matters in deep embedding learning." ICCV 2017.

[B] Wang, Hao, et al. "Cosface: Large margin cosine loss for deep face recognition." CVPR 2018.

[C] Deng, Jiankang, et al. "Arcface: Additive angular margin loss for deep face recognition." CVPR 2019.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper delves into the issue of triplet loss collapse, offering a theoretical insight into its causes. The proposed method employs isometric approximation to demonstrate that hard example mining is effectively equivalent to minimizing a distance akin to the Hausdorff distance. Experimental results on two widely used metric learning datasets reveal that network collapse tends to occur with either a large batch size or a small embedding size.

### Strengths
- This paper addresses a significant issue related to triplet loss collapse, a topic of keen interest within the research community.

- The paper offers a novel theoretical perspective on the problem of triplet loss collapse by introducing the innovative concept of isometric approximation, contributing a fresh angle to this field.

### Weaknesses
 - It would be beneficial to see a more thorough analysis of various triplet loss variants, particularly with regard to different triplet sampling methods. This in-depth examination is essential for a comprehensive understanding of the effectiveness of triplet loss in different settings.

- The figures and examples in this paper suffer from both low quality and a lack of informativeness. They do not effectively convey the discussed settings, making it difficult for readers to comprehend the content.

- The experimental evaluations in this paper are notably limited, making it challenging to substantiate the claims put forth. For instance, the use of a very large batch size with semi-hard triplets in FaceNet raises questions that require further clarification or justification.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on addressing the issue of network collapse in deep metric learning, specifically in the context of the triplet loss. Network collapse refers to a situation where the network projects all data points onto a single point, leading to ineffective embeddings. The authors propose utilizing the mathematical theory of isometric approximation to establish an equivalence between the triplet loss with hard negative mining and an optimization problem that minimizes a Hausdorff-like distance. This theoretical framework provides the justification for the empirical success of hard negative mining in preventing network collapse. Experimental results on multiple datasets and network architectures validate the theoretical findings.

### Strengths
-	The paper offers a theoretical framework based on isometric approximation theory to explain the behavior of the triplet loss with hard negative mining. This provides a solid foundation for understanding and addressing network collapse in deep metric learning
-	The paper investigates the factors that contribute to network collapse, specifically focusing on the batch size and embedding dimension. Through experiments on multiple datasets and network architectures, the authors demonstrate that larger batch sizes and smaller embedding dimensions increase the likelihood of network collapse. 
-	The authors conduct experiments on various datasets and network architectures, demonstrating the effectiveness of hard negative mining in preventing network collapse. The empirical results corroborate the theoretical findings and enhance the credibility of the proposed approach.

### Weaknesses
 - The paper primarily focuses on hard negative mining as a solution to network collapse but does not thoroughly compare its performance with alternative methods or strategies. A comprehensive comparison with other approaches would provide a more comprehensive understanding of the effectiveness of hard negative mining and its relative advantages or disadvantages compared to other techniques. Without such comparisons, it is difficult to assess the competitiveness of the proposed method. For instance, techniques like contrastive loss or other sampling strategies could be considered, and a discussion of their relative strengths and weaknesses compared to hard negative mining would be beneficial.
- While the paper presents experimental results on multiple datasets and network architectures, it does not provide precise quantitative measurements of the performance improvements achieved by preventing network collapse through hard negative mining. Without specific metrics, such as accuracy or loss values, it is challenging to assess the magnitude of the improvement or compare it with alternative approaches. Including quantitative evaluations, such as the average precision or recall for retrieval tasks, or the final loss values achieved with and without hard negative mining, would enhance the rigor and credibility of the proposed method. Furthermore, reporting the variance of these metrics across multiple runs would also be important.
- The absence of mining time analysis and discussion on the time complexity limits the applicability of the proposed method to real-time or time-sensitive applications. Real-time systems often require fast and efficient processing, and the computational cost of hard negative mining can be a critical factor in determining the feasibility of the approach. Considering the practical implications and performance trade-offs in real-time scenarios would enhance the relevance and applicability of the proposed method. Specifically, the paper should discuss the computational overhead of finding hard negatives, and how this scales with batch size and embedding dimension.
- The paper primarily focuses on the theoretical framework and experimental results of hard negative mining in preventing network collapse. However, the experiments are conducted on a limited set of network architectures, and it does not include widely used backbone architectures such as ResNet-50 or Inception-BN. These mainstream architectures are commonly employed in deep metric learning and computer vision tasks. The lack of evaluation on such architectures limits the generalizability and applicability of the proposed method to real-world scenarios. Furthermore, the paper does not discuss the impact of different initialization strategies on the observed network collapse.

### Questions
See Weaknesses

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This theoretical paper discusses and analyzes the collapse problem in the Deep Metric Learning area. The author leverages the theory of isometric approximation to show an equivalence between the triplet loss sampled by hard negative mining and an optimization problem that minimizes a Hausdorff-like distance between the neural network and its ideal counterpart function. The main conclusion is equation 17, indicating that network collapse tends to happen when batch size is too large or the embedding dimension is too small. Effective experiments were conducted to visualize and support the conclusion.

### Strengths
The collapse problem is a famous problem blocking DML training. Current literature misses the systematic explanation of this phenomenon. The theory of the paper is helping understand the reason behind the problem and will benefit the DML research community. 

The starting point of the definition of triplet-separated accurately describes and fits the optimization of triplet loss. 
By leveraging the isometric approximation theorem, the path to achieve the proof to the corollary 3.4 is clear and sound. 
Finally, the experiments with different settings to proof the conclusion is equation 17 is wee conducted and integrated

### Weaknesses
The illustrative examples are not clear. Figure 2 is clear on the examples. But the figure 3 is not clear.
1. The line in figure 3 overlaps too much. would be good to redraw it.
2. it is not clear of diso(fθ,FTS) in the figure.

Figure 4 can be extended to multiple views to illustrate the progress of the collapse as the example shown in [1]. and if the diso(fθ,FTS) value can be added in the vis, it will be valued.

miner issue in the typos: section 1 "CUBwah et al. (2011))"

### Questions
Some extended questions:
How is the lower bound curve (17) related to the retrieval performance?
Triplet loss is rarely used in Self-supervised learning with a random initialization network. Maybe one of the reasons is also collapse. Can your theory explain the problem? is the DML problem similar to the SSL problem in the embedding level?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
