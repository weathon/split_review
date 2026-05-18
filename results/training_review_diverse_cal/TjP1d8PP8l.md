Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces DGAP (Discriminator-Guided Action Optimization), a framework that trains a RoBERTa-based discriminator on a handful (10–30) of expert demonstrations to produce step-level scores measuring alignment between LLM-generated actions and expert actions. These scores are fed into a "Process-Supervised Prompt" that guides the LLM to generate higher-scoring actions iteratively, with threshold-based replanning when scores fall too low. The paper reports strong empirical results on ScienceWorld and VirtualHome across GPT-4 and Llama3-70B, consistently outperforming baselines like SwiftSage, Reflexion, and Tree Planner.

## Strengths

- **Novel step-level guidance mechanism.** DGAP is one of the first methods to use a learned discriminator (trained via L2 regression on augmented demonstration data) to provide dense, step-wise alignment scores for LLM planning. This differs from prior approaches that rely on outcome-supervised feedback (Reflexion, Inner Monologue) or trajectory-level search (Tree-of-Thought). The idea is well-motivated in Section 3.1 and the data construction pipeline (expert data scored 10, random negatives scored 0, and offline augmentation via a fine-tuned LM with cosine-similarity scoring) is creative.

- **Strong and consistent empirical performance.** DGAP outperforms strong baselines across both benchmarks. In ScienceWorld (Table 1), it beats SwiftSage on the majority of task types. In VirtualHome (Table 2), it achieves higher Success Rate (SR) with lower standard deviation than all competitors (e.g., SR 0.73 vs. SwiftSage 0.54 on NovelTasks with GPT-4). These gains hold across two different LLM backbones (GPT-4, Llama3-70B), supporting the method's generality.

- **Data efficiency and practical viability.** The discriminator is trained using only 10–30 expert trajectories per task, which is substantially less data than demonstration-based methods require. The paper acknowledges this as a key advantage and the results bear it out. The VLM extension (using InternVL2-8B to generate object states) also demonstrates robustness to perceptual noise, broadening applicability.

- **Theoretical connection to critic-regularized RL is insightful as qualitative motivation.** While its status as a formal proof is overclaimed (see Weaknesses), the derivation in Section 3.3 connecting DGAP's objective to a KL-constrained RL formulation provides useful intuition for why the approach should work: the discriminator acts as an implicit reward, and the LLM's prompting procedure can be seen as approximate policy optimization under a trust region.

## Weaknesses

### Fatal

None.

### Major

1. **The theoretical guarantee is overclaimed relative to what is actually delivered.** The abstract and introduction state that DGAP "is provable to achieve a stronger policy than the LLM planner," and Contribution (iii) claims a "theoretical connection" that "shows our method obtains a stronger policy." However, Section 3.3 is explicitly titled "QUALITATIVE ANALYSIS" and derives the optimal policy for a constrained optimization problem that does not match the procedure DGAP actually executes. The derivation gives \(\pi^\star(a|s) \propto \pi^{\mathrm{llm}}(a|s)\exp(R_\phi(s,a)/\beta)\), but the implemented method uses prompting with historical action-score pairs and threshold-based replanning—there is no argument that this prompting process converges to or approximates the derived policy. The paper itself acknowledges this gap in passing ("such an objective is slightly different from DGAP where the LLM planner is prompted to generate actions that maximize the single-step return rather than the cumulative return") but does not reconcile it. This is not a fatal error—the qualitative analogy is still useful—but it constitutes a significant gap between rhetoric and substance. The authors should either remove the "provable" claims from the abstract/intro or establish a genuine formal connection between the prompting procedure and the derived policy.

2. **Missing ablation study prevents attribution of improvements to specific components.** DGAP introduces several interacting components: (a) the discriminator with its custom data pipeline, (b) the Process-Supervised Prompt with historical action-score pairs, and (c) the threshold-based replanning loop. The empirical results show the full system works well, but without ablations—e.g., comparing against a version without replanning, a version with a rule-based scorer instead of the learned discriminator, or a version using the discriminator only for filtering—it is impossible to tell which component drives the gains. Given the complexity of the method (training a discriminator, tuning a threshold, engineering a special prompt), this is not an optional addition. At minimum, the paper should ablate the discriminator and the replanning mechanism separately.

### Minor

1. **Efficiency claims are asserted without quantitative support.** The abstract, results (Section 5.1), and conclusion state that DGAP achieves "better efficiency" and "reduces the necessary steps and queries," but the only evidence is the qualitative visualization in Figure 5, which shows trajectories with fewer steps for a few tasks. No actual step counts, query counts (including replanning calls), or wall-clock times are reported anywhere. Since the replanning loop can itself introduce additional LLM calls per low-scoring step, the net effect on total queries is unclear. The authors should either report quantitative efficiency metrics (step counts, LLM query counts) or remove the efficiency claim.

2. **No analysis of discriminator generalization to out-of-distribution LLM actions.** The discriminator is trained on expert data (oracle actions), random negatives, and offline data from a fine-tuned BC model, but it is evaluated during planning on actions generated by different policies (GPT-4, Llama3-70B). No analysis is provided of how well the learned score function generalizes to these OOD actions. The empirical results provide indirect validation, but reporting the discriminator's prediction accuracy or correlation on held-out LLM actions would substantially strengthen the paper.

3. **Limited description of the fine-tuned LM used for data augmentation.** The paper uses a fine-tuned LM to generate offline action candidates via beam search (Section 3.1), but does not specify what model architecture is used, how it is fine-tuned, or on what exact data (beyond "expert demonstrations"). This is a non-trivial component of the pipeline, and its details should be transparent for reproducibility.

### Trivial

- The threshold values (5 for ScienceWorld, 6 for VirtualHome) are justified only by reference to "training data distributions." A brief sensitivity study showing how performance varies with the threshold would be valuable, though the lack of one does not undermine the results.
- The paper could report the discriminator's training loss or accuracy on a validation set to give a sense of its quality.

## Nice-to-Haves

- A failure analysis examining cases where DGAP underperforms (e.g., short sequences, tasks where scores are pervasively low) would deepen understanding of the method's limitations.
- The prompt template ("Previous actions, scores and observations are as follows...") is given only as a sketch. Providing the exact prompt format in an appendix would aid reproducibility.

## Removed Points

- **Criticism that Reflexion can re-plan based on intermediate failures.** The reviewer claimed the paper overstates when it says prior methods "generally receive feedback signals at the trajectory level." However, Reflexion reflects on full trajectories after completion and replans across episodes, not step-by-step within an episode. The paper's characterization is accurate. Removed.
- **Criticism questioning why the first LM beam candidate is assigned score 10.** The paper provides a clear rationale: the fine-tuned BC model's distribution aligns with the training data domain, so its top beam is a reasonable proxy for expert quality. This is a defensible design choice, not a flaw.
- **Complaint that the VLM experiment is "tangential."** The VLM experiment is an extension that tests robustness. It does not detract from the core contribution and is clearly presented as supplementary.
- **Generic formatting/style nitpicks** and **demands for missing appendix content** (parser artifacts). These are removed per instructions.

## Novel Insights

The most interesting observation to emerge from synthesizing the reviews is that DGAP's core tension—between using a simple learned scorer to guide prompting and claiming formal RL-theoretic guarantees—parallels a broader trend in the LLM agent literature. Many methods borrow the language of RL (reward, critic, policy optimization) for prompt-based procedures, but the actual prompting dynamics rarely obey the assumptions of the theorems they invoke. The paper's qualitative RL analogy is genuinely useful for intuition, but the "provable" framing distracts from what is actually novel: a data-efficient way to inject demonstration-grounded step-level signal into an LLM's planning context without modifying the LLM's weights. The paper would be stronger if it leaned into this practical contribution rather than overclaiming the theory.

## Suggestions

1. **Reframe the theoretical section.** Remove "provable" from the abstract and introduction. Keep the RL connection as an insightful qualitative analogy and motivational framing, but clearly label it as such. Inform readers that the derivation applies to an idealized objective and the implemented prompting procedure is a heuristic approximation.
2. **Add at least two ablations:** (a) DGAP without replanning (only the Process-Supervised Prompt), and (b) DGAP with a rule-based or random scorer replacing the learned discriminator. These will clarify whether the discriminator itself provides value beyond the prompt structure.
3. **Report quantitative efficiency metrics** — step counts, LLM query counts (including replanning calls), and/or wall-clock time for DGAP and the strongest baseline on a representative subset of tasks.
4. **Characterize discriminator quality** by reporting its prediction accuracy or correlation with expert judgments on held-out actions from GPT-4 and Llama3-70B to validate OOD generalization.
5. **Specify the fine-tuned LM's architecture and training** (model type, dataset, training objective) for reproducibility.

## Score and Decision

The paper presents a genuinely novel approach with strong empirical support and a creative data construction pipeline. However, the overclaimed theoretical guarantee and missing ablation study are significant gaps that prevent full confidence in the contribution. The empirical results are suggestive but not conclusively attributed to the proposed components. With revisions addressing the overclaiming and adding ablations, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>