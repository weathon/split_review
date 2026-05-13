# Retrieval Instead of Fine-tuning: A Retrieval-based Parameter Ensemble for Zero-shot Learning

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Foundation models have become a cornerstone in deep learning, with techniques like Low-Rank Adaptation (LoRA) offering efficient fine-tuning of large models. Similarly, methods such as Retrieval-Augmented Generation (RAG), which leverage vectorized databases, have further improved model performance by grounding outputs in external information. While these approaches have demonstrated notable success, they often require extensive training or labeled data, which can limit their adaptability in resource-constrained environments. To address these challenges, we introduce Retrieval-based Parameter Ensemble (RPE), a new method that creates a vectorized database of LoRAs, enabling efficient retrieval and application of model adaptations to new tasks. RPE minimizes the need for extensive training and eliminates the requirement for labeled data, making it particularly effective for zero-shot learning. Additionally, RPE is well-suited for privacy-sensitive domains like healthcare, as it modifies model parameters without accessing raw data. When applied to tasks such as medical report generation and image segmentation, RPE not only proved effective but also surpassed supervised fine-tuning methods in certain cases, highlighting its potential to enhance both computational efficiency and privacy in deep learning applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Retrieval-based Parameter Ensemble (RPE), a zero-shot learning approach that leverages Low-Rank Adaptation (LoRA) parameters stored in a vectorized database, LoRA-VecDB, to adapt large models to new tasks without fine-tuning. For each new task, RPE retrieves and combines relevant LoRA parameters from the database based on task similarity, creating a weighted ensemble. This method targets efficient, privacy-preserving model adaptation for diverse tasks.

### Strengths
- Efficient Parameter Retrieval: The paper proposes an approach for zero-shot learning that retrieves LoRA parameters to create task-specific adaptations, reducing the need for traditional fine-tuning. 
- Privacy Consideration: The paper is motivated to tackle privacy concerns of RAG.

### Weaknesses
1. Misinterpretation of Privacy Concerns in RAG
- The paper inaccurately claims that retrieval-augmented generation (RAG) approaches require access to raw data, posing privacy risks. In reality, RAG systems typically retrieve from embedding databases, not raw data, and privacy-preserving variants (e.g., using federated learning or differential privacy) already exist. The paper would benefit from a more accurate representation of RAG’s privacy characteristics and should clarify how its approach offers advantages over these established privacy-preserving RAG methods.
2. Limited Novelty in Algorithmic Contribution
- The proposed approach closely resembles existing model zoo-based zero-shot learning techniques, such as Task2Vec, Zoo-Tuning, HyperSTAR, and Ada-Mix, which also retrieve and adapt pre-trained models based on task similarity. The main difference is the use of LoRA parameters instead of full models, offering storage advantages but not a fundamentally new algorithmic approach. The paper would be strengthened by explicitly differentiating its method from these works, detailing any unique technical contributions beyond storage efficiency.
3. Incomplete Task Representation and Retrieval Process
- The paper lacks clarity on how task representations for each dataset are generated and subsequently used in the retrieval process. Given that these representations are central to the model selection mechanism, the methodology would benefit from a detailed description of how task representations are created and validated, as well as a discussion on how task representation quality impacts retrieval performance.
4. Over-Reliance on Assumptions in Realistic Settings
- The paper assumes that a large pool of downstream LoRA models with well-defined task representations is readily available, but in practice, obtaining these representations at scale is both challenging and expensive. Additionally, the process of storing and accessing task representations carries its own privacy concerns when derived from potentially sensitive datasets. Addressing these feasibility and privacy challenges more thoroughly would improve the paper’s practicality and strengthen its claim of scalability.
5. Narrow Experimental Scope
- The experiments are limited to two tasks—medical image segmentation and medical report generation—both in the medical domain. This narrow scope makes it difficult to assess the generalizability of the approach across diverse domains or standard zero-shot learning benchmarks. Expanding the evaluation to include varied datasets and task types would provide stronger evidence of the method’s adaptability and effectiveness in broader applications.
In summary, addressing these issues would improve the rigor, novelty, and generalizability of the paper.

### Questions
Please refer to each bullet in the weakness.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article provides an example of using the RPE (retrieval-based parameter-efficient) approach, which leverages retrieval instead of fine-tuning. The author’s work uses pre-trained models to obtain representations and replaces the traditional neural network approach with a retrieval and algorithm-based method to perform mapping.  The core contribution is the use of a k-nearest neighbors (kNN) method to retrieve the closest LoRA modules, which are then used to compute weights and incorporate regularization to further improve performance. I believe this method shows promise. However, based on the current experimental setup, I’m uncertain about the performance advantage. This article needs some revisions and should provide more evidence to demonstrate the originality and performance improvements of these methods compared to others.

### Strengths
The model proposed in this article is well-structured and straightforward to implement. The experimental results, closely tied to medical data, highlight the model's significant potential for practical applications in the future. According to the model description, this method does not require additional labeling and can ensure privacy. However, these advantages have not been fully validated in the current experiments.

### Weaknesses
However, based on the current experimental setup, I’m unsure about the performance advantage. For instance, in Table 3, there is insufficient discussion about why the ensemble method outperforms other methods. The description of the experiment lacks details, especially as the data pertains specifically to the medical field. Additionally, the author claims that this ensemble method is computationally efficient, but there is no experimental evidence to validate this efficiency. The lack of clarity regarding the generalizability of the method beyond the specific medical tasks is a significant concern. The paper does not adequately address whether the observed performance is due to the method's inherent properties or if it is a result of specific characteristics of the medical datasets used. Furthermore, the originality of the method is not sufficiently demonstrated, particularly in relation to existing ensemble techniques using LoRA models. The absence of a detailed comparison with other methods raises concerns about the novelty of the approach. Finally, the section on regularization lacks crucial details, such as the method for selecting the regularization parameter, which hinders reproducibility.

### Questions
The author claims that this ensemble method is computationally efficient. If possible, could the author provide specific information on the model's time performance?

Additionally, I have a few other suggestions. The article contains a significant amount of specialized medical knowledge, so I recommend adding more background information when explaining the experiments, as many readers may not have a medical background. Given that the experiments primarily focus on medical data, I am curious whether this ensemble method is specifically suited for certain tasks in the medical field, or if it has the potential to generalize across broader applications. It would be helpful if the author could clarify this aspect.

I also encourage the author to discuss the similarities and differences between this method and other ensemble approaches that use LoRA models. For instance, is there any connection between this article and the following studies? I have concerns regarding the originality of this work, and further clarification on this point would be appreciated.

Halbheer, M., Mühlematter, D.J., Becker, A., Narnhofer, D., Aasen, H., Schindler, K., and Turkoglu, M.O., 2024. LoRA-Ensemble: Efficient Uncertainty Modelling for Self-attention Networks. arXiv preprint arXiv:2405.14438.
Zhai, Y., Zhang, H., Lei, Y., Yu, Y., Xu, K., Feng, D., Ding, B., and Wang, H., 2023. Uncertainty-penalized reinforcement learning from human feedback with diverse reward LoRA ensembles. arXiv preprint arXiv:2401.00243.
Halbheer, M., Mühlematter, D.J., Becker, A., Narnhofer, D., Aasen, H., Schindler, K., and Turkoglu, M.O., 2024. LoRA-Ensemble: Efficient Uncertainty Modelling for Self-attention Networks. arXiv preprint arXiv:2405.14438.
Finally, the article lacks certain essential details. For example, the section on regularization does not specify how to set the regularization parameter, which could hinder readers from replicating the experiments.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the Retrieval-based Parameter Ensemble method for Foundation Models that enables zero-shot adaption of foundation models. The key idea is to combine the LoRA adaptation with Retrieval-Augmented Generation mechanism. Basically, the authors consider K training datasets, adapt the foundation model using LoRA on each dataset and save the vectorized representation of the dataset along with the fine tuned LoRA weights on the vector database. To adapt to a new dataset, representation of the new dataset is computed, and its similarity with all the representations in the vector database is computed to obtain the weights. The weights are used in the ensemble of the saved LoRA parameters. Such proposed LoRA ensembling based fine-tuning enables the model to be adapted to new task in a zero-shot manner. Based on the experimental results, the proposed technique seems to be effective compared to single-task LoRA finetuning, and is beneficial in zero-shot learning.

### Strengths
- The proposed idea of Retrieval-based parameter ensemble is simple and intuitive. It is quite straightforward and can easily be applied.
- The proposed method bypasses the cost of training models on new datasets i.e. it is zero shot, and based on the empirical results, appears to be competitive. No expensive fine-tuning is required. 
- Data intensive retraining is not required in the proposed approach, and the proposed approach can minimize the privacy leaks, improving on privacy for sensitive data.

### Weaknesses
Scalability: I think the proposed idea will face scalability issue when large number of datasets appear. For each dataset, LoRA weight, along with the dataset representation would have to be stored. The experiments only consider setting with highly limited number of datasets/LoRA adaptations (4 LoRA parameters for medical report, and 6 LoRA parameters for image segmentation). I think the scalability would be major issue with number of tasks. The empirical evaluation is limited. Retrieval efficiency and storage overhead may become an issue in real-world application with large number of tasks.

Dataset representation: Representing dataset with the mean of embeddings of each data point of the dataset is quite restrictive (Eqn. 1). Though effective on the two narrow experiments carried out, this approach may not be effective and generalize for more challenging settings and problems. Some theoretical support analysis or guarantees could significantly strengthen the work. Alternatively, comprehensive empirical analysis across a diverse range of datasets could strengthen the work.

The parameter ensemble needs to weight all the LoRA parameters that may be computationally expensive, especially when considering large number of datasets, and corresponding LoRA fine-tuned weights. Moreover, the fundamental assumption of similarity of dataset representation to similarity of lora weights in parameter space may not be true. This needs to be empirically validated on more general settings beyond specialized medical task considered in the work.  

Say a completely new task/dataset appears that is distinct from the existing tasks in the vector database. Current approach is unlikely to work in such setting. 

Minor typos:
Typos:  Page 3, line 159 --> from, line 344 --> reports should be report,

### Questions
Please see and clarify on the concerns of the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Summary:
The paper combines LoRA and parameter ensembling methods to address to adaptation of foundation models.
Contributions
1.The proposed RPE adapts the foundation model without the requirement of labeled data
2.RPE is effective to zero-shot learning
3.The paper conducted experiments on extensive medical data

### Strengths
1.The paper studies an interesting issue
2.The paper proposes several strategies to compute the weights
3.The paper conducts experiments on different medical datasets

### Weaknesses
1.The paper is not self-contained, for example, the author should explain the meaning of {\delta\theta_i}, {\delta\theta_i^{ref}} and how to obtain them.
2.The improvement of the proposed method is mainly attributed to LoRA, the improvement brought by RPE is marginal

### Questions
1.What is the dataset handling process?
2.How do you obtain the four LoRA models? What is the model pre-training process?
3.Please briefly describe the evaluation metrics  and the datasets used for the segmentation task

### Soundness
2

### Presentation
2

### Contribution
2
