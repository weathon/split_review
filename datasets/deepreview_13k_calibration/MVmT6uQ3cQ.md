# The Need for Speed: Pruning Transformers with One Recipe

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
We introduce the \textbf{O}ne-shot \textbf{P}runing \textbf{T}echnique for \textbf{I}nterchangeable \textbf{N}etworks (\textbf{OPTIN}) framework as a tool to increase the efficiency of pre-trained transformer architectures, across many domains, without requiring re-training. Recent works have explored improving transformer efficiency, however often incur computationally expensive re-training procedures or depend on architecture-specific characteristics, thus impeding practical wide-scale adoption across multiple modalities. To address these shortcomings, the OPTIN framework leverages intermediate feature distillation, capturing the long-range dependencies of model parameters (coined \textit{trajectory}), to produce state-of-the-art results on natural language, image classification, transfer learning, and semantic segmentation tasks. Our motivation stems from the need for a generalizable model compression framework that scales well across different transformer architectures and applications. Given a FLOP constraint, the OPTIN framework will compress the network while maintaining competitive accuracy performance and improved throughput. Particularly, we show a $\leq 2\%$ accuracy degradation from NLP baselines and a $0.5\%$ improvement from state-of-the-art methods on image classification at competitive FLOPs reductions. We further demonstrate the generalization of tasks and architecture with comparative performance on Mask2Former for semantic segmentation and cnn-style networks. OPTIN presents one of the first one-shot efficient frameworks for compressing transformer architectures that generalizes well across \textit{multiple} class domains, in particular: natural language and image-related tasks, \textit{without re-training}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces OPTIN, a framework designed to prune neural networks without the necessity of additional training. It prunes weights that have least impact on the intermediate embeddings and final logits within neural networks. The authors have tested OPTIN across a variety of tasks in both vision and language domains, showcasing its potential effectiveness.

### Strengths
1. **Comprehensive Experiments**: The authors have conducted a wide array of experiments, covering domains such as vision, language, and semantic segmentation tasks, ensuring a comprehensive evaluation of OPTIN.
2. **Strong Performance**: OPTIN demonstrates robust results across the tasks it was tested on, showcasing its effectiveness in network pruning.

### Weaknesses
1. **Performance on Vision Models**: As highlighted in Table 3, the performance of OPTIN (without token reduction) appears to be inferior to that of VTP and PoWER for both evaluated models. It seems that the impressive performance of $OPTIN_\tau$ can be mainly attributed to token reduction. Does it mean OPTIN is more suitable for language models rather than vision models? The core pruning mechanism of OPTIN, which focuses on removing weights based on their impact on intermediate embeddings and logits, seems less effective in vision tasks compared to methods that employ techniques like patch-wise pruning or dynamic token selection. This raises concerns about the general applicability of the base OPTIN method across different modalities, particularly when compared to vision-specific pruning techniques.

Minor issues:
1. Table 1: "(a)Explores" -> "(a) explores".
2. A.6: "Tab ??"

### Questions
1. In Table 2, the results for PTF are directly cited from the original paper. Could the authors confirm that the pre-trained checkpoints and fine-tuning settings are consistent across all experiments to ensure a fair comparison?
2. Could the authors provide details on the estimated time required for OPTIN to prune different models across various datasets? This information would be helpful to evaluate the practicality of implementing OPTIN in different scenarios.
3. Could the authors give further explanations on 'IM-Dense (After dense embedding layer)'. What does it mean?
4. How does OPTIN determines layer-wise sparsity? Does OPTIN rank weights globally? 
5. In Table 1.(d), why $\lambda_c$ is chosen to be 0.1 even though 0.01 provides better results?

I am willing to adjust my rating if my questions are addressed.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces One-shot Pruning Technique for Interchangeable Networks (OPTIN) to prune networks with re-training. With intermediate knowledge distillation, the proposed method saves remarkable computational costs. Experiment results prove the effectiveness of the method.

### Strengths
1. This paper targets on a practical problem, model compression in a more efficient way. 
2. Overall this paper is well-written and easy to follow. It presents the proposed method very clearly.

### Weaknesses
1. I think this paper is a ok paper. For discussion, I want to see the method performance on more complicated network architecture or datasets. 
2. I shall mention that I am not very familiar with the baseline methods. Therefore, if the other reviewers points out the missing related works, please add the comparison results.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a post-training pruning method that operates iteratively. The idea is to approximate each weight's impact on the validation error. To achieve this, the authors mask out weights, then run the forward pass and compute the change in logits.

### Strengths
- The paper presents a significant number of experimental results and ablations.  The ablations in Table 1 are convincing evidence that the design choices made were fully vetted.
- Overall, the study seems very thorough. I don't have any strong reasons to reject or to accept. (suggestions below)

### Weaknesses
 - It seems like PTF is the most relevant and competitive baseline. Per 4.1, the authors compare with an abridged version of PTF however. If you use the same tricks that PTF used (e.g., mask rearrangement -- maybe mask tuning), would your method outperform PTF?
- Figure 1 is a bit complicated to look at. One possibility is to break up this figure into two (the left vs. the right). The details are nice, but they detract from the main point (e.g., the activation difference and the final difference in logit distribution). The logits could be illustrated as two histograms, highlighting their difference.
- The double axis in Figure 2 right is really confusing. Maybe just add a 5th plot? Might not be so easy to see for anyone with color blindness.
- How long does the search take to run? On the order of minutes? Hours? Days? PFT said it took minutes, so that seems like the baseline. Is there significant latency overhead in storing and fetching large activations in RAM, especially for vision models?
- The paper's motivation could be stronger. The abstract and title focus heavily on "without retraining" but it seems like many previous papers already focus on the post-training regime (as the paper cites). The more important motivation is then: What is PFT lacking that is present in this method? *Why is that difference important, intuitively?*

Summary: In short, I'm very lackluster about the paper. The results seem reasonable, but the motivation and the presentation (figures for example) can be improved to make a more convincing case.

### Questions
- typo "Perforamnce" in 4.1
- Every instance of "without re-training" is italicized; it's a bit excessive to do that, particularly given there is previous work that already introduced the idea.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
