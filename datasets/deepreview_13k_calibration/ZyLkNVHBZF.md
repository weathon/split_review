# How Far Is Video Generation from World Model: A Physical Law Perspective

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 5, 6, 3

## Abstract
OpenAI's Sora highlights the potential of video generation for developing world models that adhere to fundamental physical laws. 
However, the ability of video generation models to discover such laws purely from visual data without human priors can be questioned.
A world model learning the true law should give predictions robust to nuances and correctly extrapolate on unseen scenarios.
In this work, we evaluate across three key scenarios: in-distribution, out-of-distribution, and combinatorial generalization.
We developed a 2D simulation testbed for object movement and collisions to generate videos deterministically governed by one or more classical mechanics laws.
This provides an unlimited supply of data for large-scale experimentation and enables quantitative evaluation of whether the generated videos adhere to physical laws.
We trained diffusion-based video generation models to predict object movements based on initial frames.
Our scaling experiments show perfect generalization within the distribution, measurable scaling behavior for combinatorial generalization, but failure in out-of-distribution scenarios.
Further experiments reveal two key insights about the generalization mechanisms of these models: (1) the models fail to abstract general physical rules and instead exhibit ``case-based'' generalization behavior, \textit{i.e.}, mimicking the closest training example; (2) when generalizing to new cases, models are observed to prioritize different factors when referencing training data: color $>$ size $>$ velocity $>$ shape.
Our study suggests that scaling alone is insufficient for video generation models to uncover fundamental physical laws, despite its role in Sora's broader success.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper conducts a systematic investigation of video diffusion models from a physical law perspective. It explores three generalization scenarios, such as combinatorial generalization, and trains the model under various settings, such as different movement types and training data scales. The experimental results reveal several intriguing findings.

### Strengths
1. This paper provides a systematic investigation of video diffusion models from a physical law perspective, supported by extensive experiments and solid analysis.

2. This paper shows several intriguing findings, improving the understanding of physical laws in video diffusion models.

3. The paper is well-organized and clearly written.

### Weaknesses
1. This paper investigates physical laws by training video diffusion models on specifically designed data.  How would the findings apply to open-source pretrained models, such as Stable Video Diffusion [1]?

2. Based on the analysis in this paper, are there guidelines for improving the ability of video diffusion models to learn physical laws?

### Questions
Please refer to the above weaknesses.

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
4

### Summary
The authors train their own video diffusion models on synthetic video models and run thorough analysis on how the physics based video generation.

### Strengths
* The paper train many video diffusion models from scratch on small physical datasets across model parameter sizes. 
* They have thorough evaluation of extrapolation behavior
* The paper attempts to tackle a very complex problem, by simplifying it to a synthetic data setting.
* The analysis between in distribution and OOD seems useful, and this distinction could inform the creation of future video models, particularly the experiments in 5.4

### Weaknesses
 * Instead of training a "small" video model from scratch, why not try finetuning SOTA models on these video datasets? One issue with this analysis it supposes that there is not a minimum threshold for the number of parameters needed for a useful diffusion video model or for generalization to hold. I would not be surprised if these models generalized when simply having more parameters and train on more data, even out of domain data. Finetuning a model like SVD should be doable on a similar level of compute.

* The rendering of the synthetic examples are overly simplistic and do not have imaging artifacts that video models could exploit in real world use cases to generalize, like motion blur.

* Many of these reasoning weakness of generative models have been brought before in other domains. Such as Arc-AGE Challenge - "On the Measure of Intelligence" by François Chollet.

*  "For example, in Figure 10, it is difficult to determine if a ball can pass through a gap based on vision alone when the size difference
is at the pixel level, leading to visually plausible but incorrect results. Similarly, visual ambiguity in a ball’s horizontal position relative to a block can result in different outcomes. These findings suggest that relying solely on visual representations, may be inadequate for accurate physics modeling." Pixel level differences will be obliterated by the VAE encoder. It is a compressive architecture, information will be lost to train the model more cheaply. Pixel level criteria is not a motivating example as a result. If you want pixel level accuracy, you need pixel level diffusion models, not one trained on latent. I would disregard these experiments or rewrite this entire section 5.5 as this is a fundamental issue with the model architecture, and reveals no new information. Can you at least verify that the VAE is able to reconstruct different images with pixel level differences? I think you will find that it will not, as Stable Diffusion's VAE architecture cannot. The number of channels is way too limiting which is why it's been massively increased in more recent models like BlackForrest's FLUX.

* " This ranking could explain why current video generation models often struggle with maintaining object consistency" Please support with evidence? Or at least specify with which video models?


* Our in-depth analysis suggests that video model generalization relies more on referencing similar training examples rather than learning universal rules.
All generative models exhibit this behavior, and it is well known. Similar observations can be made on small language models, but they usually generalize way better when scaled up in terms of compute. What is the new observation here with respect to physics?


Rather a better way to frame this paper might be what role do VAE reconstruction issues prevent us from using existing video world models for physics in critical settings? How do the video VAE's and the diffusion model prioritize shape color and velocity? The main issue here is that some of the experiments are clearly demonstrating architectural failures of the VAEs and the authors are attempting to generalize it to all video models, which is an massive overclaim. 

This paper has useful experimental and scientific data, but it needs to be rewritten to support the claims in the paper. Furthermore, it could massively benefit by examining which of these issues are coming from the VAE and which are coming from the latent video diffusion.

Claims are made that scaling cannot solve these physics problem. The evidence this paper shows that scaling parameters and perhaps date in the video diffusion model is ineffective if the VAE removes important information for the video model.

### Questions
* In what real world cases would the data be significantly outside of the distribution of the training data. Should the solution not be scaling the number of parameters or the number of data, but rather the diversity of the data then?

* What aspects of the behavior you observation are purely artifacts of the latent encoder / decoder?

* Why did you not finetune any existing video models on these tasks? Surely this task is entirely OOD from the training task since it's a synthetic environment. Furthermore, if as a researcher your goal is to train the best video world model possible, why would you not start with a pretrained model. If you are confident that these problems cannot be solved purely by scaling, than pretrained video models on real world images should not generalize to this simple benchmark and should observe similar biases as in this paper. If you are making a claim that this behavior can be observed on all video models, than you should be able to evaluate this lack of generalizations on existing pre-trained models right?


* We design datasets which delibrately leave out some latent values, i.e. velocity. After training, we test model’s prediction on both seen and unseen scenarios. We mainly focus on uniform motion and collision processes
From an optimization point of view, what sparsity level is needed for the model to be able to linearly extrapolate then? After all, a diffusion model must also know what NOT to generate. There is surely some level sparsity for which the video model will generalize? What level of sparsity is it?

* "color > size > velocity > shape" how much of this is simply affected by this explicit instantiation of the video VAE? What about other ones like Stable Video Diffusions? Or more recently released video model like COGVideo's?

### Soundness
1

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
The authors study the capability of state-of-the-art video generation models (akin to SORA, combinations of VAE+DiTs) of acquiring world models from data. To this end, they create a video dataset using a basic 2D physics simulation, featuring different interacting objects. The authors study the model capability of forecasting from a given point in time, and study failure modes of video generation models. Crucially, they find that simply scaling the models is not sufficient to meaningfully improve the capability of acquiring world models, highlighting an important limitation of current video-generation techniques.

### Strengths
The addressed question is important, and the authors carefully design datasets and experimental settings to investigate ID/OOD behavior during model and dataset scaling, along with compositional generalisation. The overall contribution of the paper is good. The approach includes generation of a new benchmark dataset.

### Weaknesses
The general flow of the paper is lengthy and at times, a bit hard to parse. The overall writing needs to be improved.

I find the overall structure of the paper confusing: Sec. 2 starts with outlining some of the methods/experimental setting, then, Sec. 3 highlights ID and OOD, first introducing the setup (3.1) then the result (3.2); Sec. 4. proceeds with combinatorial generalisation, starting with the setup (4.1.) and results (4.2); Sec. 5 then mixes model setup, directly referencing results in 5.1 and each of the following sections. Given that a lot of the methodology is shared, I wonder why the authors did not write one "methods/experiments" section upfront, and then go over the different results. In particular, it would help if the headings would reflect the main results, vs. starting "main result" multiple times.

Additional points:

- I find Figure 8 hard to parse, the caption does not help much. Is this a hypothesis of what happens, or a description of the experiment?
- The paper focuses *only* on video generation models. The achieved results are not contextualised by other modeling approaches. (which might be fine within the scope of the paper, if the authors manage to contextualize the results in every figure otherwise)
- ll 74-99 already present a lot of results, without sufficient context or references. The conclusions are hard to parse. The paragraph in ll. 112-125 also seems out of place.
- The model definition in Sec 2.2 is quite slim. An overview figure would help, and more details need to be given/referenced from the appendix.
- Sec 4.2. starts with a broken sentence.

Besides, I do not see major weaknesses, I would need to clarify a few questions with the authors first to engage in further discussion, see below.

### Questions
- Will the dataset be fully released under a permissive license alongside the study? If you do, it would enhance adaptation a lot if all relevant latent variables from the physics simulator would be included in that release.
- What is the role of color in the different datasets? E.g. in Fig 4, you mention that color contains information about the object type (fixed vs. dynamic). What information is conveyed by color, and is this on purpose? Are there potential confounders introduced via the color?
- Sec 7: "Video generation is believed as a promising way towards scalable world models": Is this actually the case? What is scalable about video generation models? Isnt it rather the case that for video generation models, compute scales with the complexity of the data to model, and other approaches (like latent variable models, JEPA architectures, contrastive learning, ...) are the scalable models that do not need to model the input signal in full complexity?
- How was the "Abnormal rate" derived, what was the study setup? ll. 297-298 do not provide sufficient information on that.
- Larger models sometimes get larger errors (Fig 3). Could this hint at the fact that the models are undertrained? In general, could you motivate how the data sizes are picked for the different model categories, and how this relates to the amount of data these model sizes are typically trained on.
- The intro states the ordering "color > size > velocity > shape" which also takes a central role in the conclusion paragraph. Where was the "pairwise analysis" mentioned in l. 97/98 performed?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper examines video generation models' ability to learn physical laws from visual data, testing their generalization across in-distribution (ID), out-of-distribution (OOD), and combinatorial scenarios. Claimed key contributions include:
1. Evaluation Framework: A structured assessment for how well models follow physical laws across different data distributions.
2. Scaling Insights: While data scaling improves ID generalization, it has minimal effect on OOD.
3. Prioritization in Generalization: Models prioritize attributes (color > size > velocity > shape) when referencing training data.
These findings could provide some insights for building robust world models in video generation.

### Strengths
The paper presents limited originality, as it largely builds on existing approaches to video generation and world modeling, applying these to well-studied physical scenarios without introducing novel methodologies or frameworks. (see weaknesses)

However, it demonstrates good quality in experimental design and data scaling, using systematic evaluations across in-distribution, out-of-distribution, and combinatorial scenarios, which provides valuable insights into model limitations. 

The **clarity of the paper is strong**, with well-defined sections on methodology, findings, and practical insights, making the results and their implications easily accessible to the reader. In terms of **significance**, the contributions are moderate, as the findings—while informative—are more incremental than groundbreaking. They highlight known limitations in model generalization rather than offering transformative advances for video generation or physical law discovery. 

Overall, the paper is a solid study with strengths in clarity and quality but limited novelty and moderate significance in its contributions to the field.

### Weaknesses
The paper's main weaknesses revolve around its misalignment between its stated focus on physical law discovery and the actual content of its experiments:

1. Although the paper claims to investigate the learning of physical laws, the experiments primarily assess model sensitivity to superficial attributes like color, size, and shape. This focus on object properties, rather than fundamental dynamics such as force or acceleration, detracts from the paper’s relevance to physical law discovery, as these experiments fail to represent deeper physical principles. The experiments, for instance, do not explore how models handle scenarios with varying gravitational forces or complex interactions between multiple objects, which are more relevant to understanding the learning of physical laws.

2.  The findings are primarily reiterations of known phenomena—such as the ease of in-distribution (ID) generalization versus the challenges of out-of-distribution (OOD) generalization. These are well-established issues in machine learning, and the paper does not contribute fresh insights specific to physical law generalization. The paper does not offer any novel analysis or theoretical framework that would advance our understanding of how neural networks learn physical laws beyond the existing understanding of ID/OOD generalization.

3. Most observations (e.g., the prioritization of color over shape) apply to general video model generalization rather than to any specific domain of physics. Consequently, the paper’s insights into generalization mechanisms are not uniquely tied to physical laws, making the connection to physical modeling somewhat tenuous. The observed prioritization of attributes like color over shape is a common phenomenon in image and video models, and the paper does not demonstrate how this relates specifically to learning physical laws.

4.  The paper appears to position itself as a study on physical law discovery, yet the experimental design and findings align more closely with a standard exploration of OOD and ID generalization in video generation. This disconnect may suggest an attempt to frame familiar findings in a new light, without sufficiently novel contributions to the study of physical law generalization.

Overall, the paper does not fully deliver on its premise of exploring physical laws, focusing instead on known generalization issues in video models without advancing the state of research in physics-informed AI.

### Questions
Have you compared your findings with a long list of previous works on examining OOD and IND generalization of neural network models in general? For example, this paper:
Visual Representation Learning Does Not Generalize Strongly Within the Same Domain

### Soundness
3

### Presentation
3

### Contribution
2
