# Provable unlearning in topic modeling and downstream tasks

- Decision: Accept
- Scores: 6, 8, 6, 3

## Abstract
Machine unlearning algorithms are increasingly important as legal concerns arise around the provenance of training data, but verifying the success of unlearning is often difficult. 
Provable guarantees for unlearning are often limited to supervised learning settings.
In this paper, we provide the first theoretical guarantees for unlearning in the pre-training and fine-tuning paradigm by studying topic models, simple bag-of-words language models that can be adapted to solve downstream tasks like retrieval and classification.
First, we design a provably effective unlearning algorithm for topic models that incurs a computational overhead independent of the size of the original dataset.
Our analysis additionally quantifies 
the deletion capacity of the model -- \emph{i.e.,} the number of examples that can be unlearned without incurring a significant cost in model performance. 
Finally, we formally extend our analyses to account for adaptation to a given downstream task.
In particular, we design an efficient algorithm to perform unlearning after fine-tuning the topic model via a linear head.
Notably, we show that it is easier to unlearn pre-training data from models that have been fine-tuned to a particular task, and one can unlearn this data without modifying the base model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies machine unlearning in topic models and downstream tasks. The authors developed unlearning algorithms that enjoys provable guarantees, for both the topic model and downstream tasks. The proposed unlearning algorithms can be implemented efficiently, with runtime independent of the dataset size.

### Strengths
The authors developed unlearning algorithms with provable guarantees for topic models and its downstream tasks. This can be viewed as the first theoretical guarantees for unlearning in the pretraining and finetuning paradigm. Also, the proposed unlearning algorithms can be implemented efficiently, with runtime independent of the dataset size.

### Weaknesses
1. It seems that the proposed algorithms are heavily related to the learning algorithm developed by Arora et al. 2012. Can authors generalize their results to other learning algorithms?
2. Since this is the first unlearning algorithm in the pretraining and finetuning paradigm that enjoys provable guarantees, can authors highlight their technical contributions in deriving the results? What are the main breakthroughs compared to developing provable unlearning algorithms in the supervised setting?
3. There are several constants in Definition 4 (e.g., 0.9 and 0.01). Is that possible to make these constants more universal, e.g., to $\gamma_1$ and $\gamma_2$? If so, how would $\gamma_1$ and $\gamma_2$ affect the developed guarantees?

### Questions
See the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies machine unlearning for topic models. Topic modeling is proposed as one of the simplest case of the pretrain/finetune paradigm, where the distribution of words for each topic can be "pretrained" using provable algorithms (Arora et al., 2012), and this matrix can then be adapted for downstream classification tasks (fine-tuning). The authors propose algorithms for unlearning documents in both the pretraining and fine-tuning phases and prove that the models output by these algorithms have similar performance to, and are nearly indistinguishable from, models that were never trained on the unlearned documents. The results also show that unlearning is "easier" (more documents can be unlearned with the same degradation in task performance) in the fine-tuning phase. The key technique in the proof (as I understand it) is to show that the estimates of word co-occurrence statistics in terms of "anchor word" co-occurrence vectors don't change much when updated by the unlearning algorithm.

### Strengths
- Serious theoretical effort to give provable unlearning guarantees in a simplified setting. An important step towards understanding unlearning for more complicated pretrain/finetune setups.

- Builds on the provable topic modeling results of Arora et al. (2012) to give much stronger unlearning guarantees than other work on provable unlearning.

- The main results are clearly explained and contextualized, especially the difference between unlearning for pretrained models and unlearning for fine-tuned models.

### Weaknesses
 - The presentation is a bit hard to follow and relies heavily on many results from Arora et al. (2012).
  - $(\epsilon, \delta)$-unlearning is mentioned but not defined in L85--86. It would be helpful for those unfamiliar w/ the formalization of unlearning to at least sketch the details here so the reader can understand the type of guarantee that the paper is trying to give.

  - The need for a utility-preserving unlearning definition is not well-motivated. In Definition 4, it seems intuitive that (1) should imply that the unlearned model is not much worse than the output of $\mathcal{A}(S)$ except in pathological cases.

  - Related to the previous point, why does (2) compare to the irreducible loss (i.e., the best-achievable loss) $h^*$ and not the loss of the model output by $\mathcal{A}(S)$? "Utility-preserving" intuitively sounds like unlearning from a model $m = \mathcal{A}(S)$ gives me a new model $m'$ that is not much worse than $m$. But instead this definition compares to the loss of the optimal model $m^*$. Doesn't this essentially pre-suppose that $\mathcal{A}(S)$ is a very good learner?

  - In Lemma 1, $(\epsilon, \delta)$-differentially-private is not defined. Can the authors relate it back to Definition 3?

  - What is the intuition for $\gamma$ in Theorem 1?

  - The stated results don't indicate how the unlearning capacity depends on the minimum anchor word conditional probability $p,$ but clearly this is a very important quantity. What if my unlearning set contains all the samples with that topic's anchor word? (It's clear in the proof, but maybe it'd be better to make it clear in the Theorem statement)

  - Important quantities, such as $C^{F}$, are never defined in the text and only explained in pseudocode in Algorithm 1.
  - A numerical example / walkthrough of the proposed algorithm on a synthetic example would be very helpful for understanding. It's currently easy to get lost in the notation

- The results would be stronger if the authors connected them more to empirical results in other settings (beyond topic models). For example, they show that unlearning is easier for task-specific models than pretraining. Is this backed up by empirical evidence with more realistic models?

### Questions
- other questions above

- "it is unclear why one would want to use A without w or vice versa." I agree $w$ isn't useful without $A$, but isn't $A$ useful without $w$? It seems plausible that $A$ and $w$ would be released separately so $A$ can be used some other unforseen tasks.

- For related work on "Theoretical analysis of pre-training and fine-tuning", the authors might be interested in work that studies provable guarantees for contrastive pretraining and head tuning in the context of topic models: https://www.jmlr.org/papers/volume22/21-0089/21-0089.pdf

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes and analyzes unlearning algorithms in topic language models. In a language model, unlearning algorithms are algorithms to forget a specified set of documents $S_f$ present in training data (used in pre-training or fine-tuning stages). Ideally, once the unlearning is done, the model should be equivalent to one trained without $S_f$.

In the context of the paper, topic modeling means, learning $A: n \times r$ whose columns are word probability distributions for the topics and $R: r \times r $: a topic-topic co-occurence matrix. Here $n$ is the vocabulary  size and $r$ is the number of topics.

The key components of the unlearning algorithms are (a) a Hessian update to the $n$ word-topic distribution vectors $C_i$ each of size $r$ (b) update A, R  and finally (c) introduce DP-noise with Gaussian mechanism.
The key contributions of the paper are to show DP guarantees on the proposed unlearning algorithms.

### Strengths
* The paper gives solid theoretical results.

### Weaknesses
Unlearning algorithms for language models have practical applications, as the authors argued in the introduction of the paper. However, it is an indeed a limitation — as the authors rightly point out — that the analysis is on topic models, which are not state of the art at this time. Further — I am saying this without citations — Gaussian mechanism is also not practical as it introduces too much noise to make the output useful.

### Questions
Footnote in page 4 says that L = 2; that is, the document length is fixed to 2 words. That seems limiting.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper combines old with new: an old theoretical bag-of-words topic-model that has provable guarantees, with a new problem: unlearning. It designs unlearning algorithms and proves theorems about these, that in certain cases unlearning can be done using less time than it would take to re-run the learning algorithm.

### Strengths
This paper is very well written and addresses a problem that is in the spotlight: unlearning. I haven't checked the math carefully, but it looks like it is likely correct.

### Weaknesses
I'm sorry to say it, but bag-of-words language models have little remaining relevance today. Furthermore, in the few cases where they are relevant, they are quite fast to train. Therefore, proving complex theorems about speeding them up is not of general interest. It also does not seem likely that the takeaways from these bag-of-words models provide insight into the larger relevant models. This paper might be of interest to specialized theoretical conferences such as ALT.

### Questions
To be honest, this may have been an excellent paper 5-10 years ago, but I'm curious what someone can learn from it today.

### Soundness
3

### Presentation
4

### Contribution
1
