### Summary

This paper of interest to the ICLR community studies a new attack surface about the availability of large vision-language models (VLMs) such as GPT-4. Specifically, the authors investigate the scenario that attackers maliciously induce high energy consumption and latency time (energy-latency cost) during inference of VLMs. To achieve the goal, the authors propose verbose images to craft an imperceptible perturbation to induce VLMs to generate long sentences during inference. Experimental results are provided to validate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. This paper is well written.
2. The proposed approach is simple and effective.
3. Extensive experiments demonstrate the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. Energy consumption and latency time have been studied in prior work. What is the novelty in this paper?
2. Do the energy consumption and latency time remain high for the verbose images once the VLMs are fine-tuned?
3. What is the attack success rate of the proposed method? How does the success rate change with different perturbation budgets?
4. Is the proposed method robust against possible defenses?
5. What is the impact of the proposed attack in real-world scenarios?

### Suggestions

The paper introduces an interesting concept of using verbose images to increase the computational cost of vision-language models (VLMs). However, several aspects require further investigation. First, while the paper demonstrates an increase in energy consumption and latency, it does not adequately address the practical implications of this attack. Specifically, the paper should explore the feasibility of generating these verbose images in a real-world setting, considering the computational resources required for the optimization process. The authors should provide a detailed analysis of the time and resources needed to generate these adversarial examples, and whether this process could be realistically deployed by an attacker. Furthermore, the paper should discuss the potential for detection and mitigation of these verbose images, such as through input sanitization or model hardening techniques. A more thorough analysis of the attack's robustness against common defense mechanisms is needed to assess its practical threat.

Second, the paper should delve deeper into the relationship between the perturbation budget and the attack's effectiveness. While the authors show that a larger perturbation budget leads to longer generated sequences, they do not explore the trade-off between the attack's success and the perceptibility of the perturbation. It is crucial to understand the minimum perturbation required to achieve a significant increase in energy consumption and latency, as this would determine the attack's stealthiness. The paper should also investigate the impact of different types of perturbations, such as those that are more semantically meaningful or those that are more difficult to detect. A more comprehensive analysis of the perturbation space is needed to fully understand the attack's capabilities and limitations. Additionally, the paper should explore the generalizability of the proposed method across different VLM architectures and datasets, as the current evaluation is limited to a few specific models.

Finally, the paper needs to provide a more concrete analysis of the real-world impact of this attack. While the authors mention the potential for resource exhaustion, they do not provide specific examples of how this could manifest in practice. For instance, how would this attack affect a cloud-based VLM service? What are the potential economic costs associated with this attack? The paper should also discuss the ethical implications of this research, particularly the potential for misuse of this technology. A more thorough discussion of the societal impact of this work is needed to justify its contribution and ensure its responsible development. The authors should also consider the potential for this attack to be used in conjunction with other attacks, and how this could amplify its impact.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
