### Summary

In this paper, the authors propose FTA, a generator-assisted backdoor attack. The proposed attack leverages a generative model to generate sample-specific triggers. As such, the generated triggers are stealthy, flexible, and adaptive.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The idea of using a generator to generate sample-specific triggers is interesting.
- The authors evaluated the proposed method against several defenses.

### Weaknesses

#### Some Related Works

[1] Invisible backdoor attack with sample-specific triggers.
[2] Subpopulation backdoor attacks: Training time backdoors without poisoning.

#### comment

 - The novelty of this paper is only incremental. The idea of using a generator to generate sample-specific triggers has been investigated in [1]. The authors should discuss the difference between the proposed method and existing approaches.
- The authors did not explain why the proposed method can bypass defenses, especially backdoor detection defenses. For example, the authors evaluated their method against FLIP, but they did not explain why their method can bypass FLIP. I think the authors should provide some insights into this. The same applies to other defenses.
- The authors did not compare their method with state-of-the-art backdoor attacks, e.g., [2]. As such, it is unclear whether the proposed attack is more effective than existing attacks.
- The paper is hard to follow. The authors used a lot of notations, but some of them were not defined. For example, what is $D^{cln}$ and $D^{bd}$? What is the target labeling function $\eta$? What is the dataset $D_{cln}$? What is the sampled subset $D_{bd}$? Who is the server? What is the malicious model?

### Suggestions

The authors should provide a more thorough comparison to existing backdoor attacks that utilize generative models, specifically highlighting the differences in trigger generation and attack methodology. A detailed analysis of how the proposed method's sample-specific triggers differ from those in [1] is crucial. This should include a discussion of the advantages and disadvantages of each approach, focusing on aspects such as stealthiness, flexibility, and adaptivity. Furthermore, the authors should clarify the specific mechanisms that enable their attack to bypass backdoor detection defenses, such as FLIP. A deeper explanation of why the sample-specific triggers are more effective at evading detection compared to fixed triggers is needed. This should involve an analysis of how the generative model manipulates the feature space and how this manipulation affects the detection capabilities of defenses. The authors should also consider providing a theoretical analysis of the attack's robustness against different types of defenses.

To strengthen the paper, the authors should include a comprehensive comparison with state-of-the-art backdoor attacks, including those that do not rely on generative models. This comparison should not only focus on attack success rate but also on other relevant metrics such as stealthiness, robustness against defenses, and computational cost. The authors should clearly define all notations used in the paper, including $D^{cln}$, $D^{bd}$, $D_{cln}$, $D_{bd}$, the target labeling function $\eta$, the server, and the malicious model. A clear description of the experimental setup, including the network architectures used for the generative model and the target model, is also necessary. This should include details about the number of layers, activation functions, and optimization parameters. The authors should also provide a more detailed explanation of the training process, including the loss functions used and the training schedule.

Finally, the authors should provide more insights into the limitations of their proposed method. This should include a discussion of the potential vulnerabilities of the attack and the scenarios where it might fail. For example, the authors could discuss the impact of different hyperparameter settings on the attack's performance and the potential for defenses that specifically target the generative model. The authors should also consider the ethical implications of their work and discuss potential mitigation strategies. By addressing these points, the authors can significantly improve the clarity, rigor, and impact of their paper.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
