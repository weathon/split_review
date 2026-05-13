# Continual Traffic Forecasting via Mixture of Experts

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
The real-world traffic networks undergo expansion through the installation of new sensors, implying that the traffic patterns continually evolve over time.
Incrementally training a model on the newly added sensors would make the model forget the past knowledge, i.e., catastrophic forgetting, while retraining the model on the entire network to capture these changes is highly inefficient. 
To address these challenges, we propose a novel Traffic Forecasting Mixture of Experts (\proposed) for traffic forecasting under evolving networks.
The main idea is to segment the traffic flow into multiple homogeneous groups, and assign an expert model responsible for a specific group. 
This allows each expert model to concentrate on learning and adapting to a specific set of patterns, while minimizing interference between the experts during training, thereby preventing the dilution or replacement of prior knowledge, which is a major cause of catastrophic forgetting.
Through extensive experiments on a real-world long-term streaming network dataset, PEMSD3-Stream, we demonstrate the effectiveness and efficiency of~\proposed. Our results showcase superior performance and resilience in the face of catastrophic forgetting, underscoring the effectiveness of our approach in dealing with continual learning for traffic flow forecasting in long-term streaming networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tries to handle the catastrophic forgetting problem in the fields of traffic forecasting. The authors introduce the method referred to as TFMoE, which is based on mixture of experts technique.

### Strengths
1. The authors decompose the problem in structured way
2. The paper is well written and easy to follow
3. The problem which this paper handles is very interesting

### Weaknesses
1. Experiments are only done in one dataset. It is better to extend the scope of experiments to validate the method.
2. While the components are well combined, most of them are existing techniques.
3. Lack of analysis. Only the ablation of components were conducted. The paper would benefit from the additional analysis.

### Questions
See weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript delineates a novel approach, termed as TFMoE, which is devised for continual traffic forecasting where the traffic patterns continually evolve over time. In addressing this issue and the challenge of catastrophic forgetting, the TFMoE exhibits an innovative usage of Mixture-of-Experts,  along with three complementary mechanisms - namely Reconstructor-Based Knowledge Consolidation Loss, Forgetting-Resilient Sampling, and Reconstruction-Based Replay, that endow the model with superior performance in comparison to baseline methods.

### Strengths
S1. The paper's significance is underscored by its goal to address a real-world problem.

S2.  The TFMoE model's novelty is encapsulated in its innovative usage of Mixture-of-Experts,  along with three complementary mechanisms, effectively addressing the unique challenges in continual traffic forecasting.

S3. The evaluation is comprehensive, with comparisons to baseline methods providing a compelling demonstration of the superior performance of the TFMoE model.

S4. The clarity of the manuscript enhances accessibility for readers, facilitating a straightforward understanding of the proposed approach.

### Weaknesses
W1.  Although the paper provides a comprehensive explanation of the methodology, further technical insights regarding the implementation and specific algorithms within the TFMoE method would be beneficial. For instance, the precise mathematical formulations for the Reconstructor-Based Knowledge Consolidation Loss, the sampling strategy in Forgetting-Resilient Sampling, and the reconstruction process in Reconstruction-Based Replay are not explicitly detailed, making it difficult to fully grasp the nuances of the approach.

W2. The paper falls short in providing a detailed analysis of the limitations of the proposed TFMoE, a factor which could be significant for future research and practical applications. Specifically, the manuscript does not discuss scenarios where the proposed method might fail or underperform, such as in cases of highly volatile traffic patterns or when the underlying data distribution shifts dramatically.

W3. The computational complexity of the TFMoE algorithm, especially in the phases of continual training and forecasting, which could be a concern for large-scale datasets, is not discussed in the manuscript. A thorough analysis of the time and space complexity, including the number of parameters and the computational cost of each step, would be necessary to assess the scalability and practicality of the method.

W4.  Although the paper employs sound-good methodology and achieves competitive performance,  further efforts regarding the technical innovation and methodological novelty would be beneficial. While the combination of Mixture-of-Experts with the three proposed mechanisms is interesting, the individual components are not entirely novel, and the paper could benefit from a more detailed discussion of how these components are adapted and integrated in a unique way for the specific task of continual traffic forecasting.

W5. The manuscript could delve deeper into the parameter study, a factor which could be pivotal for practical applications. The paper lacks a detailed sensitivity analysis of the various hyperparameters, such as the learning rate, the number of experts in the Mixture-of-Experts, and the parameters associated with the sampling and replay mechanisms. This analysis is crucial to understand the robustness and generalizability of the method.

W6. A more detailed exposition of the dataset and the experimental settings used in the evaluation, including their characteristics and potential biases, would enrich the manuscript. The paper does not provide sufficient information about the specific characteristics of the traffic datasets used, such as the temporal resolution, the spatial coverage, and the presence of any missing data or outliers. This information is critical for the reproducibility and generalizability of the results.

### Questions
C1. How does the proposed method address the heterogeneous graph structures over time?

C2. Does the model's performance have a dependence on the pre-trained clustering results?

C3. Does the model have sensitivity to the parameters?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
In this paper, the authors focus on one specific traffic forecasting problem where the traffic information expands over time, and they aim to design a method that can simultaneously learn from the new data as well as the old data. Instead of training the model on the entire dataset once new data arrives, they adapt continual learning where the model can integrate the knowledge of the new data while not forgetting the past knowledge. Furthermore, they propose a set of modules to improve the performance of the model, such as clustering, VAE-based reconstruction, and forgetting-resilient sampling. The experiments on real-world datasets show the performance of the proposed method.

### Strengths
1. It proposes a novel approach to address the challenges of catastrophic forgetting and inefficiency in traffic forecasting under evolving networks. The Traffic Forecasting Mixture of Experts (TFMoE) method segments traffic flow into multiple homogeneous groups and assigns expert models to specific patterns, achieving superior performance and resilience in long-term streaming network datasets. 
2. The paper provides extensive experimental results on a real-world long-term streaming network dataset, demonstrating the effectiveness and efficiency of TFMoE. 
3. The paper emphasizes the importance of ethical considerations and reproducibility in scientific research, providing an ethics statement and reproducibility statement.

### Weaknesses
1. The Structure of the paper could be improved - Section 4 seems to be a bit too long, while part of the experiments, especially the settings and principles have to be left in the appendix. As I am not an expert in this area, section 4 is a little hard to follow, many complex modules are introduced in this section which makes it easy to lose. The sheer number of components introduced in section 4, including clustering, VAE-based reconstruction, and forgetting-resilient sampling, makes it difficult to grasp the overall architecture and how these modules interact. The lack of a clear, high-level overview before diving into the specifics of each module further exacerbates this issue. It would be beneficial to provide a more intuitive explanation of the model's overall structure before detailing each component. For instance, a diagram or a concise paragraph outlining the data flow and the role of each module would significantly improve readability. Furthermore, the decision to place crucial experimental details in the appendix hinders the reader's ability to fully evaluate the validity of the results and the reproducibility of the experiments.
2. As far as I know, clustering seems to be a common technique in the field of machine learning, while seldom reference is about the utilization of clustering in the traffic area. I think a discussion of clustering in this area is needed. Besides, the clustering operation seems to cost extra resources, in the sense of time or memory. Do the authors consider that? The paper lacks a thorough discussion on the specific challenges and considerations when applying clustering techniques to traffic data. It's not clear why a particular clustering algorithm was chosen over others, and how the hyperparameters were tuned for this specific application. Moreover, the computational overhead of the clustering step, particularly in terms of time and memory, is a significant concern that needs to be addressed. The authors should provide a detailed analysis of the computational cost of clustering and its impact on the overall efficiency of the proposed method. This is crucial for assessing the practicality of the method in real-world scenarios.
3. The paper does not discuss the generalizability of the proposed method to other traffic datasets, as there is only one dataset in the paper. I understand the hard of acquiring real-world data. Can we just use the real-world roadnet but generate several new traffic flows? In this way we can evaluate the methods on multiple datasets and see its generalization ability. The evaluation of the model on a single dataset limits the ability to assess its generalizability to diverse traffic patterns and network structures. While the authors acknowledge the difficulty in acquiring real-world data, they do not explore alternative approaches to address this limitation. For example, using the existing road network but generating synthetic traffic flows based on different distributions or scenarios could provide valuable insights into the robustness and adaptability of the model. The absence of such analysis raises concerns about the model's ability to perform effectively under different traffic conditions and network configurations.

### Questions
As I mentioned in the weakness, I suggest the authors discuss more about clustering in the literature and try to improve their experiments.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
