# LDMol: Text-to-Molecule Diffusion Model with Structurally Informative Latent Space

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
With the emergence of diffusion models as the frontline of generative models, many researchers have proposed molecule generation techniques with conditional diffusion models. However, the unavoidable discreteness of a molecule makes it difficult for a diffusion model to connect raw data with highly complex conditions like natural language. To address this, we present a novel latent diffusion model dubbed LDMol for text-conditioned molecule generation. 
LDMol comprises a molecule autoencoder that produces a learnable and structurally informative feature space, and a natural language-conditioned latent diffusion model. 
In particular, recognizing that multiple SMILES notations can represent the same molecule, we employ a contrastive learning strategy to extract feature space that is aware of the unique characteristics of the molecule structure. 
LDMol outperforms the existing baselines on the text-to-molecule generation benchmark, suggesting a potential for diffusion models can outperform autoregressive models in text data generation with a better choice of the latent domain.
Furthermore, we show that LDMol can be applied to downstream tasks such as molecule-to-text retrieval and text-guided molecule editing, demonstrating its versatility as a diffusion model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents LDMol, a latent diffusion model for generating molecules based on text conditions. It overcomes the challenges in aligning molecular discreteness with natural language descriptions. LDMol employs a SMILES autoencoder that uses contrastive learning to create a chemically informative and structurally consistent latent space.

### Strengths
1. By incorporating contrastive learning into the SMILES autoencoder, LDMol achieves a chemically informative latent representation.
2. LDMoI proves effective in related applications like molecule-to-text retrieval and text-guided molecule editing, demonstrating the model's adaptability and potential utility across various domains within chemical and biomedical research.

### Weaknesses
1. The performance relies on text-molecule paired datasets, which are often limited to structural descriptors. This limitation is significant because many crucial aspects of molecular activity and function are not captured by simple structural descriptions, such as electronic properties, specific binding affinities, or dynamic behaviors. The model's ability to generate molecules with desired functional properties may be constrained by this lack of comprehensive data.
2. LDMol relies on detailed text prompts to generate precise molecular structures, which may reduce its effectiveness with vague or less specific text conditions. While the model can handle some level of ambiguity, the need for detailed prompts to achieve accurate molecular generation could limit its usability in scenarios where only general or high-level descriptions are available. This dependence on precise text input may also hinder the model's ability to explore novel chemical spaces that are not explicitly described in the training data.

### Questions
1. Since LDMol relies on paired text-molecule data, how does the model perform with smaller or less detailed datasets? Could the model be trained effectively on a smaller dataset, and are there any plans to explore data efficiency?
2. The model struggles with distinguishing stereoisomers effectively. What impact does this limitation have on downstream tasks like molecule editing or retrieval? Are there specific modifications that could improve the model’s stereoisomer sensitivity?
3. How does the computational efficiency of LDMol compare to SOTA autoregressive models?

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
* The authors propose LDMol, a latent diffusion model for text-to-molecule generation.
* A contrastive learning method is applied to learn a latent representation for molecules, and an LDM (with DiT backbone) is trained over the compressed latent space.
* The generative pipeline finally involves feeding the latent produced by the LDM to a separate AR decoder.

### Strengths
* The use of contrastive learning to learn SMILE representations that are invariant to traversal order is convincing and seems well-motivated.
* Solid evaluation of their proposed method featuring a lot of existing baselines on a variety of metrics.
* There is a clear need and desire in the community for more works on diffusion generation, especially on discrete data domains, rendering this work relevant and timely.

### Weaknesses
 * It seems odd that an AR transformer is needed for decoding when one of the selling points of LDM / diffusion models is parallel generation that relaxes the AR factorization of probability. The need for an LDM as well as a separately trained AR decoder makes the pipeline more convoluted in comparison to the usual domains (e.g., LDM for text-to-image generation). Specifically, the necessity of an AR decoder undermines the potential for parallel generation inherent in diffusion models, which is a significant drawback. The authors should clarify why the latent space produced by the diffusion model cannot be directly mapped to the SMILES string without resorting to an AR decoder.
* The work seems to largely apply existing techniques proposed in the image / text-to-image literature with little to moderate modifications for adaptation to the molecule generation domain. While the application of contrastive learning for SMILES representation is interesting, the overall pipeline closely mirrors existing LDM frameworks. The novelty of the approach is therefore limited, as it primarily involves adapting existing techniques to a new domain rather than introducing fundamentally new methodologies. The core idea of using a diffusion model with a latent space and a separate decoder is not novel in itself, and the modifications for molecular generation seem incremental.


### Questions
* Why is a separate linear compressor layer necessary? Why not configure the size of the latent space for the SMILE encoder / decoders to be smaller to begin with?
* (Related to above) Why is it necessary to train a separate AR transformer for the decoding step? Is it possible to feed the DiT output back into the SMILE decoder to generate a molecule sequence? The linear compressor layer is not invertible so this is probably not possible in the current setup, but assuming it were, would it not be simpler to use the trained decoder?
* Relative to compared baselines, is the proposed method faster? How does the runtime of the backward diffusion step compare to the AR decoding step?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study introduces LDMol, a latent diffusion model specifically designed for text-conditioned molecule generation. LDMol integrates a chemically informed autoencoder and employs contrastive learning to maintain structural consistency within the latent space, addressing issues with multiple SMILES representations for identical molecules. Experimental results indicate that LDMol surpasses current models in SMILES validity, structural fidelity, and condition adherence. Furthermore, LDMol proves versatile for applications such as molecule-to-text retrieval and text-guided molecule editing, offering a structurally aware diffusion model as a robust alternative to autoregressive methods in molecular generation research.

### Strengths
1.	It offers a thorough background on the difficulties of integrating text-based conditions with the discrete nature of molecular data, clearly outlining how LDMol tackles these challenges.
2.	The language and presentation are clear and scientifically rigorous, aligning well with standards for peer-reviewed publication.
3.	The authors substantiate their claims of enhanced text-conditioned generation through extensive benchmarking and showcase LDMol's applicability in downstream tasks, reinforcing its potential impact.

### Weaknesses
1. While the contrastive learning approach with SMILES enumeration is well-justified and innovative, a comparative discussion on why prior methods struggled with achieving structural consistency would enhance the reader's understanding of LDMol’s novelty. 	

2. The manuscript could enhance clarity by detailing the hyperparameter tuning process for the contrastive loss, especially concerning the InfoNCE loss temperature τ and its impact on the latent space.

3. The manuscript uses a linear compression layer to reduce the dimensionality of the latent space, which is sensible to avoid overfitting. The authors should, however, provide a more thorough justification of the chosen dimension (64) and discuss alternatives.

4. To refine the SMILES encoder’s capacity to distinguish between subtle structural variations (e.g., stereoisomers), it would be beneficial to conduct experiments incorporating additional molecular descriptors (e.g., 3D structural descriptors). This may improve encoding accuracy for complex molecular structures.

5. Some related works are needed to discuss in the manuscript, such as [1-2].

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents LDMol, a latent diffusion model for text-to-molecule generation. LDMol leverages a structurally informative latent space to enhance the generation of molecules conditioned on natural language. The model incorporates a molecule autoencoder and utilizes contrastive learning to improve its feature extraction capabilities. The results suggest that LDMol outperforms existing autoregressive models and demonstrates versatility in tasks like molecule-to-text retrieval and text-guided molecule editing.

### Strengths
1. The use of a latent diffusion model for text-conditioned molecule generation is novel and addresses the discreteness of molecular data.
2. The application of contrastive learning to capture structural features of molecules is well-motivated and effectively implemented.
3. LDMol shows superior performance over baseline models in generating valid SMILES that align well with text conditions.

### Weaknesses
1. The model architecture, including the use of multiple components like autoencoders and diffusion models, might be complex to reproduce and understand without extensive background knowledge. The specific implementation details of the autoencoder, such as its architecture, loss function, and training procedure, are not sufficiently detailed, making it difficult to assess its impact on the overall model performance. Furthermore, the interaction between the latent space of the autoencoder and the diffusion model is not clearly explained, raising questions about the stability and convergence of the training process.

2. While the model performs well on specific datasets, its generalization to other types of chemical data or broader text inputs could be further examined. The evaluation is primarily focused on a single dataset, and it is unclear how the model would perform on datasets with different chemical structures or text descriptions. For example, the model's ability to handle complex molecules with multiple functional groups or text inputs with nuanced chemical concepts is not thoroughly investigated.

3. Although the paper compares LDMol to existing models, more detailed comparisons with a wider range of benchmarks could strengthen the claims. The comparison is limited to a few baseline models, and it is not clear how LDMol would perform against other state-of-the-art models or more challenging benchmarks. The evaluation metrics used might not fully capture the quality of the generated molecules, and a more comprehensive evaluation using a wider range of metrics is needed.

4. The reliance on large datasets for training might limit the applicability of the model in scenarios where such data is unavailable. The paper does not provide a clear analysis of how the model's performance scales with the size of the training dataset. It is unclear whether the model can be effectively trained with smaller datasets or if it requires a large amount of data to achieve good performance.

### Questions
1. How does the model handle ambiguous or contradictory natural language inputs?

2. Can the approach be adapted for other domains beyond molecules, such as protein or material generation?

3. What are the computational requirements for training and deploying LDMol compared to traditional autoregressive models?

4. Are there any limitations in terms of the types of molecules that can be generated using this model?

### Soundness
2

### Presentation
2

### Contribution
2
