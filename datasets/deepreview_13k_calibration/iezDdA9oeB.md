# Fast and Accurate Blind Flexible Docking

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Molecular docking that predicts the bound structures of small molecules (ligands) to their protein targets, plays a vital role in drug discovery. However, existing docking methods often face limitations: they either overlook crucial structural changes by assuming protein rigidity or suffer from low computational efficiency due to their reliance on generative models for structure sampling. To address these challenges, we propose FABFlex, a fast and accurate regression-based multi-task learning model designed for realistic blind flexible docking scenarios, where proteins exhibit flexibility and binding pocket sites are unknown (blind). Specifically, FABFlex's architecture comprises three specialized modules working in concert: (1) A pocket prediction module that identifies potential binding sites, addressing the challenges inherent in blind docking scenarios. (2) A ligand docking module that predicts the bound (holo) structures of ligands from their unbound (apo) states. (3) A pocket docking module that forecasts the holo structures of protein pockets from their apo conformations. Notably, FABFlex incorporates an iterative update mechanism that serves as a conduit between the ligand and pocket docking modules, enabling continuous structural refinements. This approach effectively integrates the three subtasks of blind flexible docking—pocket identification, ligand conformation prediction, and protein flexibility modeling—into a unified, coherent framework. Extensive experiments on public benchmark datasets demonstrate that FABFlex not only achieves superior effectiveness in predicting accurate binding modes but also exhibits a significant speed advantage (208$\times$) compared to existing state-of-the-art methods. Our code is released at~\url{https://anonymous.4open.science/r/FABFlex-7007}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the challenging and realistic scenario of blind flexible molecular docking, where the binding sites are unknown and the proteins exhibit dynamic behavior during the docking process. This is a critical problem that reflects how molecules interact with proteins. The paper argues that current flexible docking methods, predominantly reliant on sampling strategies with diffusion models, suffer from significant inefficiencies. To overcome this drawback, the paper explores the potential of regression-based model in handling flexible docking. Utilizing AlphaFold2-predicted apo protein conformations, this paper proposes an end-to-end regression-based model named FABFlex, designed to achieve both fast computation and accurate docking performance in blind flexible docking scenarios. Experiments show that FABFlex not only significantly enhances the ligand structures and positively performs impacts on pocket conformations, but also substantially accelerates docking speed compared to the recent SOTA method, DynamicBind.

### Strengths
1.	The paper tackles the blind flexible molecular docking scenario, which is a more practical and crucial setting compared to many existing studies that focus on rigid docking, where proteins are assumed to be static during the docking process.
2.	The architecture of the proposed model is intuitive and easy to comprehend, with each module specifically designed to address a subtask of the blind flexible docking problem. It is easy to follow.
3.	The model significantly outperforms the SOTA docking methods, such as DynamicBind, DiffDock, and TankBind, on ligand structure predictions. Additionally, it operates much faster than recent SOTA flexible docking method, DynamicBind (approximately 208 times).
4.	This model maintains a robust generalization ability on those unseen proteins. The visualization of the iterative mechanism is very interesting, illustrating how the ligand is gradually docked from the apo to the holo state.

### Weaknesses
1.	It is unclear why the number of ligand-protein sample pairs of PDBBind v2020 used in this paper is smaller than that in the existing studies such as TankBind, FABind.
2.	It seems that FABFlex relies on FABind layer as the fundamental component to construct the model, but the details of how this layer is adapted for use in FABFlex are not clearly articulated. Specifically, the paper lacks a detailed explanation of how the FABind layer's message-passing steps are utilized within each of the three modules of FABFlex (pocket prediction, ligand docking, and pocket docking). It is not clear how the node and edge features are initialized and updated in each module, and how the outputs of the FABind layer are processed to achieve the specific tasks of each module. Furthermore, the paper does not clarify whether the FABind layer is used in its original form or if any modifications were made to its architecture or parameters for the FABFlex model.
3.	It seems that the model assumes that there is only a single binding pocket in a given ligand-protein pair, whereas in reality, there are possibly multiple potential binding pockets. This assumption limits the applicability of the model to more complex biological systems where multiple binding sites may be present. The paper does not discuss how the model would handle cases with multiple binding pockets or how it would select the most relevant binding site.

### Questions
1.	Does FABFlex’s docking result have atomic clash problem? If so, how to mitigate or resolve this problem?
2.	Can you provide more details of the construction and workflow of FABFlex?
3.	Can you use some way to intuitively demonstrate the pocket prediction performance?

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
5

### Summary
In this paper, the authors introduce FABFlex, a regression-based flexible blind docking model. FABFlex uses the EGNN architecture, with FABind as its main layer. The model is composed of three modules: (1) the pocket prediction module, (2) the ligand docking module, and (3) the pocket docking module. FABFlex focuses on finding holo structures to enable flexible docking. Compared to other models, FABFlex demonstrates accuracy with a higher percentage of ligands achieving RMSD < 2 Å and RMSD < 5 Å, and it is also accurate in identifying holo pockets based on RMSD metrics.

### Strengths
- The paper presents all details clearly and comprehensibly.
- This is the one of first applications of regression-based flexible blind docking.
- It employs an interesting multi-task approach, addressing more than a single task simultaneously.
- The use of flexibility, rather than just rigidity, in docking, combined with a regression approach, makes the paper compelling.
- The pipeline provides a systematic, data-driven approach to molecular docking.
- The experiments are detailed and clearly presented, with comprehensive benchmarking against other models.
- The code is openly shared (though the README is empty; see weaknesses).

**Originality:** FABFlex is innovative as a regression-based model for flexible docking. It also stands out for its multi-task capability, predicting not only apo structures but also holo-structures.

**Quality:** The paper's quality is highlighted by its comprehensive benchmarking against other models. Additionally, it goes beyond ligand RMSD to include pocket RMSD analyses, further enhancing the study’s depth.

**Clarity:** The paper is well-written grammatically, with equations that are scientifically clear, readable, and easy to follow.

### Weaknesses
 - This study closely resembles the FABind[1,2] approach in both training and inference, with many of the techniques used already present in FABind. Consequently, flexible docking appears somewhat overshadowed by FABind.
- It is not specified whether protein preprocessing is used for inference runtime, affecting the runtime comparison.
- Using binary classification to identify pocket regions could limit flexibility at the atomic level; a more adaptable approach may be beneficial.
- The study relies solely on the RMSD metric, which does not always ensure plausible structures. Metrics such as semi-empirical binding affinity, protein-ligand steric clashes, and ligand strain energy, as suggested by [3,4,5,6,7], should be considered.
- Although proteins and ligands are visually classified as apo or holo, this classification does not guarantee bioactive, chemical, or physical plausibility. Including metrics like binding affinity, steric clashes, and ligand strain energy would provide greater insight, as demonstrated in studies like Posebuster[3], PoseCheck[4], PoseBench[5], CompassDock[6], and PLINDER[7].
- The binding affinity, protein-ligand steric clashes, and ligand strain energy for the processed PDBBind’s apo and holo structures were not examined.
- While RMSD may increase due to holo pocket region flexibility, the focus should instead be on binding affinity, steric clashes, and ligand strain energy, but the study only emphasizes RMSD.
- It is unclear if other DL-based models in the benchmark used the same timesplit or were retrained for comparability.
- If RMSD is the chosen metric, timesplit information leakage may occur, as described in the PLINDER study. Clarifying timesplitting methods would strengthen the study.
- As a FABind user, I found the reported runtime of 0.12 sec inaccurate. When protein preprocessing is included, runtime is closer to 10-15 seconds, with 0.12 sec applying only to ligand conformation prediction. Based on FABind, I expect FABFlex’s runtime to exceed the stated 0.49 sec with protein preprocessing included.
- Although FABFlex claims faster runtime than DiffDock, normalizing per-ligand runtime suggests DiffDock may be more efficient, as DiffDock samples ~40 ligand conformations in ~2 sec per conformation, while FABFlex takes ~10-15 sec for one prediction.

**Quality:** The RMSD metric may lack biological, chemical, or physical relevance. For benchmarking, it would be better to include up-to-date metrics like semi-empirical binding affinity, protein-ligand steric clashes, and ligand strain energy.

**Clarity:** The criteria for selecting the values of alphas in the loss function are not clearly explained.

**Reproducibility:** Although the code is open source, the README section is empty, and usage instructions are not provided. If the README were clarified, I could test and reassess the code’s reproducibility. Additionally, the conda environment in the YAML file is named "FABind," raising anonymity concerns regarding double-blind review, as it suggests potential overlap with FABind’s authors.

**Minor Mistake**

"Subsequent" is used twice:
> "The predicted pocket sites by pocket prediction module enable the subsequent subsequent ligand"

### Questions
- Do you account for protein preprocessing during inference? Based on my experience with FABind, preprocessing typically takes around 10-15 seconds.
- Does the flexibility in your model prevent steric clashes between protein and ligand?
- Did you use the same timesplitting approach for training other DL-based methods as you did for FABFlex?
- Did you experiment with different pocket site radii, such as 10 Å or 5 Å, in addition to 20 Å?
- Are the alpha values learnable, or do you use a predetermined approach for them?

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
4

### Summary
This paper introduces FABFlex, a framework for fast and accurate blind flexible docking. It consists a pocket identification module (blind), a ligand conformation prediction module (docking), and a protein flexibility modeling module (flexible).  FABFlex achieves sota results on  blind flexible docking benchmark, and is 208x faster than previous sampling-based deep learning methods.

### Strengths
1. The paper is well-written, with clearly designed figures and thorough explanations of each component.

2. The experiments, ablation studies, and visualizations are comprehensive and well-detailed.

3.  The framework demonstrates strong performance and significantly faster inference times compared to sampling-based approaches.

### Weaknesses
1. The primary concern is that this work appears to be a direct application of the FABind series. It just introduces an additional pocket conformation prediction module to handle the flexible docking setting, which limits the overall contribution and novelty of the paper.


### Questions
1. Why does this paper focus solely on blind (global) flexible docking, instead of exploring pocket-based (local) flexible docking? It seems feasible to adapt the framework to a local flexible docking setting and compare it against models such as DiffDock-Pocket[1], ReDock[2], FlexPose[3], and DiffBindFR[4]. 

[1] Plainer, Michael, et al. "DiffDock-Pocket: Diffusion for Pocket-Level Docking with Sidechain Flexibility." NeurIPS 2023 Workshop on New Frontiers of AI for Drug Discovery and Development.

[2] Huang, Yufei, et al. "Re-Dock: Towards Flexible and Realistic Molecular Docking with Diffusion Bridge." Forty-first International Conference on Machine Learning.

[3] Dong, Tiejun, et al. "Equivariant flexible modeling of the protein–ligand binding pose with geometric deep learning." Journal of Chemical Theory and Computation 19.22 (2023): 8446-8459.

[4] Zhu, Jintao, et al. "DiffBindFR: an SE (3) equivariant network for flexible protein–ligand docking." Chemical Science 15.21 (2024): 7926-7942.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes FABFlex, a regression-based model for fast and accurate docking of protein-ligand pairs. The pipeline of blind flexible docking is decomposed of three stages: 1) predicting the binding pockets, 2) predicting the holo structure of ligand and 3) predicting the holo structure of receptor pockets. An iterative update mechanism is utilized for continuous structure refinement. Solid experimental results verify the superiority of FABFlex in terms of ligand prediction, pocket prediction and inference efficiency.

### Strengths
1. At a time when diffusion is prevalent, the work verifies the efficacy of iterative update mechanism for structure refinement, which achieves extremely high efficiency and better experimental results.
2. Very solid experimental results are reported to show the superiority of FABFlex, including multiple tasks of interest in blind docking and various strong baselines.

### Weaknesses
1. Although good experimental results were achieved, the innovation of this work is relatively insufficient (e.g., using existing network architectures and training objectives), which is only reflected in the proposed iterative update mechanism. The core architecture relies heavily on existing components, and the modifications, while effective, do not represent a significant departure from established methods. The iterative update, while novel in this context, is a relatively straightforward application of existing iterative refinement techniques, and the paper lacks a deep analysis of why this specific approach was chosen over other possible iterative strategies.
2. In some tasks, the results of FABFlex are worse than those of some models based on protein rigidity prior (e.g., pocket prediction performance in Table 2). This anomaly requires further explanation. Specifically, the fact that models explicitly trained with a rigidity assumption outperform FABFlex in pocket prediction raises questions about the robustness of the proposed method. The paper does not adequately explore the potential reasons for this performance discrepancy, such as the impact of the flexible docking objective on the pocket prediction module or the potential for overfitting to the flexible docking task at the expense of pocket prediction accuracy.

### Questions
1. In Table 2 we see that FABind and FABind+ achieve best results on some metrics, which seems somewhat counterintuitive since they are tailored based on the assumption of protein rigidity. Could you please give futher explanations of this phenomenon?
2. In Table 3, the ablation of "iterative internally" shows better results on mean and median of ligand RMSD. I wonder if there is room for further improvement in protein-ligand interaction modeling.

### Soundness
4

### Presentation
4

### Contribution
3
