# CLEX: Continuous  Length Extrapolation for Large Language Models

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Transformer-based Large Language Models (LLMs) are pioneering advances in many natural language processing tasks, however, their exceptional capabilities are restricted within the preset context window of Transformer. Position Embedding (PE) scaling methods, while effective in extending the context window to a specific length, demonstrate either notable limitations in their extrapolation abilities or sacrificing partial performance within the context window.  Length extrapolation methods, although theoretically capable of extending the context window beyond the training sequence length, often underperform in practical long-context applications.
To address these challenges, we propose \textbf{C}ontinuous \textbf{L}ength \textbf{EX}trapolation (\textbf{\ourMethod{}}) for LLMs. We generalise the PE scaling approaches to model the continuous dynamics by ordinary differential equations over the length scaling factor, thereby overcoming the constraints of current PE scaling methods designed for specific lengths. Moreover, by extending the dynamics to desired context lengths beyond the training sequence length, \ourMethod{} facilitates the length extrapolation with impressive performance in practical tasks. We demonstrate that \ourMethod{} can be seamlessly incorporated into LLMs equipped with Rotary Position Embedding, such as LLaMA and GPT-NeoX, with negligible impact on training and inference latency. Experimental results reveal that \ourMethod{} can effectively extend the context window to over 4$\times$ or almost 8$\times$ training length, with no deterioration in performance. Furthermore, when evaluated on the practical LongBench benchmark, our model trained on a 4k length exhibits competitive performance against state-of-the-art open-source models trained on context lengths up to 32k.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the length extrapolation problem of large language models, i.e., training on short sequences while testing on long sequences. The work is built upon RoPE. Continuous PE scaling is introduced as a RoPE embedding scaling method.

### Strengths
Originality:
Continuous PE scaling is introduced as a RoPE embedding scaling method.


Clarity:
The paper is easy to follow and understand.

Significance: 
Long-sequence modeling is important for many downstream applications.

### Weaknesses
 - The work is built upon RoPE, which limits its application to other models that don't use RoPE.

- According to Table 1, the models still do not perform "real" length extrapolation. The PPL results become worse when the length is increased. If PPL becomes worse, why not directly use window-based methods in practice? The real-world value of the proposed method is questionable.

- Straightforward method (such as https://arxiv.org/abs/2309.16039) works well in practice. It also challenges the value of research on length extrapolation, as long as we finetune the models. So the evaluation setting can be improved.

- Fig 5 indicates that different models perform similarly across tasks, despite GPT. The significance of the method is not clearly demonstrated.

- The lines in the right subfigure of Fig 5 are not correctly shown. The figure can be updated.

### Questions
- The work is built upon RoPE, which limits its application to other models that don't use RoPE. How to use the proposed method for other PE methods?

- According to Table 1, the models still do not perform "real" length extrapolation. The PPL results become worse when the length is increased. If PPL becomes worse, why not directly use window-based methods in practice? The real-world value of the proposed method is questionable.

- Straightforward method (such as https://arxiv.org/abs/2309.16039) works well in practice. It also challenges the value of research on length extrapolation, as long as we finetune the models. The proposed method can be integrated into the above pipeline, which provides more valuable evaluation metrics.

- Fig 5 indicates that different models perform similarly across tasks, despite GPT. The significance of the method is not clearly demonstrated.

- The lines in the right subfigure of Fig 5 are not correctly shown. The figure can be updated.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new positional embedding scaling to be used for using a model with different context lengths than seen during training.
The idea is an extension of rotary positional embedding, for which the frequencies used are dynamically updated depending on the desired context length. The method used to actually update those frequencies is through a neural ODE whose parameters are also trained.

### Strengths
I think the proposed method has some value. It sticks to a well established PE scheme, and then proposes a way to update its parameters that is _trained_ to be good, instead of just wishing it will be based on some assumptions. For this reason, the paper definitely deserves consideration in my opinion.

The proposed method moreover seems to be providing good performance for extrapolation, which was the intent.

### Weaknesses
 * Not much details is provided in the main text regarding how we train such a beast. I must say this looks quite daunting to me how I would train a NODE along my transformer model. I guess it would help to have some explanations to it.
* I am missing some exploration of what the model is producing regarding the frequencies for ROPE. As I understand, it boils down to being able to produce a new set of frequencies for ROPE to use for any input lengths. This would have been feasible to actually display that. Since many people have played with the idea of manually setting such parameters, I am curious whether a trained method could give us insights as to what good frequencies actually look like. Are we observing high frequencies to disappear to favor long term dependencies? Such things.

### Questions
The paper is mostly interesting and I guess that anyone working on the topic would have a few questions
* the random sampling method you propose look like a strong and nice ingredient of your approach. Could you just make it clear for me whether the _order_ of the samples is maintained within the sequence?
* Your method definitely allows some extrapolation as per your experiments. However, I somehow feel that it could also shine for "superresolution"/"interpolation", i.e. infilling missing data within a sequence. This feeling comes from your random sampling idea. It looks like you are basically simulating "missing data".
* "Unlike the previous PE scaling methods built on a larger scaling factor would lead to inferior performance on the lengths corresponding to smaller counterparts, the continuous PE scaling would enable non-destructively generalisation to larger scaling factors via adaptive continuous dynamics". This would be great, but at this point in the paper, I don’t see why the proposed scaling method would _necessarily_ enable it. Maybe you could rephrase that in a more humble way

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces CLEX, a method to efficiently extend the context window of LLMs without compromising performance. Traditional methods either have length limitations or suffer performance drops. CLEX overcomes these by modeling the relation of sequence length and frequency in RoPE during position extrapolation as a continuous system. Specifically, it utilizes Neural ODE as a tool to do this. In tests, CLEX extends context windows to over 4x the training length without performance loss and beat several popular methods both in long sequence modeling and downstream tasks.

### Strengths
1: The theory part is closely combined with practical part. And the performance of the proposed method also aligns with the theoretical derivation. 
2: The performance of the proposed method is good. And the experiments are comprehensive. 
3: Besides the main results, this paper also provided some insightful observations about LLMs' length generalization.

### Weaknesses
Please check the question section

### Questions
1: By my understanding, the core idea of this paper is to do position extrapolation with an appropriate frequency for different sequence lengths. Is it necessary to utilize Neural ODE? In another word, can we use a regular NN? As it seems that a regular NN can do the same thing. (Not quite sure, for I'm not an expert of Neural ODE)

2: Could you please provide more details about the training/fine-tuning? Did you train all the baseline models with the same number of tokens, the same batch size as well as the same steps? If so, for PI, its paper mentioned that they only fine-tuned the LLM for ~ 1000 steps, while for some other baselines such as replacing RoPE with Alibi for Llama-2, the tuning steps should definitely be much larger. With different required number of training steps is the performance comparison fair enough? 

3: Also, I'm wondering if there's any explanation to the poor performance on LongBench's synthetic tasks.

4: Compared to Random Position, the main difference is that CLEX add adaptive frequency for different sequences, it that correct?

5: Still about Random Position, its original paper and some blogs (https://kexue.fm/archives/9444, it's in Chinese, you may translate it to English first) showed that it shows good length generalization ability. But in  Table-1, Random Position does not work at all ( trained on 4k, and can only keep low PPL at 4k), do you have any thoughts about it?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes CLEX, a method that enables length extrapolation on Rotary position embedding (RoPE) by finetuning on a dataset. Prior work has found that finetuning with a position embedding scaling (PE scaling) on either the position or the frequency values of RoPE can enhance the extrapolation of a pre-trained language model. Based on the PE scaling, CLEX models the position-frequency values of RoPE with a neural ODE and the YaRN model, with an aim to learn the continuous dynamics over the length scaling factor during PE scaling. The experiments demonstrate a strong extrapolation compared with prior PE scaling methods (Position Interpolation, YaRN, CodeLLaMA) and non-PE scaling methods (ALiBi, RandomPos).

**Post Rebuttal Update**

I acknowledge the authors' efforts in addressing the questions. The new experiments have effectively addressed my concerns. As a result, I have raised my score.

### Strengths
* CLEX demonstrates strong length extrapolation results (evaluation length > train length) compared with prior PE scaling methods such as Position Interpolation,YaRN, and CodeLLaMA.

* When the evaluation length is smaller than the train length (i.e. finetuning length), CLEX exhibits a better performance compared with prior PE scaling methods.

* The ablation includes a few useful topics such as continuous vs. discrete dynamics, sampling strategy, and log-scaling.

### Weaknesses
 * Despite a strong extrapolation performance, the motivation for adopting continuous modeling is a bit unclear. It seems that the continuous model has to be somehow discretized on a few points (e.g. evaluating the integral of equation 12). If this is true, doesn't this imply an equivalent discrete modeling? Furthermore, the specific discretization strategy and its impact on performance should be more thoroughly analyzed. The choice of discretization points and their density could significantly affect the approximation of the continuous function and thus the final results. 
* CLEX is adopting YaRN in equation 13, so it seems some part of the performance of CLEX is due to YaRN. An ablation of CLEX without YaRN is needed. It is crucial to understand the individual contributions of the learned continuous scaling function and the YaRN component to the overall performance. Without this ablation, it is difficult to ascertain the true effectiveness of the proposed continuous modeling approach.
* CLEX is based on PE scaling, which requires a finetuning dataset. However, non-PE scaling methods (e.g., ALiBi and RandomPos) don't require finetuning. So it doesn't seem fair to compare CLEX with non-PE scaling methods. The comparison should focus on methods that operate under similar constraints, such as requiring finetuning. The practical applicability of CLEX should be evaluated against other PE scaling methods, rather than methods that do not require finetuning.
* The author mentioned that CLEX is computationally demanding due to the evaluation on the integral. Maybe the author can comment more on the training time. The computational cost of evaluating the integral, especially during training, needs to be quantified and compared with other methods. This is important for understanding the practical feasibility of the approach.
* The author claimed that AliBi-like methods (attention biasing) struggle in practical tasks requiring long-context dependency; however, the cited evidence is on AliBi. Among the author-cited AliBi-like methods, there are attention-biasing methods that achieve better long-context dependency than Alibi. Maybe the author can clarify on this. The claim about the limitations of attention-biasing methods should be supported by a more comprehensive analysis, including a comparison with other attention-biasing methods that have demonstrated better long-context performance. The specific types of tasks where these methods fail should also be clarified.
* The notations are confusing sometimes. For example, $\lambda$ is supposed to be an amplification factor but is missing in equation 13. The notation should be consistent and clearly defined throughout the paper. The role of each parameter and its impact on the model should be explicitly stated.

### Questions
* In Table 1, the authors provided numbers for CLEX with training length 4k, 8k, and 16k. However, most of the other PE scaling methods (PI and YaRN) are trained only on 16k. I wonder how PI and YaRN perform when finetuning with 4k and 8k context length.

* For other questions, see the Weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
