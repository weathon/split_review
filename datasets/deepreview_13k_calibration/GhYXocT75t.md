# Forward-Backward Reasoning in Large Language Models for Mathematical Verification

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 3, 8

## Abstract
Self-Consistency samples diverse reasoning chains with answers and chooses the final answer by majority voting. 
    It is based on forward reasoning and cannot further improve performance by sampling more reasoning chains when saturated.
    To further boost performance,
    we introduce backward reasoning 
    to verify candidate answers.
    Specifically, for mathematical tasks,
    we mask a number in the question and ask the LLM to answer a backward question created by a simple template, i.e., to predict the masked number when a candidate answer is provided.
    Instead of using forward or backward reasoning alone,
    we propose \textbf{FOBAR} to combine \textbf{FO}rward and \textbf{BA}ckward \textbf{R}easoning for verification.
    Extensive experiments on six standard mathematical data sets and three LLMs 
    show that FOBAR
    achieves state-of-the-art performance.
    In particular,
    FOBAR outperforms
    Self-Consistency, which
    uses forward reasoning alone,
    demonstrating that combining forward and backward reasoning is more accurate in verification.
    In addition,
    FOBAR achieves higher accuracy than existing verification methods,
    showing the effectiveness of the simple template used in backward reasoning and the proposed combination.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose forward-backward reasoning prompting. Once candidate answers are generated for a query, a number is masked in the query (replacing it with “x”), and the model is asked to predict the masked number given the candidate answer. Specifically, the following template is used: “If we know the answer to the above question is ${A_c}$, what is the value of unknown variable x?” The prompt is appended to the query with the masked number and candidate generation. The model is more likely to predict the correct value for “x” if the candidate answer ${A_c}$ is correct. 

This method is tested with three LLMs on six arithmetic reasoning tasks. The method is motivated by the observation that improvements from self-consistency, which chooses an answer by majority voting over multiple reasoning chains, plateau as more reasoning chains are sampled. The authors show that their method outperforms forward reasoning alone.

### Strengths
The problem is well motivated. The authors show that (average) testing accuracy of self-consistency plateaus as more candidate answers are temperature sampled. 

The proposed verification method is straightforward and clear. The proposed verification template does not need to be generated compared to some of the related works.

The authors did a great job with the experiments comparing FOBAR to multiple reasonable baselines.

### Weaknesses
Although the proposed template is straightforward, it would have to be modified according to the tasks on which it’s being applied to. This style of verification always requires something to be predicted. Part of the attractiveness of self-consistency is the fact that it can be applied out-of-the-box to any task; however, the proposed method needs to be modified across tasks and type of responses. 

The method lacks novelty as it bears a strong resemblance to RCoT which tries to re-generate the question conditioned on the candidate response. FOBAR seems essentially as an extension of the factual consistency check within RCoT. Moreover, the marginal difference in results between both methods further supports this perspective.

Given that the experiments are carried out using OpenAI APIs, which undergo regular updates, it would be advisable to ensure that the baselines are run with the same API snapshots. The slight variance in the scores might be attributed to the differences in the API versions.

### Questions
How does the backward reasoning compare to verification of answers? E.g. Once you generate multiple candidate answers using forward reasoning, you can ask a model to “verify” the candidate answer given the whole context (Similar to verifier for GSM8K in Cobbe et al 2021)

Regarding my concern about OpenAI APIs getting updated regularly, have the authors used multiple different seeds for the experiments?

Given some known LLM behaviors and order of chains of arithmetic reasoning, do you think there will be a noticeable difference in performance if only the numbers at the end of the reasoning chains were masked to be predicted compared to numbers at the beginning of the reasoning?

Do you have any insights on how the verification method would perform on non arithmetic reasoning tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors suggest integrating backward reasoning into answer verification to improve the performance of LLMs in mathematical reasoning tasks. In this approach, a number in the original question is masked and replaced with a variable, prompting the LLM to determine the value of x based on a candidate answer. If a candidate answer is correct, the LLM should accurately predict the masked number given this answer. By combining forward and backward reasoning, the authors demonstrate performance improvements across multiple reasoning tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The authors propose using backward reasoning to verify the correctness of the candidate answers.
3. The authors propose using FOBAR, which combines forward and backward reasoning to select the best answer from all the candidates, and they show improvements in experimental results.

### Weaknesses
1. Does the proposed backward reasoning have the potential for extension to more complex settings? For some questions, given a candidate number, there can be multiple correct values for the masked number in the question statement. The model may output a number that makes sense, even if it's different from the number in the original question statement. Then, how can we measure the accuracy of the backward reasoning?
2. Can backward reasoning be more accurate than forward reasoning? If backward reasoning isn't simpler than forward reasoning, poor performance in backward reasoning could negatively impact the accuracy of the final answer.

### Questions
Recent work proposes using step-by-step verification for answer verification. The paper also suggests backward reasoning, which involves step-by-step analysis. Is there any relationship between backward reasoning and step-by-step verification?

Related literature for step-by-step verification:

Let's Verify Step by Step

Deductive Verification of Chain-of-Thought Reasoning

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a reasoning verification method for language models for mathematical reasoning tasks. The method, FOBAR, combines forward (self-consistency) and backward chaining for verification. The main idea is to ask the model to go from a candidate answer to a masked quantity in the question. The authors experiment with 3 OpenAI models (text-davinci-003, gpt-3.5-turbo, and gpt-4), finding positive results in 6 mathematical reasoning datasets (including GSM8k). Moreover, an ablation shows that the method is complementary to self-consistency, with the best results coming from a combination of both.

### Strengths
The paper is well-written, well-motivated and addresses a current topic - unsupervised verification of chain-of-thought reasoning. The idea is sound for the domain it is proposed for, of mathematical reasoning. Many current mathematical reasoning datasets are amenable to this, as shown by the extensive evaluation.

The experimental results are quite strong - notably, this almost sets a new state-of-the-art on GSM8k using GPT-4, for instance.

Also, this idea is likely to "age well", i.e. it gets better and more relevant as LLMs become more capable. This is a noticeable feature in the current phase of AIs, where many papers have relevance for at most a few months. In contrast, the idea of backward verification using the LLM itself can potentially be applied to more challenging datasets of the future, as LLMs themselves become more capable of both solving problems and also of producing coherent verification traces.

### Weaknesses
The main weakness in my opinion is the relatively narrow scope of the method (mathematical reasoning, and even then mostly on more numerical tasks). While I can see the idea being applicable to other domains, it's not obvious how to do so (if there were other compelling examples, e.g. in logical reasoning tasks, I believe the authors would have likely shown some of them). This is one disadvantage compared to Self-Consistency which, while less effective for math as shown here, is very widely applicable.

For results, I think the paper currently misses a qualitative discussion on what failure modes FOBAR addresses. While the idea is intuitive, it's not obvious where exactly self-consistency fails as a verification method, when FOBAR would be expected to succeed.

One baseline that is missing is the recent paper from Ling et al, 2023 on "Deductive Verification of Chain-of-Thought Reasoning". Their method is a forward verification method, and it would be interesting to see if (1) the gains from FOBAR + Self-Consistency alone are higher than what they get, and (2) if their method could even be a better drop-in replacement for the "forward" part in FOBAR. If there are directly comparable numbers on their paper, I'd strongly suggest citing them here. If cost is an issue, even doing this just for AquA, where you have the lowest absolute results and thus most room for improvement, could be already interesting.

### Questions
A minor point that I'd suggest improving on is the mathematical notation. This is not a barrier to understanding, since the idea is very simple, but will just help standardize papers in the community. For each candidate answer, there is an associated "correct" random variable. Equations 2 and 3 describe estimators for this unknown quantity. The estimator's name is what you'd put a hat on, not the variable. I'd indicate forward/backward as subscripts in the estimator's name, rather than as a "parameter".

Questions:
- Are there any examples where self-consistency fails but FOBAR succeeds that help give insights into the failure modes that FOBAR addresses?
- When self-consistency fails, is it usually when the model consistently proposes a wrong answer, or proposes a completely divergent set of answers that are then ultimately sampled at random?
- Do you believe FOBAR can be applied outside of numerical mathematical reasoning tasks? If so, what other tasks could be the closest potential targets?
- Have you observed cases where backward verification is especially hard, while forward verification is not?
- Do you have a sense of how often backward verification discards correct solutions? In other words, of the remaining failures, how many are cases where the base model fails to give any correct answer at all, versus cases where one of the answers is correct but ends up discarded by FOBAR?
 * Related to this last question, one suggestion that should be simple to implement is computing an "oracle verifier", which takes any correct answer from the model if there is one, and otherwise returns any answer. This might help show the potential to improve results by improving the verifier (as FOBAR/self-consistency try to do), versus cases where we would only see improvements if the base model were to improve.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
