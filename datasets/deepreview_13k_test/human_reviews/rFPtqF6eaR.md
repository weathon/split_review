# Training Physics-Driven Deep Learning Reconstruction without Raw Data Access for Equitable Fast MRI

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
\noindent Physics-driven deep learning (PD-DL) approaches have become popular for improved reconstruction of fast magnetic resonance imaging (MRI) scans. Even though PD-DL offers higher acceleration rates compared to existing clinical fast MRI techniques, their use has been limited outside specialized MRI centers. One impediment for their deployment is the difficulties with generalization to pathologies or population groups that are not well-represented in training sets. This has been noted in several studies, and fine-tuning on target populations to improve reconstruction has been suggested. However, current approaches for PD-DL training require access to raw k-space measurements, which is typically only available at specialized MRI centers that have research agreements for such data access. This is especially an issue for rural and underserved areas, where commercial MRI scanners only provide access to a final reconstructed image. To tackle these challenges, we propose \textbf{C}ompressibility-inspired \textbf{U}nsupervised Learning via \textbf{P}arallel \textbf{I}maging Fi\textbf{d}elity (CUPID) for high-quality PD-DL training, using only routine clinical reconstructed images exported from an MRI scanner. CUPID evaluates the goodness of the output with a compressibility-based approach, while ensuring that the output stays consistent with the clinical parallel imaging reconstruction through well-designed perturbations. Our results show that CUPID achieves similar quality compared to well-established PD-DL training strategies that require raw k-space data access, while outperforming conventional compressed sensing (CS) and state-of-the-art generative methods. We also demonstrate its effectiveness in a zero-shot training setup for retrospectively and prospectively sub-sampled acquisitions, attesting to its minimal training burden. As an approach that radically deviates from existing strategies, CUPID presents an opportunity to provide equitable access to fast MRI for underserved populations in an attempt to reduce the inequalities associated with this expensive imaging modality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This manuscript proposed an unsupervised approach to improve MR DICOM image quality by introducing the loss term $l_{comp}+\lambda l_{pif}$, where $l_{comp}$ is to suppress noise and $l_{pif}$ is to keep fidelity to the input.

### Strengths
This manuscript is well-written, and the figures are well-drafted.

### Weaknesses
1. The motivation is weak. Starting reconstruction from DICOM output rather than raw k-space is unusual for MRI practitioners, as it does not allow us to construct the encoding operator, $\mathrm{E}$.

2. The title is misleading: claiming a "physics-driven" approach while dismissing the need for raw k-space data is contradictory. In MRI, k-space data represents the underlying physical imaging process.

3. The reported results for the baseline method, scoreMRI, are questionable, with performance significantly below that in the original publication.

4. The novelty and contribution of this work are limited. The author attempted to improve the image quality with the proposed loss term $l_{comp}+\lambda l_{pif}$, where $l_{comp}$ is to suppress noise and $l_{pif}$ is to keep fidelity to the input. In my eyes, this is a simple combination of existing approaches for MRI image quality enhancement.

### Questions
1. Refer to Weakness 1, how the coil sensitivity and sampling pattern are handled in the $\mathrm{E}$?

2. Refer to Weakness 2, how to construct the $\mathrm{E}$ for scoreMRI?

3. The proposed method resembles SSDU, yet its performance is reportedly better to CUPID. Could you clarify the reason for this?

### Soundness
2

### Presentation
3

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
The article proposes a deep-learning reconstruction method without having access to multi-coil $k$-space data. For the full-column-rank forward operator $E_{\Omega}$ and the under-sampled $k$-space $\textbf{y}$, the authors assume access to $E_{\Omega}^+ \textbf{y}$ where $+$ denotes the Moore-Penrose inverse. Compared to having access to fully sampled $k$-space as in fully supervised reconstruction, or undersampled $k$-space as in self-supervised reconstruction, this assumption is less restrictive. The proposed method was shown to perform on par with PD-DL methods requiring $k$-space data at relatively low acceleration rates ($4\times$).

### Strengths
1. The data access assumption is less restrictive compared to fully- and self-supervised reconstruction methods, and the article focuses on a real-life problem, as raw k-space access is a known limitation in this field.
2. The method is physics-based; thus, it is expected to be less prone to hallucinations compared to methods that do not utilize the forward operator.
3. The method was tested in various settings, focusing on both retrospective and prospective undersampling.

### Weaknesses
1. The quantitative results table is missing the standard error of the mean, which is crucial for a fair comparison.
2. It is incorrect to say that equispaced undersampling patterns were not explored in score-based models. In fact, the authors have already cited at least one article ("Robust Compressed Sensing MRI with Deep Generative Priors") that explored equispaced undersampling, discussing it not only in the appendix but also in the main text (e.g., Fig. 2, 9, 10). 
3. The generative method baseline is weak and outdated, given how rapidly state-of-the-art methods are advancing.  Several approaches published in the last 12 months can achieve better results. Including this particular method is fine, but labeling it as state-of-the-art is misleading.

### Questions
1. Does the clinical PI reconstruction readily allow saving the complex-valued image without any research agreements, or does it only allow the magnitude image to be saved? I am asking because it is rare to see a DICOM dataset containing anything other than magnitude images.
2. Regardless of whether ScoreMRI is state-of-the-art, its performance appears unexpectedly low. Is it possible that it was significantly under-trained? In our experience, these models require much longer training times compared to unrolled networks, which might explain why it underperforms even at $4\times$.
3. The choice of perturbations seems somewhat arbitrary. Could you elaborate on this choice? Learning the perturbations simultaneously with reinforcement learning could also be a potential direction for future work.
4. In Figure $2$, loss function, the left hand side was written as $\mathcal{L}(\mathbf{x}^{(k)}, \mathbf{x_{PI}})$ but the $\mathcal{L}_{\text{comp}}$ on the right hand side has $\mathbf{x}^{(m)}$ rather than $\mathbf{x}^{(k)}$. Is this intentional or a typo? 
5. Line $151-152$, while unrolled methods achieved top positions in reconstruction challenges three years ago, it is unknown if they remain the highest performers. To the best of my knowledge, no recent, fair comparison between state-of-the-art diffusion and unrolled methods has been published, including a reader study to compare their clinical effectiveness.

**Minor comments** 

* The fastMRI knee matrix size is $320\times 320$, not $320\times 368$. Please see Table 1 in DOI: 10.1148/ryai.2020190007
* Line $42-43$, demand have shown -> demand has shown
* Line $269$, shapes that has different intensity values -> shapes that have different intensity values
* Line $46$, Fig.$1$ -> Fig. $1$, the space was omitted in most, if not all, references to figures, tables, and sections.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper present an novel MRI reconstruction method that only requires dicom data (even undersampled data), with the motivation that rural regions won't have the raw data access. The key idea is through using random perturbations.

### Strengths
1. I like the idea of using random image domain perturbations, sounds like a good way to capture pior distribution.
2. I appreciate the authors for the experiments on the prospective undersampled MRI reconstruction, which is a very important experiment for all MRI reconstruction tasks.

### Weaknesses
Overall, there are a few weaknesses that concerns me:
1. I didn't really buy the idea of this rural region raw-data access. why we need raw-data? its for the training purpose! we already have a great number of raw k-space data (from fastMRI, mridata.org and others), as long as we have a good model trained, the rural regions can just use it without any training. In the end of the day, all MRI scanner will sample raw k-space data, so the whole motivation doesn't sound solid to me. 
Meanwhile, from what i understand from your method, the input is CG-SENSE of undersampled MRI, is it realistic? the input quality is not really diagnoistic.

2. The presentation is not very clear and the paper is not well-writtened, all the method section for your method is condensed to one *single* page with a figure (figure 2), i have to go back and forth to understand whats R, whats DF, and how you do the perturbations, thats supposed to be the main part of the paper.

3. The score-MRI results look kinda weird to me, try to look at other generative models. It shouldn't be that bad.

4. Figure 3, the result doesn't look good to me, over smoothing textures.

### Questions
1. how do your method compared to single-coil DL-based reconstruction.
2. how sensitive is your method to different input? (different vendors tend to have different reconstruction pipelines.)

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
4

### Summary
This paper proposes a loss formulation for unsupervised MRI reconstruction that directly operates on under-sampled DICOM images, bypassing the need for raw k-space measurements. The proposed loss involves a reweighted L1 loss term that enforces compressibility of the output image and a consistency loss term under designed perturbations to prevent trivial solutions. The method is shown to also work in a scan-specific setting. The experiments were conducted on knee and bran scans of fastMRI datasets with 4x acceleration and equidistant undersampling patterns, as well as prospective undersampled images.

### Strengths
- The loss design is reasonable.  
- The overall method is succinct and achieves very competitive performance.
- Evaluated the method on both retrospectively and prospectively undersampled datasets.

### Weaknesses
1: In [1], equivariance to image perturbations is also enforced alongside the measurement consistency term. Given the similarity, what makes the proposed method work so much better than [1] ?  
2: The authors mention that the overfitting issue here is not as severe as in other self-supervised scan-specific methods due to $L_{comp}$. However, $L_{comp}$ is also associated with some important parameters that are subject to manual tuning. It's not clear how those choices would affect overfitting. 

[1] "Equivariant Imaging: learning beyond the range space." Chen et al., ICCV 2021.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2
