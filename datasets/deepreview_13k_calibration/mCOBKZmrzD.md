# EquiformerV2: Improved Equivariant Transformer for Scaling to Higher-Degree Representations

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Equivariant Transformers such as Equiformer have demonstrated the efficacy of applying Transformers to the domain of 3D atomistic systems. 
However, they are limited to small degrees of equivariant representations due to their computational complexity.
In this paper, we investigate whether these architectures can scale well to higher degrees.
Starting from Equiformer, we first replace $SO(3)$ convolutions with eSCN convolutions to efficiently incorporate higher-degree tensors. 
Then, to better leverage the power of higher degrees, we propose three architectural improvements -- attention re-normalization, separable $S^2$ activation and separable layer normalization.
Putting this all together, we propose EquiformerV2, which outperforms previous state-of-the-art methods on large-scale OC20 dataset by up to $9\%$ on forces, $4\%$ on energies, offers better speed-accuracy trade-offs, and $2\times$ reduction in DFT calculations needed for computing adsorption energies.
\revision{Additionally, EquiformerV2 trained on only OC22 dataset outperforms GemNet-OC trained on both OC20 and OC22 datasets, achieving much better data efficiency.}
\revision{Finally, we compare EquiformerV2 with Equiformer on QM9 and OC20 S2EF-2M datasets to better understand the performance gain brought by higher degrees.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose EquiformerV2, which incorporates eSCN convolutions to efficiently include higher-degree tensors and introduces three architectural improvements: attention re-normalization, separable $S^2$ activation, and separable layer normalization. These enhancements allow EquiformerV2 to outperform state-of-the-art methods across OC20 and OC22.

### Strengths
- One of the significant contributions of this paper is the comprehensive experiments across OC20, OC22, and QM9. And EquiformerV2 achieves the state-of-the-art result over OC20 and OC22. The authors deserve commendation for their efforts in this aspect.
- The use of attention re-normalization, separable $S^2$ activation, and separable layer normalization is novel.

### Weaknesses
Major:
- Although the authors did a fantastic job on the experiments, EquiformerV2 is an incremental improvement over existing methods of both eSCN and Equiformer w.r.t. theory. And the novelty lies in those three specific techniques and enhancements. To see if these techniques are generalizable, I would like to see the ablation study of attention re-normalization, separable $S^2$ activation, and separable layer normalization, respectively, on the QM9 dataset like what the authors did in Table (a) for OC20.

Minors:
- Equation (2) in Appendix A.1: Use $\ddots$ instead of $\dots$
- Equation (4) in Appendix A.3: Commonly, the left side of an equation is used for assigning new notation. I recommend write $D^{(L)} = D^{(L)}(R_{ts})$ and $\tilde{x}_s^{(L)} = D^{(L)} x_s^{(L)}$ for a degree $L$ before Equation (4).

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
EquiformerV2 is proposed to improve the efficiency of Equiformer on higher-degree tensors. 
To achieve this, original tensor product (TP) with spherical harmonics is changed to eSCN convolution which can reduce the complexity from $O(L^6)$ to $O(L^3)$.
Besides, three archtecture module is replaced to improve the performance in attention normalization, nonlinear activation and layer normalization.

### Strengths
The empirical results of EquiformerV2 is great. It achieves SOTA performance on OC20 and OC22, where higher-degree tensor shows great improvement. Meanwhile, the efficiency is denoted in Figure 4 showing that EquiformerV2 can has better efficient ability than eSCN.

### Weaknesses
The modification of proposed architecture is similar to the previous Equiformer. Although the ablation studies show the improvement of proposed modules, the results on QM9 is similar compared to Equiformer.



### Questions
Minor issue:
There is a double citation. Gao Huang, Yu Sun, Zhuang Liu, Daniel Sedra, and Kilian Q. Weinberger. Deep networks with stochastic depth. In European Conference on Computer Vision (ECCV), 2016a.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors proposed EquiformerV2, which is a newly developed equivariant network for 3D molecular modeling built on the Equiformer. From the experimental evaluation, the EquiformerV2 model achieved strong performance on the large-scale OC20/OC22 benchmark, QM9 dataset and also the new AdsorbML dataset. Such performance improvement upon Equiformer is achieved via several architectural modifications: (1) levering eSCN's efficient SO(2) convolution implementation for SO(3) convolutions (tensor product operations); (2) Attention Re-normalization for stabilizing training; (3) Separable S2 activation for mixing representations with different degrees; (4) separate Layer Normalization.

### Strengths
1. **Regarding the problem studied in this paper**. By leveraging the key techniques from eSCN, the EquiformerV2 also achieves learning irreducible representations with larger maximum degrees, which has been verified again to be useful for large-scale DFT benchmarks.

2. **Regarding the empirical performance**. In the OC20 benchmark, EquiformerV2 sets a new standard by delivering state-of-the-art performance in the Structure-to-Energy-Force task. The model, further trained on this task, effectively serves as a force-field evaluator, demonstrating impressive performance in both IS2RS and IS2RE tasks. EquiformerV2 surpasses the performance of the compared baselines across all tasks, with a notable edge in force prediction. Furthermore, it significantly enhances the success rate on the AdsorbML dataset.

### Weaknesses
The novelty of the proposed architectural modifications is limited. Both the efficient SO(2) convolution and S^2 activation are from eSCN, while the attention re-normalization and layer normalization are more like engineering tricks. Among these differences from Equiformer, the eSCN SO(2) convolution plays an essential role in enabling the use of irreducible representations of higher degrees, and the S^2 activation also replaces all non-linear activations. In fact, these design strategies should be mainly credited to the eSCN work.

### Questions
See the comments in the Weaknesses section

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
