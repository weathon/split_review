# Conformal Language Modeling

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 3, 8, 8

## Abstract
In this paper, we propose a novel approach to conformal prediction for  language models (LMs) in which we produce prediction sets with performance guarantees. 
LM responses are typically sampled from a predicted distribution over the large, combinatorial output space of  language. Translating this to conformal prediction, we calibrate a \emph{stopping rule} for sampling LM outputs  that get added to a growing set of candidates until we are confident that the set covers at least one acceptable response. Since some samples may be low-quality, we also simultaneously calibrate a \emph{rejection rule} for removing candidates from the output set to reduce noise.
Similar to conformal prediction, we  can prove that the final output set obeys certain desirable distribution-free guarantees. Within these sets of candidate responses, we also show that we can also identify subsets of individual components---such as phrases or sentences---that are each independently correct (e.g., that are not ``hallucinations''), again with guarantees.   
Our method can be applied to any LM API that supports sampling. Furthermore, we empirically demonstrate that we can achieve many desired coverage levels within a limited number of total samples when applying our method to  multiple tasks in open-domain question answering, text summarization, and radiology report generation using different LM variants.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the conformal prediction framework to language models (LMs). The aim is to construct prediction sets of LM responses such that at least one is "acceptable" with a desired probability.

This goal is achieved by sampling responses repeatedly from the LM and adding them to the prediction set until a stopping rule occurs: either (i) an upper bound $k_{\max}$ on the number of samples drawn from the LM, or (ii) a lower bound $\lambda_{3}$ on the prediction set confidence score, quantifying how good it is. Additionally, samples are removed from the prediction set (to reduce noise) based on a rejection rule: either (i) a lower bound $\lambda_{2}$ on the individual response's quality, or (ii) an upper bound $\lambda_{1}$ on the response's similarity with others in the set. $\lambda = (\lambda_{1}, \lambda_{2}, \lambda_{3})$ is a configuration that is picked via the Learn Then Test [Angelopoulos et al. 2021a] framework; $k_{\max}$ is fixed by the user. Note that not all desired errors are achievable. The paper also proposes an extension to identify individual components of the responses (for instance, sentences from paragraphs) that are each independently "acceptable" with desired probability.

The paper goes on to provide empirical results to corroborate its methodology. Experiments on open-domain question-answering, text summarization, and radiology report generation empirically verify the proposed algorithm and its statistical guarantees.

### Strengths
1. This paper tackles an important research area of providing statistical guarantees on the output of language models.
2. These statistical guarantees are provided by leveraging the conformal prediction framework and extending it to language models, which is a generative task.
3. The proposed algorithm is easy to interpret: sample responses from the language model as long as the rejection and the stopping rules are not triggered.
4. The theoretical results are corroborated experimentally on 3 tasks.

### Weaknesses
1. The proposed algorithm is easy to interpret. However, the paper does not explain all design choices.
2. The experimental results support Theorem 4.2. However, Proposition 4.4 is not experimentally validated.
3. Theorem 4.2 guarantees at least one "acceptable" language model response in the prediction set but does not say much about the individual responses. While the paper considers components of the responses, the response as a whole is not.

### questions:
 1. Design choices:
    1. Why is $\hat{\lambda}$ defined as in Eq. 7? Similarly, why is it desirable for $C^{\text{inner}}_{\gamma}$ to be large ($\hat{\gamma}$ in Eq. 10)? Explicitly explaining these would help the reader. Are there alternative definitions that might be advantageous?
    2. What is the reason for using a different definition of $C^{\text{inner}}_{\gamma}$ during calibration?
    3. The Pareto Testing procedure is used in the proposed algorithm for efficiency. However, the appendix only provides a high-level overview. Can the authors include more details and explain how this procedure helps efficiency?

2. Experiments:
    1. The achievable risk range for MIMIC-CXR is very high. How can one reduce this for the practicality of the proposed method?
    2. How is the AUC for the set loss plots greater than 0.5? The diagonal should have an AUC of 0.5, and since all the curves are under this, their respective AUCs should be lower than 0.5.
    3. The First-$k$ scoring function does not utilize rejection. As a result, the likelihood-based approaches have better prediction efficiency. Did the authors try First-$k$ with the rejection scheme for a more apples-to-apples comparison?
    4. What about the set loss in the individual component case? Experimental results on that would corroborate the theoretical result in Proposition 4.4.
    5. What is $k_{\max}$ set to for the experiments?
    6. The data splits to obtain the train, calibration, and test sets aren't well explained in the paper (appendix included). For example, the authors use a dev set for the conformal prediction experiments, but in what way? Can the data splits be explained more succinctly for the datasets used?

3. "While Eq. 1 stipulates the existence of at least one "acceptable" generation in $C_{\lambda} (X_{\text{test}})$, it does not tell us much about individual responses, $y \in C_{\lambda} (X_{\text{test}})$" (Section 1). Is there any remedy for this? This paper discusses individual components (for example, sentences) but not the whole LM responses.

Clarifications:

1. It would be helpful for the reader to highlight why admission functions $A_{i}$ are used rather than labels $Y_{i}$ in Section 1 (where the setup is explained).
2. Shouldn't the function $A^{c}$ be a mapping $\mathcal{Y} \mapsto \{0, 1\}$ instead of $2^{\mathcal{Y}} \mapsto \{0, 1\}$ (Section 4.4) as it acts on individual components?
3. $\mathcal{Y}$ and $\mathcal{V}^{*}$ are used interchangeably. Making it consistent would help the reader.
4. It would be helpful for the reader to add more descriptive captions for the tables in Appendix H. For example, the authors can highlight what the findings are not just in the text but in the table captions as well.
5. Should Eq. 20 be replaced with Eq. 7?
6. Missing definitions:
    1. $\mathcal{Y}$ is not defined in Section 1 but is used right before Eq. 1.
    2. $L_{\text{test}} (\lambda)$ is not defined but is used right before Eq. 3.
    3. $F_{X} (u), F_{Y} (y)$ are not defined in Appendix D.1.
7. Missing superscripts:
    1. The superscript $c$ in $A^{c}_{\text{test}}$ is missing in the text before and after Eq. 9.
    2. The superscript $c$ in $\bar{L}^{c} (\gamma)$ is missing in the text after Eq. 22.

### Questions
1. Design choices:
    1. Why is $\hat{\lambda}$ defined as in Eq. 7? Similarly, why is it desirable for $C^{\text{inner}}_{\gamma}$ to be large ($\hat{\gamma}$ in Eq. 10)? Explicitly explaining these would help the reader. Are there alternative definitions that might be advantageous?
    2. What is the reason for using a different definition of $C^{\text{inner}}_{\gamma}$ during calibration?
    3. The Pareto Testing procedure is used in the proposed algorithm for efficiency. However, the appendix only provides a high-level overview. Can the authors include more details and explain how this procedure helps efficiency?

2. Experiments:
    1. The achievable risk range for MIMIC-CXR is very high. How can one reduce this for the practicality of the proposed method?
    2. How is the AUC for the set loss plots greater than 0.5? The diagonal should have an AUC of 0.5, and since all the curves are under this, their respective AUCs should be lower than 0.5.
    3. The First-$k$ scoring function does not utilize rejection. As a result, the likelihood-based approaches have better prediction efficiency. Did the authors try First-$k$ with the rejection scheme for a more apples-to-apples comparison?
    4. What about the set loss in the individual component case? Experimental results on that would corroborate the theoretical result in Proposition 4.4.
    5. What is $k_{\max}$ set to for the experiments?
    6. The data splits to obtain the train, calibration, and test sets aren't well explained in the paper (appendix included). For example, the authors use a dev set for the conformal prediction experiments, but in what way? Can the data splits be explained more succinctly for the datasets used?

3. "While Eq. 1 stipulates the existence of at least one "acceptable" generation in $C_{\lambda} (X_{\text{test}})$, it does not tell us much about individual responses, $y \in C_{\lambda} (X_{\text{test}})$" (Section 1). Is there any remedy for this? This paper discusses individual components (for example, sentences) but not the whole LM responses.

Clarifications:

1. It would be helpful for the reader to highlight why admission functions $A_{i}$ are used rather than labels $Y_{i}$ in Section 1 (where the setup is explained).
2. Shouldn't the function $A^{c}$ be a mapping $\mathcal{Y} \mapsto \\{0, 1\\}$ instead of $2^{\mathcal{Y}} \mapsto \\{0, 1\\}$ (Section 4.4) as it acts on individual components?
3. $\mathcal{Y}$ and $\mathcal{V}^{*}$ are used interchangeably. Making it consistent would help the reader.
4. It would be helpful for the reader to add more descriptive captions for the tables in Appendix H. For example, the authors can highlight what the findings are not just in the text but in the table captions as well.
5. Should Eq. 20 be replaced with Eq. 7?
6. Missing definitions:
    1. $\mathcal{Y}$ is not defined in Section 1 but is used right before Eq. 1.
    2. $L_{\text{test}} (\lambda)$ is not defined but is used right before Eq. 3.
    3. $F_{X} (u), F_{Y} (y)$ are not defined in Appendix D.1.
7. Missing superscripts:
    1. The superscript $c$ in $A^{c}_{\text{test}}$ is missing in the text before and after Eq. 9.
    2. The superscript $c$ in $\bar{L}^{c} (\gamma)$ is missing in the text after Eq. 22.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a different kind of sampling for LMs. The idea is to extend ideas from Conformal Prediction to produce solution sets that contain diverse outputs. Generation follows a three step process involving sampling, accepting (if the answer is sufficiently high probability), and then possibly resampling if there aren't enough diverse answers in the set yet.

Evaluation is done on a few tasks and LMs -- chest Xrays with a GPT2 small LM + ViT, news summarization on CNN/dailymail with T5-XL, and Open-domain QA on triviaQA sampled from LLaMA-13B. To the best of this reviewer's understanding the evaluation is done assuming access to the ground truth set of references, and so early stopping is done if the prediction set contains the answer already.

### Strengths
To this reviewer, the application of conformal prediction to LMs could be interesting. Sampling in a way that preserves diversity and quality; and that returns a variety of different generations at the sequence level, could be a solid contribution. There's a lot of math here (mostly beyond the understanding of this reviewer, who is not an expert on conformal prediction in particular) but that could be helpful to people working in this space, for how to extend these ideas to LMs where the solution space is vast.

### Weaknesses
To this reviewer, it's a bit unclear what the benefit of this approach is (ie what problem it's solving). There's a worked example but it's a bit hard to follow as I'm neither an expert in conformal prediction nor cardiology. I guess my confusion comes down to this part:

"Like conformal prediction, our method offers a rigorous coverage guarantee by constructing prediction sets that, in our case, provably contain at least one acceptable response with high probability. Unlike conformal prediction, however, we do not enumerate the entire output space (which is impossible). Instead, we derive a calibrated stopping rule for sampling different outputs from the LM that get added to a growing output set of candidates, until we are confident that the output set is sufficient"

This seems reasonable to this reviewer, but it also seems like from the experiments, the stopping rule involves having access to the test set answers, which seems not realistic. It's not quite clear what the objective is (minimize loss, minimize excess numbers of samples).

I think this paper would also benefit from some stronger yet simpler baselines that don't follow conformal prediction. E.g. sampling N times and checking whether any of the samples is in the ground truth.

I think this paper would benefit from comparison with other types of ways of controlling diversity, e.g. Stochastic Beam Search https://arxiv.org/abs/1903.06059 or NeuroLogic sampling https://aclanthology.org/2022.naacl-main.57/ . A worry I have with this approach (that I asked in the 'questions' field) is that the procedure in Sec 4 might never terminate because the LM might keep returning the same kind of answer over an over again (or at least a sufficiently strong LM might); maybe lexically constrained decoding would fix this.

Finally there's the evergreen concern that this approach might become less important at scale; comparing e.g. GPT2small vs GPT2-XL could help here.

### Questions
for the 3-step procedure described in section 4, is it possible this will never terminate? To this reviewer, it seems a little bit sketchy to use ROUGE or BLEU to score diversity.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies inference of responses generated by large language models (LLMs), 
leveraging ideas of conformal prediction. The specific aim is to construct a set of 
responses for a given prompt $x$, such that at least one response in the set is 
``acceptable'' (compared with an expert response that we do not get to observe).

The main technical component is from [1], where the Learn then test (LTT) method is 
tailored for this specific setting. The authors evaluate the proposed method on the task 
of radiology report generation, news summarization, and open-domain question answering.

[1] Angelopoulos, Anastasios N., et al. "Learn then test: Calibrating predictive algorithms to achieve risk control." arXiv preprint arXiv:2110.01052 (2021).

### Strengths
1. The paper is very written: it contains sufficient details and is easy to follow. 
2. This work provides an interesting application of the LTT framework. From my understanding, the major 
contribution includes formulating the task as a risk-controlling problem, specifying the tuning parameters, 
and identifying the optimization problem that fits practical goals. 
3. The paper also provides abundant numerical evidence supporting the validity and efficiency of the proposed method.

### Weaknesses
I do not see obvious weaknesses of this work, but a few questions regarding some details (they are in the question section).

### Questions
1. I wonder how the computational time (or relative excess samples) changes with regard to the choice of $k_\max$?
2. In the proposed method, $k_\max$ is fixed. As pointed out by Remark 4.3, the choice of $k_\max$ does not affect 
the coverage guarantee, but could result in uninformative results. I wonder if it could be possible to treat $k_\max$ as a tuning 
parameter as well, e.g., $\lambda_4 = k_\max$, and we can then optimize over all ``valid'' k_\max.
3. For the individual component pruning, I also wonder if the $\gamma$ can be tuned jointly with the $\lambda$'s to avoid the 
union bound?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an extension of the learn-then-test framework which could help generating responses from language models with risk control. It proposes a sampling pipeline which involves adding generations to a prediction set until the set-level confidence score is above a threshold. The whole pipeline involves using LTT to search for viable configs of three hyperparameters (for the quality of single generation, the rejection/diversity of single generation, and the quality of the prediction set). The experiments were carried out on three medical and benchmark datasets, suggesting that this pipeline generally is able to find feasible hyperparams.

### Strengths
This is a first (yet quite solid) step forward in conformal prediction in NLG. It proposes a general framework to sample responses from language models with some given criteria (admission function), and allows independent research to improve the various scoring functions (quality estimate, diversity rejection criteria, etc.) in the pipeline. Breaking down the full generation into different components is also a nice way to address the question of UQ for longer texts.

### Weaknesses
The main weakness is the use of ROUGE-L as a proxy of the quality of the generation. This only captures the the lexical similarity between the generation and the reference, which undermines the experiments quite a bit, in the following sense:
1. the LTT framework might return null hyperparameters, which might happen more often should the admissible function by the human be stricter than ROUGE
2. ROUGE was also used in the pipeline (detecting duplicate) so it's kind of "being its own judge"

Another potential improvement is to include a stronger baseline than first-K - for example, the duplicated responses (maybe even basing on rouge) should at least be deleted?

### Questions
1. How are the thresholds 0.4 and 0.35 for ROUGE-L determined? What does "These thresholds are picked through manual validation" mean exactly?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
