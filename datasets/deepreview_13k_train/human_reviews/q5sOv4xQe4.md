# HART: Efficient Visual Generation with Hybrid Autoregressive Transformer

- Decision: Accept
- Scores: 8, 6, 6, 8, 6

## Abstract
We introduce \textit{\method} (\methodshort), an autoregressive (AR) visual generation model capable of directly generating 1024$\times$1024 images, rivaling diffusion models in image generation quality. Existing AR models face limitations due to the poor image reconstruction quality of their discrete tokenizers and the prohibitive training costs associated with generating 1024px images. To address these challenges, we present the \textit{hybrid tokenizer}, which decomposes the continuous latents from the autoencoder into two components:  discrete tokens representing the big picture and \textit{continuous} tokens representing the residual components that cannot be represented by the discrete tokens. 
The discrete component is modeled by a \textit{scalable-resolution} discrete AR model, while the continuous component is learned with a lightweight  \textit{residual diffusion} module with only 37M parameters. Compared with the discrete-only VAR tokenizer, our hybrid approach improves reconstruction FID from \textbf{2.11} to \textbf{0.30} on MJHQ-30K, leading to a \textbf{31\%} generation FID improvement from \textbf{7.85} to \textbf{5.38}. \methodshort also outperforms state-of-the-art diffusion models in both FID and CLIP score, with \textbf{4.5-7.7$\times$} higher throughput and \textbf{6.9-13.4$\times$} lower MACs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses limitations in autoregressive models (AR models), particularly the challenges in image reconstruction due to discretized tokens and the high computational costs of generating high-resolution images. To overcome these issues, the authors introduce a novel hybrid tokenizer that combines both discrete and continuous tokens. Specifically, discrete tokens are generated in an AR style, while continuous tokens are generated in a diffusion style conditioned on the discrete tokens. Compared to the VAR tokenizer, this approach demonstrates enhanced reconstruction FID performance. Moreover, in generative modeling tasks, it shows superior efficiency compared to current state-of-the-art models.

### Strengths
The hybrid tokenization approach presented in this paper demonstrates impressive reconstruction quality, outperforming methods that rely solely on discrete tokens. Additionally, the necessity of residual tokens is convincingly validated through detailed ablation studies, which provide strong empirical support for their inclusion. The model architecture—an autoregressive model with discrete tokens and conditioned diffusion on continuous tokens—exemplifies an effective design choice that balances efficiency and performance. This hybrid approach not only achieves comparable speeds to VAR in class-conditional image generation tasks but also scales effectively to large datasets, as evidenced by its application to tasks like text-to-image generation.

### Weaknesses
While Figure 7 demonstrates that residual tokens in HART are indeed easier to learn than full tokens in MAR, the results from the class-conditional image generation task seem to contradict this intuition. MAR, which generates full continuous tokens, achieves competitive FID performance despite having fewer parameters than HART, which focuses on generating residual tokens—ostensibly a less complex task. 

This raises questions about the specific aspects that contribute to the observed performance gap between the two models. It would be interesting to explore whether this difference could be mitigated by increasing the diffusion steps for HART, similar to the approach in MAR. Further clarification or analysis in this area would provide valuable insights into the comparative efficiency and effectiveness of the models.

### Questions
In Table 4, I am interested to know if increasing the diffusion steps for HART during inference—similar to the approach used in MAR—would lead to an improvement in generation quality. Clarifying this aspect would help in understanding the impact of diffusion steps on HART's performance.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents HART, a Hybrid Autoregressive Transformer model for efficient, high-resolution text-to-image generation. Key innovations include a hybrid tokenization approach that combines discrete and continuous tokens, enabling finer detail capture while reducing computational overhead. HART achieves better efficiency, with lower latency and higher throughput than comparable models, and directly generates 1024x1024 images without super-resolution. However, the paper could benefit from a stronger theoretical foundation, exploration of alternative text conditioning methods, more comparative analysis with similar models like VAR-CLIP and STAR, and clearer differentiation from MAR, especially regarding inference optimizations. Overall, HART is a promising work in autoregressive T2I generation.

### Strengths
- The model demonstrates efficiency improvements over state-of-the-art diffusion models. The residual diffusion approach minimizes memory and processing costs, achieving a reduction in latency and MACs. As a result, HART’s latency and throughput metrics are efficient, offering a speed and computational advantage.

- the hybrid tokenizer combining discrete and continuous tokens is efficient in autoregressive (AR) image generation, providing higher fidelity in image reconstruction and generating fine details often missed by discrete-only models. This method addresses the usual limitations of discrete tokenizers by retaining important image details, especially at high resolutions (1024×1024）

### Weaknesses
 - **Limited Theoretical Foundation**:
    - The paper relies predominantly on experimental results, without providing a thorough theoretical basis for the proposed methodology. A more detailed theoretical analysis would strengthen the paper’s rigor and enhance the broader applicability of the approach. Specifically, the paper lacks a formal analysis of why the hybrid tokenization approach is superior to discrete-only methods in the context of autoregressive image generation. While the empirical results are promising, a theoretical justification, perhaps drawing from information theory or rate-distortion theory, would provide a more solid foundation for the method.
- **Ambiguity in Differentiation Between HART and other work, e.g. MAR**:
    - The distinction between HART and MAR is not fully clear, especially concerning optimizations like sampling efficiency and inference techniques. For example, while HART achieves optimal quality with just 8 sampling steps due to its diffusion setup, it is unclear why MAR could not potentially achieve similar results with similar diffusion adaptations. Additionally, some statements (lines 329-335) imply that certain optimizations, such as KV-caching, are unique to HART, but MAR could likely implement these as well. Further clarification on these points would provide a more accurate comparison between the two models and help readers understand the unique contributions of HART. The paper needs to explicitly address the architectural differences that prevent MAR from achieving similar sampling efficiency and clarify which specific components of HART enable its superior performance.

- **Unexplored Alternatives for Text Conditioning**:
    - The current approach employs text tokens as the sequence start token, but it does not explore or compare this choice with other established methods, such as cross-attention mechanisms commonly used in diffusion models for text-to-image (T2I) tasks. Including comparisons with alternative conditioning methods would clarify the advantages or limitations of the current setup. The paper should investigate how the chosen method compares to cross-attention in terms of both computational cost and the quality of text-image alignment, and provide a rationale for the specific choice.
- **Insufficient Comparative Analysis**:
    - The paper would benefit from a broader evaluation against similar autoregressive T2I models, such as VAR-CLIP and STAR. A horizontal comparison would add depth to the experimental results, positioning HART more clearly within the landscape of current models. The paper should include a detailed comparison of the architectural differences, training procedures, and performance metrics of these models to provide a comprehensive understanding of HART's relative strengths and weaknesses.

### Questions
See the weaknesses, and my major concern is that: 
 
Can you provide a more in-depth theoretical explanation of HART's hybrid tokenization and why it outperforms traditional discrete-only AR approaches? Not only to put some tricks to improve the performance. This would help clarify whether the hybrid approach could serve as a generalized framework for other AR T2I tasks.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a feasible scheme for AR model to produce high quality images effectively, and has a great improvement in performance and throughput.

### Strengths
1. This paper proposes a feasible scheme to solve the key problem of AR model: effective modeling of image quality, which is ahead of other methods in FID.
2. The paper is logical, the process of problem solving is very smooth, and the experimental setting is also reasonable.

### Weaknesses
1. There is doubt about the use of 50% for modeling discrete and continuous tokens, what happens if it is alternate, please explain the necessity of 50% here, and if there is a 30% accident, whether the other probability will break the balance, in other words, whether 50% is the best balance between the probabilities of the two modeling methods.
2. The overall solution of this paper is based on the random selection of two mature pipelines. There is a lot of randomness in training in this way, will it lead to poor stability of the network? Besides, this kind of scheme is not the most ideal for balancing the combination of continuous tokens and the separation of tokens, and it is a cheating scheme.

### Questions
Please explain the above questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces HART, an innovative autoregressive transformer designed for efficient visual generation. It employs a hybrid token space to represent images, with the discrete component modeled by a VAR model and the continuous component modeled by a compact diffusion model. Extensive experiments demonstrate that HART outperforms previous baselines in both image quality and efficiency.

### Strengths
1. The paper is well-written and easy to follow.
2. The idea of using a compact diffusion model to model the residual continuous token is both simple and effective. I believe this design will offer valuable insights to the community.
3. The experiments are carefully designed. The results and conclusions are convincing.

### Weaknesses
The paper notes that a lower rFID does not necessarily indicate a better gFID, which is also supported by the ablation experiments. However, I feel that there is a lack of analysis regarding this phenomenon. For instance, it would be beneficial to provide insights into which design elements are crucial for obtaining tokens that achieve both good rFID and gFID simultaneously, and the other designs lead to a bad gFID. Specifically, the paper should delve deeper into the interaction between the discrete and continuous token spaces and how this interaction impacts the final generation quality. The ablation study, while demonstrating the issue, does not provide sufficient mechanistic understanding of why certain configurations lead to a decoupling of rFID and gFID. A more detailed analysis of the decoder's role in this process is needed, particularly how the decoder's training regime affects its ability to translate the hybrid token space into high-quality images.

### Questions
see Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an efficient and high-resolution autoregressive visual generation model with a hybrid tokenizer. The hybrid tokenizer includes a discrete tokenizer and a continuous tokenizer. The discrete tokenizer that is widely used in existing AR models is applied to model image structure, while the continuous tokenizer is used to represent residual image details. To model these image token priors, this paper also introduces a scalable discrete AR model and a light-weight residual diffusion model. Based on above modules, the proposed method beats VAR in rFID and outperforms sota diffusion models in both FID and CLIP score.

### Strengths
+ This paper proposes a hybrid tokenizer, addressing the poor image reconstruction quality of existing discrete tokenizer. Also, the hybrid tokenizer is simple and easy to implement.
+ To model tokens generated by the hybrid tokenizer, this paper introduce a scalable-resolution discrete AR model and a light-weight residual diffusion model. Based on these modules, the proposed method can generate 1024px image efficiently.
+ The authors conduct exhaustive experiments to validate the proposed method. Compared with existing AR and diffusion models, the proposed method achieves superior performance on text-to-image and class-conditioned image generation tasks.

### Weaknesses
- The condition of residual diffusion. As shown in line 320~321, the condition consists of last layer hidden states from AR transformer and the discrete tokens predicted in the last sampling step. To my knowledge, the discrete tokens predicted in the last sampling step only contain residual image details. It is not enough to predict the residual tokens. Thus, the hidden states are important. Does the hidden states come from all sampling steps? It's unclear how the hidden states from the autoregressive transformer, which are inherently sequential, are effectively combined with the discrete tokens to condition the diffusion process. The paper lacks a detailed explanation of this fusion mechanism, and it's not immediately obvious how the temporal dependencies captured by the AR model are leveraged in the diffusion model's conditioning.
- Efficiency enhancements (Training). In line 346~349, the fist sentence is about the overhead of residual diffusion module. But the following solution (discarding 80% tokens) is used to mitigate training overhead of VAR, which is also illustrated in Appendix A.1. In my opinion, there is a mismatch between these two parts. The connection between the overhead of the residual diffusion module and the proposed solution of discarding 80% of tokens is not clearly established. It's not evident how reducing the number of tokens directly addresses the computational burden introduced by the diffusion module itself. The explanation needs to clarify whether the token reduction is applied to the input of the diffusion model, the AR model, or both, and how this specifically alleviates the diffusion module's overhead.
- Alternating training in hybrid tokenizer. To my knowledge, with this training scheme, visual decoder is robust to the error of predicted tokens. For generation model, the error is large in the early training. Thus, the decoder with this scheme performs better than others, as shown in Figure 7 (middle and right). Does the great advantage of alternating training exist after generation model training? The paper does not provide sufficient analysis on the long-term effects of the alternating training scheme. While the initial benefits are clear, it's not obvious if this advantage persists after the model has fully converged. It's crucial to understand whether this training strategy leads to a more robust and stable model in the long run, or if its benefits diminish as training progresses.

### Questions
- The illustration of Figure 6. First, the arrow direction of scalable-resolution autoregressive transformer is wrong. Second, the last layer hidden states are not figured out in Figure 6. Third, the HART attention mask (right) does not contain much information. The attention mechanism of each stage is not easy to obtain for the readers.

### Soundness
3

### Presentation
3

### Contribution
3
