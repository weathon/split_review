# POLYATOMIC COMPLEXES: A TOPOLOGICALLY INFORMED LEARNING REPRESENTATION FOR ATOMISTIC SYSTEMS

- Decision: Reject
- Avg Score: 4.17
- Scores: 6, 3, 5, 3, 5, 3

## Abstract
Developing robust representations of chemical structures that enable models to learn topological inductive biases is challenging. In this manuscript, we present a representation of atomistic systems. We begin by proving that our representation satisfies all structural, geometric, efficiency, and generalizability constraints. Afterward, we provide a general algorithm to encode any atomistic system. Finally, we report performance comparable to state-of-the-art methods on numerous tasks. We open-source all code and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a characterization method for polyatomic complexes that meets more properties compared to existing methods, such as Invariances, continuity and differentiability, and generality, generalizability.
It achieves strong results across multiple benchmarks.

### Strengths
1). Theoretical proof and experimental validation are sufficient.

### Weaknesses
1). The readability of the paper, including its organization and tables, could be improved. Could you provide more explanation for Figure 1?

2). Could you provide more explanations of the datasets and metrics used in the benchmarks section of the experiments? It might be a bit difficult for those without relevant background to understand.

### Questions
Refer to the questions in the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a new representation (polyatomic complexes) for chemical systems, aimed at capturing topological properties of molecules. In particular, the representation 'stitches' together representations of different neutrons, protons and electrons. The authors prove that polyatomic complexes satisfy (rotational, translational, permutational) invariances, continuity (with respect to atomic positions), generalizability (in the sense of being well-defined for arbitrary chemical compounds) and topological accuracy (upto electronic structure).
The authors perform experiments on the photoswitches, ESOL, FreeSolv and Matbench JDFT2D dataset with two variants of their method (Fast Complex and Deep Complex), and find comparable performance to state-of-the-art methods.

My main concerns are the readability of the paper together with the lack of convincing empirical results (which the authors also admit to). It would be nice to come up with a task where this representation is provably better than existing methods.

### Strengths
- The idea of polyatomic complexes for describing chemical systems is novel as far as I know. I think there are some good ideas in this paper, and it would be nice to improve the writing to flesh them out a bit more.
- The choice of datasets and baselines is quite comprehensive and interesting. I really appreciate the authors' honesty here in showing all results even when their representation is not the best-performing.

### Weaknesses
 - This paper is quite difficult to read (but this might also be my lack of familiarity with the notation). It is hard to understand what exactly the representation corresponds to. Some more figures describing the construction of polyatomic complexes could help. Specifically, the connection between the abstract mathematical definitions and the concrete implementation is unclear. For instance, how exactly are the 'stitched' representations of neutrons, protons, and electrons combined into a single tensor? The paper would benefit from a more detailed, step-by-step explanation of this process, perhaps with a visual example showing how a simple molecule like water is represented.
- The formatting could be improved significantly. For example, Figure 1 is barely readable due to small text, and there is extra whitespace throughout the paper (eg. "( 2.12)" on page 3 and so forth.) The inconsistent formatting makes it harder to follow the technical details and detracts from the overall presentation. The paper would benefit from a thorough pass to eliminate all unnecessary whitespace and ensure consistent font sizes and spacing.
- The modeling assumption of an electron as a single sphere is quite chemically inaccurate (especially for delocalized systems). It would be good for the authors to discuss this weakness and how to improve this aspect of their representation. Representing electrons as simple spheres fails to capture the complex spatial distribution of electron density, particularly in molecules with pi systems or lone pairs. This simplification could significantly limit the representation's ability to accurately model electronic properties and reactivity. A discussion of how to incorporate more realistic electron representations, such as using atomic orbitals or electron density maps, is needed.
- Experimental results are not super convincing, given that the RMSE of their method is often much higher than state-of-the-art methods. The authors do mention this as a weakness, but I would like to see how improvements can be made. The paper needs a more thorough analysis of why the proposed representation underperforms compared to existing methods. It is not sufficient to simply acknowledge the lower performance; a detailed investigation into the limitations of the representation and how they contribute to the observed errors is necessary. This should include a discussion of the specific types of molecules or properties where the method struggles most.

### Questions
- 'Generalizability': I felt that this property could be differently named, in order to avoid confusion with its definition in the ML literature. Perhaps, 'completeness' captures the essence of the property better?
- e3nn is not a chemical representation, it is a framework for training E(3)-equivariant neural networks (which may be used to learn representations of chemical systems).
- Section 3.1: "Since we believe the values to be missing at random, we utilize mean imputation, instead of discarding experimental data". This is a big assumption, do the results change significantly if missing values are removed?
- Please highlight your method in all tables for clarity.
- What exactly is the role of the random matrix denoting proton-electron interactions? Are these forces/energies learned?
- Some of the definitions seem arbitrary. eg. where does the constant 2.8 fm come from in Definition 2.1?

### Soundness
3

### Presentation
2

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
The paper proposes a novel way of representing molecules and materials by incorporating topological information through a series of cell complexes that satisfy all structural, geometric, efficiency, and generalizability.

### Strengths
- A novel way of constructing a representation for molecules satisfying key ingredients
- Incorporating structural, topological information to construct representation

### Weaknesses
 - The paper's writing lacks clarity, making it difficult to follow.
- The latter part of the introduction, which describes and compares various representation approaches, could be more effectively presented in a table. This would also help clarify where the proposed method fits within current methods, with detailed explanations that can be moved to an appendix.
- Including a subsection on notation would improve readability by clearly defining the meaning of each symbol used.
- Although the representation meets vital criteria, it still underperforms in benchmarks (e.g., ESOL and FreeSolv). Could this be due to limitations in the current method's ability to leverage higher-level topological information from this representation, or are there other underlying reasons?

### Questions
- Could the authors discuss the time complexity of the proposed algorithm for constructing the complex, along with an ablation study? This would help clarify the potential trade-offs associated with the method.
- During the construction of the atom complex, is there a way to incorporate neutron and proton arrangements in energy levels (similar to the nuclear shell model)?
- Regarding the uniqueness of the representation, can the method distinguish between chiral molecules or stereoisomers of the same molecule by obtaining distinct representations?
- Given that the method represents an atom complex by decomposing electrons, neutrons, and protons and then reconstructing the molecule, how does it handle bond formation between electron-donating and electron-accepting atoms, where the atoms may carry a charge? or in general, representing a charged molecule?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method using CW-complex to build representations for atomistic systems. It consists two stages: in the first stage the CW complex representation is built for single atom based on proton, neutron and electrons; in the second stage, the CW complex representation is built for multiple atoms using the representations from single atoms. Numerical experiments have been performed on multiple benchmarks and compared with other baselines.

### Strengths
- The idea of building representation from topological information is novel.
- Numerical experiments have been done and compared comprehensively

### Weaknesses
 - Some statements related to relevant works have factual incorrectness. For example,
    - In line 142-146, in the description of ACE, the computational cost is not N! for permutations, and (J N) for J-neighbors. I suggest the authors to check the original ACE paper (Ralf Drautz, PRB 2019). The permutation invariant within atoms of the same element is achieved by simply summing over basis function of neighbor displacement, and by using clusters it also circumvents the (J N) summation.
    - In line 391, the authors state that the electromagnetic force, strong nuclear force and weak nuclear force hold the atom together, which is not a physically correct statement.
- The construction with proton, neutron, and electron is not very physically meaningful for the tasks of interests. This is just to obtain a representation for a single atom, which basically includes only the element and isotope information. A direct embedding on the element type will be simpler and achieve the same goal and learnable. The use of proton, neutron, and electron counts to generate a CW complex seems unnecessarily complex for capturing basic elemental information, especially since the tasks focus on molecular properties where electronic structure and bonding are more relevant than nuclear composition. The representation essentially boils down to a unique identifier for each isotope, which could be achieved more efficiently.
- In the comparison with other methods, this method does not show impressive results. E.g. on benchmarks like ESOL, FreeSolv, ChEMBL, the error is much worse than SMILES and SELFIES. The performance gap is significant, suggesting that the topological representation, as implemented, does not capture the relevant chemical information for these tasks as effectively as simpler string-based representations. The lack of competitive results raises concerns about the practical utility of the proposed approach in its current form.

### Questions
It is not very clear to me how the CW complex is implemented. The authors should clarify the form of the final representation (e.g. scalar/vector/tensor/graph, what is the dimension) which is input to the regression model.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper  developed a new molecular representation encoding atomistic systems called polyatomic complexes, which constructs mathematical models by CW complexes and connects different elementary particles through gluing maps.

Besides, this paper expanded the criteria for good molecular representations and demonstrated that the proposed method satisfies all these constrains.

The authors also demonstrated the performance of this representation on several benchmark datasets in chemistry and materials science.

### Strengths
This paper demonstrates strong originality at the theoretical level, introducing a method grounded in a rigorous mathematical model that meets stringent constraints.

### Weaknesses
The method presented in this paper exhibits weak predictive accuracy across multiple benchmark datasets. 
Although the polyatomic complexes method characterizes at the electronic level, its performance is still less than that of the molecular level methods, e.g. SMILES and SELFIES.


 The method's practical implementation appears to make significant simplifications and approximations, potentially undermining the theoretical advantages. While the theoretical framework is strong, the practical application seems to sacrifice key aspects to achieve computational efficiency. This raises concerns that the method, in its current form, may not fully realize the potential suggested by the theory. For example, the use of a Tanimoto kernel may not be optimal for capturing the nuances of the proposed representation, which could explain the lower predictive accuracy.


We notice that the authors have added more stringent constraints of molecular representations based on [1], such as Topological Accuracy, Long-range interactions and Chemical and Physical Informedness. We are skeptical about the necessity of these additional criteria.  Molecular representation is a lossy compression of information, and expecting a perfect representation of all properties may be challenging. Perhaps focusing on certain aspects while neglecting others could be more helpful for specific tasks. For example, electronic structure information and topological accuracy may not be very helpful in predicting macroscopic properties such as solubility, which is also experimentally demonstrated in Table2 and Table 3. Have the authors discussed why these criteria are added and are these additional criteria really useful?

### Questions
- Time cost of computing representations compared with other methods is not provided to evaluate the **efficiency** constrain.
- The theory behind the model is excellent, but the practical implementation employs many simplifications and approximations to save computational efficiency, raising concerns that it may not achieve the capabilities claimed in theory.

- We notice that the authors have added more stringent constraints of molecular representations based on [1], such as Topological Accuracy, Long-range interactions and Chemical and Physical Informedness. We are skeptical about the necessity of these additional criteria.  Molecular representation is a lossy compression of information, and expecting a perfect representation of all properties may be challenging. Perhaps focusing on certain aspects while neglecting others could be more helpful for specific tasks. For example, electronic structure information and topological accuracy may not be very helpful in predicting macroscopic properties such as solubility, which is also experimentally demonstrated in Table2 and Table 3. Have the authors discussed why these criteria are added and are these additional criteria really useful?



[1] M. F. Langer, A. Goeßmann, and M. Rupp, “Representations of molecules and materials for interpolation of quantum-mechanical simulations via machine learning,” npj Comput Mater, vol. 8, no. 1, p. 41, Mar. 2022, doi: 10.1038/s41524-022-00721-x.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new representation for chemical structures, designed to offer a more robust alternative to existing methods such as SMILES and fingerprints. By incorporating the physical characteristics of the target material, the proposed representation seems to demonstrate several desirable features that are critical for an effective chemical representation.

### Strengths
S1. The author asserts that the proposed representation satisfies several key criteria, including invariance, uniqueness, continuity and differentiability, generalizability, efficiency, topological accuracy, long-range interaction handling, and incorporation of chemical and physical insights.

S2. These claims are supported, at least partially, by mathematical discussions.

### Weaknesses
The paper appears to be in a draft stage, possibly intended to gather feedback before submitting to another conference or journal. This is inferred from several issues:

W1: The overall structure, figures, and explanations appear incomplete. For instance, the contents and sentences in Figure 1 are too small and difficult to understand. Section 2 lacks sufficient explanations connecting the lemmas and theorems, making it challenging to follow the argument. The description of the algorithm in Section 2.3 is brief and does not fully clarify the logic. Additionally, Figure 2 is uninformative and takes up space that could be better used to elaborate on the explanation and discussion.

W2: The experiments do not convincingly demonstrate the effectiveness or utility of the new representation. Across most datasets, the performance of the proposed representation is suboptimal, failing to justify its usefulness. The experiments focus solely on property prediction performance. It would be more informative to include comparisons of computational cost, assessments of generalizability, evaluations of long-range interaction capabilities against machine learning interatomic potential (MLIP) models, and tests on datasets where other representations struggle due to issues such as lack of uniqueness. In such cases, MLIP models could serve as a meaningful baseline due to their ability to represent diverse materials.

W3:  Due to the suboptimal layout, the sections on experiments and discussions (Sections 3 and 4) are very brief and lack insightful analysis that could demonstrate the effectiveness of the new representation.

### Questions
W2. What new tasks could be uniquely enabled by the proposed representation, and how do the authors plan to validate its performance in these tasks?

For additional concerns, please refer to the "Weaknesses" section above.

### Soundness
2

### Presentation
1

### Contribution
2
