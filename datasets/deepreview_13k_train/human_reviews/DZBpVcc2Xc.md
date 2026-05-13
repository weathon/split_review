# HiddenKey: Parameter-Efficient FineTuning Meets Dropout under a Unified Framework

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
The emerging powerful capabilities exhibited by large language models (LLMs) have established them as a fundamental element in various applications that rely on advanced language understanding. At the same time, fine-tuning has become the standard learning approach to adapting LLMs to a concrete application (e.g., instruction tuning, alignment tuning, and task/user-specific specialization). Due to the high cost associated with full finetuning, parameter-efficient finetuning (PEFT) methods, especially LoRA, have gained popularity due to their lower storage, memory, and computation requirements. However, the possible contradiction between limited trainable parameters and the dropout regularization methods (which aim at alleviating overfitting associated with excessive parameter redundancy), has been largely overlooked. With extensive experiments of LoRA-based PEFT, we first confirm that PEFT is also overfitting-prone. We then revisit transformer-specific dropout methods, and validate their equivalence and differences mathematically and empirically. To facilitate a comprehensive comparison, we introduce a unified framework to instantiate them along dropping position, structural pattern and compensation measure, and uncover their new preferences and performance comparisons in PEFT scenarios. This framework also enables us to integrate the best of all into a new dropout method named HiddenKey, which shows performance superiority over existing methods on both NLU and NLG tasks. Compared to baselines, it also achieves better performance with less finetuning time, and offers continuous improvement with further finetuning. These highlight HiddenKey as the better practice for high-performance and parameter-efficient finetuning of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper first shows that LoRA also suffers from overfitting, then develops a unified framework to compare dropout methods in terms of methodology and performance. The authors finally propose HiddenKey, a dropout method with consistency regularization for LoRA by integrating existing methods. Extensive experiments demonstrate the superiority of HiddenKey in many NLU and NLG tasks.

### Strengths
1. The paper comprehensively compares existing dropout methods for transformer models in terms of their gradient behavior, compensation measure, providing valuable insights for method interpretation.
2. The paper provides benchmark results and empirical observations for applying dropout to LoRA, which are useful for future research.

### Weaknesses
1. The technical novelty for the proposed new method is limited. HiddenKey is an integration of existing dropout methods.
2. In Table 1, it is hard to evaluate different patterns based on the results. The values are close and have large variance. This makes the design choice of combining "elementwise HiddenCut" and "column-wise DropKey" a bit arbitrary. It's unclear why this specific combination was chosen over other possibilities given the lack of clear performance differences.
3. In both NLU and NLG experiments, HiddenKey$^-$ does not exhibit a clear gain over the best baselines, and the improvement of HiddenKey is not very significant. The reported improvements are marginal, and it's difficult to ascertain if these gains are consistent or statistically significant. It would be nice to include results on more NLG tasks like wikitext and cnn/dm to demonstrate the method's robustness across diverse tasks.
4. (Minor) The authors only show llama's improvements on two small NLU tasks, which is insufficient to verify the method's effectiveness on generative LLMs. It would be beneficial to show llama's performance on more complex NLG tasks to truly evaluate its potential.
5. (Minor) All claims regarding PEFT methods are only verified on LoRA. It is unclear if the conclusions drawn from LoRA can be generalized to other PEFT techniques, such as adapter-based methods or prefix tuning.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a unified framework for various transformer architecture specific dropout variants (including DropKey, DropAttention and HiddenCut). Then, the authors propose a new dropout scheme called HiddenKey which combines DropKey dropout position and R-drop idea by adding a KL divergence loss between dropout applied and non-applied outputs. The authors use this proposed dropout scheme to LoRA based PEFT setting and show that LoRA training is overfitting and can be improved by HiddenKey technique. The authors show that the proposed approach can outperform LoRA fine-tuning on various NLU and NLG tasks. Finally, the authors present the training loss curves and downstream accuracy curves to show another evidence that LoRA fine-tuning is overfitting.

### Strengths
- The paper summarizes the existing transformer specific dropout methods together and proposes a unified framework to see them as variants with different dropout locations, dropout patterns, and recovery methods.
- The authors show that the proposed method: HiddenKey can (slightly) outperform vanilla LoRA fune-tuning

### Weaknesses
 - There's missing analysis of training cost of HiddenKey. Especially, it uses double forward pass with KL and JS training, there must be memory consumption and iteration time implications. The paper needs to quantify the overhead of the additional forward pass and KL divergence calculation, including memory usage for storing intermediate activations and the impact on training throughput (iterations per second). This is crucial for assessing the practical applicability of the method.
- Overall, writing can be improved with more revisions. Even though the sentences are grammatically correct, some sentences look not natural. (e.g. the very first sentence in the abstract - if you could ask chatgpt like tools, it would tell you the sentence is not natural) Some more details are will be in the Questions section. The introduction could be more compelling and clearly motivate the need for a unified dropout framework. The sudden introduction of DropKey, DropAttention, and HiddenCut without prior context makes the narrative disjointed. Furthermore, the paper would benefit from a more consistent and precise use of terminology throughout.
- Full fine-tuning baseline (not just LoRA) would help understanding the upper bound of the performance. It will be good to have at least RoBERTa model experiments. The lack of a full fine-tuning baseline makes it difficult to assess the true potential of the proposed method. It is important to compare against the performance ceiling achievable through full fine-tuning to understand the trade-offs made by using LoRA and the effectiveness of HiddenKey in that context. Additionally, expanding the experiments to include models like RoBERTa would increase the generalizability of the findings.

### Questions
- The sentence at the end of page 1 (starting with However) and the next sentence are not naturally flow.
- At the end of introduction, DropKey, DropAttention and HiddenCut suddenly appear without any context. Please add some more explanation that those are from previous research and references for them.
- Figure 3 is Illustration of HiddenKey? Not DropKey?
- Is there a training cost analysis with KL divergence?
- In Figure 4, dropkey_column is HiddenKey? It will be useful if this is mentioned somewhere.
- In Table 1, superscripts in HiddenKey+KL seem strange? 1000.00, 5.00. And, why only HiddenKey- has two values? Shouldn't all HiddenKey variants have two values?
- In Figure 5, can you include the validation loss? It might behave similarly to the accuracy.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates three Transformer-specific dropout methods and their performances under PEFT scenarios, and proposes a new dropout scheme named HiddenKey to integrate the best of all the three methods.

### Strengths
1. A novel aspect: This paper investigates the dropout mechanism in PEFT methods, which is kind of novel to me.

2. Sufficient experiments: This paper conducts experiments on various tasks and datasets to validate the effectiveness of HiddenKey.

### Weaknesses
1.  Writing:
- The Introduction conclusively describes the phenomenon of overfitting without dropout in PEFT. After reading the Intro, I naturally associate this paper with “Dropout neurons in LoRA” or something like this. However, in Sec. 2 and 3, when formulating problems and methodology, there is nothing about PEFT, which makes me really confused about what this paper is really about.
- The contribution of this paper is not summarized, leading to more confusions.
- The results that validates the insight (dropout helps overfitting) should be a pivot experiment arranged before the method. Otherwise, the logic may fall in and jump out rapidly, and readers may lose concentration of the conclusion that the results intend to present.
2.  Investigated Methods:
When talking about dropout methods, it is so limited to only talk about DropKey, DropAttn and HiddenCut methods. At least, the very basic Dropout or DropConnect should be investigated. This paper also mentions dropout in so many aspects: Neuron-wise, input-wise, and also attention-wise. There are so many works concerning those aspects, and a comprehensive analysis can be really complicated. However, there is no systematic analysis concerning different types of dropouts. I suggest to focus on a more specific aspect (e.g., attention-wise). Otherwise, a case-by-case analysis in this paper should not be concluded with such a big title - “PEFT meets Dropout”.
3.  Theoretical Analysis:
When talking about preventing overfitting, some analyses about the generalization error bound is expected. However, this paper only conducts some gradient calculation to present “proofs” about reducing gradient noises. However, it is unclear what gradient noises are. There is also no formal definition or theories that can defines or support the noise reductions and lower error bounds of your methods.
4.  Novelty of the Proposed Method:
The core method is simply a mixture of three mentioned dropout schemes. I do not think this is novel enough for ICLR.

### Questions
I have no questions. The detailed suggestions please see Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors motivate their work on the gap between parameter-efficient finetuning and dropout regularization. They introduce a framework to unify PEFT and dropout called HiddenKey and demonstrate performance improvements with lower finetuning cost on two tasks.

### Strengths
- Mathematical comparison on how HiddenKey differs from DropKey and DropAttention was given.
- The authors have evaluated their proposed method on two holistic benchmarks, although as a minor point, the number of iterations to compute the standard deviations was not indicated.

### Weaknesses
 - incremental improvement: In Table 1, the HiddenKey method with KL achieves the best score of 92.01 on average, but this is not a significant improvement (< 1%) from either DropKey or HiddenCut methods. Similarly, HiddenKey only demonstrated marginal improvements in Table 2 to 5, with the highest improvement in Table 2 CoLA (1.95%). I would not claim performance superiority given these results.

 - lack of analysis: While the paper describes the intuition of how HiddenKey differs from DropKey, DropAttention, HiddenCut, it does not give any analysis to describe the difference in empirical experiments e.g. what features were learned or how the computations are empirically different. Minimally, an ablation study is necessary to elucidate which component of HiddenKey is required for the marginal performance gains. 

 - unsupported claim for faster convergence: The authors claimed that "HiddenKey outperforms baseline with shorter finetuning process". When training a model, the training loss is usually used as the metric to determine when model training should be stopped. In Fig.5, at the point of the black vertical line, the baseline model has clearly plateaued while HiddenKey is still decreasing. To reiterate, if i were to use the HiddenKey method, I would take reference from the plateauing of the training loss and not the accuracy, which in this case is significantly longer than the baseline method.

### Questions
- Fig 4 seems that DropKey method is more stable and contributes to a better performance than hidden method with increasing dropout rate?
- Is Fig 5 indicating training or test loss? A decrease in training loss does not indicate overfitting, as hypothesized by the authors.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
