---
job_id: 4f022d4e-ae23-4333-80c8-82909acb9488
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: uXecy0nKiJ.pdf
paper: The Rogue Scalpel: Activation Steering Compromises LLM Safety
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on LNN/representation-level interventions, activation steering, mechanistic interpretability, and safety of learned representations.

## Minimum Quality
Pass ✅. The paper includes the expected scientific components, namely Abstract, Introduction, Related Work, Methodology, Experiments, quantitative/qualitative results, and Conclusion. While I have substantial concerns about experimental design and claim calibration, these are review-stage weaknesses rather than desk-reject-level failures.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies the safety risks of activation steering in aligned LLMs. The authors show that adding steering vectors at inference time, including random directions and SAE-derived benign-looking features, can increase harmful compliance on JailbreakBench prompts, and they further construct an aggregated “universal” steering attack by averaging prompt-specific jailbreak vectors. The paper evaluates multiple open-weight model families, analyzes layer and coefficient sensitivity, and includes a case study using a public SAE steering API.

## Strengths
The paper asks an important question. A large amount of recent work presents activation steering as a precise and interpretable control mechanism, so systematically testing whether such interventions can erode refusal behavior is timely and relevant to ICLR’s representation learning and safety communities.

The empirical message is easy to understand and, at least at a coarse level, plausible: representation-space interventions can have unintended side effects on safety. I appreciated that the paper does not restrict itself to handcrafted adversarial steering vectors, but also looks at random vectors and SAE features, since this broadens the discussion from “attacks exist” to “the intervention class itself may be risky.”

The setup spans several model families and scales, rather than a single cherry-picked checkpoint. The cross-model perspective in **Figure 2a** and **Figure 6** is useful because it shows that the effect is not unique to one architecture. In particular, **Figure 6** gives a clear visual summary that averaging successful prompt-specific vectors can materially increase compliance over random directions for several models.

The paper contains some effective figures. **Figure 1** is a good high-level illustration of the claimed failure mode, and **Figure 4a** is informative because it conveys that dangerous SAE features are not isolated outliers. Even though I have reservations about some interpretations, the histogram is a useful way to communicate distributional behavior rather than only reporting mean compliance.

The qualitative case study in **Figure 5** is also helpful. The two examples make concrete the “disclaimer-then-compliance” pattern that often gets lost when papers report only a binary unsafe/safe score. That figure supports the claim that binary refusal metrics can hide a more subtle behavioral failure mode.

The paper is generally readable. Sections 3 and 4 are organized in a way that makes the experimental story straightforward to follow, and the main intervention itself is simple and transparent, especially through **Equation (3)**.

## Weaknesses
I have several substantial concerns. The core issue is not that the paper’s phenomenon is implausible, it is that the current evidence does not fully support the breadth of the claims being made.

1. **The central claims are stronger than what the evaluation setup can justify.**  
   The paper repeatedly frames the result as showing that activation steering “systematically breaks model alignment safeguards” and “consistently compromises safety mechanisms” (Abstract, Pages 1-2, and throughout Section 4). However, the empirical metric is a single binary compliance rate on 100 harmful prompts from JailbreakBench, judged by another LLM, under greedy decoding. This supports a narrower claim, namely that certain steering interventions increase unsafe compliance on this benchmark under this decoding policy. It does not by itself establish a general statement about “alignment safeguards” as a whole, nor does it isolate whether the intervention truly targets refusal circuitry rather than causing broader distribution shift, degraded calibration, or prompt-specific instability.  
   Why this matters: the paper is trying to make a field-level argument against a safety narrative around interpretability-based control. That requires a more careful distinction between benchmarked harmful compliance and the more sweeping notion of alignment failure.

2. **Hyperparameter selection appears entangled with the test benchmark, which weakens the strength of the reported rates.**  
   In Section 3.2 the authors choose layer locations and coefficients from a small set, then in Section 4.1 they sweep these choices on a single harmful prompt to identify vulnerable configurations, and in Section 4.2 they use selected settings for the full JailbreakBench evaluation. This is not outright invalid, but it is a form of attack tuning using harmful prompts from the same benchmark family. The universal attack in Section 4.4 is even more explicitly optimized by selecting vectors that already jailbreak a harmful prompt, then testing on the remaining 99 prompts.  
   Why this matters: for a security paper, tuning attacks is expected; for a scientific claim about the inherent safety properties of activation steering, one needs a cleaner separation between exploratory search and held-out evaluation. Otherwise the reported “systematic vulnerability” risks being partly an artifact of attack construction and benchmark reuse.

3. **The comparison between random steering and SAE steering is not apples-to-apples enough to support the interpretability claim.**  
   The paper’s headline is that benign SAE features are comparably dangerous to random directions. But the SAE experiments are only on Llama3.1-8B, at a fixed SAE layer supplied by Goodfire, while the random-vector experiments span other models and layers. Even within the single-prompt sweep, **Figure 2c** compares random and SAE vectors “under identical conditions,” yet the text elsewhere states that the SAE investigation is limited to a specific model and layer because only that SAE is available (Section 3.3). The scope mismatch makes the conclusion sound broader than the actual evidence.  
   More importantly, the paper interprets benign semantics of SAE features as evidence that “interpretability does not imply safety.” That may be directionally true, but the paper does not show that these feature labels are reliable, stable, or mechanistically meaningful for the jailbreaking behavior. It mostly shows that labeled SAE features can be used as steering vectors and sometimes cause harmful compliance.  
   Why this matters: the paper’s strongest conceptual punchline is aimed at the safety-through-interpretability narrative, so this part needs much tighter evidence and more cautious language.

4. **The judge-based evaluation is only partially validated, and the way it is validated is one-sided.**  
   Section 3.4 defines compliance via an LLM-as-judge, and Appendix B reports a precision estimate on 100 responses already classified as harmful. This checks only one side of the error profile, namely false positives among predicted unsafe outputs. There is no estimate of recall, no calibration study for borderline disclaimer-then-compliance cases, and no category-wise reliability analysis. In addition, the rule that incoherent or repetitive responses are always counted as SAFE can be reasonable operationally, but it also means the paper’s metric mixes “not harmful” with “harmful but garbled” in a way that may distort comparisons across coefficients and layers.  
   Why this matters: many results hinge on differences of a few percentage points, especially the claim that SAE steering is 2-4% more dangerous than random steering in **Figure 2c**. Without stronger annotation reliability, it is hard to know whether such small margins are meaningful.

5. **There is too little statistical treatment for claims based on modest percentage differences.**  
   The paper reports averages over 1,000 vectors and includes visible error bars in **Figure 2** and **Figure 6**, which is good, but the paper does not clearly specify what those intervals represent, nor does it provide formal significance testing or uncertainty estimates for key pairwise conclusions. For example, the claim that SAE steering gives a 2-4% higher compliance rate than random steering in **Figure 2c** is one of the central takeaways, yet the figure itself suggests overlap may matter depending on the interval definition. Similarly, **Figure 3** reports category-level compliance rates, but there is no statistical discussion of variation across prompts within categories.  
   Why this matters: when the paper moves from “non-zero vulnerability exists” to “SAE features are more dangerous” or “middle layers are maximally vulnerable,” the burden of evidence becomes higher.

6. **The universal attack construction in Section 4.4 is interesting but under-controlled.**  
   The method selects 20 successful vectors for one prompt, averages them, renormalizes, and evaluates on the remaining 99 prompts. This indeed shows some transfer, but the paper does not compare against several obvious baselines: averaging 20 random vectors regardless of success, averaging the top-20 by some non-safety proxy, or selecting 20 vectors that increase verbosity/coherence but do not jailbreak. **Figure 6** includes “random direction,” “individual unsafe direction,” and “average of 20 unsafe directions,” which is useful, but it still does not isolate whether the gain comes from success-conditioned selection, from simple variance reduction by averaging, or from accidental alignment with a broader unsafe subspace.  
   Why this matters: the universal-attack result is one of the most consequential claims in the paper. Right now it is suggestive, but it does not fully disentangle mechanism from construction heuristic.

7. **The layer analysis is narrower than the text suggests.**  
   Section 3.2 says the authors consider three canonical depths, and **Figure 2b** shows layer dependence, but the analysis is only on one prompt and appears limited to a small number of models. The text then interprets this as evidence that “safety mechanisms are most vulnerable in intermediate processing stages” (Page 6). That is a mechanistic conclusion from rather thin evidence. At best, the paper shows that this attack is more effective in some middle layers under this setup.  
   Why this matters: the difference between an empirical attack heuristic and a claim about where refusal policies “form” inside the network is substantial. The current experiment supports the former, not the latter.

8. **Equation-level specification is somewhat underspecified at key points.**  
   **Equation (3)** defines steering as adding $\alpha \mathbf{v}$ to every token’s residual stream at a fixed layer, but the implementation details matter a lot here and are not fully pinned down in the main text. For example: is the same $\mu^{(l)}$ used across prompts and token positions; is it computed over prompt tokens, generation tokens, or both; and how sensitive are results to using mean norm versus RMS norm or per-token normalization? Likewise, **Equation (4)** defines compliance rate as a simple average of binary judgments, but no notation is introduced for multiple sampled vectors, prompts, and repeated attack constructions, which makes some reported averages in Section 4 harder to parse precisely.  
   This is not a fatal mathematical error, but for a paper whose main contribution is an intervention protocol, the notation should be tighter. The implementation choices behind $\alpha = c \cdot \mu^{(l)}$ are central, not incidental.

9. **The case study is vivid, but scientifically it is mostly anecdotal.**  
   **Figure 5** is compelling as a demonstration, yet it uses a public API with proprietary default hyperparameters. That makes it hard to know whether the observed behavior is representative of the main controlled experiments or due to external settings not otherwise described in the paper. The text presents the case study as practical validation, which is fair, but it should not carry much weight for the broader scientific claim.  
   Why this matters: readers may over-index on the qualitative examples, while the actual experimental support remains elsewhere.

10. **The literature positioning is incomplete on safety-oriented steering methods and contemporaneous analyses of steering risks.**  
   The related work discusses adversarial steering and some safety uses of activation steering, but the framing would be stronger if it more directly engaged with papers that try to use internal activations selectively for safety, or papers that analyze safety tradeoffs of steering vectors rather than only their utility. As written, the paper sometimes sets up a straw version of the field, namely that interpretability-based steering is generally assumed safe, without adequately distinguishing between unconditional steering and safety-gated interventions.  
   Why this matters: the contribution is partly about overturning a narrative. If the narrative is oversimplified, the paper’s novelty and significance are overstated.

11. **Some of the strongest conclusions rely on appendix-only evidence that should have been in the main paper if they are central.**  
   For example, the claim on Page 6 that the safety compromise is “not due to simple alignment with known refusal directions nor general capability degradation” depends on Appendix E, including **Table 1** and **Table 2**. Those analyses are useful, but if the paper wants to rule out these alternative explanations, the evidence should be summarized in the main text more concretely.  
   Since the review outcome should be based on the main paper, I do not treat Appendix E as decisive evidence. I mention it because the paper itself relies on it rhetorically.

12. **Figure and result interpretation is sometimes a bit overconfident.**  
   **Figure 3** is one example. It does support non-zero compliance across all categories, which is an important observation. But the text then goes beyond that by calling the vulnerability “systemic” and suggesting monitoring is “practically infeasible.” The heatmap in **Figure 4b** does suggest poor transfer, yet “practically infeasible” is a deployment claim requiring stronger evidence than low conditional probabilities on one benchmark with one judge and one SAE source.

## Questions
1. Can the authors provide a cleaner held-out evaluation protocol for attack tuning? For example, choose layers and coefficients on one prompt subset or one benchmark, then report final compliance on a disjoint prompt set without any further tuning. This would substantially increase my confidence that the observed effects are not benchmark-specific search artifacts.

2. For the key random-vs-SAE comparison in **Figure 2c**, what exactly are the error bars, and are the pairwise differences statistically significant? Please report uncertainty estimates and, ideally, per-feature/per-vector distributions rather than only means.

3. Can the authors quantify judge reliability beyond precision on predicted harmful outputs? In particular, I would like to see a human audit of false negatives and borderline cases, especially for “disclaimer-then-compliance” responses like those shown in **Figure 5**. If the recall is weak, some of the reported compliance rates may be conservative; if the judge is unstable, small differences may not be meaningful.

4. How sensitive are the results to decoding policy? The paper uses greedy decoding throughout. Would the same qualitative conclusions hold under temperature sampling or nucleus sampling? This matters because some steering perturbations may primarily alter the probability mass rather than the argmax token sequence.

5. For **Equation (3)** and the scaling rule $\alpha = c \cdot \mu^{(l)}$, please clarify precisely how $\mu^{(l)}$ is computed: over which prompts, token positions, and token types, and whether prompt and generation tokens are pooled. Also, did the authors try per-token norm matching or other normalization schemes?

6. In Section 4.4, what happens if you average 20 random vectors without conditioning on success, or average 20 vectors successful on a benign prompt rather than a harmful one? This would help isolate whether the universal attack arises from success-conditioned selection or from averaging alone.

7. The paper interprets middle-layer sensitivity as evidence about where refusal policies form. Can the authors tone this down or provide stronger mechanistic evidence, for example by relating steering effects to known refusal probes or layerwise logit changes?

8. The appendix reports **Table 1** on cosine similarity with a refusal direction and **Table 2** on MMLU degradation. Could the authors summarize these more prominently in the main paper, and ideally extend them? In particular, I would like to know whether the lack of cosine similarity holds beyond the top 30 features and whether capability preservation also holds for random vectors.

9. Can the authors compare against a more direct baseline from the safety-steering literature, namely a known refusal or anti-refusal direction, to calibrate how strong these random/SAE effects are relative to purpose-built steering attacks?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper presents an attack recipe for increasing harmful compliance in open-weight LLMs via activation steering, including a transferable aggregation method in Section 4.4 and concrete examples of harmful outputs in **Figure 5**. While the study is legitimate safety research, it materially lowers the barrier for misuse by readers who have model access and steering capability. The qualitative examples include categories such as phishing, bomb-making, scams, and violent harm. I do not view this as a reason to reject the paper on its own, but it does warrant ethics review and careful consideration of release details.

## Soundness Rating
2: fair. The core phenomenon is plausible and supported by a meaningful amount of experimentation, but several headline claims are stronger than the methodology cleanly supports, and the evaluation/tuning protocol leaves important uncertainties.

## Presentation Rating
3: good. The paper is readable and the narrative is easy to follow, with informative figures, but some interpretations are overstated and several implementation details should be specified more precisely.

## Contribution Rating
2: fair. The paper highlights a relevant safety risk and assembles useful empirical evidence, but the novelty is more in the breadth and framing than in a fundamentally new methodological or mechanistic insight, and the current positioning overshoots the actual evidence.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
This is a timely and potentially impactful paper, and I do think the underlying phenomenon is real. However, the current version overclaims relative to what is actually demonstrated. The evidence convincingly shows that some activation steering interventions can increase harmful compliance on JailbreakBench, but it falls short of supporting the broader conclusions about activation steering as a class, interpretability as a safety paradigm, and the mechanism of refusal failure. With tighter evaluation, stronger controls, and more careful claim calibration, this could become a solid paper.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with activation steering, mechanistic interpretability, and LLM safety evaluation, and I checked the main empirical and mathematical details carefully.