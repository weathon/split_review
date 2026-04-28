# FedBiOT: a solution for federated large language model fine-tuning with intellectual property protection

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Due to data and information privacy concerns, data owners are not willing to share the data with others, but each of them may not have sufficient data to fine-tune a satisfactory large language model (LLM) individually. Parallelly, the LLM owners may not be willing to disclose the LLMs' details, including their architectures and parameters. Therefore, this leads to the challenge of fine-tuning an LLM on a federated learning task where the clients with task-specific data cannot obtain the complete LLM. To solve the challenge, this paper introduces FedBiOT, a method that guarantees the clients' data privacy and avoids the disclosure of an LLM. Specifically, we formulate and solve a bi-level optimization problem to ensure that the emulator distilled on the public dataset by the LLM owner can help the adaptors' local fine-tuning on clients' private datasets, regardless of the distribution drift between those datasets. Different clients' adapters are synchronized in a federated learning style, and the full model composed with the final derived adapter can achieve better performance on downstream tasks. We conduct extensive experiments on LLaMA-7B training for various federated learning tasks and witness significant improvements over existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes improvements to offsite tuning, a pre-existing large-scale federated learning model's partial tuning method. It is built upon the existing approach of offsite tuning, which involves splitting a transformer model into various sub-models by layer index, such as adapters and emulators. During FL training, clients receive a combination of adapters and emulators, with the emulator being frozen while the adapter is fine-tuned. This paper makes two key improvements. First, it selects the last few transformer layers as the adapter. Second, it introduces a public dataset on the server and reduces the KL divergence between the adapter-emulator and full model outputs through knowledge distillation.

### Strengths
1.	The paper is built upon a relatively recent work so that it may offer modern insights into the related research fields.

2.	Experimental results support the proposed improvements in the paper.

3.	The proposed improvements in the paper are general and should be easy to adopt.

### Weaknesses
1.	From a technical perspective, the two improvements proposed in the article may be incremental. One involves changing the index of the fine-tuning layers (based on observation), and the other relies on the traditional distillation method. Both methods are essentially at the level of tricks and are insufficient to serve as contributions to the paper. Specifically, the selection of the last few transformer layers as the adapter, while empirically effective, lacks a strong theoretical justification. Similarly, using KL divergence for knowledge distillation is a well-established technique, and its application here does not introduce significant novelty. The paper does not explore alternative distillation methods or provide a comparative analysis to justify the choice of KL divergence.

2.	I have doubts about the "intellectual property protection" aspect of the paper. In this framework, although local clients can only obtain a portion of the model instead of the entire model, this sub-model can still be fine-tuned and used for inference, which implies that the majority of the model's functionality has been preserved. Essentially, malicious users can still steal this intellectual property. This framework does not seem to provide significant protection, so I do not consider the "intellectual property protection" mentioned in the title appropriate. The concern is that the fine-tuned adapter, even if a smaller portion of the overall model, might still encapsulate a substantial amount of the original model's knowledge and capabilities, making it a potential target for intellectual property theft. The paper needs to more rigorously demonstrate the limitations of the extracted adapter in replicating the full model's performance, especially in scenarios where the attacker has access to a large amount of data for fine-tuning.

3.	The paper should provide a detailed algorithm to help readers follow.

### Questions
Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces FedBiOT, a method that guarantees the clients’ data privacy and avoids the disclosure of an LLM. The authors conduct extensive experiments on LLaMA-7B training for various federated learning tasks and witness significant improvements over existing baselines.

### Strengths
The topic is timely and interesting.

### Weaknesses
1. The experimental evaluation was only implemented in LLaMA-7B. How does it work on other mainstream models such as ChatGPT2?
2. In the experiment, federated learning only considered 8 clients. There is a lack of experiments that vary the number of clients and the number of training samples each client own.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

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
This paper considers a relatively new setting: federated learning over large language models. There are two key considerations of this paper: limited computation resource of clients and intellectual property of server's full LLM. Based on these motivations, this paper proposes an FL algorithm FedBiOT, which trains adapter and emulator in a bi-level optimization manner. Experiments on three datasets shoe the effectiveness of FedBiOT by comparing with two baselines.

### Strengths
- This paper considers a relatively new setting in federated learning and large language models.
- This paper proposes a new FL algorithm FedBiOT, which trains adapter over emulator to achieve parameter-efficient tuning.
- Experiments show the effectiveness of FedBiOT by comparing with two baselines.

### Weaknesses
 - The contributions need to be clarified. For me, I think the topic of this paper is interesting and worth exploring. However, it is not so clear what are the main contributions of this paper since previous work [1] has considered such setting and proposed FedOT (federated learning with offsite-tuning). Are the main contributions lying on improving FedOT via a bi-level optimization approach?
- The motivations need to be further clarified. This paper claims that the clients cannot obtain the full model due to intellectual property of LLM. However, I wonder if such claim still holds after the release of Llama2.
- Some meaningful experiments are missing.
  - Some experiments for reference. It would be more helpful if the authors can provide the results when clients can obtain the full model, such that we could see how large the gap is.
  - Computation resources comparisons. This method requires more training resources (e.g., more training steps) compared to baselines. However, this paper does not show such comparisons, which would promote readers' understanding.
- Some confusions:
  - "Improvement 1" at page 5. What are the definations of bottom / first / last layers. Suggest consistent expressions like first / last.

Currently, my rating is between 5 and 6. I would consider re-rating if the authors can address the above concerns.

### Questions
- According to this sentence "We apply offsite-tuning with one single client, where all data are loaded to the client.", it seems like the Offsite-tuning is training over the gathered dataset of all clients. But why its performance is quite low? Please describe how you implement offsite-tuning with more details.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Due to privacy concerns, data owners and large language model (LLM) owners are reluctant to share data and models. This paper proposes FedBiOT, a method that ensures data privacy while enabling fine-tuning of LLMs on federated learning tasks. It formulates and solves a bi-level optimization problem to distill an emulator on a public dataset that can support local fine-tuning on private datasets without disclosing the LLM.

### Strengths
1. The combination of LLM and federated learning is interesting.
2. The problem formulation is well presented.
3. The layer selection and dropout mechanism is interesting.

### Weaknesses
However, there are some improvements for the paper:
1. The number of clients is very small. In section 4.1, the number of clients is 4, which is relatively very small compared with that in real FL settings.
2. The idea is straightforward, which is presented in existing works, e.g., Yosinski et al., 2014.
3. The selection of dropout rate is not well elaborated. 
4. Tables 1 and 2 are not clear. The first line is not explained. The unit can be added, and the meaning of the numbers can be explained.
5. The experimentation show that the performance of FedBiOT may be inferior than baselines.
6. The classic FL approaches can be added as baselines.

### Questions
1. Tables 1 and 2 are not clear. The first line is not explained. What is the unit can be added?
2. The classic FL approaches can be added as baselines. I wonder if the authors can compare FedBiOT with classic approaches.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
