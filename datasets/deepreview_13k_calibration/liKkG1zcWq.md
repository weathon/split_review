# Sliced Denoising: A Physics-Informed Molecular Pre-Training Method

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 5, 5, 8

## Abstract
While molecular pre-training has shown great potential in enhancing drug discovery, the lack of a solid physical interpretation in current methods raises concerns about whether the learned representation truly captures the underlying explanatory factors in observed data, ultimately resulting in limited generalization and robustness. Although denoising methods offer a physical interpretation, their accuracy is often compromised by ad-hoc noise design, leading to inaccurate learned force fields. To address this limitation, this paper proposes a new method for molecular pre-training, called sliced denoising (SliDe), which is based on the classical mechanical intramolecular potential theory. SliDe utilizes a novel noise strategy that perturbs bond lengths, angles, and torsion angles to achieve better sampling over conformations. Additionally, it introduces a random slicing approach that circumvents the computationally expensive calculation of the Jacobian matrix, which is otherwise essential for estimating the force field. By aligning with physical principles, SliDe shows a 42\% improvement in the accuracy of estimated force fields compared to current state-of-the-art denoising methods, and thus outperforms traditional baselines on various molecular property prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
the paper introduces "sliced denoising" (slide), a novel molecular pre-training method that enhances the physical interpretation of molecular representation learning. traditional denoising methods, though physically interpretable, can suffer from inaccuracies due to ad-hoc noise design, leading to imprecise force fields. slide addresses this by utilizing classical mechanical intramolecular potential theory, leading to a 42% improvement in force field estimation accuracy over existing methods.

### Strengths
1. innovative approach: slide introduces an innovative noise strategy (bat noise) and a random slicing technique. this approach significantly enhances the accuracy of force field estimations, making it a pioneering method in the field.

1. alignment with physical principles: the method closely aligns with classical mechanical intramolecular potential theory. it appears to improve the realism of molecular representations as well as help that learned representations are physically interpretable, a critical aspect in molecular sciences.

1. empirical validation: slide demonstrates empirically strong results in force field estimation accuracy and downstream task performance on benchmark datasets qm9 and md17.

1. methodology: the paper combines theoretical soundness with methodological innovations effectively. the use of a quadratic energy function approximation and the consequent noise strategy is interesting.

1. network architecture integration: integrating a transformer-based network architecture that encodes relative coordinate information is a notable strength. this architectural choice complements the novel denoising method, enhancing its adaptability to other works using transformer backbones.

### Weaknesses
1. computational complexity: while the random slicing technique addresses computational challenges associated with jacobian matrix estimation, the overall computational demand and efficiency, especially in large-scale applications, are not comprehensively addressed​​​​​​. Specifically, the paper does not provide a detailed analysis of how the computational cost of the sliced denoising method scales with the size of the molecules and the number of atoms. The method relies on a quadratic energy function approximation and the calculation of the Hessian matrix, which can be computationally expensive for large systems. The paper should include a discussion of the practical limitations of the proposed method in terms of computational resources and time. 

1. robustness to noisy data: the robustness of slide to noisy or imperfect real-world data is not thoroughly examined. this aspect is crucial for practical applications where data quality can vary significantly​​. The paper lacks a discussion on how the method would handle deviations from ideal equilibrium structures, which is a common scenario in experimental data. The current evaluation is primarily focused on clean, curated datasets, and further investigation is needed to assess the method's performance in more realistic and challenging settings. It's unclear how the method's performance would degrade with increasing levels of noise in the input data, and what preprocessing steps might be necessary to mitigate these issues.

### Questions
1. regarding computational efficiency: can the authors provide more details on the computational requirements of slide, especially when applied to large molecular datasets? how does its computational efficiency compare to existing methods?

2. on generalizability and applicability: what are low-hanging fruits to test the generalizability of slide to other types of geometric data or applications beyond molecular science? how might the method need to be adapted for such scenarios?

3. empirical validation across diverse datasets: could the authors elaborate on potential plans to validate slide on a broader range of datasets, particularly those that may present different challenges than qm9 and md17, such as des15k or oc20 as in the coord paper https://arxiv.org/abs/2206.00133?

a curiosity question:
1. dependence on equilibrium structures: the method's reliance on equilibrium structures, to be clear same as most other methods in this space, for training may limit its effectiveness in scenarios where such structures are not readily available or accurate. are there ways to advance molecular representation learning in such a setting?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel approach to molecular pre-training called Sliced Denoising (SliDe) that leverages physical principles to improve molecular property prediction. The authors introduce a new noise distribution strategy that improves sampling over conformations and a denoising task that learns the force field of the energy function. They evaluate SliDe on benchmark datasets QM9 and MD17 and show that it outperforms traditional baselines in terms of physical consistency and molecular property prediction accuracy.

### Strengths
The main contribution of the paper, the pre-training algorithm, seems to be extremely relevant to the drug discovery domain with the magnitude of improvement achieved across all benchmark tasks. The paper could be of great interest to scientists in this area. 

The pre-training method introduced leverages physical principles and is more interpretable. In addition, the experimental results seem very thorough.

### Weaknesses
While the paper is interesting, and makes an important contribution to the field of drug discovery, I would like to raise the question of if ICLR is the correct venue for this submission. This is an important area, and there will be a subset of audience interested in the field, but I would assume that a broader audience will have trouble understanding the paper due to the about of domain knowledge involved. I will leave it to the AC to determine this.

I found the paper hard to read and understand due to the amount of domain knowledge involved. I understand that it is not possible to introduce all the background information in 8 pages, but I would urge the authors to rewrite the paper in a more accessible way for non-domain but ML experts.

### Questions
NA

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new pre-training method, Slide, that is based on intramolecular potential theory. To lower the computational expense of Slide, the authors introduce a random slicing approach. In addition, a new MLFF architecture is introduced (GET).

### Strengths
Strength 1: The writing and motivation of this paper is very clear, with a good description of related works.

Strength 2: Molecular pre-training is an important problem which the authors propose a novel approach for.

### Weaknesses
Weakness 1 (Major): The baselines used in this paper are not up to date. In fact, Gemnet (2021) and Nequip (2022) can outperform Slide on basically all of the MD17 and require no pre-training. In addition, the authors claim they set a new state of the art on these benchmarks, which is incorrect. The comparison to NequIP is particularly problematic, as the authors do not specify which variant of NequIP they are comparing against. NequIP has multiple configurations, including different orders of spherical harmonics, which significantly impact performance. The authors should clarify the specific NequIP model used and ensure a fair comparison. Furthermore, the claim of achieving state-of-the-art results on MD17 is misleading, as the authors only achieve SOTA on a small subset of molecules, specifically uracil and toluene. This overstatement needs to be corrected to accurately reflect the paper's contributions.

Weakness 2 (Major): For the downstream task only one random seed is used and the gains over other methods are relatively minor (i.e. compared to Coord and Frad). This makes me doubt that the results are really significant or if they are just due to tuning. I think that multiple random seeds should be reported. The lack of statistical significance testing further compounds this issue. The authors should provide statistical analysis, such as t-tests or ANOVA, to demonstrate that the observed improvements are not due to random chance. The current presentation of results makes it difficult to ascertain whether the gains are truly meaningful.

Weakness 3 (Minor): Showing the best result over random seeds in table 1 is kind of strange. I think that the mean result should be shown.

### Questions
Question 1: How does your slicing method related to sliced score matching [1]?

[1] Song, Yang, et al. "Sliced score matching: A scalable approach to density and score estimation." Uncertainty in Artificial Intelligence. PMLR, 2020.

Question 2: How does the scale of the pre-training data effect performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed a improved denoising pretraining method for 3D GNN in molecular machine learning tasks. The proposed method, called sliced denoising (SliDe), is inspired by classical intramolecular potential theory. SliDe adds different levels of noise to the length of bonds, the magnitude of angles, and the magnitude of torsion angles. Through a series of theoreticall derivation, the authors demonstrate the equivalence of SliDe method and learning the molecular force field. Lastly, the authors show that the SliDe has outperformed previous denoising training methods on the QM9 and MD17 dataset.

### Strengths
1. Comparing to previous work such as the Fractional Denoising, the noise designing of this work is a more "physical" formulation because changing either one of the bond length, angle degree, or torsion angle degree does not affect the rest. 

2. The writing and proof process are of high clarity. 

3. Some efforts to the direction of explainablity are interesting. For example, the correlation coefficient between the learned force field and ground-truth force field (Table 1) is a nice way to quantified the learned force field.

### Weaknesses
1. In section 3.1, the claim above Eq. 6 is not correct. Modeling long-range electrostatic (coulomb) interaction is critical in many areas including energy calculation and md simulation. For large system, long-range vdW outside of a cutoff distance may be neglected, but for small molecules in QM9 and MD17, it should not be neglected. When using GNN that takes 3D coordinate and atom type as input approximate energy function, the model should be able to learn those two terms, thus not affecting the approximation of Eq.6. However, the authors should rephrase the sentence. The two citations associated with the sentence does support the claim so they should be removed.

2. The noise design is very import in this work. In the BAT noise (Eq. 9), the parameter vectors are critical but there isn't detailed explaination of them. The authors briefly discussed in the section C.1, but I do think more details and example of those parameter vectors can substentially help reader in understanding the noise design. 

3. Missing parenthesis in the second exponential term of Eq. 8. $(\theta_{i} - \theta_{i, 0})^2$

4. I do think the superiority of the SliDe method can be strengthen by more downstream experiments, especially energy prediction. For example, the ANI-1x dataset (www.nature.com/articles/s41597-020-0473-z) is a excellent dataset for such task.

### Questions
1. Table 7 is confusing. My understanding is that “Training from Scratch” meaning no pretraining, and Coord and Frad meas pretrained with different method and then fine-tuned on MD17-Aspirin. What does DFT label supervised mean? Isn’t “Training from Scratch” also supervised? The authors should elaborate. The unit of the prediction MAE should also be included in the table.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
