# Generating Multi-Modal and Multi-Attribute Single-Cell Counts with CFGen

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
Generative modeling of single-cell RNA-seq data has shown invaluable potential in community-driven tasks such as trajectory inference, batch effect removal and gene expression generation. However, most recent deep models generating synthetic single cells from noise operate on pre-processed continuous gene expression approximations, ignoring the inherently discrete and over-dispersed nature of single-cell data, which limits downstream applications and hinders the incorporation of robust noise models. Moreover, crucial aspects of deep-learning-based synthetic single-cell generation remain underexplored, such as controllable multi-modal and multi-label generation and its role in the performance enhancement of downstream tasks. This work presents Cell Flow for Generation (CFGen), a flow-based conditional generative model for multi-modal single-cell counts, which explicitly accounts for the discrete nature of the data. Our results suggest improved recovery of crucial biological data characteristics while accounting for novel generative tasks such as conditioning on multiple attributes and boosting rare cell type classification via data augmentation. By showcasing CFGen on a diverse set of biological datasets and settings, we provide evidence of its value to the fields of computational biology and deep generative models. 
 \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes CFGen, which is a latent flow-matching generative model for single-cell data, where the latent space is first learned by an autoencoder. To capture statistical properties specific to single-cell data, the autoencoders learn to decode the parameters of a negative binomial distribution and Bernoulli distribution, for RNA-seq and ATAC-seq data, respectively. Conditional generation is achieved through classifier guidance. Empirical results demonstrate that CFGen outperform other single-cell generative models in terms of (1) data generation to approximate the real data distribution, (2) data generation for rare cell type classification, and (3) batch correction.

### Strengths
- Adapting flow matching for single-cell data generation is a novel contribution.
- The proposed framework CFGen can be easily adapted for different uni- and multi-modal scenarios, as long as there are modality-specific autoencoders with a common latent space.

### Weaknesses
 - scVI should be included as a baseline in Figure 2 because scVI accounts for overdispersion and zero inflation, whereas the current baselines in Figure 2 (scDiffusion and scGAN) do not.
- For downstream applications that rely on conditional generation, it is unclear how the classifier guidance strength is determined. Specifically, the manuscript lacks a clear methodology for selecting the guidance strength parameters, which are crucial for balancing the trade-off between data generation fidelity and the desired conditional effect. This makes the results difficult to reproduce and interpret.
- Quantitative results are lacking when evaluating the compositional classifier guidance in Section 5.3. The change in MMD and WD with respect to the target distribution when increasing guidance strength can suffice. Furthermore, it is unclear how the authors ensure that the generated cells at the intersection of the two labels are not simply a result of mode collapse, where the model only generates a limited set of samples that happen to satisfy both conditions.

### Questions
- For batch correction, is CFGen's performance (in terms of the Batch and Bio scores) sensitive to varying the guidance parameters? How does one tune the guidance parameters in practice?
- For cell type classification, simple models such as logistic regression (with or without regularization) are often used. Does data augmentation with CFGen improve performance for a logistic regression model?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents conditional flow-based generative models for single-cell RNA-seq and accessibility data. Single cell data is generally sparse, noisy, and has high feature variance. The authors suggest a flow matching based approach as a more expressive, and consistent generative model compared to VAEs, and GANs for generating synthetic cells. They also present a compositional variant of classifier-free guidance for flow-based models to allow conditioning on various attributes. Finally, they evaluate the model on two downstream tasks: (1) generating synthetic samples of rare cell-types and using them for data-augmentation,  (2) leveraging CFGen for batch correction.

### Strengths
1. The paper addresses an important problem in single-cell data generation by generating raw count values, and further extending this to multimodal generation.
2. The paper is well-written, and the authors convey major limitations of their model clearly.
3. The results show that CFGen is able to capture characteristics of the training dataset and generate single cell data with similar statistical properties.
4. They also show the effectiveness of generating rare cell-types to improve classification performance for other models.

Post Rebuttal comments:

The authors have addressed my concerns regarding the presentation. They have also added the additional details I addressed in the weaknesses below. After going through their responses to other reviewers, I believe the paper will be a valuable addition to ICLR. I am raising my score to accept.

### Weaknesses
1. Fig 3. is not really clear to me. Firstly, I suggest adding contrasting colors for points representing generated and real data. Secondly, what are the red points representing? I also suggest perhaps adding a quantitative metric (perhaps a oracle model that predicts the attributes) as well.
2. I also suggest removing the bars from Fig. 2b as they make it hard to observe the overlapping density curves which are easier to infer from.
3. For Sec 5.2, it might be worthwhile to also add a comparison with CFGen just trained on RNA-data in order to measure the effects of using multimodal data for training.
4. A comparison of inference times might also be useful in this case, especially to compare scDiffusion and CFGen, since both require multiple time steps. Adding approximate training times for each of the comparable models would also be valuable.
5. Fig.4 should also report the raw accuracy numbers for each of the cell-types to evaluate the effect of CFGen,

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors of this paper present CFGen, a flow-based generative model designed for multi-modal single-cell data. CFGen addresses the challenges of generating discrete, multi-modal data while allowing conditional generation based on various biological attributes. The model extends the flow matching framework to handle compositional guidance across multiple attributes and provides promising results on tasks like data augmentation, rare cell type classification, and batch correction.

### Strengths
- The authors nicely demonstrate practical applications of their method such as data augmentation in rare cell types, improving downstream classification, and performing batch correction. 

- The idea to extend flow matching for generation with multiple attributes is interesting and important for single-cell data.

- The paper is well-written, the related work is appropriately referenced, and the experimental setup is detailed.

### Weaknesses
 -  The authors do not discuss the computational complexity of the proposed method. A more detailed breakdown of computational requirements, including training and sampling times for the proposed method and the baselines, would improve the paper.

- One important task in single-cell data analysis is gene expression imputation, where missing or zero-inflated gene expression values are inferred to provide a more complete view of cellular states. It is unclear from the paper whether CFGen can effectively handle this task, given its focus on generating new cells rather than imputing missing data within existing cells. Could the authors clarify if CFGen’s architecture or the flow matching framework could be adapted for imputation?

### Questions
- Can CFGen be applied to gene expression imputation tasks? If so, could the authors describe how the current framework could handle imputation, or if modifications would be needed?

- Could the authors provide details about the computational complexity of the model?

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
4

### Summary
In summary, I initially rate this paper as  "5: marginally below the acceptance threshold". But I'm open to increase my score if authors properly answer my doubts in the rebuttal.

Summary of paper: The paper proposes a generative model for scRNA as well as accessibility modalities. The model can take in a combination of attributes, which suits the biological settings where for each cell only a subset of attributes are available. The method is evaluated in generation, handling label imbalance in cell type classification for rate cell types, and batch correction.

### Strengths
- The model is tailored to real biological settings: it handles 2 modalities (scRNA and ATAC) and any number of attributes.
- The results properly support the good performance of the method. 
- Besides generation power, two very interesting applications are demonstrated: handing rare cell types in cell type classification and batch correction.

### Weaknesses
 - Handling discrete count data via negative binomial distribution is presented as a "contribution" of this paper. But there is a plethora of methods that make use of negative binomial (or alternatives like poisson distribution) to handle count data as well as over-dispersion. So why should it be listed as a contribution of this paper?
- According to the paper, "... the proposed factorisation is novel". In the factorisation of Eq. 5 what is the rational behind conditioning the latent factor z on library size? It's unclear why this is necessary, especially given that library size is often considered a technical artifact. The paper should provide a more thorough justification for this design choice.
- In proposition 1, the attributes $y_1$, $y_2$, ... are assumed to be conditionally independent given $z$, but with the factorisation of Eq. 5 the attributes are connected to $z$, hence $z$ forms a V-structure which according to d-separation causes the attributes to be dependant given $z$ ? This point needs further clarification, as the current explanation appears to contradict the conditional independence assumption.
- Regarding the proposed guidance scheme, the only difference to the normal classifier-free guidance is that only some attributes (and one attribute during training) is fed to the decoder. Is this approach equivalent to the normal classifier-free guidance with all attributes plus some attributes being randomly dropped out? Even if so, it wouldn't decrease the value of the proposed method. The paper should clarify the specific advantages of their approach over standard dropout-based methods.
- In Table 1 scDiffusion is heavily outperformed by the proposed method, but one may say diffusion models may perform on par with flow matching (apart from training stability etc.). In the paper I'd recommend providing an explanation for the superior performance of the proposed method compared to scDiffusion. The paper should delve deeper into the architectural and training differences that lead to this performance gap, rather than simply stating that it performs better.

### Questions
Please see the "Weaknesses" part.

### Soundness
2

### Presentation
3

### Contribution
2
