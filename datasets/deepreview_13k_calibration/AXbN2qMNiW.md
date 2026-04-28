# Protein-ligand binding representation learning from fine-grained interactions

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
The binding between proteins and ligands plays a crucial role in the realm of drug discovery. Previous deep learning approaches have shown promising results over traditional computationally intensive methods, but resulting in poor generalization due to limited supervised data. In this paper, we propose to learn protein-ligand binding representation in a self-supervised learning manner. Different from existing pre-training approaches which treat proteins and ligands individually, we emphasize to discern the intricate binding patterns from fine-grained interactions. Specifically, this self-supervised learning problem is formulated as a prediction of the conclusive binding complex structure given a pocket and ligand with a Transformer based interaction module, which naturally emulates the binding process. To ensure the representation of rich binding information, we introduce two pre-training tasks, i.e.~atomic pairwise distance map prediction and mask ligand reconstruction, which comprehensively model the fine-grained interactions from both structure and feature space. Extensive experiments have demonstrated the superiority of our method across various binding tasks, including protein-ligand affinity prediction, virtual screening and protein-ligand docking.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a representation learning approach for protein-ligand interactions in a self-supervised learning manner. Inspired by the insufficiencies of previous methods in addressing the interaction module between proteins and ligands, this paper employs a Transformer-based interaction module, designed to emulate the binding process. In addition, the paper suggests two pre-training strategies to optimize the Transformer-based module. The first strategy is an atomic pairwise distance map prediction, grounded in the understanding that various interactions between proteins and ligands correlate with their inter-molecular distances. The second strategy is a mask ligand reconstruction within a feature space, rather than based on atom type, to capture the conditional dependencies between proteins and ligands.

### Strengths
- It empirically shows various experiments for protein-ligand binding
- It achieves good performance through simple but effective loss based on the domain knowledge

### Weaknesses
 * As the major argument of the paper is regarding the capturing of the **interactions** through a Transformer-based interaction module, analysis on the interactions and its consequence should have been provided (e.g., specific types of interactions captured by this new module), which are missing in the paper.
* While it contends that they present a Transformer-based interaction module, the explanation provided is notably insufficient.
* The authors argue that the framework is flexible, allowing for the integration of various pre-existing encoders for proteins and ligands. However, for the distance matrix associated with the atomic pairwise distance map prediction, it appears to necessitate a pair representation in the Uni-Mol. In other words, the architecture seems to be tailored specifically for Uni-Mol.
* If the system is indeed flexible, there should be experimental evidence presented with other encoders.

### Questions
* BindNet was pre-trained using BioLip. However, were the other baseline models also pre-trained on BioLip? Notably, the pre-trained model weights for Uni-Mol, available on their GitHub, seem to have utilized other datasets. If Uni-Mol, initially pre-trained on other datasets, was subsequently pre-trained using BioLip, this could create an inequity with the other baselines due to the discrepancy in the number of datasets used for pre-training.
* Did the other baseline models use the primary state for ligands in experiments?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper present a new training methodology with two novel training loss: the atomic pairwise distance prediction and mask ligand reconstruction. The trained model then fine-tuned on down-stream tasks like binding affinity prediction and virtual screening. The experimental results seem encouraging.

### Strengths
- Overall, the paper is clearly represented.
- The authors conducted multiple down-stream tasks to verify the efficacy of their method.

### Weaknesses
 - The authors claim that it is a "self-supervised" method, but actually the pocket-ligand complex data are still required for pre-training. So, the data volume is limited by this requirement.  For example, only 458k BioLip data is used for pre-training, and thus earlier stage pretraining like UniMol is required.

 - Another concern is about label leakage. Is there any overlap between the BioLip and downstream datasets (LBA, DUD-E, PDBBind, etc.)?

 - The authors claim that "a variety of pre-existing encoders for pockets and ligands can be utilized. ", but only Uni-Mol used in experiments.

 - Using RDKit to build the primary state is not accurate and sometimes even fail. The authors are encouraged to use more advanced methods for this.

### Questions
- What is the " N-layer 3D-invariant Transformer" used in the paper? The authors should provide more details about this part.
- How to choose the mask ratio in MLR? The 0.8 seems to be a very high value.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel approach named BindNet, designed for the pretraining of protein and ligand 3D representations. This method leverages two core objectives:

    Utilizing 3D representations of proteins and ligands sourced from Uni-Mol, BindNet aims to predict the pairwise atomic distances between atoms within a ligand-protein 3D complex.

    BindNet also employs protein 3D representations from Uni-Mol to predict masked ligand 3D representations, also obtained from Uni-Mol.

Both of these tasks are initially pretrained on a subset of the BioLiP dataset. Subsequently, the resulting protein and ligand representations are fine-tuned for tasks such as binding affinity prediction (LBA 30%, LBA 60%, LEP), virtual screening (DUDe, AD), and docking (CASF-2016). The performance of BindNet is compared against several baseline methods including UniMol, CoSP, GeoSSL, DeepAffinity, and SMT-DTA.

The study demonstrates that BindNet outperforms these baseline methods significantly in various downstream tasks. Additionally, the authors conduct an analysis to determine the importance of each pretraining objective in the process of representation learning.

While the experimental results are interesting, there are some concerns regarding the adequacy of leakage controls, a lack of comparison to stronger baselines, and the overall reproducibility of the research.

### Strengths
The experimental findings are interesting. It's the first time I've encountered a research work where the 3D protein-ligand complex is harnessed to learn a unified representation for both proteins and ligands, which has promising implications for practical binding affinity prediction.

Both of the proposed objectives for acquiring this joint representation yield compelling results, despite their simplicity. The paper is excellently written and presents a comprehensible narrative. The experiments encompass a wide range of tasks, including affinity prediction, docking, and virtual screening, and they feature thorough comparisons against numerous baseline techniques, including state-of-the-art methods in the field.

### Weaknesses
I hold a significant concern regarding the potential data leakage in the evaluation process. It appears that the representations learned from BioLiP, which contains a subset of PDBind used for validating the results, may introduce a form of leakage, thus giving pretrained methods an advantage over other baseline techniques. To address this, it is advisable to consider re-executing the experiments with the exclusion of all overlapping data between BioLiP and the downstream tasks, including overlaps with datasets for binding affinity prediction (LBA 30%, LBA 60%, LEP), virtual screening (DUDe, AD), and docking (CASF-2016).

Furthermore, I recommend including state-of-the-art protein representations like ESM-2 and ESM-1b (accessible at https://github.com/facebookresearch/esm), molecular representations such as MolFormer (available at https://github.com/IBM/molformer), and simple yet effective drug representations like Morgan fingerprints as baseline representations for a more comprehensive comparison. Specifically, the absence of comparisons against sequence-based protein representations like ESM-2 and ESM-1b is a significant oversight, given their demonstrated effectiveness in various protein-related tasks. Similarly, the lack of comparison with advanced molecular representation methods such as MolFormer, which leverages transformer architectures for molecular encoding, limits the scope of the evaluation. The inclusion of Morgan fingerprints, a widely used and computationally efficient method, would also provide a valuable baseline for comparison.

Another significant concern is the reproducibility of the work. The absence of available code, missing details regarding hyperparameter settings, and the lack of transparency in releasing experimental settings, including dataset splits and configurations for downstream tasks, hinder the reproducibility of the research. Addressing these issues would greatly enhance the credibility and transparency of the work.

### Questions
1. Could you please kindly consider removing the potential leakage as advisable in the weakness discussion and release new results without leakage?
2. Could you please kindly include the comparison to state-of-the-art protein representations like ESM-2 and ESM-1b and molecular representations such as MolFormer and  Morgan fingerprints as baseline representations for a more comprehensive comparison?
3. Could you please kindly work-out on the reproducibility as advisable  the weakness discussion?

I would be very happy to consider revising my score when all the requests above are fulfilled.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
