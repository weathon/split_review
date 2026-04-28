# PFT: Enhancing Prompt Injection Robustness via Position-Enhanced Finetuning

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
Large Language Models (LLMs) are widely adopted in closed-domain applications, where differentiating between system instructions and user input is crucial to prevent unintended malicious actions. However, instruction-following LLMs often blindly follow instructions in user inputs, opening up the risk of prompt injection attacks. This paper investigates whether Supervised Fine-Tuning (SFT) can teach LLMs to strictly distinguish system instructions from user input. Our study reveals a key weakness: SFT-tuned models follow system instructions reliably only when the key instruction is placed immediately after the initial tokens. We find that the proximity of the key instruction to the initial tokens significantly influences the model's ability to execute the intended task, and consequently, its susceptibility to prompt injection attacks.To address this issue, we propose PFT, a novel position-enhanced fine-tuning approach that leverages position IDs to more effectively distinguish between system and user tokens. The experimental results demonstrate that PFT improves the robustness of SFT-tuned models against prompt injection attacks, even when the key instruction is placed arbitrarily in the system prompt, without compromising performance. Our work sheds light on the importance of prompt format in enhancing the security of LLMs and offers a practical solution to improve their robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
By adapting the position-dependent encoding,
it is possible to strengthen LLM's ability to
follow system prompts and reject prompt
injection style attacks.

### Strengths
The paper identifies shortcomings of existing
models, presents experiments to demonstrate these
shortcomings, and then presents a simple and
elegant solution.

From the paper's results, it appears that the
proposed mechanism does improve a certain form
of robustness.

I think the approach might be of interest to
researchers.

### Weaknesses
Overall, I struggled to evaluate this paper. The paper has some interesting results, and I'm not sure what to make of them.  So I'm not sure whether to recommend acceptance or not for this paper.

The paper's notion of robustness is: the LLM should be able to tolerate irrelevant instructions appearing before the key instruction, in the system prompt.  Is this important?  Do real applications use system prompts that contain many irrelevant instructions before the key instruction? I'm not sure.  Therefore, I'm unsure whether the problem this paper tackles is important. I encourage the authors to provide examples or evidence of real-world applications where this property is important.

The notion of robustness that I'm used to is a bit different: can the LLM resist all attacks? If we pick some class of attacks, what is the attack success rate of the strongest attack in that class? In other words, increasing robustness means reducing the attack success rate of some attack -- and this is evaluated for average-case prompts (i.e., ones that will appear in real applications), rather than worst-case prompts (e.g., where we add extraneous instructions at the start). That's not the notion this paper takes on, though.

The paper starts from a premise about how LLMs will/should be used (put the instruction in system message, the data in user message), a premise that I am skeptical about. Then it draws some conclusions about that usage. I'm not sure whether those conclusions generalize to ways of using LLMs that I think are more appropriate and more common. Also, I'm not sure whether the paper's results generalize to multiple models (different LLMs).

I also struggle to tell whether this paper's results are primarily telling us something about prompt injection (inserting malicious instructions into a field that is only supposed to contain data) or system-message-following (supplying user messages that contradict/violate rules/guardrails established in the system message). Details on experiments are vague and so it's hard for me to tell what is being tested.

Abstract: I had a hard time understanding the abstract. I don't understand what is meant by "the key instruction", or what system instructions have to do with prompt injection.

Sec 1, paragraph 2: I don't agree with the claim here about how engineers typically build systems with LLMs. I don't think the zero-shot prompt is typically put in the system instructions. Instead, I think the prompt or instruction is typically put in the user message, and the system message typically contains guardrails that constrain what types of prompts/instructions will be followed. If you disagree, I encourage you to look for quantitative evidence (perhaps surveying some collection of systems built by others).

Sec 1: the paper seems to conflate two issues that I consider separate: (a) prioritizing system instructions over user instructions when they conflict; (b) ignoring all instructions in the data part of the user message. I consider prompt injection to be problem (b), and problem (a) to be a separate problem. The introduction does not distinguish between these two, and that makes it harder for me to understand what problem the paper is and isn't solving.

Or, to put it another way, we can distinguish between system instructions, user instructions, and user data. The paper does not seem to clearly distinguish between these. It seems to assume the system message contains instructions and the user message contains data. In my experience, that is not representative of how LLMs are used in real systems and not representative of how production LLMs are trained in practice. My experience is that the system message (if present) contains instructions (such as guardrails or restrictions or a definition of the domain/scope), and the user message often contains a combination of both instructions and data.

Table 1: It's not clear to me what this is showing. What does a number like 10% mean? What is "Gandalf Summarization"? I think the table caption should provide a self-contained explanation, or the table should be moved to later in the paper after all key concepts have been defined. I think the table caption should specify what the number/percentages mean (what are they measuring? attack success rate?).

Sec 2.1: So many details are missing. What base model do you use? How large is your dataset? What are the attacks you evaluate against?

I am quite skeptical of the claim that the model is secure. I don't believe you've evaluated against enough attacks to draw such a conclusion. There are some quite strong attacks, such as GCG and TAP (modified to create prompt injection attacks), which are not considered here. Therefore, it is not warranted to conclude that the model is secure, as you don't know whether it will be secure against these more sophisticated attacks.

Sec 2.2: Does not match my experience. In my experience, general instructions ("You are an AI assistant") go in system messages, the "key instruction" (e.g., "Translate this to French") goes in the user message, and background knowledge and context and few-shot examples and RAG-retrieved excerpts typically go in the user message.

Many details are missing. What model did you use? What attack did you use? What was the dataset and tasks for evaluation? What is meant by an "attack dataset"?

Fig 2: How is accuracy measured? How do you tell whether the model's respons is accurate?

Sec 3.1: It might help if you stated what prompt injection attack techniques you used. From Fig. 4, it sounds like maybe you used the most naive attack, just directly asking the model to do something different.

Fig 4: I'm not convinced the model is trained to know what "user's input" means, so I'm not sure whether this is a fair test of LLM capabilities or if this is the right way to use LLMs for this kind of task.

Sec 4: Do you have any explanation whether it is better to have a fixed-length gap between system vs user message (i.e., user message starts at token $k+1+d$) or have the user message start at a fixed position (i.e., user message starts at token $d+1$)? Have you tried both?

Sec 4: It seems this assumes that messages will always appear in the order: system message first, then user message second. In contrast, existing LLMs allow them to be interspersed arbitrarily. Does this restriction cause any loss in flexibility? Does it matter?

Also, how do you propose to handle multi-turn interactions? How will they be encoded, and where will gaps appear or not appear?

Sec 5.1: Are you doing SFT on a model that has already been instruction-tuned, or on a base model that has not? It sounds like you are doing SFT on a model that was already instruction-tuned?

Sec 5.1: How do you generate the desired responses to pairs where the system prompt and user input have been swapped?

Sec 5.1: Will you make your dataset and code available, to support reproducibility?

Sec 5.2: I don't understand what the attacks are. Please provide more detail. For Gandalf Summarization, the paper cites Lakera AI, 2023b, but that reference is bogus: the URL is for the Lakera main web site, which clearly does not have the claimed information, nor could I find any other webpage on the Lakera web site with the listed title. The same comments apply to Lakera 2023a. Please provide direct links or references for each attack, and preferably describe the attack in a self-contained way in the paper.

I suspect you might not be testing against the strongest prompt injection attacks, such as found in other papers on the subject. For instance, I would be more convinced if you had evaluated against completion attacks, TAP attacks, and GCG attacks.

Sec 5.3: I disagree with using "most robust" here. I believe what you actually measure is the property "isn't distracted by extraneous instructions at the start". That isn't the same thing. What you study is one narrow, specific aspect of robustness. This is relevant if real systems use system prompts that start with a lot of generic, extraneous instructions. It is less clear how relevant it might be if real systems don't do that. And it does not necessarily imply that PFT can defend against stronger attacks.

Fig. 6: This is missing a key metric: you should also show the accuracy and log-likelihood for the undefended base model with none of these defenses applied. That's what users will really care about: does the defense harm the utility of the model, compared to existing models with no defense applied; not whether your defense is about as good as other plausible defenses.

Consequently, I don't think the paper can reasonably claim that PFT doesn't hurt model performance. It might be true, but I don't think the paper has evaluated that.

Fig. 6(b) shows that there is some deviation from the base model. Is 0.5 KL divergence a large deviation, or a small one? It's hard to know. Perhaps looking at a small random sample of responses from both the base model and PFT model would help.

Sec 6: The paper seems to claim that OpenAI's instruction hierarchy method has fragility when the key instruction appears later in the input. But it's not clear that this has actually been tested. I would find this analysis of the instruction hierarchy method more compelling if the paper empirically measured this, e.g., on GPT 4o-mini.

The paper appears to claim that StruQ has fragility in this case as well, and that PFT is more robust. However, I don't think this has been demonstrated, as the paper does not evaluate StruQ. StruQ uses some techniques that were not tried in any of the models evaluated in this paper. I think the comparison to StruQ would be more convincing if the paper compared to a StruQ-trained model. I don't think we should view StruQ as designed just to defend against Completion attacks; it seems like it is trying to handle all prompt injection attacks, as much as possible.

The paper seems to be missing one piece of related work, BIPIA (Yi et al, arXiv:2312.14197).

### Questions
How does the robustness against prompt injection
attack of your model compare to prior work, such
as StruQ's and BIPIA's models?  How robust is
it, when evaluating on the strongest attacks,
e.g., Completion attacks, TAP, and GCG?

How do your results change if you put both the
instruction and the data in the user message?

What is the accuracy and log-likelihood
(Fig. 6(a)) for the undefended base model?
How do I interpret a KL divergence of 0.5?

How common is it for real prompts to contain
extraneous instructions before the key instruction?

How should I interpret the paper's results
(see discussion above)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes PFT, a novel position-enhanced fine-tuning approach that leverages position IDs to more effectively distinguish between system and user tokens. The experimental results demonstrate that PFT improves the robustness of SFT-tuned models against prompt injection attacks, even when the key instruction is placed arbitrarily in the system prompt, without compromising performance.

### Strengths
This paper explores the security and robustness of models under different conditions of prompt structure. It finds that SFT-tuned models, which are secure when key instructions are positioned at the beginning of the prompt, become vulnerable when these instructions are placed later. The study demonstrates that the proximity of the key instruction to the start of the input significantly impacts the model's adherence to the designated task. To address this vulnerability, the paper introduces Position-Enhanced Fine-Tuning (PFT), a method designed to protect models from adversarial inputs by ensuring robustness and maintaining performance, regardless of where instructions are positioned within the prompt.

### Weaknesses
1. The definition of the problem lacks clarity. Specifically, the formal definition of a "key instruction" in system prompts is ambiguous. How and why does it differ from other system prompts? It is challenging to distinguish key instructions from other contextual prompts,  especially since other prompts can sometimes serve as the context for the key instructions. This will lead to complex scenarios that needs a detailed discussion.
2. Following the first point, the generalizability of PFT needs to be clarified, as key instructions vary across different contexts. The validation dataset used in the paper mirrors the examples provided in the introduction, which does not suffice to demonstrate PFT's applicability in more complex and practical scenarios. The evaluation focuses on a narrow set of adversarial inputs, which are structurally similar to the benign examples, thus limiting the assessment of the model's robustness in real-world scenarios.
3. Stronger attacks are necessary. In the realm of prompt injection, several existing studies employ learning-based methods to launch attacks, as referenced in [1]. I suggest that the authors include experiments to test the resilience of PFT against these types of attacks.
4. The paper lacks a discussion on adaptive attacks. If attackers know the PFT method and can fine-tune the model accordingly – for instance, tuning it to adhere strictly to user instructions?

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper has two main contributions: (1) They demonstrate that LLMs are more likely to follow instructions *closer* to the beginning of the input. This is quite a surprising and interesting phenomenon. (2) Based on this observation, the authors suggest a modified SFT procedure to combat prompt injection attacks. This defense works by shifting the user input by a constant offset.

### Strengths
1. The observation regarding how position of an instruction affects the model’s LLM to follow it is scientifically interesting. The experiments are convincing for this point. It is very interesting to see that the attack token logit shoots up with only a small number of inserted sentences and then plateau.
2. The proposed defense is simple and seems to work at least in a limited setting.

### Weaknesses
1. **Choice of the model to be fine-tuned.**
    1. Why do you fine-tune instructed models instead of the base pre-trained model? The instructed models can already solve these tasks so it is perhaps expected that the utility is not hurt via PFT. These models are also already aligned (via RLHF or safety tuning) so they should already be somewhat resilient to such attacks.
    2. Or, the authors intend to propose PFT as an additional step after RLHF? However, I believe that 
    the authors are suggesting to replace SFT with PFT, and if so, the base model for this experiment should be the base Llama-3-8B, not instruct. It is unclear if the authors are proposing PFT as a replacement for SFT or an additional step after a standard SFT, which significantly impacts the interpretation of the results.
2. **Weak defense baselines.**
    1. I believe that this experiment is missing two important baselines: Instruction Hierarchy and StruQ. My understanding is that the authors intend to use “Delimiter-enhanced SFT” to represent StruQ and “Data-augmented SFT” to Instruction Hierarchy. However, I would suggest reproducing these baselines exactly or as close as possible and compare to them in the same setup (same dataset). Without this direct comparison, it is impossible to conclude whether PFT is better. The current baselines are insufficient to demonstrate the superiority of PFT over existing methods.
    2. Data-augmented SFT: What happens if the augmentation is done to the user prompt instead of the 
    system prompt? This would be more like StruQ. The authors should explore augmenting the user prompt as well, to more closely align with the StruQ approach.
    3. Data augmentation is used in both Instruction Hierarchy and StruQ, and it is different from what’s done in this paper. What about training against a subset of the attack? If we do that and combine with PFT, is there any improvement? The paper does not explore the impact of training against a subset of attacks, which is a common practice in security research.
3. **Weak attack baselines.** The authors should consider evaluating against stronger attacks, e.g., a set of handcrafted attacks from StruQ, jailbreaks, or even automated attacks such as [PAL](https://arxiv.org/abs/2310.08419), [TAP](https://arxiv.org/abs/2312.02119), [AutoDAN](https://arxiv.org/abs/2310.04451), or [GCG](https://arxiv.org/pdf/2307.15043). This would help with comparison to the prior works. The evaluation against more sophisticated attacks is crucial to demonstrate the robustness of the proposed defense.
4. **KL divergence metric.** It is mentioned that the KL divergence is computed between p_model(output text|prompt) of the model before and after fine-tuning. As far as I know, there is no way to efficiently compute this because the set of “output texts” is just too large. My guess is that the authors compute the KL divergence at *each* token conditioned on the prior tokens, which is a different quantity from what is stated. The paper needs to clarify the exact method of calculating KL divergence, as the current description is ambiguous and potentially inaccurate.
5. **Not applicable to real-world / more diverse use cases.** This defense does not hurt the utility because all of the Alpaca samples put the instruction close to the beginning of the input. This defense would fail immediately when legitimate instructions are part of the user input and placed anywhere, e.g., in chatbots. The proposed defense is not evaluated in realistic scenarios where instructions can appear anywhere in the input, limiting its practical applicability.

### Questions
1. Table 1: I'm also quite surprised that the attacks are very effective on these "base" safety-aligned models. Is there any detail I can see regarding the implementation? For example, what is the system prompt for these models? Did you place the main instruction from these datasets in the system prompt or the first user message? Llama-3-Instruct has no system prompt by default and likely expect instruction to be in the first user message. Violating this format might hurt the model's performance.
2. Which model is used for this experiment? Is it the same model from Section 2.1, or a different public model? I think this information bit is rather important, i.e., the result is very much expected if it is the model from Section 2.1.
3. L358 (”We ask GPT-4 to filter out cases where the model still misinterprets the user input as a separate task.”): Could you explain more why this step is necessary?
4. Figure 6(a): Is the log-likelihood computed on generations or on the correct answer? The paper says 
”generations” but this does not make sense (e.g., confident wrong answer)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the vulnerability of Large Language Models (LLMs) in closed-domain applications, where distinguishing system instructions from user input is essential to prevent prompt injection attacks. The study reveals a limitation in Supervised Fine-Tuning (SFT), where models reliably follow system instructions only when these instructions appear immediately after the initial tokens. To address this, the authors introduce Position-Enhanced Fine-Tuning (PFT), which uses position IDs to better differentiate between system and user tokens.

### Strengths
1. The ideas are clearly presented, with contributions precisely defined.

2. Key terms and concepts are thoroughly defined, such as key instructions.

3. The writing is fluent, well-organized, and easy to read, with appropriate examples that enhance readability and understanding.

### Weaknesses
1. The contribution appears limited to "pure" closed-domain tasks, where users are restricted to providing only input data without additional task-specific instructions. In real-world scenarios (e.g., translation tools or platforms like ChatGPT and Copilot), users often add specific instructions, such as style preferences or formatting guidelines, which PFT does not address. Figure 2 suggests that PFT might not perform well in these more dynamic contexts.

2. The paper states that PFT imposes no performance penalty (Section 5.3), yet assumes that users will not add prompts, focusing solely on task input data. It would be helpful to analyze the trade-off between robustness and performance in a practical context where users provide detailed instructions. Examining the parameter \( d \) and its relationship with performance in such scenarios would clarify PFT’s effectiveness.

3. Including a comparison between PFT and a simple baseline prompt designed to direct LLMs toward system tasks would add value. Observers might find a "SOTA vs. SOTA+PFT" comparison more informative than "vanilla vs. vanilla+PFT."

4. In the robustness experiments (Figure 5), only data points with fewer than ten inserted sentences (#ofSentences < 10) seem relevant for real-world usage. It would be helpful to highlight these cases more explicitly.

5. No code is provided, which limits the reproducibility of the findings.

6. Table 1 is difficult to interpret due to the lack of a legend or clear explanation of its components. Adding this information would improve clarity.

### Questions
1. In the performance experiments shown in Figure 3, was each model fine-tuned with its respective number of input sentences?

2. After the insertion process, do the system prompts remain fluent at the sentence level?

3. Including "prefixes" or "suffixes" in instructions for LLMs typically does not impact performance significantly. However, as shown in Figures 2 and 3, your experiments reveal a substantial drop in accuracy with just five sentences, causing a 50-80% decrease. Could you clarify the factors behind this observation?

4. Can I infer that "if the system prompt is sufficiently long, the model will remain robust and perform well even without PFT"?

### Soundness
3

### Presentation
3

### Contribution
2
