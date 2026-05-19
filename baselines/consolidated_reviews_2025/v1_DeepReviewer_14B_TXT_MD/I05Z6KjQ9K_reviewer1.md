### Summary

This paper presents a method for performing gradient based attacks on vision-language models (VLMs) in the white-box setting. The key motivation for the attack is to demonstrate the vulnerability of VLMs to adversarial examples, which is an important research problem. The key novelty of the paper is a gradient regularization technique to reduce the variance in gradients during attack optimization. The paper also presents some interesting observations about instability of SOTA attacks and show how gradient regularization helps with it. Overall, the paper is interesting and has the potential to make valuable contributions to the field, but there are some important issues that need to be addressed.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors have done a good job of presenting their work and it is easy to understand their main ideas.
2. The experiments are comprehensive and cover a wide range of models and attack settings. The authors have also provided sufficient details about their experimental setup, which makes it easy to reproduce their results.
3. The proposed method is simple and elegant. The authors have demonstrated that a simple gradient regularization technique can significantly improve the performance of VLMs on adversarial examples, which is a non-trivial result.
4. The authors have also provided some interesting insights into the behavior of VLMs on adversarial examples. For example, they show that VLMs are more vulnerable to adversarial examples when they are prompted with questions that are related to the image content, as opposed to generic questions. This is an interesting finding that could have implications for the design of VLMs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear threat model, which makes it difficult to assess the practical implications of their findings. For example, it is not clear what kind of attacker would be able to generate the kind of adversarial examples presented in this paper, or what kind of defenses could be effective against them. The authors should discuss these issues in more detail in order to make their work more relevant to practitioners.
2. The paper only considers white-box attacks, which may not be realistic in many practical settings. It would be interesting to see if the proposed method can also be used to generate black-box attacks, or if there are other methods that could be more effective in this setting. The authors should also discuss the limitations of their work in terms of its applicability to real-world scenarios.
3. The paper does not provide any insights into how the proposed method could be used to develop more robust VLMs. While the authors show that gradient regularization can improve the performance of VLMs on adversarial examples, they do not discuss how this could be used to design more robust models. This is an important issue that should be addressed in order to make the paper more impactful.

### Suggestions

The authors should clarify the threat model by explicitly stating the attacker's capabilities and goals. For instance, what level of access does the attacker have to the model? Can they access the model's parameters, or only its input and output? What is the attacker's objective? Is it to cause the model to produce a specific output, or simply to cause it to fail? A clear definition of the attacker's capabilities and goals is essential for understanding the practical implications of the attack. Furthermore, the authors should discuss the potential defenses against the proposed attack. For example, are there any input sanitization techniques that could be used to remove the adversarial perturbations? How effective would adversarial training be against these attacks? Addressing these questions would make the work more relevant to practitioners.

To enhance the practical relevance of the work, the authors should explore the possibility of extending their method to black-box settings. While white-box attacks are useful for understanding the vulnerabilities of a model, they are often not realistic in real-world scenarios. A more practical approach would be to develop methods that can generate adversarial examples without requiring access to the model's internal parameters. This could involve techniques such as transfer attacks, where adversarial examples are generated on a surrogate model and then transferred to the target model. The authors should also discuss the limitations of their approach in terms of its applicability to real-world scenarios. For example, how would the attack perform in the presence of noise or other distortions? How robust is the attack to changes in the input format or the model architecture?

Finally, the authors should provide more insights into how their method could be used to develop more robust VLMs. While they show that gradient regularization can improve the performance of VLMs on adversarial examples, they do not discuss how this could be used to design more robust models. For example, could the proposed regularization technique be used as a form of adversarial training? Could the insights gained from the attack be used to develop new defense mechanisms? Addressing these questions would make the paper more impactful and would provide valuable guidance for future research in this area. The authors should also consider exploring the relationship between the proposed attack and other types of attacks, such as those based on semantic perturbations. This would help to better understand the nature of the vulnerabilities of VLMs and to develop more effective defenses.

### Questions

1. The authors claim that Multi-P attack is proportional to the number of prompts. However, this seems counter-intuitive, as adding more prompts should not necessarily make the attack stronger. It would be interesting to see if there is any theoretical justification for this claim.
2. The authors mention that they have tried various methods for enhancing transferability, but do not provide any details about these methods. It would be helpful if they could provide more information about these methods and why they did not work well in their setting.
3. The authors should discuss the limitations of their work in more detail. For example, what are the assumptions that they have made, and how might these assumptions affect the generalizability of their results? What are the potential ethical implications of their work, and how might it be used for malicious purposes?

### Rating

5

### Confidence

4

**********
