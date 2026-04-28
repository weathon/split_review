# CORTEX: Concept-Oriented Token Explanation in Vector-Quantized Generative Model

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
Vector-Quantized Generative Models (VQGMs) have emerged as powerful tools for image generation. However, the key component of VQGMs---the codebook of discrete tokens---is still not well understood, e.g., which tokens are critical to generate an image of a certain concept? This paper introduces Concept-Oriented Token Explanation (CORTEX), a novel approach for interpreting VQGMs by identifying concept-specific token combinations. Our framework employs two methods: (1) a saliency-based method that analyzes token saliency value in individual images, and (2) an optimization-based method that explores the entire codebook to find globally relevant tokens. Experimental results demonstrate CORTEX's efficacy in providing clear explanations of token usage in the generative process, outperforming baselines across multiple pretrained VQGMs. CORTEX not only improves VQGM transparency but also enables tasks such as targeted image editing, offering valuable insights into the model's internal representations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach, named CORTEX, for interpreting token selections under given specific concept-related conditions in VQGMs. The authors develop a framework based on information extraction and derive two methods, i.e., saliency-based method and optimisation-based method, to analyse token combination modes for case-dependent and case-independent scenarios. Extensive experiments conducted under various settings indicate these two methods can well explain the mode of token combinations in VQGMs, thus demonstrating the effectiveness of proposed method and framework.

### Strengths
- There is a lack of sufficient interpretability and controllability analysis in the field of VQGM. This paper provides an effective supplement to this field.
- The author's writing is relatively clear and fluent.
- The author(s) conduct various experiments to comprehensively evaluate the quality of the proposed model from both qualitative and quantitative perspectives.

### Weaknesses
- Lack of some context, such as the source and performance of the VQGAN used. Specifically, the paper does not mention which pretrained VQGAN model was employed, nor does it provide quantitative results demonstrating the VQGAN's performance on the chosen dataset. This omission makes it difficult to assess the foundation upon which the proposed interpretability methods are built.
- The discussed domain is relatively narrow. It can be better if there are further discussions about the generalisation of proposed methods in a broader context. For instance, the paper could elaborate on how the proposed methods might perform when the number of concepts increases significantly or when the codebook size varies. Additionally, exploring the applicability of these methods to other tasks, such as text-to-image generation, would strengthen the paper's impact. It is not clear how well the proposed information extractors would adapt to substantially different concept distributions or codebook structures.
- It would be better if the author(s) could further analyze the relationship between saliency-based and optimization-based methods, and under what circumstances which one can provide more information / observations, rather than simply discussing the two methods side by side based on whether they are related to input. A more thorough comparison, potentially with a discussion of their respective computational costs and the types of insights they provide, would be valuable.

### Questions
- Regarding saliency-based method, the author(s) estimate TSV based on the absolute value of the gradient of $E$. Is it possible that the values in various dimensions of the embedding itself will affect the result? What if all the code entries have been normalized into unit vectors? 

- Regarding information extractors, it seems that there is tiny performance difference between these two extractors in Figure 3, Table 2 and Table 3. The author(s) attribute this to the insensitivity to extractor structure. However, RE and CE are actually both CNN-based extractors. Will the author(s) consider other kinds of structures like transformers? 

- Regarding the optimization-based method, the author(s) choose concept pairs with high similarity, and add a mask to study how tokens evolve in a small region. What would happen if we choose two concepts with a large distance in semantics and / or remove the mask constraint?

- Regarding the pretrained model, the sensitivity of ViT and CNN is different. Is there related analyses to this observation? 

- The author(s) mention that the proposed methods can help improve controllability of VQGMs. How can these two methods be used to improve the controllability of VQGMs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces CORTEX, a novel framework designed to enhance interpretability in Vector-Quantized Generative Models (VQGMs) by identifying concept-specific token combinations within the model’s codebook. CORTEX leverages two main methods: a saliency-based approach for analyzing token importance within individual images and an optimization-based approach to identify globally relevant tokens across the codebook. By doing so, CORTEX facilitates concept-specific explanations in VQGMs, enabling practical applications like targeted image editing. Experiments demonstrate the framework’s efficacy in interpreting token contributions, providing insights into the VQGM’s internal workings.

### Strengths
* The tackled explainability of vector-quantized tokens used in image generative models is an interesting problem worth exploring.
* The two proposed methods are solid defined and well presented

### Weaknesses
 * The comparison between a CNN-based extractor and a Resnet-based extractor does not provide valuable information on the effectiveness of the proposed approach.
* It remains unclear how useful the explanation obtained via both methods potentially is. Possibilities for identifying biases, improving robustness, etc. need to be clarified to justify the proposed design.
* The experiments are limited on imagenet with class-conditioned generation, whereas the more general text to image setup where explanation might be more important is not explored.

### Questions
* Since the submission focuses on the explanation of the tokens used during generation, can some visualization of the token space rather than pixel space be provided as a better presentation of the explanation process?
* Although image tokens are usually strongly correlated to the corresponding pixel region, simply masking the pixel region remains questionable as the token could have affected other pixels during the token-to-pixel decoding. Have the authors trying masking the tokens before decoding to pixels?
* What would be a reasonable setup to evaluate the proposed methods on text-to-image models?
* How to present some empirical and quantitative results to justify the usefulness of the explanations produced by the proposed methods? What new capabilities could be possibly enabled if we can explain them?

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
2

### Summary
This paper discusses Vector-Quantized Generative Models (VQGMs) as effective tools for image generation, highlighting a gap in understanding the specific function of discrete tokens within these models' codebooks. To address this, the paper introduces Concept-Oriented Token Explanation (CORTEX), a novel methodology for interpreting VQGMs by identifying critical token combinations linked to specific concepts. CORTEX utilizes two main approaches: a saliency-based method that evaluates token significance in individual images, and an optimization-based method that searches the entire codebook to identify globally relevant tokens. The experimental results indicate that CORTEX provides clearer explanations of token usage in the image generation process compared to existing baselines and enhances the transparency of VQGMs. This improvement facilitates advanced applications such as targeted image editing and offers valuable insights into the internal representations of the models.

### Strengths
- The introduction of CORTEX provides a fresh perspective on interpreting VQGMs by focusing on concept-specific token combinations. This approach enhances the understanding of how models generate specific concepts, which is crucial for improving model transparency and usability.

- By addressing the challenge of distinguishing between essential and non-essential tokens, the paper contributes to the interpretability of VQGMs. This focus is particularly important in applications where understanding model decisions is critical.

### Weaknesses
 - The saliency-based method, while effective for identifying relevant tokens, may risk overfitting to specific instances of a concept rather than providing a more generalized understanding. This could result in explanations that are too tailored to particular images, reducing their utility for broader applications. Specifically, the method might highlight tokens that are only relevant due to the unique background or lighting conditions of a single image, rather than capturing the core concept. For example, if analyzing a 'cat' concept, the saliency map might overemphasize tokens related to a specific type of fur pattern or a particular room's lighting, instead of the fundamental features that define a cat across various contexts.

### Questions
- Can you provide more details on how CORTEX compares to existing explainability methods for generative models?

- How do you address the potential issue of biases present in the pretrained VQGMs affecting the explanations generated by CORTEX? What steps can be taken to ensure that the explanations are fair and unbiased?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work looks to expand explainability and interpretability methods to vector-quantized generative models. The authors spend little time motivating the work, but the goal seems to be to discover how the discrete tokens used by VQGMs can be meaningfully interpreted in deployed models on a concept level. The authors propose a token based saliency-based information bottleneck in conjunction with a proposed input independent method for codebook search in an input dependent and input independent approach, respectively.

Briefly summarised; the input dependent framework applies a gradient based saliency method (Simonyan et al., 2013) to retrieve a token saliency value (TSV). Then, by using a support set of conceptually related images to mine for highly frequent tokens related to a specific concept. For the input-independent approach, tokens are mined using a token selection matrix with gradient based discrete optimization with the GumbelSoftmax.

Overall, the work unfortunately comes across as somewhat niched. In conjunction with the limited motivation by the authors, this reviewer has difficulty placing the work in the broader context of current research, neither in the field of explainability nor generative image modelling. Showing how the approach could be applied in more general context could potentially strengthen the work.

### Strengths
S1: The methodology of combining saliency and optimization methods for selecting relevant tokens in codebook approaches has a degree of novelty, which could possibly generalise to other applications, such as mining concept based prototypes. This would possibly also allow for more baselines, as this field is an active field of study with several contributions in active use and development.

S2: Targeted editing with VQGMs have applications in content moderation and interactive generation. The proposed method’s basis in delineating regions by concept seems appropriate in these tasks.

### Weaknesses
W1: The saliency method is based on Simonyan et al. 2013, which has been shown to be highly independent of model predictions. Adebayo et al. 2018 show that saliency maps produced by these methods demonstrate little change when replacing most of the layers of a network under scrutiny with randomly initialised weights, hence the method the current work bases its saliency method on has dubious interpretive value.

W2: The use of a tailored synthetic dataset generated as an evaluation of the proposed method strikes this reviewer as dubious, even given the setting of interpretations for generative models. This limits the overall generalisability of the approach to be specific for VQGMs, as opposed to a more general mining approach. If this was a necessity for training the method (which is not clear to this reviewer at this point), the argument for its use in evaluation should be emphasised in the manuscript.

W3: The value of the proposed method comes across as highly specific and somewhat niched. This necessarily translates to limited context and baselines in other works.

W4: Aside from targeted image editing with VQGMs, the fundamental motivation behind the work is insufficiently established in the introduction. The importance of interpretability in VQGMs could be more strongly emphasised in the manuscript. Consider demonstrating the motivation behind the work to the reader through examples or potential applications.

W5: The overall methodology is, in this reviewer's opinion, somewhat unclear. This could be improved by highlighting the importance of input dependence / independence, discussing how these two approaches interact, and more explicitly clarifying or showing how they are combined to form a unified interpretation with concepts.

W6: The proposed method is designed specifically for VQGMs, and as such, has somewhat limited scope. As diffusion models have been shown to generally provide higher quality in image generation, the method is naturally more limited in impact. While this in and of itself does not mean the work does not have value, considering the impact plays a role in evaluating the work for the conference.

### Questions
Q1: What are the authors opinions on the broader impact of the work, and what concrete problems their proposed methods solve, aside from targeted editing with VQGMs? 

Q2: Could the reliance on the synthetically generated dataset be dropped? If not, could the authors provide a convincing rationale for its necessity?

Q3: Can mined concepts from the codebook be applied in other applications with discrete token-based backbones?

Q4: Given aforementioned issues with Simonyan et al., did the authors consider ablating the effects of token based saliency with alternative approaches?

### Soundness
2

### Presentation
2

### Contribution
2
