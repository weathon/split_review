# Controllable Data Generation with Hierarchical Neural Representations

- Decision: Reject
- Scores: 5, 5, 6, 6, 6

## Abstract
Implicit Neural Representations (INRs) represent data as continuous functions using the parameters of a neural network, where data information is encoded in the parameter space. Therefore, modeling the distribution of such parameters is crucial for building generalizable INRs. Existing approaches learn a joint distribution of these parameters via a latent vector to generate new data, but such a flat latent often fails to capture the inherent hierarchical structure of the parameter space, leading to entangled data semantics and limited control over the generation process. Here, we propose a $\textbf{C}$ontrollable $\textbf{H}$ierarchical $\textbf{I}$mplicit $\textbf{N}$eural $\textbf{R}$epresentation ($\textbf{CHINR}$) framework, which explicitly models conditional dependencies across layers in the parameter space. Our method consists of two stages: In Stage-1, we construct a Layers-of-Experts (LoE) network, where each layer modulates distinct semantics through a unique latent vector, enabling disentangled and expressive representations. In Stage-2, we introduce a Hierarchical Controllable Diffusion Model (HCDM) to capture conditional dependencies across layers, allowing for controllable and hierarchical data generation at various semantic granularities. Extensive experiments on CelebA-HQ, ShapeNet, SRN-Cars, and AMASS datasets demonstrate that CHINR improves generalizability and offers flexible hierarchical control over the generated content.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel method for Implicit Neural Representations (INRs) called Controllable Hierarchical Implicit Neural Representation (CHINR). The method introduces a hierarchical approach to sampling and constructing latents that captures the layer-wise dependencies in the weights of a network and allows for controllable generation. The method is benchmarked on data generation against previous INR models, and qualitative results show the efficacy of the hierarchical approach.

### Strengths
-The hierarchical approach is interesting and worth exploring in more detail.

-The diffusion approach is novel and seems like a good approach to modeling the causal structure between the latents across different layers.

### Weaknesses
Overall, the paper seems incomplete to me. Table 1 is missing a lot of values, and there is a lack of benchmarking. The idea is not wholly uninteresting—in fact, I think with more benchmarking on the novel aspects of their method, the authors can put together a compelling manuscript. Ultimately, however, this manuscript is not ready for ICLR. I suggest the authors use this feedback to prepare for a submission to the next available proceedings.

-The glaring weakness in this paper is the lack of benchmarking against alternative methods. Even the only benchmarking table, Table 1, is incomplete. The only method that was fully benchmarked is mNIF, which seems to be the predecessor upon which this paper is based. Furthermore, the generation results show only marginal improvement, and it is hard to determine whether these are significant without repeats and standard errors. E.g. line 354: “Our model outperforms existing methods on most datasets.”—this is not sufficiently justified by the half-completed table.

-Related to the previous point, the hierarchical component of the model is the heart of the method, yet the only analyses I see are the qualitative figures and the correlation matrix between layers. The authors should think of a benchmark that can exploit the hierarchical structure of their model to demonstrate its utility.

-Without some kind of benchmark of the utility of the hierarchical construction of latents, the method presents itself as only a slight generalization of mNIF with much more baggage, owing to the diffusion component needed to generate the hierarchical latents. Additionally, the generation benchmark shows CHINR is at best comparable to mNIF.

-The paper is a bit hard to read—for example, I recommend clearly outlining the training procedure in stage-1, as I don’t think the mNIF method is a well-known standard method. This is less of a concern than the previous points.

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
In this paper, authors first posit that current generative Implicit Neural Representations (INRs) ignore hierahical structure in latent parameter distributions. To address this issues, authors propose Controllable Hierarchical Implicit Neural Representation (CHINR), consisting of two innovations: (1) Layers-of-Experts (LoE) Network and (2) Hierarchical Controllable Diffusion Model (HCDM).

### Strengths
1. The paper addresses a core limitation in Implicit Neural Representations (INRs): the use of a "flat" latent distribution $h$ which overlooks the inherent hierarchical structure of the data. To resolve this, the authors propose a diffusion model that leverages conditional distributions to capture this hierarchy. The motivation is clearly articulated, and the solution is well-suited to tackle the challenge by directly modeling hierarchical dependencies in the latent space.

2. The paper is well-written, presenting the proposed method with clarity and precision. Despite the complexity of the approach, the authors have structured the content effectively, making it accessible and straightforward to follow.

### Weaknesses
1.  The improvement over the most comparable method, mNIF, appears incremental. This paper builds upon the mNIF framework, adopting a similar two-stage process with latent modulation and a mixture of networks/layers, targeting the same challenge of capturing layer-wise hierarchical structure. However, despite the added complexity and potential inference cost, the performance gains relative to mNIF methods seem incremental. I am not sure the increased model complexity justifies the marginal improvements — since the method seems quite complicated. 

2. Although the analysis in Section 4.3 effectively demonstrates how different layers control distinct semantic aspects of the generated content and highlights the importance of conditional modeling, the ablation study in Section 4.4 is less convincing. The authors primarily provide anecdotal examples without sufficient quantitative evidence. Even though the examples shown in Figure 8 indicate the importance of conditioning, expanding the experimental details and including quantitative metrics would be helpful — since it is so central to the main contribution of the paper.

### Questions
1. I am not an expert on this, but I noticed that mNIF reports the number of parameters and inference cost across different generation models, which seems relevant for a fair comparison. Would it be important to consider the size of the data generator as a factor here? How does CHINR's inference cost and model size compare to its competitors?

### Soundness
3

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
3

### Summary
This paper introduces a novel deep generative model for Implicit Neural Representations (INRs), designed to capture hierarchical dependencies between INR layers through a structured latent space. The proposed model, CHINR, employs a Layers of Experts (LoE) framework, where weights are globally shared, and the expert weights are obtained through data-specific learnable latent vectors mapped into gates for the LoE. After learning these latent vectors, the second stage leverages a hierarchical conditional diffusion model to approximate $p(\mathbf{h})$ in a layered manner. Extensive empirical evaluation supports the design choices, showing that CHINR outperforms most baselines while offering improved interpretability and controllable generation capabilities.

### Strengths
- The contributions are both relevant and well-supported by empirical results.
- The paper is clearly structured and easy to follow.
- The proposed method demonstrates robustness across evaluations.
- Limitations are thoughtfully discussed, with suggestions for future work to address them.

### Weaknesses
 - The background section omits a few relevant recent works.

 - Recent generative models of INRs are not referenced in the background section. While [1-4] are included as methods that learn the latent distributions that map to or modulate INR parameters, it’s important to note that not all of these methods use meta-learning or a two-stage training approach. Specifically, [1,5,6] introduced end-to-end models where both the latent model and the latent-to-INR model are learned jointly, using GANs and VAEs. Also, there are other recent two-stage works that trained diffusion models over the latent vectors mapped to INRs, such as [7]. I suggest the authors include all the references to these additional works.

 - In Section 3, the text states that "the high dimensionality of raw weights is intractable." However, in [1,5,6] the full set of INR weights is efficiently generated via hypernetworks, achieving competitive results.

 - Typo on Line 465: "dependecy" should be corrected to "dependency."

### Questions
### Background

- Recent generative models of INRs are not referenced in the background section. While [1-4] are included as methods that learn the latent distributions that map to or modulate INR parameters, it’s important to note that not all of these methods use meta-learning or a two-stage training approach. Specifically, [1,5,6] introduced end-to-end models where both the latent model and the latent-to-INR model are learned jointly, using GANs and VAEs. Also, there are other recent two-stage works that trained diffusion models over the latent vectors mapped to INRs, such as [7]. I suggest the authors include all the references to these additional works.

### Minor Comments

- In Section 3, the text states that "the high dimensionality of raw weights is intractable." However, in [1,5,6] the full set of INR weights is efficiently generated via hypernetworks, achieving competitive results.

- Typo on Line 465: "dependecy" should be corrected to "dependency."

### References

[1]: Dupont, Emilien, Yee Whye Teh, and Arnaud Doucet. "Generative Models as Distributions of Functions." International Conference on Artificial Intelligence and Statistics. PMLR, 2022.

[2]: Du, Y., Collins, K., Tenenbaum, J., & Sitzmann, V. (2021). Learning signal-agnostic manifolds of neural fields. Advances in Neural Information Processing Systems, 34, 8320-8331.

[3]: Dupont, Emilien, et al. "From data to functa: Your data point is a function and you can treat it like one." International Conference on Machine Learning. PMLR, 2022.

[4]: Bauer, Matthias, et al. "Spatial functa: Scaling functa to ImageNet classification and generation." arXiv preprint arXiv:2302.03130 (2023).

[5]: Koyuncu, Batuhan, et al. "Variational Mixture of HyperGenerators for Learning Distributions over Functions." International Conference on Machine Learning. PMLR, 2023.

[6]: Xu, Siyuan, et al. "Uncertainty-aware Continuous Implicit Neural Representations for Remote Sensing Object Counting." International Conference on Artificial Intelligence and Statistics. PMLR, 2024.

[7]: Park, Dogyun, et al. "DDMI: Domain-agnostic Latent Diffusion Models for Synthesizing High-Quality Implicit Neural Representations." The Twelfth International Conference on Learning Representations.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors exploit a hierarchical and sparse structure prevalent in INRs to conceive a data generation method that is more controllable and modular than contemporary approaches.

I am far from knowledgable in this field. Take my review with a heap of salt.

### Strengths
- The compositionality aspect of this method is enticing
- The controllability and clear hierarchical order (Fig 1) is fascinating
- The premise of utilizing the hierarchical structure of the SIREN INR seems intuitive and reasonable to me.

### Weaknesses
 - Table 1 needs uncertainties to gauge superiority or consistency. The method  does not seem super strong on the performance front.
- Given the discrepancy in the conditional chain (and thus worse image quality) when controlling the latents as done in Fig. 6 (see L456ff), is the controllability aspect still a valid bonus? Is this a drawback that can be retroactively fixed by somehow iterating multiple times over the hierarchies?



### Questions
- How does it happen that, for instance in the middle of Figure 1, the hierarchies so nicely align with human abstractions over the data? It seems somewhat coincidental to me that the first layer corresponds to the type of object (chair, jet, table) and the next layer corresponds to the type of chair, and so on.
- It would be nice to see an equation for the LoE. Is each expert a SIREN model? Are the experts fully connected, and then controlled by a layer-specific gating function?
- In eq.3, isn’t $p(h^l|h^{<l}) = p(h^l|h^{l-1})$ (i.e. markov)?
- The design of the condition seems very ad-hoc, specifically the quantization. Can you motivate this further beyond “removing enough information to not overtrain”? Since the very coarse quantization causes a discontinuity in the condition, I expect this to have weird side effects, albeit maybe not super prominent in this domain.
- Nit: citation needed in L32 for INRs

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel framework called Controllable Hierarchical Implicit Neural Representation (CHINR), aimed at enhancing data generation and control through hierarchical neural representations. CHINR leverages implicit neural representations (INRs) to represent complex data as continuous functions and incorporates hierarchical dependencies across layers to improve generalizability and control. The framework operates in two stages: first, it builds a Layers-of-Experts (LoE) network where each layer uses specific latent vectors to manage distinct data features, allowing for a disentangled representation. In the second stage, a Hierarchical Controllable Diffusion Model (HCDM) is used to capture conditional dependencies across layers, enabling nuanced control of generated content. Experiments across various datasets (e.g., CelebA-HQ, ShapeNet, and AMASS) show that CHINR offers improved generalizability and hierarchical control over generated data.

### Strengths
1. CHINR’s two-stage framework with LoE and HCDM effectively captures hierarchical structures in data, enhancing representation control and generalisability.
2. The model is rigorously evaluated across multiple modalities, showing consistent improvement over baseline methods, especially in quality and generalisation.
3. The model’s ability to control data generation at multiple granular levels (e.g., overall structure, fine details) is a substantial advancement for applications requiring precision.

### Weaknesses
see questions.

### Questions
1. Could the proposed binary conditions be replaced or optimised further to improve interpretability or training efficiency?
2. How does CHINR handle data types with less hierarchical structure (e.g., text), and is its control mechanism adaptable to such cases?
3. How sensitive is the hierarchical control to variations in input data quality, and could this affect generalisation in real-world applications?

### Soundness
3

### Presentation
3

### Contribution
3
