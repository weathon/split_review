# Dual Prompt Tuning for Domain-Aware Federated Learning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Federated learning is a distributed machine learning paradigm that allows multiple clients to collaboratively train a shared model with their local data. Nonetheless, conventional federated learning algorithms often struggle to generalize well due to the ubiquitous domain shift across clients. In this work, we consider a challenging yet realistic federated learning scenario where the training data of each client originates from different domains. We address the challenges of domain shift by leveraging the technique of prompt learning, and propose a novel method called Federated Dual Prompt Tuning (Fed-DPT). Specifically, Fed-DPT employs a pre-trained vision-language model and then applies both visual and textual prompt tuning to facilitate domain adaptation over decentralized data. Extensive experiments of Fed-DPT demonstrate its significant effectiveness in domain-aware federated learning. With a pre-trained CLIP model (ViT-Base as image encoder), the proposed Fed-DPT attains 68.4% average accuracy over six domains in the DomainNet dataset, which improves the original CLIP by a large margin of 14.8%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed Fed-DPT, a prompt learning-based technique to efficiently utilize the pre-trained vision-language model to mitigate the domain difference challenge in federated learning. Specifically, the participants of the FL system would locally optimize both language prompt and soft prompt for image encoding, and the server would aggregate these prompts and send them back to the clients. The experiments on several benchmark datasets show the performance of the Fed-DPT compared to the baselines.

### Strengths
1. The prompt tuning is lightweight and efficient for local training.

2. The target problem is novel and practical. Most of the FL literature are targeting on the non-iidness of the label distribution, but this paper concentrates on the domain difference of the local dataset, which is more challenging and practical in wild FL applications.

3. Compared to previous work such as PromptFL, Fed-DPT took both language and vision prompt into consideration.

### Weaknesses
1. For the textual prompt design and aggregation, would each client know the detailed information of the other's domain? As the setup in the experiment part, each client would only have one domain of images under extreme non-iidness, which means that the client would only know the domain name of its own. However, as each client needs to send its textual prompt to each other, each participant would know the detailed domain information about others, which is a privacy leakage.

2. As the paper concentrates on using the pre-trained vision-language model, the application scenario is limited to the cross-silo setups. The CLIP model is not practical to deploy in the cross-device FL setup.

### Questions
1. In the experiment part, why does the author not consider using the FedAvg/FedProx to directly fine-tune the CLIP model as the baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Prompt learning is utilized to address the challenge of domain shift of training data between different clients. A novel approach called Federal Dual Prompt Tuning (Fed-DPT) is proposed, which uses pre-trained visual language models combined with text and image data. The experimental results demonstrate the effectiveness of the method.

### Strengths
1. Prompt learning is introduced into federated learning for solving the problem of domain transfer between clients.

2. The experimental results show that the method can improve the performance compared to the state-of-the-art methods under certain experimental settings.

### Weaknesses
1. The contributions need to be more clearly described. The combination of prompt learning and federated learning is a means of enhancing the effectiveness of the experiments. It lacks of innovation.

2. It is recommended to combine Figures 1 and 2, and draw a framework. And it’s better to list the whole algorithm. At present the overall process is not very clear.

3. At the end of subsection 4.2, it is mentioned that this paper does not observe the problem of training crash. It is just a summary of the observation from the experimental view, whether it is possible to make a theoretical analysis of the algorithm in terms of convergence or generalization bounds, etc.

### Questions
1. It is mentioned that some text information needs to be shared between clients such as class names, does it involve privacy protection?

2. In the section of experimental results, the performance is greatly improved on DomainNet dataset. It is suggested to analyze the reasons.

3.  The results of the ablation experiments show that the federated frameworks and textual cues are key factors for improving the effectiveness of the experiments. While the domain-aware mechanism slightly improves the performance. It’s better to give a more detailed reason.

4. Prompt learning is also adopted in "Efficient Model Personalization in Federated Learning via Client-Specific Prompt Generation" in ICCV2023. What is the difference between the proposed and the ICCV2023 methods, and it is suggested to add a comparison with this method in the experimental section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a prompt tuning-based FL method that solves the domain shift problem in FL. Based on pre-trained vision-language model, both visual and textual prompt tuning strategies are utilized to facilitate domain adaptation. Experiments on CLIP model and benchmark datasets are conducted to show the performance enhancement achieved by Fed-DPT.

### Strengths
1. This paper has a unique contribution to the FL community by investigating the utilization of prompt tuning in dealing with domain shift problems. 

2. A specific prompt tuning-based mechanism is developed under the FL framework and shows promising results compared with conventional FL methods and vision–language tuning FL methods.

### Weaknesses
1. It seems that the proposed Fed-DPT can only be applied to the vision-language model-based federated learning scenarios. Considering that there is a wide range of model architectures along with the domain shift problems, a more general method is preferred. 

2. The novelty of textual prompt tuning and visual prompt tuning is limited. Since these two prompt tuning schemes were not first proposed by this paper, it is better to demonstrate the unique contributions of the prompt tuning part. 

3. It is still implicit why the visual prompts can help detect the correlation between an input image and the domains and how this can help alleviate the domain shift problem. 

4. It is better to also provide a comparison between the proposed method and traditional FL methods that address domain shift problems, such as FedBN[1] and some SOTA personalzied FL methods.

[1] FedBN: Federated Learning on Non-IID Features via Local Batch Normalization

### Questions
Will there be any privacy concerns when optimizing the prompts in an FL manner?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
