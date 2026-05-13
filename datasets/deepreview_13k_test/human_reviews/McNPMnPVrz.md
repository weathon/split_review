# Universally Applicable And Tunable Graph-Based Coarse-Graining For Machine Learning Force Fields

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Coarse-grained (CG) force field methods for molecular systems are a crucial tool to simulate large biological macromolecules and are therefore essential for characterisations of biomolecular systems. While state-of-the-art deep learning (DL)-based models for all-atom force fields have improved immensely over recent years, we observe and analyse significant limitations of the currently available approaches for DL-based CG simulations. In this work, we present the first transferable DL-based CG force field approach (i.e., not specific to only one narrowly defined system type) applicable to a wide range of biosystems. To achieve this, our CG algorithm does not rely on hard-coded rules and is tuned to output coarse-grained systems optimised for minimal statistical noise in the ground truth CG forces, which results in significant improvement of model training. Our force field model is also the first CG variant that is based on the MACE architecture and is trained on a custom dataset created by a new approach based on the fragmentation of large biosystems covering protein, RNA and lipid chemistry. We demonstrate that our model can be applied in molecular dynamics simulations to obtain stable and qualitatively accurate trajectories for a variety of systems, while also discussing cases for which we observe limited reliability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a new CG mapping method which builds over[1]. The authors demonstrate that their CG mapping outperforms standard mapping approaches by evaluating it with the MACE force field [2]. To substantiate the performance gains, they generate their own dataset, showcasing the improvements achieved by their CG mapping compared to the standard method.

references.
[1]https://www.osti.gov/servlets/purl/1558004
[2]https://github.com/ACEsuit/mace-jax

### Strengths
1. Coarse-graining is a critical challenge, as efficiently reducing the complexity of large bimolecular systems is essential for feasible modelling.

2. I commend the authors for identifying the lack of suitable datasets and generating their own to address this gap.

### Weaknesses
1. The paper claims{line 74 to 80}:
                      a) Generalizibility across chemically different molecules -> Which result in paper supports this claim?
                      b) Transferable across system size  -> Isn't this property of coarse graining itself? What unique contribution their approach makes beyond the inherent properties of coarse-graining methods?

2. Its not clear to me what exactly is the core contribution of this paper in terms of proposing a new method. What is different from proposed in[1]. Can you please clarify this using a pseudo code(Highlighting the lines which is original to this work)? For instance - provide a side-by-side comparison or annotated pseudocode highlighting the key differences and innovations compared to the reference work [1]

3. I see this paper has some development components but mainly an application paper. The selection of MACE as the modelling framework is a good choice, given its status as a top-performing model [2]. Adding more force fields and datasets on evaluation will considerably strengthen the paper. I suggest using more equivariant potentials like allegro[3] and nequip[4]. Additional types of dataset may include presence of diverse atoms/bonds in the molecule. 

references:
[1] https://www.osti.gov/servlets/purl/1558004
[2] https://matbench-discovery.materialsproject.org/
[3]https://www.nature.com/articles/s41467-023-36329-y
[4]https://github.com/mir-group/nequip

### Questions
Please see weaknesses as well.

1. Figure 3. shows the training loss curve and  tuned model is doing well. Do you have the test loss so we know it is not just overfitting?

2. For figure 5. can you also please include comparison to standard model. Also it will appreciable if the performance can be quantified.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work discusses a specific type of coarse graining approach for all-atom to coarse grained simulations, and uses MACE learned interatomic potentials to predict properties necessary for simulations. The key contributions are (1) the specific strategy (with some learnable parameters) for coarse-graining and (2) the use of MACE potentials rather than other ML potentials for the dynamics of the coarse-grained beads. 

The primary metrics for identifying the performance of the resulting coarse-grained potential are qualitative comparisons between all-atom (ML, GFN-FF) and coarse grained (MARTINI, this work) simulations for a couple representative biomolecular systems without solvent (e.g. biomolecules in vacuum).

### Strengths
**Originality:** The authors use a specific coarse-graining strategy that appears to be unique in literature. 

**Quality:** The authors consider a number of constraints and edge cases in how the coarse graining should be achieved, and necessary properties for the system/approach. They include some simulations of reasonably large simulations to verify the outcomes (albeit without solvent). 

**Clarity:** The paper is clearly written and easy to follow in the structure and logic. 

**Significance**: The process of coarse-graining (and back-mapping) are very important for the biomolecular community, but notoriously difficult to implement/improve on, and thus difficult to apply outside of very well studies areas such as water/DNA/RNA/etc. This is clearly an important research area.

### Weaknesses
The authors describe the key innovations as extending a cited work (Webb et al) as the specific coarse-grained mapping, and the use of MACE potentials. It is very surprising that they do not provide any qualitative or quantitative comparisons with that work to show that either the updated (tuned) strategy or the use of MACE potentials significantly improves the performance on either the original benchmarks in Webb et al, or in the case studies in this work. The only ablations here appear to be for the 'tuned' vs 'untuned' models.

A key contribution of this work is the use of MACE potentials. As the authors state on Page 2 "Furthermore, previous CG-MLFF approaches have been relying on the invariant SchNet architecture for the force field model, which for all-atom force fields has been mostly replaced by other (typically equivariant) architectures in recent studies, for example, MACE (Batatia et al., 2022b), VisNet (Wang et al., 2022), or Allegro (Musaelian et al., 2023)." However, some recent works have already considered models beyond SchNet, such as Allegro (Loose, Both et al. JPC-B 2023) or FLARE (Dushatko, Kozinsky et al. npj Comp Materials 2024). A comparison to these existing strategies should be included to show the improvement on this work over prior literature. 

The accuracy of a coarse-grained potential requires more validation than a simple qualitative check compared to the all-atom potential. This is especially the case when comparing for fixed time windows, as the equivalent timescales in coarse grained potentials are typically much longer than the timestep would suggest. Thermodynamic consistency, accuracy of averaged functions like the RDF or radius of gyration or other observables would be a much better check. Also see the Opinion (Durumeric, Clementi et al, Opinion in Structural Biology, 2023) for a nice overview of the important considerations and specifically Figure 3 which highlights quantitative agreement for an all-atom and coarse grained potential. 

Reproducibility: The code for the coarse-graining implementation does not appear to be available (or if it is already present in MACE-JAX, that is not clear from the text). Thus it might be difficult to reproduce or understand the details of the implementation.

### Questions
1. Quantitative agreement and thermodynamic consistency should be shown for reference systems in prior work. Qualitative comparisons of energy or RMSD for a fixed time window is not sufficient validation of a coarse grained simulation. 

2. Ablations are needed to show the improvements of MACE vs SchNet and original (Webb et al) vs the CG implementation here would be very helpful. Alternatively, quantitative comparisons between this work and prior work would also establish the improvements in this work. 

3. The authors should clarify the novelty of their work compared to prior work using potentials like Allegro (Voth et al, see citation above) or FLARE (Kozinsky et al, see citation above) and show quantitative comparisons with these prior works. This is especially the case since those prior works demonstrated quantitative agreement between all-atom and coarse grained observables for the simulations of interest.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a deep learning (DL)-based approach for coarse-grained (CG) molecular dynamics (MD) simulations, targeting large biomolecules like proteins, RNA, and lipids. It builds on a graph-based coarse-graining method, adding tunability to the priority values assigned to atoms, which group them into CG beads based on structural importance. The model aims to create more transferable CG simulations across a wide range of biosystems and improve training stability by reducing noise in force predictions. This work uses the MACE architecture for the force field model and trains it on a custom dataset derived from fragmented large biomolecules.

### Strengths
1. **Efficient Coarse-Graining with Tunable Parameters**: The authors' introduction of tunable priority values in the graph-based coarse-graining process allows for optimization based on the dataset. This tunability provides flexibility in CG mapping, allowing it to balance accuracy and computational efficiency effectively.

2. **Application of MACE Architecture**: Leveraging the advanced MACE architecture, a message-passing neural network, allows the model to capture complex interatomic potentials with high accuracy. The architecture’s flexibility and power make it well-suited to the demands of coarse-grained molecular dynamics, potentially enabling more stable and accurate simulations.

3. **Extensive Custom Dataset**: The authors created a robust dataset of 4.9 million biomolecular fragments, supporting model training across varied chemical structures. This comprehensive dataset could facilitate the model’s ability to generalize to new systems, enhancing its reliability in MD simulations.

### Weaknesses
### 

1. **Unclear Parameter Tuning for Coarse-Grained (CG) Models**: The paper lacks clarity on whether the CG parameters were tuned using the MLFF-predicted forces or the DFT-aggregated forces at the CG level. If the tuning was based on MLFF-predicted forces, it would be valuable to consider tuning with DFT-aggregated forces as well. Although the differences between the **Tuning** CG and standard CG with no machine learned force filed might be slight, DFT-based tuning could yield marginal improvements with respect to the primary loss function. However, it is unclear if this approach, in comparison to the original CG method, significantly enhances generalization or universal applicability, as suggested by the authors. This raises questions about the method’s novelty and practical impact, especially if it does not introduce substantial improvements over existing approaches.
2. **Limited and Insufficient Metrics**: The study's metrics are simplistic and may not support robust conclusions about the model’s generalizability or real-world applicability. For instance, the stability measure, assessed via temperature, provides only intermediate insights. A more comprehensive evaluation could follow metrics like those in [1], which evaluate atom-level stability and bond accuracy to better capture molecular coherence in 3D molecular generation. Moreover, the authors should compare their CG model to standard coarse-grained force fields, such as Martini, rather than only to their trained baseline. Additional limitations include the use of only one system each for RMSD and energy landscape evaluations, with no stable RMSD data for differentiating conformational states, where the author just quoted “Visual
inspection of the trajectory hints at the fact that the side chains of the two more distant amino acids
move further away from each other in this conformation” but not shown in the figure. Furthermore, the CG model's energy landscape lacks overlap in low-energy modes with the reference, suggesting a poor representation of molecular dynamics. A more rigorous evaluation design, as demonstrated in [2], would strengthen the validation of CG model performance.
3. **Minimal Contribution to the Machine Learning Community**: The paper’s contribution to ML is limited, as it does not address core ML topics such as optimization, representation learning, or generative modelling. Nor does it apply ML techniques innovatively to scientific problems, as seen in works like [3] and [4]. Instead, the study mainly adopts a prior CG approach with minimal innovation in priority calculation and applies the MACE model for CG force learning. This limited novelty and applicability may reduce the work’s relevance to the broader ML community.

**References:**

- [1] Hoogeboom, Emiel, et al. "Equivariant diffusion for molecule generation in 3d." *International Conference on Machine Learning.* PMLR, 2022.
- [2] Charron, Nicholas E., et al. “Navigating protein landscapes with a machine-learned transferable coarse-grained model.” *Nature Communications*, 2023.
- [3] Li, Shaoning, et al. "F $^ 3$ low: Frame-to-Frame Coarse-grained Molecular Dynamics with SE (3) Guided Flow Matching." *arXiv preprint arXiv:2405.00751,* 2024.
- [4] Arts, Marloes, et al. "Two for one: Diffusion models and force fields for coarse-grained molecular dynamics." *Journal of Chemical Theory and Computation* 19.18 (2023): 6151-6159.

### Questions
1. Could the authors provide more detail on how the CG parameters were tuned? Specifically, was the tuning based on MLFF-predicted forces or on DFT-aggregated atomic forces? Understanding this would help clarify the basis of the tuning choices and how they contribute to model accuracy.

2. For stability assessment, could the authors consider more comprehensive indicators beyond temperature alone? For example, studies like [1] (Hoogeboom et al., 2022) use atom-level stability and bond-type accuracy, which might provide additional insights into molecular coherence and CG model reliability.

3. Additionally, including a comparison to a well-established CG force field, such as Martini, might provide a useful reference point for assessing performance.

4. The RMSD and energy landscape analyses are insightful. Would the authors consider expanding these analyses to more than one system? Multiple systems could reinforce the stability and generalizability of the model across different molecular configurations.

5. In the energy landscape analysis, there seems to be limited overlap in low-energy modes between the CG model and the reference. Could the authors share their perspective on this outcome and any potential implications for MD applications?

6. The paper makes good strides in applying MACE to CG molecular dynamics. Could the authors further clarify how this work fits into broader ML themes, such as optimization or representation learning? Discussing this may help frame the study’s relevance to the ML community.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces an extension to a coarse-graining method for force fields: The previous work coarse grains the molecule by assigning priorities to atoms and then iteratively summarizes nodes based on these priorities. The priorities are assigned based on the first eigenvector of the Laplacian. The current paper proposes to use not just the Laplacian matrix but instead constructs weighted Laplacians with the same edges but weighted by three different features, resulting in four separate Laplacian matrices. The priorities are then calculated as a linear combination of the four first eigenvectors of the four matrices. The weights in the linear combination are found by optimizing an objective that is easy to calculate. The authors claim that this extension leads to a universally applicable method due to the higher degree of flexibility compared to the baseline. They support this by showing that their method leads to better training and qualitatively correct behaviours on their tested systems. To test their method, the authors also introduce a new dataset with large molecules designed to better test coarse-graining methods over a variety of systems.

### Strengths
The scalability of force fields is an essential open problem and still hinders their applicability in many domains despite big increases in computing power over recent years. Coarse-graining is an underexplored but promising avenue to contribute to faster force fields. I am not an expert on coarse-graining, but it looks like there is a lack of publicly available datasets with a large variety of systems that are simultaneously big enough to assess coarse-graining methods. Therefore, I think the authors are tackling a significant open problem with their work. The dataset alone would be a good contribution if there were some better defined automatically measurable metrics. I would encourage the authors to flesh out this part of their work. 
The proposed method for coarse-graining is based on accepted work and is a sensible, although straightforward, extension that shows promising results. I also appreciate that the authors were honest and discussed the limitations of their method's somewhat reduced stability, but I am missing more discussion on this topic.

### Weaknesses
I think the work generally has potential but is lacking polish:

The authors use the term "fragments" in the main text (abstract and line 150 and 151) and only explain what fragments are way later in the text, which is confusing because it can be confused with the "beads"

In line 124 its stated that "the simplicity is expected to be advantageous for model generalizability because the introduced inductive bias acts as a natural regularisation". However, I don't see where the inductive bias comes in. The eigenvector of the Laplacian of a molecular graph isn't a physically meaningful concept, as far as I know. 

Equation 5 is central to the paper, and an intuitive explanation would be great if possible.

What is the intuition for the three introduced weights? Why do we expect these to be meaningful, and couldn't other ones also be helpful? Since this is the central contribution of the work, a discussion of these aspects is necessary. 

The 1/R_ij features change over time and, therefore, can shuffle the priorities, leading to different coarse-grainings for different time steps. Wouldn't this induce unsmooth behaviour in the simulation? If I understand this correctly, since the original work uses only chemical bonds, this wouldn't be the case for the original work unless there is bond breaking.

In line 296: Is the element composition really the number of elements? Could this lead to cases where a lot of elements of the same type are coarse-grained, leading to a large input number, something that is known to make neural networks unstable?

Line 340: how can you just use 100 fragments? Dont we need the entire system to correctly predict energies/forces? 

Line 342: what loss do you use?

Line 372: person correlation between what?

Figure 3: This looks promising, but why don't we (also) look at validation/test curves?

Line 402: Why did the tuned model not reach the final training epoch?

Line 428: It is great that the authors were honest and mentioned the reduced stability, but possible reasons for this should be discussed, even if the issue has not yet been solved

Figure 4: I am not sure what these plots are trying to tell me, especially because they are not comparable between the different models, as mentioned in the text. It would be better to replace them with more helpful metrics. For example, if you can visually make out different conformers in the ground truth simulation, why not coarse-grain them with the different methods and then calculate the distance between the model's trajectories and these coarse-grained ground truth conformers? This would make it much easier to see if the different models found the same conformers. It doesn't have to be precisely this metric, but anything more informative would be great.

### Questions
Why are only first eigenvectors used?

Does any of this consider bond-breaking?

### Soundness
2

### Presentation
1

### Contribution
2
