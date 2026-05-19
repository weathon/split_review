### Summary

This paper introduces a domain adaptation method for image restoration. The authors propose to leverage the unique property of how auxiliary conditional inputs influence the multi-step denoising process in diffusion models. A diffusion loss is derived to align the restored synthetic and real-world outputs with a target clean distribution. The paper also presents strategies such as channel-shuffling layer and residual-swapping contrastive learning to prevent shortcut learning during joint training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The idea of using diffusion loss for domain adaptation in image restoration is novel and well-motivated.
- The proposed channel shuffling layer and residual-swapping contrastive learning strategy are effective in eliminating shortcut learning.
- The method is evaluated on three different image restoration tasks and outperforms existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The method requires paired synthetic data and real-world data for training, which may not always be available in practice.
- The method is not specifically designed for low-light image enhancement and may not perform well on other image restoration tasks such as super-resolution and deblurring.

### Suggestions

The reliance on paired synthetic and real-world data is a significant limitation. While the authors mention the use of synthetic data, the process of generating high-quality, realistic synthetic low-light images that accurately reflect the complexities of real-world scenarios is non-trivial. The paper should include a more detailed discussion of the synthetic data generation process, including the specific transformations and augmentations applied, and how these choices impact the final performance. Furthermore, the authors should explore methods to reduce the dependence on paired data, such as using unpaired domain adaptation techniques or self-supervised learning approaches. This would make the method more practical and applicable to a wider range of real-world scenarios where paired data is scarce or unavailable. The paper should also include a sensitivity analysis of the method's performance with respect to the quality and quantity of synthetic data.

Although the method is evaluated on three different image restoration tasks, the paper lacks a thorough analysis of its performance on other common image restoration tasks such as super-resolution and deblurring. The authors should provide a more detailed explanation of why they expect the method to generalize to these tasks and what specific challenges might arise. For example, super-resolution often involves hallucinating high-frequency details, which may require different network architectures and training strategies than low-light enhancement. Similarly, deblurring requires the model to understand the specific blur kernel, which may not be well-represented in the training data. The paper should include experiments on these tasks to demonstrate the method's versatility and identify its limitations. A more comprehensive evaluation would strengthen the paper's claims and provide a better understanding of the method's applicability.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed method. The use of diffusion models can be computationally expensive, and the paper should discuss the training time and memory requirements of the method. This is particularly important for practical applications where computational resources may be limited. The authors should also explore methods to reduce the computational cost of the method, such as using more efficient diffusion models or training strategies. A detailed analysis of the computational cost would make the paper more practical and accessible to a wider range of researchers and practitioners.

### Questions

How does the method perform on other image restoration tasks such as super-resolution and deblurring?
How does the method handle cases where the real-world data is significantly different from the synthetic data?

### Rating

6

### Confidence

3

**********
