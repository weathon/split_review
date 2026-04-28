# Closed-loop Scaling Up for Visual Object Tracking

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Thanks to the principles of the scaling law, current neural networks have experienced remarkable performance improvements. While much of the existing research has concentrated on upstream pretraining, the application of the scaling law to downstream vision tasks remains underexplored. Understanding the scaling law in downstream tasks can aid in the design of more effective models and training strategies. Thus, in this work, we aim to investigate the application of the scaling law to downstream vision tasks. Firstly, we explore the impact of three key factors of scaling law: training data volume, model size, and input resolution. We empirically verify that increasing each of these factors can lead to performance enhancements. Secondly, to address naive training's optimization challenges and lack of iterative refinement, we introduce DT-Training which leverages small teacher transfer and dual-branch alignment to further exploit model potential. Thirdly, building on DT-Training, we propose a closed-loop scaling strategy to incrementally scale the model step-by-step. Finally, our scaled model exhibits strong ability and outperforms existing counterparts across diverse test benchmarks. Extensive experiments also reveal the robust transfer ability of our model. Moreover, we validate the generalizability of the scaling law and our proposed DT-Training on other downstream vision tasks, reinforcing the broader applicability of our approach. We hope that our findings can deepen the understanding of the scaling law in downstream tasks and foster future developments on downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper explores the application of the scaling law to downstream vision tasks, specifically visual object tracking. The authors investigate the impact of three key factors: training data volume, model size, and input resolution. They introduce a novel DT-Training approach that leverages small teacher transfer and dual-branch alignment to enhance model performance. Additionally, they introduce a closed-loop scaling strategy for incremental model scaling. The paper demonstrates  performance improvements over existing methods across various benchmarks and validates the generalizability of the proposed methods to other downstream vision tasks.

### Strengths
The paper provides a thorough analysis of the scaling law's impact on visual object tracking, covering multiple dimensions (data volume, model size, input resolution). The introduction of DT-Training and the closed-loop scaling strategy are novel contributions that address optimization challenges and enable iterative refinement. The authors conduct extensive experiments on diverse benchmarks, validating the robust transfer ability and generalizability of their model. The paper demonstrates the applicability of the proposed methods to other downstream vision tasks, such as object detection, further strengthening the contribution. The paper is well-organized and clearly written, making it easy to follow the methodology and results.

### Weaknesses
The computational cost and resource requirements of the proposed methods (especially the closed-loop scaling strategy) should be discussed in more detail. This information is crucial for practical applications. The sensitivity of the model to hyperparameters, particularly those involved in the DT-Training and closed-loop scaling, should be explored and reported. The paper could benefit from additional experiments or case studies in real-world scenarios to demonstrate the practical utility of the proposed methods. The limitations of the proposed approach and potential directions for future research should be more explicitly discussed. It is strange to utilize a smaller model to guide the training of a larger model.

### Questions
1. Could the authors provide more details on the specific steps and criteria for the closed-loop scaling strategy?
2. How does the computational cost of the proposed methods compare to existing approaches, especially in real-time applications?
3. What are the main hyperparameters involved in the DT-Training and closed-loop scaling, and how sensitive is the model to these parameters?
4. Could the authors discuss the potential limitations of the proposed approach and suggest directions for future research?
5. Why do the authors utilize a smaller model to guide the training of a larger model, not using larger model as teacher?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors first discovered through experiments that the scaling law is also effective on downstream tasks. However, the improvement brought by conventional training methods on larger models, data and resolution is limited. Therefore, the authors propose a closed-loop training method to unleash the effect of the scaling law. The proposed traning method uses a small teacher transfer and a dual-branch alignment module to iterate step by step.

### Strengths
[1] The study problem is interesting and the solution makes sense.
[2] The ablation comparison experiments are well designed and the experimental results also prove the effectiveness of the proposed method.
[3] The studied problem is inspiring for other tasks, and the proposed method also has good generalization ability for other tasks.

### Weaknesses
[1]Although the proposed training method seems to show that expanding data and models can bring better results, there needs to be a balance between the cost of consumption and the improvement brought by the model. The author may discuss this point in the experiment.
[2] The author can describe the training steps in detail, when and how to increase the size of the model and the training data, in an end-to-end training process.

### Questions
[1] Is there an upper limit to the scaling law for downstream tasks?
[2] Can the proposed training method speed up the convergence? Perhaps the authors could discuss this.

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
5

### Summary
This paper explores the application of the scaling law to downstream vision tasks, with the goal of enhancing the effectiveness of larger, task-oriented models. Specifically, the authors investigate the impact of three key factors on visual object tracking: training data volume, model size, and input resolution. They observe that performance improvements tend to saturate as models grow larger. To further unlock the potential of large models, the authors introduce a novel training method called DT-Training. This method leverages small teacher transfer and dual-branch alignment to overcome optimization challenges and enable iterative refinement. Building on DT-Training, they propose a closed-loop scaling strategy to incrementally scale the model. The results demonstrate that the scaled model outperforms existing methods across various benchmarks and exhibits strong transferability and generalizability.

### Strengths
I agree with the authors that exploiting the scaling law in fundamental vision tasks is both necessary and interesting. The paper effectively identifies the bottleneck in training large models for visual tracking and proposes a framework to successfully mitigate this gap. The evaluation is comprehensive, performed across various benchmarks, and demonstrates the effectiveness of the proposed method. Additionally, the authors provide preliminary evidence of the method's generalizability to other tasks, which is a valuable contribution.

### Weaknesses
Despite the aforementioned admiration, I still have some concerns regarding the motivation and methods presented in the paper.

- Choice of Task: It is unclear why the authors chose visual tracking as the primary target. Object detection, being a more fundamental task, might have been a more suitable choice for exploring the scaling law. The class-agnostic nature of tracking, while simplifying certain aspects, may obscure the impact of scaling on semantic understanding, which is crucial for many vision tasks. A more detailed justification for this choice, considering the broader implications for scaling in vision, is needed.

- Efficiency Concerns: Visual tracking requires high efficiency, and despite the improvements achieved by the proposed method, the closed-loop training process introduces significant computational costs. It is questionable whether such extensive resources and a complex training process are justified for learning a larger model. In other words, the proposed framework may be overly complicated. The paper lacks a thorough analysis of the trade-offs between performance gains and the increased computational burden, especially considering the real-time constraints often associated with tracking applications. The computational cost of the iterative refinement process, specifically the dual-branch alignment, needs to be quantified and compared against simpler training strategies.

- Benchmark Evaluation: Collecting and evaluating existing benchmarks, while useful, should not be considered a major contribution, as it does not introduce new knowledge to the field. Moreover, recent datasets like VAST [1], which contain a larger number of videos and present greater challenges, should be a better choice?

- Comparison with Prior Work: Previous work, such as LoRAT [2], has also explored how to leverage larger models in visual tracking. The proposed method is more complex, yet it does not outperform LoRAT in key benchmarks. For instance, LoRAT-L384 achieves a success rate of 75.1% in LaSOT, while the proposed method only reaches 73.1%. A more detailed comparison, including computational costs and performance across a wider range of benchmarks, is necessary to fully assess the advantages of the proposed method over existing approaches.

### Questions
- Please provide a detailed computational cost analysis.
- Please provide an evaluation on the VAST dataset.
- Please compare the proposed method with LoRAT.

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
4

### Summary
In this article, the authors propose applying the scaling law to downstream tasks in computer vision with the aim of obtaining more efficient models and training strategies. Specifically, they explore three scaling factors, introduce a novel training approach called DT-Training(which contains a small teacher transfer and dual-branch alignment), and then propose a closed-loop scaling strategy. These methods effectively improve the performance of the tracker, demonstrating the potential of the scaling law in downstream tasks.

### Strengths
1.This paper introduce DT-Training which leverages small teacher transfer and dual-branch alignment to further exploit model potential.
2.The authors proposed a closed-loop scaling strategy to incrementally scale the model step-by-step.
3.The proposed tracking method achieved competitive performance on most dataset.

### Weaknesses
1.The motivation is not clear enough: from the abstract, I cannot understand what specific benefits applying the scaling law to downstream tasks can bring, nor what problems it addresses in existing tasks. Furthermore, the three points you mentioned—how are they related to the scaling law?

2.It is not easy to understand how your work goes in the tasks, because I cannot even see what scaling law specifically is in your Introduction. The meaning of your model always confuses me, such as the closed-loop scaling strategy, and I had to look for answers from every corner.

3.According to your statements in abstract and introduction, it’s hard to convince me the methods you add are reasonable and do make some differences, cause it's just like a flash of inspiration that you want to try them in a downstream task.

4.The proposed method lacks novelty.
a)The impact of image input size, model parameter size, and training data volume on object tracking is significant, as evidenced by popular trackers such as OSTrack [1] and ODTrack [2]. However, the paper only provides a simple comparison of model scales (e.g., Base, Large) in terms of their impact on tracking performance, without offering detailed insights into how specific increases in parameter size affect the tracker.
b)The teacher-student model is a commonly used knowledge distillation method, widely applied in lightweight tasks. In object tracking, several trackers also employ this approach, such as Mixformer-V2 [3] and AttTrack [4].

5.The experimental results are not detailed enough and lack comparison with the latest trackers. Additionally, in line 287 on page 6, you mention using OSTrack [4] as the baseline and expanding the training dataset. However, this led to a drop in AUC from 69.1 to 68.4. This result seems to contradict your claim that expanding the training dataset improves performance.

### Questions
1.According to your statement, the performance always improves consistently and fully harnessing its ability. But the benefits of specifically each method you expressed are still vague. What’s the detailed potential of the model and how on earth does your work unlock the model’s potential?

2.The structure shown in Figure 2 is a little difficult for readers to understand. Maybe you should explain it more specific and clear.

### Soundness
2

### Presentation
1

### Contribution
2
