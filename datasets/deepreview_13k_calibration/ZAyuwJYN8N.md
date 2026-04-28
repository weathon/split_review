# InterMask: 3D Human Interaction Generation via Collaborative Masked Modelling

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Generating realistic 3D human-human interactions from textual descriptions remains a challenging task. Existing approaches, typically based on diffusion models, often generate unnatural and unrealistic results. In this work, we introduce \emph{InterMask}, a novel framework for generating human interactions using collaborative masked modeling in discrete space. InterMask first employs a VQ-VAE to transform each motion sequence into a 2D discrete motion token map. Unlike traditional 1D VQ token maps, it better preserves fine-grained spatio-temporal details and promotes \textit{spatial awareness} within each token. Building on this representation, InterMask utilizes a generative masked modeling framework to collaboratively model the tokens of two interacting individuals. This is achieved by employing a transformer architecture specifically designed to capture complex spatio-temporal interdependencies. During training, it randomly masks the motion tokens of both individuals and learns to predict them. In inference, starting from fully masked sequences, it progressively fills in the tokens for both individuals. With its enhanced motion representation, dedicated architecture, and effective learning strategy, InterMask achieves state-of-the-art results, producing high-fidelity and diverse human interactions. It outperforms previous methods, achieving an FID of $5.154$ (vs $5.535$ for in2IN) on the InterHuman dataset and $0.399$ (vs $5.207$ for InterGen) on the InterX dataset. Additionally, InterMask seamlessly supports reaction generation without the need for model redesign or fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article introduces a new framework called InterMask for generating 3D human interaction actions from text descriptions. The proposed framework appears to be based on the T2M-GPT framework, modeling in discrete space using generative masks, while also incorporating the concept of interhand to collaborate within the mask modeling framework by utilizing tokens from two interacting individuals. During the inference process, it starts with a fully masked sequence and gradually fills in the tokens for both individuals.

### Strengths
1. A Transformer structure combined with VQ-VAE has been proposed for generating 3D human interaction actions. 
2. It utilizes a 2D discrete motion token map to represent motion, distinguishing itself from traditional 1D representation methods. This representation better preserves spatiotemporal details and spatial awareness, which is crucial for accurately capturing complex motion relationships in human interactions. 
3. The framework has achieved state-of-the-art results on the InterHuman and InterX datasets, performing exceptionally well on various metrics. 
4. The average inference time is only 0.77 seconds, significantly lower than InterGen's 1.63 seconds, providing a considerable advantage in practical applications by enabling faster result generation.

### Weaknesses
1. In the visualization results, issues such as body penetration between interacting individuals and unnatural sliding movements still occur.
2. The article also mentions the masking strategy, but I believe its effectiveness may be influenced by various factors, such as the setting of the mask ratio and the dynamic adjustment of masks at different stages. The article does not delve deeply into how these factors affect model performance or how to optimally set these parameters. Specifically, the masking strategy's reliance on a fixed probability for random masking versus interaction masking, and the lack of a clear rationale for this choice, raises concerns about its adaptability to diverse interaction scenarios. Furthermore, the method for dynamically adjusting masks during the unrolling process, which is crucial for progressive refinement, lacks detailed explanation and empirical justification, making it difficult to assess its robustness and effectiveness.

### Questions
1. I noticed that in the second video of the visualization "Everyday Actions," the character on the right makes a sudden arm-raising motion, which seems somewhat disconnected. Additionally, is there a 10-second video available for reference? I saw that the authors mentioned the ability to generate interactive results up to 10 seconds long.

2. In terms of quantitative experiments, it seems there is no comparison with PriorMDM, which also produces results for two-person interactions. Similarly, there doesn't appear to be a comparison with other VQ-VAE methods like T2M-GPT. I'm curious about their results, especially since they perform very well on single-person datasets. If T2M-GPT were given a reference action sequence for one individual as an additional condition, how would it perform in generating interactive individuals, particularly on interactive datasets?

3. Regarding the Inter-M Transformer structure, although there is some evidence in the ablation studies concerning the relative importance of different attention mechanisms, it may not fully clarify their specific roles and trade-offs in different interaction scenarios and data distributions.

### Soundness
2

### Presentation
2

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
The paper presents InterMask, a framework for generating 3D human interactions using masked modeling in discrete space. By encoding motion as 2D token maps and modeling intra- and inter-person dependencies with a custom transformer, InterMask achieves impressive results on the InterHuman and InterX datasets. The model shows strong performance in terms of realism and alignment with text prompts, outperforming existing methods in controlled settings.

### Strengths
1. The use of 2D token maps and spatial-temporal attention layers in the Inter-M transformer enables more nuanced modeling of human interactions, demonstrating improved fidelity in motion generation.

2. InterMask achieves state-of-the-art results on key metrics in standard datasets, indicating its effectiveness in generating realistic, text-aligned interactions.

3. The model is relatively lightweight and demonstrates reduced inference time.

### Weaknesses
1. The paper’s innovative contribution is not well-defined. Although the authors introduce a transformer module to model intra- and inter-person spatial-temporal dependencies, this approach is widely used in various generative tasks. The ablation studies, which compare only with/without this module, do not sufficiently demonstrate the model’s unique contribution. If this module is intended as a core innovation, the authors should focus on explaining why its internal structure, arrangement, or sequence specifically suits the 3D interaction modeling problem. Merely showing the presence or absence of the module does not justify its relevance, as it is a fairly standard approach. The specific configuration of the transformer, including the number of layers, attention heads, and the precise arrangement of self, spatial-temporal, and cross-attention mechanisms, is not sufficiently justified in the context of 3D human interaction. A more detailed analysis of how these architectural choices are tailored to the nuances of human motion and interaction is needed, rather than simply stating its presence.

2. The process of converting each motion sequence into a 2D discrete motion token map lacks detailed description. The main innovation of this paper appears to lie in the combination of the 2D discrete motion token map with MAE; however, there is insufficient explanation of how the 2D token map is constructed. Providing a more thorough description, ideally with a detailed diagram, would enhance clarity and better communicate this aspect of the method. The paper lacks specifics on the exact convolutional layers used for downsampling, the size of the codebook, and the quantization method. Without these details, it's difficult to assess the impact of the 2D token map design choices on the overall performance of the model. The paper should clarify how the spatial and temporal dimensions are handled during the downsampling and quantization process.

3. User Study. The user study includes only three participants, which is insufficient to draw robust conclusions on user preference. A larger sample size and detailed descriptions of the study’s methodology would add reliability and provide stronger validation for claims of user preference for InterMask-generated interactions. The paper should specify the exact protocol used for the user study, including the number of samples evaluated per user, the method of comparison (e.g., side-by-side, A/B testing), and the specific criteria used for evaluation. Without these details, the user study results are difficult to interpret and may not be reliable.

4. Upon reviewing the supplementary videos, the generated motions appear to lack the fluidity seen in InterGen’s outputs. A discussion on this aspect would be valuable, particularly to understand any limitations in InterMask’s approach to generating smooth, natural motion. The paper should discuss the potential reasons for the observed lack of fluidity, such as the frame-by-frame processing or limitations in the model's ability to capture temporal dependencies. A comparison with other methods, specifically addressing the differences in motion smoothness, would be beneficial.

### Questions
1. Could the authors comment on the suitability of the current framework for multi-person interactions? Given the focus on two-person setups, it would be useful to understand any potential modifications or challenges in adapting this approach for more complex, multi-person interaction scenarios.

2. How does the model handle longer, more complex instructions or instructions that are less structured (in-the-wild)? 

3. Do the authors see potential for combining InterMask with language models to improve interpretability or to handle a wider range of textual prompts?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the problem of generating human-human interaction from textual descriptions. The authors introduce InterMask, a novel framework that employs 2D VQ-VAE to encode interactions into a discrete space and generative masked modeling to capture complex spatio-temporal interdependencies.

### Strengths
1. This paper introduces a novel 2D VQ-VAE that quantizes motion into a 2D discrete map, which can more effectively preserve fine-grained spatio-temporal details than the 1D version.

2. The proposed method achieves SOTA performance on the InterHuman and InterX benchmarks.

### Weaknesses
1. The method does not appear substantially different from prior work. Overall, the paper feels somewhat underwhelming, lacking distinctive insights, though there are no major issues with the experiments or writing. I would rate it as borderline.

2. The proposed approach faces challenges in generating human reactions in an online manner (although this isn’t the primary focus of the current setting). This capability would be more practical for some virtual reality applications.

### Questions
I have no other questions.

### Soundness
3

### Presentation
3

### Contribution
2
