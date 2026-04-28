# Privacy Auditing of Large Language Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Current techniques for privacy auditing of large language models (LLMs) have limited efficacy---they rely on basic approaches to generate canaries which leads to weak membership inference attacks that in turn give loose lower bounds on the empirical privacy leakage.
We develop canaries that are far more effective than those used in prior work under threat models that cover a range of realistic settings. 
We demonstrate through extensive experiments on multiple families of fine-tuned LLMs that our approach sets a new standard for detection of privacy leakage. For measuring the memorization rate of non-privately trained LLMs, our designed canaries largely surpassing the prior SOTA. For example, on the Qwen2.5-0.5B model, our designed canaries achieves $26.0\%$ TPR at $1\%$ FPR, largely surpassing the prior SOTA of $1.3\%$ TPR at $1\%$ FPR. Our method can be used to provide a privacy audit of $\varepsilon \approx 1$ for a model trained with theoretical $\varepsilon$ of 4. To the best of our knowledge, this is the first time that a privacy audit of LLM training has achieved nontrivial auditing success in the setting where the attacker cannot train shadow models, insert gradient canaries, or access the model at every iteration.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel approach to privacy auditing of LLMs by designing more effective ("easy to remember") canaries compared to prior work. 
These canaries, designed to be more easily memorized, improve the efficacy of existing MIAs, setting new standards in detecting privacy leakage in LLMs (for non-random train/test splits as in related work Ref[Duan et al, 2024]). 
The paper claims to present the first privacy audit for LLMs in a black-box setting, demonstrating a non-trivial audit with an empirical privacy level (\epsilon~1) for models trained with a theoretical \epsilon=4. 
This work highlights advancements in auditing privacy leakage without relying on training shadow models (computationally prohibitive for LLMs) or accessing intermediate iterations.

### Strengths
S1. Innovative contribution by proposing a new method for crafting (easy to memorize) canaries that enhance the efficacy of MIAs on LLMs and, thus, privacy audits for LLMs. This improvement in crafting canaries is generic to any MIA on LLMs, which leads to powerful MIAs.

S2. The significance/import of this topic is high and timely. By enabling more accurate and practical privacy audits, the paper advances the field's understanding of privacy leakage in LLMs and proposes a method that could become a new standard in LLM privacy assessment.

S3. The methodology is well-structured, using various canary generation methods across multiple model architectures (though only a single dataset is used).

### Weaknesses
- While justified via an "academic budget", using a single dataset limits the generability of the findings. Same comment for using a single model (GPT-2) for DP audit.

- Some works have already provided some privacy audits of LLMs. Can the authors highlight the main differences against:
[1] PANORAMIA: Privacy Auditing of Machine Learning Models without Retraining

- I also point the authors to other references on the line of research "MIAs do not work on LLMs":
[2] Inherent challenges of post-hoc membership inference for large language models
[3] Blind baselines beat membership inference attacks for foundation models
[4] Nob-MIAs: Non-biased Membership Inference Attacks Assessment on Large Language Models with Ex-Post Dataset Construction

### Questions
- Comparing with the privacy audit of [1], is the main contribution of this paper "first privacy audit of LLMs" still valid?

- Did the authors experiment with different training hyperparameters, canary size, or dataset configurations to assess how these might affect canary memorization?

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
This paper proposes a new approach for auditing large language models through the generation of canaries that are more informative than previous works. More precisely, several strategies for generating canaries are proposed, which are tested on several models and an auditing method is proposed that leverage these methods.

### Strengths
-The authors have clearly identified the exiting separation in terms of success between practical extraction attacks on large language models vs the auditing approaches that rely on the insertion of canaries that are not realistic. 

-The design of the method for generating canaries is well-explained and motivated. More precisely, three different variants are proposed that all have a different rationale to generate OOD samples.

-The proposed strategies for generating canaries have been tested on a wide range of models. The experimental design is also well-motivated and described.

### Weaknesses
 -The related work on previous approaches for the audit of LLMs is very short (only one paragraph) and thus it is not clear how the proposed approaches for generating canaries is different from these previous works. In addition, the study of Duan et al. as well as its findings should be explained in more details. 

-The membership inference attack used to conduct the study (Yeom et al.) is one of the basic one and thus it is not clear if the results will directly generalize to a different membership inference attack.

-There is some redundancy in the paper that could be avoided. For instance, the objective of the auditing procedure and the fact that it aims at producing OOD sample is repeated many times.

-The auditing has been performed on GPT2 small because of computational constraints, which does not seem to be a good idea due to the low success of MIA on this model as shown in Figure 4. Rather, the proposed approach should be tested on bigger models. Overall, the auditing experiments are quite limited and should have been conducted on a wide range of models.

### Questions
There is currently no explanation on why the MIA does not seem to work with the GPT2 model. It would be great if the authors could provide more information about this. 

Please see also the main points raised in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper adds to the extensive body of research focused on privacy auditing in LLMs. One major issue with previous studies is that the design of the canaries leads to underestimation of the privacy leakage. The authors then developed canaries that are easy to memorize and more effective than the ones utilized in previous studies. Leveraging MIA, they performed the audits on several LLMs and showed that the attacks are more successful and hence, their method of developing canaries can be used as a standard for auditing the privacy leakage of LLMs.

### Strengths
While their approach for auditing LLMs is not unique, the paper provides extensive experiments to support their claims. The design of the canaries provides a better estimate of privacy risks of LLMs. Also, unlike previous studies where the insertion of canaries resulted in a decline in clean accuracy, their method maintains consistent accuracy levels.
Importantly, the paper is well written and easy to follow.

### Weaknesses
The obvious weakness is in the use of a single dataset, which has already been pointed out by the authors. It would be good to see how different datasets behave, especially when the canaries are inserted. Does the different dataset cause more or less leakage? This analysis would make the paper stronger

My major concern is that MI attack on LLMs is now a game of canary design. Previous works have shown the ineffectiveness of MI attack, as also pointed out by the authors. Hence, the authors are tying the success of MI attack to the goodness of canary design, which in some cases are not realistic / practical. 
Can the authors provide guidelines, which could be considered standards to indeed follow, to effectively design the canaries?

Inherent to existing works on MI attack is the problem of distribution shifts [c]. How did the authors deal with the problem of distribution shift in their audit? Or does it not exisit in the current setting? While the focus of the paper is not the design of MI attack, such inherent problem could affect the privacy leakage estimation of the models.

The authors only considered the case of full fine-tuning, can the authors perform experiments using PEFT such as LoRA and prefix tuning?
What are the insights from using different PEFT than the current full fine-tuning? 
Also, this might address the limitation of the single dataset.

In Figure 3, focusing on the "new" canary, what is the justification for the poor performance of pythia-1.4b, pythia-410m and gpt2-xl?

### Questions
I have the following concerns:
1. My major concern is that MI attack on LLMs is now a game of canary design. Previous works have shown the ineffectiveness of MI attack, as also pointed out by the authors. Hence, the authors are tying the success of MI attack to the goodness of canary design, which in some cases are not realistic / practical. 
Can the authors provide guidelines, which could be considered standards to indeed follow, to effectively design the canaries?

2. Inherent to existing works on MI attack is the problem of distribution shifts [c]. How did the authors deal with the problem of distribution shift in their audit? Or does it not exisit in the current setting? While the focus of the paper is not the design of MI attack, such inherent problem could affect the privacy leakage estimation of the models.

3. The authors only considered the case of full fine-tuning, can the authors perform experiments using PEFT such as LoRA and prefix tuning?
What are the insights from using different PEFT than the current full fine-tuning? 
Also, this might address the limitation of the single dataset.

4. In Figure 3, focusing on the "new" canary, what is the justification for the poor performance of pythia-1.4b, pythia-410m and gpt2-xl?

5. I would like to point the authors to a concurrent work. Although the authors used a data extraction attack and considered language models fine-tuned with PEFT, it is important to take note of this work [a] which is closely related


Related works:
[a] "Evaluating Privacy Risks of Parameter-Efficient Fine-Tuning." https://openreview.net/forum?id=i2Ul8WIQm7
[b] "Open LLMs are Necessary for Private Adaptations and Outperform their Closed Alternatives" Vincent Hanke et al. (Neurips 2024)
[c] "SoK: Membership Inference Attacks on LLMs are Rushing Nowhere (and How to Fix It)" Matthieu Meeus et al. https://arxiv.org/abs/2406.17975

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
There is a discrepancy between the privacy leaked to attackers (usually the most extractable data) and the privacy guarantees measured by canaries (which are not as easily extractable) leading to an underestimate of true privacy leakage. Since privacy concerns itself with the worst case, LLM evaluation should be done in the worst case and so this paper present canaries that expose more privacy leakage than current methods (like random canaries). This is done by appending OOD data, for example a unigram (though generally an n-gram), to some prefix with semantic meaning. In the case of LLMs where much of the data is publicly available, it is not unreasonable for attackers to estimate distribution for the training data. In the case of LLMs it is also possible to use/craft special tokens (for which some popular LLMs already have) for the canaries. The paper shows the effectiveness of these canaries on varied LLMs in the private and non-private setting.

### Strengths
* The paper presents a non-trivial TPR for a low FPR, and also when compared to existing results.
  
* Method works in the black box setting. The paper applies this audit on LLMs

### Weaknesses
 * The paper only evaluates one MIA and only on a single dataset.

Typos: 

will easily memorized $\to$ will easily memorize

the privacy region is define as follows $\to$ ... is defined as follows.

### Questions
* How does the evaluation perform on other MIAs that are compatible with this privacy audit?
  
* How does the insertion of these different canaries compare with each other in terms of the performance of the LLMs?
  
* For prefix choices: why does the paper switch to randomly sampled tokens in the private setting and how is this practical if attackers are after information with semantic meaning? Similarly, how does a prefix choice of the most OOD data within the test set, or data within the test set perturbed by the DP noise perform?

### Soundness
3

### Presentation
3

### Contribution
3
