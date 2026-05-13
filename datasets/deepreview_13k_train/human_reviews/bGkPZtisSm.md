# On the Generalization of Preference Learning with DPO

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable capabilities but often struggle to align with human preferences, leading to harmful or undesirable outputs. 
Preference learning, which trains models to distinguish between preferred and non-preferred responses based on human feedback, has become a crucial component for ensuring that LLMs align with human values. Despite the widespread adoption in real-world systems, a thorough theoretical understanding of the generalization guarantees for these models remains lacking.
This paper bridges that gap by introducing a new theoretical framework to analyze the generalization guarantees of models trained with direct preference optimization.  While existing generalization theory often focuses on overparameterized models achieving near-optimal loss or models independent of the training process, our framework rigorously assesses how well models generalize after a finite number of gradient steps, reflecting real-world LLM training practices. 
 By analyzing the reward margin associated with each sample and its trajectory throughout training, we can effectively bound the generalization error. 
We derive learning guarantees showing that, under specific conditions, models trained with DPO can correctly discern preferred responses on unseen data with high probability. These insights are empirically validated on contemporary LLMs, underscoring the practical relevance of our theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper attempts to understand the generalization of models trained using DPO. Different from classic generalization theory, which often assumes the underlying model is overparameterized and with near-zero loss (i.e., can perfectly fit the training data), the assumption in the paper is more realistic and tailored to LLMs. The authors considers scenarios where LLMs are fine-tuned over a few gradient steps rather than extensive training. The key idea is to analyze each sample's reward margin and track how it evolves during training. The authors derived the conditions to keep the reward margin positive for all training samples.. Additionally, they also provide generalization  bounds for new samples from the same preference distribution. The theoretical results were also validated empirical.

### Strengths
1. The theoretical results derived in this paper provide a better understanding on the dynamics of DPO training, which are helpful for the community to understand the mechanism of preference training. 

2. The empirical verification shows the theory aligns with the practice to some extent. This confirms the usefulness of the theories, though the empirical verifications are still very limited.

### Weaknesses
1. Typically, in RLHF, the choice of algorithm doesn't matter much; most of the effort goes into working on RLHF infrastructure and data. DPO is a promising technique to reduce infrastructure demands, but it still shows a gap compared to on-policy algorithms like PPO—assuming the infrastructure is well-optimized. This may limit the real-world impact of follow-up works, but I think it's a relatively minor issue here.

2. I highly doubt that ignoring the fact that the LLM is pre-trained would lead to any meaningful theoretical results. This consideration is crucial in explaining why we need much less post-training data to align LLMs. For small or under-trained LLMs, this result may not hold. Therefore, if the derived result is agnostic to this setting, I am not convinced it will be useful or even correct. However, I understand the challenge in mathematically formulate a "pretrained  LLM".

3. For LLMs, I think the traditional generalization bound analysis doesn't seem particularly interesting (i.e., in-distribution). The post-training data is relatively small and cannot cover all the cases of user queries, yet the LLM can still generalize to most cases that have not seen anything similar in the training dataset. To work on something really impactful and solid, I think it's essential to have a careful and thorough thinking about the above mentioned factors.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides the first theoretical analysis of generalization in preference learning, specifically for Direct Preference Optimization (DPO). Through a novel theoretical framework, the authors analyze how well models trained with DPO can generalize to unseen data by examining the reward margin and its trajectory during training. The paper's key contribution is deriving learning guarantees showing that DPO-trained models can correctly discern preferred responses on unseen data with high probability under specific conditions. The analysis reveals that generalization capability depends on factors like the number of preference concepts in the dataset and the similarity between different responses. The theoretical insights are validated through empirical experiments on contemporary large language models.

### Strengths
The paper presents several notable strengths. First, it offers a rigorous theoretical foundation for understanding generalization in preference learning - an area that previously lacked thorough theoretical analysis despite its practical importance. Second, the paper successfully bridges theory and practice by providing concrete bounds and conditions under which DPO can generalize, with these insights validated through careful empirical studies. Third, the analysis of reward margin dynamics provides actionable insights into how different factors (like number of concepts and sample size) affect generalization. Finally, the work demonstrates strong technical depth while maintaining practical relevance, as shown through experiments on both synthetic data and real-world language models.

### Weaknesses
 
**Major Concerns:**

1. The theoretical analysis decomposes the model output into the product of W g(x), whereas we only consider the dynamic of W. It is reduced to a linear analysis. This simplification, while potentially tractable, neglects the complex interplay between the weight matrix W and the feature representations g(x), which are crucial for capturing the non-linear nature of language models. By only analyzing the dynamics of W, the analysis essentially treats the feature representations as fixed, which is a strong assumption that may not hold in practice, especially when fine-tuning the entire model. This linear approximation could limit the applicability of the theoretical results to scenarios where the feature representations also change significantly during training.

2. The assumption of mixture of Gaussians distribution of the distribution of preference is rather interesting. However, it is verified the cosine similarity and orthogonality between persona. It is still unclear why we could have a Gaussian distribution for each cluster. The justification for using a Gaussian mixture model to represent preference distributions is not sufficiently strong. While the authors provide some empirical evidence based on cosine similarity and orthogonality, this does not fully justify the assumption of a Gaussian distribution for each cluster. The underlying preference data may exhibit more complex structures that are not well-captured by Gaussians. It is important to consider that the preference data might have heavier tails or exhibit multimodality, which would not be accurately represented by a Gaussian distribution. The lack of a strong theoretical justification for this assumption weakens the validity of the theoretical results.

Therefore, the two main bounds look fine, but these too points make the theoretical analysis not very strong.

**Clarity Issue:**

The paper has inconsistent descriptions about what component performs the prediction:

1.	Line 70: "The loss can correctly predict all training samples into the preferred vs. non-preferred categories"

2.	Line 280: "the implicit reward model from DPO can correctly predict all training samples into the preferred vs. non-preferred categories"

First, "implicit reward model" is not defined. From lines 159-162 it seems to be the same thing as reward margin, but this should be clarified.

Second, both "loss" and "implicit reward model" are weird subjects here. Actually, we use only the LLMs rather than the implicit reward model to predict. I sense the authors don't use LLM $\pi_\theta$ as the subject and say "The trained LLM can correctly predict all training samples into the preferred vs. non-preferred categories" because this statement would be incorrect.
This makes the analysis confusing - the generalization guarantee applies to the implicit reward model, but what we actually use is the LLM. Actually, there could not exist such a guarantee for $\pi_\theta$, creating a disconnect between theory and practice.


**Minor Concern:**

1. In the claim 

"While existing generalization theory often focuses on overparameterized models achieving near-optimal loss or models independent of the training process, our framework rigorously assesses how well models generalize after a finite number of gradient steps, reflecting real-world LLM training practices" 

and the discussion of related work, the authors seem ignore another line of generalization bound research called algorithmic stability or uniform stability, which also bound the generalization gap by training steps T.

2. Llama 2-7B is relatively old, experiments on 3/3.1/3.2 would be better.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper provides a finite time theorectical guarantee for the generalization capability of the preference learning algorithms, with primary focus on Direct Preference Optimization algorithm.

### Strengths
1. Novelty of Research Question: Generalization capability of preference optimization algorithm is of crucial importance, either in theory or practice. This paper provides analysis towards theorectically understanding the generalization guarantees of alignment algorithms, defined as averge 0-1 loss in distinguishing prefered from non-preferred answers. Limited theorectical works have been done for understanding the success of these algorithms, and this paper could possibly entrigger further research along this line to improve the understanding of at least offline RLHF algorithms.

2. Clarity of Introduction and notations: The introduction part and preliminaries are clean and well written.

### Weaknesses
1. Unclear assumption on LM: On line 187-188, the authors made an important assumption/simplied setting by describing the model outputs as $Wg(x)$. This simplification lacks relevant discussion or introduction, and is hard for readers like me to understand the intuitions of this assumption and following arguments. In addition, since nowadays (almost) all LLM models are autoregressive, this model assumption in the paper can not incoporate the stochasticity, which seems to be way too strong. How to understand that the deterministic models weights lead to random outputs in this setup (otherwise how preference pairs are formulated)?

2. Overall, I think that the section 3.2 is not well written and very hard to follow, especially several key assumptions or results are missing or not clarified. Equation (6) should be a continuous approximation to the SGD of the loss function in (4) from my understanding, but no derivation or illustration is given. For a theorectical oriented paper, this section needs additional heavy polishing for a clearer formulation of the model class to be analyzed. Specifically, the dimensions of $W$ and $g(x)$ are not clearly defined, making it difficult to understand the nature of the linear transformation. The lack of clarity on how this linear transformation interacts with the non-linear feature extraction $g(x)$ further obscures the model's behavior. The connection between the discrete SGD updates in (4) and the continuous approximation in (6) is not rigorously established, leaving a gap in the theoretical development.

3. Theorem 4.2's bound looks to be quite vacuous. I did a simple check of math, looks like the bound is meaningless until Q is extremely large (which is impossible if you need that many samples for preference learning from a simple example of k clusters). The bound seems to thus have very limited practical meanings.

### Questions
Is there any connection of paper to the analysis of generalization error of PbRL in the literature? See other questions in weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studied the generalization error of alignment with preference learning using DPO. They considered a simplified TF model in which only the last layer is trainable and analyzed the dynamics of gradient flow given a fixed set of training samples from some clusters. They derived high-probability bounds on both the training error and generalization error of gradient flow in terms of  0-1 classification loss based on reward margin. The gradient of the reward margin in the multi-token generation scenario is also computed and discussed. In addition, the authors conducted experiments to justify their data  assumptions and theoretical findings.

### Strengths
The paper is clear and well-written. The theoretical results on DPO are novel and the assumptions made are justified via experiments.

### Weaknesses
 * The paper assumes only the last readout layer of the transformer is trainable and the output has the form $y=Wg(x)$, where $g(x)$ is some feature map realized by the previous layers of the transformer. This effectively turns the model into a linear/logistic regression model, although trained on a different loss. Thus the proof techniques follows from standard ODE analysis and I do not find much novelty in the proof.

* The analysis on generalization error is done only for the single-token case. I wonder if similar results can be established for the multi-token case.



### Questions
* Is it possible to generalize the analysis in this work to other fine-tuning settings? For example, what if the updates on the weight matrix have low-rank structure as in LORA?

* Line 266-269: what are the values of $x,y$? Is  $y$  a  $|V|$-dimensional vector or a one-dimensional label?

* Typos: Eq (3) misses an expectation on the log-ratio term. Line 233-235: it seems that the conclusions for two the cases are swapped?

### Soundness
3

### Presentation
3

### Contribution
3
