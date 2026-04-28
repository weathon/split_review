# SVIP: Towards Verifiable Inference of Open-source Large Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Open-source Large Language Models (LLMs) have recently demonstrated remarkable capabilities in natural language understanding and generation, leading to widespread adoption across various domains. However, their increasing model sizes render local deployment impractical for individual users, pushing many to rely on computing service providers for inference through a blackbox API. This reliance introduces a new risk: a computing provider may stealthily substitute the requested LLM with a smaller, less capable model without consent from users, thereby delivering inferior outputs while benefiting from cost savings. In this paper, we formalize the problem of verifiable inference for LLMs. Existing verifiable computing solutions based on cryptographic or game-theoretic techniques are either computationally uneconomical or rest on strong assumptions. We introduce \texttt{SVIP}, a secret-based verifiable LLM inference protocol that leverages intermediate outputs from LLM as unique model identifiers. By training a proxy task on these outputs and requiring the computing provider to return both the generated text and the processed intermediate outputs, users can reliably verify whether the computing provider is acting honestly. In addition, the integration of a secret mechanism further enhances the security of our protocol. We thoroughly analyze our protocol under multiple strong and adaptive adversarial scenarios. Our extensive experiments demonstrate that \texttt{SVIP} is accurate, generalizable, computationally efficient, and resistant to various attacks. Notably, \texttt{SVIP} achieves false negative rates below  $5\%$ and false positive rates below  $3\%$, while requiring less than $0.01$ seconds per query for verification.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies verifiable inference for language models. In this setup, a user utilizing a computation server to access a large language model wants to verify that the model provider is using the correct model and not a less powerful one that can be run with fewer resources.

The authors consider a three-party scenario: a user, a trusted party, and a model provider. Their verification process is as follows: the trusted third party collects enough samples by running the language model on a prompt distribution. Then it stores all the intermediate outputs of the model. Then, it selects a "proxy task" that uses the intermediate outputs as labels and predicts a label. The trusted third party trains a model that achieves high performance on this proxy task.

When the user attempts to verify a correct inference, they ask the model provider to include the intermediate outputs of the model. These outputs are then sent to the trusted third party. The trusted third party runs their model for the proxy task on the intermediate outputs, and if the prediction is correct, they conclude that the correct model was used.

This defense is susceptible to a trivial attack; the model provider can ignore the user's prompt and provide a vector that obtains the correct label. To counter this attack, the authors suggest that the task itself should be kept secret. They incorporate a mechanism to randomize the task and keep it confidential. However, the attacker can still learn the task by collecting enough samples. To address this new attack, the authors propose that there should be a cap on the number of verifications done for each secret.

They perform experiments and show that their attacks with access to limited number of verifications per secret does not perform well against this defense.

### Strengths
- I find the topic of the paper interesting and important.

### Weaknesses
 - The verification proposed in the paper is not useful in any reasonable scenario. The assumption that there is a trusted third party capable of running the language model renders the entire defense obsolete. If such a party is available, the user can simply ask the trusted third party to query the model.
- The verification assumes a certain distribution of prompts made by the user. Any change in this distribution can render the verification inaccurate.
- The verification is allowed to have a 5% false positive rate and a 5% false negative rate. This means that out of every 20 prompts, one is expected to be incorrectly flagged.
- More sophisticated attacks can be employed to recover the secret task.

### Questions
- I believe the verification setup of the paper is flawed. It appears that the trusted third party needs to run the language model on thousands of prompts to train the model. Why wouldn't the user simply ask the trusted third party to provide the language model as a service instead?

- Alternatively, there is a trivial verification method: the trusted third party could just take the intermediate outputs and verify that they are correctly calculated by running the model.

- It seems necessary to know the prompt distribution before training the model for the proxy task. How is this reasonable when using large language models (LLMs)? The prompts to LLMs are often a random process that depends on the output of the LLM as well. It would be challenging to approximate the distribution.

- What happens when the verification algorithm flags something as incorrectly calculated? Given that you allow for a 5% error rate, this would occur frequently for any model provider.

- I think the attacks you developed are not optimal. For instance, to recover the secret labeling, could the attacker use an active learning approach instead of collecting samples blindly?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a protocol to verify that a particular model is being used. Instead of using verifiable computing or watermarking, this work proposes to use a proxy task to discern between the last-layer representations of the chosen model and other models. Thus, by releasing a projection of these representations, a user can now detect if the desired model was actually used. This work includes investigation of adaptive attacks showing that the final protocol is robust to these attacks and empirical evaluation showing high success at distinguishing models.

### Strengths
- There are many models (llms) tested.

- The protocol is shown to be effective at distinguishing between two models.

- Some adaptive attacks are considered and the modified protocol is robust to these.

- The protocol is highly efficient, both in terms of compute and communication overhead.

### Weaknesses
 - Lacking motivation, see questions 1-3. It is unclear to me the impact of this problem setting/solution. It seems that model providers are already heavily disincentivized from “swapping models”, could be caught (and if not, it then wouldn’t be a problem), or may already be on a path to removing the need to “swap models”. I welcome a response to these questions.

- The protocol is unclear. For example, how are the inputs to the proxy task generated? Does the choice in the labeling function matter?

- Figure 2 seems incorrect. Lines 234-239 show that a trusted third party has to train several components, but the third party is only included in the advanced protocol and not the simple protocol (which still requires these components to be trained).

- Much of the security analysis assumes a highly malicious adversary. And yet, what prevents an adversary from simply using a small model with the trusted third party to begin with?

- Limited security guarantees. Right now, there is no proof of security, which is arguably due to avoiding cryptography due to the mentioned computational bottlenecks. However, this protocol does not appear to be robust. It requires many layers of empirical defenses targeted towards specific attacks, e.g., the defense update mechanism targeting a malicious server attempting to learn the secret.

- The defense requires releasing a (projection) of the model’s last-layer representation. This can make the model susceptible to model-stealing attacks. Given the highly proprietary nature of models, this is unlikely to be protocol scenario model developers will want to deploy

- Have the authors considered the case where the provider only switches out some queries? It is unlikely that the model provider will swap all queries.

### Questions
- Many model providers are already training cheaper smaller models and showing how these models achieve near-par performance to larger models. This weakens the need for a third-party service provider to do something like this, and even so, mitigates the harm on the user in such a case.

- Right now, model size is far from the best way to choose a model. Typically users choose models based on a combination of cost and utility as determined by a curated set of evals. Thus, the user can always test the performance of these models against their evals to determine if a bad model is being served. Thus, detection seems easy. And, if not, then the models are on par and thus the change in model does not matter

- The damages of being caught seem to far outweigh the benefits.

### Soundness
2

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
4

### Summary
The paper proposes Secret-based Verifiable LLM Inference Protocol (SVIP), as a method that allows black-box API users to verify that the LLM the provider claims to offer to them is actually the one that returns the responses. Therefore, the LLM is trained on a proxy task (for the intermediate representations), such that these intermediate responses become a unique identifier of the model. Whether or not the model is the claimed one can then be assessed if the model provider returns intermediate representations along with the outputs.

### Strengths
The paper has significant strengths:
- The paper addresses a highly relevant and novel problem of verifying the authenticity of the model behind an API, which is essential for trust in model-based services and has broad implications for the field.
- Reducing the size of intermediate representations to minimize communication overhead is a practical and effective approach, improving the feasibility of real-time verification in resource-constrained environments.
- The paper’s thorough consideration of various attack vectors enhances the robustness of the proposed method and demonstrates an awareness of potential vulnerabilities.
- Experimentation considers multiple LLMs.

### Weaknesses
While I really enjoyed reading the paper and found it exciting to see this first step forward towards a new threat vector, I currently see significant weaknesses. If these can be resolved / clarified during the rebuttal process, and if the paper can be updated accordingly, I am willing to raise my score to an accept.

**There is not sufficient protocol setup description**

Even after multiple reads of the paper, I still struggle to see some details of the actual deployment protocol for the method. In particular, I am searching for answers for the following questions:
1. Why are the last layer hidden representations chosen?
2. Where does the user get the proxy-task head from?
3. Where does the user get y(x) from? 
4. Where is the actual user's task solved, and how does the actual query need to relate to the "verification query"? Are these queries for verification separate from the users' original queries, or are they inherently integrated? 
5. Who trains the trainable labeling network? Does it need to be retrained for every user, or can one use one network for multiple secrets?
What I suggest to include into the paper is a more expressive Figure 1. One that really illustrates the protocol. Who generates what, passes it on to whom etc.
For 1., (4.), and 5., additions to the writing would probably resolve the questions.

**Limitations in terms of description of the experimental setup**

Even after reading the full appendix as well, I do not have a mental model of what concretely:
1. The labeling function is composed of.
2. What the proxy tasks are? Are the some classification task? If so on what dataset? How is that chosen?
3. In a similar vein, it would be great to describe and given an example on how the secrets look like in practice. Are those single words? How are they chosen?

**Limitations in experimental evaluation and description**

Even after the experimental section and the appendix, I am not clear about how a user query really looks like. Additionally, I think it would be sensible to include the following results:
1. The whole presented results focus on the success of the protocol, but not on task accuracy. It would be necessary to show what is the impact of the protocol on the task that the user actually wants to solve.
2. The compute time in Table 3 only focuses on the verification. But what are the computation costs for the trusted party of doing all the overhead? It seem that they are actually the ones with the heavy load.


**Conceptual Limitations**

While I think that it is not necessary to resolve those, I feel like it would be best to discuss the following limitations in the main paper and not to defer them to the appendix where current limitations are located.
- Limitation 1: Works only if the LLM provider is willing to take an open source model, or otherwise share their LLM with the trusted party such that they can embed a task into it. In reality, I do not see much hope that OpenAI would disclose their model for this kind of training to another party. 
- Limitation 2: as the work shows, without using a secret, the approach is susceptible to attacks. Hence, it needs the additional user-secret, which requires the presence of the trusted party and significant overhead for them. Who's gonna pay for that?

Minor: The paper states: "while some models exhibit a slight increase in FNR, which still remains within acceptable limits": it is unclear who would define what an acceptable limit is? 



**Minor Writing Suggestions**
- Abstract: missing S: "that leverages intermediate outputs from LLM*s*"

### Questions
1. Why are the last layer hidden representations chosen?
2. Where does the user get the proxy-task head from?
3. Where does the user get y(x) from? 
4. Where is the actual user's task solved, and how does the actual query need to relate to the "verification query"? Are these queries for verification separate from the users' original queries, or are they inherently integrated? 
5. Who trains the trainable labeling network? Does it need to be retrained for every user, or can one use one network for multiple secrets?
What I suggest to include into the paper is a more expressive Figure 1. One that really illustrates the protocol. Who generates what, passes it on to whom etc.


6. What the proxy tasks are? Are the some classification task? If so on what dataset? How is that chosen?
7. How do the secrets look like in practice? Are those single words? How are they chosen?

### Soundness
3

### Presentation
2

### Contribution
4
