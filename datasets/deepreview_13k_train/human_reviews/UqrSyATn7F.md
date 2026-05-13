# Tokenizing 3D Molecule Structure with Quantized Spherical Coordinates

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
The application of language models (LMs) to molecular structure generation using line notations such as SMILES and SELFIES has been well-established in the field of cheminformatics. 
However, extending these models to generate 3D molecular structures presents significant challenges. Two primary obstacles emerge: (1) the difficulty in designing a 3D line notation that ensures SE(3)-invariant atomic coordinates, and (2) the non-trivial task of tokenizing continuous coordinates for use in LMs, which inherently require discrete inputs.
To address these challenges, we propose Mol-StrucTok, a novel method for tokenizing 3D molecular structures. Our approach comprises two key innovations:
(1) We design a line notation for 3D molecules by extracting local atomic coordinates in a spherical coordinate system. This notation builds upon existing 2D line notations and remains agnostic to their specific forms, ensuring compatibility with various molecular representation schemes.
(2) We employ a Vector Quantized Variational Autoencoder (VQ-VAE) to tokenize these coordinates, treating them as generation descriptors. To further enhance the representation, we incorporate neighborhood bond lengths and bond angles as understanding descriptors.
Leveraging this tokenization framework, we train a GPT-2 style model for 3D molecular generation tasks. Results demonstrate strong performance with significantly faster generation speeds and competitive chemical stability compared to previous methods. 
Further, by integrating our learned discrete representations into Graphormer model for property prediction on QM9 dataset, Mol-StrucTok reveals consistent improvements across various molecular properties, underscoring the versatility and robustness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on the task of 3D molecule generation with language models (LMs). The main step is to convert 3D molecules to sequences of discrete tokens. The authors first use SMILES (or SELFIES) to convert a molecule's atom and bond information to a sequence. They then use spherical coordinates and VQ-VAE to convert 3D information to discrete tokens. After obtaining these 3D molecule sequences, they train a GPT-style model for molecule generation by next-token-prediction. The model is evaluated on the random generation and conditional generation tasks.

### Strengths
1. This paper is well-written and easy to follow, with clear and informative tables and figures. 
2. The proposed method performs well, especially on the conditional generation task.
3. The ablation study is thorough and provides useful insights.

### Weaknesses
1. The proposed method is quite similar to existing methods, such as FoldSeek and FoldToken. Specifically, similar to the SE(3)-invariant spherical coordinates here, FoldSeek also uses distances and angles computed based on reference nodes as SE(3)-invariant representations. In addition, Furthermore, both methods employ VQ-VAE to learn discrete tokens. These overlapping components limit the novelty of this work.
2. About the datasets: the proposed method is only evaluated on QM9 dataset, which includes only small molecules. It will be better to evaluate on larger molecules, such as geom-drug dataset.
3. More LM-based baseline methods should be included and compared, such as Geo2Seq and BindGPT.
4. Further analysis and potential visualizations of the learned structural alphabet, for example, which types of local structures can be mapped to the same code? Refer to Figure S2 and S3 of FoldSeek.

Other questions:
1. line 52: SE(3) invariance is invariance under rotation and translation, but not reflection
2. What is the model size?

### Questions
See weaknesses

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
4

### Summary
The authors introduce a novel method for tokenizing 3D molecular structures. The authors design a 2D line notation for 3D molecules by extracting the local atomic spherical system, then employ VQ-VAE to tokenize upon this 2D line notation to tokenize the spherical coordinates. Results show the competitive performance compared to several SOTA methods.

### Strengths
The combination of spherical line notation with vector quantization enables language models to process complex 3D data, which is challenging to discretize. This approach stands out from traditional graph-based or continuous-coordinate models by providing a discrete representation for language models without losing SE(3)-invariant information. Particularly, the augmented tokens incorporate both generation and understanding descriptors, including local spherical coordinates, bond lengths, and angles, allowing a better capture of molecular topology and spatial arrangements.

### Weaknesses
### Major
The authors should clarify the rationale behind selecting exactly four neighbors for the atomic descriptor and explicitly address how the descriptor $\mathbf{z}_i$ is defined for atoms with fewer than four neighbors. This is essential, as molecules with varying coordination environments will likely have different numbers of neighbors, impacting the generality of the descriptor across datasets. The arbitrary choice of four neighbors without a clear justification or a strategy for handling atoms with fewer neighbors raises concerns about the robustness of the method, particularly for molecules containing atoms with coordination numbers other than four. The lack of a principled approach to this issue undermines the claim that the method can effectively capture the local environment of diverse molecular structures. Furthermore, the impact of this choice on the performance of the model should be analyzed and discussed.

### Minor
1. The paper’s notations are somewhat inconsistent and could benefit from simplification and unification. For instance, symbols like $\mathcal M$ are used only within specific sections, such as Section 3.1, and do not appear elsewhere. Additionally, the notation in Appendix C is different from that in Section 3.1. A more streamlined notation would improve readability and coherence across sections.
2. Line 177, the phrase should be rephrased as "we tokenized the molecular graph into a sequence of atom tokens $\mathbb A$ and non-atom tokens $\mathbb B$".
3. In Line 248 and Line 268, references are made to "Section X" and "Figure X," which seem placeholders. These should be updated with specific section and figure numbers
4. Line 239, "Inspired by previous works" is ambiguous. The authors should specify which studies or methods they are referring to here.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors express 3D structure using spherical coordinates, then tokenize them with a VQ-VAE. The tokens are then used for training a GPT-2 model for 3D molecular generation tasks. They also use the discrete representations in a Graphormer model for property prediction on QM9, and observe consistent improvements across various molecular properties.

### Strengths
1. The authors conduct an extensive set of experiments. They measure validity+uniqueness of generated molecules with different bond assignment methods, perform PoseBusters tests, evaluate quantum mechanical properties, and measure MAE for QM9 property prediction. They achieve state-of-the-art results in most experiments.
2. They also perform additional analysis regarding the inference speed of their method and the effect of the generation temperature on balancing quality and diversity.

### Weaknesses
1. This is a hand-crafted tokenization scheme and should be compared to other tokenizers (e.g. BPE-based tokenizers), not just diffusion models and MPNN-based methods. It's unclear if the performance gains are due to the spherical coordinate representation or the specific tokenization method. A more thorough comparison with established tokenization techniques is needed to isolate the impact of the proposed approach.
2. It may also be helpful to compare with structures expressed in other coordinate systems. I'd imagine that without SE(3) invariance there would be a wider range of possible tokenized sequences, making it harder for the GPT-2 model to learn. The current choice of spherical coordinates, while convenient, lacks a clear justification against other coordinate systems and their potential impact on the learning process. The authors should explore how different coordinate representations affect the complexity of the learned token sequences and the overall performance.

### Questions
1. To the best of my knowledge, PoseBusters has an energy ratio test, which tends to be very difficult to satisfy. Have you tried on that test? I think that test would be more meaningful since most methods already perform very well on the tests you demonstrated in Table 2.

2. What's the motivation for a purely MLP-based quantized auto-encoder architecture? Most other autoencoder-based tokenizers use some form of GNN or sequence model. What are the tradeoffs between element-wise discretization and discretization with message propagation?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a novel language model based 3D molecule generation framework. Novel spherical coordinate based 3D line notation method combined with VQ-VAE model is adopted to tokenize 3D molecules, and GPT-2 models are applied to this tokenization framework. Benchmark experiments are conducted to show the promising performance of the proposed method.

### Strengths
Originality:  
This work makes a good originality contribution of  proposing a novel 3D molecule tokenization method that is applicable for language models.

Quality:  
This work presents sufficient theoretic analysis and proofs for the proposed 3D tokenization method, and benchmark experiments are conducted to demonstrate the promising performance.

Clarity:  
The writing of this paper is fairly good. The paper gives sufficient description to help readers understand the key pipeline and steps of 3D molecule generation.

Significance:  
The proposed method is useful in leveraging the power of large language models to the generation and modeling of complicated 3D molecule structures.

### Weaknesses
(1) Some important methods details are not clearly clarified or presented. Authors are encouraged to add explanations to the following questions: 
- How the order of atom tokens in equation (2) is decided? By BFS or DFS traverse algorithm on 2D topology graphs?
- The $x_i$ in line 266 is actually $g_i$ in equation (7)?
- Why the sign of torsion angle $sign(\varphi_i)$ appears in the generation descriptor of equation (7) but not in the combined descriptor of equation (9)?
- Why local atomic environment (line 266-267) is needed? Can authors discuss the negative impacts of not including it and conduct ablation studies if possible?

(2) In benchmark experiments, an important baseline Geo2Seq [1] (it also proposes a spherical coordinate based 3D molecule tokenization framework) is not presented and compared. Particularly, Geo2Seq has higher molecule stability than authors' method, so more discussion about differences and advantages over Geo2Seq is needed.

(3) VQ-VAE based vector quantization is applied to atom descriptor in equation (9) to form the final generation target. A natural question is what is the advantages of VQ-VAE over simple discretization (i.e., map floating numbers to pre-split bins, e.g., 0-30, 30-60, 60-90, ... for angles) ? Authors are encouraged to discuss different possible quantization methods and conduct ablation experiments to justify the advantages of VQ-VAE.

### Questions
See Weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
2
