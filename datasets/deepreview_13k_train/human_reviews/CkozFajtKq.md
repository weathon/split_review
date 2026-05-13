# Flow Matching for Accelerated Simulation of Atomic Transport in Materials

- Decision: Reject
- Scores: 8, 3, 8, 8, 5, 6

## Abstract
We introduce \textsc{LiFlow}, a generative framework to accelerate molecular dynamics (MD) simulations for crystalline materials that formulates the task as conditional generation of atomic displacements.
The model uses flow matching, with a \textit{Propagator} submodel to generate atomic displacements and a \textit{Corrector} to locally correct unphysical geometries, and incorporates an adaptive prior based on the Maxwell--Boltzmann distribution to account for chemical and thermal conditions.
We benchmark \textsc{LiFlow} on a dataset comprising 25-ps trajectories of lithium diffusion across 4,186 solid-state electrolyte (SSE) candidates at four temperatures.
The model obtains a consistent Spearman rank correlation of 0.7--0.8 for lithium mean squared displacement (MSD) predictions on unseen compositions.
Furthermore, \textsc{LiFlow} generalizes from short training trajectories to larger supercells and longer simulations while maintaining high accuracy.
With speed-ups of up to 600,000$\times$ compared to first-principles methods, \textsc{LiFlow} enables scalable simulations at significantly larger length and time scales.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The LiFlow framework presents an innovative ML-based approach to accelerating molecular dynamics simulations specifically for atomic transport. By combining a propagator and corrector network in a symmetry-aware conditional flow matching framework, the model achieves high performance while maintaining physical consistency across larger time scales and system sizes.

### Strengths
- The paper is clearly written, with thorough notation and well-organized sections, making it accessible and valuable to the AI for Science community. Its presentation facilitates understanding of the model's design and methodology.
- The model architecture is built with strong symmetry considerations, effectively leveraging domain-specific invariances essential for applications in atomic transport. This symmetry-aware approach not only improves the model's robustness but also reinforces its applicability to material science challenges.

### Weaknesses
 - While the model is effective for atomic transport in crystalline materials, its applicability to other systems like biomolecules or amorphous structures remains unexplored. Extending this method to diverse types of molecular dynamics systems could increase its impact.
- While the paper provides dataset statistics of elemental count distribution and Hitogram of MSD, it would benefit from including detailed statistics of the dataset. Information such as the number of atoms, types of atoms, and lattice structures used in the training and testing sets would offer a more comprehensive understanding of the model's training conditions and its generalizability across different material structures.

### Questions
- In principle, it seems the propagator network alone should be sufficient for simulating MD if it’s well-designed. Why was the corrector network included, and what specific benefits does it provide? Was there a reason for not focusing on further enhancing the propagator network instead?
- What aspects of this method make it particularly well-suited for atomic transport? Would it also apply to simulating protein MD, such as Alanine Dipeptide?
- Is there a reason for not comparing this approach with other ML-based MD acceleration methods, such as Time-warp?
- In Table A1, the model appears sensitive to the choice of internal GNN architecture and representation. What were the main considerations when selecting the GNN, and is there another option instead of a modified PINN?
- Does the model maintain supercell and global translation invariance within the corrector network? I noticed that in Appendix D.2, edge construction on the denoised positions was skipped—how might this impact these invariances?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces LIFLOW, a generative framework for improving molecular dynamics (MD) simulations in crystalline materials, particularly solid-state electrolytes (SSEs). It formulates the simulation task as conditional generation of atomic displacements and employs a flow matching approach with a 'Propagator' for generating atomic displacements and a 'Corrector' to ensure physical stability. Model also leverages adaptive prior based on the Maxwell–Boltzmann distribution to account for chemical and thermal conditions. The model is benchmarked on a dataset of lithium diffusion across SSE candidates, achieving significant speed-ups over traditional Ab Initio Molecular Dynamics (AIMD) methods.

### Strengths
The application of flow matching to model atomic transport is an innovative approach, offering a transformative potential for simulating dynamics efficiently across large spatiotemporal scales. LIFLOW achieves remarkable computational performance, delivering speed-ups of up to 600,000× compared to AIMD and 400× compared to MLIP-based simulations. By tackling the significant challenge of high computational costs in MD simulations, this work addresses a crucial bottleneck in materials research. The focus on lithium-based solid-state electrolytes is both timely and highly relevant, given the growing need for advancements in energy storage technologies.

### Weaknesses
The primary comparison is with AIMD simulations and MLIP, which are used to generate the data. The paper does not compare LIFLOW to existing machine learning-based approaches for MD acceleration, such as GNN-based models [1, 2], diffusion models [3], variational approaches [4] or normalizing flows [5]. Inclusion of such comparisons would greatly improve the credibility of the claims of ths work.

While the model is shown to work well on lithium SSEs, there is limited discussion on generalizing LIFLOW to other types of materials or chemical systems. This could restrict the perceived impact of the method. An additional showcase on different datasets, such as MD17 [6] and OC20 [7] could further shine light on the model's generalization. 

The model struggles with extrapolating to conditions outside the training regime, such as lower temperatures, where rare events are poorly captured. This suggests potential limitations in scenarios requiring greater generalization. Considering well know enhancement approaches, such as physics informed neural networks for the loss function modification or active learning to sample when rare events occur can be benificial.   

The model relies on several hyperparameters, such as the prior scale, that require careful tuning, which could impact its ease of use and robustness. While the authors acknowledge this issue and discuss the need for a more principled method for prior design, further improvements could be explored. Specifically, I suggest that the authors discuss any sensitivity analyses they performed to understand the impact of these hyperparameters on model performance. This could provide insights into the stability and reliability of the model across a range of settings. Additionally, the authors might consider implementing automated hyperparameter tuning methods, such as Bayesian optimization or hyperparameter sweeps, to alleviate the need for manual tuning. Such techniques could enhance the model's usability and reduce the dependency on empirical parameter selection. Finally, exploring the integration of adaptive or learnable priors might offer a more dynamic approach, allowing the model to adjust parameters in response to varying data conditions automatically.

Some of the modifications to the PaiNN [8] architecture, such as the integration of equivariant flow fields and the use of a Maxwell-Boltzmann prior distribution, appear to be necessary adjustments rather than novel contributions. These changes are essential to adapt PaiNN into a flow-based model while preserving physical symmetries and ensuring accurate molecular dynamics simulations. Additionally, given that similar flow matching techniques have been applied in related work (as discussed in previous papers, such as [9, 10, 11]), the degree of novelty in these architectural modifications may be limited, as they are fundamental requirements for the chosen modeling approach rather than unique innovations. Furthermore, these modifications likely contribute to increased computational costs compared to the original PaiNN architecture, which may limit the model’s efficiency and scalability in large-scale simulations, even if performance is improved for the experiments at hand.

The paper's readability could be significantly improved, as the current structure and presentation make it challenging to follow. Enhancing the flow of the text and providing clearer explanations would greatly benefit readers and better convey the complexity of the work. Location of Table 1 and Table 2 distrupts the flow. Specifically, I suggest reorganizing the sections for better coherence. Large-scale inference and computational costs can be subsection intead of bolds. Additionally, the discussions on the effect of hyperparameters like P and C, as well as the choice of prior, could be moved to the Ablation Studies section following the main experimental results. Each dataset and its results given as 4.2 and 4.3 but it is very hard to pinpoint the results. I think 'effect of prior study' and 'case study'  is where you share results for 4.2. These can be created into a subsetion as 'Results for Universal Model' or something. 'Reproducing kinetic properties' and 'Reproducing structural features' is where you share your results for 4.3, which can also benefit from similar fashion. Figure 2 and Figure 3 can be merge into one figure which spans 2 columns. A figure of the proposed model can be shared in addition to the scheme. I believe these or similar changes would streamline the narrative and make it easier for readers to understand the work and its effect. Initial sentece in the introduction needs a reference as well as the 'Crystalline materials and representation' subsection. 'REPRODUCIBILITY STATEMENT' is given in 11th page.

### Questions
1) Why authors did not include comparisons with other ML-based MD acceleration methods, such as GNNs, diffusion, variational autoencoders, and normalizing flows. For a fair effectiveness of the model, some of the state-of-the-art ML approaches could have been implemented [1, 2, 3, 4, 5].

2) Can LIFLOW be easily adapted to simulate other materials beyond lithium-based SSEs? If so, what modifications would be necessary? For example, can you apply this model to MD17 [6], OC20 [7], or Ani-1x [8] dataset and show its effectiveness compared to other state-of-the-art?

3) The model relies on several hyperparameters, such as the prior scale, that require careful tuning, potentially impacting its ease of use and robustness. While you acknowledge the need for a more principled method for prior design, did you perform any sensitivity analyses to understand how these hyperparameters affect model performance and stability? Additionally, have you considered implementing automated hyperparameter tuning techniques, like Bayesian optimization or hyperparameter sweeps, to minimize the reliance on manual tuning? Finally, do you see potential benefits in exploring adaptive or learnable priors that could dynamically adjust based on data conditions, and if so, how might this improve the model’s performance and generalizability?

4) Authors mention the risk of generating physically fictitious dynamics. Are there ways to quantify or mitigate this risk more systematically?

5) Amorphous materials often exhibit complex atomic transport mechanisms due to their lack of long-range order [9]. How well would LIFLOW generalize to amorphous systems, and have you considered testing the model on amorphous materials such as amorphous silicon or lithium-phosphorus oxynitride (LiPON) electrolytes [10]? If not, what challenges do you foresee in applying your approach to such systems, and how might the model be adapted to handle the inherent structural disorder?

6) In Section 3.2.1, you provide a comprehensive explanation of how your model ensures invariance to various symmetries, including permutation, translation, and rotation. Given the complexities involved in modeling these symmetries, did you encounter any specific challenges or limitations when implementing these equivariant properties, particularly for higher-order interactions or rare configurations? Additionally, do you believe that incorporating more advanced equivariant architectures (e.g., equivariant graph attention [1]) could further improve the performance or generalizability of your approach?

7) The modifications you made to the PaiNN architecture,  such as integrating equivariant flow fields and using a Maxwell-Boltzmann prior, seem necessary for adapting PaiNN into a flow-based framework that preserves physical symmetries. Given that these changes are essential for the model's operation and that flow matching techniques have been previously applied in related contexts (as seen in [11, 12, 13]), do you consider your approach to be a novel contribution, or do you view it as an adaptation of existing methods for this specific application? Furthermore, how do these modifications impact the computational cost compared to the original PaiNN architecture? Does the accuracy gained with the changes still overshadows the computational cost for the larger simulations?


[1] Liao, Y. L., & Smidt, T. (2022). Equiformer: Equivariant graph attention transformer for 3d atomistic graphs. arXiv preprint arXiv:2206.11990.

[2] Batzner, S., Musaelian, A., Sun, L., Geiger, M., Mailoa, J. P., Kornbluth, M., ... & Kozinsky, B. (2022). E (3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials. Nature communications, 13(1), 2453.

[3] Wu, F., & Li, S. Z. (2023, June). DIFFMD: a geometric diffusion model for molecular dynamics simulations. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 37, No. 4, pp. 5321-5329).

[4] Wang, W., & Gómez-Bombarelli, R. (2019). Coarse-graining auto-encoders for molecular dynamics. npj Computational Materials, 5(1), 125.

[5] Tamagnone, S., Laio, A., & Gabrié, M. (2024). Coarse-Grained Molecular Dynamics with Normalizing Flows. Journal of Chemical Theory and Computation, 20(18), 7796-7805.

[6] Chmiela, S., Tkatchenko, A., Sauceda, H. E., Poltavsky, I., Schütt, K. T., & Müller, K. R. (2017). Machine learning of accurate energy-conserving molecular force fields. Science advances, 3(5), e1603015.

[7] Chanussot, L., Das, A., Goyal, S., Lavril, T., Shuaibi, M., Riviere, M., ... & Ulissi, Z. (2021). Open catalyst 2020 (OC20) dataset and community challenges. Acs Catalysis, 11(10), 6059-6072.

[8] Smith, J. S., Zubatyuk, R., Nebgen, B., Lubbers, N., Barros, K., Roitberg, A. E., ... & Tretiak, S. (2020). The ANI-1ccx and ANI-1x data sets, coupled-cluster and density functional theory properties for molecules. Scientific data, 7(1), 134.

[9] Philibert, J. (1991). Atom movements: diffusion and mass transport in solids (p. 577). Les Ulis, France: éditions de Physique.

[10] Lacivita, V., Artrith, N., & Ceder, G. (2018). Structural and compositional factors that control the Li-ion conductivity in LiPON electrolytes. Chemistry of Materials, 30(20), 7077-7090.

[11] Song, Y., Gong, J., Xu, M., Cao, Z., Lan, Y., Ermon, S., ... & Ma, W. Y. (2024). Equivariant flow matching with hybrid probability transport for 3d molecule generation. Advances in Neural Information Processing Systems, 36.

[12] Klein, L., Krämer, A., & Noé, F. (2024). Equivariant flow matching. Advances in Neural Information Processing Systems, 36.

[13] Dunn, I., & Koes, D. R. (2024). Mixed Continuous and Categorical Flow Matching for 3D De Novo Molecule Generation. ArXiv.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce a generative modeling framework called LIFlow that serves to accelerate molecular dynamics (MD) simulations of crystalline materials. A physically-correct propagator is combined with a stabilizing corrector, and an adaptive prior based on the Maxwell-Boltzmann distribution is leveraged. The resulting generative model is thoroughly evaluated and results in massive speedups over direct MD simulations, all while maintaining high accuracy.

### Strengths
The authors introduce a novel method for generative acceleration of molecular dynamics (MD) simulations for crystalline materials by generating atomic displacements. They also develop a flow matching approach that takes into account chemical and thermal conditions, and incorporate a corrector to ensure stability. The authors also contribute a new dataset useful for the material science community. Overall, the paper is exceptionally well written and the methods appear sound and novel, to the best of my knowledge. As written, the scope feels laser focused on MD simulations, but I'm confident the ideas in this work could be applied to other scenarios as well; see the weaknesses and questions sections for some ideas there.

### Weaknesses
The primary issue is that the paper needs to be cleaned up for more general audiences, by including more citations where appropriate and adding more information to the appendix section. See "Questions" for more concrete details and suggestions. I encourage the authors to revise the paper so a broader audience can read and understand what's going on, not just folks from the atomic transport and SSE community.

### Questions
1. I had to do a lot of background reading on atomic transport in order to even begin understanding this paper. I suggest that the authors include a set of links to seminal works, right at the end of the first sentence for the paper.

2. I understand space is at a premium, but the paragraph on page 4, lines 169-176, is very dense and assumes a lot of prior knowledge with no citations. Please add citations so the interested reader can follow them. ICLR is a broad conference for a general audience, and it is plausible that your techniques may be usable elsewhere.

3. Eq 11, why linear interpolation? Is the only rationale to come up with a simple combination of the prior sample and the data sample to design the flow + also satisfy symmetry conditions?

4. On line 245 and 246 on page 5, you say you use an RBF expansion of atomic distances and the unit vector directions along edges. This is one of those examples of an extremely dense statement that should be unpacked somewhere (perhaps the appendix). Please elaborate.

5. Please explain your evaluation metrics more clearly for someone who is not from your community. I suggest adding a section to the appendix. I had to do a lot of searching to figure out why your presented metrics were reasonable ones.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a machine-learning-accelerated approach to simulating atomic dynamics in crystalline materials. The approach uses a flow matching model to predict the atomic positions at the next (physical) time given their current positions. An auxiliary “corrector” flow matching model denoises the predicted displacements of any errors introduced by the aforementioned “propagator” model. The authors take care to design an equivariant flow and invariant prior distribution that respect symmetries inherent in the problem. The authors created two datasets of MLIP and AIMD computed trajectories, respectively, to train the flow matching models. They compare the mean squared displacement (MSD) and radial distribution functions (RDF) of the estimated trajectories against those of the ground truth. Ablation studies verify the design choices.

### Strengths
* The proposed method is sound, and the ablation studies show significant improvement provided by each of the components (i.e., the task-informed prior and corrector model).
* I especially like that the authors elegantly incorporate physics knowledge in the generative approach. Namely, they choose a prior based on the Maxwell-Boltzmann distribution, check that the prior distribution is invariant with respect to the relevant symmetries, and check that the flow (although linear interpolation is already a common choice) is equivariant with respect to the symmetries.
* Overall, the presentation is good. The background was easy to follow and provided just enough information for a non-domain-expert to understand the paper. The reason I rate the presentation as a 2 instead of a 3 is because the results section refers too much to the appendix, and technically the paper (i.e., everything before references) goes beyond ten pages.

### Weaknesses
 * The MSD and RDF metrics appear to be high-level summary metrics of an estimated trajectory, making me wonder how much information is lost when using them to compare to the ground truth. For example, why is RDF not averaged across the whole simulation (line 345)? Why not compute something like MAE of estimated positions across the whole trajectory? The use of MSD and RDF, while common, may obscure important details about the quality of the generated trajectories. Specifically, these metrics provide aggregate information about the system's behavior but do not reveal the accuracy of individual atomic positions over time. A more granular analysis, such as the MAE of atomic positions at each time step, would provide a more direct measure of the model's ability to reproduce the reference trajectory. Furthermore, the RDF is averaged over a portion of the simulation, which could potentially mask discrepancies that occur during the initial equilibration phase or at later stages.
* The authors should have made more effort to make the presentation compact enough to fit on 9-10 pages without having to refer to appendix figures. All the material up to the references technically takes up more than 10 pages. As an example of excessive reliance on appendix material, an entire subsection (lines 455-466) refers only to appendix figures. The excessive reliance on the appendix makes it difficult to assess the core contributions of the work without constantly flipping back and forth. This disrupts the flow of reading and makes it challenging to grasp the key results and their significance. The main text should be self-contained and provide a clear and concise presentation of the method and its performance. The appendix should be reserved for supplementary information and not be essential for understanding the main findings.

### Questions
* Intuitively, it seems that the corrector model should be easier to learn than the propagator model since its task is simpler (just removing small amounts of noise from displacements). Why not make it a one-step conditional generative model instead of an entire flow? Have you tried reducing the number of flow steps to 1 for the corrector?

Suggestions:
* Line 71 mentions a “lattice matrix.” It would help to describe what this is intuitively for someone unfamiliar with the field.
* In the footnote on line 107, should the $t$ be a $\tau$?
* Line 230 defines a $\sigma_\mathcal{S}$ variable that does not appear in Equation 10 above.
* The language in lines 331-332 makes it sound like the MSD is computed *between* configurations and not for a single configuration.
* It’s hard to tell what the purpose of Table 3 is, and it’s not explained much in the text. What are these results supposed to convey about your method?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The manuscripts proposes LiFlow, a conditional generative model as a surrogate of MD simulation for Li diffusion in electrolytes, an important technical application. The goal of accelerating MD with generative surrogate model is a rapidly developing field and as the authors noted, there are a good number of papers. There is no substantial and quantitative comparison to those papers. While the technical work here is solid, it lacks enough novelty or substantial improvement as a methodology development paper.

### Strengths
The paper was written in a clear, easy to understand way. The technical details and results were clearly presented. Citations were comprehensive and demonstrated knowledge of the authors with the fast-evolving field. The experiments were performed nicely. The results were decent. The release of of an open dataset for Li diffusion simulations is a positive contribution.

### Weaknesses
The ideas presented are not very new

* The overall idea of flow-based generative model for MD surrogate modeling was employed in e.g. TimeWarp (Karras et al 2023), and F3LOW (Li et al 2024) even though the applications of these papers were protein dynamics.

* The equivariant GNN (PaiNN) was adopted from an existing, mature design.

* The periodicity aspect is trivial for any work on crystalline materials modeling.

* As the authors properly cited, the predictor (called propagator here) + corrector idea was previously employed in (Fu et al 2023). This paper also discussed Li-ion diffusion.

* The idea of two sets edge in the conditional GNN network was previously employed in (Hsu et al 2024).

* The physics-inspired prior was, as the authors admitted, employed previously.

* The results were good as proof-of-concept, but not practically useful enough.

### Questions
* As discussed in the paper, a majority of generative surrogates for MD were applied to biomolecular simulation. A closely related paper, Fu et al 2023, already studied surrogate models based on the diffusion model for Li-ion electrolyte. In their response to this review, the authors are advised to compare more carefully to that paper and show that they are offering something better.

* Please consider explaining how the work compares to TimeWarp and F3LOW.

* Please cite Arts et al 2023, "Two for one ...".

* Overall, I find it hard to accept it as a method development paper to ICLR. It can be a good paper for a chemistry/materials science journal.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
As informed to the area chairs, I’m unable to review this paper due my lack of expertise in this area. Please disregard the assigned scores, since I’ve added them just to complete the submission.

### Strengths
As informed to the area chairs, I’m unable to review this paper due my lack of expertise in this area. Please disregard the assigned scores, since I’ve added them just to complete the submission.

### Weaknesses
As informed to the area chairs, I’m unable to review this paper due my lack of expertise in this area. Please disregard the assigned scores, since I’ve added them just to complete the submission.

### Questions
As informed to the area chairs, I’m unable to review this paper due my lack of expertise in this area. Please disregard the assigned scores, since I’ve added them just to complete the submission.

### Soundness
2

### Presentation
2

### Contribution
2
