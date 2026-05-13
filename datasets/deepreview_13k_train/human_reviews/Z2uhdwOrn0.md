# SPARQ: Outlier-free SpeechLM with Fast Adaptation and Robust Quantization

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
We propose SpARQ (outlier-free SpeechLM for Fast Adaptation and Robust Quantization) to address the outlier problem in Speech and Language multi-modal Models (SpeechLMs). Our primary observation is that outliers stemming from cross-modal (speech and text) low-rank adaptation and post-training quantization stages affect the performance of the current SpeechLMs. Methodologically, SpARQ leverages a pretrained language model as its foundation, substituting the traditional attention layer with a novel stabilized outlier-free layer. This modification eliminates outliers typically arising during cross-modal low-rank adaptation and post-training quantization. The model is then fine-tuned on multi-modal data using this outlier-free architecture, allowing it to handle textLM, speechLM, ASR, and TTS tasks through a unified interface while maintaining compatibility with parameters adapted from standard pretrained LLMs. Consequently, on the OPT-1.3b model, the proposed framework achieves relative performance improvements: 41\% in cross-modal low-rank adaptation and 45\% in post-training quantization, along with a 1.33x training speedup. We benchmark it against state-of-the-art low-rank adaptation and post-training quantization methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose a way to integrate text and speech into a one single model where outliers do not have a significant impact on the modeling.

### Strengths
Good empirical performance and reasonable model structure. 
Theoretical analysis presented in the appendices is also appreciated, even though most are from previous papers. But for completeness it is good to have them there.

### Weaknesses
I am puzzled but this paper. It is well written, experimented and mathematized. But the central claim about the outliers is not clearly presented and it is not theoretically pursued! As an example, I would have expected that at least following things would be easy to find in the paper, taking into account that the keyword "outlier" is in the title: 
1. Definition of the outlier in the context of the paper. Especially considering that classical definition of outlier in statistics and ML is that observation is _not_ from the distribution that is being modeled. 
2. Explaining theoretically why Eq. (3.2) is resistant to outliers as defined in the 1. 
3. Show in experiments explicitly that this indeed happens in practice also. Noting that this is different to showing general performance of the model in some downstream tasks.

### Questions
- What is meant by "Given this challenge, we would like to develop a transformer architecture that can efficiently solve
the challenge in Equation (3.1). "

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper, "SpARQ: Outlier-Free SpeechLM with Fast Adaptation and Robust Quantization," tackles a major hurdle in Speech and Language Models (SpeechLMs): the disruptive effects of outliers in multi-modal settings. To address this, the authors present SpARQ, a framework that replaces traditional attention layers with a mechanism specifically designed to handle outliers. This innovation helps overcome challenges in cross-modal low-rank adaptation and post-training quantization, resulting in a more efficient and accurate approach to tasks like Automatic Speech Recognition (ASR) and Text-to-Speech (TTS). The goal is to streamline training while improving performance across these applications.

### Strengths
Innovative Approach: SpARQ introduces an outlier-free layer within the SpeechLM architecture, a novel solution to the inefficiencies caused by outliers that often hamper model performance and computational effectiveness.

Enhanced Performance: The framework brings notable improvements to Automatic Speech Recognition (ASR) and Text-to-Speech (TTS) tasks, showing a remarkable 41% boost in cross-modal adaptation and a 45% gain in post-training quantization accuracy.

Training Efficiency: With a 1.33x increase in training speed, SpARQ is well-suited for environments with limited computational resources, making advanced applications more accessible.

Thorough Evaluation: The model’s effectiveness is rigorously tested across various quantization and adaptation techniques, establishing a strong empirical basis for its success.

### Weaknesses
Testing Constraints: The paper notes that due to computational limitations, the model hasn’t been tested on extremely large models, such as OPT 6.7B. This restriction could affect the generalizability of results for larger-scale applications. The absence of empirical validation on models of this scale leaves open the question of whether the observed performance gains will hold, particularly given the potential for emergent behaviors and different scaling properties in larger models. It is unclear if the outlier-free layer will continue to provide the same benefits when the model size and complexity increase significantly.

Architectural Complexity: The architecture includes several layers and a specialized stabilization method, which could make practical implementation challenging without advanced technical expertise. The introduction of a novel outlier-free layer, along with the max-shift normalization, adds to the complexity of the model, potentially increasing the difficulty of debugging and fine-tuning. The paper does not provide sufficient details on how these additional components interact with existing transformer layers, making it unclear how to integrate this approach into existing pipelines. The reliance on a specific stabilization method, max-shift normalization, also raises concerns about the robustness of the approach if this method is not optimal for all scenarios.

Risk of Bias Amplification: Although not deeply explored, the framework’s emphasis on reducing computational demands might unintentionally increase biases inherited from pre-trained models, given the reduced resources available for extensive fine-tuning. By prioritizing computational efficiency, the framework may inadvertently limit the capacity for fine-tuning, potentially leading to the amplification of biases present in the pre-trained model. The paper lacks a thorough analysis of the potential impact on fairness and equity, particularly in sensitive applications where bias amplification could have significant consequences.

### Questions
Given the computational limitations that prevented testing with larger models, how might SpARQ perform when scaled up to models with billions of parameters, such as OPT-6.7B? Are there specific architectural adjustments needed to maintain stability and performance at this scale?

Several stabilization methods are compared in the paper, with max-shift normalization performing best. What were the primary reasons for choosing max-shift, and are there conditions under which other methods (like L1 or mean-centering) might be more effective?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces SpARQ, an outlier-free framework designed to address performance degradation in SpeechLMs by mitigating outliers. SpARQ replaces the standard attention mechanism with a stabilized, outlier-free layer that improves the model's adaptability in cross-modal tasks and enhances post-training quantization robustness. Built on the OPT model, SpARQ demonstrates resilience to outliers and offers performance gains across several tasks, such as textLM, speechLM, ASR, and TTS.

### Strengths
1. The paper addresses an important challenge induced by the outliers in multimodal attention mechanisms, particularly in SpeechLMs.
2. The stabilized outlier-free layer demonstrates effective mitigation of outliers during cross-modal low-rank adaptation and quantization, showing promise for real-world SpeechLM applications.

### Weaknesses
1. The primary contribution of this paper is the integration of the Outlier-Efficient Hopfield Layer with max-shift normalization, which limits the originality of SpARQ. While this is the first application of outlier mitigation specifically within SpeechLMs, the Outlier-Efficient Hopfield Layer itself was previously introduced by Hu et al.
2. Techniques like Clipped Softmax and Gated Attention are potential alternatives but were not included in comparisons. Experimental results of adapting them to the SpeechLM setup would further validate SpARQ's relative effectiveness.
3. It remains unclear how much of SpARQ's improvement is attributable to the outlier-free Hopfield layer itself versus the max-shift stabilization. An additional experiment applying the stabilization module to a standard Transformer would help clarify the effectiveness of SpARQ's contributions.
4. The author states that outliers negatively impact LoRA and quantization performance. Yet, in some cases (e.g., With OPT-350m), QLoRA performs better than LoRA. Clarification on this result would improve understanding.
5. Previous studies (e.g., “Robust multimodal models have outlier features and encode more concepts” by Crabbe) mention that outlier features increase robustness for out-of-domain (OOD) samples, but OOD evaluations of SpARQ are missing. Demonstrating SpARQ’s performance on OOD data would add value to this paper.
6. There is insufficient analysis in the ablation study to explain why the max-shift stabilization uniquely works in SpARQ.
7. In Equation 3.2, the notation "S = S - max(S)" should clearly distinguish between the normalized and original versions of S.

### Questions
1. Why does fully fine-tuned SpARQ generally show worse performance than fully fine-tuned Vanilla, despite the claim that multimodal samples have more outliers that degrade performance?
2. What is the number of trainable parameters for LoRA in the tables presented in the paper?
3. Do Table 1 and Table 2 reflect experiments with only PTQ and LoRA, respectively? If so, what are the results when applying PTQ on the LoRA-trained SpARQ? Including these results would clarify the model’s performance when combining the techniques.

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
4

### Summary
This paper proposes to use the outlier-free layer within the attention to reduces the occurrence of weight outliers for quantization and LoRA adaptations with a SpeechLM model. The outlier-free layer is constructed by replacing the first softmax layer with a layer that uses S = S - max(S) as the input, where S is the original input vector. The authors conducted three sets of experiments to validate the proposed approach: quantization, LoRA, and ablation studies / analyses.

### Strengths
* Although the novelty is a combination of existing works (SpeechLM + outlier-free layer), the combination seems to be novel. The authors also provided systematic theory support for the proposed approach.
* The organization of paper is good. Paper writing is good. References are enough.

### Weaknesses
 * Quantization experiments: A common approach to remove outliers in quantization is to do clipping. For example, ignore the 5% tail weight values during computing the quantization scale. It’d be helpful to include this as a baseline to correctly validate the effectiveness of the proposed work. It's important to clarify that clipping during quantization typically refers to excluding outlier values when calculating the quantization scale, not directly clipping the weights themselves. The current experiments seem to implement a form of clipping that removes attention values exceeding a certain threshold, which is not standard practice for quantization and may explain the performance regressions observed. This difference in implementation needs to be addressed to properly assess the proposed method's effectiveness against standard quantization techniques.
* LoRA experiments: rank=128 seems to be large. Please add the percentage of adapter size compared to the full model.
* LoRA experiments: I would also suggest to separate the experiments to two fold, if LoRA+Quantization is one of the focus on this work. In a first experiment, we can investigate the impact of LoRA (with FP 32/16). In a second experiment, we investigated the confounding effect between LoRA and quantization (should be more aggressive than just INT8).
* Table 2: Why are the ASR WEB numbers of vanilla -125M model much better than 350B and 1.3B. Is it because the rank is set to 128 across the board? If so, the experimental setup is problematic. When applying LoRA, the rule of thumb is to control the adapter size to be under a certain percentage.
* Table 3: where does the training efficiency improvement come from? Does it require fewer steps to converge? Or is it quantization?

### Questions
See weaknesses section. I'm happy to increase my ratings if my concerns can be addressed.

### Soundness
2

### Presentation
3

### Contribution
3
