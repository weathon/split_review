---
job_id: 9fc1cbff-dcbc-44c0-aee3-d3d7fb38984e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4iu9Lj0Ist.pdf
paper: Machine Unlearning Meets Continuous Learning: A Theoretical Foundation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, at the intersection of continual learning, machine unlearning, privacy, and learning theory.

## Minimum Quality
Pass ✅. The paper contains the required research components, including abstract, introduction, related work material, methodology, experiments, quantitative results, and conclusion; although I found substantial technical and empirical weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies certified machine unlearning in a continual learning setting, where tasks arrive sequentially and past datasets may no longer be fully available. The authors formalize a continual learning-unlearning problem, decompose post-unlearning excess risk into a continual-learning excess-risk term and an unlearning-loss term, and analyze two adaptations of existing certified unlearning ideas: a storage-free natural-forgetting / gradient-style method and a Hessian-based method with higher storage cost. The paper also provides a theoretical excess-risk bound for an $\ell_2$-regularized continual learning algorithm and a small-scale empirical study on MNIST with a linear classifier.

## Strengths
1. The paper addresses an interesting and timely problem setting. Bringing certified unlearning into continual learning is a natural and important question, and the paper does make a real effort to formalize this interaction rather than just proposing a heuristic.

2. The decomposition in Equations (6) and (7), on Page 4, is conceptually useful. Separating post-unlearning excess risk into an unlearning-induced term and a continual-learning excess-risk term gives the paper a coherent organizing principle, and this is one of the clearer aspects of the work.

3. I appreciated the attempt to compare two different design points, rather than pushing a single algorithm. Algorithm 1 emphasizes zero storage overhead, while Algorithm 2 emphasizes better approximation via second-order information. That trade-off is meaningful and relevant for practical continual systems.

4. Figure 1 on Page 2 is helpful. It gives a reasonably intuitive picture of the two-stage process, namely continual learning in Stage I and unlearning / publishing in Stage II, and clarifies the distinction between the internal model state and the released noisy model. Given how notation-heavy the paper becomes later, this figure plays an important role in grounding the setup.

5. The paper does not overclaim empirical breadth. The authors keep the experiments relatively modest and present them mainly as a sanity check for the theory, which is preferable to making sweeping practical claims from a tiny benchmark.

6. The storage discussion in Section 5.3 is a useful addition. The modified Hessian-based variant that combines forgetting and local Hessian storage is at least directionally sensible, even if it is only lightly validated in the main paper.

## Weaknesses
1. The main theoretical setting is too narrow relative to the claims and motivation, and the mismatch with modern continual learning is serious.  
   The entire theory rests on Assumption 2.1 on Page 3, namely that $\ell$ is $L$-Lipschitz, $\mu$-strongly convex, and $M$-smooth, and the core algorithm is the simple regularized update in Equation (1). This setup may be mathematically convenient, but it is far from the deep nonconvex models highlighted in the introduction, including ChatGPT-scale systems. I do not object to theory under simplifying assumptions per se, but the paper repeatedly frames itself as a theoretical foundation for continual learning and unlearning broadly. That is too ambitious given the very restrictive scope. In practice, most continual learning systems use replay, distillation, parameter-isolation, or adapter-style methods, not just an $\ell_2$ penalty to the previous iterate. This matters because the central conclusions, especially the claimed trade-off through $\lambda$, may be specific to this toy regularization-based setting rather than illuminating the broader problem.

2. The certified unlearning guarantee is underspecified and arguably not cleanly aligned with the algorithmic state that is actually maintained.  
   Definition 2.1, Equation (4), on Page 4, defines indistinguishability between the released model $\tilde w_t^{-\mathbf S_{1:t}}$ and the perfect retraining model $w_t^{-S_{\le t}}$. However, Section 4 explicitly notes that Algorithm 1 internally keeps the secret model $w_t$, which may still contain deleted-task information, and only the public model is noised. This is not a minor footnote, it changes what kind of unlearning guarantee the method offers. The paper says this is addressed in Appendix C.2, but in the main paper the guarantee is weaker than the high-level framing suggests. Since the method is presented as certified continual unlearning, the distinction between public release indistinguishability and system-side forgetting should be much more explicit in the main text. Otherwise, readers can easily walk away with an overstated impression of what is actually forgotten.

3. Several mathematical statements and derivations are hard to trust because the notation is inconsistent, definitions appear malformed, and some formulas seem incorrect on their face.  
   This is my biggest technical concern. A few examples:
   - In Definition 2.2 on Page 4, the task-wise population loss is defined as $F_\tau(w)=\mathbb E_{z\sim \mathcal D_t}[\ell(w,z)]$ for task $\tau$. That should presumably use $\mathcal D_\tau$, not $\mathcal D_t$. As written, the definition is inconsistent.
   - Equation (4) uses $\mathcal W$ both as the parameter space and as the measurable event inside the probability statement, which is confusing and formally sloppy. The event should likely be some measurable set $O \subseteq \mathcal W$.
   - In Theorem 4.1, Equation (9) on Page 5, the exponent $\rho^{1-s-n_{t,i+1}^{k}}$ appears inconsistent with the surrounding textual explanation. Immediately below, the paper says each unlearned task $s$ contributes a term proportional to $\rho^{t-s-\tau_{t,s+1}^{k}} \frac{L}{\lambda}$, which does not match Equation (9). This is not cosmetic, because the decay with time is the key insight.
   - Proposition 5.1, Equation (14) on Page 7, has multiple indexing and symbol issues. Terms like $\rho^{n_{t_i,s}^k-n_{t_i,s}^k}$ trivially equal $1$, suggesting a typo where two different indices were intended. The surrounding explanation also refers to examples that do not line up with the expression.
   - Proposition 5.2, Equation (15) on Page 8, includes $w_m^{S_{\le t}\setminus\{m+1,\ldots,t\}}$ and $w_m^{-\mathbf S_{1:m-1}}$, but $m$ is not clearly defined in the summation statement. The formula is too underspecified to be checkable.
   
   When the central results rely on these equations, this level of notation instability materially lowers confidence in the proofs.

4. The theoretical development contains multiple places where the object being differentiated or expanded changes notation in suspicious ways.  
   For example, in Appendix B and C the proof alternates between $\hat F_t$, $\tilde F_t$, and sometimes $F_t$ when writing first-order conditions and Taylor expansions, but the definitions are not kept consistent. In Lemma B.2, the proof starts from $\nabla \hat F_t(w_t)+\lambda(w_t-w_{t-1})=0$, then immediately Taylor expands $\nabla \tilde F_t(w_t)$ at $\hat w_t$. Unless $\tilde F_t$ is explicitly defined as the same object, that step is unjustified. Similarly, throughout Appendix C and D, the Hessian matrices $\hat H_i$, $\tilde H_i$, and $H_i$ are used with changing meanings. I understand that appendices can be rougher than the main paper, but here these are not harmless typos, they affect whether the derivations are even logically valid. Since the main contribution is theoretical, the burden for clean notation is higher than usual.

5. The excess-risk theorem is difficult to interpret and not convincingly connected to actionable insights.  
   Theorem 3.1, Equation (8), on Pages 4 to 5 gives a large bound with many nested sums and task-heterogeneity terms. In principle this is fine, but the paper does not do enough to explain which terms dominate, under what regimes the bound is informative, or how a practitioner would choose $\lambda$ without access to the unknown quantities $\|w_{\tau_j}^*-w_{\tau_i}^*\|$ and $\|w_{\tau_i}^*\|$. The brief discussion on Page 5 says the optimum depends on task differences and does not vanish under heterogeneity, but this remains qualitative hand-waving. If the core message is a trade-off controlled by $\lambda$, the paper should do more than say the best $\lambda$ depends on unknown task geometry. Right now the theorem reads more as an existence-of-bound exercise than an insight-rich result.

6. The empirical evidence is far too limited for the scope of the claims.  
   Section 6 evaluates only a linear softmax classifier on MNIST, split into 30 tasks. That is a very small and forgiving benchmark for a paper that motivates itself with modern continual-learning systems and claims a general theoretical foundation. There is no study on even moderately more realistic continual learning benchmarks such as Split CIFAR, Permuted MNIST with deeper models, or standard rehearsal/distillation baselines. The result is that the experiments do not provide much confidence that the proposed phenomena matter outside a highly simplified linear setting.

7. The experiments are not well aligned with the assumptions and, paradoxically, this weakens the paper rather than strengthening it.  
   On Page 9, the authors explicitly state that they “relax” the $\mu$-strong convexity assumption in experiments by using cross-entropy with a linear softmax model. But the entire theory, including Theorem 3.1, Theorem 4.1, and Corollary 5.3, depends on strong convexity. So the experiments are not really validating the theory as claimed, they are showing that some qualitative trends persist in a different setting. That can still be acceptable, but then the paper should be honest that the experiments are illustrative rather than theoretical validation. Right now Section 6 says “experiments on MNIST validate our theory,” which is too strong.

8. The results section is too narrow and lacks key baselines.  
   Table 1 on Page 9 only reports the Hessian-based method against perfect retraining, at $\lambda \in \{10,20,30\}$. There is no quantitative post-unlearning comparison for Algorithm 1 in the main table, even though one of the paper’s main claims is the trade-off between the two methods. More importantly, the table does not include practical baselines from continual learning or unlearning literature, not even non-certified heuristics or retraining-from-checkpoints variants, so it is impossible to judge whether the proposed methods are competitive in any meaningful sense. Also, the interpretation of Table 1 is not entirely reassuring: at $\lambda=30$, the Hessian-based unlearning accuracy slightly exceeds the reported “perfect retraining” accuracy, which the text calls a “loose accuracy upper bound.” This wording is odd, because perfect retraining should be the target reference, not merely a loose upper bound on accuracy. If noise is added, one would not expect systematic improvement over retraining without a more careful explanation of randomness and variance.

9. Figure 2 raises concerns about the claimed practical utility of the natural-forgetting algorithm.  
   In Figure 2(b) on Page 9, the natural forgetting method has substantially larger approximation error than the Hessian-based method across the full range of $\lambda$, and the gap is not small. Combined with Equation (10), this implies much larger noise and worse post-unlearning risk. The paper does acknowledge this to some extent, but the overall narrative still presents Algorithm 1 as a meaningful certified alternative because of zero storage cost. The problem is that Figure 2(b) suggests that, except perhaps for very old tasks and very particular $\lambda$, the approximation error may be too large for the method to be practically attractive. This matters because Algorithm 1 is not just a side note, it is one of the two headline methods.

10. The presentation quality is below the bar for a theory-heavy ICLR paper.  
   There are many grammatical errors, malformed expressions, and notation inconsistencies throughout the main paper. Examples include “only a few work” on Page 2, “unleamning” typos in Equations (6) and (7), the malformed line “Output: $\tilde w_t^{-\mathbf S_{1:t}} \leftarrow w_{t,0}+\epsilon_t$” in Algorithm 1 on Page 5 where $w_{t,0}$ is undefined, and several places in Algorithm 2 on Page 7 where superscripts are missing minus signs or formatting is broken. These issues make an already difficult paper harder to read and, more importantly, make it harder to distinguish typos from genuine technical mistakes.

11. The paper’s novelty claim is somewhat overstated relative to related work.  
   The paper does cite several relevant works on continual learning plus unlearning, especially Chatterjee et al. (2024), Liu et al. (2022), Cha et al. (2024), and Huang et al. (2025). So this is not a missing-citation complaint. My concern is instead that the framing “first theoretical foundation” is stronger than what is established. The paper analyzes one regularization-based continual learner, adapts two existing certified unlearning templates, and gives bounds under strong convexity. That is a useful first step, but “foundation” suggests broader coverage and cleaner, more stable formalism than the paper currently provides.

12. Some experimental details are not sufficiently specified for reproducibility or proper evaluation.  
   The paper does not clearly describe how $\lambda$ is selected, whether there is a validation split, whether reported test results are averages over multiple random task splits and random seeds, or what variance exists in Table 1 and Figure 2. Because Figure 2 and Table 1 are based on random task decompositions and unlearning sequences, the absence of error bars or repeated-trial summaries is a real weakness. In small benchmarks, variance can be large, and without it the reported trends may be partly an artifact of one split.

## Questions
1. Several equations in the main paper appear inconsistent or malformed, especially Equation (9), Equation (14), and Equation (15). Could the authors provide a cleaned-up version of these formulas and explicitly confirm whether there are typos in the exponents / indices? In particular, for Equation (9), what is the correct exponent governing forgetting decay as a function of current time $t$ and deleted task index $s$?

2. Can the authors clarify the exact scope of the certified unlearning guarantee in the main algorithmic pipeline? For Algorithm 1, is the guarantee only for the released model $\tilde w_t^{-\mathbf S_{1:t}}$, while the internal state $w_t$ may still encode deleted data? If so, I strongly encourage the authors to foreground that limitation in the main text rather than deferring it to the appendix.

3. How should one choose $\lambda$ in practice? The bounds in Equation (8) and Equation (10) depend on unknown quantities such as $\|w_i^*-w_j^*\|$. Is there a principled proxy or data-dependent procedure the authors recommend? A clearer prescription would substantially improve the paper’s usefulness.

4. Why does Table 1 show the Hessian-based method at $\lambda=30$ slightly outperforming the reported perfect retraining accuracy? Is this due to randomness, noise, or a difference between training and evaluation protocols? Please report averages and standard deviations across multiple seeds / task splits.

5. Please provide a more direct quantitative comparison between Algorithm 1 and Algorithm 2 on post-unlearning performance, not only approximation error. Right now Figure 2(b) suggests a large error gap, but the main table only reports the Hessian-based method. A side-by-side table of test accuracy and approximation error for both methods would be much more convincing.

6. Can the authors explain more carefully how the experimental setup relates to Assumption 2.1? Since the experiments use a non-strongly-convex objective, in what precise sense do they “validate” the theory rather than just illustrate the qualitative trends?

7. The paper would be much stronger with at least one experiment beyond linear MNIST. If the authors can add a modest but more realistic benchmark, even a shallow model on Split CIFAR or a standard continual benchmark with repeated seeds, that would materially increase my confidence.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns arise from the paper as presented. The work studies privacy-motivated machine unlearning and uses a standard benchmark dataset. I do note that the practical deployment implications of “certified unlearning” should be stated carefully so that readers do not overinterpret public-model indistinguishability as full system-side deletion, but this is primarily a scientific clarity issue rather than an ethics flag.

## Soundness Rating
2: fair. The paper has a reasonable high-level technical direction, but the main mathematical presentation contains enough inconsistencies and underspecified formulas that I am not fully confident in the correctness of several central claims, and the empirical support is limited.

## Presentation Rating
2: fair. The overall structure is understandable and Figure 1 helps, but the writing, notation, and algorithm statements need substantial cleanup. For a theory-heavy submission, the current exposition is too error-prone.

## Contribution Rating
2: fair. The problem is interesting and the framing has value, but the contribution feels like a narrow first step with limited empirical backing and insufficiently stable technical presentation to merit a stronger score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see the appeal of the problem and there is a potentially useful idea here, especially the decomposition of post-unlearning excess risk and the comparison of storage-free versus Hessian-based approaches. However, the paper currently falls short of ICLR standards because the theory is presented too sloppily for me to trust it fully, the assumptions are very restrictive relative to the broad motivation, and the empirical section is too small to compensate. With a careful revision of the math and stronger experiments, this could become a solid paper, but I do not think it is ready in its current form.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main equations, algorithms, figures, and tables carefully, although some notation problems make full verification unnecessarily difficult.