# TextGenSHAP: Scalable Post-hoc Explanations in Text Generation with Long Documents

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Large language models (LLMs) have attracted huge interest in practical applications given their increasingly accurate responses and coherent reasoning abilities. 
Given their nature as black-boxes using complex reasoning processes on their inputs,
it is inevitable that the demand for scalable and faithful explanations for LLMs' generated content will continue to grow.
There have been major developments in the explainability of neural network models over the past decade. 
Among them, post-hoc explainability methods, especially Shapley values, have proven effective for interpreting deep learning models.
However, there are major challenges in scaling up Shapley values for LLMs, particularly when dealing with long input contexts containing thousands of tokens and autoregressively generated output sequences.
Furthermore, it is often unclear how to effectively utilize generated explanations to improve the performance of LLMs.
In this paper, we introduce \ours, an efficient post-hoc explanation method incorporating LM-specific techniques.
We demonstrate that this leads to significant increases in speed compared to conventional Shapley value computations, reducing processing times from hours to minutes for token-level explanations, and to just seconds for document-level explanations.
In addition, we demonstrate how real-time Shapley values can be utilized in two important scenarios, providing better understanding of long-document question answering by localizing important words and sentences; and improving existing document retrieval systems through enhancing the accuracy of selected passages and ultimately the final responses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a very efficient method for calculating Shaply values for text generation with long documents. To speed up the computation, it proposes a set of techniques, including speculative decoding, flash attention and in-place encoding. Experiments show that the proposed method is applicable for long inputs, large models, and generative outputs, in the meantime, it decreases the computation time from hours to minutes.

### Strengths
The paper provides us with an efficient method to calculate Shapley values for LLMs, solving the notorious problem of slowness in generating explanations. The improvement in the efficiency is impressive.

### Weaknesses
1. Some essential details are omitted in the paper. For example, how to do speculative decoding is not clear to me.
2. I'm not an expert in this field. I'm wondering whether the proposed decoding techniques lead to different generations.
3. What's the limitation of the proposed method?

### Questions
Please see the weakness above.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces TextGen-SHAP, an innovative method that adapts the Shapley value for text generation tasks, ensuring faster computational speed especially tailored for large language models (LLMs). They prioritize the complex situation of providing explanations when employing lengthy input prompts, especially in tasks like abstractive question answering from extensive texts. Their approach is highlighted in three main areas: a) managing extended contexts with thousands of tokens, b) supporting vast models with billions of parameters, and c) promoting open-ended text generation, in contrast to tasks like classification. Additionally, the authors showcase how the explanations from TextGenSHAP can improve the efficiency of question answering from long documents.

### Strengths
- This paper focuses on a significantly important question on how to explain LLMs' behaviors on text generation tasks.
- The authors propose a straightforward and intuitive method for approximating and estimating the Shapley value on text generation task.
- The paper is overall well-written and easy to read. The idea and method proposed in this paper are clearly illustrated and introduced, making the reader easy to understand.

### Weaknesses
 - On the token-wise explanations, Shapley-derived insights offer only superficial clarity on text generation tasks. The significant scores of tokens give minimal information to the audience. For instance, the tokens are sometimes not even readable words. Moreover, identical tokens in the starting prompt and following question context could have varying importance ratings, which can potentially confuse the audience.
- The Shapley attributions on input tokens reveal unreliable explanations on text generation tasks, as the outputs of LLMs are usually uncertain. The output quality of LLMs usually highly depends on the instructions given to LLMs, which means the prediction changes may related to the changes in instructions rather than the input questions and other stuff.
- TextGenSHAP claims to estimate Shapley Values. However, the proposed evaluation metrics are insufficient to support the claims. It is highly recommended to provide either theoretical analysis on the axiom of Shapley Value on the generated values from TextGenSHAP or empirical evidence with commonly used evaluation metrics (e.g., absolute error metrics or l2 error) that can directly reveal the values are similar to Shapley Values. Furthermore, case studies are insufficient to demonstrate the faithfulness of the generated explanation scores. Empirical studies focusing on both word-level and sentence-level explanations are needed to validate the quality of the explanations.
- Some annotations are not stated clearly in the methodology section. For instance, $v(\cdot)$ is only illustrated as a value function, but this is still vague under the settings of LLMs. According to the paper, the value function maps features to text outputs, which means the output of the value function is only the tokens but not the probability of each token. If this is the case, could the authors explain how the estimation of Shapley values in Eq. (2) has been processed?
- The input capacity of T5 is limited to 512 tokens, which is considerably less than modern state-of-the-art LLMs like Vicuna that can handle around 2k tokens. When compared to other advanced LLMs, evaluations with an input size of 512 may be overclaimed as being effective for managing long inputs. The paper does not provide sufficient evidence that Flan-T5 can effectively handle inputs exceeding its training context length of 512 tokens. Using LLMs beyond their intended context window can lead to unreliable output values, thus impacting the faithfulness of the generated Shapley-based importance scores. If the input context is truncated before processing through Flan-T5, the resulting explanations could be less reliable, potentially removing essential features or words for accurate explanations.

### Questions
- The outputs produced by LLMs can be considerably influenced by various sampling strategies (e.g., temperature, search methods, etc.), which means the output probability can be very different even the LLMs receive the same input text. Are there specific approaches within your framework designed to address these challenges? Please correct any misinterpretation on my part. From my perspective, the mechanism proposed in this paper does not equip to tackle or circumvent these inherent difficulties when explaining the generative results of LLMs.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the post-hoc explanation of text generation with long documents. The key idea is to speed up the Shapley value explanation method with techniques such as speculative decoding. The experimental results show that the proposed method considerably speeds up the explanation and can be used as a document retrieval method.

### Strengths
1. The problem of post-hoc explanation for text generation with long documents is interesting and timely.

2. The paper used several speedup techniques to make the explanation faster and more affordable.

3. The experiments show a practical use of the proposed method for document retrieval.

### Weaknesses
1. Notations are not fully explained and are hard to parse. For example, in Notation paragraph, why is the input space of a language model defined as $\mathbb{R}^d \times \mathcal{P}([d])$. What do these notations correspond to in plain English? In the same paragraph, $[.]_+$ is introduced but not used. It would be helpful if the authors could update the notation and check the consistency throughout the paper.

2. The motivation for technical details is not fully explained. For example, in the current version, I do not understand why Eq (2) is better than Eq (1) in explaining text generation. Specifically, what are the practical implications of using a different function $v_p$ in Eq (2) compared to $v_l$ in Eq (1)? How does this choice address the limitations of directly applying Shapley values to text generation?

3. Figure 4 shows that the proposed method is not always better than an extremely simple baseline (i.e., similarity score), especially on MIRACL. This raises questions about the practical advantages of the proposed method in real-world scenarios, particularly when compared to much simpler alternatives.

4. Lack of baselines. Although previous works on text generation explanation would take a long time to run, it would still be interesting to see their performances and time consumption. Currently, the paper does not include any baseline for explanation. It would be beneficial to see a comparison, even if it's limited to a small subset of the data, to understand the trade-offs between the proposed method and existing approaches.

### Questions
See Weaknesses.

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
The paper introduces "TextGenSHAP", a method designed to adapt the Shapley value for text generation tasks in Large Language Models (LLMs). TextGenSHAP addresses the scalability issues associated with traditional SHAP for LLMs with large inputs/parameters. The main contribution is its ability to provide real-time explanations for LLM outputs, especially in tasks like long-document question answering and document retrieval.

### Strengths
- The paper addresses a timely issue and is well grounded in existing literature.
- It covers a significant breadth: multiple steps such as speculative decoding and flash attention are considered to facilitate speed-ups.
- The approach naturally allows flexible control over the runtime of the algorithm through its hyperparameters.
- The use of (linked) interactive visualizations is commendable.
- The adaptation of block sparsity and flash attention shows forward-thinking.

### Weaknesses
 - The main issue with this paper is its lack of readability:
  - The description of the actual method is fairly sloppy, and there is no algorithm provided in the main text despite a reference to one (important parts of the paper are either not included or delegated to the appendix). There are few points throughout the paper that very clearly describe the process and contributions. As a result, the paper was quite difficult to read, despite the contributions made.
  - No diagram or algorithm besides Figure 2, which is poorly captioned and ambiguous in places. The paper includes many details, but compelling and concise high level summaries are lacking.
  - For instance, *"In the traditional Shapley, log-probabilities are needed for every candidate output"* should come at the start of section 3.1 and not the end (the start of the paragraph is less motivated and more confusing as a result).
- The introduction of several techniques might complicate the implementation and debugging of the method. Some clarity on the ease of implementation or integration of these techniques would be valuable (the aforementioned speculative decoding, etc).
- The improvements are less pronounced on the MIRACL dataset and performance appears varied.

### Questions
1. The section discussing speculative decoding references grafting new answers onto a "causal decoding tree" and updating its attention matrix. Could you elaborate more on the nature, structure, and significance of the "causal decoding tree" mentioned?
2. It would be interesting to know how TextGenSHAP performs with sampling techniques other than argmax.
3. How closely do perturbed inputs need to resemble already decoded samples for speculative decoding to be efficient? Is there a threshold, and how was it determined?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
