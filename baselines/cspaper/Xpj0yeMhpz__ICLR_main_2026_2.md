---
job_id: 0f2f5156-f694-4e4f-aafd-c36def85bfc7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Xpj0yeMhpz.pdf
paper: Decoupling the Class Label and the Target Concept in Machine Unlearning
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, centered on machine unlearning, representation dynamics, and trustworthy ML, with clear relevance to representation learning, privacy, and safety.

## Minimum Quality
Pass ✅. The paper contains the required research components, including abstract, introduction, methodological development, experiments with quantitative results, and conclusion; despite multiple notation and exposition issues, it presents a nontrivial problem formulation, a concrete method, and substantial empirical evaluation.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies machine unlearning when the target concept to forget does not align with the model’s label space, formalizing three mismatch settings beyond the conventional class-wise case: target mismatch, model mismatch, and data mismatch. To address these settings, the authors propose TARF, a framework that combines annealed gradient ascent on identified forgetting data with selective gradient descent on retained data chosen via a representation-gravity signal, and they evaluate it across several image benchmarks and a few application-style case studies.

## Strengths
The main strength is the problem formulation. The paper goes beyond the standard assumption that “class label = forgetting target,” and this is not a cosmetic rephrasing. The mismatch taxonomy in **Figure 1** is useful and easy to grasp, and it motivates settings that are closer to how practical unlearning requests may arise, especially when the request is concept-level, coarser than the training taxonomy, or only partially specified. This broadening of the task itself is a meaningful contribution.

The empirical story is generally convincing. **Table 3** is the most important evidence in the paper, and it does show a consistent pattern: many standard unlearning baselines behave reasonably in the all-matched setting but degrade substantially in the mismatch settings, while TARF usually achieves a much smaller gap to retraining. The contrast is especially strong in target mismatch and data mismatch on both CIFAR-10 and CIFAR-100, where TARF gets near-zero UA with much better RA/TA trade-offs than FT or GA. Even if one debates some metric choices, the qualitative conclusion from the table is fairly robust.

I also appreciated that the paper does not stop at aggregate metrics. **Table 2** is helpful because it exposes the model-mismatch setting at a finer granularity inside a superclass. That table makes the intended claim more concrete, namely that forgetting one subclass while retaining nearby subclasses is where naive gradient ascent spills over, and TARF partially fixes that. This is a better diagnostic than only reporting the averaged “Gap”.

The representation-level analysis is one of the more interesting parts of the paper. **Figure 3** is genuinely informative: the left/right t-SNEs and corresponding loss trajectories support the narrative that entangled versus under-entangled features create different forgetting failures. I am usually skeptical of papers that wave around latent-space plots, but here the figure is paired with task-dependent behavior and connected to the method design. Similarly, **Figure 5** provides a reasonable visual explanation of the target-identification and target-separation phases, rather than just showing one more accuracy curve.

The method itself is relatively simple and operational. The TARF objective in **Equation (3)** is intuitive, and the idea of pairing a decaying forgetting term with selective retention is sensible for approximate unlearning. Compared with methods that only ascend on the forget set or only fine-tune on the retain set, TARF has a clear design rationale tied to the failure modes identified earlier in the paper.

The experimental coverage is broad for a main paper. Beyond CIFAR, the paper includes ImageNet-scale results in **Table 4**, additional architecture checks in **Figure 7**, and some exploratory applications. I would not overstate the realism of the case studies, but the authors did make an effort to test the framework outside the tiny-benchmark comfort zone.

## Weaknesses
1. **The theoretical part is much looser than the paper’s framing suggests, and several mathematical details are not properly specified.**  
   The central theoretical claim is **Theorem 3.2** on Page 4, but as written it is closer to an intuition sketch than a rigorous result. The update is stated as $\theta^{t+1} = \theta^t + \nabla L_{s_1}(\theta^t)$, while **Equation (2)** includes a factor $\eta$; the theorem statement and the bound are therefore inconsistent unless one silently absorbs the learning rate into the update. More importantly, the term $\lambda_{\max}(J_{\theta^t}(x_1))$ is not well defined if $J_\theta = \partial h(x)/\partial \theta$ is a general Jacobian, since this matrix is not necessarily square; presumably the authors mean an operator norm or largest singular value, but that is not what is written. The proof in Appendix C then introduces an $O(\epsilon)$ term without a precise definition and silently drops the Jacobian-difference term with only a hand-wavy “$O(\epsilon)$” argument. If the theorem is meant to support the method, these issues matter because the theory is doing real rhetorical work in justifying the “representation gravity” mechanism.

2. **The core selector $\tau(x,y,t)$ and the quantity $I_{\mathrm{con}}$ are underspecified in the main paper, which makes the algorithm hard to pin down scientifically.**  
   In **Definition 3.3** on Page 5, $I_{\mathrm{con}}(x,y,\theta)$ is defined as either a loss difference or, alternatively, “we can calculate class-wise accuracy change.” Then in **Equation (5)**, $\tau(x,y,t)$ depends on $I_{\mathrm{con}}(x,y,\theta_{t_1})$ and threshold $\beta$, but the actual operational choice is unclear from the main text. Is TARF using sample-level loss changes, class-level accuracy drops, or both depending on the scenario? How is this reconciled with the instance-wise notation of $\tau(x,y,t)$? This is not a minor implementation detail, because target identification is one of the paper’s main claims. Without a crisp main-text definition, the method can look more deterministic on paper than it really is.

3. **The paper relies on prior knowledge about the target structure that weakens the claimed generality, especially in target mismatch.**  
   On Page 3, the authors explicitly assume “that the number of classes in $\mathcal{D}_{\mathrm{un}}$ belonging to the target concept is known in target mismatch forgetting.” This is a strong assumption. In practice, when the whole point is that the target concept does not align with the training taxonomy, knowing in advance how many extra classes belong to the concept is already substantial semantic supervision. The method may still be useful under this assumption, but the paper oversells the practical breadth a bit. The target-identification phase in **Figure 5(a)** looks strong partly because the method is ranking under a quota that is externally known.

4. **The evaluation protocol mixes task-specific label spaces and then compresses everything into one averaged “Gap,” which is convenient but scientifically muddy.**  
   The issue is visible in **Table 3** and explained in Appendix B.2. In model mismatch, UA/RA/TA are evaluated using superclass labels, while in all-matched and target mismatch they are evaluated using class labels. Then the paper reports a single averaged gap to retraining, giving equal weight to UA, RA, TA, and MIA. This means the same “Gap” is aggregating metrics with different semantics across settings, and sometimes UA is near zero because of concept forgetting while in model mismatch the retrained UA is itself very high due to superclass labeling. The metric is usable as a rough summary, but the paper leans on it too hard. A reader could easily conclude the method is uniformly close to retraining across scenarios when the underlying notion of “unlearning accuracy” is changing.

5. **There are substantial notation inconsistencies and table/presentation errors in the main paper, enough to slow down careful reading.**  
   This is not just cosmetic. On Page 3, the dataset notation flips between $\mathcal{D}_l$, $\mathcal{D}_t$, $\mathcal{D}_f$, $\mathcal{D}_r$, $\mathcal{D}_{\mathrm{un}}$, and related sets, sometimes with apparent OCR or typesetting corruption in **Table 1**. **Equation (1)** has a typo in the underbrace label and a confusing statement of the retraining objective. **Remark 3.3** is used twice for different remarks. In **Table 3**, the TARF rows are visibly misaligned, which makes the CIFAR-100 entries hard to parse without cross-checking later tables. For a paper whose contribution partly depends on carefully distinguishing several datasets, label domains, and partitions, this level of notation drift matters more than usual.

6. **The claim that the method “approaches retraining” is not really established beyond heuristic optimization behavior.**  
   The language around **Equations (3) and (4)** and the discussion of Phase III suggests that TARF progressively approximates the retraining objective. But this is not shown in any formal sense, nor is there a direct trajectory analysis of distance to retrained parameters or outputs. **Figure 5(b)** gives a plausible empirical story that additional retaining epochs can reduce over-deconstruction, but that is much weaker than the surrounding wording implies. I would tone down the statement “$L_{\mathrm{TARF}} \rightarrow L_{\mathrm{retrain}}$” unless the paper can justify what kind of convergence is intended.

7. **The computational story is mixed, and the efficiency claims are weaker than the tables first suggest.**  
   In **Table 3**, TARF is often much slower than GA or other cheap baselines, sometimes by an order of magnitude, though still faster than full retraining. That by itself is fine. The issue is that the paper sometimes frames TARF as generally efficient, while its target-identification step requires scanning remaining data and computing ranking signals. The authors do discuss overhead later, but in the main paper the trade-off is understated. This is particularly relevant because the method’s advantage hinges on the extra identification machinery. A cleaner presentation would say bluntly: TARF buys better selectivity by paying more than simple ascent, but still much less than retraining.

8. **Some baselines are strong, but the comparison protocol still leaves room for concern about whether TARF is benefiting from more task-specific adaptation than the baselines receive.**  
   The paper compares against many representative methods, which is good, but TARF is explicitly tailored to the new mismatch settings while most baselines are used more or less off-the-shelf. That is not inherently unfair, but it does mean the headline is partly “a method designed for this problem beats methods designed for a different assumption.” This is especially visible in **Figure 2**, where the result is used to motivate TARF, but those methods are not given analogous mismatch-aware variants. The comparison still has value, but the paper should acknowledge more directly that the setup favors methods that can use additional structure such as target-size priors and ranking-based retain selection.

9. **The paper’s use of attack terminology and privacy metrics is sloppy in places.**  
   On Page 7 the text defines MIA as Membership Inference Attack, which is standard, but Appendix B.2 calls it “Model Inversion Attack” while describing a confidence-based membership inference predictor. These are not the same thing. Since privacy-oriented unlearning papers are often scrutinized on evaluation details, this inconsistency undermines confidence in the metric description even if the implementation may be standard in practice.

10. **The application sections are interesting but too thin to carry much evidentiary weight in the main-paper argument.**  
   **Figure 6** and **Table 5** are presented as real-world applications, but in the main paper they are under-explained and partly reliant on appendix details. The TOFU table is also difficult to parse as presented, with formatting irregularities and little context on what the numbers mean relative to standard baselines. I would not count these as strong validation in their current form. The core classification experiments are doing most of the actual evidentiary work.

## Questions
1. Please clarify exactly how target identification is implemented in the main experiments. Is $\tau(x,y,t)$ computed from per-instance loss change, per-class accuracy drop, or scenario-dependent variants of both? A precise main-text definition would substantially increase my confidence.

2. In **Theorem 3.2 / Equation (2)**, what is the intended meaning of $\lambda_{\max}(J_{\theta^t}(x_1))$ when $J_\theta$ is a Jacobian from parameters to representation? If this is meant to be an operator norm or largest singular value, please state it explicitly and revise the proof accordingly.

3. How sensitive is TARF to misspecifying the amount of false-retaining data or the number of extra target classes in target mismatch? The current formulation assumes this quantity is known. If the estimate is wrong, does performance degrade gracefully or sharply?

4. Could the authors provide a more direct retraining-approximation analysis, for example output-space KL to the retrained model over time, rather than relying mostly on the aggregate “Gap” metric? This would better support the narrative around Phase III.

5. In **Table 3**, TARF is often best on Gap, but not always best on the individual RA or TA values. Could the authors discuss when TARF’s selective retention helps most, and when it still over-deconstructs representations relative to methods like SCRUB?

6. For the model-mismatch setting, **Table 2** is useful. Could the authors add similarly fine-grained analyses for target mismatch and data mismatch, separating the initially given forgetting subset from the unidentified false-retaining subset? That would make the claimed identification mechanism easier to verify.

7. Please clarify the privacy metric terminology. The paper alternates between membership inference and model inversion wording. Which attack is actually implemented?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work studies machine unlearning and concept removal, which intersects with privacy and safety applications, but the paper itself does not raise an ethics issue that requires special review based on the provided main-text content. The datasets are standard public benchmarks, and the method is framed as improving controlled forgetting rather than enabling harmful capabilities.

## Soundness Rating
3: good. The main empirical claims are generally supported, but the mathematical presentation and some methodological details, especially around the selector and theorem, need tightening.

## Presentation Rating
2: fair. The paper is readable at a high level, but notation drift, table formatting issues, and several imprecise definitions materially hurt clarity.

## Contribution Rating
3: good. The mismatch formulation is valuable and the empirical evidence suggests a useful advance for approximate unlearning beyond standard class-wise settings.

## Overall Rating
8: Accept, good paper (poster). The paper opens up an important and underexplored formulation of machine unlearning, and the empirical results, especially in **Table 3**, support the claim that conventional methods break under label-domain mismatch while TARF improves the retraining approximation. I do have real reservations about the looseness of the theory, the dependence on prior target-size information, and the messy exposition, so this is not close to spotlight level for me, but I still view it as a worthwhile contribution for ICLR.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main technical and experimental details carefully, though some implementation choices remain difficult to verify from the main text because of notation and exposition issues.