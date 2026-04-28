# Controlling Vision-Language Models for Multi-Task Image Restoration

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Vision-language models such as CLIP have shown great impact on diverse downstream tasks for zero-shot or label-free predictions. However, when it comes to low-level vision such as image restoration their performance deteriorates dramatically due to corrupted inputs. In this paper, we present a degradation-aware vision-language model (DA-CLIP) to better transfer pretrained vision-language models to low-level vision tasks as a multi-task framework for image restoration. More specifically, DA-CLIP trains an additional controller that adapts the fixed CLIP image encoder to predict high-quality feature embeddings. By integrating the embedding into an image restoration network via cross-attention, we are able to pilot the model to learn a high-fidelity image reconstruction. The controller itself will also output a degradation feature that matches the real corruptions of the input, yielding a natural classifier for different degradation types. In addition, we construct a mixed degradation dataset with synthetic captions for DA-CLIP training. Our approach advances state-of-the-art performance on both \emph{degradation-specific} and \emph{unified} image restoration tasks, showing a promising direction of prompting image restoration with large-scale pretrained vision-language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a framework called degradation-aware CLIP (DA-CLIP) that combines large-scale pretrained vision-language models with image restoration networks. The authors address the issue of feature mismatching between corrupted inputs and clean captions in existing vision-language models (VLMs) by an Image Controller that adapts the VLM's image encoder to output high-quality content embeddings aligned with clean captions. The controller also predicts a degradation embedding to match the real degradation types. The paper presents the construction of a mixed degradation dataset for training DA-CLIP and demonstrates its effectiveness in both degradation-specific and unified image restoration tasks. The results show highly competitive performance across ten different degradation types.

### Strengths
- This paper proposes a novel framework, DA-CLIP, which combines large-scale pretrained vision-language models with image restoration networks.
- This paper introduces an Image Controller that addresses the feature mismatching issue between corrupted inputs and clean captions in existing vision-language models. In addition, they introduce a prompt learning module to better utilize the degradation context for unified image restoration.
- It demonstrates that DA-CLIP in both degradation-specific and unified image restoration tasks, achieving highly competitive performance across all ten degradation types.

### Weaknesses
 - In Figure 1, DA-CLIP achieves surprisingly high accuracy in ten degradation types. How are these experiments set up? In contrast, CLIP performs poorly in many types. What prompts do the authors use for classifying degradations in CLIP?
- In Figure 6, PromptIR is comparable or even better than the proposed DA-CLIP in most tasks on fidelity metrics.
- In Table 2(c), the PSNR of DA-CLIP highly deviates from that of MAXIM. In addition, the results on task-specific restoration do not show a clear benefit of using a universal model for all tasks. It is believed that the merit of universal models is that different tasks can benefit each other, or at least be helpful in generalization to new domains.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a degradation-aware CLIP model. It is aligned with language through dual aspects of image content and degradation during training. This DA-CLIP can extract information not only about the image content but also about image degradation. The authors also combined DA-CLIP with image restoration, proposing what they call a "universal" image restoration method. This method is based on Diffusion-Based restoration techniques, but the DA-CLIP's results are used as controlled prompts for input. The authors have showcased many results.

### Strengths
I hold a positive view on the idea of incorporating degradation information into CLIP.

### Weaknesses
My main concern with this paper is its task setting. First, "Universal Image Restoration" is a term that is not so easily justified. This paper simply brings together ten different image restoration tasks, which is closer to "multi-task" than the so-called "universal". For a large model, mixing these ten tasks in such a separate manner for training, the model would internally categorize the problems before handling them in a single-task manner. This would not endow the model with sufficient generalization capabilities. For instance, an image with both rain streaks and subsequent compression artifacts cannot be accurately restored. This is not "universal". Moreover, this paper seems to ignore a host of more "universal" solutions, such as Real ESRGAN, BSRGAN, StableSR, DiffBIR, etc. Merging degradations to achieve better generalization is a new direction (which is not so new anymore). But this paper barely discusses whether these methods are "universal" or not.

Secondly, DA-CLIP's ability to predict degradation is not particularly special, considering the task setting only involves ten types of degradation; it can be said that almost any image restoration model trained on these degradations or any model that understands or classifies them would have this ability. I can only say that introducing degradation into CLIP is a very promising direction and could be very useful. However, the approach taken in this paper fails to reflect any significance in doing so. Due to the inherent issues with the task setting of the paper, the experimental part also fails to demonstrate the corresponding contributions.

### Questions
See Weakness

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a degradation-aware vision language model (DA-CLIP) to generate high-quality image representation and distinct the degradation types of low-quality inputs for all-in-one image restoration. The DA-CLIP model can be integrated into different image restoration networks to improve the performance. Extensive experiments are conducted to demonstrate the effectiveness of the proposed method.

### Strengths
1. The idea of constructing a vision-language model to restore clean semantic image representation and distinct degradation types of low-quality images is interesting.
2. The method of using clean image representative and degradation prompt to instruct restoration networks for better performance is sound.
3. The results look good, and the experimental analysis demonstrate the effectiveness of the DA-CLIP on all-in-one image restoration.
4. The writing is well, and the paper is easy to read.

### Weaknesses
1. It is questionable that the caption embedding can provide a high-quality image representation supervision for the content embedding. $e_c^T$ can indeed provide a semantic supervision, but there is no guarantee that it is a clean image representation. Therefore, I think the claim that the image encoder with the controller outputs high-quality content features is not rigorous. It seems that $e_c^I$ mainly serves to provide semantic instruction for the restoration network, especially for diffusion-based models. The assumption that a caption embedding derived from a low-quality image can accurately guide the learning of a high-quality content embedding is not well-justified. The caption, while semantically related, may lack the fine-grained details necessary for precise image reconstruction, particularly in cases of severe degradation. The method relies on the assumption that the text encoder is invariant to image degradation, which may not hold true in practice, potentially leading to inaccurate content embeddings.
2. The used experimental setup is too simple to demonstrate the superiority of this complex method. It is not difficult for a unified network, e.g., a vanilla version Restormer, to deal with the all-in-one image restoration setting with a specific degradation level for each degradation type. The experiments lack a thorough comparison with simpler baselines, and the performance gains may not be solely attributed to the proposed DA-CLIP. The use of a fixed degradation level for each degradation type simplifies the problem, and the method's effectiveness in more complex scenarios with varying degradation levels within the same type is not demonstrated. The experimental design does not sufficiently challenge the proposed method, making it difficult to assess its true potential.
3. This paper do not provide the experiment about the generalization ability of the proposed method. I do some tests using the code provided by the authors, and the results show that the model cannot deal with out-of-distribution degradations as well as OOD degradation levels well. It is not surprising as the used degradation model is too simple. This also reflects that $e_c^I$ is not always a high-quality image representation. The lack of experiments on out-of-distribution data raises concerns about the method's practical applicability. The simple degradation model used for training limits the method's ability to handle real-world degradations, which often exhibit complex and diverse characteristics. The observation that $e_c^I$ does not consistently represent a high-quality image further undermines the core claim of the proposed approach.
4. This method may be difficult to handle tasks with different degradation levels, because it is difficult to describe the specific degradation level in texts. Since the authors do not provide relevant experiments, the potential of this method to handle multiple degradation levels is still questionable. As far as the current results are concerned, the approach is not practical enough. The method's reliance on text prompts to describe degradation types may not be sufficient to capture the nuances of varying degradation levels. The absence of experiments demonstrating the method's performance across a range of degradation levels makes it difficult to assess its robustness and practical utility. The inability to explicitly represent degradation levels in text limits the method's applicability to real-world scenarios where degradation severity can vary significantly.

### Questions
1. Do both $e_c^I$ and $e_d^I$ have an important impact on the restoration performance? Intuitively, it is reasonable for diffusion-based models as $e_c^I$ controls the content and $e_d^I$ indicates the degradation. However, it seems not reasonable for mse-based models to use $e_c^I$ in the restoration process. 
2. What performance can be achieved by directly providing the semantic text prompt and the degradation type prompt to train the all-in-one image restoration diffusion model?
3. What performance can be achieved by directly training a vanilla Restormer under the same all-in-one setting?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel method for universal image restoration. The method, named as DA-CLIP, is based on the CLIP and diffusion model (IR-SDE). An additional controller is proposed to help predict high-quality content embedding and degradation type embedding. These two embeddings are then used through cross attention in a diffusion unet to help restore the degraded images. The proposed method is tested on the image denoising, inpainting, deblurring, etc. The experimental results show that the proposed method can achieve better performance than the state-of-the-art methods.

### Strengths
1. The paper proposes a novel framework, DA-CLIP, to learn high-quality content and degradation embeddings through contrastive learning. 
1. The integration of the degradation and content prompts to universal image restoration appears effective and innovative.
1. Extensive experiments on various tasks are conducted to show the effectiveness of the proposed method.

### Weaknesses
1. There are no justifications about what is embedded in the HQ content embedding. It is better to provide some comparisons with the HQ content embedding and the original image embedding.
1. The effectiveness and necessity of the prompt learning module is not well discussed. It is better to provide some ablation studies to show the effectiveness of the prompt learning module compared with naive cross-attention.  
1. The performance compared with `NAFNet+DA-CLIP` is not superior.  
1. Although the paper discussed the computation complexity in supplementary material, it only provides #params and FLOPS. It is known that the FLOPS is not a good metric for the computation complexity, especially for diffusion models which require multiple iteration steps. The paper should provide the inference time for the proposed method, and better in main paper. 
1. Experiments on more complex degradation scenarios, involving multiple concurrent degradation types, would emphasize the model's robustness and versatility.
1. A deeper discussion about the text encoder's role in the performance could lead to a better understanding of the proposed framework.

### Questions
#### **1. Why VLM like CLIP is necessary in this paper ?**

After reading the paper, I think that the proposed method does not have much relationship with VLM like CLIP. The DA-CLIP serves as a degradation type classifier and a content classifier. It seems OK to replace CLIP with simple CNNs such as ResNet. Given that the degradation types are quite limited in this paper, a text-encoder like CLIP is easily to be replaced with simple classification. As for the captions, we may also simply replace it with just clean image embeddings to perform contrastive learning.   

#### **2. Why diffusion model is used for restoration process ?**

Given the slow inference of diffusion model, it is not clear why diffusion model is used for restoration process. After all, the proposed method has little relationship with diffusion model, especially when the diffusion network is trained from scratch. Compared with `NAFNet+DA-CLIP`, the diffusion based backbone does not have much advantages.

#### **Summary & Conclusion**
In summary, I think that using contrastive learning to learn degradation type embedding and content embedding for universal image restoration is a good idea. And the experiments are also quite comprehensive and effective. However, the proposed integration with VLM and diffusion models are not well justified. And I do not think it is appropriate to claim vision-language models as the main contribution and novelty of this paper.

To conclude, I would like to give borderline to this paper. However, there is no such options in the review form. So I choose to give a marginal accept. I hope the authors can address my concerns in the rebuttal.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
