# POC-SLT: Partial Object Completion with SDF Latent Transformers

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
3D geometric shape completion hinges on representation learning and a deep understanding of geometric data.
Without profound insights into the three-dimensional nature of the data, this task remains unattainable.
Our work addresses this challenge of 3D shape completion given partial observations
by proposing a transformer operating on the latent space representing Signed Distance Fields (SDFs).
Instead of a monolithic volume, the SDF of an object is partitioned into smaller high-resolution patches leading to a sequence of latent codes.
The approach relies on a smooth latent space encoding learned via a variational autoencoder (VAE), trained on millions of 3D patches.
We employ an efficient masked autoencoder transformer to complete partial sequences into comprehensive shapes in latent space.
Our approach is extensively evaluated on partial observations from ShapeNet and the ABC dataset where only fractions of the objects are given.
The proposed POC-SLT architecture compares favorably with several baseline state-of-the-art methods,
demonstrating a significant improvement in 3D shape completion, both qualitatively and quantitatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a sdf latent transformer for partial object completion. Specifically, it first divides high-resolution voxels into multiple smaller voxels and learns latent representations $z$ of these smaller voxels using a vae. Then, these latent representations are arranged as a sequence and processed by a masked transformer, which shares similarities with masked autoencoder. The experiments are conducted on three datasets for the completion task. The experimental results are better than those of the compared approaches.

### Strengths
1. The paper is easy to understand.
2. The experimental results are better than the compared methods.

### Weaknesses
The novelty of this paper is very limited.

1. The division of high-resolution voxels into smaller patches is reasonable but is straightforward and thus of limited innovation.

2. The p-VAE is almost identical to the original vae without any adaptation or improvements for this task.

3. The SDF-Latent-Transformer idea is very similar to the masked autoencoder [1], so it lacks novelty.

In short, the method proposed in this paper is somewhat like a combination of different well-known models, therefore, the novelty is the main concern.

### Questions
There is no questions, as the method proposed in this paper combines different existing models and therefore straightforward.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper works on the problem of partial object shape completion. Given a partial SDF volume, the proposed method first encodes the SDF volume into a latent code for each patch using the proposed Patch Variational Autoencoder(P-VAE), which encodes  SDF patches of resolution 32^3 into a latent code. 4^3 latent code encoded by the P-VAE can be used to train a masked autoencoder for the shape completion task. The proposed method achieved a significant reduction in the running speed thanks to its MAE architecture and short context length (64) for the transformer. The authors tested the proposed method on ShapeNet and ABC datasets and achieved better performance on metrics for reconstruction quality compared to previous methods. The qualitative study also demonstrated the results of reconstruction.

### Strengths
1. The authors proposed an efficient architecture that runs much faster than previous diffusion-based methods and auto-regressive-based methods and still demonstrated decent quantitative and qualitative results on shape completion benchmarks. The efficient design and fast running speed are appreciated for possible real-world applications. 
2. This paper addressed an interesting problem of 3D shape completion, which could lead to possible applications in 3D reconstruction and robotics. 
3. The authors compared the proposed method with the previous method quantitatively and qualitatively with high-quality renderings.

### Weaknesses
1. Lack of ablative study on the resolutions of the patch size and number of patches. The 32^3 SDF volume seems to be a relatively large SDF with lots of information. It will be good to have an ablative study with smaller patch sizes, such as 16^3 or 8^3. Furthermore, the impact of the number of patches used as input to the transformer is not explored. It is unclear if the current 4x4x4 grid of patches is optimal, or if a sparser or denser grid would yield better results, given the computational cost of the self-attention mechanism.
2. The presentation of the proposed method is vague and confusing. It will be much easier for the reader to understand if the authors point out they only use a transformer with 8x8x8 context length, and each token encodes the information of a 32^3 SDF volume, and that's why the whole model is lightweight. It would be good if the pipeline figures and method section made this point clear. The current description does not clearly articulate the relationship between the patch size, the input to the transformer, and the overall architecture, making it difficult to grasp the core design choices.
3. Multiple publications have followed AutoSDF, such as DiffComplete, but the authors did not quantitatively compare to those newer publications, which makes it difficult for the reviewer to judge the technical improvements over that method. The lack of comparison to these more recent methods makes it hard to assess the true advancement of the proposed approach.
4. Previous shape completion, like AutoSDF and Shapeformer, also demonstrated its power to generate multiple hypotheses when the partial observation is ambiguous. However, the proposed method did not discuss nor benchmark the task of multi-modal shape completion. Would it be possible to also evaluate total mutual difference(TMD)? The absence of multi-modal completion evaluation limits the understanding of the method's capabilities in handling ambiguous inputs.
5. The authors provided autoencoding results in Table 4 but did not compare them against any baseline methods such as shapeformer, providing limited information on understanding the effectiveness of the power of presentation. The autoencoding results are presented in isolation, making it difficult to gauge the effectiveness of the proposed method's representation learning capabilities.

### Questions
1. Can authors elaborate on the design choice for the patch size and size of the SDF volume and how changes to those hyper-parameters will affect the proposed method's performance?
2. The SDF volume contains much more information in the shape completion task than point cloud input because it hinted the location of the possible surface. How did the authors address this possible information leak in the evaluation benchmarks? Real-world sensors typically cannot provide SDF volume as an input because the location of the real surface is yet to be known; how could this method be applied to real-world 3D reconstruction applications?
3. Can authors provide the number of parameters in Table 1 to better understand differences compared to the previous method?
4. Can authors provide more information on the quantitative comparison to demonstrate the proposed method is comparable to more recent publications?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a shape completion method for high-resolution signed distance functions (SDFs), leveraging shared weights to efficiently represent small SDF patches.

The model encodes the entire shape as a sequence of latent codes generated by a patch-based variational autoencoder (P-VAE). Each patch is labeled as either "masked" (incomplete) or "non-masked" (complete), and shape completion is performed in latent space, with the result decoded back into an SDF using the P-VAE decoder. This patch-based approach allows for efficient inference and achieves high-quality results.

### Strengths
* Fast inference time: a key advantage over other sequential (eg autoregressive) approaches is utilizing the MAE decoder. 
* Modular Patch-VAE architecture enables generalization by pre-training on small-scale patches, an effective component, even if previously used in related works.  
* High-quality shape completion, especially in capturing fine-grained details.  
* Simple yet effective approach, that avoids unnecessary complexity with a straightforward architecture and objective.

### Weaknesses
 - Potential "leakage" issue: Non-masked voxels adjacent to masked patches may encode distances to missing parts, indirectly leaking information about regions to be completed. Discussing this limitation and potential remedies (e.g., using TSDF instead of SDF) would strengthen the work. Beyond conducting an ablation study of usage of SDF vs TSDF, first it should be qualitatively checked how much information is in fact encapsulated in non-masked patches, which regards the masked patches.
Masking in inference seems to require predefined regions marked as "known" or "unknown" potentially limiting the method. If so, this should be clarified as it diverges from traditional shape completion tasks, which typically address irregular partial shapes. You can also suggest possible modifications and future directions which allow general completion patterns.
- The approach is similar to pre-training on (T)SDF patches as done in [1]. This related work should be cited and discussed. Additionally, [1] demonstrated generalization to large scenes; it would be valuable to discuss whether the proposed method can achieve similar scalability.
- Limited model comparisons: The evaluation mainly compares against older methods like DeepSDF, omitting more recent approaches. To represent an implicit method such as DeepSDF, consider utilizing more recent architectures such as Neural Fields as Learnable Kernels for 3D Reconstruction.
- Comparison fairness: Competing models like SDFusion and PoinTR, unlike the proposed model, do not appear to receive explicit masking information on areas to be completed. If true, this gives the proposed model an advantage and should be addressed.
- Metrics: The evaluation relies heavily on UHD, which I believe is secondary in shape completion contexts, mainly measuring the fidelity of preserving the known region. Including additional metrics as is done in baselines would better reveal the model's performance. Those metrics can be all or at least some of the metrics you have used for your inner comparisons. Give precedence to important metrics regarding shape completion, such as Chamfer distance which is elementary as a main metric.
- The ordering of grid coordinates in the latent code (due to positional encoding in the transformer) suggests that the model expects canonically oriented shapes, which may be difficult to achieve in practice given partial input.

### Questions
* Referring to the first weakness, it is hard to understand the function of masking in inference, perhaps should elaborate / clarify.
* Is using a VAE really necessary if the model is non-probabilistic?
* Is composing SDF from patch SDFs that simple? Intuitively it appears that this might cause issues near patch boundaries

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
3

### Summary
This paper introduces a framework for efficient completion of partial SDF. Its contributions are:
1. A novel framework for efficient completion of partial SDF using VAE which is described as Patch Variational Autoencoder (P-VAE) and MAE-like transformer architecture which is described as SDF-Latent-Transformer (SLT).
2. Evaluation of P-VAE and SLT on ShapeNet and ABC dataset that indicates that P-VAE is superior to some of the state-of-the-art methods.

This paper indicates the effectiveness of P-VAE and SLT with a lot of qualitative and quantitative results. But this method lacks some special designs for SDF and there are still some questions that need to be clarified.

### Strengths
1. This paper introduces VAE-like encoder-decoder architecture and MAE-like transformer architecture to efficiently complete partial SDF.
2. P-VAE and SLT have shown superior performance on ShapeNet and ABC dataset.

### Weaknesses
1. SDF represents the surface of an object with a signed distance function, and the value reflects the distance to the surface. However, P-VAE has no unique design for addressing the conflicts caused by inconsistent values in different SDF patches, which may harm the performance of shape completion based on SDF. The authors should discuss how to handle or mitigate potential inconsistencies between SDF patches or provide an analysis of how much this affects the completion results in practice. Specifically, the method lacks a mechanism to ensure that the predicted SDF values at the boundaries of adjacent patches are consistent, which could lead to artifacts or discontinuities in the completed shape. A more detailed analysis of the magnitude and frequency of these inconsistencies is needed to fully assess the method's robustness.

2. In lines 250-251, the authors mention that position encoding is helpful for shape completion, but the paper lacks details like how to design the position embedding and some results that indicate it impacts shape completion. The authors should provide the exact formulation of the positional encoding and the ablation study showing the impact of including against excluding the positional encoding on completion quality. It is not clear if the positional encoding is simply a concatenation of the patch coordinates or if a more sophisticated encoding scheme is used. Without this information, it is difficult to reproduce the results and understand the contribution of this component.

3. In lines 306-307, measuring the completion performance by measuring how faithfully the geometry given in the input was preserved during the completion may not be enough. The metrics that evaluate the plausibility or realism of the completed regions should also be considered. The paper should include metrics that assess the quality of the completed regions, such as the smoothness of the surface, the absence of artifacts, and the overall geometric plausibility. Relying solely on input fidelity may not capture the full picture of completion quality.

4. There are three types of completion, but there is no qualitative result about randomly removing the patches. The authors should include qualitative examples of the random patch removal completion task in their results section or supplementary materials. This is important to visually assess the method's performance in a more realistic scenario where the missing regions are not predefined or structured.

5. The paper compares the quantitative results with some state-of-the-art methods only on chairs, which is insufficient to prove the effectiveness of P-VAE and SLT. More object categories should be considered. The current evaluation is limited to a single object category, which makes it difficult to generalize the findings to other types of shapes. A more comprehensive evaluation across a wider range of object categories is needed to demonstrate the robustness and versatility of the proposed method.

### Questions
- See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
