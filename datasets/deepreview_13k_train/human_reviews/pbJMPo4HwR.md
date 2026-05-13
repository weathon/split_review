# Learning Monotonic Attention in Transducer for Streaming Generation

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Streaming generation models are increasingly utilized across various fields, with the Transducer architecture being particularly popular in industrial applications. However, its input-synchronous decoding mechanism presents challenges in tasks requiring non-monotonic alignments, such as simultaneous translation, leading to suboptimal performance in these contexts. In this research, we address this issue by tightly integrating Transducer's decoding with the history of input stream via a learnable monotonic attention mechanism. Our approach leverages the forward-backward algorithm to infer the posterior probability of alignments between the predictor states and input timestamps, which is then used to estimate the context representations of monotonic attention in training. This allows Transducer models to adaptively adjust the scope of attention based on their predictions, avoiding the need to enumerate the exponentially large alignment space. Extensive experiments demonstrate that our MonoAttn-Transducer significantly enhances the handling of non-monotonic alignments in streaming generation, offering a robust solution for Transducer-based frameworks to tackle more complex streaming generation tasks. Codes are publicly available in supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses the challenges faced by Transducer-based streaming generation models, particularly in tasks requiring non-monotonic alignments, such as simultaneous translation. These challenges arise from the input-synchronous decoding mechanism of Transducers, which can result in suboptimal performance. To address this, the authors propose integrating a learnable monotonic attention mechanism within the Transducer architecture. This mechanism uses a forward-backward algorithm to calculate the posterior probability of alignments between predictor states and input timestamps. Consequently, it allows for the estimation of context representations of monotonic attention during training, enabling the model to adaptively adjust its attention scope based on predictions. This innovative approach eliminates the need to explore the exponentially large alignment space. Experiments reveal that the proposed MonoAttn-Transducer significantly improves performance in streaming generation tasks dealing with non-monotonic alignments. The codes for this study are available in the supplementary materials.

### Strengths
1. The authors propose a learnable monotonic attention mechanism within the Transducer architecture to solve the non-monotonic alignments in streaming generation.

2. The propsoed method is effectiveness and easy to reproduce.

### Weaknesses
1. I am unable to discern the difference between the proposed monotonic attention mechanism and the cross-attention mechanism.

2. Furthermore, the authors should compare the cross-attention approach (Liu et al., 2021; Tang et al., 2023) with other methods that utilize input history.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes MonoAttn-Transducer, a novel approach to enhance Transducer models with learnable monotonic attention for streaming generation tasks. The key contributions are:

- A method to integrate monotonic attention into Transducer's architecture while maintaining its efficient training through the forward-backward algorithm.
- A training algorithm that uses posterior alignment probabilities to estimate context representations for monotonic attention.
- A chunk synchronization mechanism to bridge the gap between training and inference.
- Extensive experiments demonstrating improved performance on simultaneous translation tasks.

### Strengths
Technical Innovation:

- The proposed method cleverly solves the exponential state space problem by using posterior alignments to estimate context representations
- The solution maintains the same computational complexity as vanilla Transducer
- The chunk synchronization mechanism shows thoughtful consideration of practical deployment

Theoretical Foundation:

- The approach is well-grounded in probability theory and previous work on Transducers
- The mathematical derivations are sound and clearly explained
- The relationship between prior and posterior alignments is well-analyzed

Empirical Results:

- Comprehensive experiments on MuST-C dataset
- Strong improvements over baseline Transducer (+0.75-1.0 BLEU, +0.95-2.06 COMET)
- Thorough ablation studies and analysis
- Competitive performance against SOTA methods

### Weaknesses
Limited Experimental Scope:

- Experiments focus only on speech-to-text translation.
- Only two language pairs (En->De, En->Es) are tested.
- No experiments on other streaming generation tasks like ASR or TTS.

Training Efficiency:

- The paper doesn't discuss training time comparison with baseline Transducer.
- Memory usage analysis could be more detailed.
- No discussion of potential overhead from posterior alignment calculation.


Algorithmic Limitations:

- The method still requires chunk-based processing.
- The impact of chunk size on performance could be better theoretically explained.
- The choice of diagonal prior distribution seems somewhat arbitrary.

### Questions
/

### Soundness
4

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
This paper describes an extension for Transducers for tasks where the input and output are not monotonically aligned, such as speech translation. The method is evaluated on two languages of the MuST-C benchmark and it is compared to existing methods.

### Strengths
* The paper addresses an interesting setting which has practical implications
* The method is described in detail and a large portion of the paper is dedicated to this description.

### Weaknesses
 * The method is fairly complex, requiring a range of steps in addition to Transducer training as shown in Algorithm 1 (which is already complex).
* The description of the method is sometimes not very clear. It would be helpful to provide intuition in addition to equations.
* The evaluation was done on languages with relatively similar word order: En-Es and En-De differ in their word order but much less so, then say En-Chinese or English and any non-European language. There are speech translation benchmarks which enable these settings, e.g., FLEURS and which would provide more interesting results.
* It seems a bit surprising that the BLEU improvements for En-Es and En-De between Transducer and the new method seem fairly similar across most chunk sizes (about 1 BLEU, Table 2). I would have expected En-De to benefit more the new method than En-Es given that the word order of En-De is more different.

### Questions
* Did you consider evaluating on other settings than En-De/En-Es where word order is more different?

### Soundness
2

### Presentation
2

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
This paper presents a solution to the challenges faced by Transducer-based streaming generation models in handling non-monotonic alignments, particularly in simultaneous translation tasks. The authors introduce a learnable monotonic attention mechanism that integrates with Transducer decoding. Utilizing the forward-backward algorithm, they infer alignment probabilities between predictor states and input timestamps, allowing adaptive adjustments in attention scope. Experimental results show significant performance improvements of the MonoAttn-Transducer, offering a robust method for complex streaming generation tasks. Their code is publicly available.

### Strengths
1. This paper improves the Transducer architecture, making it more suitable for streaming generation tasks.  
2. The experiments demonstrate that the proposed method achieves commendable performance in the Speech-to-text Simultaneous Translation task.

### Weaknesses
1. The experiments in this paper only provide results on the Speech-to-Text Simultaneous Translation task, and do not validate the method on other streaming generation tasks.  
2. Under lower latency conditions (about 1000 ms) for the EnDe and EnEs tasks, the performance of MA-T appears to be inferior to that of CAAT, another transducer-based method. This may indicate that the proposed method in this paper is not highly effective.  
3. The proposed method in this paper shares a very similar model structure with both CAAT (Liu et al. 2021) and  MILK (Arivazhagan et al 2019), which raises concerns about the lack of novelty in the article.

### Questions
1. After incorporating a unidirectional encoder, the model structures of MA-T and CAAT are very similar. What are the specific differences between the two? How does MA-T manage to perform attention computations while ensuring that Memory Overload remains O(1)?  
2. Using AL as a latency metric may not accurately assess the phenomenon of over-generation. Could you provide alternative latency metrics, such as LAAL or LAAL-CA?  
3. Regarding the comparison between MA-T and TAED, could you provide more experimental results to demonstrate that your method truly achieves better performance than MA-T? From the perspective of AL and BLEU, while TAED has a larger computational overhead, it does achieve higher translation quality at a lower latency and the overhead is still acceptable.

### Soundness
3

### Presentation
3

### Contribution
3
