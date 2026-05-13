# Interpretable Compressed Descriptions For Image Generation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Generative models can be applied in diverse domains, from natural language processing to image synthesis. A key aspect to control the generation process is the definition of adequate data representations, allowing users to access and efficiently manipulate the semantic factors shaping the data distribution.
This work advocates for the adoption of succinct, informative, and interpretable descriptions, quantified using information theoretic principles. Through extensive experiments, we demonstrate the efficacy of this proposed framework both qualitatively and quantitatively. We conclude that it significantly contributes to the ongoing quest to enhance both controllability and interpretability in the generation process.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a new method for selecting human-interpretable semantic descriptions that allow for precise and reliable control of diffusion image generative models. The authors find these descriptions via the Information Pursuit optimization with neural networks, collect datasets to support and evaluate their approach, and quantitatively and qualitatively validate the effectiveness of InCoDe (the proposed method) on four different datasets. Specifically, these datasets consist of image and query-answer pairs for each image that describe its semantic content. Out of the four datasets, two are new and created by the authors, where existing LSUN Bedroom and LSUN Church images are given relevant query-answer pairs to describe the images.

### Strengths
I find the paper generally well-written and polished. As a result, it was easy to read and understand. For instance, the mathematical equations are clear and notions used in this paper are explained in the appendix. The diagrams in Fig. 3 and Fig. 4 clearly show the how InCoDE is trained. 

Making image generation more controllable via succinct, human-interpretable descriptions is of great value to the image generation creative community. 

InCoDe is compared against solid baselines (Figure 8, Figure 9), where it achieves significant improvements in image quality. 

The authors promise the newly created datasets will "be released for public use", which is a big plus given the lack of similar datasets at the moment. 

The authors do a good job explaining the model architecture, datasets, and the hardware setup in A.3 EXPERIMENTAL DETAILS, which I believe makes the results reproducible.

### Weaknesses
The related works section is somewhat oversimplified -- I think the authors could do a better job offering more context on the current state of interpretability and controllability in image diffusion models. Specifically, the authors could delve deeper into methods that use attention mechanisms for control, or those that explore disentangled representations for semantic manipulation. The current discussion lacks sufficient detail on how InCoDe compares to these existing approaches in terms of both methodology and performance. 

Despite the effectiveness the authors have discovered with using InCoDe on the four dataset which they tested, it is not clear whether InCoDe can generalize to more "free-form" types of controllability. All four datasets include a fixed set of 40-58 queries that are hand-selected and deemed relevant, but in the real world, users use image diffusion models to generate highly diverse images. It would seem that they are out of luck if these images do not comply with one of the pre-defined set of queries. The paper does not address how the method would perform with queries outside of the training distribution, or how the model would handle compositions of multiple semantic concepts not explicitly seen during training. This raises concerns about the practical applicability of the method in real-world scenarios where users might want to combine or modify concepts in novel ways.

### Questions
*minor questions and concerns from the reviewer*
Some figures, e.g., Figures 8 and 9 appear to be raster rather than vector graphics? They look a bit blurry when I zoom in.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a framework InCoDe designed to improve the interpretability and control of image generation models. InCoDe provides a user-friendly, interpretable interface for custom image generation, enhancing both semantic control and user experience. The authors use the compressed, interpretable descriptions based on query-answer pairs to guide image generation, addressing limitations in current text-to-image models that struggle with composing multiple concepts accurately. And they also collected two new datasets along with sets of binary queries and answers about their content.

### Strengths
1. **A Novel User Friendly Interface:** InCoDe’s query-answer framework allows users to control image generation through a sequence of intuitive questions, making it more approachable and interactive than text-based inputs. This structure lets users directly specify attributes without needing technical prompts.
2. **Enhanced Interpretability and Control:** By using interpretable, information-rich query chains, InCoDe enables users to understand and shape each step of the image generation process, offering a clear view of how specific attributes impact the final image. This makes image manipulation more transparent and precise.
3. **Comprehensive Experimental Validation:** The framework’s effectiveness is demonstrated across diverse datasets and scenarios, with strong performance in generating accurate, attribute-aligned images.

### Weaknesses
1. **Limited Flexibility Compared to Text Input:** While the query-answer format improves control, it may restrict expressiveness compared to free-text descriptions. Users can only manipulate images within the bounds of available queries, which might not capture all desired nuances or novel concepts. The reliance on a predefined set of queries limits the ability to explore the latent space of the generative model in an unconstrained manner. For example, a user might want to generate an image with a very specific, unusual combination of attributes that is not covered by the existing query set, making it impossible to achieve the desired result.

2. **Potential Challenges in Real-World Scenarios:** InCoDe has been tested on curated datasets, but real-world image generation tasks may introduce more variability and ambiguity. Handling this with a fixed query-answer system may be challenging and could limit the framework’s effectiveness in broader, unstructured contexts. The curated datasets used in the experiments may not fully represent the complexity and diversity of real-world images, where objects and attributes can appear in a wide range of contexts and combinations. The framework's performance in these more complex scenarios remains unclear.

3. **Reliance on Visual Question Answering (VQA) Accuracy:** The framework depends on accurate VQA responses to generate coherent descriptions and images. Errors in VQA performance could affect the quality and alignment of generated images, especially in complex or nuanced queries. The VQA model's performance is crucial, and any inaccuracies in its responses could propagate through the system, leading to incorrect image generation. For instance, if the VQA model misinterprets a query about the color of an object, the generated image will likely depict the object with the wrong color, highlighting the fragility of the framework's reliance on VQA.

### Questions
See the weaknesses.

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
3

### Summary
The paper proposes a framework called InCoDe, designed to improve the control and interpretability of image synthesis models. InCoDe leverages information-theoretic principles and compressed, interpretable descriptions, enabling users to generate images through a sequence of query-answer pairs. The model uses an Information Pursuit technique to select the most informative queries for defining images and then generates images using a diffusion model based on these descriptions. InCoDe’s primary modules include a Querier, Decoder, and Generator, which work together to iteratively refine image generation given user's attributes.

### Strengths
+ The paper is well written and the authors have done a good hob in providing the motivation for the paper. In addition, the given examples throughout the paper help providing intuition and a more clear understanding.

+ Information-Theoretic Foundation: The method relies on information-theoretic principles to determine query relevance and hence, prioritizes the most informative attributes.

+ Conditioning pre-existing diffusion models to harness their prior while "smoothing" the training procedure is interesting.

### Weaknesses
- The theoretical foundations are mainly taken from [1], and adapted into a new domain (text-to-image generation)

- Experimental part - the used models are relatively obsolete - the method is demonstrated on SD 1.4 while there are newer and stronger model, that perhaps more capable of following user-specified instructions. Moreover, utilizing BLIP as an evaluation does not express the generated images quality. Perhaps inCode is capable of following the user specified attributes better but while decreasing images quality? I believe that images quality evaluation (e.g., FID) should be considered.

- The method requires pre-defined set of attributes, which is feasible in simple datasets, but significantly less in real-world datasets such as ImageNet or COCO.

- Minor - error in the axis names in Fig 8?

### Questions
Please see weaknesses.

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
2

### Summary
To improve generative modelling for multi-concept inputs, the paper proposes the Interpretable 'Compressed Descriptions for Image Generation' (InCoDe) Framework, which consists of a query encoder, an answer decoder, and a diffusion model. 

The proposed framework sidesteps natural language to condition the generator. If I understand correctly, concept vectors replace natural language embeddings. The concept vector is constructed using a visual question answerer in tandem with an Embedder + MLP combination. The resulting embedding is fed into a pre-trained diffusion model.

The methods section builds upon the work of Chattopadhyay et al. The paper's key innovation is that we can modify the answers from the visual question answerer, which leads to changed images.

The proposed framework is experimentally tested on the CLEVER, LSUN Bedroom, and LSUN Churches Datasets.

### Strengths
The work focuses on interpretability and is relevant to the community. The paper presents a solid extension of Chattopadhyay et al.'s (2023) work in an image generation setting.

### Weaknesses
Evaluation:

It would have been nice to compare it to an off-the-shelf diffusion model (https://proceedings.neurips.cc/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf) conditioned on, for example, the facial attributes of the CelebA dataset. The paper's introduction claims that generative models struggle when asked to compose images with multiple concepts. While Figure 2 illustrates the situation qualitatively, it would have been nice if the paper had followed up with a quantitative analysis of the situation, including a comparison to established work. Table 2 might be doing this. I am not sure if lines 342 to 351 refer to Table 2. Please clarify in the rebuttal.


Minor points:

- Links to the supplementary material are broken. Please consider submitting single files in the future. The author guide specifically encourages single file submission ( https://iclr.cc/Conferences/2025/AuthorGuide ).
 -  The writing was hard to follow at times. Consider lines 342 to 351, for example. It would have been nice to mention and link to a table where readers can find the numerical results right there.

### Questions
Figure 3:

- Why does the QueryAnswerer in Figure 3 compute $\hat{Q}(X)$ instead of $\hat{Q}({\hat{X}})$? Arent we minimizing the a 
cost term with $\hat{Q}({\hat{X}})$?

Equation two:

- How is the constraint in equation two enforced in practice?
- Do we need the decoder if we are mainly interested in the modified image?

Figure 8:

- What does DT-IC refer to?
- What does TopK-IC refer to?
- Are these related to lines 342 to 351?

Table 2:
- What do Stab. D and Stu. D refer to?
- Are these related to lines 342 to 351?

### Soundness
2

### Presentation
2

### Contribution
3
