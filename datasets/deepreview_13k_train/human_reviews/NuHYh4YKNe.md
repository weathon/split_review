# Where Am I and What Will I See: An Auto-Regressive Model for Spatial Localization and View Prediction

- Decision: Accept
- Scores: 3, 8, 6, 8

## Abstract
\textit{Spatial intelligence} is the ability of a machine to perceive, reason, and act in three dimensions within space and time.
Recent advancements in large-scale auto-regressive models have demonstrated remarkable capabilities across various reasoning tasks. However, these models often struggle with fundamental aspects of spatial reasoning, particularly in answering questions like "Where am I?" and "What will I see?". 
While some attempts have been done, existing approaches typically treat them as separate tasks, failing to capture their interconnected nature. 
In this paper, we present \textbf{G}enerative \textbf{S}patial \textbf{T}ransformer (\NickName), a novel auto-regressive framework that jointly addresses spatial localization and view prediction. Our model simultaneously estimates the camera pose from a single image and predicts the view from a new camera pose, effectively bridging the gap between spatial awareness and visual prediction. The proposed innovative camera tokenization method enables the model to learn the joint distribution of 2D projections and their corresponding spatial perspectives in an auto-regressive manner. 
This unified training paradigm demonstrates that joint optimization of pose estimation and novel view synthesis leads to improved performance in both tasks, for the first time, highlighting the inherent relationship between spatial awareness and visual prediction. 
Project page: 
\href{https://sotamak1r.io/gst/}{https://sotamak1r.io/gst/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to do view prediction and pose estimation with a single autoregressive model. The paper claims that humans do this task effortlessly, and that their own model does it effortlessly too. The method is inspired by LLMs, by which the authors mean: it is autoregressive. The paper claims to be the first to tokenize camera data. The model itself is enormous: >1.4B parameters. It achieves good results.

### Strengths
This paper's figures are very well designed. Good color coordination across the paper.

### Weaknesses
The paper says that, given an image of a scene, humans can "effortlessly reconstruct the entire scene". I don't think this is true. Can the authors give some support for this claim?

The paper says that it wants the model to "effortlessly" estimate camera poses and estimate novel views. What does this mean? How can we distinguish effortless vs effortful models?

In talking about pose estimation vs. view prediction, the paper says "human cognition does not perceive these processes as isolated entities". I think it's quite clear that this is false. If we did not perceive these as separate tasks, how could we even talk about them so distinctly?

The paper says that their approach is "a model designed to align its understanding of 3D space with that of humans". Given that I question the paper's description of human cognition, I also question whether it's a good idea to design a model based on this shaky foundation.

The paper makes a major claim about novelty by saying "we introduce, for the first time, the concept of tokenizing the camera". It is not the first time. The authors can read, for example, "Input-level inductive biases for 3d reconstruction" (CVPR 2022). There are probably dozens of papers that convert camera information into tokens; checking the papers that cite the input-level biases paper should reveal many references. The paper goes on to say, "Specifically, we leverage Plucker coordinates to transform the camera into a camera map akin to an image". This has also been done before: check "Cameras as Rays: Pose Estimation via Ray Diffusion" (ICLR 2024). I can see that this is in fact cited in a later part of the paper, so perhaps there was some mixup in the writing, and the author of this section is not aware of the related work and what the actual contributions are. Nonetheless, this is a serious issue.

Overall, it is unfortunate for a work like this, which appears to be otherwise quite well polished, to make wild and unsupported statements about human cognition, and to claim novelty on techniques that have been published before (and even gained re-use across follow-up work). It is possible that this paper actually has novel parts and useful contributions, but the amount of false (or unsupported) and misleading material is overwhelming.

the Al puzzle -> the AI puzzle

### Questions
Please interpret some of my stated "weaknesses" as questions.

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the Generative Spatial Transformer (GST), an innovative autoregressive framework capable of simultaneously handling spatial localization and view prediction tasks. By introducing a novel camera tokenization method, GST learns the joint distribution of 2D projections and spatial perspectives during training, thereby improving the performance of camera pose estimation and novel view synthesis. Experiments demonstrate that GST achieves state-of-the-art performance in these tasks, highlighting the intrinsic connection between spatial awareness and visual prediction.

### Strengths
First, the paper's approach and the scientific questions it raises are novel and intriguing.
Second, the method proposed in the paper can simultaneously estimate camera pose from a single image and predict the view from a new camera pose, effectively bridging the gap between spatial awareness and visual prediction. Interesting validations are shown in Figure 7.
Finally, the writing of the paper is clear and accessible, with excellent explanations from the motivation to the introduction of the method, and the provided conceptual diagrams are easy to understand.

### Weaknesses
I did not find any obvious shortcomings. I only have one suggestion: when citing the methods of other articles, it would be better for the author to briefly introduce them.

### Questions
My main concerns are as follows:
Line 268. I am curious about the effect of the concatenation order of the three tokens on the experimental results in this problem.
Line 342, GST only uses part of the data set for training, but I want to know what the results will be if the same experimental settings are maintained as Zero-1-to-3.
In line 375, the author does not elaborate on the definition of Unseen Categories. Of course, I can understand that due to the experimental settings, there may be some disadvantages compared to these methods.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to jointly model the distribution of camera poses and novel views via a shared Generative Spatial Transformer (GST).

### Strengths
1. The idea of jointly modeling the distribution of camera poses and novel views via a Generative Spatial Transformer is cool and novel.
2. The writing is clear, and the figures are nice.
3. This paper presents comprehensive ablation studies to justify model designs.

### Weaknesses
1. Insufficient evaluation:
    1. Novel view synthesis: The model has been trained on real-world images (CO3D, RealEstate10k, MVImgNet), but the evaluation is only on Objaverse (where the object shows simple and unrealistic textures). Can authors (quantitatively and qualitatively) compare to other baselines in terms of novel view synthesis on CO3D as well? One possible baseline is Zero123, fine-tuned on real-world images by ZeroNVS [1]. 
    2. Multi-image condition: Can the proposed approach synthesize novel views/estimate camera poses conditioned on multiple images? It'd be interesting to see its flexibility by showing these results (e.g., comparing with baselines, say Ray Diffusion with 3-8 images).
    3. How does the proposed approach compare with the state-of-the-art method, DUSt3R [2]?
2. Unfair comparison: In Tab.3, the proposed method achieves higher accuracy on unseen categories than the baseline. However, this could be explained by the more training datasets used by the proposed method, while the baselines, e.g., Ray Diffusion, are trained only on CO3D. Can the authors train the model on the same data used by Ray Diffusion and compare with it?
3. Minor issue: I think the two arrows in Tab.4 are in the wrong direction (Rot@15, Rot@30).

### Questions
1. How does the proposed method deal with scale differences of camera poses from different datasets? Is any normalization used for ground truth camera poses across datasets?
2. Can authors provide more details about training resources? For example, how many GPUs are used, and how long has the model been trained?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduced a auto-regressive framework to simutaneously estimate camera pose of a given image, and synthesize novel views at new camera poses. The authors achieve this via modeling the joint distribution of camera frustums and their image projections in a unified training paradim.

### Strengths
1. How the authors leverage VQVAE to tokenize camera views consistent with image tokenization is considered novel.
2. The effective adoptation of language models for autoregressive image/camera pose predictictions is interesting.
3. The choice to model the joint distribution of camera views and frustums within the same model seems clean and effective in combining the task of novel view synthesis and camera estimation.
4. Descent visual illustrations and writing.

### Weaknesses
1. The NVS results seems to be mostly on par or slightly better than existing state of the art models only based on the training of "a subset of objaverse," and I am curious of the particular choice of the data subset used in training. What's stopping the authors from training on the same dataset as Zero-1-to-3 to make a more fair comparison?
2. The camera rotation accuracy metric of 15 degree is rather a relatively coarse metric, and the authors did not present the camera translation accuracies in any kind.

### Questions
1. As the results are presented as training only on a subset of Objaverse, do the authors have any expectations on how the method will scale?
2. For other camera rotation accuracies (5 degree or 10 degree), will GST's performance still be competitive to state of the art methods?
3. What's the rough GPU memory and latency performance of the proposed pipeline relative to existing work (would this be a potential downsides of autoregressive modeling)? 
4. Would it be possible to leverage the model's understanding of the joint distribution of camera angles and views for 3D reconstruction/NVS from a set of potentially uncaliberated images?

### Soundness
3

### Presentation
3

### Contribution
3
