# Simulating Training Dynamics to Reconstruct Training Data from Deep Neural Networks

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Whether deep neural networks (DNNs) memorize the training data is a fundamental open question in understanding deep learning. A direct way to verify the memorization of DNNs is to reconstruct training data from DNNs' parameters. Since parameters are gradually determined by data throughout training, characterizing training dynamics is important for reconstruction. Pioneering works rely on the linear training dynamics of shallow NNs with large widths, but cannot be extended to more practical DNNs which have non-linear dynamics. We propose Simulation of training Dynamics (SimuDy) to reconstruct training data from DNNs. Specifically, we simulate the training dynamics by training the model from the initial parameters with a dummy dataset, then optimize this dummy dataset so that the simulated dynamics reach the same final parameters as the true dynamics. By incorporating dummy parameters in the simulated dynamics, SimuDy effectively describes non-linear training dynamics. Experiments demonstrate that SimuDy significantly outperforms previous approaches when handling non-linear training dynamics, and for the first time, most training samples can be reconstructed from a trained ResNet's parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
SimuDy, a novel framework designed to reconstruct training data from the parameters of deep neural networks. SimuDy simulates the complex, non-linear training dynamics characteristic of deep architectures like ResNet by optimizing a dummy dataset to match the final parameters of a trained model. The authors demonstrate that SimuDy can accurately recover training samples under various conditions, including scenarios with unknown hyperparameters, outperforming previous linear-dynamics-based methods.

### Strengths
1.  Novelty: By simulating non-linear dynamics, SimuDy extends dataset reconstruction capabilities to deeper models, such as ResNet, making it applicable to practical, real-world architectures rather than limiting it to simpler models.
2. Robustness to Unknown Hyperparameters: SimuDy’s ability to reconstruct data even without exact training hyperparameters is a notable contribution, as real-world scenarios often lack complete information about training configurations.
3. Quantitative and Qualitative Performance Improvements: SimuDy outperforms existing methods both in terms of structural similarity index and visual quality of reconstructed samples.
4. The authors conduct extensive experiments, including robustness tests across varying dataset sizes, initializations, and dummy dataset configurations.

### Weaknesses
1. While SimuDy demonstrates promising results in reconstructing training samples from model parameters, there is limited discussion on the practical implications such as privacy or data security or in federated learning. 
2. SimuDy requires storing the entire training computation graph, which may limit its feasibility for very large models or datasets. The paper would benefit from a detailed breakdown of computational costs and memory requirements, especially for scaling to industry-sized datasets.
3. The initialization of dummy datasets appears somewhat arbitrary (e.g., using noise or natural images). Conduct a systematic study on different initialization techniques for dummy datasets, such as starting with more structured priors, to assess their impact on reconstruction quality and convergence speed.
4. Although SimuDy achieves high-quality reconstructions for small datasets, it’s unclear if these results generalize to larger, more diverse datasets. Extend experiments to larger datasets like ImageNet or tasks outside image classification to validate the scalability and generalization of SimuDy. Also it will be interesting to see the results of reconstruction when multiple objects are involved in an image.
5. Lack of experiments in Vision Transformers. It will be interesting to extend some experiments on Vision Transformers, which differ from CNNs in their patch-based processing and self-attention mechanisms. Also, perform a comparative study to examine the differences in reconstruction quality between CNNs and transformers.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the data reconstruction problem for more realistic neural networks (particularly ResNet-18) than previous works. They propose to optimize the input data so that the training direction by the optimized data aligns with the direction trained by the target data. The experiments show that the proposed method successfully reconstruct CIFAR10 data from the trained parameter (and also the initial parameter) of ResNet-18. The method and results are really fascinating, but there are some concerns in their experiments as explained below.

### Strengths
1. The paper is clearly written and easy to follow. The method is also clearly described.
2. The proposed method is derived in a straightforward way, and the implementation is also very simple. In spite of these simplicity, the results seem really impressive compared to previous works. I like both the idea and the simplicity.

### Weaknesses
1. The method assumes the initialization parameter to be given a priori, which is an unrealistic assumption for data reconstruction attack. However, I think this is not a critical issue because the contributions of this paper may not be limited to such attacks.
2. As authors also mentioned, the computational and memory budget may be terribly large due to higher order differentiation. Although this does not hurt the contribution of this work, it should be worth reporting the actual reconstruction time.
3. In experiments, the proposed method is only compared with Loo et al.'s method [1]. However, it should be also (rather) compared with Buzaglo et al.'s [2] (or Haim et al. [3]) method since this is the first successful method for data reconstruction from parameters. Moreover, to verify the generality of the proposed method, i.e., to check the results being not overfitting to CIFAR10 with ResNet18, the experiments should include several datasets (e.g. SVHN or MNIST) and model architectures like other ResNet architectures etc, with quantitative comparison to the baselines.
4. It is unclear how the coefficient of the TV regularization affects the quality of reconstructed data. It should be worth reporting the quantitative analysis from this perspective.
5. There are some missing related works [4,5] on gradient/trajectory matching for non-linear training dynamics. Zhao et al. [4] optimizes the input space by the cosine symmetry of two training dynamics, and hence is strongly related to this paper. Chijiwa [5] also optimizes the cosine similarity of two training dynamics, but focusing on the symmetry in a neural network rather than input data.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Simulation of training Dynamics (SimuDy), an easy and effective approach that reconstructs datasets from neural networks by optimizing dummy datasets through the comparison of resulting network parameters after training. The proposed method demonstrates better performance compared to existing baselines and shows promising results on relatively more advanced architectures like ResNets.

### Strengths
1. The proposed method has much better performance compared to existing baseline. The method is also easy to implement.
2. This work is both novel and interesting to me.

### Weaknesses
I am mainly concerned about the implication and the usefulness of the proposed method.
1. **Practicality and Scalability.** Back propagating with multiple training steps can be computationally intensive and challenging to scale for larger models and with larger datasets with high resolutions. The computational cost of iteratively optimizing a dummy dataset through multiple training steps, especially when each step involves a full forward and backward pass through a large network, is a significant hurdle. Additionally, the method requires prior knowledge of hyper-parameters such as the number of training steps, batch size, and weights at initialization/end which limits its applicability. The sensitivity of the reconstruction to these hyper-parameters is also unclear, potentially requiring extensive tuning for each new model and dataset. The method's reliance on specific initial and final weights also raises questions about its robustness to variations in training procedures.
2. **Implication and Usefulness.** I wonder how SimuDy can contribute to a deeper understanding of neural network training dynamics. It difficult to assess its broader usefulness in the field of machine learning. While the method demonstrates the ability to reconstruct training data, it is not clear how this reconstruction provides insights into the underlying mechanisms of neural network learning or generalization. The practical applications of this reconstruction, beyond verifying memorization, are also not well-defined. It is unclear how this method can be used to improve training algorithms, enhance model interpretability, or address other pressing issues in the field.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission proposes a method to reconstruct training data from neural network models by simulating their non-linear training dynamics. It adopts a nested optimization approach, where the outer optimization tunes the data being reconstructed, and the inner optimization performs regular training to match the original model’s parameters. Experimental results demonstrate successful dataset reconstruction for larger, more complex models like ResNet, where previous methods in linear regimes struggle, albeit assuming full access to weights, architecture, and hyperparameters.

### Strengths
- The paper is generally well-written and clear, making the core ideas easily accessible. 
- The proposed nested optimization approach is a meaningful extension over prior work for the task, effectively addressing non-linear training dynamics in a way that previous methods in linear regimes could not. This method is well-motivated and aligns with the challenges of reconstructing data from more complex models like ResNet.  
- Experimental evaluation is thorough and supports the claims within the chosen setting. The authors evaluate across different dataset and model sizes, confirming the performance benefits of SimuDy over baseline methods in similar constrained scenarios.

### Weaknesses
 - The submission lacks a defined threat model for data reconstruction. That makes it challenging to evaluate the setting, how broad or narrow it is, and what comparable methods might be. It seems to require knowledge about model architecture, weight (history) and hyperparameters - just not the gradients and training data. To me, that seems to be rather specific and I would ask the authors to elaborate on why they chose that particular setting. 
- Relatedly, the model-to-data ratio used here raises questions about both the threat model and the generalizability of the findings. A ResNet-18 trained on 120 images represents a highly constrained regime compared to standard machine learning applications. Is model depth less of a challenge here than dataset size? This also leads me to question whether memorization and an overfitted model-to-data ratio are necessary conditions for SimuDy’s success. If not, I would be interested in an experiment using a similarly complex model trained on a larger dataset, such as the full CIFAR-10 or CIFAR-100, with an attempt to reconstruct samples. Even if complete recovery is not feasible, partial reconstruction of a meaningful subset could provide insights into the general applicability of this method.
- Finally, I would like to see a more comprehensive evaluation against baseline methods. Model inversion attacks seem relevant here; if not, I would suggest the authors clarify why these are not comparable and discuss performance and computational cost of either approahces. Such a comparison would contextualize the efficiency and effectiveness of SimuDy against established approaches.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
