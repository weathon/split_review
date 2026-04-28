# LumiSculpt: A Consistency Lighting Control Network for Video Generation

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
\gb{
Lighting plays a pivotal role in ensuring the naturalness of video generation, significantly influencing the aesthetic quality of the generated content.
However, due to the deep coupling between lighting and the temporal features of videos, it remains challenging to disentangle and model independent and coherent lighting attributes, limiting the ability to control lighting in video generation. 
In this paper, inspired by the established controllable T2I models, we propose \sysname, which, for the first time, enables precise and consistent lighting control in T2V generation models.%
\sysname equips the video generation with strong interactive capabilities, allowing the input of custom lighting reference image sequences. 
Furthermore, the core learnable plug-and-play module of \sysname facilitates remarkable control over lighting intensity, position, and trajectory in latent video diffusion models based on the advanced DiT backbone.%
Additionally, to effectively train \sysname and address the issue of insufficient lighting data, we construct \dataname, a new lightweight and flexible dataset for portrait lighting of images and videos. 
Experimental results demonstrate that \sysname achieves precise and high-quality lighting control in video generation.
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes LumiSculpt to deal with the lighting control for video generation. Controlling lighting is a fundamental need for image and video synthesis tasks. This work can control the light intensity, position, and trajectory. Besides the proposed model, this work also constructs a dataset composed of portraits with different lighting conditions.

### Strengths
1. This work achieves precise control of the lighting of the portrait in the video generation tasks. 
2. The plug-and-play design of the module makes this work flexible to be combined with other foundation models. 
3. The LumiHuman will benefit the community if it can be made public available.

### Weaknesses
1. From what I understand, the LumiHuman is synthetic, which may limit the model's performance in real-world cases. I wonder if there can be a thorough evaluation of real-world cases. Meanwhile, there are only 65 individuals in the dataset, which may limit the model to generalize to new portraits. 
2. The generated videos are not informative enough. The motion dynamics are not enough. I wonder if there are results where the portrait and background can move more vividly. Furthermore, the lack of diversity in motion and background severely limits the practical application of the model. The current results do not demonstrate the model's ability to handle complex real-world scenarios where both lighting and motion are dynamic and varied. The over-exposure in some generated videos also raises concerns about the robustness of the lighting control mechanism.

### Questions
More cases on real-world cases.

### Soundness
3

### Presentation
3

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
The paper propose a approach to precise lighting control in text-to-video (T2V) generation. The authors design a model named LumiSculpt, which introduces plug-and-play lighting control to enhance video generation with adjustable lighting intensity, direction, and trajectory, all controlled through textual inputs. LumiSculpt uses a dual-branch framework with a frozen branch to ensure diversity in appearances while maintaining lighting control.  Besides, the authors introduce a specialized dataset, LumiHuman, containing diverse portrait lighting data generated via Unreal Engine, which supports various lighting trajectories.  The model’s performance is evaluated against state-of-the-art methods, Open-Sora and IC-Light, demonstrating its superiority in lighting accuracy, inter-frame consistency, and semantic alignment with text descriptions.

### Strengths
+ The model design is novel. The introduction of an additional lighting embedding in the diffusion process is reasonable and easy for model to control the lighting. The loss design is cool. It is based on the concept of style transfer but in the latent space. This loss controls the lighting intensity and direction while preserving the appearance.
+ This paper prepares a dataset to enhance lighting control in video generation. Although the sample size is limited, the pipeline design can provide valuable insights for future work.

### Weaknesses
 - This algorithm seems more suitable for image generation, as I did not observe any specific design tailored for video tasks. Video generation is merely an extension of the algorithm’s application. The use of 3D attention is mentioned, but it's unclear how this is specifically integrated to handle temporal lighting consistency, beyond what a standard video diffusion model already provides. The paper lacks a detailed explanation of how the lighting embeddings are processed across frames to ensure smooth transitions, which is critical for video applications.
- In the comparisons, the authors use images generated by the network as the foreground. Does this imply that, limited by the synthetic data used during training, the algorithm may not generalize well to real-world scenes? I also noticed unnatural foreground (human) generation results in the video demo. The reliance on synthetic data for training raises concerns about the model's ability to handle the complexities of real-world lighting conditions and diverse scene content. The paper does not provide sufficient analysis on the impact of synthetic data on the model's generalization capabilities, particularly when dealing with real-world image and video data.

### Questions
In addition to the weaknesses mentioned, I have the following concerns:
1. Can this dataset be open-sourced to ensure reproducibility for future work?
2. I find the caption augmentation section somewhat unclear. Is it simply replacing captions, or does it involve corresponding changes in the image background as well?

### Soundness
3

### Presentation
2

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
This paper proposes a control module for Text-2-Video models to enable lighting control. This is an extremely challenging task due to the lack of large-scale lighting datasets and the ambiguity between lighting and material properties. The key idea of the paper is to train a control network using a synthetic dataset, LumiHuman, consisting of 65 identities under various frontal illuminations defined over a uniform grid. The proposed dataset allows to combine the frames into various lighting trajectories. During training, a flat shading map is used as conditioning signal. The method shows impressive lighting control for static human portraits and is able to introduce cast shadows as well, which is really impressive.

### Strengths
* The proposed LumiHuman dataset can be valuable to the community. It is a great idea to place point lights close to each other to make it possible to compose frames into videos.
* The results look great, especially the cast shadows. 
* The paper can provide interesting insights about the internal lighting prior of recent diffusion models.

### Weaknesses
I believe that the paper has multiple crucial flaws, which would require a major revision:
* **W1 -** The proposed dataset, which is one of the main contributions, seems to be a bit limited. The synthetic renderings could follow the usual light stage setup with full coverage, not just frontal lighting. Furthermore, it is not clear whether 65 identities can provide enough diversity. I believe that the main advantage of using a synthetic dataset is that it can be scaled. To verify this benefit, it would also be crucial to show that available real-world light-stage datasets cannot provide enough supervision to achieve such quality for lighting control. 
* **W2 -** The novelty and effectiveness of the proposed pipeline, which is the second contribution, is not clear. It would be important to highlight the key difference to ControlNet. Now, it seems that the key difference is the dual-branch predictions, although the effectiveness of this idea is questionable based on the ablation. Furthermore, the proposed disentanglement loss is not well-motivated. The key assumption is that the latents reflect the appearance. However, the latents contain geometric, material, and also lighting features, thus not being disentangled. 
* **W3 -** It would be great to show the diversity of the generated samples - more samples with the same conditioning.
* **W4 -** Additional baseline comparisons would be important. Although the method uses the T2V models for light editing, the resulting videos are static, making it fair to compare against T2I models. Such comparisons could also give interesting insights about the lighting priors of T2I and T2V models. 
* **W5 -** The key contribution is not clear. Based on the title and abstract it is LumiSculpt, based on the intro (L.087 - Additionally...) it is the dataset LumiHuman. 

Additional weaknesses
* **W6 -** Recent T2I lighting control methods, such as [LightIt](https://peter-kocsis.github.io/LightIt/) could be discussed. 
* **W7 -** The notation on the pipeline figure is not clear. I would recommend naming the specific parameters instead of using "?". However, this might be due to some LaTex errors. 
* **W8 -** Typo in L.204: "using a unreal engine" -> "using Unreal Engine [XYZ]"
* **W9 -** Typo in L.290: "an naive" -> "a naive"
* **W10 -** The formulation could be more precise. E.g., the lighting representation seems to be a flat shading map, but it is not clear. 
* **W11 -** It might be better to narrow the title, reflecting that the domain is human portraits. 
* **W12 -** The lighting is not entirely consistent with the results, e.g., in the first row of Fig. 1. the lighting seems to start from the bottom and move to the top right instead of moving only upwards as depicted in the trajectory.

### Questions
* **Q1 -** What is the reason that the generated samples have a very similar geometry and appearance as IC Light, but highly different to Open-Sora, although the proposed method uses Open-Sora. 
* **Q2 -** Could you please give a bit more details, how exactly are the augmented captions used? If I understand it correctly, the goal with those is to give additional noise to the model to avoid overfitting. 
* **Q3 -** The results look oversaturated, what can be the reason for that?

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
This paper introduces LumiSculpt, a novel model that provides precise and consistent lighting control in text-to-video (T2V) generation. LumiSculpt. This allowing users to input custom lighting reference image sequences. The model includes a plug-and-play module that enables adjustable control over lighting intensity, position, and movement in latent video diffusion models, leveraging the advanced DiT (Denoising Transformer) backbone.

To train LumiSculpt effectively and address the lack of sufficient lighting data, the authors developed LumiHuman, a new, lightweight dataset specifically for portrait lighting in images and videos. Experiments demonstrate LumiSculpt’s ability to achieve precise, high-quality lighting control in video generation, marking a significant advancement in T2V lighting manipulation.

### Strengths
I felt the biggest pros of this paper is that authors explore how to propsoe a  LumiHuman dataset that could benefits current research community. But authors didn't mention whether they will release the dataset.

### Weaknesses
1. My point is that authors biggest contributions are the relighting dataset for video. However, the discussion on these dataset is so limited and there are a lot of details missing on the dataset.
For example: 1.1 How diverse the MetaHuman dataset is since it is only contains 65 individuals.
1.2 how accurate your caption could describe the lighting since  lighting caption is a very unique task that current LLM model is not doing well.
1.3 From the results, I didn't see any caption related to lighting.


2. Since the model is trained on synthetic rendered images, the results are far from photo realism and most of the results from the teaser images are 'fake' portrait with unrealistic facial texture.  

3. It is not clear how authors control the lighting intensity. 


4. IC-light has much better photo-realistic results compared with your methods. And what's the advantage of authors method ? 


5.  It seems that authors only show white/black lighting but not color lighting which ICnet could do. 


6. Regarding model, I don't see any difference between yours and controlnet besides it is a video version.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
