### Summary

This paper proposes a new attack on LLMs, called neural phishing, which enables an adversary to extract sensitive or personally identifiable information (PII) from a model trained on user data. The attack assumes that an adversary can insert as few as tens of benign-appearing sentences into the training dataset using only vague priors on the structure of the user data. The paper demonstrates that the attack can achieve high success rates, especially when the model is larger or overtrained. The paper also discusses some possible defenses against the attack, such as deduplication, watermarking, and regularization.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel and practical attack on LLMs, called neural phishing, which can extract sensitive or personally identifiable information (PII) from a model trained on user data.
- The paper evaluates the attack on three phases: poisoning, finetuning, and inference, and shows that the attack can achieve high success rates, especially when the model is larger or overtrained.
- The paper discusses some possible defenses against the attack, such as deduplication, watermarking, and regularization.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not compare the proposed attack with other existing data extraction attacks, such as model inversion attacks or membership inference attacks. It is unclear how the proposed attack differs from or improves upon these attacks in terms of effectiveness, efficiency, or stealthiness.
- The paper does not provide any real-world examples or case studies of the proposed attack. It is not clear how the attack would work in practice, and what kind of damage it could cause.
- The paper does not discuss the ethical implications of the proposed attack. The attack could potentially violate the privacy and security of individuals and organizations, and it is important to address these issues.

### Suggestions

The paper should include a more thorough comparison with existing data extraction attacks. Specifically, the authors should compare their attack with model inversion attacks and membership inference attacks, providing a detailed analysis of the differences in terms of attack success rate, computational cost, and stealthiness. This comparison should include a quantitative analysis of the quality and quantity of extracted data, as well as a discussion of the attack's robustness against various defenses. For example, the authors could compare the proposed attack with a state-of-the-art model inversion attack, such as the one proposed by Shokri et al. (2017), and evaluate the attack's performance on a common benchmark dataset. This would provide a clearer understanding of the advantages and disadvantages of the proposed attack compared to existing methods.

To enhance the practical relevance of the paper, the authors should provide real-world examples or case studies of the proposed attack. This could involve demonstrating the attack on a publicly available dataset containing sensitive information, such as the MIMIC-III dataset or a similar dataset with PII. The authors should also discuss the potential impact of the attack in real-world scenarios, such as the extraction of customer data from a model trained on customer support logs. This would help to illustrate the practical implications of the attack and highlight the potential risks associated with it. The case study should also include an analysis of the resources required to carry out the attack, such as the number of poisoned samples and the computational cost of the attack.

The paper should also include a detailed discussion of the ethical implications of the proposed attack. The authors should discuss the potential harms and risks associated with the attack, and propose some guidelines or recommendations for responsible research and development. This discussion should include an analysis of the potential for misuse of the attack, and how to mitigate the risks associated with it. The authors should also discuss the potential impact of the attack on individuals and organizations, and propose some measures to protect against the attack. For example, the authors could discuss the use of differential privacy or other privacy-preserving techniques to mitigate the risks associated with the attack.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
