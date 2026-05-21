---
job_id: 6e8b275a-7f19-433b-b7b7-ffe34e9eb18f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: CNrU5kGJYG.pdf
paper: TrojanTO: Action-Level Backdoor Attacks Against Trajectory Optimization Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, sequence modeling, and ML security/safety, with a focus on backdoor attacks against trajectory optimization models.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including Abstract, Introduction, Related Work, Methodology, Experiments, quantitative results, and Conclusion, and it presents a coherent empirical study with reproducibility details, even though there are several technical and evaluation limitations.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies backdoor attacks against trajectory optimization models for offline RL, focusing on action-level attacks in continuous action spaces. The authors propose TrojanTO, a post-training attack that combines trajectory filtering, batch poisoning, and alternating trigger/model optimization, and evaluate it on D4RL tasks with DT, GDT, and DC. The paper also includes empirical investigations of target action choice, trigger design, and reward manipulation.

## Strengths
The paper tackles a timely and underexplored security problem. The focus on post-training backdoors for trajectory optimization models is well motivated in the context of increasingly reused pretrained decision-making models, and the paper makes a reasonable case that the standard reward-manipulation paradigm from online RL does not transfer cleanly to TO models.

The empirical scope in the main paper is fairly broad. **Table 4** evaluates three victim architectures, six environments, and three baselines/settings, and the aggregate picture is consistent: TrojanTO usually improves the combined attack metric CP over Baffle and IMC, often substantially. In particular, the gains on DT-Half, DT-Walk, and several DC settings are large enough that they are unlikely to be noise. I also appreciate that the paper reports both attack effectiveness and benign performance, rather than optimizing only ASR and ignoring utility collapse.

The decomposition of the method into three modules is clear at a high level, and **Figure 2** is useful for understanding the intended pipeline. The figure makes the interaction between trajectory filtering, partial batch poisoning, and alternating trigger/model updates much easier to follow than the text alone. This is one of the clearer parts of the presentation.

The ablation in **Table 5** is helpful and suggests that the proposed components are not entirely ornamental. In particular, removing batch poisoning or alternating training drops ASR and CP noticeably, while removing trajectory filtering mainly hurts BTP. Even though some details remain underspecified, the ablation does support the claim that the method’s three ingredients play different roles.

The paper also does a good job highlighting a nontrivial issue specific to continuous control: target action difficulty matters. **Table 1** shows a striking spread in ASR across target types, especially between boundary actions and interior/random/arithmetic targets. That is a useful observation for future work because papers in this area could otherwise cherry-pick easy boundary targets and overstate attack strength.

## Weaknesses
1. **The core optimization formulation is inconsistent across the paper, and several equations are underspecified or mathematically sloppy.**  
   The threat-model objective in **Equation (1), Page 3-4** defines
   \[
   \min_{\tilde{\pi}} \sum_s \left\|\tilde{\pi}([a],[s]+\delta,[\hat R])_t-a^\dagger\right\| + \lambda \left\|\tilde{\pi}([a],[s],[\hat R])_t-\pi([a],[s],[\hat R])_t\right\|,
   \]
   which compares the attacked model to the clean model on benign inputs. But the actual training objective later uses \(\mathcal L = \mathcal L_p + \lambda \mathcal L_c\), where **Equation (6), Page 7** compares \(\tilde{\pi}(B_c)_t\) to the dataset action \(a_t\), not to the clean model output. These are materially different objectives, especially when the clean model is imperfect relative to the dataset. If the central claim is that the attack preserves the original policy behavior, then the paper should explain why matching dataset actions is an adequate surrogate for matching the clean model, or rewrite the formal objective to align with the implemented one. As written, the paper presents one optimization problem in the threat model and then solves another in the method section.

   There are additional notation issues. In **Equation (6)**, the summation is written from \(t=0\) to \(T\), while the earlier reconstruction loss on **Page 3** uses \(t=0,\dots,T-1\). Since trajectories were defined as \((s_0,a_0,r_0,\dots,s_{T-1},a_{T-1},r_{T-1},s_T)\), there is no action target \(a_T\). This looks like an off-by-one error. Likewise, in **Equation (7)** the lower problem is written as \(\arg\min_{\tilde{\pi}_\star}\) but the expectation depends on \(\tilde{\pi}\), not \(\tilde{\pi}_\star\), which is notationally inconsistent for a bilevel program. These may seem cosmetic, but here they obscure what is actually optimized.

2. **The evaluation metric for ASR is fragile and may overstate or distort attack success in continuous control.**  
   In **Equation (2), Page 4**, ASR counts an attack as successful if *all* action dimensions are within a threshold \(\varepsilon\) of the target action at a single triggered step. This is a very strict geometric criterion, but the paper never justifies the value of \(\varepsilon\) in the main text or discusses sensitivity to it. In continuous action spaces, ASR can change dramatically with \(\varepsilon\), target dimensionality, and action scale. A method can look much better or worse depending on whether \(\varepsilon\) is permissive. Since the paper’s central contribution is “action-level” precision, robustness to this threshold is not a side issue, it is the metric definition itself.

   Relatedly, the paper introduces CP in **Equation (4)** as the harmonic mean of ASR and BTP. While this is convenient, it bakes in a particular value judgment that attack success and benign utility should be equally weighted. That is not obviously appropriate across all environments, especially when some tasks already have very different clean return scales and difficulty levels. A stronger evaluation would include raw action distance to target, environment return under triggered execution, and sensitivity over \(\varepsilon\), not just a single binary ASR plus a derived harmonic mean.

3. **The comparison to baselines is narrower and less fair than the headline claims suggest.**  
   The main comparison in **Table 4, Page 8** is against Baffle and IMC. Baffle is a natural baseline, but IMC is not originally an RL backdoor method; it is an input-model co-optimization idea adapted here. That makes it more of a component-level inspiration than a strong domain-native baseline. The paper’s “first action-level backdoor against TO models” angle may well be true, but the empirical positioning would be stronger if the authors compared against more recent offline RL backdoor methods or stronger trigger optimization baselines tailored to RL, not only a dataset-poisoning method and a generic co-optimization baseline.

   Even within the shown results, some claims deserve more restraint. For example, **Table 4** averages over three target actions, but the appendix results in **Table 24** show enormous variance by target type. TrojanTO is extremely strong on target action “1”, but much weaker on “arithmetic” and mixed on “fixed random”, with several near-zero or low-CP entries such as DT-Hopp and Pen for arithmetic, and Ant for fixed random. Therefore the average in Table 4 compresses important heterogeneity. The method is clearly effective in many settings, but the paper sometimes writes as if the attack is uniformly robust across “diverse objectives”, which the detailed table does not fully support.

4. **The claim that reward manipulation is negligible is not established as strongly as the text suggests.**  
   Section 4.3 argues that reward manipulation is ineffective for TO models, and **Figure 1, Page 6** is presented as evidence. The figure indeed suggests that, on Walk and for the selected target type/triggers, multiple reward manipulation variants track similarly over epochs for ASR and BTP. However, the evidence is much narrower than the prose. It appears to be one environment family in the main paper, one target type (“1”), and one trigger dimension setting. The appendix adds Hopper, but this is still far from a comprehensive basis for the broad statement that reward manipulation has negligible impact for TO backdoors.

   More importantly, the comparison is somewhat confounded because the paper is no longer studying standard offline RL reward poisoning, but a post-training fine-tuning attack on a sequence model where rewards appear through RTG conditioning. If reward manipulation “does not matter,” the relevant scientific question is *why* the conditioned sequence model is insensitive under this setup. The paper gestures at this intuition, but it does not isolate whether the effect is due to RTG redundancy, target-return initialization, local sequence context domination, or the specifics of the poisoned training procedure. So the figure is suggestive, not definitive.

5. **Some design choices look heavily tuned or task-specific, which weakens the generality claims.**  
   The trigger dimensions are fixed to \((1,2,3)\) in later experiments based on the exploratory results in **Table 2, Page 5**. But Table 2 itself shows dramatic variance across dimension choices, including zeros for several options and “all dimensions”. That means attack performance depends strongly on an ex ante favorable trigger subspace. The paper acknowledges this somewhat, but then proceeds to use a hand-selected trigger dimension tuple for the main attack. This is closer to reporting performance under a good trigger choice than demonstrating a generally reliable procedure for finding one.

   The same issue appears with target actions. **Table 1** shows boundary actions are much easier than interior ones. The appendix **Table 24** confirms that a large fraction of the strong results are driven by target action “1”. Since the main paper repeatedly emphasizes broad applicability across “diverse target actions”, the stronger standard should be consistent performance on non-boundary, harder actions, not just averaged performance where easy boundary targets dominate the story.

6. **The threat model is plausible in some supply-chain settings, but still stronger than the paper lets on.**  
   On **Page 4**, the attacker is assumed to modify pretrained model parameters and obtain a small set of poisoned trajectories, while also being able to manipulate observations at inference time to inject the trigger. This is a meaningful attack model, but it combines several privileges: access to model weights, ability to perform substantial post-training optimization, and test-time control over observations. In real deployments, any one of these may be difficult. The paper frames this as “highly practical,” which overstates the case. It is practical in some model-sharing or insider scenarios, but not broadly representative of all TO deployment contexts.

   This matters because post-training attacks are being sold here as more realistic than training-time attacks. That can be true, but only if the assumptions are carefully bounded. The paper would benefit from a more explicit discussion of what exact supply-chain scenarios support all three capabilities simultaneously.

7. **The defense section in the main paper is too thin to support the concluding security implications.**  
   Section 6.5 on **Page 10** states that several defenses were tested and that fine-tuning works best, with others largely ineffective, but essentially all substance is deferred to the appendix. In the main paper, this reads more like a teaser than an evaluated defense study. Since one of the paper’s practical takeaways is that TrojanTO poses a serious security risk, the natural question is whether there are viable countermeasures. Without even a summary table in the main paper, readers cannot judge whether the defense results are convincing, narrow, or fragile.

   The appendix tables are also a bit mixed. For example, fine-tuning in **Table 11** appears effective in one setting, which is important and somewhat softens the “potent vulnerability” narrative. If fine-tuning with only 10 clean trajectories can drive ASR from 1.0 to 0.04 while preserving reasonable BTP, that should be discussed more centrally rather than buried.

8. **Presentation is serviceable but uneven, with several wording and consistency issues that make the paper feel less polished than it should.**  
   There are repeated imprecise or awkward claims, for example “the insensitivity to reward manipulation confirms its limit” in Section 4.3, or “the model \(\tilde{\pi}\) are updated” on **Page 8**. More seriously, the paper occasionally overstates what the data show. The wording around robustness, stealthiness, and generality should be toned down given the dependence on selected trigger dimensions and easier target actions.

   There are also inconsistencies in terminology. The paper introduces “trajectory filtering”, “batch poisoning”, and “alternating training” in the main method, but the appendix later refers to “TrojanTO w/o TF” as if TF were “trigger generation” in one paragraph of **Page 28**, which is simply wrong relative to the acronym used elsewhere. That kind of inconsistency does not invalidate the experiments, but it does reduce confidence that the method description and ablations were edited carefully.

## Questions
1. In **Equation (1)** the benign term matches the attacked model to the *clean model output*, whereas **Equation (6)** matches it to the *dataset action*. Which objective is actually optimized in code? If it is Equation (6), please justify why preserving dataset imitation is an adequate proxy for preserving the original policy’s benign behavior.

2. Please specify the exact threshold \(\varepsilon\) used in **Equation (2)** in the main paper, and provide ASR sensitivity to \(\varepsilon\). Given that the work is about action-level precision in continuous spaces, this analysis could materially change my confidence.

3. Can you report results where trigger dimensions are selected automatically, rather than fixing \((1,2,3)\) after exploratory analysis? Even a simple search-budget-constrained procedure would help determine whether TrojanTO is robust or whether it depends on favorable manual trigger placement.

4. For the reward manipulation study in **Figure 1**, can you clarify whether the conclusion is intended to hold generally for TO models, or only under your particular post-training attack setup? A mechanistic explanation of why RTG-channel manipulation fails here would strengthen the paper.

5. In **Table 24**, TrojanTO is much stronger on boundary targets than on arithmetic or some random targets. Could you characterize the geometry of “easy” versus “hard” target actions, for example by distance from the behavior-policy action distribution or by saturation near action bounds?

6. The defense results suggest fine-tuning may be reasonably effective. Can you provide a concise main-paper summary of the defense trade-offs, including how much clean data and how many update steps are required, and whether the attacker can easily survive subsequent benign fine-tuning?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper presents a concrete backdoor attack against offline RL/trajectory optimization models, with explicit methodological guidance for implanting malicious behavior while preserving benign utility. This has clear dual-use implications, particularly for robotics, autonomous control, and other sequential decision-making systems discussed in Sections 1 and 3.4. The concern is not misconduct by the authors, but that the work lowers the barrier for weaponizing backdoors in pretrained control models, so careful framing and responsible release practices matter.

## Soundness Rating
2: fair. The empirical study is substantial and many conclusions are supported directionally, but several central claims are weakened by objective inconsistencies, underspecified metrics, and limited analysis of sensitivity and generality.

## Presentation Rating
2: fair. The overall structure is readable and Figure 2 helps, but notation inconsistencies, equation issues, and some overclaimed interpretations reduce clarity.

## Contribution Rating
3: good. The paper addresses an important and underexplored problem and provides a useful empirical baseline for post-training backdoors in TO models, even though the methodological and evaluative weaknesses keep it from being a stronger contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The problem is important and the experiments are stronger than average for this area, but the paper overstates generality, the optimization/evaluation setup needs tightening, and several key claims are not established cleanly enough for a more positive recommendation.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some parts or missed some related work.