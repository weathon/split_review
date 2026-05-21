---
job_id: 82a32a2e-ba83-465d-8319-075aec316ba5
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: VbTLgEUocp.pdf
paper: LLMs Can Hide Text in Other Text of the Same Length
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through generative modeling, language models, steganography with LLMs, and AI safety implications.

## Minimum Quality
Pass ✅. The paper contains an abstract, introduction, related work, a clearly described method, quantitative and qualitative empirical analysis, and a conclusion/discussion. While several claims are overstated and the empirical study is narrower than ideal, the submission clears the minimum bar for a full scientific review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts or reviewer-targeted manipulations in the paper content. The paper studies text hiding as its scientific topic, but this is presented openly as the object of study rather than as an attempt to manipulate the review process.

# Expected Review Outcome:
## Summary
This paper presents **Calgacus**, a very simple rank-based protocol for hiding a text \(e\) inside another plausible text \(s\) of the same token length using an autoregressive LLM. The encoder records the rank of each token of \(e\) under the model, then regenerates \(s\) under a secret prompt \(k\) by choosing at each step the token with the same rank; decoding reverses this process given the same model and key.

The paper argues that this gives a full-capacity steganographic channel in the sense that the stegotext has the same token length as the hidden text, and it explores plausibility, detectability, and security implications, including a concrete AI-safety scenario where a compliant visible response could conceal an unsafe hidden one.

## Strengths
1. **The core idea is simple, clean, and easy to verify from the paper.**  
   The main protocol in **Section 3** and **Figure 3** is unusually direct: extract rank sequence from \(e\), then replay the same ranks under prompt \(k\) to generate \(s\). This simplicity is a real strength because the reader can immediately understand both encoding and decoding, and the claimed same-length property follows naturally from the token-by-token construction.

2. **The paper makes a clear and concrete point that differs from standard “bits hidden in text” framing.**  
   The emphasis on hiding a meaningful text inside another meaningful text of the same length is interesting and operationally distinct from many steganography papers that focus on bit payload, distribution matching, or low-rate embedding. Even if the underlying mechanism is simple, the formulation is memorable and the paper communicates it effectively.

3. **Some figures are genuinely helpful rather than decorative.**  
   In particular, **Figure 1** is a strong opening example because it makes the contribution legible immediately: the same hidden message is rendered as two very different plausible texts, one culinary and one political. Likewise, **Figure 3** does a good job visualizing the rank-preservation idea with token ranks and generated continuations, and this substantially improves clarity over the textual recipe alone.

4. **The paper includes an intuitive diagnosis for why stegotexts are typically less probable than the original texts.**  
   The discussion around low-entropy token choices in **Page 5-6**, supported by **Figure 5**, is one of the more insightful parts of the submission. The contrast between rank preservation and probability preservation is important, and the histograms for rank-1, rank-2, and rank-3 tokens help explain why preserving ranks does not preserve overall likelihood.

5. **The empirical section, while limited, does support the basic plausibility claim.**  
   **Figure 4** shows that the cumulative log-probabilities of generated stegotexts fall within the distribution of 1000 real Reddit texts, while random ASCII or random English-word strings do not. This is not a full security evaluation, but it does support the narrower claim that the outputs are often plausible rather than degenerate nonsense.

6. **The paper does not hide important practical caveats.**  
   I appreciated that the authors explicitly state on **Page 6** that sender and receiver must run the chosen LLM under identical conditions and obtain identical logits. This is a serious limitation, but the fact that it is acknowledged in the main paper improves trustworthiness.

7. **The cross-model plausibility check is useful.**  
   **Figure 14** suggests that the real-vs-fake likelihood gap is not purely an artifact of scoring stegotexts with the same model used to create them. This strengthens the claim that the generated texts may remain statistically atypical in a broader sense, which is relevant for detectability.

8. **The model and domain sensitivity analysis is informative.**  
   **Figure 7** and **Figure 8** provide useful qualitative evidence that success depends strongly on how well the underlying LLM models the source domain and how capable the model is. I especially liked **Figure 7**, where chess and Python can still produce somewhat coherent Oxford-themed prose while Romanesco fails badly. This concretely demonstrates where the method is likely to break.

## Weaknesses
1. **The paper overstates its security claims relative to the evidence actually provided.**  
   The title and framing suggest a broad capability, but the main technical evidence is mostly about plausibility, not security under realistic steganalysis. In **Section 3.1 (Page 6-7)**, the paper discusses key guessing and deniability largely at a high level, with an upper bound \(O(d^{|k|})\) for brute force and qualitative speculation that adding random strings helps. This is not a real security analysis. It ignores structured key spaces, semantic priors over prompts, and attack strategies that search for prompts maximizing decoded plausibility or mutual consistency. For a steganographic paper, this matters a lot: plausibility to a human reader is not the same as concealment against an informed adversary.

2. **The empirical evaluation is too narrow for the breadth of the paper’s claims.**  
   The quantitative study on **Page 5** uses 1000 Reddit posts of fixed length 85 tokens, and then selects only three originals, at \(\mu\), \(\mu-2\sigma\), and \(\mu+2\sigma\), to generate 100 stegotexts each. That is a very small slice of the space of possible messages. The paper then uses this to support broad claims about meaningful hidden text and plausibility. This matters because the method is explicitly sensitive to domain, prompt, and model, as the authors themselves show in **Figure 7** and **Figure 8**. A method with such strong conditional behavior needs a broader and more systematic evaluation.

3. **The paper lacks proper baseline comparisons to prior LLM steganography methods.**  
   The related work section cites several relevant generative steganography papers, including Meteor, Wu et al., and Zamir, but there is no direct experimental comparison on capacity, quality, detectability, or decoding reliability. As a result, it is hard to judge whether the practical value of “same-length meaningful text” outweighs what may be a substantial detectability cost. This is especially problematic because the paper repeatedly argues significance through the “full capacity” property, but does not show where Calgacus sits on the usual tradeoff frontier relative to prior methods.

4. **The paper’s quantitative notion of “soundness” is too weak to support some of the wording around meaningfulness.**  
   On **Page 5**, the paper defines \(p(A)=\prod_{t=1}^{n} p(a_t \mid a_{<t})\) and uses cumulative log-probability as a proxy for plausibility for equal-length texts. That is acceptable as a rough diagnostic, but the text frequently slides between plausibility, soundness, coherence, meaningfulness, and security. Those are not interchangeable. A text can have normal perplexity and still be obviously machine-generated, semantically incoherent at larger scale, or easy to detect using a specialized classifier. The histogram in **Figure 4** is therefore suggestive, not sufficient, and the paper should be much more careful in limiting its claims.

5. **Some mathematical and probabilistic statements are informal to the point of being shaky.**  
   The explanation in the low-entropy section on **Page 5-6** says “we can reasonably model the ranks we obtain from \(e\) as a random process” and then estimates the probability of rank 1 by empirical frequency. This may be useful intuition, but it is not a derivation, and the paper uses it to motivate a fairly strong explanation of the probability gap. More generally, the notation around text probability should specify whether BOS/EOS and prompt tokens are included, whether ranks are computed over the full vocabulary including special tokens, and how ties are resolved. Since exact rank recovery is the entire protocol, underspecifying rank definition is not a minor issue.

6. **The practical assumptions are restrictive enough that the claimed threat scenarios feel somewhat underdeveloped.**  
   The protocol requires white-box access to logits and identical model/tokenizer behavior between sender and receiver, as admitted on **Page 6**. In the AI-safety scenario in **Page 7-8**, this assumption becomes central: the user must reproduce the same open-source model behavior locally. That does not invalidate the method, but it substantially narrows deployment realism. The paper’s discussion is strongest as a proof-of-possibility argument, weaker as a near-term practical attack blueprint.

7. **The presentation, while engaging, often slips from scientific argument into essayistic rhetoric.**  
   Large parts of the introduction and discussion, especially on **Page 1** and **Page 7-10**, are written in a philosophical and provocative style. Some readers will enjoy this, but it comes at a cost: the paper sometimes blurs the boundary between demonstrated results and broader social extrapolation. Statements like “end of history itself” or the stronger claims about intent and hallucination are not supported at the same level as the technical claims. For ICLR main track, the paper would benefit from a sharper separation between measured findings and speculative interpretation.

8. **Several qualitative examples actually reveal failure modes that deserve more systematic treatment.**  
   **Figure 8** is useful, but it also highlights how uneven the method is across models. Phi3-3.8B and GPT2 examples are visibly poor, and even some “good steering” examples contain obvious artifacts. **Figure 13** similarly shows that code-like outputs are brittle. These are not mere aesthetic issues; they are evidence that the method’s “same-length plausible text” claim depends on a rather forgiving definition of plausibility. The paper should quantify these failures more directly instead of mostly relegating them to illustrative examples.

9. **The deniability discussion is intriguing but not convincingly established.**  
   In **Section 3.1**, the paper claims deniability because some bogus prompts can yield plausible decoded messages with probability comparable to the true message, with **Figure 15** as a toy example. But one example is not enough to support deniability as a property of the scheme. Deniability is a strong notion in cryptography and steganography; here it is demonstrated only anecdotally. The paper should either weaken the claim or provide a more systematic empirical search over alternate keys and decoded outputs.

10. **There are signs of insufficient polish in the manuscript.**  
   The references section is messy, with malformed entries and apparent corruption near the end, for example on **Page 10-13**. There are also several typographic and grammatical issues throughout the examples. These do not negate the contribution, but they do affect confidence in the care with which the paper was prepared.

11. **The related-work positioning is not fully convincing around imperceptibility and detection-resilience.**  
   The paper cites several generative steganography works, but the discussion centers mostly on capacity and conceptual framing. There is much less engagement with prior work whose main goal is near-imperceptibility or distribution preservation. Since Calgacus appears to trade detectability for full payload capacity, the paper should position that tradeoff much more explicitly, both conceptually and empirically.

12. **The safety discussion is important, but the paper underexplores countermeasures.**  
   The gas-meter example in **Figures 11 and 12** is memorable and makes the threat concrete, but the paper mostly stops at illustrating the risk. There is little analysis of obvious defenses, such as rank-randomization, logit perturbation, watermarking, prompt filtering, response canonicalization, or dedicated steganalysis detectors. For an ICLR audience, a stronger security paper would not just present the attack channel, it would also characterize at least some defensive levers.

## Questions
1. **How often does exact decoding fail in practice under small implementation mismatches?**  
   The paper notes on **Page 6** that sender and receiver must obtain identical logits. Please provide quantitative evidence on sensitivity to common sources of mismatch, such as different quantization levels, GPU/CPU inference, library versions, or sampling backends. A rebuttal with even a modest robustness table would materially improve my confidence in the practical relevance of the protocol.

2. **Can the authors provide direct comparisons with prior LLM steganography baselines?**  
   In particular, I would like to see capacity, text quality, and detectability compared against at least one or two representative prior approaches already cited in **Section 2**. Without this, it is hard to assess whether the same-length property yields a worthwhile tradeoff.

3. **How should rank ties and special tokens be handled exactly?**  
   Since the protocol depends on exact rank recovery, please specify the rank convention precisely. Is the rank computed over the full tokenizer vocabulary including special tokens? How are ties broken? Are BOS/EOS or chat-template tokens included? These details affect reproducibility and correctness.

4. **Can you strengthen the empirical claims about detectability?**  
   Right now the paper mainly evaluates log-probability under LLMs. Could the authors report results from a dedicated classifier or steganalysis detector trained to distinguish real vs fake texts, or at least a stronger unsupervised detector than simple likelihood? If such detectors perform well, the paper’s claims about concealment need reframing; if they fail, that would significantly strengthen the work.

5. **How general is the “plausible same-length text” phenomenon across domains and languages?**  
   **Figure 7** suggests strong dependence on domain familiarity, and **Figure 6** gestures at multilingual examples, but the main quantitative evaluation is narrowly English/Reddit. A rebuttal clarifying whether the authors tested other languages or more formal domains would be helpful.

6. **Can the deniability claim be made more systematic?**  
   Rather than one toy example in **Figure 15**, can the authors report how often alternate prompts produce plausible decoded messages with similar likelihood to the true \(e\)? This would help determine whether deniability is an occasional curiosity or a robust property.

7. **What is the strongest concrete countermeasure the authors have tried, and does it break the channel?**  
   Even a brief experiment applying a simple defense, such as adding tiny logit noise or response paraphrasing, would help readers understand whether the attack relies on a brittle exactness or survives realistic perturbations.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper explicitly presents a channel for concealing harmful or policy-violating content inside apparently compliant text, and **Figures 11 and 12** instantiate this with instructions for tampering with a gas meter. The paper does include a warning not to do so, but it still provides a concrete harmful-use pathway that could facilitate circumvention of safety controls.

More broadly, the paper argues that aligned visible outputs can carry hidden unsafe answers, which has clear implications for misuse, platform abuse, covert communication, and evasion of content moderation. I do not view this as a reason for rejection by itself, since the safety relevance is real, but it does merit ethics review and careful consideration of whether the level of procedural detail is necessary.

## Soundness Rating
3: good.  
The central mechanism is technically straightforward and the basic proof-of-possibility claim is supported, but the security and detectability claims are only partially substantiated, and the experiments are too narrow for some of the broader conclusions.

## Presentation Rating
3: good.  
The paper is readable and memorable, with several effective figures, especially **Figures 1, 3, 4, and 5**. However, the writing is often more rhetorical than scientific, and there are noticeable issues in precision and manuscript polish.

## Contribution Rating
3: good.  
The paper offers a clear and interesting formulation with a very simple protocol and relevant safety implications. That said, the contribution is limited by insufficient comparison to prior work and by a relatively shallow empirical characterization of the claimed steganographic properties.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I lean positive because the paper contains a simple, memorable, and genuinely thought-provoking technical idea, and the main claim, that meaningful text can often be hidden in another plausible text of the same length via rank replay, is convincingly demonstrated. I remain hesitant because the evaluation is narrow, the security analysis is much weaker than the rhetoric suggests, and the paper needs sharper positioning against prior steganography work. Still, I think the proof-of-possibility result and AI-safety relevance are enough to put it slightly on the positive side of the line.

## Reviewer Confidence
4: confident.  
I am confident in this assessment. The core method is simple enough to verify from the paper, I checked the equations and the main empirical evidence carefully, and my uncertainty is mostly about how much weight to place on the paper’s broader framing versus its narrower demonstrated result.