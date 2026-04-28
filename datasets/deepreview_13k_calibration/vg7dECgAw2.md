# Automatic Calibration and Error Correction for Generative Large Language Models via Pareto Optimal Self-Supervision

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Generative Large language models (LLMs) have demonstrated remarkable capabilities for a wide range of applications, but reducing ungrounded or erroneous responses remains a major growth area. Unlike task-specific models, there lack an effective method to calibrate the confidence level of LLM responses to indicate potential errors and facilitate human-in-the-loop verification. An important source of calibration stems from expert-stipulated programmatic supervision, which is often available at low cost but has its own limitations such as noise and coverage. In this paper, we introduce a Pareto optimal self-supervision framework that can leverage available programmatic supervision to systematically calibrate LLM responses by producing a risk score for every LLM response, without any additional manual efforts. This is accomplished by learning a harmonizer model to align with LLM output as well as other weak supervision sources. The model assigns higher risk scores to more uncertain LLM responses and facilitate error correction. Experiments on standard relation extraction and classification tasks in biomedical and general domains demonstrate that the proposed risk score is highly correlated with the actual LLM error rate. By using a dynamic prompting strategy based on the risk score, we observed significant accuracy improvement for off-the-shelf LLMs, boosting GPT-3.5 results past state-of-the-art (SOTA) weak supervision model and GPT-4 results past SOTA supervised results on challenging evaluation datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Although the development of large language models (LLMs) is in full swing, the phenomenon of hallucinations has been an issue that we cannot ignore, as it poses a significant challenge to the reliability of LLMs in real-world scenarios. Given the lack of an effective method to calibrate the confidence level of LLM responses to reveal potential errors, this paper proposes a novel framework for LLM calibration using Pareto optimal self-supervision. Specifically, it leverages available programmatic supervision to systematically calibrate LLM responses by producing a risk score for every LLM response without any additional manual efforts. Experimental results show the proposed risk score is consistently well-calibrated to the probability of LLM error. On this basis, a dynamic prompting strategy has been further developed to automatically correct LLM errors, boosting GPT-4 results past SOTA supervised results on challenging evaluation datasets.

### Strengths
- It's a meaningful attempt to calibrate the confidence level of LLM responses to indicate potential errors. Combining information from both the LLM response and other supervision sources, the paper presents a flexible framework that optimizes a harmonizer network $h(x)$ to assist in assessing the risk of LLMs' outputs using Pareto optimal learning.
- The article is rich in theoretical arguments, explaining how calibrating LLM and detecting errors can be achieved by learning a harmonizer network using the Pareto optimal theory.
- Experiment results demonstrate that the proposed Pareto optimal learning assessed risk (POLAR) score is effective in estimating LLM error probability, and the designed dynamic prompting strategy boosts a significant accuracy improvement for off-the-shelf LLMs without any manually labeled training data.

### Weaknesses
 - The proposed framework is restricted to tasks where the desired output space $\mathcal{Y}$ is finite, which can be impractical for real-world applications when there is no definitive answer in a finite set, e.g., recommending websites for learning languages.
- I am sorry, but I don't think the two intuitions behind how calibration can be achieved (mentioned by the authors in the introduction) are easy to understand, perhaps due to my lack of expertise. They look like two conclusions that other works have confirmed. Are there any references?
- I do not see a natural connection between **Proposition 1**, **Proposition 2** and Pareto optimal learning. According to the **Proposition 1**, fitting a model $h(x)$ to $Λ(x)$ is equivalent to training on ground truth labels with label smoothing. However, I do not find that the author mentioned using the "label smoothing" technique while optimizing the harmonizer network $h(x)$. Also, I'm not sure how this is solved by using Pareto optimal learning.

### Questions
- As a major part contributing to the multi-objective optimization, the supervision functions $\lambda_j$ do not seem to be clearly presented.
- In the **Definition 2** (Pareto scalarizer), what is the difference between $G(\mathcal{l}_0, \cdots, \mathcal{l}^{'}_j, \cdots, \mathcal{l}_m)$ and $G(\mathcal{l}_0, \cdots, \mathcal{l}_j, \cdots, \mathcal{l}_m)$, as far as I understand, they have the same $m$ objectives?
- So is the Pareto scalarizer actually equivalent to the uniform weighting scheme?
- How are the two metrics based on  POLAR score, i.e., expected calibration error (ECE) and $R^2$ calculated?
- For every baseline method, is the error rate calculated by comparing the estimated class probabilities with ground truth labels?
- From Figure 3(a), it seems that we can always use the dynamic self-supervision prompting strategy to achieve a decent error rate?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
It is important to detect when Large Language Models (LLMs) hallucinate. Namely, we'd like to know the level of confidence of an LLM, e.g. the quantity $\Pr(\Lambda(x) = y | x)$. To better calibrate LLMs, this paper leverages external sources of supervision to estimate this confidence score. The paper frames this as a multi-objective problem, training a harmonizer that minimizes discrepancies between the LLM's output and the supervision functions. One can then derive the POLAR score from the harmonizer, which serves as an estimate of the actual risk associated with each data sample. The paper also presents a way to use the POLAR score for dynamic prompting, where a prompt that is likely overconfident is patched with feedback/reflection from the supervision functions. Empirically, the paper demonstrates a strong correlation between the POLAR score and the true error rate obtained from gold labels. It also shows the effectiveness of using the POLAR score to rectify errors in LLMs, compared to approaches based on standard weak supervision (Snorkel) or training a smaller model on the LLM output (Distillation).

### Strengths
Originality:
- Pareto-optimal multi-objective approach is novel compared to other weak supervision techniques.

Quality:
- Strong empirical validation
- Dynamic prompting appears to work very well

Clarity:
- Paper's results and problem setup were easy to follow.

Significance:
- The paper touches on an important issue in using LLMs and gets around approaches that can include the model's own biases. Beyond calibrating, the dynamic prompting approach shows a workflow in which error detection and model editing can be carried out effectively.

### Weaknesses
Originality:
- Weighting dilemma is not something new in weak supervision. A major goal is rather than using one weight per supervision function across the entire dataset, we'd like to have input-specific weight parameters (such as https://arxiv.org/abs/2107.02233).

Quality:
- Limitations of theoretical results are not discussed well. For instance in proposition 2, the existence of a function doesn't imply that this function class is how $\Lambda(x), w(x)$ is aggregated.
- The paper could be made stronger by comparing to weak supervision methods that also solve the weighting dilemma, like the paper linked above I think.

### Questions
- Can you discuss limitations of theoretical results?
- See my question about comparing to additional weak supervision methods.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
# Summary
AUTOMATIC CALIBRATION AND ERROR CORRECTION FOR GENERATIVE LARGE LANGUAGE MODELS VIA PARETO OPTIMAL SELF-SUPERVISION

## What is the problem?
LLMs are very powerful and impactful, but suffer from significant rates of miscalibration resulting in possible hallucinations, which can be seen as erroneous responses made by the model with high confidence. These significantly degrade model performance in practice. This paper is concerned with designing a weak-supervision signal to produce calibrated estimates of the model's likelihood of error, and using those signals to improve model performance in the first place.

## Why is it impactful?
Reducing rates of hallucinations would have major impact on the utility and safety of LLMs.

## Why is it technically challenging/interesting (e.g., why do naive approaches not work)?
Model calibration is always challenging, let alone in the domain of LLMs in which we often work with complex, large input domains of free-text and arbitrary, under-defined labeling functions.

## Why have existing approaches failed?
Existing approaches have not (to the best of my knowledge) as rigorously examined leveraging weak supervision as is explored in this work.

## What is this paper's contribution?
This paper uses pareto-optimization techniques to maximally harmonize a set of weak-supervision signals and an LLMs output to produce a score estimating the model's uncertainty in its predictions.

## How do these methods compare to prior works?
There are some existing works that should be referenced in this paper that seem to be missing:
  1. https://arxiv.org/abs/2104.08455
  2. https://ojs.aaai.org/index.php/AAAI/article/view/26596
  3. https://dl.acm.org/doi/abs/10.1145/3583780.3614905?casa_token=QsAQ_cJ35qwAAAAA:m4oawA8tORNEv3Nkn3zON32LJtqmBBkQgoL7dOGC5IeeNCt59-tcyoHUDsTcs5O0lzerxmtXSSJi

This is a very fast moving space, so there are some more recent works that should also be cited in the final draft (though they weren't out when this paper was submitted):
  1. https://arxiv.org/abs/2309.11495
  2. https://arxiv.org/abs/2308.11764
  3. https://arxiv.org/abs/2310.03951
  4. https://arxiv.org/abs/2310.00259
  5. https://arxiv.org/abs/2309.02654

## How do they validate their contributions?
They show that these uncertainty estimates are well calibrated and that using them via a self-supervision technique can significantly improve model performance.

### Strengths
## Key Strengths (reasons I would advocate this paper be accepted)
  1. This is a critical problem area to study.
  2. This approach is well thought out and the empirical results are compelling.
  3. This approach seems extensible to other sources of weak supervision as well.

### Weaknesses
## Key Weaknesses (reasons I would advocate this paper be rejected)
  1. This paper has major issues with clarity. You have a lot of typos / odd grammatical issues and sentence structures that make it hard to understand. E.g., "Unlike task-specific models, there lack an effective method..." in the abstract. Even beyond these, there is some major missing information throughout in important sections. For example, on the top of page 4 (from the end of Proposition 1 to the start of Proposition 2), you have a paragraph that contains a lot of statements illustrating potential problems and arguing that certain things are therefore needed with little to no explanation of these key ideas and why we should believe they are true. E.g., why does Proposition 1 show a path towards calibrating an LLM via distillation? How does this show the need of external signals? etc. In addition, some mathematical statements are not sufficiently explicitly stated to be correct as written, which need to be corrected for sure.
  2. Your proposition 2 is not sufficiently well specified to be true. You need to expand on what "weak independent signal ensemble" means to eliminate the case that the weak ensemble contains no new information relative to your LLM itself (and therefore cannot contribute meaningful improvements over the LLM). Also your notation for the function $\psi$ is inconsistent, as $\psi$ is listed as a function of both the functions $\Lambda$ and $w$ as well as of their outputs. And you need to clarify why your $w$ is a continuous estimator, not a categorical, given you work in the categorical space in other settings.
  3. The inference you make in the second sentence of 3.3 is invalid given that you don't know that these "weakest supervision sources such as reg-ex or knowledge base" are actually independent of the LLM. I know you go back and state this in the next sentence or two, but if you're going to acknowledge it there, just be specific and clear from the outset.
  4. Isn't your "pareto optimization scalarizer" functionally reducing all your weak supervision signals to a single signal, thereby suffering the same concerns that you state the existing works will suffer by combining loss terms via a weighted sum?

### Questions
## Minor Questions
  1. Do you iterate repeatedly in Algorithm 2 until your POLAR score is below $\delta$? Or do you just do the process once.

## Things I need to see to improve my score:
While I listed only a small amount of content in the strengths section and a lot in the weaknesses section, my overall recommendation here is a marginal accept. I feel that this contribution, and the results reported, suggest that this contribution is possibly of sufficient significance to warrant acceptance despite its somewhat severe issues with clarity and presentation. 

What I vigorously want to see in the revision to further improve my score is a significant revision to improve the quality of the writing (eliminate typos, grammatical errors, etc.), clarify all of the sections of the text, especially w.r.t. the methodology and details behind the experiments, and formal, correct, full statements behind the mathematical claims made in the work.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper found that even weak supervision sources can correct the erroneous responses from large language models. Based on this finding, the paper proposes to correct the erroneous responses from large language models by first calculating a Pareto optimal learning assessed risk (POLAR) score to indicate error rate. Then according to each term in the weak supervision, the model will decide if more evidence needed to be add to the current prompt through the self-examination process. Finally, new responses will be generated given the enhance prompt. The POLAR score best aligns with the actual error rate in most cases on four datasets.

### Strengths
The paper proposes a systematic way to correct erroneous responses by first training a scoring function with weak supervision and then automatically enhancing the prompt based on the learned scoring function.

### Weaknesses
My biggest concern about this paper is I think it's over-claimed. This paper frames the learning objective to be a Pareto loss scalarizer, and also requires the Pareto scalarizer to be a convex function, which is too strong. In this case, the Pareto optimal is only a single point in the whole function space, which seems not satisfying the realistic scenario. A more natural way should be giving a different weight to different $l$, and then finding the Pareto optimal under specific weight. Thus, we have the Pareto frontier. According to different scenario, we may choose different Pareto optimal on the frontier. If in this paper's setting, then it seems the pipeline is just like first it learns some score functions using additional supervision signals. Then it uses these scoring function to enhance prompt, and finally it gets better responses based on better prompts, which seems no novelty to me.

### Questions
1. In Theorem 1, if G is always a convex function, then Theorem 1 always holds. I don't see any importance from Theorem 1. Does Theorem 1 still hold when G is a non-convex function?

2. In Equation 7, for generation task, there might be multiple correct  and incorrect responses such as the descriptions following the Negative in Figure 1 might be different. Taking one as the ground truth and all others as error ones, the calculated thePOLAR score might have some bias. Besides, how to calculate this score as the search space is huge right? I saw the author assumed that Y space is finite, but how to guarantee that as the description is different, leading to different LLM function score?

3. In Table 1 and Figure 1, what scalarizer is used?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
