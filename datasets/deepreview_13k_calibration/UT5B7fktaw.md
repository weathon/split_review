# Variational Inference for Self-Supervised Speech Models Fine-tuning on Downstream Tasks

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
Despite the growing interest in self-supervised speech models, recent research has primarily focused on modifying upstream model architectures and pretraining techniques, with less attention given to how features from self-supervised models are used. In this paper, we explore the use of variational inference to enhance the performance of self-supervised audio models in downstream tasks. We hypothesize that adaptively reweighting the outputs of the model layers is crucial to improving performance on these tasks. We extensively evaluate our method alongside widely used baselines, demonstrating that understanding sample-specific information is essential for improved performance on several tasks. Our proposed method surpasses existing approaches and generalizes to various speech tasks, including automatic speech recognition, speaker verification, and emotion recognition. Finally, we analyze our method to provide deeper insight into the importance of our modifications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces VARAN, an innovative layer aggregation technique for finetuning self-supervised speech models motivated from variational inference field. The authors emphasize that adaptively adjusting the weights of outputs from various model layers based on individual samples is essential for boosting performance in downstream tasks. VARAN generates weights for each layer tailored to the specific sample, achieving superior results compared to existing layer-aggregation methods like weighted sum and layerwise attention pooling (e.g., SV and SER). Additionally, it demonstrates competitive performance on the ASR task.

### Strengths
VARAN adapts the weight of different layers used conditioned on each sample. It is shown to be very effective for the SER task.

### Weaknesses
The authors do not compare VARAN to adapters, which are (i) a more cost-effective finetuning method (involving fewer parameters) and (ii) better suited for adapting models to different downstream tasks, especially when there is limited data available for finetuning. This is demonstrated in the paper, "CHAPTER: Exploiting Convolutional Neural Network Adapters for Self-Supervised Speech Models."

For tasks like ASR, SV, and SER, the performance gains with VARAN may not be as significant compared to adapters, as shown in the CHAPTER paper. Thus, a direct comparison becomes essential to substantiate general claims about VARAN.

Moreover, the reliance on choosing an appropriate prior for each task underscores the importance of understanding what each layer encodes. Tables 4 and 5 demonstrate that selecting the right prior is crucial for achieving performance gains.

### Questions
In Figure 1, how multihead self attention is used is unclear to me. 

Why using data2vec for SER task and not for all the tasks?

Typo in line 34. with these classical >> with classical.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces VARAN, which demonstrates that different layers encode varying levels of information for different tasks. The authors argue that simple weighted summation is insufficient to capture sample variance. To address this challenge, VARAN automatically learns layer posterior distributions and performs tasks (ASR, SR, and ER) on each layer separately. The aggregated results show improved performance compared to using only the last layer.

### Strengths
VARAN adopts variational inference to semi-automatically extract layer-wise information, providing novel insights.


The paper is written in a clear and concise manner, making it easy to follow both the ideas and experiments.


The experimental results support the authors' claims, demonstrating that VARAN outperforms last-layer counterparts in several tasks (ASR, PR, and ER)

### Weaknesses
While the experimental results show interesting findings on common ASR, speaker recognition, and emotion benchmarks, these results are not entirely convincing as they rely on relatively simple benchmarks. For ASR evaluation, more challenging robust benchmarks (as used in Whisper or detailed in https://arxiv.org/abs/2401.10446) would be more appropriate. Overall, the experimental validation appears insufficient.

This limitation is reflected in Table 1, where VARAN fails to outperform weighted combination methods - a drawback explicitly mentioned in lines 53-54. This suggests that VARAN may still 'not account for sample variation and its possible dependence on information from SSL layers.'

The reliance on human knowledge for prior distribution is problematic. Specifically, finding appropriate prior distributions for each task is impractical in real-world applications. Even within a single task like ASR, it's unclear whether a single prior distribution can effectively handle variations across languages, dialects, and noise conditions. This raises questions about the method's practical utility, given that humans already inherently adjust such 'priors' for different tasks.

Several technical details require clarification:

How is discrete variational inference (both prior and posterior) modeled? Is Gumbel-Softmax used? The paper mentions softmax application but lacks implementation details.

The architecture appears to differ between speaker-dependent and speaker-independent tasks - this needs elaboration.
State-of-the-art ASR systems typically incorporate language model integration. Why was this omitted?

In conclusion, while the core idea is interesting, the experimental validation is insufficient to fully support the proposed approach.

### Questions
See Weaknesses

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
This study proposes a novel layer aggregation approach using variational inference. It demonstrates that this method outperforms traditional aggregation strategies across various downstream tasks. By allowing the adjustment of layer importance through a prior distribution, this paper shows that models can be better adapted to task-specific situations.

### Strengths
1. This paper introduces a new layer aggregation method that differs from Multi-head Factorized Attentive Pooling layer aggregation by adjusting the prior distribution to control layer output weight.
2. The experiments and analyses demonstrate that the actual posterior distribution follows the prior distribution, and shows good performance on various downstream tasks.

### Weaknesses
1. The proposed method (VARAN) involves setting a prior distribution for knowledge distillation (KD) learning, which presents the limitation that one must already know the optimal layer weight distribution for each downstream task.
2. In the ASR experiments, the evaluation was conducted using LibriSpeech data, the domain employed in the pre-training. This method does not align with the goal of assessing generalizability, suggesting a need to test with other speech datasets. Furthermore, the use of LibriSpeech, a dataset consisting primarily of read speech, may not adequately represent the diversity of acoustic conditions found in real-world ASR applications.
3. This paper conducted experiments on automatic speech recognition, speaker verification, and emotion recognition. Additional datasets are necessary to demonstrate more generalized performance compared to existing methods. The selection of these three tasks, while diverse, does not fully cover the range of potential applications for self-supervised speech models, such as speech translation or keyword spotting, which could reveal further limitations or strengths of the proposed method.

### Questions
1. How was the prior distribution chosen, and what were the criteria for selecting the non-central Chi-squared distribution?
2. Why were the WavLM and Data2vec chosen among various self-supervised models, and why did you not experiment with other models?
3. In Figure 2, experiments were conducted to set various beta values for the non-central Chi-squared distribution. Is the optimal beta value found simply by grid search, or if another search method was used?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an layer aggregation approach inspired by variational inference. It adds a classifier after each layer along with a final attention layer, and then minimize the variational lower-bound loss to find the best importance distribution for the outputs from each layer. To validate the approach, the authors conducted a series of experiments on SUPERB benchmark, including ASR, speaker verification, and emotion recognition.

### Strengths
* The idea of using variational to generate the impact distribution from all the layer outputs seem to be new and interesting.
* The authors conducted extensive experiments on 3 speech related tasks, along with a set of ablation studies with insightful analysis.

### Weaknesses
 * For ASR evaluations, the WER improvement is too limited. Usually the 2nd digit after the decimal point differences are mostly noise. In this case, it would be helpful to run experiments on other testsets (e.g., common voice, TED-LIUM) to verify if we are actually seeing performance gains.  
* The proposed approach requires running additional multi-headed attention during serving time. How many more parameters are in this layer? What’s the latency impact?
* The presentation needs improvement. Please see my questions below. In addition, the title and abstract sound a bit confusing. The proposed approach is on layer aggregation, but neither the title or the abstract mentioned this.
* From the discussions of question #3, it seems that the proposed approach still needs hyper-params tuning, so this is not an actual benefit compared to prior work. I would suggest to remove this argument from the manuscript to make it a fair comparison to prior work.

### Questions
General question: Is the proposed layer aggregation approach applicable to SSL model? Feels like they can work for models trained from scratch?

Section 2.2: How does it enforce V to learn speaker-discriminative information only, while K has phonetic information?

Section 2.2: The authors mentioned that MHFA requires additional requires searching additional hyperparameters. However, in section 5.2, the regularization weight also needs to be tuned. This doesn’t seem to be a fair comparison to prior studies.

Section 3.1: “Choosing the right layer or combination of layers is challenging, as the training data does not have the optimal layer distribution.” Please explain more on this. Does it mean the empirically learned weights from training data (is it from pretraining or finetuning?) are not exactly the same as their real distribution?

Section 3: Please explain how exactly the proposed method works during inference time. Is it using a weighted average of pooled hidden as the input to the final softmax layer?

Section 4:Please explain the baselines. How are the “weighted” exactly computed?

### Soundness
3

### Presentation
2

### Contribution
3
