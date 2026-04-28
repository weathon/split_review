# XiEff Representation for Near-Field Optics

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Near-field optics, or near-field electrodynamics, is a field that studies the interaction between materials and light at spatial scales smaller than the wavelength. At these extremely small scales, below the diffraction limit, the interaction between materials and electromagnetic fields can exhibit unique behaviors and properties not observed in conventional optics. This area of research is crucial for understanding the optical characteristics of nanotechnical systems and nanoscale biological objects. One of the primary tools used in near-field optics research is scanning near-field optical microscopy (SNOM), which allows researchers to measure near-field optical images (NFI). However, these images often lack visual clarity and interpretability, hindering a comprehensive understanding of the properties of the probed particles.

The main goal of this paper is to introduce a novel approach that addresses these challenges. Inspired by the prominent progress in Neural Radiance Fields (NeRFs) from computer vision and ideas from physics-informed neural networks (PINNs). We propose an unsupervised method that introduces the XiEff representation – a neural field-based reparameterization of the effective susceptibility tensor. By integrating XiEff into the Lippmann-Schwinger integral equation framework for near-field optics we develop an optimization strategy to reconstruct the effective susceptibility distribution directly from NFI data.

The optimized XiEff representation provides an interpretable and explainable model of the particle's shape. Extensive evaluations on a synthetically generated NFI dataset demonstrate the effectiveness of the method, achieving high intersection-over-union scores between XiEff and ground truth shapes, even for complex geometries. Furthermore, the approach exhibits desirable robustness to measurement noise, a crucial property for practical applications. The XiEff representation, combined with the proposed optimization framework, potentially introduces a valuable tool for enabling explainable near-field optics imaging and enhancing the understanding of particle characteristics through interpretable representations

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the problem of effective susceptibility distribution reconstruction from near-field imaging data. The idea is to use the physics-informed neural networks (PINN) to solve the Lippman-Schwinger equation given the external field observation from the SNOM probe.

### Strengths
In general, the paper is clearly written, though there are some formatting issues (such as the citation format and the section fragments) should be fixed.

### Weaknesses
The paper, however, can be viewed as an exercise of PINN for the specific near-field imaging tasks without any algorithmic innovations. Note, ICLR typically emphasizes novelty on the algorithmic side. Simply adopting an existing (and well-known) approach to a highly domain-specific problem (like the near-field imaging) would not be recommended for ICLR publication. 
I would suggest the authors further refine their paper, focus on the experiments (the experiments conducted in this paper are too toy to be attractive), and submit it to an optics/photonics journal for next-round evaluation. 
Particularly, a 3-D experimental setup with non-diagonal effective susceptibility would be interesting to be explored, in contrast to the 2D, diagnonal cases tested in the paper.

### Questions
See above

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a method, termed XiEff Representation, for reconstructing particle shapes from near-field optical images obtained through Scanning Near-Field Optical Microscopy. The approach leverages neural fields inspired by Neural Radiance Fields (NeRF) and Physics-Informed Neural Networks (PINNs) to parameterize the effective susceptibility tensor within the Lippmann-Schwinger equation framework. The authors propose this technique as an interpretable model for particle shape reconstruction, particularly under noisy conditions, using an unsupervised optimization framework.

### Strengths
This approach adapts NeRF and PINNs, for effective shape reconstruction in nano-optics; and shows robustness in noise on a synthetic dataset with various particle geometries.

### Weaknesses
While the XiEff representation is positioned as an improvement over traditional methods, the paper lacks a rigorous quantitative comparison with existing approaches for solving inverse problems in nano-optics, such as traditional discretization, iterative, or diagram-based solutions. A discussion on seminal works such as Chen et al. (2020, 2022), which apply PINNs to inverse problems in nano-optics, is also absent. The method's performance is only validated using IoU, which is insufficient to demonstrate its advantages over other reconstruction techniques. The paper does not provide any quantitative comparison with other reconstruction methods mentioned in the related work, making it difficult to assess the actual improvement offered by the proposed approach. Furthermore, the lack of application to real SNOM data raises concerns about the practical relevance of the method, as the domain shift from synthetic data to real experimental data is not addressed.

### Questions
1. While the proposed XiEff method shows good shape reconstruction, it is not clear how much is improved compared to traditional reconstruction methods. Better to include these in the related work section, as well as add a reconstruction result comparison.
2. The paper only presents results on synthetic data. How does this technique work on real SNOM data?
3. Similarly, should also acknowledge and discuss prior works on PINNs in nano-optics/near-field optics to better position itself within the existing literature.

### Soundness
2

### Presentation
2

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
**Summary**  
This submission proposes the use of Physics-Informed Neural Networks (PINNs) for processing data from Scanning Near-Field Optical Microscopy (SNOM). While the motivation is clear, the contribution is poor, with significant literature missing regarding the application of PINNs for inverse problems in nano-optics, as well as specific applications to SNOM data.

**Clarity**  
- The work would benefit from a dedicated Related Work section, which should discuss prior research on PINNs and their application in nano-optics optimization, as well as relevant papers on near-field optics.

**Significance and Originality**  
(-) The originality of this paper is limited, especially as it omits relevant literature on its proposed contribution. Notably, the foundational paper by Chen et al. (2020), “Physics-informed neural networks for inverse problems in nano-optics and metamaterials,” is not discussed. Additionally, the paper specifically addressing this problem by Chen et al. (2022), “Physics-informed neural networks for imaging and parameter retrieval of photonic nanostructures from near-field data,” is missing from the discussion. The 2020 paper has 500 citations, while the 2022 paper has 40 citations, making these omissions a critical oversight.

**Results**  
(-) By 2024, it is insufficient to present PINN-related work at a top conference using only 2D toy results, especially considering the breadth of related research. The authors should either address the failure modes of previous methods or propose a novel methodology with robust validation.

**References:**  
- Chen, Yuyao, et al. "Physics-informed neural networks for inverse problems in nano-optics and metamaterials." *Optics Express*, 28.8 (2020): 11618-11633.  
- Chen, Yuyao, and Luca Dal Negro. "Physics-informed neural networks for imaging and parameter retrieval of photonic nanostructures from near-field data." *APL Photonics*, 7.1 (2022).

### Strengths
Introducing "neural fields + optics" into ICLR is an interesting endeavor.

### Weaknesses
 **Summary**
This submission proposes the use of Physics-Informed Neural Networks (PINNs) for processing data from Scanning Near-Field Optical Microscopy (SNOM). While the motivation is clear, the contribution is poor, with significant literature missing regarding the application of PINNs for inverse problems in nano-optics, as well as specific applications to SNOM data.

**Clarity**
- The work would benefit from a dedicated Related Work section, which should discuss prior research on PINNs and their application in nano-optics optimization, as well as relevant papers on near-field optics.

**Significance and Originality**
(-) The originality of this paper is limited, especially as it omits relevant literature on its proposed contribution. Notably, the foundational paper by Chen et al. (2020), “Physics-informed neural networks for inverse problems in nano-optics and metamaterials,” is not discussed. Additionally, the paper specifically addressing this problem by Chen et al. (2022), “Physics-informed neural networks for imaging and parameter retrieval of photonic nanostructures from near-field data,” is missing from the discussion. The 2020 paper has 500 citations, while the 2022 paper has 40 citations, making these omissions a critical oversight.

**Results**
(-) By 2024, it is insufficient to present PINN-related work at a top conference using only 2D toy results, especially considering the breadth of related research. The authors should either address the failure modes of previous methods or propose a novel methodology with robust validation.

**References:**
- Chen, Yuyao, et al. "Physics-informed neural networks for inverse problems in nano-optics and metamaterials." *Optics Express*, 28.8 (2020): 11618-11633.
- Chen, Yuyao, and Luca Dal Negro. "Physics-informed neural networks for imaging and parameter retrieval of photonic nanostructures from near-field data." *APL Photonics*, 7.1 (2022).

### soundness:
 1

### presentation:
 2

### contribution:
 1

### strengths:
 Introducing "neural fields + optics" into ICLR is an interesting endeavor.

### weaknesses:
 stated above.

### questions:
 Stated above.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

### role:
 Review

### Questions
Stated above.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article addresses the issue of lacking visual clarity and interpretability in images captured by scanning near-field optical microscopy. Based on the principle of neural radiance fields, the authors propose an effective susceptibility tensor parametrization method grounded in neural fields. This method enhances the interpretability of imaging and the morphological accuracy of micro-objects.

### Strengths
1. The article introduces a new representation method called XiEff. This approach is inspired by Neural Radiance Fields (NeRFs) in computer vision and Physics-Informed Neural Networks (PINNs).

2. The authors have integrated the XiEff representation into the Lippmann-Schwinger (LS) integral equation framework used in near-field optics, developing an optimization strategy that can directly reconstruct the effective susceptibility distribution from Near-Field Imaging (NFI) data.

3. An unsupervised optimization framework is proposed that can directly reconstruct the effective susceptibility distribution from NFI data. The authors claim that this method improves the practicality and efficiency of near-field optical analysis.

### Weaknesses
Weakness：
I have multiple concerns and questions about this paper, please see the detailed comments and suggestions.

1. The authors did not provide a systematic introduction to the relevant research background of this study, i.e., the most pertinent previous works were not discussed.
2. Most of the references cited in the paper are relatively old; the authors need to incorporate comparisons with more recent research content.
3. The "interpretability" emphasized in this task requires a clear definition from the authors.
4. Ground Truth should be separately listed in Figure 4.
5. The experimental section is rather thin; there are no ablation studies or evaluations of model parameters.
6. All the data used in the paper are synthetic samples; real-world microscopic data were not utilized.
7. Whether the paper fits within the scope of ICLR is questionable, as it does not delve deeply into concepts from machine learning or artificial intelligence.

### Questions
1. The authors did not provide a systematic introduction to the relevant research background of this study, i.e., the most pertinent previous works were not discussed.
2. Most of the references cited in the paper are relatively old; the authors need to incorporate comparisons with more recent research content.
3. The "interpretability" emphasized in this task requires a clear definition from the authors.
4. Ground Truth should be separately listed in Figure 4.
5. The experimental section is rather thin; there are no ablation studies or evaluations of model parameters.
6. All the data used in the paper are synthetic samples; real-world microscopic data were not utilized.
7. Whether the paper fits within the scope of ICLR is questionable, as it does not delve deeply into concepts from machine learning or artificial intelligence.

### Soundness
2

### Presentation
3

### Contribution
2
