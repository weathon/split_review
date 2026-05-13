# Revealing the 3D Cosmic Web through Gravitationally Constrained Neural Fields

- Decision: Accept
- Scores: 8, 3, 3, 6

## Abstract
Weak gravitational lensing is the slight distortion of galaxy shapes caused primarily by the gravitational effects of dark matter in the universe. In our work, we seek to invert the weak lensing signal from 2D telescope images to reconstruct a 3D map of the universe’s dark matter field. While inversion typically yeilds a 2D projection of the dark matter field, accurate 3D maps of the dark matter distribution are essential for localizing structures of interest and testing theories of our universe. However, 3D inversion poses signficant challenges. First, unlike standard 3D reconstruction that relies on multiple viewpoints, in this case, images are only observed from a single viewpoint. This challenge can be partially addressed by observing how galaxy emitters throughout the volume are lensed. However, this leads to the second challenge: the shapes and exact locations of unlensed galaxies are unknown, and can only be estimated with a very large degree of uncertainty. This introduces an overwhelming amount of noise which nearly drowns out the lensing signal completely. Previous approaches tackle this by imposing strong assumptions about the structures in the volume.  We instead propose a methodology using a gravitationally-constrained neural field to flexibly model the continuous matter distribution. We take an analysis-by-synthesis approach, optimizing the weights of the neural network through a fully differentiable physical forward model to reproduce the lensing signal present in image measurements. We showcase our method on simulations, including realistic simulated measurements of dark matter distributions that mimic data from upcoming telescope surveys. Our results show that our method can not only outperform previous methods, but importantly is also able to recover potentially surprising dark matter structures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
***Late review: Apologies my review is in one day late. I will aim to engage as quickly as needed to makeup.***

This very interesting paper considers a very important application, although using some well-established tools in machine learning and computer vision. The paper focuses on the difficult weak-lensing regime, where deflections are too weak to be interpretable reliably for a single galaxy. The idea is that attempting to understand how weak lensing alters (or shears) images of galaxies in dense fields, one could reconstruct a density map of the underlying matter. This is a difficult problem as the matter density is usually analyzed in 2D: the measured shear map is used to recover a projected 2D estimate. The paper aims to solve the inverse problem i.e. to obtain a 3D reconstruction of the dark matter field from 2D images. From a modeling perspective, this becomes challenging as galaxies are observed from a single view. Further, unlensed shapes of known visible sources are themselves not fully understood, introducing a large amount of uncertainty. The main idea of the paper is to use the underlying physics of gravitational lensing to recover a continuous 3D field, with a focus on also capturing non-Gaussian features, which are not easy with traditional methods, which use strong priors. The idea is to use coordinate-based neural fields augmented with the underlying physics (clearly described in figures 1 and 2), with the total loss function described in equation 7. The experiments, over simulated data, are able to show that the method has promise in both reconstructing the 3D matter field and also non-Gaussian features.

### Strengths
-- The paper attacks a problem of quite some importance. While the machine learning used is standard, its combination with the underlying physics allows the authors to obtain a promising solution, although it is only tested on simulations (standard for this area of physics at the moment). 

-- The paper is well-written, well-structured and easy to follow. While I am not an expert in this specific application, I have worked in some adjacent applications. I think the results support the underlying proposal and motivation well, and are creative in combining standard ML tools with physics-based models.

### Weaknesses
 -- More of a question: Could the authors elaborate in the paper why are strong Gaussian priors usually made? This will not be obvious to a standard ML audience. I see that it could make sense from the perspective of filtering. But I am not sure I understand why this should drop out from the physics models. I would expect the features to be highly non-Gaussian. I find this confusing whenever I venture to look at papers in this area.

-- Could the authors elaborate on the training protocols and how difficult it was to get stabilized training? From the writeup, it is not clear how easy it is to get the model to work.

### Questions
-- Could the authors elaborate on the training protocols and how difficult it was to get stabilized training? From the writeup, it is not clear how easy it is to get the model to work.

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
2

### Summary
The paper provides a new method for recovering the 3D cosmic web from galaxy weak lensing signal.
The proposed approach uses a coordinate-based neural field method with positional encoding. (Equation 6).
The reconstruction results are demonstrated in a series of experiments.

### Strengths
* The paper proposes a new method for an important physics problem.
* The paper is well-written; I enjoyed reading it.
* The physics background is exceptionally well-presented, and even non-experts can understand the main scientific ideas.
* The proposed method works better than the leading baseline.

### Weaknesses
I think this is a great paper, but in my opinion, ICLR might not be the best venue for this.
The new machine learning contributions are quite limited: neural field models and positional encoding have been around for some time, and I didn't find significantly new machine learning contributions in the paper.

Nonetheless, the proposed algorithm works well, and the physics application, estimating the 3D cosmic web, is a very important problem.
Since the most significant contributions of the paper are in astrophysics, I think an astrophysics or cosmology journal would be a better venue for this paper.

### Questions
* I would like to know some more details about the number of CPUs/GPUs used for training, memory requirements, and the training and inference time of the proposed method.

* I'm also curious about the next steps. After the 3D cosmic web estimation step is done, what are the next science questions that can be answered with the new results?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The article considers the task of reconstructing a 3D map of the universe from weak gravitational lensing obtained in 2D signals. The methods consider first to encode the overdensities using a neural field based on the spherical coordinate and its Fourier decomposition.  The target density field is used for two purposes: (i) to match the power spectrum of the dataset under consideration and (ii) to match the shear observed (after using the transformation from overdensity to shear) in the data. The method is tested on simulated data mimicking the instrumental observations from an N-body simulation. The results show that the method seems better than using Wiener filter for the same task.

### Strengths
The authors apply ML techniques to a dataset that is different from the usual benchmarks.

### Weaknesses
My overall impression is that we have just an application of ML methods to a cosmological problem, which neither
- make relevant improvement on the side of ML (unless I'm mistaking, it takes out-of-the-box methods)
- make a strong advance in the considered field
I would like the authors to comment on how their work is particularly timely. I'm also thinking that the Wiener filter is not very modern. By quickly looking on the web, we can find more elaborated techniques:
 * sparsity prior: https://www.aanda.org/articles/aa/pdf/2021/05/aa39451-20.pdf, https://arxiv.org/pdf/1801.08945
 * wavelet: https://www.aanda.org/articles/aa/pdf/2006/21/aa2997-05.pdf
And I can imagine there are many others. This work does not provide any comparison to these methods.

The last section that investigate non-Gaussian structure is a bit of a mystery to me. Does the application of the method to MNIST (whatever it means) should be considered of a test of something precise ? In addition,

### Questions
- it might be useful to related the various red-shift to a number of years, it is done for z=0 and z=2 but not for z=1. 
- The caption of Fig. 3 says: "results includes 12 lens planes from redshift z=0 to z=1", can the authors specify the precise value of the considered z ?
- In addition, the authors say that they average over 3 lens planes. Why ? to which values of z does that correspond ?
- The ground truth images are blurred with a factor that maximize the cross-correlation with the reconstructed picture. It seems a bit weird to do so, it might bias the reader to believe that a reconstruction is better than what it should be.
- The cross-correlation between the reconstructed signal and the true one seems quite small... while we can agree that it is even worse using the Wiener filter, I have the impression that it is working very-well.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method for reconstructing the underlying 3D dark matter distribution from weak gravitational lensing observations (specifically, shape distortions of galaxies). This is an important problem in cosmology, and is of contemporary relevance given the number of astronomical surveys which will be measuring galaxy shapes. The overall approach is to model the dark matter distribution implicitly through a neural network (NeRF-like or implicit neural representation), and use a differentiable forward model that models the observed shear field. The authors compare the method to a few traditional approaches for mass mapping, finding it to especially perform well in reconstructing non-Gaussian structures.

### Strengths
- **Novel approach and good technical execution:** Using an implicit representation to model the underlying dark matter field along with a differentiable forward model is a very neat but challenging idea, and the authors set it up and executed it very well. 
- **Paper straddling AI and fundamental physics:** This is a bit of a meta point, but AI + physics (in particular a sub-field like cosmology) is not particularly mainstream at AI conference so far, in contrast to e.g. AI + bio. This makes presenting a paper like this while being faithful to the domain science particularly challenging, and the authors do a good job in this respect.
- **Simulation realism:** The authors use a realistic set of tools from the cosmology literature, e.g. JaxPM in the differentiable forward model, making it a contribution beyond a simple proof-of-principle. 
- **Baseline comparisons:** Comparisons with baselines are well-presented, and highlight the advantage of the method in particular regimes (e.g. in recovering non-Gaussian structures).

### Weaknesses
 - **Context in current literature and state of the field:** There exists substantial literature in neural approaches to mass mapping; e.g., https://arxiv.org/abs/2201.05561. While the authors compare to traditional approaches like Kaiser-Squires (KS) and Wiener filter, they do not contextualize their work in the more recent ML-based approaches to weak lensing mass mapping. Another example is https://arxiv.org/abs/2206.14820, which uses an implicit neural representation to perform *strong* lensing reconstruction; high-level comparison with existing literature could be improved. The lack of comparison with other ML-based methods makes it difficult to assess the true novelty and performance gains of the proposed approach. Specifically, the authors should discuss how their method compares in terms of computational cost, data requirements, and reconstruction accuracy with these existing ML-based mass mapping techniques.
- **Hyperparameter choices:** The authors mention specific hyperparameter choices, e.g. bandwidth of positional encodings L=2 and 5, without further justification. This should be expected to have a significant impact on the results, as it controls the spectral biases of the implicit representation, and should be further expanded upon, possibly including ablations. The choice of positional encoding bandwidth directly influences the ability of the neural network to capture different spatial frequencies in the dark matter distribution. Without a clear understanding of how these choices affect the reconstruction, it's difficult to assess the robustness and generalizability of the method. A more systematic exploration of the hyperparameter space is needed, including a discussion of the trade-offs between different bandwidth values.
- **Role of induced prior:** Traditional approaches typically have a regularization mechanism, often explicit, which allows for mass reconstruction (since the inverse problem is fundamentally ill-posed). In this study, the authors mention that "neural fields have been shown to provide a good implicit prior"; while true in the real-world setting of scene reconstruction, scientific problems are inherently different in nature, and it is not clear a-priori whether the implicit prior induced by the neural field is a good one. The authors approach this empirically, however further understanding of the role of induced priors is necessary for downstream science from the mass maps. The implicit prior induced by the neural network could be biasing the reconstruction towards certain types of structures, potentially leading to inaccurate results. A more thorough analysis of the induced prior is needed, possibly by comparing the power spectrum of the reconstructed mass maps with the expected power spectrum from simulations. This would help to quantify the impact of the implicit prior on the reconstruction and identify any potential biases.

### Questions
- The authors use an ensembling approach, taking the median to get a point estimate on the reconstructed mass map. Much of the ongoing literature/effort is focused on _probabilistic_ approaches to mass mapping. The authors mention in a footnote that ensembling can lead to good predictive uncertainties -- can it be expected that this can be used to yield a calibrated distribution over plausible mass maps? If not, are there alternative approaches to this incorporating neural fields, e.g. variational or Bayesian approaches?
- What is the role of bandwidth $L$ and the induced spectral bias in the study? How does the induced prior compare with that assumed in traditional and model ML-based approaches?

### Soundness
3

### Presentation
3

### Contribution
3
