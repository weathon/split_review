### Summary

This paper presents a method for identifying the domain of unknown models. The proposed method uses a generative model to generate images based on text descriptions and then uses a pre-trained model to classify these images. By iteratively refining the text descriptions, the method can identify the domain of the unknown model. The authors demonstrate the effectiveness of their method on several datasets and models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting.
2. The method is well-motivated and addresses an important problem in machine learning.
3. The authors provide a thorough evaluation of their method on several datasets and models.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on the availability of a pre-trained model that can classify the generated images. This may not always be the case, especially for domains that are not well-represented in existing datasets.
2. The method may be sensitive to the choice of hyperparameters, such as the number of iterations and the learning rate. The paper does not provide a detailed analysis of the sensitivity of the method to these hyperparameters.
3. The method may not be able to identify the domain of models that are trained on very small datasets or models that are trained on data that is very different from the data used to train the pre-trained model. The paper does not provide a detailed analysis of the performance of the method on such models.

### Suggestions

The paper introduces an interesting approach for identifying the domain of unknown models using a generative model and a pre-trained classifier. However, several aspects of the method require further investigation. First, the reliance on a pre-trained model for classification is a significant limitation. While the authors mention using ImageNet, it is unclear how the method would perform with models trained on more specialized datasets. Future work should explore the use of more diverse pre-trained models or investigate methods to adapt the pre-trained model to new domains. For example, techniques like domain adaptation or fine-tuning could be explored to improve the robustness of the method when the pre-trained model is not well-suited to the target domain. Additionally, the paper should provide a more detailed analysis of the performance of the method when the pre-trained model is not aligned with the target domain, including a quantitative analysis of the classification accuracy and the impact on the final domain identification.

Second, the sensitivity of the method to hyperparameters needs to be addressed more thoroughly. The paper mentions the number of iterations and the learning rate, but it does not provide a detailed analysis of how these parameters affect the performance of the method. A more systematic study of the hyperparameter space is needed, including a sensitivity analysis to determine the optimal values for different datasets and models. This analysis should include not only the final accuracy but also the convergence speed and the stability of the method. Furthermore, the authors should explore adaptive hyperparameter tuning methods to reduce the manual effort required to set these parameters. For example, techniques like Bayesian optimization or reinforcement learning could be used to automatically find the optimal hyperparameter values for a given dataset and model.

Finally, the paper should provide a more detailed analysis of the performance of the method on models trained on small datasets or models trained on data that is very different from the data used to train the pre-trained model. The current evaluation is limited to relatively large datasets and models that are similar to the pre-trained model. The authors should investigate the performance of the method on more challenging scenarios, including models trained on very small datasets or models trained on data that is very different from the data used to train the pre-trained model. This analysis should include a quantitative evaluation of the performance of the method in these scenarios, as well as a discussion of the limitations of the method and potential solutions to address these limitations. For example, the authors could explore techniques like data augmentation or transfer learning to improve the performance of the method on models trained on small datasets.

### Questions

1. How does the method perform on models trained on very small datasets?
2. How does the method perform on models trained on data that is very different from the data used to train the pre-trained model?
3. How sensitive is the method to the choice of hyperparameters?
4. Can the method be used to identify the domain of models that are trained on data that is not well-represented in existing datasets?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
