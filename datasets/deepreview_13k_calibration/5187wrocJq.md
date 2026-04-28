# Dice-GAN: Generative Adversarial Network  with Diversity Injection and Consistency Enhancement

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
In the field of natural language description tasks, one challenge for text-to-image modeling is to generate images that are both of high quality and diversity and maintain a high degree of semantic consistency with the textual description. Although significant progress has been made in existing research, there is still potential for improving image quality and diversity. In this study, we propose an efficient attention-based text-to-image synthesis model based on generative adversarial network named Dice-GAN. To enhance the diversity of image generation, we design a diversity injection module, which injects noise several times during the image generation process, fuses the noise with the textual information, and incorporates a self-attention mechanism to help the generator maintain global structural consistency while enhancing the diversity of the generated image. To improve the semantic consistency, we designed a consistency enhancement module, which enhances the semantic consistency of image generation by combining word vectors and a hybrid attention mechanism to achieve dynamic weight adjustment for different image regions. We conducted experiments on two widely used benchmark datasets, CUB and COCO. Dice-GAN demonstrated significant superiority in improving the fidelity and diversity of image generation compared to the existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes DICE-GAN, a single-stage text-to-image GAN to produce high-quality and high-diversity images with improved semantic consistency with text condition. The paper proposes two modules: The Diversity Injection (DI) module, which adds learnable noise to the image features for increasing diversity in generated images, and the Consistency Enhancement (CE) module, which allows the model to dynamically adjust the weights of different image features according to input text conditions for improved semantic consistency and fidelity.

### Strengths
1. The idea of adding learnable noise in different training phases and correction with self-attention to improve generation diversity is novel and interesting.

2. The authors demonstrate improved performance on the IS and FID metrics on the CUB dataset and on the FID metric on the MS-COCO dataset.

3. The authors provide an ablation study demonstrating improvements in results by adding Diversity Injection (DI) and Consistency Enhancement (CE) modules.

### Weaknesses
1. The novelty of the work is limited. The idea of feature fusion in Eq 1 in the DI module is not novel and has been explored before[1,2,3] in the context of image generation. Further, the idea of masking features in a condition-dependant manner has limited novelty. 2. Lack of clarity in Sec 3.2 writing and Fig 4. The idea behind Conditional Channel Attention mask($M_c$) and Spatial Attention attention($M_s$) is unclear. The motivation behind generating masks from both average and max channels is also unclear. Further, quantities including $G^{c}_{max}$ and $G^{c}_{avg}$ are missing in Fig 4, making it difficult to understand figure pipeline. 3. The authors claim that Dice-GAN utilizes a single-stage model structure for improved performance but are missing comparisons with multi-stage methods, including StackGAN++[4]. 4. Missing ablation studies: - Why are two feature fusion layers are needed in the DI module? How was this hyperparameter determined? - How does learnable noise $\sigma$ vary when going from lower to higher layers in the trained model? - Missing ablation on design choices in CE module on use of average and max features and conditional channel attention and spatial attention submodule. 5. The proposed method achieves a lower IS score on the MS-COCO dataset, and the authors argue that this is due to the Inception model used in IS computation being pre-trained on the ImageNet dataset. The authors should provide results on Imagenet or Imagenet subset to back their claims.

### Questions
Please see weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, they propose the diversity injection and consistency enhancement module for text-to-image generation. This method contribute to produce high-quality images with increased diversity and enhanced semantic consistency based on text descriptions.

### Strengths
1. Enhanced Diversity: The Diversity Injection module injects noise and text vectors multiple times, ensuring a broad range of image outputs without sacrificing structure.

2. Improved Consistency: The Consistency Enhancement module dynamically adjusts focus on image regions, aligning visuals closely with text descriptions.

### Weaknesses
1. A comparison with recently proposed text-to-image generation models is needed. Not only should there be an analysis of issues with GANs, but also recent Diffusion models, along with performance comparisons. Is there a specific reason you only compared with ShiftDDPMs in the case of Diffusion models? Please provide a detailed response.

2. Please provide a detailed explanation of the table and figure captions.

3. Performance comparisons on diverse datasets are required. Additionally, besides IS and FID, comparisons with other performance metrics are requested (e.g., CLIP score).

4. The examples of qualitative results are too limited.

5. There is a lack of experimental analysis demonstrating the effectiveness of the proposed model structure.

### Questions
Please, see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The manuscript introduces Dice-GAN which incorporates Diversity Injection and Consistency Enhancement modules to address critical challenges in generating high-quality, diverse images while maintaining semantic alignment with textual descriptions. Experimental results demonstrate that Dice-GAN outperforms state-of-the-art models on the CUB and MS-COCO datasets, underscoring its efficacy in enhancing visual quality and fidelity.

### Strengths
1. The introduction of the DI and CE modules marks a significant advancement in text-to-image synthesis. The DI module, which injects noise at multiple stages of generation, and the CE module, which integrates word vectors with hybrid attention, effectively improve both image diversity and semantic consistency.

2. This method achieves SOTA performance.

### Weaknesses
1. The manuscript lacks a detailed examination of the model's performance across varying levels of text complexity. Given that text descriptions can range from simple to highly nuanced, an analysis based on text complexity would provide stronger evidence of the model's robustness and its ability to handle diverse linguistic inputs. Specifically, the paper should include a quantitative analysis of performance metrics (e.g., Inception Score, FID) across different text complexity levels, rather than relying solely on qualitative examples. This would allow for a more rigorous assessment of the model's ability to generalize to different types of textual inputs.

2. The reviewer wants to see the experiment about computational efficiency. The paper does not provide a clear analysis of the computational cost associated with the proposed Dice-GAN model, including training time, inference time, and memory requirements. This is crucial for assessing the practicality of the model, especially when compared to existing state-of-the-art methods. The paper should include a detailed comparison of these metrics with other models, providing a more complete picture of the model's efficiency.

3. The study does not thoroughly investigate the model's capacity to handle various textual attributes, such as color, size, and object positioning. A more focused evaluation of these specific attributes could offer deeper insights into the model's capability to accurately reflect detailed descriptive features and further demonstrate its adaptability. For example, the paper could include experiments where the model is explicitly tasked with generating images based on specific color, size, and position attributes, and then quantitatively evaluate the accuracy of these attributes in the generated images. This would provide a more granular understanding of the model's strengths and limitations.

### Questions
1. How does Dice-GAN perform under different levels of input noise? Given the pivotal role of the DI module, understanding the model's sensitivity to noise levels could provide valuable insights into balancing image diversity and visual quality effectively.

2. What measures were implemented to ensure that the DI module does not excessively degrade visual quality due to noise injection? A detailed discussion on the strategies used to balance noise injection and maintain visual quality would be beneficial.

3. Does the CE module exhibit limitations in maintaining semantic consistency for longer, more detailed text descriptions? An analysis of the CE module's performance with nuanced and complex descriptions would provide a clearer understanding of its efficacy in handling diverse linguistic inputs.

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
4

### Summary
he paper proposes Dice-GAN, an efficient attention-based text-to-image synthesis model. To enhance image diversity, a diversity injection module is introduced, incorporating noise and a self-attention mechanism. A consistency enhancement module, combining word vectors and a hybrid attention mechanism, improves semantic consistency. Experimental results on CUB and COCO datasets demonstrate Dice-GAN's superiority in image fidelity and diversity compared to existing approaches.

### Strengths
- Clear and well-organized presentation.
- Superior performance to other GAN-based methods.

### Weaknesses
 - Limited novelty: While the diversity injection module is a contribution, the core idea of adding noise is not entirely novel.
- Lack of comparison to diffusion models: Given the current dominance of diffusion models in text-to-image generation, a more comprehensive comparison to state-of-the-art diffusion-based methods is essential to establish Dice-GAN's significance.
- Insufficient discussion of other generative models: The paper could benefit from a more in-depth discussion of how other generative models, such as flow-based models and StyleGAN, could be adapted or combined with Dice-GAN to further enhance diversity and quality.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

### Contribution
1
