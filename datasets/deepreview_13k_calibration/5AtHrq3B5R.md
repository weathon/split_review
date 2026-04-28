# PnP-Flow: Plug-and-Play Image Restoration with Flow Matching

- Decision: Accept
- Avg Score: 5.50
- Scores: 3, 5, 6, 8

## Abstract
In this paper, we introduce Plug-and-Play (PnP) Flow Matching, an algorithm for solving imaging inverse problems. 
   PnP methods leverage the strength of pre-trained denoisers, often deep neural networks, by integrating them in optimization schemes. 
    While they achieve state-of-the-art performance on various inverse problems in imaging, PnP approaches face inherent limitations on more generative tasks like inpainting. 
    On the other hand, 
    generative models such as Flow Matching pushed the boundary in image sampling yet lack a clear method for efficient use in image restoration.
    We propose to combine the PnP framework with Flow Matching (FM) by defining a time-dependent denoiser using a pre-trained FM model.
    Our algorithm alternates between gradient descent steps on the data-fidelity term, reprojections onto the learned FM path, and denoising. 
    Notably, our method is computationally efficient and memory-friendly, as it avoids backpropagation through ODEs and trace computations. 
    We evaluate its performance on denoising, super-resolution, deblurring, and inpainting tasks, demonstrating superior results compared to existing PnP algorithms and Flow Matching based state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the PnP-Flow Matching algorithm for addressing imaging inverse problems, including denoising, super-resolution, deblurring, and inpainting. The method combines the Plug-and-Play (PnP) framework with Flow Matching (FM) models by using a time-dependent denoiser to tackle image restoration tasks. Specifically, the algorithm alternates between gradient descent on a data fidelity term, reprojection onto a flow matching path, and denoising. The experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. Low memory usage, making it suitable for high-resolution images.
2. Consistently performs well across multiple tasks, showing stable PSNR and SSIM improvements.

### Weaknesses
1. The writing quality needs Improvement. Certain explanations lack clarity, particularly in describing the algorithmic process, e.g., the function F. Specifically, the description of how the time-dependent denoiser integrates with the Plug-and-Play framework lacks sufficient detail. The paper does not clearly articulate how the gradient descent step, the reprojection onto the flow matching path, and the denoising step interact within each iteration. The role of the time parameter in the denoising process and how it is updated is also unclear.
2. The details of the proposed method are insufficient. The paper lacks a detailed explanation of the specific architecture used for the time-dependent denoiser. It is unclear how the flow matching model is trained and how its parameters are used in the PnP framework. The paper should provide more specifics on the implementation details, such as the choice of optimizers, learning rates, and other hyperparameters.
3. The experiment section should be improved. Please refer to the details below.

### Questions
1. The formula "y = noisy(Hx)" uses a general definition for the noisy function. It would be helpful if the paper and experiments explored multiple types of noise to assess the method’s robustness.

2. In Tables 1 and 2, the comparison is limited, particularly with only one diffusion-based method, PnP-Diff, which is a workshop paper, not a main conference paper. The authors should include comparisons with more diffusion-based methods, such as DPS, DeqIR, and DDRM, to provide a fuller view of how their method performs relative to the latest diffusion techniques.

3. The authors could enhance the evaluation by including the ImageNet dataset. For the denoising and deblurring tasks. Testing the method across various noise levels and degrees of blur on a large, diverse dataset like ImageNet would offer more insight into how well the algorithm handles different types of degradation.

4. In Figure 3, the visual results do not show a significant improvement over other methods (e.g., in the last row), even though the PSNR scores are higher. 

5. For real-world data with unknown degradation, it would be important to understand how well this method generalizes. 

6. It would strengthen the paper if the authors included examples of failure cases. 

7. In Table 3, not all methods are compared for computational time and memory usage. Including all relevant methods in this comparison would give a clearer picture of how the proposed algorithm stacks up in terms of efficiency across different benchmarks.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a zero-shot method (PnP-flow) for Inverse problems based on a pre-trained flow-matching (FM) model. The method combines the plug-and-play (PnP) framework with flow matching  by alternating between gradient descent steps on the data-fidelity term, reprojections onto the learned FM path, and denoising. PnP-flow achieves state-of-the-art (SOTA) results compared to existing PnP and flow-based algorithms  across different image inverse problems.

### Strengths
1. The method is training-free which makes it computationally practical.
2. The method achieves SOTA results compared to existing flow-based methods.

### Weaknesses
1. My major concern is the lack of comparison to recent zero-shot methods based on a pre-trained diffusion model such as DDNM [1] and DPS [2]. Specifically, the method's performance should be benchmarked against these methods, especially considering their state-of-the-art results in similar inverse problems. The absence of these comparisons makes it difficult to assess the true novelty and effectiveness of the proposed approach.
2. The proposed method is non-blind (assume the full knowledge of the degradation model) which limits its applicability. In real-world scenarios, the degradation model is often unknown or only partially known. Therefore, the assumption of full knowledge of the degradation model is a significant limitation that restricts the practical use of the method.

### Questions
1. Could you add comparisons with [1] and [2], or explain why those comparison are missing?
2. Could you comment on the potential applicability/extension of your method to the blind case?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to use flow matching in the plug-and-play framework for image restoration. The key is to use FM model as the denoisier. To avoid the numerical challenges, it integrates the implicit FM prior into a custom denoisier.

### Strengths
1, It proposes a design a time-dependent denoiser based on a pre-trained velocity field v learned through Flow Matching

2, This denoiser is integrated into an adapted Forward-Backward Splitting PnP framework that cycles through a gradient step on the data-fidelity term, an interpolation step and a denoising step

3, Being computationally efficient and memory-friendly via the use of ODE

### Weaknesses
1, Why the percpetual metrics are missing? From the visual results, it also seems that the results tend to be blurry. What’s the underlying reason? Is it due to the gradient step or the interpolation step, or something else? The lack of perceptual metrics makes it difficult to assess the practical value of the proposed method, especially given the observed blurriness in the visual results. It is crucial to understand if this blurriness is an inherent limitation of the method or a result of specific parameter choices in the gradient or interpolation steps.

2, In addition, one of the advantages of these generative method is its high perceptual quality, but this method seems to have achieved good distortion performance. How about the results of employing the same end-to-end U-Net model as a simple baseline (for example, using the L1 loss)? It is important to compare the proposed method against a strong baseline that uses a similar architecture but is trained end-to-end. This would help to isolate the benefits of the proposed approach compared to a standard method.

3, Can you visualize all the intermidate resutls of all three steps for all time steps? It could better help readers understand the method. The lack of visualization of the intermediate steps makes it challenging to understand the dynamics of the proposed method. Visualizing the results of the gradient, interpolation, and denoising steps at different time points would provide valuable insights into the method's behavior and potential failure modes.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors proposed a plug-and-play image restoration method based on flow matching. The reformulation starts from the forward-backward splitting algorithm, where the proximal step is replaced by a denoising step to form the plug-and-play forward-backward splitting algorithm. The authors insert a specific flow matching method, namely straight-line flows into the PnP-FBS framework due to the computation efficiency of the straight-line flows. Formally, the PnP flow matching algorithm consists of three steps: a gradient step on the data fidelity term, an interpolation step, and a PnP denoising step that is specifically designed to denoise inputs drawn from the straight path.

### Strengths
1. A new plug-and-play method based on flow matching is proposed in this paper.

2. The paper is well-written.

3. The derivations in this paper are rigorous.

4. The computational complexity and memory footprint of the proposed method is lower than the previous methods due to the careful design.

### Weaknesses
1. The restored images seem to be over-smoothed.

### Questions
1. Please explain why the computational complexity and memory footprint of the proposed method is lower than the previous method. Is it due to the design of the model or the choice of the straight-line flow?

### Soundness
3

### Presentation
3

### Contribution
3
