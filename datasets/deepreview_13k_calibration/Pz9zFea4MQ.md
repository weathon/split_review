# Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
We aim to redefine robust ego-motion estimation and photorealistic 3D reconstruction by addressing a critical limitation: the reliance on noise-free data in existing models. While such sanitized conditions simplify evaluation, they fail to capture the unpredictable, noisy complexities of real-world environments. Dynamic motion, sensor imperfections, and synchronization perturbations lead to sharp performance declines when these models are deployed in practice, revealing an urgent need for frameworks that embrace and excel under real-world noise.
To bridge this gap, we tackle three core challenges: scalable data generation, comprehensive benchmarking, and model robustness enhancement. First, we introduce a scalable noisy data synthesis pipeline that generates diverse datasets simulating complex motion, sensor imperfections, and synchronization errors. Second, we leverage this pipeline to create Robust-Ego3D, a benchmark rigorously designed to expose noise-induced performance degradation, highlighting the limitations of current learning-based methods in ego-motion accuracy and 3D reconstruction quality. Third, we propose Correspondence-guided Gaussian Splatting (CorrGS), a novel method that progressively refines an internal clean 3D representation by aligning noisy observations with rendered RGB-D frames from clean 3D map, enhancing geometric alignment and appearance restoration through visual correspondence.
Extensive experiments on synthetic and real-world data demonstrate that CorrGS consistently outperforms prior state-of-the-art methods, particularly in scenarios involving rapid motion and dynamic illumination. We will release our code and benchmark to advance robust 3D vision, setting a new standard for ego-motion estimation and high-fidelity reconstruction in noisy environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a structured approach to advancing robust ego-motion estimation and 3D reconstruction in the presence of noisy video data. The authors tackle three core challenges: developing a scalable noisy data generation pipeline, creating the Robust-Ego3D benchmark to evaluate model robustness under varied perturbations, and introducing a novel model called Correspondence guidded Gaussian Splatting. The data generation pipeline is designed to synthesize large scale, customizable   datasets simulating realistic RGBD sensor noise and motion perturbations, which expose vulnerabilities in existing models. With these data, the Robust-Ego3D benchmark allows a systematic robustness evaluation of models across diverse noisy conditions.  CorrGS leverages correspondences between internally generated and observed frames to achieve photorealistic 3D reconstructions and robust pose tracking, significantly outperforming SOTA methods in both synthetic and real world experiments under rapid motion and complex noise.

### Strengths
The paper addresses the largely unexplored domain of robustness benchmarking for ego-motion and 3D reconstruction under realistic, noisy conditions. Unlike traditional methods that assume noise-free data, the paper  introduces a customizable pipeline for generating data with varied noise levels, motion deviations, and synchronization perturbations, filling a critical gap in existing SLAM evaluation techniques. Furthermore, CorrGS’s correspondence-based method is innovative, as it maintains a noise-free internal 3D representation while dynamically aligning it with noisy external inputs, a novel approach to handling real-world sensor noise. I believe the authors employ a rigorous methodological framework, incorporating a comprehensive set of experiments across both synthetic and real-world noisy datasets. They evaluate CorrGS and other baseline models on metrics including absolute trajectory rrror, PSNR, and depth loss, providing a strong quantitative foundation to support their claims. The ablation studies and theoretical analyses of perturbation effects on model performance offer a clear view of CorrGS's robustness and justify each of the model's components. The paper is clearly structured, with a logical flow from problem definition to solution details. For example, the pipeline for noisy data generation and perturbation taxonomy is visualized in Figure 1, which helps clarify complex processes. Additionally, the explanation of each perturbation type provides readers with a clear understanding of the challenges the benchmark addresses. The ablation studies further aid in understanding the impact of individual components within CorrGS on final model performance.

### Weaknesses
While the paper addresses RGB noise effectively, it could expand on the depth perturbations. Depth noise effects are discussed, the authors could delve further into the challenges that depth noise presents in reconstruction. Additional experiments on models’ performance under severe depth noise and missing depth data would strengthen the robustness evaluation and underscore CorrGS's adaptability. The PQV step is essential for their method’s robustness under complex conditions, but the rationale behind its design choices could be explained in greater detail. I believe it would be valuable to know if different loss functions  were tested and if so, why those choices were made. Demonstrating its impact across different noise levels would give a clearer picture of its effectiveness and necessity under varied conditions. The paper primarily compares CorrGS to other dense Neural SLAM models, but additional comparisons with classical non-neural SLAM methods would highlight CorrGS’s improvements in robustness.

### Questions
1. How does the pose quality verification step perform under different levels of noise? Did the authors experiment with varying PQV thresholds to understand its sensitivity to noise, and if so, what insights did they gain? 
2. Does CorrGS account for scenarios with high-frequency dynamic changes?
3.Different sensor types produce different noise profiles. Did the authors experiment with adjusting CorrGS for specific types of sensor noise (such asmotion blur for RGB or range limitations for depth sensors)?
4. The Robust-Ego3D benchmark and CorrGS are tested primarily on indoor or synthetic datasets. Do the authors envision any adjustments needed to apply these methods to outdoor environments, where conditions such as changing weather, shadows, or variable terrain could add complexity?

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
The paper addresses the challenge of ego-motion estimation and photorealistic 3D reconstruction from noisy video data. The authors present a customizable data synthesis pipeline that generates large-scale datasets with varied noise and perturbations, simulating real-world complexities such as rapid motion and sensor degradation. This pipeline powers the proposed Robust-Ego3D benchmark, which rigorously evaluates model performance under noise, revealing that current models significantly degrade under realistic conditions. Then, benchmark state-of-the-art models using the noisy data in extensive detail. Finally, the authors propose Correspondence-guided Gaussian Splatting (CorrGS), which maintains a clean internal 3D representation, aligning it with noisy observations to improve pose estimation and 3D reconstruction fidelity.

### Strengths
The most novel contribution of this paper is a novel data synthesis pipeline capable of generating large-scale, customizable datasets with various noise and perturbations. This contribution fills a crucial gap in Neural SLAM research by addressing real-world challenges in ego-motion estimation and 3D reconstruction.

The experiments are extensive, meticulously designed, and methodologically sound. Each experiment is carefully aligned with the core claims of the paper, providing solid evidence to support the proposed pipeline and benchmarking framework. The evaluation spans synthetic and real-world settings, presenting a thorough analysis of model performance under diverse noisy conditions. This approach strengthens the validity and robustness of the findings.

Tables and figures effectively illustrate complex concepts, making it easier to grasp the data synthesis pipeline, experimental setup, and results.

### Weaknesses
The paper reads more like a technical report, with an emphasis on experimental results over theoretical analysis or in-depth discussion. While the experiments are thorough, they could benefit from additional interpretive insights that go beyond reporting outcomes. For example, rather than solely presenting quantitative improvements, the authors could analyze why CorrGS outperforms other methods under certain noise conditions, offering more theoretical or practical insights into its advantages. Specifically, a deeper dive into the mechanisms by which correspondence-guided learning enhances robustness, such as how it handles occlusions or large viewpoint changes under noise, would be beneficial.

Lack of Contextual Foundation: The abstract and introduction lack a thorough discussion of why noise-free data in current reconstruction models presents a significant limitation. While the paper briefly mentions that models degrade in noisy conditions, it could strengthen its foundation by discussing why these models struggle under real-world noise and how noise impacts reconstruction quality, ego-motion estimation, and mapping accuracy. To improve, the authors should provide an analysis of these limitations with references to studies or examples that highlight the common challenges noise introduces in such models in the introduction section. For instance, discussing how noise affects feature extraction, matching, and bundle adjustment in traditional SLAM pipelines would provide a stronger context.

The transition from Problem to Method: The paper transitions too quickly from briefly mentioning the limitations of noise-free models to discussing the proposed pipeline and benchmark, missing an opportunity to underscore the problem’s significance. Expanding on how noise introduces challenges for different aspects of 3D reconstruction and SLAM (such as depth estimation, alignment, or tracking stability) would ground the paper’s contributions more effectively. A focused narrative in the introduction that explains why noise resilience is critical, perhaps by detailing specific failure modes of existing methods under various noise types, would better support the rationale for the proposed solution.

Limited Analysis of Model Vulnerabilities: Although the paper introduces a robust benchmark for noisy conditions, it lacks a detailed analysis of specific vulnerabilities of existing models across different types of noise. This analysis could enrich the understanding of how and why noise affects certain models more than others and help position CorrGS as a targeted solution to these specific gaps. For example, it would be valuable to see a breakdown of performance for each model under different noise types (e.g., Gaussian noise, salt-and-pepper noise, motion blur) and to analyze which aspects of the models are most sensitive to each type of noise. Adding such an analysis would make the benchmark more actionable and informative for future model improvement.

It can be understood the authors conducted extensive experiments and have a lot of content wish to express, yet the logic of proposing a novel method to fill a gap is overwhelmed by the extensive details. I think this work would be more fit for a journal instead of ICLR.

### Questions
What's the necessity of the problem formulation section? generate a dataset and then evaluate the model by calculating the evaluation matrix via the output and ground truth. This is a standard pipeline to conduct experiments. Why it was separately mentioned in an independent section? Please help me to understand what I missed if I misunderstood it.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper claims to have three-fold contributions. 1.A scalable noisy data synthesis pipeline that generates realistic RGB-D perturbations, addressing the gap between controlled and real-world environments for ego-motion estimation and 3D reconstruction tasks. 2. Robust-Ego3D, a benchmark based on the previous proposed pipeline that evaluates model robustness under diverse noisy conditions, setting a new standard for realistic model testing. 3. It also proposed CorrGS, a method that improves pose estimation and 3D reconstruction quality under noise, outperforming prior approaches in challenging scenarios.

### Strengths
This paper clearly defines the challenges posed by noise perturbations in ego-motion estimation and 3D reconstruction, offering a systematic exploration of how to evaluate and address these issues. This structured problem formulation provides a solid foundation for advancing robustness research in noisy environments and helps guide both model development and evaluation methodologies.

Author provides a very extensive set of experiments showcasing both the benchmark quality and methodology effectiveness across numerous noisy environments, demonstrating the generalizability of the solution.

The proposed scalable pipeline for generating realistic RGB-D perturbations is a major strength, as it introduces a systematic way to create customizable noisy datasets that mirror real-world conditions

The CorrGS method is an effective solution for improving pose estimation and 3D reconstruction under noise. It outperforms state-of-the-art models, particularly in challenging scenarios like fast motion.

### Weaknesses
While the paper identifies issues related to depth sensor noise, the evaluation and solutions for depth restoration are not as exhaustive as the RGB counterparts leaving some gaps in how to handle severe depth data inconsistencies. Specifically, the paper does not delve into the nuances of depth noise characteristics, such as the varying reliability of depth measurements at different distances or under different lighting conditions. The evaluation primarily focuses on the impact of noise on pose estimation and 3D reconstruction, but it lacks a detailed analysis of how different types of depth noise (e.g., Gaussian, salt-and-pepper, or structured noise) affect the performance of the proposed method. Furthermore, the paper does not explore strategies for depth inpainting or outlier removal, which are crucial for robust performance in real-world scenarios.

While the scalable noisy data synthesis pipeline is impressive, it relies heavily on synthetic noise generation. This might not fully capture the unpredictable nature of some real-world scenarios. The synthetic noise models, while customizable, may not fully replicate the complex interactions between different noise sources, such as sensor-specific artifacts, motion blur, and environmental interference. The paper should address the potential limitations of using synthetic noise for evaluating model robustness and discuss the need for further validation on real-world datasets with diverse noise characteristics.

This paper provides a new benchmark for evaluating ego-motion and 3D reconstruction quality in noisy environments, but it does not introduce any new evaluation metrics, relying instead on existing ones like ATE, PSNR, and Depth L1 Loss. While this is not a significant weakness, it might even be considered somewhat nit-picky to note. However, introducing new metrics specifically tailored to the unique challenges posed by noisy environments could have further strengthened the paper’s contributions. For instance, metrics that quantify the robustness of pose estimation to noise or the stability of the reconstructed 3D model under varying noise conditions could provide a more comprehensive evaluation.

Although the internal clean model is progressively refined, the method starts with the baseline assumption of a rough model that is iteratively improved. In some extreme real-world scenarios, where no good initialization is available, the system might initially struggle, which could be a practical limitation. Again, I acknowledge this may be somewhat nit-picky as well. The paper does not provide a clear analysis of the sensitivity of the method to the quality of the initial model. It is unclear how the performance of the proposed method degrades as the initial model deviates from the ground truth, and what are the limitations of the iterative refinement process.

### Questions
Q1. How does the system perform when the initial internal model is significantly misaligned or inaccurate? Does CorrGS require a reasonable starting point to work effectively, or can it handle scenarios where initial pose estimates are far off?

Q2. While CPL refines the pose estimates, how sensitive is CorrGS to extremely bad initial pose estimates? Are there scenarios where the initial pose is so far off that CPL struggles to recover accurate alignment, even with PQV in place?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a benchmark to evaluate dense neural SLAM systems that allow photo-realistic renderings. The benchmark starts from synthetic data (Replica) and considers several data degradation methods including trajectory perturbation, sensor brightness adjustment, motion blurs, etc. The authors compare several different neural SLAM methods including iMap, NICE-SLAM, and SplaTAM, as well as a traditional ORB-SLAM3 method. Extensive analysis and comparisons are conducted to understand the effect of pose accuracy under different noises added to Replica. The paper also presents a new method named CorrGS that leverages correspondence-initialized poses to improve the initialization of the system, which is demonstrated to work well on the benchmark and surpasses existing methods.

### Strengths
1. The overall contributions made by this paper are pretty extensive, with a benchmark, a thorough analysis of existing methods, and a new proposed CorrGS method that improves over the existing Neural-SLAM methods. The benchmark considers many aspects that a real capture could differ from synthetic captures that are typically overlooked by existing methods, and carefully decouples these factors into several fronts and provides their influence on the trajectory estimation accuracy.

2. While many benchmarks have been provided for real-world SLAM systems, this paper focuses specifically on Neural SLAM systems where the end product is not only camera trajectories but also a neural representation that allows photo-realistic renderings. This demonstrates the novelty of the paper.

3. The quality of the figures and the tables are of high-quality, with many details provided and essential details presented. One can easily tell the impact of different degradation methods to the performance of the SLAM systems.

### Weaknesses
1. I had a hard time reading through the entire paper when I was trying to understand the technical details, and I think that the papers need some refactors. There is extensive cross-referencing to the appendix in the middle of the main text, making the flow of understanding constantly interrupted by having to refer to the details later. While the benchmark, the analysis, and the new CorrGS method are all valid contributions, it would be nice to re-prioritize their importance and put more texts and the details of the most important part in the main text, while putting other parts in the appendix. For example, the entire section 3 could be largely shortened or even removed since the mathematical formulations are rather simple and do not help convey the simple idea behind the scenes.

2. The noise added to the synthetic Replica dataset (e.g. perturbation on depth sensor imaging) does not authentically simulate the real-world depth images. Real-world ToF cameras usually expose systematic noise with planes being pushed to curves, but the paper's enhancement method simply adds independent Gaussian noise to the depth images. This does not align with real-world observations.

3. The introduced benchmark is heavily based on Replica that only contains a limited number of indoor scenes. To further improve the utility of the benchmark it is advisable that the authors investigates into more diverse capturing settings, such as outdoor scenes (where the depth camera still works) and highly-dynamic scenes. 

4. While the main goal of the paper is to provide a benchmark that helps these Neural-SLAM methods perform better on real-world settings (by synthesizing real-world noises), it does not test its flagship method CorrGS on many real-world scenes. The only reconstruction results provided is Sec 6.3, where a relatively small chunk of real-world videos are reconstructed. It would be intriguing to see CorrGS being applied to more real-world datasets such as ScanNet++.

### Questions
I think the paper is written in a very clear way with many details already put in the appendix. I have no specific questions at the moment.

### Soundness
3

### Presentation
3

### Contribution
3
