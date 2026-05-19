### Summary

This paper proposes a novel backdoor attack against federated learning (FL) systems. The proposed attack leverages a generative neural network to produce imperceptible and adaptive triggers, making poisoned samples have similar hidden features to benign samples with the target label. Extensive experiments are conducted to demonstrate the effectiveness of the proposed attack.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed attack is novel and effective. It leverages a generative neural network to produce imperceptible and adaptive triggers, making poisoned samples have similar hidden features to benign samples with the target label. This is a novel idea that has not been explored in the literature.
2. The proposed attack is stealthy. The imperceptible triggers make it difficult for defenders to detect the attack. The adaptive nature of the triggers makes it difficult for defenders to develop effective defenses.
3. The proposed attack is robust. The attack is robust against various defenses, including norm clipping and FLAME.
4. The experimental results are promising. The proposed attack achieves high attack success rates in all the datasets and models considered in the paper.

### Weaknesses

#### Some Related Works

[1] Panda: A practical backdoor attack against federated learning.
[2] Backdoor attacks to federated learning using poison the well.

#### comment

1. The proposed attack requires a large number of local iterations to converge, which may not be practical in some scenarios. Specifically, the convergence time, while not explicitly stated as a primary metric, is implicitly tied to the number of local iterations. This could be a limitation in resource-constrained environments or when rapid model deployment is necessary.
2. The proposed attack requires a large number of local data to train the generative neural network, which may not be available in some scenarios. The reliance on a substantial local dataset for training the generative model could hinder its applicability in scenarios where data is scarce or privacy concerns limit data sharing, even within the federated learning framework.
3. The proposed attack may not be effective against some advanced defenses, such as anomaly detection and backdoor detection. While the paper demonstrates robustness against norm clipping and FLAME, the effectiveness against more sophisticated anomaly detection techniques, which might analyze the distribution of model updates or feature representations, remains unclear. Similarly, the resilience against dedicated backdoor detection mechanisms that look for specific trigger patterns or model behaviors is not fully explored.

### Suggestions

The paper presents a novel backdoor attack using generative triggers, but several aspects could be strengthened to enhance its practical relevance and robustness. First, the authors should investigate methods to reduce the number of local iterations required for convergence. This could involve exploring more efficient optimization techniques for the generative network or adapting the attack to work with fewer local updates. For example, techniques like adaptive learning rates or early stopping criteria could be explored to accelerate convergence without sacrificing attack effectiveness. Furthermore, the authors should consider the trade-off between attack success rate and convergence speed, providing a more detailed analysis of how these factors interact under different conditions. This would provide a more comprehensive understanding of the attack's practical limitations and potential for real-world deployment.

Second, the reliance on a large local dataset for training the generative network is a significant limitation. The authors should explore methods to mitigate this requirement, such as using data augmentation techniques or transfer learning from pre-trained models. For instance, the generative network could be initialized with weights from a model trained on a large public dataset, and then fine-tuned on the limited local data. Alternatively, the authors could investigate the use of synthetic data generation techniques to create additional training samples for the generative network. This would make the attack more practical in scenarios where data is scarce. Additionally, the authors should provide a more detailed analysis of how the size of the local dataset affects the attack's effectiveness, providing a clearer understanding of the data requirements for successful attacks.

Finally, the paper should include a more thorough evaluation of the attack's robustness against advanced defense mechanisms. Specifically, the authors should evaluate the attack against anomaly detection techniques that analyze the distribution of model updates or feature representations, as well as dedicated backdoor detection mechanisms that look for specific trigger patterns or model behaviors. This could involve testing the attack against defenses such as robust aggregation rules, which aim to filter out malicious updates, or techniques that analyze the feature space for anomalies. Furthermore, the authors should explore potential countermeasures that could be used to enhance the attack's resilience against these defenses. This would provide a more comprehensive understanding of the attack's limitations and potential vulnerabilities, and guide future research in this area.

### Questions

1. How does the proposed attack perform against other advanced defenses, such as anomaly detection and backdoor detection?
2. How does the proposed attack perform against other types of triggers, such as patch-based triggers or semantic triggers?
3. How does the proposed attack perform against other types of models, such as transformers or graph neural networks?
4. How does the proposed attack perform against other types of datasets, such as text or audio datasets?
5. How does the proposed attack perform against other types of federated learning settings, such as cross-silo or cross-device federated learning?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
