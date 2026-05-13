# Attribute Based Interpretable Evaluation Metrics for Generative Models

- Decision: Reject
- Scores: 5, 8, 3

## Abstract
When the training dataset comprises a 1:1 proportion of dogs to cats, a generative model that produces 1:1 dogs and cats better resembles the training species distribution than another model with 3:1 dogs and cats. Can we capture this phenomenon using existing metrics? Unfortunately, we cannot, because these metrics do not provide any interpretability beyond ``diversity". In this context, we propose a new evaluation protocol that measures the divergence of a set of generated images from the training set regarding the \textit{distribution of attribute strengths} as follows. Single-attribute Divergence (SaD) reveals the attributes that are generated excessively or insufficiently by measuring the divergence of PDFs of individual attributes. Paired-attribute Divergence (PaD) reveals such pairs of attributes by measuring the divergence of \textit{joint} PDFs of pairs of attributes. For measuring the attribute strengths of an image, we propose Heterogeneous CLIPScore (HCS) which measures the cosine similarity between image and text vectors with \textit{heterogeneous initial points}. With SaD and PaD, we reveal the following about existing generative models.
ProjectedGAN generates implausible attribute relationships such as \texttt{baby} with \texttt{beard} even though it has competitive scores of existing metrics.
Diffusion models struggle to capture diverse colors in the datasets. The larger sampling timesteps of the latent diffusion model generate the more minor objects including \texttt{earrings} and \texttt{necklace}. Stable Diffusion v1.5 better captures the attributes than v2.1. Our metrics lay a foundation for explainable evaluations of generative models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes two evaluation metrics, single-attribute divergence and paired-attribute divergence, to measure the divergence of a set of generated images with respect to the distribution of attribute strengths. The proposed metrics are defined based on heterogeneous CLIPScore, an enhanced measure from CLIPScore. THe metrics are verified on a few generative models, including PrpjectedGAN and diffusion models, to show the effectiveness and explainability.

### Strengths
- This paper is clearly written and easy to follow.
- Evaluation of generative models is a crucial problem which will attract wide research interest.
- Defining evaluation metrics based on attributes to measure the divergence between image sets is a novel and reasonable idea.

### Weaknesses
- The overall contribution is incremental, though the research motivation is fairly clear and reasonable. 
  - The heterogeneous CLIPScore is a simple extension from CLIPScore by using the centralized encodings. 
  - The proposed SaD and PaD are straightforward to measure the divergences of single and paired attributes.

- As for the interpretability, I have some concerns:
  -  For me, the interpretability comes from the attributes, which are obtained from annotation or large models. So the interpretability of the evaluation metrics are limited by the set of attributes.
  - Interpretation based on attributes is only one possible solution, which may be not complete or accurate to characterize the capability of generative models.

- The attributes selection methods are somewhat simple. Little insight can be gained from this process.
  -- What if the attributes are biased due to biased annotations or large models?

### Questions
Please refer to "weaknesses" part for my concerns.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
- This work proposes two new evaluation metrics, named Single-attribute Divergence (SaD) and Paired-attribute Divergence (PaD), that measure the divergence of a set of generated images from the training set.
- SaD measure the divergence of the marginal PDF of a single attribute, while PaD measures the divergence of the joint distribution of two attributes between a set of generated and ground truth images. 
- To measure the attribute strengths of an image, authors propose Heterogenous CLIP score which is based on heterogenous starting points. This formulation avoids the narrow range of values that result from a CLIP score achieving scores that are unrestricted and flexible.
- Finally, authors perform experiments comparing some popular GAN and Diffusion models, revealing some interesting properties, which can be attributed to the interpretability of the proposed metrics.

### Strengths
- Evaluating generative models is a very important area of research given the exponential progress achieved recently in this space. Researchers have identified several shortcomings with existing automatic evaluation methods of generative models which requires more analysis and research. This work tackles a very important research problem and proposes simple and effective evaluation metrics for generative models.
- Authors identify an important shortcoming of CLIP similarity score, a popular score used for evaluating conditioned generative models, and propose an alternative which is more interpretable. 
- The SaD and PaD metrics are theoretically well grounded and interpretable, unlike existing automatic evaluation metrics, making it a good diagnostic tool as well.
- Authors show some interesting preliminary analysis that agree with the general consensus of the public (SD 1.5 > SD 2.1).

### Weaknesses
- My major concern with the proposed metrics is with respect to resolution. How does the difference in absolute values translate to actually seeing a difference in the generations. For example, in [1] authors identify, with the help of human evaluation, that the resolution of FVD is 50, i.e. a human rater can tell the difference between generations of two models if their corresponding FVD scores differ by atleast 50 points. 
- How does SaD or PaD correlate with human evaluation? Do humans agree that the attributes identified by SaD and PaD are indeed misrepresented in the generations of the model?


[1] Thomas Unterthiner, Sjoerd van Steenkiste, Karol Kurach, Raphaël Marinier, Marcin Michalski, Sylvain Gelly, FVD: A new Metric for Video Generation, ICLRW 2019

### Questions
- Do these metrics correlate well with any existing evaluation metrics? 
- Do these metrics work with any other features than CLIP features? For example, for textures, do features from DINO/SAM (get reference features from some texture dataset and compare to features of generated images) work as well or is the joint embedding of CLIP necessary for the success of SaD and PaD.
- Can these metrics be used to measure quality and faithfulness of text to image generative models? If so, how would one go about that?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to evaluate the quality of image generation approaches by comparing the distribution of attributes (and attribute pairs) scores across the training dataset and the generated one. This is intended to capture whether the generative model has captured well the training distribution.
The requires either an auxiliary model trained for attribute detection, either ad hoc or a generic one like CLIP.

### Strengths
The method is well motivated.

### Weaknesses
1- The experiments aimed at investigating the behaviour of the approach seem to be, in their current form, inconclusive.
1.1 – In 5.1, it is not explained how the “normal images” are obtained. This prevents us from discerning whether it really is the out-of-distribution attributes that increase the scores, or simply the difference between the generated images and the normal ones.
1.2 – In 5.2, the authors intend to highlight the need of PaD over SaD. However, they do not actually compare them, with no results for SaD to be found in this section.
1.3 – The approach would be, by nature, sensitive to the quality of the attribute detector, and only attributes that are consistently visually detectable should be used, since the metrics would be a mixture of the quality of the generator and that of the detector.
2- The paper needs to be improved in terms of writing and structure.
2.1 – With respect to the writing, there are many sentences that need some improvement. Just some examples:
- “ They provide which attributes the models struggle.”
- “all SaD top-rank attributes have negative mean differences that mean SDs tend to omit some objects”
- “We infer that the color-related attributes are the inferiority of DMs”
2.2 – The mean difference (Eq 7), seems to be an element of the methodology but appears in the experiments section.
2.3 – Many of the figures (like Fig 4a) display text that is impossible to read to to its size (and when zooming in it actually becomes pixelated).
3 – Some of the comparisons could be more comprehensive. For instance, Table 4 shows no other metrics than the proposed ones.

### Questions
Please see the weaknesses.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
