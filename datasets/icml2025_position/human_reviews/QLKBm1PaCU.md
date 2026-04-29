## Human Reviewer 1

### Questions
Methods in the DPO series, such as “Knowledge Editing in Language Models via Adapted Direct Preference Optimization”, as well as model merging techniques, can also be exploited to implant attacks. It is recommended to supplement the discussion by considering how these approaches might be leveraged maliciously and to explore potential countermeasures.

Steering techniques can enable lightweight attacks since they are applied only once during the forward propagation—essentially resembling a user-initiated jailbreak. It is recommended to include those methods for discussion.

A key question is whether a unified approach exists that can render the intended behavior non-editable, or if it is necessary to design distinct strategies for different methods. This question can help define a technical roadmap for future defenses. Moreover, one area worth exploring is whether interpretable techniques, such as SAE, can be used to "X-ray" large language models to detect unauthorized edits or malicious modifications.

Multimodal foundation models, such as diffusion models, are also susceptible to editing that may lead to malicious outputs. It is recommended that future discussions consider the unique challenges and potential defenses associated with protecting these models from tampering.

### Rating
5

### Confidence
4

---

## Human Reviewer 2

### Questions
Could you elaborate on how different knowledge editing methods (memory-based, meta-learning, and locate-and-edit) may present varying levels of security risks? Are certain approaches inherently more vulnerable to malicious exploitation than others?

In your security risk assessment, did you find any evidence that specific knowledge editing techniques are more resistant to misuse? If so, could this inform safer design practices?

Have you considered specific evaluation metrics to assess the effectiveness of the countermeasures you propose? What would a comparative evaluation framework look like?

What do you see as the most significant technical challenges in implementing your proposed safeguards, and how might these challenges be addressed in future work?

The paper highlights knowledge editing as a security risk, but similar techniques are also used in machine unlearning to enhance security by removing sensitive or harmful information. Could you clarify how the same methods can both pose risks and serve as safeguards? It would be helpful to see a discussion on this trade-off.

### Rating
3

### Confidence
4

---

## Human Reviewer 3

### Questions
- How can we balance the benefits of open-source LLMs with the need to ensure their security and prevent malicious modifications?
- How can we develop more robust methods for detecting and preventing malicious knowledge editing in LLMs?
- What role should AI developers, policymakers, and end-users play in addressing the risks of malicious knowledge editing?

### Rating
3

### Confidence
3

---

## Human Reviewer 4

### Questions
Q1: What are the specific new perspectives in your opinions on this topic?

Q2: I feel KE is not actually widely used in practice, FTs have even more risks and thus more important?

### Rating
2

### Confidence
5