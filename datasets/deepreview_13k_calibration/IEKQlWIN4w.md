# CAML: Collaborative Auxiliary Modality Learning for Multi-Agent Systems

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Multi-modality learning has become a crucial technique in enhancing the performance of machine learning applications across various domains, including autonomous driving, robotics, and perception systems. Existing frameworks, such as Auxiliary Modality Learning (AML), effectively utilize multiple data sources during training and enable inference with reduced modalities, but they primarily operate in a single-agent context. This limitation is particularly critical in dynamic environments, such as connected autonomous vehicles (CAV), where incomplete data coverage can result in decision-making blind spots. To address these challenges, we introduce Collaborative Auxiliary Modality Learning ($\textbf{CAML}$), a novel extension of the AML framework for multi-agent systems. $\textbf{CAML}$ facilitates collaboration among agents by allowing them to share multimodal data during training. During inference, each agent operates effectively with fewer modalities, ensuring robustness in performance even with missing data. We analyze the effectiveness of $\textbf{CAML}$ from the perspective of uncertainty reduction and data coverage, providing a theoretical support to understand and explain why $\textbf{CAML}$ works better than AML. We then validate $\textbf{CAML}$ through experiments in collaborative decision-making for CAV in accident-prone scenarios. Experimental results show that $\textbf{CAML}$ outperforms AML across all tested scenarios, achieving up to a ${\bf 58.3}$% improvement in accident detection. Additionally, we validate our approach on real-world data from aerial-ground vehicles for collaborative semantic segmentation, achieving up to ${\bf 10.8}$% improvement in mIoU compared to AML.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends Auxiliary Modality Learning (AML) for multi-agent systems, resulting in Collaborative Auxiliary Modality Learning (CAML). Then each single-agent can maintain robustness robustness even with missing modalities during inference through multi-agent information sharing. Analysis about uncertainty reduction, and data coverage provides a theoretical support to understand and explain why CAML works better than AML. And the CAML system is validated in the application of decision-making for CAV in accident-prone scenarios, demonstrating the effectiveness of the proposed CAML.

### Strengths
1. The writing is easy to follow.  
2. The motivation and proposed method are clearly stated.  
3. This work represents a novel effort to integrate multi-agent systems into Auxiliary Modality Learning.  
4. The experiments demonstrate the effectiveness of CAML compared to previous baselines by incorporating multi-agent collaboration.  
5. It is promising that CAML can achieve comparable performance with RGBD using only RGB modality, and the benefits of multi-agent training can extend to single-agent testing scenarios.

### Weaknesses
1. Lack of ablation studies on a wider range of modalities. For instance, what happens when training involves both LiDAR and RGB modalities, while testing uses only RGB or LiDAR? Would the performance still improve when the modality gap is significant?
2. Lack of validation on real-world benchmarks. Validating real-world data is crucial, especially for applications in connected autonomous vehicles. Numerous real-world benchmarks exist, such as DAIR-V2X, V2V4Real, and TUMTraf, making real-world validation essential.
3. Lack of quantitative analysis regarding uncertainty reduction and data coverage. Additionally, providing qualitative visualization examples would enhance the presentation.

### Questions
1. If different modality embeddings are combined through concatenation, can the system only accommodate a fixed modality?  
2. What about heterogeneous scenarios where agents possess different modalities, such as in an RGBD context, including single agents with either RGB or depth data?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to generalize Auxiliary Modality Learning (AML) to the context of cooperative perception. AML benefits machine learning by enabling inferencing on reduced modality space. The paper validates its proposed CAML method from the perspective of effective uncertainty reduction and data coverage to justify its superiority over AML. Empirical experiments on accident detection further support the conclusion.

### Strengths
The paper is well-organized, with a clear objective and statement of its design logic. The experiment design comparing the proposed CAML with its baseline AML effectively showcased the benefits of extending to a cooperative context well.

### Weaknesses
1. This paper's main contribution is an extension of an existing maturely developed machine learning technique, AML, to the context of cooperative perception, which limits its scope of novelty. Despite experiments conducted by the authors to investigate the benefits of CAML compared to single-agent AML, they only investigate one of the plausible paradigms for applying the AML - ego-only paradigm. Since we are looking into a cooperative perception task, will it be more sensical to use AML for training the encoder for single vehicles in parallel before fusion (**pre-fusion**) and compare this application with the proposed CAML, which is essentially applying a joint-version of AML to train the fusion module (**on-fusion**)?
2. The authors have cited several related works to demonstrate the benefits of applying AML to a perception system. However, it would be much better if the authors could present a comparative study of CAML, AML, and other cooperative perception methods on traditional cooperative perception tasks, such as objective detection, to showcase the need for applying AML in cooperative perception.

### Questions
Problems have been raised in the discussion about the weakness of this paper. Here are a few of them in short:
1. Can you justify the need to use AML for cooperative perception in general? If it was beneficial, why had no one before this paper explored using it for more traditional tasks such as cooperative object detection?
2. What is CAML's time and space complexity concerning the number of connected agents? From your description, I presume it is quadratic. Would this trade-off in extra time and space complexity be worth it?
3. Can you compare applying AML on training the entire fusion module to using it only for the encoder and decoder on single vehicles (pre- or post-fusion)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper attempts to address the Auxiliary Modality Learning problem by means of a multi-agent system, where models are permitted to employ additional modalities during training while enabling inference with fewer or even a single modality.

### Strengths
1. The topic of  Auxiliary Modality Learning is interesting and practical. It provides solutions to deal with scenarios where limited modalities are available for inference, making it applicable in real-world situations with constrained data. 

2. The author's attempt to address AML with a multi-agent system is interesting. The use of a multi-agent system in this context is an innovative concept that can lead to more efficient and effective learning processes.

3. The analysis part puts forward three interesting questions. These questions cover important aspects of agent collaboration and can lead to a deeper understanding and evaluation of the related mechanisms and effects.

### Weaknesses
1. Many experimental settings are not described clearly. For instance, is there a correlation between the number of agents and the number of modalities? The number of agents appears not to be explicitly stated in the experiment. Additionally, I am curious about how the experiment is devised when the number of modalities exceeds 3, and what the outcome would be.

2. Accurate numbers should preferably be marked on the histograms in the experiment for convenient viewing. For example, in Figure 4(a), it is difficult to tell the highs and lows. Meanwhile, I'm also curious about why while STGN uses both RGB and depth data during testing, CAML relies solely on RGB, yet achieves comparable, or even better performance.

3. There should be a comparative analysis of training complexity. Multiple agents inevitably increase the parameters of the network. Is the source of the performance improvement due to the increase in network parameters?

4. Discussions on limitations are necessary as there is no description of the limitations of the proposed method.

### Questions
Please see weaknesses above.

### Soundness
3

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
3

### Summary
This paper introduces Collaborative Auxiliary Modality Learning (CAML), a framework that extends Auxiliary Modality Learning (AML) to multi-agent systems. CAML allows agents to collaborate and share multimodal data during training, while enabling efficient, reduced-modality inference during testing. The authors provide theoretical analysis of CAML's effectiveness from the perspectives of uncertainty reduction and data coverage enhancement, explaining why CAML outperforms AML. The framework is validated through experiments on collaborative decision-making tasks for connected autonomous vehicles in accident-prone scenarios. The paper shows CAML's modality-efficient superiority and generalizability. The paper positions CAML as a unified approach that leverages multi-agent collaboration to improve robustness and accuracy in predictions, while reducing computational costs and data requirements at test time. This has potential applications in various domains where multi-agent collaboration and multimodal learning are crucial.

### Strengths
The paper demonstrates several notable strengths across the dimensions of originality, quality, clarity, and significance: 

  

**Originality:** CAML creatively combines ideas from knowledge distillation, multi-agent systems, and multi-modal learning, resulting in a novel approach to handling complex, real-world scenarios. 

  

**Quality:**The paper provides a solid theoretical analysis of CAML's effectiveness, examining it from the perspectives of uncertainty reduction and data coverage enhancement. This adds depth and credibility to the proposed approach. 

  

**Clarity:** Well-structured: The paper follows a logical flow, clearly presenting the problem, methodology, theoretical analysis, and experimental results. 

   

**Significance:** CAML's ability to perform well with reduced modalities during testing offers potential computational and resource efficiency benefits in deployed systems. While focused on autonomous driving, the framework's principles could be applied to other multi-agent, multi-modal learning scenarios, such as distributed sensing systems. 

   

In summary, the paper presents an interesting approach to a problem in multi-agent systems, supported by thorough theoretical analysis and experimental validation.

### Weaknesses
Here are the key areas where the paper could be strengthened: 

1. Modalities in Experimentation: It’s unclear which modalities are used for the experiments. While some sections mention depth, RGB, and LIDAR, the modalities should be clearly stated in Section 5.1 (Data Collection). Clarifying the exact modalities, including whether they are raw or processed, and how they are preprocessed, would provide better insight into the data used. For example, are the RGB images rectified, and are the LiDAR point clouds filtered or downsampled? Specifying the exact sensor configurations and data formats is crucial for reproducibility.

2. Overly Simplistic Driving Scenarios: The driving scenarios seem too basic. Including more complex environments with domain randomization (e.g., varying numbers of pedestrians and vehicles, diverse weather conditions, and different road layouts) would enrich the evaluation. Results from real-world scenarios, or at least more realistic simulations with sensor noise and calibration errors, would also be valuable to demonstrate generalization. The current scenarios appear to be too controlled and may not reflect the challenges of real-world deployment.

3. Limited Analysis of Failure Cases: The paper focuses on scenarios where CAML performs well, but lacks an exploration of its weaknesses or failure cases. To strengthen the paper, include a detailed analysis of these cases, such as situations where the collaborative learning fails, or when the reduced modality inference leads to significant performance degradation. Discuss possible improvements or limitations of the approach under these conditions. For example, what happens when one agent's sensor data is corrupted or missing?

4. Insufficient Training Details: More details about the training setup would improve reproducibility. It would be useful to specify the GPU type, batch size, learning rate, optimization algorithm, and training time, and hardware resources used for training. Providing these details ensures transparency and supports future replication. It would also be helpful to include information on the specific network architectures used for each modality and how the modalities are fused.

Typos: 

1. L377: “CAML .” -> “CAML.”  There is a space between “L” and “.”

### Questions
Questions: 

1. Clarification on Modalities: Can you clarify the exact modalities used in the experiments? Section 5.1 (Data Collection) does not specify this clearly, and it is inferred that depth, RGB, and LIDAR were utilized from other sections. Are these the only modalities involved, or are there others? 

2. Complexity of Driving Scenarios: How realistic were the driving scenarios used in the experiments? Did you incorporate domain randomization, and how many pedestrians or vehicles were simulated? Additionally, are there plans to test the approach in real-world settings? 

3. Failure Case Analysis: What are the specific failure cases where CAML underperforms? Including more analysis or examples of these cases would provide a clearer understanding of the framework’s limitations and potential areas for improvement. 

4. Training Setup: Can you provide more details about the training setup, such as the GPU types, number of hours required for training, and hardware resources used? This would help improve reproducibility and enable more accurate comparisons in future work.

### Soundness
3

### Presentation
3

### Contribution
3
