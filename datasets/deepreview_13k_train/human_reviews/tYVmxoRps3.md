# IS TRANSFORMER A STOCHASTIC PARROT? A CASE STUDY IN SIMPLE ARITHMETIC TASK

- Decision: Reject
- Scores: 6, 3, 6, 1

## Abstract
Large pre-trained language models have demonstrated impressive capabilities, but 
there is still much to learn about how they operate. In this study, we
 conduct a investigation of the autoregressive transformer’s ability to
 perform basic addition operations. 
 Specifically, by using causal analysis we found that a few different attention heads in the middle layers control the addition carry, with each head processing carries of different lengths. Due to the lack of globality in these attention heads, the model struggles to handle long-sequence addition tasks. By performing inference intervention on mistral-7B, partial task performance can be restored, with the accuracy on 20-digit long-sequence additions from 2\% to 38\%. Through
fine-tuning, a new mechanism branches out for handling more complex cases, yet
it still faces challenges with length generalization. Our research reveals how the
model performs addition, and further provides insights into the debate on whether
these models are merely statistical.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies how pre-trained autoregressive language models perform addition operations. It founds that the model relies on localized attention distribution for handling carry operations. Thus it's hard for the model to process inputs with long sequences. The paper tries to restore the model's performance by intervening in attention during inference without training. The experimental findings show that autoregressive models rely on the staircase attention patterns to transmit carry-encoded value tokens to the final token for prediction Since their analysis shows that many errors stemmed from incorrect handling of carries, they try to restore the model's internal mechanisms by modifying the attention weights depending on whether there is a carry or not. The paper also tried fine-tuning with long addition data, with carry length up to 10. While fine-tuning is effective in improving the accuracy, it doesn't extend the model's ability to do addition with correct carries beyond 10, the limit set in the training time.

### Strengths
- Carefully designed tasks and intervention techniques to understand how the model performs addition. From the analysis, designing data to test the models' abilities to do addition with long carry chain.

### Weaknesses
 - Finetuning experiments are done with one of the pre-trained models in the analysis.

### Questions
- Have the authors considered similar experiments for substraction?
- How does it affect the model's performance if we revert the input so that it becomes the order that humans perform addition?
- What's the authors thought on whether the model are merely statistical or there is deeper reasoning mechanism embedded in the model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper attempts to study the carry propagation error for the task of addition when LLMs such as mistral and Lllama2 are doing the calculations. Through some ablation study, they find the attentions heads responsible for this error, and make an intervention to offset this error.  Accordingly, they suggest fine-tuning the model based on this to get better results.

### Strengths
1- The paper has developed a natural story from doing the ablation study to fine-tuning a model in Sections 3 to 5, which makes it more understandable to a general reader. 

2- To my knowledge, this is the first attempt for doing an ablation study for the task of addition in a model as large as llama2. Hopefully, this will contribute to the mechanistic interpretability of LLMs for logical tasks such as addition and parity.

### Weaknesses
1- Before, jumping to the details of experiments in section 3, it would’ve been more convenient for the reader if they had described the input and the output format. For instance, I was curious about the answer of Llama2 and prompted “233335 + 566667” twice for temperature = 1 and got the two answers below — While the final answer is the same, the format is different and needs some extra care. Did you read the final answer manually across all your experiments?  Did you set the temperature to zero? How do you ensure that the output format stays the same?

```
Sure! Here is the result of adding 233335 and 566667:
233335 + 566667 = 799992

Sure! Here is the calculation:
233335 + 566667 = 799992
```


2- In line 177, initially I thought it must be $x_{d+1} + y_{d+1}$ and $x_{d+1}' + y_{d+1}'$. I had to go over the entire section to understand that it is not the case and reason for that choice. The authors must have done a better job at explaining their experimental set up. Another example of this are equations (1) to (3) where attention scores and $m_i$’s are given without any explanation. For example, what are $\sigma$ and $\gamma$?

3- In line 200, $v$ is used for the first time in the paper. I’m still not sure what the definition of this entity is. Because of this I couldn’t understand the ablation study in section 3.3, which is the core idea of the entire work and is later used in sections 4 and 5.

4- Figure 6 is not being referred anywhere in the main body. While it is probably for the results of Section 4, please make sure to refer the reader to the right place for checking up the results. Also, this figure only includes the accuracies up to length of 20, whereas in 417 they talk about a case where sequences of length 60 are involved.

5- If the ablation study demonstrates the main cause for the carry propagation errors in a large model such as mistral, why is there no improvement in figure 6 for up to length 5? This must be discussed by the end of Section 4.2.

6- Can you compare your work to some previous result that has attempted to address the carry propagation issue? For instance, the paper below:

[1] Sabbaghi et al., Explicitly Encoding Structural Symmetry is Key to Length Generalization in Arithmetic Tasks.

7- What is the effect of fine-tuning on tasks unrelated to the addition? Does the explained procedure do any harm to the typical benchmark score of llama2 or mistral?

### Questions
Please address the concerns expressed above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper offers a comprehensive and detailed investigation into how a Transformer performs simple addition. The authors support their findings by conducting inference interference to improve addition performance. Finally, they demonstrate that fine-tuning a model on the addition task does not significantly enhance its ability to perform addition.

### Strengths
- The experiments conducted in this paper are thorough.

- Exploring the limitations of Transformers to handle mathematical tasks is a crucial research focus, as it has significant implications for their use in quantitative applications.

### Weaknesses
 - Additional details needed: What kind of positional embedding is used in the model? Previous research such as [1] has shown that positional embeddings play a crucial role. I am aware that [1] is cited, but the authors only briefly mentioned it sec 4.2.

- Fine-tuning: How many epochs were used by the authors to fine-tune the model? Can the grokking effect start to take effect with sufficient fine-tuning steps?

- Related work: The authors should position this paper more clearly within the related work section. Transformers with addition have been well-studied, and lines 90 to 93 mention at least two very similar studies. How does this work differ from them?

- Lack of an implementable algorithm: This paper does not provide an algorithm/circuit that can be directly implemented by a Transformer. That said, I understand the challenge of identifying a circuit for addition and do not expect the authors to provide one in the rebuttal.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this paper, the authors address the issue that large-scale language models based on Transformers often make mistakes in integer addition.
In integer addition, the result of the operation is often transferred from the lower digits to the higher digits. The authors define this transfer as the carry length and analyze it in detail.
The causal analysis showed that some attention heads strongly influence the output. (Sec 3.2)
Next, from the visualization of the attention pattern, it was found that the model predicts the next token by relying on a stair-shaped attention pattern, and when the carry becomes long, this stair-shaped pattern becomes disordered, and the value information is lost. (Sec 3.3)
From these analyses, the authors argue that many of the model's errors are due to incorrect processing of carries and propose a method for re-weighting the attention weights, and the experimental results show its effectiveness. (Sec 4)
In addition, the authors investigate how much the model can generalize to carry learning in out-of-distribution generalization. (Sec 5)

### Strengths
- This paper was written in an easy-to-understand way, so it was easy to understand. The theme is interesting.
- The proposed method also seems to be simple but effective.
- The experiment was conducted using three types of models (Mistral-7B, Llama-2-7B, Gemma-7B), so it is considered to be a comprehensive result.

### Weaknesses
 - In the abstract of this paper, the authors claim that 'the formation of the attention heads is crucial to the length generalization,' but I cannot find any evidence in the main text to support this claim. Therefore, this claim should at least be removed from the abstract. (If the authors make this claim, they should discuss it with position encoding. Position encoding is the most critical factor in length generalization, and there has been much research on it. However, this paper does not mention RoPE, position interpolation methods, or extrapolation. )
- (L140-141)  h_i^0 = d_i + pos(i), this formula is incorrect because Mistral-7B uses RoPE. It would be better to rewrite it.
- There is no description of the fine-tuning parameter settings or detailed description of the data set. It may appear to be non-reproducible.

**I have repeatedly asked authors to correctly describe the model in their papers. However, they insist that they want the paper to be concise and that the description in the relevant section is not incorrect. Can't the authors even make this simple correction? Usually such mistakes are corrected perfectly once pointed out.
In the course of our discussion, I realized that they did not distinguish between the GPT model and the llama model. (I should have realized this possibility at the first stage of the description, e.g., d_i+pos.)
If they are writing an analytical paper on a model, the structure of the model should be described correctly. The authors were quick to respond, but only with excuses, never providing correct statements or rationales. I can teach them the correct description, but is that really the role of the reviewer? The quality of a paper is quite low when it is not correctly described in the first place.
This is a Transformer paper; the description of the Transformer model should be written correctly.**

**Papers that neglect description in favor of simplicity should not be accepted to top conferences.**

**As a supplementary note, I pointed out the issue of the position encoding in llama, but the author replied that they had referred to the GPT model paper[1]. If you know about the llama model and the GPT model, you should be able to tell that the position encoding is different. Therefore, it is wrong to refer to the GPT model paper to describe the position encoding of the llama model.**

**To add to this, the notation $pos_i$ is incorrect. This is proof that the author has not read the original papers on RoPE[2] and Transformer[3].In the original paper on Transformers, it is defined as $pos$, and in the original paper on RoPE, it is defined as $m$.  $pos$ expresses absolute position. In RoPE and Transformer papers, $i$ is not appended in $pos$. This is because absolute position is independent of $i$. Is it the reviewer's job to teach the author basic knowledge like this? I think that the author lacks basic knowledge. Because the paper written by such an author lacks discussion (both the author and the other reviewers admit that the discussion of position encoding is lacking), this paper is not worthy of acceptance.**

### Questions
1\. (Sec 3.3) There is a large variation in the baseline scores for CC4, CC6, and CC10. What is the cause of this?
In particular, the score for Llama2-7B is very low compared to Mistral-7B and Gemma-7B for CC10.

2\. (Sec 3.3) How long is the sequence length of CC10?
Looking at Figure 8, I think the sequence length of CC10 may exceed 4k.
If it does, the effect of max_position_embeddings is significant, so a discussion or explanation should be included.
The max_position_embeddings is 32k for Mistral-7B (window size is 4k), 4k for Llama2-7B, and 8k for Gemma-7B. Is this difference affecting the results in Table 1?

3\. (Sec 4.2) The experimental results are listed in Table 1, but it is difficult to understand because there is no citation in the main text. Please include a citation in Section 4.2.

### Soundness
2

### Presentation
2

### Contribution
2
