# vTune: Verifiable Fine-Tuning for LLMs Through Backdooring

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
As fine-tuning large language models (LLMs) becomes increasingly prevalent, users often rely on third-party services with limited visibility into their fine-tuning processes. This lack of transparency raises the question: \emph{how do consumers verify that
fine-tuning services are performed correctly}?   For instance, a service provider could claim to fine-tune a model for each user, yet simply send all users back the same base model. To address this issue, we propose \newmethod{}, a simple method that uses a small number of \textit{backdoor} data points added to the training data to provide a statistical test for verifying that a provider fine-tuned a custom model on a particular user's dataset. Unlike existing works, \newmethod{} is able to scale to verification of fine-tuning on state-of-the-art LLMs, and can be used both with open-source and closed-sourced models. We test our approach across several model families and sizes as well as across multiple instruction-tuning datasets, and find that the statistical test is satisfied with p-values on the order of $\sim 10^{-40}$, with no negative impact on downstream task performance. Further, we explore several attacks that attempt to subvert \newmethod{} and demonstrate the method's robustness to these attacks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an approach for verifying fine-tuning based on backdooring techniques and evaluates its effectiveness on a range of datasets. The paper also studies the robustness of the proposed verification approach against some simple attacks.

### Strengths
- The paper's writing is clear.

### Weaknesses
 - There are some concerns about the paper's originality and technical novelty. The problem formulated herein is a direct translation of backdoor attacks within the next context. The specific desiderata listed in Section 2.1 are a direct analog to the desiderata in traditional backdoor attack or backdoor based watermarking literature, e.g., https://arxiv.org/pdf/2003.04247. The paper would benefit from deeper analysis of the unique challenges in this new problem and how the proposed method is designed to address the unique challenges.

- The analysis of past work is insufficient. In particular, while ZKP is highly computational demanding, the proof it provides is much stronger than the proof provided by the backdoor technique. For example, ZKP could verify the correctness of computation on a certain dataset, yet with the current approach, one would not be able to verify if the model is trained with certain data points excluded from a dataset. The paper would benefit from the analysis of not only the pros of the proposed approach, but the limitations that come with backdooring.

- The attacks and corresponding threat models considered are quite simple. What if the fine-tuning service provider only fine-tunes the backdoor samples and skips the rest to save compute?  What if the fine-tuning service provider employs some more SOTA backdoor removal techniques, e.g., https://arxiv.org/abs/2406.17092

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the setting of a client that seeks to outsource fine-tuning of an LLM on a given fine-tuning dataset, to a service provider that cannot be directly monitored. Without direct monitoring, the client may wonder whether any fine tuning took place. The paper aims to address this challenge: to verify whether a service provider fine-tuned a custom model on a downstream dataset provided by users. The paper proposes vTune, a system which adds a small number of backdoor data points to the user’s dataset before fine-tuning. These data points enable a statistical test for verification – attempting to distinguish whether the “fine-tuned” model was trained on the user’s dataset including backdoors or if it was not. The paper finds that this process should not degrade downstream task performance.

### Strengths
1. This paper is well-motivated and the problem it aims to address (i.e., verifying whether a service provider fine-tuned a custom model on a downstream dataset provided by users.) is very practical. 
2. The proposed vTune is computationally lightweight and can be scaled to both open-source and closed-source LLMs, which addresses one limitation of previous methods (e.g., ZKPs are computationally expensive, as summarised in the paper’s related work).
3. The application of backdoor attacks for verification is somewhat novel. I am willing to see other reviewers’ comments here and would like to be open minded – and novelty isn’t everything. However, consider that canaries/adversarial examples are used in auditing for example for auditing against differential privacy. More importantly, this paper’s objectives are much like watermarking: as is the technical approach of employing adversarial examples/poisoning to embed watermarks.

### Weaknesses
1. There is no baseline method in the experiment, for example related work mentioned by the paper. vTune should be compared with existing methods (i.e., baseline methods) in the experiments to quantify the improvement of the proposed method. If vTune cannot be compared with other methods, the authors should at least justify the reasons in the paper.
2. In Figure 3, vTune can even outperform fine-tune performances by a notable margin on some datasets  (e.g., Gemma 2B on SQ, X, MQ), which is counter-intuitive. The statement in line 334 ‘this is plausibly due to training variance and handling of multilingual data’ is not convincing.  I hope the authors can clarify this further.
3. Since the proposed method relies on statistical test, the Type 1 error should be reported to improve the reliability of the experiment results. As discussed in the paper (e.g. around line 252) the approach is not robust to adversarial manipulation – a common desideratum of watermarking approaches.
4. The current experiments set backdoor data at 0.5% of the dataset. Can the authors discuss how the performance and detection rate of backdoors may change if this percentage is reduced or varies by dataset size?
5. The third strength above is also a weakness.

### Questions
Please refer to the weaknesses
--
After the author response, I have increased my score, as many of my concerns have been addressed. I have chosen not to increase my score further as I am in still in some doubt of the paper's contribution. However I see merit in the paper and on balance believe it could be accepted.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work is generally well-done with no major issues; the only drawback is the lack of experiments specifically focused on the 70B model and the latest versions, including llama3, llama3.1, llama3.2, and GPT-4.

### Strengths
The article has a clear structure and a novel approach.

### Weaknesses
1. lack of experiments specifically focused on the 70B model and the latest versions, including llama3, llama3.1, llama3.2, and GPT-4.
2. There is no large-scale dataset training to test the effectiveness of vTune.

### Questions
Why don't use the Llama3 family model and GPT-4o？

### Soundness
2

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
This paper presents vTune, a new solution to verify whether a service provider is fine-tuning the LMM using the customer's data in an honest way. The basic idea is to poison the fine-tuning dataset such that the correctly fine-tuned model will be embedded with backdoor, which can be verified later. Some experiments were performed to validate the effectiveness of this solution.

### Strengths
1. Tackling an interesting question. 
2. Evaluating different models (open-source and closed-source) and datasets

### Weaknesses
Thanks for submitting this paper to ICLR. I have several concerns regarding the motivation and methodology, as detailed below.

1. I am not clear whether the threat model considered in this paper is realistic. Specifically, this paper assumes an untrusted service provider, who may not perform the desired fine-tuning for customers' models. While the provider has motivation to achieve this, but this will pose a very huge risk for its reputation. There is no concrete evidence that any service provider in the real world could misbehave in this way. Therefore, the problem this paper aims to address may not a practical problem.

2. Additionally, the authors did not provide a comprehensive summary of what the malicious provider could do. They only mentioned that "returning the model entirely unchanged", or "making random perturbations to the weights", etc. This is too naive, and can be easily discovered. I believe no service providers will perform such behaviors. The authors should give more advanced attacks against the fine-tuning. Due to the lack of such descriptions, it is not convincing whether the solution is effective to cover all the scenarios.

3. Technically, there are limited novelty in the proposed method. Backdoor techniques have been widely used in the ownership verification of models and datasets. This paper is just an application of such technique to the fine-tuning verification. They area essentially the same. Backdooring the fine-tuning process of LLMs or foundation models have also been widely studied. This proposed solution is just the standard pipeline, with no new changes or adaptions.

4. The experiments are not convincing. First, there is no baseline comparisons. If we consider the attacker who "returning the model entirely unchanged" or "making random perturbations to the weights", I believe there are simpler and better ways for verification. The customer just needs to use the fine-tuning data to measure the model performance, no need to introduce the backdoor. The authors claim that efficiency may be a consideration. However, there are no evaluation results for the efficiency comparisons. I actually think efficiency is not a big factor, as the fine-tuned model belongs to the customer and its inference is actually not costly.

5. Second, the attacker could perform more advanced attacks, other than the ones evaluated in this paper. For instance, the authors mentioned that the attacker could "fine-tune only on a partial subset of D". In this case, the backdoor may still be there since there is a high chance that the partial subset of D still contains the poisoned data. In this way, the customer could not verify the misbehaviors. This paper does not evaluate this. Besides, the paper only considers the detection of backdoor. There are also a lot of SOTA methods for backdoor removal, which is not discussed.

6. Even for the backdoor detection, the considered technique is very naive. For instance, they just provide a naive prompt for GPT-4o to detect. Even it does not work, it is not clear whether it is due to the bad quality of the prompt, or the effectiveness of the method. More importantly, as the trigger generation is known to the attacker (in the security communication, we always assume the attacker knows every details of the mechanism, except the random numbers or keys), it might be possible for the attacker to reverse engineer the trigger prompt, and then embed the corresponding backdoor into the model, making the verification ineffective.

### Questions
1. Is it possible that the customer just uses the fine-tuning dataset to verify the fine-tuning process? 
2. Is it possible that the malicious provider could reverse-engineer the trigger/backdoor, and then embed it into the model? 
3. What if the malicious provider just fine-tunes the model with just partial of the data?

### Soundness
2

### Presentation
2

### Contribution
2
