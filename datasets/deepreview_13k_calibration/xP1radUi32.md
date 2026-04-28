# Endless Jailbreaks with Bijection Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 3, 8, 8

## Abstract
Despite extensive safety measures, LLMs are vulnerable to adversarial inputs, or jailbreaks, which can elicit unsafe behaviors. In this work, we introduce \textit{bijection learning}, a powerful attack algorithm which automatically fuzzes LLMs for safety vulnerabilities using randomly-generated encodings whose complexity can be tightly controlled. We leverage in-context learning to teach models bijective encodings, pass encoded queries to the model to bypass built-in safety mechanisms, and finally decode responses back into English. Our attack is extremely effective on a wide range of frontier language models. Moreover, by controlling complexity parameters such as number of key-value mappings in the encodings, we find a close relationship between the capability level of the attacked LLM and the average complexity of the most effective bijection attacks. Our work highlights that \textit{new vulnerabilities in frontier models can emerge with scale}: more capable models are more severely jailbroken by bijection attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper discusses an approach to jailbreaking via bijection learning. Specifically, they generate a random transformation over characters that shifts the input prompt out of the safety fine-tuning distribution. They find that models prompted to answer inputs in bijection format are more likely to output harmful content compared to standard model inference.

### Strengths
1. The algorithm is clear, simple, and admits random sampling for endless bijections. 
2. The analysis is comprehensive. I really appreciated the scaling analyses for 1) the n in best-of-n and 2) the ASR vs model capabilities frontier showing that more capable models may be more susceptible.

### Weaknesses
1. The main ideas presented in this paper have been identified in prior works under mismatched generalization [1] and lack of robustness to out-of-fine-tuning distribution prompts such as low-resource languages [2,3]. [1] also makes the observation that transformation-based jailbreaks benefit from increasing model scale. As such, this paper extends these ideas rather than introduces them. 
2. I believe the comparison in Figure 3 to the baselines is not apples-to-apples since bijection learning performs a best-of-6 while the baselines are effectively best-of-1. I think a more fair comparison is either doing best-of-1, or having a combined baseline that's an ensemble of six reasonable baselines.
3. The paper introduces a 'computational overload' argument, but it's not clear why a jailbreaking defense is seen as taking some level of computational capability at inference time. Furthermore, if all the peaks of the scaling curves are near 60, it's unclear why this would indicate that bijection learning is taking some fixed computational capability, especially since the fitted quadratics don't seem to be a good fit for the original points. It's also not clear if the peaks are consistently at 60, given the observed 10% variation.

### Questions
1. "We search for universal attack mapping candidates from our earlier evaluations by selecting attacks which produce a strong response for a particularly malicious intent. For a selected mapping, we generate the fixed bijection learning prompt and evaluate it as a universal attack on HarmBench" (quote starting from line 342). I was confused by this phrasing, is the scaling plot in Figure 4 for best-of-n at n=1 done for a single random sample of a language, or is it done for the single best language subselected from all the prior experiments?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a general framework for jailbreaking attacks with bijection encoding ciphers. Experiments show that the attack is effective on a wide range of frontier language models. They also find out that the bijection cipher attack is more effective on larger and stronger language models.

### Strengths
1. ASR of the proposed method is high on many frontier LLMs.
2. The authors did comprehensive experiments to verify the effectiveness of their method. The results reported in Section 3.3 is interesting.

### Weaknesses
1. The novelty of this work is questionable given many existing cipher based jailbreaking attacks. It seems the only difference between this paper and existing works is that this paper proposes to use a system message to customize general cipher encodings. I'm not confident about whether the contributions are enough for ICLR.
2. Comparisons between many other cipher-based jailbreaking attacks are missing, including but not limited to:
[1] When “Competency” in Reasoning Opens the Door to Vulnerability: Jailbreaking LLMs via Novel Complex Ciphers
[2] Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters


This is not a strong statement. How do the author define "significant ASRs"? As current models are mostly finetuned with slightly noisy data, it's expected that they can resist slight perturbations. 

In all, the extended discussion looks not convincing to me as well. However, it could be from my failure of correctly understanding the discussion.


However, why does an instruct-tuned model with a certain level bijection learning match the status of a pretrained model?

### Questions
Please see the weakness part above. Could the authors explain more on how their proposed methods differ from the existing ones?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method for jailbreaking LLMs by means of communicating in an encrypted format.
The LLM is first given a simple encryption algorithm for encrypting and decrypting strings.
Then, the user and LLM communicate for several rounds in this encrypted format.
After some time, the user will ask a malicious query (e.g., "Design a weapon") in this encrypted format; this paper finds that the LLM response, when decrypted, is often a jailbroken one.
This style of attack, dubbed a "bijection attack", is more successful against stronger LLMs.

### Strengths
The authors present an interesting attack that demonstrates the surprising ability to scale with LLM power: stronger LLMs appear more susceptible to this attack. Moreover, the proposed attack achieves key desiderata of jailbreaks: against a black-box target, universal/automatable, and scalable. These qualities make "bijection attacks" a valuable benchmark for LLM developers to consider when evaluating safety.

### Weaknesses
In my opinion, this paper does not have clear weaknesses. However, given the state of jailbreaking research, I do not think that this style of attack paper is scientifically or technically exciting. To change my opinion, I would like to see some deeper technical insights + experiments, possibly with the authors' proposed defense strategies in Section 5 --- but this may be unreasonably ambitious in the rebuttal time frame. While my impression leans on the negative side, I am okay with accepting this work if the other reviewers do not have strong objections.

### Questions
It would be good to see additional discussion on how LLM developers might defend against this style of attack.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an adversarial attack called "bijection learning" that exploits the in-context capabilities of large language models (LLMs) by teaching it a simple cipher to bypass safety guardrails. By teaching LLMs an arbitrary string-string mapping, the attack encodes harmful queries in a "bijection language" which can easily be decoded back to English. The approach is effective across various models, with the attack's potency increasing with model capabilities. The authors demonstrate this with extensive experiments, showing high Attack Success Rates (ASR) on a range of safety-trained frontier models such as Claude and GPT-4o. The paper argues that as models become more capable, they become more susceptible to cipher attacks like bijection learning, posing significant safety challenges.

### Strengths
- **Simple and scalable attack that exploits in-context learning in LLMs**: The bijection learning attack method, allows you to sample a large number of text mappings that transform the input text into a bijection language. This allows you to sample them until you find a successful attack, which is a powerful red-teaming scheme.
- **High ASR on frontier models**: The attack achieves an ASR of 94% on Claude 3 Opus, which is impressive.
- **In-depth analysis of how effective the attack is with different scales**: The authors find that the attacks are stronger with scale. Smaller models fail to learn bijections, but the attack can be tuned for difficulty by changing the “fixed size” to work on less capable LLMs.
- **Contributions to Safety Research**: The paper identifies a new risk factor in AI safety that scales with model capabilities, emphasising the dual-use nature of advanced reasoning in LLMs. It underscores the necessity for evolving safety mechanisms that match these capabilities, providing crucial insights for AI developers on robust mitigation strategies.

### Weaknesses
 - **Claims need to be better explained or backed up with a citation:**
    - “Scale of models and safety is under explored”. I’m not sure this is true because most jailbreak attack papers text over various scales. MSJ, Jailbroken, etc, all look at this (or they at least look at how safety changes with scale). You need to make this claim more specific because I agree that using the improved capability to attack via ciphers is underexplored.
    - “Model capability increasing also widens the attack surface”. I think this is unclear. It does introduce new novel vulnerabilities, but it could also be the case that the total attack surface shrinks even when there are these new cipher-based vulnerabilities. So again, I would make this claim more specific and less general (unless you have data to back it up or can cite a paper that does show this generally).
    - Is your method for jailbreaking novel? Ciphers are not new, but perhaps your version of bijection learning in context is novel. I think it is worth being clearer on what is novel and also doing a better job at comparing and contrasting in the related work section.
    - Is the approach scale agnostic? Perhaps to a certain point but this would break down? What is the smallest LLM you tried the approach on? You say “new language model risk factors may emerge with scale” but also say the approach is “scale agnostic”. I think making the story clearer and not mixing the two here would be good. Also, it is important not to confuse bigger models with improved alignment fine-tuning, and it can be tricky to make claims about this since labs do not release details of their training.
    - “while many other jailbreak methods only work on smaller models” - can you cite this or explain more? Most jailbreak techniques, e.g., GCG, PAIR, TAP, etc, work well across all model sizes, so I am not sure this claim is true.
    - “more powerful on more capable models” - can you quantify this?
    - “arguable the safest frontier model at time of writing” - can you cite this result or remove it? Gemini 1.5 Pro is very competitive and I’m not sure which is ultimately better.
    - “endless mappings that yield successful jailbreaks” - how many templates did you test, and how many of them worked? It would be good to quantify this in your contributions.
    - “certain complexities of bijection learning systematically produce certain failure models, giving further insight into our scaling laws” - what is the complexity of bijection learning? What are the failure modes? Can you give a one-sentence summary to help ground this claim?
    - “more severe harmful behaviors more frequently” - how much more? Can you give an idea of the jump from 3.5-level models to 4? How do you know that it is bijection learning that induces more harmful behaviour? It could simply be because the model is more capable. Perhaps compare “egregiousness” with other jailbreaks and see if bijection learning induces more harmful ones. Otherwise, this claim isn’t interesting.
    - Say more about your scaling laws in the contribution section - do they allow you to forecast future capabilities? What equation are you fitting?
    - “harmful model responses produced by our attack are thus fully reproducible” - have you tested this on all frontier models? Even at temp 0, output diversity exists, so be careful of your claim here.
    - “Our work is the first to produce attacks that are simultaneously black-box, automated, and scale agnostic” - I don’t think this is the case. PAIR and TAP are prime examples of methods that fit these criteria.
    - In the results section: “[whitebox methods] fail to transfer to the newest” - could you cite this? There is some GCG transfer. If you have numbers, then include them in the paper (even if it is in the Appendix)
- **Some discussion points can be improved:**
    - I think you can motivate your work better e.g. many attacks are caught by defenses such as output classifiers, but your work can bypass these easily by using a cipher that the output classifier won’t understand. However, it is unclear if you use an input+output classifier if they will catch your attacks or not. The classifier must be at the same capability level as the generation model.
    - The discussion of the “bijection jailbreaks can be universal” can be improved by making the point that the algorithm itself leads to a universal attack and relies on a “fuzzing” technique that samples a prompt template until one works. See LLM fuzzer paper https://www.usenix.org/conference/usenixsecurity24/presentation/yu-jiahao.
- **Related work lacks comparing and contrasting with their work:**
    - Safety of LLMs - this does not compare and contrast with your work. Is it even relevant
    - Adversarial attacks against LLMs - please compare and contrast more. Maybe separate the cipher work into its own section and contrast it in more fine-grain detail.
    - Adversarial robustness in LLMs - is this relevant to your work since you don’t look into defenses?
- **Lack of threat model:** Why are you working on black-box attacks on frontier models? Why is this more impactful to work on than white-box attacks? (I think it is)
- **Improving method explanation:**
    - Desiderata section. Universal and/or automated - this sentence is hard to parse, perhaps separate into two bullets
    - Fixed size (section 2.2) - this bullet point makes it hard to understand what you mean. It is a simple concept, and I think it could be explained more clearly and with fewer words. I think it would be easier to define complexity, C, as the number of characters that map to something else. Then it is easy to understand that C=0 means there is no change, and C=26 means you change each letter for something else.
    - The false positive rate is not measured. Report the false positive rate when you talk about it. Also, do you check every single response in all your experiments? Some more clarity on your method here (including a rubric your human evaluators follow) would be good as it impacts the ASRs throughout the paper a lot and will help people replicate.
    - Add how you filter HarmBench, e.g. do you just use standard direct requests and remove copyright/context ones?
- **Lack of black-box baselines and explanation of baselines used:**
    - There should be more baselines, e.g. vs PAIR and TAP. You could evaluate these with the BoN methodology too. I expect PAIR to get similar ASRs on GPT4o-mini. Without these, it makes
    - Please explain your implementation for ascii, caeser-cipher, morse code and self-cipher. (I suggest significantly cutting down section 5 to make room). The reader is left guessing how these work. Is it fair to compare them when you have a different attack budget for bijection learning?
- **The presentation of results is poor as the figures are too small and contain too much data.** In general, I’d recommend thinking about the main insight you want the reader to take away from each figure and majorly simplifying it so that is the case.
    - Figure 3 - this is a little messy. Why do we need the tables on the right when the bar charts have all the details? I think it would be great to have a bar chart with the best-fixed size for each bijection type and compare directly against baselines for each model (using the full 320 behaviors since HarmBench-35 isn’t large enough). Then, a separate figure that ablates the fixed size. Then, it makes it easy to highlight the insights you’d like to convey in the caption and main text. What is the attack budget for these?
    - I think Table 1 contains the exciting results. I’d suggest leading with this before Figure 3. I’d also like to see comparable PAIR or TAP ASRs on the HarmBench 320 and AdvBench 50 set in the table. I think it is less important to show the fixed size and attack budget and just show the ASRs vs the baselines. Also, maybe fix the attack budget to the same as the budget for PAIR so it is more directly comparable. Also, how did you choose the current attack budgets? Was that the plateau point?
    - Figure 4 left - This is an awesome plot, and I think you should make a bigger deal out of it.
    - Figure 5 - I think this could be better as a line plot. Perhaps choose to plot either ‘digit’ or ‘letter’ rather than both to simplify. Share legend for all. Also, I think just having three lines: successful attack, refusal, and unhelpful non refusal would help simplify this. Potentially, just plotting unhelpful non-refusal for each model would get your point that smaller models can’t learn complexity bijections the best.
    - Figure 6 - share the legend so each plot is bigger. The main point you are trying to make is that the capability degrades as fixed size increases, but this message is easily lost with the amount of information you present. I’d recommend simplifying - just show it averaged over models and maybe drop some of the multi-digit results. You can put this plot in the appendix to refer to some nitty gritty details.
    - Figure 7 - I don’t think this is a scaling law. It is more of a Pareto frontier plot where you want to show the trade-off in two metrics. A scaling law would involve the amount of computing, data size, or size of the model. Did you experiment with different fits? A quadratic might not be as good as a higher-order polynomial. Why is a quadratic the right fit for this data?
    - General plotting advice: Please use error bars for all plots that take into account the sample size used (this can just be a standard error of a proportion that doesn’t involve rerunning many seeds). Use a colour-blind pallet, and make the font in figures a similar size as the font of paper.

### Questions
Most of my questions are in the weaknesses section, but here are some other questions/discussion points.

- What does “endless” mean? How is it different from any “adaptive” attack (like PAIR or random search suffixes) that will craft many potential jailbreaks until it finds one that works? I’m not sure emphasising this makes sense. Maybe you reframe it as an “Adaptive in context learning attack”?
- In the abstract, what does universal mean? Is it transferred across harmful requests or across models? Do you have a % of how the same bijection template transfers across requests and across models?
- Multi-turn conversation history - do you think it would be best to use the term few-shot learning here and then, in methodology, talk about how many shots you use (it looks like it is 10-shot?). Also, you call it “teaching examples” later. I would use few-shot since it is clear what it means.
- What defenses work / don’t work against your attack?
- Intro: I wouldn’t describe perplexity filtering, paraphrasing, etc as an alignment technique like RLHF. I’d describe it as an adversarial defense against jailbreaks.
- Maybe add the GPT-4o rewriter to correct typos in Figure 1, so it is clear how it works without needing to read the paper.

This paper has the potential for a much higher rating, but not in its current form. I would happily raise my score if the claims I mention in the weaknesses section are better explained and the results are significantly simplified in the figures and presented well. In addition, I’d like to see the comparison to adaptive black-box attack baselines like PAIR with a comparable attack budget.

### Soundness
3

### Presentation
3

### Contribution
3
