### Summary

The paper proposes a method to improve conditional generation using pretrained diffusion models. The key idea is to constrain the optimization of the guidance loss to the tangent space of the manifold of the data. The authors propose several ways to achieve this, including a shortcut method that does not require projection onto the tangent space. The authors evaluate their method on several tasks, including image restoration, super-resolution, and style transfer, and show that it outperforms existing methods in terms of both quality and speed.

### Soundness

4 excellent

### Presentation

4 excellent

### Contribution

4 excellent

### Strengths

* The paper is well-written and easy to follow.
* The proposed method is simple and effective.
* The experimental results are convincing and demonstrate the superiority of the proposed method over existing approaches.

### Weaknesses

#### Some Related Works


#### comment

 * The proposed method requires a pre-trained autoencoder, which may not be available for all tasks or datasets.
* The authors only provide qualitative results for the style guidance with Stable Diffusion. More quantitative results are needed to better evaluate the proposed method.

### Suggestions

The paper introduces an interesting approach to conditional generation by leveraging the tangent space of the data manifold. However, the reliance on a pre-trained autoencoder is a significant limitation that needs to be addressed more thoroughly. While the authors mention the use of VQGAN, they should explore the impact of different autoencoder architectures and training procedures on the final results. For example, the choice of quantization method in VQGAN could significantly affect the quality of the latent space and, consequently, the performance of the proposed method. A more detailed analysis of the sensitivity of the method to the autoencoder's characteristics is needed. Furthermore, the authors should investigate the possibility of using other types of autoencoders, such as variational autoencoders or normalizing flows, and compare their performance. This would provide a more comprehensive understanding of the method's applicability and robustness.

Regarding the evaluation, the lack of quantitative results for the style guidance task is a major concern. While qualitative results can be visually appealing, they are not sufficient to objectively assess the performance of the method. The authors should include quantitative metrics such as perceptual similarity scores (e.g., LPIPS, FID) and style similarity scores (e.g., Gram matrix loss) to compare their method with existing approaches. Furthermore, the authors should evaluate their method on a wider range of style transfer datasets and compare it with state-of-the-art style transfer methods. This would provide a more rigorous evaluation of the method's effectiveness and generalizability. The current evaluation is limited to a single dataset and a few qualitative examples, which is not sufficient to draw strong conclusions about the method's performance.

Finally, the authors should provide more details about the implementation of their method, including the specific hyperparameters used for training and inference. This would allow other researchers to reproduce their results and build upon their work. The authors should also discuss the computational cost of their method and compare it with existing approaches. This is important for practical applications, as the computational cost can be a limiting factor in many cases. A more detailed analysis of the method's limitations and potential failure cases would also be beneficial. This would help to identify areas for future research and improvement.

### Questions

* Can the authors provide more details about the implementation of their method?
* How does the proposed method compare to other state-of-the-art methods in terms of computational cost?

### Rating

8: accept, good paper

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
