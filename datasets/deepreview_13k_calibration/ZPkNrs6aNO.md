# Effectively Steer LLM To Follow Preference via Building Confident Directions

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Having an LLM that aligns with human preference is essential for accommodating individual needs, such as maintaining writing style or generating specific topics of interest.The majority of current alignment methods rely on fine-tuning or prompting, which can be either costly or difficult to control. Model steering algorithms, which construct certain steering directions used to modify the model output}, are typically easy to implement and optimization-free. {However, their capabilities are typically limited to steering the model into one of the two directions (i.e., bidreictional steering), and that there has been no theoretical understanding to guarantee their performance. In this work, we propose a theoretical framework to understand and quantify the model steering methods. Inspired by the framework, we propose a confident direction steering method (CONFST) that steers LLMs via modifying their activations in inference time. More specifically, CONFST builds a {\it confident direction} that is closely aligned with users' preferences, and then this direction is added to the activations of the LLMs to effectively steer the model output. Our approach offers three key advantages over popular bidirectional model steering methods: 1) {It is more powerful, since multiple (i.e. more than two) users' preferences can be aligned simultaneously; 2) It is very simple to implement, since there is no need to determine which layer the steering vector should be added to; 3) No explicit user instruction is required. We validate our method on GPT-2 XL (1.5B), Mistral (7B) and Gemma-it (9B) models for tasks that require shifting the output of LLMs across a number of different topics and styles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel model steering approach, CONFST, to enhance LLMs by aligning outputs more closely with user preferences. The authors provide a theoretical framework for understanding and quantifying model steering, a method that adjusts LLM outputs to meet diverse user needs without explicit instructions or exhaustive fine-tuning. CONFST operates by creating a “confident direction” based on user history, which is integrated into LLM activations to guide outputs toward desired styles or topics. Unlike existing bidirectional steering methods, CONFST supports multiple preferences, making it a scalable solution for complex user alignment tasks. Validation experiments on models like GPT-2 XL and Mistral demonstrate CONFST's effectiveness, particularly in topic and style shifts.

### Strengths
S1. The paper provides a clear theoretical basis for understanding the mechanics of model steering, which is often underexplored in existing literature.
S2. CONFST’s ability to handle multiple alignment directions and user preferences offers a versatile approach, going beyond simple bidirectional steering.
S3. By reducing the need for fine-tuning, CONFST presents a resource-efficient alternative for LLM personalization, which is particularly valuable for large-scale models.

### Weaknesses
W1. The examples in Figure 1 are not intuitive. Why does a user hide her need when using LLMs? How can the proposed method successfully guess what a user thinks?
W2. Despite the theoretical foundation, how specific steering directions map to nuanced user preferences could benefit from further empirical examples or interpretability measures.
W3. The success of CONFST appears sensitive to confidence threshold settings, which may require careful tuning, especially in applications with noisy data.

### Questions
Please refer to Weaknesses.

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
3

### Summary
This paper proposes a theory to explain how steering vectors work, and describes an algorithm for constructing steering vectors inspired by this theory. The paper then empirically tests the proposed steering method across different topics and datasets.

### Strengths
Originality: To my knowledge, this method is original, however I have a limited background in this area.
Clarity: Apart from some minor typos, the paper made sense overall.

### Weaknesses
Significance: My main issue with this paper is one of framing -- while the paper claims to be about steering LLMs to follow a user's preferences, it is primarily about topic modeling and steering an LLM to generate text which is on a particular topic.
Quality:
2a) The theory seems to obscure some questions around how to infer the user preferences $\theta$ given the user history $(A_{1:n}$. Namely, the steering vector clearly influences the probability of a particular output $A_i$ via $P_M(A_i | \theta; X )$, but the proposed theory simply assumes that $\theta$ can be directly estimated from $f(\Tau(A_{1:n}))$, and looks at the Bayesian posterior over $\theta^*$  given $f(\Tau(A_{1:n}))$ without proposing a concrete likelihood function $Pr(f(\Tau(A_{1:n})) | \theta))$. Instead, they implicitly assume that logistic regression trained to separate between $f(\Tau(A_{1:n})) | \theta)$ for different topics will work.
2b) The paper does not compare its results to a baseline method such as the original Activation Addition method by Turner et al, making it unclear that the proposed method beats the prior art.

### Questions
1) Does the proposed method outperform any baselines?
2) Is there empirical evidence to suggest that the optimal steering vector $\theta$ can be inferred solely from the activations $f(\Tau(A_{1:n}))$?
3) What is the likelihood function for $Pr(f(\Tau(A_{1:n})) | \theta))$?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an effective theoretical framework, as well as a general and efficient preference alignment method that guides large language models (LLMs) to generate outputs that match user preferences. The paper gives the corresponding theoretical analysis on generating derivation. The proposed method CONFST achieves personalized alignment by modifying model activations without requiring fine-tuning, and the authors validated the robustness of CONFST on several large foundation models.

This excellent work has brought new insights to the community in terms of theoretical contributions and preference alignment schemes. However, there is a lack of consideration in terms of experimental design and the design of multi-user preference conflicts.

### Strengths
The paper provides an innovative theoretical framework that deepens the understanding of preference alignment principles.

CONFST is general and efficient, allowing alignment of multiple user preferences without fine-tuning, thus reducing resource costs.

The robustness and broad applicability of the algorithm are demonstrated on several benchmark models, including GPT-2 XL, Mistral, and Gemma.

### Weaknesses
The experimental setup is relatively simple; for instance, the topic shift task is primarily a sentiment classification task, a classical one that even traditional ML methods would be easy to produce a good performance, which somewhat limits the persuasiveness of this work. More kinds of evaluations may help.

The baseline comparisons are limited. A dedicated section explaining the absence of other baselines, or additional baseline comparisons, would strengthen the paper.

The paper lacks case studies, which would demonstrate the method’s performance in specific contexts. Personalized alignment could benefit from concrete case studies to showcase detailed performance.

The paper does not consider potential conflicts in multi-user preference alignment. Since CONFST supports multiple preference alignments, how would conflicting preferences among users affect model output? It seems that this paper does not address this type of conflict in its design.

### Questions
How do the authors demonstrate that the method can align with a broader range of unexplored preferences?

If conflicting user preferences are input, how would this affect the model's output?

If the authors can effectively address my concerns or clarify my potential misunderstandings through experiments or discussion (supporting material should be included), I would be happy to raise my score (Please see "Weaknesses" and "Questions" for detailed feedback).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on a crucial problem: how to efficiently achieve alignment between LLMs and human preferences and specifically targeted at activation modification in inference time. It also conducts a theoretical analysis of activation steering methods and proposes an approach to handle multiple preferences. Experimental results demonstrate that this method performs better than massive mean steering algorithms across several datasets and specific settings.

### Strengths
This paper addresses a key challenge: how to effectively align large language models (LLMs) with human preferences, with a particular focus on activation modification during inference.

The experiments are extensive in model architecture.

### Weaknesses
The main issue with this paper lies in its limited contribution and the vague description of its settings. For example, in line 97 where the contributions are outlined, first, the proposed theoretical framework seems to have very little connection to the presented method. The connection between the theoretical framework, which focuses on maximizing the posterior probability of a preference given a steering vector, and the actual algorithm, which uses a classifier to select activations, is not clearly established. It's unclear how the theoretical goal of maximizing  $P(\theta^*|v)$ is directly translated into the practical steps of the algorithm. Second, regarding the claim that it enables the alignment of multiple preferences, we could simply modify the output dimension of the linear probe in [1] from 2 to the number of preferences to achieve this expansion just like the authors did. As for "implicit model steering," [1] also operates in a similar way. The paper does not adequately distinguish its approach from a straightforward extension of existing linear probing techniques. Lastly, the "enabling adjustable levels of relevance" is actually controlled by a threshold, and in [1], this can similarly be achieved by controlling the number of selections in top-k merging, which is analogous to the method presented in this paper. The paper fails to highlight any significant advantage over existing methods in terms of adjustable relevance. 

Regarding the setting and description, the descriptions of “user”, “user preference” $\theta$ , “user history” $\mathcal{H}$, history dataset $A$ are confusing and maybe redundant. Why we need to introduce the term “user history” to this context? The authors refer to news from different categories and responses generated by models with different labeled categories as the history data of different users, which is inappropriate and ambiguous. Why not just simply use “data of different preferences” to represent it? And also please provide a problem setup to make your setting more clearer. The use of “user history” adds unnecessary complexity and does not accurately reflect the experimental setup, which is based on labeled datasets rather than actual user interactions. The lack of a clear problem setup makes it difficult to understand the motivation and applicability of the proposed method.

The author does not validate the challenges they proposed, such as why existing methods would perform poorly when there is high noise in the samples, nor do they provide any experimental evidence to support this claim. If this challenge does indeed exist, the author does not explain why the method proposed in this paper is able to address it. In fact, the author mentions in the experimental section that the selection of the threshold also determines the level of introduced noise, which seems to contradict the claims made earlier. The paper lacks a rigorous analysis of how noise affects existing methods and how the proposed method mitigates this issue. The claim that the threshold controls the noise level further weakens the argument for the method's robustness to noise. Assumption 2 mentioned that ”$\hat{\theta}$ with the highest occurrence probability…”, but then P($\hat{\theta}$|…)<P($\theta$|…)for any $\theta$!=$ \hat{\theta}$, which seems contradict the claims too. This contradiction undermines the theoretical foundation of the method. 

The paper lacks detailed descriptions of the parameter settings for its method, raising concerns about transparency. On one hand, the proposed method involves a large number of hyperparameters that can be set, but the authors do not provide details about these settings. For instance, critical factors like layer l , the position of activation for the beginning token t, and the length s are not explained. The proposed method has too many hyperparameters, and the significance of these hyperparameters is questionable. Moreover, the authors do not offer a reasonable explanation or experimental validation for their settings. The absence of detailed parameter settings makes it difficult to reproduce the results and assess the method's sensitivity to different configurations.

Minor: 
In line 466, the reference to figure 4 is incorrect. The authors should check the notations.

### Questions
In previous work [1], token-level activations were not concatenated, but this paper proposes concatenating activations. What is the motivation behind this? In fact, using the activation of the last token already represents the information of the entire prompt+response pair. Why is it necessary to concatenate a segment of token activations? Would it be possible to have ablation studies to verify the effect of this part?


Figure 3 is confusing, with some elements missing explanations. And, under "TVs," the value 0.45 > 0.4 is shown, but it seems the activation was not selected for averaging—why is this?


[1] Li, Kenneth, et al. "Inference-time intervention: Eliciting truthful answers from a language model." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
2

### Presentation
3

### Contribution
2
