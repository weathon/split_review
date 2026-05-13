# SparseVLM: Visual Token Sparsification for Efficient Vision Language Models Inference

- Decision: Reject
- Scores: 6, 6, 6, 5, 3

## Abstract
In vision-language models (VLMs), visual tokens usually consume a significant amount of computational overhead, despite their sparser information density compared to text tokens. To address this, most existing methods learn a network to prune redundant visual tokens and require additional training data. Differently, we propose an efficient training-free token optimization mechanism dubbed SparseVLM without extra parameters or fine-tuning costs. Concretely, given that visual tokens complement text tokens in VLMs for linguistic reasoning, we select visual-relevant text tokens to rate the significance of vision tokens within the self-attention matrix extracted from the VLMs. Then we progressively prune irrelevant tokens. To maximize sparsity while retaining essential information, we introduce a rank-based strategy to adaptively determine the sparsification ratio for each layer, alongside a token recycling method that compresses pruned tokens into more compact representations. Experimental results show that our SparseVLM improves the efficiency of various VLMs across a range of image and video understanding tasks. In particular, LLaVA equipped with SparseVLM reduces 61\% $\sim$ 67\% FLOPs with a compression ratio of 78\% while maintaining 93\% of the accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SparseVLM, a method to accelerate vision-language models (VLMs) by prunning vision tokens incrementally over layers, based on its significance for (a subset) the text tokens. The set of (significant) visual tokens to keep is computed from the self-attention scores in each layer, and the set of relevant text tokens is computed just once, using the dot-product between the text and image tokens after being embedded to the same size. This tries to reduce the computational overhead of the method, achieving real wallclock time speed-ups, for different prunning levels. The authors also propose to aggregate and reconstruct some tokens, to prevent completely losing the information of the tokens that are decided to prune. 
The paper presents results in different image and video understanding benchmarks, and compares the proposed method against two recent baselines (ToME and FastV). The results show that the proposed method improves over these baselines across different prunning thresholds, and achieves significant memory, FLOP and runtime reduction with roughly the same accuracy, when compared to FastV.

### Strengths
- The proposed method is compared against two recent and popular baselines: ToMe and FastV.
- The paper is well structured and the method is well explained (modulo some typos / ambiguous equations, see weaknesses).
- The method does not require any type of fine-tuning, so it can be used on top of different VLMs, which broadens its potential adoption.
- For the same number of retained tokens, Table 1 and Table 2 show that the proposed method represents a huge accuracy improvement respect the baselines.
- The paper ablates the use of token reconstruction in Table 3, which shows that the proposed improvement significantly improves over the core SparseVLM method.

### Weaknesses
 - The results in Table 1 and Table 2 do not reflect the reduction in neither FLOP, nor wallclock runtime. Only Table 4 offers some results comparing the proposed method only against FastV. However it's not clear to which benchmark(s) the reported accuracy corresponds to. Also, the baseline storage memory is missing (although it can be calculated from the remaining values). I would suggest that the authors report a similar figure to Figure 4 with two plots showing the avg accuracy w.r.t. a) letency or total runtime and b) FLOPs. This would represent much better the cost-vs-quality tradeoffs, for SparseVLM applied on both LLaVA and MGM. This is crucial to increase the rating of the paper. If space is limited, I would suggest reporting values for individual datasets in the appendix, and report only the average in the main text (unless there are any major outliers).
- Table 2 does not even represent the speed-vs-accuracy trade-off, nor the "token budget"-vs-accuracy, since only a single token budget of 135 is represented. Also, this value is not the same used in any of the image results reported in Table 1. Which begs the question: why was this particular value used? Please, provide figures as described above.
- It's not 100% clear how $\mathbf{P}$ in section 3.2 is calculated. According to eq. (1) and (2), $\mathbf{P}$ is a subset of rows and columns of the attention matrix (after the softmax), but lines 183-184 refer the "logits" (i.e. $\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{D}}$). It's also not clear if the attention matrix is re-normalized after the selected visual tokens are dropped from the keys or not.
- Notation in eq. (7) is ambiguous. The index $j$ in the sum isn't used anywhere. Also, notice that the size of $\mathbf{H}_v \mathbf{H}_q^\top$ is $L_v \times L_q$, which is inconsistent with the sum over $j$, assuming $j$ denotes a column index, since $\mathbf{R}_i$ supposed to be the average over visual tokens for the $i$-th query token. This is a small mistake that can be fixed by using $\mathbf{H}_q \mathbf{H}_v^\top$, to match the dimension order of $\mathbf{P}$ is $L_v \times L_q$ (i.e. text $\times$ vision).
- The choice of the relevant text token select threshold $m = \text{Mean}(\mathbf{R})$ isn't justified. Why this threshold and not something else? E.g. the text tokens in the with the highest $R$ score such that the sum of 
- The number of vision tokens to prune is based on the rank of $\textbf{P}$, this can be problematic due to numerical precision. For instance, suppose that $n = L_t = L_v$, what happens if we get that half of the the singular values of P are $10^{-5}$ and the rest are $10^5$? The rank would be technically $n$, but is it really or do we get $10^{-5}$ rather than 0 due to numerical errors?

### Questions
- Suggestion: Instead of using the rank, an alternative approach (which is not prone to the numerical issues that I discussed above), is to prune based on the (relative) singular values of $\mathbf{P}$: 
    1) First compute the singular values of $\mathbf{P}$, assume that these are returned in decreasing order.
    2) Divide each value by the total sum of singular values (a.k.a. the "energy" of the matrix). Let's call this vector $E$, i.e. the relative energy of each singular value.
    3) Prune $N - k$ tokens, where $k$ is the smallest value such that $\sum_{i=1}^k E_i \geq \lambda$.
- Could you please add the memory used by the baseline in Table 4?

### Soundness
2

### Presentation
3

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
This paper introduces SparseLVM, a training-free method to prune redundant visual tokens in LVLMs. SparseLVM leverages visual-relevant text tokens to rate the significance of vision tokens within the self-attention matrix, leading to the progressive pruning of irrelevant visual tokens. Specifically, SparseLVM proposes a rank-based strategy to adaptively determine the sparsification ratio for each layer and a token recycling method that compresses pruned tokens into center tokens. SparseLVM reduces the number of tokens with less performance drop than ToMe and FastV.

### Strengths
1. The proposed SparseLVM framework, including rank-based strategy and token recycling, is reasonable.

2. The paper is clear to read. It is easy for the audience to follow the sophisticated designs in SparseLVM.

3. Experiments are performed on both image and video benchmarks.

### Weaknesses
1. The proposed SparseLVM is not practical for two reasons.

- First, it is not compatible with FlashAttn, which is a standard solution for accelerating the calculation of self-attention. In SparseLVM, the attention matrix must be explicitly obtained to select redundant visual tokens in **each layer** of LVLMs. However, FlashAttn does not support attaining the explicit attention matrix. Without compatibility with FlashAttn, SparseLVM will be limited in its efficiency. The SparseLVM should be compared with the original LVLMs with FlashAttn. 
- Second, although the performance drop of SparseLVM is less than ToMe and FastV, it is still considerably large. More explanations and discussions are necessary.

2. Some important ablation studies are not shown.

- For verifying efficiency, the SparseLVM should be compared with the original LVLMs with FlashAttn. 
- For verifying effectiveness, the SparseLVM should report more results on high-resolution image understanding benchmarks, such as DocVQA, InfoVQA, AI2D, etc, as in leading LVLMs [1].


3. Some details of SparseLVM are not clearly introduced. 
- What is the value of m in equation (6), lambda in equation (8), and tau in equation (9)? How does SparseLVM determine them?
- After Visual Token Recycling, how does SparseLVM insert these recycled tokens into the preserved tokens? It seems that these recycled tokens have the risk of spatial relationship between different image tokens.

### Questions
Due to the weakness of this paper, I tend to be borderline negative about this paper. See weakness section for details of my concerns and questions.



###################

Thanks for your reply. Most of my concerns are solved. I will raise my rating to 6. Hope to see the SparseVLM with Flash Attention to be released.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces SparseVLM, a training-free token optimization that improves the efficiency of Vision-Language Models (VLMs) by reducing visual token. The method improve the efficency of VLM by three steps: 1) first identify text tokens strongly correlated with visual signals via cross-attention, and then 2) measure the contribution of visual tokens to the selected visual-relevant text tokens (raters), and finally 3) adaptively prune the insignificant vision token. Experiments show the LLaVA equipped with SparseVLM reduces 61%∼67%
FLOPs with a compression ratio of 78% while maintaining 93% of the accuracy. The proposed method consistently outperforms the
existing state-of-the-art method FastV by 7.7%∼14.8% on LLaVA, 10.2%∼21.6% on MiniGemini, and 34.4% on VideoLLaVA.

### Strengths
1. The proposed Text-Guided Visual Token Pruning is novel, which  introduce text-aware guidance for visual token sparsification. The experiments showing this approach outperforms text-agnostic methods like FastV by 14.8% on LLaVA when retaining only 64 tokens, which validate the effectiveness of using text tokens as "raters" for visual importance.

2. The proposed method is training-free, which is easy to deploy. 

3. The paper introduces a rank-based strategy to adaptively determine the sparsification ratio for each layer, which saves the number of hyperparameters and reduces the engineering effort.

4. Instead of directly pruning tokens, the proposed method merges them into compact representations. Ablation studies show this recycling mechanism improves accuracy from 1.5% to 17.7% on POPE when pruning to 64 tokens, demonstrating significant information preservation.

### Weaknesses
1. The proposed method requires the attention scores to select the visual tokens to be pruned. This would not be compatible with FlashAttention, and may require significantly more memory and possibly extra latency. The authors are encourage to do comparison with baselines powered with FlashAttention and show the result. My concerns is that without using FlashAttention the proposed method could cost much more memory, and make it harder or infeasible to be deployed. Specifically, author should show the peak memory consumption and latency comparision between proposed method vs Baseline with FlashAttention.

2. The experimental evaluation lacks comparison with latest token reduction methods that outperform FastV. Notably absent are Token summarization[https://arxiv.org/abs/2410.14072 ], Progressive Token Pruning[https://arxiv.org/abs/2301.13741]- all of which have better performance comparing to FastV in different tasks. Including these state-of-the-art baselines is essential for a comprehensive evaluation.

3. The experimental focuses on a single VLM architecture: LLaVA, which limiting evidence of the method's broader applicability. Testing across other VLM architectures like Flamingo would better demonstrate generalizability, particularly with different visual and textual feature fusion mechanisms.

### Questions
See weakness for details.

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
5

### Summary
This paper proposes an efficient training-free token optimization mechanism dubbed SparseVLM without extra parameters or fine-tuning costs.

The contributions of this paper are summaried as follows:
1. The paper introduces a sparsification framework dubbed SparseVLM for vision-language models. 
2. The paper first assigns visual-relevant text tokens as raters, adaptively prunes VLMs with the rank of the attention logits, and recycles partial tokens.
3. Consistently outperforms the FastV.

### Strengths
1. The paper is well-written, showcasing a clear and articulate presentation of ideas.
2. The paper is simple and easy to follow.
3. The training-free token optimization mechanism is more universal and can be better adapted to various VLM models compared to methods that require training.

### Weaknesses
1. One motivation of the paper is that visual tokens should be sparsified adaptively based on the question prompt. This prompt-aware sparsification, while preserving the original model's performance as much as possible, causes the VLM to lose its ability for multi-turn conversations.
2. The method in the paper requires explicitly obtaining the attention map, but in many inference acceleration frameworks, the attention map is not accessible, such as in FlashAttention. In Table 4, is the baseline using the standard attention mechanism? If compared with FlashAttention, does it still have a speed advantage?

### Questions
1. How to deal with RoPE for the sparsified visual tokens?
2. In Equation 7, why was it chosen to use the features from the visual encoder and text embeddings to select raters? Does this lead to the method performing poorly on problems that require logical reasoning, such as the performance on MMMU、Reasoning-related subset of MMBnech?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces SparseVLM, an efficient, training-free optimization method for visual tokens in vision-language models (VLMs). Recognizing that visual tokens in VLMs often introduce high computational costs due to their low information density, SparseVLM selectively prunes redundant tokens without needing additional training data or parameters. By using the visual-relevant text tokens (from the self-attention matrix) to rate the importance of visual tokens, SparseVLM identifies and prunes unnecessary tokens progressively. A rank-based strategy is used to determine the pruning ratio per layer, while a token recycling method condenses pruned tokens into compact forms, maintaining essential visual information.

### Strengths
1. The paper presents SparseVLM, a training-free mechanism designed to improve the efficiency of vision-language models (VLMs) by optimizing the handling of visual tokens.
2. The paper is well-written and clearly presents the proposed framework. The authors provide detailed descriptions of their methodology.
3.  Considering the recycling of deleted image tokens is an effective method to alleviate performance degradation.

### Weaknesses
1. The primary focus on efficiency must maintain performance; otherwise, efficiency becomes meaningless. In Table 1, even the setting with the least acceleration, "Retain 192 Tokens," exhibits substantial performance drops across multiple benchmarks. Specifically, GQA drops by 4.3%, POPE by 2.3%, VQAv2 by 2.9%, MMB by 2.2%, and TextVQA by 2.1%, which are unacceptable losses.
2. In Section 5.1, why was the unusual number of 142 image tokens chosen for the experiment? Additionally, if the goal is to demonstrate the effectiveness of the "text rater," it would be insufficient to test only one efficiency setting. A range of settings retaining different proportions of image tokens should be used to substantiate its effectiveness across varying conditions.
3. In the section "Sparsification Level Adaptation",  N is calculated to determine the number of tokens deleted in each layer for adaptive purposes. However, in the later experimental sections, the number of retained image tokens (e.g., 192) is specified directly. If the result of N in a decoder layer is 0, how can you specify retained image tokens to 192? Isn’t this contradictory? 
4. Rank(P) is a rather unusual way to compute visual redundancy. P represents a part of the attention map, but it is unclear why the linear correlation among attention vectors would relate to visual redundancy. Is there any supporting evidence for this, such as a reference to a paper?
5. Figure 1 shows that the patches selected by fastv are identical under different questions, which is unreasonable. Since fastv relies on the attention between text and image (this can be found in the source code), the selected patches should not be exactly the same. You may check for any errors in the process.
6. The paper mentions, "We reuse the self-attention matrix of visual-text tokens directly from the decoder layers without extra training parameters for sparsification." However, if the method requires outputting the self-attention matrix, it can not use FlashAttention, which would significantly impact inference speed.
7. In Table 1, it would be helpful to include efficiency evaluation like FLOPs and latency directly alongside performance scores on the benchmarks to facilitate comparison, the number of retained image tokens is not sufficient to evaluate efficiency.
8. One contribution claims, "it is the first attempt to explore the potential of text-aware guidance for efficient inference of VLMs." This is inaccurate, as the "fastv" approach also prunes image tokens based on text tokens’ attention to image tokens.
9. The description of the ToMe method in the Related Work section is inaccurate. "For example, ToMe (Bolya et al., 2022) prunes according to the relevance between visual tokens and text and merges both modalities through the BSM algorithm."
10. In the introduction, the calculation of the number of image tokens seems incorrect. The claim, "For instance, a 672 × 672 image in LLaVA (Liu et al., 2024) yields 2304 vision tokens that span over half of the context length," does not align with the correct calculation of 576 × 5 (four sub-images plus one resized original image). You can check it again, there might be an error somewhere.

### Questions
1. In Table 1, for the experimental results under the settings "Retain 192/128/64 Tokens," what exactly do these settings mean? For FastV, does this mean that only this number of image tokens is retained across all layers?
2. 5.1 section，"3 settings (using all tokens, only text tokens, and only text raters we select)"，explain the settings in detail.
3. Are you doing the pruning and recycling process in the prefilling stage? "we introduce a rank-based strategy to adaptively determine the sparsification ratio for each layer". If as said like this, do we prune and recycle at each layer in the prefilling stage to keep 192/128/64 tokens in experiment? Please give a clear explanation of your sparsification process, which is not stated in the paper.

### Soundness
3

### Presentation
3

### Contribution
2
