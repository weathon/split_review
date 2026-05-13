# Disentangling Inter- and Intra-Video Relations for Multi-event Video-Text Retrieval and Grounding

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Video-text retrieval aims to precisely search for videos most relevant to a text query within a video corpus. However, existing methods are largely limited to single-text (single-event) queries, which are not effective at handling multi-text (multi-event) queries. Furthermore, these methods typically focus solely on retrieval and do not attempt to locate multiple events within the retrieved videos. To address these limitations, our paper proposes a novel method named Disentangling Inter- and Intra-Video relations, which jointly considers multi-event video-text retrieval and grounding. This method leverages both inter-video and intra-video event relationships to enhance the performance of retrieval and grounding. At the retrieval level, we devise a Relational Event-Centric Video-Text Retrieval module, based on the principle that more comprehensive textual information leads to a more precise correspondence between text and video. It incorporates event relationship features at different hierarchical levels and exploits the hierarchical structure of corresponding video relationships to achieve multi-level contrastive learning between events and videos. This approach enhances the richness, accuracy, and comprehensiveness of event descriptions, improving alignment precision between text and video and enabling effective differentiation among videos. For event localization, we propose Event Contrast-Driven Video Grounding, which accounts for positional differences between different events and achieves precise grounding of multiple events through divergence learning of event locations. Our solution not only provides efficient text-to-video retrieval capabilities but also accurately locates events within the retrieved videos, addressing the shortcomings of existing methods. Extensive experimental results on the ActivityNet-Captions and Charades-STA benchmark datasets demonstrate the superior performance of our method, clearly validating its effectiveness. The innovation of this research lies in introducing a new joint framework for video-text retrieval and multi-event localization, while offering new ideas for further research and applications in related fields.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel task, MVT-RG, and propose the Disentangling Inter- and Intra-VideoRelations method. They develop the relational RE-CVTR module and a EC-DVG module to build relationships between video segments. This approach enhances the richness, accuracy, and comprehensiveness of event descriptions, improving alignment precision between text and video and
enabling effective differentiation among videos.

### Strengths
1. This paper introduce a extend task MVT-RG which focuses on the multi events localization.
2,They build a novel model containing RE-CVTR module and EC-DVG module.

### Weaknesses
1. The experiment metric seems to be different with most of researches for this field.  The wildly used metric is (R@(1,5),IoU = m)
2. The paper uses the 2D map[1] and reconstruction strategy[2] for weakly supervied setting. There are some works based on these paradigms. It is neccessary to introduce them and compare the effectiveness with them.

### Questions
1. This paper introduce a novel task,MVT-RG. However, not all of the dataset has the multi event labeling in a same video. How to solve the problem of dataset?

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
This paper proposes a novel task and a pipeline to address the limitations of single-text (event) queries and effectively handle multi-text (event) queries. The method improves retrieval and grounding performance by combining relationships between videos and internal event relationships. Experimental results on benchmark datasets Charades-STA and ActivityNet Captions demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper introduced a novel task setting, Multi-event Video-Text Retrieval. With utmost limited amount of labeling, it is indeed that the challenge of this task should be huge. This setting would make extensive sense in a real world scenario such as online video searching and item recommendation.

2. Event positioning of the two-level grounding can be applied to other tasks.

3. Outperforms current best methods in experiments. The reproducing of the previous methods is informative.

### Weaknesses
 1. Although the proposed task is highly research-worthy, I don't think the current Video Moment Retrieval (VMR) and Video Corpus Moment Retrieval (VCMR) methods are able to tackle such a difficult task. The previous approach such as JSG is still preliminary, it is certainly not credible to conduct comparative experiments by reproducing them in order to verify the effectiveness of the new method. Therefore, the rationality of the proposed method should be re-considered.
 
2. The comparison is limited to two benchmark datasets, which requires additional experimentation to prove generalizability. Additionally to overview the whole pipeline, I think it may have some error in event localization for certain scenario.

### Questions
1. Although the proposed task is highly research-worthy, I don't think the current Video Moment Retrieval (VMR) and Video Corpus Moment Retrieval (VCMR) methods are able to tackle such a difficult task. The previous approach such as JSG is still preliminary, it is certainly not credible to conduct comparative experiments by reproducing them in order to verify the effectiveness of the new method. Therefore, the rationality of the proposed method should be re-considered.
 
2. The comparison is limited to two benchmark datasets, which requires additional experimentation to prove generalizability. Additionally to overview the whole pipeline, I think it may have some error in event localization for certain scenario.

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
5

### Summary
Considering that existing video-text retrieval methods are largely limited to single-text queries and typically focus solely on retrieval and do not attempt to locate multiple events within the retrieved videos, this paper introduces a new joint framework for video-text retrieval and multi-event grounding, which leverages both inter-video and intra-video event relationships to enhance retrieval and grounding performance. Authors clearly explain the motivation and proposes corresponding methods, and conducts extensive experiments and visualizations to verify them.

### Strengths
1.The motivation of this paper is clearly stated, that is, combining MVT-R and SVT-RG, proposing a novel task named MVT-RG and the corresponding approach.

2.The methodology section is well-written and easy to understand. The proposed method can cover the motivation, including the relationship modeling of multiple queries and the implementation of grounding module.

3.The training and inference are detailedly described. Besides, the datasets, implementation details, and evaluation metrics are also clearly explained.

### Weaknesses
1.There are some errors that need further verification, including but not limited to MV-TRG on line 186 and Fig. 1 on line 276.

2.Lines 52-53 of the paper claim that MeVTR relies on time labels, but to our knowledge this method does not need time labels.

3.Based on the MVTR task defined in the paper, we do not think that MeVTR belongs to this task. We think that the MVTR task defined is more similar to this work (https://arxiv.org/abs/2201.03639).

4.The experiments in this paper are not complete enough.

(a) The proposed model has both retrieval and grounding capabilities, we hope to see the performance of these two capabilities in the experiment respectively instead of just final results. 

(b) The ablation studies only include the ablation of three modules, and there are many details in your approach that need experiments to show their necessity, e.g., each loss in Formula 11 and the necessity of using GCN to model queries relationship. 

(c) As far as we know, the accuracy of multi-query retrieval (directly concat multi-query to retrieval) is much better than that of single query (refer to https://arxiv.org/abs/2201.03639). We remain skeptical whether the method in this paper obtains better results because it uses more query information for retrieval. We think that an implementation of JSG based on multi-query retrieval is the suitable baseline of this paper. 

(d) The proposed model in this paper is relatively complex. It is recommended to present tests and evaluations of the model's computational overhead. 

(e) The paper may also lack the following two aspects of experimentation: visualization of retrieval results and an exploration of the impact of different ranking strategies on the retrieval subtask. 

(f) All the SOTA experimental results in this paper are directly taken from the JSG model's experiments on the Event-level Retrieval subtask. However, the JSG model and its methods are designed for single-event query retrieval, may making such a comparison seemingly unfair. The appropriate approach should be to suitably modify the SOTA models to adapt to the novel task proposed in this paper and to detail the modifications within the manuscript. However, the paper does not mention any adaptation of the SOTA models.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
