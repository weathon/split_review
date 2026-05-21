---
job_id: c7d6036a-d23c-4cda-9839-cb8bb7852a14
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: W42oLSwI9p.pdf
paper: One-step Diffusion Solver for Non-binary Integer Linear Programming
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, sitting at the intersection of generative models, optimization, graph learning, and neural solvers for structured prediction.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, methodology, experiments with quantitative results, and conclusion/limitations; while there are notable technical and empirical weaknesses, they do not rise to the level of an immediate desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes three one-step diffusion-style neural solvers for integer linear programming, CMILP, SCMILP, and MFILP, with the goal of reducing the high inference cost of prior diffusion-based ILP solvers. To extend beyond binary ILP, the paper introduces an Iterative Integer Projection (IIP) layer for non-binary integer outputs, and it further adds objective-guided sampling with a momentum variant to improve feasibility and solution quality. Experiments are reported on binary ILP benchmarks, synthetic non-binary ILP datasets, and inventory-management-style instances.

## Strengths
The paper tackles a relevant problem. Most neural ILP work is indeed much more developed for binary settings, and the attempt to handle bounded non-binary integer variables directly, instead of binarizing them, is practically meaningful.

The runtime motivation is well taken. The paper is correct to identify inference speed as a major bottleneck of diffusion-based optimization methods, and the choice to explore one-step or few-step generative solvers is aligned with an important practical pain point.

The empirical section is reasonably broad in task coverage. The authors evaluate on three classic binary ILP families, several inventory management variants, and synthetic random ILPs. This is better than a narrowly scoped demonstration on one toy domain.

The proposed IIP mechanism is simple and easy to understand. In **Figure 2**, the iterative map visually shows how repeated application of \(f_{\mathrm{proj}}(x)=x-\frac{\sin(2\pi x)}{2\pi}\) sharpens values toward integers. Even though I have concerns about the theoretical treatment, the figure does help readers grasp the intended behavior quickly.

The paper does provide useful head-to-head runtime comparisons against prior diffusion baselines. For example, in **Table 2** and **Table 3**, the proposed methods are often orders of magnitude faster than IP Guided DDPM and materially faster than IP Guided DDIM, which supports the central speed claim. On several non-binary datasets, the proposed solvers appear to offer a favorable speed-quality tradeoff relative to prior neural generative baselines.

The architectural overview in **Figure 1** is helpful at a high level. It makes clear that the same projected-graph representation is shared across the three one-step solver variants and that objective-guided sampling acts after decoding. This figure improves accessibility of what would otherwise be a somewhat fragmented method section.

## Weaknesses
1. **The core mathematical formulation is much less rigorous than the paper’s claims suggest, especially around the consistency objective and posterior-guidance derivation.**  
   The most serious issue is that several equations are stated in a way that is either underspecified or mathematically dubious. In **Equation (6)**, the target is written as \( \delta(\mathbf{x}-\mathbf{x}^*) \), yet \(f_\theta(\mathbf{x}_t,t,\mathcal P)\) seems to output a sample, feature, or decoded solution rather than a probability distribution. A distance \(d(\cdot,\cdot)\) between a model output and a Dirac delta is not meaningfully defined unless the output space and metric are explicitly specified. The paper says this loss is minimized only if consistency holds across all trajectories and yields the optimal solution distribution, but that implication is not established. As written, this is not a valid consistency-model derivation; it reads more like an intuition sketch than a trainable, well-defined objective. Since CMILP is one of the paper’s central methods, this matters a lot.

2. **The objective-guided sampling section contains notation and derivations that are difficult to reconcile with a correct probabilistic formulation.**  
   In **Equation (7)**, the objective \(F\) includes terms like \(-\log Z - \mathbf y^*\), where \(\mathbf y^*\) is introduced as a conditional quantity and later as the minimum of \(l(\mathbf x;\mathcal P)\) in **Equation (8)**. The dimensions and semantics are unclear. Also, \(q(\mathbf x|\mathcal P)\) is first approximated as a point mass \(\delta(\mathbf x-\boldsymbol\eta)\), yet the expectation is over \(q(\mathbf h|\boldsymbol\eta,\mathcal P)\), and it is never clearly shown how differentiation through the latent trajectory yields the stated update. This section appears to borrow from plug-and-play posterior guidance arguments, but the adaptation to the current latent-solution-decoder setup is incomplete. Given that objective-guided sampling is presented as a key improvement, the lack of a clean derivation weakens confidence in the method.

3. **The paper’s claim that previous guidance is “a special case of gradient descent” is asserted much more strongly than it is justified.**  
   In **Section 3.3**, the paper states that previous guidance methods can be viewed as a single optimization step and then introduces momentum via **Equation (9)**. However, this equivalence depends heavily on the exact form of the guidance operator, step size, variable parameterization, and whether the decoder is linear or not. None of this is spelled out. Right now the paper is effectively saying, “our sampling refinement resembles iterative gradient optimization, therefore prior guidance is a special case,” which is too hand-wavy for a methodological claim of this kind.

4. **The IIP layer is interesting, but the paper does not analyze important properties that directly affect trainability and correctness.**  
   The projection map in **Equation (3)** is differentiable and has fixed points at integers, but the paper does not discuss the derivative  
   \[
   f'_{\mathrm{proj}}(x)=1-\cos(2\pi x),
   \]
   nor the behavior of repeated composition \(f_{\mathrm{proj}}^{(K)}\). Around integers, the derivative is zero, which can help stabilization, but around half-integers it can be as large as \(2\), so repeated composition can also distort gradients in nontrivial ways. The paper also does not discuss whether this map preserves bounded domains, how it interacts with upper/lower bounds, or whether multiple iterations at test time but only one at train time create a train-test mismatch. **Figure 2** provides intuition, but the paper needs more than a pretty staircase approximation to justify the practical optimization behavior of the layer.

5. **The method description is incomplete in several places, making the work hard to reproduce and hard to evaluate scientifically.**  
   Some examples: the paper says it collects “500 optimal and sub-optimal solutions” per instance on **Page 4**, but it does not explain how these solutions are generated, what diversity criterion is used, whether duplicates are removed, or how suboptimality is bounded. The transformer encoder/decoder setup is described only at a very high level, and key details such as latent dimensionality, conditioning mechanism, decoder parameterization, and training schedules are absent from the main paper. The penalty coefficient \(\lambda_{\mathrm{penalty}}\) in **Equation (2)** is introduced but not specified in the main text. These are not cosmetic details, because performance and feasibility can be highly sensitive to them.

6. **The empirical story is mixed, and some of the tables undercut the paper’s stronger claims.**  
   The paper repeatedly emphasizes “superiority” and near-perfect feasibility, but the actual numbers are more uneven. In **Table 1**, on binary ILP, the proposed methods are faster than DDPM/DDIM but often have very large optimality gaps, and they are clearly worse than IP Guided DDIM on gap across all three benchmark families. For example, on CA, CMILP/SCMILP/MFILP report gaps around \(79\%\) to \(85\%\), while IP Guided DDIM reports \(25.4\%\). That is not a small difference. If the main claim is “comparable performance with much faster inference,” that can be defended; if the claim is broad superiority, the table does not support it.

7. **The binary ILP comparison against classical and hybrid methods is not very convincing as a case for practical adoption.**  
   In **Table 1**, Gurobi achieves \(0\%\) gap with 100% feasibility under the stated budget, and even some traditional heuristics are competitive in settings where the proposed models still have large gaps. On these datasets, the paper’s own results suggest that the neural methods are mainly attractive for speed relative to slow diffusion baselines, not as serious alternatives to mature solvers. That narrower takeaway is still acceptable, but the writing oversells practical competitiveness.

8. **The non-binary experiments are useful, but the evaluation protocol makes it hard to separate modeling advances from dataset simplicity and solver-specific tuning.**  
   Many non-binary datasets are synthetic or semi-synthetic, with all labels produced by Gurobi and only 800 training / 100 test instances. This is not inherently wrong, but the paper does not study distribution shift, generalization to unseen sizes beyond a few hand-picked settings, or sensitivity to bound size in a systematic way. For example, **Tables 2 and 3** show strong speedups, but feasibility and gaps degrade substantially as the bound or scale increases, especially on IM-(50,5,10) and IM-(100,10,2). The resulting picture is less stable than the narrative suggests.

9. **Some table entries and metric definitions raise correctness and clarity concerns.**  
   In **Section 4.1**, Gap is defined as
   \[
   \frac{|e^{\top}\mathbf{x}_{gt} - c^{\top}\mathbf{x}_{pred}|}{|e^{\top}\mathbf{x}_{gt}|},
   \]
   but the objective in the ILP is \(c^\top x\), not \(e^\top x\). This looks like a notation error in the metric definition, and it should be corrected because it directly concerns evaluation. There are also several suspicious table typos, for example “rms” instead of “rins” in **Table 2/3**, “nus” and “leaspump” in **Table 6**, and duplicated row labels in **Table 5** where both first two rows are listed as “SCMILP (\(T_i=10\), Opt+MGD)”. These issues may sound minor, but when they appear in the main quantitative evidence, they reduce trust.

10. **The improvement due to momentum-guided search is rather modest and under-analyzed.**  
    The momentum extension is framed as an important contribution, and **Figure 3** gives an intuitive cartoon of why momentum can help reach feasible regions faster. But in **Table 5**, the gain appears limited, a few percentage points in dataset feasibility and a relatively small change in gap. The table is also too narrow: it only evaluates one dataset family and one model class. If momentum is a core contribution, I would expect broader ablations across CMILP, MFILP, multiple datasets, and sensitivity to \(\gamma\) and step count.

11. **The paper’s positioning against prior work is incomplete in a way that hurts the novelty argument.**  
    The related work covers Zeng et al. (2024), Nair et al. (2021), and Tang et al. (2025), but the discussion of diffusion-based ILP solving is still too narrow. There has been related work on diffusion-guided ILP search in hybrid symbolic-neural settings, which is relevant for contextualizing what is actually new here: is it one-step distillation, end-to-end feasibility prediction, non-binary handling, or all three together? The paper would benefit from a sharper novelty decomposition rather than bundling several partially incremental ideas into one package.

12. **Presentation quality is below the bar expected for a methods paper with this many moving parts.**  
    There are many notation inconsistencies and awkward statements. A few examples: on **Page 5**, \(\alpha_t\) and \(\bar\alpha_t\) are written with malformed notation; in **Equation (6)**, \(x_t\) and \(x_t'\) appear with inconsistent bolding and undefined spaces; in **Equation (8)**, the optimization variable is \(\mathbf x\) but the objective uses \(\mathbf z=\text{Decoder}(\mathbf x)\), which blurs latent and solution space. These issues make it difficult to tell whether some statements are just poorly written or conceptually incorrect. For a paper whose central value is methodological, that distinction matters.

## Questions
1. **Can the authors give a precise, self-contained derivation of the CMILP loss in Equation (6)?**  
   Please specify exactly what \(f_\theta\) outputs, what space \(d(\cdot,\cdot)\) operates in, and how the Dirac target \(\delta(\mathbf x-\mathbf x^*)\) is implemented in practice. If the actual implementation differs from the written equation, please say so explicitly.

2. **Can the authors clarify the posterior-guidance derivation around Equations (7) and (8)?**  
   In particular, what is \(\mathbf y^*\) concretely, scalar optimum value or conditioning variable, why does it appear additively inside \(F\), and how do you obtain the gradients with respect to \(\boldsymbol\eta\) when decoding from latent space? A cleaner derivation here would increase my confidence substantially.

3. **What are the train-time and test-time values of the IIP iteration count \(K\), and how sensitive are results to this mismatch?**  
   Since the paper states that fewer iterations are used in training and more in testing, it would be helpful to see an ablation over \(K_{\text{train}}\) and \(K_{\text{test}}\), as well as whether repeated projection ever harms feasibility or objective quality.

4. **How are the “500 optimal and sub-optimal solutions” obtained for each instance?**  
   Are they sampled from solver solution pools, local perturbations, heuristic restarts, or some other mechanism? Also, how often do you actually have 500 distinct solutions per instance, especially for binary tasks?

5. **Can the authors provide broader ablations isolating the sources of gain?**  
   I would like to see, in the main setting, at least: (i) one-step model without IIP, (ii) one-step model with IIP but without feasibility penalty, (iii) without objective-guided sampling, and (iv) with GD vs MGD across more than one dataset. Right now it is difficult to tell which component is carrying the method.

6. **How should readers interpret the paper’s practical claim relative to IP Guided DDIM and to commercial solvers?**  
   On several datasets, especially **Table 1**, the proposed methods are much faster than DDIM but substantially worse in gap, and still far worse than Gurobi in quality. Is the intended message “fast neural warm-start / feasible-solution generator” rather than “solver replacement”? A more calibrated claim would help.

7. **Please correct the metric notation in Section 4.1 and audit the tables for possible typos.**  
   The use of \(e^\top x\) instead of \(c^\top x\) in the gap definition, and row-name inconsistencies in **Tables 5 and 6**, make it difficult to fully trust the quantitative reporting.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are apparent from the paper. The work studies general-purpose optimization methods and does not appear to involve sensitive data, human subjects, or direct high-risk deployment claims.

## Soundness Rating
2: fair. The paper has a plausible high-level idea and a nontrivial empirical effort, but several central mathematical formulations are underspecified or questionable, and the experiments do not fully support some of the stronger claims.

## Presentation Rating
2: fair. The paper is readable at a high level, and the figures help, but the notation, derivations, and several result tables need substantial cleanup for the methodology to be evaluated with confidence.

## Contribution Rating
2: fair. The direct treatment of non-binary ILP and the emphasis on one-step diffusion-style inference are meaningful directions, but the novelty is not crisply isolated and the evidence for the claimed advances is mixed.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is aiming at an important problem and has some promising ingredients, especially direct handling of non-binary ILP and much faster inference than prior diffusion baselines. However, the current version overclaims relative to the evidence, the mathematical core is too loose in several places, and the empirical story is not strong enough to offset that. With a cleaner formulation and sharper experimental analysis, this could become a solid paper, but I do not think the current submission is ready for ICLR main-track acceptance.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details because the presentation of the math and training objectives is often imprecise.