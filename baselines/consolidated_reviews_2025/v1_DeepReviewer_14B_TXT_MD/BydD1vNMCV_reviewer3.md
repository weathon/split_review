### Summary

This paper introduces a stochastic variant of deep neural networks, called stochastic neural networks (StoNet), and shows that the StoNet falls into the framework of statistical modeling. It not only enables us to address fundamental issues in deep learning, such as structure interpretability and uncertainty quantification, but also provides with us a platform for transferring the theory and methods developed for linear models to the realm of deep learning. Specifically, it shows how the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models; establish that the sparse StoNet is consistent in network structure selection; and provides a recursive method to quantify the prediction uncertainty for the Stonet. Furthermore, it extends this result to the DNN by its asymptotic equivalence with the Stonet, showing that consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty. Additionally, it proposes to remodel the last hidden layer output and the target output of a well-trained DNN model using a Stonet on the validation dataset, and then assess the prediction uncertainty of the DNN model via the Stonet.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The authors provide a novel approach to address fundamental issues in deep learning, such as structure interpretability and uncertainty quantification, by introducing a stochastic variant of deep neural networks, called stochastic neural networks (StoNet). The paper shows that the StoNet falls into the framework of statistical modeling, enabling the adaptation of theory and methods developed for linear models to deep learning. The authors demonstrate how the sparse learning theory with the Lasso penalty can be adapted to deep neural networks (DNNs) from linear models, establish that the sparse StoNet is consistent in network structure selection, and provide a recursive method to quantify the prediction uncertainty for the Stonet. The paper also extends this result to the DNN by its asymptotic equivalence with the Stonet, showing that consistent sparse deep learning can be obtained by training a DNN with an appropriate Lasso penalty. Additionally, the paper proposes to remodel the last hidden layer output and the target output of a well-trained DNN model using a Stonet on the validation dataset, and then assess the prediction uncertainty of the DNN model via the Stonet.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed comparison of the proposed method with other existing methods for addressing the issues of structure interpretability and uncertainty quantification in deep learning. It would be beneficial to include a comprehensive comparison with other methods to highlight the advantages and limitations of the proposed approach. Specifically, the paper lacks a discussion on how the proposed StoNet compares to methods that directly regularize the DNN architecture, such as those using group sparsity or other structural constraints. Furthermore, the paper does not address the computational cost associated with training the StoNet, particularly in comparison to standard DNN training procedures. The practical implications of the asymptotic equivalence between StoNet and DNN are not fully explored, and it is unclear how this equivalence translates to finite sample scenarios, which are more common in practice. The paper also does not discuss the sensitivity of the StoNet to the choice of the noise variance parameters, which could significantly impact the performance and interpretability of the model.

### Suggestions

The paper should include a more thorough comparison with existing methods for structure interpretability and uncertainty quantification in deep learning. This comparison should not only focus on the theoretical aspects but also on the practical performance and computational cost. For example, the authors could compare their approach with methods that directly impose sparsity on the DNN weights or activations, such as group Lasso or other structural regularization techniques. A detailed analysis of the computational overhead of training the StoNet compared to standard DNN training is also necessary. This analysis should include the time complexity of the training algorithms and the memory requirements, especially when dealing with large-scale datasets. Furthermore, the authors should provide a more detailed discussion on the practical implications of the asymptotic equivalence between StoNet and DNN. It is crucial to investigate how this equivalence holds in finite sample settings and what are the limitations of this approximation. The paper should also include a sensitivity analysis of the StoNet to the choice of the noise variance parameters. This analysis should explore how different values of these parameters affect the model's performance, interpretability, and uncertainty quantification. The authors could consider using techniques like cross-validation to select optimal values for these parameters. 

To enhance the practical relevance of the proposed method, the authors should consider including experiments on real-world datasets. These experiments should demonstrate the effectiveness of the StoNet in addressing the issues of structure interpretability and uncertainty quantification in practical scenarios. The authors could also explore the use of the StoNet in different application domains, such as image classification, natural language processing, or time series analysis. This would help to showcase the versatility of the proposed method and its potential impact on various fields. The paper should also discuss the limitations of the proposed approach and suggest directions for future research. This discussion should include the potential challenges in applying the StoNet to very deep networks or very large datasets, as well as the limitations of the asymptotic equivalence assumption. The authors could also explore the possibility of developing more efficient algorithms for training the StoNet or extending the proposed method to other types of neural networks, such as convolutional neural networks or recurrent neural networks.

Finally, the paper should provide a more detailed explanation of the practical implementation of the proposed method. This explanation should include the specific steps involved in training the StoNet, selecting the noise variance parameters, and quantifying the prediction uncertainty. The authors could also provide code examples or tutorials to help other researchers reproduce their results and apply the proposed method to their own problems. This would make the paper more accessible and facilitate the adoption of the proposed method by the broader research community. The paper should also discuss the potential ethical implications of using the StoNet for uncertainty quantification, especially in high-stakes applications. This discussion should address the potential biases that could be introduced by the model and the importance of using the model responsibly.

### Questions

N/A

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
