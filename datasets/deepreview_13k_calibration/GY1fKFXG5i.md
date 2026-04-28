# Non-Vacuous Generalization Bounds for Large Language Models

- Decision: Reject
- Avg Score: 6.60
- Scores: 8, 5, 6, 8, 6

## Abstract
Modern language models can contain billions of parameters, raising the question of whether they can generalize beyond the training data or simply parrot their training corpora. We provide the first non-vacuous generalization bounds for pretrained large language models (LLMs), indicating that language models are capable of discovering regularities that generalize to unseen data. In particular, we derive a compression bound that is valid for the unbounded log-likelihood loss using prediction smoothing, and we extend the bound to handle subsampling, accelerating bound computation by orders of magnitude on massive datasets. To achieve the extreme level of compression required for non-vacuous bounds, we devise SubLoRA, a simple low-dimensional nonlinear parameterization that leads to non-vacuous generalization bounds for models with nearly a billion parameters. Finally, we use our bounds to understand LLM generalization and find that larger models have better generalization bounds and are more compressible than smaller models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Low Rank Adaption where parameter updates $\Delta W$ is taken to be a product of two lower rank matrices that can be learnt; is combined with subspace training that uses  a projection to/from lower dimension subspace and arithmetic coding; to propose a combination of the two suitable for LLMs. Under i.i.d. assumption, risk generalization bounds are derived for LLMs on token prediction task. These bounds (that depend on empirical risk) are computed for several methods, with the bounds, and the empirical performance is shown to be best for the proposed method.

### Strengths
- Compression bounds obtained with a neat smoothing trick
- Code provided and also one that does not require industrial grade resources (but see Questions)
- Very nicely written and presented
- Improves upon previously reported bounds
- Context of research contributions and related work reviewed very well
- A bound is given where the empirical risk can be computed over a small subsample of the dataset
- Bounds computed for some  methods, bounds best for SubLoRA

### Weaknesses
 **Task and Error**
- I would suggest better clarity about what the task is (token prediction) early on in the paper and also in the abstract and methodology section.
- Also perhaps more clarity about errors. When it is said top-1 error, do you mean the worst sequence, or the worst token? 

**I.I.D. Assumption**
	- i.i.d assumption is a very strong assumption
	- but then a workaround is found which considers sequences not tokens, but then it's unclear how the parameter L is chosen



### Questions
**Artifact**
- It seems the provided code is running the glue suite, and the code involves LoRA, but not subLoRA? And the other folder seems to be from nanoGPT?
	- Glue suite seems to be unrelated to the task in paper: token prediction?
- At first because of the copyright line in the provided file, I was going to make a comment how it seems double blindness of the review is compromised as it seemed the submission was from the Hugging Face Team, but then I realized it is a minor modification of the same file from the Hugging Face Repository
- Can you please check if the provided code is what you intended to submit? And let me know if I am missing something? And also some rough system specifications on which it can be run?

**Comparison with Other Methods**
- when comparing LoRA and Subspace (e.g. in figure 1) we see a comparison of train error, but not test error. Is there a reason for that?

**I.I.D Assumption**
- Can you please comment on why, despite the i.i.d. assumption, these results are still significant?

**Possible Minor Typos / Formatting / Clarity** 
- page 6. 'payed'
- abbreviation NLL used without definition
- references need to be reviewed for formatting
- page 4, second last line, shouldn't it be "u: = flatten( ...)" instead of "LoRA(u) := flatten ( ... )"
- page 6, last paragraph says we use "several" values for r, giving the impression they are more than two, but the appendix mentions two values {1,4}
- page 14, second last paragraph: "Choosing an overall ... ". Please recheck this for clarity.


In summary the only major reservations I have are about the provided code and the i.i.d assumption, to the best of my knowledge. I apologize if I overlooked something important. Please feel free to correct me for any errors I may have made while reviewing; and to address these concerns. Thank you.

My vote is to for strong accept, conditional on addressing concerns regarding the prototype code.

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
The paper aims to compute non-vacuous generalization bounds that apply to LLM pre-training. The authors employ a compression-based PAC-Bayes approach to achieve this goal. To obtain good compression they employ both LoRA and subspace training. Further, they apply a trick to bound the prediction probability of tokens so that the NLL becomes bounded, making it amenable to standard PAC-Bayes analysis. Finally, their experimental results show that their approach outperforms state-of-the-art generalization bounds.

### Strengths
- The authors compute non-vacuous generalization bounds for LLM which can be challenging. 
- The paper is well-structured and the language is good. 
- The experimental results seem to outperform the current state of the art.

### Weaknesses
 - While the paper is well-written for the most part, some parts are confusing. 
- The technical contribution is moderate on the conceptual part is fair, however, engineering a working non-vacuous bound can be challenging.
- In Equation (2) it seems that LoRA is applied to $Pw$, it is not clear to me how that can be implemented, in particular, how the weights can have the forms $Pw$ and $UV$ simultaneously. It might, however, be just a typo and the equation should be $P \cdot LoRA(w)$. 
- In section 4.4, it is not clear why we can assume that $\hat{R}_{\sigma_{i}}(h)$ are independent. In general, taking a random sample of a sequence does not make such a random sub-sample independent.

A minor typo:
$Q_1, Q_2 \sim \mathcal{N}(0,1)^{\sqrt{D}\times d}$ ----> $Q_1, Q_2 \sim \mathcal{N}(0,1)^{\sqrt{D}\times \sqrt{d}}$

### Questions
- In Equation (2) it seems that LoRA is applied to $Pw$, it is not clear to me how that can be implemented, in particular, how the weights can have the forms $Pw$ and $UV$ simultaneously. It might, however, be just a typo and the equation should be $P \cdot LoRA(w)$. 
- In section 4.4, it is not clear why we can assume that $\hat{R}_{\sigma_{i}}(h)$ are independent. In general, taking a random sample of a sequence does not make such a random sub-sample independent.

A minor typo:
$Q_1, Q_2 \sim \mathcal{N}(0,1)^{\sqrt{D}\times d}$ ----> $Q_1, Q_2 \sim \mathcal{N}(0,1)^{\sqrt{D}\times \sqrt{d}}$

### Soundness
3 good

### Presentation
2 fair

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
In this paper, the authors aim to establish non-vacuous generalization bounds for large language models (LLMs) by employing a compression-based approach. The challenges they address include (1) dealing with the non-iid nature of tokens, (2) handling unbounded loss, and (3) managing extremely large model parameters. To tackle these issues, the authors propose specific solutions: for (1), leveraging entire sequences to treat tokens as iid; for (2), introducing a smoothed model to manage unbounded loss; and for (3), developing SubLoRA, a novel technique that combines LoRA and subspace training during the training process. Notably, the authors demonstrate the non-vacuous nature of the derived bound for GPT-2.

In consideration of the fact that this represents the first non-vacuous generalization bound in the context of Large Language Models (LLMs), I have assigned a moderately favorable score. It's important to note that I have not conducted an exhaustive investigation to confirm whether this is indeed the inaugural non-vacuous bound, and I am relying on the authors' assertion in this regard.
My reasons for not awarding a higher score can be attributed to the following factors:

1. I hold the perspective that the existence of vacuous bounds in LLMs during the pretraining phase might not be of paramount significance.
2. The authors primarily synthesize existing techniques rather than introducing fundamentally novel methods. It should be acknowledged that this does not necessarily translate to incremental progress since discovering these techniques is not a straightforward endeavor. However, a higher rating is withheld due to the absence of groundbreaking or distinctly tailored contributions to LLMs.

### Strengths
1. The authors pioneer the introduction of a non-vacuous generalization bound for LLMs in the pretraining phase.
2. The SubLoRA method, which amalgamates LoRA and subspace training, enhances model compressibility.
3. The paper highlights and addresses various challenges in deriving generalization bounds for LLMs.
4. Experimental verification of the proposed bounds adds credibility to the research.

### Weaknesses
1. While the authors emphasize the importance of non-vacuous bounds during the pretraining phase, a more detailed justification of its significance *within the LLM context* would enhance the paper's impact. At least I am not sure that for LLM, generalization in the pretraining phase is such important. Specifically, the paper does not adequately address why a non-vacuous bound on pretraining loss is crucial for downstream task performance. It's unclear if a tighter pretraining bound directly translates to better generalization on downstream tasks, which are the ultimate goal for most LLM applications. The paper should provide a more compelling argument for why focusing on pretraining generalization is valuable, given that the pretraining objective is not directly aligned with downstream objectives.
2. Given the point 1, I wish to see some novel techniques. However, it seems that the techniques in this paper are not very novel. The methods presented in this paper largely combine existing techniques (e.g., SubLoRA). While the combination of LoRA and subspace training is interesting, the paper lacks a detailed analysis of how this specific combination provides a significant advantage over simply using LoRA or subspace training independently. A more in-depth exploration of the interaction between these techniques is needed to justify the novelty of SubLoRA. The paper should also discuss the limitations of this approach and in what scenarios it might not be effective.
3. The paper claims that tokens exhibit non-iid behavior but resolves this issue by considering entire sequences, which might be considered a somewhat coarse approach. Treating entire sequences as i.i.d. might mask the underlying dependencies between tokens within a sequence, which are crucial for language modeling. The paper should acknowledge this limitation and discuss potential alternative approaches that could better capture the sequential nature of language data. For example, a more fine-grained analysis of token dependencies within sequences could be considered.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper derives a compression bound that is valid for the unbounded log-likelihood loss using
prediction smoothing, and we extend the bound to handle subsampling, accelerating bound computation on massive datasets. Using this approach, we find that larger models have better generalization bounds and are more compressible than
smaller models.

### Strengths
1. This paper provides the first non-vacuous generalization bounds for LLM
pertaining by using extreme levels of model compression. The bounds suggest that compression
bounds present new possibilities for understanding how and why language models generalize.
2. The experiments verify their theoretical results.

### Weaknesses
None

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors derive generalization bounds for auto-regressive
language models pre-training combining four ingredients:

1.  a non-uniform hypothesis prior in the PAC-bound
2.  the intrinsic dimension to bound the complexity of the neural model
3. a form of label smoothing (prediction-smoothing) for bounding the
negative log-likelihood
4. subsampling to reduce the cost
of empirical risk estimation. 

They also propose to combine LoRA with
subspace fine-tuning for finding the intrinsic dimension more
efficiently. The empirical part demonstrates their generalization bounds by
performing experiments on GPT-2-style models with less than 200M parameters.

### Strengths
1. A simple and elegant proposal, prediction smoothing, to accomodate the unbounded NLL loss in deriving generalization bounds.

2. A novel proposal that combines LoRA with subspace training for pre-training on a lower dimensional subspace.

3. An empirical verification of the effect that text structure has on generalization bounds.

### Weaknesses
 1. The paper seems to lack a thorough comparison to previous theoretical work that
  highlights the novel theoretical contributions. For example, the cited
  **Aghajanyan et. al (2020)** proves a generalization bound for
  classifiers that have been obtained by fine-tuning a pre-trained
  language model. Their bound already relies on intrinsic dimension
  (Ingredient 2) to reduce the hypothesis space and what seems to me a version of Ingredient 1 for compression based on **Arora et al**: *Stronger Generalization Bounds for Deep Nets via a Compression Approach*. Ingredients (1, 2) and a version of Ingredient (4) seem to be present in **Lofti et. al**.
  
* Exposition could be improved if the main generalization results
  were stated as a Theorem with a discussion of the proof ingredients.
  
* Experiments are carried out on small model sizes (from the Appendix it seems
  < 200M). It is then unclear if these findings would generalize to
  large LMs, e.g. to the > 10B scale. The bounds for NLL seem
  to improve in the tested scales, but it is unclear how these are related
  to the generalization abilities in the few-shot or instruction following
  capabilities that large LMs exhibit.

### Questions
My initial rating inclines towards rejection because I have some
concerns regarding:

1. the novelty of the bounds and the theoretical arguments wrt to previous work
2. the empirical part seems limited to small model sizes
3. the benefits of SubLoRA in downstream applications are not clear.

I am leaving some questions that would help me to improve
my assessment and in case increase the initial rating.

**Questions**:

1. Could you highlight the novel contributions and comparison to the work discussed in Weaknesses 1?

2. What was the biggest model you trained and using how many tokens?

3. In Table 1 is it the case that Subspace only is enough to achieve non-vacuous generalization bounds?

 4. What is the tradeoff between SubLoRA and standard pre-training?
 
5. If a pre-trained model exhibits few-shot capabilities, does its counterpart that was pre-trained with SubLoRA exhibits the same
    abilities?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
