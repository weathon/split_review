# The Crystal Ball Hypothesis in diffusion models: Anticipating object positions from initial noise

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
Diffusion models have achieved remarkable success in text-to-image generation tasks; however, the role of initial noise has been rarely explored. In this study, we identify specific regions within the initial noise image, termed trigger patches, that play a key role for object generation in the resulting images. Notably, these patches are ``universal'' and can be generalized across various positions, seeds, and prompts. To be specific, extracting these patches from one noise and injecting them into another noise leads to object generation in targeted areas. We identify these patches by analyzing the dispersion of object bounding boxes across generated images, leading to the development of a posterior analysis technique.  Furthermore, we create a dataset consisting of Gaussian noises labeled with bounding boxes corresponding to the objects appearing in the generated images and train a detector that identifies these patches from the initial noise. To explain the formation of these patches, we reveal that they are outliers in Gaussian noise, and follow distinct distributions through two-sample tests. Finally, we find the misalignment between prompts and the trigger patch patterns can result in unsuccessful image generations. The study proposes a reject-sampling strategy to obtain optimal noise, aiming to improve prompt adherence and positional diversity in image generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In the paper, the authors introduce the concept of "trigger patches," which are specific regions within the initial noise image that determine the positional information in object generation. They present a method for localizing these trigger patches, provide analyses to validate their correctness, and demonstrate two applications.

### Strengths
1. The concept of "trigger patches" in the diffusion generation process is both interesting and useful, as it enhances the controllability of the generation.
2. The experiments and analyses are thorough and comprehensive.
3. The writing is clear and intuitive.

### Weaknesses
1. In the evaluation of the second application (Sec 5.2), only "left" and "right" are considered. Is it possible to include more fine-grained positional information, such as "left-down"?
2. In the introduction, it is mentioned that "moving/removing trigger patches can achieve certain image editing effects." Including some image editing results in the experimental section would support this claim.
3. In cases where "trigger patches" and prompts are aligned, the positional generation accuracy is 63.5%. What factors contribute to the failures in the remaining cases? Can the authors provide a failure analysis?

### Questions
Please address the questions / concerns in the weaknesses section.

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
This article introduces the intriguing concept of trigger patch noise. The authors first demonstrate the existence of trigger patch noise, then propose a method using neural networks to detect this noise in initial noise. They experimentally verify the unique characteristics of trigger patch noise and explore its potential applications, such as controlling object generation position by embedding trigger patch noise into the initial noise.

### Strengths
1.The insight is interesting.

2.The authors not only demonstrated the existence of trigger patch noise through experiments but also provided a method for its detection. Additionally, the authors thoroughly explored the effects of multiple trigger patch noises, examined the relationship between trigger patch noise and prompt guidance, and investigated the generalization capabilities of trigger patch noise.

3.I believe that the proposed concept of trigger patch noise has the potential to advance research and development in the field of controllable generation.

### Weaknesses
1.The experiment was conducted with only five object categories. Can trigger patch noise be generalized to a broader range of object categories? This could provide insights into its robustness across diverse applications.

2.Does trigger patch noise commonly exist within any randomly sampled Gaussian noise? Additionally, if multiple trigger patch noises are present in a single Gaussian noise, what criteria should be used to select the most effective trigger patch noise?

3.In the training process of the trigger patch noise detector, how do you define the ground truth for trigger patch noise? Providing a detailed algorithm or clarification of this aspect would be valuable. Furthermore, does every one of the 17,000 noises in the training set contain trigger patch noise?

4.There seems to be an impact on image realism when inserting trigger patch noise. How significant is this effect, and are there any methods to mitigate it? (The BLIP-Text results in Table 11)

5.The detection accuracy of trigger patch noise reported in the paper appears somewhat limited. Are there plans or suggestions for enhancing detection performance?

6.What would be the effect of inserting multiple (e.g., three) trigger patch noises? Additionally, when aiming to control the size of the generated object, does resizing the trigger patch noise (e.g., scaling) still yield the intended effect?

7.Can the trigger patch noise work for DiT models?

### Questions
See weakness.

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
3

### Summary
The work finds out that there are some locations in the image frame where the diffusion often gets biased. These locations are marked as trigger patches. An object detector is trained to detect these patches before the sampling process. After that, rejection sampling is used to reject samples with trigger patches to obtain the better generative image diversity.

### Strengths
Strength:
1. The paper provides an interesting point of view on diffusion sampling
2. The new sampling methods help to increase the diversity

### Weaknesses
Weaknesses:
1. According to Figure 1 and Figure 3, the trigger patches are always in the right part of the image and only applicable to some objects. The whole paper also only focuses on some round objects like balls and tennis balls. This results in the question of generalization of the work. Whether or not this phenomenon will happen across datasets or with different objects?
2. The experimental results do not show the quantitative values to measure the output quality. There could be a trade-off between diversity and quality according to the new rejection sampling.
3. The current diversity result is not standard in generative measures such as FID/Recall.

### Questions
1. Please test on wider range of objects as well as datasets or find the trigger patches on different locations of the dataset instead of the right edge of the photo.
2. Please provide the qualitative values for image quality and observe the trade-off between diversity and image quality from the proposed rejection sampling method.
3. Please provide more comprehensive evaluations on diversity such as FID/Recall.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the influence of initial noise in the text-to-image generation tasks. They identify specific regions within the initial noise termed as trigger patches, which contribute to the positional bias in the generated images. In order to automatically discover the trigger patches, the authors train a detector. Next, the authors explore several special and interesting attributes of trigger patches, and discover the differences between the random patch within the initial noise and trigger patch. At last, based on the discoveries, the authors design two speical applications for trigger patch.

### Strengths
Thanks for the authors` efforts. I find this paper very interesting, and the experimental section is quite comprehensive. It has provided me with many insights and considerations.

1. The paper is well-organized, and the presentation of this paper is very good.

2. The motivation of this paper is clear, and it first explores the influence of positional bias in the initial noise. I think the experiments are quite comprehensive. I think this paper is valuable.

3. Some experiment results are very attractive, and they have sparked a lot of my thoughts and reflections.

### Weaknesses
Although, from my perspective, this paper is good, I think it still has several drawbacks:

Presentation:

1. In line 231, "As shown in the Figure", missing reference to the Figure. In line 293, missing (2) before "Can noises with multiple ...". In line 417, ":" is missing after "Control", and the first word after ":"， should be lowercase.  In line 1070, "Please refer to the Fig F.2 for visualized results.", I can not find the Fig.F2.

2. In Figure 13, the prompt is not consistent with the provided images.

3. All intuitive images in the main paper only contain five concepts. Can the authors provide more visualization results?

Methods and Experiments:

1. For the evaluation metrics, the authors only utilize the CLIP. I think it is crucial to utilize some human preference models like PickScore, HPSv2 to evaluate the quality of the generated images.

2. The dataset constructed by the authors only contains five single concepts, consisting of 500K samples. How do the authors ensure that whether the trigger patches exist beyond these five prompts, and the detector trained in this manner can recognize other concepts? Besides, I think the construction of the dataset is resource-consuming.

3. The authors claim that low entropy ISR will be higher; however, Table 6 shows that certain mid-entropy ISRs are also quite high. How should the authors explain this phenomenon?

4. All of the main results are conducted only in Stable Diffusion v2. Can the authors provide the existence of the trigger patches in other diffusion models?

5. Experiment results in Table 5 reveal “Random” can surpass "Initno" and "Attend-and-Excite". This phenomenon is very strange because as far as I know, both of them optimize the noise during the reverse process. They should be higher than "Random"?

6. The experiment results in Generalization part raise my concerns. From the results presented in Table 8, it seems that trigger patch injection is only effective with deterministic samplers, showing no impact on stochastic samplers. The authors also default to using a deterministic sampler. Besides, based on the results in Table 10, why is the gap reduction so pronounced across other models? If the initial noise inherently carries positional bias, then its performance across different diffusion models should be similar. However, the experimental results seem to contradict the notion that the trigger patch is universal.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
