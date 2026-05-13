# ED-NeRF: Efficient Text-Guided Editing of 3D Scene With Latent Space NeRF

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
Recently, there has been a significant advancement in text-to-image diffusion models, leading to groundbreaking performance in 2D image generation. These advancements have been extended to 3D models, enabling the generation of novel 3D objects from textual descriptions. This has evolved into  NeRF editing methods, which allow the manipulation of existing 3D objects through textual conditioning. However, existing NeRF editing techniques have faced limitations in their performance due to slow training speeds and the use of loss functions that do not adequately consider editing.
To address this,  here
we present a novel 3D NeRF editing approach dubbed ED-NeRF by successfully embedding real-world scenes into the latent space of the latent diffusion model (LDM) through a unique refinement layer. % inspired by an analysis of the latent space of a latent diffusion model (LDM).
This approach enables us to obtain a NeRF backbone that is not only faster but also more amenable to editing compared to traditional image space NeRF editing. Furthermore, we propose an improved loss function tailored for editing by migrating the delta denoising score (DDS) distillation loss, originally used in 2D image editing to the three-dimensional domain. This novel loss function surpasses the well-known score distillation sampling (SDS) loss in terms of suitability for editing purposes. 
Our experimental results demonstrate that ED-NeRF achieves faster editing speed while producing improved output quality compared to state-of-the-art 3D editing models. Code and rendering results are available at our project page\footnote{\url{https://jhq1234.io/ed-nerf.io/}}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method for text-guided 3D NeRF editing. Compared to the existing method, to solve the efficiency, it embeds real-world scenes into the latent space of the latent diffusion model (LDM) through a refinement layer. Moreover, it presents an improved loss function tailored for editing by exploiting (DDS) distillation loss and binary mask for accurate editing. The experiment validates the effectiveness of the proposed method.

### Strengths
1. The paper is in general well organized and easy to follow. 
2. The DDS distillation loss with the binary mask is shown to be effective.

### Weaknesses
1. The key contribution of the proposed method lies in the integration of several small techniques, e.g., latent NeRF representation and DDS distillation loss, without too much novel insight. I am not pretty sure whether it is enough for the ICLR. The novelty seems incremental, combining existing latent space techniques with a distillation loss. The paper does not clearly articulate a fundamental breakthrough in the underlying methodology, making the overall contribution somewhat limited. The core idea of applying DDS to NeRF editing, while potentially useful, lacks a strong theoretical justification or a significant departure from existing approaches.
2. One of the motivations of the method is the efficiency of NeRF editing.  To this end, the latent NeRF representation is adopted, while the efficiency comparison with the existing methods is not shown in the main paper. Moreover, there is a lot of work for fast NeRF training/finetuning, which makes the improvement less interesting. The paper claims efficiency gains through latent space representation, but lacks empirical validation of this claim against existing fast NeRF methods. Without concrete benchmarks, the practical advantage of the proposed approach remains unclear. Furthermore, the paper does not adequately address the existing body of work focused on efficient NeRF training and fine-tuning, which diminishes the significance of the claimed efficiency improvements.
3. The design of Refinement layers is straightforward to me, and it is more like adding some additional layers after the volume rendering, which is a normal way to improve the rendering quality. Moreover, from Fig. 2, it looks like some layers are adopted directly from the SD VAE. What's the benefit of such a desgin? The refinement layers, while improving reconstruction quality, appear to be a standard application of post-processing layers, lacking a novel architectural contribution. The direct adoption of layers from the SD VAE raises questions about the design choices and whether they are optimal for the specific task of NeRF editing. A more detailed analysis of the design decisions and a justification for the selected architecture is needed.
4. In the experiment, most of the examples are about color changes or local texture editing. I am wondering whether the proposed method works for other 2D editing, such as the whole image style transfer or object replacement as shown in Instruct-NeRF2NeRF. Moreover, from Fig.4, we can see that compared to Instruct-NeRF2NeRF, the improvement lies in the accuracy of the editing for certain areas. I am wondering whether Instruct-NeRF2NeRF will perform better just with the mask constraint. The experimental evaluation primarily focuses on color and local texture edits, failing to demonstrate the method's capability for more complex editing tasks such as style transfer or object replacement. The comparison with Instruct-NeRF2NeRF highlights improvements in local accuracy, but it is unclear whether these improvements are significant enough to justify the proposed method, especially since the comparison does not include a masked version of Instruct-NeRF2NeRF.

### Questions
Please refer to the weakness. Besides, there are two small questions. 
1. It looks like that there is a typo in Fig. 2(c). 
2. There are some minor typos in the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a novel 3D NeRF-based approach for editing real-world scenes using a latent diffusion model (LDM) and a refinement layer. The proposed approach is faster and more amenable to editing than traditional NeRF methods. The authors conduct an analysis of the latent generation process and the proposed refinement layer based on that can significantly enhance performance. To further improve editing performance, the authors propose an improved loss function that is tailored for editing tasks by incorporating the delta denoising score (DDS) distillation loss. The experimental results show that the proposed approach achieves faster editing speed and improved output quality compared to traditional NeRF methods. Notably, the proposed approach effectively alters specific objects while baseline methods often fail to maintain the region beyond the target objects and fail to guide the model towards the target text.

### Strengths
1. The paper provides a well-motivated solution to the problem of editing pre-trained 3D implicit networks. The proposed approach effectively preserves the integrity of the original 3D scene while enabling desired modifications. This is a significant advantage as it ensures that the edited results are coherent and consistent with the original scene.

2. The incorporation of DDS into 3D for ED-NeRF editing is a reasonable and innovative adaptation. This allows for more precise editing of implicit 3D models, thereby enhancing the overall quality of the edited results.

3. The qualitative results presented in the paper demonstrate that the proposed technique can efficiently modify specific objects while preserving regions beyond the target objects. This is an improvement over baseline methods that often face difficulties in guiding the model toward the intended text. The ability to accurately edit specific objects while maintaining the integrity of the surrounding environment is a crucial advantage of the proposed method.

4. The author's provision of the necessary code enhances reproducibility.

### Weaknesses
1. Although the paper showcases impressive qualitative editing results, it does not provide free-viewpoint rendering results in video format. Consequently, it is hard to determine whether the proposed method can generate view-consistent editing. This is my primary concern regarding the acceptance of this submission, and I am open to increasing my rating if the author can provide video results.

2. The author presents a time analysis in the appendix; however, it is not comprehensive and does not sufficiently support the claim of "improved efficiency." The analysis only reports the time for inference, excluding training time. Given that the "Generate source image and latent feature map" paragraph in Appendix A states their approach involves generating novel view images and extracting their latent feature maps, the time required for this procedure should also be reported and factored in when comparing with baseline approaches.



### Questions
1. The paper presents an innovative approach for editing pre-trained 3D implicit networks while preserving the surrounding environment. It would be helpful if the author could provide additional insights into why their method can edit the targeted object while preserving other parts without introducing unwanted artifacts. This would enhance the understanding of the proposed method and its underlying mechanisms.

2. The paper mentions adopting a 4-channel latent representation for the proposed method. It would be beneficial if the author could provide more details about the adopted latent feature vectors. Specifically, it would be helpful to know if this representation is strong enough for the task of editing, and how the feature maps are visualized since they appear visually similar to original RGB images.

3. The rendered depth map presented in the paper appears somewhat coarse. It would be useful if the author could explain this observation.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an improved 3D NeRF editing pipeline to overcome existing challenges like long training time, instability, and dropped image quality. The key idea is to bring NeRF training into the latent space of Stable Diffusion (SD), and perform all editing on the rendered latent feature directly. A refinement layer is introduced to enable nearby pixel feature interactions thus enhancing rendering quality, while an adapted mask-aware DDS loss (compared to the common SDS loss) is utilized to distill the SD guidance more effectively and ease the color saturation and mode-seeking. Various ablations analysis, comparison to baselines have demonstrated its effectiveness and superior performance against previous methods.

### Strengths
[**Significance**] 
- Inspired by Latent-NeRF, the author proposes to train and edit NeRF in VAE latent space, which can help reduce time and computation costs, this is a smart and important move for NeRF editing related works. 
- Their results have surpassed existing methods both quantitatively and visually;

[**Originality**] 
- The author further proposes the refinement layer to let pixel correlations help increase model capacity, which overcomes the major drawbacks of quality drifting when using ray-based rendered latent feature for NVS. The proposed modification is simple yet effective.
- While other works tend to follow existing SDS-based distillation scheme, the author is well aware of the limitations of SDS loss, and further proposes to borrow recent advancements in image editing to help 3D editing. Though DDS method is not developed by the authors, the application and extension in 3D is novel;

[**Clarity** and **Quality**] 
I like the figure 2 and figure 3 for pipeline design, which is clear and easy to understand. The author has compared with various baselines, and conducted a lot of visual comparisons, which is informative, and clarified well.

### Weaknesses
 - The paper seems to be casual on writing, and there might be mistakes. Like Eq. 12 and Eq.13, why are L_{tot}  and L_{Mrec} part of each other? Further, there should be a formal table in the main paper on computing time comparison, rather than coarse text in the supp. The Efficiency improvements are one of the major claim and contributions of the paper, it is even added into the title of the paper ": EFFICIENT TEXT-GUIDED...", thus putting the time comparison in supp. is not good. 
- Lacking of object removal and insertion experiments. Maybe I'm wrong, but most examples shown in the paper seem to only about modifying the centric object material, identity, or the background, it doesn't show how the methods works about removing an object, or inserting another object.

### Questions
- It seems the view consistency is not as good as several previous methods, while the small gap is acceptable, I am wondering what would be an example of view inconsistency, this can help us understand the space to improve;
- In Eq. 9, I guess the order of these two items are wrong? The target SDS item should sit first, or it doesn't matter? I am also wondering what if we combine the original SDS loss in addition to the DDS loss, would it further improve the performance?
- Reflection is an issue in NERF if not handling well, and the tensor-RF backbone doesn't model that. However, it seem that Figure 4 the car example demonstrated the vivid reflection, is this true? If this is the case, should we give the credit to the refinement layer?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for NeRF editing by incorporating the latent diffusion model and masked segmentation to control the editing of rendered views. Unique in the process is the iterative refinement process which ensure the multi-view consistency in NeRF, while ensuring the editing agrees with the target latent direction. The proposed method is compared with InstructNeRF2NeRF and other NeRF editing methods which show superior results over the compared methods.

### Strengths
The proposed method is straight forward and it demonstrates good editing results on large variety of examples.

### Weaknesses
After checking the paper in detail, I got an impression that the improved performance are mainly due to the usage of object mask, instead of the DDS proposed in the paper. This impression is strengthen after checking the experimental comparisons with the InstructNeRF2NeRF. In that sense, I also feel that the comparisons are entirely fair since the compared method does not use any object mask. The paper also did not mentioned how these masks are obtained and how sensitive is the proposed method against the object mask segmentation accuracy. Overall, I think this is a good attempt for NeRF editing, but I somewhat feel that this is an incomplete submission if the authors cannot resolve my concerns above.

### Questions
Please correct me if I have ever made mistakes in my evaluations.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
