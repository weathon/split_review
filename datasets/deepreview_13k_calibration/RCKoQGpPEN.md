# MaXTron: Mask Transformer with Trajectory Attention for Video Panoptic Segmentation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Video panoptic segmentation requires consistently segmenting (for both ‘thing’ and ‘stuff’ classes) and tracking objects in a video over time. In this work, we present MaXTron, a general framework that exploits Mask XFormer with Trajectory Attention to tackle the task. MaXTron enriches an off-the-shelf mask transformer by leveraging trajectory attention. The deployed mask transformer takes as input a short clip consisting of only a few frames and predicts the clip-level segmentation. To enhance the temporal consistency, MaXTron employs within-clip and cross-clip tracking modules, efficiently utilizing trajectory attention. Originally designed for video classification, trajectory attention learns to model the temporal correspondences between neighboring frames and aggregates information along the estimated motion paths. However, it is nontrivial to directly extend trajectory attention to the per-pixel dense prediction tasks due to its quadratic dependency on input size. To alleviate the issue, we propose to adapt the trajectory attention for both the dense pixel features and object queries, aiming to improve the short-term and long-term tracking results, respectively. Particularly, in our within-clip tracking module, we propose axial-trajectory attention that effectively computes the trajectory attention for tracking dense pixels sequentially along the height- and width-axes. The axial decomposition significantly reduces the computational complexity for dense pixel features. In our cross-clip tracking module, since the object queries in mask transformer are learned to encode the object information, we are able to capture the long-term temporal connections by applying trajectory attention to object queries, which learns to track each object across different clips. Without bells and whistles, MaXTron demonstrates state-of-the-art performances on video segmentation benchmarks. Code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors mainly study the clip-level video panoptic segmentation. They propose a new framework using Mask Xformer with trajectory attention, named MaXTron. It includes within-clip and cross-clip tracking modules, to use trajectory attention. The experimental results show the effectiveness of their proposed model.

### Strengths
This paper is well-written and easy to follow. The idea of using trajectory information to help the segmentation and decompose the attention into height and width in two directions, greatly reducing the computational complexity. They have done comparison and ablation studies to validate their proposed components.

### Weaknesses
The figures might not be easy to follow. For example, in Fig. 3, they show H and W-axis attention maps of one point. It would be much better, if they also show how to get the probabilistic path of a point between frames and what the whole attention maps for static and dynamic points. Besides, the authors should show the details in trajectory attention module and temporal ASPP in Fig. 4 and it can help readers to understand. 

The main contribution of this work is the trajectory based within-clip and cross-clip module, which might be limited and insufficient for this conference, even if the authors could clearly introduce their modules using Fig. 3 and 4 after revision. 

In the experiment, the authors are suggested to add some examples to show the attention maps and how to get the trajectories or the trajectories might not be perfect.

### Questions
The main contribution of this work is the trajectory-based within-clip and cross-clip modules, which might be limited and insufficient for this conference, even if the authors could clearly introduce their modules using Fig. 3 and 4 after revision.

In the experiment, the authors are suggested to add some examples to show the attention maps and how to get the trajectories or the trajectories might not be perfect.

It would be much better if they also showed how to get the probabilistic path of a point between frames and what the whole attention maps for static and dynamic points.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed trajectory attention based mask transformer for video panoptic segmentation. Specifically, two types of tracking modules (within-clip and cross-clip tracking) are proposed to improve the temporal consistency by leveraging trajectory attention. The within-clip tracking module, an axial-trajectory attention is proposed for effectively computing the trajectory attention for tracking dense pixels sequentially along the height- and width-axes, while the cross-clip tracking module is used to capture the long-term temporal connections by applying trajectory attention to object queries. The experimental shows that the proposed solution is able to help boost the performance of existing solutions (e.g., Video-kMax and Tube-Link) on multiple datasets.

### Strengths
1. The proposed solution sounds solid. (1) Using trajectory attention to force the model pay more attention spatially and temporally on trajectories (maybe simply on pixel trajectories) while doing video segmentation sound solid in theory. The attention should be able to provide extra useful information to the model. (2) Splitting the trajectory attention along different axes (horizontal and vertical) indeed helps reduce the complexity while calculating attention. 
2. The experimental results on multiple datasets and models prove that the proposed solution works in varying application scenarios. 
3. This paper is well-organized, which help readers easy to read and understand. Expecially, there are more implementation details and results reported in the appendix, which helps readers better understand their work and the performance.

### Weaknesses
1. It will be better to report some failure cases. It will be helpful if the authors could report some failure cased that caused by applying the proposed MaxTron. In this case, readers will better understand their work and the performance, which may inspire more ideas along this direction. 
2. The proposed solution sounds like an add-on to the existing solutions, which was inspired by other works (e.g., Patrick et al. 2021). The novelty may be incremental.

### Questions
1. What if we change the number of frames within one video clip? Is there any positive / negative impact on the model performance? Is there any guidances (or suggestion) of how many frames should be selected while spliting the video?
2. Does the proposed solution perform differently if we (1) process all continuous frames or (2) only process key frames (with some down-sampling temporally)? The later operation will speed up motions in videos.

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a novel panoptic segmentation method, namely MaXTron, which enhances temporal consistency by the proposed within-clip and cross-clip tracking modules. Axial-trajectory attention is the essential component of the introduced tracking modules, which aims at associating objects meanwhile reducing computational complexity.Experimental results have shown state-of-the-art performance on video segmentation benchmarks.

### Strengths
It sounds interesting to conduct in-clip tracking and cross-clip tracking via axial-trajectory attention.

Association with non-overlapping clips is more efficient than previous overlapping-based methods. 

The results are promising.

### Weaknesses
The writing of sec.3 (method) should be improved. It‘s a bit confusing about the implementation details.

Besides the performance, it is suggested to provide the cost, e.g. training cost and inference speed, of integrating the proposed model into existing methods.

Besides the overall performance, a deeper analysis is expected. For instance, how does the association capability improve after integrating the proposed modules into an off-the-shelf method?

### Questions
see weakness

### Soundness
3 good

### Presentation
2 fair

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
This paper tackles the well-known video task, video panoptic segmentation, and presents MaXTron. From the inherent property of the VPS task that comprises other video segmentation tasks such as VSS and VIS, MaXTron can be considered as a general video segmentation framework.
The authors points out a couple of challenges of the video segmentation tasks, and target to alleviate such challenges. Specifically, per-clip segmentation methods (which MaXTron also belongs to) have put efforts in improving inter-clip and intra-clip predictions. In order to improve inter-clip predictions, the authors suggest the Within-Clip Tracking Module, which consists of a stack of multi-scale deformable attention followed by Axial-Trajectory Attentions. For intra-clip association, MaXTron fully leverages the object queries that possess object-level information, and insert into the Cross-Clip Tracking Module that has Trajectory Attention and Temporal ASPP.
Finally, utilizing the presented modules, MaXTron achieves compelling results, demonstrating state-of-the-art accuracy.

### Strengths
This paper has a clear structure that ease the readers to follow and understand which components are being used. 
The authors points out important problems of the video segmentation tasks and each module is designed with a specific goal.
Combining them all, MaXTron achieves improvements in the accuracy on multiple benchmarks, highlighting the effectiveness of each module.

### Weaknesses
The main concern that has not fully been addressed is the significance of the claimed contributions. For the past few years, numerous works have been published to address the quadratic computation issue of self-attention. There are many approaches that can handle the CUDA OOM issue such as reducing the scope of attention, decomposing the attention, reducing the number of tokens by taking hierarchical approach, and so on. A lot of those works have already presented such approaches, and they also provide customized CUDA codes that actually makes the model feasible. Compared to those works, I believe the axial-trajectory attention of this paper is much of a naive extension of self-attention: limiting the number of visiting tokens. In order to prove its effectiveness, the authors should have provided thorough analysis of the module and a comparison between temporal extension of existing transformer variants, not only the MSDeformAttn which does only 2D spatial encoding. To list a few, here are some of the references that I believe that could have been simply extended to a spatio-temporal version, and be applied to the VPS task.
    - Bertasius et al. Is Space-Time Attention All You Need for Video Understanding
    - Ramachandran et al. Stand-Alone Self-Attention in Vision Models
    - Hassani et al. Neighborhood Attention Transformer
    - Beltagy et al. Longformer: The Long-Document Transformer
    - Xie et al. SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers
    - Pan et al. Slide-Transformer: Hierarchical Vision Transformer with Local Self-Attention

Especially, since the first reference can be directly applied, what is the benefit (accuracy & efficiency?) of the proposed module over Bertasius et al?



- Thank you for pointing out that the authors do not claim ASPP as their novelty. However, I do not view the application of ASPP as an enough contribution. It is true that there are not many applications to the dense video pixel-level prediction tasks. However, given that the VPS task is not a significantly popular task, and ASPP is an extremely well-known module in the vision domain, I cannot agree with the authors that it can be considered as a major contribution. Indeed, it is very obvious that ASPP can be seamlessly integrated into any module. I do not mean that this work should not have used the transformer decoder. To clarify, I believe the contributions for the overall architectural design is limited, e.g., using the transformer decoder is to be expected.

-----

- Thanks for providing the comparison to VITA. Despite I understand that the time can be limited for experimenting during the rebuttal period, my remaining concern is that it is only experimented on top of Video-kMaX.

----

- From the 15 GFlops reduction over VITA, the authors mentioned that the presented module is more computationally efficient. Then, as shown in Table C3, it seems like MaXTron is extremely heavier than Video-kMaX (more than 30% increase).
    - What’s the GFlops and FPS of other state-of-the-art methods such as TarVIS, VITA, DVIS? Referring to the DVIS paper, DVIS has much less params even than Video-kMaX (which is much lighter than MaXTron).
        - I believe the FPS comparison can be reported if they are experimented on VIS benchmarks.
        - Since MaXTron also provides accuracies on VIS datasets, it might be easier and more straight-forward to compare on the VIS benchmarks.

### Questions
How much are the FLOPs and FPS of MaXTron compared to other methods?
What's the statistical significance, i.e. how many runs were executed for reporting the numbers? Are the numbers mean/median of multiple trials?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
