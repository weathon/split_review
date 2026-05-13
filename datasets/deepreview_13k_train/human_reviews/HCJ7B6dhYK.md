# Radon Implicit Field Transform (RIFT): Learning Scenes from Radar Signals

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Data acquisition in array signal processing (ASP) is costly because achieving high angular and range resolutions necessitates large antenna apertures and wide frequency bandwidths, respectively. The data requirements for ASP problems grow multiplicatively with the number of viewpoints and frequencies, significantly increasing the burden of data collection, even for simulation. Implicit Neural Representations (INRs) — neural network-based models of 3D objects and scenes — offer compact and continuous representations with minimal radar data. They can interpolate to unseen viewpoints and potentially address the sampling cost in ASP problems. In this work, we select Synthetic Aperture Radar (SAR) as a case from ASP and propose the \textit{\textbf{R}adon \textbf{I}mplicit \textbf{F}ield \textbf{T}ransform} (RIFT). RIFT consists of two components: a classical forward model for radar (Generalized Radon Transform, GRT), and an INR based scene representation learned from radar signals. This method can be extended to other ASP problems by replacing the GRT with appropriate algorithms corresponding to different data modalities. In our experiments, we first synthesize radar data using the GRT. We then train the INR model on this synthetic data by minimizing the reconstruction error of the radar signal. After training, we render the scene using the trained INR and evaluate our scene representation against the ground truth scene. Due to the lack of existing benchmarks, we introduce two main new error metrics: \textit{\textbf{p}hase-\textbf{R}oot \textbf{M}ean \textbf{S}quare \textbf{E}rror} (p-RMSE) for radar signal interpolation, and \textit{\textbf{m}agnitude-\textbf{S}tructural \textbf{S}imilarity \textbf{I}ndex \textbf{M}easure} (m-SSIM) for scene reconstruction. These metrics adapt traditional error measures to account for the complex nature of radar signals. Compared to traditional scene models in radar signal processing, with only 10\% data footprint, our RIFT model achieves up to 188\% improvement in scene reconstruction. Using the same amount of data, RIFT is up to $3\times$ better at reconstruction and shows a 10\% improvement generalizing to unseen viewpoints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents the Radon Implicit Field Transform (RIFT), a novel method for reconstructing scenes from for synthetic aperture radar (SAR) imaging using an Implicit Neural Representation (INR). By encoding scene reflectivity in an INR, RIFT can reconstruct scenes with high fidelity from limited data samples, addressing the high data acquisition costs typical in SAR. The authors introduce custom error metrics—magnitude-SSIM (m-SSIM) for scene reconstruction and phase-RMSE (p-RMSE) for radar signal interpolation—to evaluate performance. Experimental results show that RIFT significantly improves scene reconstruction and viewpoint interpolation with reduced data compared to baseline models, demonstrating its potential for data-efficient radar-based imaging applications.

### Strengths
- The proposed method works well and outperforms existing approaches.
- Due to a lack of existing benchmarks, the authors created their own benchmark problems.  This can be a significant contribution if the authors make their benchmark open and easily accessible to the community.  I would encourage them to do so.

### Weaknesses
 - Presentation of the paper could be improved.  Figures generally contains small plots which are sometimes difficult to inspect, some (e.g. Figure 5) are surrounded by a lot of white space, some are not discussed in the text.
- 3D scenes considered are very simple.

- It is commented that a non-standard approach is taken of "accumulating gradients within an individual epoch across different views.... This gradient accumulation is specifically designed to mimic the physical motion inherent in synthetic aperture radar systems..."  This comment is somewhat cryptic and I did not fully understand why a non-standard approach was needed and, if so, how it mimics motion in SAR systems.  Could this comment please be elaborated and clarified.
- The abstract should stand alone and should not reference figures and tables in the paper.
- Figure 3 is not discussed in the text, as far as I could tell.
- Caption of Figure 4 is incomplete: "The data is"
- Typo p4, line 178: "scenarios, We"

### Questions
- It is commented that a non-standard approach is taken of "accumulating gradients within an individual epoch across different views.... This gradient accumulation is specifically designed to mimic the physical motion inherent in synthetic aperture radar systems..."  This comment is somewhat cryptic and I did not fully understand why a non-standard approach was needed and, if so, how it mimics motion in SAR systems.  Could this comment please be elaborated and clarified.
- The abstract should stand alone and should not reference figures and tables in the paper.
- Figure 3 is not discussed in the text, as far as I could tell.
- Caption of Figure 4 is incomplete: "The data is"
- Typo p4, line 178: "scenarios, We"

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenges of data acquisition in array signal processing (ASP), particularly in Synthetic Aperture Radar (SAR), where high angular and range resolutions require extensive data collection. To mitigate the costs associated with large antenna apertures and wide frequency bandwidths, the paper proposes the Radon Implicit Field Transform (RIFT), which integrates a classical forward model (Generalized Radon Transform) with an Implicit Neural Representation (INR) learned from radar signals. The method enables efficient scene representation and interpolation at unseen viewpoints, potentially reducing data collection burdens across various ASP applications. In addition, the paper introduces two novel error metrics to radar signal interpolation and evaluate performance. Experimental results demonstrate that RIFT achieves up to 188% improvement in scene reconstruction accuracy with only 10% of the data footprint compared to traditional models.

### Strengths
1. The paper learn implicit scene representations directly from radar signals, which is a new perspective for radar signal processing.
2. The proposed method can reconstruction and interpolate views using fewer measurements that non-deep learning methods.
3. The proposed two metrics are meaningful for the community.
4. The selected experiments show the efficiency of the proposed modules.

### Weaknesses
1. While the paper presents a novel method (RIFT) for radar signal processing, the experimental validation may not be comprehensive enough. The use of simulated data, while convenient, raises questions about the method's performance in the presence of real-world noise, multipath effects, and other signal distortions common in actual radar measurements. The paper lacks a thorough investigation into how these factors might impact the robustness and accuracy of RIFT. Additional datasets or real-world scenarios could strengthen the claims regarding the method's effectiveness and robustness.
2. The novelty of integrating deep learning methods with Generalized Radon Transform (GRT) is not well illustrated. The paper does not sufficiently articulate the specific advantages gained by combining these two techniques beyond a simple concatenation. It remains unclear what unique capabilities this integration provides compared to applying either method independently or in a more conventional cascaded manner. What is the main contribution, only a combination of them?
3. The criteria and methodology for this benchmarking may require further elaboration. The paper does not provide sufficient detail on how the benchmarks were selected, what specific radar parameters were used (e.g., frequency range, pulse repetition frequency, antenna configuration), and how the ground truth data was generated. A more detailed description of how the benchmarks were selected and validated could enhance the paper's credibility. The lack of clarity makes it difficult to assess the significance and generalizability of the reported performance gains.
4. The influence of hyperparameter selection on the performance of the INR model is not sufficiently explored. The paper does not discuss the sensitivity of the model to different hyperparameter settings, such as the learning rate, network architecture, or activation functions. This omission makes it difficult to understand the practical considerations for implementing and optimizing the proposed method in different scenarios.

### Questions
1. How do the data acquisition costs for radar imaging compare with those of other ASP applications, and what specific factors contribute to these differences?
2. How does the proposed Radon Implicit Field Transform (RIFT) manage to achieve scene reconstruction with only 10% of the data footprint compared to traditional models, and what specific mechanisms facilitate this reduction?
3. How does the joint benchmark for radar scene reconstruction and signal interpolation proposed in this study align with existing benchmarks in other imaging modalities?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper describes an application of implicit neural representation with a radar forward model to recover the 3D complex reflectivity of a scene radar array observations. A bi-static forward model is introduced and used to supervise a SIREN network with recovery results shown on simulated test cases. Two evaluation metrics are designed to quantify success both in reflectivity reconstruction and novel radar view synthesis.

### Strengths
The strength of the paper is the introduction of a new forward model to the ICLR community and its integration with neural fields. In general this is an interesting inverse problem which could a) open up new areas for research with the ML community and b) use ideas from the ML community, such as neural fields, for improving reconstructions, uncertainty quantification, run-time and scalability etc.

### Weaknesses
Overall I like the idea of the paper, however, I think the execution is quite lacking and it is not quite ready for publication. The experimental design is quite simplistic and I am unable to verify basic things like the validity of the forward model or if any improvements from the inclusion of neural fields would translate to real world scenarios. Below I detail some of the bigger issues and some minor ones:

1. The main issue is that the simulations are way too simplistic. SAR is a well established imaging modality and so I would expect to see real world data reconstructions. In the absence of real data reconstructions I would still expect to see more realistic simulations than the ones shown in the paper. I don’t think we can learn anything from the cube experiments and how they translate to real world scenarios. The simulated scenes lack complexity, and the single cube or simple blob-like structures do not capture the intricate scattering phenomena observed in real-world SAR data. This makes it difficult to assess the practical utility of the proposed method.

2. The experimental setup is not adequately described, so it is hard to assess the methodology. Here is a small subset of questions to guide the authors to a more complete picture:
  2.1. What is the sampling of the view angles? Is it sampled uniformly? Is it sampled according to a realistic path of a SAR instrument? 
  2.2. What noise, if any, is added to the data? Is this noise realistic and mimics real SAR instruments?
  2.3. Is there any mismatch between the forward GRT model used to generate the observations and the one used to recover the reflectivities? 
  2.4. Is the data/radar assumed to have perfect calibration, is this assumption realistic? 
  2.5. Is the GRT model described in Line 146 adequate? Are there any underlying assumptions that would introduce noise (systematic or otherwise) to real radar observations? What is the noise model? 
  2.6. How does R_b (Line 149-150) take into account differences in transverse vs along line of sight movement of the SAR?
  2.7. In sec 3.1 it is not clear what is granularity refers to when SIREN is a continuous representation
  2.8. The entire paragraph and discussion given in lines 188-193 is completely unclear. Also matrix A was never defined in the text.
3. I think that there are some over claims in the text that should be addressed. 
  3.1 For example lines 216-217 state: “It is crucial to note that during training, we employ a nonstandard approach of accumulating gradients within an individual epoch across different viewpoints.” . This seems to me quite standard in multi-view setting, and I think even the original NeRF and any multi-view algorithm before nerf (e.g. bundle adjustment, multi view stereo, etc) uses rays from multiple views in each gradient calculation. Furthermore the highlighted claim: “This gradient accumulation is specifically designed to mimic the physical motion inherent in synthetic aperture radar systems” is not entirely clear to me, how is that different to any other multi-view setup? Where is the motion taken explicitly into account for the SAR system. It would help the paper if you could explicitly clarify these statements that seem like a key contribution.
  3.2. Line 485: “lays a cornerstone for research into the representation of INRs in less-explored data modalities.” I think this is an over claim. This work certainly is in line with a recent trend but I wouldn’t say it is laying the corner stone. Work in the past couple of years have demonstrated the use of nerf with wild and interesting forward models from biology, astronomy, transient imaging to name a few, see a handful of links below:
            - https://arxiv.org/abs/2307.09555
		- https://arxiv.org/abs/1909.05215
            - https://arxiv.org/abs/2204.03715
           - https://arxiv.org/abs/2405.04662
           - https://arxiv.org/abs/2309.04437
           - https://ojs.aaai.org/index.php/AAAI/article/view/20171


Minor comments:
 - Figure 1 should not appear in the first page where it’s not referenced. 
 - Could be useful to give equation numbers for referencing.
 - The use of “ground truth” should be reserved for reflectivities and it is confusing to use it in the context of radar data, even if this “data” was simulated from ground truth reflectivities. (e.g. lines 173, 231 etc).
 - Lines 418-424 describe the setup in a very complex way. I think this could be resolved with a single illustration figure.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents RIFT (Radon Implicit Field Transform), a novel method for learning scene representations directly from radar signals using implicit neural representations (INRs). The approach combines classical radar forward modeling (Generalized Radon Transform, GRT) with modern neural network techniques to address the data acquisition challenge in array signal processing (ASP), particularly in Synthetic Aperture Radar (SAR) applications.

The main contributions include:

1. A framework that integrates INR with GRT to learn scene representations directly from radar signals, enabling scene reconstruction with reduced data requirements

3. Introduction of new evaluation metrics specifically designed for radar signal processing:
   - phase-Root Mean Square Error (p-RMSE) for radar signal interpolation
   - magnitude-Structural Similarity Index Measure (m-SSIM) for scene reconstruction

The authors demonstrate their method's effectiveness through extensive experiments on synthetic data, showing improvements in both scene reconstruction quality and viewpoint interpolation capability compared to traditional methods. They also present a case study on weak target detection in far-field scenarios, demonstrating the method's potential practical applications.

### Strengths
Good Originality:

- The paper presents a novel application of implicit neural representations to radar signal processing, particularly in SAR imaging
- While similar to computer vision approaches, its adaptation to radar domain represents meaningful innovation

Good Quality:

- The technical development is thorough and well-grounded in both radar signal processing and deep learning principles
- The paper introduces well-designed evaluation metrics specifically for radar signals:
  * phase-Root Mean Square Error (p-RMSE) for signal interpolation
  * magnitude-Structural Similarity Index Measure (m-SSIM) for scene reconstruction

### Weaknesses
# Major Weaknesses:

1. **Lack of Real-World Data Validation**: **The most critical concern**
- The paper relies entirely on synthetic data for evaluation.
- Many public mmWave and SAR datasets are available but not utilized.
- The gap between synthetic and real data is not addressed:
  * Real scenarios involve complex multipath effects, including non-specular reflections and scattering from diverse materials.
  * The accuracy of GRT in real-world conditions is questionable, particularly with non-ideal antenna patterns and calibration errors.
  * Environmental factors affecting radar signals, such as atmospheric attenuation, temperature variations, and humidity, are not considered.
- The effectiveness on synthetic data is expected due to neural rendering's ability to fit training data, but this doesn't validate real-world applicability where the underlying physics are far more complex.
- Therefore, this significant omission raises serious doubts about the validation and practical value of the proposed method.

> I would significantly improve my assessment if the authors could demonstrate their method's effectiveness on real-world SAR or mmWave radar datasets.

2. **Accuracy of GRT Forward Model**
- The paper doesn't address GRT's limitations in complex real-world scenarios:
  * Multipath effects, including non-line-of-sight propagation and diffuse scattering, are not accounted for, which can lead to significant errors in scene reconstruction.
  * Material properties, such as frequency-dependent permittivity and permeability, are not considered, which can affect the accuracy of the forward model.
  * Environmental interference, such as radio frequency interference (RFI) and clutter from unwanted reflections, are not addressed, which can degrade the quality of the radar signals.
- These limitations could severely impact the method's practical applicability, as real-world radar data is often corrupted by these effects.
- The validation of GRT accuracy is crucial but missing from the current work, especially given the sensitivity of inverse problems to modeling errors.

3. **Related Work Citiation and Discussion**
- RadarFields (published May 2024) has already explored similar ideas.
- While concurrent development is understandable, proper citation and discussion are needed to contextualize the contribution of this work relative to existing approaches.

# Minor Weaknesses:

- Inconsistent mathematical notation in Section 3.1:
  * Variable x is used inconsistently, sometimes as a scalar and sometimes as a vector.
  * Matrix A notation varies throughout the paper, making it difficult to follow the mathematical derivations.

- Typos

### Questions
Please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
4
