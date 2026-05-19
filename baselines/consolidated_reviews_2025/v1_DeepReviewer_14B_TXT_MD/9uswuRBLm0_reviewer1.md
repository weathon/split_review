### Summary

The paper proposes a novel architecture for neural networks, called Cyclic NN, which allows for cyclic connections between neurons, inspired by the connectomes of biological neural networks. To overcome the challenges of cyclic dependencies, the work proposes to use local losses for optimization. As a concrete example, the paper of proposes a Graph Over Multi-layer Perceptron (GOMLP), and compares it with a set of baselines on MNIST, NewsGroup, and IMDB datasets.

### Soundness

1

### Presentation

2

### Contribution

2

### Strengths

1. The idea of introducing biologically-motivated architectures for deep learning is interesting and timely. There has been a surge of interest in this direction in recent years, and cyclic dependencies have been a challenge in implementation and training.

2. The paper does a good job of motivating the problem and the challenges of cyclic dependencies and localized training.

3.  The paper provides a good overview of the relevant concepts in a relatively concise manner.

### Weaknesses

#### Some Related Works

[1] Snns: An implementation framework for spiking neural networks.
[2] Neural networks: a comprehensive foundation .
[3] Deep learning with spike-time dependent plasticity.

#### comment

1. The implementation details and experimental setup are not clear. Specifically, the paper does not clearly describe the framework used for the implementation. Is it a modification of TensorFlow, PyTorch, or something completely different? There is also no information about the hardware used for the implementation or the runtime of the algorithms. Furthermore, the paper does not describe how the hyperparameters of the algorithms were selected, and it does not mention the number of random seeds used for the experiments. This lack of detail makes it difficult to reproduce the results and assess the validity of the proposed method.

2. The paper does not provide a clear definition of "computational neuron." It is unclear how it differs from a standard neuron in an MLP or an LSTM cell. The paper should provide a formal definition and explain the underlying assumptions. Without a clear definition, it is difficult to understand the novelty and contribution of the proposed architecture.

3. The paper does not provide a clear definition of "synapse." It is unclear how it differs from a weighted connection in a standard neural network. The paper should provide a formal definition and explain the underlying assumptions. Without a clear definition, it is difficult to understand the novelty and contribution of the proposed architecture.

4. The paper does not provide a clear explanation of how the model is trained with cyclic dependencies. The paper mentions that it uses a "local loss" for optimization, but it does not explain how this loss is computed and how it is used to update the model parameters. The paper should provide a detailed explanation of the training procedure, including the loss function and the optimization algorithm.

5. The paper does not provide a clear explanation of how the "goodness" score is used in the training process. The paper mentions that it is used to update the model parameters, but it does not explain how it is computed and how it affects the training dynamics. The paper should provide a detailed explanation of the goodness score and its role in the training process.

6. The paper does not provide a clear explanation of how the input data is encoded for the different datasets. The paper mentions that the input data is encoded as $h_{pos}$, $h_{neg}$, and $h_{neu}$, but it does not explain how this encoding is performed. The paper should provide a detailed explanation of the encoding procedure and its impact on the model performance.

7. The paper does not provide a clear explanation of the "readout layer." The paper mentions that it is used to produce the final output, but it does not explain how it is implemented and how it is trained. The paper should provide a detailed explanation of the readout layer and its role in the model architecture.

8. The paper does not provide a clear explanation of the "neutral" input. The paper mentions that it is used in the readout layer, but it does not explain what it represents and how it is used. The paper should provide a detailed explanation of the neutral input and its role in the model architecture.

9. The paper does not provide a clear explanation of the "positive" and "negative" inputs. The paper mentions that they are used in the computational neuron optimization, but it does not explain what they represent and how they are used. The paper should provide a detailed explanation of the positive and negative inputs and their role in the model architecture.

10. The paper does not provide a clear explanation of the "local loss" and how it is used in the training process. The paper mentions that it is used to update the model parameters, but it does not explain how it is computed and how it affects the training dynamics. The paper should provide a detailed explanation of the local loss and its role in the training process.

### Suggestions

To address the identified weaknesses, the authors should provide a more detailed description of the implementation framework, including the specific libraries and versions used. They should also specify the hardware used for the experiments, including the CPU, GPU, and memory configurations. Furthermore, the authors should provide a detailed explanation of the hyperparameter selection process, including the range of values explored and the criteria used for selection. The number of random seeds used for the experiments should also be specified to ensure the reproducibility of the results. The authors should also provide a clear and concise definition of the term "computational neuron," explaining how it differs from standard neurons in MLPs and LSTMs. This definition should include the underlying assumptions and the specific operations performed by the computational neuron. Similarly, a clear definition of "synapse" should be provided, explaining how it differs from weighted connections in standard neural networks. The authors should also provide a detailed explanation of the training procedure, including the loss function and the optimization algorithm. This explanation should include a clear description of how the cyclic dependencies are handled and how the local losses are computed and used to update the model parameters. The authors should also provide a detailed explanation of the "goodness" score, including how it is computed and how it affects the training dynamics. The encoding procedure for the input data should also be explained in detail, including how the input data is transformed into the $h_{pos}$, $h_{neg}$, and $h_{neu}$ representations. The role of the readout layer should be clarified, including how it is implemented and how it is trained. The authors should also provide a clear explanation of the neutral, positive, and negative inputs, including what they represent and how they are used in the model architecture. Finally, the authors should provide a clear explanation of the local loss, including how it is computed and how it affects the training dynamics.

Furthermore, the authors should consider providing a more detailed comparison of their approach with existing methods for training cyclic neural networks. This comparison should include a discussion of the advantages and disadvantages of each approach, as well as a comparison of their performance on various datasets. The authors should also consider providing a more detailed analysis of the computational complexity of their approach, including a comparison with the computational complexity of standard neural networks. This analysis should include a discussion of the time and memory requirements of the proposed method, as well as a discussion of the scalability of the approach to larger datasets and more complex models. The authors should also consider providing a more detailed analysis of the convergence properties of their approach, including a discussion of the conditions under which the training process converges to a stable solution. This analysis should include a discussion of the impact of the local loss function and the goodness score on the convergence properties of the approach.

Finally, the authors should consider providing a more detailed discussion of the limitations of their approach and potential directions for future research. This discussion should include a consideration of the challenges of applying the proposed method to more complex datasets and models, as well as a discussion of the potential for improving the performance of the approach through the use of more advanced optimization techniques. The authors should also consider providing a more detailed discussion of the potential for extending their approach to other types of cyclic dependencies, as well as a discussion of the potential for applying their approach to other areas of machine learning. The authors should also consider providing a more detailed discussion of the potential for combining their approach with other machine learning techniques, such as reinforcement learning and transfer learning.

### Questions

1. The paper proposes a novel architecture for neural networks, called Cyclic NN, which allows for cyclic connections between neurons, inspired by the connectomes of biological neural networks. To overcome the challenges of cyclic dependencies, the work proposes to use local losses for optimization. As a concrete example, the paper of proposes a Graph Over Multi-layer Perceptron (GOMLP), and compares it with a set of baselines on MNIST, NewsGroup, and IMDB datasets.

2. The work is interesting, but there are several weaknesses that need to be addressed.

3. The paper does not clearly define what a "computational neuron" is. How is it different from a neuron in an MLP or an LSTM cell? What are the underlying assumptions?

4. The paper does not clearly define what a "synapse" is. How is it different from a weighted connection in a standard neural network?

5. How is the model trained with cyclic dependencies? The paper mentions that it uses a "local loss" for optimization, but it does not explain how this loss is computed and how it is used to update the model parameters.

6. What is the "goodness" score and how is it used in the training process?

7. How is the input data encoded for the different datasets? The paper mentions that the input data is encoded as $h_{pos}$, $h_{neg}$, and $h_{neu}$, but it does not explain how this encoding is performed.

8. What is the "readout layer" and how does it produce the final output?

9. What is the "neutral" input and how is it used in the readout layer?

10. What are the "positive" and "negative" inputs and how are they used in the computational neuron optimization?

11. What is the "local loss" and how is it used in the training process?

### Rating

3

### Confidence

4

**********
