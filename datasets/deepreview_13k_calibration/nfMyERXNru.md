# Video Decomposition Prior: Editing Videos Layer by Layer

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
In the evolving landscape of video editing methodologies, a majority of  deep learning techniques are often reliant on extensive datasets of observed input and ground truth sequence pairs for optimal performance. Such reliance often falters when acquiring data becomes challenging, especially in tasks like video dehazing and relighting, where replicating identical motions and camera angles in both corrupted and ground truth sequences is complicated. Moreover, these conventional methodologies perform best when the test distribution closely mirrors the training distribution. Recognizing these challenges, this paper introduces a novel video decomposition prior `VDP' framework which derives inspiration from professional video editing practices. Our methodology does not mandate task-specific external data corpus collection, instead pivots to utilizing the motion and appearance of the input video. VDP framework decomposes a video sequence into a set of multiple RGB layers and associated opacity levels. These set of layers are then manipulated individually to obtain the desired results. We addresses tasks such as video object segmentation, dehazing, and relighting. Moreover, we introduce a novel logarithmic video decomposition formulation for video relighting tasks, setting a new benchmark over the existing methodologies. We evaluate our approach on standard video datasets like DAVIS, REVIDE, & SDSD and show qualitative results on a diverse array of internet videos.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to propose a general framework for video editing. It starts by predicting the video into several individual layers and then utilizes task-specific knowledge to reconstruct the video. A reconstruction loss and a warping loss are utilized to train the network. This is an inference-time optimization framework that does not rely on external training tools. However, the framework is rather standard, and the choice of a few loss functions for the decomposition tasks is straightforward. Overall, the novelty is limited. I am inclined to reject this article. Please check the details in other sections.

### Strengths
The motivation to propose such a general framework is good.

### Weaknesses
-: The reconstruction loss and warp loss used are very common loss functions and do not offer any novelty.

-: The method is still not sufficiently general. For example, for the task of video segmentation, additional loss functions need to be designed as constraints. The three task-specific losses mentioned in Section 3.2 are the only ones provided. From this perspective, it is difficult to see what this framework proposed in the paper brings to this community. The lack of a clear, unifying principle beyond the basic architecture makes the framework feel like a collection of task-specific solutions rather than a truly general approach.

-: The comparison results of the experiments are not that fair. For instance, in Table 3, the comparison is made with the latest algorithm, CG-IDN (a 2021 algorithm). There are many dehazing algorithms that could be compared, including single-image hazing algorithms with stability processing (references [1][2]). The choice of a single, relatively older baseline significantly weakens the claims of the paper.

-: Additionally, Table 2 lacks many baselines. Looking at the official website of DAVIS2016, the best baseline achieves an IOU score of over 82. Why wasn't this paper compared against that?

-: Sometimes it is necessary to introduce additional prior knowledge, such as for the task of dehazing, where the effectiveness is actually limited.

### Questions
See weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the Video Decomposition Prior (VDP) framework, a new approach for video editing tasks, including object segmentation, dehazing, and relighting. VDP decomposes videos into multiple layers and optimizes parameters without explicit training. The proposed logarithmic video decomposition enhances video relighting, resulting in state-of-the-art performance in downstream tasks: unsupervised video object segmentation, dehazing, and relighting.

### Strengths
1. Sound approach: The VDP framework presents an innovative approach to video editing, offering practicality and cost-effectiveness by not relying on extensive datasets or ground truth annotations. The ability to optimize parameters using the test sequence itself distinguishes VDP from traditional deep learning methods, which often require extensive training data.

2. State-of-the-Art Performance: VDP demonstrates top-tier performance in key downstream tasks, including unsupervised video object segmentation, dehazing, and relighting.

3. Good writing and representation.

### Weaknesses
I am generally positive about this paper. my main concern lies in the lack of comprehensive comparison: The paper does not provide a comprehensive comparison with other video editing techniques, making it difficult to assess the VDP framework's performance against other state-of-the-art methods. Furthermore, video editing is a broad field, including tasks such as adding or removing objects. It seems that the proposed method may not be suitable for handling these scenarios. Therefore, I suggest that the authors consider refining the title and corresponding claims.

### Questions
Please see the weakness

### Soundness
3 good

### Presentation
3 good

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
This paper introduces a new approach called the Video Decomposition Prior (VDP) framework. Unlike conventional methods, VDP leverages the motion and appearance of the input video, decomposing it into multiple RGB layers with associated opacity levels. These layers are then manipulated individually to achieve the desired results, addressing tasks like video object segmentation, dehazing, and relighting. The paper also introduces a logarithmic video decomposition formulation for relighting tasks. The approach is evaluated on standard video datasets, including DAVIS, REVIDE, and SDSD, demonstrating qualitative results on a diverse range of internet videos.

### Strengths
+ The proposed video decomposition prior leverages the motion and appearance of the input video, decomposing it into multiple RGB layers with associated opacity levels.
+ The proposed VDP is employed in different video-based tasks, including video object segmentation, video dehazing and video relighting.

### Weaknesses
 - In the paper, the limitations of the VDP is not discussed in the paper, and all the results are good cases. 
- In the introduction of Flow similarity loss, the VGG embeddings of masked flow-RGB and those of other layers are used to calculate the cosine similarity. It is unclear how to generate VGG embeddings from masked feature maps for cosine similarity calculation. 
- In equation (12), the behavior of the reconstruction layer loss resembles that of the L1 loss in the reconstruction loss. To validate the rationale behind the design, it is essential for the paper to elucidate the distinctions between them and elucidate the impact of the reconstruction layer loss.

### Questions
Please refer to the questions in the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new framework that decomposes a video into multiple multiple RGB layers and associated opacity levels for various video editing tasks.
The proposed framework uses two neural network modules, RGB-net and α-net, to predict RGB layers and opacity/transmission layers for each video frame. 
These layers are then composited to reconstruct the input video or achieve the desired effects during optimization.
The paper conducted experiments on video relighting, dehazing, and VOS tasks and achieves superior results compared to some existing baselines.

### Strengths
- Writing is overall clear.
- Various tasks are conducted and better performance w.r.t to some baseline is reported.
- No pre-training is required (test-time optimization).

### Weaknesses
 - This paper proposes to unify various downstream tasks by video decomposition. However, the formulation of the video relighting task in this paper uses one RGB layer to represent the enhanced video and an alpha-layer to represent gamma correction. This formulation does not have any meaning of “decomposition”. On the other hand, this paper carefully designs different decomposition definitions and corresponding constraints for different downstream tasks, but these constraints and decomposition definitions seem to lack a unified and general formulation. Therefore, I felt such kind of “unification” seems too artificial and forced.

- The proposed formulation is not new (or at least has very few novelty).
Overall, the proposed formulation can be summarized as a "data-term + prior" approach, which is a rather common formulation in optimization-based approach for image / video synthesis tasks. 
Using neural networks as an implicit prior for data term is not new (as also mentioned in the paper - "These approaches have highlighted the importance of formulating a loss function,
combined with the optimization of neural network parameters") and the proposed paper extends this idea into other tasks.
Yet, the exact formulation designed for each task is dedicated but common (e.g., gamma-correction curves [1] for relighting; alpha-blending [2,3] for video-segmentation, dark-channel prior for dehazing).

- Missing baselines for UVOS tasks: The paper compares with both pre-trained methods and test-optimization methods. For pre-trained methods, there are massive VOS methods [4,5,6] that has far better performance than compared methods in this paper; For test-optimization methods, there are also other video decomposition methods that targets this task [2,3].

### Questions
- While the proposed method does not require pre-training, it needs to optimization on each input sequence which takes time. How long does it take for optimizing a video sequence?

- Is there a common insight or general guidance on applying this framework to downstream tasks? For example, what if applying this framework to tasks like denoising or super resolution?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
