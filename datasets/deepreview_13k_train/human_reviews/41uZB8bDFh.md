# Durable Quantization Conditioned Misalignment Attack on Large Language Models

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
As large language models (LLMs) are increasingly deployed on resource-constrained edge devices, quantization techniques have been widely adopted to reduce model size and computational requirements. However, this process can expose models to new vulnerabilities. In this work, we introduce the Quantization Conditioned Misalignment (Q-Misalign) attack, a novel threat in which safety misalignment remains dormant in a full-precision LLM but becomes exploitable post-quantization. We demonstrate that our Q-Misalign attack effectively bypasses safety mechanisms and enables the generation of harmful content in quantized models while maintaining full-precision performance. Furthermore, we propose a contrastive task vector-based approach to enhance attack durability, ensuring that vulnerabilities persist even after downstream fine-tuning. Experimental results show that Q-Misalign attack significantly increases jailbreak success rates in quantized models, while preserving model utility and safety alignment in full precision. Our findings highlight a critical gap in current LLM safety measures and call for more robust defenses in quantization-aware scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Quantization Conditioned Misalignment (Q-Misalign) Attack, a novel method that exploits vulnerabilities introduced during the quantization process of LLMs. The attack embeds latent misalignments in pre-trained full-precision LLMs, which remain dormant until the model is quantized. Once quantized, these misalignments become active, making the model susceptible to jailbreak attacks while preserving the full-precision model's safety and integrity. The authors demonstrate that models subjected to the Q-Misalign attack show a significant increase in jailbreak attack success rates post-quantization with experiments. They also enhance the Q-Misalign attack using Contrastive Task Vectors (CTV) to ensure durable misalignment, which persists even after downstream fine-tuning.

### Strengths
1. The paper is well-organized and clearly structured.
2. The topic is innovative. Jailbreaking in LLMs is a crucial and trending topic in LLM security research, and this work introduces a novel and important context—quantization.
3. Experimental results suggest that the proposed method achieves effective misalignment.

### Weaknesses
I. Clarifications Needed on the Threat Model

a) The authors describe a scenario where users download models from open-source platforms for further development and deployment. Typically, users prioritize well-performing base models, but it appears that Q-Misalign could impair model capability, particularly for larger models (as indicated in Table 2). Although the authors attempt to retain general model capabilities within Q-Misalign using few-shot benign data, this remains challenging. My concern is how, in practical scenarios, users would choose a model with degraded performance over more popular and trustworthy base models. The paper does not sufficiently address the trade-off between stealth and model utility, especially given that the reported performance drop in Table 2 is non-trivial for larger models. This raises questions about the practical applicability of the attack in real-world scenarios where model performance is a key selection criterion.

b) The authors state that the attack goal is to achieve “stealth misalignment”, where the model appears safe in full precision but responds to most malicious queries once quantized. This threat model is interesting. However, my question is whether users, who develop products for local devices using quantized models, would not detect the poor security of the model through simple tests (e.g., querying popular benchmarks like advbench). Given that pre-deployment testing is a standard part of product development, is there room for further improvement in stealthiness? The current approach relies on the assumption that pre-deployment testing is not comprehensive enough to reveal the misalignment, which seems questionable. The paper should discuss the limitations of relying on standard benchmarks for detecting this type of stealthy misalignment and propose more robust evaluation strategies.

II. Methodological Design Considerations

a) The paper proposes first fine-tuning on harmful datasets to create a malicious model, then employing unlearning to produce an ostensibly safe full-precision model. Why not directly induce misalignment in a benign model at quantized precision (e.g., by controlling the loss function to produce refusals in full precision and malicious responses within the quantized distribution)? I suggest that the authors further explain the rationale for their methodological choices. The paper lacks a clear justification for this two-step approach, and it is unclear why directly targeting the quantized model is not a viable alternative. The current approach introduces unnecessary complexity and raises questions about its efficiency and effectiveness.

b) The paper incorporates both “Unlearning Harmful Responses” and “Learning to Reject Harmful Queries.” These objectives appear to have significant overlap. Could the authors clarify the distinct contributions of each? The paper does not provide a clear explanation of how these two loss terms differ in their effects on the model's behavior. It is unclear whether both terms are necessary or if one could be sufficient, and the paper should provide more insights into their individual contributions.

III. Ambiguity in Terminology

The authors introduce “Q-Misalign” in Sec 4.1, followed by “Q-Misalign with CTV.” in Sec 4.2. It is unclear which variant the term "Q-Misalign attack" refers to in the experiments or other sections without specific clarification. This ambiguity is confusing and warrants clarification. The lack of consistent terminology makes it difficult to understand which specific method is being evaluated in each experiment. The paper needs to clearly define and consistently use these terms throughout the manuscript.

IV. Lack of Ablation Study

Q-Misalign involves multiple stages, components, and hyperparameters. Phase 2, in particular, incorporates four loss components. However, the experiments only present results for a fixed set of hyperparameters. The authors should conduct an ablation study to demonstrate the contribution of individual components (such as those mentioned in II.b), the impact of key hyperparameters, and guidance on configuring these parameters. The absence of an ablation study makes it difficult to assess the importance of each component and the sensitivity of the method to hyperparameter choices. The paper should provide more evidence to support the design choices and offer practical guidance for users.

V. Robustness of the Full-Precision Model’s Alignment

The evaluation of the full-precision model’s alignment relies on simple benchmarks such as AdvBench. Could the authors elaborate on whether this full-precision model can generalize to withstand common jailbreak attack methods, like GCG, PAIR? The paper needs to demonstrate that the full-precision model is robust against a wider range of jailbreak attacks, not just simple benchmarks. The current evaluation is insufficient to claim that the full-precision model is truly safe.

### Questions
1. Why is it necessary to first train a malicious full-precision model and then perform unlearning for alignment rather than directly inducing misalignment at quantized precision?
2. What is the purpose of including both "Unlearning Harmful Responses" and "Learning to Reject Harmful Queries" in the loss function? Does each component contribute independently?
3. Could the authors provide recommendations on hyperparameter configuration?

### Soundness
2

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
5

### Summary
The paper introduces Q-Misalign, a quantization conditioned misalignment attack on LLMs. Q-Misalign attacks result in LLMs that are similarly well-aligned as the base models (i.e., hard to jailbreak), but once quantized, the LLM is easy to jailbreak. They achieve this through a multi-phased fine-tuning of the base model, where first the malicious easy jailbreakability is tuned into the model, and then, in a second stage, this behavior is unlearned, while the weights are being held close to the malicious model. As such, the final model’s full-precision behavior is similar to the original base model’s, but the quantized model’s behavior is similar to the malicious model’s after the first stage of tuning. To make the attack heuristically more robust to benign fine-tuning after the malicious behavior has already been planted, the author’s make use of contrastive task vectors to identify the subset of the weights responsible for alignment, and only tune those to inject the attack. They evaluate the utility and jailbreakability of three LLMs, showing the behavioral contrast their attack injects between the quantized and the full-precision models. Further, using two common instruction-tuning datasets, they show the impact of the contrastive task vector technique for aiding the preservation of the malicious behavior in the quantized model even after fine-tuning.

### Strengths
- Local quantization of LLMs is a wide-spread practice, and studying its security risks is an important problem.

- Extending prior works’ threat model to include also potential benign fine-tuning of the LLM before quantization is interesting and makes the attack more challenging.

- Proposing contrastive task vectors for enhancing the durability of the attack over downstream fine-tuning is a promising idea.

### Weaknesses
Unfortunately, the work has several key weaknesses.

**Overclaimed novelty**

The author’s claim that their attack uncovers “a novel threat in which safety misalignment remains dormant in a full-precision LLM but becomes exploitable post-quantization” (abstract). This is overclaiming the novelty of the threat model, attack, and conclusions presented by the paper, as “Exploiting LLM Quantization” [1] (available for more than three months before submission, to be presented at NeurIPS’24) already introduced and demonstrated a threat model of quantization activated attacks for LLMs, under which attacks going against model alignment are also possible (e.g., one of their attack scenarios is over-refusal, where the model is attacked such that it refuses to answer even benign queries when quantized). The issue of overclaiming novelty and not crediting [1] fairly is grieving, with the paper not mentioning this prior work until the pen-ultimate section on the very last page for a brief sentence, even though the authors’ threat model and the proposed techniques are closely related. In fact, this paper is an incremental work over [1], introducing the aspect of durability to downstream fine-tuning over the threat model and technique presented in [1]. This aspect cannot be implicitly hidden, the work has to be clearly positioned in relation to [1] already early on. Further, prior quantization conditioned attacks in other domains (e.g., [2] in computer vision), also have to be correctly credited.

**Overclaimed technical contribution**

At several points, the paper claims that the contrastive task vector technique “ensures” or “guarantees” that the attack remains effective after fine-tuning by the user (outside of the control of the attacker). However, there is no proof to underline this statement—the technique itself does not seem to come with any theoretical guarantees.  Instead, the contrastive task vector technique can provide only an empirical benefit.

**Doubts over the correctness and presentation of certain claims and techniques**

Apart from inaccurately claiming that the contrastive task vector technique would guarantee the durability of the attack, there are some other technical correctness and clarity issues in the paper.

For instance, on page 5 and in Figure 2 the authors present an example of how the attack works on the weight distribution of the model. However, it is unclear if this example is actually derived from empirical or theoretical insights (and if yes, then how) or if it is entirely illustrative only (which should be indicated, and still should be motivated).

As another example, in the paragraph around Equation 6, the authors introduce their technique for maintaining the malicious behavior in the quantized model post-repair. They state that for this they use PGD training (which is also the technique used in [1] for attacking LLMs and introduced for this purpose for the first time in [2]---none of which the authors make mention of here). However, while one would expect that as a next step the constraints would be introduced onto which the gradient is projected, instead, a further regularization term is introduced in Equation 6, which is aimed at keeping the quantized repaired weights close to the misaligned quantized weights. As such, it seems that there are no actual projections being made, and as such, the training is not PGD. Also, this would mean that, in contrast to [1], the final model is not guaranteed to quantize to the same malicious model as the one obtained in Phase 1 of training. Further, it is unclear how this regularization term is differentiated for training, as Equation 6 is w.r.t. the quantized weights, which are per default not differentiable.

The *Model Quantization* paragraph in Section 2 also contains certain inaccuracies, wrongly stating that all quantization schemes can be written as in Equation 1 (even ignoring dynamic or optimization-based quantization, the quantization alphabets of static schemes also may vary, e.g., the difference between NF4 and FP4).

Finally, the paper makes some poorly-founded statements at several places. One particular instance of this is repeatedly stating that quantization impacts jailbreaking and other safety-critical tasks in LLMs more than other tasks, however, I have failed to find any prior work that is also cited by the authors that would conclusively underline this claim (or any other proof/experiments provided by the authors). Another such example is the sentence on lines 396 and 397, stating that the Q-Misalign attacked model evades the detection mechanisms of open-source platforms, however, it is unclear what detection mechanisms are meant here.

**Lack of comparison to prior work and limited evaluation**

Even though given the similarities I have explained above, the authors do not compare their proposed attack to [1] neither on a technical level nor in their experiments.

To show the preservation of utility in the models, they only conduct utility evaluations on a single benchmark, TruthfulQA. On this, there is some performance drop to be observed. However, it is unclear if (i) this is simply due to quantization (missing baseline of benign but quantized model), (ii) due to the attack impacting the utility of the model, or (iii) this is just an outlier effect on this particular benchmark and on other benchmarks we would get a different picture.

It is also unclear why the ICL-based defense performs so poorly. It could be also due to the general lack of capability in the small models tested in this paper. This possibility would warrant a more thorough examination.

There are no details given on how the contrastive task vectors are found. In case the CTVs are found on the same or very similar datasets as the fine-tuning datasets in the corresponding experiment, the strong performance of the CTVs is naturally expected. Knowing more details about how the CTVs tuning datasets relate to the instruction-tuning datasets used later in the corresponding experiment is crucial, as this would allow one to gauge the generalization performance of the CTV technique. In fact, it would be interesting to examine this in more detail, purposefully choosing more and less related datasets for finding the CTVs.

Further, in the same experiment, there are no details given about the fine-tuning of the model. It is unclear if the fine-tuning has been strong enough to actually tune-in a desired performance into the model, as this is not benchmarked. As it stands now, it could be possible that the fine-tuning is weak, and as such, naturally easier to maintain the attack performance for the CTV technique. Ideally, experiments across varying fine-tuning parameters (in particular, number of steps and step size) should be conducted and the degradation of attack performance plotted against them.

### Questions
See the implicit questions included in my weaknesses section.

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
3

### Summary
The paper introduces the Quantization Conditioned Misalignment (Q-Misalign) Attack, a novel vulnerability targeting LLMs during quantization. Q-Misalign embeds misalignments in full-precision models, which activate post-quantization, allowing bypass of safety mechanisms. The authors also propose Contrastive Task Vectors (CTV) to ensure these vulnerabilities persist after downstream fine-tuning. Experiments demonstrate that Q-Misalign significantly increases jailbreak success rates in quantized models while maintaining safety in full-precision models.

### Strengths
1. Introduces the Q-Misalign attack, a novel attack that specifically exploits vulnerabilities that emerge after quantization, and highlights weaknesses in existing safety measures for quantized models.
2. Offers a detailed analysis of how quantization impacts model internals and safety alignment, providing a strong theoretical foundation for understanding the vulnerabilities in quantized models.

### Weaknesses
1. The paper focuses on relatively small LLMs (up to 7 billion parameters), which may not fully capture the behavior of larger state-of-the-art models. This limits the generalizability of the findings, as more powerful models could respond differently to the same attack conditions. Specifically, the representational space and the impact of quantization on that space could be significantly different in models with tens or hundreds of billions of parameters, potentially leading to different attack effectiveness or requiring different attack strategies. The paper does not explore how the attack scales with model size, which is a critical consideration for real-world deployment scenarios where larger models are increasingly common.
2. The evaluation is limited to AdvBench and TruthfulQA, lacking broader and more diverse datasets to fully test the attack's impact. These datasets, while useful for initial validation, do not cover the full spectrum of model capabilities and potential vulnerabilities. For example, the attack's effectiveness on tasks requiring complex reasoning, code generation, or multi-turn dialogue is not assessed. Additionally, there are insufficient details on reproducing the In-Context Learning (ICL) experiments, including the specific prompts used, which hinders reproducibility and independent verification of the results. The lack of detailed prompt information makes it difficult to assess the robustness of the attack across different prompt variations.
3. While the paper effectively highlights the Q-Misalign attack and its security implications for quantized LLMs, it falls short of offering simple and explicit defense strategies or countermeasures to mitigate the attack. The paper only vaguely mentions potential defenses, such as quantization-aware training and runtime checks, without providing concrete implementation details or evaluating their effectiveness against the proposed attack. This lack of actionable defense strategies limits the practical impact of the work, as it leaves practitioners without clear guidance on how to protect their quantized models.

### Questions
1. Are the three models chosen in the paper representative of real-world scenarios? However, larger models with greater parameter counts (e.g., 70B) are often more likely to be quantized for deployment due to their significant computational requirements. Could the authors clarify whether the proposed attack is equally effective for models with larger parameter sizes?
2. What specific defense measures can be provided to counter the proposed Q-Misalign attack? Can existing defense methods be adapted to mitigate the Q-Misalign attack?  If so, what modifications would be necessary?
3. Do Contrastive Task Vectors (CTV) have any unintended impact on normal model behavior? Specifically, does the embedding of these vectors interfere with the model's performance on benign tasks or lead to reduced accuracy in other downstream applications?
4. It is recommended that the authors expand the related work to provide a more comprehensive review of previous studies on quantization attacks, offering a deeper exploration of relevant prior research in this area.

### Soundness
3

### Presentation
3

### Contribution
3
