# LLCP: Learning Latent Causal Processes for Reasoning-based Video Question Answer

- Decision: Accept
- Scores: 8, 5, 6, 3, 8

## Abstract
Current approaches to Video Question Answering (VideoQA) primarily focus on cross-modality matching, which is limited by the requirement for extensive data annotations and the insufficient capacity for causal reasoning (e.g. attributing accidents). To address these challenges, we introduce a causal framework for video reasoning, termed Learning Latent Causal Processes (LLCP). At the heart of LLCP lies a multivariate generative model designed to analyze the spatial-temporal dynamics of objects within events. Leveraging the inherent modularity of causal mechanisms, we train the model through self-supervised local auto-regression eliminating the need for annotated question-answer pairs. During inference, the model is applied to answer two types of reasoning questions: accident attribution, which infers the cause from observed effects, and counterfactual prediction, which predicts the effects of counterfactual conditions given the factual evidence. In the first scenario, we identify variables that deviate from the established distribution by the learned model, signifying the root cause of accidents. In the second scenario, we replace embeddings of previous variables with counterfactual ones, enabling us to forecast potential developments. Once we have identified these cause/effect variables, natural language answers are derived through a combination of grammatical parsing and a pre-trained vision-language model. We assess the efficacy of LLCP on both synthetic and real-world data, demonstrating comparable performance to supervised methods despite our framework using no paired textual annotations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel causal framework, LLCP, that advances the field of VideoQA by focusing on self-supervised learning of spatial-temporal dynamics without the need for annotated data. The model is adept at reasoning about video content through accident attribution and counterfactual predictions, leveraging a generative model and natural language processing to generate answers. This approach demonstrates comparable performance to supervised methods, showcasing its potential to reduce reliance on large annotated datasets and enhance the AI's understanding of causality in videos.

### Strengths
The paper in question exhibits a commendable level of originality by shifting the focus of Video Question Answering (VideoQA) from pattern recognition to causal reasoning, an approach that has not been extensively explored in this field. The introduction of the Learning Latent Causal Processes (LLCP) framework marks a creative synthesis of self-supervised learning, generative modeling, and natural language processing, tailored to decipher the causal dynamics of video content without relying on annotated question-answer pairs. This methodological innovation reflects the paper's high quality, as it seemingly adheres to rigorous empirical standards and offers a robust validation on both synthetic and real-world datasets. In terms of clarity, the paper articulates its contributions and methodologies with precision, making the novel concepts accessible and understandable, which is indicative of the authors' commitment to effective communication of complex ideas. The significance of this work is multifold, promising to reduce the need for labor-intensive labeled data in VideoQA, enhance the interpretive and interactive capabilities of AI systems with causal reasoning, and potentially influencing a range of applications where understanding the underlying causal relationships in visual data is crucial. Overall, this paper appears to make a substantial and meaningful contribution to the literature, potentially setting a new course for future research in the AI domain, with implications that extend beyond the immediate scope of VideoQA.

### Weaknesses
In the paper, potential areas for improvement include enhancing the model's robustness to spurious correlations and label noise, more explicitly demonstrating LLCP's ability to capture causal relations through additional experiments, and benchmarking its causal reasoning against current approaches. The paper could also benefit from a more detailed discussion of the challenges in video reasoning it aims to address and a clearer explanation of its operation independent of established causal frameworks and annotations. Finally, a dedicated section that explicitly outlines the paper's limitations and assumptions would add transparency and guide future research directions. Addressing these points could strengthen the paper's contributions and its value to the VideoQA field.

### Questions
Could the authors provide a comprehensive list of the limitations and assumptions inherent in LLCP, and discuss how these might affect the generalizability and applicability of the model?
Could you provide additional empirical evidence or case studies that demonstrate LLCP's specific capability to uncover underlying causal relations as opposed to merely correlational patterns?
Is there a quantitative evaluation comparing LLCP's causal reasoning capacity with that of existing approaches, and if so, what benchmarks or metrics were used?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Learning Latent Causal Processes (LLCP) framework introduces a novel approach to Video Question Answering (VideoQA) by focusing on causal reasoning rather than traditional cross-modality matching. LLCP utilizes a multivariate generative model to analyze spatial-temporal dynamics and trains through self-supervised local auto-regression, thus eliminating the need for annotated question-answer pairs. It adeptly handles accident attribution and counterfactual prediction tasks, identifying root causes and forecasting potential outcomes through modifications in variable embeddings.

### Strengths
1. The idea of learning causality from video is interesting.
2. The paper is overall presented clearly.
3, The authors made efforts on providing fair comparisons with existing methods.

### Weaknesses
1. The main concern is that the current setting is too far from realistic settings. The current evaluation setting is really more like hacking parts of existing datasets. The reviewer encourage the authors to make this work more complete.

a. It is too constraint to only evaluate the proposed method when it has no access to QA labels. If the obtain model really captures the casual relationship in videos, plugging it into existing methods in the supervised training setting can show a much more broad application of the proposed method.

b. It is also not realistic to exclude the text query from the training process since the fusion between visual and textual input is also the crucial design to really solve the VQA problem. For example, if there are two accidents going on in the video, the current framework will have systematical flaw as the model is not conditioned on the question text which specifies which accident it is about.

c. Despite the effort of re-training many existing methods, it is not well-justified why it is necessary to discard important features like motion or object as used in Causal-Vid-QA, which brings all the models to a low-performance scheme.

d. There is no proper comparison with methods that do not require QA data like but not including to [a,b,c]. The authors should also acknowledge and at least provide comparison with some of these relevant methods to really provide the audience a correct and comprehensive understanding of the relevant solution to this setting.

e. Once a and b are done, it is also necessary to provide additional comparison on broader VideoQA datasets to understand the importance of causal learning process in videos for broader videoQA tasks, which is really beneficial for the community.


Minor:
1. Title, related work: Video Question Answer -> Video Question Answering.

### Questions
Please check weakness for details.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focused on the task of reasoning-based video QA. The challenge is the lack of causal relations in the cross-modal matching pipelines. This work employs a temporal multivariate generative model to understand the latent causal patterns, which can be used to answer caused-based and effect-based questions about videos. The experiments are conducted on two simulation datasets and two real-world VideoQA datasets.

### Strengths
+ The proposed model can achieve comparable performance to supervised methods while no paired textual annotations are used. The proposed framework can answer both cause-based (i.e., accident attribution) and effect-based (i.e., counterfactual prediction) reasoning questions. It shows the potential of self supervision.

+ The motivation of explore latent causal relations for video QA makes sense and is interesting.

### Weaknesses
 - The presentation is not satisfying enough. It is hard for me to figure out the connection between motivation and implementation details, especially how the method can guarantee that the learned relation is causal rather than temporal, and the terminologies of variables. Please see "questions" for detailed comments.

- Another main concern is whether the model is causality-based or just capture temporal relations. In addition to the concept of causal relation, I didn't see how the implementation reflect the tools of causal inference or causal reasoning. Therefore, I am wondering whether the causal understanding ability is over-claimed. Experimental results can verify the ability empirically, but theoretical explanations or guarantees are missing.

- The ablation studies in Table 4 mainly demonstrate the contributions of sub-networks rather than the role of historical states and environment. What if we replace the historical states and environment with wrong ones? What is the performance then? That would show that the performance drop is due to the lack of visual information rather than fewer parameters.

### Questions
1. What does the red node in Figure 1 (b) mean? What it is red during test pipeline but not highlighted during training pipeline?

2. The abstract mentioned that the proposed LLCP employs a temporal multivariate generative model to understand the causal patterns. I am not aware of how the *temporal* model can discover *causal* relations. I am wondering how to guarantee that the learned pattern are causal relations rather than temporal correlations using the so-called temporal model? In the method part, I am not aware of how the learned pattern are causality rather than correlation.

3. I didn't find strict definitions of historical state, neighborhoods, and environment variables. Could the authors provide a precise and accurate definition, or give examples of these three variables? For example, are they features of a single frame, an object, or a set of tracked frames? How does the object tracking model obtain these three variables in temporal and spatial dimensions? It seems that Figure 4 provide an example, but it appears a bit late when I was reading Sec. 3.1 but didn't find the examples.

4. In Ex. (2), is x_{t,i} an image (or region of interest) or feature vector?

5. According to Figure 4, the question seems to be the input of text side rather than video side. In this case, how can we determine the object of interest when extract the visual information and make the prediction of visual states? Is it reasonable to extract question-independent visual feature to answer the question?

6. What does the arrows mean in Figure 5? Are they drew manually or automatically estimated by the model?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a video reasoning framework called Learning Latent Causal Processes (LLCP). LLCP first makes use of a conditional VAE framework to extract the spatio-temporal dynamics of objects in videos in a self-supervised manner. These extracted dynamics then serve as weak supervision to analyze the relationships between events during inference time, facilitating the identification of root cause of accidents and counterfactual effects. Tested on both synthetic and real-world benchmarks, the proposed method demonstrates advantage over baselines while still underperforming supervised methods.

### Strengths
- It is well-motivated and a desired but missing capability in AI systems to model causal relationships between objects/events in video understanding.

- The implementation seems straightforward.

- The proposed method demonstrates promising results when compared with some baseline methods and its supervised counterparts on both synthetic and real-world benchmarks.

### Weaknesses
 - The novelty of the paper is limited. While the paper draws motivation from causal modeling, both the theoretical analysis and the implementation of TMGM using conditional VAEs do not adequately realize the causal processes in Eq. 1. Specifically, the paper claims to learn causal relationships, but the conditional VAE framework, even with the proposed temporal modeling, does not inherently enforce the necessary properties for causal inference. The model learns to predict future states, but this predictive power does not necessarily equate to understanding causal mechanisms. The use of auto-regression, while capturing temporal dependencies, does not guarantee the identification of causal directions or the disentanglement of confounding factors.

- It is not clear how the authors enforce the independence constraints, both spatially and temporally, on the noise variables by the three subnetworks f_N, f_H and f_E. I would say the fusion of these three networks encodes spatio-temporal dynamics across objects (agents) but it is unclear if this has any bearing on causal relations. The paper mentions a KL divergence loss, but it is not clear how this loss enforces the conditional independence of the latent variables given their parents, as required by the causal model. The model seems to learn a joint distribution of the latent variables, but this does not necessarily imply the independence of the noise terms, which is crucial for causal identification. The fusion of the three subnetworks, while potentially capturing different aspects of the input, does not guarantee the disentanglement of causal mechanisms.

- Experiments only compare LLCP with weaker variants of VAEs which offer little to no  temporal modeling. In addition, the proposed method largely underperforms supervised methods as indicated by Table 5 and Table 6. The baselines used for comparison lack sophisticated temporal modeling capabilities, making the performance gains of LLCP less significant. The comparison with supervised methods highlights the limitations of the unsupervised approach. The paper needs to demonstrate its performance against more competitive unsupervised baselines, particularly those that explicitly model temporal dynamics and causal relationships.

### Questions
Apart from my concerns in the Weakness section. I have some other questions:

- Regarding the first task of root cause analysis, is there any reference for the definition of root causes in Sec. 3.2? The provided definition seems to be applicable with only anomaly/outlier detection.

- In Sec. 3.4, what happens if we formulate counterfactual questions in an open-ended format, i.e. “what if”?

- The outlier analysis at inference times relies on extracted features from pretrained models (i.e., CLIP) which can be brittle if tested data is outside of the trained distribution. In addition, using language parser to parse user queries is not ideal as well. Have you thought of an alternative solution towards this?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces a weakly-supervised approach for reasoning about accidental events, leveraging causal representation learning combined with experimental tests on the derived causal variables. These causal variables, when integrated with CLIP, are aligned into natural language, forming an explainable AI (XAI) system. The proposed method undergoes rigorous analysis on simulated data and demonstrates comparable, performance to recent supervised techniques when tested on two real-world datasets.

### Strengths
1. The paper is well-structured, appealing to a broad readership.
2. It effectively applies causal learning to a real-world scenario, using a robust implementation with statistical tests on TMGM-derived causal variables.
3. The technique innovatively connects causal variables and natural language through CLIP, potentially reshaping standards in explainable AI (XAI).
4. Evaluation is thorough, including simulations and comparisons with supervised methods.
5. Impressively, the weakly-supervised approach matches the performance of supervised methods.

### Weaknesses
The authors primarily use a generative model for potential causes and treat language as a secondary filter. This approach however neglects language cues. Is that possible to have the lanuage involved for the genertive process? While the experiments show good improvements, could the author clarify the motivation of unsupervised generative approach over the supervised ones.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
