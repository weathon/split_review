# Toward Robust Real-World Audio Deepfake Detection: Closing the Explainability Gap

- Decision: Reject
- Scores: 1, 5, 3, 1

## Abstract
The rapid proliferation of AI-manipulated or generated audio deepfakes poses serious challenges to media integrity and election security. Current AI-driven detection solutions lack explainability and underperform in real-world settings. In this paper, we introduce novel explainability methods for state-of-the-art transformer-based audio deepfake detectors and open-source a novel benchmark for real-world generalizability. By narrowing the explainability gap between transformer-based audio deepfake detectors and traditional methods, our results not only build trust with human experts, but also pave the way for unlocking the potential of citizen intelligence to overcome the scalability issue in audio deepfake detection.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper analyses the existing explainable methods, such as Occlusion and Attention visualization, for deepfake audio detection tasks. The authors show results using three baseline models such as AST, GBDT, Wav2Vec. The authors evaluate these methods on two existing datasets.

### Strengths
- Authors provide an analysis of explainable and interpretable methods for audio deepfake detection methods. The authors compare these methods on two different benchmark datasets.

### Weaknesses
- The paper is merely an analysis paper of existing explainable methods. There are no significant novel contributions to this paper. The authors mention in line 052 that the contributions are "Empirical evaluations of novel explainability methods for audio transformers". However, I cannot judge what novelty is in attention visualization for transformers. It has happened a lot in literature. 
- When authors compare explainable methods for audio deepfake detection, they must show the results on existing approaches such as Shapley[1]. 
- The authors should include more explainable mechanisms as baselines, such as [2], [3].
- The authors should show results on multilingual deepfake audio datasets such as MLAAD, DECRO, and WaveFake since AST and Wav2vec are pre-trained on the AudioSet dataset, primarily English. Evaluating a multilingual dataset would help strengthen the analysis.
- Authors show results on the ASVspoof5 dataset. The authors mention that the dataset was released in June 2024 (line 750). However, The dataset is still not available for public use and review. Authors should show the results on the publicly available datasets.
- FakeAVCeleb dataset is primarily an audio-video deepfake dataset, not only for audio deepfake detection. The FakeAVceleb dataset contains 500 real videos, which means there should be 500 real audio. However, authors in line 7716 mention 9712 real audio samples. Why is there a difference in the numbers?
- Even the baseline models such as GBDT, Wav2Vec and AST are general audio architectures, not specifically designed for audio deepfake detection. Authors must show results on models such as ASSIST, RawGAT-ST and some state space models such as RawBMamaba.
- More then 50% of the paper is just explaining trivial and non paper contributions only.



[1] Explaining deep learning models for spoofing and deepfake detection with SHapley Additive exPlanations
[2] Listen to Interpret: Post-hoc Interpretability for Audio Networks with NMF
[3] Focal Modulation Networks for Interpretable Sound Classification

### Questions
Please see the weakness listed above.

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
4

### Summary
This paper addresses the limitations of existing audio Deepfake detection models in terms of generalization ability and interpretability in real-world scenarios. It proposes a novel interpretability approach and establishes a new benchmark to assess model generalization performance. The study trains models on the ASVspoof dataset and evaluates them on the FakeAVCeleb dataset, demonstrating the superior performance of Transformer-based audio detection models on unseen data. Additionally, the paper introduces attention visualization and occlusion techniques to enhance model interpretability, aiming to bridge the gap between model performance and interpretability.

### Strengths
1. The paper introduces an interpretability framework for the audio domain, incorporating interpretability techniques from visual and natural language processing into audio Deepfake detection, providing a clearer interpretative path for the model's black-box decision-making process.

2. Two interpretability methods (attention visualization and occlusion techniques) are systematically explored to assess the interpretability of Transformer-based audio detection models, with a comparison of each method's strengths and weaknesses.

3. Cross-validation using the ASVspoof and FakeAVCeleb datasets demonstrates the model's generalization capability across varying data distributions, simulating data shift scenarios common in real-world applications.

### Weaknesses
1. The author mentions three limitations in the Limitation section, of which the latter two could serve as directions for future work. However, the first limitation needs to be addressed in the current phase of the task: relying solely on the ASVspoof and FakeAVCeleb datasets may not cover the full range of audio deepfake techniques encountered in real-world scenarios, presenting a dataset limitation. A wider variety of datasets and scenarios is needed to demonstrate the robustness and completeness of the current approach.

2. The introduced attention visualization and occlusion techniques are computationally intensive, potentially affecting the efficiency of practical deployment. Further analysis and comparison of computational costs would be beneficial.

3. The paper’s contribution is somewhat limited, as occlusion and attention visualization are commonly used techniques in computer vision and natural language processing. While adapting these methods for audio Deepfake detection is interesting, the lack of specific modifications tailored to the characteristics of audio forgery detection tasks reduces the overall impact of the proposed approach. Simple method transfer limits the originality of the contribution.

### Questions
1. It is recommended to incorporate a wider variety of audio forgery datasets to validate the model's generalization capability across different forgery techniques, aligning more closely with the diversity encountered in real-world scenarios.

2. While interpretability is essential, it would be beneficial to analyze how interpretability can contribute to designing better models or evaluating existing ones. Adding such analysis could enhance the paper's contribution by illustrating the practical impact of interpretability on model improvement and assessment.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel explainability framework for audio transformers in audio deepfake classification. It proposes utilizing image occlusion to detect feature importance and attention roll-out to understand features better. It also open-sources a novel benchmark for detecting audio deepfakes in real-world cases, which consists of training on ASVspoof5 dataset and testing on FakeAVCeleb dataset.

### Strengths
The authors have analyzed the information available from Attention Rollouts and Image Occlusion methods. They also noted that some very short frames from audio signal representation are influential to transformers in classifying and these frames typically appear in groups, which, if further explored, may potentially lead to better interpretability of audio deepfake classifications.

### Weaknesses
As the authors themselves have pointed out, attention roll-out and image occlusion-based analysis have been in existence for quite some time, but the novelty of the proposed work lies in applying them in spectrograms to aid in the explainability of audio deepfake analysis. However, how these attention roll-out and image occlusion-based analyses are aiding explainability specific to the audio deepfake analysis is not adequately explained, and how their contribution differs from already existing contributions of attention roll-out and image occlusion-based analysis methods in image feature explainability remains unclear. 

They have utilized the occlusion method in an attempt to explain how the model is reaching these decisions, but as they themselves pointed out, it was not helpful in explaining the model’s decision-making. They have also used an attention visualization method and stated that they can attribute specific frames that were instrumental to classification. However, using attention visualization to attribute where a transformer model is putting importance is not novel, and their analysis does not show enough contribution specific to explaining the decision process in audio deepfake classification in transformers. 

They have proposed a new benchmark, which consisted of training on one existing dataset and testing on another. They have not provided adequate explanations as to how their novel benchmark would be more helpful in audio deepfake classification, and the idea of testing on a new dataset itself is not particularly novel.

### Questions
1. How are these attention roll-out and image occlusion-based analyses aiding explainability specific to the audio deepfake analysis, and how does this contribution differ from the contributions of attention roll-out and image occlusion-based analysis methods in image feature explainability?

2. Are the normalized token attention plots taken as an average of multiple audio samples or the entire dataset? How do these token attention plots vary with different samples? Further information is needed on the normalized token attention plots. 

3. It is stated that “..we can pinpoint specific frames that were instrumental in the classification and inspect them more closely…. and we observe that influential tokens typically appear in groups.” This is one of the primary focus of the paper, and further analysis should be done to elaborate these findings.

4. What is the significance of training ASVspoof5 and inferring on FakeAVCeleb over existing benchmarks, beyond the test of generalizability? What specific challenges might inferring on FakeAVCeleb bring that training on ASVspoof5 would not cover?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper focuses on the limitations of explainability in current audio deepfake detection methods and provides three-fold contributions to the subject. Firstly, the paper proposes a conceptual explainability framework emphasizing sample-specific, time-specific, and feature-specific explanations interpretable by humans. Secondly, the paper provides empirical evaluations of novel explainability methods for transformer-based detection models, using occlusion and attention visualization techniques. The occlusion method masks out sections of a mel-spectrogram to reveal which parts are most important for final classification. The attention visualization technique and roll-out method are utilized to get a distribution of attention across all layers and can be used to point out parts of the input sequence most relevant for the final classification. Finally, the paper also introduces a novel framework to evaluate the generalizability of deepfake classifiers, where models are trained on one dataset but evaluated on another dataset.

### Strengths
1. The paper is very well written, the concepts are easily understood and the limitations of the work are discussed as well.
2. The subject of explainability in audio deepfake detection is a significant and timely problem, especially as deepfake generation technology is readily accessible to the public and has a high capacity of being misused. Research into this subject is very important due to the impact on society this technology can have.
3. The paper makes a difference between interpretability and explainability and proposes that explainable methods should provide interpretable explanations that are sample-specific, time-specific, and feature-specific. This robust definition of explainability would ensure greater applicability of these methods to interpret black-box models.

### Weaknesses
1. Both the proposed methods for audio explainability, occlusion and attention visualization, are already existing methods that are very common in literature, especially for vision and language tasks. This is also recognized by the paper, which mentioned that their contribution is porting the methods to the audio task. But to do that, the paper didn't make any modality-specific changes to the methods or edit the methods in any way. For the occlusion method, it's well-known that mel-spectrograms can be treated as images and the paper directly used them on the traditional method. For the attention-visualization method, this is modality agnostic and is based on transformer architecture which takes tokens as input. The roll-out attention method was introduced for natural language tokens and the paper claims to adapt the method for audio tokens, but it's unclear what kind of modifications they did except just replacing the tokens. So the novelty introduced by the paper in these methods is questionable.
2. The paper provided the results of their methods in Figure 4 and Figure 5. First of all, the paper understands that the result in Figure 4 doesn't help explain the model's decision-making (line 420) and instead is suggestive of transformer model behavior. Second of all, the result in Figure 5 is also not very helpful in human interpretation. When these methods are applied to a visual or textual domain, a human can more easily interpret the segment and decision-making rationale. This suggests that more work needs to be done in the audio domain to make the results more human-interpretable. These observations are also recognized by the paper in their limitation section. So the usability of these methods is questionable.
3. The paper claims to introduce a novel benchmark to evaluate the generalization capabilities of deepfake audio classifiers, where they train the model in the ASVspoof5 dataset and evaluate it on the FakeAVCeleb dataset. Here the only contribution of the benchmark is training on one dataset and evaluating on another dataset. This mechanism is already well-known and well-practiced to show the generalization capability of a model to out-of-domain datasets. Here, there is no contribution to the dataset, no new evaluation metric is introduced or any other changes are proposed. Thus, it's questionable to consider this benchmark as a contribution. The abstract also claims to "open-source a novel benchmark for real-world generalizability". The question is what is there to "open-source" here, as the datasets are already available.

### Questions
1. What is the technical novelty contribution of the paper's usage of existing explainability methods? Were any changes needed to adapt these existing methods for audio classification? Why not introduce modifications that can take advantage of features specific to audio modality?
2. The result of the explainability methods didn't seem helpful for explaining model behavior. Can you provide more insights regarding this? For example, a concrete deepfake audio sample and its corresponding outputs for explainability and your analysis that will help reason about model behavior? Also, it would be helpful if a scenario is provided where the techniques are useful in practice and have a big impact on our understanding of a model's capabilities.
3. Why is the benchmark considered a novel contribution? This kind of evaluation is very common in deep learning models.

### Soundness
1

### Presentation
3

### Contribution
1
