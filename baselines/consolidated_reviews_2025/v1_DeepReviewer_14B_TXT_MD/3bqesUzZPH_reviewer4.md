### Summary

The paper proposes a new backdoor attack against federated learning. The key idea is to use a generative model to generate a sample-specific trigger. The proposed attack is stealthy, flexible, and adaptive. Extensive experiments are conducted to demonstrate the effectiveness of the proposed attack.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. 
2. The idea of using a generative model to generate sample-specific triggers is novel and interesting. 
3. The proposed attack is stealthy, flexible, and adaptive. 
4. The experimental results are promising.

### Weaknesses

#### Some Related Works

[1] Panda: A practical backdoor attack against federated learning.
[2] Backdoor attacks to federated learning using poison the well.

#### comment

1. The proposed attack requires a large number of local iterations to converge, which may not be practical in some scenarios. 
2. The proposed attack requires a large number of local data to train the generative neural network, which may not be available in some scenarios. 
3. The proposed attack may not be effective against some advanced defenses, such as anomaly detection and backdoor detection. 
4. The paper lacks a comparison with other state-of-the-art backdoor attacks in federated learning, such as Panda [1] and Poison the Well [2]. It is unclear how the proposed attack compares to these existing attacks in terms of effectiveness and stealthiness.

### Suggestions

The paper introduces an interesting approach using generative models for backdoor attacks in federated learning. However, several aspects could be improved to strengthen the paper's contributions. First, the practical limitations of the proposed attack need to be addressed more thoroughly. While the authors claim the attack converges quickly, the number of local iterations required for convergence should be explicitly stated and compared against other attacks. Furthermore, the computational cost of training the generative model on local devices should be analyzed, especially considering the resource constraints often present in federated learning scenarios. It would be beneficial to provide a detailed analysis of the trade-off between attack effectiveness and computational overhead, including the impact of different generative model architectures and training parameters. This analysis should also consider the impact of varying dataset sizes and model complexities on the convergence speed and overall attack performance.

Second, the paper should include a more comprehensive evaluation of the attack's robustness against various defense mechanisms. While the authors mention anomaly detection and backdoor detection, a more detailed analysis of specific defense strategies is needed. For example, the paper could evaluate the attack's performance against gradient clipping, which is a common defense against adversarial attacks. Additionally, the paper should explore the attack's resilience against more advanced backdoor detection techniques, such as those based on model behavior analysis or input sanitization. A thorough evaluation of these defenses would provide a more complete picture of the attack's limitations and potential vulnerabilities. Furthermore, the paper should discuss potential countermeasures that could be employed to mitigate the proposed attack, such as techniques for detecting and filtering out malicious updates.

Finally, the paper needs a more detailed comparison with existing state-of-the-art backdoor attacks in federated learning. The current comparison is limited, and it is unclear how the proposed attack compares to other attacks in terms of stealthiness and effectiveness. A more thorough comparison should include a quantitative analysis of the attack success rate, the impact on benign accuracy, and the computational cost. The paper should also discuss the advantages and disadvantages of the proposed attack compared to other attacks, highlighting the specific scenarios where the proposed attack is most effective. This comparison should also consider the assumptions made by each attack, such as the attacker's knowledge of the global model or the ability to control a subset of clients. A more comprehensive comparison would help to better position the proposed attack within the existing literature and highlight its unique contributions.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
