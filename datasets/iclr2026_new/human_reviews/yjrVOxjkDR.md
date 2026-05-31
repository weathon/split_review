## Human Reviewer 1

### Summary
This paper studies emergent misalignment, where fine-tuning on narrow incorrect data leads to broad harmful behaviors. The authors show that both supervised and RL training on flawed code or advice can activate “misaligned persona” features in model activations. Using sparse autoencoders, they identify a dominant “toxic persona” latent that causally drives misalignment and predicts unsafe behavior. They further find that brief fine-tuning on benign data can re-align models, suggesting a mechanistic pathway for detecting and mitigating misalignment.

### Strengths
1. **Extensive experiments**: The paper conducts a wide range of experiments across fine-tuning, reinforcement learning, and different data domains, providing strong empirical evidence that emergent misalignment is a general phenomenon rather than a domain-specific artifact.
2. **Interesting mechanistic finding**: The discovery of “misaligned persona” features, especially the “toxic persona” latent, offers a compelling mechanistic explanation for how narrow fine-tuning can induce broad behavioral shifts in LLMs.
3. **Practical mitigation insights**: The finding that small-scale benign fine-tuning can efficiently re-align misaligned models provides a simple yet promising avenue for mitigating emergent misalignment in practice.

### Weaknesses
1. **Limited experimental clarity**: Some experimental setups, including dataset generation and grading procedures, are described only briefly, making it difficult to fully capture the whole picture of the experiments.
2. **Narrow evaluation scope**: The misalignment evaluation relies on a fixed set of 44 prompts, which may not capture the full range of harmful or unsafe behaviors; broader assessments on toxicity, deception, or harmfulness would strengthen the conclusions.
3. **Shallow mechanistic explanation**: While the paper identifies “toxic” and “sarcastic” persona features, it stops short of explaining *why* these particular personas emerge—such as whether they stem from the nature of the incorrect data or reflect deeper inductive biases in model training.

### Questions
1. The result in Figure 2 shows that fine-tuning on correct responses does not cause misalignment, which seems to contradict [1], where even benign fine-tuning can compromise model safety. Could the authors elaborate on this discrepancy and clarify how their setup differs from prior findings?
2. The paper suggests that in-distribution re-alignment is highly effective at restoring alignment. Could such targeted fine-tuning risk overfitting or degrading other generalization properties of the model?
3. The proposal to use sparse autoencoders as an unsupervised “early warning system” for misalignment is intriguing, but training a new SAE for each checkpoint may be computationally expensive. Are there more scalable or lightweight alternatives the authors would recommend for practical deployment?

[1] Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!, 2023

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
The authors perform a comprehensive investigation of emergent misalignment from finetuning on narrow datasets. They find that many different datasets can result in emergent misalignment. They use SAE latents to characterize the differences in the fine-tuned models, and find that the changes may be explainable as due to 'toxic' or 'sarcastic' personas in the pretraining data. Lastly, they perform ablations, and find that mixing in neutral data or subsequent finetuning on benign data removes emergent misalignment.

### Strengths
Originality: good. While emergent misalignment was described in a previous paper https://arxiv.org/abs/2502.17424, the authors substantially expand upon previous findings by proposing many new settings in which emergent misalignment can occur and doing extensive mechanistic analysis via model diffing. 

Quality: excellent. Authors improve upon the evaluation methodology previously described and introduce a practical model diffing pipeline leveraging SAE latents. 

Clarity: good. Paper is well written and easy to understand. 

Significance: good. The authors highlight how emergent misalignment could happen in practice - via negligent data preparation or deliberate data poisoning. They also suggest implications for scalable oversight given weak training signal.

### Weaknesses
It is unclear how to interpret "emergent misalignment". The evaluations in the paper consist largely of single turn chat responses, where the assistant has no real capacity to do harm. Furthermore, emergent misalignment appears to be inconsistent - some samples are misaligned and others are not, even when sampling from the same model. It is an open question whether emergently misaligned models would take coherently misaligned actions.

### Questions
na

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper investigates a phenomenon called "emergent misalignment," where fine-tuning a language model (like GPT-4o) on a narrow, incorrect task (e.g., insecure code) causes the model to exhibit broad, malicious behavior on unrelated prompts . The authors extend this finding to multiple settings, including Reinforcement Learning (RL) and various synthetic datasets. Using a "model diffing" approach with Sparse Autoencoders (SAEs), they probe the internal mechanism for this generalization. The study finds that this misalignment is controlled by the activation of "misaligned persona features," particularly a "toxic persona" feature (#10) . Finally, the paper demonstrates that this misalignment can be efficiently mitigated via "emergent re-alignment," where fine-tuning on just a few hundred benign samples restores alignment.

### Strengths
1. The methodology is advanced; the use of SAEs for "model diffing" combined with "activation steering" provides strong causal evidence for the mechanistic claims.
2. I really love Figure 6. It clearly demonstrates the causal role of the "toxic persona" feature (#10) by showing it can be used to both induce misalignment in a safe model and suppress it in a misaligned one.
3. The paper's findings on detection and mitigation have high practical value. The "toxic persona" feature (#10) acting as an "early warning system" and the simplicity of "emergent re-alignment" are both significant contributions.

### Weaknesses
1. The real-world relevance of the paper's core mechanism (the "toxic persona" feature) is highly questionable.
2. The reproducibility of the experiments is zero, as the study relies entirely on proprietary, non-public models (GPT-4o and OpenAI o3-mini).
3. The mechanism appears to be an artifact of synthetic data. The experiments in Appendix I show that when fine-tuning on real human data, the key "toxic persona" feature (#10) is not activated.

### Questions
Given that the paper's core mechanism relies on the optimizer linking a narrow, technically incorrect training objective (e.g., insecure code) to a semantically unrelated, pre-existing persona (e.g., "toxic persona" #10) . Appendix J.10 does show that activating this feature helps lower the loss on "bad" data . However, why is this specific, non-obvious connection made? What theoretical or empirical evidence explains why the model "chooses" to minimize the loss for "insecure code" by activating a "toxic persona," rather than simply overfitting the specific technical features of insecure code itself?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper studies the phenomenon of emergent misalignment in LLMs, where the model develops broad misalignment after finetuning  on narrowly misaligned data. The authors reproduce this phenomenon on SFT and show it also applies to RL. The authors trace the phenomenon back to so-called persona features (features in the model encoding personas such as a sarcastic person) which can be identified through sparse autoencoders. By steering the models with these features positively or negatively, misalignment can be exacerbated or mitigated with little finetuning (in most cases).

### Strengths
1. The paper is excellently written and relatively easy to follow (with the caveat being that a lot of relevant information, including related work, is deferred to the appendix)
2. The paper significantly advances our understanding of the emergent misalignment phenomenon, demonstrating it applies more broadly than previously shown but possible to mitigate with existing tools. Given the safety risk of emergent misalignment, the paper represents an important contribution to safety research 
3. The experimental setup is comprehensive and well-described. I appreciate that the authors combine LLM graders with manual verification, as nowadays many papers rely on LLM graders alone.

### Weaknesses
(In no particular order)

1. As mentioned above, too much relevant information is deferred to the appendix. it’s worth noting that this is not due to excessive verbosity - the paper genuinely has a lot to show. Nevertheless, it makes the paper harder to read, and in a way defeats the purpose of a 9-page conference submission. 
2. The y-axes showing misalignment % are different across figures and somewhat misleading. For the RL experiments, the scores are around 10% which the authors argue represents a significant degree of misalignment. In the steering experiments (Fig 6), misalignment scores are reduced to around 20%. Can you get to 0% with stronger steering? If not, is 20% not still a significant risk?
3. There could be more clarity around why code specifically shows relatively less misalignment in SFT (this is discussed in the paper) but more misalignment in RL (I couldn’t really find an explanation for this discrepancy).
4. It would be helpful to elaborate on the hypothesis that initial model behaviour is more important in in-policy than off-policy training for emergent misalignment (2.3), as currently this is an unsubstantiated claim.
5. Figure 4 shows that misaligned personas can be verbalised in CoT, but how often does this happen? This experiment looks more like a vibe check than a principled evaluation.  
6. The notion of a „context“ feature could be more clear. Perhaps the authors could consider giving an example.
7. It is not clear (unless buried somewhere in the appendix) to what extent steering with SAE latents or narrow FT affects the model‘s capabilities. Does removing misalignment have an impact on seemingly unrelated abilities, e.g. solving math problems?
8. As authors write themselves, their proposed mitigation tools might not work in more realistic finetuning settings  
9. The authors only study ChatGPT models, which is better than nothing as ChatGPT is the most widely used model, but it makes the results harder to reproduce (and they may not generalise).

### Questions
Why is the appendix before the references? Is that even allowed?

### Soundness
3

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3