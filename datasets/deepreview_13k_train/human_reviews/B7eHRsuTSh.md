# Revisiting Noise Resilience Strategies in Gesture Recognition: Short-Term Enhancement in Surface Electromyographic Signal Analysis

- Decision: Reject
- Scores: 3, 8, 5, 6, 6

## Abstract
Gesture recognition based on surface electromyography (sEMG) has been gaining importance in many 3D Interactive Scenes. However, sEMG is easily influenced by various forms of noise in real-world environments, leading to challenges in providing long-term stable interactions through sEMG. Existing methods often struggle to enhance model noise resilience through various predefined data augmentation techniques.
In this work, we revisit the problem from a short term enhancement perspective to improve precision and robustness against various common noisy scenarios with learnable denoise using sEMG intrinsic pattern information and sliding-window attention. We propose a Short Term Enhancement Module(STEM) which can be easily integrated with various models. STEM offers several benefits: 1) Learnable denoise, enabling noise reduction without manual data augmentation; 2) Scalability, adaptable to various models; and 3) Cost-effectiveness, achieving short-term enhancement through minimal weight-sharing in an efficient attention mechanism.
In particular, we incorporate STEM into a transformer, creating the Short Term Enhanced Transformer (STET).
Compared with best-competing approaches, the impact of noise on STET is reduced by more than 20\%. We also report promising results on both classification and regression datasets and demonstrate that STEM generalizes across different gesture recognition tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a Short Term Enhancement Module (STEM) to improve noise resilience in sEMG-based gesture recognition. The results show that the proposed method performs the best, both with and without additive noise, on the publicly available EMG dataset, GRABMyo.

### Strengths
Gesture recognition using sEMG is a significant field with applications in prosthetic control and rehabilitation.  Extensive experiments have been conducted in this work. The inclusion of code is appreciated. However, clearer instructions are needed.

### Weaknesses
Cons
- There are a few novel components here, but I don't find the combination especially well developed or compelling. It is likely the case that their combination of masking, parallel coarse and fine transformers and asymmetric losses improves performance but the intuition advances is a little ad hoc. Unsupervised pretraining might help, but likely not by reducing gaussian noise in the signal. It is unclear whether the short of long term components are more important for affecting different types of gestures, it is not clear what window sizes are important. There are experiments oriented at some of these, but they don't quite get to the bottom of things. 

- It is unclear if the developed approach can be run online, and how it performs in the most important generalization domain for sEMG, across novel participants. So in practice I am not sure how useful this approach is. 

- Given the lack of documentation of hyperparameters for all models (see below) or statistics it is hard to evaluate the results critically. 

- The novelty of the long and short timescale approach is questionable. As they note, other manuscripts in the literature use this approach eg L262 claims that these long and short timescales are run in serial in LST-EMG-Net, but based on Figure 3 of Zhang et al 2023 they appear to be run in parallel. 

- The added gaussian and multiplicative noise experiments are not especially convincing to me as a realistic noise aggressor for sEMG, where the predominant failure mode is generalization across participants or issues like contact loss or power line interference. Given that the masking approach only improves accuracy by 0.6-1% in the GrabMYO data, it seems like these noise sources are not large. I find the noise discussion is a bit of a digression from the rest of the manuscript. 

- The related work section can be better organized, and the novelty and distinction between the architectures can be better presented in the related work, rather than throughout the text and appendix.

### Questions
See comments in the 'Weakness' section above. The current version of the manuscript is not satisfactory, but I am willing to raise my score if the authors can address any of my major concerns.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Surface Electromyography (sEMG) is highly susceptible to noise in real-world environments. To enhance noise resilience in sEMG-based models, this paper presents three key contributions:
1) introduction of the Short-Term Enhancement Module (STEM): A scalable, learnable, and low-cost module that enhances noise resistance. When integrated into neural networks, STEM improves performance by focusing on short-term signal features critical for distinguishing gestures amidst noise.
2) Self-Supervised Signal Masking: This technique leverages intrinsic variability in sEMG signals to enhance pre-training, allowing the model to learn robust representations without requiring extensive labeled data.
3) comprehensive Evaluation on the GRABMyo Dataset: Experiments on the largest available wrist sEMG dataset, GRABMyo, demonstrate that the Short-Term Enhanced Transformer (STET) achieves superior accuracy and robustness compared to existing methods, with reduced accuracy drop rates under noise and more precise gesture classification boundaries.

### Strengths
1) to address the risk of self-supervised learning fitting to ineffective patterns and missing meaningful temporal semantics, the authors introduce a sophisticated masking strategy. This approach uses a geometric distribution to control masked and unmasked segments, promoting more robust temporal feature learning and improving the model's ability to capture essential sEMG patterns.
2) the authors propose a dual-decoder approach that extracts both long-term and short-term dependencies within the signal sequences. The long-term decoder captures the global context and overall signal structure, while the short-term decoder focuses on specific local characteristics critical for accurate gesture differentiation, enhancing both precision and robustness.
3) an asymmetric loss function is introduced to address class imbalance and improve model optimization by emphasizing difficult samples. This loss function enhances the model's ability to generalize across varied gesture categories, prioritizing accurate classification for challenging cases without overfitting on easy negatives.
4) the paper is well-structured and logically organized, with clear presentation of theorems, statements, and methodological components. The writing is precise and effectively communicates the technical contributions, making the model and findings accessible to readers.

### Weaknesses
1) The experimental evaluation presents classification results solely on the GRABMyo dataset, which may introduce dataset bias. To improve the robustness and generalizability of the findings, it would be beneficial to include experiments on additional publicly available datasets.

### Questions
1) The authors claim that the proposed STEM module is low-cost; however, the paper lacks a detailed description or analysis of the module's computational efficiency. Could the authors clarify how they evaluated STEM's efficiency and provide comparative metrics or benchmarks to substantiate its low-cost nature? Additionally, how does STEM’s computational cost compare to other common noise resilience approaches?

### Soundness
3

### Presentation
3

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
This manuscript proposes a new framework for gesture recognition and regression from sEMG signals. They two existing datasets, GRABMyo and Ninapro that record sEMG alongside gesture identity and finger joint angles and develop a framework, STET, to process the signals. STET combines a pre-trained masked autoencoder with two transformers that are designed to process short term and long term information in parallel. These signals are concatenated, and in the case of gesture recognition, use a new asymmetric loss to upweight positive samples. The approach is thus a combination of novel components, although there is considerable past precedent for these approaches in the literature (eg LST-EMG-Net for separately modeling long and short term context and CutMix for time and channel wise masking of temporal signals). The experiments compare accuracy for gesture classification with a variety of baselines and perform ablations of different network components. They perform separate experiments simulating the addition of noise.

### Strengths
- The approach appears to be novel. While I am somewhat surprised that this approach would be better than a single transformer with a variety of temporal scales, it is reminiscent of other work in CV integrating different spatial context.
- The ablations are thorough, and there are numerous baselines.
- The pretraining appears to reduce the effects of additive and multiplicative noise.
- the application domain is timely and interesting

### Weaknesses
Cons
- There are a few novel components here, but I don't find the combination especially well developed or compelling. It is likely the case that their combination of masking, parallel coarse and fine transformers and asymmetric losses improves performance but the intuition advances is a little ad hoc. Unsupervised pretraining might help, but likely not by reducing gaussian noise in the signal. It is unclear whether the short of long term components are more important for affecting different types of gestures, it is not clear what window sizes are important. There are experiments oriented at some of these, but they don't quite get to the bottom of things. 

- It is unclear if the developed approach can be run online, and how it performs in the most important generalization domain for sEMG, across novel participants. So in practice I am not sure how useful this approach is. 

- Given the lack of documentation of hyperparameters for all models (see below) or statistics it is hard to evaluate the results critically. 

- The novelty of the long and short timescale approach is questionable. As they note, other manuscripts in the literature use this approach eg L262 claims that these long and short timescales are run in serial in LST-EMG-Net, but based on Figure 3 of Zhang et al 2023 they appear to be run in parallel. 

- The added gaussian and multiplicative noise experiments are not especially convincing to me as a realistic noise aggressor for sEMG, where the predominant failure mode is generalization across participants or issues like contact loss or power line interference. Given that the masking approach only improves accuracy by 0.6-1% in the GrabMYO data, it seems like these noise sources are not large. I find the noise discussion is a bit of a digression from the rest of the manuscript. 

- The related work section can be better organized, and the novelty and distinction between the architectures can be better presented in the related work, rather than throughout the text and appendix.

### Questions
- The data collection done for the robustness analysis is unclear. Is it the experiment described in Figure 6? Similarly, it is unclear if the methods in ‘dataset’ section describe data collected for this work or different work
- How were hyperparameters determined e.g. the short window length, for this dataset? what about the hyperparameters for the other baselines? what was the train/test/validation strategy? Was the data tested on held out users or held out gestures within a user? What fraction of data was used for the unsupervised pretraining? 
- How was the model run online in a streaming fashion? Is the architecture benchmarked offline the same as run online? 
- Is it the short term or long term e.g. for table 3 what is the breakdown by gesture.

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
This paper proposes an innovative solution for improving sEMG-based gesture recognition, tackling issues such as noise interference and distinguishing similar gestures, especially in non-laboratory settings. The authors introduce the Short-Term Enhancement Module (STEM), which captures local signal variations to maintain noise resistance, and a self-supervised sEMG Intrinsic Pattern Capture (EIPC) for pre-training and learning intrinsic signal patterns. STEM is designed to be easily integrated into various time-series deep learning models. Experiments show it significantly improves performance in classification and regression tasks, making it suitable for practical applications.

### Strengths
The paper is well-written and structured clearly, making it easy to follow.
The parallel use of both long-term and short-term decoders is an innovative approach that preserves context without losing important information from different stages in the sequence. This approach helps address limitations in existing sEMG models and presents a new way of combining local and global signal features, adding originality and significance to the field.
The self-supervised pre-training method effectively reduces the need for extensive labeled data and boosts the model's generalization, making it practical for real-world applications.
Additionally, the emphasis on noise robustness, a common challenge in sEMG signal processing, enhances the model's real-world applicability.

### Weaknesses
Insufficient Methodological Rationale: The paper would benefit from more detailed explanations for certain design choices, such as the selection of the window size in the short-term decoder and the masking ratio in the EIPC module. Clarifying how these parameters were optimized or chosen could strengthen the methodological foundation.

### Questions
1. On line 80, the authors state, *“we show that the long-term and short-term features are complementary in sEMG-based gesture recognition tasks.”* While the methodology section explains these concepts, it would improve reader clarity if a brief explanation of short-term and long-term features were included earlier in the paper.
2. Please clarify the rationale behind the choice of a sensor-wise masking strategy over other potential approaches, and how this decision impacts the model’s ability to generalize to various sEMG signal conditions.
3. Please provide more detail on why the specific masking ratio (0.15) and the average length of masked segments were chosen. Also, please add explanation of the sensitivity of the model’s performance to these parameters.
4. Could the authors explain why a multi-head self-attention layer was chosen for the long-term decoder and a sliding-window self-attention layer for the short-term decoder. 
5. For the sliding-window self-attention, how was the window size determined, and how sensitive is the model’s performance to variations in this parameter?
6. Please clarify how normalization was performed for the NRMSE (Normalized Root Mean Squared Error) metric.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the task of gesture classification and hand joint angle prediction from sEMG signal from a multi-electrode array. Specifically, the authors make three main contributions: 1)  Self-supervised pre-training based off of a signal masking objective 2) The introduction of short-term and long-term modules which are fused to create a final prediction 3) Use of asymmetric loss function to address asymmetries to address the imbalance between positive and negative samples.
The self-supervised pre-training step enables training on unlabeled EMG signals which is valuable given the sparse state of labeled EMG datasets. The self-supervised objective consists of reconstruction of masked signals, its loss denoted by MSE. The masks were constructed such that contiguous chunks of signal are masked at once, as otherwise neighboring signal timestamps make the objective too simple.
The short-term and long-term modules are both transformer-based models. The main difference between the two is that for the short-term module, the attention is limited within a certain window size. This forces the model to focus only on this short-term context to perform predictions.
The asymmetric loss follows Ridnik et al., and was introduce after making the observation that the positive and negative samples given a gesture is severely unbalanced in favor of the negatives.
Experimental results demonstrate improved performance over related work. Ablation studies show improved robustness to artificially added noise, as well as the improvement each proposed component gives.

### Strengths
- Thorough empirical investigation of their proposed approach with various ablation studies
- Comparisons to related work show SotA performance
- Approach tested on both hand joint angle prediction as well as gesture classification
- Statistical significance test performed, which isn't common but valuable (appendix)
- Combination of their proposed approach with prior works architecture demonstrates generalizability of the improvements (e.g TEMGNet 78% vs TEMGNET+STEM 84%)

### Weaknesses
- Although the long term module has been empirically validated to show improved performance I would've liked to see better explanation / investigation on what kind of information is being stored in long term vs short term module. EMG inherently encodes force and gestures are performed on a short time scale. Therefore it is not immediately clear to me why the long term module improves performance
- In similar manner, the ablation study demonstrates the performance of one module over the other and over their combined performance, where the combined performance yields the best results. However, one could also conclude from these results that having an extra module is what lead to the improved performance (i.e extra model parameters), and not the the type of module. To that end, how would the model perform with two LT or ST units and how does that compare to the fused variant?

### Questions
- L035-036: motoring -> monitoring
- L240-241: slide -> sliding
- What kind of information does LT vs ST store?
- Could the author clarify what kind of data pre-training was done on vs. fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3
