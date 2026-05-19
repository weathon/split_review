### Summary

This paper proposes a practical data extraction attack called "neural phishing" that enables an adversary to extract sensitive or personally identifiable information (PII) from a model trained on user data with high success rates. The attack assumes that an adversary can insert a few benign-appearing sentences into the training dataset and has vague priors on the structure of the user data. The paper demonstrates that the attack can achieve success rates of up to 50% in extracting sensitive information such as credit card numbers.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces a novel attack vector on large language models, demonstrating that it is possible to extract sensitive information with high success rates by inserting a few benign-appearing sentences into the training dataset.

2. The paper provides insights into the vulnerability of large language models to memorization and extraction attacks, highlighting the need for robust defenses against such attacks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on a specific type of attack, namely neural phishing, which targets the extraction of sensitive or personally identifiable information (PII) from a model trained on user data. While the attack is shown to be effective, it is not clear how generalizable the findings are to other types of attacks or models. Specifically, the paper does not explore the attack's efficacy against models trained with different architectures or on datasets with varying characteristics. The reliance on a specific model and dataset limits the scope of the conclusions.

2. The paper does not discuss potential defenses against the proposed attack. It is important to understand how the attack can be mitigated or prevented in practice. For example, the paper does not explore techniques such as adversarial training, input sanitization, or differential privacy, which could potentially mitigate the risk of sensitive information extraction. The lack of discussion on defense mechanisms is a significant gap.

3. The paper does not provide a detailed analysis of the computational resources required to carry out the attack. This information is important for understanding the feasibility of the attack in practice. The paper should specify the hardware requirements, training time, and the number of poisoned samples needed to achieve the reported success rates. Without this information, it is difficult to assess the practicality of the attack.

### Suggestions

The paper should broaden its investigation to include a more diverse set of models and datasets. Specifically, the authors should evaluate the neural phishing attack on models with different architectures, such as transformer variants or recurrent neural networks, and on datasets with varying sizes and characteristics. This would provide a more comprehensive understanding of the attack's generalizability and limitations. Furthermore, the paper should explore the impact of different training parameters, such as learning rate and batch size, on the attack's success rate. This would help to identify the conditions under which the attack is most effective and provide insights into potential defense mechanisms. The authors should also consider evaluating the attack on datasets with different levels of sensitivity to understand the attack's applicability in various real-world scenarios.

The paper should include a thorough discussion of potential defense mechanisms against the proposed attack. This should include an analysis of existing techniques, such as adversarial training, input sanitization, and differential privacy, and their effectiveness against neural phishing. The authors should also explore novel defense strategies specifically tailored to this attack. For example, they could investigate methods to detect and remove poisoned samples from the training data or develop techniques to make the model more robust to memorization of sensitive information. The paper should also discuss the trade-offs between the effectiveness of different defense mechanisms and their computational cost. A comprehensive analysis of defense strategies is crucial for making the research practically relevant and for promoting the development of more secure machine learning systems.

The paper should provide a detailed analysis of the computational resources required to carry out the attack. This should include a specification of the hardware used for the experiments, such as the type of GPUs and the amount of memory, as well as the training time required to achieve the reported success rates. The authors should also provide a breakdown of the computational cost of different stages of the attack, such as the poisoning phase and the extraction phase. This information is essential for assessing the feasibility of the attack in practice and for understanding its potential impact. Furthermore, the paper should discuss the scalability of the attack to larger models and datasets, as well as the potential for optimizing the attack to reduce its computational cost.

### Questions

1. How does the neural phishing attack compare to other types of attacks on large language models? Are there any existing attacks that are more effective or easier to carry out?

2. What are the potential defenses against the neural phishing attack? How can the attack be mitigated or prevented in practice?

3. What are the ethical implications of the neural phishing attack? How can the research be used responsibly and for the benefit of society?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
