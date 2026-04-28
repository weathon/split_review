# PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models~(LLMs) are trained with a pre-defined context length, restricting their use in scenarios requiring long inputs. Previous efforts for adapting LLMs to a longer length usually requires fine-tuning with this target length~(\textit{Full-length} fine-tuning), suffering intensive training cost. 
To decouple train length from target length for efficient context window extension, we propose \textbf{Po}sitional \textbf{S}kip-wis\textbf{E}~(\methodname{}) training that smartly simulates long inputs using a fixed context window. This is achieved by first dividing the original context window into several chunks, then designing distinct \textit{skipping bias terms} to manipulate the position indices of each chunk. These bias terms and the lengths of each chunk are altered for every training example, allowing the model to adapt to all positions within target length. Experimental results show that \methodname{} greatly reduces memory and time overhead compared with Full-length fine-tuning, with minimal impact on performance. Leveraging this advantage, we have successfully extended the LLaMA model to 128k tokens using a 2k training context window. Furthermore, we empirically confirm that \methodname{} is compatible with all RoPE-based LLMs and position interpolation strategies. Notably, our method can potentially support infinite length, limited only by memory usage in inference. With ongoing progress for efficient inference, we believe \methodname{} can further scale the context window beyond 128k.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a method called Positional Skip-wise Training (PoSE) to extend the context window size of large language models (LLMs) during fine-tuning. PoSE simulates long inputs by manipulating position indices within a fixed training context window, decoupling the training length from the target length.

### Strengths
1. The proposed PoSE approach is effective in extending the context window size of various RoPE-based LLMs to up to 128k tokens with minimal performance degradation compared to full-length fine-tuning.

2. PoSE significantly reduces the memory and time complexity compared to full-length fine-tuning, achieving up to 64x speedup.

3. PoSE is compatible with various RoPE-based language models and positional interpolation strategies.

4. The idea of manipulating position indices within chunks to simulate longer inputs is novel and effective as shown in the experimental results.

### Weaknesses
1. The theoretical analysis of PoSE is limited. More discussion of how manipulating position indices allows the model to generalize to longer contexts could strengthen the paper. Specifically, the paper lacks a rigorous explanation of why training with manipulated positional indices within a fixed window can effectively simulate longer context windows. It would be beneficial to include a more in-depth analysis of the positional encoding space and how the proposed method affects the model's ability to extrapolate to unseen positional ranges. The current analysis is purely empirical, and a theoretical grounding would significantly improve the paper's contribution.

2. The experimental setups and hyperparameters are not thoroughly described. More details would increase reproducibility. For example, the specific choices of batch size, learning rate, optimizer, and regularization techniques are not clearly stated. The paper should also include details about the hardware used for training and inference, as well as the specific datasets used for evaluation. Without these details, it is difficult to verify the claims made in the paper and replicate the results.

3. It would be better that if the authors could provide some failure cases that this method might leads to some missing details or inferior answers to the standard fine-tuned models. Because it should be inevitable that the speedup has a cost on performance. Only the perplexity comparison is a bit unclear for understanding. It would be more clear that the perplexity gap lies in retrieval, summarization, or some other abilities. The paper should investigate specific tasks where PoSE might underperform full-length fine-tuning, such as tasks requiring precise positional understanding or long-range dependencies. A more detailed analysis of the trade-offs between computational efficiency and performance on various downstream tasks would be valuable.

### Questions
Please see the weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed Positional Skip-wisE (PoSE) training for extending the context length of LLMs. The idea is to divide the input into multiple chunks and add randomly sampled bias values to later chunks. This effectively simulates the positions the model will see during the inference stage. Experiments with LLaMA show that PoSE is effective in extending RoPE-based LLMs, and is compatible to other length extension techniques like linear, NTK, and YaRN,

### Strengths
1. The idea of PoSE is neat and novel. PoSE is able to reduce the GPU memory requirement for training long-context LLMs.
2. Experiments show that PoSE is effective in extending models trained on 2k context length to 32k. Also, the author explored extending models trained on 2k to 128k in Table 2 and demonstrated the potential of PoSE.

### Weaknesses
1. Finetuning the model with PoSE will degrade its performance on standard benchmarks, according to Table 3. It is unclear if it can be mitigated from the paper. Also, the perplexity of PoSE is worse than finetuning with the target sequence length (shown in Table 1). Thus, if the user really cares about the performance, finetuning with the target sequence length still gives the best result.
2. From Table 1, I haven't seen the comparison between PoSE and applying NTK directly without training. In addition, the author has not provided enough details in how it conducted full-length finetuning. Is it to first extend the sequence length to 16K via linear or NTK and finetune the model on the 16k sequence length?

### Questions
How did you do full-length finetuning? Have you used length expansion before finetuning on the target sequence length?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce a novel technique known as Positional Skip-wise Training (PoSE) for extending the context window of Large Language Models (LLMs). While existing methods like Positional Interpolation (PI), YaRN, and NTK Interpolation have proven effective in extending the context window of LLMs, they require extensive fine-tuning of the LLM with the entire context window. This fine-tuning process imposes a high computational cost due to the quadratic complexity of LLMs relative to the length of the context window.

To address this challenge, the authors propose a strategic approach during training by selectively skipping certain positions in the middle for each batch. As illustrated in Figure 1, this technique allows the model to effectively perceive a context length of 8192 tokens while using a training-time context window of just 2048 tokens. Consequently, this method significantly reduces the training cost. When evaluated on prominent long-context datasets, including GovReport, Proof-pile, and PG19, the authors demonstrate that PoSE achieves comparable performance to full-context fine-tuning, all while delivering a substantial speedup (as shown in Figure 3).

### Strengths
1. The paper is well-written and offers clear, accessible explanations.

2. The results presented in Table 1 demonstrate the effectiveness of the proposed method in extending the context of Language Model (LLM). Furthermore, the performance of PoSE is comparable to that of full-length fine-tuning, highlighting the evident benefit of skipping contiguous token chunks.

3. PoSE excels in both memory reduction and computation time, as illustrated in Figure 3.

4. PoSE proves to be adaptable across various positional encoding interpolation methods, including linear, NTK, and YaRN, thereby enhancing its versatility and applicability.

### Weaknesses
I am uncertain about whether PoSE has genuinely extended the contextual window. While the current PPL evaluation results are undoubtedly promising, there's a possibility that methods demonstrating low PPL on PG19/GovReport might not effectively comprehend longer contexts. It's possible that the proposed method excels in consistently generating fluent text over extended periods but falls short in truly grasping the nuances of extended context. If that is the case, the potential impact of PoSE could be rather limited, since there are training-free methods (StreamingLLM, LM-Infinite) that can achieve this goal.

To address this concern, I recommend that the authors consider conducting additional experiments using benchmarks like LongBench and ZeroSCROLLS. Additionally, employing benchmarks utilized by Llama 2 Long could provide valuable insights into the capabilities of PoSE in handling more extensive contextual information.

### Questions
I believe that PoSE demonstrates proficiency in both PPL and key retrieval evaluations. I look forward to your response to my inquiry regarding the real extension of the context window, as mentioned in the Weaknesses section.

In addition, I am curious about the performance of the proposed method when the first trunk does not initiate from position 0. Recent concurrent works, such as LM-Infinite and StreamingLLM, have highlighted the significance of retaining the first few tokens in the KV cache for zero-shot context extension, without requiring fine-tuning. I am intrigued to know if the design of $u_0=v_0=0$, which resembles the approach proposed in these two papers, holds the same relevance when applied to a fine-tuned LLM. It would be greatly appreciated (though not obligatory) if the authors could include a discussion on the efficacy of fine-tuning in comparison to these zero-shot methods. For example, does the PPL on long context benchmarks improve with PoSE? Does PoSE unlock new capabilities which zero-shot methods do not have? I will update the score to 8 if the authors provide interesting discussions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
the paper presents pose, a novel mechanism to extend the context window of LLMs that decouples train length from target length. It achieves this by simulating longer inputs instead of directly training on longer inputs.

### Strengths
1. the paper is well written; the method is well illustrated.
2. the problem is important, and the method can greatly reduced the memory and computation requirements.

### Weaknesses
1. section 3.1 and 3.2 are better to be placed in a different background section, or in related work.
2. the evaluation for long context is limited - they are mostly all perplexity based. The only available non-perplexity experiment is the one with passkey retrieval, but the baselines are not comprehensive. Can the authors either provide more non-perplexity based measure, or include more baseline for Figure 2?

### Questions
Please address the weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
