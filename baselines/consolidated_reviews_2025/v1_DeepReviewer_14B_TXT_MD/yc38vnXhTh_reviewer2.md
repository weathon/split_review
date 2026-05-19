### Summary

This paper introduces ACTOR, an LLM-powered agent designed to simulate realistic human behavior in 3D scenes. ACTOR integrates an LLM controller to perform complex behaviors through planning on goal decomposition guided by hierarchical activity prior. The value-driven mechanism further deepens its understanding of environment. The authors also created BEHAVIORHUB, a large-scale dataset that contains 3D scenes, human motion sequences and the corresponding plan. The dataset is generated automatically by leveraging existing resources of human motions and indoor scenes. The dataset is split into a training set and a dynamic test set, where the test set introduces dynamics changes. The experiments show that ACTOR exhibits more robust planning performance in BEHAVIORHUB than two baseline methods. The authors also show that BEHAVIORHUB can be used as a training dataset for scene-aware motion generation and language-conditioned motion generation tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The proposed dataset contains 3D scenes, human motion sequences and the corresponding plan. The dataset is generated automatically by leveraging existing resources of human motions and indoor scenes. This dataset can be a good supplementary to the existing datasets in the community, especially for the tasks that require 3D scenes and holistic plan.
- The proposed method ACTOR utilizes a value-driven mechanism to guide the LLM planning, which shows better planning performance than the baseline methods.

### Weaknesses

#### Some Related Works


#### comment

 - The motion quality is still a big issue for the proposed dataset. I understand that the main contribution of the dataset is not the motion quality, but the dataset will not be useful if the motion quality is too low. Maybe the authors can consider using the recent motion generation models that can produce high-quality motion, e.g., https://arxiv.org/pdf/2310.13986, https://arxiv.org/abs/2312.14011.
- The dataset lacks the diversity in human-scene interactions, e.g., the person sits on the sofa instead of standing above the sofa, the person reaches the object, etc. This also affects the motion quality.
- The authors should provide a more detailed description of the AMASS dataset, including the specific subset used, the original annotations, and the criteria for selecting motion sequences. The current description lacks sufficient detail to understand the data's characteristics and potential biases.
- The authors should provide more details about the "interchangeable groups" mentioned in line 290. The current explanation is unclear, and it is difficult to understand how these groups are defined and used in the dataset. A more precise definition and examples are needed.
- The authors should provide more details about the verification process, including the specific criteria used by the verifiers, the number of samples verified, and the inter-annotator agreement. The current description is too vague to assess the reliability of the verification process.
- The authors should provide more details about the experimental setting of LLMaP, including the specific prompts used, the hyperparameter settings, and the training procedure. The current description lacks the necessary details to reproduce the results.
- The authors should also evaluate the motion quality on the test set, as the motion quality issues in the training set are likely to propagate to the test set. The lack of motion quality evaluation on the test set is a significant oversight.
- The authors should provide more details about the "ungrounded LLM" mentioned in line 431. The current explanation is unclear, and it is difficult to understand the specific limitations of the LLM in this context.
- The authors should provide more details about the "pre-request steps" mentioned in line 459. The current explanation is unclear, and it is difficult to understand how these steps are defined and used in the dataset.
- The authors should provide more details about the "language commands" mentioned in line 461. The current explanation is unclear, and it is difficult to understand the specific language commands used and their impact on the agent's behavior.
- The authors should provide more details about the "environmental dynamics" mentioned in line 464. The current explanation is unclear, and it is difficult to understand the specific types of environmental dynamics considered in the dataset.
- The authors should provide more details about the "completeness" metric mentioned in line 483. The current explanation is unclear, and it is difficult to understand how this metric is calculated and what it measures.
- The authors should provide more details about the "sequential order" mentioned in line 485. The current explanation is unclear, and it is difficult to understand how this order is defined and used in the dataset.
- The authors should provide more details about the "semantic similarity" mentioned in line 498. The current explanation is unclear, and it is difficult to understand how this similarity is calculated and what it measures.
- The authors should provide more details about the "contact distance threshold" mentioned in line 501. The current explanation is unclear, and it is difficult to understand how this threshold is defined and used in the dataset.
- The authors should provide more details about the "GSR" mentioned in line 504. The current explanation is unclear, and it is difficult to understand how this metric is calculated and what it measures.
- The authors should provide more details about the "GSRPL" mentioned in line 506. The current explanation is unclear, and it is difficult to understand how this metric is calculated and what it measures.
- The authors should provide more details about the "recognition accuracy" mentioned in line 509. The current explanation is unclear, and it is difficult to understand how this metric is calculated and what it measures.
- The authors should provide more details about the "Frechet Inception Distance (FID)" mentioned in line 510. The current explanation is unclear, and it is difficult to understand how this metric is calculated and what it measures.
- The authors should provide more details about the "RNN action recognition classifier" mentioned in line 511. The current explanation is unclear, and it is difficult to understand how this classifier is trained and used in the evaluation.
- The authors should provide more details about the "GPT-3.5" mentioned in line 547. The current explanation is unclear, and it is difficult to understand how this model is used in the experiments.
- The authors should provide more details about the "GPT-4" mentioned in line 547. The current explanation is unclear, and it is difficult to understand how this model is used in the experiments.
- The authors should provide more details about the "Vicuna-7b" mentioned in line 550. The current explanation is unclear, and it is difficult to understand how this model is used in the experiments.
- The authors should provide more details about the "PROX" mentioned in line 586. The current explanation is unclear, and it is difficult to understand how this dataset is used in the experiments.
- The authors should provide more details about the "HumanML3D" mentioned in line 588. The current explanation is unclear, and it is difficult to understand how this dataset is used in the experiments.
- The authors should provide more details about the "supp. §A.4" mentioned in line 356. The current explanation is unclear, and it is difficult to understand what information is provided in the supplementary material.

### Suggestions

The paper would benefit from a more thorough analysis of the motion quality in the generated dataset. While the authors acknowledge that motion quality is not the primary focus, the current level of motion quality significantly limits the dataset's potential impact. The authors should explore more advanced motion generation techniques, such as those based on diffusion models or transformers, to improve the realism and diversity of the generated motions. Specifically, they could investigate methods that explicitly model human-scene interactions, ensuring that the generated motions are not only realistic in isolation but also contextually appropriate within the 3D scenes. Furthermore, a detailed ablation study on the impact of different motion generation models on the downstream task performance would be valuable. This would help to understand the trade-offs between motion quality and task performance, and guide future research in this area. The authors should also consider incorporating more complex human-scene interactions, such as object manipulation, reaching, and sitting, to enhance the dataset's richness and applicability.

To address the lack of clarity in several aspects of the paper, the authors should provide more detailed explanations and examples. For instance, the concept of "interchangeable groups" needs a more precise definition, along with concrete examples of how these groups are identified and used in the dataset. The verification process should be described in detail, including the specific criteria used by the verifiers, the number of samples verified, and the inter-annotator agreement. This would help to assess the reliability of the verification process and ensure the quality of the dataset. Similarly, the experimental settings for LLMaP, including the specific prompts used, the hyperparameter settings, and the training procedure, should be clearly documented to ensure reproducibility. The authors should also clarify the meaning of terms like "ungrounded LLM," "pre-request steps," and "language commands," providing specific examples of how these concepts are used in the experiments. A more detailed explanation of the evaluation metrics, such as GSR, GSRPL, FID, and recognition accuracy, is also needed, including how these metrics are calculated and what they measure. This would help to understand the results and compare them with other methods.

Finally, the authors should provide more details about the datasets used in the experiments, including the specific subsets of AMASS, PROX, and HumanML3D. The authors should also clarify the meaning of "supp. §A.4" and provide a link to the supplementary material. The paper would also benefit from a more thorough discussion of the limitations of the proposed approach and the potential directions for future research. This would help to contextualize the contributions of the paper and guide future work in this area. The authors should also consider releasing the code and the dataset to the public to facilitate further research and development in this area.

### Questions

Please refer to the weakness part.

### Rating

6

### Confidence

4

**********
