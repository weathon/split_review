### Summary

This paper proposes a backdoor attack method in federated learning, which designs a generator to generate sample-specific triggers. Experiments are conducted to evaluate the performance.

### Soundness

2 fair

### Presentation

1 poor

### Contribution

2 fair

### Strengths

1. The studied topic is important.
2. The idea of designing a generator to generate sample-specific triggers is interesting.

### Weaknesses

#### Some Related Works

[1] Invisible backdoor attack with sample-specific triggers.
[2] Rethinking Backdoor Attacks.

#### comment

1. The writing is poor. The authors use a large number of notations without any explanation, e.g., $D^{cln}$, $D^{bd}$, $D_{cln}$, $D_{bd}$, $\eta$, $f$, $g_\xi$, $\theta$, $\xi$, $\epsilon$, etc. Although some of them are explained in the appendix, the writing is still very hard to read.

2. The novelty is limited. The idea of designing a generator to generate sample-specific triggers has been studied in [1]. The difference between the proposed method and [1] is not discussed.

3. The authors do not provide the results of benign accuracy. In backdoor attacks, it is important to keep the benign accuracy unchanged while achieving a high backdoor accuracy. "One of the primary goals of a backdoor attack is to ensure that the backdoored model performs well on benign samples" [2].

4. The authors do not compare with SOTA backdoor attacks, e.g., [1,2]. It is unclear whether the proposed method outperforms SOTA attacks or not.

### Suggestions

The paper needs significant improvement in clarity and technical depth. The use of numerous undefined notations makes it extremely difficult to follow the methodology. For instance, the sets $D^{cln}$ and $D^{bd}$ are introduced without specifying whether they represent datasets, distributions, or something else entirely. Similarly, the variables $\eta$, $f$, $g_\xi$, $\theta$, $\xi$, and $\epsilon$ are used without clear definitions of their roles and relationships. A rigorous definition of each symbol, including its type (e.g., scalar, vector, function, dataset) and its purpose within the proposed framework, is crucial for the paper to be understandable. Furthermore, the authors should provide a clear explanation of how these notations relate to the federated learning setting and the backdoor attack mechanism. Without this, the paper is essentially unreadable.

Regarding novelty, the authors need to clearly articulate how their approach differs from existing methods, particularly those employing generative models for trigger creation. The paper should include a detailed comparison with [1], highlighting the specific technical differences in the trigger generation process, the attack strategy, and the evaluation methodology. A simple statement that the proposed method is different is insufficient; the authors must provide a rigorous analysis of the differences. For example, are the triggers generated in a different space (e.g., pixel space vs. feature space)? Does the proposed method use a different optimization strategy? Does the proposed method have different assumptions about the federated learning environment? These are the types of questions that need to be addressed to establish the novelty of the work. The lack of such a comparison makes it impossible to assess the contribution of this paper.

Finally, the evaluation of the proposed method is incomplete. The authors must include results for benign accuracy alongside backdoor accuracy. It is essential to demonstrate that the backdoor attack does not significantly degrade the performance of the model on clean data. The paper should also compare the proposed method with state-of-the-art backdoor attacks, such as those described in [1,2], to demonstrate its effectiveness. This comparison should include a detailed analysis of the performance of each method in terms of both backdoor accuracy and benign accuracy, under various experimental settings. Without these comparisons, it is impossible to determine whether the proposed method is a significant advancement over existing techniques. The authors should also consider including ablation studies to analyze the impact of different components of their method.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
