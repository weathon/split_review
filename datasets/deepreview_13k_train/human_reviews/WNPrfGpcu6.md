# FourierMamba: Fourier Learning Integration with State Space Models for Image Deraining

- Decision: Reject
- Scores: 5, 5, 8, 6

## Abstract
Image deraining aims to remove rain streaks from rainy images and restore clear backgrounds. 
Currently, some research that employs the Fourier transform has proved to be effective for image deraining, due to it acting as an effective frequency prior for capturing rain streaks. 
However, despite there exists dependency of low frequency and high frequency in images, these Fourier-based methods rarely exploit the correlation of different frequencies for conjuncting their learning procedures, limiting the full utilization of frequency information for image deraining.  
Alternatively, the recently emerged Mamba technique depicts its effectiveness and efficiency for modeling correlation in various domains (e.g., spatial, temporal), and we argue that introducing Mamba into its unexplored Fourier spaces to correlate different frequencies would help improve image deraining.
This motivates us to propose a new framework termed FourierMamba, which performs image deraining with Mamba in the Fourier space.
Owning to the unique arrangement of frequency orders in Fourier space, the core of FourierMamba lies in the scanning encoding of different frequencies, where the low-high frequency order formats exhibit differently in the spatial dimension  (unarranged in axis) and channel dimension (arranged in axis).
Therefore, we design FourierMamba that correlates Fourier space information in the spatial and channel dimensions with distinct designs.
Specifically, in the spatial dimension Fourier space, we introduce the zigzag coding to scan the frequencies to rearrange the orders from low to high frequencies,  thereby orderly correlating the connections between frequencies; in the channel dimension  Fourier space with arranged orders of frequencies in axis, we can directly use Mamba to perform frequency correlation and improve the channel information representation.
Extensive experiments reveal that our method outperforms state-of-the-art methods both qualitatively and quantitatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a Mamba-based image deraining algorithm. The proposed FourierMamba mainly involves two components: spatial interaction SSM and channel evolution SSM. The spatial branch further consists of spatial mamba and frequency mamba. The main contributions of the paper primarily lie in the adaptation of mamba in the frequency domain for image deraining and the scanning strategy for the spatial-dimensional spectra.

### Strengths
1.	The paper applies mamba in the frequency domain to enhance frequency interactions. To this end, it devises a zigzag scanning strategy.
2.	The proposed methods are evaluated on synthetic and real-world deraining datasets and achieve promising performance.

### Weaknesses
1.	The paper lacks the theory analyses to support the importance of frequency interactions for image restoration. The authors do not provide a clear justification for why processing in the frequency domain, specifically with the proposed Mamba architecture, is superior to spatial domain processing for deraining. A theoretical framework explaining how frequency-specific information is beneficial for separating rain streaks from underlying image details is missing.
2.	The channel fft has already been proposed in REVITALIZING CHANNEL-DIMENSION FOURIER TRANSFORM FOR IMAGE ENHANCEMENT. Why does the channel mamba outperform the 1x1 channel version? The reviewer thinks a 1x1 convolution can also model interactions between channel spectra. Moreover, the idea of interactions between frequencies is already implemented in Fourmer via convolutions. The paper does not sufficiently explain why the proposed Mamba-based approach is better than existing convolution-based methods for frequency interaction, especially considering the computational overhead of Mamba.
3.	The authors replace mamba with 1x1 conv for the first ablation studies. However, the flops or parameter comparisons are not provided. Is it possible that the improvement of mamba versions is derived from the additional computation overhead compared to the 1x1 conv version? The ablation study lacks a controlled comparison where computational costs are equivalent, making it difficult to isolate the impact of the Mamba architecture itself.
4.	Regarding the experimental results, the paper only provides results on four datasets in Tab.1, lacking the test100 dataset. Moreover, the competitors in Fig.6 are a little outdated. From my side, the experiments are insufficient. Specifically, compared to other mamba-based methods, the evaluation data/tasks are fewer. Compared to other deraining methods like drsformer, the authors adopt only a rain13 dataset plus spad for evaluation, which is also insufficient.

### Questions
Please refer to Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes Fourier Mamba, an image rain removal framework. It improves the rain removal effect by applying the Mamba technique in Fourier space and utilizing the correlation between different frequencies. This method uses zigzag encoding to rearrange the frequency order in the spatial dimension and directly uses Mamba for frequency correlation in the channel dimension. Experiments have shown that Fourier Mamba has achieved more competitive results in image rain removal tasks.

### Strengths
1. The proposed framework combines Fourier priors and state space models to correlate different frequencies in Fourier space to enhance the rain removal effect of images. This combination utilizes the advantages of the Fourier transform in global modeling and introduces the efficient feature modeling capability of the Mamba model.

2. To rearrange the order from low frequency to high frequency in the Fourier space of the spatial dimension, Fourier Mamba proposed a scanning method based on zigzag encoding, which systematically associates different frequencies. This method introduces zigzag encoding in Fourier space to rearrange the frequency order, thereby orderly associating the connections between frequencies.

### Weaknesses
1. The experiment is insufficient and lacks comparison with methods such as DRSformer [1] and FADformer [2].
2. I am a bit concerned about the quantitative results in this paper. The difference between the results shown in Table 1 and FreqMamba is not significant. Please further explain the differences between the proposed method and FreqMamba, as they both use Fourier correlation strategies. It is recommended to add visualization results to supplement this.
3. It is worth noting that FFT is a complex valued computation. Suggest the author to add a comparison of the actual inference time of the model. FLOP comparison is not enough, because many works now have lower FLOP but slower running speed, and other issues such as memory consumption may slow down computation speed.

### Questions
Please see the Weaknesses.

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
4

### Summary
This paper proposed a new network for image deraining by introducing the state space models, or more specifically, the recently proposed Mamba structure, in the Fourier spaces. By virtue of the Mamba, the frequency correlations can be better captured and utilized in the Fourier domain, such that the better deraining performance can be expected. Experiments on various deraining datasets have been conducted to demonstrate the effectiveness of the proposed method.

### Strengths
- The application of Mamba to the Fourier domain is new and worthy to explore.

- The experimental results are promising

### Weaknesses
 - The motivation should be strengthened. Currently, it seems the work is mostly about applying Mamba in the Fourier domain, though this task itself could be non-trivial. However, it is unclear why Mamba is more effective than other architectures for processing the Fourier frequencies. Specifically, the paper lacks a detailed explanation of how Mamba's sequence modeling capabilities translate to improved performance in the frequency domain compared to, for example, a transformer architecture with global attention. Visualizing the intermediate features, particularly the learned representations in the Fourier domain, could provide valuable insights into the advantages of Mamba. 

- As reviewed by the authors, another work (Zhen et al., 2024) considers Mamba in the frequency domain but with wavelet transformation. It is better to discuss more about wavelet transformation and Fourier transformation in dealing with frequencies. The current discussion is insufficient to justify the choice of Fourier transform over wavelet transform, especially given that the performance of (Zhen et al., 2024) is close to the proposed method on several datasets. A more detailed analysis of the theoretical and practical differences between these two transforms in the context of image deraining is needed. Besides, as shown in Table 1, the performance of (Zhen et al., 2024) is close to the proposed method on several datasets, but the comparison with this method on SPA-Data is missing.

- The quantitative comparison is conducted with respect to PSNR and SSIM. However, as more and more researchers realized, these two metrics can be often inconsistent with human perceptions and thus some newly developed metrics that can better reflect human perceptions should be considered. The paper should include metrics such as LPIPS, or other perceptual metrics, to provide a more comprehensive evaluation of the method's performance from a human perception perspective.

### Questions
- In Section 4.1, the authors mentioned the "progressive training strategy". What does it mean? And why is it called "progressive"?

- There are several writing issues that I can find:
1) Line 75-76: "...build correlation the correlation among...";
2) The rightmost of Line 73: ".arrangement";
3) According to the formatting of other parts of this manuscript, the "Fourier transformation." in Section 3.1 should not take the whole line.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach to image deraining by integrating Fourier transformation with a state-space model. Unlike previous methods, the proposed approach applies the state-space model in both the spatial and frequency domains, introducing a new scanning strategy referred to as zigzag scanning. This strategy gradually processes both low- and high-frequency components, aiming to enhance the model's ability to capture rain-related distortions. The key contribution of the paper lies in the introduction of this zigzag scanning mechanism, which differentiates it from existing methods.

### Strengths
The proposed model involving zigzag scanning is novel and intuitive.

The paper provides a thorough and intuitive discussion of the advantages of zigzag scanning in the context of the deraining task.

The proposed model demonstrates state-of-the-art performance, balancing accuracy with reasonable computational cost and model size.

### Weaknesses
Although the motivation for zigzag scanning is well-discussed, the paper lacks details on its implementation. Considering the complexity involved, the implementation is non-trivial and deserves attention. The way zigzag scanning is executed, along with pixel organization strategies, can significantly impact inference speed. Including a comparison of running times would enhance the evaluation.

The visual comparison baselines could also be updated. It would be beneficial to include comparisons with more recent methods (post-2022) and provide additional zoomed-in patches or error maps to better highlight performance differences.

There are several confusing typographical issues, such as "FCS" being used as the abbreviation for "Fourier Channel Evolution" and "C-FFT" lacking a clear explanation (possibly referring to "channel FFT"). These should be clarified.

Furthermore, the paper overlooks several closely related works, including:
[1] Wavelet Approximation-Aware Residual Network for Single Image Deraining, 2023.
[2] A Hybrid Transformer-Mamba Network for Single Image Deraining, 2024.
[3] Image Deraining with Frequency-Enhanced State Space Model, 2024.

Additionally, applying the L1 norm directly in the frequency domain may be less accurate than alternative metrics, such as coherence-based distances. An ablation study on the impact of different frequency-domain loss functions would strengthen the analysis.

Finally, the zigzag scanning strategy appears intuitive for other low-level vision tasks, such as deblurring. It would be valuable to investigate the model's performance on additional tasks to assess its generalizability.

### Questions
The main points of confusion, as outlined in the Weakness section, are as follows:

**Implementation and Efficiency of Zigzag Scanning**:
The paper does not provide sufficient details on how the zigzag scanning is implemented, despite its potential complexity. Additionally, it is unclear how efficient the scanning strategy is in practice. A more thorough discussion of the implementation and its impact on inference speed would strengthen the work.

**Generalization to Other Tasks**:
Given that the motivation for zigzag scanning is not specific to rain removal, it would be valuable to evaluate the performance of the proposed method on other low-level vision tasks. Demonstrating its effectiveness beyond the deraining scenario would provide further evidence of its broader applicability.

### Soundness
3

### Presentation
3

### Contribution
2
