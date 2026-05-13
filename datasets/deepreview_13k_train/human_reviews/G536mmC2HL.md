# TorSeq: Torsion Sequential Modeling for Molecular 3D Conformation Generation

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
In the realms of chemistry and drug discovery, the generation of 3D low-energy molecular conformers is critical. While various methods, including deep generative and diffusion-based techniques, have been developed to predict 3D atomic coordinates and molecular geometry elements like bond lengths, angles, and torsion angles, they often neglect the intrinsic correlations among these elements. This oversight, especially regarding torsion angles, can produce less-than-optimal 3D conformers in the context of energy efficiency. Addressing this gap, we introduce a method that explicitly models the dependencies of geometry elements through sequential probability factorization, with a particular focus on optimizing torsion angle correlations. Experimental evaluations on benchmark datasets for molecule conformer generation underscore our approach's superior efficiency and efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper showed that torsion angles in a molecular is related and proposed a model named TorSeq which uses LSTM for sequential torsion angle prediction. Compared with the torsional diffusion's backbone, authors argued that LSTM models can explicitly model the interrelations between the torsion angles by imitation of decomposition of conditional probabilities. Such highlight of the model of interrelations can enhance the performance. Experiments show that TorSeq outperforms multiple baseline methods in terms of both effeciency and accuracy.

### Strengths
1. Efficacy Demonstrated through Experimental Results: Empirical evidence substantiates TorSeq's exceptional efficiency when juxtaposed with other extant methods. This compelling empirical validation underscores the robustness of TorSeq as a pertinent solution within the domain of interest.

2. Innovative Resolution of the Gradient Vanishing Problem: TorSeq introduces an interesting strategy for mitigating the gradient vanishing problem, representing a novel and noteworthy contribution to the field. The simplicity of this method belies its effectiveness in surmounting a challenge that has previously posed significant impediments to progress.

### Weaknesses
The primary contribution of this research paper lies in the proposition of an enhanced method for the more accurate prediction of torsion angles, which takes into account their interrelations. A mere reliance on the decomposition of conditional probability and the simplistic application of LSTM appears insufficient in addressing the intricacies inherent in modeling torsion angles. Consequently, there exist notable limitations and inadequacies associated with such an approach, which warrant discussion and exploration.

1. About explicit and implicit: The authors contend that earlier models have predominantly employed implicit mechanisms to capture the correlations among torsion angles. In contrast, the utilization of a RNN to emulate conditional probability enables the explicit modeling of these correlations. It is apparent that the principal disparity between the proposed model and its predecessors lies in the emphasis on explicit modeling through conditional probability. Nonetheless, it is noteworthy that previous models can also be interpreted as involving conditional prediction and, consequently, the explicit modeling of such correlations. A more comprehensive analysis is warranted to delineate the differentiating aspects of the proposed model in comparison to the antecedent approaches.

2. About highlights on adjacent torsion angles: The authors have emphasized the importance of highlighting the interdependence among torsion angles, particularly those that are adjacent to one another. However, a thorough examination of the proposed model reveals a lack of explicit emphasis on this characteristic. As an illustrative example, one can refer to Figure 3, where the authors suggest that the relationship between the torsion angles $\tau_4$ and $\tau_7$ should be accentuated, given their adjacency to the chemical moiety c1nnc. Nevertheless, in the case of LSTM employed in the model, there is a paucity of specific information to robustly establish a strong connection between $\tau_4$ and $\tau_7$. Given that most adjacent torsion angles in a molecule are also adjacent in the torsion angle sequence, LSTM may inadvertently overlook the correlation between $\tau_4$ and $\tau_7$ in such instances. This leads to the conclusion that the explicit representation of torsion angle correlations in the proposed model is arguably inadequate. It is posited that the integration of an attention mechanism may address these concerns, yet the paper lacks a detailed analysis of this potential solution.

3. About conditional probability: While Equation 2 is unquestionably mathematically sound, it fails to account for the potential presence of a ``dominant'' torsion angle within a molecule. It is conceivable that certain torsion angles exert a significant influence on the overall structure, while others exhibit limited dependencies to each other. In scenarios where such a dominant torsion angle is positioned at the rear end of the torsion angle sequence, the predictive accuracy for other torsion angles may be compromised.

### Questions
1. Object of modeling: To create conformations, it is essential to have access to both torsion angles and local structures. Equation 1 posits the primary objective as the generation of torsion angles based on a given molecular graph. This raises the question of how the local structures are acquired prior to predicting the torsion angles. Is it necessary to employ a tool like RDKit to generate these local structures, akin to the methodology employed in Torsional Diffusion?

2. Distinguishing prediction and generation tasks: In Equation 1, the author characterizes the task as a generative one. However, ensuring that the generated torsion angles faithfully adhere to the distribution of the dataset presents a significant challenge. How can we establish the veracity of the claim that the generated torsion angles indeed conform to the dataset's distribution?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
this paper propose TorSeq for MCG task,which introduce an artificial torsional sequence enabling explicitly modeling interrelations among torsion angles. results in GEOM also show effectiveness and efficiency of the proposed methods.

### Strengths
propose a sequential based MCG method, which predict low energy torsion, also this method can intergate with torsion diffusion.

### Weaknesses
Autoregressive generation is less novelty, also experiment gain is not signicfiant enough ( compare with serval SOTA DL based models).

As mentioned in recently works[https://arxiv.org/pdf/2310.14782.pdf], `a recent approach combining ETKDG with clustering (Zhou et al.,
2023), which was shown to outperform most existing machine learning methods in the low energy conformation generation task.` 
I believe that a more in-depth discussion on this topic is warranted, particularly regarding the usefulness and informativeness of the datasets employed for general molecular conformation generation or try to generate pure GFN2-xTB level(semi-DFT as in GEOM-Drugs) conformation is enough?

### Questions
As mentioned in recently works[https://arxiv.org/pdf/2310.14782.pdf], `a recent approach combining ETKDG with clustering (Zhou et al.,
2023), which was shown to outperform most existing machine learning methods in the low energy conformation generation task.` 
I believe that a more in-depth discussion on this topic is warranted, particularly regarding the usefulness and informativeness of the datasets employed for general molecular conformation generation or try to generate pure GFN2-xTB level(semi-DFT as in GEOM-Drugs) conformation is enough?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to model ligand torsions with LSTM.

Specifically, it 1) finds a way of extracting torsions as a sequence; 2) build torsion features with inputs and GNN features; and 3) tries to add diffusional training to the pipeline.

Experiments shows that the generated conformations are in good quality, in different senses.

### Strengths
1. Shown metrics are elevated compared with listed baselines.

2. The method is fast.

3. Not many research explored to model torsions as sequences so at least the paper is a novel exploration.

### Weaknesses
0. Overall the method does not seem to be interesting to the majority of the community. Pure Mol. Conf. Gen does not lead to any direct applications, and the general interest of the community is now moving to more challenging tasks. I would suggest the authors to demonstrate the usage of their model in some scenarios with real applications, such as trying their methods in docking.

1. Modelling torsion angles with LSTM is generally not a good idea. The permutation issues should be very carefully addressed, also the interactions in-between may not be fully explored (compared with using Transformer).

2. Recent work [1] shows that when used appropriately RDKit itself is a strongest baseline in conformation generation. It has better reported COV and MAT compared with this one. This hinders the significance of speeding up in this paper.

3. Technical details are not good. Sources of Figure data are not articulated (Fig2/4). Benmark performance, especially for GEOM-DRUGS, are not directly comparable to a majority of works in the community.

### Questions
1. Why is LSTM a better choice than Transfomers? And how is the permutation issue dealed in this work? The canonical order derived from SMILES seems to be artificial. At least data augmentation tricks shall be leveraged.

2. Please explain the sources of data in Fig2/4.

3. I would expect some visualization to justify why the work is better than other baselines such as [1]

4. Analysis in steric clashes is required.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces TorSeq, a new method for 3D molecular conformation generation that focuses on predicting torsion angles between atoms using sequential probability factorization and LSTM networks. A key innovation is the modeling of dependencies between torsions. The method also incorporates a novel random torsion angle deviation during training to avoid vanishing gradients. Experiments demonstrate state-of-the-art accuracy and efficiency for TorSeq over existing methods like OMEGA on standard benchmarks.

### Strengths
The paper is well-written and presents the impressive runtime of TorSeq, which is indeed remarkably fast. The experiments conducted are comprehensive, featuring evaluations on two benchmark datasets, comparisons to numerous state-of-the-art baselines, and ablation studies. Furthermore, the authors have made the code and datasets publicly available, fostering reproducibility in the field.

### Weaknesses
 - The related work section appears insufficient, as only three previous studies are mentioned. A more comprehensive review of the literature would strengthen the paper.
- The proposed method does not seem to outperform "Torsional Diffusion" as a standalone technique. While combining it with "Torsional Diffusion" yields better results than "Torsional Diffusion" alone, the increased runtime compromises its efficiency. Thus, the paper's claim of achieving both effectiveness and efficiency is not well-supported, as a trade-off exists between the two.
- A key aspect of TorSeq is defining a suitable sequence of torsions to capture structural dependencies. Relying on SMILES ordering is a straightforward yet imperfect solution, as the model may underperform or fail if torsions are provided in an incorrect or suboptimal order. The authors should analyze the sensitivity of their approach to changes in the torsion sequence more thoroughly.
- The paper focuses on single conformation generation, which is not as relevant as generating Boltzmann distributions, considering that low-energy states form a Boltzmann distribution rather than a single state. Recent works like [1], [2], and [3] have explored Boltzmann distribution generation. The paper's emphasis on maximum likelihood training on the GEOM dataset does not guarantee sampling proportionally to the Boltzmann distribution, making the approach outdated and less interesting.
- The paper should include a more extensive comparison with baseline methods, as only a few are currently examined.

### Questions
- How sensitive is the model's performance to variations in the SMILES format or the canonicalization method employed for determining torsion order?
- Can you suggest and assess alternative approaches for defining the torsional sequence, such as using 3D distances? How does the model's accuracy change if torsions are supplied in a random order rather than in the SMILES order?
- Is it possible to enhance the LSTM dependency modeling with positional encodings or attention mechanisms to reduce reliance on sequence order?
- Have you explored any data augmentation techniques during training, like altering the torsion order?
- I recently came across this paper [1] and noted that the performance of simple RDKit + Clustering from [2] is quite impressive. Could you include it as a baseline for comparison?

[1] Towards equilibrium molecular conformation generation with GFlowNets.
[2] Do deep learning methods really perform better in molecular conformation generation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
