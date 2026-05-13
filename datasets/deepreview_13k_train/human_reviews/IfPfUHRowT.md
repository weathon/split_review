# Inpainting the Sinogram from Computed Tomography using Latent Diffusion Model and Physics

- Decision: Reject
- Scores: 3, 3, 6, 1

## Abstract
Computed Tomography (CT) is a widely used non-invasive imaging technique for materials at microscopic or sub-microscopic length scales in synchrotron radiation facilities. Typically, the object is rotated relative to the X-ray beam, and 2D projection images are recorded by the detector at different rotation angles. The 3D object is then reconstructed by combining these projections and solving a computationally demanding inverse problem. The quality of the reconstructed image is critical for scientific analysis and is influenced by various factors, including the number of projections, exposure time or dose, and the reconstruction algorithm. In this work, we develop a foundation model by integrating a Generative AI-based Latent Diffusion Model (LDM) with physics-based domain knowledge. Specifically, we first incorporate a set of loss functions into our LDM that accurately capture the physical properties of the CT data acquisition process. We demonstrate that addition of these loss functions aids in stable training of the autoencoder in the LDM and improves its accuracy. The autoencoder and the Diffusion model of the LDM is trained with real-world experimental data. Collecting real world experimental data from Synchrotron beamlines is often time-consuming and challenging. We demonstrate that the autoencoder trained with a combination of real world experimental data and phantom shapes features also performs comparable to the autoencoder trained with real world data. Second, we introduce a novel image blending method to combine the LDM’s generated output with the original, extremely sparse sinogram data. Since our model integrates physics-guided loss functions focused on CT data acquisition, it simplifies the creation of downstream tasks and facilitates the adaptation of new features from different experiments. Our experimental evaluation demonstrates improvements of upto 23.5 % in SSIM for sinogram quality and 13.8 % for reconstructed image quality compared to state-of-the-art techniques.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel foundation model for sinogram inpainting based on the latent diffusion model (LDM). By considering certain physical characteristics of CT acquisition and sinograms, they designed an innovative physics-informed loss function that significantly enhances the autoencoder's training performance. Additionally, they introduced a sinogram blending technique that balances content and style perception to improve the synthesis quality between predicted and real sinograms. Experimental results demonstrate that this method outperforms current state-of-the-art approaches in sinogram inpainting, highlighting its potential as a foundational model for CT applications.

### Strengths
By incorporating the physical characteristics of CT acquisition and sinograms into the design of the loss function, this approach effectively combines domain knowledge with advanced techniques, enabling more efficient learning for domain-specific tasks.

### Weaknesses
The structure of this paper is highly disorganized. For instance, in lines 171–176, after introducing various works on sinogram inpainting, the authors abruptly shift to discussing image blending, which may confuse readers. Furthermore, the authors seem unfamiliar with the proper use of `\citet` and `\citep` commands, as nearly all citations fail to meet academic writing standards, particularly in Section 2, where incorrect citation formatting severely disrupts the reading experience. In Section 4.4, almost all citations are wrong, with many references not corresponding to their intended sources. The authors should thoroughly review and correct all citations with careful attention to detail.
- Figure 9 is severely blurred, making it difficult to discern the comparative effectiveness of the proposed method against other approaches. Additionally, the paper lacks a quantitative performance comparison with the baseline methods. Although the primary task is sinogram inpainting, in practical applications, the focus is ultimately on the quality of the final CT images reconstructed from the inpainted sinograms. This aspect is missing from the current work. The authors should consider including both quantitative and qualitative results of the CT images reconstructed from sinograms completed using the proposed method.

### Questions
- In line 206, the phrase “perceptual loss term, $L_P$ in addition” seems to have incorrect comma placement. It should be written as “perceptual loss term $L_P$, in addition,” correct?
- In line 263, the authors state, “we also need a ramp filtering operation for noise removal in the image.” This is inaccurate; it should be clarified that the purpose of the ramp filtering operation is to remove blurring effects.
- In line 367, the authors mention, “we fine-tune the model with fewer data,” and that “this fine-tuning approach does not require a high computational overload and can be implemented on a compute node with limited GPU resources.” However, they also mention using 25,000 real-world training samples for fine-tuning, which is not a small dataset. This raises the question of how it can be feasible “with limited GPU resources.”

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposed a model which integrate the Latent Diffusion Model (LDM) with physics-based domain knowledge. A set of loss functions were designed. The paper proposed a blending algorithm to improve the accuracy of inpainting task. The proposed method is work for simulated parallel projection data (not real-world data).

### Strengths
(1)	domain specific physics knowledge of CT image formation for inpainting sinograms taking into account both measurement and reconstruction domains.
(2)	Recover sinogram with different masks and different sampling ratio. 
(3)	Suitable for Sparse data acquisition and Missing Wedge Problem.

### Weaknesses
(1)	The loss is complex and too many parameters. Ablation of every part is necessary.
(2)	The paper uses the simulated projection data other than real word data.
(3)	The proposed method is only work with Parallel beam projection geometry with is xxxxx
in real application.

(4)	The downstream task of the method is image reconstruction. Comparison with reconstruction method for sparse view reconstruction and limit view reconstruction is necessary, such as dual domain reconstruction.
[1] W. Wu, D. Hu, C. Niu, H. Yu, V. Vardhanabhuti and G. Wang, "DRONE: Dual-Domain Residual-based Optimization NEtwork for Sparse-View CT Reconstruction," in IEEE Transactions on Medical Imaging, vol. 40, no. 11, pp. 3002-3014, Nov. 2021, doi: 10.1109/TMI.2021.3078067
[2] Ding, Q., Ji, H., Gao, H., Zhang, X. (2021). Learnable Multi-scale Fourier Interpolation for Sparse View CT Image Reconstruction.
(5) The literature review is limited, many CT reconstruction works, such as iterative reconstruction and deep learning reconstruction (image domain, unrolling (ADMM-Net), and plug-&play method) are not given

### Questions
1 The training and inference time comparison is necessary for sampling is time-consuming.
2 Notation is not defined clearly, e.g. equation (1) sg. and z_qn never used.
3 Can the method extend to 2D fan-beam and 3D Cone beam reconstruction
4 Visual comparison of reconstructed image from recovered sinogram also needed for that a minor error of sinogram may lead to streaky artifacts in image.

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
3

### Summary
This paper deals with the problem of sparse sinograms in CT. The authors combine an autoencoder with a latent diffusion model which incorporates physics knowledge in the loss functions. This stabilizes the training process of the autoencoder. Furthermore, a blending algorithm is applied such that the output of the diffusion model also aligns with the measurement data.

### Strengths
* Including physics-domain knowledge is an essential task in machine learning.
* Sparse sinograms are problems in practice to reduce the dose and/or the acquisition time.
* The method was tested on a real-world dataset.
* The paper has a good structure, explaining the individual components.

### Weaknesses
 * The proposed method seems very complex. There are many different sub-modules: autoencoder, diffusion model, blending.
* Training an autoencoder is hard.
* There are many hyperparameters to adjust in the different loss functions.
* The blending technique is not suitable for lower mask ratios.

### Questions
* Do we really need such a complex setting? Isn’t it possible to use a simpler model like a diffusion model and include all the losses there?
* Is this approach end-to-end trainable?
* What are phantom features?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a method that integrates a Latent Diffusion Model (LDM) with physics-based loss functions to address missing data issues in CT imaging by inpainting sinograms. The paper demonstrates an approach by combining machine learning techniques with CT-specific physical properties. However, the manuscript has shortcomings regarding organization, precision, and detail.

### Strengths
This paper presents an approach by integrating a Latent Diffusion Model (LDM) with physics-based loss functions for CT sinogram inpainting, demonstrating originality in combining generative AI with domain-specific knowledge. The work introduces unique physics-driven loss functions that enhance the stability and accuracy of the model.

### Weaknesses
The manuscript is challenging to read due to disorganized logic, unprofessional expressions, and vague descriptions, making it hard to follow the motivation and methodology.

 1.     This manuscript is challenging to read, with disorganized logic and non-standard, unprofessional expressions:
	•	The paper only lists existing methods without clearly identifying their limitations or explaining the motivation for the proposed approach.
	•	Expressions such as “During a CT experiment” and “CT experimental time” are imprecise and lack professionalism.
	•	The statement, “The object is rotated stepwise around a central axis,” is misleading; typically, it is the source and detector that rotate, not the object itself.
	•	Phrases like “Combining several such projections, a specialized algorithm” are vague and difficult to understand. Please clarify.
	•	The sentence, “it can also lead to morphological deformation in the sample due to extended radiation exposure,” seems to imply that deformation results from patient motion over extended scan times.
	•	The phrases “In one approach,” “In another approach,” and “In a third approach” might be referring to sparse-view CT, limited-angle CT, etc. However, other forms of incomplete projection data also exist, which could be covered or referenced in a comprehensive review article [1].

 2.     The so-called “novel blending algorithm” proposed in this paper is, in fact, a common practice in CT reconstruction from incomplete measurements.

 3.     The term “realistic simulated data” raises ambiguity regarding the authenticity of the experimental data; it is unclear whether the data are from real experiments or simulations. Although the paper emphasizes the importance of physics-based loss functions, there is no detailed description of imaging parameters. Additionally, the use of “re-project” suggests that the projection data may not be genuine, but rather re-generated, which further questions the authenticity of the data used.

 4.     Since the method uses FBP with a reconstruction loss, why not present the reconstructed CT images? This would provide a more intuitive understanding of the results.

 5.     The resolution of Figure 9 is too low, making it difficult to read the results.

 6.     The paper involves many hyperparameters but lacks any analysis or justification regarding their selection. Given the importance of these parameters to the model’s performance, a sensitivity analysis or at least a discussion on hyperparameter tuning would enhance the reliability and reproducibility of the results.

### Questions
1.     This manuscript is challenging to read, with disorganized logic and non-standard, unprofessional expressions:
	•	The paper only lists existing methods without clearly identifying their limitations or explaining the motivation for the proposed approach.
	•	Expressions such as “During a CT experiment” and “CT experimental time” are imprecise and lack professionalism.
	•	The statement, “The object is rotated stepwise around a central axis,” is misleading; typically, it is the source and detector that rotate, not the object itself.
	•	Phrases like “Combining several such projections, a specialized algorithm” are vague and difficult to understand. Please clarify.
	•	The sentence, “it can also lead to morphological deformation in the sample due to extended radiation exposure,” seems to imply that deformation results from patient motion over extended scan times.
	•	The phrases “In one approach,” “In another approach,” and “In a third approach” might be referring to sparse-view CT, limited-angle CT, etc. However, other forms of incomplete projection data also exist, which could be covered or referenced in a comprehensive review article [1].

[1] Wang T, Xia W, Lu J, et al. A review of deep learning ct reconstruction from incomplete projection data. IEEE Transactions on Radiation and Plasma Medical Sciences, 2023.

2.     The so-called “novel blending algorithm” proposed in this paper is, in fact, a common practice in CT reconstruction from incomplete measurements.

3.     The term “realistic simulated data” raises ambiguity regarding the authenticity of the experimental data; it is unclear whether the data are from real experiments or simulations. Although the paper emphasizes the importance of physics-based loss functions, there is no detailed description of imaging parameters. Additionally, the use of “re-project” suggests that the projection data may not be genuine, but rather re-generated, which further questions the authenticity of the data used.

4.     Since the method uses FBP with a reconstruction loss, why not present the reconstructed CT images? This would provide a more intuitive understanding of the results.

5.     The resolution of Figure 9 is too low, making it difficult to read the results.

6.     The paper involves many hyperparameters but lacks any analysis or justification regarding their selection. Given the importance of these parameters to the model’s performance, a sensitivity analysis or at least a discussion on hyperparameter tuning would enhance the reliability and reproducibility of the results.

### Soundness
2

### Presentation
1

### Contribution
2
