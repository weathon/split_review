# Same Accuracy, Twice As Fast: Continual Learning Surpasses Retraining From Scratch

- Decision: Reject
- Scores: 3, 6, 3, 5, 3

## Abstract
Continual learning aims to enable models to adapt to new datasets without losing performance on previously learned data, often assuming prior data is no longer available. However, in many practical scenarios, both old and new data are accessible. In such cases, good performance on both datasets is typically achieved by abandoning the model trained on the previous data and re-training a new model from scratch on both datasets. This training from scratch is computationally expensive. In contrast, methods that leverage the previously trained model are worthy of investigation as they could significantly reduce computational costs. Our evaluation framework quantifies the computational savings of such methods while maintaining or exceeding the performance of training from scratch. We identify key optimization aspects - initialization, regularization, data selection, and hyper-parameters - that can each contribute to reducing computational costs. For each aspect, we propose effective first-step methods that already yield substantial computational savings. By combining these strategies, we achieve up to 2.7x reductions in computation time across various computer vision tasks, highlighting the potential for further advancements in this area.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work "proposes" a continual learning framework/analysis based on optimization to reduce the computational cost during the continual learning of models.

### Strengths
The authors conduct a thorough analysis of the SGD optimization scheme on a continual learning (CL) setup and open new insights into a new direction. The analysis is limited and not thorough. The literature on CL has moved way ahead, considering the core data and model assumptions that this work has considered. However, such an analysis is also important.

### Weaknesses
The core contributions of this work are completely minimal and rely on the analysis of standard deep-learning optimization schemes, especially with regard to the parameter update rule, in a continual learning (CL) scheme. The results are not dense and the experimental setup is very basic. Rigorous experiments are to be done on a wide scale. The authors claim that "old" and "new" data are usually available, which is very impractical by today's standards. Please take a look at recent works [1, 2, 3]. However, many works have proposed CL methods with no access to past data + (data and parametric)-efficient ways. This work doesn't meet the standards of an ICLR submission, however. The analysis is decent, but the experiments are not thorough with no clear "proposed method". My suggestion would be to conduct such analysis on a larger scale, covering a wide range of cases - training setups (CIL, TIL), model backbones, challenging scenarios, etc.

### Questions
1. It is not clear to me how important saving "computational time" is. Could the authors benchmark against FLOPs? 
2. If the "old" data isn't available, can the authors benchmark their work against prompt-based CL methods like L2P [1]? Or can a similar analysis be done with a ViT backbone?
3. Why do the authors use a 70+30 split on CIFAR-100? How about a uniform split in tasks?
4. How would the analysis hold with rapid domain shifts? 
5. Is there a typo in Fig 6 caption/analysis? In the main text (4.2), a CIFAR-100 (70+30) was used.
6. How is the analysis with an Adam/AdamW optimizer? Is this analysis model invariant and holds everywhere?



[1] Wang, Z., Zhang, Z., Lee, C.Y., Zhang, H., Sun, R., Ren, X., Su, G., Perot, V., Dy, J., Pfister, T.: Learning to prompt for continual learning. In: CVPR. pp. 139–149

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers a new continual learning setting where the old data and new data are both accessible for training and the efficiency is the main concern. For each task, the straightforward baselines include training the model from scratch with both old and new data and fine-tuning the model trained on old data with new data. The former serves as a strong baseline considering the accuracy but is computationally expensive. The latter suffers from a much worse accuracy. Thus, this paper investigates a bag of tricks used in SGD training to improve both the accuracy and efficiency of the way that fine-tunes the model pretrained on old data. Empirical study verifies the effectiveness of proposed method.

### Strengths
- The paper is generally well-written and easy to follow. 

- The empirical results are good. 

- It verifies a bag of tricks which may help the practitioners to continually train a model with satisfactory accuracy and efficiency.

### Weaknesses
 - Some details are not clear. For example, in Fig. 3, the curve corresponding to the legend "L2" means "scratch + L2" or "naive + L2"? If it is the later, how about the curve of "scratch + L2"? 

  I don't quite understand the descriptions from Line 415-419. I am confused about how the authors compute different costs. Besides, for 
  Fig. 6, I don't understand what the curve between $T_{i-1}$ and $T_i$ means. And I am not clear how the authors draw the curve. 

- There is a typo in Eq. (6), the $x$ and $y$ on the right side of equal sign should be $x_j$ and $y_j$. 

- For the batch composition trick, it can be shared across the fine-tuning way and the scratch way. From the empirical results shown in Table 1, applying this trick to the "continuous" and the "scratch" yields the same speed considering $L_{100}$ and almost the same speed considering $L_{99}$. Also, by comparing "init+reg" and "init+reg+data" (continuous), it seems that the batch composition trick does not work. To me, the results are reasonable. I don't understand why batch composition can yield larger gain when combined with continuous model compared to that combined with scratch model. Do the authors have any explanations for this?

### Questions
- The authors applied a bag of tricks which may be proposed in previous works to the considered continual learning setting. Can the authors provide any insights why those tricks work in the continual learning setting? Are there any other tricks which may also benefit the accuracy and efficiency of continual learning?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles the practical aspect of continual learning setup, wherein access to both new and old data exists and the major cost of training newer models is on the computation side. With the set of previously known techniques, authors show that when used,  in combination they provide significant speed-up in the training of a new model under the described continual learning paradigm. The experiments are done on the standard datasets which shows the validity of the claims.

### Strengths
1. This method shows the combination of model initialization, learning rate scheduling, batch composition and the loss function, affect the rate at which the model learns on new data.
2. Though the method is simple and a combination of known techniques, it provides good improvement on some of the datasets.
3. The paper is well-written and easy to read.

### Weaknesses
1. The major issue with this work is how generalizable are the claims on the varied set of backbone architecture and datasets. For eg. ViT backbones, downstream tasks, like object detection or segmentation, or varied datasets like ImageNet or wider domain shifts like in WiLDS[1]. It will make the claims stronger with more extensive results. As section 4.3 suggests the claim might not hold under domain shifts.
2. Will the method benefit already existing CL methods(ones mentioned in Sec1.2)? if the claims are general, it should benefit the CL methods and one can hope for the best of both, performance-boost and computation efficiency.
3. The comparisons with existing CL methods are missing in the experiments in terms of performance and compute efficiency. $L_r$ can be computed for them too. This makes the assessment of the contribution difficult.
4. The test accuracy is reported for combined new and old data. It will be better to see the accuracy on them separately.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the problem of efficient model training through the lens of continuous training. It focuses on four aspects: initialization, regularization, data selection and hyper-parameter tuning. For each aspect, it introduces specific techniques to enhance the training efficiency. The experiments are performed on several image classification datasets using a ResNet-18 network. By integrating all the proposed methods, the paper demonstrates improved performance while reducing training costs.

### Strengths
1. It is interesting to explore efficient training from the perspective of continuous training. 
2. This paper provides an initial investigation using different training techniques and shows their effectivenss. The strategies employed perform well even in multi-step training scenarios.
3. This paper is easy to follow.

### Weaknesses
1. This paper only demonstrates its feasibility on small-scale models and datasets. However, efficiency gains are more critical when dealing with large models and datasets. Please also provide the validation on larger model and datasets. It would be better to see results on ImageNet-1k with ViTs and comparing with training from scratch or other pre-train based continual leanring baselines such as [A].
2. The use of the term "continual learning" may be misleading, as it conficts with its wildly accepted meaning in the field. It would be better to use other phrase like "continuous training" instead. Additionally, providing a clear definition of the task is necessary to avoid confusion.
3. There are some discrepancies in the reported results. For instance, in Table 2(b), the cost reduction ratios are ×1.61 and ×1.45 for CIFAR-100 (70+30) with full data, and ×4.74 and ×4.34 with 25\% data. However, in Table 1, the reported values are ×1.96, ×1.69, and ×5.73, ×5.32, respectively. These inconsistencies should be addressed and clarified.

### Questions
Line 315, "More formally, they define learning speed ls of a sample $x_j$ as the epoch $e$ in which sample is classified correctly" is unclear. $e$ is not used in Equation 6.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Overall, this paper first defines a new setting of "continual learning", where the old data, the current data, and the model that has been trained on the old data are all accessiable. After that, it presents a bag of tricks that can enable the model to achieve much faster convergence in this new setting of "continual learning".

### Strengths
Overall, I believe that the problem that this paper aims to handle is an important problem. In other words, when we already have a model that has been trained over part of the dataset, it is a waste to simply re-train everything from scratch.

Also, the paper present this problem in a well-motivated way.

### Weaknesses
Overall, I believe that this paper is not ready to be accepted. Below are my concerns.

1. The main concern I have w.r.t. this paper is over its defination that its setting is a ``continual learning'' setting. Specifically, correct me if I am wrong, yet, based on my understanding of continual learning, the catastrophic forgetting is always a key problem in this area, no matter over which of its sub-settings such as class-incremental learning, domain-incremental learning, and so on. Yet, with the access of the old data, the paper seems to define a continual learning setting that is essentially different from the general continual learning concept. This worries me that whether this paper fits itself in a wrong area for the research community. For example, if my understanding is not wrong, warm starting is a method that is kind of just solving the problem that this paper aims to solve. Yet, no one would recognize warm starting as a continual learning method.

2. Furthermore, the paper highlights that it makes several "first-step methods". Yet, I am confused over the first step here. If I am not wrong, the paper seems to be highly inspired by previous methods and thus seems to be closely related to them. For example, the initialization part seems to be closely related to Ash & Adams (2020), the batch composition part seems to be closely related to Hacohen & Tuytelaars (2024), and so on. Specifically, while I can admit that adapt some method to a new area is a contribution, as mentioned in my previous concern, I doubt whether the authors do propose a "new" setting, not to say that the contribution behind adaptation can be small.

3. My last concern lies in the generalizability of the proposed method. Specifically, it seems to me that the method just try some approaches and observe that they work on a few (small) datasets. I am not sure whether this can well justify and demonstrate the effectiveness of the proposed method.

### Questions
Overall, I believe that this paper is not ready to be accepted. Below are my concerns.

1. The main concern I have w.r.t. this paper is over its defination that its setting is a ``continual learning'' setting. Specifically, correct me if I am wrong, yet, based on my understanding of continual learning, the catastrophic forgetting is always a key problem in this area, no matter over which of its sub-settings such as class-incremental learning, domain-incremental learning, and so on. Yet, with the access of the old data, the paper seems to define a continual learning setting that is essentially different from the general continual learning concept. This worries me that whether this paper fits itself in a wrong area for the research community. For example, if my understanding is not wrong, warm starting is a method that is kind of just solving the problem that this paper aims to solve. Yet, no one would recognize warm starting as a continual learning method.

2. Furthermore, the paper highlights that it makes several "first-step methods". Yet, I am confused over the first step here. If I am not wrong, the paper seems to be highly inspired by previous methods and thus seems to be closely related to them. For example, the initialization part seems to be closely related to Ash & Adams (2020), the batch composition part seems to be closely related to Hacohen & Tuytelaars (2024), and so on. Specifically, while I can admit that adapt some method to a new area is a contribution, as mentioned in my previous concern, I doubt whether the authors do propose a "new" setting, not to say that the contribution behind adaptation can be small.

3. My last concern lies in the generalizability of the proposed method. Specifically, it seems to me that the method just try some approaches and observe that they work on a few (small) datasets. I am not sure whether this can well justify and demonstrate the effectiveness of the proposed method.

Given my above concerns, I believe that this paper is not ready to be accepted in its current version.

### Soundness
2

### Presentation
2

### Contribution
1
