# Disentangling Latent Shifts of In-Context Learning Through Self-Training

- Decision: Reject
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
In-context learning (ICL) has become essential in natural language processing, particularly with autoregressive large language models capable of learning from demonstrations provided within the prompt. However, ICL faces challenges with stability and long contexts, especially as the number of demonstrations grows, leading to poor generalization and inefficient inference. To address these issues, we introduce \sticl (Self-Training ICL), an approach that disentangles the latent shifts of demonstrations from the latent shift of the query through self-training. \sticl employs a teacher model to generate pseudo-labels and trains a student model using these labels, encoded in an adapter module. The student model exhibits weak-to-strong generalization, progressively refining its predictions over time. Our empirical results show that \sticl improves generalization and stability, consistently outperforming traditional ICL methods and other disentangling strategies across both in-domain and out-of-domain data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Self-Training ICL (STICL), a novel approach that stabilizes in-context learning (ICL) through self-training. Specifically, STICL uses a student model (LoRA adapter) trained to mimic the output of prompted teacher models, achieving a disentanglement of query and few-shot examples that goes beyond the approximations of previous studies. The authors demonstrate the superior performance and out-of-distribution (OOD) generalizability of this adapter, highlighting its effectiveness over prior ICL methodologies.

### Strengths
- Motivation and Clarity: The motivation behind this work is well-explained, with clear distinctions from previous studies. The paper is well-organized and easy to follow, making it accessible to readers.

- Empirical Validation: The paper provides strong empirical evidence supporting the effectiveness of STICL, particularly in OOD settings. This solidifies its contributions and highlights its practical relevance.

### Weaknesses
 - While Table 3 discusses OOD generalizability, it would be beneficial to include a cross-tabulation across datasets to show the performance in-domain. Understanding the performance gap between in-domain and OOD settings is a key factor that could add depth to the findings.

- Comparison with MetaICL: This study’s use of adapters for STICL could be interpreted as an adaptation of MetaICL, making it important to explicitly clarify the differences between the two approaches. Unfortunately, this work does not appear to cite MetaICL, which may cause readers to miss relevant context and comparisons.



### Questions
1. How were the subsets in Table 4 selected? Additional context on this decision would clarify the setup.

2. How are the LoRA parameters configured? Specifically, what level of low-rank approximation is achievable in this setting?

3. Could you clarify the connection between the claim in line 219 and prior studies? A clearer explanation of why this design is impactful would be helpful.

4. In Section 4, the discussion on the Lipschitz constant and weak-to-strong generalization feels somewhat unclear. Could you elaborate on how this contributes to the proposed approach?

### Soundness
3

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
The paper proposes to use unlabeled data to stabilize and improve in-context learning. The paper formalizes a form of decomposition of the information obtained from demonstrations vs query. The particular approach involves utilizing pseudolabels in a teacher-student framework. Empirical results suggest that this form of self-training can effectively leverage labeled data to improve robustness and stability in downstream performance.

### Strengths
The self-training analysis of the paper is interesting and useful - connecting to "classical" ideas of local consistency and coverage expansion. This work brings in the perspective of self-training to LLMs and shows that with just a few demonstrations but large amount of unlabeled data, one can adapt LLMs to have strong and robust performance on various downstream tasks. 

The approach, while adding complexity over vanilla ICL, is fairly intuitive and builds on solid foundations of how pseudolabels can enable weak-to-strong generalization and can be leveraged for better and more robust performance. This is an important question of real-world significance. 

The empirical investigations span a variety of datasets and models.

### Weaknesses
One main weakness (and source of confusion for me) is the terminology of "in-context learning" when the models are being fine-tuned via self-training. The whole point of ICL is to eliminate the need for finetuning models, so it is confusing how the current approach fits into the framework. The current process does some kind of finetuning, so it should be pitched as a finetuning method. The method is much more expensive than n-shot, and in general, the computational aspects need to be considered for fair comparisons. 

Keeping terminology aside, the motivation of the paper - in terms of disentangling latent shifts is also quite confusing and seems unnecessary. It seems like the goal is to just "distill" the ICL process into the adapter. I'd recommend the authors to simplify this presentation a bit, because it is currently distracting from the main message. I don't think this disentanglement introduces a fundamentally new perspective - in-context learning can be approximated by (the more expensive) finetuning on related task data. As far as I understand, that is the main connection.

### Questions
(1) For the pattern-based finetuning baseline - do you finetune on just the {4, 8, 16, 32} demonstrations?

(2) Are the demonstrations used at train and test-time the same or different? How should one think of what the demonstrations are meant 

(3) I'm assuming the "unlabeled samples" come from the standard training set, with labels removed? What's the "oracle" performance of finetuning on ground truth labels?

(4) Is the following a reasonable story that faithfully captures what's going on? The main idea is to do some form of self-training (via finetuning an adapter), and the labels are generated on this unlabeled data via in-context learning?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper collects two issues of ICL: (1) instability: ICL is affected by ordering and selection of demonstrations (2) context length: ICL is limited by context window.
The paper assumes that the demonstration of ICL introduces a latent shift to the language model.
The paper points out a series of works on linear functions have a similar idea that demonstrations shift zero-shot $W_\text{zs}$ to $W_\text{zs}+\Delta W_\text{ICL}$, where $\Delta W_\text{ICL}$ can be regarded as the latent shift coming from demonstrations.
The paper then introduces existing methods on disentangling latent shift and the main idea of the paper, i.e., the proposed method of finetuning an LLM with query aligning its output to an LLM with both demonstrations and query.
Therefore, the latent shift is injected into the LLM via alignment, and when inference, there is no demonstration needed.
Finally, through experiments, the paper shows that the proposed method can improve stability and generalization, and show weak-to-strong generalization.
The paper also mentioned the proposed method is more efficient than vanilla ICL since no demonstration is involved in the input prompt.

### Strengths
(1) The proposed method is straightforward, makes sense, and very interesting -- regarding ICL as an alignment task is very interesting.

(2) The proposed method can handle the ordering issue since in the alignment state, the input of the teacher model can take input with arbitrary order. It's not very clear how to handle the ordering issue in vanilla ICL, but in the proposed method, the ordering issue is handled naturally via training sample construction (STICL-S in Table 2).

(3) The proposed method can reduce the inference cost, since no demonstration is involved when inference.

(4) The proposed method has better scores than baselines for ID generalization (Table 1).

(5) The proposed method has better scores than baselines for OOD generalization (Table 3)

### Weaknesses
 (1) Though the proposed method decreases the inference of cost since no demonstration is involved, it requires training for alignment.

(2) It's unclear how the paper posits Sec. 3.2 since the existence of STICL-R. It's more natural for me to take 16 samples from k$\times$16 examples to construct 16-shot demonstrations for STICL-R, rather than construct k separate 16-shot sets for k adapters in STICL-S. The author could consider clarifying their reasoning behind the design choices for STICL-R and STICL-S

(3) It's unclear how the paper calculates the Lipschitz constant for each method in Figure 2, due to page limitation. The author could consider providing a more detailed explanation of their Lipschitz constant calculation method in the Appendix.

(4) It's unclear how the paper desgins the pseudo-label correction, due to page limitation. The author could consider providing a step-by-step description of their pseudo-label correction algorithm, possibly with package algorithm.

### Questions
I like the idea very much, but some things are unclear in the paper, thus I lower my score.

(1) This is an important one. What is the algorithm for the pseudo-label correction? I can only find several descriptions for it. Could the author give a detailed description of it?

(2) This is less important. How is the Lipschitz constant calculated? I still can only find some rough description of it in the appendix on Page 17, but without a detailed description.

(3) It would be interesting to see the scores of 16-shot on the student model. We know the student is good at 0-shot, how about 16-shot?

Others:

(4) The idea of Sec. 3.2 could be applied to joint training of multiple tasks. In Table 3, we see OOD generalization via training on task A and testing on task B. It would be interesting to train multiple tasks and test on the others.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
When using in-context learning to solve tasks with LLMs, they can suffer from instability, characterised by biases toward the first and last examples in the demonstrations. Furthermore, using many demonstrations in long contexts extends the length of the LLM’s prefix window, increasing computation. This paper proposes a method to disentangle unlabelled demonstrations in-context from queries using self-training. A teacher model sees the demonstrations along with the query and produces a pseudo-label that a student model is trained on using adapters. These adapters (approximately theoretically) learn the demonstrations, allowing the student to be prompted with only the query and achieve comparable (in fact, better due to a weak-to-strong generalisation effect) performance than n-shot prompting. The method is also shown to outperform other comparable approaches.

### Strengths
As far as I am aware, the method (self-training from unlabelled demonstrations using a teacher to generate pseudo-labels) is simple but novel. However, I note that I am not extensively familiar with the literature in this area. The paper is clearly written and mostly easy to understand. The idea is nicely motivated by the theory used based on linear attention. I think that the work is significant. Long-context models suffer from serious inference-time bottlenecks. This work has not only shown a way to eliminate this bottleneck in certain scenarios where demonstrations may dominate (which on its own I would deem significant), but also improves in terms of quality compared to comparable approaches. The discussion on weak-to-strong generalisation is interesting and valuable.

### Weaknesses
 - There is no section on limitations. I would be interested in seeing some discussion on this with respect to both the chosen method and results. In particular, the computational cost of training vs using demonstrations, when is the method not applicable, and the lack of exploration with very large demonstration sets.
- Some of the discussion on weak-to-strong generalisation in section 2 is unclear. It does not explain why the student is expected to outperform the teacher or about what local-to-global consistency is in the context of in-context learning. I had to refer quite a lot to the cited paper to understand what was being said here. Please clarify.
- The theory is interesting motivation but based on an approximation of quadratic attention. To provide further support, given the limited theory, is there a way you could experimentally determine whether the demonstrations have been disentangled?

### Questions
- Regarding the evaluation setup, are the queries used in training the student with pseudo-labels disjoint from those used when evaluating the student?
- Is stability an issue beyond transformer-based LLMs? E.g. for state-space/diffusion-based LLMs?
- Do you have any quantification of how much more efficient your method has made inference?

### Soundness
3

### Presentation
3

### Contribution
3
