# Periodic Materials Generation using Text-Guided Joint Diffusion Model

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Equivariant diffusion models have emerged as the prevailing approach for generating novel crystal materials due to their ability to leverage the physical symmetries of periodic material structures. However, current models do not effectively learn the joint distribution of atom types, fractional coordinates, and lattice parameters of the crystal material in a cohesive end-to-end diffusion framework. Also, none of these models work under realistic setups, where users specify the desired characteristics that the generated structures must match. In this work, we introduce TGDMat, a novel text-guided diffusion model designed for 3D periodic material generation. Our approach integrates global structural knowledge through textual descriptions at each denoising step while jointly generating atom coordinates, types, and lattice parameters using a periodic-E(3)-equivariant graph neural network. Through extensive experiments with popular datasets on benchmark tasks, we first demonstrate that integrating textual knowledge significantly improves the material generation capabilities of existing state-of-the-art models. Furthermore, we show that TGDMat surpasses text-guided variants of existing baseline methods by a substantial margin, highlighting the effectiveness of our joint diffusion paradigm. Additionally, incorporating textual knowledge reduces overall training and sampling computational overhead while enhancing generative performance when utilizing real-world textual prompts from experts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents TGDMat, a novel text-guided diffusion model for generating periodic crystal materials. TDGMat jointly models the generation of atom types, coordinates, and lattices of materials using separate diffusion processes. Specifically, it uses a Denoising Diffusion Probabilistic Model for lattice modeling, and uses a discrete diffusion model D3PM for modeling atom types. As for atom coordinate modeling, the authors mainly follow DiffCSP and use a score matching objective. Note that, they apply diffusion on fractional coordinates, instead of Cartisian coordinates, which cannot reflect the periodicity of crystal materials. To ensure geometric symmetry, TGDMat uses the CSPNet proposed by DiffCSP, which ensures periodic E(3) invariance for periodic crystals.

For the text-guided component, material descriptions are generated using Robocrystallographer software. Text embeddings, produced by a language model, are then concatenated with node embeddings to guide material generation.

### Strengths
1. The overall performance is good, as shown in Table 3. TGDMat shows significant improvement on the random material generation task compared to previous methods. Additionally, the authors demonstrate the importance of incorporating text-guidance by showing the improved performance of baselines in Table 1 and Table 2.
2. The method is overall sound and well-engineered. The authors have employed state-of-the-art diffusion methods for each modality associated in the whole material generation process. The source code is attached as a supplementary material. 
3. The textual annotation for the material dataset is a nice additional contribution, and is potentially impactful. It can stimulate future research for joint text and material modeling.

### Weaknesses
1. It seems that a large proportion of the methodology is borrowed from the previous work DiffCSP. This includes the diffusion process for atom coordinates, the diffusion for lattice, and the GNN backbone. 
2. The authors are suggested to use the \citep command instead of \cite for citations to improve the readability. 
3. The proposed method has achieved significant performance on the employed evaluation metrics, like validity and coverage. Does this mean the model can be readily employed for practical material discovery in industry? If yes, can you include further discussion on this application? If not, what is a barrier? Are there any other evaluation metrics that should be measured, like the novelty of the generated material compared to the training set, before application?

### Questions
1. How large is the proposed model and the compared baselines for material generation?

### Soundness
4

### Presentation
3

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
The paper introduces a text-guided diffusion model for generating 3D periodic materials. The work leverages a periodic-E(3)-equivariant graph neural network (GNN) to jointly generate atom types, fractional coordinates, and lattice structures, while integrating textual descriptions at each denoising step.

### Strengths
1. The model effectively learns the joint distribution of atom coordinates, types, and lattice structure through an end-to-end diffusion network, which is a significant improvement over existing models that handle these aspects separately.
2. Incorporating textual descriptions as a condition during the denoising process enhances the model's ability to generate materials that meet specific user-defined criteria, making it more versatile and user-friendly.

### Weaknesses
1. The paper does not provide sufficient detail on how the contextual representation of long, detailed text data is fused into the denoising network to generate text-guided variants of baseline models. 
2. The visualization of de novo generated materials lacks a thorough discussion on whether the results align with the given prompts. Additionally, the alignment of generated materials with general textual conditions is not adequately discussed, which is crucial for validating the model's performance.
3. There is a need for a more comprehensive ablation study comparing the effects of long, detailed descriptions versus short prompts on the model's guidance performance. This would help understand the robustness and versatility of the model under different input conditions.

### Questions
1. Could the authors provide more details on how the contextual representation of long, detailed text data is integrated into the denoising network? What specific techniques or architectures are used to achieve this?
2. Could the authors include an ablation study comparing long and short text prompts on the baselines in Table 1 or 2? How would the results differ, and what insights could be gained from such a study?
3. Can the authors provide more detailed visualizations of the generated materials and explicitly discuss how well these results align with the given text prompts? Are there any metrics or qualitative assessments to evaluate this alignment?

### Soundness
3

### Presentation
2

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
The paper focuses on a text-guided diffusion model for periodic material generation. It first designs a diffusion model that can jointly model atom types, coordinates, and lattice structures for periodic materials, then proposes incorporating material structures and properties through text to enhance generation performance. In the experiments, it demonstrates improvements by incorporating text into existing diffusion models, such as SyMat and DiffCSP, followed by showing the superiority of the proposed TGDMat over existing baselines.

### Strengths
- This paper proposes the joint learning fashion for three types of crystal structural information. Text guided denoising network can be the right way to the solution of the problem.
- The paper is well-organized, self-contained with a comprehensive and detailed reference section.
- The design of textual description in the reverse diffusion process is convincing according to the supplementary material.
- The paper provides the computational advantage of integrating text knowledge during reverse diffusion compared to other baseline models.

### Weaknesses
- Motivation should be clarified: (a) Providing guidance in diffusion models for improved generation is important, but it is unclear why text must be used to incorporate such guidance. The guidance information in line 70 could also be modeled as feature vectors, reducing the need for text embedding models, which may not always provide accurate text-based embeddings. Additionally, text-based models may struggle to capture subtle numerical differences. Is there any prior work on using feature vectors for guidance? What are the advantages of using text rather than directly using numerical values or feature vectors? (b) The idea of studying joint diffusion over all three components of crystal structures: the lattices, atom types, and coordinates, by employing a periodic-E(3)-equivariant denoising model, kind of the same as the DiffCSP. Though exploring both crystal structure prediction (CSP) and random generation task (Gen), the text guided denoising network seems to be straightforward by further considering the CSP model architecture. It is not clear how much of this part of work is based on previous research and what is new. 

- Method design should have rationales: The authors applied the diffusion process independently to three variables: lattice (line 210), atom types (line 248), and atom coordinates (line 272). However, in the reverse process, the denoising models use all variables with conditions for noise estimation (line 289). Given that lattice noise is independent of atom types/coordinates and vice versa, is there a reason for not simply using the lattice variable (plus $C_p$) for lattice denoising?

- Experiments should be improved: The paper lacks an evaluation of whether the generated materials meet the text descriptions. Coverage may reflect this to some extent, but it is too general and lacks details on specific properties mentioned in the descriptions. Property statistics are at the distribution level between two sets and lack point-to-point comparisons. Also, the paper lacks the ablation study for the denoising model to demonstrate the individual importance of each component (or the authors could highlight the part if I missed it).

### Questions
- In line 48, to address issues in local message passing, how about using Transformers?
- I am not sure if I missed anything, Figure 2 shows ‘SE(3)-Equivariant GNN model’.. Also, are the diffusion and reverse processes in Figure 2 are correct?
- The paper conducts joint diffusion on lattices, atom types, and coordinates, is there any ablation study for the separately and jointly learning of crystal geometry?
- The CDVAE employs SE(3) equivariant GNNs adapted with periodicity to ensure the invariance of materials. Why not use it and what’s the difference between SE(3) and periodic E(3)-equivariant denoising model backbone?
- Noticing there would be several generated samples in Table 4, how would one select the best sample if the ground truth was not available?

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
This paper presents a text-guided diffusion model for periodic material generation. Compared to the baseline methods, the proposed text-guided approach achieves more valid and stable performance on benchmark datasets.

### Strengths
1. Integrating text information to guide crystal structure generation is a novel practice in the field of material structure generation.
2. From the experimental results, the method proposed in this paper achieves better performance compared to baseline methods. Additionally, the proposed method also demonstrates improved generation efficiency.

### Weaknesses
1. Although combining text information in the field of material generation is an innovative approach, the text-guided diffusion model is not a new model framework. Therefore, the contribution of this paper is limited from the perspective of architectural innovation.
2. TGDMat(Short) does not always outperform baseline methods, and the improvement of TGDMat(Long) over baseline methods is also marginal. This indicates that the model's results are heavily dependent on how the text information is constructed, and richer textual information can lead to slightly better outcomes than the baseline.
3. As metrics commonly used to evaluate generative performance, the authors should consider including diversity and novelty as additional metrics for comparison.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
