# LLM-VTP: LLM-Reasoned Visual Token Pruning for Efficient Multi-Modal Video Understanding

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 8, 6, 5, 5

## Abstract
In this paper, we introduce LLM-VTP, a visual token pruning method designed to enhance the efficiency of multi-modal video understanding. Large Language Models (LLMs) have shown promising performance in video tasks due to their extended capabilities in comprehending visual modalities. However, the substantial redundancy in video data presents significant computational challenges for LLMs. To address this, we propose a training-free approach that leverages the inherent reasoning abilities of LLMs to selectively prune visual features based on question tokens, thereby optimizing model efficiency. We validate our method across multiple-choice, open-ended, and text-generation benchmarks. Our results demonstrate that LLM-VTP can prune 80\%-90\% of tokens while maintaining competitive performance. This highlights its superior effectiveness and efficiency compared to existing pruning methods. The source code will be released to facilitate future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a new method to improve the inference efficiency of LLMs for long video understanding. The core idea of the paper is very straightforward. Due to the redundancy of the video data, the LLMs do not need to process every token from the video sequence. By pruning video tokens, the inference speed of the LLMs can be improved. The criteria for pruning used by the paper is the learned attention weights between the query questions and extracted video tokens. In combination with techniques such as KV cache, the paper is able to achieve 1.4x faster inference speed without sacrificing the accuracy. Experimental results are provided using two baseline LLMs (PLLaVA and Tarsier).

### Strengths
The idea of the paper is very intuitive and straightforward, and can also generalize to different LLMs which make the paper more applicable in real-world applications.

The paper provided thorough experimental results and ablation study to justify the effectiveness of the proposed method.

The writing of the paper is clear and easy to follow.

### Weaknesses
Based on the results from Figure 3, the choice of the target layer M seems to be very sensitive. It also seems to be data dependent as well. This makes it tricky to pick a proper M without extensive experiments, which defeats the whole purpose of a training-free approach. Specifically, the optimal M value appears to vary significantly across different datasets and even within the same dataset when using different models. This variability makes it difficult to establish a general guideline for selecting M, potentially requiring a computationally expensive grid search for each new application. The lack of a clear, principled method for choosing M undermines the practical utility of the proposed approach, as it introduces a hyperparameter tuning step that is not easily automated or generalized.

The paper motivated the idea from the application of the long video understanding. However, the paper didn’t provide any analysis about how well the method works on long videos. The experiments are primarily conducted on relatively short video clips, and it remains unclear whether the proposed token pruning strategy is effective for longer video sequences where temporal dependencies and information redundancy might be more complex. The absence of experiments on long videos limits the scope of the paper and raises questions about the general applicability of the method to the specific use case that motivated its development.

### Questions
Please consider addressing my questions in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
LLM-VTP is a training-free visual token pruning method that enhances multi-modal video understanding efficiency by leveraging LLMs' reasoning abilities to selectively prune visual features based on questions, reducing 80%-90% of tokens while maintaining competitive performance.

### Strengths
The paper introduces LLM-VTP, a simple yet effective, training-free framework that prunes video tokens by leveraging LLMs' ability to locate question-specific visual tokens from shallow layers, enhancing multi-modal video understanding efficiently without compromising performance, and demonstrating superior results across multiple benchmarks.

### Weaknesses
Impaired Relative Position Understanding: The proposed method appears to diminish the model's ability to capture relative positional information. This is indicated by performance drops in the Object Spatial (OS) and Motion Direction (MD) metrics on the MV-Bench dataset for both PLLaVA with the proposed approach and Tarsier with LLM-VTP. The method's reliance on attention mechanisms to identify salient tokens for pruning seems to prioritize object-centric features, potentially neglecting the contextual information crucial for understanding spatial relationships and directional changes. This is particularly concerning because the model's ability to discern relative positions is fundamental for many video understanding tasks, such as action recognition and scene understanding. The observed performance degradation suggests that the pruning process may be inadvertently discarding tokens that encode vital positional cues, leading to a loss of spatial awareness. Could the authors explain why the method lacks proficiency in calculating relative positions? If the method is effective in this aspect, please provide experimental evidence or references that support this capability.

Evaluation on Long-Form Video Understanding: The paper does not address how the proposed model performs on long-form video understanding tasks, which require the model to handle challenging temporal complexities. The current evaluation focuses primarily on relatively short video clips, which may not fully expose the limitations of the pruning strategy when dealing with extended temporal dependencies. Evaluating the method on datasets containing very long-form videos, such as a subset of EgoSchema, and comparing it to the original models like Tarsier, would provide valuable insights into whether localization by attention and pruning is sufficient to induce long temporal relations. Such an evaluation would demonstrate the model's applicability and effectiveness in handling extended video sequences, highlighting its strengths or revealing areas for improvement. The lack of experiments on long-form videos leaves a gap in understanding the method's scalability and robustness in real-world scenarios where videos often span several minutes or even hours.

### Questions
I asked questions in the weakness section.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces LLM-VTP, which leverages the ability of LLMs to identify useful visual signals for pruning visual features. Experiments on two video LLMs and multiple video understanding tasks validate that this method can effectively reduce the number of tokens without compromising model performance.

### Strengths
1. This paper is well written. 
2. The proposed method is training-free and small computational burden.

### Weaknesses
1. What is the performance of this method in long videos or scenes with drastic changes in temporal?
2. The author should verify the validity of the method on more different types of backbone.
3. The comparative experimental Settings of some tables require further clarification. For example, in Table 1, under the Tarsier method, why is 20% Retained Ratio retained? If 10% is retained, what are the relevant experimental results? In Table 2, under PLLaVA and Tarsier, the Retained Ratio is 20%. So what does that look like for the 10 percent? In Table 3, the comparison methods are all based on PLLaVA. Why does the authors express their own method as Tarsier w/LLM-VPT (Ours)? So what do all the comparisons look like under the same method?
4. The author lacks in-depth analysis of many experimental phenomena. For example "However, the choice of which layer's attention weights to use differs across datasets."

### Questions
Please see the weaknesses.

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
This paper proposes LLM-VTP, a training-free token pruning method for multi-modal video understanding.
Specifically, authors uses the attention score between question token and visual tokens to select semantically related tokens. 
Authors integrate LLM-VTP with two Video LLMs, i.e., PLLaVA and Tarsier and conduct experiments on several benchmarks including MVBench, MSVD-QA, MSRVTT-QA, ActivityNet-QA, TGIF-QA and VideoChatGPT-Bench. 
Results show that LLM-VTP reduces sequence length of the transformer while maintaining a comparable performance.

### Strengths
- The motivation is clear, i.e., using question related visual tokens to prune redundant tokens.
- Experiments are conducted on various benchmarks, demonstrating the effectiveness of LLM-VTP.
- The research topic, i.e., video LLM pruning, has real-world application potential which is valuable.
- On MVBench, the pruned video LLM model even show a better performance compared with the original model.

### Weaknesses
 -The proposed method uses an encoder to extract all video tokens, a process that is significantly more computationally expensive than reducing tokens in subsequent layers. Reducing tokens post-attention is largely ineffective, as the necessary feature information is already captured by other tokens.
- Is the ablation study of different alpha parameters conducted using PLLaVA? Does similar results appear for Tarsier?
- Does LLM-VTP work on other models like ST-LLM, VideoChat, etc. One concern is that for different models, authors select different hyperparameters for token selection ratio and model layer. This might restrict the generalization ability of LLM-VTP.
- Why Table 3 compares LLM-VTP on Tarsier with other methods on PLLaVA? Is it fair as the alpha and M are different in the two video LLMs.
- For the Figure 4 and Figure 1 (b), the highlighted activation area in different layers are quite similar, then what leads to the performance variance between pruning different layers?

### Questions
see the weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a video LLM that focuses on visual token pruning. While previous work has used training-based approaches to reduce redundancy in video data, the authors consider them suboptimal due to the lack of question-specific designs. They develop a training-free pruning method based on attention scores between questions and video tokens. In particular, only the top-ranked video tokens are retained and the KV cache is compressed accordingly, which significantly reduces the computational cost. The proposed method is validated with two video LLMs on multiple video understanding benchmarks, showing significant speedup by pruning 80-90% of the tokens with competitive performance.

### Strengths
* The paper is generally well written and easy to follow.
* The authors' analysis of the current limitations of visual token pruning approaches is reasonable, and the proposed approach directly addresses these limitations.
* Extensive quantitative and qualitative results are provided to support the effectiveness of the proposed method.

### Weaknesses
 * The "LLM-reasoned" in the tile is an overclaim. While LLMs have demonstrated impressive reasoning capabilities, they are not explicitly utilized in the paper. There is also a lack of evidence or further analysis to prove that the LLM has implicitly reasoned about how to prune the visual tokens. The visualizations in Figure 1b and Figure 4 may be the authors' attempts to illustrate this, but they seem too vague for me to draw any conclusions.
* Limited technical contribution. Both token pruning and KV compression are widely used techniques in (multimodal) LLMs, and the proposed approach through attention score-based top-$α\%$ selection does not seem to be a significant contribution. This strategy should be sensitive to the hyperparameter $\alpha$ and might fail on certain videos with more dense information.
* The comparative results with PruMerge and Look-M in Table 2 are mixed. The proposed method does not always achieve a better performance-efficiency tradeoff than the baselines, and there is no intuitive summary of the comparison. The authors have provided some explanation in lines 362-371, but they do not fully address these concerns.
* The retained ratio may not be not a good metric because it does not consider token merging as an effective strategy for reducing computational cost. For token merging, the authors only mentioned that "merging the less informative tokens actually negatively impacts performance" in line 485, which is not a very solid argument since the result is only obtained from a single comparison. It would be better if additional metrics such as FLOPS are included to provide a comprehensive analysis of computational efficiency.

### Questions
* Could the authors provide visualizations of which tokens are pruned by their ranking-based selection strategy? Perhaps in the form of a side-by-side comparison of the original and pruned attention heatmaps. This would make the results more intuitive.
* Could the authors tune the hyperparameters for the PruMerge baseline and compare with it on the same retained ratio? I cannot tell if the performance disadvantage of the proposed method is due to a higher compression rate or some weakness of the method.

### Soundness
3

### Presentation
2

### Contribution
2
