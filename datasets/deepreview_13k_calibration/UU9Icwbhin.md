# Retentive Network: A Successor to Transformer for Large Language Models

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
In this work, we propose \textbf{Retentive Network} (\textsc{RetNet}) as a foundation architecture for large language models, simultaneously achieving training parallelism, low-cost inference, and good performance. We theoretically derive the connection between recurrence and attention. Then we propose the retention mechanism for sequence modeling, which supports three computation paradigms, i.e., parallel, recurrent, and chunkwise recurrent. Specifically, the parallel representation allows for training parallelism. The recurrent representation enables low-cost $O(1)$ inference, which improves decoding throughput, latency, and GPU memory without sacrificing performance. The chunkwise recurrent representation facilitates efficient long-sequence modeling with linear complexity, where each chunk is encoded parallelly while recurrently summarizing the chunks. Experimental results on language modeling show that \textsc{RetNet} achieves favorable scaling results, parallel training, low-cost deployment, and efficient inference. The intriguing properties make \textsc{RetNet} a strong successor to Transformer for large language models. Code will be available at \url{https://aka.ms/retnet}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes RetNet, a model that promises training parallelism, low cost-inference and good performance. It is presented as a successor to Transformers and comes with very impressive results to back up this stance.

### Strengths
The experimental results of this approach are compelling. It appears that as model parameters increase beyod 2B, retentitive networks outperform Transformers on language modelling according to perplexity.

Inference no longer requires addititional KV cache allowing for O(1) inference cost.

RetNet allows for O(N) long-sequence memory complexity by accumulating into a buffer.

### Weaknesses
Novelty: this is essentially a transformer without the softmax and an added time decay. It just so happens that with scale, it appears that this difference does not hinder RetNet performance.

Clarity: The paper gets pretty dense at times affecting readability. Also figure 2b is hard to understand without the code.


This paper lacks a broader impacts section, its addition would strengthen the paper.

The code for the work appears to be closed source, given the overwhelmingly positive results.. it makes comparison and benchmarking against this approach difficult for other researchers in the field.

### Questions
So the results look overwhelmingly positive, could the authors discuss the shortcomings of this approach? On which tasks does this model not work well?


Will the code for this paper be open-sourced?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a new network architecture, retentive network (RetNet) for large language modeling. Similarly as state space models (SSMs) and Linear Attention models, RetNet can be formulated both in a parallel and recurrent views, achieving parallel training and efficient inference/decoding. 

The authors conducted experiments on large-scale pre-training form language modeling, with model size from 1.3B to 13B. The proposed RetNet obtained better zero/few-shot performance on benchmarks than standard Transformer. And the speed and memory efficiency of RetNet is also slightly better than Transformer with Flash Attention.

### Strengths
The RetNet is well-motivated and the equations are clear. The experiments are conducted with relatively large models.

### Weaknesses
There are several serious concerns about this paper:

1. Table 1 is mis-leading. If I understand correctly, the recurrent state $s_n$ in Eq (1) is in the shape of $d\times d$, where $d$ is the model dimension and is very large in practice (sometimes even larger than $N$). In S4 or other SSMs, the shape of the recurrent hidden state is $h\times d$ with relatively small $h$, e.g. $h=32$. However, in Table 1 the authors claimed the inference cost of RetNet is $O(1)$. The authors should clarify the exact shape of the recurrent state in the multi-head setting and provide a more detailed analysis of the inference cost, especially considering the computational overhead of managing a potentially large state during decoding.

2. Table 3 is unclear. If I understand correctly, the parallel representation in Eq(5) is used for model training. However, the complexity of Eq(5) is almost the same with standard attention mechanism, with only difference that it does not need to compute softmax. Then why RetNet is faster and using less-memory than Flash Attention? Flash Attention also leveraged the block-wise computation of the attention matrix, which is similar to the chunkwise representation of RetNet. In addition, which version of Flash Attention was used in these experiments? Flash Attention v2 has been significantly optimized. The authors need to provide a more detailed breakdown of the computational steps and memory access patterns to justify the claimed speed and memory efficiency gains over highly optimized attention implementations like Flash Attention.

3. The experimental setting is unconvincing. Though the authors scaled-up RetNet to 13B, the total number of training tokens are only 100B. It is well-known that Transformer is data-eager, and it is unfair to compare with Transformer with relatively small training data. Moreover, the improved version of Transformer in Llama (with RMSNorm and SwiGLU) has achieved significantly better results than the standard Transformer. But all the comparisons in this paper are with standard Transformer. The authors should provide a more comprehensive comparison with state-of-the-art Transformer variants and also justify the choice of training data volume given the known data requirements of Transformer models.

4. In Table 1, the authors claimed that only Transformer and RetNet are achieving "good performance". However, there are no direct comparison of RetNet with other models in large-scale setting. The results in Table 4 were conducted with a small 200M model size and only 5B tokens. The authors need to include more extensive comparisons with other relevant architectures, especially in large-scale settings, to support the claim of RetNet achieving "good performance" relative to the broader landscape of sequence models.

### Questions
The parallel allocation adjustment, i.e setting $V$ twice dimension of $d$, has already been investigated in prior works, such as Flash[1] and Mega[2].


[1] Hua et al., Transformer Quality in Linear Time.

[2] Ma et al., Mega: Moving Average Equipped Gated Attention.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Retentive Network as a foundational architecture for large language models. Compared to Linear Transformers, Recurrent Networks, and Transformers, Retentive Networks can train in parallel, are low cost in inference, and have high quality. This paper discusses an interesting architectural design space where: 1) Transformer model families are inference inefficient while can be trained in parallel and are high quality; 2) Recurrent Networks on the other hand, can run inference relatively at lower cost but cannot be trained efficiently. The proposed Retentive Networks achieves all three by introducing a multi-scale retention mechanism to substitute multi-head attention. The method is greatly simplified without key-value cache tricks. The chunkwise recurrent representation can perform efficient long-sequence modeling. Empirical resuolts decodes 8x faster and saves 70% of memory compared to Transformer. During training, it is 7x faster with 20%-50% lower memory.

### Strengths
- The proposed retention mechanism has a dual form of recurrence and parallelism. 

- The paper is well written and formalized properly.

### Weaknesses
 - The paper is not clear to the reviewer why these two forms in Figure 2 (a) and Figure 2 (b) are equivalent.

- Are there any theoretical proof that retention is more capable than full attention?

- The paper is not clear why in Figure 3, RetNet is more effective in the large model regime. According to some prior work [1][2], two model architectures should not cross over when scaling the model up in log scale.

- Results are only provided on classification and summarization tasks, not generative tasks like translation and question answering. This shows limited generalization of the model architecture.

### Questions
1. Why would RetNet be better than full attention based transformer in terms of quality? Full attention should be more capable than recurrent networks. 

2. Do you have results on NLG tasks? Refer to GPT3 paper and report some numbers on generative tasks. 

3. The model scaling curve in Figure 3 looks odd to me. Why would the two lines cross over? It does not align with other empirical findings in early papers.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a network called RetNet for language modeling, which has a linear training complexity and constant inference complexity.

### Strengths
This paper proposes a new architecture called RetNet, which has linear training complexity and constant inference speed.

### Weaknesses
The main weakness with this paper are overclaiming and lack of citations, which can be misleading for readers. For example, the claim in Figure 1 that "RetNet makes the 'impossible triangle' possible" is an absolute overclaim because the paper lacks validation with larger models and comparison with open-source Transformer models. On the other hand, the authors claim that RWKV and Linear Attention perform poorly, but according to [1], [2], their performance can be on par with Transformers. In Section 2, the authors introduce a new term called "Retention," but this is essentially the same as Linear Attention without the denominator, which has already been proposed in [2, 3]. Additionally, the use of EMA in MEGA and RWKV has been implemented, but the authors fail to cite these works.



### Questions
1. Figure 1 is an absolute overclaim because RWKV[1] and H3[2] have already demonstrated models at the billion-scale level that can achieve performance comparable to Transformers, with parallel training and constant inference. I suggest the authors remove this figure as it could mislead readers.
2. The description of RWKV in Table 1 is completely wrong. According to RWKV[1] and the description in [2], RWKV can indeed be computed in parallel. On the other hand, according to the RWKV paper, its performance is comparable to Transformers, so describing its performance as ✔ is also inaccurate. Overall, Table 1 is highly misleading and can affect the authors' judgment of model performance. I suggest the authors reorganize this table accordingly. 
3. The form of Equation 1 is similar to RFA-GATE presented in [7], but the authors did not cite these articles throughout the paper.
4. The form of GroupNorm in Equation 8 is consistent with the NormAttention proposed in [5], but the author does not cite it at all.
5. There is a mistake in the description of the Linear Attention section in Section 2.4. Firstly, Linear Attention refers to the use of the Right-product trick to reduce complexity, but it does not necessarily imply approximation. For example, [4], [5], and [6] do not involve an approximation approach like softmax. 
6. The statement "However, linear attention struggles to effectively encode position information, rendering the models less performant" should be supported by a reference since there could be various reasons for the poor performance. Moreover, the issue of the performance of Linear Attention has already been addressed in [5], where they propose a solution.
7. The discussion about MEGA and MEGA-chunk is missing, as they are similar to RetNet in utilizing the EMA technique.
8. Table 2 lacks comparison with open-source models. Firstly, the configuration of the Transformer is not mentioned, whether it is based on GPT2 architecture or Llama architecture. Additionally, there is no information provided regarding the parameter count or training data. On the other hand, there is no comparison with open-source models such as Bloom, Pythia, GPT-Neo, or RWKV. Comparing with these open-source models would allow readers to better understand the performance level of the proposed model. 
9. The evaluation scope is too limited, for example, MMLU is not assessed.
10. It is indeed odd that the evaluation datasets in Tables 4 and 5 are inconsistent with Table 3. There should be further explanations provided to clarify this discrepancy.
11. There is a lack of ablation analysis on the architectural design, such as why the dimension of $W_v$ is chosen as d * 2d. On the other hand, an ablation for adding head dimension should be included in Table 5.

[1] Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, Kranthi Kiran G. V., Xuzheng He, Haowen Hou, Przemyslaw Kazienko, Jan Kocon, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Xiangru Tang, Bolun Wang, Johan S. Wind, Stanislaw Wozniak, Ruichong Zhang, Zhenyuan Zhang, Qihang Zhao, Peng Zhou, Jian Zhu, and Rui-Jie Zhu. RWKV: reinventing rnns for the transformer era. CoRR, abs/2305.13048.

[2] Tri Dao, Daniel Y. Fu, Khaled Kamal Saab, Armin W. Thomas, Atri Rudra, and Christopher Ré. Hungry hungry hippos: Towards language modeling with state space models. CoRR, abs/2212.14052, 2022.

[3] Eric Martin and Chris Cundy. 2017. Parallelizing linear recurrent neural nets over sequence length. ArXiv, abs/1709.04057.

[4] Zhen Qin, Weixuan Sun, Hui Deng, Dongxu Li, Yunshen Wei, Baohong Lv, Junjie Yan, Lingpeng Kong, and Yiran Zhong. cosformer: Rethinking softmax in attention. In ICLR, 2022.

[5] Zhen Qin, Xiaodong Han, Weixuan Sun, Dongxu Li, Lingpeng Kong, Nick Barnes, and Yiran Zhong. The devil in linear transformer. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 7025–7041, Abu Dhabi, United Arab Emirates, Dec. 2022. Association for Computational Linguistics.

[6] Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention. In Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event, volume 119 of Proceedings of Machine Learning Research, pages 5156–5165. PMLR, 2020.

[7] Hao Peng, Nikolaos Pappas, Dani Yogatama, Roy Schwartz, Noah Smith, and Lingpeng Kong. Random feature attention. In International Conference on Learning Representations, 2020

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
