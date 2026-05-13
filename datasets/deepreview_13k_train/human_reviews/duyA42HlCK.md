# HyperHuman: Hyper-Realistic Human Generation with Latent Structural Diffusion

- Decision: Accept
- Scores: 1, 6, 8, 6

## Abstract
Despite significant advances in large-scale text-to-image models, achieving hyper-realistic human image generation remains a desirable yet unsolved task.
Existing models like Stable Diffusion and DALL·E 2 tend to generate human images with incoherent parts or unnatural poses. 
To tackle these challenges, our key insight is that human image is inherently structural over multiple granularities, from the coarse-level body skeleton to the fine-grained spatial geometry. 
Therefore, capturing such correlations between the explicit appearance and latent structure in one model is essential to generate coherent and natural human images.
To this end, we propose a unified framework, \modelname, that generates in-the-wild human images of high realism and diverse layouts. Specifically, \textbf{1)} we first build a large-scale human-centric dataset, named \textit{HumanVerse}, which consists of $340$M images with comprehensive annotations like human pose, depth, and surface-normal. \textbf{2)} Next, we propose a \textit{Latent Structural Diffusion Model} that simultaneously denoises the depth and surface-normal along with the synthesized RGB image. Our model enforces the joint learning of image appearance, spatial relationship, and geometry in a unified network, where each branch in the model complements to each other with both structural awareness and textural richness. \textbf{3)} Finally, to further boost the visual quality, we propose a \textit{Structure-Guided Refiner} to compose the predicted conditions for more detailed generation of higher resolution. Extensive experiments demonstrate that our framework yields the state-of-the-art performance, generating hyper-realistic human images under diverse scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces HyperHuman, a novel framework designed to address the challenge of generating hyper-realistic human images from text and pose inputs. It builds upon the foundations of diffusion models, improving upon the limitations of existing models like Stable Diffusion and DALL·E 2 that often fail to generate human images with coherent parts and natural poses. The key innovation is the integration of structural information across different granularities within a unified model to generate realistic images. The authors also curated a new dataset, HumanVerse, featuring a vast number of images with comprehensive annotations.

### Strengths
1. The Structure-Guided Refiner and improved noise schedule for eliminating low-frequency information leakage showcase thoughtful technical innovation.

2. The Latent Structural Diffusion Model's ability to simultaneously process and align RGB images, depth, and surface normals could result in more accurate and detailed images.

3. The paper achieves state-of-the-art performance in generating diverse and high-quality human images, which, if validated, marks a significant advancement.

4. The HumanVerse dataset's extensive size and detailed annotations can greatly benefit the generative model by providing a diverse range of training examples. Is valuable for the community.

### Weaknesses
I don't have major concerns, but it would be beneficial to discuss the following questions:

1. Given the model's architecture involves shared modules for different data modalities, could you elaborate on how the framework ensures the distinctiveness of modality-specific features? In particular, is there any mechanism within the model to prevent potential feature homogenization and maintain the integrity of the unique distributions associated with RGB, depth, and normal maps? It is unclear how the model avoids learning a common representation that blurs the lines between these distinct modalities, especially given the shared layers in the architecture. A more detailed explanation of the specific architectural choices that enforce modality separation is needed.

2. It would be insightful to understand how the model generalizes to unseen poses and whether there are specific pose complexities that present challenges. While the paper demonstrates impressive results on common poses, it's important to understand the limitations of the model when faced with more complex or unusual poses. For example, how does the model perform with extreme limb articulations or poses that involve significant self-occlusion? A discussion of these limitations is crucial for a thorough evaluation.

3. The computational requirements for annotation and training are significant, given the use of multiple GPUs. Are there potential optimizations or simplifications that could maintain performance while reducing resource demands? The paper mentions the large scale of the HumanVerse dataset, but doesn't provide much detail on the computational cost of creating and using this dataset. It would be helpful to understand the bottlenecks in the training process and potential ways to alleviate them, such as through more efficient model architectures or training strategies.

4. The model can generate photo-realistic and stylistic images. How does the model balance realism with artistic style variations, and could there be a more detailed explanation of how this balance is achieved? The paper demonstrates the ability to generate both photorealistic and artistic images, but it's not clear how the model achieves this balance. Is it simply a matter of prompt engineering, or are there specific mechanisms within the model that allow for this control? A more detailed explanation of this aspect would be valuable.

5. Considering the rapid pace of advancement in this field, what are the authors' plans for updating or maintaining the model to keep up with emerging techniques and standards?

### Questions
Please see the Weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper constructs a large-scale dataset HumanVersea containing 340M images for better human image generation with stable diffusion. The proposed approach also denoised depth and surface normal in addition to the RGB space and shows further improvements. The paper compares with multiple baselines to demonstrate the superiority of the proposed method.

### Strengths
1. The proposed approach is simple yet effective. It’s interesting to see how predicting depth and normal improves the human image quality.

2. The paper addresses an important problem where existing methods show various limitations. The paper compares multiple baseline methods and shows promising results. The constructed dataset is a notable contribution.

3. The paper is in general easy to read.

### Weaknesses
1. The curated dataset is filtered with the criteria: only those images containing 1 to 3 human bounding boxes are retained; people should be visible with an area ratio exceeding 15%; plus rule out samples of poor aesthetics (< 4.5) or low resolution (< 200 × 200). I wonder if these rules reduce the diversity of the images that the model could produce, e.g., group/family photo or small faces? This is also observed in some visualizations in the supplementary materials where it does seem like the model improves the visual quality at the cost of diversity. I wonder if the authors could comment more on this? Besides, the CLIP alignment score is also a bit lower than SDXL, is it related to this diversity issue?

2. Since providing accurate poses in real applications is hard, it would be very useful if the model also produces pleasant unconditional results. So I am also curious about the unconditional results. To be specific, how about images synthesized with just the text input without the poses? 

3. Related to the previous question, how robust the model is to the input pose? If the input skeleton is jittered for all joints, would the model still produce high-quality images? I am also curious if the sampled noise is fixed and only the input pose is animated, is it possible to animate the image?

4. In Table 2, how about RGB + normal? Since depth and normal are closely related, is it necessary to include both?

5. Regarding the results in Table 1, I am not sure why SDXL is much worse than SD? Could the authors further clarify on this? In addition, it also looks a bit strange to have DeepFloyd-IF 1024 images downsampled. Is it possible to directly compare the 1024 resolution with the proposed method?

6. Since the numerical results are mainly without the second-stage refiner plus the second-stage dataset is internal, it would be helpful to show visual results with only the first stage.

7. I am not sure if this intuition is well explained. Maybe the authors could further clarify “Such monotonous images may leak low-frequency signals like the mean of each channel during training; The zero terminal SNR (αT = 0, σT = 1) is further enforced to eliminate structure map’s low-frequency information.” in subsection “Noise Schedule for Joint Learning”.

8. Will the dataset be released for both stages?

9. Does the input pose also contain the face landmarks or hand poses? Or just the body skeleton? If it's just skeleton, would adding hand poses helps with the generated details?

### Questions
Pease see my questions above. I think in general the paper shows promising results but I am not sure if this comes with additional cost of the diversity.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a unified framework called HyperHuman for generating high-quality human images with diverse poses, appearances, and layouts. The authors curate a new dataset called HumanVerse with rich annotations (human pose, depth, and surface normal) to train the model. The framework consists of two modules: the Latent Structural Diffusion Model and the Structure-Guided Refiner. The former module denoises the depth and surface normal along with the RGB image conditioned on the caption and skeleton, while the latter module generates higher-resolution images based on the predicted depth, surface normal, and provided skeleton. The paper's contributions include introducing a new dataset with rich annotations, proposing a novel framework for human image generation which yields superior performance, and generating realistic humans under diverse scenarios.

### Strengths
1. The paper proposes a large-scale curated human-centric dataset with comprehensive annotations (human pose, depth map, surface normal) that may benefit a lot in future research in the field of human image generation.
2. The author introduces a new approach for incorporating the body skeletons, depth and surface normals by jointly denoising depth, surface normal and RGB images and a robust conditioning scheme with text prompt and human pose. The paper also conducts ablation study to prove the effectiveness of this.
3. The proposed method is extensively evaluated on the human-centric dataset MS-COCO 2014 Validation Human to many other SOTA approaches and outperforms on almost quantitative metrics.
4. The paper also extensively experiments and does an ablation study on the effectiveness of the Structure-Guided Refiner with and without many conditions, noise scheduler and expert branch denoising mechanism.

### Weaknesses
1. The label of the HumanVerse dataset has been created based on other pre-trained models, such as depth and pose estimation models. However, the quality of the dataset does not guarantee accurate labelling (especially in crowded scene or extreme lighting condition), and its reusability for other tasks remains uncertain. The reliance on pre-trained models for annotation introduces potential biases and error propagation, which could limit the dataset's utility for tasks requiring high-precision labels. The lack of a thorough analysis of the annotation quality, particularly in challenging scenarios, raises concerns about the reliability of the dataset.
2. The approach has a noteworthy computational cost. However, when evaluating the results in comparison to the second approach, it becomes evident that the gains in Pose Accuracy are not substantial. (Tab. 1) The marginal improvement in pose accuracy, given the increased computational burden, questions the practical efficiency of the proposed method. The trade-off between computational cost and performance gains needs further justification.
3. The paper's objective is to address incoherent parts and unnatural poses. However, it falls short in terms of providing quantitative metrics to evaluate the effectiveness of the proposed method in addressing these issues. The absence of specific metrics for evaluating coherence and naturalness makes it difficult to objectively assess the method's success in these areas. The reliance on qualitative results alone is insufficient to validate the claims.
4. This paper lacks a fair comparison on two fronts. Firstly, it compares itself to other non-pose conditional guided methods (such as SD and DeepFloy-IF). Secondly, the method discussed in the paper was trained on the HumanVerse dataset, which exclusively contains the rich human class, while other methods are trained on a broader set of classes. The comparison with non-pose conditional methods is not directly relevant, and the training data discrepancy introduces a bias that makes the comparison unfair. The lack of a controlled comparison setting limits the validity of the performance claims.

### Questions
1. According to Figure 2, the pose skeleton is encoded before being concatenated with noise. What is the encoder used for the pose, and how does the author process the pose input before encoding it?
2. What about inference requirements (GPU memory, time)?
3. How do we ensure the input pose and caption are aligned with the predicted depth, map, and surface normal? Is there any evaluation on this?
4. In the qualitative result, the comparison among other SOTA methods does not include the pose skeleton figure, I suggest adding it for better visualization.
5. The description of Figure 2 lacks clarity, particularly when the authors refer to the colours "purple" and "blue." However, the figure itself makes it confusing to recognize which part they mention. I suggest the authors should redraw it.  
6. I suggest adding the ablation study between joint denoising the targets and individually denoising the targets to show the effectiveness of joint denoising. This is the main technical contribution beside the new dataset. 
7. In Table 7: Additional Ablation Results for Structure-Guided Refiner, no ablation study on conditioning on predicted low-resolution image x (from the first module).

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a framework aiming to better preserve and enhance human generation using T2I models. It has multiple contributions, it first collects a large-scale human-century dataset with structure information like depth/skeleton and surface-normal. It also proposes a latent structure module to jointly model images and other structure output, further, it proposes a structurally guided Refiner to better compose the predicted conditions and improve image quality. Experiments show HyperHuman can achieve SoTA performance in diverse scenarios.

### Strengths
– This paper is well written and has clear motivation – trying to improve the control consistency in human generation, which is missing from the current control pipeline work like controlnet and T2I-adapter
– The proposed expert branches are interesting and well-study, i.e. how to balance feature sharing and model capacity for each modality,

### Weaknesses
– A study on modality-specific reconstruction using RGB VAE is missing, I think the author needs to study if RGB VAE is suitable to encode structure information or if further finetuning is needed.
-- An important baseline that finetunes on HumanVerse images without structure outputs using the SoTA network architecture is missing. It is not clear to me how much improvement the structure prediction brings to the performance. i.e. do we really need to predict the structure information or we can just fine-tune the general-purpose T2I model to the human images dataset?
-- The curated HumanVerse dataset is claimed to be one of the contributions, but the author did not mention if they will open-source the dataset. I hope the authors can clarify this as it can hurt the contribution of this paper if the dataset is kept internal.

### Questions
– It is not clear to me why to use independent noise for modeling the different modalities, have you tried modeling using a single noise?
– Depth, normal etc have different distributions to RGB images, how do you ensure the VAE can capture its semantic in the latent space?
– It is not clear to me how you use the output of the first stage model which is in lower resolution, and input into the Refiner model

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
