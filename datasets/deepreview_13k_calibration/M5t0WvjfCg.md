# AdaIR: Adaptive All-in-One Image Restoration via Frequency Mining and Modulation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
In the image acquisition process, various forms of degradation, including noise, blur, haze, and rain, are frequently introduced. These degradations typically arise from the inherent limitations of cameras or unfavorable ambient conditions. To recover clean images from their degraded versions, numerous specialized restoration methods have been developed, each targeting a specific type of degradation.
Recently, all-in-one algorithms have garnered significant attention by addressing different types of degradations within a \emph{single model} without requiring the prior information of the input degradation type.
However, these methods purely operate in the spatial domain and do not delve into 
the distinct frequency variations inherent to different degradation types.
To address this gap, we propose an adaptive all-in-one image restoration network based on frequency mining and modulation. 
Our approach is motivated by the observation that different degradation types impact the image content on different frequency subbands, thereby requiring different treatments for each restoration task.
Specifically, we first mine low- and high-frequency information from the input features, guided by the adaptively decoupled spectra of the degraded image. 
The extracted features are then modulated by a bidirectional operator to facilitate interactions between different frequency components. 
Finally, the modulated features are merged into the original input for a progressively guided restoration. 
With this approach, the model achieves adaptive reconstruction by accentuating the informative frequency subbands according to different input degradations. 
Extensive experiments demonstrate that the proposed method, named \xnet, achieves state-of-the-art performance on different image restoration tasks, including image denoising, dehazing, deraining, motion deblurring, and low-light image enhancement.

  
  \keywords{Image restoration \and All-in-one model \and Frequency analysis}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents AdaIR, which aims to address multiple forms of degradation, such as noise, blur, haze, and rain, within a single model. AdaIR is motivated by the observation that different types of degradation impact image content on different frequency subbands.  AdaIR leverages both spatial and frequency domain information to effectively separate and remove these degradations using customised modules.

### Strengths
The paper highlights a key insight for any image restoration: Noisy and rainy images are contaminated with high-frequency content while the low-frequency content degrades more in Low-light and hazy images.

Exploiting frequency domain is a key differentiation, as previous methods like AirNet, IDR, and PromptIR operate solely on spatial domain information

Frequency Mining Module (FMiM) extracts relevant frequency signals from degraded images through adaptive spectral decomposition, targeting degradation-specific frequency content. The use of a dynamic, learnable Mask Generation Block (MGB) to separate low- and high-frequency representations based on the input image's degradation type allows AdaIR to adapt to different degradations effectively

Frequency Modulation Module (FMoM) refines these frequency features by enabling interaction between different frequency components, enhancing the model’s effectiveness on various degradation types.

Experiments on a wide set of benchmarks demonstrates consistent performance gains over competing approaches in both three-degradation and five-degradation settings

The improved quality of discriminative feature learning (shown in Fig. 2) is impressive.

### Weaknesses
While the paper demonstrates the generalisation ability of AdaIR by testing it on an unseen desnowing task and synthetic images with mixed degradations (rain and noise) in Table 7 and 8, there are no experiments on real out-of-distribution images. Extensive qualitative comparisons on real images should be included. Evaluation on a wider range of out-of-distribution degradations would strengthen the claims of the model's generalisation capabilities.

The quantitative tables primarily compare AdaIR with other all-in-one methods but not the scores of single-task trained state-of-the-art models. Including the highest scores achieved by SotA single task models on each individual task would provide a more comprehensive assessment of AdaIR's performance relative to specialised approaches.

While Table 4 shows the overhead of AFLB in terms of parameters and FLOPs, a more in-depth analysis of its computational cost and potential impact on real-time applications would be beneficial.
FLOPs are only reported for ablation studies, but there are no FLOPs comparisons with competing methods.
In addition to FLOPs, there should also be comparison between inference time of different models.
using frequency domain processing inherently introduces additional processing for transformations eg IFFT. 
Although they are beneficial for accuracy, a potential drawbacks of such approaches is the computation cost and incompatibility with edge platforms. 

The paper doesn't cite or compare with any existing models that use frequency domain processing. There have been many such studies [1-7]. Some of these papers are quite related as they propose transformer modules that focus on high/low frequencies.

Furthermore, comparing with alternative transform-domain methods, such as wavelet transforms or other adaptive filtering techniques, commonly used in related papers, could enhance the performance and adaptability of AdaIR.

The MGB dynamically generates a mask to separate low and high frequencies based on the input image. It would be interesting to see the difference in generated masks for different tasks. This vanilla approach could be prone to overfitting, especially since the training dataset does not adequately cover the diversity of real-world degradations. A more robust approach might involve specifically incorporating prior knowledge about frequency characteristics of different degradations or exploring regularization techniques to prevent overfitting

Paper lacks deeper analysis on how the interaction between different frequency bands contributes to the restoration process. Such analysis could lead to more informed design choices and potentially improve the interpretability of the model.

The graph in Fig. 1 right doesn’t clearly demonstrate the stark frequency-domain differences between different tasks.

### Questions
Address weaknesses above.

### Soundness
3

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
5

### Summary
This paper presents an all-in-one image restoration framework that can generate clean images from multiple degradation patterns, such as noise, blur, haze, and rain. Different from existing all-in-one algorithms that perform only in the spatial domain, the proposed network deals with all-in-one tasks from the perspectives of frequency mining and modulation. The network extracts different frequencies from the degradation images and modulates features for high-quality reconstruction. The adaptive strategy enhances the learning of informative frequency signals based on input degradation. Comprehensive experiments on two kinds of all-in-one settings demonstrate the model's effectiveness.

### Strengths
1) The paper presents a novel adaptive all-in-one image restoration architecture that can effectively decouple the input into different frequencies and modulate them for high-quality reconstruction. The paper is well-motivated, and Figure 1 makes sense.
2) The proposed blocks are reasonable and can be easily injected into other algorithms.
3) The visualizations well demonstrate the efficacy of the proposed model and motivation.
4) The model is computationally efficient. It achieves sota, and the experiments on two kinds of all-in-one settings are thorough, while other algorithms only experiment on a single setting.

### Weaknesses
1) The comparisons using only PSNR/SSIM seem insufficient to measure the quality of the resulting images. LPIPs can be used to further verify the proposed model's superiority.
2) The architecture is mainly based on Restormer. However, Tab. 1 does not include Restormer's performance.
3) The paper lacks comparisons with recent methods, such as Harmony in Diversity: Improving All-in-One Image Restoration via Multi-Task Collaboration.

### Questions
Please refer to the weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an adaptive all-in-one image restoration model called AdaIR using frequency information. A key motivation is that different degradation types impact the image’s different frequency sub-bands. AdaIR mines low- and high-frequency information from input features (FMiM) and modulates the extracted features by facilitating the cross-interaction between low-frequency mined features and high-frequency mined features (FMoM).

### Strengths
- The motivation for incorporating frequency information in an all-in-one image restoration model is well-founded. The authors substantiate their claim that various degradation types influence image content across frequency subbands. For instance, the t-SNE visualizations in Figures 2 and 11 illustrate how degradations can be clustered based on their types.
- The authors successfully demonstrate the function of each module within the model through extensive ablation studies. For example, in Figure 9, the visualizations of intermediate features and spectra effectively highlight the roles of the AFLB module, which is composed of the FiMM and FMoM components.

### Weaknesses
 - The authors claim that all previous approaches operate solely in the spatial domain and do not consider frequency information (L086-L087). However, several studies [1-2] have already explored the frequency domain. The authors should clarify how their approach differs from or advances these existing frequency-based methods. Given the existence of prior frequency domain exploration, the primary motivation for this work may need to be revised.
- The proposed AdaIR appears to be a straightforward combination of existing techniques, such as Restormer [3] and CBAM [4]. Specifically, all encoders and decoders utilize multiple Transformer blocks from Restormer, and the cross attention (CA) mechanisms in both FMiM and FMoM leverage the MDTA approach from Restormer. Additionally, the H-L unit in FMoM seems to replicate the channel attention mechanism found in CBAM. 
- The authors should appropriately cite the sources in both the figures and the main text. For example, in Figure 3, Restormer should be referenced for the TB in (a) and the CA in (d). Furthermore, CBAM should be cited since its channel attention mechanism is employed in the H-L unit of FMoM, both in Figure 3 and the main text. The authors should add citations to Restormer and CBAM in the caption of Figure 3, as well as in the relevant sections of the main text where these components are described.
- The roles of the H-L and L-H units appear to be similar in facilitating cross-interaction between low and high-frequency mined features. However, the authors have implemented different designs for these two units. It would be helpful for the authors to clarify the rationale behind using distinct methods for each.
- The metrics in the tables require clarification. For instance, Table 1 should include column headings that explicitly indicate the inclusion of PSNR and SSIM. The authors should add column headers in Table 1 (and any other relevant tables) to clearly indicate which metrics are being reported (e.g. "PSNR / SSIM").
- The benchmark models referenced are somewhat outdated. The authors should consider updating the comparison models to more recent ones [5-7]. Additionally, they should include comparisons with all-in-one restoration models that account for frequency information [1-2].

### Questions
- Could the authors provide both the original and enlarged images in the figures? If this is not possible, assessing the performance of the proposed methods becomes challenging. For instance, while AdaIR appears to excel in rain removal, other models might perform better in different regions.
- The total number of parameters appears large (28.77M). Can authors add a column to their comparison tables (e.g. Tables 1 and 2) showing the number of parameters for each model? This would allow for a more comprehensive comparison of model efficiency alongside performance metrics.
- Can the authors clarify the term "Fixed" in Table 4? It is unclear whether the mask value is also fixed or not. The current caption in Table 4 only mentions that the mask shape is fixed at $10 \times 10$.
- Could the authors demonstrate that AdaIR, as an all-in-one model, performs well on unseen and mixed degradation using the UDC-SIT dataset [8], which features complex degradations?
- It would be helpful if the authors could explain more clearly the significance of the channel-wise features and the corresponding attention scores depicted in Figure 7.
- Can the authors elaborate on why AdaIR outperforms the Encoder + Decoder + AFLB configuration presented in Table 12? The explanation should include the advantages of AdaIR's design compared to the alternative.
- The additional ablation study regarding the design choices of FMoM in Appendix B may not be entirely fair. For example, the proposed design in Figure 8(b) does not initially concatenate $X_h$​ and $X_l$. Instead, each feature passes through the H-L or L-H unit before being cross-multiplied. The reviewer believes that the spatial attention comparison in Figure 8(a) should also avoid concatenation initially; instead, $X_h$​ and $X_l$​ should go through channel attention separately before their respective spatial attention maps are cross-multiplied. Could the authors provide a comparison based on this suggestion?

[8] Ahn, K., Ko, B., Lee, H., Park, C., & Lee, J. (2024). UDC-SIT: a real-world dataset for under-display cameras. Advances in Neural Information Processing Systems, 36.

### Soundness
2

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
5

### Summary
This work solves the all-in-one problem in image restoration from a frequency perspective and demonstrates its effectiveness. But my main problem is that I think the insights and designed modules are fallen behind and there are already many homogenized work. Therefore, the novelty of this paper does not appeal to me.

### Strengths
The AdaIR model offers significant advantages by adaptively addressing various types of image degradations through innovative frequency analysis. Its frequency mining module precisely extracts relevant frequency components that reflect underlying degradations, while the frequency modulation module optimizes these components by allowing the exchange of complementary information across different features. Integrated into a U-shaped Transformer backbone, these components enable AdaIR to achieve state-of-the-art performance across diverse image restoration tasks, highlighting its robust adaptability and effectiveness.

### Weaknesses
1. In the t-sne clustering in Figure 2, the model is better at learning discriminative degradation contexts. First, the comparison method is relatively old, so some more recent comparison methods is suggested in the t-SNE analysis.

2. Moreover, I do not think that this completely separated state can help solve the all-in-one problem more effectively. In fact, the correlation between various degradations may need to be learned to solve it better. For example, an image of rainy scene should also have heavy haze, so these two degradations should have something in common. And the rain lines can be regarded as a kind of noise, so they may also be correlated in AirNet and PromptIR of Fig 2, rather than completely decoupled.  In other word, I doubt that the reason for the decoupling of the t-sne analysis may be the overfitting of the model on each dataset.

3. As the core motivation of this work, the idea in Figure 1 has been discussed extensively, and I think it is not innovative. Please see the question section for detailed discussion.

4. The method design is also based on the combination of the very traditional U-Net network and the attention mechanism. This design has obviously fallen behind. Diffusion model may be a more proper framework to solve this problem.

### Questions
Some works as following also have discussed using the frequency domain perspective to solve various degradation problems. [1] and [2] observe a specific degradation from the perspective of frequency domain.  [3] and [4] also adopt frequency mining and modulation to solve various degradations condition. It is suggested  to provide a point-by-point comparison of the proposed method with these works, highlighting key similarities and differences in approach and performance.

[1] Efficient Frequency Domain-Based Transformers for High-Quality Image Deblurring, CVPR, 2023
[2] Wavelet-based Fourier Information Interaction with Frequency Diffusion Adjustment for Underwater Image Restoration, CVPR, 2024
[3] Hybrid Frequency Modulation Network for Image Restoration, IJCAI, 2024
[4] Selective Frequency Network for Image Restoration, ICLR, 2023

### Soundness
2

### Presentation
2

### Contribution
2
