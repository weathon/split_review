# EquiPocket: an E(3)-Equivariant Geometric Graph Neural Network for Ligand Binding Site Prediction

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Predicting the binding sites of target proteins plays a fundamental role in drug discovery. 
Most existing deep-learning methods consider a protein as a 3D image by spatially clustering its atoms into voxels and then feed the voxelized protein into a 3D CNN for prediction. However, the CNN-based methods encounter several critical issues: 1) defective in representing irregular protein structures; 2) sensitive to rotations; 3) insufficient to characterize the protein surface; 4) unaware of protein size shift. To address the above issues, this work proposes EquiPocket, an E(3)-equivariant Graph Neural Network (GNN) for binding site prediction, which comprises three modules: the first one to extract local geometric information for each surface atom, the second one to model both the chemical and spatial structure of protein and the last one to capture the geometry of the surface via equivariant message passing over the surface atoms. We further propose a dense attention output layer to alleviate the effect incurred by variable protein size. Extensive experiments on several representative benchmarks demonstrate the superiority of our framework to the state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a novel method for protein binding site predictions. 
To address the limitations of previous approaches (e.g., relying on voxelization, insensitive to se3 transformation, unaware of protein size, insufficient characterization of protein surface), the authors propose to model both the local geometrical features of surface atoms and global protein features based on chemical graphs and spatial graphs.

To account for variable protein sizes, they also devise a novel dense attention layer to aggregate representations of different encoding layers based on their importance.

They conduct extensive experiments including ablation studies to validate the effectiveness of the method.

### Strengths
1. The paper summarizes several common limitations of previous works. It seems the proposed method fairly addresses these issues according to numerical results and the story presented in the paper.

2. Modeling surface features of target proteins is of crucial importance to the success of the binding site prediction. This paper gives insights into modeling surface features. In specific, they propose a way to construct surface graphs and corresponding node features given spatial information of proteins. They also adapt the EGNN into surface-EGNN, which seems to be effective at modeling both the chemical and geometrical features of target proteins.

3. To account for the variable protein sizes, the authors propose a dense attention output layer to aggregate features from different layers according to their importance. They show via ablation study that the module is crucial to the performance.

### Weaknesses
1. My main concern is that the proposed method is unaware of the structure of ligand molecules (or proteins). In a real-world setting, the binding site of a target protein might be dependent on the ligands they bind to.

2. P2rank is a widely used package in literature (e.g., TANKBIND[1], E3BIND[2]) for locating the ligand-binding pockets based on protein structures. It is quite accurate and efficient. The authors should include it as a baseline method.

### Questions
1. What is the rationale behind Eq.3? Why do you swap the order or MLP and Pooling?
2. Can the proposed method be adapted to protein-protein binding site prediction?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a E(3)-equivariant graph neural network for ligand binding site prediction, where only the protein is given and the goal is to classify which protein atoms belong to the binding site. The model consists of a local structure modeling module, a global structure modeling module and a surface message passing module. The experiments show that the proposed method outperforms geometric-based method, CNN-based methods, 2D/3D graph-based methods with a clear margin.

### Strengths
- The proposed method shows clear superior empirical performance compared to existing methods.
- The paper is well-written and easy to follow
- The code is provided

### Weaknesses
The significance of the studied problem is limited, given lots of ligand docking prediction models and structure-based drug design models are proposed. It would be better if the authors could show how much improvement the proposed method can bring to the downstream tasks.



### Questions
- Why is relative direction prediction needed? The ablation study about this loss is needed.
- I'm a bit confused with the setting of this task. For the same protein, there may exist multiple ligands that can bind with it. Then, how are the ground-truth labels computed? If they are viewed as individual datapoints, one input protein may have multiple different sets of labels. Will it influence the training and prediction phase?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed a new method, named EquiPocket, for ligand binding site prediction. Their model contains a local geometric modeling module, a global structure modeling module and a surface passing module to gather the surface geometric and multi-level structure features in a protein. Based on the experimental results, their method showed superiority, compared with other existing methods on several real data sets.

### Strengths
The idea of using an E(3)-equivariant GNN for binding site prediction is of interest especially in the bioinformatic domain.  
Writing and presentation skill is well. 
The proposed method is relative better than previous methods, which is not lack of significance.

### Weaknesses
[1] The authors did not compare their method with latest state-of-the-art methods, such as (1).
(1) Tubiana J, Schneidman-Duhovny D, Wolfson H J. ScanNet: an interpretable geometric deep learning model for structure-based protein binding site prediction[J]. Nature Methods, 2022, 19(6): 730-739.
[2] Some details need to be clarified. For example, proteins have multiple binding sites. How did the authors select binding sites.
[3] There is a significant correlation between binding sites and the properties of small molecules, not just spatial relationships.

### Questions
[1] The authors did not compare their method with latest state-of-the-art methods, such as (1).
(1) Tubiana J, Schneidman-Duhovny D, Wolfson H J. ScanNet: an interpretable geometric deep learning model for structure-based protein binding site prediction[J]. Nature Methods, 2022, 19(6): 730-739.
[2] Some details need to be clarified. For example, proteins have multiple binding sites. How did the authors select binding sites.
[3] There is a significant correlation between binding sites and the properties of small molecules, not just spatial relationships. 
[4] The role of Dense Attention in reducing the negative impact caused by the protein size shift is limited.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an e(3)-equivariant geometric graph neural network for ligand binding site prediction. This model consists of three modules including the local/global geometric modeling module and surface message passing module, which are used to address several issues of the previous approach. The author compares their method with other methods and shows it has the best performance in terms of model parameters efficiency and accuracy.

### Strengths
1. The writing is generally great and the description of the proposed method is clear.
2. The discussion regarding the protein size shift is great.

### Weaknesses
1. Geometric aware E(3)-equivariant GNN has been applied to several very related tasks like protein-ligand docking [1]. Consequently, the novelty of introducing E(3)-equivariant GNNs may be diminished.
2. I think it might be also necessary to compare with protein-ligand docking methods as binding site prediction is one of their outputs.

### Questions
1. It would be better to also compare the inference speed of different methods. Because this approach does massage passing on full protein atoms graph, it appears the inference speed would be very slow.
2. The setting for some baseline methods (EGNN, SchNet) needs to be more clear. For example, what kinds of graphs do you use for the EGNN? Do you also use the surface atom graph?
3. A more informative ablation would involve comparing EquiPocket, EquiPocket/L, EquiPocket/R, and EquiPocket/LR, where the symbol '/' means exclude. This is because L and R appear to be two feature extractors.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
