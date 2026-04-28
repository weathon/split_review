# I4VGen: Image as Free Stepping Stone for Text-to-Video Generation

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Text-to-video generation has trailed behind text-to-image generation in terms of quality and diversity, primarily due to the inherent complexities of spatio-temporal modeling and the limited availability of video-text datasets. Recent text-to-video diffusion models employ the image as an intermediate step, significantly enhancing overall performance but incurring high training costs. In this paper, we present \textsc{I4VGen}, a novel video diffusion inference pipeline to leverage advanced image techniques to enhance pre-trained text-to-video diffusion models, which requires no additional training. Instead of the vanilla text-to-video inference pipeline, \textsc{I4VGen} consists of two stages: {anchor image synthesis} and {anchor image-augmented text-to-video synthesis}. Correspondingly, a simple yet effective generation-selection strategy is employed to achieve visually-realistic and semantically-faithful anchor image, and an innovative noise-invariant video score distillation sampling (NI-VSDS) is developed to animate the image to a dynamic video by distilling motion knowledge from video diffusion models, followed by a video regeneration process to refine the video. Extensive experiments show that the proposed method produces videos with higher visual realism and textual fidelity. Furthermore, \textsc{I4VGen} also supports being seamlessly integrated into existing image-to-video diffusion models, thereby improving overall video quality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presented a two-stage text-to-Video Generation method I4VGEN, i.e., anchor image synthesis and anchor image-augmented text-to-video synthesis. Experiments are provided to assess its effectiveness in text2video generation and enhancing I2V methods.

### Strengths
+ Two-stage text-to-Video Generation method I4VGEN.
+ Can be integrated into existing image-to-video diffusion models.

### Weaknesses
 - The integration with existing image-to-video diffusion models is interesting, but the authors are suggested to combined with more I2V models, especially several recent ones.
- More ablation studies are required to show whether the anchor image selection and the NI-VSDS  are optimal.
- In the bottom of Fig. 6, albeit better image quality, it seems that the motion of the proposed method is smaller than that by SparseCtrl. More experiments are suggested to assess this aspect.

### Questions
- The integration with existing image-to-video diffusion models is interesting, but the authors are suggested to combined with more I2V models, especially several recent ones.
- More ablation studies are required to show whether the anchor image selection and the NI-VSDS  are optimal.
- In the bottom of Fig. 6, albeit better image quality, it seems that the motion of the proposed method is smaller than that by SparseCtrl. More experiments are suggested to assess this aspect.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a video diffusion inference pipeline that leverages image generation techniques to enhance a pre-trained text-to-video (T2V) diffusion model. Instead of directly generating videos from noise, the method first utilizes a text-to-image (T2I) model to generate a high-quality anchor image. This image is then used to produce an initial video via Score Distillation Sampling (SDS) through the T2V model. A regeneration process is adopted to refine it, resulting in the final video. Experiments have been conducted to evaluate the effectiveness of the proposed method both qualitatively and quantitatively.

### Strengths
1. The proposed method uses a pre-trained image generation model to improve frame quality in text-to-video generation, which is helpful for high-quality video generation.
2. The presented results demonstrate good quality.

### Weaknesses
1. The proposed method appears to integrate the T2I model with SDS distillation for video generation, and the contribution seems incremental. The core idea of using an initial image to guide video generation is not entirely novel, and the specific implementation using SDS for video refinement, while effective, does not represent a significant departure from existing techniques. The method essentially combines two existing techniques, T2I generation and SDS-based video distillation, without introducing a fundamentally new approach to video synthesis.
2. The motion observed in Fig. 1 appears to be smaller compared to the baselines. This suggests that the method might be prioritizing temporal consistency at the expense of dynamic motion, which could limit its applicability in scenarios where more pronounced motion is desired. The lack of more complex motion patterns in the generated videos could be a limiting factor.
3. There is a lack of analysis for different regeneration steps. The paper does not adequately explore how the number of regeneration steps affects the quality and characteristics of the generated videos. This lack of analysis makes it difficult to understand the sensitivity of the method to this hyperparameter and how to optimize it for different scenarios.

### Questions
1. What are the effects of using different image generation models? Can better video quality be achieved if a better image model (e.g., FLUX) is used to generate anchor images?
2. Will the SDS degrade image quality? It would be better to provide quantitative results in Table 2 to show its effects.
3. In Fig. 8, the prompt for the last video is mistaken.

### Soundness
2

### Presentation
3

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
This paper presents I4VGEN, a novel video diffusion inference pipeline that enhances pre-trained text-to-video models without additional training. It tackles the complexities of spatio-temporal modeling by utilizing advanced image techniques in two stages: first, synthesizing anchor images with a strategy to ensure visual realism and semantic accuracy; second, augmenting these images to generate videos through a noise-invariant video score distillation sampling (NI-VSDS) method. This process also includes a video regeneration step for refinement. Experiments show that I4VGEN significantly improves the visual quality and textual accuracy of generated videos and can be easily integrated into existing models, boosting overall video quality.

### Strengths
1. This paper introduces a training-free pipeline called I4VGen to improve the performance of text-to-video diffusion models throught image reference information.
2. A simple yet effective generation-selection strategy is proposed to obtain high-quality-images, while a noise-invariant video score distillation sampling is introduced for image animation.
3. Extensive experiments show that the proposed method comsiderably outperforms the performance of video diffusion baselines in terms of video quliaty.

### Weaknesses
1. The technical contributions of the paper are somewhat limited. The proposed noise-invariant video score distillation only modifies some hyper-parameters of the original SDS techinque. The modification to the score distillation sampling (SDS) appears to be primarily focused on adapting it for video by adjusting the noise schedule and number of optimization steps, rather than introducing a fundamentally new approach to score-based video generation. The core mechanism of using a pre-trained image diffusion model and applying score distillation remains largely unchanged, raising questions about the novelty of the method.
2. Compared to the baseline results, the video actions enhanced using the proposed method in this paper are minimal or essentially stationary. The metrics in Table 1 also show that the proposed method heavily harm the dynamic degree of generated videos. While the method may improve visual quality and consistency, the lack of significant motion in the generated videos is a major drawback, especially for a video generation task. The method seems to prioritize temporal consistency at the expense of dynamic motion, which limits its applicability to scenarios requiring more complex actions. This trade-off needs to be better addressed and justified.
3. AnimateDiff relies on high-quality LoRAs to improve the quality and consistency of generated videos. Please provide generated videos of AnimateDiff with high-quality LoRAs for a fair comparison. The comparison with AnimateDiff is not entirely fair without considering the impact of high-quality LoRAs, which are known to significantly enhance its performance. The lack of a comparison with AnimateDiff using such LoRAs makes it difficult to assess the true improvement offered by the proposed method.

### Questions
1. Concerns about inference time. The proposed method consists of two stages: anchor image synthesis and anchor image-augmented video synthesis. The reviewer wants to know whether the time in the table includes the time used in the first stage.
2. Low-quality face video in Fig.6. In 1st row of Fig6, SparseCtrl produces a video in extremely low quality, could the authors explain reasons?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a novel method to initialize the noise for T2V. To endow the noise with motion prior, the paper take the idea of SDS in T-to-3D in a video generation way, which is considered to be novel and inspiring to the community.

### Strengths
The paper focuses on the video generation quality from a noise initialization viewpoint, which is hot and also vital to AI-generated content. The authors try to use the off-the-shelf T2I and T2V models in a novel way, to be specific, anchor image synthesis using T2I and motion prior using T2V in a novel SDS way.

### Weaknesses
Generally speaking, video generation is notoriously for its lengthy inference cost. Noise initialization adds more cost, which is not practical. The authors are thus encouraged to add more discussion. Besides, the experiments can be more consolidated to enhance the authors' claim. Please refer to the question part for details.

I have several concerns as follow
1. More proof of the anchor image synthesis. Generally speaking, anchor image act as a low frequency component to mitigate the information leak. A question then rise that whether the anchor image synthesis is necessary. In ablation study, the authors use an example in Fig.5 to validate the assumption. Meanwhile, the authors also confirms that without the generation-selection strategy, the proposed method still performs well. Can the authors give more examples to support this claim?
2. In User study, the 20 volunteers with expertise in image and video processing participated. Does the expert bias exist? that is to say, the participants are more tolerant to the defects of the methods? Will the ordinary participants from a consumer's perspective be better?
3. It's a trend that video generation tends to produce more diverse content with long duration, for example, the large camera pose change. Will the proposed method still work?
4. The proposed method further increase the inference cost. More comprehensive measures are better presented from a practical perspective.

### Questions
I have several concerns as follow
1. More proof of the anchor image synthesis. Generally speaking, anchor image act as a low frequency component to mitigate the information leak. A question then rise that whether the anchor image synthesis is necessary. In ablation study, the authors use an example in Fig.5 to validate the assumption. Meanwhile, the authors also confirms that without the generation-selection strategy, the proposed method still performs well. Can the authors give more examples to support this claim?
2. In User study, the 20 volunteers with expertise in image and video processing participated. Does the expert bias exist? that is to say, the participants are more tolerant to the defects of the methods? Will the ordinary participants from a consumer's perspective be better?
3. It's a trend that video generation tends to produce more diverse content with long duration, for example, the large camera pose change. Will the proposed method still work?
4. The proposed method further increase the inference cost. More comprehensive measures are better presented from a practical perspective.

### Soundness
3

### Presentation
3

### Contribution
3
