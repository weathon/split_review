### Summary

This paper proposes a data poisoning attack that can extract sensitive information from LLMs. The attacker only needs to insert a few benign-appearing sentences into the training dataset to make the model memorize the secret information. The experimental results show that the proposed attack can achieve a high success rate.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed attack is practical and easy to implement.
2. The experimental results show that the proposed attack can achieve a high success rate.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well organized. The proposed attack is not clearly stated in the introduction section.
2. The paper lacks a detailed discussion of the threat model. It is unclear what assumptions are made about the attacker's capabilities and goals.
3. The paper does not provide a clear comparison with existing data poisoning attacks. It is unclear what makes the proposed attack unique or more effective.
4. The paper does not discuss the limitations of the proposed attack. It is unclear under what conditions the attack might fail or be less effective.

### Suggestions

The paper needs to clearly define the threat model in the introduction, specifying the attacker's goals, capabilities, and access to the system. For example, does the attacker have full control over the training data, or are there constraints on the type of data that can be poisoned? What kind of access does the attacker have to the model during training or inference? Specifying these details is crucial for understanding the scope and limitations of the proposed attack. Furthermore, the paper should clearly articulate how the proposed attack differs from existing data poisoning techniques. A detailed comparison with other methods, highlighting the unique aspects of the proposed approach, is necessary to establish its novelty and contribution. This comparison should not only focus on the attack methodology but also on the experimental setup and evaluation metrics used. For example, how does the proposed attack perform compared to other attacks in terms of success rate, poison rate, and computational cost? The paper should also discuss the limitations of the proposed attack. Under what conditions might the attack fail? Are there specific types of models or datasets where the attack is less effective? Addressing these questions will provide a more comprehensive understanding of the attack's applicability and limitations. For instance, the paper could explore the impact of different model architectures, training data distributions, or defense mechanisms on the attack's effectiveness. A thorough discussion of these limitations is essential for a balanced assessment of the proposed method.

### Questions

1. What are the assumptions made about the attacker's capabilities and goals?
2. How does the proposed attack compare with existing data poisoning attacks?
3. What are the limitations of the proposed attack?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
