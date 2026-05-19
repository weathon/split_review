### Summary

This paper proposes a generative pre-training method for video understanding. The method is inspired by generative pre-training from images, iGPT. To enable scaling to videos, the authors make several important improvements along the data, architecture, and evaluation axes. The model, called Toto, is a causal transformer that generates videos autoregressively, one token at a time. The authors pre-train their model on a diverse set of videos with over 1 trillion visual tokens. The tokens are quantized patch embeddings, rather than pixels, and the authors use relative embeddings for coarse-to-fine pre-training. The authors conduct a large-scale study across a suite of diverse benchmarks, including image recognition, video classification, object tracking, robotic manipulation, and scaling behaviors. The authors find that, despite minimal inductive biases, their approach achieves competitive performance across all benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise description of their method, making it easy for readers to understand the key concepts and contributions.
2. The authors conduct a large-scale empirical study, evaluating their method on a diverse set of benchmarks. This comprehensive evaluation provides strong evidence for the effectiveness of their approach.
3. The authors make several important improvements to enable scaling to videos, including the use of quantized patch embeddings and relative embeddings for coarse-to-fine pre-training. These improvements demonstrate the authors' deep understanding of the challenges of video pre-training and their ability to develop effective solutions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational costs associated with training and deploying Toto. Given the large scale of the model and the amount of data used for pre-training, it is important to understand the computational requirements of the method. Specifically, the paper does not provide a breakdown of FLOPs for different stages of training (e.g., pre-training, fine-tuning), nor does it discuss the memory footprint of the model during these stages. This makes it difficult to assess the practical feasibility of the approach, especially for researchers with limited computational resources.
2. The paper does not thoroughly address the potential limitations of the pre-training approach. For example, the authors do not discuss the potential for overfitting to the pre-training data or the challenges of adapting to tasks that are very different from those used for pre-training. The paper also lacks a discussion on the sensitivity of the model to hyperparameter choices during pre-training, which could impact its robustness and generalizability. Furthermore, the authors do not explore the impact of different pre-training dataset compositions on downstream task performance, which is crucial for understanding the model's biases and limitations.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the FLOPs required for both pre-training and fine-tuning stages. This should include the computational cost per training step, the total number of training steps, and the overall training time. Additionally, the authors should report the memory footprint of the model during training and inference, including the size of the model weights and the memory required for intermediate computations. This information should be provided for different model sizes and batch sizes to give a comprehensive view of the computational requirements. Furthermore, it would be beneficial to compare the computational cost of Toto with other state-of-the-art video pre-training methods to provide context for the reader.

To address the limitations of the pre-training approach, the authors should conduct a more thorough analysis of the model's generalization capabilities. This should include experiments on datasets that are significantly different from the pre-training data to assess the model's ability to adapt to new domains. The authors should also investigate the sensitivity of the model to hyperparameter choices during pre-training, such as the learning rate, batch size, and the number of training epochs. This could be done by performing ablation studies where different hyperparameter values are tested and the impact on downstream task performance is analyzed. Furthermore, the authors should explore the impact of different pre-training dataset compositions on downstream task performance. This could involve training the model on different subsets of the pre-training data and evaluating the performance on downstream tasks. This would help to identify potential biases in the pre-training data and to understand how the model's performance varies with different data compositions.

Finally, the authors should provide a more detailed discussion of the limitations of their approach. This should include a discussion of the potential for overfitting to the pre-training data, the challenges of adapting to tasks that are very different from those used for pre-training, and the sensitivity of the model to hyperparameter choices. The authors should also discuss the potential ethical implications of their work, such as the potential for bias in the pre-trained model and the potential for misuse of the technology. By addressing these limitations, the authors can provide a more complete and balanced view of their work and its potential impact.

### Questions

1. What are the computational costs associated with training and deploying Toto? How does the computational cost scale with the size of the model and the amount of data used for pre-training?
2. How does the choice of pre-training data affect the performance of Toto on downstream tasks? Are there any specific types of videos or tasks that Toto is particularly well-suited for or poorly-suited for?
3. How does Toto compare to other state-of-the-art video pre-training methods in terms of performance and computational cost? What are the key advantages and disadvantages of Toto compared to these methods?
4. What are the limitations of the proposed approach? Are there any specific scenarios or tasks where Toto is likely to fail or perform poorly? How can these limitations be addressed in future work?

### Rating

6

### Confidence

3

**********
