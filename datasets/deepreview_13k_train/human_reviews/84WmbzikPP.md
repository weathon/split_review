# Stiefel Flow Matching for Moment-Constrained Structure Elucidation

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Molecular structure elucidation is a critical step in understanding chemical phenomena, with applications to identifying molecules in natural products, lab syntheses, forensic samples, and the interstellar medium.
We consider the task of elucidating a molecule's 3D structure from only its molecular formula and moments of inertia, motivated by the ability of rotational spectroscopy to precisely measure these moments.
While existing generative models can conditionally sample 3D structures with approximately correct moments, this soft conditioning fails to leverage the many digits of precision afforded by experimental rotational spectroscopy.
To address this, we first show that the space of $n$-atom point clouds with a fixed set of moments of inertia is embedded in the Stiefel manifold $\textrm{St}(n, 4)$.
We then propose Stiefel flow matching as a generative model for elucidating 3D structure under exact moment constraints.
Additionally, we learn simpler and shorter flows by finding approximate solutions for optimal transport on the Stiefel manifold.
Empirically, Stiefel flow matching achieves higher success rates and faster sampling than Euclidean diffusion models, even on high-dimensional manifolds corresponding to large molecules in the GEOM dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the molecular structure elucidation problem using a generative approach. This task involves inferring a molecule's 3D structure from its molecular formula and moments of inertia. Traditional generative models conditioned on moments of inertia fail to leverage the precision offered by rotational spectroscopy, which measures moments with high accuracy. The paper introduces Stiefel Flow Matching, a generative model that operates on the Stiefel manifold, where the set of point clouds with fixed moments of inertia is embedded. Empirical results demonstrate higher accuracy and efficiency in generating 3D molecular structures compared to Euclidean diffusion models.

### Strengths
- As far as I can tell, the approach used in the paper of embedding the molecular structure elucidation task in the Stiefel manifold is original. This approach leverages manifold geometry to respect exact moment constraints, improving over traditional Euclidean diffusion models. 
- In general, the paper is written and formatted very well. I appreciate the consistent and well-written formalisms and figures, making the otherwise quite abstract paper well-readable. Moreover, the formalisms support the methodology of the work well. 
- The results show some performance improvements, particularly in maintaining moment constraints and reducing sampling cost.
- This work has potential applications in chemistry, pharmacology, and materials science, where precise molecular structures are essential. By leveraging constraints from rotational spectroscopy, this model could significantly improve the accuracy of 3D structure predictions for unknown molecules.

### Weaknesses
 - Most obviously, for larger datasets like GEOM, the model struggles with validity and stability of generated structures, indicating possible underfitting issues. I think some more concrete suggestions on how to improve these issues would be greatly beneficial.
- Some connections to recent approaches to molecular generation with discrete flow matching are missing in the paper. Even though these problems consider a slightly different task as they operate on discrete domains, some intuition of why the authors' approach does not involve discrete dynamics/generation at all would be useful, as it intuitively would be beneficial for this task. 
- As far as I understand it, some of the alignment and validation steps rely on heuristic checks. Some reflection on how task-specific these are, or some intuition behind the thereby introduced bias would be useful.
- While the authors provide some baseline comparisons, they are somewhat limited and some discussion on how Stiefel Flow Matching specifically outperforms or complements existing diffusion models on continuous or Riemannian spaces could benefit the paper. Moreover, adding more experimental results would aid in this too.
- The paper is longer than 9 pages.

### Questions
- The model seems to underfit the GEOM dataset, with low stability and validity rates. Could techniques from recent flow matching techniques or regularization methods improve performance? Alternatively, could a hybrid approach that combines Stiefel Flow Matching and discrete approaches maybe be beneficial here? 
- While optimal transport reduces trajectory length, it appears to slightly reduce success rates. Would a more flexible trade-off strategy that selectively applies optimal transport based on the target molecule’s complexity yield better outcomes? Some comparisons here would be nice. On a similar note, the paper embeds the structure space on the Stiefel manifold, which assumes exact moment constraints. Have the authors considered using approximate embeddings on simpler manifolds for faster computation at the expense of slight constraint violations?
- Do I understand correctly the canonical metric on the Stiefel manifold is used? Given recent developments in Riemannian FM, did the authors explore alternative Riemannian metrics?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a generetive model approach for generating 3D molecular structures conditioned on the molecular formula and moments of inertia. The generative method is an extension of Riemannian flow matching with equivariant optimal transport on the Stiefel manifold.

### Strengths
The paper shows the effectiveness of the proposed approach through evaluations over two molecule benchmarks: QM9 and GEOM. The method achieved lower RMSD for the generated molecules with a lower number of function evaluations (NFE) compared to the Euclidean diffusion model.

### Weaknesses
Limited model comparisons: The paper only compares its results against one method in the literature, where it might consider other works on Riemannian generative models.



### Questions
Does the Stiefel manifold have any constraints? How does it handle the increased complexity of larger molecules and the number of conformers?

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
2

### Summary
This paper proposes the use of flow matching generative models to obtain the 3D structure of molecules. This is achieved by explicitly enforcing problem constraints using Stiefel manifold and its properties.

### Strengths
- The paper is generally well-written and easy to follow. The math is sound and clearly presented. 

- The use of Stiefel manifold and its connection to the problem and the constraints in (2). 

- The use of geodesics in the Stiefel manifold that provides straight lines for navigating the manifold.

### Weaknesses
 - How generalizable is the proposed method? Can the authors perform OOD evaluation?

- Why the need to generate K=10 samples and report only the one with the lowest RMSD? Is this the standard practice? if yes, support is needed. If not, then performing this indicates instability which requires further investigation. 

- The evaluation metric for the proposed method seems to depends on RMSD thresholds defined by the authors. Have these thresholds been employed by previous methods that utilize neural networks for predicting the 3D structure of molecules? If yes, then citations are needed. The authors in Cheng et al. (2024) used correctness and reported the exact RMSD values. 

- Why not reporting the RMSD directly? For example, when predicting a protein 3D structure (e.g., in AlphaFold), the RMSD is reported directly after alignment.

- In lines 175 to 177, how practical is the assumption $n\geq 5$? How many examples with $n<5$ are removed from the datasets? 

- To compute the loss in (8), the authors listed 4 requirements. All are well explained other than the second. Further clarification is needed here.

- Many details of the paper is put in the Appendix. This is disrupting the flow of the paper. I suggest that the authors to place an algorithmic procedure for the sampling part. 

- Based on the definition of $\mathbf{m}$, shouldn't the total number of masses $M$ be equal to $n$?

- Vector $\mathbf{a}$ is not being used in the problem definition other than specifying the number of atoms. 

- The use of $st(n,3)$ instead of $st(n,4)$ in the main body is not well justified. Why Theorem 4 is put in the Appendix? 

- The sampling procedure is not as clearly presented as the training of $v_\theta$. Methmatical procedure of how the pre-trained $v_\theta$ is employed to perform sampling is needed. 

- In practice, the authors use t=0.001 to 1, but the uniform distribution in (8) uses U[0,1]. Shouldn't this be U(0,1]? 

- The last sentence in the Datasets paragraph in Section 4 requires support by a citation. 

- Why the FM model has more parameters than the diffusion model in Cheng et al. (2024)? 

- Ill-sentence in lines 445 to 446.

### Questions
### Major Comments/Questions: 

- In lines 175 to 177, how practical is the assumption $n\geq 5$? How many examples with $n<5$ are removed from the datasets? 

- To compute the loss in (8), the authors listed 4 requirements. All are well explained other than the second. Further clarification is needed here.

- Many details of the paper is put in the Appendix. This is disrupting the flow of the paper. I suggest that the authors to place an algorithmic procedure for the sampling part. 

### Minor Comments/Questions:

- Based on the definition of $\mathbf{m}$, shouldn't the total number of masses $M$ be equal to $n$?

- Vector $\mathbf{a}$ is not being used in the problem definition other than specifying the number of atoms. 

- The use of $st(n,3)$ instead of $st(n,4)$ in the main body is not well justified. Why Theorem 4 is put in the Appendix? 

- The sampling procedure is not as clearly presented as the training of $v_\theta$. Methmatical procedure of how the pre-trained $v_\theta$ is employed to perform sampling is needed. 

- In practice, the authors use t=0.001 to 1, but the uniform distribution in (8) uses U[0,1]. Shouldn't this be U(0,1]? 

- The last sentence in the Datasets paragraph in Section 4 requires support by a citation. 

- Why the FM model has more parameters than the diffusion model in Cheng et al. (2024)? 

- Ill-sentence in lines 445 to 446.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposed a novel flow-based generative framework to address the generation task of molecules with moment constraints. The authors noted the connection between the molecules with fixed moments and the Stiefel manifold and applied flow matching on such a manifold to ensure exact moment constraints. Empirical experiments demonstrated better generation results that satisfy these moment constraints.

### Strengths
- The manifold structure of n-body particles with fixed moments was demonstrated to be a Stiefel manifold in the paper, which, to the best of my knowledge, is the very first work.
- Equipped with such a Riemannian structure, the proposed framework can effectively navigate through the Stiefel manifold with the moment constraints exactly satisfied. Empirical experiments also demonstrated zero errors against the moment constraints.
- A thorough mathematical introduction to the Stiefel manifold was provided in the Appendix, together with efficient algorithms to calculate the exponential and logarithm maps on the Stiefel manifold, which makes practical training feasible.

### Weaknesses
1. The idea of the moment-constrained generation is not well-motivated in the paper.
    - **Molecules are not rigid bodies**. The dynamics of a molecule (e.g., stretching, twisting of bonds) make it possible for it to have various conformations that vary slightly by their principal moment of inertia. In other words, the moment of inertia measured by rotational spectroscopy is an ensemble property that reflects the average (or effective) moment of inertia of a molecule. In this sense, it seems more reasonable to allow for some violation of the moment constraints. Furthermore, the paper does not adequately address the fact that rotational spectroscopy measures effective moments of inertia, which are influenced by vibrational averaging, rather than the equilibrium moments directly. This distinction is crucial, and the paper should clarify how the proposed method accounts for or addresses this difference.
    - **Practical applications are missing**. It remains unclear what the practical applications of generating molecules with specific moments are. As an example, generating molecules with a specific HOMO-LUMO gap can be significant to the discovery of photoelectric molecules. The moment of inertia, however, does not hold a specific connection to real-world applications. The paper needs to provide a more compelling use case for generating molecules with precise moment constraints, beyond a purely theoretical exercise. The connection to experimental techniques like rotational spectroscopy needs to be more clearly articulated, especially considering the vibrational averaging issue.

2. **The number of baselines compared in the paper was small**. Indeed, only KREED was compared. There are other baselines available:
    - The conditional generative model in [1] where molecular properties are fed as additional information during both training and sampling for the conditional generation of molecules with desired properties. As the generative model implicitly learns the connection between the property and the molecule, it does not guarantee the exact satisfaction of constraints, but in practice, it does provide fairly competitive generation results. The paper should include a comparison against such conditional generative models, as they represent a more standard approach to property-constrained molecule generation. The lack of this comparison makes it difficult to assess the true advantage of the proposed method.
    - As it is always possible to project the generation to the corresponding Stiefel manifold according to Appendix B.6, another natural baseline would be directly projecting the unconstrained generation onto the Stiefel manifold, which also ensures the exact moment constraints. This projection-based baseline should be included to demonstrate the necessity of the proposed flow-based approach. It is not clear if the flow-based approach offers any advantage over a simple projection, and this needs to be empirically verified.

3. **The experimental results were not convincing enough** to demonstrate the superior performance of the proposed method. Although the moment constraint errors were indeed zero, the validity and stability scores were worse. The RMSD percentage also outperformed the baseline by only a small margin on the GEOM dataset. The paper should provide a more comprehensive analysis of the trade-offs between constraint satisfaction and other metrics like validity and stability. The small margin of improvement in RMSD, coupled with the decrease in other metrics, raises questions about the overall effectiveness of the method.

4. **The filtering procedure on the GEOM evaluation may give the proposed model with inappropriate advantages**, as it is essentially picking from a larger number of generations with a high likelihood of finding better samples. A similar procedure should be applied to the KREED baseline for a fair comparison. The paper needs to address this potential bias by applying the same filtering procedure to all baselines, or by providing a justification for why this is not necessary. Without this, the comparison is not fair.

### Questions
1. What are the practical applications of the moment-constrained molecule generation? Why is it important to enforce the exact moment constraints? See Weakness 1.
2. What are the performance of additional baselines? See Weakness 2.
3. Can you follow the same postprocessing procedure and compare the proposed model with the KREED-filter baseline performance? See Weakness 3 & 4.
4. What is the empirical training and sampling time of the proposed method compared to a normal unconstrained Euclidean flow matching model? I would expect extra time as the exponential map and logarithm map on the Stiefel manifold are far more complex to compute. Nonetheless, it is always beneficial to know the empirical time.
5. The logarithm map was calculated with 20 iterations. Does it provide a good enough approximation? Can you provide an analysis of the logarithm errors with respect to the number of iterations to better demonstrate your choice of 20 iterations (and 1 iteration for OT)?

### Soundness
3

### Presentation
4

### Contribution
3
