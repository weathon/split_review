### Summary

The paper proposes a method to generate SVG code that is more readable by humans. The authors identify three desiderata for readable SVG code: logical structure, appropriate element use, and redundancy removal. They introduce three metrics (SPI, ESS, and RQ) to evaluate these aspects and design differentiable objectives to optimize the generation process. The method is tested on a synthetic dataset and the GPT-3.5 generated SVG code, showing improvements in readability and code structure compared to baseline models.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an interesting problem in the context of vector graphics and human-computer interaction. Improving the readability of generated SVG code can make it more accessible and easier to modify for users.

- The proposed metrics (SPI, ESS, and RQ) are well-motivated and provide a structured way to evaluate the readability of SVG code.

- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The evaluation is primarily qualitative, relying on GPT-3.5 to assess the readability of the generated SVG code. While GPT-3.5 is a powerful language model, its evaluation of code readability may not be entirely reliable or consistent. A more rigorous evaluation could involve human subjects rating the readability of the generated SVG code, which would provide a more direct measure of the method's effectiveness.

- The paper focuses on generating SVG code from synthetic and GPT-3.5 generated images. It would be beneficial to evaluate the method on real-world datasets with more complex and varied images to demonstrate its generalizability and robustness.

- The paper does not provide a detailed analysis of the computational cost associated with the proposed method. It would be helpful to understand the time and resources required to generate readable SVG code, which is important for practical applications.

### Suggestions

To strengthen the evaluation, the authors should conduct a user study involving human participants who assess the readability of the generated SVG code. This would provide a more direct and reliable measure of the method's effectiveness compared to relying solely on GPT-3.5's assessments. The user study should include a diverse group of participants with varying levels of expertise in SVG and code, and the evaluation should consider different aspects of readability, such as ease of understanding, logical structure, and visual coherence. The authors should also provide clear guidelines for the participants to ensure a fair and consistent evaluation process. Furthermore, the authors should analyze the correlation between GPT-3.5's assessments and human ratings to quantify the reliability of the automated evaluation.

To address the lack of real-world evaluation, the authors should extend their experiments to include a dataset of real-world images with complex and varied patterns. This would demonstrate the generalizability and robustness of the proposed method. The dataset should include images with different levels of complexity, varying types of patterns, and different levels of noise. The authors should also provide a detailed description of the dataset, including the number of images, the types of images, and the characteristics of the images. The evaluation should include both quantitative metrics and qualitative analysis of the generated SVG code. The authors should also compare the performance of their method on real-world images with its performance on synthetic and GPT-3.5 generated images.

Finally, the authors should provide a detailed analysis of the computational cost associated with the proposed method. This analysis should include the time and resources required to generate readable SVG code, as well as the scalability of the method to larger and more complex images. The authors should also discuss the potential limitations of the method in terms of computational cost and identify areas for future research to improve its efficiency. This analysis should include a breakdown of the computational cost of each step of the method, such as the VAE training, the differentiable objectives, and the SVG generation. The authors should also provide recommendations for optimizing the method to reduce its computational cost.

### Questions

- How does the proposed method handle cases where the input image is noisy or contains artifacts? Does the method still generate readable SVG code in such cases?

- The paper mentions that the proposed method can generate SVG code with simpler elements. How does the method ensure that the generated SVG code is not overly simplified and still accurately represents the input image?

- How does the proposed method compare to other state-of-the-art methods for generating vector graphics or code? A more comprehensive comparison would help to contextualize the contributions of the paper.

### Rating

5

### Confidence

3

**********
