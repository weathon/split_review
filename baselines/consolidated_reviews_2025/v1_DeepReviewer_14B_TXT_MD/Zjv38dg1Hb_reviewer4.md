### Summary

This paper introduces Generalized Consistency Trajectory Models (GCTMs), an extension of Consistency Trajectory Models (CTMs). Unlike CTMs, which are limited to translating between Gaussian noise and data, GCTMs enable one-step translation between arbitrary distributions using ordinary differential equations (ODEs). The authors demonstrate GCTM's effectiveness across various image manipulation tasks, including unconditional generation, image-to-image translation, image restoration, and image editing.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel extension of CTMs to GCTMs, enabling one-step translation between arbitrary distributions, which is a significant advancement over existing CTMs.
2. The paper provides a comprehensive exploration of the design space of GCTMs, including different coupling strategies and perturbation techniques, which enhances the model's flexibility and applicability.
3. The paper demonstrates the effectiveness of GCTMs across a wide range of image manipulation tasks, including unconditional generation, image-to-image translation, image restoration, and image editing, with competitive results using only one function evaluation (NFE=1).

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison with other state-of-the-art models in terms of quantitative metrics, which would help in better understanding the relative performance of GCTMs. Specifically, while the paper presents results for various tasks, it does not provide a clear benchmark against established methods in each domain. For instance, in image-to-image translation, a comparison with models like CycleGAN or MUNIT using metrics like FID or LPIPS would be beneficial. Similarly, for image restoration tasks, comparisons with methods like DnCNN or Restormer using PSNR and SSIM would provide a clearer picture of GCTM's performance.
2. The theoretical contributions, while valuable, might not be sufficiently highlighted or explained in a way that is accessible to a broader audience, potentially limiting the paper's impact. The paper introduces the concept of Generalized Consistency Trajectory Models and provides theoretical justification, but the presentation could be more intuitive. A more detailed explanation of the underlying mathematical principles and their implications for practical applications would be beneficial. For example, a more detailed explanation of how the generalized consistency condition is derived and how it relates to the original consistency condition in CTMs would be helpful.

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
