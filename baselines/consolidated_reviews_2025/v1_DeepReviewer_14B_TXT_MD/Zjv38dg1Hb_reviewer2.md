### Summary

This paper extends the consistency trajectory model (CTM) by introducing generalized CTMs (GCTMs), which enable translation between arbitrary distributions through ordinary differential equations (ODEs). Unlike CTMs, which are limited to mapping from Gaussian noise to data, GCTMs can handle a broader range of transformations. The authors explore the design space of GCTMs, discussing how different design choices impact performance across various image manipulation tasks, including image-to-image translation, restoration, and editing. Theoretical contributions include proving that CTMs are a special case of GCTMs when one side is Gaussian. Empirically, GCTMs achieve competitive results with just one function evaluation (NFE=1), demonstrating their efficiency and effectiveness in tasks like unconditional generation, image restoration, and editing.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach by extending CTMs to GCTMs, enabling translation between arbitrary distributions, not just from Gaussian to data. This generalization broadens the applicability of CTMs to a wider range of tasks.
2. The authors provide a comprehensive exploration of the design space for GCTMs, discussing how different design choices impact performance. This detailed analysis helps in understanding the flexibility and potential of GCTMs in various applications.
3. The paper demonstrates the effectiveness of GCTMs across multiple image manipulation tasks, including unconditional generation, image-to-image translation, restoration, and editing, with competitive results using only one function evaluation (NFE=1). This showcases the practical utility and efficiency of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with other state-of-the-art models in terms of quantitative metrics, which would help in better understanding the relative performance of GCTMs. Specifically, while the paper mentions achieving competitive results with NFE=1, it does not provide a clear comparison against other fast sampling methods or models optimized for similar tasks. This makes it difficult to assess the true advantage of GCTMs in a quantitative manner. For instance, a comparison with other one-step generative models or fast sampling techniques using metrics like FID, PSNR, or SSIM would be beneficial.
2. The theoretical contributions, while valuable, might not be sufficiently highlighted or explained in a way that is accessible to a broader audience, potentially limiting the paper's impact. The paper proves that CTMs are a special case of GCTMs, but the implications of this theoretical result and its practical benefits are not fully explored. The connection between the theoretical framework and the practical applications could be made more explicit, making it easier for readers to grasp the significance of the theoretical contributions.

### Suggestions

To address the lack of quantitative comparisons, the authors should include a more comprehensive evaluation against state-of-the-art models, especially those designed for fast sampling or one-step generation. This should include a table comparing FID scores for unconditional generation, PSNR and SSIM for image restoration tasks, and potentially LPIPS for perceptual quality. The comparison should not only focus on the final performance but also on the convergence speed and stability of the training process. Furthermore, it would be beneficial to compare against other methods that achieve similar low NFE, to better contextualize the performance of GCTMs. This would provide a clearer picture of the advantages and limitations of the proposed approach in a quantitative manner, allowing readers to better understand the practical impact of GCTMs.

To improve the accessibility and impact of the theoretical contributions, the authors should provide a more detailed explanation of the implications of proving that CTMs are a special case of GCTMs. This could include a discussion of how this theoretical result enables new applications or improves existing ones. For example, the authors could elaborate on how this generalization allows for more flexible manipulation of the latent space or how it can be used to develop new training strategies. Additionally, the authors should provide more intuitive explanations of the theoretical concepts, possibly using visual aids or analogies to make the material more accessible to a broader audience. This would help in highlighting the significance of the theoretical contributions and their practical relevance.

Finally, the authors should consider adding a section that explicitly discusses the limitations of GCTMs. This could include scenarios where GCTMs might not perform as well as other methods, or potential challenges in applying GCTMs to different types of data. By acknowledging the limitations, the authors can provide a more balanced view of their work and guide future research in this area. This would also help in setting realistic expectations for the readers and avoid overclaiming the capabilities of GCTMs.

### Questions

1. Could the authors provide more detailed comparisons with other state-of-the-art models in terms of quantitative metrics to better illustrate the advantages of GCTMs?
2. How do the theoretical contributions of the paper translate into practical benefits for the proposed GCTMs, and could these be explained in a more accessible manner for readers unfamiliar with the underlying theory?

### Rating

6

### Confidence

2

**********
