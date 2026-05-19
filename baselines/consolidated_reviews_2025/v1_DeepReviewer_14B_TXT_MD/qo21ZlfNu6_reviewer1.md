### Summary

The paper proposes a data extraction attack, in which an adversary can extract sensitive or personally identifiable information (PII), e.g., credit card numbers, from a language model. The adversary can insert a few benign-appearing sentences into the training dataset.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well written and easy to follow.

2. The authors show that the attacker does not need to know the exact secret prefix at inference time to extract the secret, and prefixing the model with random perturbations of the `true` secret prefix actually increases attack success.

### Weaknesses

#### Some Related Works


#### comment

1. The adversary needs to insert some poisoned data into the training dataset, which seems unrealistic. In general, the training dataset is very large and is usually collected from the web. It is hard for the adversary to inject the poisoned data.

2. The adversary needs to know the structure of the secret. For example, the adversary knows that the secret is a credit card number or a social security number. However, this assumption seems unrealistic.

3. The adversary needs to know the secret's prefix. For example, the adversary knows that the secret is preceded by "My social security number is". This assumption also seems unrealistic.

4. If the above assumptions are true, then it is very surprising that the proposed attack is effective, because the adversary does not know the exact secret and the number of the poisoned data is very small compared to the size of the training dataset.

### Suggestions

The paper's primary weakness lies in the unrealistic nature of its threat model. While the authors demonstrate a novel attack, the requirement for an adversary to inject poisoned data into a target model's training set is a significant hurdle. In most real-world scenarios, training datasets are massive and sourced from diverse, often uncontrolled, environments like the web. The likelihood of an attacker successfully injecting specific, targeted poisoned data into such a large dataset is extremely low. The paper should address this limitation by either justifying the realism of the threat model or by exploring alternative attack scenarios that do not rely on direct manipulation of the training data. For example, the authors could investigate whether a similar attack could be achieved through manipulation of the model's input during inference time, which would be more practical.

Furthermore, the assumption that the adversary has detailed knowledge of the secret's structure and prefix is also problematic. While the authors show that the attack is robust to some variations in the prefix, the requirement that the adversary knows the general format of the secret (e.g., a credit card number or social security number) and a likely prefix is still a strong assumption. In many real-world scenarios, the exact format and context of sensitive information may be unknown to the attacker. The paper should explore the attack's effectiveness under more realistic conditions where the adversary has less prior knowledge about the secret. This could involve testing the attack with a wider range of secret formats and less specific prefixes, or by exploring methods for the attacker to learn the secret's structure and prefix through interaction with the model.

Finally, the paper should provide a more thorough analysis of the attack's practical implications. While the authors demonstrate the attack's effectiveness under their specific assumptions, it is important to understand the attack's limitations and the conditions under which it is most likely to succeed. This analysis should include a discussion of the attack's sensitivity to various parameters, such as the number of poisoned examples, the length of the secret, and the size of the model. It would also be beneficial to explore potential defenses against the attack, such as data sanitization techniques or adversarial training methods. By addressing these limitations and providing a more comprehensive analysis, the paper would be more impactful and relevant to the broader research community.

### Questions

Please address my concerns in Weaknesses.

### Rating

3: reject, not good enough

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
