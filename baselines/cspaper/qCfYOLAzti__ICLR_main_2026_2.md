---
job_id: 8b5bdfd6-af5b-42ac-92cd-53a93d485612
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: qCfYOLAzti.pdf
paper: LLM Unlearning with LLM Beliefs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, it studies LLM unlearning, safety/privacy, optimization objectives, evaluation methodology, and learning dynamics for generative language models.

## Minimum Quality
Pass ✅ The submission contains the expected components, including abstract, introduction, methodological sections, experiments/results, and conclusion, and it presents a coherent empirical study with a concrete proposed method. There are technical and presentation issues, but they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden or explicit instructions targeting automated reviewers, nor suspicious embedded text or manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper argues that many GA/NPO-style LLM unlearning methods only suppress the exact target response while shifting probability mass toward semantically similar rephrasings, a phenomenon the authors call the squeezing effect. To address this, the paper proposes a bootstrapping framework that uses the model’s own high-confidence predictions as additional forgetting targets, in token-level form (BS-T) and sequence-level form (BS-S), and evaluates the approach on TOFU, MUSE, and WMDP with both standard benchmark metrics and an LLM-as-a-judge evaluation.

## Strengths
The paper tackles a real and important failure mode in current LLM unlearning evaluation, namely the gap between low lexical-overlap metrics and actual semantic forgetting. The qualitative examples in Section 3.1 are useful and concrete, and they make the central concern easy to understand: low ROUGE or probability can still coexist with clear semantic leakage.

I found the core intuition of using the model’s own high-confidence alternatives as auxiliary forgetting targets to be sensible and practically motivated. The split into BS-T and BS-S is also a reasonable design choice, since token-level and sequence-level leakage are genuinely different phenomena.

The paper is generally well organized. The progression from failure cases, to mechanism, to method, to experiments is easy to follow. In particular, **Figure 1** does a good job communicating the intended mechanism of the method. The left panel makes the claim about mass shifting into nearby semantic regions visually intuitive, and the right panel clarifies the conceptual distinction between BS-T and BS-S. For a paper centered on a behavioral failure mode, this overview figure is genuinely helpful rather than decorative.

The empirical section is broader than many papers in this space. The inclusion of three benchmarks, multiple model families/scales, and both forget/retain trade-off metrics is a plus. **Table 1** is especially informative because it reports TOFU results across three forget ratios and three model scales, rather than cherry-picking a single setup. The trend that BS-S is usually slightly ahead of BS-T, while BS-T remains competitive, is at least internally consistent with the paper’s claim that sequence-level bootstrapping yields stronger forgetting at somewhat higher cost.

I also appreciated that the paper does not only report headline benchmark numbers but tries to diagnose the advocated mechanism. **Figure 2(a)** is useful because it connects semantic similarity to likelihood bands, which is central to the squeezing-effect story, and **Figure 4(c)** attempts to close the loop by showing improved LLM-judge scores for naturalness and similarity after applying the proposed methods.

## Weaknesses
1. **The central theoretical claim contains a concrete sign inconsistency, which undermines confidence in the analysis.**  
   On **Page 8, Theorem 5.2**, the paper states that for any component \(v \neq y_u^i\),
   \[
   \mathcal{G}_{\mathrm{BST}}^i[v] = \mathcal{G}_{\mathrm{GA}}^i[v] + \lambda \mathbf{q}^i[v].
   \]
   But from the theorem’s own preceding definition,
   \[
   \mathcal{G}_{\mathrm{BST}}^i = \pi - \big((1-\lambda)\mathbf{e}_{y_u^i} + \lambda \mathbf{q}^i\big),
   \]
   so for \(v \neq y_u^i\), one gets
   \[
   \mathcal{G}_{\mathrm{BST}}^i[v] = \pi[v] - \lambda \mathbf{q}^i[v] = \mathcal{G}_{\mathrm{GA}}^i[v] - \lambda \mathbf{q}^i[v],
   \]
   not plus. This is not a cosmetic typo because the theorem is exactly the place where the paper argues that BS-T “spreads forgetting pressure” over nearby alternatives. The sign determines whether nearby high-belief tokens are additionally pushed down or effectively relieved. The appendix proof reproduces the same inconsistency and then flips the sign again in the concluding sentence, so this is not isolated. At minimum, the theorem statement, proof, and surrounding interpretation need correction. As written, the theoretical section does not reliably support the claimed mechanism.

2. **The proposed losses are underspecified in places where the exact implementation matters for both reproducibility and interpretation.**  
   For **Equation (5)** on **Page 7**, the paper defines the soft target using the top-\(k\) restricted model distribution, but several practically important details are vague in the main paper: how ties in Top-\(k\) are handled, whether the target token is guaranteed to be inside \(\mathcal{H}_k^{(i)}\), whether temperature smoothing is actually used in all experiments or only suggested conceptually, and how \(k\) interacts with subword tokenization for semantically related alternatives. Similarly, for **BS-S in Equation (7)**, “high-confidence generations” are said to be sampled with temperature-controlled decoding, but the main paper does not specify the decoding algorithm, confidence filter, truncation rule, or whether generations are deduplicated. These details are not minor engineering trivia here, because the whole method depends on what counts as a “belief” sequence. Without this, it is difficult to tell whether improvements come from the specific belief construction or from a more generic augmentation effect.

3. **The empirical evidence for the squeezing effect is suggestive, but not fully isolating the claimed cause.**  
   The main mechanistic claim is that softmax normalization redistributes mass into semantically related high-likelihood regions, and that this is the main source of spurious unlearning. However, the evidence in **Figure 2(b,c)** mainly tracks grouped log-probabilities of high/mid/low likelihood bands over training epochs. This shows redistribution patterns, but it does not cleanly distinguish the proposed squeezing effect from a broader phenomenon of local distributional drift under any unlearning update. For example, one would want more direct evidence that the increased mass is concentrated on semantically related alternatives rather than just any frequent or stylistically generic continuations. **Figure 2(a)** helps by measuring similarity across likelihood bands, but the paper still stops short of establishing a stronger causal link between “high-likelihood region” and “semantic paraphrase region.” Right now the story is plausible, though a bit too neat.

4. **The evaluation argument is partly persuasive but also somewhat self-serving, because the replacement evaluation introduces its own unvalidated proxy.**  
   A substantial part of the paper’s pitch is that benchmark metrics such as ROUGE, probability, and truth ratio can misreport success. I agree with the broad concern. However, the paper then leans on its own **LLM-as-a-judge (LaaJ)** evaluation in **Section 3.1** and **Figure 4(c)** as an auxiliary arbiter, without enough validation in the main paper. The “Similarity” prompt on Pages 31–32 asks the judge to rate semantic similarity on a 0–5 scale, where “higher is better” according to the prompt wording, yet in the paper’s discussion this quantity is used as evidence of stronger unlearning when higher. There is a conceptual mismatch here: if the judge is truly rating similarity to the forgotten target, then lower should indicate better forgetting. The paper seems to reinterpret the score as success, but that mapping is not clearly explained in the main text. This matters because part of the contribution is “metrics are misleading, our evaluation reveals the truth,” and that claim requires a cleaner treatment of the new metric’s directionality and calibration.

5. **The comparison set is strong on GA-style baselines, but weak on disentangling what part of the gains comes from the specific proposed idea versus generic augmentation or stronger supervision.**  
   The method adds extra forgetting signal by targeting either top-\(k\) token beliefs or sampled belief sequences. This naturally increases the coverage of penalized outputs. A missing experimental question in the main paper is whether the gains are due to belief-awareness specifically, or simply because the method unlearns more variants of the target. For BS-S in particular, a stronger control would be to augment with alternative sequences that are not sampled from the current model belief distribution, or with generic paraphrases from another source, and compare against that. Without such controls, the causal attribution to “beliefs” remains incomplete. The paper does include some ablations in the appendix, but the main paper’s conclusions are stronger than what the main-paper evidence establishes.

6. **Some of the claimed superiority in the main quantitative table is narrower than the prose suggests.**  
   In **Table 1 (Page 9)**, BS-S is usually best or tied-best on the aggregate score, but several margins are very small. For instance, in TOFU 10% with 3B and 8B, BS-S improves Agg. from 0.62 to 0.63 and from 0.63 to 0.64 over NPO, while utility is comparable. That is respectable, but not a dramatic separation. More importantly, the table also shows that retrain remains ahead on some utility values and matches or exceeds the proposed methods on several retention-related entries. The paper sometimes presents the results as though the method has established a clearly superior forget-retain balance across the board; the table supports “consistent but modest gains” more than “decisive improvement.” I would encourage the authors to tone down the rhetoric accordingly.

7. **The sequence-level method is computationally heavier, yet the main paper gives very limited cost analysis.**  
   BS-S requires sampling \(N\) additional generations and optimizing over them, which can be nontrivial for larger models and longer responses. The main paper acknowledges that BS-T is more efficient and BS-S is more thorough, but the practical cost trade-off is pushed to the appendix. Given that this method is proposed as a generally applicable LLM unlearning framework, some runtime or memory discussion should have appeared in the main paper, especially because the gains of BS-S over BS-T in **Table 1** and **Table 2** are often incremental. This matters for adoption: if the gains are small but the cost is much higher, practitioners may reasonably prefer BS-T or even a simpler baseline.

8. **The method can still produce odd or fabricated outputs, which complicates the claim of “more reliable unlearning while preserving utility.”**  
   The qualitative examples in the appendix suggest that BS-S can avoid direct leakage, but sometimes by producing noisy or implausible content rather than clean abstention or benign redirection. This concern is already faintly visible in the main paper’s framing around naturalness in **Section 3.1** and **Figure 4(c)**. A method that replaces true facts with fluent but fabricated alternatives may look good under forgetting metrics, yet still be problematic in deployment. The paper would benefit from a more direct discussion of whether the desired behavior is abstention, uncertainty expression, harmless alternative completion, or simple semantic divergence. Right now “less similar to the target” and “more natural” are treated as sufficient, which is not obviously the right target behavior for safety-critical unlearning.

## Questions
1. **Please clarify and correct Theorem 5.2.**  
   The sign of the residual correction term appears inconsistent with the theorem’s own definition. Can the authors provide the corrected statement and explain whether the intended mechanism is that BS-T makes non-target high-belief components more negative, i.e.
   \[
   \mathcal{G}_{\mathrm{BST}}^i[v] = \mathcal{G}_{\mathrm{GA}}^i[v] - \lambda q^i[v],
   \]
   for \(v \neq y_u^i\)? This is the single most important clarification for my confidence in the theory section.

2. **How exactly are belief sequences constructed in BS-S in the reported experiments?**  
   Please specify in the main text or rebuttal the decoding scheme, temperature, any top-\(p\)/top-\(k\) truncation, maximum length, deduplication, and any confidence filtering. If “high-confidence” simply means ordinary sampled generations from the current model, that should be stated clearly.

3. **Can the authors provide a stronger control for the role of “beliefs” versus generic augmentation?**  
   For example, what happens if the forget set is augmented with paraphrases not sampled from the model itself, or with random same-length completions, while keeping the amount of extra supervision matched? Evidence along these lines would strengthen the central claim that model beliefs specifically counteract squeezing.

4. **How should the LaaJ Similarity score be interpreted directionally?**  
   The prompt shown in the appendix appears to define 0 as completely different meaning and 5 as identical meaning, yet **Figure 4(c)** and the surrounding text talk about higher Similarity as better unlearning. Please clarify whether the plotted quantity is raw similarity, inverted similarity, or a success score derived from it.

5. **How large is the practical overhead of BS-S relative to BS-T and NPO for the main reported settings?**  
   Even a short summary of wall-clock and memory overhead in the rebuttal would help assess whether the incremental gains in **Table 1** and **Table 2** justify the extra cost.

6. **Does the method reduce leakage under alternative prompting or decoding settings?**  
   Since the motivating problem is semantic leakage rather than exact-match memorization, I would like to know whether the observed gains hold under non-greedy decoding, paraphrased prompts, or adversarial prompting, especially on TOFU and WMDP.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper is about unlearning harmful or sensitive knowledge from LLMs, including privacy-related content and hazardous domain knowledge, so it directly touches privacy and safety. The concern is not that the work is unethical per se, but that incomplete or merely cosmetic unlearning could create a false sense of safety. This is especially relevant for **TOFU** privacy-style forgetting and **WMDP** hazardous knowledge forgetting, discussed in **Section 6**. If a method mainly drives outputs toward paraphrases or fabricated alternatives rather than robust removal or safe refusal, deployment claims should be made carefully.

## Soundness Rating
3: good. The paper has a plausible method and a reasonably broad empirical study, but the theoretical section contains a nontrivial inconsistency, and several methodological details central to the claim are underspecified in the main paper.

## Presentation Rating
3: good. The paper is generally readable and well structured, with effective motivating figures, though some notation/details and the evaluation narrative need tightening.

## Contribution Rating
3: good. Identifying semantic leakage behind apparent unlearning success is useful, and the belief-aware objective is a meaningful extension of existing unlearning methods, though the gains are mostly incremental rather than transformative.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper identifies a meaningful failure mode, proposes a sensible remedy, and backs it with fairly broad experiments. I am leaning positive because the practical idea is useful and the empirical trends are consistent, but the theory needs correction, and the paper overstates a few conclusions relative to the evidence.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main technical claims carefully, including the equations and theorem statements, though I did not independently verify all experimental details beyond what is reported.