## Human Reviewer 1

### Summary
This paper investigates how activation steering, both through random directions and SAE-derived concept vectors, can compromise LLM safety mechanisms. The authors test steering across layers and magnitudes on JailbreakBench, showing that middle-layer steering often leads to higher compliance with harmful requests. They further demonstrate that certain SAE features can generalize into universal jailbreak vectors that work across prompts and models. Overall, the paper argues that interpretable steering methods, often assumed to enhance control, can inadvertently weaken safety alignment.

### Strengths
1. **Novelty of motivation**: The paper identifies a previously underexplored safety concern that activation steering, including interpretable SAE-based methods, can unintentionally reduce model safety.
2. **Practical relevance**: The authors demonstrate that SAE-derived features can act as jailbreak tools raises concrete concerns about how interpretability techniques may be weaponized.
3. **Empirical insight**: The finding that middle layers are particularly vulnerable and that steering effects generalize across prompts adds useful understanding to where safety mechanisms fail.

### Weaknesses
1. **Unclear conceptual grounding of steering vectors**: Although the paper motivates activation steering as conceptually meaningful (e.g., France concept in Figure 1), most experiments use Gaussian-random directions. This makes it difficult to interpret what the steering is actually doing beyond injecting noise into activations.
2. **Narrow evaluation scope**: All results are based on JailbreakBench. Testing the same steering methods on other safety benchmarks (e.g., AdvBench[1] or other aspects of safety like privacy and toxicity) and on general capability tasks like MMLU or CSQA could help determine whether the steering trade-offs generalize beyond safety settings.
3. **Weak causal interpretation**: It remains unclear whether steering compromises safety through meaningful feature activation or through general perturbation effects. A more careful causal or ablation-based analysis could clarify the mechanism.

[1] Universal and Transferable Adversarial Attacks on Aligned Language Models, 2023

### Questions
Please refer to weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper examines how activation steering during inference can degrade LLM refusal behaviors. The authors experimented with models like Llama3, Qwen2.5, and Falcon across multiple layers and steering magnitudes, under settings of using random Gaussian vectors and SAE features from pre-trained public SAEs. They measure harmful compliance using LLM-as-judge on 100 harmful prompts. The main finding is that even random or benign steering can raise compliance rates up to 27%. Moreover, combining 20 randomly sampled steering vectors can create a universal attack.

### Strengths
1. **The framing and angle are novel.**
- Prior work emphasized more purpose-built steering vectors, while this paper explores ordinary vectors. Also, the argument that activation steering can be risky is an interesting and underexplored angle.

2. **Aggregating the vectors into a universal attack (Section 4.4) is a simple and neat experiment** that supports the authors’ claim and demonstrates a plausible, real-world threat.

### Weaknesses
1. **Unsteered baseline results are not clear from the paper.**
- In Figures 2, 3, 6, the comparisons begin at nonzero steering coefficients and do not include a no steering condition. And from the paper, it’s ambiguous whether the baselines that the authors refer to are actually measured through unsteered models. Without this it’s hard to interpret the reported changes caused by steering.

2. **Compliance measurement (Section 3.4) is insufficient.**
- The authors consider incoherent or repetitive outputs as safe, and this design choice can potentially lead to false negatives. Although some quality assessment is done (Appendix B),  this is only based on precision.
- For reported compliance rates across figures, no uncertainty quantification such as confidence intervals is provided.

3. **SAE feature selection process is not clear enough.**
- The paper highlights a few high impact features like “brand identity” (Figure 4), but it’s unclear the total number of features tested, whether the reported features were cherry-picked, or how labels were assigned.

### Questions
1. Out of the 668 SAE features that can jailbreak at least five prompts, is this distribution uniform or concentrated around specific semantic types, like emotion, identity, etc?

2. What is your hypothesis on that semantically benign SAE concepts can jailbreak harmful prompts, for example, whether this is due to linear compositionality (ex. features accidentally aligning with refusal-suppression directions) or something else?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper presents evidence that steering LLM activations with random vectors and benign SAE features makes LLMs more susceptible to jailbreaking. It further explores combining jailbreak-inducing random vectors to create a "universal" attack vector.

### Strengths
The paper identifies a potentially important and underappreciated threat vector. A finding that a large majority of randomly chosen directions increase jailbreak susceptibility is surprising enough to be important, and jailbreak susceptibility induced by steering with benign SAE features has practical relevance.

### Weaknesses
The claim made in the abstract and introduction that steering with benign SAE features is even more alignment-breaking that steering with random directions appears to be based on a single prompt and model, evaluated at a depth that's not optimal for random directions (Figure 2); the more comprehensive evaluation shown in Figure 3 shows precisely the opposite, with Llama3-8b-it compliance rates much higher with random vectors on every prompt category save one. This claim also appears misleadingly in the Conclusion, where random steering on one model is compared with SAE steering on another.

The judge model used is quite small, despite the fact that much better models could be used at very modest cost. The authors argue that manual labelings mostly agreed with the model; still, this is an unnecessary source of uncertainty added to critical evaluations.

Figures lack confidence intervals.

Figure 4b is quite hard to interpret on its own. 

The claim that to be used as an attack this method only requires "black-box API access" (line 461) seems misleading, as with the exception of Goodfire's research API designed specifically for this purpose, hosts do not allow steering via API; the practical implication of this work are that researchers should test for jailbreak vulnerability before deploying steering to production.

### Questions
Figure 2b shows a Llama3-8b-it 2/3rds depth random steering compliance rate across scaling coefficients that differs from the one shown in Figure 2c; why?

How were the 1000 SAE features chosen?

What temperature(s) was used?

Can you clarify the methods for creating the universal attack vector? What does "top 20 vectors that successfully induce compliance" mean? There's only one prompt, so each vector either induces compliance or doesn't. Why do you need "100-500" trials to identify them? What is the dependence on "the model's baseline vulnerability" mean? If the baseline compliance rate is not ~0%, then it's important to show it in Figure 3.

What do you think explains your findings? It seems quite surprising that steering with most SAE features would lead to alignment breaking. Anthropic opened up a "Golden Gate Bridge" feature-steered model to the world, with no apparent jailbreaking issues; did they just get lucky?

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper asks whether activation steering for the purpose of inducing a behavior unrelated to safety (e.g. style transfer) may inadvertently cause jailbroken behavior. The authors find that indeed activation steering even with random vectors consistently induce jailbroken behavior. They find that when using SAEs as a source of steering vectors this effect is exacerbated. The authors introduce a technique for "universal" jailbreaking: averaging a sample of random vectors that have proven effective against certain attacks.

### Strengths
The paper studies an important area: inadvertent jailbreaking as a result of inference time interventions designed for an unrelated purpose, such as steering with SAEs. The authors study different danger categories when it comes to jailbreaking and measure their cross generalization.

### Weaknesses
I would have liked to see results not just for random vectors but also for steering vectors that were actually trained for some benign purpose from the literature - do meaningful steering vectors also induce jailbroken behavior? For example, it has also been reported in the literature (Ghandeharioun 2024 - https://arxiv.org/pdf/2406.12094) that steering vectors may inadvertently cause increased refusal behavior. Also the steering coefficients at which the authors observed misaligned behavior (>1) is generally outside the recommended regime for use.

I also feel that the core result: random vectors induce misalignment - is well predicted by the literature. For example Qi 2024 - https://arxiv.org/pdf/2406.05946, and especially Qi 2023 - https://arxiv.org/pdf/2310.03693 (Fine-tuning aligned language models compromises safety even when users do not intend to! - which the authors cite), also Peng 2024 - https://arxiv.org/pdf/2405.17374v1 - regarding the fragility of safety alignment.

### Questions
What is the recommended steering coefficient when using SAE features? It seems it's only problematic / jailbreaks the model near 2.0. At that point, is the original intended behavior of SAE feature preserved?

If possible, it would be great to use a more powerful model to classify safe / unsafe than Qwen 8B. 

nit: Figure 2 - I think it would help with clarity to use the same y-range across all 3 figures.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
3