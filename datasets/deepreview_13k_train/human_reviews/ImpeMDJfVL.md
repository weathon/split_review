# IV-mixed Sampler: Leveraging Image Diffusion Models for Enhanced Video Synthesis

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
The multi-step sampling mechanism, a key feature of visual diffusion models, has significant potential to replicate the success of OpenAI's Strawberry in enhancing performance by increasing the inference computational cost. Sufficient prior studies have demonstrated that correctly scaling up computation in the sampling process can successfully lead to improved generation quality, enhanced image editing, and compositional generalization. While there have been rapid advancements in developing inference-heavy algorithms for improved image generation, relatively little work has explored inference scaling laws in video diffusion models (VDMs). Furthermore, existing research shows only minimal performance gains that are perceptible to the naked eye. To address this, we design a novel training-free algorithm \textit{IV-Mixed Sampler} that leverages the strengths of image diffusion models (IDMs) to assist VDMs surpass their current capabilities. The core of \textit{IV-Mixed Sampler} is to use IDMs to significantly enhance the quality of each video frame and VDMs ensure the temporal coherence of the video during the sampling process. Our experiments have demonstrated that \textit{IV-Mixed Sampler} achieves state-of-the-art performance on 4 benchmarks including UCF-101-FVD, MSR-VTT-FVD, Chronomagic-Bench-150, and Chronomagic-Bench-1649. For example, the open-source Animatediff with \textit{IV-Mixed Sampler} reduces the UMT-FVD score from 275.2 to 228.6, closing to 223.1 from the closed-source Pika-2.0.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel sampling scheme for video diffusion models that leverages pre-train image diffusion models, as they generally have higher visual fidelity compared to current open source video models. The sampling method takes steps forward / backward (DDIM inversion / DDIM) in the diffusion model, alternating between the score functions of the image and video models. Results show high fidelity visual quality while retaining consistent motion in generated video.

### Strengths
* The paper is generally clear, and well written
* The proposed method is novel and interesting
* Results seem to show good improvement in generation quality of the videos, while retaining consistent motion
* Main experiments and ablations are thorough and show the benefits and tradeoffs of different instantiations of the proposed method

### Weaknesses
 * The sampling process requires both I/V models to be in the same underlying latent space, which may be restrictive. How would this method also be used in cases where there is temporal downsampling in the video latent space (as this this is a very common video generation architecture)?
* It is unclear how useful / relevant this method may be ~6+ months from now, as the main motivation of the paper is leveraging the lack of good open source video models, and public video datasets will get better (e.g. OpenVid10M [1]), and better video generation models will be released (e.g. Mochi-1 [2] as of recently).
* What is the variance of the quantitative metrics (e.g. FVD in Tables 1 and 2)? The values are pretty close and it’s unclear  if the results are statistically significant
* It would be nice to have more video samples to look at (e.g. on an anonymous website). There is only one set of videos in the supplementary, and it is hard to see motion for ones in the paper appendix.
* Does this method still work in scenarios using distilled models? E.g. 1 step or 2 step generation

### Questions
* What is the variance of the quantitative metrics (e.g. FVD in Tables 1 and 2)? The values are pretty close and it’s unclear  if the results are statistically significant
* It would be nice to have more video samples to look at (e.g. on an anonymous website). There is only one set of videos in the supplementary, and it is hard to see motion for ones in the paper appendix.
* Does this method still work in scenarios using distilled models? E.g. 1 step or 2 step generation

### Soundness
3

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
3

### Summary
The paper proposes IV-Mixed Sampler, which is to combine image diffusion models (IDMs) with video diffusion models (VDMs) to get the benefit of higher image quality of IDM and good temporal consistency of VDM. This is achieved by sampling from x_t to x_{t+∆t} and from x_{t+∆t} to x_t using IDM and VDM

### Strengths
+ The paper combines theoretical proof with practical implementations, and is relatively well-rounded
+ The proposed method seems to make intuitive sense

### Weaknesses
The writing of the paper can be improved. Here are several comments but not just limited to these points. Overall the presentation is a bit confusing.
- Why do the paper keep mentioning OpenAI's strawberry in Abstract and Intro, which is closed-sourced and no paper or technical detais was released? How is this important or even related to motivating the paper?
- Figure 2 is confusing and should not be put in the intro. This is more like ablation studies, and it is made rather confusing, especially authors also start to talk about "R-" in the intro out of nowhere (line 94), and the starts to discussion "I-" and "V-" in line 107 without any explanation
- The use of "go", "back", "begin", "end" etc in the equations are also confusing
- Plots like Fig 6 are also hard to read

The results of the model is decent but not very strong. For example, FreeInit is significantly better than ours for UMT-FVD on ModelScope-T2V

### Questions
See weakness

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces IV-Mixed Sampler, a novel algorithm designed to enhance video synthesis by leveraging the strengths of both Image Diffusion Models (IDMs) and Video Diffusion Models (VDMs). The core innovation is the use of IDMs to improve the quality of individual video frames while maintaining temporal coherence through VDMs during the sampling process. The authors claim state-of-the-art performance on four benchmarks, including UCF-101-FVD, MSR-VTT-FVD, Chronomagic-Bench-150, and Chronomagic-Bench-1649. The paper also provides a theoretical analysis of the IV-Mixed Sampler and its transformation into a standard inverse ODE process, as well as an exploration of the design space for hyperparameters.

### Strengths
Originality: The concept of combining IDMs and VDMs to enhance video synthesis is innovative. The paper addresses a significant gap in the field by improving the visual quality of synthesized videos while preserving temporal coherence.

Quality: The paper is well-structured, with a clear problem statement, methodology, experimental validation, and conclusion. The theoretical analysis provides a solid foundation for the proposed algorithm.

Clarity: The authors have done an excellent job of explaining complex concepts in a clear and concise manner. The figures and tables are well-designed and aid in understanding the content.

### Weaknesses
Evaluation Metrics: The paper employs benchmarks like UCF-FVD and MSR-VTT-FVD, which are not ideal for assessing text-to-video generation models. These metrics primarily focus on frame-level quality and temporal consistency but do not adequately capture the semantic alignment between the text prompt and the generated video content. More suitable benchmarks, such as those that evaluate text-video correspondence, are needed for a comprehensive evaluation. The current metrics fail to capture the nuances of text-to-video generation, potentially leading to inflated performance scores that do not reflect real-world applicability.

Demonstration Insufficiency: The provided demos do not clearly demonstrate the proposed method's superiority over baselines. The visual differences between the generated videos using the IV-Mixed Sampler and those generated by baseline methods are subtle, making it difficult to discern the claimed improvements. The demos lack the compelling examples needed to showcase the method's effectiveness, particularly in complex scenarios or when generating videos with intricate motion patterns. More visually striking examples are needed to convince the reader of the method's advantages.

Illustration Clarity: Figure 3's illustrations are not clear. The images presented do not effectively convey the differences in quality and temporal coherence, making it difficult for readers to grasp the paper's points regarding the performance of various samplers. The lack of clear visual distinctions between the outputs of different samplers hinders the reader's ability to understand the benefits of the proposed method. High-quality, clear visualizations are crucial for helping readers understand the nuances of video synthesis methods, and the paper would benefit from improved clarity in its visual aids, perhaps by using zoomed-in sections or side-by-side comparisons.

Limited Applicability: The method's compatibility with state-of-the-art video generation models, which often use distinct VAEs from image models, is limited. This restricts its potential applications and prospects in the field. The reliance on shared VAEs between image and video models is a significant constraint, as many advanced video generation models utilize specialized VAEs optimized for temporal data. This limitation hinders the method's ability to integrate with cutting-edge video synthesis pipelines, potentially limiting its impact and practical use.

### Questions
1. What are the detailed reasons that we can't use different VAEs for IDM and VDM when adapting the proposed method? Do you have experiment results about this?
2. How does the IV-Mixed Sampler perform as the length and complexity of the video sequences increase? Are there any scalability issues that the authors have identified?
3. Potential Limitations: Are there any specific scenarios or types of video content where the IV-Mixed Sampler might underperform? If so, how might these limitations be addressed?

### Soundness
2

### Presentation
3

### Contribution
2
