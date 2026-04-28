# Once-for-All: Controllable Generative Image Compression with Dynamic Granularity Adaption

- Decision: Accept
- Scores: 6, 8, 3, 5, 6

## Abstract
Although recent generative image compression methods have demonstrated impressive potential in optimizing the rate-distortion-perception trade-off, they still face the critical challenge of flexible rate adaption to diverse compression necessities and scenarios. To overcome this challenge, this paper proposes a \textbf{Control}lable \textbf{G}enerative \textbf{I}mage \textbf{C}ompression framework, termed \textbf{Control-GIC}, the first capable of fine-grained bitrate adaption across a broad spectrum while ensuring high-fidelity and generality compression. \textbf{Control-GIC} is grounded in a VQGAN framework that encodes an image as a sequence of variable-length codes (\emph{i.e.} VQ-indices), which can be losslessly compressed and exhibits a direct positive correlation with the bitrates. Drawing inspiration from the classical coding principle, we correlate the information density of local image patches with their granular representations. Hence, we can flexibly determine a proper allocation of granularity for the patches to achieve dynamic adjustment for VQ-indices, resulting in desirable compression rates. We further develop a probabilistic conditional decoder capable of retrieving historic encoded multi-granularity representations according to transmitted codes, and then reconstruct hierarchical granular features in the formalization of conditional probability, enabling more informative aggregation to improve reconstruction realism. Our experiments show that \textbf{Control-GIC} allows highly flexible and controllable bitrate adaption where the results demonstrate its superior performance over recent state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper titled "ONCE-FOR-ALL: CONTROLLABLE GENERATIVE IMAGE COMPRESSION WITH DYNAMIC GRANULARITY ADAPTION" introduces Control-GIC, a framework for controllable generative image compression. It addresses the challenge of flexible rate adaption in image compression by leveraging a VQGAN framework that encodes images as variable-length codes . The framework correlates local image patch information density with granular representations, allowing for fine-grained bitrate control. It includes a granularity-informed encoder, a statistical entropy coding module, and a probabilistic conditional decoder. The experiments demonstrate that Control-GIC outperforms state-of-the-art methods in terms of flexibility, perceptual quality, and compression efficiency.

### Strengths
1. Control-GIC combines classical coding principles with VQGAN to achieve controllable generative compression across various bitrates with a unified model.
2. The framework allows for highly flexible and controllable bitrate adaption, which is a significant advancement over existing methods.
3. Unlike other methods that require training multiple models for different bitrates, Control-GIC can adapt to various bitrates with a single model, reducing computational costs.

### Weaknesses
1. More comparion with other GIC methods need to be provided.
2. The novelty is limited compared to other VQGan based GIC method

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces Control-GIC, a controllable generative image compression framework aimed at addressing the limitations of existing generative image compression methods in achieving flexible bitrate adjustment. Built upon the VQGAN framework, Control-GIC incorporates multi-granularity encoding mechanisms and a probabilistic conditional decoder to achieve flexible bitrate control and high-quality image reconstruction. Both qualitative and quantitative results demonstrate the effectiveness of the proposed method.

### Strengths
1. The proposed Control-GIC introduces a unified model that allows dynamic bitrate adjustment, which effectively solves the inefficiencies faced by existing models that need multiple fixed-rate versions.
2. The granularity-informed encoder and probabilistic conditional decoder are well-designed to achieve efficient encoding and high perceptual fidelity.
3. Experimental results show superior performance over state-of-the-art methods, demonstrating both flexibility and effectiveness in compression.

### Weaknesses
1. The paper lacks sufficient details on how the features are divided into different granularities in Section 3.1.
2. The DIV2K comparisons in Figure 4 do not include evaluations against important baselines like VVC, M&S, and other methods (presented in Figure 3), which limits the completeness of the analysis.
3. The paper does not compare Control-GIC with other VQ-based methods, such as GLC [1], Mao et al. [2], and UIGC [3], which would provide a better context for understanding the model's relative performance.
4. It is suggested that the authors add more comparisons with results from other datasets featuring different image sizes to enhance the robustness, such as CLIC-dataset.


References:
[1] Jia Z, Li J, Li B, et al. Generative Latent Coding for Ultra-Low Bitrate Image Compression[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 26088-26098.
[2] Qi Mao, et al, Extreme image compression using fine-tuned vqgan models. DCC, 2024.
[3] Naifu Xue, Qi Mao, et al, Unifying Generation and Compression: Ultra-low bitrate Image Coding Via Multi-stage Transformer.ICME.2024.

### Questions
1. Why is the mask ratio set to 50%, 40%, 10% for fine, medium, and coarse features in the training setting? Please provide further justification for this choice.
2. In Mao et al.'s papers [2, 3], the bitrate used in VQGAN is significantly lower, ranging from <0.05 bpp to ≤0.03 bpp, while in GIC, the bpp ranges from 0.1 to 0.6 bpp. Could you explain why the bitrate range cannot be lower in Control-GIC, and if it is possible to extend the model to support lower bitrates?



References:
[1] Qi Mao, et al, Extreme image compression using fine-tuned vqgan models.DCC, 2024.
[2] Naifu Xue, Qi Mao, et al, Unifying Generation and Compression: Ultra-low bitrate Image Coding Via Multi-stage Transformer.ICME.2024.

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
This paper targets at addressing the challenge of rate adaption proplem for generative image compression and proposes a controllable generative image compression framework. The paper represents the image patches of sequential spatially variant VQ-indices to support precise variable rate control and adaption. A non-parametric statistical entropy coding is devised to encode the VQ-indices losslessly.
A probabilistic conditional decoder is proposed to aggregate historic encoded multi-granularity representations, achieving realism improvements.

### Strengths
The paper proposes to flexibly determine a proper allocation of granularity for patches, supporting dynamic adjustment for VQ-indices and make the framework capable of fine-grained bitrate adaptation.

### Weaknesses
- In Figure 3, the proposed method shows worse performance than CDC for DISTS, and is also worse than CDC at the high bitrate range. Could you give some analysis? 

- In Figure 4, why do you compare only with BPG, CTC, and HiFiC, instead of aligning with the methods used in Figure 3?

- In Figure 3 and Figure 4, most metrics are nearly reaching saturation when the bpp increases. Is there obvious difference for the visualization quality when the bpp increases at the high bitrate range? For example, in Figure 6, when the bpp increases, I do not see obvious enhancement between r2=40%(bpp=0.3864) and r2=32.9%(0.4171).

- Visualization analysis about the influence of the granularity of image patches. Will increasing the image patch size lead to block artifacts in the reconstructed images? And can making the image patch size smaller solve some artifacts in VQ based methods, such as the unsatisfactory artifacts for small faces?

### Questions
see the weakness part

### Soundness
1

### Presentation
1

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
The paper Once-for-All: Controllable Generative Image Compression with Dynamic Granularity Adaption introduces Control-GIC, a flexible framework for high-quality image compression that allows fine-grained bitrate control without needing multiple models. Built on a VQGAN foundation, Control-GIC encodes images as variable-length sequences, adapting bitrate based on local image information density, which allows for effective compression adjustments to meet different content complexities. The model includes a granularity-aware encoder that assigns varying levels of detail across image patches, and a probabilistic conditional decoder that reconstructs images with high perceptual quality by aggregating multi-scale features. Experimental results show that Control-GIC outperforms recent state-of-the-art methods in perceptual quality, flexibility, and efficiency, achieving this with a single unified model across a wide bitrate range.

### Strengths
1. The authors’ granularity-informed encoder effectively leverages the information density distribution to distill image patches into a hierarchical structure with three levels of granularity. This approach enables compression with a controllable encoding rate, providing a novel solution for adaptable image compression.

2. The paper’s codec framework is lightweight and demonstrates relatively fast encoding and decoding speeds, making it more suitable for practical applications where computational efficiency is a priority.

### Weaknesses
1. The experimental results show mixed outcomes compared to existing baselines like HiFiC, without demonstrating a clear advantage.
2. The paper should consider comparing with MS-ILLM [1], which uses a similar VQ-VAE structure, to better position its contributions.
3. Tests on the CLIC 2020 dataset are missing, which would help validate the model's robustness across diverse datasets.
4. Section 3.2 is overly detailed and could be streamlined for clarity and conciseness.
5. Section 3.3 appears to be a direct application of existing methods, which could benefit from additional elaboration or innovation.

[1] Muckley M J, El-Nouby A, Ullrich K, et al. Improving statistical fidelity for neural image compression with implicit local likelihood models. International Conference on Machine Learning. PMLR, 2023: 25426-25443.

### Questions
1. How are the masks $m_1$, $m_2$, and $m_3$ obtained? The main text does not seem to provide a clear calculation method for these.
2. If compression is required at a specific bitrate, how should $r_1$, $r_2$, and $r_3$ be determined?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a novel framework for controllable generative image compression (Control-GIC). The proposed Control-GIC integrates a granularity-aware encoder to enable precise variable rate control and adaptation, a non-parametric statistical entropy coding method for lossless encoding of VQ-indices, and a probabilistic conditional decoder to reconstruct hierarchical granular features. Experimental results on the Kodak and DIV2K datasets demonstrate that Control-GIC not only delivers strong perceptual compression performance but also provides highly flexible and controllable bitrate adaptation.

### Strengths
1. A comprehensive explanation on adapting VQ-GAN into a rate-adaptive perceptual codec.

2. Highly flexible and controllable bitrate adaptation.

3. Well-conducted ablation study.

4. Open-sourced code! This is fantastic, and I want to thank the authors for their commitment to sharing this.

### Weaknesses
1. Lack of comparison with the latest state-of-the-art (SOTA) perceptual codec, MS-ILLM [1]. It appears that MS-ILLM outperforms both HiFiC and Control-GIC in terms of compression performance.

2. Control-GIC utilizes a mask for multi-scale encoding, but the method for generating the masks $m_1, m_2$ and $m_3$ during training and inference is not clearly explained. Please provide a more detailed description of this process.

3. Misuse of capitalization: 'The Encoding and decoding' on line 432 should be corrected to 'The encoding and decoding.'"

[1] MJ Muckley, A El-Nouby, K Ullrich, H Jegou, J Verbeek. Improving Statistical Fidelity for Neural Image Compression with Implicit Local Likelihood Models. In ICML, 2023.

### Questions
Please see the above weakness.

### Soundness
3

### Presentation
3

### Contribution
3
