# CO-MOT: Boosting End-to-end Transformer-based Multi-Object Tracking via Coopetition Label Assignment and Shadow Sets

- Decision: Reject
- Scores: 6, 8, 6, 3

## Abstract
Existing end-to-end Multi-Object Tracking (e2e-MOT) methods have not surpassed non-end-to-end tracking-by-detection methods. One potential reason is its label assignment strategy during training that consistently binds the tracked objects with tracking queries and then assigns the few newborns to detection queries. With one-to-one bipartite matching, such an assignment will yield an unbalanced training, \textit{i.e.}, scarce positive samples for detection queries, especially for an enclosed scene, as the majority of the newborns come on stage at the beginning of videos. Thus, e2e-MOT will be easier to yield a tracking terminal without renewal or re-initialization, compared to other tracking-by-detection methods. To alleviate this problem, we present Co-MOT, a simple and effective method to facilitate e2e-MOT by a novel coopetition label assignment with a shadow concept. Specifically, we add tracked objects to the matching targets for detection queries when performing the label assignment for training the intermediate decoders. For query initialization, we expand each query by a set of shadow counterparts with limited disturbance to itself. With extensive ablations, Co-MOT achieves superior performance without extra costs, \textit{e.g.}, 69.4\% HOTA on DanceTrack and 52.8\% TETA on BDD100K.  Impressively, Co-MOT only requires 38\% FLOPs of MOTRv2 to attain a similar performance, resulting in the 1.4$\times$ faster inference speed.  Codes are attached for re-implementation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces CO-MOT, a method that enhances the performance of end-to-end Transformer-based MOT. It addresses issues in the existing framework where label assignment fails to fully utilize detection queries due to the exclusive nature of detection and tracking queries. To overcome this, a coopetition alternative is proposed for training intermediate decoders. Additionally, a shadow set is developed to augment queries and mitigate training imbalances caused by one-to-one matching. The experiments are conducted on MOT17, BDD100k and DanceTrack.

### Strengths
+ This paper mentioned that there is a large amount of post-processing in non-end-to-end methods in the MOT field, which leads to difficulties in parameter tuning in application. In this paper, some improvements have been made based on existing end-to-end methods, resulting in certain speed and accuracy improvements.

+ This paper analyzes the shortcomings of existing e2e-MOT models and proposes a new network design strategy based on the analyses.

### Weaknesses
- The layout of the article is quite chaotic. Figure 1 is used as an example in the method introduction, but it is too far from the text information. For another example, in Section 3.2 of the introduction of strategies and methods, formulas are mixed in a large paragraph without a comprehensive formula or image description, making it difficult for readers to understand. The reviewer must refer to the paper of the baseline tracker MOTR for a comprehensive understanding. The authors should re-organize the method introduction and include a detailed figure to highlight the technical improvements of the new approach, including both the label assignment and shadow set.

- The comparisons with more tracking approaches on the BDD100k or DanceTrack datasets are required to demonstrate the performance improvement.

### Questions
Please see the Weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper works on an end-to-end Multi-Object Tracking problem via a query-based Transformer, which assumes that the existing label assignment leads to scarce positive samples for detecting newborns. With this limitation in training, this paper observes a tracking terminal without renewal or re-initialization compared to other tracking-by-detection methods. To remedy this issue, this work presents Co-MOT by matching detection queries to all the tracked and untracked targets. Additionally, each query is augmented by a set with limited disturbance to itself. CO-MOT, with extra costs, achieves 69.4 HOTA on DanceTrack and 52.8 TETA on BDD100K, making it 1.4 times faster than the previous approach MOTRv2.

### Strengths
Deep observation of the existing approaches: This paper provides qualitative results in Figure 1 and quantitative results in Table 1 to bring the readers to what has been done to the existing e2e-MOT via Transformer. The bipartite matching label assignment in the previous approaches has a limitation regarding the video task, compared to the image task, such as object detection. From this perspective, this work involves the inherent property of the e2e-MOT via Transformer and offers a promising solution to the limitation. The superior performance of the proposed method is inspiring, which only requires fewer FLOPS of MOTRv2 to achieve a similar performance. I reckon this work reveals the core problem of the Transformer-based e2e-MOT.

Simple and effective solutions: The paper reveals that the target assignment on detection queries is scarce due to the exclusive tracking queries, leading to unbalanced training. The proposed coopetition label assignment solves this problem by allowing the detection queries to match all the targets in the intermediate decoders except the last decoder. This simple solution can effectively recall newborn detection in the intermediate decoders while keeping standard MOT in the final outputs.  In addition, the shadow concept is introduced to augment each query in a feature-augmentation manner. A bulk of ablations are provided to demonstrate the effectiveness of each proposed solution.

### Weaknesses
Missing experiments on more models: In Section 3.2, this paper mentions that we revisit the Tracking Aware Label Assignment (TALA) used to train end-to-end Transformers such as MOTR and TrackFormer for MOT. However, all the ablations are conducted on MOTR. I cannot find evidence that COLA and shadow work on other models like TrackFormer. The authors should provide results of TrackFormer on two datasets at least to make the proposed solutions more solid.

Comparison of failure cases: The failure cases shown in Figure 5 are the common cases of all the Transformer-based approaches.  The authors should provide the failure cases of previous approaches and denote which kind of case has been solved by CO-MOT.

### Questions
In Table 2, the authors categorize all the methods into Non-End-to-end and End-to-end. What are the exact definitions of these two categories? Also, it will be better to list all the methods using Transformer. 

In Figure 4, do the FLOPs of the MOTR include the YOLOX detector? What are the specific numbers of parameters for different approaches? The specific number of parameters should be indicated in Figure 4. For example, the number can be placed in circles.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an end-to-end Transformer-based MOT method. It introduces a coopetition alternative for training the intermediate decoders, and also develops a shadow set as units to augment the queries. Experimental results on some public datasets demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper is well written and organized. The S-COLA is also clearly explained.
2. Experimental results on some public datasets demonstrate the effectiveness of the proposed method.

### Weaknesses
1. For the tracking queries and the detection queries, they both self-attend each other and then cross-attend the image feature tokens. Intuitively, all the queries can perceive the whole image, and it is not good enough to split them into two parts, which may degrade the detection results.

2.  Why not evaluate the proposed method on the crowded dataset MOT20? In crowd scenes, the tracking query has the similar semantic information with the detection query, and may fail to assign correct label in crowd scenes.

3. In Table 1, the authors point out that the detection result of MOTR can be improved by removing the tracking queries. How about the proposed CO-MOT? If CO-MOT is only used as a detection task, and whether the tracking performance can be further improved?

4. It is better to evaluate the effect of the number of decoders L on the tracking performance.

5. Pease reorganize the formats of the references, and make them consistent.

### Questions
See the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper is about using Transformer to perform multi-object tracking task. Authors introduce "coopetition alternative" strategy to train Transformer's decoders, also a "shadow set" is proposed to maintain a set of queries when tracking each object. Experiments are conducted on DanceTrack, BDD100K, MOT17 to compare with prior works.

### Strengths
1) This paper comes with a good motivation by first analyzing the drawbacks transformer based trackers, such as MOTR and MOTRv2, then try proposing some improvements based on that.

2) The idea of using a set of queries to track each object, is interesting. 

3) Results on DanceTrack seems to be strong, e.g. it is comparable to MOTRv2 from Table 2(a) and it is better than a recent work MeMOTR, which is also based on Transformer.

### Weaknesses
1) The performance is not stable across different datasets. For instance, the tracker cannot even achieve comparable performance with existing trackers such as GTR/PA3Former/GRTU on MOT17, which is by far the most widely used and trusted benchmark within MOT community. While authors claim that MOT17 is rather a small dataset to train transformer-based trackers, other ways such as using synthetic dataset[a] could be one option. 

 Also the proposed tracker performs worse than the major baseline MOTRv2, which is also transformer-based, in terms of IDF1 and HOTA. In this case, it is a bit hard to justify that authors are making a direction towards improving MOTRv2. 

In fact, I would stay away with a rather heavier tracker (Transformer with multiple layers and many parameters) that gives even worse performance on MOT17 than light-weight tracking-by-detection/regression based trackers that require way less data to train, while still work better on major tracking benchmarks.

2) The current approach lacks some form of interpretability. For example, from this claim "COLA and TALA on the different decoders,", why different label assignment should be used in different decoders? What exactly happened inside the decoder part for Transformer-based MOT, is it solving data association exactly or approximately? It would be more advocated if authors could come up with a more insightful explanation for this, and it will also benefit readers.

3) For the idea of using shadow set, too many engineering tricks such as min, max, operations are used, it would be much better if authors could come up with some mathematical formulations as a technical sound approach to replace these simple heuristics, so as to better justify the use of this method. For example, IMHO, how about borrowing ideas from particle filter, to use importance sampling to maintain a set of queries to track each object?

References:
[a] Motsynth: How can synthetic data help pedestrian detection and tracking? ICCV2021

### Questions
I see in Table 3(a) that adding COLA and shadow set both improves performance than not having them, but this is only tested on DanceTrack, would the COLA and shadow set also work better than not having them at all, on MOT17 validation set?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
