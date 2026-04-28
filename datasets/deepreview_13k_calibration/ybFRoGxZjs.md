# ThermalGaussian: Thermal 3D Gaussian Splatting

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 5, 8, 6, 6

## Abstract
Thermography is especially valuable for the military and other users of surveillance cameras. Some recent methods based on Neural Radiance Fields (NeRF) are proposed to reconstruct the thermal scenes in 3D from a set of thermal and RGB images. However, unlike NeRF, 3D Gaussian splatting (3DGS) prevails due to its rapid training and real-time rendering. In this work, we propose ThermalGaussian, the first thermal 3DGS approach capable of rendering high-quality images in RGB and thermal modalities. We first calibrate the RGB camera and the thermal camera to ensure that both modalities are accurately aligned. Subsequently, we use the registered images to learn the multimodal 3D Gaussians. To prevent the overfitting of any single modality, we introduce several multimodal regularization constraints. We also develop smoothing constraints tailored to the physical characteristics of the thermal modality.
Besides, we contribute a real-world dataset named RGBT-Scenes, captured by a hand-hold thermal-infrared camera, facilitating future research on thermal scene reconstruction. We conduct comprehensive experiments to show that ThermalGaussian achieves photorealistic rendering of thermal images and improves the rendering quality of RGB images. With the proposed multimodal regularization constraints, we also reduced the model's storage cost by 90\%. The code and dataset will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduce ThermalGaussian, a multimodal Gaussian technique that renders high-quality RGB & thermal images from new views.
Also they introduce a new real-world dataset named RGBT-Scenes, to address the issue of existing problems.
Authors propose multimodal regularization to prevent overfitting and show that ThermalGaussian outperforms previous methods by enhancing rendering quality, reducing storage requirements, and improving efficiency.

### Strengths
The proposed approach is novel, especially in integrating thermal and RGB images in 3D reconstruction via Gaussian splatting. And the experimental results are clear, and include diverse evalutaion metrics and ablation studies to validate performance of this methods.

Also, introducing the RGBT-Scenes dataset is a valuable contribution that can serve as a benchmark for future work in thermal 3D reconstruction.

### Weaknesses
The process of multimodal initialization and the specific configurations for the thermal Gaussian construction are intricate, making the approach challenging to implement without in-depth knowledge. Specifically, the paper lacks a detailed explanation of how the thermal and RGB camera parameters are aligned and calibrated, which is crucial for accurate multimodal Gaussian construction. Furthermore, the paper does not provide sufficient detail on how the thermal Gaussian splats are initialized and how their parameters (e.g., position, covariance, opacity) are determined in relation to the RGB splats. This lack of clarity makes it difficult to reproduce the results or adapt the method for different sensor setups. And, although the RGBT-Scenes dataset is comprehensive, details regarding environmental diversity and lighting conditions could strengthen its applicability across broader contexts. The dataset description should include more information on the range of temperatures, the presence of occlusions, and the variability in surface materials, as these factors can significantly affect the performance of thermal reconstruction algorithms.

### Questions
- Can the authors clarify the choice of hyperparameters for multimodal regularization? Are there general guidelines for adjusting them?

- How does the model handle extreme cases, such as highly reflective surfaces or objects at temperatures that differ significantly from ambient conditions?

- Could the RGBT-Scenes dataset be expanded to include data for real-time applications, like moving objects or dynamic scenes?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method based on 3DGS that jointly learns multi-modal scene representations of RGB and thermal images. In fact, the authors present and evaluate three different strategies to incorporate thermal images into 3DGS: MFTG (based on fine-tuning), MSMG (leverages multi-task learning), and OMMG—the latter yields a single Gaussian, which is achieved by extending 3DGS with spherical harmonics to represent thermal data. Moreover, a regularization term is proposed that accounts for the smooth nature of thermal images, and a new weight scheduling strategy prevents the proposed MSMG from overfitting to a single modality. Based on a newly collected RGB+thermal dataset consisting of ten scenes, the authors could successfully show that their method outperforms 3DGS baselines and a recent NeRF-based method in terms of RGB and thermal rendering quality while requiring less memory.

### Strengths
- The topic is interesting and of importance to the community, as demonstrated by the large body of recent work [1-5].

- The paper is well-written and easy to follow. Experiments are well described and cared out thoroughly. The ablation study nicely supports all design decisions. All in all,  I don’t see any obvious flaws.

- This is (to the best of my knowledge) the first paper to use some kind of scheduling to dynamically adjust the weight that balances the RGB and thermal loss in Eq. (12). The proposed strategy seems plausible to me, and, according to the experimental evaluation, significantly reduces the memory footprint while only slightly decreasing image quality. Due to the reduced number of Gaussians, this strategy also increases rendering speed.

- Compared to prior work [1,3] (but similar to [5]), the method presented in this work is actually capable of *improving* the RGB rendering quality, especially in low-light conditions.

- The paper proposes and evaluates not only a single method but three different strategies to incorporate thermal images into 3DGS, thus can be seen as the 3DGS-based pendant to [1].

- I appreciate the newly collected dataset. Although small-scaled (like all other publicly available RGB+thermal datasets), it is diverse, contains forward-facing and 360-degree scenes, and encompasses indoor and outdoor environments. This is very helpful to the community.

References:

[1] Mert Özer et al. Exploring Multi-modal Neural Scene Representations With Applications on Thermal Imaging. ECCVW, 2024.

[2] Yvette Y. Lin et al. ThermalNeRF: Thermal Radiance Fields. ICCP, 2024.

[3] Miriam Hassan et al. ThermoNeRF: Multimodal Neural Radiance Fields for Thermal Novel View Synthesis. arXiv, 2024.

[4] Tianxiang Ye et al. Thermal-NeRF: Neural Radiance Fields from an Infrared Camera. arXiv, 2024.

[5] Jiacong Xu et al. Leveraging Thermal Modality to Enhance Reconstruction in Low-Light Conditions. ECCV, 2024.

### Weaknesses
 - I am missing citations (and discussions) of recent related works [1,2,5] in the introduction and related work sections.

- I would love to see empirical evidence for the statement in L337: "we observe that the weight coefficients of a modality align linearly with the Gaussian it ultimately generates". This is a quite interesting finding that would be much better supported with data.

- Authors claim multiple times (for example in L028, L104, and L536) that they are the first to use 3DGS to model RGB and thermal images. This statement is actually not true and should be revised. The authors of [5] already presented a 3DGS-based method that incorporates RGB and thermal data (see Section 4.5 of the main paper and Section 4 of supplementary).

- In Table 1, the following open-source multi-view RGB+thermal datasets are missing: ThermalMix proposed in [1], the datasets presented in [2], and MVTV proposed in [5]. Why is the proposed dataset better than these datasets? Also, it would be good to provide specific criteria for how multi-view consistency and content richness is evaluated across datasets. This would help clarify the comparison and justify any claims about the proposed dataset's advantages.

- With the high number of recently published RGB+thermal datasets, I think it might make sense to evaluate the introduced method on at least one of these datasets, also to mitigate potential dataset bias. 

- In addition, the proposed method could be compared to some more of the recently published NeRF-based methods. There is code available for [2].

- In L097 authors mention that ThermoNeRF [3] reduces RGB rendering quality, while the proposed method improves it (according to Table 3, an average increase of almost 5% in PSNR). I think that is a huge plus for the proposed method; however, this argument would be much stronger if authors would add comparisons with NeRF-based methods to Table 3.

- I would love to see a side-by-side comparison of thermal renderings with and without the smoothness term.

- Although the proposed weight scheduling used in MSMG yields lower storage requirements, the average rendering quality for RGB and thermal data is worse than for OMMG (see Tables 2 and 3; difference higher for thermal renderings, drop of about 1% in PSNR). So, if one wants to maximize rendering quality and therefore uses OMMG, the benefit of having lower memory requirements is gone (see Table 4; OMMG requires about 60% of the storage space of 3DGS in contrast to 8% for MSMG).

- In Section 3.2, three different strategies to obtain camera poses for thermal images are mentioned. What strategy is actually used for the experiments? Also, what strategy performs best? A quantitative comparison would be really helpful, also because MSX seems to perform best (just by looking at Figure 2). The problem I see is that MSX is patented by FLIR, as such it is not available to other cameras. Hence, the practical use of the third strategy is highly limited, and it would be good to know which strategy could be used instead. Do the other strategies in any form make use of MSX images as well?

### Questions
- What does „Mix50“ in Figure 2 stand for? Is Eq. (5) applied with $\beta=0.5$? If so, please leave a note in the caption of Figure 2.

- How sensitive is $\lambda_{smooth}$? Would it be possible to provide a small ablation study?

- How was $\lambda$ in Eq. (6) and Eq. (10) set? Also, are these two lambdas the same?

- As far as I understand, MSMG uses the cost function described in Eq. (7), i.e., without multimodal regularization. So, whenever "Ours_MSMG" is used in Tables 2 and 3, it refers to MSMG method trained without multimodal regularization. This is in accordance with Table 4, where authors add a dedicated row for "Ours_MSMG+MR" which would not be necessary if MSMG uses MR per default (in this case, I would rather expect a row with "Ours_MSMG w\o MR" in Table 4). As this would mean that MR has never been used except in the ablation study, I would guess that per default, Eq. (12) has been used to train MSMG. Please make this more clear (e.g., by replacing Eq. (7) with Eq. (12) and referring to Section 3.4. on how to choose $\gamma$).

- What cost function is used to train OMMG? Is it Eq. (7)? If so, please move it to the respective paragraph (starting L296).

- In Figures 5 and 6, which strategy does "Ours" refer to?

- To be honest, it is quite surprising to me that a conventional chessboard pattern printed on normal paper produces such highly contrasting thermal images. There are numerous works (see, e.g., [6] and references therein) that try to design special calibration objects for thermal cameras. I wonder why all these papers exist when a simple chessboard pattern printed on paper will also work. What are the physical principles behind why a simple chessboard pattern printed on paper works, and how does it compare to more complex calibration objects in terms of accuracy and ease of use?

References:

[6] Issac N. Swamidoss et al. Systematic approach for thermal imaging camera calibration for machine vision applications. Optik 247, 2021.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an enhanced method that extends the 3D Gaussian Splatting (3DGS) technique through the ThermalGaussian model, allowing for joint learning and rendering of RGB and thermal data. By learning thermal images together with RGB data in a multimodal framework, the approach aims to improve 3D scene reconstruction capabilities across fields where thermal imaging is valuable, such as in military, industrial, and medical applications. The paper presents initialization strategies for aligning and merging RGB and thermal data, a loss function tailored to the characteristics of thermal imaging, and multimodal regularization techniques to prevent overfitting and optimize storage. Additionally, a new dataset, RGBT-Scenes, is introduced, providing research data that includes both RGB and thermal images.

### Strengths
1. Effective Multimodal Learning and Loss Function Design

The paper introduces an initialization strategy for aligning RGB and thermal data, along with a loss function tailored to thermal characteristics, allowing these modalities to learn complementarily. This approach enables each modality to mitigate the limitations of the other, achieving optimal reconstruction performance​.

2. Model Efficiency and Storage Optimization

By applying multimodal regularization to prevent overfitting and reduce redundant Gaussians, the model reduces storage requirements by approximately 90% compared to conventional methods. This enables high-quality 3D reconstruction while also enhancing storage efficiency and rendering speed​.

2. Contribution of the RGBT-Scenes Dataset to the Research Community

The RGBT-Scenes dataset introduced in this paper provides paired RGB and thermal images across diverse indoor and outdoor scenes, offering a valuable resource for thermal-based 3D reconstruction research. This dataset provides a foundation for researchers to test and expand upon the proposed model, thereby promoting advancements in the field​.

### Weaknesses
1. Lack of Thermal Data Description

While the provision of a dataset is one of the significant contributions of this paper, it lacks sufficient information for readers to understand the characteristics of thermal data. Including details about general characteristics of infrared imaging, as well as optical or photographic settings used during data collection (e.g., imaging wavelength range, whether exposure values were fixed), would help readers better understand the dataset's properties and enhance reproducibility. Specifically, the paper should detail the thermal camera's spectral sensitivity, the noise characteristics of the sensor, and whether any radiometric calibration was performed. Furthermore, the absence of information regarding the ambient temperature during data capture and the emissivity of the materials in the scene makes it difficult to assess the accuracy of the thermal measurements.

2. Lack of Discussion on Limitations

The paper focuses on the model's performance but lacks an explicit discussion of its limitations. For example, it would benefit from exploring conditions under which the proposed multimodal regularization and initialization strategies may not perform well. Specifically, the paper should address the potential for misalignment between RGB and thermal data due to parallax or calibration errors, and how this might impact reconstruction quality. Additionally, the method's performance in scenarios with significant temperature variations or highly reflective surfaces should be discussed. Including such a discussion would allow for a more realistic assessment of the model's applicability and provide important insights for researchers who may wish to build upon this work.

3. Lack of Discussion on Applicability and Future Work
Although the multimodal learning approach for RGBT data proposed in this paper is academically valuable, the discussion on future work is somewhat general. The paper mentions super-resolution and dynamic scene reconstruction as directions for further research, but these are relatively standard research topics rather than areas specifically tailored to advancements in thermal 3D reconstruction. The discussion should include the challenges of applying this method to real-world scenarios, such as outdoor environments with varying weather conditions, or in industrial settings with complex thermal patterns. Furthermore, the paper should explore the potential for using the reconstructed 3D thermal fields for quantitative analysis, such as heat transfer modeling or thermal anomaly detection.

### Questions
1. Applicability to a Broader Range of Hyperspectral Imaging

While the RGBT images presented involve the addition of a single channel, they can broadly be considered a form of hyperspectral imaging, as they incorporate the infrared spectrum. Could the authors discuss the potential for their multimodal approach to be applied to a broader range of hyperspectral imaging? Additionally, I am interested in the authors' views on whether this approach could be extended to studies involving multi-wavelength, multichannel data, and if it could serve as a basis for hyperspectral data analysis.

2. Requirement for Well-Aligned RGB and Thermal Data and Practical Field Applicability 

The proposed method relies on the availability of well-aligned RGB and thermal data, which may limit practical field applications. In cases where precise data alignment is challenging or unfeasible in real-world scenarios, are there any methods the authors could suggest to mitigate this limitation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
ThermalGaussian is the first work with thermal 3D reconstruction with 3DGS representation.

The paper achieves thermal and RGB 3D reconstruction simultaneously, and improves the rendering results both of color and thermal images.

Finally, the paper reduces the model storage cost by 90%.

### Strengths
The paper presents new thermal-RGB datasets which will be helpful in future research.

The method shows quality improvement not only for thermal reconstruction but also for RGB reconstruction.

The method that adds thermal reconstruction on 3DGs is effective and straightforward.

### Weaknesses
The paper proposes three multimodal training methods, which are MFTG, MSMG, and OMMG. The reviewer is confused about the pros and cons of each model, and users are confused about which model to choose. In the quantitative evaluation, the best performing models are distributed across each scene, with no model performing overwhelmingly well.

In the three multimodal training methods, the insight about why these three design are needed is lacked. In L. 283, the authors say “thermal Gaussian training in the second phase may not fully leverage the information from the color modality”, and there is no evidence about this.

There is no discussion about the limitations.

In L.448, there is a type. “Ours” → “ours”

### Questions
In the paper, the authors say that thermal imaging is practical task and 3D reconstruction gives significant applications which 2D images cannot provide. The reviewer wonders what is the specific case of that thermal 3D reconstruction is practical than 2D thermal image? There is a logical jump in the connection between the two. This context would be added at the related work 2.1 section.

In L. 314, the paper denotes thermal equilibrium, and it would be nice to explain what this means.

In the related work section, both of ThermoNeRF and ThermalNeRF are denoted but why only ThermoNeRF is compared to your method?

The reviewer suggests that comparison to existing thermal 3D reconstructions and to datasets used in previous studies, such as ThermoNeRF and Thermal-NeRF, would further emphasize the strength of the method itself.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of scene reconstruction with both RGB and thermal image inputs. Specifically, 3D Gaussian Splatting is adopted as the baseline method as a replacement to NeRF. To equip 3D Gaussian Splatting with the ability to also learn 3D thermal representations, this paper proposes a series of strategies for multimodal Gaussian reconstruction, including multimodal initialization, three different thermal Gaussians, constraints specific to thermal modalities, and multimodal regularization. The paper also introduces a new dataset designed for thermal 3D reconstruction. 

Experiments demonstrate the advantage of the proposed method in the quality of reconstruction, in both RGB and thermal modalities.

### Strengths
The paper investigates an interesting problem of incorporating thermal information into 3D reconstruction by improving on the prevalent 3D Gaussian Splatting method. The presentation is clear and easy to follow. The results are also interesting in that both RGB and thermal reconstruction have improved.

### Weaknesses
I do not hold critical concerns to this paper. However, there are some issues that I'd be happy to see clarified.

In the Multiple Single-Modal Gaussians strategy, it is stated that "Each Gaussian model is influenced
not only by its corresponding input modality but also by others." But how so? RGB modality and thermal modality seem to be uncorrelated to me since 3D Gaussians are trained separately for each. It's unclear how the gradients from one modality influence the other during backpropagation, given that the Gaussian parameters are distinct.

Regarding experiments, is there a specific reason that Thermal-NeRF has not been included in the comparison?

### Questions
Please respond to the points made in the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2
