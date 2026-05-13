# EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING

- Decision: Accept
- Scores: 8, 6, 6, 3

## Abstract
Neural language models are predominantly trained using maximum likelihood estimation~(MLE), which is equivalent to minimizing the forward cross-entropy between the empirical data distribution and the model distribution. However, various degeneration phenomena are still widely observed when decoding from the distributions learned by such models. We establish that the forward cross-entropy is suboptimal as a distance metric for aligning human and model distribution due to its (1) recall-prioritization (2) negative diversity ignorance and (3) train-test mismatch. In this paper, we propose \textbf{E}arth \textbf{M}over Distance \textbf{O}ptimization~(EMO) for auto-regressive language modeling. EMO capitalizes on the inherent properties of earth mover distance to address the aforementioned challenges. Due to the high complexity of direct computation, we further introduce a feasible upper bound for EMO to ease end-to-end training. Upon extensive evaluation, EMO demonstrates a consistently better language modeling performance than MLE across domains.
    Moreover, EMO shows noteworthy enhancements in downstream performance with minimal fine-tuning on merely 25,000 sentences, highlighting its potential as a lightweight calibration method for enhancing large-scale pre-trained language models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to train "decoder-only" language model with a different loss function EMO  derived from the EMD (Earth Moving Distance).  The motivation is threefold: Tradeoff between Recall and Precision, Negative Diversity, Train-Test Consistency. These three points are clearly defined and compared for the standard loss (maximum loglikelihood, MLE) and EMO. The authors propose to define the inner cost of this distance with a semantic similarity (cosine between word vectors obtained from a pretrained LM). They also use a more tractable upperbound on the EMD.  The experimental setup proposes different kind of evaluation to assess the impact of this new training strategy.

### Strengths
The paper is overall well written and describes an interesting idea. The experimental setup is well described and the results look reproducible.

### Weaknesses
A "related work" section is missing, and it could be nice to better discuss the introduction of EMD (and optimal transport in general) in NLP and this kind of task. 

The experimental setup focuses on the improvement of MAUVE. This is a quite recent metric that makes a tradeoff between precision and recall. While it is interesting to use that metric, it could be nice also to provide also perplexity. I know MLE optimizes the perplexity so it is not fair for EMO, but it can provides a meaningful comparison point (I mean in table 1).


### Questions
The decoding process is unique and since your purpose is to improve diversity, it could be nice to have a discussion on decoding, ie generation.

### Soundness
4 excellent

### Presentation
4 excellent

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
The authors propose to train the language model using an upper bound of Earth Mover Distance. The cost function of EMO is established by the similarity of embeddings from pretrained language model. The authors provide theoretical analysis and argue that EMO is better at handling synonyms compared with MLE. Experiments on various tasks demonstrate EMO's superiority.

### Strengths
1. The authors propose to apply the Earth Mover Distance to train the language model and establish an upper bound for practical backward propagation training.
2. The experiments demonstrate promising performance of EMO on various tasks.

### Weaknesses
1. The authors argue that MLE exhibits a recall-prioritization behavior, which serves as the primary motivation for introducing their proposed approach, EMO. The claim appears to be confusing, as MLE is equivalent to minimizing the forward KL-divergence, i.e., $KL(p||q_{\theta})$.
If the model $q_{\theta}$ has sufficient capacity, the optimal $q_{\theta}$ converges to $p$. Otherwise, $q_{\theta}$ tends to exhibit a mean-seeking behavior. Therefore I have doubts about whether "recall-prioritization" is proper.

2. As pointed out in Section 3.3, EMO exhibits a property of harmonizing recall and precision. A straightforward inference is that EMO is better at handling synonyms compared to MLE, potentially granting EMO-trained models the capability to generate more diverse texts than models trained with MLE. The authors did not conduct such experiments.

3. I guess the distribution of model trained by EMO is very different from that by MLE. However, there's no experiments and analyses regarding that.

### Questions
What are the results of EMO-trained models and MLE-trained models when employing beam search instead of sampling?
I am curious as sampling reflects the entire distribution, whereas beam search captures the distribution's mode.

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
This paper introduces a novel loss function, EMO. The main idea behind emo is to soften the loss function (vanilla cross entropy) based on the cosine similarity of pretrained lm head embeddings. EMO demonstrates consistently better than MLE across models, tasks, scales, and metrics.

### Strengths
1. This paper is well-organized and well-written, so it is generally easy to follow.
2. The intuition of the idea makes sense, and it is good that the complex earth mover distance loss can be reformulated into the cosine similarity dot probability. 
3. The author(s) conducted extensive and detailed experiments, encompassing different model sizes, data scales, and evaluation metrics (which is very important). The thorough and detailed experiments show the advantages of EMO, adding to the soundness of the paper.

### Weaknesses
I have two concerns here.

1) Originality of the method.
In my view, the final loss function is very similar to the d2gpo loss, the authors did cite the d2gpo paper, but they ignored the methodology comparison and they should add d2gpo as a baseline.

2) Why Cosine Similarity?
Using cosine similarity is a choice, but may not be the best choice. The cosine similarity relies on the pre-trained llm head embedding, which makes it not unbiased. And through the 3.3 section, the gradient of the proposed EMO is very similar to the REINFORCE with cosine similarity as the reward, so maybe RLHF/RLAIF will be a better reward model?

### Questions
pls see weakness and the following questions:

3) why EMO can make ppl better? ppl is directly related to MLE, in other words, there does not exist a training-test mismatch problem. Is that because the evaluation is conducted over the sampled sentences instead of the test set. If so, please also report the ppl in another table.

4) please also compare with label smoothing, which is also a very useful loss function in the era of pre-llm.

5) what does the accuracy mean in sec 4.2.3?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a training objective called Earth Mover Distance Optimization (EMO) for autoregressive language models. In contrast to maximum likelihood estimation, which solely enhances the likelihood of the ground-truth token, EMO takes into account the embedding similarity between predicted tokens and the ground-truth token, promoting predictions of tokens with high embedding similarity. Experimental results demonstrate that EMO generates superior outputs compared to MLE when employing unbiased sampling.

### Strengths
This paper is easy to follow. The presentation is mostly clear.

### Weaknesses
1. **There are significant concerns regarding the evaluation methodology in this paper. Comparing MLE and EMO based on outputs generated by unbiased sampling is unfair, as the two objectives result in considerably different model distributions.** The expected MLE loss, $-\sum P \log Q$, is minimized when the model distribution Q matches the data distribution P. As mentioned in the paper, the expected EMO loss, $E_{v_i \sim Q}[\sum_{j=1}^{|V|}P(v_j)C(v_i, v_j)]$, is minimized when the model distribution Q is a one-hot distribution that only outputs the token i that maximizes $\sum_{j=1}^{|V|}P(v_j)C(v_i, v_j)$. Consequently, models trained using EMO will predict a much sharper distribution, leading to higher-quality but lower-diversity outputs when sampling from EMO. The evaluation methodology in this paper, i.e., comparing the sampling results of EMO and MLE, is therefore like comparing the output quality of greedy decoding and unbiased sampling, which is inherently unfair. The fair way is to compare their decoding results of greedy/beam search, necessitating further experiments to establish the effectiveness of EMO.

2. Based on the above analysis, the authors' motivation appears to be flawed. Under ideal circumstances, MLE trains the model to conform to the data distribution. In contrast, EMO results in a one-hot distribution, which is recall-prioritization and negative diversity ignorance. 

3. The proposed EMO loss is very similar to the word embedding-based loss [1]. The only difference lies the choices of distance mertics (Cosine distance in EMO, Euclidean distance in [1]).

### Questions
None

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
