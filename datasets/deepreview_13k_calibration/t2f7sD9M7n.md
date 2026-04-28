# Learning the Hamiltonian of Disordered Materials with Equivariant Graph Networks

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Graph neural networks (GNNs) have shown promise in learning the ground-state electronic properties of molecules and crystalline materials, subverting computationally intensive density functional theory (DFT) calculations. Materials with structural disorder, however, are more challenging to learn as they exhibit higher complexity and a more extensive palette of local atomic environments, all of which require large (10+ Angstrom) cells to be accurately captured. In this work, we adapt efficient equivariant GNN approaches to learn disordered materials' electronic properties, represented by the Hamiltonian matrix ($\mathbf{H}$). Since creating a large graph corresponding to the whole structure of interest would be computationally prohibitive, we introduce an 'augmented partitioning' approach in which the graph is sliced into multiple partitions, each augmented with masked virtual nodes and edges. This method maintains correct atomic neighborhoods within a single message passing layer, allowing for the network to learn the electronic properties of amorphous HfO$_2$ materials with 3,000 nodes (atoms), 500,000+ edges, and $\sim$28 million orbital interactions (non-zero entries of $\mathbf{H}$).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents an efficient adaptation of equivariant graph neural networks for learning the electronic properties of disordered materials. It introduces an 'augmented partitioning' approach that divides large structures into smaller, manageable graphs, each enhanced with masked virtual nodes and edges while maintaining correct atomic neighborhoods during message passing. This method enables the effective learning of electronic properties, providing a scalable alternative to computationally intensive density functional theory (DFT) calculations.

### Strengths
The paper extends the application of equivariant neural networks to a challenging scientific problem that traditionally requires significant computational resources. It offers a specific strategy to address the computational cost and enhance the scalability of the implemented equivariant neural networks.

### Weaknesses
 - While the proposed methods are promising for the specific task addressed, they appear to be limited to this particular problem domain. I suggest the authors apply their proposed graph partitioning methods to other materials-related challenges beyond the scope of this paper. For example, exploring applications in molecular modeling, crystalline structures, or other materials science problems would significantly broaden the impact of the work. This could be complemented by additional practical evaluations, such as comparing the method’s performance on various datasets or against other state-of-the-art approaches. Including metrics such as computational efficiency and accuracy in these broader contexts would provide a stronger empirical basis for the proposed method. 

- I think this paper is not theoretically solid enough to meet the standards expected at this conference. The contributions are modest and mainly focused on a graph partitioning approach, which lacks a strong theoretical foundation. To enhance the work, I recommend the authors further develop the theoretical framework, particularly by providing more rigorous analysis or proofs regarding the scalability or performance guarantees of their approach.

### Questions
- The subject appears to be using an outdated template (ICLR 2024). 
- Please address my concerns in the weakness section.

### Soundness
3

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
The paper aims to develop a deep learning model, specifically leveraging Graph Neural Networks (GNNs), that can predict the ground-state Hamiltonian matrix (a representation of electronic properties) of disordered materials, which efficiently predicting the electronic properties of disordered materials compared to the traditional methods, such as Density Functional Theory (DFT). What’s more, this work lies in adapting equivariant GNNs and introducing an augmented partitioning approach to efficiently scale the model for large disordered systems.

### Strengths
1.The paper applies the equivariant GNNs combined with augmented partitioning is a significant methodological advancement. It allows the model to scale to large disordered systems, which is a critical capability in material science applications.
2.The authors provide an extensive suite of experiments that test the model’s accuracy, scalability, and generalization ability. The ablation studies in particular strengthen the claim that virtual nodes are essential for capturing disordered materials' electronic properties.
3.This work holds potential for practical applications, as it reduces the dependence on computationally intensive DFT simulations. The approach could pave the way for faster exploration of disordered materials in fields like electronics and energy storage.

### Weaknesses
1.The paper provides empirical discussions regarding the connectivity and choice of cutoff radius, it does not delve deeply into the theoretical basis behind these choices. Specifically, the paper lacks a rigorous justification for how the chosen cutoff radius relates to the underlying physics of the disordered materials being studied. While the authors discuss convergence of eigenvalue spectra and prediction accuracy, they do not connect these observations to the fundamental electronic interactions that dictate the Hamiltonian matrix elements. A more in-depth analysis of how the cutoff radius affects the locality of interactions and the representation of long-range effects would be beneficial.
2. The paper lacks comprehensive experiments to illustrate the specific capabilities and limitations of the proposed GNN architecture in predicting Hamiltonian matrix elements across a range of disordered materials. The empirical evaluation is limited in scope, primarily focusing on a single material system. Additional benchmarks comparing the model’s performance on Hamiltonian matrix predictions with different materials or conditions would strengthen the empirical foundation and highlight the robustness of the GNN approach for diverse applications. It is unclear how the model will generalize to materials with different bonding characteristics, degrees of disorder, or elemental compositions.

### Questions
1. Can additional experiments be conducted on other datasets? For instance, it would be beneficial to see the model tested on larger graph datasets that necessitate a higher cutoff radius. Are there any practical limitations to testing on much larger systems that the authors should discuss?

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
5

### Summary
This paper presents an approach to learn the ground-state Hamiltonian of disordered materials using equivariant graph neural networks (GNNs). The key methodological contribution is an "augmented partitioning" scheme that aims to handle large atomic systems by slicing the graph into multiple partitions and adding virtual nodes/edges at boundaries. The authors demonstrate their method on amorphous HfO2 with 3,000 atoms, claiming acceptable accuracy compared to DFT calculations.

### Strengths
The main contribution lies in the augmented partitioning scheme that enables the application of equivariant GNNs to large-scale atomic systems. The work demonstrates systematic validation through comprehensive ablation studies and detailed analysis of computational performance, supported by comparison with DFT calculations on HfO$_2$ systems. The technical presentation is well-structured, with clear mathematical formulations and thorough documentation of the computational workflow. From a practical perspective, the work provides a solution for electronic structure prediction of large-scale systems (3000+ atoms), offering significant computational savings compared to traditional DFT calculations.

### Weaknesses
The paper has several fundamental methodological issues. The most critical concern is that the proposed partitioning scheme breaks the hierarchical nature of Message Passing Neural Networks. While standard MPNNs use multiple MP layers to incrementally increase the receptive field, this method's single-layer virtual node approach artificially truncates information flow at partition boundaries, compromising the network's ability to capture long-range interactions. The authors attempt to justify this limitation by invoking the "near-sightedness" of the Hamiltonian, but provide no rigorous analysis of how Hamiltonian matrix elements Hij are affected by distant atoms or how the neglected higher-order interactions might impact accuracy. The validation is severely limited, with only three structures of a perfect stoichiometric HfO2 being tested. In real materials applications, amorphous HfO2 often contains various defects such as oxygen vacancies and the Hf:O ratio can deviate from the ideal 1:2 stoichiometry. The absence of these realistic material features in the training data raises serious concerns about the method's practical utility. Without testing on structures with different stoichiometries, defects, and degrees of disorder, it's impossible to assess whether this approach can truly address real computational challenges in materials science. Furthermore, the authors' justification for single-layer message passing reveals a critical physical limitation. Single-layer MP can only capture pairwise (2-body) interactions between atoms, effectively modeling Hij as a sum of independent 2-body terms with neighboring atoms. However, in reality, Hij should depend on the collective electronic environment through many-body effects, which are particularly important in disordered systems. Multiple MP layers are necessary to capture these higher-order correlations. Therefore, the authors' argument that single-layer MP is sufficient because "Hij decays with distance" misses the fundamental physics: while Hij may decay spatially, its value for nearby atoms depends on complex many-body correlations that cannot be captured by pairwise interactions alone. This limitation could significantly impact the model's accuracy, especially for disordered systems. The authors' analysis of Hamiltonian locality is also incomplete and potentially misleading. While the authors demonstrated that Hij decays with increasing interatomic distance rij, this only establishes the sparsity pattern of the Hamiltonian matrix - a well-known property. However, they failed to address the more fundamental question of locality: whether the significant Hamiltonian matrix elements (those between nearby atoms i and j) can be accurately determined using only local atomic environments. To properly establish the locality approximation, the authors need to demonstrate that Hij can be accurately predicted using only local structural information. Specifically, for atom pairs (i,j) where rij is small and Hij is significant, they should systematically perturb the positions of distant atoms k through various mechanisms, such as atomic displacements, introduction of defects, and atomic substitutions, then quantify the response of Hij to these perturbations, and demonstrate that this response decays rapidly with increasing distances |rk-ri| and |rk-rj|. Simply showing that Hij becomes small for large rij is insufficient - this merely establishes matrix sparsity. The crucial physical question is whether the non-zero elements of the Hamiltonian can be determined from local structural information alone. This distinction is particularly important for amorphous systems, where local structural disorder could potentially lead to more complex non-local effects.

### Questions
1.  Standard Message Passing Neural Networks (MPNNs) are designed to capture hierarchical structural information through multiple layers, where each additional MP layer extends the receptive field and allows nodes to aggregate information from more distant neighbors. The partitioning scheme presented in this paper fundamentally breaks this mechanism by using only single-layer MP with virtual nodes at boundaries. The authors shoule provided more  justification for using single-layer MP.  they should provide quantitative analysis demonstrating how Hamiltonian matrix elements Hij are affected by atoms at different distances, and how this relates to their architectural choices? This should include comparison with full multi-layer MP on smaller systems.

2. The work emphasizes parallel training through system partitioning to handle large disordered systems. However, if the locality of the Hamiltonian truly holds as claimed, then a model trained on small cells should be able to generalize to larger disordered systems, as the local atomic environments would be similar. In this case, standard GNN approaches without partitioning would remain valid.  The authors should provided quantitative comparison between their method  and a standard GNN model trained on small cells and directly applied to large systems .

3. The paper only presents the validation with perfect stoichiometric HfO$_2$ structures, which is far from realistic material conditions. Could the authors demonstrate how their method performs on structures wit Hf or O vacancies, varying Hf:O ratio.

4. The reported accuracy of 5.87 meV is significantly higher than the sub-meV accuracy achieved by state-of-the-art models in electronicHamiltonian prediction. The authors should either justify why this level of accuracy is sufficient, or provide direct comparisons with other methods (e.g., DeepH, HamGNN, etc.) on benchmark systems on small systems. If the accuracy loss is a trade-off for handling larger systems, this limitation should be explicitly discussed and quantified.

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
3

### Summary
This paper presents an equivariant graph neural network (GNN) method based on EquiformerV2 to predict disordered materials’ ground state Hamiltonian matrix $\mathbf{H}$. An augmented partitioning approach is used to partition the large, highly connected graph, addressing the computational cost issue. The method is tested on an $\ce{H2O}$ benchmark and a custom dataset of large-scale amorphous $\ce{HfO2}$, showing accuracy and computational efficiency improvements. The effects of graph construction (cutoff radius and connectivity), model hyperparameters (virtual nodes, number of layers, etc.), and the augmented partitioning approach are investigated.

### Strengths
- This work tackles an important topic in materials science. Predicting the Hamiltonian to provide an accurate initial guess could speed up DFT calculations, thus improving the efficiency of computational materials modeling.
- The proposed partitioning approach leads to a considerable reduction in computational cost.

### Weaknesses
 - The novelty and contributions should be better articulated. Currently, the Background and Related Works section mainly describes the physics. What past works this work is built upon and what are the new things should be made clear. Perhaps listing the contributions in the Introduction could be helpful.
- Some mathematical notations are unclear or confusing. (1) Scalars, vectors, and matrices should be distinguished using, e.g., boldface. (2) $N_A$ denoting the number of atoms could be confused with the Avogadro constant.

- The proposed methods are mainly tested on the $\ce{HfO2}$ dataset, which does not convincingly show the generalizability to other disordered materials systems. Would the authors consider adding other test cases, or discussing the applicability and limitations?
- Sec 3.3 says “…generated a dataset of only three unique a-$\ce{HfO2}$ structures for training, validation, and testing”. How is “unique” defined? Could there be significant overlap (e.g., same local environments) between these three structures?
- How is the “near-sightedness” of $\mathbf{H}$ defined and supported? Does this hold strictly or approximately in theory? 
- What metric is used to obtain the 0.87% accuracy, is it MAE? If so, is the mean value calculated over all eigenvalues? Given the large difference of magnitude between eigenvalues of $\mathbf{H}$, I’m not sure whether this is a reasonable metric.

### Questions
- The proposed methods are mainly tested on the $\ce{HfO2}$ dataset, which does not convincingly show the generalizability to other disordered materials systems. Would the authors consider adding other test cases, or discussing the applicability and limitations?
- Sec 3.3 says “…generated a dataset of only three unique a-$\ce{HfO2}$ structures for training, validation, and testing”. How is “unique” defined? Could there be significant overlap (e.g., same local environments) between these three structures?
- How is the “near-sightedness” of $\mathbf{H}$ defined and supported? Does this hold strictly or approximately in theory? 
- What metric is used to obtain the 0.87% accuracy, is it MAE? If so, is the mean value calculated over all eigenvalues? Given the large difference of magnitude between eigenvalues of $\mathbf{H}$, I’m not sure whether this is a reasonable metric.

### Soundness
3

### Presentation
3

### Contribution
3
