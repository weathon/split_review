# Joint Denoising of Cryo-EM Projection Images using Polar Transformers

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Deep neural networks (DNNs) have proven powerful for denoising individual images, but there is a limit to the noise level they can handle.
In applications like cryogenic electron microscopy (cryo-EM), the noise level is extremely high but datasets contain hundreds of thousands of projections of the same molecule, each taken a different viewing direction.
This redundancy of information is useful in traditional denoising techniques known as class averaging methods, where images are clustered, aligned, and then averaged to reduce the noise level.
We present a neural network architecture based on polar representation of images and transformers that simultaneously clusters, aligns, and denoises cryo-EM projection images.
Results on synthetic data show accurate denoising performance using this architecture, with a relative mean squared error of $0.06$ at signal-to-noise (SNR) level of $0.05$, outperforming traditional filter-based methods by a factor of $2\times$.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper develops a strategy for jointly denoising single particle cyroEM particle projections. The proposed approach is based upon applying a CNN (to one image) or a transformer architecture (to many images) that is/are transformed into polar coordinates. The network architectures are specialized to have desirable invariances in the polar domains. The proposed method is tested on simulated data with varying amount of Poisson and Gaussian noise. The proposed method outperforms simple Weiner filtering.

### Strengths
+++Proposed method (using an invariant network to jointly denoise multiple images in the polar domain) is novel and well-motivated

### Weaknesses
---Contextualization/Practical relevance: The manuscript states the single particle reconstruction pipeline "involves first extracting images of individual particles from the micrographs, denoising these images, estimating their corresponding viewing directions, and then reconstructing a 3D density map". However, it is my understanding that modern reconstruction techniques (e.g., expectation maximization [A]) marginalize over the various view directions and avoid denoising the 2D projections all together. 
The manuscript mentions contamination detection as another possible use case for denoising, which may be valid. The manuscript needs to clarify which parts of the reconstruction pipeline it may and may not improve.

[A] Scheres, Sjors HW. "RELION: implementation of a Bayesian approach to cryo-EM structure determination." Journal of structural biology 180.3 (2012): 519-530.


---Weak baselines: The proposed method outperforms Weiner filtering by a large margin. How does it compare to advanced non-learning-based methods like BM3D? How does it compare to a conventional CNN without a polar transformation?

---Missing ablations: There is no evidence any of the proposed network choices are useful. How does the proposed method compare to a single U-net applied to cartesian coordinates? How important are the various architectural choices?

---Section 1 says the proposed method clusters, aligns, and denoises but the next section states it is assumed the images have been centered. If so, why is alignment necessary?

----How does proposed method compare to denoising entire micrographs?

---Typo: L464 a reference is missing

---Ignores CTF effects. To the paper's credit, this limitation is clearly acknowledged.

### Questions
How relevant is the proposed contributions in modern single particle cryoEM pipelines? Do denoisers have a role to play?

How does the proposed method compare to high-performance image denoisers?

Which of the design choices (e.g, polar coordinates) matter and which don't?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a deep learning approach to denoise cryo-EM images, which is challenging due to high noise levels and varied viewing directions. The authors apply polar representation within both proposed CNN and transformer models, achieving improved results in denoising.

### Strengths
1. Leveraging polar representation can simplify the denoising task by translating rotational variance into angular shifts. This approach is promising for denoising given the rotational nature of cryo-EM.
2. Using a dataset of 5,000,000 images strengthens the model's robustness and enables it to learn effectively from diverse viewing angles.
3. Testing both Gaussian and Poisson noise further validates the proposed model.
4. Testing both CNN and transformer architectures increases the reliability of the proposed method.

### Weaknesses
1. Some key details in the approximations lack mathematical measurements (see Q1).
2. Results are only compared to the Wiener filter method. Including comparisons with more state-of-the-art methods would be better.
3. Adding a mathematical proof explaining why and how polar representation improves denoising accuracy would strengthen the theoretical foundation of the approach (Related to Q3). 
4. At leat two typos. (See Q5).

### Questions
1. Could you provide more details on the approximations in Eq. (8) and Eq. (10), such as the error order?

2. Will your model work with negative binomial noise?

3. You stated that "f(R_alpha(x)) = R_alpha(f(x))" when f could be a statistical noise distribution. If we consider the denoising model H_theta as an inverse of a statistical noise distribution, would "H_theta(R_alpha(x)) = R_alpha(H_theta(x))"? If so, how does the polar representation improve accuracy? If not, could you explain the key difference?

4. In Section 5.2, I think "f_key" and "f_query" are symmetric. That is, using "m - l" in either should work. So, why is f_key chosen over f_query? I also wonder if adding both query and key with the same value, but with output as "S_l = (sqrt(2) / 2 * S_l_key) * (sqrt(2) / 2 * S_l_query)" would yield more accurate results, since it allows the model more freedom to learn more features.

5. On line 178 and 179, should “the” be changed to “they”? On line 229 and 230, should it be "L/2 - 1"? And on line 464 and 465, there is an a question mark.

### Soundness
2

### Presentation
2

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
This paper addresses denoising in cryo-EM images by designing a neural network that is equivariant to rotations. The authors achieve this by constructing a polar representation of the image and applying convolutions in this transformed space, thereby effectively converting the translational equivariance of standard convolutions into rotational equivariance. These _polar CNNs_ then serve as the key and query networks in a transformer to obtain a rotation-equivariant attention mechanism between images that should allow for solution of the full set denoising task, i.e. the implicit clustering of images by viewing angle for an improved denoising performance.

### Strengths
The paper is clearly written and provides a great introduction to the problem of denoising in cryo-EM reconstruction. The authors introduce their method step-by-step, making it easy to follow the rationale of each of their design choices.

The use of a polar representation to achieve rotational equivariance is innovative and well-founded, facilitating deep learning-based denoising that can leverage the signal from images taken at the same viewing angle without requiring an explicit preprocessing step to cluster by angle.

### Weaknesses
While the theoretical foundation of the method is convincing, the experimental validation of its effectiveness is lacking. 

The only baseline comparison is to Wiener filtering, with no comparisons to other deep learning-based methods, despite several being mentioned in the related work section. I suggest to include a comparison to at least one of the deep-learning based methods, such as the DnCNN (Zhang et al., 2017) or a U-Net denoiser adapted for cryoEM data.

Further, all experiments are conducted on simulated data. It therefore remains unclear whether the method would generalize to real data acquisitions as well. Do the authors envision the method to be trained on simulated data and then be applied to real data? In particular, the training and evaluation both use sets of images that only contain two viewing angles. How can this be achieved for real data? This apparent limitation is not discussed. I suggest the authors either 1) include experiments where they apply their method to real data or 2) discuss challenges they foresee in the application to real data, including possible domain shift and a random sampling of viewing angles.

In conclusion, the paper could be strengthened significantly by an extended set of experiments that show this theoretically-compelling method to work well in practice and a discussion of its real-world limitations. Specifically, I suggest the authors include a deep-learning based method as an additional baseline to make their evaluation more comprehensive and demonstrate or discuss the applicability of their method to real data. If application to real data is currently not feasible, I suggest to include a discussion of those limitations and an outline for future work for how those limitations could potentially be overcome.

### Questions
Questions:
- Are the weights shared between key and query networks?
- The conclusion mentions that important future work includes scaling the method to larger datasets. Which part of the method does not scale right now?

Typos/Format:
- L142: providing a stronger priors -> providing stronger priors
- L229/230: -L/2, ..., -L/2-1 -> -L/2, ... , L/2 -1 
- L269: fourier transform of $\phi$?
- L464: reference not resolved

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper deals with the denoising of images produced in the context of cryogenic electron microscopy (cryo-EM) single-particle analysis. In cryo-EM single-particle analysis, an electron microscope records 2D projections of the unknown 3D structure of a single type of particle (e.g., a specific protein) at random orientations. These projections can then be used to estimate a 3D model of the particle. Due to data acquisition limitations, the 2D particle projections have very low signal-to-noise ratios, requiring denoising.

The authors propose two novel deep learning architectures to improve the denoising of 2D particle projections: The Polar CNN and the polar transformer.
- The polar CNN is designed to be equivariant to 2D rotations. The authors argue that this property is desirable because the 2D particle projections capture the particle at random orientations.

- The polar transformer is based on the polar CNN and additionally exploits redundancy in the data by combining information from projection images that show the particle from a similar direction. 

The authors test their new architectures on synthetic data and compare them to denoising with a Wiener filter.

**Recommendation:** I do not recommend the paper for publication at ICLR. In my opinion, the weaknesses in the experiments outweigh the reasons to accept the paper (see "Weaknesses" for more details). However, I would like to emphasize that the paper has potential and I am willing to change my evaluation if all my concerns regarding the experiments are sufficiently addressed.

**Post rebuttal:** I have increased my score from **3 to 5**.  As part of their rebuttal, the authors have clarified the details of the angular attention mechanism. Moreover, they have included a comparison to a deep learning-based denoiser in which they show that the polar transformer architecture outperforms "vanilla" networks. Overall, I think that the proposed architectures are interesting contributions.
I have not increased my score further because one of the main concerns I described in my review remains: The authors have not tested their methods on real data which comes with additional challenges such as the need for self-supervised training due to the lack of ground truth.

### Strengths
- The use of architectures that are rotationally equivariant and explicitly exploit redundancy for denoising individual particle projections is a novel and interesting idea and has the potential to improve upon existing deep learning-based denoising methods.
- Experiments on synthetic data suggest that exploiting the redundancy in the data (as done by the polar transformer in the "directional" setup) is beneficial to the denoising performance.
- The paper is clearly written in most parts (only section 5.2 is a bit unclear, see "Weaknesses").

### Weaknesses
Major Weaknesses:


- Weaknesses in the experiments (Section 6):

	- The authors only compare their polar CNN and their polar transformer to a denoising Wiener filter, and there is no comparison to other deep learning-based denoisers, which typically outperform classical denoising methods. Good candidates for deep learning based baselines could be, e.g., CryoCARE [1] and Topaz [2].

	- There is no experiment that compares the denoising performance of a standard 2D convolutional network with that of a polar CNN and a polar transformer.
		Therefore, it is unclear how much denoising actually benefits from the equivariance properties of the polar CNN and the polar transformer. 

	- The authors train their polar CNN and their polar transformer in a supervised manner. In my opinion, this setup is not realistic, since pairs of noisy images and clean underlying ground truth are typically not readily available in cryo-EM single-particle analysis (see also "Questions").
		Perhaps it would be possible for the authors to consider self-supervised training without clean ground truth for their experiments. (This has already been done for methods such as CryoCARE and Topaz).

	- All experiments are on synthetic data. There are no experiments on real images produced with cryo-EM. This recent dataset proposed by Dhakal et al. [3] contains real cryo-EM images with picked particles. Maybe this data can be used for further evaluation. 


- Section 5.2 on angular attention, which is one of the central contributions of the paper, is unclear to me. There is no explicit definition of the angular attention layer $f_\theta^{\text{ang-attention}}$. I have formulated some questions about angular attention in the "Questions" section.

Minor weaknesses:
- It is unclear to me which parts of the polar CNN and polar transformer architectures are novel and which are from existing work. Perhaps the authors could make this clearer in the paper.
- This is more of a suggestion: Figures illustrating angular convolution and angular attention mechanisms might make these concepts a bit easier for readers to grasp.




--------------------------------------------
[1] Buchholz, Tim-Oliver, et al. "Cryo-CARE: Content-aware image restoration for cryo-transmission electron microscopy data." 2019 IEEE 16th International Symposium on Biomedical Imaging (ISBI 2019). IEEE, 2019.

[2] Bepler, Tristan, et al. "Topaz-Denoise: general deep denoising models for cryoEM and cryoET." Nature communications 11.1 (2020): 5208.

[3] Dhakal, Ashwin, et al. "A large expert-curated cryo-EM image dataset for machine learning protein particle picking." Scientific Data 10.1 (2023): 392.

### Questions
- Given the challenges associated with supervised training of a denoiser (see "Weaknesses"), how would the authors train a model that can be used to denoise real, experimental images? Is it possible for the model to generalize well from synthetic to real data?

- In lines 63 - 65, the authors state that denoising a micrograph is easier than denoising selected projections of individual particles. If this is true, wouldn't a method that denoises the entire micrograph *before* picking perform better than the authors' proposed approach of denoising individual particle projections? 

- Questions about angular attention:
	- Why are only the keys rotated by the angle $\alpha_\ell$? (line 373-374)
	- The authors state that "[they] apply a corresponding rotation to the value vectors". Does this require knowing the angle $\alpha_\ell$? If so, why can the angle be assumed to be known?
	- Could the authors please provide an explicit formula or algorithm for the angular attention mechanism?
		
- Why is the value net in the polar transformer "set to identity" (line 417)?

### Soundness
2

### Presentation
3

### Contribution
3
