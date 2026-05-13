# What's New in My Data? Novelty Exploration via Contrastive Generation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Fine-tuning is widely used to adapt language models for specific goals, often leveraging real-world data such as patient records, customer-service interactions, or web content in languages not covered in pre-training.
These datasets are typically massive, noisy, and often confidential, making their direct inspection challenging.
However, understanding them is essential for guiding model deployment and informing decisions about data cleaning or suppressing any harmful behaviors learned during fine-tuning.
In this study, we introduce the task of novelty discovery through generation, which aims to identify novel domains of a fine-tuning dataset by generating examples that illustrate these properties.
Our approach － Contrastive Generative Exploration (CGE) － assumes no direct access to the data but instead relies on a pre-trained model and the same model after fine-tuning.
By contrasting the predictions of these two models, CGE can generate examples that highlight novel domains of the fine-tuning data.
However, this simple approach may produce examples that are too similar to one another, failing to capture the full range of novel domains present in the dataset.
We address this by introducing an iterative version of CGE, where the previously generated examples are used to update the pre-trained model, and this updated model is then contrasted with the fully fine-tuned model to generate the next example, promoting diversity in the generated outputs.
Our experiments demonstrate the effectiveness of CGE in detecting novel domains, such as toxic language, as well as new natural and programming languages.
Furthermore, we show that CGE remains effective even when models are fine-tuned using differential privacy techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers a novel task of finding what is new in a fine-tuning dataset, given the fact that we have a pre-trained model, but it is unclear what the distribution of data was for the same. In particular, they introduce Contrastive Generative Exploration or CGE, which tries to find novel properties which are unique to the fine-tuning data. This basically leverages the difference in predictions between the pre-trained model and the model fine-tuned on the new dataset, and appropriately generates new sentences. Using this metric itself of new probability scoring, they are able to get much higher true positive rates of detecting novel content. At the same time, they are also able to generate novel sentences. The work discusses two different methods of CGE, one which is iterative and one which is static, and do experiments on non-English languages or toxic text or code data to find novel content. Finally, there is also a section in the paper that talks about how this can work with differential privacy as well, and in scenarios when we do not have access to visualizing the true data.

### Strengths
- Shifting Focus from Data Inspection to Model Behavior: This is a neat transition because direct data access is often restricted due to privacy concerns or the sheer scale of the datasets involved. CGE, therefore, offers a practical and potentially more scalable solution for understanding novelties in fine-tuning data.
- Contrastive Decoding for Dataset Exploration: This technique, originally developed for controlling text generation properties, is cleverly adapted to distinguish between in-distribution and novel examples by contrasting the predictions of pre-trained and fine-tuned models. 
- Synergy with Differentially Private fine-tuning: In line with the first goal of exploring datasets novelties without direct access to them, the paper does a good job at showing how a model fine-tuned with DP can still allow inspection of properties of the dataset it was trained on by looking at the induced model behaviors.
- High AUC with metric: The new metric of detecting novel content achieves substantially better performance than most existing metrics.

### Weaknesses
 - Missing an honest baseline like n-gram: This paper misses basic baselines such as n-gram distribution change, or top-k nearest neighbour distance in the embedding space.
   - This could quite naturally be done in the RPJ experiments.
   - Can also be adapted in the DP-SGD experiments by returning privatized n-gram stats.
   - You might like the infini-gram paper as a tool to enable such analysis
- Constraint: The paper writes that one of the constraints for the method to work effectively is that the number of novel examples substantially smaller than the remaining examples in the fine-tuning data. This is a very hard-to-match constraint in my opinion
- No axis labels on graphs 2,3
- No samples shown:

### Questions
- Can you think of adapting this metric to measure the distance between two distributions?
- I would like to view CDE generated samples

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors introduce to discover through generation, which aims to identify properties in a fine-tuning dataset without directly accessing the fine-tuning data. They propose the Contrastive Generative Exploration (CGE) to fine-tune datasets by generating examples that represent these properties.

### Strengths
1. The experimental setting are soild. They conduct experiments on multiple base LLM and mulitple datasets. The authors report the experimental results on multiple evaluation metrics.

2. To achieve contrastive generative exploration, the methods consists of static approach, iterative approach, and so on. The design of methods seem reasonable.

3. The task (direction) this paper focusing on sounds interesting. Achieve a indirect and effective tine-tuning is curical in LLM and generalized methods can be widely-used in many LLM scenarios.

### Weaknesses
1. The baseline methods are kind of old and weak. It would be better to compare methods proposed in 2023 or 2024, but the baselines used in this submission are proposed before 2021.

2. To compare with DP-based methods, the stardard setting is to compare over different \epsilon instead of the noise multiplier. \epsilon indicates the strength of the privacy protection but noise multiplier is not so clear to show the privacy protection performance since the scale of noises varies in different models.

3. The source code should be public accessible.

4. It is better to bold the best results in Table1. From the experimental results shown in Tables 1, the proposed model cannot always outperform the baselines' results. More detailed and insightful explanations are required.

### Questions
Will the authors release the code?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a method based on contrastive learning that can generate examples from classes that are in the fine tuning set that are not in the pre-training set. The authors' experiments involves evaluating GradNorm and various proposed probabilities methods on OpenLLaMA and Falcon-RW.

### Strengths
- Identifying what kind of examples in the fine-tuning set that are not present in the pretraining set is interesting.

### Weaknesses
 - The writing is poor, and the story and motivation are vague and confusing. The authors keep switching between writing "novelty exploration", "novel characteristics", and "novel domains" which makes it difficult to understand what the actual task is. After much digging, this work is basically about identifying example classes that are in the fine-tuning set and not in the pretraining set. Perhaps the title could be, "identifying new classes in the finetuning set".

- It is not clear what the goal of this work is in terms of the benefits of identifying new classes in the fine-tuning set. The introduction mentions that this capability would allow us to remove toxic values, but how would the model know the new classes are "toxic"?

- There are so many trivial ways to identify whether the model knows whether a certain type of examples were in the pretraining set. What if you simply compute the uncertainty or the entropy of the model output on the examples, and identify those with the highest entropy? those are most likely examples that the model hasn't seen.

### Questions
Could you address the weaknesses above?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method called Constrastive Egneration Exploration(CGE) and its interative version, which aims to capture novel characteristics of fine-tuning data. Since fine-tuning data might be confidential sometime, this work are something trying to generate examples that similar to fine-tuning data. More specificlly, by using probability of fine-tuned models minus probability of pre-trained models (called Contrastive Score), it apply contrastive decoding to generate examples. Experiments results show contrasrtive score is able to robustly identify such ood examples, and

### Strengths
1. The question itself seems new. Though using so called contrastive score (difference between two model's probability) to identify some ood texts is not something new, but successfully using it to somehow identify/recover part of fine-tuning datasets is intertesing.
2. It might be interesting to see whether this can be used as an attack method to recover some confidential fine-tuning data (given known pretrained model and fine-tune model.

### Weaknesses
1. The application of this question seems limited, because for real-world cases, i.e. confidential fine-tuning datasets, we might not know which pre-train model they are using. Also we may not be able to access the probability of fine-tuned model.
2. Experiments are limited and not so solid. Consider authors are using only two models on two different settings. (1) it is better to do controlled experiments. When you change to a new experimental setting, you can keep the model and other things unchanged. (2) The number of ood-domain is limited.
3. Writing about evaluation on novel examples is not clear.

### Questions
1. For the iterative version, how to make sure you fine-tune the pre-trained model on generated text can produce a new model with appropreate distribution. i.e. for the first iteration, the distribution of pre-trained model has no problem, and you identify and generate some  Japanese text. However, when you fine-tune on Japanese task, it is possible Japanese text will dominent the distribution and English/Russian will be "novel character" and it is possible to generate English again. 
2. The evaluation process for different domains (i.e. Non-English and toxic) is not clear. Which domain is chosen as the ground truth for first iteration? How the accuracy is calculated based on the 100 generated texts? They are not clearly stated.

### Soundness
3

### Presentation
2

### Contribution
2
