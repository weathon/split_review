# COrAL: Order-Agnostic Language Modeling for Efficient Iterative Refinement

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
\iffalse
Self-reflection and iterative improvement have recently emerged as an effective paradigm for enhancing the capabilities of Large Language Models (LLMs) in tackling complex tasks. However, as autoregressive modeling becomes the de facto standard for generative language modeling, these approaches face inherent limitations, including potential inductive bias and high inference latency from the monotonic dependency in next-token prediction. To address these challenges, we present \underline{C}ontext-Wise \underline{Or}der-\underline{A}gnostic \underline{L}anguage Modeling (\method), a novel training paradigm that enhances LLM capabilities through target-aware multi-token prediction and reconstruction. Our method unifies token-level dependency modeling with sequence-level denoising, enabling parallel multi-token generation while retaining high output quality. Leveraging the order-agnostic nature of \method, we introduce blockwise order-agnostic decoding. This approach allows us to perform backward correction for iterative refinement and forward multi-token prediction for speed optimization simultaneously. Experimental results demonstrate significant performance improvements with backward self-enhancement and reduced inference time through forward order-agnostic decoding. Our findings reveal a quality--speed trade-off, elucidating how \method effectively augments the self-enhancement capabilities of conventional autoregressive models without necessitating additional architectural components or extensive pre-training. This work underscores the promise of order-agnostic modeling in advancing LLMs for more efficient and effective natural language processing.
\fi

Iterative refinement has emerged as an effective paradigm for enhancing the capabilities of large language models (LLMs) on complex tasks. However, existing approaches typically implement iterative refinement at the application or prompting level, relying on autoregressive (AR) modeling. The sequential token generation in AR models can lead to high inference latency. 
To overcome these challenges, we propose \underline{C}ontext-Wise \underline{Or}der-\underline{A}gnostic \underline{L}anguage Modeling (\method), which incorporates iterative refinement directly into the LLM architecture while maintaining computational efficiency. Our approach models multiple token dependencies within manageable context windows, enabling the model to perform iterative refinement internally during the generation process. Leveraging the order-agnostic nature of \method, we introduce sliding blockwise order-agnostic decoding, which performs multi-token forward prediction and backward reconstruction within context windows. This allows the model to iteratively refine its outputs in parallel in the sliding block, effectively capturing diverse dependencies without the high inference cost of sequential generation.
Empirical evaluations on reasoning tasks demonstrate that \method improves performance and inference speed, respectively, achieving absolute accuracy gains of $4.6\%$ on GSM8K and $4.0\%$ on LogiQA, along with inference speedups of up to $3.9\times$ over next-token baselines. Preliminary results on code generation indicate a drop in 
pass rates due to inconsistencies in order-agnostic outputs, highlighting the inherent quality--speed trade-off.\looseness=-1

\iffalse
While iterative refinement has emerged as an effective paradigm for enhancing the capabilities of Large Language Models (LLMs) on complex tasks, existing approaches predominantly rely on autoregressive (AR) modeling. The inherent left-to-right dependency in AR models leads to limitations such as high inference latency due to sequential token generation. Non-autoregressive (NAR) models address this by generating tokens in parallel to reduce inference time but often suffer from degraded text quality because of difficulties in modeling complex token dependencies.
To overcome these challenges, we propose \underline{C}ontext-Wise \underline{Or}der-\underline{A}gnostic \underline{L}anguage Modeling (\method), unifying the strengths of AR and NAR models. Our approach models token dependencies within manageable context windows, balancing the capture of long-range dependencies with computational efficiency. Leveraging the order-agnostic nature of \method, we introduce blockwise order-agnostic decoding, which performs forward multi-token prediction and backward reconstruction within context windows. This enables the model to capture diverse dependencies in an order-agnostic manner within the context window.
Empirical evaluations on reasoning tasks demonstrate that \method improves both performance and inference speed, achieving absolute accuracy gains of $4.6\%$ on GSM8K and $4.0\%$ on LogiQA, along with inference speedups of up to $3.9\times$ over next-token baselines. Preliminary results on code generation indicate a drop in pass rates due to inconsistencies in order-agnostic outputs, highlighting the inherent quality–speed trade-off.
By unifying denoising with context-wise order-agnostic language modeling and introducing target-aware positional encoding, \method addresses the limitations of both AR and NAR methods. This approach offers a promising direction for developing more efficient and capable large language models by effectively capturing local dependencies within context windows while maintaining computational efficiency.
\fi

\iffalse
Autoregressive (AR) language models effectively capture rich context by predicting text sequentially, but their left-to-right dependency leads to high inference latency. Non-autoregressive (NAR) models generate tokens in parallel to reduce inference time but often suffer from degraded text quality due to difficulties in modeling complex token dependencies.

To address these challenges, we propose Context-Wise Order-Agnostic Language Modeling (\method), unifying the strengths of AR and NAR models. Our approach models token dependencies within manageable context windows, balancing the capture of long-range dependencies with computational efficiency. By integrating non-autoregressive modeling with denoising techniques, \method performs forward multi-token prediction and backward reconstruction within these context windows, enabling the model to capture diverse dependencies in an order-agnostic manner.

Empirical evaluations on reasoning tasks demonstrate that \method improves performance and inference speed, achieving absolute accuracy gains of 4.6% on GSM8K and 4.0% on LogiQA, along with inference speedups of up to 3.9× over next-token baselines. Preliminary results on code generation indicate a drop in pass rates due to inconsistencies in order-agnostic outputs, illustrating the inherent quality–speed trade-off.

By unifying denoising with context-wise order-agnostic autoregressive modeling and introducing target-aware positional encoding, \method addresses the limitations of both AR and NAR methods. This approach offers a promising direction for developing more efficient and capable large language models by effectively capturing local dependencies within context windows while maintaining computational efficiency.

================================================

Longer version I started with ?
Autoregressive (AR) language models have achieved remarkable success by predicting text sequentially in a fixed left-to-right order, effectively capturing rich contextual information. However, this sequential dependency leads to high inference latency. Non-autoregressive (NAR) language models aim to overcome these limitations by generating tokens in parallel, significantly reducing inference time. Despite this advantage, NAR models often suffer from degraded text quality and instability due to challenges in modeling complex token dependencies, resulting in issues like repetition and incoherence.

To address these challenges, we propose Context-Wise Order-Agnostic Language Modeling (\method), unifying the strengths of AR and NAR models to enhance large language model (LLM) capabilities. Our approach focuses on modeling token dependencies within context windows rather than across entire sequences. By limiting the order-agnostic modeling to manageable context windows, we balance the complexity of capturing long-range dependencies with computational efficiency. This context-wise strategy reduces optimization challenges associated with modeling all possible token permutations while still capturing rich local dependencies crucial for iterative refinement.

By integrating non-autoregressive modeling with denoising techniques, \method combines forward multi-token prediction and backward reconstruction within these context windows, enabling the model to capture diverse dependencies in an order-agnostic manner. 

Empirical evaluations on reasoning tasks demonstrate that \method significantly improves performance and inference speed, achieving absolute accuracy gains of 4.6% on GSM8K and 4.0% on LogiQA, along with inference speedups of up to 3.9× compared to next-token baselines. Preliminary results on code generation reveal a performance drop in pass rates due to inconsistency in order-agnostic outputs, illustrating the inherent quality–speed trade-off.

By unifying denoising with context-wise order-agnostic autoregressive modeling and introducing target-aware positional encoding, \method addresses the limitations of both traditional AR and NAR methods. This approach offers a promising direction for developing more efficient and capable LLMs by effectively capturing local dependencies within context windows while maintaining computational efficiency.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Context-Wise Order-Agnostic Language Modeling (COrAL), which incorporates iterative refinement directly into the LLM architecture while maintaining computational efficiency. Empirical evaluations on reasoning tasks demonstrate that COrAL improves performance and inference speed, and results on code generation indicate a drop in pass rates due to inconsistencies in order-agnostic outputs, highlighting the inherent quality–speed trade-off.

### Strengths
- This paper is well-writen and easy to follow. 
- The performance on logical reasoning tasks are good.

### Weaknesses
 - I think this paper is similar to the other type of works, i.e., speculative decoding, what the difference between them? 
- The noverty is limited, since the specific ways for iterative refinements, the training methods to learn correction, are borrowed from previous works. 
- The significant one: this method seems to only work in specific tasks, the logical reasoning tasks in this paper. However, we always focus on the generalization of current language models, i.e., the competitive on a wide range of tasks.

### Questions
- If the way to generate tokens in the first step is different from that in the process of iterative refinements? Are there any better methods to generate draft tokens.

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
5

### Summary
The paper proposes COrAL(Context-Wise Order-Agnostic Language Modeling), a novel architecture for language modeling that enhances efficiency in iterative refinement, aiming to reduce inference latency in large language models (LLMs). Traditional autoregressive models, which generate text sequentially, struggle with efficiency due to the natural linear time complexity in inference. COrAL incorporates iterative refinement directly into the model, allowing multi-token generation and backward reconstruction within manageable context windows. This order-agnostic approach enables simultaneous forward and backward decoding within sliding context windows, effectively accelerating inference and improving performance on reasoning tasks. Empirical tests show significant improvements in both accuracy and inference speed, demonstrating COrAL's promise in capturing diverse token dependencies without the high latency typical of AR models. However, challenges remain, such as reduced performance in code generation due to output consistency issues, indicating areas for further refinement.

### Strengths
- Improved Efficiency and Performance:  COrAL’s order-agnostic framework allows simultaneous forward and backward processing, significantly reducing inference latency compared to traditional autoregressive models. Compared to the ablated baselines, empirical results on datasets like GSM8K and LogiQA demonstrate notable accuracy gains, confirming the model’s effectiveness in complex reasoning tasks.
- Scalably Adaptable from Existing Models: By using context-wise modeling and target-aware positional encoding, COrAL manages to enhance dependency capture without substantially increasing computational resources, making it feasible for deployment in large-scale applications, even with existing large language models with only minor adaptation.

### Weaknesses
 - Lack of survey of some (maybe kind of obsolete yet important) existing methods: This method resembles Scheduled Sampling in multiple aspects, yet it severely lacks the acknowledgement of this method (no citation nor even mentioning). It shares many ideas and practices with SS, necessitating a deeper analysis on the connection and differences between the method. For example, I'd recommend the authors to emphasize the capability of the proposed method on semi-parallel, refinitive generation, whereas SS was originally only proposed for improvements of performance in sequential generation.
- Lack of deeper discussion on the theoretical insights: I appreciate the authors' awesome work in presenting and delivering the empirical results, but I presume it would appeal the community more if some insightful conclusions can be presented alongside the experiment observations.

### Questions
The clarity of the paper is good, it's easy for people to follow generally. I don't have further questions.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce a novel decoding strategy combining autoregressive modelling with ROBERTA-like order agnostic refinement. Given a partial sequence, they predict multiple tokens ahead, which they subsequently refine using ROBERTA-like denoising autoencoder. The authors see performance improvements on GSM8K and LogiQA and poor performance on code generation.

### Strengths
* the authors propose an interesting paradigm and show that it has promise for reducing computational cost and enhancing performance in certain settings
* the method is applicable to autoregressive pretrained language models and seems to improve their performance in certain settings
* the authors provide a quite extensive ablation study for their method
* the paper contains some beautiful figures such as figure (2) and (3). Even though Figure (2) is a little bit unclear to me. Why are there seemingly different offsets for the refinements and why is there not much visual seperation inbetween forward prediction and refinement?

### Weaknesses
 * pseudo-code for Algorithm 1 is provided without walking through the pseudo-code
* in the experimental section the baselines are not described in enough detail, just AR. the proposed method requires finetuning, are the AR baselines also finetuned on the tasks?
* the by-far-best performance is achieved using the w\o multi-head prediction ablation, which is not the proposed method and thus weird. I assume this variant suffers from increased computational cost compared to the proposed method. It would be interesting to compare this ablation with a method from the related work that has a similar computational cost.
* comparison to refinement methods from the related work is missing
* a somewhat non-standard notation for expected values is used. their subscripts seem to be used much like in summations, but usually subscripts at an expected value are used to indicate over which distribution the expectation is taken: e.g., equation (1) and equation (3)
* The paper lacks a clear explanation of how the order-agnostic refinement interacts with the autoregressive generation process. Specifically, it's unclear how the model handles inconsistencies that may arise when the refinement step alters previously generated tokens, potentially disrupting the autoregressive chain. A more detailed discussion of the interplay between these two components is needed.
* The computational cost of the proposed method, especially the w/o multi-head prediction variant, needs to be more thoroughly analyzed. While the authors mention that it has a higher cost, a detailed breakdown of the computational overhead compared to standard autoregressive decoding and other refinement methods is missing. This should include a discussion of memory usage and latency, which are crucial for practical applications.

### Questions
It would be really interesting to check how much performance is lost by starting from a pretrained model as compared to full training a method employing coral from scratch. Do you think that some performance is left on the table because you start from a pretrained model? 

In the main result part, to increase my rating I would like to see a comparison to other interative refinement methods that have a similar computational cost as the w/o multi-token prediction variant of the proposed method and also a more detailed description of the autoregressive baseline.

Suggestion: Maybe it would be a good idea to incorporate an application in which this method shines. E.g., by looking into domains that can benefit from the order-agnostic aspect such as protein language modelling.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a new decoding method, called CORAL, which can speed up the decoding process and maintain (or upraise) the performance of the model in some tasks. CORAL has 2 parts: prediction and verification. The experiment shows that the verification part can help the model to generate more accurate results. CORAL also designed a strategy named "multi-forward" to speed up the decoding process (although it may hurt the performance). The result shows that the CORAL is useful in math problems but is useless in the code generation task.

### Strengths
1. The topic of the paper is interesting, transformer-based model do have the problem of slow decoding speed. 

2. It make a good balance between the speed and the performance.

### Weaknesses
1. The improvement of the CORAL is not generalizable enough. It only works well in the some math/logic problems but not in the code generation task.

2. Although the speed of the decoding process is improved, it needs to use more GPU memory (and "waste" some computation because of verification and multi-forward) to achieve this. So it is not friendly to equipment that most people use.

### Questions
In eq.8 entropy is always positive, so -H(x) is always negative and exp(-H(x)) is always less than 1. So min(a,a*exp(-H(x))) is always a*exp(-H(x)).

### Soundness
4

### Presentation
2

### Contribution
3
