# LRVS-Fashion: Extending Visual Search with Referring Instructions

- Decision: Reject
- Scores: 8, 5, 5, 3

## Abstract
This paper introduces a new challenge for image similarity search in the context of fashion, addressing the inherent ambiguity in this domain stemming from complex images. We present Referred Visual Search (RVS), a task allowing users to define more precisely the desired similarity, following recent interest in the industry.
    We release a new large public dataset, LRVS-Fashion, consisting of 272k fashion products with 842k images extracted from fashion catalogs, designed explicitly for this task.
    However, unlike traditional visual search methods in the industry, we demonstrate that superior performance can be achieved by bypassing explicit object detection and adopting weakly-supervised conditional contrastive learning on image tuples. Our method is lightweight and demonstrates robustness, reaching Recall at one superior to strong detection-based baselines against 2M distractors.\footnote{The dataset is available at \url{https://huggingface.co/datasets/Slep/LAION-RVS-Fashion}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the Referred Visual Search (RVS) task, addressing the challenges of image similarity search in the fashion domain, particularly in scenarios where product images need to be retrieved from query images containing multiple products or from model pictures. The authors present a large dataset, LRVS-Fashion, containing 272k fashion products and 842k images, designed for this task. They propose a novel method based on weakly-supervised conditional contrastive learning, achieving superior performance without relying on explicit cropping or segmentation. The study demonstrates the effectiveness of their approach in comparison to a variety of baselines. The paper is overall well written.

### Strengths
The introduction of RVS as a task for fashion images addresses a gap in the current literature and reveals significant value for practical applications such as e-commerce systems.

The LRVS-Fashion dataset is extensive in terms of its scale, organization, and cleaning process, providing valuable resources for future research and enhancing the field's accessibility.

The proposed approach, based on conditional contrastive learning, is intuitive yet elegant. By avoiding explicit object detection or segmentation, it is efficient and easier to implement in various applications, particularly by reducing the extra stages of data collection or model design. In addition, it demonstrates impressive robustness against a large number of distractors, which is critical in real-world applications.

The paper provides a thorough literature review and extensive comparisons with existing methods. For example, it compares with compositional image retrieval methods that share a conditional learning requirement but targeting at different application scenarios. The experiment setup is clear and the overall results are convincing in terms of accuracy and efficiency.

### Weaknesses
While the experimental results are solid, it could be more comprehensive if the analysis can go deeper into the impact of objects' visibility in query images considering object sizes, occlusions or viewpoints. Or, a simpler referring aspect could be segmentation mask area or its ratio to a detected object bounding boxes? One example is how the retrieval accuracy changes among shirts because they are often partially visible due to overlaid with outwears.

### Questions
The study focuses primarily on fashion images and leverages LAION-5B to create the benchmark dataset. While it serves as a valuable testbed for future research, it would be interesting to discuss how to construct larger datasets in real-world scenarios and the challenges associated with generalizability to close domains such as street outfit photos that have noisy backgrounds, or even beyond fashion such as furniture, landmarks, etc. This would further strengthen the impact of this work?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Referred Visual Search (RVS) in the fashion domain. The paper makes two main contributions: (1) A new large-scale dataset called LRVS-Fashion and (2) A weakly-supervised method that outperforms detection-based approaches.

### Strengths
1. The paper proposes a high-quality dataset that will be beneficial to the field
2. The paper is well-written and easy to read.

### Weaknesses
1. The proposed task is like a special case for the task of composed image retrieval(CIR). However, the experiment is not compared with recent CIR methods, which makes the result not convincing. 
2. The proposed method shows high performance in LRVS-F, as shown in Table 2, nearly 99% in Cat@1. These superior performances raise the question of the proposed dataset's motivation. Is there any specific problem the dataset wants to diagnose?

### Questions
see weakness

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
This paper proposes a new visual search task with referring instructions as the hints.
It also creates a new large public dataset, LRVS-Fashion, as the benchmark.
The authors also introduce a CLIP-like simple baseline.

### Strengths
1. The efforts on collecting the benckmark is worthy of applause. This dataset could be potentially used for other fashion-related tasks.
2. The writing of this paper is good and easy to follow.

### Weaknesses
1. I am not convinced on the motivation of the proposed task. I cannot fully imagine a real application scenario for the proposed Referred Visual Search. According to my experience and understanding on fashion/ads, the query image (ie, dressed human) and the target image (ie, garment, product and so on) shown in Figure 1 are normally from the same product set which provided by the advertiser (at least they share some common information, eg, brand name). In that case, we don't need to do large-scale image-base retrieval, which is implementation-wise expensive in the industry. The only case I understand is letting the user themselves upload their individual query images and do a cross-domain image retrieval. However, the target and query image used in this paper are from the same domain and thus    cannot model the real world problem, although I understand collecting cross-domain benchmark is even harder.
2. I believe the proposed RVS is just a sub-task of Composed Image Retrieval (CIR), while their relationship is not clearly discussed (between L147 and L153) and the latest CIR related works were not cited. Regarding "rather than modifying the image" in L151, I think getting the feature of the ROI of the query image (Figure 4) is also kind of modifying the query image feature.
3. The proposed model arch is okayish but not that innovative (L081) to me. I agree this can be regarded as a strong baseline but don't think this widely used arch can be claimed as innovative.
4. I think some zero-shot methods (no training needed) should be considered as baselines too, eg, multimodal LLM that can fuse the query image feature and the instructions.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new task, Referred Visual Search, which retrieves specified products within a given image based on user requirements, and constructs a new dataset for this task. Additionally, a CLIP-based model architecture is proposed and its performance is validated on the newly created dataset.

### Strengths
1.	The proposed new task has practical application value in the e-commerce domain.
2.	The illustrations are clear and detailed, facilitating understanding.

### Weaknesses
1.	The significance of the proposed task needs further clarification. What distinguishes Referred Visual Search from text-guided visual localization or composed image retrieval? Can existing methods in these areas be adapted to this task? 
2.	The paper lacks novelty, as applying the CLIP architecture in the e-commerce domain has been previously explored [a-c]. The authors need to further explain the innovation of their proposed method compared to existing methods. 
3.	The experiments require further refinement. Given that the authors utilized methods from composed image retrieval for performance comparison, it is essential to validate the proposed method on the FashionIQ and Shoes datasets within this context to effectively demonstrate its efficacy.
4.	The proposed method incorporates the Grounding DINO and SAM models; thus, a discussion on the fairness of performance comparisons with other methods is warranted. Additionally, the time and space complexity of the proposed method should be compared against other representative methods to provide a comprehensive evaluation.

[a] Han Y, Zhang L, Chen Q, et al. Fashionsap: Symbols and attributes prompt for fine-grained fashion vision-language pre-training[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023: 15028-15038.

[b] Zhou J, Zheng X, Lyu Y, et al. E-clip: Towards label-efficient event-based open-world understanding by clip[J]. arXiv preprint arXiv:2308.03135, 2023.

[c] Han X, Zhu X, Yu L, et al. Fame-vil: Multi-tasking vision-language model for heterogeneous fashion tasks[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023: 2669-2680.

### Questions
Please refer to the Weaknesses section and address my concerns regarding the task setup, methodological innovation, and performance of the proposed method.

### Soundness
3

### Presentation
2

### Contribution
2
