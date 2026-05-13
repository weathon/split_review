# MFN: Metadata-Free Real-World Noisy Image Generation

- Decision: Reject
- Scores: 5, 8, 8, 3

## Abstract
Real-world noise poses a significant challenge in signal processing, especially for denoising tasks.
Although end-to-end denoising approaches have achieved exceptional performance, they are constrained to scenarios with abundant noisy-clean image pairs, which can be technically challenging and resource-intensive to collect.
To address this issue, several generative methods have been developed to synthesize realistic noisy images from limited real-world datasets.
While prior studies require camera metadata during training or testing to handle various real-world noise, the absence of metadata or variations in the information across different capturing devices is common in real-world scenarios, such as medical or microscope imaging, which limits their applicability.
Thus, we aim to eliminate the need for explicit camera-related labels in both stages, enhancing applicability in real-world scenarios.
To achieve this, we propose a novel framework called the Metadata-Free Noise Model (MFN), which extracts prompt features that encode input noise characteristics and generates diverse noisy images that adhere to the distribution of the input noise.
Extensive experimental results demonstrate the superior performance of our model in real-world noise generation and denoising across various benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a metadata-free noise model to model real-world noise in denoising tasks without relying on camera metadata. The key idea is that the proposed method is composed of a Prompt Autoencoder and Prompt DiT, encodes input noise characteristics to generate realistic noisy images. Experimental results on various benchmark datasets verify MFN’s strong performance in noise generation and denoising.

### Strengths
- The motivation for MFN is clear, which successfully removes metadata dependency, offering a new approach for real-world noise generation.
- The framework is well-structured, and experiments across many denoising benchmarks validate its effectiveness in realistic noise generation and denoising.
- The paper is clearly writen and the overal explanation is logical.

### Weaknesses
 - In Table 4, I am not sure how $\textit{Real}$ is trained. I mean if the data for training the proposed noise model covers the data for training $\textit{Real}$, the modeling-synthesizing-denoising pipeline becomes meaningless since the complex pipeline doesn't provide any performance gain over $\textit{Real}$ in terms of denoising results. This should be clarified with more detailed information.
- The noise distribution of sRGB images are very complex, it is signal-dependent, spatial-correlated, and also has consistent fixed patterns. How do the latent code and decoder handle this complexity to accurately model a signal-dependent, spatially correlated noise distribution? Specifically, how does the model ensure that the generated noise maintains the intricate spatial correlations and signal dependencies observed in real-world sRGB noise, and what mechanisms are in place to prevent the model from generating unrealistic or overly simplistic noise patterns?
- The entire pipeline is not clearly explained. Do we need to train a new PAE and P-DiT for each new camera? Additionally, I would like clarification on whether $n_{Real}$, $I_{Clean}$, and $I_{Noisy}$ are from the same scene. Specifically, is $n_{Real} = I_{Noisy} - I_{Clean}$ for both training and inference? While it makes sense to assume this during training, Figure 1(b) seems to imply the same notation in the reference, which raises questions about generating noisy images from the same noise. In addition, if $n_{Real}$ is derived from a different image captured with the same target camera and ISO, this approach may still be more challenging and less practical than directly obtaining ISO and camera metadata, as $n_{Real}$ would require paired noisy and clean images. The paper should clarify whether the noise is extracted from the same image pair or different image pairs, and how this impacts the practicality of the proposed method.
- I recommend that the authors compare their method with state-of-the-art self-supervised denoising methods such as LGBPN, as well as with supervised training results using the same data as the data for training the proposed noise model. (I am not sure whether this corresponds to $\textit{Real}$ in Tables 4 and 5.)

### Questions
In conditions where the ISO value and camera type is known in advance, will it performs better if we inject the ISO and camera information into the framework?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a neural network for generating images with realistic camera noise from noise-free images without metadata. The proposed method incorporates a diffusion model, two-stage training, and transformer-based global and local attention. Experimental results present that the proposed method outperforms the compared methods in noise generation, image denoising, and metadata classification.

### Strengths
The proposed method is reasonable, and the ablation studies present the effectiveness of each technique component.

The performance improvements on various real-world denoising datasets (Table 5) indicate a practical use case of noise generation using noisy-clean image pairs.

The experiments on metadata classification are interesting for evaluating the performance of noise generation.

### Weaknesses
The literature review in the introduction and related work is limited.
For real-world image denoising, the works [A, B, C] have addressed different approaches worth discussing and comparing in experiments (if possible) for future research.
In particular, NERDS generates noisy-clean image pairs without metadata and clean images using raw-sRGB noisy image pairs.

The analysis for the generalization performance on various real-world datasets (Table 5) is limited.
Given that the proposed method uses noisy-clean image pairs to train noise generators while MFN and ‘real’ present similar performances in the SIDD benchmark, the generalization performance is the major advantage of using the proposed method for real-world image denoising.
However, the manuscript does not incorporate any further analysis of the generalization performance.
For instance, the restoration performance comparisons on different numbers of noisy images per clean image and the noise diversity control can help us better understand generalizations about real-world denoising.

### Questions
Why should the training stages be separated? And how does the separation affect performances?

### Soundness
4

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
The paper presents a Metadata-Free Noise (MFN) model, designed to generate realistic noisy images without relying on explicit camera metadata. This framework is particularly useful in practical applications where metadata might be unavailable, such as in medical imaging or low-level vision tasks. MFN uses a Prompt Autoencoder (PAE) and Prompt DiT (P-DiT) components to capture noise characteristics, allowing for the generation of noise that resembles real-world conditions. The model’s performance is demonstrated through extensive experiments on various datasets, showcasing its effectiveness in generating realistic noise and achieving strong results in denoising applications.

### Strengths
Contribution: MFN’s ability to generate realistic noise without requiring metadata significantly broadens its application scope, especially in fields where metadata is unavailable or irrelevant, addressing a notable gap in real-world denoising research. 

Method: The dual-component framework (PAE and P-DiT) is well-conceived. By leveraging prompt features instead of metadata, the model effectively captures and recreates noise characteristics, enhancing its realism and robustness. 

Experiments: The paper presents comprehensive evaluations across multiple datasets (SIDD, PolyU, NAM, and DND) and denoising tasks. The results consistently demonstrate MFN’s superior performance in noise synthesis and denoising. 

Comparison with SOTA: MFN outperforms various existing models (e.g., NAFlow, NeCA-W) on key metrics like Kullback-Leibler Divergence (KLD) and PSNR, showcasing both quantitative and qualitative improvements in noise generation and denoising quality. 

Ablation studies: The authors include thorough ablation studies that highlight the contribution of different model components, such as the Global Prompt Block (GPB) and Local Prompt Block (LPB), to the quality of the generated noise.

### Weaknesses
Computational complexity: While MFN demonstrates strong performance, its two-stage architecture may be computationally intensive, particularly for high-resolution images. The paper could benefit from discussing the model’s runtime and potential optimizations for real-time applications. 

Limited comparison: Although MFN is compared with several state-of-the-art methods, the selection could be expanded to include other prompt-based and noise-aware generation models, which would provide a more robust evaluation of its unique contributions. 

Potential overfitting: The model’s performance on specific datasets such as SIDD+ is noted, but additional evaluations in extreme or highly diverse noise scenarios could further validate its generalization. 

Dependence on training setup: MFN’s performance depends heavily on the training setup, which is highly specialized (e.g., custom noise schedules and curriculum training). This setup may limit reproducibility and adaptability in different research settings.

### Questions
What could be potential solutions to enhance the method's efficiency, especially for real time applications? How efficient is the proposed method in terms of higher image resolutions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a method for generating real-world noisy images without relying on meta information, which seems to be useful in medical imaging. It consists a Prompt Autoencoder to encodes noise characteristics into a latent space. The Prompt Diffusion Transformer is utilized to integrate the prompt features from PAE  and generate the noisy images. The experiments are conducted on several datasets.

### Strengths
1. The method operates without the need for metadata, which could be especially beneficial for certain specialized sensors and applications
2. The paper is well-written..

### Weaknesses
1. During inference, the method requires real noise as input. In practice, we could directly use noise and clean images to create noisy-clean image pairs, which would be ideal for training and work better that the proposed method.
2. Although the paper claims (L49) that the metadata-free setting is reasonable, it does not provide real-world application examples, such as in medical imaging. It remains unclear whether the method can generalize to such contexts. 
3. The model was trained on the SIDD dataset but performs well on other datasets, even when noise characteristics differ significantly, which is somewhat unexpected.
4. More discussion should be conduct with the existing physics-based noise modeling paper [1-2].

### Questions
See the strengths and weaknesses

### Soundness
1

### Presentation
4

### Contribution
2
