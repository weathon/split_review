# NeRAF: 3D Scene Infused Neural Radiance and Acoustic Fields

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
Sound plays a major role in human perception. Along with vision, it provides essential information for understanding our surroundings. Despite advances in neural implicit representations, learning acoustics that align with visual scenes remains a challenge. We propose NeRAF, a method that jointly learns acoustic and radiance fields. NeRAF synthesizes both novel views and spatialized room impulse responses (RIR) at new positions by conditioning the acoustic field on 3D scene geometric and appearance priors from the radiance field. The generated RIR can be applied to auralize any audio signal. Each modality can be rendered independently and at spatially distinct positions, offering greater versatility. We demonstrate that NeRAF generates high-quality audio on SoundSpaces and RAF datasets, achieving significant performance improvements over prior methods while being more data-efficient. Additionally, NeRAF enhances novel view synthesis of complex scenes trained with sparse data through cross-modal learning.
NeRAF is designed as a Nerfstudio module, providing convenient access to realistic audio-visual generation. 
Project page: \url{https://amandinebtto.io/NeRAF}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents NeRAF, a novel framework for synthesizing both vision and spatial audio in 3D scenes (spatial audio is the main focus of this paper). NeRAF’s key innovation is its ability to jointly learn visual neural radiance fields and spatial acoustic fields. The approach leverages cross-modal learning, meaning it incorporates visual features to enhance audio field prediction, and vice versa. It improves efficiency and realism in generating room impulse responses (RIRs). Unlike previous methods, NeRAF does not require aligned audio-visual data, making it more versatile and data-efficient. The method achieves state-of-the-art results in accuracy and quality of audio rendering, particularly in benchmarks like SoundSpaces and the Real Acoustic Fields (RAF) dataset.

### Strengths
1. **Enhanced Realism**. NeRAF uniquely integrates visual and acoustic information, using visual scene features to inform the acoustic model and vice versa. This cross-modal approach improves the fidelity of both visual and acoustic outputs, leading to more realistic audio-visual experiences without the need for additional aligned datasets.

2. **Data EVersatility**: Unlike other methods requiring dense, aligned audio-visual data, NeRAF operates effectively with sparse datasets and does not rely on co-located audio-visual sensors for training. This flexibility makes it suitable for various real-world applications, especially where dense data collection is impractical.

3. **State-of-the-Art Performance**: This paper demonstrates measurable improvements over existing methods in key metrics like Clarity (C50), Reverberation Time (T60), and Early Decay Time (EDT), setting a new standard for realistic audio-visual scene synthesis.

### Weaknesses
1. **Problem Setting Correctness**: In section 3.4, the authors write both the audio source and two microphones' (two ears) have directions. If so, it contradicts with the claim that: Sound propagation is omnidirectional (L205), because sound propagation from directional source isn't uniformally directional and thus may not be measured by RIR (the situation becomes more complex if the microphones are also directional). Moreover, the SoundSpaces 1.0 data provided RIR are emitted by point source without specific direction. The authors should 1. provide more detail discussion and theoretical proof showing how RIR they learned fits for directional source and microphones setting. 2. More detail regarding how directional information are used in SoundSpace 1.0 data or their own Habitat-sim simulated data (like how to set the direction and how to ensure the simulated RIR is conditioned on the set direction). The issue is not just about the source being directional, but also how the model handles the directional information of both source and microphone, especially when the training data uses omnidirectional sources. The model's ability to generalize to directional sources and microphones needs more rigorous justification, especially given that RIRs are inherently tied to the specific directivity patterns of the source and receiver. The current explanation lacks a clear mathematical formulation of how these directional parameters are incorporated into the acoustic field and how the model accounts for the variations in RIRs due to these directional properties. A more detailed explanation of how the model handles directional information, including the specific mathematical transformations and the impact on the predicted RIRs, is needed.

2. **Motivation Concern**: The task of this paper is to learn an acoustic field that can predict binaural RIR, but this paper proposes to learn auxiliary visual NeRF together with the acoustic field learning. One question naturally arises is that the authors should show why learning NeRF is essential for learning acoustic field, through either ablation study or theoretical analysis. If crossmodal visual learning is essential to improve acoustic field learning, is there any other more light weight visual learning mechanism other than NeRF can also improve the acoustic field learning. Given the title "3D scene infused neural radiance and acoustic fields" emphasizes the neural radiance field, more detailed discussion and investigation on the impact of visual radiance field on acoustic fields are required. The authors need to provide a more thorough analysis of why NeRF is the optimal choice for incorporating visual information, especially when considering the computational cost and complexity. The paper should explore alternative, potentially lighter-weight, visual representations and justify why NeRF provides superior performance compared to these alternatives. Furthermore, the paper should include a more in-depth discussion of the specific mechanisms through which the visual radiance field influences the acoustic field, providing a clear understanding of the cross-modal interaction and its impact on RIR prediction accuracy.

### Questions
1. See weakness section.

2. Experiment: since the framework is scene-specific where the train and test are based on the same room, how do the authors guarantee the train and test data are different? Another important discussion, if we fix a source position, what the predicted RIR accuracy difference on microphone position close to furniture and position on spacious area?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a method that jointly learns acoustic and radiance fields named as NeRAF, which can synthesize both novel views and spatialized room impulse responses at arbitrary target viewpoints. They claim by conditioning the acoustic field on 3D radiance field, NeRAF can benefit both visual and acoustic modalities. Experiments on both synthetic and real datasets show NeRAF generates high-quality audio and improves performance on both novel view synthesis and acoustic modeling tasks.

### Strengths
+ The paper aims for a very interesting topic: joint learning of visual and acoustic rendering for 3D scenes. The authors proposed an effective pipeline to solve this challenging task, and explore how the two modalities can combine together.

+ Thorough experiments are conducted on both synthetic and real datasets, comparing with reliable baselines and plenty of ablations to show the effectiveness of the proposed modules. Especially for the grid sampling visualization, from which we can see what physical meaning the grids have learnt through the joint training.

+ The paper is well organized and easy to follow with clear presentation.

### Weaknesses
 - Weak cross-modality learning. The proposed cross-modality learning way for acoustic learning is to use ResNet3D to extract 3D geometric and appearance priors, and then inject it for acoustic rendering. However, I doubt it due to two aspects: 
    - The model is scene-dependent, which means fits one scene per model. In this case, it's hard to guide the ResNet3D to truly focus on properties that affect acoustic learning and physically correspond to geometry/materials etc., especially without any explicit supervision on it. The model can easily just take the grid sampling extractor as a large latent feature generator to help the model memorize the data distribution in the room. The ResNet3D, lacking explicit supervision to extract acoustic-relevant features, might simply learn to map the grid's spatial information to the specific acoustic characteristics of the scene, effectively acting as a high-capacity memorization module rather than a feature extractor that generalizes across different scenes or acoustic properties. This is further compounded by the fact that the grid itself is not trained, limiting its ability to adapt to acoustic-specific information.
    - From visualization of grids in Figure A3, we can see the grids feature is more correlated to visual rendering task, which makes sense since visual rendering has strong supervision on the grids directly (density and color etc.). However, this can be tricky if we want to understand how the two modalities are actually integrated. The grids seem to fail to correlate with acoustics. According to the first aspect, strong evidence is needed here to support the two modalities are actually helping each other in a way that has claimed physical meanings (instead of just more latent features that benefits memorizing the scene)

- One way that may help to really use the visual modality is to do multi-conditioning training, i.e. one model fits multiple scenes. In this case, the visual can be helpful to adapt to different rooms, and we may be able to observe how audio and visual modality integrate. With real visual representation, the model can do more than just fitting single room. 

- If the visual and audio modality are helping each other in a pure latent way without any physical meaning, the soundness of claimed motivations and contribution will be largely weaken.

- The grids are in the fixed shape, which might be hard to fit large room, where the resolution can be super coarse and may degrade the performance. The fixed grid resolution poses a significant limitation, especially when dealing with larger or more complex acoustic environments. The current approach lacks the flexibility to adapt to varying room sizes and acoustic complexities, potentially leading to a loss of detail in larger spaces or an unnecessary computational burden in smaller ones. This fixed resolution could also limit the model's ability to capture fine-grained acoustic phenomena that require higher spatial sampling rates.

### Questions
Please see the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces NeRAF, a new method for simultaneously learning acoustic fields and visual radiance fields. The authors demonstrate that this joint training approach enhances the quality of both generated room impulse responses and RGB images. Additionally, the proposed method offers flexibility, allowing for independent generation of single modalities during inference. Experiments conducted on both simulated (SoundSpace) and real-world (RAF) datasets show that NeRAF outperforms state-of-the-art methods in both audio and visual generation tasks.

### Strengths
- In general, I like the proposed multi-modal joint training approach that is appealing for its concise design and its potential to enhance the generated quality of both visual and acoustic fields. The flexibility to leverage single modalities when needed is also an advantage.
- The paper is generally straightforward to follow. Extensive studies have been conducted on both synthetic and real datasets, along with healthy supplementary materials, code, and a demo video.

### Weaknesses
 - The task of rendering on both visual and acoustic signals has been previously explored (e.g., AV-Nerf), thus limiting the novelty of this work. From a technical perspective, the primary distinctions between NeRAF and AV-Nerf lie in 1) the use of 3D scene features for RIR generation and 2) the joint training pipeline. However, these technical contributions are not particularly significant to me.
- More analyses on cross-modal learning are needed. Table 2, Figure 6, appendix I and J show that joint training of cross-modal learning improves novel view synthesis but it is unclear whether there is any improvement in acoustic field synthesis. Specifically, the paper does not provide a clear ablation study on the impact of visual information on acoustic field synthesis. It's not clear if the 3D scene features are truly necessary or if a simpler representation would suffice.
- It is unclear why 3D ResNet is the best scene feature extractor. Some ablation studies would be helpful here. The paper lacks a comparison with other feature extractors, such as those based on transformers or other convolutional architectures. This makes it difficult to assess the optimality of the chosen architecture.
- The loudness maps in Figure 5 exhibit some non-smooth textures. Why does it happen? Can NeRAF effectively represent a continuous acoustic field? The discrete nature of the visualization raises concerns about the model's ability to capture the continuous nature of acoustic fields. The paper should discuss the limitations of this representation and how it might affect the accuracy of the results.
- NeRAF demonstrates better performance on RIR and image generation metrics, yet significant challenges persist. These include multi-scene representations, multiple or/and unknown sources, discrepancies between synthetic and real-world scenarios, and inverse problems. While this paper showcases improved training data efficiency, the impact is limited due to the density of synthetic datasets like SoundSpace. Even at 20%, the volume of training data remains substantial.
- From the perspective of human perception, it is unclear whether users can perceive actual difference between NeRAF and AV-NERF. The paper lacks a perceptual study to validate the improvements in audio quality. Objective metrics may not fully capture the nuances of human perception.
- NeRAF is obviously not a small model (Table A1). Especially it is still for single scene purpose.
- Some minor comments:
  - there was no context for Nerfstudio module until L90. Please clarify and add references in abstract and intro.
  - typo: wrong subscript $\sigma_{vi}$ in Eqn 4
  - In demo video, it would be better to provide trajectories in real scenes as well.

### Questions
- Why choosing magnitude spectrogram + griffin-lim instead of directly optimizing on waveform?
- Acoustic data in SoundSpace is actually in 2D (RIRs are the same for different heights). How does the 3D grid features help? Are 2D features good enough?
- In the demo video, are all videos shown on the right synthesized?

### Soundness
2

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
This paper introduces a novel method that simultaneously learns acoustic and radiance fields for a recently introduced problem, novel acoustic view synthesis. The core idea involves integrating 3D scene features when rendering room impulse responses for the acoustic field. Experiments conducted on both a synthetic dataset using SoundSpaces and the recently introduced real-world dataset, RAF, demonstrate the effectivenss of the proposed method over previous methods.

### Strengths
- The paper tackles an interesting and novel problem, and the concept of jointly learning acoustic and radiance fields is well-motivated, as visual and acoustic information can complement each other to learn spatial cues.

- Although AV-NeRF also utilizes vision to aid in learning an acoustic field, the proposed approach uniquely learns a radiance field and introduces a grid-sampler to extract visual features, which the acoustic field is conditioned upon.

- Table 1 demonstrates that the proposed method achieves notable improvements compared to AV-NeRF, INRAS, etc.

- It's good to see that the proposed method is evalauted on a real-world dataset, apart from simulated data in SoundSpaces. The authors also faithfully evaluate on the RWAVS dataset and reported the results, despite the different settings of the tasks.

### Weaknesses
 - In supplementary video, it only shows the comparisons of the proposed method againt audio-only baseline, which is a weak baseline? It would be compare the qualitative differences between the proposed method and the closest performing prior work (AV-NeRF or NACF), to demonstrate the quantitaive improvement is perceptually meaningful.

- The main new component is the grid sampler component that extracts scene features to condition the RIR rendering. How beneficial is the joint training? What if separately training the visual component and a fixed grid sampler? How useful is the scene feature from grid sampler? What if a single image is provided as input and a ResNet 2D is used? How helpful is conditioning the task on 3D scene information?

- Following on the above questions, some additional ablations could be informative, such as 

1. Comparing joint training vs. separate training of visual and acoustic components

2. Evaluating the impact of using a fixed vs. trainable grid sampler

3. Comparing 3D scene features from the grid sampler vs. 2D features from a single image

4. Quantifying the benefit of 3D scene conditioning vs. no scene conditioning

### Questions
Please see above.

### Soundness
3

### Presentation
2

### Contribution
3
