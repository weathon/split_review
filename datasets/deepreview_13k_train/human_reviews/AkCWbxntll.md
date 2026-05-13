# GBIR: A Novel Gaussian Iterative Method for Medical Image Reconstruction

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Computed Tomography (CT) and Magnetic Resonance Imaging (MRI) are crucial diagnostic tools, but undersampling techniques like Sparse-View CT (SV-CT) and Compressed-Sensing MRI (CS-MRI), aimed at reducing patient exposure and scan time, make image reconstruction more challenging. While deep learning-based reconstruction (DLR) methods have made significant strides, they face limitations in adapting to varying scan geometries and handling diverse patient data, hindering widespread clinical use.
  In this paper, we propose a novel **G**aussian-**B**ased **I**terative **R**econstruction (**GBIR**) framework that uses learnable Gaussians representations for personalized medical image reconstruction, addressing the shortcomings of DLR methods. GBIR optimizes case-specific parameters in an end-to-end fashion, enabling better generalization and flexibility under sparse measurements. Additionally, we introduce the **M**ulti-**O**rgan Medical Image **RE**construction (**MORE**) dataset, comprising over 70,000 CT and MRI slices across multiple body parts and conditions.
  Our experiments show that GBIR outperforms state-of-the-art methods in both accuracy and speed, offering a robust solution for personalized medical image reconstruction.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a 3D Gaussian-based iterative reconstruction framework, termed Gaussian-Based Iterative Reconstruction (GBIR), to address the challenge of sparse sampling reconstruction in various medical imaging applications. Inspired by the 3D Gaussian splatting technique, this method reconsiders the practical demands of medical imaging, suggesting the abandonment of the splatting operation. Instead, it leverages 3D Gaussian representations to discretize the data into a volumetric form and applies an iterative reconstruction framework. Extensive experiments demonstrate that GBIR significantly outperforms other baseline methods. Additionally, the paper introduces a comprehensive Multi-Organ Medical Image REconstruction (MORE) dataset.

### Strengths
- This paper presents an efficient iterative reconstruction framework based on 3D Gaussian representation, introducing a set of strategies to enhance reconstruction efficiency. These include: 1) a 3D Gaussian representation truncated using the 3-sigma principle, and 2) efficient volume reconstruction through decomposition and parallelization. Experimental results demonstrate that these measures significantly reduce the spatial and temporal complexity of the reconstruction process.

- Additionally, this paper proposes a comprehensive multi-organ medical image reconstruction dataset, which, if open-sourced as anticipated, would provide substantial value to the research community.

### Weaknesses
 - The paper presents an extensive comparison of quantitative results; however, it lacks any qualitative comparisons. In the field of medical image reconstruction, qualitative comparisons often provide a more accurate reflection of a method’s true performance. As the saying goes, “Visual results don’t lie.”

 - Recently, several studies have proposed incorporating the principles of 3D Gaussian representation into medical image reconstruction [1-4]. There has also been some exploration of approaches that employ 3D Gaussian representation without using a splatting process [1,3]. This suggests that the proposed method may lack sufficient novelty. The authors should conduct a more comprehensive literature review in their paper and compare their method with SOTA 3D Gaussian-based techniques for medical image reconstruction.

> [1] Cai, Yuanhao, et al. "Radiative gaussian splatting for efficient x-ray novel view synthesis." European Conference on Computer Vision. Springer, Cham, 2025.

> [2] Zha, Ruyi, et al. "R $^ 2$-Gaussian: Rectifying Radiative Gaussian Splatting for Tomographic Reconstruction." arXiv preprint arXiv:2405.20693 (2024).

> [3] Fu, Xueming, et al. "3DGR-CAR: Coronary artery reconstruction from ultra-sparse 2D X-ray views with a 3D Gaussians representation." International Conference on Medical Image Computing and Computer-Assisted Intervention. Cham: Springer Nature Switzerland, 2024.

> [4] Li, Yingtai, et al. "Sparse-view ct reconstruction with 3d gaussian volumetric representation." arXiv preprint arXiv:2312.15676 (2023).

 - In line 161, the authors state that "DIFGaussian is based on 3D Gaussian splatting, whereas our proposed GBIR does not involve any ‘splatting’ process." However, to my knowledge, DIF-Gaussian also does not utilize a ‘splatting’ process, as discussed in detail in [MICCAI 2024 - Open Access Page](https://papers.miccai.org/miccai-2024/448-Paper0250.html).

 - The authors conducted experiments on the compressed sensing MRI reconstruction task; however, they appear to have omitted specific details regarding the task setup, such as the exact acceleration factors and sampling patterns used.

### Questions
- In line 161, the authors state that "DIFGaussian is based on 3D Gaussian splatting, whereas our proposed GBIR does not involve any ‘splatting’ process." However, to my knowledge, DIF-Gaussian also does not utilize a ‘splatting’ process, as discussed in detail in [MICCAI 2024 - Open Access Page](https://papers.miccai.org/miccai-2024/448-Paper0250.html).

- The authors conducted experiments on the compressed sensing MRI reconstruction task; however, they appear to have omitted specific details regarding the task setup, such as the exact acceleration factors and sampling patterns used.

### Soundness
2

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
3

### Summary
The article proposes a reconstruction method by learning Gaussian representations and illustrates the method using sparse-view CT and compressed-sensing MR image reconstruction. Furthermore, the authors provide a new dataset of CT and MRI slices across multiple anatomies.

### Strengths
- The idea of learning Gaussian representations for medical image reconstruction is novel.
- The introduction of a multi-organ CT and MRI dataset is beneficial, as public datasets containing certain anatomies are quite rare.

### Weaknesses
 **The discussion on previous work on Compressed-Sensing MRI is very limited**

Related Work section skips a lot of significant work in MR image reconstruction and focuses on lesser-known methods. Part b, titled "Compressed-Sensing MRI", skips the development of physics- and deep-learning-based reconstructions via unrolling networks such as ISTA-Net (Zhang, J., & Ghanem, B. ), MoDL (Aggarwal, H. K., Mani, M. P., & Jacob, M. ), and Variational Network (Hammernik, K., Klatzer, T., Kobler, E., Recht, M. P., Sodickson, D. K., Pock, T., & Knoll, F. ). Similarly, examples of generative MRI reconstruction methods need to include  more well-known methods than those which were cited. For example, a well-known method is Robust Compressed Sensing MRI with Deep Generative Priors (Jalal, A., Arvinte, M., Daras, G., Price, E., Dimakis, A. G., & Tamir, J.). 

**Section 3 contains multiple unconventional choices**

- Target volume in MRI is not real-valued but complex-valued: Section 3 does not account for the domain of MR images since $\mathbf{V}\in\mathbb{R}^{C\times H\times W}$ is incorrect. To model volumes as Gaussians, one needs to use complex-valued Gaussian random vectors. 
- In Equation 12, $M$ and $\hat{M}$ are complex valued $k$-space measurements for MRI. The Structural Similarity Index Measure (SSIM) is applied in measurement domain. SSIM, as given in the Appendix A.2., cannot handle complex-valued inputs. Also, SSIM is designed to assess similarity between images, not between complex-valued frequency domain measurements. The authors need to explain how SSIM is used in this context. 

**Issues in Experiments Section**

- The dataset used (BRATS) does not contain raw $k$-space data. It only provides preprocessed, magnitude-only MR images in the image domain. This basically means one cannot perform under-sampling and simulate compressed-sensing MRI without _inverse crimes_, i.e., see "Implicit data crimes: Machine learning bias arising from misuse of public data" (Shimron et al.). There are many extensive, public $k$-space datasets that one can use for MR image reconstruction, such as SKM-TEA, M4Raw, and fastMRI to avoid inverse crimes. 
- In MR image reconstruction experiments, no details regarding the undersampling parameters were provided. 
- Both in SV-CT and CS-MRI quantitative results tables (Table 4 and 5), only the average values were provided. For a fair comparison, standard error or similar deviation measures need to be provided. 
- The baselines used are relatively weak and may not represent the state-of-the-art. There are several recent variants of unrolled networks such as ISTA-Net, MoDL, and Variational Network that might perform better than the provided baselines.

### Questions
1. How do you calculate SSIM between measurements, especially when they are complex-valued, with extremely dense centers and very small outside regions?
2. How do you choose the $\lambda_i$s in Equation 12? The SSIM term is a similarity measure, while the other two are loss functions.
3. DuDoRNet is not mentioned anywhere in the text but is used in the table.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a mixture of Gaussian-based reconstruction scheme for CT and MRI. The main idea is to learn the means of the Gaussian mixture components on a per patient basis, and then use this representation for volumetric reconstruction. Computational cost reduction is proposed using neighborhood processing, though the reconstruction still takes ~8 hours per subject. They also introduce a new database for medical image reconstruction with both CT and MRI data.

### Strengths
1) Authors introduce a new dataset, MORE, containing both MRI and CT data.
2) Authors are aware that the patient-based Gaussian mixture model takes a long time in training, so they propose to use a neighborhood processing approach to reduce computational time.
3) Results are shown on different datasets.

### Weaknesses
Unfortunately, the authors seem to not be aware of a large body of literature in medical image reconstruction, particularly for MRI.

1) The authors are unaware of physics-driven methods that are considered the state-of-the-art in MRI reconstruction. These have better generalization abilities, as the forward operator is explicitly used for data fidelity in reconstruction.

2) A lot of emphasis is placed on the well-known 3-sigma argument for computational efficiency. However, the way the neighborhoods are implemented with a k \times k \times k cuboid shows the authors treat their Gaussians as isotropic. Yet, each Gaussian is specified to be non-isotropic with a covariance function \Sigma_k in (4). Thus, the assumption does not reconcile with the reality, as \delta should depend on the covariance function.

3) I cannot find where the authors discuss how they learn \Sigma, though I can see they talk about learning \mu. Without learning \Sigma, this is just a combination of isotropic Gaussians with shifted means. For learning \Sigma, how is this modeled, as it cannot possibly be modeled as a full-rank Hermitian matrix? How about initialization etc? Please provide all the details.

4) Eq. (11) for MRI suggests the authors are unaware that virtually all MRI raw data is multi-coil.

5) The authors test their MRI methods on BRATS dataset. Unfortunately, this dataset contains no raw data. Thus, it looks like the authors transformed the DICOM data to k-space and treated this as raw data. This is problematic for a number of reasons, please see Shimron et al, doi: 10.1073/pnas.2117203119.

6)  Related to the previous two points, MRI reconstruction and CT reconstruction do not even have the same output size. The former is complex-valued (i.e. 2 channels), while the latter is real-valued (i.e. 1 channel). So it does not even make sense to assume one would generalize to the other for standard DL techniques.

7) MORE dataset is interesting. On a minor note, details are missing on demographics. On a more major note, it is unclear if there are any matched MRI/CT data on the same subjects or if this is a mere concatenation of an MRI dataset and a CT dataset? Finally, does the MRI data actually contain raw data or just DICOMs? From the previous methodology and results, it seems like the latter is the case.

8) The authors propose to learn new parameters for each patient. If training is done per subject, of course, there would be no "generalization" issue, but this comes at the cost of a long reconstruction time (8 hours per dataset according to Table 3!) which would make this method clinically unusable. 
Furthermore, there are scan-specific training methods for aforementioned physics-driven reconstructions, which have been published in ICLR, e.g. Yaman et al, ICLR 2022.

9) The MRI comparisons are outdated. Nobody would use AUTOMAP for MRI reconstruction. Please use more relevant methods listed in the fastMRI challenges, e.g. Muckley et al, doi: 10.1109/TMI.2021.3075856.

10) The most relevant methods to the current proposed method are reconstruction schemes based on Gaussian processes, some examples include:
- Xu et al, doi: 10.1038/s41598-023-39533-4
- Ye et al, doi: 10.1101/2024.10.08.617197
as well as well-known processing approaches, such as:
- Andersson et al, doi: 10.1016/j.neuroimage.2015.07.067

It would be good to highlight how the current work compares to these ideas.

11) (minor) The method only applies to volumetric reconstruction. There are several MRI scan setups that are performed as 2D with slice gaps. It is unclear how the method extends to those cases.

### Questions
I mentioned these in my weaknesses, but I'll repeat here:
1) Is \Sigma_k learned?  If so,  how are these covariance matrices modeled, as they cannot possibly be modeled as full-rank Hermitian matrices? How about initialization etc? 
2) For MORE dataset: Does the MRI data actually contain multi-coil raw data or just DICOMs? Are there any matched MRI/CT data on the same subjects or if this is a mere concatenation of an MRI dataset and a CT dataset?

### Soundness
2

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
4

### Summary
This paper presents a  Gaussian-Based Iterative Reconstruction for reconstructing medical images, specifically CT and MRI scans.

### Strengths
1. This method utilizes learnable 3D Gaussian functions for personalized medical image reconstruction.
2. GBIR outperforms state-of-the-art methods in both speed and accuracy, particularly under sparse measurement conditions. The introduction of the MORE dataset also adds significant value.

### Weaknesses
1. While GBIR performs well in accuracy and generalization, the method introduces additional computational complexity compared to traditional deep learning methods. A more detailed analysis of the computational trade-offs, especially regarding memory consumption and training times on larger datasets, could improve the paper. Specifically, the paper lacks a breakdown of the computational cost associated with the iterative optimization process, including the forward and backward passes for each Gaussian parameter update. This makes it difficult to assess the practical scalability of the method.

2. deep learning and optimization-based methods, emerging techniques such as diffusion models are only briefly addressed. A deeper exploration of how GBIR stacks up against the latest diffusion-based methods could provide more comprehensive insights into its comparative strengths and limitations. The discussion should include a more detailed analysis of the differences in reconstruction quality, particularly in terms of preserving fine details and handling noise, as well as a comparison of the computational cost of the different approaches.

### Questions
1. How's the performance of GBIR conduct on  prospective dataset? Including a prospective experiment will be strengthen the robustness of this method.

2. The paper does not provide a figure that illustrate the framework.

### Soundness
2

### Presentation
2

### Contribution
3
