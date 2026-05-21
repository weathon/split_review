---
job_id: a5f2c661-ae34-4572-bbde-d631b87dcc4c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: r5Ii1GTEWj.pdf
paper: Motion-R1: Latent-Intent Motion Generation with Physical Consistency
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, generative modeling, language-conditioned motion generation, and physically grounded control for embodied AI.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, methods, experiments with quantitative and qualitative results, and conclusion. While there are serious issues in novelty positioning, methodological specification, and empirical support, these are review-stage weaknesses rather than desk-reject-level omissions.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Motion-R1, a two-stage framework for latent-intent human motion generation under physical constraints. The method combines a newly introduced Motion2Motion dialogue dataset, a GRPO-style reinforcement fine-tuning objective with a Jensen-Shannon divergence regularizer for high-level action/skill generation, and a low-level RL controller intended to enforce kinematic and dynamic feasibility. The experiments compare JS- and KL-regularized variants on action and skill generation metrics, include a qualitative example against Anyskill, and report GPT-4-based judging results.

## Strengths
The paper targets a meaningful problem. The gap between language-level intent understanding, especially for long or multi-turn inputs, and physically executable motion generation is real, and the attempt to connect high-level semantic reasoning with low-level physical control is directionally interesting.

The high-level decomposition is sensible. Separating intent inference / action-skill generation from low-level physically constrained execution is a reasonable systems design choice for this class of problems, and the paper does articulate this pipeline clearly at a conceptual level in Section 3.

The manuscript does provide a full pipeline rather than stopping at language-side evaluation. In particular, Section 3.3 at least attempts to connect textual motion descriptions to executable control via RL and style rewards, which is more ambitious than purely text-side instruction generation papers.

**Figure 1** is one of the clearer parts of the paper. It communicates the intended positioning of the work, namely that prior methods either miss physical constraints or fail on more complex contextual understanding, while the proposed pipeline tries to combine both. Even though the figure is schematic rather than evidentiary, it helps the reader understand the claimed motivation and the three-stage structure.

The paper includes both quantitative and qualitative evaluation artifacts. For example, **Table 1** and **Table 2** do show consistent numerical improvements of the proposed JS variant over the KL variant and over the listed unfine-tuned baselines, and **Figure 3** provides an intuitive qualitative comparison on a long-text skill extraction example.

## Weaknesses
I have substantial concerns about soundness, novelty positioning, and empirical support. The main issue is not that the paper’s direction is uninteresting, it is that the current version does not convincingly establish what was actually built, what part is new, and which claims are genuinely supported by the presented evidence.

1. **The paper’s central claim is much broader than the actual evidence shown.**  
   The title, abstract, and conclusion repeatedly claim “motion generation with physical consistency,” yet the main experiments in Section 4 are almost entirely on **text outputs**, specifically action generation and skill generation metrics such as semantic similarity, keyword matching, Jaccard, precision, and recall. These are language-side evaluations, not motion-generation evaluations. There is no quantitative evaluation of generated motions themselves, no standard motion-generation metrics, no physical realism metrics, no collision / foot sliding / penetration / stability statistics, and no success-rate measurements in simulation. This matters because the strongest claim of the paper is about physically consistent motion synthesis, but the presented tables support only text generation quality.

2. **The low-level physical component is dramatically under-evaluated relative to its importance in the paper’s claims.**  
   Section 3.3 introduces a low-level RL policy with rewards in **Equations (11) to (14)**, including a task reward and an adversarial style reward. However, Section 4 contains no real ablation or quantitative evaluation isolating this controller. The only concrete motion-side evidence is **Figure 3**, a very small qualitative comparison showing door-related behavior against Anyskill. That is far from enough to substantiate claims of “strict adherence to kinematic constraints” or “superior performance under physically constrained simulation environments.” A single visual example cannot stand in for a systematic physical evaluation.

3. **The novelty is insufficiently differentiated from existing planning-then-control or language-to-motion pipelines.**  
   The paper presents the combination of high-level language reasoning plus low-level physically grounded control as if this were a major methodological leap, but the manuscript does not do enough to explain what is genuinely new beyond combining existing ingredients: LLM-based instruction generation, GRPO-style RL fine-tuning, and AMP-style / adversarial low-level motion control. The related work discussion in Sections 2.1-2.3 is broad but not precise about the closest methodological neighbors. As written, the contribution feels more like a loosely connected assembly of known ideas than a sharply defined new algorithmic contribution.

4. **The proposed dataset contribution is underspecified and weakly validated.**  
   Section 3.1 describes Motion2Motion as a dataset of 7,132 annotated samples with latent-intent reasoning chains, but the paper provides almost no hard dataset characterization beyond **Figure 2**, which is merely a word cloud and a frequency histogram. Those visualizations are not enough for a benchmark paper or even a strong dataset component. The paper does not report train/validation/test split details, annotation protocol statistics, inter-annotator agreement, error rates, coverage across action classes, dialogue length distributions, or examples of the “latent intent reasoning chains” beyond a single JSON snippet in the appendix-like last page. This matters because the dataset is positioned as a core contribution and as the basis for RL training, yet readers cannot judge its quality or difficulty.

5. **Several equations are either imprecise, inconsistent, or insufficiently specified for reproducibility.**  
   There are multiple mathematical issues that need attention:
   - In **Equation (3)**, the GRPO objective uses  
     \[
     \min\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) A_i
     \]
     which is not the standard PPO-style clipping form. Normally one expects something like  
     \[
     \min\left(r_i(\theta)A_i,\ \mathrm{clip}(r_i(\theta),1-\epsilon,1+\epsilon)A_i\right).
     \]
     The expression written in the paper takes the minimum over three scalars directly and does not match the usual clipped surrogate objective. If this is intentional, the authors need to explain why; if not, the equation is simply wrong or at least miswritten.
   - In **Equation (5)**, the midpoint distribution \(m\) is mentioned but never explicitly defined as \(m=\frac{1}{2}(\pi_\theta+\pi_{\text{ref}})\). That is easy to fix, but it reflects the broader lack of care in the mathematical exposition.
   - In **Equation (4)**, the standardized reward  
     \[
     A_i=\frac{r_i-\mathrm{mean}(r_1,\dots,r_G)}{\mathrm{std}(r_1,\dots,r_G)}
     \]
     is undefined when the group standard deviation is zero. The paper does not mention an \(\varepsilon\)-stabilizer or any degenerate-case handling.
   - In **Equations (7)-(10)**, the reward model depends on \(\Phi_{\text{action}}\), \(\Phi_{\text{skill}}\), \(\mathcal{S}_{\text{BERT}}\), XML validity, and tree edit similarity, but none of these are concretely instantiated. What model produces \(\Phi_{\text{action}}\)? How are skills extracted from free-form responses? What XML schema is being enforced, and why is XML formatting central to motion generation? As written, the reward design reads more like a generic LLM structured-output recipe than a motion-specific objective.
   - In **Equation (12)**, the notation overuses \(D\) for both the discriminator and the data distribution, which is confusing. The first expectation says \((s_t,s_{t+1})\sim D\), but \(D\) is already the discriminator. This is a notational error that should have been caught.

6. **The exposition in Sections 3.1 and 3.2 often sounds generic and disconnected from motion generation.**  
   For example, the text motivating JS divergence emphasizes “structured generation tasks like XML/JSON formatting” on **Page 6**, which feels oddly detached from the paper’s stated goal of motion generation. Similarly, ERA-CoT is described using broad dialogue-analysis language, entity extraction, relationship triplets, and ontology consistency, but the paper never concretely demonstrates how these structures improve motion generation. The result is a paper that often reads like three partially connected projects stitched together: a dialogue dataset, an RL-for-LLM recipe, and a physical controller.

7. **The empirical baselines are too weak and not properly aligned with the paper’s claims.**  
   In **Table 1** and **Table 2**, the baselines are mostly unfine-tuned general LLMs, namely Qwen2.5 and Llama3.2 in different sizes. That is not enough. If the claim is about motion generation, then strong motion-language or text-to-motion baselines should be compared directly. The current setup makes the gains look larger than they really are, because beating an unfine-tuned base LLM on action/skill extraction is not the relevant bar for ICLR. This is especially problematic because the paper repeatedly frames itself against prior motion-generation systems.

8. **The result tables themselves raise questions about evaluation design and data difficulty.**  
   Looking at **Table 1**, the raw baseline numbers are extremely low, and some entries are suspiciously duplicated across different models, for example Qwen2.5 7B and Llama3.2 8B have exactly the same values in that table. In **Table 2**, Qwen2.5 7B and Llama3.2 8B again have nearly identical or identical values. Exact duplication across distinct models is possible but unusual enough that it deserves explanation. More importantly, the paper does not describe how CPS is computed, how references are normalized, or whether these metrics are averaged over multiple generations and seeds. Without that, it is hard to know whether the improvements are robust or artifacts of the evaluation pipeline.

9. **The GPT-4-as-judge evaluation is under-specified and too lightly interpreted.**  
   Section 4.3 and **Figures 4a and 4b** report rationality and relevance comparisons, but the judging prompt, number of samples, agreement procedure, randomness control, and exact scoring rubric are not given in the main paper. Since GPT-4 judgments can be sensitive to prompt wording and ordering, the lack of methodological detail limits how much weight these figures should carry. Also, the figures show percentage-like bars, but the axes and comparison setup are not sufficiently explained in the text.

10. **Figure 3 does not convincingly support the textual claim made around it.**  
    The surrounding text says Anyskill “cannot understand long text, and therefore cannot perform the knocking action, while our model can effectively understand the knocking action.” First, the example in **Table 3** describes “Kick the Door,” not “knocking action,” so the narrative is internally inconsistent. Second, **Figure 3** is only a short sequence of frames from one example, with no accompanying task metric, no prompt standardization details, and no evidence that both methods were given equivalent conditions. Qualitative examples are useful, but here the figure is over-asked to carry a strong comparative claim.

11. **The paper claims broader reasoning gains, including mathematical computation, that are not evidenced in the main paper.**  
    The abstract claims improved reasoning capability on both motion generation and mathematical computation benchmarks, but in the main paper the GSM8K result is only referred to as being in Appendix B, and only a tiny table appears at the end of the provided text. This is not integrated into the main empirical story, and it is not clear why better GSM8K performance would validate the proposed motion-specific contributions anyway.

12. **The presentation quality is well below the bar expected for a top conference.**  
    There are many signs of insufficient polishing: grammatical issues in the abstract and introduction, inconsistent naming of GRPO as “Generalized Reinforcement Policy Optimization” versus “Group Relative Policy Optimization,” malformed equations such as \(R^{\prime}*i\) and \(v*th\) in **Equations (1) and (2)**, awkward sectioning, and repeated high-level claims that are not matched by concrete implementation detail. The paper is readable in broad strokes, but not at the level needed for a technically ambitious claim.

13. **There is no convincing ablation isolating the value of the proposed ingredients.**  
    The main comparative claim is that JS divergence is better than KL divergence, and indeed **Table 1** and **Table 2** show small but consistent gains for JS over KL. However, this is not enough to justify the broader “Motion-R1” package. There is no ablation on ERA-CoT, no ablation on dataset size or annotation type, no ablation on each reward term in **Equation (6)**, and no ablation on the low-level RL controller. Therefore, even if the JS-vs-KL result is real, it does not demonstrate that the overall framework is meaningfully validated.

14. **The connection between the high-level output space and the low-level controller is not concretely defined.**  
    Section 3 says the GRPO model generates “motion descriptions” or “motion specifications,” but the interface to the low-level RL controller is never precisely described. Does the controller receive a skill label, a structured XML plan, a sequence of subgoals, or a latent embedding? This missing bridge is a serious issue because the paper’s core claim is about end-to-end intent-to-physical-motion generation. Right now, the bridge between language outputs and executable control is hand-wavy.

## Questions
1. The paper’s strongest claim is about physically consistent motion generation, but the main tables evaluate text outputs rather than motion. Can the authors provide **quantitative motion-side results in the main paper**, such as physical plausibility, collision/penetration rate, foot-sliding, contact consistency, task success, or standard text-to-motion metrics, and compare against strong motion-generation baselines?

2. Please clarify the exact optimization objective in **Equation (3)**. Is the intended objective the standard PPO/GRPO clipped surrogate
   \[
   \min\left(r_i(\theta)A_i,\ \mathrm{clip}(r_i(\theta),1-\epsilon,1+\epsilon)A_i\right),
   \]
   or something else? If something else, please derive it carefully and explain why it is preferable.

3. How exactly are \(\Phi_{\text{action}}\), \(\Phi_{\text{skill}}\), \(\mathcal{S}_{\text{BERT}}\), XML validity, and tree similarity instantiated in **Equations (7)-(9)**? A concrete implementation description would substantially increase confidence in reproducibility.

4. What is the exact interface between the high-level GRPO model and the low-level policy in Section 3.3? What structured representation is passed from one to the other, and how is it converted into goals \(g\) or low-level reward terms in **Equation (11)**?

5. For the Motion2Motion dataset, please provide in the rebuttal or revision the train/validation/test split, dialogue-length statistics, annotation protocol, quality-control procedure, and examples of the latent-intent reasoning chains. Right now **Figure 2** is too superficial to assess the dataset contribution.

6. For **Table 1** and **Table 2**, please explain the duplicated values across different baseline models, define CPS precisely, and report variance across runs or seeds. These details would materially affect confidence in the reported gains.

7. For **Figures 4a and 4b**, please specify the GPT-4 judging prompt, sample count, randomization/order control, and whether pairwise blind evaluation was used. If the judge evaluation is robustly designed, it would be more persuasive with these details.

8. Can the authors provide an ablation isolating the contribution of each component: Motion2Motion data, ERA-CoT annotation, JS regularization, reward terms in **Equation (6)**, and the low-level RL stage? This is necessary to determine whether the proposed framework is more than the sum of loosely connected parts.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work uses generated / curated dialogue-style annotations and motion synthesis in simulation. That said, if the dataset is released, the authors should clearly document data provenance, annotation practices, and any licenses governing underlying sources.

## Soundness Rating
2: fair. The broad idea is plausible, and some components are standard, but the main claims are only partially supported. The mathematical specification has notable issues, and the experiments do not adequately validate the claimed physical motion generation contribution.

## Presentation Rating
1: poor. The paper is difficult to assess due to imprecise equations, under-specified objectives, inconsistent terminology, and an empirical section that does not cleanly align with the headline claims.

## Contribution Rating
2: fair. The problem is important and the attempted combination of latent-intent reasoning with physical control is relevant, but the contribution is not yet convincingly differentiated or validated at the level expected for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an interesting problem and has a potentially useful high-level decomposition, but the current submission overclaims relative to the evidence, under-specifies crucial parts of the method, and evaluates mostly language outputs rather than physically consistent motion generation itself.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is possible some implementation details are omitted rather than absent. My main concerns come directly from the mismatch between the paper’s claims and the evidence presented in the main text, as well as from concrete issues in the equations and evaluation design.