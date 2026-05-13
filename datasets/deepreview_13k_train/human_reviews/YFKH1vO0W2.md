# From Noise to Factors: Diffusion-based Unsupervised Sequential Disentanglement

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Unsupervised representation learning, in particular, sequential disentanglement, where the goal is to learn disentangled static and dynamic factors of variation, remains a significant challenge due to the absence of labels. Existing models, based on variational autoencoders and generative adversarial networks, achieved success in certain domains, but they often struggle with disentangling sequences, especially when dealing with real-world complexity and variability. Further, there is no real-world evaluation protocol for assessing the effectiveness of sequential disentanglement models. Recently, diffusion autoencoders have emerged as a new promising generative model, offering semantically rich representations by gradual noise-to-data transformations. Despite their advantages, these models face limitations: they are non-sequential, fail to disentangle the latent space effectively, and are computationally intensive, making them difficult to scale to sequences. In this work, we introduce our diffusion sequential disentanglement autoencoder (DiffSDA), a novel approach effective on real-world visual data and accompanied by a new and challenging evaluation protocol. DiffSDA is based on a new probabilistic modeling and is implemented using latent diffusion models and efficient samplers, facilitating processing of high-resolution videos. We test our approach on several real-world datasets and metrics, and we demonstrate its effectiveness in comparison to recent state-of-the-art sequential disentanglement methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a probabilistic model for disentangling static and dynamic features from a series of videos, expanding on the idea of DiffAE. Specifically, the authors expand DiffAE to denoising a series of images, and factorize $z_{sem}$ to $s$ and $d$ which stands for static and dynamic features. A simplified score matching object is also utilized and empirically shows reasonable results for reconstruction. Moreover, the authors experimented on various disentanglement-oriented experiments including conditional/unconditional and zero-shot swapping, and also latent probing.

### Strengths
1. The PGM factorization is natural and elegant, and the network design are simple but effective.
2. Quantitative results shows good reconstruction and swapping. Qualitative results also demonstration good disentanglement and generation capacity.

### Weaknesses
1. Experiments are mostly shown on short sequence face/motion datasets, where the static feature is appearance and dynamic feature being the keypoints/expressions. Under the framwork that the author proposed, ideally longer sequences should facilitates the disentanglement of $s$ and $d$.
2. It's not clear if the effect of disentanglement comes mostly from the factorization, or from the fact that $d$ has small size and $s$ has larger size.

### Questions
1. It's not required, but would be good if the authors include the derivation of the training objective from the score matching objectives.
2. Would like to see the comparison and results on longer sequences.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper is concerned with the problem of learning disentangled generative models for sequential (e.g. video) data. It proposes a method based on the Diffusion VAE framework that splits the latents into two groups - static (does not vary with frame) and dynamic (varies per frame). The proposed method is benchmarked on a number of (single) person-centric datasets.

### Strengths
* Generally well-written and clear.
* Strong empirical results on the chosen benchmarks.
* The proposed solution to obtaining disentangled representations is interesting in that it relies on the structure of the model rather than auxiliary losses.

### Weaknesses
 **Major**
* The paper touches on the problem of disentangled representation for sequential data in general. However, the presented experiments are limited - they only make use of simple (single person) video data. This does not give a fair picture of the methods usefulness and applicability because (i) it targets only a single modality; and (ii) because even within this modality the model targets very structured datasets (e.g. single view, single object). The method's ability to generalize to more complex scenarios, such as multi-person interactions, dynamic backgrounds, or varying camera viewpoints, remains unclear. The current evaluation fails to demonstrate the robustness of the proposed approach beyond these constrained settings. Furthermore, the disentanglement is only demonstrated on datasets where the static and dynamic factors are already well-defined, which may not be the case in real-world scenarios where these factors are intertwined and more difficult to separate.

**Minor**
* The Introduction section gives a skewed picture of the state of image generation with VAEs and GANs (e.g. citing works from 2016 and 2018) to support the claims of GANs being unstable and VAEs blurry. A large body of work has been introduced since the introduction of these methods that makes GAN training very stable in practice, and improves VAE generation quality. The introduction should acknowledge the progress in these areas and focus on the specific limitations of these methods in the context of sequential data disentanglement, rather than relying on outdated characterizations of their general performance. The current framing of the problem does not accurately reflect the state of the art in image generation.
* Please double-check citations. For example, line 651 has an incorrect author name.

### Questions
* It would be great to see the method shine in more (real-world) domains, for example audio (e.g. speaker vs content) disentanglement, multi-object video (controlling aspects of objects as is shown in this work, but then on the object rather than video level), multi-view video (e.g. controlling viewpoint)

Relevant works:
* View point synthesis: "DORSAL: DIFFUSION FOR OBJECT-CENTRIC REPRESENTATIONS OF SCENES"
* Object disentanglement: "Neural Assets: 3D-Aware Multi-Object Scene Synthesis with Image Diffusion Models"
* Audio benchmark: "Sample and Predict Your Latent: Modality-free Sequential Disentanglement via Contrastive Estimation"

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
In this paper, the authors present a diffusion sequential disentanglement autoencoder (DiffSDA) for unsupervised sequential disentanglement. The proposed DiffSDA is based on DiffAE but improves DiffAE from three perspectives. Moreover, the authors introduce three new datasets for the evaluation and verify the effectiveness of the proposed DiffSDA by comparing with several SOTA baselines.

### Strengths
1. The paper proposes to deal with a practical, meaningful and challenging problem setting, that is unsupervised sequential disentanglement.
2. The paper presents a diffusion sequential disentanglement autoencoder (DiffSDA) framework for the unsupervised sequential disentanglement problem.
3. The paper conduct experiments on three practical datasets, and demonstrate the effectiveness of the proposed DiffSDA compared with given baselines.

### Weaknesses
1. One major concern of the work is on the technical novelty. The disentanglement function is decoupled with the diffusion module but is done in the semantic encoder. However, the way of extracting the dynamic and static information in the semantic structure, i.e., using LSTM to explore the temporal relations and its last hidden to calculate the static one, has been well studied in existing studies, e.g., disentangled sequential VAE and S3VAE. To this reviewer, this work is a conditional diffusion with the extracted dynamic and static feature representations as conditions. In this sense, the technical significance of the proposed DiffSDA is limited.
2. The paper misses some important related works. Using diffusion for animation generation, e.g., Animate Anyone, MagicAnimate, not only transfers face/appearance but also changes the motion to follow the driven sequence. There are also a lot of image2video works that generate (zero-shot) target video sequences using a single target image and a source driving videos. Although these methods do not explicitly use the terminology ‘disentanglement’, they have similar application scenarios with the paper.   
3. It is always encouraging to introduce and test new datasets. However, unsupervised sequential disentanglement is a well-defined/studied problem setting, and testing on some benchmark datasets (maybe naïve) is necessary. The authors may refer to the datasets used in disentangled sequential VAE and S3VAE. 
4. To show the effectiveness of the disentanglement, it is necessary to show the reconstruction results with only one latent factor, e.g., keeping dynamic one and set the static one as zeros. Moreover, a project page with some video results is encouraged, which clearly helps the readers to understand your results as well as to compare with the other baselines.
5. Since the method is built on DiffAE, the reviewer wonders how the performance of the proposed DiffSDA compared with DiffAE where frame-by-frame swap can be done.
6. To show the superoirty of the proposed method in the fast sampling, complexity analysis or time-cost analyses, e.g. rtf, need to be done.

### Questions
Please refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a decoder framework for the latent spaces within diffusion generative models. By incorporating sequential aware neural networks (LSTM) into the proposed DiffSDA method, it is able to extract some sequential features that allow for video editing tasks.

### Strengths
The paper extends the static diffusion space decoders to their dynamic sequential version, which can be applied to video editing tasks. It is an interesting application scenario.

### Weaknesses
- Above all, I believe that it is not appropriate to show a video example with gender being modified in the first illustration figure, the authors can choose many other alternative examples to convey the same idea other than this particular case. On top of that, the results shown in this first figure are some qualitative examples of "video editing" (at least to me), and there is a misalignment between what is “disentanglement” and “editing or semantic manipulation tasks” within this context.
- A major weakness of this paper is the lack of a clear problem definition. The abstract and introduction start with an ambitious, high-level goal—representation disentanglement in an unsupervised learning setting—but the focus quickly shifts to generative modeling across a range of architectures, including VAEs, GANs, and DMs. There is a significant gap in explaining how this broad question is formulated within a generative framework.
- Building on my previous point, the authors may risk overclaiming the contribution of the proposed framework. It functions as a post-hoc decoder that applies additional disentanglement to the diffusion latent space, rather than as an unsupervised learning framework that directly addresses disentanglement challenges.
- Even within this diffusion generative context, many recent works have demonstrated the intrinsic ability of diffusion models to learn disentangled features, such as [a,b,c]. The authors fail to discuss and/or compare these related works in the paper.
- I see a strong implicit assumption in the problem formulation in Section 4.1, where the authors assume the data distribution can be factorized into a "state-independent distribution density of static (time-invariant) and dynamic (time-variant) factors," treating them as independent variables. This assumption seems questionable and requires, at a minimum, some justification. Additionally, Eq. (4) is somewhat unclear and unprofessional—what is V? It is mentioned in Line 185 but not defined.

### Questions
Please see my detailed Weaknesses section. While there are several minor issues throughout the manuscript, I have highlighted what I consider to be the major concerns. Overall, I believe the paper is not yet ready for publication.

### Soundness
2

### Presentation
3

### Contribution
2
