# Distribution-Aware Diffusion Model Quantization via Distortion Minimization

- Decision: Reject
- Scores: 6, 3, 8, 5

## Abstract
Diffusion models have attained significant performance in image/video generation and related tasks. However, while diffusion models excel in delivering excellent results, they suffer from substantial computational complexity due to their large volume of parameters. This poses a significant issue for deployment on mobile devices and hampers the practical applications of diffusion models. In this work, we propose a new post-training quantization approach designed to reduce the computation complexity and memory cost of diffusion models. As the distributions of the outputs of diffusion models differ significantly across timesteps, our approach first splits the timesteps into different groups and optimizes the quantization configuration of each group separately. We then formulate the quantization of each group as a rate-distortion optimization problem to minimize the output distortion caused by quantization given the model size constraint. Because output distortion is highly related to model accuracy, by minimizing the output distortion, our approach is able to compress diffusion models to low bit widths without hurting accuracy. Furthermore, our approach applies Taylor series expansion approximation and proposes an efficient method to find the optimal bit allocation across layers with linear time complexity. Extensive experimentation over four datasets including CIFAR-10, CelebaHQ, LSUN-Bedroom, and LSUN-Church validates the effectiveness of our approach. Empirical results show that our approach obtains a notable improvement over state-of-the-art and can reduce the bit width of diffusion models to 5-6 bits while maintaining high accuracy levels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on post-training quantization of the diffusion models for both the model parameters and layer activations. It adopts a mixed precision approach wherein different layers are quantized with different number of bits for precision. It groups different diffusion time steps and applies the quantization procedure per group. At the heart of this paper is quantization based on output distortion that is defined by the Structural Similarity Index Measure (SSIM) loss between the original layer output and the quantized layer output. The paper formulates this as an optimization across layers and show an additive property of the output distortion. Further, it splits this optimization on per layer output distortion objective, which is easily tractable. Finally, various empirical evaluations are conducted to quantize diffusion models trained on CIFAR-10, CelebaHQ, LSUN-Bedroom, and LSUN-Church datasets. This work shows performance of models quantized from 8-bit to 4-bit and evaluates them both quantitatively as well as qualitatively.

### Strengths
- Post-training quantization results on various datasets shows that these diffusion models can be quantized efficiently to bits as low as 6 bits (both in weights/activations) without loosing lot of quantitative performance. 
- Proposed scheme performances quite competitively compared to other post-training frameworks.

### Weaknesses
 - Lack of insights into how quantization affects different model layers. Since these insights would be very helpful to understand the impact of various components in the diffusion models. 
- Since the experiments are done on smaller datasets, it would be hard to understand how the conclusions transfer to other networks / datasets / diffusion frameworks. 
- Although the quantitative metrics look good in Table 1, qualitative images in Figure 2 shows some artifacts in 6bit compression. It would be good to evaluate these more thoroughly.

### Questions
- Why use the output distortion metric (aka SSIM between output of the original and quantized models)? Since there are many other ways to define the distance between these two outputs (like mean-squared error, maximum mean discrepancy, absolute-difference, or other form of distributional distance metric)?
- In Eq.7, why does the total size constraint sum up both the quantized activation and the quantized weights? Shouldn't the weights and activations have separate constraint, one for the model parameters and other for the activations?
- Have you tried only parameter quantization to see how much lower bit-widths the models can tolerate if activations are kept in higher bits (8bit or higher)?
- How does one adapt the proposed quantization scheme for quantization aware training schemes?
- Since the proposed scheme is a mixed-precision scheme, do you have any analysis of which layers require more bits and which layers can tolerate lower bits?
- Can you clarify when the scheme says 4-bit quantized models, it means all the layers (except input/output) use 4 or fewer bits for quantization (for both weights/activations)?
- What modifications does one need to apply this scheme to Text-to-Image diffusion models?
- Most of the experiments involve UNet style networks, do you know if the same insights would hold true for transformer networks? Similarly, currently experiments only involve DDPM/DDIM frameworks, will the similar conclusion hold true for rectified flow / EDM frameworks?
- While the performance of W6A6 scheme looks comparable to full precision scheme from the quantitative metrics on Celeba-HQ (9.01 FID vs 9.06 FID), the qualitative images in Figure 2 shows a lot of distortions in the generated images. Do you have any insights as to why this issue occurs?
- In Table 1, why does the model performance increase with lower bits (for instance, Celeba-HQ with 8/8 has better performance than full precision)?
- Can you comment on the computational cost of various methods in Table 2 ? How does the proposed scheme fare against these baselines?

Missing references:
- Stable diffusion with core ml on apple silicon : https://github.com/apple/ml-stable-diffusion 
- BitsFusion: https://arxiv.org/abs/2406.04333
- LEARNED STEP SIZE QUANTIZATION https://openreview.net/pdf?id=rkgO66VKDS
- Efficientdm: Efficient quantization-aware fine-tuning of low-bit diffusion models: https://openreview.net/forum?id=UmMa3UNDAz

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present an approach to jointly quantize weights and activations of a diffusion model after it has been trained (i.e, post training quantization). To do so, a joint optimization problem is formuled: the authors propose to minimize the structured similarity index between original and quantized model, where the optimization paramters are bitwidth of quantization of weights and activations. The authors show that global SSIM optimization can be simplified (under some assumptions) into sum over SSIM measurements after every layer.

### Strengths
-

### Weaknesses
In the current form paper does not present the complete information to assess its merits and contributions. Paper's writing (grammar, style, flow) is good, but once it comes to describing the actual working soluiton (end of section 3) it strugles to present the final algorithm. There are inconsistentices in what is announced (i.e., abstract/intro) vs what is presented and demonstrated (experiments). The issue is significant: I am not confident that any reader would be able to implement the approach following the presentation in the paper.  I am not able to give any positive rating to this paper while these issues are clarified and/or resolved.

The authors present an approach to jointly quantize weights and activations of a diffusion model after it has been trained (i.e, post training quantization). To do so, a joint optimization problem is formuled: the authors propose to minimize the structured similarity index between original and quantized model, where the optimization paramters are bitwidth of quantization of weights and activations. The authors show that global SSIM optimization can be simplified (under some assumptions) into sum over SSIM measurements after every layer. 

Unfortunately, this is as much details I can provide about their approach after reading the paper. Paper omits the final presentation of the quantization approach/algorithm; has some logical inconsistencies, and as such raises many questions:
1. Section 3.4 does not present any readily awailable optimization algorithm. Lines 350-357 describe an approach, but it is impossible to follow. 
2. Given the problem defintion (eq.8, eq.16), authors never discuss what kind of optimization it is: in my understanding it is mixed-integer (some parts are fully differentiably, some parts are integer, like sizes of weights/activations). Therefore, in the same section 3.4 I do not understand how authors propose taking a derivative wrt s_w; which is defined as size of the weights?
3. When describing the soltuion on lines 350-357; authors propose enumeration over different choices; it would be highly benefitial to make very presize statements: what is being enumertaed, what are different choices there etc. As such, saying that total runtime of O(K*M*N) has "linear time complexity" is misleading: linear wrt what? size of the model? if it is then K, M, N needs to be clearly counted
4. The authors write that algorithm uses mixed precision (layers can have different bitwidth) and timestep-aware quantization. There is no word on how these are achieved and no experimental evaluation/discussion.
5. Experiments. I would like to understand how big are the networks that are being compressed, what is their architecture, and other basic information. Has authors trained them from scratch or obtained from somewhere? Visually speaking, it seems like 6bits quantizaiton introduces noticable quality degradation, and probably shouldn't be counted as a major achievement.
6. Experimetns. Where are the experimetnts where per-layer bitwidt are different? All presented experiments have same per layer setting.

### Questions
Please see weaknesses above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a post-training quantization approach for diffusion models. The paper finds that distributions of the outputs of diffusion models differ significantly across timesteps, and they utilize this finding to split the timesteps into meaningful groups and optimize the quantization configuration of each group separately. Empirical results demonstrate that the proposed approach achieves significant improvements over state-of-the-art methods, enabling the reduction of diffusion models' bit width to 5-6 bits while preserving high accuracy.

### Strengths
- The paper is written clearly and is easy to read.
- The paper provides both theoretical as well as empirical evidence that the proposed approach works.

### Weaknesses
For details, please see the Questions section.
- The motivation behind some of the design choices are not explained clearly
- Some parts of the proposed method is missing elaboration 

Minor:
- The paper does not provide specific implementation details such as the exact algorithms or code snippets used for quantization and optimization. Including these would help in reproducing the results.
- Including a user study or qualitative analysis to assess the perceptual quality of the generated images could provide additional insights into the effectiveness of the quantization method.

### Questions
- It is not clear how the timesteps are grouped. Please provide more details, as this is one of the major steps in the algorithm.
- It is mentioned that “the output distortion is defined as the Structural Similarity Index Measure (SSIM) loss between $O$ and $\hat{O}$ plus the MSE”. Is this a common method for evaluating output distortion? Why not e.g., PSNR?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a post-training quantization (PTQ) approach to reduce the model size and computational complexity of diffusion models. Specifically, it introduces a method that splits timesteps into groups, optimizing quantization parameters within each group independently. The quantization process for each group is then formulated as a rate-distortion optimization problem to minimize output distortion. Additionally, the approach employs mixed-precision quantization, applying different bit widths across layers.

### Strengths
1. Quantization in the diffusion model is important.
2. The use of mixed-precision quantization, with varying bit widths across layers, enhances the adaptability and precision of the quantization process.
3. Formulating the quantization as an optimization problem is reasonable.

### Weaknesses
1. Please elaborate on the advantages and differences of your mixed-precision strategy compared to prior quantization methods like MixDQ [1] and BitsFusion [2]. And provide a brief comparison table or paragraph highlighting key differences in approach and results.

2. The "Related Works" section has numerous typos and informal language, such as in lines 122 and 128 where "Zhong et al. Zhong et al. (2022)" and "Ma et al. Ma et al. (2023)" are repeated. And I also recommend consolidating several paragraphs into one paragraph in Section 2.2 for better flow.

3. Additionally, some sentences in this section are confusing. For instance, "Li et al. introduced a post-training quantization (PTQ) Li et al. (2023b) method called Q-Diffusion, tailored specifically to the distinctive multi-timestep pipeline and model architecture of diffusion models," could be rephrased for clarity. For example, " Li et al. (2023b) proposes Q-Diffusion, which is a PTQ method tailored specifically to the distinctive multi-timestep pipeline and model architecture of diffusion models". The preliminaries would also benefit from conciseness due to limited space, especially for details on diffusion models. For example, Eq. (2) and (4) can be removed or inserted in the paragraph.

4. The motivation for splitting timesteps into groups needs clarification. Currently, it's unclear how the approach of “splitting timesteps into groups to optimize quantization for each group” logically leads to “using mixed precision to quantize parameters across layers.” in line 215. Authors could include a brief explanation or diagram illustrating how these components of their approach are connected.

5. Lastly, Table 2 does not sufficiently demonstrate the advantages of the proposed method. With recent works achieving quantization at or below 4 bits, such as MixDQ (4 bits) and BitsFusion (1.99 bits), the lowest comparison at 6 bits in Table 2 is less compelling. Authors can include results for lower bit-widths (e.g. 2 bits, 4 bits) in their comparisons or explain why their method may not be applicable at such low bit-widths if that is the case. Additionally, it's better to provide more results compared to state-of-the-art methods [1,2].

### Questions
1. What is the difference of your mixed-precision strategy compared to prior quantization methods like MixDQ [1] and BitsFusion [2].

[1] MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed Precision Quantization. ECCV 2024.

[2] BitsFusion: 1.99 bits Weight Quantization of Diffusion Model. NeurIPS 2024.

2. What is the motivation for splitting timesteps into groups?

### Soundness
2

### Presentation
2

### Contribution
2
