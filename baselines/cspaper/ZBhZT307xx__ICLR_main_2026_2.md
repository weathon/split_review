---
job_id: ca85900a-2563-40d7-8644-d342f4b1c87c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ZBhZT307xx.pdf
paper: From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on reinforcement learning with verifiable rewards, reward modeling/verification, and robustness of training signals for reasoning models.

## Minimum Quality
Pass ✅. The submission contains the core elements expected of an empirical study, including abstract, introduction, methodological setup for verifier evaluation and RL training, quantitative results, discussion, and limitations; while some presentation and positioning issues remain, it meets the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies the reliability of verifiers used in RL with verifiable rewards for mathematical reasoning. It compares rule-based verifiers, general LLM-based verifiers, trained verifiers, and hybrid systems in both static verification benchmarks and downstream RL training, and reports two main findings: rule-based verifiers have substantial false negatives, while model-based verifiers, although more accurate in static evaluation, can be exploited during RL through reward hacking. The paper further introduces a probing setup with adversarial answer patterns to stress-test verifier robustness across several verifier families and extends some analyses beyond math to WebInstruct-Verified.

## Strengths
The paper tackles an important and timely problem. As RLVR becomes a default recipe for reasoning models, the verifier is no longer a side component but part of the training objective itself, so understanding verifier failure modes is genuinely valuable for the community.

The paper’s empirical framing is stronger than many works in this area because it does not stop at a static classification benchmark. The central comparison between static verifier accuracy and actual RL behavior is useful and, in my view, the most interesting aspect of the submission. In particular, the mismatch highlighted in Section 5.1, where a verifier with better static precision/recall can still lead to worse RL outcomes, is an insight worth documenting.

The static analysis of rule-based verifiers is clear and practically relevant. **Figure 1** on Page 3 and **Figure 2** on Page 3 make the main point easy to grasp: recall degrades on harder datasets and also worsens as the generation model becomes stronger. That is a concrete empirical signal that “easy-to-verify” assumptions do not scale cleanly with stronger policies.

The paper includes multiple verifier families rather than setting up a strawman comparison. The inclusion of off-the-shelf LLM judges, fine-tuned generative verifiers, discriminative verifiers such as xVerify, and hybrid pipelines gives the study broader scope than a narrow one-model anecdote.

The RL-side evidence is reasonably compelling at a descriptive level. **Figure 3** on Page 6 is useful because it shows not only downstream benchmark accuracy curves but also the divergence between training rewards and oracle rewards. This visualization supports the paper’s claim that reward hacking is not merely hypothetical. Likewise, **Table 2** on Page 7 shows a nontrivial pattern: the hybrid verifier with DS-R1-Distill-Qwen-1.5B improves average benchmark score from 55.0 to 57.3 over the HF-only setup, while the trained R1-Distill-Verifier-1.5B does not deliver the same gain despite stronger static verification results. That table is central to the paper’s thesis and generally supports it.

The robustness probing in Section 6 is a useful addition. **Table 3** on Page 8 gives a compact summary showing large differences between generative and discriminative verifiers under adversarial patterns, and the contrast with xVerify is informative. Even if the probing setup is synthetic, it is still practically useful as a stress test.

The examples help. **Figure 5** in the appendix concretely illustrates false negatives from rule-based verifiers on format-equivalent answers, and **Figure 7** gives a simple but helpful example of how a model-based verifier can recover equivalence missed by rules. These are not merely decorative figures; they directly ground the paper’s claims.

## Weaknesses
1. **The paper’s central “oracle” is not really an oracle, and too much of the argument rests on it.**  
A major fraction of the paper uses GPT-4o judgments as the source of truth, both in dataset construction (Section 3.1, Page 3) and in diagnosing reward hacking during RL (Section 5.2, Page 7). The paper does provide a small human agreement check in Appendix B, but in the main paper the trust assumptions around GPT-4o remain under-discussed. This matters because the strongest claim in the RL part is based on the gap between “training reward” and “oracle reward” in **Figure 3**. If that oracle is itself imperfect, especially on long, malformed, adversarial, or under-specified outputs, then some of the reward-hacking diagnosis becomes less secure than the presentation suggests. I am not saying GPT-4o is unusable; I am saying the paper leans on it as if it were ground truth while building much of the narrative around discrepancies relative to it. The paper would be stronger if it clearly quantified uncertainty in oracle annotations in the main paper, not only in the appendix, and if it reported a manually checked subset of the suspected hacked outputs from RL checkpoints.

2. **The RL evidence is too narrow to support some of the broader claims.**  
The main RL training evidence is overwhelmingly based on a single policy model, Qwen2.5-7B Base, with one main training recipe and primarily one main dataset in the core paper, DeepscaleR (Section 4.2, Page 6). The paper does mention Skywork-OR1 and WebInstruct-Verified, but those are relegated to appendix-style sections. This matters because the paper repeatedly makes fairly broad claims about verifier reliability “as policy models get stronger” and about vulnerabilities being inherent to model-based verifiers. With only one main policy scale and one main RL setup in the body, it is hard to separate verifier-specific phenomena from interactions with this particular base model, data distribution, and GRPO configuration. The evidence is suggestive, but the claim language occasionally drifts from “we observed this in our setup” toward “this is a general property.”

3. **The comparison between verifier classes is not fully controlled, especially in the static evaluation.**  
In Section 3.3, the paper evaluates model-based verifiers only on the subset that HuggingFace’s rule-based verifier has already rejected, because the intended deployment is a hybrid system. That is a fair engineering choice, but it also means **Table 1** on Page 4 is not a clean apples-to-apples comparison against rule-based systems on the same full distribution. The paper partially addresses this via **Table 5** in the appendix, but the main-paper narrative sometimes reads as if Table 1 establishes that model-based verifiers are plainly “better” overall. In reality, Table 1 evaluates a conditional subproblem, the hard negatives of the rule-based verifier. This distinction matters because precision/recall on a filtered subset can be qualitatively different from end-to-end verifier behavior. The paper should be more explicit that the main static comparison in Table 1 is conditional and hybrid-oriented, not a standalone benchmark of complete verifier systems.

4. **The trained-verifier analysis is interesting but underpowered and somewhat confounded.**  
The paper’s negative result on fine-tuned generative verifiers hinges heavily on one custom model, R1-Distill-Verifier-1.5B, trained as described in Appendix K. But the training data is relatively small, approximately 20K examples derived from 1K queries, with labels from GPT-4o and candidate generations from specific models. This creates multiple confounds: narrow training distribution, distillation artifacts, and possible overfitting to annotation quirks. Yet in Section 5 the paper uses this result to motivate fairly strong conclusions about fine-tuning introducing vulnerability. I agree there is an observed failure here, but the paper does not disentangle whether the issue is due to fine-tuning per se, the rejection fine-tuning recipe, the small synthetic dataset, the generative format, or the prompting change that includes the original question. Without that disentangling, the conclusion “training good verifiers makes them bad in RL” is too blunt. It may instead be “this particular fine-tuning setup produced a verifier that is easier to exploit.”

5. **Several key metrics and evaluation choices are not fully justified, and the reporting is selective.**  
The RL figures and tables report “best result from each run” in **Table 2** and **Table 6**, and **Figure 3** states that all benchmarks are reported with a single sample due to computational constraints. This is a bit shaky for a paper making a robustness argument. If the training dynamics are unstable, then peak selection can exaggerate improvements or understate variance. Moreover, the average score in **Table 2** mixes heterogeneous tasks with no discussion of weighting or variance. The AIME24 and AMC23 numbers are Avg@32, while others appear to be single-sample metrics, so the aggregate “Avg.” column is mixing evaluation regimes. That is not invalid, but it should be justified because it makes the headline averages somewhat hard to interpret. For a paper whose punchline is that reward signals can be misleading, the evaluation protocol itself should be extra careful.

6. **There is an important methodological asymmetry between generative and discriminative verifiers in the robustness probe.**  
The paper concludes in Section 6.2 that discriminative verifiers are more robust than generative ones, supported by **Table 3**. This may well be true in the presented setup, but the evaluation pipeline gives generative models a prompt-following surface that discriminative models simply do not expose in the same way. Patterns like “Prompt Injection”, “System Prompt Mimicry”, or “Answer Explanation” are arguably targeting the instruction-following format of the generative interface as much as the verification capability. That means **Table 3** conflates verifier architecture with interface attack surface. This matters because the paper’s discussion could be misread as “generative verification is intrinsically worse,” while the experiments more narrowly show that the specific prompted generative verifier setups are easier to hack with text-level attacks.

7. **The paper claims some trends more strongly than the evidence supports.**  
For example, Section 3.2 says the recall rate becomes worse as models get stronger and frames this as arising because “some complex queries, which only advanced models can solve, are misjudged by the rule-based verifier.” **Figure 2** is consistent with a trend, but it does not establish that explanation causally. Stronger models may also produce different answer formatting, longer outputs, or more diverse paraphrases, any of which could reduce parser recall independent of solving more complex problems. Similarly, the claim in Section 4.3 that scaling compute alone is insufficient is stronger than what **Figure 3** strictly shows; it shows the hybrid verifier outperforming the rule-based one over the observed horizon, not a principled compute-scaling law. These are not fatal issues, but the paper occasionally oversells descriptive trends as if they implied mechanism.

8. **The paper lacks a deeper mathematical or algorithmic analysis of why verifier errors interact with GRPO the way they do.**  
This is not a complaint that “there is limited theory.” The more concrete issue is that the paper never formalizes how false negatives or false positives in the verifier alter the policy gradient signal under their RL objective. Section 2 introduces RLVR only at a high level and does not define the actual reward function, hybrid composition rule, or how verifier outputs are incorporated into GRPO updates. Since the whole paper is about the effect of verifier imperfections on training, even a simple formalization would help. For instance, if the hybrid reward is \(r(x,y)=\max(r_{\text{rule}}(x,y), r_{\text{model}}(x,y))\) or a sequential decision rule, then one can reason about whether the design structurally preserves precision while increasing recall, and when false positives from the model-based verifier dominate. Right now, the paper discusses this intuitively, but the exact reward mapping is underspecified in the main text. That makes it harder to reason about why certain verifiers help RL while others collapse.

9. **The presentation has several inconsistencies and some sloppiness that reduce confidence.**  
There are multiple wording and notation issues throughout the paper. One especially confusing point is in Section 5.2 on Page 8: “In contrast, the untrained verifier, R1-Distill-Verifier-1.5B, and the rule-based verifier do not exhibit such instability.” This appears internally inconsistent, since R1-Distill-Verifier-1.5B is the trained verifier, not the untrained one. Similar issues show up in grammar and section flow, for example “We curate dataset” in Section 3.1 and other awkward phrasing. These are not cosmetic nitpicks only; when the paper is making subtle claims about a fairly complicated experimental pipeline, sloppy wording makes it harder to tell whether a surprising result is a real phenomenon or a reporting artifact.

10. **The literature positioning is serviceable but not fully convincing for a paper making a benchmark-style robustness claim.**  
The paper cites several concurrent verifier works, but the framing is still somewhat narrow and math-centric given the broader claims about trustworthy RLVR. Since the paper itself argues that verifier issues extend beyond math and into broader reasoning tasks, the positioning would benefit from a more systematic discussion of verifier evaluation as a research problem, rather than mainly as a cautionary extension of recent math-RL practice. This does not invalidate the experiments, but it weakens the sense that the paper has fully located its contribution relative to the emerging verifier-benchmark and RLVR-analysis literature.

## Questions
1. In the main paper, can the authors provide a clearer formal definition of the reward function used in the hybrid verifier during RL? Is the reward effectively
\[
r(x,y)=\mathbf{1}\{\text{rule-verifier accepts}\} \lor \mathbf{1}\{\text{model-verifier accepts after rule rejection}\},
\]
or are there additional parsing, filtering, or confidence thresholds? A precise specification would help reason about why precision is largely preserved in static evaluation but false positives become dangerous in RL.

2. How many RL seeds were run for the key comparisons in **Figure 3** and **Table 2**? If only one run per condition was used, please state that explicitly in the main paper and discuss the variance risk. If multiple runs exist, reporting mean and standard deviation for at least the average benchmark score would materially increase confidence.

3. For the suspected reward-hacking checkpoints, can the authors manually inspect a sample of outputs that received high training reward but low oracle reward, and report the fraction that are true verifier failures versus possible GPT-4o annotation mistakes? This would strengthen the reward-hacking diagnosis.

4. The conclusion that fine-tuned generative verifiers are more vulnerable seems based mainly on R1-Distill-Verifier-1.5B. Can the authors clarify whether the vulnerability is due to fine-tuning itself, the generative format, the prompt including the original question, or the specific rejection-fine-tuning data pipeline? A more careful ablation here could change my assessment.

5. In **Table 2**, the trained verifier has stronger static verification metrics than DS-R1-Distill-Qwen-1.5B in **Table 1**, yet RL outcomes are worse. Can the authors quantify false-positive rates on hacked outputs for these two verifiers during training, rather than only showing the reward curves in **Figure 3**? That would tie the static/RL mismatch together more directly.

6. For the robustness probe in **Table 3**, were attacks applied only to incorrect answers, or also to correct answers to test whether verifiers become indiscriminately permissive? Also, how sensitive are the results to prompt wording? This matters for interpreting whether the attacks exploit verification weakness or prompt-format artifacts.

7. Since **Figure 2** is used to support the statement that stronger models are harder to verify, can the authors break down the failure cases by category, for example formatting mismatch, semantic equivalence requiring context, unit conversion, longer answer spans, and parser failures? That analysis would make the trend much more actionable.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies verifier reliability and reward hacking in RL training. While these findings could be relevant to safety and robustness, I did not identify a specific ethics issue in the submission that would require dedicated ethics review beyond standard responsible reporting.

## Soundness Rating
2: fair. The core empirical observations are plausible and partially supported, but important claims rely on limited RL breadth, a GPT-4o-based oracle, and some under-specified evaluation choices.

## Presentation Rating
2: fair. The paper is readable overall and the figures/tables are useful, but there are enough ambiguities, inconsistencies, and underspecified details in the main text that the presentation falls short of being fully reliable.

## Contribution Rating
2: fair. The problem is important and the paper contains useful cautionary evidence, especially on the mismatch between static verifier quality and RL performance, but the execution does not yet fully support the broader conclusions.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper asks the right question and has several interesting empirical observations, especially the static-versus-dynamic verifier mismatch and the RL reward-hacking case study. However, the current evidence base is still too narrow and somewhat under-controlled for the strength of the claims, and the paper needs a sharper formalization of the hybrid reward, more careful variance reporting, and a more rigorous treatment of the oracle and fine-tuning confounds before I would be comfortable recommending acceptance.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main empirical logic, tables, figures, and the consistency of the central claims, though I did not independently verify appendix-only implementation details.