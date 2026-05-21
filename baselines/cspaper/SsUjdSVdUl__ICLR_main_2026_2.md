---
job_id: 2731be6f-19a9-4ec3-8b01-90e3ea8d5e02
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: SsUjdSVdUl.pdf
paper: CRITIQUE-RL: Training Language Models for Critiquing Through Two-Stage Reinforcement Learning
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, language model post-training, and scalable oversight for reasoning.

## Minimum Quality
Pass ✅. The paper includes the expected core sections, presents a complete method and experimental study, and does not exhibit any fatal methodological flaw or obvious test leakage from the main paper text, although several technical and empirical weaknesses remain.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies how to train language models to act as critics, producing both correctness judgments and natural-language feedback that help a fixed actor refine its answers. The main claim is that optimizing critics only through indirect rewards from actor refinement is insufficient, because it improves helpfulness but not discriminability; to address this, the paper proposes a two-stage RL procedure, where Stage I directly optimizes discriminability via rule-based rewards and Stage II optimizes helpfulness while regularizing to preserve discriminability.

The method is evaluated mainly on mathematical reasoning tasks with Qwen2.5-based actors/critics, with additional analyses on iterative refinement, ablations, inference-time scaling, out-of-domain transfer, and a summarization setting using a learned reward model.

## Strengths
1. The paper tackles a meaningful problem. Training critics without stronger external critique supervision is an important direction for scalable oversight, and the paper frames the central tension, discriminability versus helpfulness, in a way that is concrete and operational rather than purely rhetorical.

2. The two-stage decomposition is sensible and easy to follow. The contrast in **Figure 2** is especially effective: the baseline RL pipeline on the left/top makes clear that indirect rewards supervise the critic only through the actor’s refinement outcome, while the proposed pipeline explicitly inserts a discrimination-focused optimization stage before the helpfulness-focused stage. This figure supports the paper’s main conceptual contribution better than the prose alone.

3. The empirical story is generally coherent across metrics. In **Figure 3**, the training dynamics are one of the stronger parts of the paper. The plots show that indirect-reward baselines drift toward asymmetric behavior, either conservative or aggressive, and that Critique-RL improves both Acc@Refine and Acc@Dis more stably. This is more informative than only giving endpoint numbers, because it directly supports the paper’s diagnosis of the optimization failure mode.

4. The main benchmark results are strong relative to the baselines included. In **Table 1**, Critique-RL consistently improves both final refined accuracy and discrimination accuracy over SFT, STaR, Retroformer, and CTRL on MATH and GSM8K for both 3B and 7B backbones. The gains on Acc@Dis are particularly notable, for example on Qwen2.5-7B over CTRL, and this aligns with the stated objective of Stage I.

5. The paper includes meaningful ablations. **Table 3** is useful because it does not only ablate entire stages, but also ablates the Stage II reward design. The drop from removing discrimination preservation in Stage II is consistent with the central claim that helpfulness optimization alone destabilizes discriminability.

6. I appreciated that the paper does not stop at in-domain math accuracy. **Table 4** suggests some transfer to OOD datasets, and **Figure 5** attempts to disentangle helpfulness from discriminability by evaluating the setting with an oracle verifier available at test time. That is the right kind of analysis for this paper.

7. The presentation is mostly clear. The high-level method, algorithmic structure, and evaluation protocol are understandable without needing to reverse-engineer the intent.

## Weaknesses
1. The paper’s core supervision still relies heavily on oracle or oracle-like verification, and this limits the strength of the broader claim about training critics “without stronger labeling.”  
   In the main setting, Stage I uses a direct reward
   \[
   r_{\text{dis}}(x,y,c)=\mathbbm{1}\!\left(f(x,y,c)=r_{\text{oracle}}(x,y)\right)
   \]
   in **Equation 7**, which requires access to a correctness verifier for the actor’s original response. Stage II additionally depends on \(r_{\text{oracle}}(x,y')\) through \(r_{\text{refine}}\) in **Equation 9**. For math tasks this is practical, but the headline framing suggests a broader removal of strong supervision than the paper really achieves. The issue is not philosophical, it matters because the feasibility of the method in many realistic settings depends almost entirely on the availability and quality of these verifiers. The summarization experiment in Appendix G acknowledges this by swapping in a learned reward model, which actually reinforces the concern: the method is verifier-dependent, not supervision-free.

2. The mathematical specification of the RL objective is sloppier than it should be, and in a paper centered on a training objective that matters.  
   First, **Equation 2** is written as
   \[
   \mathcal{L}_{\text{SFT}}(\phi)=\mathbb{E}_{(x,y,c)\sim\mathcal{D}_{\text{SFI}}}\big[\log\pi_{\phi}(c|x,y)\big],
   \]
   but a loss should presumably be minimized as negative log-likelihood, so either the sign is wrong or the optimization direction is misstated. There is also an inconsistency between \(\mathcal{D}_{\text{SFT}}\) and \(\mathcal{D}_{\text{SFI}}\).  
   Second, the expectation in **Equation 9** is taken over
   \[
   c\sim \pi_{\phi}^{\text{Stage-I}}(\cdot|x,y),\ y'\sim \pi_\theta(\cdot|x,y,c),
   \]
   while the objective is supposed to optimize \(\pi_{\phi}^{\text{Stage-II}}\). Sampling critiques from the Stage I policy instead of the Stage II policy is not a harmless typo, because it changes the policy gradient interpretation. If this is only a notation mistake, it should be corrected; if intended, it needs justification as an off-policy procedure.  
   Third, the KL term is repeatedly written as \(\mathrm{KL}(\pi_{\text{ref}}(c|x,y)\|\pi_{\text{new}}(c|x,y))\), but for sequence models this is not a simple scalar unless the authors specify whether it is token-level KL under the new-policy trajectory, exact distributional KL, or an approximation. In practice this affects optimization and reproducibility.

3. The extraction function \(f(x,y,c)\), which is central to Stage I, is underspecified.  
   In **Algorithm 1** and **Equation 7**, the whole discriminability reward depends on whether \(f(x,y,c)\) matches the oracle reward, but the main paper never defines in enough detail how the model judgment is parsed from the generated critique. Is \(f\) reading the final-answer correctness only, aggregating step judgments, or applying a template-based parser? What happens when the model output is malformed, ambiguous, or inconsistent between step-level and final-answer judgments? This matters scientifically because a brittle parser can inflate or deflate Acc@Dis and can also alter the Stage I reward landscape. Given that the claimed contribution is improved discriminability, the reward extraction mechanism should not be a black box.

4. Some empirical gains may be entangled with extra compute and pipeline structure, and the paper does not fully isolate this.  
   The method adds a dedicated Stage I RL phase, then a Stage II phase, while baselines are presented as single-phase alternatives. The comparison in **Table 1** is encouraging, but it is still unclear whether the improvements come primarily from the proposed discriminability/helpfulness factorization, or simply from more optimization budget plus a strong initialization trajectory. The iterative results in **Table 2** and the scaling results in **Figure 4** further suggest that repeated critique-refinement and repeated training both improve results, which is useful, but they also make it harder to separate “better objective” from “more rounds of training/inference.” A stricter compute-matched comparison would make the empirical claim much stronger.

5. The evaluation remains narrow relative to the paper’s framing.  
   The main paper is overwhelmingly centered on verifiable mathematical reasoning tasks. That is a reasonable first testbed, but the introduction and conclusion gesture toward general scalable oversight. The only explicit open-ended experiment is moved outside the main paper. This matters because the claimed distinction between discriminability and helpfulness is likely task-dependent: in math, correctness is crisp; in open-ended generation, both the definition of “correctness” and the parser \(f\) become much murkier. I am not asking for a dozen new domains, but the main-paper conclusions should be toned down to the setting actually studied.

6. The baseline set is decent but not fully convincing for the specific claim being made.  
   The paper compares against SFT, STaR, Retroformer, and CTRL, which are all relevant. However, the claim is about training better critics, not only getting better refinement accuracy. Several recent lines of work on stronger critic construction, multi-agent critique generation, and deliberate stepwise critique are close enough in spirit that the paper’s positioning still feels a bit too comfortable. Even within the baselines used, some choices need more detail. For example, STaR is a somewhat awkward comparator for critique-model training, and it is not obvious that the strongest plausible non-RL critic-training recipe has been represented.

7. The interpretation of discriminability can be too coarse.  
   Acc@Dis, as defined in **Section 3.3**, is a binary agreement metric between the critic judgment and true correctness. That is fine as a starting point, but the critic outputs richer step-level assessments and explanations. A model could game this metric by emitting the right final verdict while giving poor or contradictory local reasoning. **Figure 2** visually emphasizes both step-level critique and final-answer judgment, yet the main quantitative discriminability metric collapses that structure. This matters because the paper’s central narrative is about developing genuinely better critics, not merely verdict classifiers with helpful-sounding text.

8. Some writing and notation issues reduce confidence more than they should in a paper that is otherwise fairly readable.  
   Beyond the objective-level inconsistencies already noted, there are several avoidable slips: “accessed” instead of “assessed” in **Section 3.3**, dataset symbol inconsistency in **Equation 2**, and parameter inconsistency between the main text and Appendix I, where **Page 8** states \(\beta_1=0.2\) for Stage II, while **Table 13** on **Page 22** discusses selecting \(\beta_1=0.9\) and \(\beta_2=0.95\). These may be bookkeeping issues, but they are not minor when they concern the exact reward weights used in the proposed objective.

9. The compute-efficiency claim is suggestive rather than fully established.  
   **Figure 1** and **Figure 6** indicate improved majority-vote scaling versus pure response sampling, and the curves are indeed favorable. Still, the comparison bundles multiple operations into one “sample,” and a response-critique-refinement chain is not equivalent in latency or token cost to a single direct response. If the paper wants to argue compute efficiency, it should normalize by actual generated tokens or wall-clock cost, not only sample count. Right now the evidence supports “sample-efficiency under this pipeline accounting,” not the stronger compute-efficiency phrasing.

## Questions
1. Please clarify the exact optimization objective in **Equation 9**. Should the expectation be over \(c \sim \pi_{\phi}^{\text{Stage-II}}(\cdot|x,y)\) rather than \(c \sim \pi_{\phi}^{\text{Stage-I}}(\cdot|x,y)\)? If the current equation is intentional, please explain how gradients are computed and whether this is off-policy optimization.

2. Please define \(f(x,y,c)\) precisely in the main paper. What text span is parsed, how do you handle malformed outputs, and how do you resolve disagreement between step-level judgments and the final-answer judgment? A concrete definition or pseudocode would substantially increase confidence.

3. Can the authors provide a compute-matched comparison against the RL baselines, either by equalizing total RL updates, total actor calls, or total generated tokens? This would help isolate whether the gains are due to the two-stage objective rather than additional training budget.

4. Relatedly, can the authors report whether Stage I alone, with a compute-matched extension, can close most of the gap to full Critique-RL? **Table 3** suggests both stages matter, but a more controlled analysis of budget allocation would strengthen the causality claim.

5. How sensitive are the conclusions to the choice of oracle verifier quality? The paper’s broader relevance would be clearer if the authors could discuss or test what happens when \(r_{\text{oracle}}\) is noisy, especially since many realistic domains do not have exact verifiers.

6. For **Table 1**, do the reported numbers come from one run or multiple seeds? If multiple seeds were used, please report variance; if not, please explain why the observed margins should be considered robust. This is especially important for RL comparisons.

7. Since **Figure 3** is a central diagnostic for the paper, could the authors clarify whether the plotted curves are smoothed, averaged across runs, or single-run trajectories? This affects how much one should infer about stability.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns require escalation based on the main paper. The work trains critique models for model oversight, and the paper includes a brief ethics statement. While stronger discussion of misuse and verifier bias would be welcome, I did not identify a concrete issue that rises to the level of formal ethics review from the evidence presented here.

## Soundness Rating
3: good. The empirical evidence is fairly strong and generally supports the main claim, but there are important specification issues in the objective and some limits in external validity.

## Presentation Rating
3: good. The paper is mostly clear and well organized, with effective figures and tables, though several notation inconsistencies and underspecified details should be fixed.

## Contribution Rating
3: good. The discriminability/helpfulness decomposition and two-stage RL recipe are useful contributions, even if the method is somewhat verifier-dependent and the evaluation scope is narrower than the framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real contribution, a coherent empirical case, and a good diagnostic story, especially through Figure 3 and the gains in Table 1. That said, the method relies more on verifier access than the framing suggests, several equations and implementation-critical definitions need correction, and the broader generality claims should be toned down.

## Reviewer Confidence
4: confident. I am confident in this assessment and checked the main technical and empirical details carefully, though a few implementation ambiguities remain unresolved from the main paper.