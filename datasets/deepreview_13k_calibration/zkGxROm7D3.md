# State & Image Guidance: Teaching Old Text-to-Video Diffusion Models New Tricks

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
Current text-to-video (T2V) models have made significant progress in generating high-quality video. However, these models are limited when it comes to generating dynamic video scenes where the description per frame can vary dramatically. Changing the color, shape, position and state of objects in the scene is a challenge that current video models cannot handle. In addition, the lack of a cheap image-based conditioning mechanism limits their creative application. To address these challenges and extend the applicability of T2V models, we propose two innovative approaches: **State Guidance** and **Image Guidance**. **State Guidance** uses advanced guidance mechanisms to control motion dynamics and scene transformation smoothness by navigating the diffusion process between a state triplet <initial state, transition state, final state>. This mechanism enables the generation of dynamic video scenes (Dynamic Scene T2V) and allows to control the speed and the expressiveness of the scene transformation by introducing temporal dynamics via a guidance weight schedule across video frames. **Image Guidance** enables Zero-Shot Image-to-Video generation (Zero-Shot I2V) by injecting reference image into the initial diffusion steps noise predictions. Furthermore, the combination of **State Guidance** and **Image Guidance** allows for zero-shot transitions between two input reference frames of a video (Zero-Shot II2V). Finally, we introduce the novel **Dynamic Scene Benchmark** to evaluate the ability of the models to generate dynamic video scenes. Extensive experiments show that **State Guidance** and **Image Guidance** successfully address the aforementioned challenges and significantly improve the generation capabilities of existing T2V architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
# Summary

The paper proposes a training-free framework for generating better motion dynamics and adding image conditions with existing pre-trained T2V models. Extensive experiments demonstrate the effectiveness of the proposed framework


EDIT:

### Strengths
# Strengths

- The proposed framework is training-free, and indeed achieves better motion dynamics for the mentioned types of prompts
- The proposed framework outperforms the mentioned baselines

### Weaknesses
# Weaknesses

- In Sec. 3, the definition of diffusion models might be incorrect
- The idea of state guidance seems similar to the deforum-like technique used in the stable diffusion user community
- While the guidance schedule seems reasonable, the paper does not mention how it was designed/selected
- Entries in the proposed dynamic scenes benchmark consist of three states tailored for the proposed framework, resulting in inconsistent experiments settings when compared with other baselines which does not support this type of inputs. In that case, is unclear how reliable the proposed benchmark is
- The paper does not mention how generated results were selected. Considering diffusion models can generate various of results from the same input conditions from different seeds, it would be better to report mean+std for each metric and report the success rate of each generation
- For II2V experiments, the paper does not compare with SEINE
- The scale of user study seems relatively limited and the design of user study seems flawed: "more changes" in question 2 does not necessarily indicate the result is better in terms of visual quality. The results with flickering artifacts and incorrect/unfavourable color changes could also be considered as "more changes"


### Questions
Please refer to the weaknesses section

### Soundness
3

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
3

### Summary
This paper proposes a novel video generation guidance method capable of producing videos with drastically different cross-frame descriptions, such as texture changes, morph transformations, and large motions. The core innovation of the method is the state triplet, which decomposes the video into different phases, each with its own distinct description. The state triplet can be generated either from a large language model (LLM) or manually. The proposed method is training-free and has been evaluated on a new video benchmark, achieving performance comparable to methods that require task-specific training.

### Strengths
The proposed method is practically useful given that:

* It enables the transformations that would be very difficult to model with pretrained models, such as morph transformation, drastic texture changes over frames. 

* The method is training-free and does not require text-video pairs with the target motion patterns, which is hard to collect in scale. The training free method achieves comparable performance as the compared training-based method.

### Weaknesses
- The T2V limitation mentioned in L202 is not convincing enough. The prompts used in the paper are relatively simple, consisting of only one or two sentences. Some related works, such as CogVideoX [1], utilize DiT-based structures and demonstrate that detailed prompts significantly improve video generation quality, both in appearance and motion. Therefore, if we consider a scenario with both detailed video captions and a DiT-based model that relies less on explicit per-frame modeling due to (1) temporal compression in the tokenizer, and (2) stronger spatial-temporal modeling capabilities (i.e., cross-frame modeling rather than per-frame), the limitation highlighted for the T2V model becomes less relevant. This is because we would not be restricted by a limited T2I model (point 2) and would benefit from enhanced spatial-temporal modeling (point 1). Furthermore, the paper does not explore the impact of varying prompt complexity on the proposed method's performance, leaving a gap in understanding its robustness. Specifically, it is unclear how the method would perform with more intricate prompts that describe complex object interactions or scene dynamics, which are known to be challenging for current text-to-video models.

- The paper lacks key information on how the transition order is maintained. While Eq. 1 models the joint conditional distribution given the prompt triplet, it does not specify how the generated images are constrained to follow the prompt order: initial -> transition -> final stage.  Ensuring this sequential alignment is crucial for achieving controllability and realism in the generated video. The method needs to explicitly define how the temporal consistency is enforced to ensure that the generated video follows the intended sequence of states, rather than producing frames that are a mix of all states without a clear temporal progression. The absence of such a mechanism raises concerns about the method's ability to generate coherent and realistic videos.

- As mentioned in the limitation section in the supplementary, the method introduces additional hyper-parameters, such as the guidance scale at for the triplet states. Tweaking those hyper-parameter would be a case-specific effort and paper does not propose a principled approach for estimating/optimizing those hyper-parameters. The lack of a systematic approach for hyperparameter tuning makes the method less practical, as users would need to manually adjust these parameters for each specific scenario, which is time-consuming and requires significant expertise. This limitation undermines the method's usability and general applicability.

- As mentioned in the first item, there are strong models taking much more descriptive prompt as input for video generation. However, the paper does not include the comparison with those methods. The lack of this comparison makes the claim about the T2V limitation and the proposed method less convincing. The absence of a comparison with state-of-the-art models that handle complex prompts makes it difficult to assess the true novelty and effectiveness of the proposed method. Without such a comparison, it is unclear whether the method offers a significant advantage over existing approaches, particularly in scenarios with more detailed and complex text prompts.

### Questions
In addition to the key information missing mentioned above, I have several questions related to the details of the paper:

1. How to handle different combinations of text and image prompt? For example, what if we have the triplet description and only the end frame of the generated image? How is this case different from the case where we have the triplet description and only the first frame of the generated image?

2. How is the method able to handle the morph transform even although the pretrained model is rarely trained on videos with morphism since it is not common? More discussion on this would be appreciated.

3. Have the authors try a more detailed caption vs. the simple ones used in the paper? Will that lead to better motion?

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
3

### Summary
The paper describes a method for Text To Video (T2V) generation.
The method proposes two extensions: State and Image guidance.
State Guidance uses state triplets (initial, current, last) to help T2V generate the proper video frame.
Image guidance injects noise in the early stages of the diffusion model to steer it in the right direction.
This is then used to: generate more dynamic video sequences, as well as zero shot video generation from a single image, and a video interpolating between two images.

### Strengths
The extensions are reasonable and the various experiments does show nice videos produced by the system.

In addition, a new dataset is introduced that, hopefully, will help future contributions to the field.

### Weaknesses
 The paper feels rushed. (The caption of the teaser figure misplaced the text for sub-figures (B) and (C)).

I wonder what is the novelty of the proposed method given the "Make Pixels Dance" (CVPR'24) paper.
They, too, use a triplet state representation to encourage better video synthesis. 
Yet, I could not find a direct comparison. Can the authors explain why?

There are many results and one must appreciate the work done by the authors, but it is extremely difficult to follow the experimental results and appreciate the contributions. For example, 

1. Please add a reference to the different methods shown in the various tables.
2. I'm not sure the ablation experiments should appear in the main text. 
3. The supplemental material is difficult to navigate. There are many folders and no easy way to navigate and compare the different results presented there.
4. Table 3: The boldface numbers are confusing as they only refer to the method without SG. Yet, in almost each column there is a better alternative, so it's difficult to judge the overall quality of the results.
5. Table 5: It is confusing to compare VC2+IG with three thresholds to TI2V-Zero and then highlight in bold different measures for different thresholds.

### Questions
Can the authors elaborate on the comparison to "Make Pixels Dance"?

### Soundness
2

### Presentation
2

### Contribution
2
