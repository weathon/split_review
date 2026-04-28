# A Generic Class-agnostic Object Counting Network with Adaptive Offset Deformable Convolution

- Decision: Reject
- Avg Score: 4.83
- Scores: 5, 5, 3, 5, 5, 6

## Abstract
Class-agnostic object counting (CAC) aims at counting the number of objects in the unseen category in an image. In this paper, we design a generic class-agnostic object counting network with Adaptive Offset Deformable Convolution (AODC), which initially focus on the reference-less class-agnostic object counting task without any exemplar. Our method calculates the self-similarity maps of the image features and performing a 4D convolution on these maps, obtaining the adaptive offsets for the deformable convolution, so that the model can obtain complete information about the object at that location. Through this process, AODC is able to recognize objects of different scales in a same sample. In addition to this, we adopt our approach to both zero-shot setting and few-shot setting, the former with semantic text and the latter with visual exemplars as references. We conduct experiments on the few-shot object counting dataset FSC-147, as well as other large-scale datasets, and show that our method significantly outperforms state-of-the-art approaches on all the three settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a generalized counting framework with the proposed adaptive offset deformable convolution (AODC). By augmenting pixel-wise self-similarity map as offset to deformable convolution, it effectively enhances localization that converges to the center of each object. In particular, the use of 4D convolutions transforms self-similarity map into adaptive offset. Along with attention mechanisms for feature refinement and generalized loss(GL) to supervise dot labels, the proposed, unified framework acquires SOTA across few-shot, zero-shot, and reference-less settings.

### Strengths
1. The empirical result is impressive, especially on zero-shot and reference-less settings. Experiments are comprehensive. It shows the generalizability of the framework. 
2. The use of 4D convolutions to exploit the local information of self-similarity map to capture object-level information and transform into offsets is insightful, especially under reference-less setting.
3. The paper is relatively easy to follow

### Weaknesses
1. The novelty is somewhat limited. The use of deformable convolution has been used in SPDCN. The author’s proposed contribution is to improve the offset to be adaptive on self-similarity maps. Attention for feature refinement is used in existing counting works such as LOCA. While GL is not a proposed contribution by the authors, it not new as well
2. My main concern lies in the impact of GL on the improved performance. Shown in the ablation studies (Table 3), the reference-less performance without GL is worse than prior works that uses MSE loss, which suggest that GL is the core factor for improvement. The performance achieves SOTA after employing GL, which is not a fair comparison given other models are trained on MSE, a suboptimal solution of GL. It would be fairer if you compare against prior works trained on GL. Please provide explanations on your setup
3. The performance on CARPK is not SOTA under few-shot setting. CounTR yields better performance than your proposed method (MAE: 5.75, RMSE: 7.45)
4. Missing newer counting methods such as [1] (from ECCV 24’)

### Questions
1. Regarding the impact of GL loss on few-shot setting, it would be beneficial to provide the ablation study to verify whether the SOTA result is benefitted by GL or the proposed AODC framework?
2. Could you visualize the ablation study to concretely demonstrate the role of each component?
3. (Minor comment) Is the method scalable to ViT-based backbones, in which the ability to capture global dependencies could benefit in identifying counting targets? 
4. (Minor Comments) Table 4 discusses the choice on the number of attention blocks and the phenomenon of overfitting. While stacking too many attention blocks worsens the validation performance, it is only overfitting if the training loss is continually decreasing. I am not certain whether this is the case, and if not, I would suggest remove such wording. I am more inclined to state that excessive number of attention blocks strengthens dominant features and yet filter out less dominant features that might correspond to target objects. 

I am willing to raise my score if the above questions (especially GL) are adequately addressed.

### Soundness
2

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
This paper tackles the problem of class-agnostic counting. For reference-less setting, the proposed method computes self-similarity map to obtain shape and size information of the objects, and applies 4D convolution to learn adaptive offsets for deformable convolution. For few-shot and zero-shot settings, the proposed method uses cross-similarity maps instead of self-similarity maps. The proposed method is evaluated on the three settings of class-agnostic counting.

### Strengths
1. The proposed method is generalizable to different settings in class-agnostic counting.
2. The proposed framework shows good performances on different settings.

### Weaknesses
1. My main concerns are with the technical contributions and the novelty. Though it can be important to adaptively learn object shapes and structures, the proposed method seems to learn adaptive offsets for convolution kernels in a quite straightforward way. It seems like a composition of existing techniques (e.g., deformable convolution, 4D convolution, generalized loss, etc.). The core idea of using self-similarity or cross-similarity maps to guide the deformable convolution is not particularly novel, as similar approaches have been explored in other contexts. The specific implementation of the 4D convolution to generate offsets also lacks significant technical depth; it appears to be a direct application of existing 4D convolution techniques without any novel modifications or insights.
2. The writing of the method section is not very clear. I can understand the high-level pipeline, but I'm confused about the details, especially the deformable convolution module. The explanation of how the self-similarity or cross-similarity maps are precisely used to generate the offsets for the deformable convolution is vague. It's unclear how the 4D convolution is parameterized and how it interacts with the similarity maps to produce the adaptive offsets. The lack of clarity makes it difficult to assess the technical soundness of the proposed approach.
3. There lacks some analysis on why using adaptive offsets and deformable convolution improves the performance, e.g., why the authors chose to adopt deformable convolution instead of other adaptive modeling techniques? The paper does not provide a clear justification for choosing deformable convolution over other potential methods, such as attention mechanisms or dynamic filters. A more thorough analysis of the advantages and disadvantages of deformable convolution in this specific context is needed. Furthermore, the paper should provide insights into how the learned offsets are related to the object shapes and sizes, and why these offsets are effective for class-agnostic counting.
4. The ablation study shows that the adopted generalization loss improves the performance a lot, but it is not proposed by this paper and is not claimed as a contribution of this paper. It is also not adopted by some of the compared methods. The reliance on an existing loss function as a major contributor to performance raises concerns about the novelty of the proposed method. The paper should clearly distinguish between the contributions of the proposed architecture and the contributions of the adopted loss function.

### Questions
1. Would the performance of the proposed framework be affected by the background in the input image? As mentioned in Line 54-55, the target objects become "more obvious when the object is in a background with a large difference in colour compared to itself".
2. Can the proposed method deal with objects with various sizes? In class-agnostic counting, a major challenge is the varying sizes and colors of the target objects in the same image. I'm curious about whether the adaptive offsets learned can adjust to different sizes.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose Adaptive Offset Deformable Convolution (AODC), which aims to recognize objects of different scales in a same sample. It can be also extended to zero-shot and few-shot settings, achieving state-of-the art performance across different counting datasets.

### Strengths
1. Handling objects of varying scales is a critical challenge in counting.
2. The method achieves state-of-the-art performance on different counting datasets.

### Weaknesses
1. The motivation of the paper is not particular clear. Although the introduction mentions that the objects for counting are of varying scales, and the proposed method can recognize these variations, there is not enough evidence to show the effectiveness across objects of different sizes. Most of objects from FSC-147 dataset are similar in size, and the objects shown in Fig. 4 and Fig. 8 are also of similar sizes. These results may not sufficiently validate the method's ability to effectively handle diverse scales. Specifically, the paper lacks a quantitative analysis demonstrating performance gains on images with a wide range of object scales, and the qualitative examples provided do not showcase this capability convincingly. A more rigorous evaluation, perhaps with artificially generated datasets containing objects of drastically different sizes, would be beneficial.

2. The novelty is limited. The use of deformable convolution for object counting has been previously proposed in [1]. The only difference from [1] is the replacement of a fixed scale with multiple scales, which is not a significant contribution. The paper does not adequately address why simply using multiple scales with deformable convolutions is a novel contribution, and it does not provide a detailed analysis of the limitations of the previous work [1] that this method overcomes. A more thorough discussion of the specific technical challenges addressed by the proposed approach, beyond simply using multiple scales, is needed.

3. The performance of models in the few-shot on COCO appears to be inferior to that of comparison methods, which raises concerns about the effectiveness in this setting. The paper does not provide a clear explanation for why the proposed method underperforms in the few-shot setting on COCO, and it does not offer any analysis of the potential reasons for this performance gap. Further investigation into the limitations of the method in few-shot scenarios is needed, along with potential strategies to mitigate these issues.

### Questions
Can the authors show the results of the images in Fig. 5 under zero-shot setting?

### Soundness
2

### Presentation
2

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
The paper introduces a novel approach for class-agnostic object counting, focusing on counting unseen object classes using an Adaptive Offset Deformable Convolution (AODC) network. The key innovation lies in generating self-similarity maps from image features, followed by a 4D convolution to create adaptive offsets for deformable convolution. This design enables the model to capture multi-scale objects effectively. The method is adapted for zero-shot and few-shot counting and achieves state-of-the-art results across various datasets and counting scenarios.

### Strengths
1. The proposed AODC framework, grounded in adaptive offset deformable convolution, presents a novel approach for capturing spatial structures of objects at different scales. It achieves impressive results across reference-less, zero-shot, and few-shot settings, showing its adaptability.
2. Extensive experiments across multiple datasets, including FSC-147, CARPK, and a COCO subset, underscore AODC’s effectiveness and generalization capability.

### Weaknesses
1. This paper focuses on the design of deformable convolution; relevant work should be discussed in the literature review. Specifically, the paper should discuss and compare the proposed approach with existing deformable convolution methods, highlighting the novelty and advantages of the adaptive offset generation. The current literature review lacks a detailed discussion of how the proposed AODC differs from other deformable convolution techniques, particularly in the context of object counting.
2. The architecture in Fig. 2 lacks clarity and explanation. For example, $F$ is related to multiple components, but the arrows lack further clarification. The diagram should clearly delineate the flow of information and the specific transformations applied to the feature maps at each stage. The role of each block and the mathematical operations involved should be explicitly stated, making it easier to understand the overall architecture and its components.

### Questions
1. The ablation study only shows the reference-less setting. Could additional analysis be provided to show the impact of different components across other settings?
2. Could you provide a visualization comparing the effects of using vs. not using Adapt-O, similar to the format used in Fig. 6?
3. In Tab. 2, the few-shot settings on Val-COCO and Test-COCO seem to have moderate performance. Is there any explanation?
4. From my observation, most images in the test dataset are dominated by a single object category (e.g., an image filled with strawberries). 
The proposed method, which utilizes a self-attention like mechanism, may lead the model to focus on all objects within an image, potentially achieving high performance on such datasets without truly understanding the similarity between exemplars and the image.
Could you demonstrate the model's ability to distinguish different object categories within the same image? (e.g., using exemplars of different categories, such as apples and strawberries, on an image containing various fruits.)

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a unified framework for the Object Counting problem, in which firstly proposed for reference-less Object Counting and can be easily adapted to the few-shot and zero-shot setting. Through the experiments, the paper successfully shows the method has good performance over each setting.

### Strengths
- This paper has a clear structure, motivation, and experiment to validate the effectiveness of the proposed methods.
- The idea of having an unified framework for few-shot, zero-shot and reference-less setting from the reference-less setting is new, but is not significant (see the weakness).

### Weaknesses
 **Significance of the contribution**: 
- The ideas of the generalized framework are good, but it is not new. LOCA [1] can perform object counting for referenceless and few-shot settings, as indicated in the paper. With appropriate modification, for example, injecting the cross-attention with CLIP, it may gain the capability of zero-shot counting.
- In the ablation study (Tab 3), there are 3 main factors contribute to the good performance of the model. 1) The Generalized Loss, which is already used in [2], 2 )the Deformable Convolution part, which is the main focus of the paper, is not clearly written. Therefore, it makes the contribution less significant.

**Clarity**: It is not well clearly written in the Deformable Convolution part. In Fig 2, there is a branch that connects from $O_{local}$ to the Deformable Conv, but is not mentioned in the Deformable Convolution Section, therefore, it is hard to understand the reason why the paper needs to predict $O_{local}$ and $O_{adaptive}$ seperately. In addition, there is a term "fusion convolution" in L 223-224, which is not clearly defined.

**Experiment**:
- The results for the Few-shot setting is not good as LOCA [1], even LOCA use only L2 loss for the training of the model, and in the paper, the ablation study (Table 3) shows that the Generalized Loss can achieve better performance compared to L2 loss.
- Compared to previous works, for example LOCA [1], the paper added a deformable convolution part. And to mitigate the deformable convolution, the paper tries to add some 4D Convolution to predict the offsetmap. I think the paper should report the time and GPUs memory running in the whole process, is it worth to run the big module, since the performance in the few-shot setting is not good compared to LOCA [1].

### Questions
1. What is $O_{local}$ and $O_{adaptive}$ represented for? And how do we incoporate only $O_{local}$ in the Deformable Convolution block?
2. Why do not use the cross attention in the few-shot setting similar to the zero-shot setting, since we can treat the features of the examplars as the CLIP features?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper designs a generic class-agnostic object counting network with Adaptive Offset Deformable Convolution (AODC), which focuses on the reference-less class-agnostic object counting task.

### Strengths
The outstanding performance of this paper is reflected in the experimental results.

### Weaknesses
1) The motivation is not clear, please explain why you focus more on reference-less tasks. Based on my understanding of this task, few-shot and zero-shot tasks based on text descriptions or visual exemplars are more practical. Users tend not to count how many objects there are in an image, but rather to count the number of specific categories. This is why recent research focuses more on these two types of methods. Based on this, please give application scenarios. The paper does not adequately justify why a reference-less approach is valuable, especially given the prevalence of category-specific counting tasks. The lack of a clear use case makes the contribution seem less impactful. The paper should elaborate on scenarios where counting all objects, regardless of category, is genuinely useful. 

2) The presentation of Fig. 2 is confusing. It seems that the few-shot setting and the main branch are partially repeated. If they are different, what is the difference? Please reorganize this figure to make it easier for readers to understand. The diagram lacks clarity in distinguishing between the few-shot and reference-less pathways. The overlap in the diagram suggests redundancy or a lack of clear separation between the two approaches. It is unclear how the feature fusion operation is applied and how it differs from the main branch. A more detailed and distinct visualization of each pathway is needed.

3) Please explain why 4D convolution was used rather than 3D convolution. The justification for using 4D convolution over 3D convolution is not adequately explained. The paper needs to clarify why the self-similarity map necessitates a 4D convolution and why a 3D convolution would not be suitable. A more detailed explanation of the dimensionality of the feature maps and the convolution operation is required.

4) It seems that deformable convolution has been used for counting tasks for a long time. Please explain the novelty of the proposed method and compare it with related methods, such as: ADCrowdNet: An Attention-Injective Deformable Convolutional Network for Crowd Understanding. The paper fails to adequately highlight the novelty of the proposed approach in the context of existing deformable convolution-based counting methods. The use of adaptive offsets needs to be better justified and compared to other methods that use deformable convolutions for counting. The paper should clearly articulate the differences and advantages of the proposed method over existing approaches, such as ADCrowdNet.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2
