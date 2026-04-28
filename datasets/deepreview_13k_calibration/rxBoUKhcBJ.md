# LM-Switch: Transforming Word Embedding Space for Flexible Language Model Steering

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 3, 5

## Abstract
Large language models (LLMs) have advanced significantly as general-purpose tools. Varied real-life demands, ranging from risk management for specific audiences to customizing text styles for different scenarios, all necessitate customizing general-purpose LLMs to different conditions. However, existing pre-training or fine-tuning solutions are still not efficient or flexible enough, and can compromise LLMs’ original quality. Applying classifiers as constraints requires an expensive decoding process. We motivate ourselves by theoretically interpreting the role of word embeddings in modeling output distribution. By analyzing a variant of Hidden Markov Models (HMMs), we find that different conditions in HMMs can be surprisingly understood as linear transformations in the output word embedding space. This finding inspires LM-Switch, a novel, theoretically grounded, lightweight, transferrable, and flexible method for generative language model conditioning. LM-Switch simply deploys a linear transformation in the output word embedding space. It can achieve comparable or superior performance compared with state-of-the-art baselines in LM detoxification and sentiment control while maintaining a better balance with generation quality, despite training only 0.2% of model parameters. It is also able to learn from a few sentences or one document. One can continuously steer LLMs by scaling the transformation, or compose multiple conditions by adding their transformations. Moreover, a learned LM-Switch can be transferred to other LLMs of different sizes. We will make our code available to the research community following publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an approach for controlled text generation called “LM-switch”. This approach modifies the output embedding matrix (the one that produces logits given context) by adding a linear perturbation which is parametrized by a matrix W, that is learned by finetuning the perturbed language model on text satisfying the desired control variable. This approach is empirically compared against other controlled generation approaches that also involve finetuning on domain data like DAPT, DExperts, LoRA etc. on controlled generation tasks like sentiment-controlled generation and toxicity reduction. This approach is also applied to generation of text controlled by political stance.

### Strengths
– The paper is well-organized and easy to understand.

– The proposed technique is simple to implement and shows promising results.

– The proposed approach achieves the target attribute better than the baselines considered.

– The interpretability and transfer analysis is interesting and hints at the effectiveness of the proposed approach.

### Weaknesses
– The baselines appear to be disadvantaged/weak. For example, the approach reports results on GPT-2 base, medium, and large sizes but the baselines, many of which are GPT2-based seem to not be implemented under different GPT-2 sizes.

– Related to above, details of LoRA are not provided. There are many implementation possibilities and options for LoRA based finetuning but I am not sure from the writeup if this aspect was tuned to get a strong LoRA baseline. Specifically, the rank of the low-rank matrices, the initialization strategy, and the optimizer settings are crucial details that are missing.

– The paper only performs quantitative comparison on two surface-level controlled generation tasks. Although this is mentioned in the appendix, it does not consider other controlled generation tasks, especially the ones which require manipulation of deeper attributes in language, such as style transfer or persona-based generation. The current evaluation is limited to sentiment and toxicity, which are relatively straightforward to control.

– MuCoLa is tested as a baseline for detoxification but not for sentiment-controlled generation.

– Although the paper emphasizes that the proposed approach makes it easy to compose different control attributes, I am unable to find adequate evidence of such compositional control abilities in the results. Relatedly, figure 2b is difficult to understand and I am not sure how exactly it relates to compositional control abilities. The figure lacks clear labels and a detailed explanation of how the axes correspond to different control attributes and their intensities. It is unclear how the color changes and height variations directly demonstrate compositional control.

– The connection of neural autoregressive LMs to HMMs is tenuous but the manuscript overstates this relationship. Practically, finite state HMMs are not as expressive as neural LMs. Moreover, finding a clean transformation of the HMM state space to a neural autoregressive LM’s vectors is non-trivial and typically intractable. Therefore, the motivation of the approach via HMM hidden state representation feels forced and disconnected. Moreover, the assumptions underlying the theorems are too unrealistic. Unless I missed something, more convincing evidence should be provided to justify the validity of the assumptions. The paper does not address the limitations of using HMMs to model the complex dynamics of neural language models.

– Assumption 1, eqn 2: what does the variable “h” mean?

### Questions
Please address the concerns in the review above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel method to control/condition language model generation by adapting the word representations for large language models (LLM). The method is based on the hidden-markov-modelling to guide word representations to a given direction (e.g. sentiment) with a linear transformation.  The main contributions are: i) method for conditioning LLM generation, ii) application of the proposed method to LM detoxification and sentiment control generation, and iii) interpretability and computational cost of the proposed method. The method shows competitive results compared to the baselines on both application tasks.

### Strengths
- A principled method for conditioning LLM generation.
- Clear description of background knowledge and related work needed to understand the proposed method.  
- The authors perform a  comprehensive comparison of the proposed method with baselines on detoxification and sentiment control.

### Weaknesses
 - It is not clearly defined the selection for the model's hyperparameters.
- A possible extra contribution can be the addition of a statistical significant test or uncertainty estimates of the results.

### Questions
Please address the following questions during the rebuttal:

- Could you elaborate on the selection and importance of hyper-parameters (e intensity)? 
- Please speculate if the proposed approach can be extended (or combined) to other tuning methods for LLM, e.g. instruction tuning.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a linear transformation of word embedding $E = E + \epsilon WE$ (called LM-Switch) that can be plugged into any LM to steer generation. LM-Switch is evaluated on 3 tasks: 	language detoxification, sentiment control, and political stance control. The evaluation shows that LM-Switch performs on par or slightly better than published results.

### Strengths
LM-Switch is simple to implement and has a small number of parameters..

### Weaknesses
The major weakness of this paper is its evaluation.

- The evaluation is too simple and unrealistic to assess the effectiveness of the proposed method LM-Switch. First, the three tasks in the evaluation are binary tasks. This allows for picking positive and negative values of e to control. Thus, it’s unclear whether the LM-Switch generalizes to non-binary tasks.

- While LM-Switch achieves a better Max Toxicity score than other models, the fact that the soft-blacklist method is doing well might suggest that the testset for toxicity is simple.	Moreover, it looks like the results from other methods are quoted in the paper instead of direct comparison by implementing those methods on the same GPT-2 base-model. This leads to unfair comparison.

- There is no human evaluation. Note that for language generation tasks, it is important to have human evaluation as we can’t trust automatic metrics. DExperts paper has human evaluation for both language detoxification and sentiment control. The political stance study in this paper is not systematic and based on some cherry pick examples. Having said that, without properly running human evaluation, it’s unclear how good LM-Switch is.

- The GPT-2 large model has only ~800M parameters, which is considered small by today's standard. Thus I do not find the argument about parameter efficiency in the paper is convincing. Why not apply the proposed method for Llama-7b or Llama-65B models?

- How does LM-Switch change the behavior on language generation after being tuned for binary tasks? The paper said LM-Switch maintains balanced generation quality but it is evaluated using only perplexity. For a language generation application, I could imagine a prompt such as “write a review criticizing a movie X but in a positive tone”, how does the model behave in such a case?


Other minor weaknesses:

- The paper claims LM-Switch is theoretically grounded by analyzing HMM. But HMM is completely different from autoregressive LM and analysis on HMM with markov assumption is not true on LM unless it’s proven directly for autoregressive LM.

### Questions
See questions in the weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To adapt existing LLMs to diverse conditions efficiently without extensive retraining or a compromise in performance, this paper presents a lightweight method for language model conditioning named LM-Switch and provides both theoretical and empirical analysis. It applies a $d \times d $ trainable linear transformation $W$ on the output word embedding, by which the embedding $e$ of each word is replaced with $e + \epsilon W e_v$. It explains the feasibility of LM-Switch from the perspective of Hidden Markov Model, and obtains guarantees for continuous control and compositional control through its linearity properties.

### Strengths
1. The proposed LM-Switch is flexible and adaptable, which can be fine-tuned or adjusted to different conditions with minimal data, making it a versatile tool for various applications.
2. The author clearly demonstrated the motivation and performance of LM-Switch in LM conditioning.

### Weaknesses
1. There are inconsistencies in the table, some of the best metrics are highlighted in bold, while others are not (e.g. Table 1 and 2).
2. There is a formatting error in the text description of Figure 2(b).
3. The design of the baseline experiment is not well-developed and does not intuitively demonstrate the effectiveness of LM-Switch. It is necessary to provide metrics from the vanilla backbone model of LM-Switch on relevant tasks as an ablation study to validate the effectiveness of LM-Switch. A comparison of the performance between LM-Switch and directly training embedding parameters also needs to be provided.
4. Missing citations for DExperts in the main text and repeated references “Alisa Liu, Maarten Sap, Ximing Lu, Swabha Swayamdipta, Chandra Bhagavatula, Noah A. Smith, and Yejin Choi. DExperts: Decoding-time controlled text generation with experts and anti-experts”
5. It is a little hard to understand. Section 3.2 presents a bunch of fancy mathematical formulas, followed by an assumption. Then, in theorem 1, it is assumed that the assumption holds. I feel like it's not very solid. In addition, I feel like introducing the concept of Hidden Markov Models (HMM) is a bit unnecessary or overly complicated.

### Questions
1. In training, do you freeze the LLM parameters?
2. In section 3.3, the author said “When negative texts are available, we also fit them with M(-\epslion W)” I do not see why negative text should be fit with M(-\epslion W), since W is a learnable parameter. I hope the author can provide further explanation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
