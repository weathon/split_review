### Summary

This paper proposes AI2TALE, a new learning framework to localize phishing attacks in email content. The proposed method is based on a selector network and a classifier network. The selector network selects the most important sentences in the email, which are then used by the classifier network to predict the phishing label. The two networks are jointly trained with two loss functions, with the goal of maximizing the mutual information between the selected sentences and the phishing label, while minimizing the mutual information between the selected and all original sentences. This is intended to select the minimal subset of sentences that maximally contribute to the phishing label. Two intrinsic interpretable models are used as baselines, and the proposed method outperforms them in terms of label-accuracy and cognitive-true-positive rate. A human study with 25 participants shows that the top-1 selected sentences are perceived as affecting users’ decision to follow the instructions in the email.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

* Phishing attack localization is an interesting problem, and this work proposes a new approach to the problem.
* The human study results show that the selected sentences can affect users’ decision to follow the instructions in the email.

### Weaknesses

#### Some Related Works


#### comment

 * The paper is difficult to follow. It provides a good high-level idea of the proposed method, but the discussion on mutual information and Gumbel-Softmax is hard to follow, and it is not clear what the concrete implementation details are.
* The paper lacks a clear description of how the proposed method is applied to the email dataset, and it is not clear how the input is prepared for the model.
* The paper does not provide a clear justification for the use of multi-Bernoulli distribution for sentence selection, and it is not clear why this is the most appropriate choice.
* The paper does not provide sufficient details on the human study, including the study protocol and how the results demonstrate the validity of the proposed method.
* The paper does not provide a clear explanation of the cognitive-true-positive rate metric, and it is not clear how this metric is calculated or why it is an appropriate measure of performance.
* The paper does not provide sufficient details on the baselines, including the specific models used and how they were adapted to the phishing localization task.
* The paper does not provide a clear explanation of how the selected sentences are used to predict the phishing label, and it is not clear how the top-k sentences are determined or why this is the appropriate approach.
* The paper does not provide a clear explanation of how the top-1 selected sentence is used to predict the phishing label, and it is not clear how this is done or why this is an appropriate approach.
* The paper does not provide a clear explanation of how the human study results support the claim that the selected sentences are meaningful to users, and it is not clear how the study was designed to ensure objectivity.

### Suggestions

The paper needs to provide a more detailed explanation of the implementation details of the proposed method. Specifically, the authors should provide a clear description of how the selector and classifier networks are implemented, including the specific architectures used and the activation functions. The paper should also provide a clear explanation of how the mutual information loss is calculated and how the Gumbel-Softmax trick is used to sample from the Bernoulli distribution. Furthermore, the paper should provide a clear explanation of how the input email data is preprocessed and prepared for the model, including the specific steps used to convert the email text into a format that can be used by the model. This should include details on the embedding layer and how it handles the variable length of emails. The paper should also provide a clear explanation of how the model handles the structural information of emails, such as the header and body, and whether this information is used to improve the performance of the model.

The paper should provide a more detailed justification for the use of the multi-Bernoulli distribution for sentence selection. The authors should explain why this distribution is the most appropriate choice for this task and what the advantages of using this distribution are compared to other alternatives. The paper should also provide a more detailed explanation of the human study, including the specific questions that were asked to the participants and how the responses were analyzed. The authors should also provide a clear explanation of how the study was designed to ensure objectivity and to minimize potential biases. The paper should also provide a clear explanation of the cognitive-true-positive rate metric, including the specific formula used to calculate this metric and why this is an appropriate measure of performance. The authors should also provide a clear explanation of how the selected sentences are used to predict the phishing label, including the specific steps used to combine the selected sentences into a final prediction.

Finally, the paper should provide a more detailed explanation of how the top-k sentences are determined and why this is the appropriate approach. The authors should explain how the importance scores are calculated and how they are used to select the top-k sentences. The paper should also provide a clear explanation of how the top-1 selected sentence is used to predict the phishing label, including the specific steps used to make this prediction. The authors should also provide a more detailed explanation of how the human study results support the claim that the selected sentences are meaningful to users. The paper should provide a clear explanation of how the study was designed to ensure that the participants were not primed to give certain responses and how the results demonstrate the validity of the proposed method. The paper should also provide a more detailed explanation of the baselines, including the specific models used and how they were adapted to the phishing localization task.

### Questions

* How is the proposed method applied to the email dataset? How is the input prepared for the model?
* What is the multi-Bernoulli distribution and why is it used to model the sentence selection process? Is this the most appropriate distribution to use for this task?
* How are the parameters of the selector model learned? How is the network trained to output high values for the most important sentences?
* What is the human study protocol? How do the results demonstrate the proposed method is valid?
* What is the cognitive-true-positive rate metric? How is this calculated?
* What are the baselines used in the experiments? How are they applied to the phishing localization task?
* How are the top-k sentences used to predict the phishing label? How is the top-1 selected sentence used to predict the phishing label?
* How do the human study results support the claim that the selected sentences are meaningful to users? How was the study designed to ensure objectivity?

### Rating

3

### Confidence

3

**********
