# You Know What I'm Saying: Jailbreak Attack via Implicit Reference

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
While recent advancements in large language model (LLM) alignment have enabled the effective identification of malicious objectives involving scene nesting and keyword rewriting, our study reveals that these methods remain inadequate at detecting malicious objectives expressed through context within nested harmless objectives.
This study identifies a previously overlooked vulnerability, which we term \textbf{A}ttack via \textbf{I}mplicit \textbf{R}eference (\textbf{AIR}). AIR decomposes a malicious objective into permissible objectives and links them through implicit references within the context. This method employs multiple related harmless objectives to generate malicious content without triggering refusal responses, thereby effectively bypassing existing detection techniques.
Our experiments demonstrate AIR's effectiveness across state-of-the-art LLMs, achieving an attack success rate (ASR) exceeding \textbf{90\%} on most models, including GPT-4o, Claude-3.5-Sonnet, and Qwen-2-72B. Notably, we observe an inverse scaling phenomenon, where larger models are more vulnerable to this attack method. These findings underscore the urgent need for defense mechanisms capable of understanding and preventing contextual attacks. Furthermore, we introduce a cross-model attack strategy that leverages less secure models to generate malicious contexts, thereby further increasing the ASR when targeting other models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Attack via Implicit Reference (AIR) that decomposes a malicious objective into nested harmless objectives. AIR framework has a 2-step attack approach, wherein in the first step it uses LLM to rewrite the original malicious objective into nested objectives, and in the second step it uses multiple objectives to refine the model's response. The authors show that this technique jailbreaks LLMs. It shows higher ASR on state-of-the-art LLMs and also shows that ASR increases with increasing the size of the target model. This paper also shows cross model attack.

### Strengths
1. This paper shows good ASR on SoTA LLMs IN Table 1. 
2. The authors also show cross model attack in Table 2 (as explained in the algorithm).
3. The authors compare their attack with baseline defenses and report the rejection rate in Table 5.

### Weaknesses
1. There is not much information available regarding the dataset details, like the number of samples during the training approach in the experimental section 4.1.
2. This method makes use of LLM calls thrice in the method - once while rewriting the input prompt and next two times in the first and second stage of attack respectively. Three calls to an LLM for a single prompt is expensive with respect to time taken to rewrite a prompt. The authors should comment on the inference time of their approach so as to make it feasible to use their approach in practical scenarios.
3. The paper is not very well written. There are some spelling mistakes on lines 40, latex syntax error in algorithm section "iscrossmodel".
4. Overall, the paper is not well presented and lacks novelty. Like the "Continue Attack" in section 3.2 is just addition of a prompt-based filter. Prompt-based filters have been used before like in the work titled "LLM Self Defense: By Self Examination, LLMs Know They Are Being Tricked".

### Questions
1.  First Attack Success Rate (FASR) is used in Table 1 across all approaches. It would be helpful to reader if the calculation method or reference to FASR is provided or does it simply mean ASR in the first stage of attack? The authors must define this in paper as it may be confusing to the readers.
2. How the authors arrive at Equation 2 ? This needs to be explained in detail.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a jailbreak attack referred as Attack by Implicit Reference (AIR). AIR decomposes a prompt with malicious objective into nested prompts with benign objective. This method employs multiple related harmless objectives to generate malicious content without triggering refusal responses, thereby effectively bypassing existing detection techniques. AIR achieves attack success rate (ASR) of more than 90% on open-source and close-source LLM. It is highlighted that heavier model, i.e. models with more parameters, are more vulnerable to Jailbreak than heavier models.

### Strengths
1. The AIR method achieves a high ASR (above 90%) on models with large number of parameters.
2. The Cross-model strategy, wherein, a less secure model is targeted first to create malicious content, which is then used to bypass more secure models, emphasizes the potential transferability of vulnerabilities between LLMs.
3. The paper identifies an inverse relationship between model size and security, highlighting that larger model, typically with enhanced in-context learning capabilities, are more susceptible to AIR.

### Weaknesses
1. The success of the AIR method appears to heavily rely on models with high comprehension abilities, specifically in areas like nuanced language understanding, contextual retention, and sophisticated in-context learning. These capabilities are essential because AIR requires the model to maintain and link fragmented, implicitly harmful objectives across multiple interactions without overtly identifying them as malicious. Authors should test this with lighter models (models with fewer parameters) like LLaMa-3-8B and Mistral-7B etc.
2. While the paper evaluates existing defenses (e.g., SmoothLLM, PerplexityFilter), there’s a lack of exploration or proposal for new countermeasures against AIR. Further suggestions on possible defenses could enhance the practical value of the paper.
3. In principle the AIR attack looks very similar to other template based/ word substitution attacks example- (i) When "Competency" in Reasoning Opens the Door to Vulnerability: Jailbreaking LLMs via Novel Complex Ciphers by, Handa et. al., (ii) Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks, by Andriushchenko et.al. . Therefore, the novelty in the approach is not apparent. Authors should highlight what makes these attacks unique compared to the other template based or word substitution attacks.

### Questions
1. In the Introduction Section, line number ‘040’, ‘cyber-attacks’ have not been spelled correctly. Kindly do the needful.
2.  Refine Cross-Model Strategy Analysis, by optimizing the selection criteria for initial "less secure" models in cross-model attacks could be beneficial for replicating or further developing this approach.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new jailbreak method **AIR**, which decomposes the malicious objectives into nested harmless objectives and uses implicit references to cause LLMs to generate malicious content without triggering existing safety mechanisms. In the first stage, AIR bypasses the model's rejection mechanism by breaking down malicious into nested benign objectives. In the second stage, AIR sends a follow-up rewrite request that includes implicit references to the content generated for the second objective in the previous stage
while excluding any malicious keywords. Experiments have shown the effectiveness of AIR and some other insights.

### Strengths
1. The introduction of "nesting objective generation" is interesting.

2. The paper is easy to follow.

### Weaknesses
1. While interesting, as the motivation and basis of your method, Section 2.3 "Nesting Objective Generation" needs more detailed analysis. You could add more analysis about the connection between the attention mechanisms and your proposed concept (nesting objective generation and implicit inferences). For example, you could analyze how the attention mechanism affects the nesting objectives. The existing version makes Section 2.3 more like a guess.

2. This paper needs to be polished in its writing, for example, the full name and abbreviation of LLM are mixed. This reviewer suggests using the full name "Large Language Model" on the first mention, followed by "LLM(s)" thereafter.

3. The technical contribution is limited, especially "Cross-Model Attack". As you cite as the baseline, PAIR and its following version TAP both employ another LLM as an attacker or the red-teaming assistant to attack the target model. You should explicitly highlight the difference between your paper with other related papers and are recommended you provide a comparative analysis to demonstrate your unique contributions.

4. What is the evaluation method used in your experiment? You mentioned in "Evaluation Metrics" part that this paper employed three complementary evaluation methods. However, you should provide a clear breakdown of which evaluation methods were used of each experiment. If all of the three metrics are used, please give more details about how these three are balanced.

5. Section 5 is more like experiment part than analysis. In this section, you give some "insights" such as the impact of LLMs' size and the number of objectives. However, this section lacks of detailed disccusion or further analysis behind this phenomenon.

### Questions
1. Which part is the main contribution of this paper? If the introduction of nesting objective generation, see weakness 1. If the method and cross model attack, see weakness 3.

2. See weakness 4. What is the evaluation method used in your experiment?

3. See weakness 5.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work propose a new jailbreak attack against Large Language Models (LLMs), namely Attack via Implicit Reference (AIR). The design is to decompose a malicious objective into permissible objectives and links them through implicit references within the context. The experiment shows the effectiveness of the proposed attack. Also the evaluation on some defenses shows the robustness of AIR attack.

### Strengths
- The motivation and attack design is intuitive and straightforward.
- The experiment setup covers different sets of LLMs, including both open-sourced and closed-sourced models and in different size.
- The evaluation results shows the proposed method is relatively efficient compared to baselines.

### Weaknesses
 - The evaluated samples is relatively small (i.e., 100), for some studies shows only marginal difference, e.g., Table 4 and 5, confidance interval is necessary to make the conclusion.
- Attack baseline setup needs justification. Specifically, the proposed attack shared some insight from contextual attack, and multi-turn attack, while the compared baselines may not strictly fall into the same category. Some more related work, such as COU[1], COA[2] and ArtPrompt[3], is expected. 
- Defense baseline setup needs justification. Specifically, the evaluated defense baselines are primarily designed for attack that generated adversary tokens, which is quite away from the proposed attack. Though it is ok to include these defense, but it is necessary to cover more defense that may be more suitable for contextual and multiturn attack, such as moderation-based defense. 



### Questions
- The notation and definition in Sec. 2.3 is confusing. What is the support set of objectives, in text/tokens/embeddings space? What is the sum of objectives? How is $\alpha$ defined, and in the LLM backbone, there are various attention layers and heads, how do these count together?
- The conclusion in Sec 5.1 is interesting but under-explored. In particular, as the model size get larger, the general ability including rewriting is increasing as well as the safety awareness, the trade-off is more interesting to me. I would expect to see a study on a more fine-grained family (e.g., QWen 2.5 with 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B variants), to see if there is any turn-over point along the evaluation. Also, I would expect an experiment to use the same model for the first stage, e.g., gpt-4o, then use each of the victim models for the second stage. Then the relationship is more straightforward.
- Overall, I did not see the distinguishment between the proposed attack and some related work, especially contextual attack and multi-turn attack, and therefore, the novelty of so-called implicit reference design is unclear.

### Soundness
2

### Presentation
3

### Contribution
2
