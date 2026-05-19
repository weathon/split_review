### Summary

This paper introduces a concept-based explainable image representation learning method. It uses GPT-4 to generate a concept set and CLIP to project image features into the concept space. Then, a VAE is trained to reconstruct the concept vectors, and the latent embedding is used for downstream tasks. The authors demonstrate the effectiveness of the proposed method on unsupervised clustering and linear probe classification. The concept importance scores are calculated using the integrated gradient method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The idea of combining concept bottleneck models with representation learning is interesting.
2. The proposed method achieves good performance on unsupervised clustering tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The concept set generation process is similar to LF-CBM, and the concept vector construction process is similar to CLIP-Dissect. The main difference is that a VAE is trained to learn a more compact latent embedding for downstream tasks.
2. The performance on linear probe classification is worse than CLIP, which makes the proposed method less practical. The use of a VAE, while intended to create a more compact representation, appears to result in a loss of discriminative information crucial for classification tasks. This raises concerns about the trade-off between interpretability and performance.
3. The method has many hyperparameters, which may limit its generalizability. The reliance on multiple hyperparameters, including those for the VAE, concept selection, and integrated gradient calculation, introduces a potential for overfitting and makes it challenging to apply the method to new datasets without extensive tuning. The lack of a clear strategy for hyperparameter selection further exacerbates this issue.

### Suggestions

The paper should more clearly articulate the specific advantages of using a VAE for concept vector compression, beyond simply stating that it creates a more compact representation. A detailed analysis of the VAE's latent space, including visualizations and an examination of the learned features, would be beneficial. Furthermore, the authors should investigate alternative methods for concept vector compression that might preserve more discriminative information for classification tasks. For example, exploring different loss functions or regularization techniques within the VAE framework could potentially mitigate the performance drop observed in linear probe classification. It would also be valuable to compare the proposed method with other representation learning techniques that focus on preserving class-specific information, to better understand the trade-offs between interpretability and classification performance.

To address the hyperparameter sensitivity, the authors should provide a more systematic approach for hyperparameter selection. This could involve a sensitivity analysis to identify the most critical hyperparameters and their optimal ranges. Additionally, the authors should explore techniques for automatic hyperparameter tuning, such as Bayesian optimization or grid search, to reduce the manual effort required for each new dataset. The paper should also include a discussion of the computational cost associated with hyperparameter tuning and the overall method, which is important for assessing its practicality. Furthermore, the authors should investigate the robustness of the method to different hyperparameter settings, to ensure that the results are not overly sensitive to specific choices.

Finally, the paper should include a more thorough evaluation of the interpretability of the learned representations. While the concept importance scores provide some insight, a more comprehensive analysis is needed to demonstrate the practical value of the proposed method. This could involve a qualitative evaluation of the concept importance scores for different images, as well as a comparison with other interpretability methods. The authors should also investigate the ability of the method to identify spurious correlations or biases in the data, which is a key benefit of concept-based interpretability. A more detailed analysis of the limitations of the method, including cases where it fails to provide meaningful interpretations, would also be valuable.

### Questions

1. How does the VAE help to learn a better representation? The authors claim that the VAE helps to enhance the pertinent concepts while possibly diminishing others that are less crucial. However, the VAE is trained to reconstruct the concept vectors, which contain all the concept information. It is unclear how the VAE can distinguish between important and unimportant concepts. Besides, the reconstruction loss in Eq (2) is based on the full concept vector. Why not use the concept importance-weighted vector for reconstruction?
2. How are the hyperparameters selected? The proposed method has many hyperparameters, which may limit its generalizability. It would be helpful if the authors could provide more details on how the hyperparameters are selected and how sensitive the method is to different hyperparameter settings.
3. What is the difference between the proposed method and LF-CBM+CLIP-Dissect+VAE? It seems that the proposed method is a combination of these three methods.
4. Why is the performance on linear probe classification worse than CLIP? The authors claim that the transformation enhances interpretability, which may lead to some information loss. However, the concept vector is derived from the CLIP image encoder, which contains more information than the CLIP image features. It is unclear why the performance drops after this transformation.
5. How can the concept importance scores be used for model debugging or bias detection? The authors should provide more concrete examples to demonstrate the practical value of the proposed method.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
