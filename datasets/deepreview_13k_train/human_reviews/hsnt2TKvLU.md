# Object-Aware Audio-Visual Sound Generation

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Generating accurate sounds for complex audio-visual scenes is challenging, especially when multiple objects and sound sources are present. In this paper, we introduce an object-aware sound generation model that aligns generated sounds with visual objects in a scene. By grounding sound generation in object-centric representations, our model learns to associate specific visual objects with their corresponding sounds. We fine-tune a conditional latent diffusion model with dot-product attention to improve sound-object alignment. At test time, users can compositionally generate sounds by selecting objects via segmentation masks. We theoretically validate our test-time object-grounding ability, ensuring that even subtle sounds can be represented. Quantitative and qualitative evaluations show that our model outperforms baselines, achieving better alignment between objects and their associated sounds.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors propose an object-aware sound generation model that generates sounds aligned with visual objects in the scene. This approach overcomes the limitation of forgotten or underrepresented sound events in complex scenes. Results show that the framework can generate more complete and contextually relevant sounds and surpasses baselines.

### Strengths
1. The framework seems simple yet effective. By combining existing encoder and decoder blocks and fine-tuning the diffusion weights, the framework successfully grounds sound generation in object-centric representations. Results demonstrate the effectiveness of the framework. 
2. The paper is well-written and easy to understand.

### Weaknesses
1. No ground-truth spectrums are provided in Figure 3, making it hard to directly compare the performance of different approaches.
2. The authors only provide the overall performance on the whole test set without breakup. The distribution of the test set is not clearly illustrated. The authors are encouraged to provide a more detailed analysis of their model's performance. Please refer to the 'Questions' part below.

### Questions
1. It is hard to directly judge the quality of generated sounds from current qualitative results in Figure 3, as no ground-truth is provided. Could you add ground-truth spectrums so that the readers can better compare the performance of different methods?
2. Could you clarify the distribution of the test set? Specifically, is it composed of single-source or multi-source audio samples, and what is the category distribution of the test set? Additionally, I recommend considering a division of the test set into subsets of varying difficulty or category distribution (e.g., human, animal, etc.). This could offer a more detailed evaluation of the framework's performance across different scenes.
3. The current image-text fusion method is relatively simple as only a cross-attention mechanism is adopted. Could you try different fusion mechanisms?

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
This paper tackles a task of object-aware sound generation and proposes conditional diffusion model with object-centric representations by exploiting image-text attentions during training, and segmentation masks during test time. Authors validate the proposed model with both quantitative and qualitative evaluations and it shows the model outperforms baselines. Additionally, ablation study was conducted to demonstrate the effectiveness of the proposed components. Finally, the paper also presents theoretical analysis why the proposed object-grounding mechanism is equivalent to segmentation masks and thus segmentation masks may be used during inference.

### Strengths
- The idea of using object-centric representation for object-aware sound generation is interesting and makes sense.
- The experimental results are promising. Both quantitative and qualitative evaluation demonstrate the effectiveness of the proposed approach.
- Presented theoretical and ablation analyses are nice.
- In general, writing is easy to follow.

### Weaknesses
- Object-aware sound generation is not new. That is, there have been prior work using similar ideas for sound generation, e.g., [1] and [2]. I think the novelty is from explicitly modeling object-centric representation by using image-text attentions. But its novelty is somewhat incremental as this mechanism is not new, either. 
- The baselines are not for object-aware sound generation, so it seems natural that the proposed model outperforms the baselines. I think it would be beneficial to compare the proposed model with other object-aware models for fairer comparison.
- Even though the authors present a theoretical analysis why the proposed object-grounding mechanism (i.e., image-text attention) is equivalent to segmentation masks and thus segmentation masks may be used during inference, it is still not clear why they are differently used in training and test time. e.g., can we use segmentation masks during training? 




References 

[1] Zhao et al., The sound of pixels, ECCV 2018

[2] Li et al., Cyclic Learning for Binaural Audio Generation and Localization, CVPR 2024

### Questions
- Using text-image attention at test time in ablation study, does it mean that it has access to text during inference? Or, was the text description generated with image captioning model such as BLIP?
- How about using segmentation masks during training instead of text-image attention since presumably they are equivalent?
- How about using both image and text for object-grounding mechanism, e.g., image-text-audio attention?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims at generating sounds that accurately align with visual objects in complex scenes. The authors address the challenge of creating context-specific sounds for scenes with multiple sound sources, such as urban environments with varied ambient sounds (e.g., crowd noise, car engines, and wind). The model uses object-centric representations to link sounds to specific objects by enhancing a conditional latent diffusion model with dot-product attention. This approach allows the model to capture subtle audio details and facilitates user control over sound generation through object selection via segmentation masks.

### Strengths
1. The paper is well-structured and clearly presented, making it accessible and easy to follow. 

2. Additionally, the authors provide a supplementary video that intuitively showcases the results, enhancing the clarity of the model's capabilities.

### Weaknesses
The paper faces several conceptual and methodological concerns. 

1. The task itself may lack clear purpose: since a text prompt is required, using a large language model (LLM) to parse the prompt into object names could streamline the process without necessitating visual inputs. Given that this method builds on the text-to-audio AudioLDM model, conditioning audio generation directly on text prompts would likely be more effective and efficient than relying on images.

2. The theoretical analysis presented lacks practical evaluation. While the authors posit that the soft attention mechanism could be theoretically replaced with segmentation masks, no experiments are conducted to assess the impact of this substitution. Comparative experiments examining the performance of soft attention versus segmentation masks would strengthen this theoretical claim.

3. The proposed method also offers limited novelty, as it primarily integrates existing models with minor modifications. 

4. The results raise questions about consistency. In Table 1, AudioLDM 1 is the weakest baseline, while Table 2’s "frozen diffusion" configuration—seemingly equivalent to AudioLDM 1—shows a sharp discrepancy in performance. Given that the method builds on AudioLDM, it is unclear if the proposed attention mechanism alone is responsible for transforming the baseline into a top-performing model, which may challenge the credibility of these results.

### Questions
Please refer to the weaknesses section.

### Soundness
2

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
This paper proposes a framework to generate sound from visual input by selectively attending to masked regions in images. Using a pre-trained conditional latent diffusion model as a backbone, the proposed framework learns to integrate a soft attention mask with visual features, which is replaced with a hard segmentation mask from SAM during inference. The effectiveness of the proposed framework is evaluated on a newly curated dataset based on Sound-VECaps, where it outperforms a wide range of prior art, both qualitatively and quantitatively.

### Strengths
- The proposed framework proposes a plausible way to integrate a strong off-the-shelf audio generation model, AudioLDM, for image-to-audio generation.
- Evaluation metrics cover diverse aspects of ensuring the quality of audio generation, and the qualitative evaluation is conducted rigorously.
- Generated audio samples on the project page are visually relevant and sound natural.

### Weaknesses
- I'm not convinced that the proposed framework can legitimately claim "compositional generation" of audio from visual input, a term frequently used in the draft. The framework generates output audio directly from hard/soft masks, rather than considering combinations or selections of different components in the visual input. For instance, the generated sound for a specific object may vary significantly between using a full scene versus partial objects as input, and the model appears to lack control over this variation.
- The theoretical analysis in Section 3.3 appears to have been retrofitted to match the heuristics addressing the gap between training and inference, lacking sufficient rigor. The validity of the value metric in Line 258 is not adequately justified, and the claim that bounding the expectation of value differences leads to test-time generalization remains unclear. Furthermore, the Lipschitz assumption represents an especially strict condition for deep/foundational neural networks, and its adoption without thorough justification is questionable. Most critically, the statement in Line 283 that "Since errors are _usually_ small, and regularity parameters are _commonly modest_, our method can be _guaranteed_ to achieve high accuracy" is overly vague. Given such an imprecise conclusion, the inclusion of Theorem 3.1 seems unnecessary.
- The reproducibility and preciseness of the dataset curation process seems to be limited. The conversion from video to static images results in nontrivial information loss during both training and inference, as not all objects produce sound continuously throughout the video in real life. Furthermore, the random selection of single frames from videos could potentially compromise both experimental accuracy and reproducibility.

### Questions
Some minor comments:
- Be consistent with the citation format in References.
- If speech and music are discarded with audio tagging model, how does the label distribution look like?

### Soundness
2

### Presentation
3

### Contribution
2
