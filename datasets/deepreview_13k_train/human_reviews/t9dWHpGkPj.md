# Language Model Inversion

- Decision: Accept
- Scores: 6, 5, 6, 5

## Abstract
Language models produce a distribution over the next token; can we use this to recover the prompt tokens? 
We consider the problem of language model inversion and show that next-token probabilities contain a surprising amount of information about the preceding text. Often we can recover the text in cases where it is hidden from the user, motivating a method for recovering unknown prompts given only the model's current distribution output. We consider a variety of model access scenarios, and show how even without predictions for every token in the vocabulary we can recover the probability vector through search. On Llama-2 7b, our inversion method reconstructs prompts with a BLEU of $59$ and token-level F1 of $78$ and recovers $27\%$ of prompts exactly. Our dataset of prompts will be provided upon paper publication.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on extracting the prompt used in LM generation given access to the probability distribution of the token following the prompt. An “inverter” model is trained on pairs of distribution of distributions and prompts for this purpose. The dataset used for training is a meta dataset comprising a collections of various prompt/instruction datasets. A distribution extraction algorithm is also experimented with in case the LM API only provides access to top-k tokens and their logprobs instead of a full distribution. This approach is compared to several reasonable baselines on the task of inverting prompts of a LLaMA-2 (2B) model and training a much smaller model like T-5. Ablation analysis and other analysis around variation with inverter size, out-of-domain prompts etc. is also reported.

### Strengths
– The paper tackles an interesting problem with a sound approach.

– The paper is well-organized and the presentation is clear.

– The baselines are reasonable and well-designed and the approach in general outperforms these baselines.

– The quantitative analysis is sound and substantive. Ablation studies and analysis on the impact of model size, out of domain prompts, distribution extraction, using partial distribution etc. provide great insight into the results. For example, the finding that whole distribution is important for good performance and losing even the tail of distribution causes a drop in performance is very interesting and provides insights into behavior of LMs in general. I am surprised however that using unnormalized logits over logprobs causes a drop in performance as well because unnormalized logits contain more information than post softmax logprobs.

### Weaknesses
– While the results show a significantly better ability to recover prompts than the baseline, the absolute numbers are fairly low – the exact match scores are discouraging and the BLEU scores are also not very high. So I am not convinced if this is a serious concern for security in terms of prompt leakage. For example, looking at the qualitative examples, the inverter struggles with proper names which are often the important target tokens where security vulnerability is concerned.

– Similar to above, the performance is significantly much worse on out-of-domain prompt datasets. This indicates an inclination of the inverter model to yield a large number of false positives. I am not entirely convinced whether this is a reliable attack on LM services.

– Following the two points above, a more pointed analysis on the recoverability of sensitive information instead of recovering general purpose prompts might help establish the significance of the proposed attack more clearly. For example, can the proposed approach differentiate between or recover mildly different prompts that result in similar responses? Conversely, how good is the model at identifying seemingly benign prompt injection attacks? How good is the attack at exploiting specific sensitive information? Overall, I think the attack would be more serious if the exact match numbers are higher or exact match over sensitive tokens (like named entities) is high. Recovering paraphrased general purpose prompts while certainly interesting in its own right, doesn’t seem like a convincing threat.

– I am not entirely sure about this but the presentation gives me an impression that it only considers “first token” distribution after the prompt. This seems limited – would using token distributions at multiple positions improve the attack?

– The distribution extraction from access to argmax/top-k logits is very expensive, requiring the number of API calls equal to the size of vocabulary at least. This is likely a concern if multiple positions other than the first token are used.

### Questions
Please address points in the review above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work tries to reverse engineer the prompt given to a language model solely using its outputs. In the case of access to the distribution over next tokens (given a particular prefix), they transform the logits of this distribution to a sequence of embeddings, feed these embeddings to a pretrained language model, and use the model’s decoder in order to predict the prompt that lead to that distribution. They provide a number of empirical results that show the effectiveness of their proposed approach and explore methods for defending against prompt inversion. The further perform ablation studies to understand which components of their approach are necessary for its success

### Strengths
* The problem that the authors try to solve is quite interesting and relevant, given the large usage of prompt-based methods and the recent prevalence of “language models as a service.” This is the first work that I know of that tries to recover the prompt from output probabilities
* The work explores methods for defending against prompt inversion, which is likely of large interest to those that provide “language models as a service”
* Empirical results appear to be strong

### Weaknesses
 * The method seems rather ad-hoc and not theoretically motivated. In the case of access to the conditional probability distribution, the method boils down to feeding (a transformed version of) the distribution back to a language model.
* The formal methodology is difficult to understand. For example, it’s unclear how the prompt is actually decoded from the embedded output probability distribution, i.e., what happens after their proposed encoding; I don’t understand what is going on in section 5. What does it mean to “control one logit?”
* Given that the vector v was projected from R^d to R^v (as part of the final linear layer of the generation model), the argument that projecting it back to R^d would lead to a loss of information feels a bit strange. Specifically, the dimensionality reduction from the victim model's output space to the inverter model's input space is not clearly justified, and the potential information loss during this projection needs more rigorous explanation.
* Where is the theoretical discussion/experiments corresponding to inversion when only the text output is available? The methodology discussed in section 5 still assumes access to probabilities from the model, which are often not available in “models as a service” platforms. The paper lacks a clear methodology for handling the more realistic scenario where only the generated text is accessible, and the theoretical underpinnings for this case are missing.
* In section 4, it mentions that there is a “fixed-length input sequence of 42 words.” Is this in reference to the sequence of _embeddings_ that are fed to the model? Or is this alluding to how the embeddings are decoded into the expected input? The paper needs to clarify whether this fixed length applies to the input embeddings or the decoded prompt, as this distinction is crucial for understanding the method's implementation.
* How does the ability to reconstruct text change as a function of the pretrained model used to construct the distribution p(x | v)? The paper should explore how the choice of the victim language model affects the inversion performance, including factors like model size, architecture, and training data.

### Questions
* In the beginning of section 4 where it’s stated that you “train on samples from the conditional model”, what is “the conditional model”?
* Given that the vector v was projected from R^d to R^v (as part of the final linear layer of the generation model), the argument that projecting it back to R^d would lead to a loss of information feels a bit strange
* Where is the theoretical discussion/experiments corresponding to inversion when only the text output is available? The methodology discussed in section 5 still assumes access to probabilities from the model, which are often not available in “models as a service” platforms
* In section 4, it mentions that there is a “fixed-length input sequence of 42 words.” Is this in reference to the sequence of _embeddings_ that are fed to the model? Or is this alluding to how the embeddings are decoded into the expected input? 
* How does the ability to reconstruct text change as a function of the pretrained model used to construct the distribution p(x | v)?

### Soundness
2 fair

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
This paper explores the concept of inversion from language model outputs. The main goal is to retrieve the hidden prompts from language model systems, even without direct access to model output distributions. The authors have presented various techniques and experiments to substantiate their findings and have approached the problem from both attack and defense perspectives.

### Strengths
Originality: The paper delves into a novel area, focusing on inverting language model outputs, which is not extensively studied before. This introduces a new perspective in understanding language models and their vulnerabilities.

Quality: The experiments are comprehensive and cover a range of scenarios, making the results more robust.

Significance: The findings could have implications for the safety and reliability of using large language models in real-world applications.

Clarity: The paper is generally well-structured with clear sections detailing the problem, methodology, experiments, and conclusions.

### Weaknesses
The descriptions of the algorithm and the results, e.g. Algorithm 1 and Figure 2, are not very clear. It's hard to fully grasp the methodology and the results without a more detailed explanation.

While the paper introduces a novel concept, the execution in terms of explaining the methodology and results could be enhanced. The paper would benefit from more detailed and clearer descriptions.

### Questions
Can the authors provide a more detailed explanation of Algorithm 1 and its workings? How were the models chosen for the experiments, and can the authors provide a more in-depth description of these models?

How do the results in Figure 2 correlate with the methodology described? It would be helpful to have a clearer description or perhaps an example to illustrate the findings.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper trains an encoder-decoder model to map an embedding back to the originating text. The problem and the method are very similar to [1]. The main differences seem to be

(1) The paper is motivated in the context of LLMs (extract underlying prompts), whereas [1] is in the context of retrievers (extract paragraphs in the knowledge base).

(2) In [1], the embedding is a low-dimensional text embedding of a retriever. Here, the embedding is the conditional token logits given the prompt, which are unrolled and transformed to be treated as encoder inputs. 

(3) This assumes access to LLM probabilities, which may not be entirely available. The paper proposes an estimator based on bisection that can be done with API calls, but this also assumes at least top-1 logit is exposed. 

(4) A critical component in [1] is the iterative refinement, which is not considered in this paper. 

[1] Text Embeddings Reveal (Almost) As Much As Text (to appear at EMNLP)

### Strengths
- Model inversion is a relatively new interesting problem.
- The proposed method is shown to be more effective than more naive versions (specifically, not using the token logits/Monte Carlo estimator for probabilities).

### Weaknesses
 - Given the high similarity between [1] and this submission, every nook and cranny of their differences must be disclosed and analyzed to make the submission's contributions clear. I found comparisons lacking with many unanswered questions like: why not use the iterative version, which is shown to be extremely useful in [1]? 
- The bisection-based estimator seems effective, but I find it a bit abrupt and lacking an explanation.
- The method does not seem to consider the setting in which the model probabilities are not available at all (i.e., generation-only APIs), which is maybe the most relevant setting for extracting prompts given that the most powerful LLMs are private.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
