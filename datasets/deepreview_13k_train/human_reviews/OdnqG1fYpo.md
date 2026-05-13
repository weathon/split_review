# Moner: Motion Correction in Undersampled Radial MRI with Unsupervised Neural Representation

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Motion correction (MoCo) in radial MRI is a particularly challenging problem due to the unpredictability of subject movement. Current state-of-the-art (SOTA) MoCo algorithms often rely on extensive high-quality MR images to pre-train neural networks, which constrains the solution space and leads to outstanding image reconstruction results. However, the need for large-scale datasets significantly increases costs and limits model generalization. In this work, we propose \textbf{Moner}, an unsupervised MoCo method that jointly reconstructs artifact-free MR images and estimates accurate motion from undersampled, rigid motion-corrupted \textit{k}-space data, without requiring any training data. Our core idea is to leverage the continuous prior of implicit neural representation (INR) to constrain this ill-posed inverse problem, facilitating optimal solutions. Specifically, we integrate a quasi-static motion model into the INR, granting its ability to correct subject's motion. To stabilize model optimization, we reformulate radial MRI reconstruction as a back-projection problem using the Fourier-slice theorem. Additionally, we propose a novel coarse-to-fine hash encoding strategy, significantly enhancing MoCo accuracy. Experiments on multiple MRI datasets show our Moner achieves performance comparable to SOTA MoCo techniques on in-domain data, while demonstrating significant improvements on out-of-domain data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a novel INR that includes motion modeling, allowing for rigid motion-corrected reconstructions. The motion is modeled using translation and rotation parameters to deform a canonical image space, and then transform the the image using the Fourier slice theorem to compute the data consistency loss with the acquired k-space data.
Evaluation is conducted on simulated motion-corrupted brain data (2 public datasets) and the individual proposed components (motion model, Fourier slice theorem, coarse-to-fine has encding) ablated.

### Strengths
The following strengths can be observed within the paper:
- The inclusion of a motion model for MR reconstruction is sound and by leveraging the Fourier slice theorem, the inclusion directly in image-space allows simple motion modeling.
- The work includes extensive evaluation, including several comparison methods as well as reasonable ablation studies.
- The paper is nicely structured.

### Weaknesses
The present work poses some major and minor weaknesses:
Major:
- The evaluation is exclusively conducted on simulated motion-corrupted data, which raises the question of its actual applciability in real settings. Particularly considering that motion artefacts not only arise from the physical movement, but also from resulting field inhomogenieties, etc., the simulation procedure might be too simplified and the model is likely to simply adapt to these parameters. If the work is aimed at MR motion-correction methods within a clinical workflow, testing the method on in-vivo data is mandatory.
- In this work, it is claimed multiple times, that the Fourier slice theorem is a crucial part of their work and this works novelty. Yet, the Fourier slice theorem was already introduced a while ago (Catalan 2023 et al,  	https://doi.org/10.48550/arXiv.2307.14363) and used in several works after. While it is definitely aiding the method, it should be cited and not included as novelty. 
- Within the results, "significant improvement" (l., 365/l.431) is often claimed, the standard deviation (e.g. in table 2) and statistical tests should be reported to support this statement. Similarly for the improvement claim regarding Table 4: Statistical testing would be helpful, since the standard deviation reported opens up questions the actual improvement

Minor:
- For full reproducibility, it would be nice to mention all post-processing steps conducted before quantitative evaluation (nect to registration mentioned in A1, e.g. if normalization was conducted, etc.?)
- There are several typos which can be corrected (line326, 504,...)

### Questions
- For the motion simulation, are all spokes corrupted by motion? Or how many spokes are chosen to be affected? Realistic motion patterns in brain would be individual lines, but this is not specified. Can you generally provide more details on the motion simulation, e.g. was only the physical movement considered / what motion patterns were the inspiration for this simulation / were any secondary motion effects considered? 
- In line 151 it is mentioned, that the methods overlook the high dynamic range problem, yet it is considered in some of the mentioned works (e.g. Huang 2023)?
- The low-frequency bias mentioned in the introduction (l.182) is highly dependent on the network settings (activation function, etc.), yet this is not mentioned in the implementation details? 
- I would suggest to add significance testing to support the result claims within the text.
- In general, while the simulation evaluation is nice for a proof-of-concept, the models performance on real-world data would be very useful to evaluate its actual capabilities and highly recommended for any future work.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Moner, an unsupervised neural representation framework for motion correction (MoCo) in undersampled radial MRI, utilizing implicit neural representations (INR) to model motion without pre-training on high-quality MR datasets. Key innovations include a quasi-static motion model integrated into INR, reformulating MRI recovery as a back-projection problem via the Fourier-slice theorem, and a coarse-to-fine hash encoding strategy. Extensive experiments on fastMRI and MoDL datasets show that Moner not only achieves high-quality reconstructions but also demonstrates robustness across diverse acquisition conditions.

### Strengths
* Unsupervised Approach: Unlike many MoCo methods that require large pre-trained datasets, Moner’s unsupervised framework enhances generalizability and applicability across different MRI modalities.
* Motion Estimation and Stability: The quasi-static motion model and back-projection formulation stabilize model optimization, effectively reducing artifacts even in challenging motion-corrupted scenarios.
* Efficiency and Robustness: Compared to existing methods like Score-MoCo, Moner achieves superior out-of-domain (OOD) performance and faster reconstruction speeds, making it highly efficient and scalable.

### Weaknesses
 * Extension to 3D and Non-Radial Sampling Patterns: The current model primarily addresses 2D radial MRI, and while extensibility to 3D MRI is suggested, it remains untested. The same applies to Cartesian or spiral sampling patterns, which are common in clinical MRI. The lack of experimental validation in 3D or with non-radial trajectories significantly limits the practical applicability of the method.
* Reliance on Motion Assumptions: The quasi-static motion model assumes rigid motion between acquisition frames. Further clarification on its limitations in more complex motion settings could strengthen the study. Specifically, the model's performance under non-rigid motion, such as tissue deformation, or motion occurring within the acquisition window of a single spoke, is not addressed, which could be a significant limitation in real-world scenarios.

### Questions
1. Could the authors elaborate on potential strategies to adapt Moner for 3D MRI data or non-radial sampling patterns?
1. How might Moner’s performance change if the motion were non-rigid or occurred within acquisition frames?
1. What specific benefits does the coarse-to-fine hash encoding offer over traditional encoding techniques for motion correction?
1. What specific attributes of Moner contribute to its improved robustness on OOD data compared to Score-MoCo? Does the implicit neural representation (INR) framework offer an inherent advantage over diffusion-based priors in terms of adaptability to different MRI datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed an unsupervised motion correction method for undersampled radial MRI reconstruction, which fits implicit neural representation (INR) of the image to the observation (undersampled k-space with motion) at test time. MRI reconstruction with motion correction is a challenging task. Though applying INR to medical image reconstruction (e.g. MRI and CT) is not new, its application to motion correction is underexplored. This paper presents its great potential in solving the problem.

### Strengths
- The paper is overall well-written, presenting an interesting method valuable to the field.
- A good background introduction that let readers know what radial MRI reconstruction is.
- Methods were well represented, with motivation explained for each design choice.
- Extensive experiments and ablation studies prove the efficacy of the proposed method and individual design choices.

### Weaknesses
 - Experiments were only conducted on brain MRI datasets with similar contrast/MR sequence. Readers would be interested in how good the proposed method is on MRI images of different contrasts or taken at different body parts. Specifically, will the optimization still converge stably with the same optimization strategy (e.g. hash encoding) and hyperparameter choice? In addition, how does noise level affect the optimization process?
- How will trans-plane motion affect the stability of optimization?
- In Fig. 8, I notice that the reconstructed image looks blurry and lacks some thin structures like vessels. In other figures, images are too small to observe such details. I suggest authors show zoomed-in images from both baselines and proposed method for better comparison.
- Authors may want to report FOV and pixel spacing to let readers get a sense of the magnitude of motion ranges used in this paper.
- It is surprising to see that a supervised method (DRN-DCMB) is worse than an unsupervised method. In Fig. 4, DRN-DCMB results look very blurry, making me doubt if it is the SOTA supervised method. Authors may consider alternative baselines such as [1].

### Questions
- How were data from different coils handled in this paper? Were data from all coils fed into the model simultaneously during the optimization?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes to use implicit neural representations (INRs) to perform unsupervised joint reconstruction and motion estimation from undersampled and motion corrupted 2D radial MRI measurements.

The method achieves the best motion estimation results across datasets compared to classical and supervised deep learning-based methods for motion estimation. 
In terms of reconstructed image quality, the method falls behind supervised deep learning for in-distribution performance but exhibits much more robustness against out-of-distribution examples. 
In terms of computation time the method is 5-6 times faster than the diffusion model baseline requiring 3-5 minutes per 2D slice.

### Strengths
1.	(Originality) It is the first paper that explores the use of untrained neural networks (here in the form of INRs) for joint reconstruction and motion estimation. The proposed extensions in terms of an adapted hash encoding optimization schedule and a loss function in the projection space are interesting. 
2.	(Significance) The investigated problem of motion correction in (radial) MRI is important. The lack of training data from all possible domains required for the supervised baselines and the resulting lack of out-of-distribution robustness is a real problem and methods that are more robust are important. 
3.	(Quality/clarity) Overall the paper is well written, and the experiments seem to be of good quality. However, some additional information and explanations are required in my opinion (see weaknesses). If those can be addressed adequately, I'm willing to raise the score.

### Weaknesses
1.	It is not clear how the motion trajectories, e.g., in Figure 7 are simulated – more information should be provided. Are there fixed intervals after which motion changes direction? In between those events does every spoke has its own motion state meaning that 300 spokes result intro estimating 300*3=900 unknowns? How does this model change when the number of spokes changes due to a different acceleration factor?
2.	Section 4.1 does not contain enough information about the dataset used in the experiments. More information should be provided either in the main body or the appendix. 25 test slices is not much depending on how the data is selected. Are the 25 slices the entire slices from e.g. two subjects or are they 25 mid-slices from 25 subjects? The fastMRI dataset is very diverse. Are the subjects for training and testing taken from the same contrasts, e.g., T2 weighted or FLAIR? What is the main difference of the MoDL dataset to the data used from the fastMRI dataset? This information is important to assess the severity of the distribution shift. From Figure 4 it seems that the main difference is the view being axial and coronal respectively. Are there any other differences?
3.	The comparison of the computational speed would benefit from a more detailed discussion. Where do the differences in terms of speed come from? How can the TV method with 200 epochs be slower than the INR with 4000 epochs? What is responsible for the speed difference compared to the diffusion model – the size of the networks or the number of steps? (What is the size of the MLP that is used?)

### Questions
1.	Is formulating the loss in the projection space specific to the radial sampling trajectory or can it also be used for e.g. Cartesian sampling as well?
2. It would be helpful to add scores to the qualitative comparisons in e.g. Figure 4 to provide a better feeling how differences in the scores translate to perceivable differences.
3. Why is the diffusion model baseline categorized as self-supervised e.g. in line 309? As the model requires fully sampled data for training I would consider it as a supervised baseline. 
4. How many spokes are acquired for the acceleration factors of 2 and 4 respectively?

### Soundness
3

### Presentation
3

### Contribution
3
