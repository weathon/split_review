---
job_id: 6968aed8-22e1-4da3-95dd-0b6de54404d6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: R0ZKcQlF2C.pdf
paper: Arenabencher: Automatic Benchmark Evolution via Multi-Model Competitive Evaluation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmarks and evaluation paper for large language models, with direct relevance to ML evaluation, safety, and dataset/benchmark design.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion. While I have substantial concerns about methodology and empirical support, these issues do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence of hidden prompts, concealed instructions to reviewers, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes ARENABENCHER, a framework for automatically evolving benchmark items using LLM-based ability extraction, candidate generation, LLM verification, and multi-model feedback to select harder test cases that are intended to remain aligned with the original benchmark objective. The method is evaluated on GSM8K, CommonsenseQA, and AdvBench Harmful Behaviors, with the paper claiming improved difficulty, fairness, alignment, and benchmark discriminability relative to the original benchmarks and relative to a single-model feedback variant.

## Strengths
The paper tackles a timely and important problem. Benchmark contamination and benchmark saturation are genuine issues for LLM evaluation, and the high-level goal of continuously refreshing test sets while preserving comparability is valuable for the community.

The overall pipeline is easy to follow at a high level. **Figure 1** is useful here, because it makes the intended loop quite concrete: ability extraction, candidate generation and verification, multi-model feedback, and iterative reuse of strong candidates as in-context demonstrations. Even though several methodological details remain underspecified, the figure helps readers understand the intended data flow and the role of each component.

The paper evaluates the method in three distinct domains, rather than only on one narrow setting. Testing on math reasoning, commonsense reasoning, and safety is a reasonable attempt at showing some breadth.

There is at least some effort to move beyond pure headline accuracy drops. In particular, **Table 2** reports additional benchmark-level metrics, namely fairness, separability, alignment, and difficulty. I appreciate that the paper does not reduce the entire story to “the benchmark got harder,” and instead tries to articulate desiderata for evolved benchmarks.

The inclusion of a failure case is a good practice. **Figure 2** is actually one of the more useful parts of the paper, because it undercuts an overly rosy narrative and shows that the authors are aware of semantic drift and malformed updates. In that example, the method preserves some superficial structure while changing the required reasoning pattern and even producing an underspecified question. That is an important limitation to surface.

The human annotation on 100 GSM8K examples, although limited, is directionally helpful. It gives at least some evidence that automatic verification is not completely unmoored from human judgment.

## Weaknesses
1. **The paper does not establish that the evolved items are genuinely contamination-resistant, even though contamination is a primary motivation in the abstract and introduction.**  
   The framing on **Pages 1-2** strongly emphasizes data leakage and memorization as the motivating problem. However, the experiments in **Section 4** do not actually measure contamination, overlap reduction, memorization sensitivity, or any proxy for “less leaked” evaluation items. What is shown in **Table 1** is mostly that the updated items are harder. Harder is not the same as less contaminated, and the distinction matters a lot scientifically. A benchmark evolution method meant to address leakage should provide at least one direct analysis of lexical/semantic overlap, retrieval-based contamination risk, or performance differences under known contaminated versus non-contaminated subsets. As written, the paper demonstrates difficulty amplification, not contamination mitigation.

2. **The empirical comparison is too weak for a paper making a general benchmark-evolution claim.**  
   The main empirical comparison is essentially ARENABENCHER with multi-model feedback, \(m=3\), versus a reduced variant with single-model feedback, \(m=1\), shown in **Table 1** and **Table 2**. That is useful as an ablation, but it is not enough as a baseline suite. The paper positions itself against prior benchmark updating and augmentation methods in **Sections 1-2**, yet there is no direct comparison against any existing automatic benchmark evolution, rewriting, perturbation, or dynamic-evaluation method. This makes it difficult to tell whether the gains come from the specific multi-model competitive mechanism, or simply from using a strong generator and judge to rewrite questions until they become harder. For a paper centered on method contribution rather than just an application note, that gap is serious.

3. **Several metric definitions are questionable or only partially aligned with the paper’s claims.**  
   The definitions in **Section 3.5, Pages 5-6** deserve much more scrutiny than the paper gives them:
   - The proposed difficulty metric is  
     \[
     \texttt{Difficulty}(\mathcal{B}',\mathcal{M}) = 1 - \max_{M_k \in \mathcal{M}} \text{Acc}(M_k,\mathcal{B}').
     \]
     This measures the inverse accuracy of the *best* model only. That is a very peculiar choice if the goal is to characterize benchmark difficulty for a pool of models. Two benchmarks with very different average hardness profiles can have the same value if the top model behaves similarly. The text in **Section 4.1** even describes difficulty as quantifying “the average performance across models,” which does not match this equation. That is not a small wording issue, it is a direct inconsistency between the formal definition and the prose interpretation.
   - The fairness metric,
     \[
     \texttt{Fairness}(\mathcal{B}',\mathcal{M}) = \Big(1-\frac{\frac{1}{K}\sum_{k=1}^{K}|c_k-\bar c|}{|\mathcal{B}'|}\Big)\times 100\%,
     \]
     rewards equal failure counts across models. But equal failure counts can arise in at least two very different situations: genuinely fair challenge, or uniformly bad benchmark corruption that hurts everyone similarly. The metric therefore conflates fairness with homogeneity of failure frequency. This is especially problematic in safety, where stronger and weaker alignment behaviors are expected to differ.
   - Separability is defined using mean absolute deviation around the mean accuracy, but the discussion in **Page 8** excuses drops in separability by saying “this is expected as model performance begins to compress under increased difficulty.” That partly undermines the earlier claim that improved discriminative power is a core objective. If the method often increases difficulty while reducing separability, then the central tradeoff needs sharper analysis, not a brief narrative gloss.

4. **The optimization and scoring formulation is underspecified, and there are inconsistencies between the equations, algorithm, and task descriptions.**  
   In **Section 3.3**, the paper defines \(\ell(M_k, x)\) as the loss of model \(M_k\) on input \(x\), “or a task-specific proxy such as inverse log-likelihood or refusal confidence,” and then averages these losses in **Equation (1)**. However, **Algorithm 1, line 9** instead computes \(\mathcal{L}(x_i^j, y_i^j)=\frac{1}{m}\sum \ell(M_k, x_i^j, y_i^j)\), which depends on both input and label. This is not a cosmetic mismatch. For GSM8K and CSQA, scoring could mean log-likelihood of the gold answer, exact-match failure, or judge-based correctness. For safety, it could mean refusal confidence, jailbreak success, or judged harmfulness. These are not interchangeable quantities, and averaging them across models requires a precise definition. Without that precision, it is hard to assess what the selection rule is actually optimizing.
   
   Relatedly, **Equation (2)** writes
   \[
   \mathcal{X}_i^\star = \text{TopK}_j\{\mathcal{L}(x_i^j)\},
   \]
   but the notation does not specify whether the top-\(k\) selection is over all valid candidates in the current round only, over all rounds, or under ties. Then in **Section 3.5** the final benchmark is written as \(\mathcal{B}'=\{(x_i^\dagger, y_i)\}\), while **Algorithm 1** returns \(\{(x_i^\dagger, y_i^\dagger)\}\). If generated answers can change, the main text and algorithm disagree; if they cannot, then the verification and generation procedure should explain why the original label remains valid. At present the mathematical presentation looks looser than it should for the core method.

5. **The justification for using \(m=\lceil \sqrt{K}\rceil\) feedback models is weak and not empirically validated.**  
   On **Page 4**, the paper motivates the \(\sqrt{K}\) rule by analogy to “classical ensemble heuristics,” citing XGBoost and Random Forests. That is not convincing in this setting. The problem here is not tree split selection or feature subsampling, but estimating challenge quality under a pool of heterogeneous LLMs. The claim that \(\sqrt{K}\) balances diversity, stability, and cost is plausible as a heuristic, but the paper presents it with more confidence than the evidence supports. Since \(K=6\) in the experiments, \(\sqrt{K}\approx 2.45\) simply rounds to 3, and the paper only compares \(m=1\) and \(m=3\). There is no evidence that 3 is better than 2, 4, 5, or 6, nor that the heuristic transfers beyond this tiny pool. This matters because the paper treats multi-model feedback as the key conceptual advance.

6. **The claimed fairness and model-agnosticism are not fully supported by the experimental design.**  
   The model pool in **Section 4.1** is very small and fairly narrow: six open-source models from a few families, mostly 1B to 7B scale, all evaluated after using GPT-4o for extraction, generation, and verification. A “model-agnostic” benchmark evolution framework should ideally show that evolved items are not overly tuned to this particular pool and still expose weaknesses for held-out models. The current experiments evaluate on the same pool used to drive the evolution. That leaves open a central concern: are the produced items broadly diagnostic, or just tuned to the quirks of the chosen six models? This is precisely where benchmark-evolution papers can accidentally overfit.

7. **The paper overclaims improved benchmark quality based on results that are mixed once one inspects the tables carefully.**  
   The narrative around **Table 2** is too optimistic. The paper says ARENABENCHER “substantially improves benchmark quality across all domains,” but the numbers are not consistently supportive:
   - On GSM8K, separability drops from 15.2 on the original benchmark to 12.2 for ARENABENCHER\(_3\).
   - On Harmful Behaviors, separability drops from 17.1 to 14.5 for ARENABENCHER\(_3\).
   - On CSQA, separability drops from 8.5 to 7.2 for ARENABENCHER\(_3\).
   
   So the one metric meant to capture discriminative spread generally *decreases* under the default multi-model setting. That directly complicates the paper’s central selling point about improved discriminative power and model separability. Similarly, fairness for Harmful Behaviors under ARENABENCHER\(_1\) is slightly worse than the original. These are not fatal results, but the paper should discuss them candidly rather than bundling everything under “improved benchmark quality.”

8. **The human evaluation is too limited to support strong claims about alignment and correctness across domains.**  
   On **Page 8**, the human study covers only 100 updated GSM8K cases. There is no human validation for CSQA or Harmful Behaviors, even though those settings arguably make semantic drift and judge brittleness more likely. Moreover, the paper reports only raw proportions, 95 aligned and 96 correct, without annotation protocol details that would help assess reliability, such as disagreement rates, adjudication, or inter-annotator agreement. Since the framework relies heavily on LLM-as-a-judge for verification and alignment, stronger human validation is not optional; it is central.

9. **The failure case in Figure 2 is informative, but it also reveals a deeper problem that the paper underplays.**  
   **Figure 2** shows that even when the extracted objective is reasonable, the evolved test case can become underspecified and can change the reasoning structure by adding a division step. This is not just an isolated anecdote. It directly challenges the validity of the ability-preservation mechanism in **Sections 3.1-3.2**. If the extracted ability description is too coarse, then many semantically drifted rewrites can still look “aligned” to the judge. The paper presents Figure 2 almost as a minor caveat, but for benchmark construction this is a core validity issue. A benchmark item that changes the latent skill being tested cannot be considered a faithful update merely because it is harder.

10. **Presentation quality is uneven, with multiple naming and notation inconsistencies that make the work look less mature than it should.**  
   Across **Pages 2-6**, the method name appears in multiple forms, including ARENABENCHER, ArenaBENCHER, ArenaBenoher, ArenaBencher, and AreNABENCHER. The set of selected candidates is written as both \(\mathcal{X}_i^\star\) and \(\mathcal{X}_i^*\). The final benchmark label is inconsistent, as noted above. These may sound minor, but in a methods paper where the contribution is primarily procedural, notation discipline matters. The same applies to the accidental prompt corruption visible in the appendix on **Page 14**, where the JSON template appears garbled. Even if the appendix is not central to the decision, the main paper already shows enough inconsistency to reduce confidence in implementation precision.

11. **The safety setting raises additional validity questions that are not addressed in the main paper.**  
   For Harmful Behaviors, the paper reports higher ASR after benchmark evolution in **Table 1**, interpreting that as exposing new vulnerabilities. But there is little detail in the main paper about how ASR is scored, how harmfulness is judged, whether the same model is used as both generator and evaluator, and whether the evolved prompts remain within the same attack taxonomy as the original AdvBench items. In safety evaluation, these details matter because an apparent ASR increase can come from changing prompt style, changing refusal criteria, or changing the underlying attack objective, not necessarily from surfacing the same vulnerability more effectively.

## Questions
1. The paper’s core motivation is contamination and memorization. Can the authors provide any direct evidence that the updated benchmark items are less susceptible to contamination than the originals, rather than simply being harder? For example, overlap analysis, retrieval-based contamination estimates, or experiments on known contaminated versus uncontaminated subsets would materially increase my confidence.

2. Please clarify the exact definition of the candidate scoring function \(\ell(M_k, x, y)\) for each domain. In **Section 3.3**, the text defines \(\ell(M_k,x)\), while **Algorithm 1** uses \(\ell(M_k,x,y)\). What exactly is being averaged for GSM8K, CSQA, and Harmful Behaviors, and how are these quantities normalized to make cross-model aggregation meaningful?

3. Why is the final updated benchmark written as \(\mathcal{B}'=\{(x_i^\dagger, y_i)\}\) in **Section 3.5**, while **Algorithm 1** returns \((x_i^\dagger, y_i^\dagger)\)? Are updated answers allowed to change or not? A precise answer is important, especially for math reasoning where rewording can easily alter the numerical target.

4. Can the authors provide a stronger ablation isolating the contributions of the four main components: ability extraction, LLM verification, multi-model scoring, and iterative in-context refinement? Right now, the evidence mostly isolates \(m=1\) versus \(m=3\), which is too coarse to tell where the gains come from.

5. Did the authors evaluate the evolved benchmarks on held-out models not used during the evolution process? This would directly test the claim that the method discovers shared weaknesses rather than overfitting to the construction pool.

6. For **Table 2**, how do the authors reconcile the claim of improved discriminative power with the fact that separability mostly decreases relative to the original benchmarks? If the intended story is a tradeoff between difficulty and separability, please make that tradeoff explicit and analyze it rather than presenting it as uniformly positive.

7. For the human study on **Page 8**, please report inter-annotator agreement or at least disagreement statistics. Also, why is there no comparable human validation for CSQA and Harmful Behaviors, where semantic drift may be even harder to detect automatically?

8. The failure case in **Figure 2** suggests the ability description may be too coarse to prevent latent skill drift. Have the authors tried structured constraints tied to operation sets, reasoning chains, or formalized rubrics, rather than relying mainly on free-form LLM judging?

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper evolves prompts for the **Harmful Behaviors** benchmark and explicitly aims to generate updated items that increase attack success rate against models. This is legitimate safety research, but it also creates a dual-use risk because the same pipeline could be used to generate stronger jailbreak or harmful elicitation prompts at scale. The concern is tied to the safety benchmark experiments in **Section 4.1** and the reported ASR increases in **Table 1**. I do not view this as disqualifying, but the paper should more clearly discuss safeguards, release policy for evolved harmful prompts, and intended access boundaries.

## Soundness Rating
2: fair. The high-level idea is reasonable, but the technical formulation is underspecified in key places, several metric definitions are not well aligned with the claims, and the empirical evidence is not strong enough to fully support the broader conclusions.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures help, but there are repeated naming/notation inconsistencies, some overclaiming relative to the tables, and important implementation details are missing or unclear.

## Contribution Rating
2: fair. The problem is important and the multi-model benchmark-evolution angle is interesting, but the paper currently falls short of establishing a strong methodological contribution beyond a plausible pipeline plus limited empirical evidence.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and has a sensible high-level idea, but the current version does not convincingly validate its central claims about fair, alignment-preserving, model-agnostic benchmark evolution. The lack of stronger baselines, the weak support for contamination-related claims, and the metric/method inconsistencies keep it below the bar for me.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the core methodology, equations, figures, and tables carefully, but a few implementation details remain ambiguous in the manuscript.