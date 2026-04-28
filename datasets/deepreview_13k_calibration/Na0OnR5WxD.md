# Redundant Queries in DETR-Based 3D Detection Methods: Unnecessary and Prunable

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 5, 6, 6

## Abstract
Query-based models are extensively used in 3D object detection tasks, with a wide range of pre-trained checkpoints readily available online.
However, despite their popularity, these models often require an excessive number of object queries, far surpassing the actual number of objects to detect.
The redundant queries result in unnecessary computational and memory costs.
In this paper, we find that not all queries contribute equally -- a significant portion of queries have a much smaller impact compared to others.
Based on this observation, we propose an embarrassingly simple approach called \bd{G}radually \bd{P}runing \bd{Q}ueries (GPQ),  which prunes queries incrementally based on their classification scores.
A key advantage of \method{} is that it requires no additional learnable parameters.
It is straightforward to implement in any query-based method, as it can be seamlessly integrated as a fine-tuning step using an existing checkpoint after training. With GPQ, users can easily generate multiple models with fewer queries, starting from a checkpoint with an excessive number of queries.
Experiments on various advanced 3D detectors show that \method{} effectively reduces redundant queries while maintaining performance.
Using our method, model inference on desktop GPUs can be accelerated by up to 1.31x.
Moreover, after deployment on edge devices, it achieves up to a 67.86\% reduction in FLOPs and a 76.38\% decrease in inference time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In query-based models, the number of queries significantly exceeds the actual number of objects for both 2d object detection and 3d object detection. The performance of models is positively correlated with the number of queries, and the performance consistently declines as the number of queries is reduced. In this paper, the authors propose that queries do not contribute equally and even there are queries are never selected as final results. The redundant queries result in unnecessary computational and memory costs. Therefore, the authors propose a query pruning method to gradually prune redundant queries in transformer.

### Strengths
1. This paper is the first study to explore query pruning in query-based detectors. 
2. The experiments demonstrate the effectiveness of proposed method, which reduces redundant queries while maintaining performance.

### Weaknesses
1. The experiment is incomplete and unpersuasive.



### Questions
1. The font in Figure 1 is not consistent with other figures. The label of Y-axis is not clear.
2. In query-based models, there are content query and spatial query. Does the proposed method perform experiments on the detectors that use both content query and spatial query? If not, the author should add additional experiments to prove the effectiveness of the proposed method on this kind of detectors.
3. In StreamPETR and FocalPETR, two variants of the model are trained for 24 epochs and 60 epochs, respectively. In StreamPETR, the models in the ablation study are trained for 24 epochs, while trained for 60 epochs when compared with others. The authors should add additional comparison experiments which trained for 60 epochs. 
4. For model pruning methods, except for precision, FLOPs and time, the number of parameters and memory cost are also important evaluation metrics. The authors should provide the comparison experiments between detectors based on the number of parameters and memory cost.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes Gradually Pruned Queries (GPQ), which removes redundant queries in transformer-based 3D object detection models. Queries are sorted by classification scores, and the lowest-score query is iteratively removed. Experiments on the nuScenes dataset validate the effectiveness of GPQ.

### Strengths
- This work proposes a simple and reasonable pruning method for transformer-based 3D detection models.

### Weaknesses
 - Numerous typos are present, such as "3D objec detection" (L351), "each query as as the fundamental" (L264), "it is the queries" (L268), "The reason of why our method" (L300). The authors are encouraged to correct all typographical errors and improve their English writing to enhance readability.
- Lack of comparison with prior work. This paper does not provide comparisons with previous pruning methods or implemented baseline pruning techniques. The authors are encouraged to include comparisons with other pruning baselines to demonstrate the advantages of their approach.
- No ablation studies. This paper lacks ablation studies on the design aspects of their method. The authors are encouraged to conduct ablation experiments to illustrate the impact of their design choices.

### Questions
- In Table 1, could the authors provide time and memory costs instead of accuracy? This would allow readers to more easily understand the relationship between the number of queries and model efficiency.
- In Figure 3, should the last column be labeled "Iteration 𝑛+1"? Or is Iteration 𝑛 run twice in this work?
- In Table 2, could the authors include model cost along with accuracy? This addition would help readers better understand the pruning effect of the proposed method.

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
4

### Summary
The paper proposes query pruning in typical query-based object detectors to improve their performance. Experiments on the nuscenes dataset show the effectiveness of the approach.

### Strengths
+ The idea of using classification scores to prune queries is nice.
+ The paper is easy to understand.
+ The approach demonstrates promising results on the nuScenes validation set.

### Weaknesses
- An alternate way to reduce the processing time of 3D detectors is to use Token Merge [A]. How does query prune quantitatively compare against Token Merge [A]? Specifically, what is the computational overhead of the proposed pruning method compared to the overhead of computing token similarity for merging, and how does this impact overall inference time, especially when considering the potentially large number of tokens in 3D detection?
- Another way to reduce processing time is to use model quantization. How does query pruning quantitatively compare against Model Quantization? It is crucial to understand the trade-offs between these two approaches, particularly in terms of accuracy, speed, and hardware requirements. For instance, how does the proposed method perform when combined with quantization techniques, and what are the limitations of each approach when applied independently?
- It would be beneficial to quantitatively include results from the nuScenes leaderboard, particularly comparing against a strong camera baseline like SparseBEV with 640x1600 resolution. The absence of this comparison makes it difficult to assess the practical applicability of the proposed method in real-world scenarios, where high-resolution inputs are common.
- The experiments are conducted with super small backbone (ResNet50). It would be insightful to quantitatively evaluate the approach on higher resolutions (512x1508 and 640x1600) to assess its performance. Furthermore, how does the performance of the proposed method scale with different backbone architectures, and what are the limitations of using a smaller backbone for evaluation?

### Questions
Please see the weakness

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
The manuscript proposes to prune queries in DETR-based 3D detectors to speed up inference by almost 2x without loss of detection performance (in some cases even improving performance). Pruning is performed after training has finished without the need for any gradients to flow. The lowest scoring queries are incrementally removed one by one.

### Strengths
- The paper is well written and and illustrated. The figures help support the text i.e. Fig 1 and 3.
- The approach is well motivated through experiment: Fig 2 shows that the imbalanced number of selections per query is prevalent across various DETR-based detectors. There indeed seem to be some queries that are used very often and others that are not.
- The experiments are thorough for the proposed approach (but lack deeper/broader investigations see weaknesses). The approach is evaluated on four current PETR-based architectures and show across the board that the pruning increases throughput and that detection performance is maintained or slightly improved. The last point is positively surprising.
- The proposed approach is indeed straight forward and it is great that it can be deployed on existing checkpoints after training. This makes it universally applicable to 3D DETR models. Simple and universally applicable enables impact.

### Weaknesses
 - The manuscript could have tried harder to investigate why training on a large set of queries and pruning them after is a better choice than training with fewer queries to begin with. The experiments show this (which is good), but the reader is left wondering about the why.
    - Which are the queries that get pruned? Is it that they attend to similar areas in space but always loose out against more confident queries? 
    - If we took the top most confident queries (as per the proposed algorithm) and the least confident ones (invert the algorithm and prune the most confident ones) how would the detections from those two pruning strategies compare? Do the least confident queries still give good OBBs just not very confidently? Or are they only giving rubish?
- There are no pruning baselines evaluated leaving the reader to wonder about some of the algorithm choices and how close to optimal this approach performs.
    - How important is the incremental pruning vs pruning down to the desired number of queries in one go?
    - How well does an oracle-based pruner perform? Always prune the worst query when matched against GT bounding boxes. How does that pruned model perform relative to the proposed score based on? 
- I appreciate that the timings were collected on a Jetson Nano device which shows the clear motivation to deploy the algorithms in practice. Checking against related methods, though the timing information was typically performed on a desktop-grade GPU. Showing those timings in addition would allow more direct comparability. I think Table 3 and 4 could have been combined to make room for the aforementioned additional investigations.
- Showing reprojections of 3D bounding boxes into frames hides any depth errors. So I would have appreciated Fig 4 to include some top down 3D visualizations instead of just frame reprojections (which frankly all look very similar). 
- Algo 1: showing an algorithm is meant to help clarify the proposed method. I do not think it is achieving this aim as is. I think the algorithm depiction should be simplified more to where it actually captures the high level information. The details can certainly be found in the code once it is released.

### Questions
Fig 2 renders poorly for me and the text is hard to read. Please fix.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the issue of redundancy in DETR-based 3D object detection models. The authors find that not all queries contribute equally to the detection task, and a significant portion of them have a minimal impact. They propose an approach called Gradually Prunes Queries (GPQ), which reduces the number of queries by pruning those with lower classification scores. The overall framework appears simple. However, my main concern lies in the discussion of related work. There is indeed a substantial amount of work aimed at speeding up query-based methods in 2D object detection. The authors did not provide a convincing and comprehensive review, nor did they offer a comparison with the most relevant methods.

### Strengths
1. The paper is well-structured, with a clear abstract, introduction, methodology, experiments, and conclusion sections that logically flow from one to the next.
2. The proposed Gradually Prunes Queries method is simple and effective.
3. The experiment results, when compared to different standard detectors, show that the design is effective.

### Weaknesses
1. There are some works aimed at speeding up query-based methods in 2D object detection, but this paper did not discuss. So, it is not clear if very similar methods exist in 2D object detection. 
[1] Yang, Chenhongyi, Zehao Huang, and Naiyan Wang. "QueryDet: Cascaded sparse query for accelerating high-resolution small object detection." Proceedings of the IEEE/CVF Conference on computer vision and pattern recognition. 2022.
[2] Zhu, Yuan, Qingyuan Xia, and Wen Jin. "Srdd: a lightweight end-to-end object detection with transformer." Connection Science 34.1 (2022): 2448-2465.
2. It is not clear what the special challenges are in 3D space, and why the experiments are only conducted in 3D space.
3. Using fewer queries may lead to slower network convergence, so fewer queries might require more training iterations. However, since the same number of epochs were used in Table 1, it's difficult to conclude that the precision drops quickly solely due to fewer queries.

### Questions
1.	Are there very similar methods proposed in the field of 2D object detection?
2.	Has there been a comparison with other methods that reduce the number of queries or speed up DETR? What challenges are there in transferring these methods to 3D object detection? How about the tested efficiency?

### Soundness
2

### Presentation
3

### Contribution
2
