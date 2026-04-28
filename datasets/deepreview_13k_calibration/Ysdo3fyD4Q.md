# VEnhancer: Generative Space-Time Enhancement for Video Generation

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
We present \emph{VEnhancer}, a generative space-time enhancement framework that improves the existing text-to-video results by adding more details in spatial domain and synthetic detailed motion in temporal domain. Given a generated low-quality video, our approach can increase its spatial and temporal resolution simultaneously with arbitrary up-sampling space and time scales through a unified video diffusion model. Furthermore, VEnhancer effectively removes generated spatial artifacts and temporal flickering of generated videos.  
To achieve this, basing on a pretrained video diffusion model, we train a video ControlNet and inject it to the diffusion model as a condition on low frame-rate and low-resolution videos. To effectively train this video ControlNet, we design \textit{space-time data augmentation} as well as \textit{video-aware conditioning}.
Benefiting from the above designs, VEnhancer yields to be stable during training and shares an elegant end-to-end training manner.
Extensive experiments show that VEnhancer
surpasses existing state-of-the-art video super-resolution and space-time super-resolution methods in enhancing AI-generated videos. Moreover, with VEnhancer, exisiting open-source state-of-the-art text-to-video method, VideoCrafter-2, reaches the top one in video generation benchmark -- VBench.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper titled "VEnhancer: Generative Space-Time Enhancement for Video Generation" introduces a novel method for enhancing AI-generated videos both spatially and temporally using a single model. VEnhancer is capable of up-sampling the resolution and frame rate of low-quality videos with many scales, while adding spatial details and synthesizing detailed motion. It also removes artifacts and flickering, improving upon existing methods by integrating a Space-Time Controller (ST-Controller) trained with space-time data augmentation and video-aware conditioning. The method aims to be end-to-end trainable, enabling multi-function enhancement within one model, and claims to surpass current state-of-the-art in video super-resolution and space-time super-resolution for AI-generated content.

### Strengths
1. Novelty: The paper presents a unified approach for generative spatial and temporal super-resolution, which is novel in the field of video generation. The integration of a pretrained generative video prior with a ST-Controller for conditioning is a creative solution that addresses the limitations of cascaded models. The concept of space-time data augmentation and video-aware conditioning is innovative and contributes to the training of the ST-Controller in an end-to-end manner.

2. Quality: The paper is well-structured, with a comprehensive presentation of the methodology, experiments, and results. The visual results and quantitative metrics provided are convincing and demonstrate the effectiveness of VEnhancer.

3. Significance: The work is relatively significant since it's an important complementary to current open-sourced video diffusion models.The ability to handle many up-sampling scales and to refine videos while maintaining content fidelity is a substantial contribution to the field.

### Weaknesses
1. Some expressions of the paper are not clear and rigorous enough, and there are certain ambiguities, ambiguities or even errors. Below are the instances:
- Wrong notations, instead of 𝐼^(1:𝑚:𝑓), 𝐼^(1:𝑚:𝑓) is typically used to denote a sequence starting from 1, ending at 𝑓, with a step size of 𝑚. Similar cases for z, t, \sigma, and s. Besides, in Fig.3 z^{1:m}_t, t^{1:m} should be z^{1:f}_t, t^{1:f} 
- Wrong illustrations. In Fig.2 Space-Time Data Augmentation part, both the noised videos (with noise strength t and \sigma) should be in latent space rather than still being natural videos. The noises are directly added to the latent videos.

2.  Some critical details are lacking such as how to do inference specifically like the initialization of z_t and z_{s, \sigma} (it should be more clear if you have a pseudocode algorithm), and the inference time and performance (like Vbench Results or other metrics) across different SSR and TSR scales.

### Questions
Are the shapes of inputs to ST-Controller different because of different interval m? How does the model handle inputs with different m?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces VEnhancer, a novel generative method designed to enhance both the spatial and temporal quality of AI-generated videos. VEnhancer increases resolution, adds detail, and reduces artifacts and flickering through a single model, leveraging a space-time controller for conditioning on low-quality inputs.
### Contributions

1. **Unified Model:** VEnhancer combines spatial and temporal super-resolution and video refinement capabilities in one model.
2. **Space-Time Controller:** Introduces a mechanism for injecting multi-frame conditions based on a pre-trained generative video prior.
3. **Performance:** Demonstrates superiority over some of the existing state-of-the-art methods in video super-resolution through extensive experiments.

### Strengths
- Handles multiple up-scaling in both space and time dimensions, allowing for versatile application scenarios.
- Improves the fidelity of generated videos while maintaining or enhancing detail, demonstrated through rigorous testing against current top methods.

### Weaknesses
 - As with most diffusion models, the complexity of the model could lead to longer inference times, which may limit its applicability in real-time or low-resource scenarios.
- The model's performance heavily relies on the availability of high-quality training data, which might not always be available or feasible to collect in certain domains.
- For each different text-to-video model, a new VEnhancer need to be trained to accommodated the different architecture, limiting the use case of the proposed method. It would be more practical if the proposed method could be a standalone video super-resolution toolkit.
- Other diffusion based video super-resolution works is not compared in the paper, e.g. Upscale-a-video.

### Questions
- It would be helpful if the authors could discuss more about how they collect the data, i.e., filtering out 350K data from Panda 70M.

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
The paper presents a diffusion-based video space-time enhancement model. Specifically, the proposed VEnhancer leverages a control branch to integrate the low-resolution and low-frame-rate video prior into diffusion. Besides, a new data augmentation strategy is proposed to carry out the video super-resolution and enhancement with different functions, e.g., enhancing video with details in different levels. Comparisons with both video super-resolution methods and cascaded super-resolution methods verify the superiority of the proposal.

### Strengths
1.	The proposed approach unifies the space-time video super-resolution through re-sampling operation over time-space axes, achieving multi-function in a single video diffusion model.
2.	Both of the objective video quality evaluation and subjective human evaluation show the effectiveness of the proposed approach in video enhancement. 
3.	The paper is well-written and technical description is clear.

### Weaknesses
1.	One of my key concerns about the technical novelty is about the involving of the UNet-based control branch whose weights are copied from the original I2VGen-XL. The novelty seems limited since the controling approach has been proposed by ControlNet and the key frame information integration via feature summation is also intuitive. Specifically, the direct copying of weights from a pre-existing model for the control branch raises questions about the extent of the contribution. While the feature summation is a straightforward approach, the paper does not provide sufficient justification for why this method was chosen over other alternatives, such as more complex attention mechanisms or adaptive fusion techniques. The lack of exploration into alternative conditioning methods weakens the claim of novelty.
2.	The technical design of space-time data augmentation should be investigated quantitatively in the main paper. Besides, the motivation of the position embedding encoded from the noise augmentation is unclear. What are the effects by exploiting this parameter $\sigma$ in video enhancement? The paper lacks a detailed analysis of how different augmentation strategies impact the final performance. The choice of using a position embedding derived from the noise level is not well-motivated, and the paper does not provide a clear explanation of how this embedding contributes to the enhancement process. A more thorough investigation into the effects of this parameter, including ablation studies, is needed to justify its inclusion.
3.	There should be more in-depth analysis or discussions with other SOTA approaches to demonstrate the technical contributions of the proposal. Only describing the visual results cannot give readers many insights, but only leads them think that the proposed approach is more like engineering rather than research. The paper needs to provide a more rigorous comparison with existing state-of-the-art methods, beyond just visual comparisons. A quantitative analysis of the proposed method's performance against other approaches, including metrics such as computational cost and memory usage, is necessary to fully demonstrate its advantages. The current presentation does not offer sufficient insight into the technical contributions.
4.	The ablation study should be conducted in the main paper instead of the appendix. 
5.	Some format issue and typos: a)	The "ramdom" in line 259; b)	Remove period symbol in the section title “Conclusion and Limitation.”

### Questions
Please see the weaknesses.

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
This paper proposes a video super-resolution algorithm called VEnhancer, which enhances video resolution in both spatial and temporal dimensions. The method is based on a pretrained video generation model, with a Spatio-Temporal (ST) Controller trained specifically for the task. The video to be enhanced is provided as a condition input to the ST-Controller. The authors constructed a test dataset, AIGC2023, to validate the effectiveness of the algorithm.

### Strengths
1. From the visual results provided by the authors, the proposed method enhances the video's spatial resolution and FPS. The details of objects are richer compared to the pre-enhancement version, and the smoothness of the video has also improved to some extent.
2. This method can achieve both temporal and spatial video super-resolution simultaneously.

### Weaknesses
1. The proposed method's overall idea is quite similar to ControlNet: both introduce a control branch by copying the encoder of the UNet model to the control branch and initializing the output layer to zero. The difference lies in their applications—this method uses the framework for video super-resolution, while ControlNet is designed for controllable generation. In this paper, the condition is the video to be super-resolved, whereas in ControlNet, conditions include modalities like depth, edge, and mask. The authors should explicitly discuss how their approach differs from or improves upon ControlNet for the specific task of video enhancement. Specifically, the core architectural similarity, which involves duplicating the UNet encoder and initializing the output layer to zero for the control branch, needs further justification. The authors should clarify why this specific design choice is optimal for video super-resolution, rather than simply adapting the ControlNet structure. The use of 3D CNNs in the video model, compared to the 2D CNNs in ControlNet's image model, is a notable difference, but the fundamental control mechanism remains largely the same and requires more detailed analysis.
2. For the video-aware conditioning (section 4.3), the noise augmentation technique proposed by the authors is a common trick that was first introduced by *Cascaded Diffusion Models* [Jonathan Ho et al., 2021] for multi-stage high-resolution image generation. Essentially, it incrementally upscales from low to high resolution, which is quite similar to this paper's application. Additionally, using the time embedding as a condition is a standard approach in diffusion models. Conditioning on the downscale factor is somewhat analogous to using FPS as a condition in video generation [Make-A-Video, Uriel Singer et al., 2022], allowing the generation process to better incorporate additional conditioning information. This approach isn't particularly novel in itself. The authors should clarify what specific innovations or improvements their approach offers over these existing techniques. The method of encoding the noise level using an MLP and a zero-initialized linear layer, while potentially effective, is not a substantial departure from existing practices for conditioning diffusion models. The authors should provide a more in-depth analysis of how this specific encoding method contributes to the performance gains, beyond simply stating that it works well. Furthermore, the conditioning on the downscale factor, while different from FPS, still falls under the general category of providing additional information to the diffusion model, and the authors need to demonstrate a more significant innovation in how this is implemented and utilized.
3. The proposed method is for video super-resolution and, theoretically, should be applicable to both AI-generated videos and real videos. However, the authors only conducted experiments on AI-generated videos (section 5.3), making this comparison less comprehensive. I suggest that the authors include experiments on real-world videos or explain why their method might not be suitable for such videos if that's the case. The lack of experimentation on real-world videos is a significant limitation. The authors should address the potential challenges in applying their method to real-world scenarios, such as handling noise, artifacts, and diverse content, and provide a justification for why their method is limited to AI-generated videos. This narrow focus limits the practical applicability of the proposed method.

### Questions
1. In terms of experimental results, the proposed method shows only minor improvements in Aesthetic Quality Dynamic, Degree of Motion, and Smoothness, while achieving relatively significant improvements in MUSIQ and DOVER. What causes this discrepancy?
2. As shown in Table 3, the improvement of the proposed method on CogVideoX-5B is relatively minor and not as significant as on VideoCrafter-2. Could the authors explain the reasons for this?
3. How many videos are there in the AIGC2023 dataset? What are the approximate resolutions and lengths of these videos? Is there any statistical information available? Will the authors release this test set in the future?

### Soundness
2

### Presentation
2

### Contribution
2
