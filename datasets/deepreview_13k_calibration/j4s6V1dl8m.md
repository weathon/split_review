# Prover-Verifier Games improve legibility of LLM outputs

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 8, 5, 3

## Abstract
One way to increase confidence in the outputs of Large Language Models (LLMs) is to support them with reasoning that is clear and easy to check --- a property we call legibility. We study legibility in the context of solving grade-school math problems and show that optimizing chain-of-thought solutions only for answer correctness can make them less legible. 
To mitigate the loss in legibility, we propose a training algorithm 
inspired by Prover-Verifier Game from~\citet{anil2021learning}. Our algorithm iteratively trains small verifiers to predict solution correctness, ``helpful'' provers to produce correct solutions that the verifier accepts, and ``sneaky'' provers to produce incorrect solutions that fool the verifier. We find that the helpful prover's accuracy and the verifier's robustness to adversarial attacks increase over the course of training. Furthermore, we show that legibility training transfers to time-constrained humans tasked with verifying solution correctness. Over course of LLM training human accuracy increases when checking the helpful prover’s solutions, and decreases when checking the sneaky prover’s solutions. Hence, training for checkability by small verifiers is a plausible technique for increasing output legibility. Our results suggest legibility training against small verifiers as a practical avenue for increasing legibility of large LLMs to humans, and thus could help with alignment of superhuman models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents work on an important direction in AI Alignment - making the outputs of highly capable LLMs legible to humans. It describes results on a setup consisting of iterative prover-verifier training which improves accuracy and legibility. It also analyzes training dynamics (e.g. impact of the verifier’s size on iterative training), rendering the paper overall quite impactful in terms of building systems that have outputs legible to human overseers.

### Strengths
- Overall, this is a strong paper presenting alignment research in a novel, viable, and important direction. It focuses explicitly on training setups that are understudied and demonstrates strong results around legibility.
- The paper rests on a strong theoretical foundation around prover-verifier games, takes into account how an adversarial prover might work, and presents important early results about points such as verifier sizes, iterative setups when it comes to training models towards legibility/alignment, etc.
- The paper addresses concerns such as reward hacking and provides a good amount of diversity around reward functions and how these could influence future research.
- The paper is open about its limitations and future work around unsupervised learning for tasks that lack ground truth labels.

### Weaknesses
 - The paper conducts all experiments exclusively on GSM8k, where explanations can indeed be step by step while being natural. Moreover, all experiments are done on a single model type (GPT-4). This raises some concerns about the generalizability of the prover-verifier setup, especially to domains such as code generation, writing, etc. and settings with different base models. The reliance on a single dataset and model architecture makes it difficult to assess the robustness of the proposed approach across diverse problem structures and model capabilities. For instance, the step-by-step nature of GSM8k might not translate well to tasks requiring more abstract reasoning or creative text generation.
- The iterative training process might lead to overfitting and the early stopping conditions don’t seem clear and generalizable. The prover and verifier could adapt to each other’s outputs, and given that there is no cross model testing, it’s difficult to make claims about generalization in this setting. The lack of a clear stopping criterion, such as validation performance on a held-out set, introduces uncertainty about the stability and convergence of the training process. The potential for the prover and verifier to co-adapt to each other's specific weaknesses, rather than learning generalizable strategies, is a significant concern that needs further investigation. The absence of cross-model testing further limits the ability to assess the robustness of the learned policies.
- Lack of experiments/comparison with existing work on Explainable AI. Work on multi-agent debate for safety/legibility [1] or other methods to improve legibility [2] are not compared against. The paper does not adequately position itself within the broader context of explainable AI and multi-agent systems. The absence of comparisons with established methods makes it difficult to assess the relative advantages and disadvantages of the proposed approach. Specifically, the lack of comparison with multi-agent debate frameworks and other legibility-focused techniques leaves a gap in understanding the novelty and effectiveness of the presented work.
- The iterative training setup introduces risks such as reward hacking, deception, collusion, or steganography. The paper does not address concerns highlighted in alignment literature such as [3][4][5][6][7] that this work directly impacts. The verifier could be jailbroken by a strong prover with steganographic methods arising out of training, or models may converge to deceptive strategies that jointly lead to higher rewards. It would be important to discuss the paper’s results against such prior work in safety. The potential for the prover to exploit the verifier's weaknesses through reward hacking or deceptive strategies is a critical concern that is not sufficiently addressed. The possibility of steganographic communication between the prover and verifier, which could lead to non-legible outputs that are nevertheless rewarded, also needs to be considered. The lack of discussion on these alignment risks undermines the credibility of the proposed approach.
- There are some points which I have raised below in my questions, such as details on the flawed campaign for collecting human data or the accuracy of synthetic GSM8k data or early stopping conditions/hyperparameter tuning.

### Questions
- How are the synthetic data samples for GSM8k checked for correctness? Are they checked for correctness?
- Could the authors provide more details on the ‘flawed campaign’ regarding human annotations in their experiments?
- Risk of overfitting the prover and verifier to each other’s outputs: what happens if one uses different models? How does this then extend to other domains? Will the same amount of training resources be required for legibility in every domain or are there any generalization results that the authors could present?
- What issues related to the safety literature highlighted in the weaknesses section do the authors see arising out of their iterative training setup, and how can early work be done to prevent such alignment issues?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper investigates the trade-off between performance and legibility in large language models (LLMs) solving  GSM8k augmented with 100k synthetic examples.
The authors find, via a human study, that RL training for correctness reduces legibility of the solutions.
To improve legibility, the papers propose a "checkability training" method, similar to “Learning to Give Checkable Answers with Prover-Verifier Games” (Anil et al., 2021), which is in turn inspired by prior research in interactive proofs and PAC learning.
This involves iterative training of small verifier models and larger "helpful" and "sneaky" prover models. 
Checkability training achieves a balance, resulting in more legible solutions at a modest cost to accuracy.

### Strengths
I find the experiments very well-motivated.   Prior papers in adjacent areas like debate focus on question-answering datasets;
but it is obvious that research on legibility of reasoning is much more important.

Although the GSM dataset is easy, this is the first paper in this direction, and honestly the experiments would have been a good contribution even if it was on a toy dataset. I also think human legibility studies are less likely to be misleading on this sort of dataset.

The paper is extremely well-written, and also proposes many interesting follow-up ideas. I am particularly interested in whether sneaky provers resulting from this sort of training are useful in other ways, for example, as model organisms for deception evals.

### Weaknesses
 **Models:** My assessment of the paper is based on the assumption that it does not matter for the purpose of this conference that the models here never available to the public in any form.


In the interest of taking everything in good faith, I see two acceptable reasons for this:
-   there is no herd of similar models over a range of compute scales used in the paper; or
-   human studies had to start before models of similar capabilities were available to the public;

This also assumes that the models used in the paper are similar in all important ways to other LLMs that the research field is aware of. I am open to reducing my score to 6 if there is a reviewer consensus that there is no good reason to do this research on the models used in the paper.


**Ground truth answers:**
As mentioned in the paper, the rewards in checkability training require ground truth labels. Most of the important applications of this line of research will be in settings where there are no ground truth labels. Given that, I am uncertain whether the method in this paper will play a major role in long-term scalable oversight research.


**Technical details:** I believe the training described in the paper might be tricky to reproduce on a different suite of models, due to the lack of details about optimization, learning rates, and so on. Would the authors be interested in disclosing whether this sort of iterative training is difficult to set up correctly, or it worked on basicaly the first try?

### Questions
Claim about prior work: Figure 4 shows a drop in legibility due to optimization for correctness. Are the authors sure this phenomenon is novel? I cannot find anything right now, but I personally thought this was the case and already established somewhere.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates how to make outputs from large language models (LLMs) more legible and reliable through a method inspired by Prover-Verifier Games (PVG). The authors focus on the challenge of maintaining both correctness and legibility in outputs when solving grade-school math problems. The proposed iterative training algorithm trains a verifier to predict solution correctness and conditions, and provers to create either correct or subtly incorrect solutions. This approach enhances verifier robustness and human assessability of solutions over time.

### Strengths
- The paper presents an innovative adaptation of the Prover-Verifier Game to train LLMs for legibility.
- It includes both theoretical proofs and empirical studies showing the benefits of their method in improving solution checkability.
- The study extends beyond automated verification to demonstrate human evaluators' performance, indicating real-world applicability.
- The authors acknowledge trade-offs between optimizing for accuracy and maintaining human-legible outputs, highlighting practical insights for future applications.

### Weaknesses
 - The study primarily focuses on grade-school math problems; exploring broader applications could demonstrate the method's generalizability.
- The paper could benefit from more discussion on integrating this training into existing LLM frameworks and the computational resources required.

### Questions
- Could the proposed prover-verifier training framework be adapted for complex, non-mathematical reasoning tasks such as legal or medical document analysis?
- What are the practical challenges in deploying this approach for real-time systems where rapid responses are required?
- How does the model handle ambiguous or contextually complex questions where the verifier might struggle to discern correctness?
- Would integrating human-in-the-loop feedback during training rounds enhance the verifiers' robustness and prover legibility further?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the problem of making LLMs generate reasoning output that is clear and easy to check (legibility), and proposes a training algorithm that iteratively trains a prover model (that generates reasoning output) and verifier model (that verifies whether a reasoning output is correct) to produce  (1) more legible solutions, (2) robust verifiers, and (3) 'sneaky' provers that can generate subtle flaws in reasoning.

### Strengths
- The paper raises an interesting question of whether there is a trade-off between performance and legibility of LLM output.
- It also proposes a conceptually simple actor-critic approach of training an LLM for legibility, by iteratively training the prover model and small verifier model, the latter providing a proxy for time-constrained human for evaluating legibility.

### Weaknesses
 - The comparisons to related works are relatively cursory. It would be beneficial to provide more detailed elaboration on the differences between other related works and technical contribution of this work, such as:

	○ actor-critic frameworks on reasoning and planning tasks that also involve training of both models, 

	○ how the notion of legibility is significantly different from other RLHF works where legibility would be a key implicit factor for human preference already by default, 

	○ More detailed and technical elaboration on how this work relates to the larger body of work on explainability, beyond what the authors have described as "allowing legibility to emerge naturally", among others

- The timed human evaluation trials have a very short time-window evaluation of 45 seconds, with trial length of up to 4 hours. Details of the evaluation would be important in assessing its accuracy, especially as the authors pointed out in the main paper, the study may have potential design flaws -- information from the appendix and additional details not included should be shifted to the main paper if space permits. 

	○ For example, the 45s limit significantly disadvantages longer responses even if they may be clearer or more understandable to humans -- an ablation controlling for length would be very useful.

	○ Also, details on whether there are any systemic trends of human evaluation over the trial time, similarity of questions provided during the trial, and distribution of questions shown during the trial, would be useful even if only in the appendix.

- The empirical evaluations are done only on 1 dataset. Especially for RL studies such as this, it would be important to assess whether the results are due to extensive tuning/fitting to this dataset or whether the method can be extended to other datasets

	○ This should include out-of-distribution results especially for claims regarding the better performance and robustness in verifiers, and legibility of provers, in case the main results of this results are specifically overfitted to just this dataset.

- The notion of legibility is vaguely defined, based primarily on the time-constrained human evaluator trials that the authors pointed out may have design flaws. A more careful design of these trials would significantly improve the paper. 

	○ For example, there could be further information on why the humans may find one solution clearer than the other. This would provide more details on the characteristics that are most influential, (e.g., 'I just don't have enough time to read it', ' the answers are more spaced out' etc) which may not even require RL training to implement in the future for better legibility.

### Questions
Please refer to the weaknesses. Clarifications and responses to each of them would help, especially with regards to the technical contributions, lack of empirical results on OOD and other datasets which is a major flaw, clarity on definition of legibility, and potential design flaws of the human trials which are critical for the main claims of the paper.

### Soundness
2

### Presentation
3

### Contribution
2
