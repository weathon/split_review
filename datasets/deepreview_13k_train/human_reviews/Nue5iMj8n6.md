# Equivariant Masked Position Prediction for Efficient Molecular Representation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Graph neural networks (GNNs) have shown considerable promise in computational chemistry. However, the limited availability of molecular data raises concerns regarding GNNs' ability to effectively capture the fundamental principles of physics and chemistry, which constrains their generalization capabilities. To address this challenge, we introduce a novel self-supervised approach termed Equivariant Masked Position Prediction (EMPP), grounded in intramolecular potential and force theory. Unlike conventional attribute masking techniques, EMPP formulates a nuanced position prediction task that is more well-defined and enhances the learning of quantum mechanical features. EMPP also bypasses the approximation of the Gaussian mixture distribution commonly used in denoising methods, allowing for more accurate acquisition of physical properties. Experimental results indicate that EMPP significantly enhances performance of advanced molecular architectures, surpassing state-of-the-art self-supervised approaches. The code for EMPP is anonymously released in https://github.com/AnonymousACode/EMPP.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Equivariant Masked Position Prediction (EMPP) model, a self-supervised learning approach for molecular representation aimed at improving molecular property prediction in graph neural networks (GNNs). EMPP differs from conventional methods by predicting the relative position of masked atoms based on surrounding atomic structures rather than masking node attributes. This avoids the Gaussian mixture approximation used in denoising methods, potentially enhancing accuracy. EMPP is presented as a versatile technique that can function both as a pre-training task on unlabeled data and as an auxiliary task for labeled property prediction, achieving strong results across molecular benchmarks.

### Strengths
- **Originality**: EMPP’s approach of modeling relative atomic positions marks a novel shift from traditional self-supervised molecular methods, which typically rely on attribute masking or denoising with Gaussian mixtures. By avoiding Gaussian approximations, EMPP proposes a fresh method that could more precisely capture quantum mechanical properties without prior assumptions on potential energy surface shape.
- **Quality**: The methodology and experiment sections are comprehensive, offering detailed descriptions of the model architecture and training procedures. EMPP’s application across QM9 and MD17 benchmarks highlights its effectiveness and consistency in molecular property prediction.
- **Clarity**: The paper is clearly structured, and the motivations for EMPP are presented well. The provided comparisons, particularly with denoising methods, effectively illustrate the advantages of EMPP.
- **Significance**: EMPP’s adaptability for both pre-training and auxiliary tasks in GNNs is particularly valuable, as it could streamline the use of self-supervised learning in various molecular and materials science applications.

### Weaknesses
 - **Unclear Evaluation in Pre-training**: EMPP is proposed for both pre-training and auxiliary loss tasks, yet performance declines are observed in some properties (e.g., HOMO, LUMO, G, H) when used as a pre-training task (see Table 1 vs. Table 3). This suggests a possible limitation in generalizability when used for pre-training. The performance drop is concerning, and it is unclear whether this is due to the pre-training task itself or the choice of the backbone model. A more detailed analysis of the pre-training process, including the impact of different pre-training epochs and the choice of the backbone model, is needed to fully understand the limitations of EMPP as a pre-training method. The current results raise concerns about the robustness of EMPP when used in a pre-training context.

- **Too simple benchmark** : The molecules in the benchmark test sets, particularly QM9 and MD17, are relatively small or simple compounds, which may not sufficiently assess EMPP’s performance on more larger and realistic molecular structures. This makes it challenging to evaluate EMPP's generalization capabilities for applications requiring more intricate molecular structures. The limited size and structural diversity of these datasets may not accurately reflect the performance of EMPP on more complex systems, such as proteins or large organic molecules. This raises questions about the applicability of EMPP to real-world scenarios where molecular structures are significantly more complex.

### Questions
- **Physical Assumptions in Modeled Distributions**: It is interesting to understand the foundational physical or chemical assumptions behind EMPP’s use of relative position modeling for capturing atomic interactions. Denoising methods typically rely on a Boltzmann distribution near local minima, with harmonic potential assumptions. By contrast, EMPP’s approach seems to focus on relative distances and directional distributions between masked and neighboring atoms. This reviewer would like clarification on the theoretical basis for this choice. Specifically, do the authors view this approach as a distinct modeling assumption, or is it comparable to the physical basis provided by Boltzmann distributions in denoising methods?

- **Comparison with Denoising Methods**: Given that both EMPP and denoising methods model unknown data distributions, EMPP’s key distinction is its focus on relative, rather than absolute, atomic positions. The authors claim that one of the reasons for the performance improvement over the existing method is that they avoided the erroneous gaussian approximation (Figure 1-(d)). Then, can we expect the same level of performance improvement even if we do not adopt the method of modeling the distance and angular parts separately in EMPP? Is it possible to adopt a method that directly estimates the positional difference vector? Is it possible that the good performance of the model is due to modeling the distance and angular part separately? Please conduct ablation experiments on this.

### Soundness
4

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
2

### Summary
This paper presents a novel self-supervised framework for molecular representation learning, named Equivariant Masked Position Prediction (EMPP). EMPP pretrains the model by directly predicting the masked positions of atoms and addresses limitations in existing self-supervised methods (attribute masking and denoising). Experimental results show EMPP achieves competitive performance. EMPP can also enhance supervised learning when used as an auxiliary task.

### Strengths
- The paper is well-organized. The method has clear explanations.
- The proposed EMPP approach is simple yet effective, achieving state-of-the-art on benchmark datasets.

### Weaknesses
In Section 5.2, the comparison does not seem entirely fair. EMPP serves as an auxiliary task and relies on the Equiformer backbone, yet it is compared with other architectures that lack this component.



### Questions
In Equation 8, does the averaging over multiple masked atoms effectively act as training for a longer time? How does it impact the efficiency of the model? Could you please provide empirical results comparing training times and computational efficiency between single and multiple masked atoms? Additionally, discussing potential trade-offs between performance gains and computational costs would be appreciated.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a self-supervised learning approach called Equivariant Masked Position Prediction (EMPP) for molecular graph neural networks. The main idea behind is to mask the 3D position of atoms while keeping their other attributes, then predict these positions using the surrounding molecular structure. The authors intend to address the limitations of other self-supervised approaches. Results show comparable/superior performance to other state-of-the-art approaches for quantum-mechanical property prediction.

### Strengths
The core idea of predicting 3D atomic positions while keeping atomic attributes seems a reasonable evolution of existing molecular self-supervised approaches, taking into account the claimed limitations of previous approaches. The paper's strongest aspect is its clear presentation. The problem motivation and methodology are well articulated. The experimental validation, while having some gaps, provides adequate evidence on standard benchmarks. These strengths suggest incremental results.

### Weaknesses
The performance improvements on MD17 are relatively modest compared to the baseline Equiformer. This raises questions about whether the added complexity of EMPP is justified by the gains. Furthermore, for non-pretaining comparisons, there are models that substantially outperform the proposed method, based also on higher-order tensors.

Also, the computational overhead of EMPP isn't adequately addressed. The method requires calculating distributions over a spherical grid (100² points according to Table 7) for each masked atom, which could be computationally expensive. An analysis of training time and memory requirements compared to simpler approaches is missing.

I feel that altering the Equivariant Transformer architecture while testing the validity of the method simultaneously makes it difficult to distill where the improvements come from.

### Questions
1) What is the computational overhead of calculating distributions over the 100² spherical grid points compared to simpler approaches? Perhaps providing training time and memory requirements compared to baseline methods could also help.

2) How sensitive are the results to the sampling rate on the sphere?

3) Providing baseline results using the modified ET from TorchMD-Net could help distill how significant is the improvement due to the inclusion of the masking task. (By the way, the citation of the ET architecture is wrong).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed EMPP, a new approach for pre-training GNNs for 3D molecules with equivariant mask positional prediction. Instead of directly denoising the position from the approximation of Gaussian mixtures, the authors proposed to model the distribution over positions with equivariant GNNs. Downstream tasks on QM9 and MD17 demonstrated improvements in the performance after such a pre-training.

### Strengths
- The idea of predicting distributions over positions instead of directly predicting the atom positions is novel. Previous work, as was demonstrated in the paper, predominantly relied on the direct prediction of the mask atoms.
- Experimental results on QM9 and MD17 demonstrated the improvement of pre-training compared to the baseline models, in both end-to-end training and pre-training settings.
- An anonymous code link is provided for better reproducibility.

### Weaknesses
1. The delivery of this paper is poor, with noticeable inconsistencies regarding the proposed method, irrelevant materials and experiments.
    - **Irrelevant related work**. The proposed method has nothing to do with language models (not even the language modeling for chemical sequences like SMILES). However, the authors started with LLM, which was misleading and confusing.
    - **Irrelevant experiments**. The ablation study in Section 5.4 demonstrated the results for denoising pre-training models, but not for the proposed method in the paper. In contrast, the ablation study in Appendix C was designed for the proposed model. It is unclear why the authors put the irrelevant ablation studies in the main text.
    - **Objective in pre-training**. In Figure 1 and Section 3.2.1, the authors seemed to indicate their proposed approach is a force-prediction network for pre-training. However, Figure 2 and Section 3.2.2 indicated that the displacement vector $r_{ij}$ was instead regressed as the learning target.
    - **Objective in finetuning**. In Section 3.3, the energy and force prediction seemed to be the auxiliary input for pre-training. However, in the QM9/MD17 setting, they are the prediction targets. It is unclear how the model was trained end-to-end without the proposed pre-training objective.

2. **The claim of Gaussian mixture issues is questionable**. The authors claimed that the proposed approach can "effectively avoid
the approximation of Gaussian mixture" (Section 3.2.1). However, the loss functions in Eq.14 also explicitly rely on the Gaussian mixture assumption to derive the KL loss. The direction loss in Eq.16 assumes an alternative form based on the softmax function. The only difference is the Gaussian is defined for the radii and angles instead of Euclidean coordinates.

3. **The innovation in force prediction is lacking**. It is unclear about the major motivation behind the proposed method of "force prediction". Previous work (e.g., [1], also cited in the paper, [2], [3]) has clearly indicated the relation between the potential energy surface and the force field prediction with equivariant GNNs. In this sense, the proposed approach is exactly the same as other denoising pre-training models. Furthermore, the indicated issues with the Gaussian mixture of variable variance landscape can be effectively addressed with iterative sampling methods (i.e., diffusion models like [4]) and annealed Langevin dynamics. Alternatively, [2] introduced invariant noise-scale prediction which can handle different noise scales.

4. **The local equivariant prediction of the position distribution is not consistent as a pre-training objective** (unless the Gaussian variance is 0). This can be easily demonstrated by the fact that the radii and direction angles are constructed with respect to different neighboring atoms such that the expanded ground truth distribution roughly follows the shape of a small region of a spherical shell. For neighboring atoms at different positions, the ground truth is inconsistent unless the variance is 0 (i.e., a Dirac distribution).


### Questions
1. What is the training objective in the end-to-end training for the QM9/MD17 dataset? See Weakness 1.
2. Why can the proposed framework address the Gaussian mixture issue? In your pre-training objectives, Gaussian assumptions (or other softmax-based assumptions) were also explicitly assumed to make the ground truth distribution target. See Weakness 2.
3. What is the major innovation of the proposed framework as a "force prediction" model? Previous work has clearly indicated the close relationship between force field prediction and the denoising process of atom positions. Equivariant GNNs were also used in these works. In this sense, the approach proposed in this work is essentially the same as existing denoising frameworks. See Weakness 3.
4. How do you address the issue of inconsistent pre-training objectives if Gaussians are assumed independently for radii and angles? See Weakness 4.
5. What is the impact of $\tau$ in Eq.13? What is the impact of $\sigma$ in Eq.14? According to the ablation study of the denoising baselines, these values that control the "sharpness" of the distributions have a large impact on the final performance. However, they were not fully tested in the paper with the proposed approach.

### Soundness
2

### Presentation
3

### Contribution
3
