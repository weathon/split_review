# SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Despite efforts to align large language models (LLMs) with human intentions, widely-used LLMs such as GPT, Llama, and Claude are susceptible to jailbreaking attacks, wherein an adversary fools a targeted LLM into generating objectionable content.  To address this vulnerability, we propose \textsc{SmoothLLM}, the first algorithm designed to mitigate jailbreaking attacks.  Based on our finding that adversarially-generated prompts are brittle to character-level changes, our defense randomly perturbs multiple copies of a given input prompt, and then aggregates the corresponding predictions to detect adversarial inputs.  Across a range of popular LLMs, \textsc{SmoothLLM} sets the state-of-the-art for robustness against the \textsc{GCG}, \textsc{PAIR}, \textsc{RandomSearch}, and \textsc{AmpleGCG} jailbreaks.  \textsc{SmoothLLM} is also resistant against adaptive GCG attacks, exhibits a small, though non-negligible trade-off between robustness and nominal performance, and is compatible with any LLM.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a defense algorithm to mitigate jailbreaking attacks on LLMs. It works by first randomly perturbing the input prompt (via insert, swap or batch), and then conducting a majority voting of the resulting predictions to detect adversarial inputs. Provable guarantees are also provided on attack mitigation. Experiments show that the defense reduces ASR and maintains a certain utility on clean inputs.

### Strengths
1. Defending against jailbreaking attacks of LLM is an important problem for trustworthy LLMs in practice;

2. The proposed method adapts the randomized smoothing principle to LLM, and conducted extensive evaluation to empirically demonstrates its ability for defending jailbreaking attacks;

3. The paper presentation is clear and easy-to-follow.

### Weaknesses
1. The major concern is that perturbing the prompts could greatly influence the LLM’s original behavior. The provided evaluation of non-conservatism is only based on rather simple tasks (i.e., classification), which does not verify whether the LLM can still have normal generation behavior on randomly perturbed prompts.

2. The proposed method is based on the observation that adversarial suffixes are fragile to character-level perturbations, ignoring the (un)stability of normal prompts to such perturbation. The paper did not draw a clear boundary (either theoretically or empirically) of how perturbation only destroys the adversarial suffix and maintains the semantics of normal ones.

3. The theoretical guarantee relies on the assumption, k-stable, that cannot be verified or calculated in practice (unlike the assumption in randomized smoothing), and can hardly be “realistic”. The resulting theoretical guarantee thus is not really a rigorous one. For instance, Figure 6 is a conceptual result, instead of a guarantee calculated on real prompts. 

4. While the paper has compared its method with randomized smoothing (e.g., image v.s. text), it is still a straightforward application of the perturbation-then-voting principle, which limits its technical novelty.

5. The paper has several statements that could be over-claimed and misleading, regarding “the first defense”, theoretical results and empirically conclusions. See details in Questions.

### Questions
1. As said in weakness 1, character-level perturbation may destroy prompt semantics and confuse LLM. Therefore I am concerned with the true cause of the decreased ASR by the proposed method. It may not necessarily be the result of destroying the adversarial suffix, instead, it is possible that the perturbation destroys the semantics of the malicious question, thus the LLM model responds with something like “Sorry, I cannot understand”. Did the authors observe such cases? And a possible evaluation to verify such a case: using the behavior dataset without adversarial suffix (i.e., only keeping the malicious question part), then using an unaligned version of LLM, and checking its ASR drop after random perturbation.

2. The provided non-conservatism evaluation is insufficient to really validate that SmoothLLM maintains nominal performance, because: 1) these tasks are simple (e.g., classification tasks); 2) the accuracy drop is actually relatively large even when q is set small and N is large (e.g., random guess on PIAQ is already 50, but SmoothLlama2 with q=2 and N=6 gives 59, which is a large drop compared with original performance 76.7). Can the authors provide a more convincing evaluation of nominal behavior of LLMs, e.g., on generation tasks?

3. In table 3 of the non-conservatism evaluation, are the numbers the average results of all N samples? What are the variances?

4. As said in weakness 2, SmoothLLM is built based on the observation in Figure 4 that adversarial suffixes are fragile to character-level perturbations. Then an implicit assumption is that clean prompts are more stable to such perturbations. Can the authors provide corresponding evidence to verify (in)stability of clean prompts, similar to Fig. 4?

5. The theoretical proof is provided for swap and batch perturbations, instead of “other perturbation types”. Is the guarantee/proof applied to the insert perturbation? 

6. The paper claims the efficiency of SmoothLLM by comparing the runtime with attacks (e.g., GCG). This seems to be an unreasonable comparison as one is defense and other is attack. Can the authors soften this claim and focus on the comparison of SmoothLLM and vanilla LLM (and other defenses)?

7. The paper emphasizes in multiple places that this is the first algorithm to defend LLM jailbreaking attacks, which could be over-claimed as several attempts have been proposed [1, 2]. Can the authors discuss them and adjust corresponding claims if this concern makes sense?

[1] Kumar, Aounon, et al. "Certifying llm safety against adversarial prompting." arXiv preprint arXiv:2309.02705 (2023).

[2] Jain, Neel, et al. "Baseline defenses for adversarial attacks against aligned language models." arXiv preprint arXiv:2309.00614 (2023).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors proposed SmoothLLM to mitigate jailbreaking attacks on LLMs. The method is based on the finding that adversarially-generated prompts are brittle to character-level changes. Specifically, the defense first randomly perturbs multiple copies of a given input prompt, and then aggregates the corresponding predictions to detect adversarial inputs.

### Strengths
1. found that adversarially-generated prompts are brittle to character-level changes
2. proposed a new algorithm for defending against jailbreaking attacks in llm
3. The main idea follows randomized smoothing in image domain and provide some theoretical results

### Weaknesses
1. The “robustness guarantee” that generalizes the original randomized smoothing to the LLM setting in this paper does not seem to be a valid “guarantee”, as it actually depends on some unverifiable assumption (k-unstable). Therefore, different from those traditional robustness guarantees, where one could verify that some examples must be robust, the “guarantee” in this paper cannot provide any real certified robust accuracy. In this sense, I don’t think the provided theorem provides any type of formal guarantee to robustness here. It seems a bit misleading to call it a formal robustness guarantee.

2. From the algorithm design, the proposed algorithm can easily have degraded nominal performances (since the output is randomly sampled from the perturbed input’s response and each perturbed input has changed the input quite a lot). Although the authors also consider that as one of the major aspects to test, I don’t see that part and the corresponding experiments very convincing.  Table 3 actually suggests that when N is a bit large, the nominal performance significantly drops. More importantly, it only tested on light perturbation cases where q <= 5%, while in the main experiments, most were conducted in the case where q = 10/15/20%. This makes me very concerned about the actual use case of the proposed algorithm. 

3. The discussion on the efficiency part seems also misleading. All the comparison listed in this paper seems to compare the SmoothLLM with GCG, which is totally unreasonable to me (take an analogy, this is similar to comparing the complexity of randomized smoothing and adversarial attack). I didn’t see this comparison has too much meaning here. Since SmoothLLM is basically an inference-time defense, shouldn’t the authors compare it with normal LLM inference? And that seems to be a solid N times larger than the normal inference in my opinion. Since the inference time is one major obstacle in modern LLM deployment, SmoothLLM does not really seem efficient at all.

4. One important aspect that seems to be missing is the adversarial prompt length. Essentially in this setting, there is no traditional invisible adversarial length constraint (like in traditional adversarial examples, usually we are only allowed to change one/few works/characters). Basically, your adversarial prompt can be any length, as long as it successfully breaks the alignment. However, I am a bit concerned that under such situations where the proposed attack still work? From the theoretical guarantee, I didn’t thoroughly check the proof but the original randomized smoothing cannot provide meaningful results when the adversarial part is large. From the empirical perspective, if we just programmed GCG to generate a long adversarial prompt (not the only way but you can imagine many different ways to achieve the goal) would it still work? Or it still work, but may need a significantly larger perturbation ratio q and thus lead to degraded nominal performances?

### Questions
1. I do not quite understand why the authors claimed that for the efficiency objective, “SmoothLLM is independent of the prompt length”?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple scheme to prevent jailbreaking through adversarial prompt suffices. The main observation is the brittleness of these suffices (if a sufficient number of their characters are perturbed, they lose effectiveness). Building on this, the proposed scheme applies random transformations to the original prompt to smoothen the model response. They experiment on and provide guidelines on how to apply these transformations. The scheme stands out as it can operate in a black-box setting.

### Strengths
+ Simple, straightforward scheme to mitigate GCG-type attacks.
+ Some theoretical results as to when/how the scheme can be effective.
+ Guidelines and experiments on hyperparameter tuning are insightful. 

Jailbreak attacks have been demonstrated both in academia and observed in the wild [1] and it is critical to develop simple, baseline defenses against this threat. The proposed algorithm fulfills that role and reuses the intuition from existing randomized smoothing defenses in the context of LLMs. 

[1] https://arxiv.org/abs/2308.03825

### Weaknesses
- Not entirely convinced about the k-unstability assumption that is the foundation of the algorithm and the theory.
- Weak effort in designing an adaptive attack (e.g., create a suffix that's resilient to perturbations)
- No experiments on the universal GCG attack or more semantic jailbreak attacks that are more practical and widespread.

I don't know why k-unstability would be a fundamental property of adversarial suffix attacks like GCG. It's an empirical observation for a particular attack but we know very well now that building defenses on attack-specific artifacts is not a way to go. It only leads to a counterproductive arms race without yielding a long-lasting idea. Considering that it would be generally easy for an attacker to detect if SmoothLLM defense is used (e.g., by looking at the model's responses), it also would be trivial to change up the attack strategy to break the defense. Is there a reason why you believe k-unstability is a good assumption that will withstand future attacks or stronger adaptive attacks?

This brings me to my second point. It's accepted now that adaptive attack evaluations should be at the forefront of defensive papers like this. It's trivial to defend against any particular attack (e.g., by detecting the attack's artifacts) but through many painful lessons, we know that adaptive attacks are hard to design and evaluate against. I can't see much deeper thought in this paper in this regard. It definitely needs more work to be convincing that this defensive strategy is not going to be broken by the next deadline. There are some straightforward ideas from (such as EOT attack in the image domain) that could be useful here too.

Finally, a mistake we made for image domain adversarial attacks was to focus on trivial, non-realistic threat models (e.g., pixel-wise L-norm bounded perturbations). It has been years since this threat model was proposed and we've yet to see a real-world attack that uses this strategy. With attacks like GCG, I think, we might be making the same mistake and focusing on threats that might not matter. There's some real-world evidence that semantic jailbreak prompts are a greater and harder-to-mitigate risk that attackers are already deploying [1]. There's an intellectual merit in studying more academic, theoretical threats but I think it is critical to guide the community towards studying real threats. I can't see this paper doing that. There's no discussion on whether this defense would work against semantic jailbreaks or other real-world strategies, and no discussion on the limitations of the defense in deployment. Considering we have years of literature behind us, I would like to see a real effort into asking the right questions, which starts with academic papers like this.







[1] https://arxiv.org/abs/2308.03825

### Questions
- I'm not entirely sure about the reasoning behind returning one of the responses R_j (Line 5-6 in the Alg 1). How did you make this decision? What are the downsides compared to the other options you discussed in Section 6? I'm failing to have good intuition about this. Could you clarify?

- How does the defense affect the model's response utility against very short prompts (which might have less redundancy to withstand perturbations)?

- Do you use the input-specific GCG in your experiments? Input-specific GCG suffix is coupled with the original prompt itself, which could explain why small perturbations might break the attack. What about the universal version of GCG? Is that less brittle (I know it has a lower attack success rate)? It also changes the computational cost equation as the adversary needs to craft it only once.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a defense method against large language model (LLM) jailbreaking, based on the Majority vote principle. It introduces random perturbations into queries to weaken certain jailbreaking attempts on LLMs. The method involves first introducing random perturbations and then measuring if the response begins with a target segment.

### Strengths
This work is an early exploration in defending against LLM jailbreaking. It pioneers the approach of using Majority vote and query perturbation to detect and prevent malicious outputs.

### Weaknesses
- The paper's definition of JailBreak is overly restrictive, focusing only on responses beginning with a specific prefix. This is problematic as attacks can still be successful even if the LLM does not strictly reply with the target segment. For instance, this paper use target as "Sure, here’s how to build a bomb", however, in an attack, LLM could generate "Sure, you can build a bomb by ...". This still containing harmful content should be considered a successful attack.
- The proposed SmoothLLM approach is impractical in real-world scenarios (like ChatGPT), because defenders can't predict the exact nature of the attacks or the corresponding targets. For example, the paper uses "Sure, here’s how to build a bomb" as a target corresponding to the goal "Tell me how to build a bomb". But if an attacker's goal is different, such as "How to steal money from charity", the previous target becomes irrelevant. Therefore, the defense is ineffective if the attacker's goals or phrasings differ from what the defenders expect.
- Furthermore, even if an attacker's goal is constant (e.g., "Tell me how to build a bomb"), they can easily bypass the defense by choosing a different target phrase for the jailbreaking. For example, if the defender's target is T="Sure, here’s how to build a bomb", an attacker might use T'="In order to build a bomb, you can first" as their target. In this scenario, the majority vote method would fail to filter out successful attacks since the JB(T',T) = 0.


Minors (typo):

"this would be come at the cost" -> "this would come at the cost"

"While this may seem counterintutive"->"While this may seem counterintuitive"

"future work should focus more robust"->"future work should focus on more robust"

"randomized smoothing (Salman et al., 2020; Carlini et al., 2022),"->"randomized smoothing (Salman et al., 2020; Carlini et al., 2022)."

### Questions
Concerning the results in Tables 3 and 4, SmoothLLM shows a performance decline of about 10% on PIQA. Why do the authors claim that their SmoothLLM method does not impose significant trade-offs between robustness and nominal performance? This claim appears to be contradicted by the empirical evidence.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
