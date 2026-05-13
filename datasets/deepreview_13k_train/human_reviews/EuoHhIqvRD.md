# Is Synthetic Data Ready for Improving Visual Grounding?

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
This paper extensively investigates the effectiveness of synthetic training data to improve the capabilities of vision-and-language models for grounding textual descriptions to image regions. We explore various strategies to best generate image-text pairs and image-text-box triplets using a series of pretrained models under different settings and varying degrees of reliance on real data. Through comparative analyses with synthetic, real, and web-crawled data, we identify factors that contribute to performance differences, and propose SynGround, an effective pipeline for generating useful synthetic data for visual grounding. Our findings show that SynGround can improve the localization capabilities of off-the-shelf vision-and-language models and offers the potential for infinite data generation. Particularly, SynGround improves the pointing game accuracy of pretrained ALBEF and BLIP models by 4.81% and 17.11% absolute percentage points, respectively, across the RefCOCO+ and the Flickr30k benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies a critical problem about data synthesis for improving visual grounding capabilities of vision and language models. It explores various strategies for generating synthetic image-text pairs and image-text-box triplets to enhance model training, comparing synthetic data with real and web-crawled data. The proposed SynGround pipeline demonstrates that synthetic data can effectively improve the localization capabilities of existing models. Notably, SynGround boosts pointing game accuracy for models like ALBEF and BLIP on benchmarks like RefCOCO+ and Flickr30k, showing the potential of synthetic data for scalable improvements in visual grounding tasks.

### Strengths
1. Visual grounding is an essential problem with current vision and language models. It's important to study an effective approach to build synthetic data to further scale up models' visual grounding capabilities. This paper is one of the approaches that study how to generate such data, and with comparisons of various approaches to generate such data.
2. SynGround improves the pointing game accuracy of pretrained ALBEF and BLIP significantly.

### Weaknesses
1. Previous synthetic visual grounding dataset are missing, for example, GRIT data - "a Ground-and-Refer Instruction-Tuning dataset with 1.1M samples.
GRIT contains multiple levels of spatial knowledge, covering objects, relationships, region descriptions, and complex reasoning" - proposed in Ferret is not compared with. It's not clear how proposed SynGround is differing from previous synthetic visual grounding data, and how it surpasses previous data generation approaches.
2. The main tables lack important SOTA baselines, for example, Shrika and Ferret on RefCOCO+ and Flickr, which are a lot better than the model fine-tuned on SynGround on RefCOCO+, and similar on Flickr.
3. In Table 1, also the proposed approach get average 0.36 marginal improvement, and also no better than directly fine-tuning on existing VG data, which get average 0.96 improvement.

### Questions
1. The selection of base vision and language models. Why not applied to more recent SOTAs. Is SynGround data benefiting recent SOTAs in visual grounding also?
2. How does SynGround compare with exisiting visual grounding data collected from public source with bounding boxes synthesized as well?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the effectiveness of synthetic training data to improve the capabilities of vision-and-language models for grounding textual descriptions to image regions. They propose SynGround, an effective pipeline for generating useful synthetic data for visual grounding. Particularly, SynGround improves the pointing game accuracy of pretrained ALBEF and BLIP models by 4.81% and 17.11% absolute percentage points, respectively, across the RefCOCO+ and the Flickr30k benchmarks.

### Strengths
This paper provides a thorough experiments with different strategies to best generate image-text pairs and image-text-box triplets using a series of pretrained models under different settings and varying degrees of reliance on real data.

### Weaknesses
I really like the analysis in this paper. However, I'm confused about EFFECTIVENESS AND GENERALIZATION ON OTHER VLMS -- how general are the conclusions / findings in this paper (e.g. in Table 3 and 5), can they apply to more recent VLMs, since both the ALBEF and BLIP are smaller sized models from before 2022. Could you extend the method to more recent models such as LLaVA, Phi3.5, etc so that it is more likely to be a general conclusion?

### Questions
Happy to raise my score if weakness is addressed.

### Soundness
2

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
3

### Summary
This paper proposes a pipeline that uses LLMs, object detector, and image generation model to improve the grounding ability of VLMs. They demonstrate that applying such a pipeline allows them to improve the performance of a baseline ALBEF model on grounding tasks (RefCOCO, Flickr30K).

### Strengths
- The ablations in the paper are rather comprehensive and highlight the importance of each part of the pipeline.
- The paper demonstrates that training on the synthetically generated data improves over the baseline results on grounding tasks.

### Weaknesses
- The baselines are weak: ALBEF is an older model that is far from SOTA on the benchmarks reported. What about applying the method to a more recent model (such as OFA [1])? One concern is that ALBEF is a much smaller model (BERT based LM), while the pipeline used to generate synthetic data leverage larger and more capable models such as LLaVA. I would be more convinced if the authors can apply their approach to improve a similar sized model. This would also alleviate concerns that this method is simply distilling a stronger ALBEF model from LLaVA generated data.
- The gains over the baselines are not really substantial enough at the moment to warrant running this (rather convoluted) synthetic generation pipeline. Even with the synthetic data, the relative improvements are worse than using real data (Table 2) and only marginally better when combined with real data (Table 3). In Figure 5, the improvement with introducing synthetic data also seems marginal, and within the error bounds of using less data (which does not bode well for scaling).
- The paper is rather difficult to read, and I found it structured in quite a confusing way. Figure 1 could be replaced with an overview of the full SynGround pipeline, including captioning, bounding box generation, image generation components, as well as the training objectives detailed in Sec 3.1.


**References**

[1] Wang, Peng, et al. "Ofa: Unifying architectures, tasks, and modalities through a simple sequence-to-sequence learning framework." International conference on machine learning. PMLR, 2022.

### Questions
- There are several versions of Llava (1, 1.5, 1.6) as well as different model sizes (7B, 13B, 34B). Which one is being used in this paper?
- Another common semi-synthetic pipeline is to re-caption images (e.g., see Sec 7.1.1 of [2]). How would such a recaptioning approach fare on the CC experiments in Sec. 3.9?

**References**

[2] Dubey, Abhimanyu, et al. "The llama 3 herd of models." arXiv preprint arXiv:2407.21783 (2024).

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores using synthetic data to improve visual grounding in vision-and-language models. The authors present SynGround, a pipeline that generates synthetic image-text-box triplets by combining advances in text-to-image generation, language models, and object detection. They compare synthetic data with real and web-crawled data on RefCOCO+ and Flickr30k benchmarks. Results show SynGround enhances localization in ALBEF and BLIP models, outperforming web-crawled data and offering potential for infinite data generation.

### Strengths
1. Systematic exploration: The paper systematically explores different strategies for generating synthetic image-text and image-text-box data, providing valuable insights into the factors influencing performance. The paper compares the performance of models trained on synthetic data with models trained on real and web-crawled data.

2. Pipeline for synthetic data generation: The proposed SynGround pipeline offers a structured approach for creating synthetic data for visual grounding, combining several advanced techniques.

3. Outperforming web-crawled data: The finding that synthetic data outperforms web-crawled data is a notable strength, suggesting the potential for creating more tailored and effective training datasets.

### Weaknesses
1. Use of older models: The paper relies on ALBEF and BLIP, which are relatively older models in the rapidly evolving field of vision and language. The performance in Experiment 1 does not compare to any of the models in the papersincode leaderboard (e.g., https://paperswithcode.com/sota/referring-expression-comprehension-on-refcoco-1). Evaluating SynGround with more recent and state-of-the-art models would significantly strengthen the claims.

2. Limited performance gains:  While improvements are reported, the absolute gains from using synthetic data, especially when combined with real data, are relatively modest and may not be statistically significant.  Error bars or further statistical analysis should be provided to support the claims of improvement.

3. Clarity and organization: The presentation of experiments could be improved.  The motivation and reasoning behind each experiment could be more clearly articulated.  Consolidating related experiments (like the BLIP experiments) into fewer tables would enhance readability.  The paper would benefit from focusing on the key findings, such as the comparison with web-crawled data, earlier in the presentation.

4. Lack of analysis on scaling limitations: While the paper mentions the potential for infinite data generation, it does not discuss or analyze potential limitations or saturation points in scaling up the use of synthetic data.

### Questions
Have you considered evaluating SynGround with more recent and state-of-the-art visual grounding models?

Could you elaborate on the computational resources required for generating and utilizing the synthetic data, especially in the context of scaling up to larger datasets?

Have you observed any limitations or saturation points when increasing the scale of synthetic data used for training?

Could you discuss the potential impact of biases present in the source data (e.g., caption descriptions) on the generated synthetic data and downstream visual grounding performance?

### Soundness
2

### Presentation
2

### Contribution
2
