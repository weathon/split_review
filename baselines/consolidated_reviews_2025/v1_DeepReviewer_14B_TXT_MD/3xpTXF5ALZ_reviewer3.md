### Summary

The paper proposes a novel method for localizing phishing attacks in emails. The method uses a deep learning-based approach to not only predict whether an email is a phishing attempt but also to identify the specific sentences that are most relevant to the phishing content. The approach is based on an information theory perspective and aims to improve the explainability of phishing detection systems. The authors evaluate their method on seven real-world email datasets and compare it to several state-of-the-art interpretable machine learning approaches.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses an important problem in cybersecurity, which is the detection and explanation of phishing attacks. Phishing remains a significant threat, and methods that can provide both accurate detection and clear explanations are valuable.

2. The proposed method is based on a solid theoretical foundation, using information theory and the information bottleneck principle. This provides a good rationale for the approach.

3. The paper evaluates the method on seven diverse real-world email datasets, which is a strength. This suggests that the method is robust and can handle different types of email data.

4. The authors introduce new metrics for evaluating the performance of phishing attack localization methods, which is a contribution to the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not adequately discuss the limitations of the proposed method. For example, how does the method perform on very long emails or emails with complex structures? Are there any types of phishing attacks that the method is particularly bad at detecting? The paper should include a more thorough analysis of the method's failure modes, including specific examples of emails where the method struggles to identify the phishing content. This should include a discussion of the types of linguistic or structural features that might hinder the method's performance.

2. The paper does not provide enough detail on the implementation of the method. For example, what specific neural network architecture is used? What are the hyperparameters? How is the training data prepared? The lack of detail makes it difficult to reproduce the results. The paper should include a detailed description of the neural network architecture, including the number of layers, the type of activation functions, and the size of the hidden layers. The paper should also specify the optimization algorithm, the learning rate, and other relevant hyperparameters. Furthermore, the paper should describe the data preprocessing steps, including how the emails are tokenized, how the sentences are represented, and how the labels are assigned.

3. The paper does not adequately compare the proposed method to existing phishing detection methods. While the authors compare to some interpretable machine learning approaches, they do not compare to other state-of-the-art phishing detection methods. A more comprehensive comparison would help to put the performance of the proposed method into context. The comparison should include a range of methods, including both traditional machine learning approaches and deep learning-based approaches. The comparison should also include a discussion of the strengths and weaknesses of each method, as well as a quantitative comparison of their performance on the same datasets.

4. The paper does not discuss the computational cost of the proposed method. How long does it take to train the model? How long does it take to make a prediction on a new email? This is an important consideration for practical applications. The paper should include a detailed analysis of the computational complexity of the method, including the time and memory requirements for both training and inference. This analysis should be performed on a range of hardware configurations to provide a realistic assessment of the method's practicality.

5. The paper does not discuss the potential for adversarial attacks on the proposed method. Could an attacker craft an email that is designed to fool the method? This is an important security consideration. The paper should include a discussion of the potential vulnerabilities of the method to adversarial attacks, as well as potential strategies for mitigating these vulnerabilities. This should include an analysis of the types of perturbations that could be used to fool the method, and a discussion of how the method could be made more robust to such attacks.

### Suggestions

The paper would benefit from a more detailed analysis of the method's limitations, particularly regarding its performance on complex emails. The authors should investigate how the method handles emails with long sentences, nested structures, or non-standard formatting. They should also explore the method's sensitivity to different types of phishing attacks, such as those that rely on subtle manipulation of language or those that use social engineering tactics. A more thorough analysis of the method's failure modes, including specific examples of emails where the method struggles, would provide valuable insights into its strengths and weaknesses. This analysis should also include a discussion of the types of linguistic or structural features that might hinder the method's performance, such as the use of jargon, ambiguous language, or unusual sentence structures. Furthermore, the authors should consider incorporating techniques to handle these challenging cases, such as using attention mechanisms to focus on the most relevant parts of the email or employing more sophisticated sentence representation methods.

To improve the reproducibility of the results, the authors should provide a detailed description of the neural network architecture, including the number of layers, the type of activation functions, and the size of the hidden layers. They should also specify the optimization algorithm, the learning rate, and other relevant hyperparameters. Furthermore, the paper should describe the data preprocessing steps, including how the emails are tokenized, how the sentences are represented, and how the labels are assigned. The authors should also provide details on the training procedure, including the batch size, the number of epochs, and the validation strategy. This level of detail is essential for other researchers to replicate the results and build upon the proposed method. Additionally, the authors should consider releasing the code and data used in the experiments to further enhance reproducibility and facilitate future research.

The paper should include a more comprehensive comparison to existing phishing detection methods, including both traditional machine learning approaches and deep learning-based approaches. The comparison should include a quantitative analysis of the performance of each method on the same datasets, as well as a discussion of the strengths and weaknesses of each method. The authors should also consider comparing their method to other interpretable machine learning approaches, to better understand the trade-offs between interpretability and performance. This comparison should be performed on a range of datasets, including those with different characteristics, to provide a more robust assessment of the method's performance. Furthermore, the authors should discuss the computational cost of each method, including the time and memory requirements for both training and inference. This analysis should be performed on a range of hardware configurations to provide a realistic assessment of the method's practicality.

### Questions

1. Can you provide more details on the implementation of the method, including the neural network architecture and hyperparameters?

2. How does the method perform on very long emails or emails with complex structures?

3. How does the method compare to other state-of-the-art phishing detection methods?

4. What is the computational cost of the method?

5. How robust is the method to adversarial attacks?

### Rating

3

### Confidence

4

**********
