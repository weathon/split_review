# X-Diffusion: Generating Detailed 3D MRI Volumes From a Single Image Using Cross-Sectional Diffusion Models

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
In this work, we present \textit{X-Diffusion}, a cross-sectional diffusion model tailored for Magnetic Resonance Imaging (MRI) data.
X-Diffusion is capable of generating the entire MRI volume from just a single MRI slice or optionally from few multiple slices, setting new benchmarks in the precision of synthesized MRIs from extremely sparse observations. The uniqueness lies in the novel view-conditional training and inference of X-Diffusion on MRI volumes, allowing for generalized MRI learning.
Our evaluations span both brain tumour MRIs from the BRATS dataset and full-body MRIs from the UK Biobank dataset. Utilizing the paired pre-registered Dual-energy X-ray Absorptiometry (DXA) and MRI modalities in the UK Biobank dataset, X-Diffusion is able to generate detailed 3D MRI volume from a single full-body DXA. Remarkably, the resultant MRIs not only stand out in precision on unseen examples (surpassing \sota results by large margins) but also flawlessly retain essential features of the original MRI, including tumour profiles, spine curvature, brain volume, and beyond. Furthermore, the trained X-Diffusion model on the MRI datasets attains a generalization capacity out-of-domain (\eg generating knee MRIs even though it is trained on brains). The code is available on the project website \url{https://emmanuelleb985.io/XDiffusion/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduces a new model for generating detailed 3D-MRI volumes from sparsified spatial-domain inputs, resulting in accurate 2D-to-3D scans reconstruction (in contrast to existing methods that require full 3D scans). The main idea is to incorporate view-dependent cross-sections during training, which is different from the current approaches.

### Strengths
The authors demonstrate superior performance in several benchmarking tasks, including brain tumor and full body MRIs. 

The authors claim that the proposed model is able to generalize to novel domains, not seen during the training. 

The problem, motivation and contributions are clearly stated. 

Thorough experiments were conducted, methodically supporting the claims in paper. The idea of conditioning MRI reconstruction on different cross-sectional viewpoints seems novel.

### Weaknesses
There are no measurements on how fast the X-diffusion is. It would be beneficial to include comparisons with previous approaches. E.g., Figure 3 shows that for good quality reconstruction, almost T=1000 steps are required. 

The limitations discussed in Sections 6 and 7 appear to be strong, potentially limiting the practical value of the work. 

The authors dismiss the study of whether it is possible to reduce the number T in diffusion without sacrificing the quality? And how would this reduction be specific to medical imaging domain? (can simply substitute ideas of speeding up from text-to-image models?)

### Questions
It would be interesting to see how X-Diffusion works with other types of augmentations, like blurring, changing colorspace etc. Intuitively, this should boost ability to generalize OOD or at least improve algorithm compared to using only SO3.

Author’s do not discuss what are the benefits of using pretrained VAE from SD without any additional finetuning (i.e VAE is frozen) to specific MRI domain. Additional discussion would be great. 

Is it possible to integrate and check performance using existing text-to-3D models. Seems like utilizing directly 3D generative model provides more inductive bias, which should improve learning.

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
4

### Summary
This paper introduces X-Diffusion, a novel MRI reconstruction algorithm that can generate 3D volumes by conditioning on single or few slice 2D MR input. In contrast to traditional MRI reconstruction, X-diffusion takes on a different challenge and tries to predict the entire 3D volume given the sparse (but uncorrupted/high-quality slice(s)). The authors conduct a variety of different experiments on multiple datasets and downstream tasks and test the meaningfulness of pathological findings in the reconstructed images. Given their experimental setting, they are able to challenge the state of the art.  In a variety of ablation studies, the authors assess the impact of individual key components, providing an explanation of the capability of the model.

### Strengths
Originality: While the proposed method is built upon recent advantages in computer vision, its combination of key components and area of application is novel. Especially the cross-sectional MRI synthesis approach, which enables the stacking of slices from arbitrary viewing directions, not just axial/coronal and sagittal planes, is of particular interest to the medical imaging community and constitutes - to the best of my knowledge - a unique contribution of the paper.

Quality: The paper is written in a very clear, concise, and comprehensive way. I believe the authors did a great job in setting their method into the context of related work, thoroughly and clearly describing it, and performing an interesting experimental section, including further experiments in the supplementary material. The ablations clarified and addressed questions that I previously had when reading the manuscript and addressed different important parameters of the pipeline, demonstrating the effectiveness of the key components, such as the stable diffusion encoder, etc. 

Clarity: The presented method, related work, and experiments are on point. Ablations serve a purpose, the mathematical foundation behind key concepts was explained quite well, and figures and tables provided a great way of deepening the understanding of the reader. The supplementary offered a lot of great insights and the possibility for reproduction of experiments. 

Significance: The method of synthesizing a 3D volume with a cross-sectional model from arbitrary viewing directions is very interesting to the medical imaging community. Also, X-Diffusion tackles a unique reconstruction scenario, which is very much unexplored.

### Weaknesses
1) Clinical relevance of the presented method:

While the clinicians in this paper argue that the model is clinically relevant - I have a conflicting opinion. While "scout" or "localizer" scans with a single or a few slices may be acquired and thus used for X-Diffusion, I believe it is dangerous to assume that these will substitute a real volumetric scan. While the authors argue that tumor information is preserved, I would rather say this information is correctly hallucinated. Especially small tumors and lesions in other neurodegenerative diseases, such as MS, often occur on a few or single slices. Given that single or few-slice acquisitions will not be able to capture this information- (at all) - I would argue only undersampled or lower-resolved images pose a clinical tradeoff between finding anomalies and reducing scan time. I feel deep learning-based reconstruction really introduces a well-motivated use case for super-resolution or reconstruction in these problem settings, especially when considering multiple (complementary contrasts), but - to me - single/few slices are far-fetched and thus X-Diffusion solves a rather unrealistic clinical setting? Consequently, I would dial this down in the manuscript and frame this more as an exploratory or proof of concept study, i.e., "confirmed the potential usefulness of the generated MRIs" feels a bit bold to me.

I would also be curious to see how the introduced method (key components would still have merit for these problem settings!) would perform on SR settings where we try to super-resolve anisotropic to isotropic scans. On another note, I acknowledge and really appreciate the study of k-space reconstruction. This poses a much more clinical use case, where X-diffusion is powerful but not on par (at least in scores) with SOTA (please correct me if I am wrong).

2) Difficulty in assessing how much is owed to conditioning with the "right" slices and the capability of the model:

While in regular medical image reconstruction, images are generally downsampled (in k-space) (c.f. ScoreMRI) or images with lower resolution are upscaled (TPDM), X-Diffusion has access to high-quality 2D slices that constitute a relevant part of the GT. In other words - the conditioning slices are not altered (i.e., they are identical and part of the GT). This is very different from the traditional scenarios - and thus poses a unique challenge in assessing the quality of the reconstruction. While the authors compare against SOTA baselines, these baselines were not originally designed to work as X-Diffusion works. This should be highlighted and discussed more prominently in the manuscript. I understand it is hard to come up with appropriate baselines, given that X-Diffusion is the first to attempt a single 2D slice to 3D reconstruction. However, the challenges that come with evaluating this should be more prominently discussed.

3) Downstream Evaluation:

Evaluation of the brain volume: While the brain volume estimation may serve as a first good downstream analysis task, I believe it constitutes an oversimplification of the problem. It would have been more meaningful to perform brain white-/grey matter analysis using, e.g., freesurfer on ground truth and reconstructed volume and comparing the results of this.

4) Please share the SSIM for all tables and experiments; these values are often more relevant to PSNR values for reconstruction.

5) A1 and A3 are almost identical. Consider merging or rewriting them to have one cohesive section.

### Questions
Clarification:

- I really appreciate the ablation for healthy patient inpainting, c.f. 6.4, but it would have been really important to know how many healthy slices were used for the inpainting experiment. How many tumors do we see if we only provide slices at the outer parts of the brain where tumors will not lie? 

- For Figure 3, please clarify how many input slices are utilized from the target image. Considering the leftmost image is considered as input, am I right to assume that single-slice conditioning was utilized? However, given the crisp reconstruction, I would be surprised if this is the case. Was there tumor information in the conditioning - or is all of it impainted?

- For Figure 6, which image(s) were used to condition X-Diffusion - was any of the tumor information of the presented slice present in the slice? If so, it is not surprising that the X-diffusion model is able to recover this 

- For Figure 9, Figure II/II Appendix (and more)  - how many slices were used to condition the model? 

Suggestions:

- Please add SSIM scores alongside to the PSNR in the reconstruction experiments to the main paper (from supplementary).
- Consider adding deep learning-based metrics for image reconstruction, such as medical LPIPS (https://docs.monai.io/en/stable/losses.html#perceptualloss) or LPIPS (https://github.com/richzhang/PerceptualSimilarity), as these often correlate better with human perception and are widely used in medical image reconstruction as well.

### Soundness
3

### Presentation
4

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
The authors propose a diffusion-based approach to reconstruct 3D MRI volumes from a single or multiple 2D slices. Their approach is conditioned by the target rotation and slice index and relies on heavy pre-training. It is applied to brain MRI (with and without tumours), whole-body MRI and knee MRI.

### Strengths
- Both the approach and the application appear quite novel.
- Many experiments were performed.

### Weaknesses
 - The experiments are confusing. It is as if the authors tried all they could think of and let the readers do what they can with the results.
- A major point that is often unclear in the experiments/results is what slice(s) was/were used as input. If the authors show in Figure VI that is has a impact on the results, it is not specified in other sections, e.g. 5.1, 5.2, 5.3, 5.4. 
- The way the authors split the BraTS dataset is not clear. On the one hand, they state that the dataset includes 5,880 MRI scans from 1,470 patients (roughly four MRI sequences per patient) and that they split it into Train (n=4704), Validation (n=588), and Test (n=588) sets, without mentioning if it is done at the subject level or not, which could mean data leakage. On the other hand, they say that they just use the FLAIR sequence, so then the numbers do not add up. Please clarify.
- When difference maps are displayed there is no scale, on top of the colormap poorly chosen, so they are impossible to analyse.
- No estimate of variation is provided in the tables.
- The evaluation by medical experts, though valuable, confirms that images generated are realistic but not that they show what they are supposed to, i.e. an image could be realistic but not correspond to the reality of a patient.
- More philosophically speaking, I fail to understand how the authors see what they propose used in practice, which is what they state they aim for. In their scenario, patients would come to the imaging centre, have 2D slices acquired and pseudo 3D volumes reconstructed and then what? Would they go home and maybe be called to come back and have a normal exam later? If so in what case? This does not seem cost-efficient nor practical.
- The related work section should cover super-resolution approaches. Also the Full-Body MRI Analysis paragraph is very generic and pretty empty. See for instance Tunariu et al., British Journal of Radiology, 2020 on the use of whole-body MRI in clinical practice and Küstner et al., Radiology: Artificial Intelligence, 2020 for the automatic analysis methods related to these applications.
- Some references are too generic or do not correspond to the statement they are supposed to comfort, e.g. Tran et al., 2015; Sohl-Dickstein et al., 2015 or Kawar et al., 2022 in the second paragraph of the introduction.

### Questions
- Please see weaknesses above.
- Please fix the hyperref links, many references in the Appendix do not point to the good figure, this makes the paper even more difficult to follow.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The proposed manuscript explores the use of a conditional generative model which can produce a full 3D MRI volume conditioned only on 1 or MRI slices. The authors conduct experiments with three MRI datasets that span brain, whole-body, and out-of-distribution knee MRI scans. Overall, this study could be improved with a justification of why such an approach that has no test-time data consistency should be favored over conventional deep learning based variational reconstruction methods that are very common and quite robust.

### Strengths
*	Multiple datasets are used for the evaluation
*	The diffusion based benchmarks are chosen well and represent some of the latest approaches in the field.

### Weaknesses
*   Many of the approaches that are used for MRI reconstruction rely on the notion of data consistency, which can ensure that there is consistency between the reconstructed imaging data and the extent of signals that are actually obtained. The proposed approach provides no sense of such confirmation. Specifically, it lacks a mechanism to enforce agreement between the synthesized slices and any acquired k-space data, which is a fundamental aspect of many established reconstruction techniques. This raises concerns about the fidelity of the generated images, particularly in the context of clinical applications where accuracy is paramount.
*   It is mostly an impractical scenario where a single high-resolution slice will be obtained instead of obtaining multiple undersampled slices. So the overall premise of the work unfortunately seems more academic rather than something that would have a clinical impact. In realistic clinical settings, acquiring multiple undersampled slices is standard practice due to time constraints and patient comfort. A method that relies on a single high-resolution slice does not align with current clinical workflows and therefore its practical utility is questionable.
*   In prior work, there is a very incomplete analysis of work in image reconstruction and super-resolution. It is unclear what “classical” means. based on the references, does classical mean anything without foundation models? This doesn’t seem accurate. The distinction between "classical" and other methods needs to be clarified, and a more thorough review of relevant literature, including recent advances in variational and deep learning-based reconstruction methods, should be provided.
*   In figure 4, the acquisition is actually axial and study depicts the acquisition to be coronal. Since there is always a fully sampled dimension readout dimension in MRI, the reformatting of this 3D volume does not accurately convey the representational capacity of the model. Actual slice traversal needs to be in the *true* slice direction. The model's ability to generate accurate images should be demonstrated in the actual slice acquisition direction to properly assess its performance.
*   A better evaluation would be show a progression of PSNR values the further away a test slice is being computed from a conditioning slice. This would provide insight into the model's ability to generalize and maintain image quality across different regions of the volume.
*   All datasets had 155 slices. In the case of using 31 conditioning slices, it is not clear why one should use this approach instead of just undersampling the 3D data by 5x and then reconstructing with variational methods. These methods can easily provide accelerations of 8-10x with much higher metrics. The rationale for using the proposed method over established, high-performing variational methods when a significant number of conditioning slices are available is not adequately justified.
*   In figure 6, up until 10-13 slices, there are significant hallucinations in the structure and contrast of the grey and white matter. These results would cause radiologists quite a bit of anxiety! Like the previous point, at this point, why not just use a variational reconstruction method? The presence of such significant artifacts raises serious concerns about the clinical applicability of the method, especially given that variational methods could likely produce superior results with this amount of input data.
*   The results in Figure 6 and the massive impact in hallucinated details entirely reduces confidence in all 1-5 slice results. This further shows how poor a metric PSNR is. The reliance on PSNR as a primary evaluation metric is insufficient, particularly when visual inspection reveals substantial artifacts. Additional metrics, such as SSIM or LPIPS, should be included to provide a more comprehensive assessment of image quality.
*   Total brain volume is not the correct metric to assess fidelity. Cortical volumes and folding patters would be better. One would hypothesize that it is likely trivial to regress total brain volume from a single brain MRI slice anyway. More clinically relevant metrics, such as cortical thickness, surface area, and gyrification index, should be used to evaluate the anatomical accuracy of the generated images.
*   It is pretty shocking to me why the model should be able to work in the OOD setting to synthesize knee MRI scans? Can the authors please provide a rationale why this should work in the first place? The UKB dataset includes IDEAL fat-water sequences that are MUCH lower resolution than the 2D TSE knee MRI fastMRI sequences that have a proton density contrast. Why should the model know this distribution Section 6.3 attempts to answer this but simply claiming Stable Diffusion training and large non-domain specific datasets unfortunately does not seem convincing. The ability of the model to generalize to out-of-distribution data, particularly from brain MRI to knee MRI, is not adequately explained. A more detailed explanation of the underlying principles that enable this generalization is needed.

### Questions
*	Since H = W = D in this study, what would happen when the data is non-isotropic, as is most common in MRI applications and protocols.
*	For the example provided in Figure 5, it is interesting to think about why the method should work in the first place? Given that this is an ill-posed problem, why should a model be able to predict a slice that is 20 slices away accurately?
*	The better test would be to pick a conditioning slice that does not have a tumor but from a patient with a tumor. Then, will the model correctly produce a tumor? That is the real test. I hypothesize that there is no reason a model should be able to predict that. A brief sentence or two is included in the paper but this analysis can be made more rigorous. 
*	Spine curvature: What is the distribution of spine curvature? One may think this is regression to the mean of healthy spines. showing a Bland-Altmann or regression pot where would be better.

### Soundness
2

### Presentation
2

### Contribution
2
