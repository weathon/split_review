# Bi-modality medical images synthesis by a bi-directional discrete process matching method

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Recently, medical image synthesis gains more and more popularity, along with the rapid development of generative models. Medical image synthesis aims to generate an unacquired image modality, often from other observed data modalities. Synthesized images can be  used for clinical diagnostic assistance, data augmentation for  model training and validation or image quality improving. In the meanwhile, the flow-based models are among the successful generative models for the ability of generating  realistic and high-quality synthetic images. However, most flow-based models require to  calculate flow ordinary different equation (ODE) evolution steps in synthesis process, for which the performances are significantly limited by heavy computation time due to a large number of time iterations. In this paper, we propose a novel flow-based model, namely bi-directional Discrete Process Matching (Bi-DPM) to accomplish the bi-modality image synthesis tasks. Different to other flow matching based models,  we propose to utilize both forward and backward ODE flows and enhance the consistency on the intermediate images over a few discrete time steps, resulting in a synthesis process maintaining  high-quality generations for both modalities under the guidance of paired data. Our experiments on three datasets of MRI T1/T2 and CT/MRI demonstrate that Bi-DPM outperforms other state-of-the-art flow-based methods for bi-modality image synthesis, delivering higher image quality with accurate anatomical regions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a flow-based generative model aimed at improving medical image synthesis across different modalities (e.g., MRI T1/T2 and CT/MRI). Unlike traditional flow-based models that focus on a unidirectional path, the proposed method leverages forward and backward Ordinary Differential Equations (ODEs) to ensure consistency across intermediate image states, enhancing the synthesis process's accuracy and quality.

### Strengths
x. Bi-DPM matches intermediate states at discrete time points between forward and backward ODEs, enhancing consistency and allowing high-quality image synthesis that preserves anatomical details.

x. Loss function flexibility: The model incorporates a loss function that can handle both fully paired and partially paired datasets using metrics like LPIPS for perceptual similarity and MMD for unpaired data.

x. Empirical validation: Experiments conducted on MRI T1/T2 and CT/MRI datasets show that Bi-DPM outperforms state-of-the-art flow-based models, such as Conditional Flow Matching (CFM) and Rectified Flow (RF), in terms of SSIM, PSNR, and FID scores.

x. Clinical relevance and 3D image synthesis: The paper includes evaluations by physicians, where Bi-DPM-generated images were deemed highly realistic, with a Turing test indicating the difficulty in distinguishing these images from real ones.

### Weaknesses
x. **Need more elaboration on mathematical derivations**: While I understand the overall purpose of the derivations, some of the deeper mathematical proofs and their implications, like those in Remark 1, could be more thoroughly explained or connected to the practical advantages of the model. Specifically, the paper lacks a detailed explanation of how the specific form of the ODEs chosen impacts the stability and convergence of the training process, and how the chosen loss function relates to the underlying geometry of the data manifold. A more rigorous analysis of the conditions under which the proposed method guarantees a consistent mapping between the source and target domains would be beneficial.

x. **Over-argument**: In Section 3.2.4, while the authors present the slicing approach as a straightforward extension of their 2D method, they do not sufficiently explain how this adapts to or addresses the complexities of 3D medical imaging. This simplification might give the impression that applying 2D techniques to 3D data is easier than it is in practice. The paper does not address potential issues such as inter-slice inconsistencies, which are common in 3D medical image synthesis, and how the model ensures spatial coherence across different slices. The method's performance on 3D volumes should be explicitly discussed, including any limitations or assumptions made during the 2D-to-3D extension.

x. **Missing details on efficiency**: While Bi-DPM is described as computationally more efficient with larger step sizes, the paper does not provide detailed comparisons of training and inference times against other models. A computational resource analysis (e.g., time per training epoch, memory requirements) would be valuable for practical considerations. The paper should also include a more detailed analysis of the computational complexity of the proposed method, including the number of parameters and the computational cost of each step in the forward and backward ODEs, and how these scale with image size and the number of steps.

### Questions
x. **ODE step size**: How sensitive is Bi-DPM to changes in the ODE step size? Did the authors test different step sizes systematically, and what were the observed trade-offs in terms of computational efficiency and image quality?

x. **Hyperparameter selection**: How were the weight parameters $w_n$ for the loss function chosen, and how do they impact the training stability and results?

x. **Physician feedback**: What qualitative feedback did the physicians provide during the image evaluation, and were there specific features or characteristics that made the synthetic images more or less convincing? 

x. **Performance on unpaired data**: While Bi-DPM handles paired and partially paired data well, how does it perform on completely unpaired data? Is there a significant performance drop, and if so, what are the main challenges?

Minor: Segmentation may be considered a downstream task / additional metrics to evaluate image quality.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents Bi-Directional Discrete Process Matching (Bi-DPM) for bi-modality medical image synthesis. Bi-DPM employs a bi-directional process to align intermediate states across discrete time steps in both forward and backward directions with flow models. This method introduces a weighted "meeting point" loss, which includes terms for paired and unpaired data, allowing it to handle both types of data. By leveraging this bi-directional matching, Bi-DPM captures complex relationships between modalities, such as MRI T1/T2 and CT/MRI.

### Strengths
The method proposes a bi-directional recipe for the flow-matching models. Compared to methods like RF and CFM, the authors propose to constrain the consistency between intermediate states instead of restricting the velocity field to the difference. This allows a non-linear translation, as is shown in Fig. 2 and 3. 

The 2D toy results shows convincing results on preserving the bi-direction relationship, even with few paired data.

### Weaknesses
The methodology may have an advantage over RF and CFM, but the authors have picked a bad application scenario. My major concern is the applicability of such methods in medical imaging. Unlike style translation in natural images, anatomy consistency is the utmost crucial factor in translating images between modalities. The MMD in (8) seems to be a very weak constraint for anatomical consistency in unpaired data. Is it even doable to translate medical images? Why can you recover T1/T2 properties of protons in the magnetic field given the HU in CT, there is as far as I know no theoretical ground to support this.

The results involved a physician rating, but the point here is not about letting them tell if the image is realistic. One can produce realistic images with many methods, like styleGAN, cycleGAN, etc., and many methods can do the same thing. The authors should have asked the question, “does the translated image tell the same information as the real images from the machine?”. The answer is probably no, because the resultant SSIM of CT-MRI is below 0.70. With such a low SSIM, most of the diagnostic-crucial information cannot be recovered. The algorithm is making random guesses in many areas. However, the accuracy of details are important for this task in clinical scenarios.

The experiments were not well-conducted, lacking ablation studies on hyper-parameters like the weight of the unpaired data MMD loss, which can be important for the final performances. The datasets are too small for a solid evaluation of the methods (described in sec. 3.2).

The figures of the paper are relatively hard to read, and the font size of the legends in Fig.5/7 is too small.

### Questions
Notation inconsistency: “X1 follows the target distribution q(z)” (line 064) “X1~q(x)” (line 065), should be “X1~q(z)” I suppose. Line 132, “to measures”. 

The paper doesn’t consider some state-of-the-art unpaired/partially paired data translation methods (e.g. Schrödinger Bridge methods and some GAN-based methods other than CycleGAN, which is relatively out of date.).

In the training settings, the paper uses an equal proportion of the unpaired data and the paired data (line 366). But the training data consists of different proportions of the paired data (1%, 10%, 50%, and 100% illustrated in the experiments). The methods of augmenting the data to balance it into equal proportions must be specified.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript presents a novel flow-based method called Bi-directional Discrete Process Matching(Bi-DPM). The method utilizes both forward and backward ODE flows and enhance the consistency on the intermediate images to maintain high-quality generation under the guidance of paired data. Notably, it achieves significant improvements in PSNR, FID and SSIM, demonstrating the superior performance.

### Strengths
1.	Innovative Approach: This manuscript introduces an innovative flow-based model of medical image synthesis techniques to enhance the consistency on the intermediate images over discrete time steps in flow-based models, which helps maintaining pair information through synthesis process.
2.	Significant Empirical Improvements: The method substantially improves PSNR, FID and SSIM scores, demonstrating its effectiveness over existing methods.
3.	Detailed Methodological Framework: This manuscript presents a well-structured and comprehensive methodological framework, introducing the use of both forward and backward flow ODEs to preserve paired information.

### Weaknesses
1.	This manuscript lacks of sufficient description of the motivation and necessity of using both forward and backward ODE flows, I can’t see the necessity of this operation. The authors may add more detailed description on this. Specifically, the manuscript does not clearly articulate why enforcing consistency between forward and backward flows at intermediate steps is crucial for maintaining paired information. The connection between this consistency and the smoothness of the velocity field is not sufficiently explained, leaving the reader to question the core rationale behind this bidirectional approach.
2.	There lacks of implementation details. I would suggest the authors to add some description on their implementation. For example, the specific architecture of the neural network used to parameterize the velocity field, the optimization algorithm, and the loss function are not described in sufficient detail. The lack of these details makes it difficult to reproduce the results and assess the practical applicability of the proposed method.
3.	The authors claim that diffusion models can not be directly used to perform image-to-image translation tasks, I wonder how do the authors draw this conclusion. I have read some researches doing this task using diffusion models, I recommend the authors to read these relevant references and add a comparison experiment with diffusion model. They are listed below:
[1]Graf, Robert, et al. "Denoising diffusion-based MRI to CT image translation enables automated spinal segmentation." European Radiology Experimental 7.1 (2023): 70.
[2]Ozbey, Muzaffer, et al. “Unsupervised medical image translation with adversarial diffusion models.” IEEE Transactions on Medical Imaging 42. 12(2023): 3524-3539.
[3]Kim, Jonghun, et al. “Adaptive Latent Diffusion Model for 3D Medical Image to Image Translation: Multi-modal Magnetic Resonance Imaging Study.” IEEE Winter Conference on Applications of Computer Vision 2023: 7604-7613.
4.	The only GAN used for comparison is CycleGAN, which is proposed in 2017. It seems out of date to me. I strongly suggest the authors to add comparisons with more advanced GAN models.
5.	The authors mentioned that the proposed Bi-DPM allows for a faster transfer process. I suggest the authors to add an experiment showing superior image synthesis speed to support their conclusion.
6.	I noticed that in the partially paired data results, 2-step Bi-DPM performs poorer than 1-step Bi-DPM when the paired ratio is low, can the authors add more detailed explanation on this phenomenon?

### Questions
1.	The authors claim that diffusion models can not be directly used to perform image-to-image translation tasks, I wonder how do the authors draw this conclusion. I have read some researches doing this task using diffusion models, I recommend the authors to read these relevant references and add a comparison experiment with diffusion model. They are listed below:
[1]Graf, Robert, et al. "Denoising diffusion-based MRI to CT image translation enables automated spinal segmentation." European Radiology Experimental 7.1 (2023): 70.
[2]Ozbey, Muzaffer, et al. “Unsupervised medical image translation with adversarial diffusion models.” IEEE Transactions on Medical Imaging 42. 12(2023): 3524-3539.
[3]Kim, Jonghun, et al. “Adaptive Latent Diffusion Model for 3D Medical Image to Image Translation: Multi-modal Magnetic Resonance Imaging Study.” IEEE Winter Conference on Applications of Computer Vision 2023: 7604-7613.
2.	The only GAN used for comparison is CycleGAN, which is proposed in 2017. It seems out of date to me. I strongly suggest the authors to add comparisons with more advanced GAN models.
3.	The authors mentioned that the proposed Bi-DPM allows for a faster transfer process. I suggest the authors to add an experiment showing superior image synthesis speed to support their conclusion.
4.	I noticed that in the partially paired data results, 2-step Bi-DPM performs poorer than 1-step Bi-DPM when the paired ratio is low, can the authors add more detailed explanation on this phenomenon?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel bi-directional discrete process matching method to model the bi-modality image synthesis tasks. This method utilizes the both forward and backward ODE flow and enhances the consistency across each intermediate images. The method only requires a few discrete time steps for inference. The method can be used for variety of paired and unpaired datasets.

### Strengths
- The paper proposes novel bi-directional flow-based method for medical two modality synthesis, each can take advantage of paired information in two modality and keep consistent cross modalities. 
- The paper is well-written and easy to follow. 
- The paper considers variety of use cases including 3D image synthesis, pairs and unpaired datasets.

### Weaknesses
 - For diffusion-based generative method, after modification, these models can be used for two-modality synthesis task.
- To keep each intermediate step matching on the flow trajectory from backward and forward direction, it might hurt the ability the model's generalization ability.
- Figures are too small to read.

### Questions
- Can the authors provide more comparison between your method with other diffusion based method, such as latent diffusion model?
- Can the authors provide some experiments on unseen data to test the generalization of your proposed method, such as EGD dataset?Chakrabarty, Satrajit, et al. "MRI-based classification of IDH mutation and 1p/19q codeletion status of gliomas using a 2.5 D hybrid multi-task convolutional neural network." Neuro-Oncology Advances 5.1 (2023): vdad023.
- Can the authors provide some comparisons between the effects on step size for MRI synthesis of proposed method, since there is only 1-step and 2-step size results?

### Soundness
3

### Presentation
3

### Contribution
3
