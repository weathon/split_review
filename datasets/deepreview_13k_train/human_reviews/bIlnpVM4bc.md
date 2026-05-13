# Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Efficiently modeling sequences with infinite context length has long been a challenging problem. Previous approaches have either suffered from quadratic computational complexity or limited extrapolation ability in length generalization. In this work, we present \textsc{Samba}, a simple hybrid architecture that layer-wise combines Mamba, a selective State Space Model (SSM), with Sliding Window Attention (SWA). \textsc{Samba} selectively compresses a given sequence into recurrent hidden states while still maintaining the ability to precisely recall recent memories with the attention mechanism.
We scale \textsc{Samba} up to 3.8B parameters with 3.2T training tokens and demonstrate that it significantly outperforms state-of-the-art models across a variety of benchmarks. Pretrained on sequences of 4K length, \textsc{Samba} shows improved perplexity in context lengths of up to 1M in zero-shot. When finetuned on 4K-length sequences, \textsc{Samba} efficiently extrapolates to a 256K context length with perfect memory recall on the Passkey Retrieval task, and exhibits superior retrieval extrapolation on the challenging Phonebook task compared to full-attention models. As a linear-time sequence model, \textsc{Samba} achieves a $3.73\times$ higher throughput compared to Transformers with grouped-query attention for user prompts of 128K length, and a $3.64\times$ speedup when generating 64K tokens with unlimited streaming.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a hybrid architecture mixing Mamba layer with Sliding Window Attention.

### Strengths
- The proposed architecture shows great results on common benchmark. 
- It seems also to be better at long contexts handling.
- Shows that hybrid models can be competitive alternatives to transformers.

### Weaknesses
 - The main contribution of combining attention with other linear mechanisms is not novel, and, as noted in the paper, a lot of alternatives exist.
- A comprehensive benchmarking against existing alternatives is lacking. Comparisons are only made to their proposed variants and Sliding Window Attention in fair setups. A thorough comparison with other models listed in Appendix A (such as MEGA, adapted to Mamba) would strengthen the findings. Additionally, selected architectures are evaluated on a very small scale and only measured by perplexity. While some models achieve lower perplexity, this alone may not suffice to establish superiority (e.g., in H3 by Dao et al., 2022b, lower perplexity is reported against transformer baselines).
- Results on common benchmarks are somewhat misleading. The paper aims to showcase the architecture’s strengths, yet comparisons are often made against models trained on different data distributions, which weakens the robustness of the conclusions.
- Conclusions on long-context handling remain vague, although this should be a key advantage over transformers. It would be helpful to include dataset statistics (average, median, min, max lengths) to clarify context length relevance.
- The only substantial long-context experiment, the summarization task, should be included in the main paper, with clearer discussion and analysis.
- Section 4, “Analysis,” could benefit from clearer motivation. Some explored dimensions may appear intuitive (e.g., l. 444, where SWA is shown to outperform full attention on larger sequence lengths than those used in training), which might limit the novelty of the findings. Other questions seems a bit unrelated to the paper topics (see Questions).
- Length extrapolation, a key aspect of the paper, is barely motivated or discussed in relation to prior work.
- The paper overall feels somewhat unstructured and difficult to follow. Tables present different baselines inconsistently, and messages regarding architectural advantages are interleaved with comments on training data quality (l. 229). The evaluation setup lacks consistency (performance is sometimes assessed on real benchmarks, other times by perplexity), and the rationale behind baseline choices or research questions is insufficiently explained.

### Questions
- In the original Mamba paper, they already experiment with mixed Mamba/Attention. Can you contextualize the your contribution with respect to this original architecture?

- What is the evaluation setup for the summarization in Appendix B? Also, please bold the best performance on SQUALITY.

- I’m having difficulty identifying the key factors that contribute to the optimal architectural design. What elements are beneficial here? Is it the MLP, Mamba, or both, and to what extent? I’d be interested in seeing results for a SWA > MLP > SWA > MLP architecture as an example (where some SWA layers are substituted with MLP).

- In the length extrapolation experiments, can you clarify whether the models can extrapolate up to 256k tokens in Passkey Retrieval, but struggle with generalization in Phonebook performance?

- In several sections, you mention that Full Attention performance deteriorates beyond a specific context size. This seems logical, couldn't these attention be converted to sliding attention especially l. 444?

- In addition to the training curves shown in Fig. 7 of Appendix D, could you also provide the validation curves?

- In Section 4, I don’t fully understand the relevance of the question: "How to train models with Sliding Window Attention (SWA)?"

- This question might benefit from rephrasing, since your response is exploratory rather than definitive, focusing on the distribution of attention rather than giving a clear answer.

- Line 051: The phrase "limited context extrapolation ability in perplexity metrics" is unclear. Are you suggesting that the extrapolation metrics increase perplexity when the models exceed their initial training context size?

- Line 164 implies that SWA was specifically designed to address Mamba’s limitations, this is misleading.

### Soundness
3

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
4

### Summary
Authors investigate the utility of attention-state-space hybrids over attention-only models (e.g. sliding window attention (SWA)) and state-space-only models (e.g. Mamba) by training language models in the 400M-4B parameter range. They propose a model block Mamba->MLP->SWA->MLP and perform ablation studies in a language modeling (LM) setup. Pretrained models are evaluated 0-shot on 15 established downstream benchmarks.

**Experiments**

1. Authors perform an ablation study on the Phi-2 training corpus (230B tokens) and report modest improvements over the Mamba->SWA->MLP baseline. On reading comprehension tasks such as SQuAD, the addition of SWA to Mamba leads to significant improvement over the Mamba-only baseline.

2. Authors explore replacing Mamba in the hybrid block with other efficient alternatives such as Gated Linear Attention and RetNet. Models are trained on SlimPajama corpus with 4k length and evaluated on lengths up to 16k, with the Mamba-based block reporting the lowest perplexity.

3. Authors study the length extrapolation abilities of models trained with 4k length. On the ProofPile test set, the hybrid block shows improved and slowly decreasing perplexity with increasing context length, and is lower than that of the SWA-only baseline.

4. Authors investigate the model's performance on memory-intensive tasks. After finetuning for 500 steps with 4k input length, the hybrid block achieves perfect performance on PassKey Retrieval for lengths up to 256k. On the PhoneBook task of retrieving phone numbers from name-number pairs, models finetuned for 100 steps with 4k input length show superior performance compared to full attention when evaluated on lengths up to 8k.

5. Analysis of attention scores reveals that middle layers have lower entropy compared to top/bottom layers, suggesting specialization in precise information retrieval.

6. The hybrid model trained on Phi-3's 3.2T token corpus matches parameter-matched Phi-3's performance on downstream tasks.

### Strengths
1. The investigation of SSM-attention hybrids is well motivated and timely. The empirical findings and model performance should interest a broad audience. The trained checkpoints would be a useful resource for the research community.

2. Experiments are comprehensive, showing significant improvements in length extrapolation tasks and efficiency on long inputs.

### Weaknesses
1. Limited novelty - adding an MLP in the model block is an incremental contribution. The performance gap between Mamba->MLP->SWA->MLP and Mamba->SWA->MLP is modest.

2. The models' strong performance relies on proprietary datasets (Phi-2 and Phi-3), making fair comparisons difficult.

3. The relationship with previous SSM+SWA hybrid works (Griffin/Hawk) needs clearer positioning.

### Questions
1. In models with SSM layers, was RoPE still necessary in SWA? (This doesn't affect my evaluation)

2. Are the Phi-2 and Phi-3 training sets open-sourced? Reproducibility is challenging without access to these datasets.

3. Please add Mamba->SWA->MLP baseline to Table 3.

4. Consider including Mistral results on PhoneBook.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper describe the hybrid Language model which combined Mamba layers and Sliding Windows Attention layers. Authors trained a number of models upto 3.8B size and showed that model performed well both on multiple standard LLM benchmarks and on some long context benchmarks (e.g. Passkey retrieval ). They also evaluated model on  Phonebook to show model limitation. Samba has better throughput comparing to regular Transformers both for  sequences with long prompt, and on generation long context.

### Strengths
Authors build a good LM which can both process long prompt and generate very long context  reliably. The simple idea - to combine mamba with SWA -  is very well executed, Solid experimental part, good ablation study. The paper is well written.

### Weaknesses
The main weakness of  Samba, is that similar to other hybrid models which use local attention it solves long context problem only partially. Experiments on Phonebooks show that the accuracy of the model rapidly goes down after 4K (Fig. 5).

I would also suggest to move the following observation from Appendix G  to main part of the paper, e.g. to Analysis or Conclusion section:  
"Although Samba demonstrates promising memory retrieval performance through instruction tuning, its pre-trained base model has retrieval performance similar to that of the SWA-based model ... "

A few minor comments:
1. Inconsistent location of captions for figures and tables (sometimes above , sometimes below). Figure 3 is located inside text. 
2. The implementation details: RoPE base is missing

### Questions
It would be interesting to see if Samba is able to handle 
 a) more complex Needle-in-the-Haistack from RULER benchmark https://arxiv.org/abs/2404.06654 
 b) complex multi--hop  reasoning tasks from HELMET benchmark https://arxiv.org/pdf/2410.02694

### Soundness
3

### Presentation
3

### Contribution
3
