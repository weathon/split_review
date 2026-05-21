---
job_id: 3e1b700c-37bd-4501-bc06-cd0e563987de
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: XKLPlnfZzM.pdf
paper: Learning to Deaggregate: Large-Scale Trajectory Generation with Spatial Priors
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies diffusion-based generative modeling, transfer/generalization, and benchmarking for spatio-temporal trajectory data.

## Minimum Quality
Pass ✅. The paper contains the core components expected of a research submission, including abstract, introduction, methodological description, experiments/results, and conclusion; while the exposition and methodology have important weaknesses, they do not rise to the level of a desk-rejectable fatal flaw.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes TDDM, a hierarchical diffusion model for trajectory generation that conditions on region-level spatial priors, defined as marginal occupancy heatmaps, and then generates trajectories in a canonicalized coordinate frame. The paper argues that separating spatial allocation from temporal realization improves controllability and enables zero-shot transfer to unseen regions and even new cities. It also introduces an evaluation benchmark across Geolife, Porto, and Cabspotting, reporting gains over several GAN, VAE, and diffusion baselines on trajectory fidelity and distributional alignment metrics.

## Strengths
The paper tackles a relevant and practically meaningful problem. Large-scale trajectory generation with some degree of control, while avoiding sample-specific conditioning, is a sensible target, and the spatial-prior formulation is easy to understand at a high level.

The main empirical signal is reasonably consistent in the paper’s own benchmark. In **Table 1** on Page 8, TDDM is better than the listed baselines on essentially all KL-based distributional metrics, JS, Density, Trip, and Pattern, and is also competitive on TSTR and Length. The improvement is not just on one cherry-picked metric, which gives the method some credibility.

The ablation in **Table 2** on Page 9 is useful. In particular, removing the spatial prior hurts KL and JS substantially while leaving TSTR almost unchanged, which supports the paper’s central claim that the prior mainly helps coverage/proportionality rather than generic sequence realism. This is one of the more convincing parts of the paper.

The visual comparisons are also aligned with the quantitative claims. In **Figure 2** on Page 3, TDDM’s heatmap is visibly closer to the real Porto density than the baselines, especially in preserving sparse holes and sharper road-like support. Likewise, **Figure 3** on Page 5 gives a serviceable overview of how trajectory tokens, heatmap tokens, and the diffusion step token are combined in the transformer, which helps the reader understand the multimodal conditioning design.

The city-to-city and intra-city transfer setting is interesting. Even though I have concerns about how strongly the results support the stated generalization claims, evaluating transfer across geographically distinct datasets is directionally valuable, and **Table 3** on Page 10 suggests that the model does retain nontrivial utility under transfer.

The paper is also refreshingly explicit that the method is not a privacy method and does not provide privacy guarantees, which is an important clarification in this application area.

## Weaknesses
1. **The central probabilistic formulation is not well specified, and Equations (1)-(5) are conceptually muddled.**  
   On **Page 4**, Equation (1) writes
   \[
   p(x)=\int p(x\mid H)p(H)\,dl,
   \]
   but the integration variable is written as \(l\), not \(H\), which is already a notational error. More importantly, the paper then says “in practice, we set \(p(H)=p(H=f(r_c,\mathbb{X}))=p(r_c)\),” collapsing a distribution over priors into a distribution over regions. This means the model is really a region-indexed mixture, not a generic latent-variable model over \(H\). Equation (5),
   \[
   p(x)=\sum_{r_c} p(x\mid H=f(r_c,\mathbb{X}))p(r_c),
   \]
   is the actual operative model, but then the role of \(H\) as an independent random variable becomes mostly rhetorical. This matters because the paper’s conceptual contribution is supposed to be “learning to deaggregate from spatial priors,” yet mathematically the training and generation are defined via region-conditioned priors extracted directly from data. The current formulation overstates generality and obscures what is really learned.

2. **Several equations and algorithmic details are inconsistent or incorrect enough to hurt confidence in the implementation details.**  
   There are multiple examples:
   - In **Equation (4)** on Page 4, the indicator is written as \(\mathbbm{1}_{r_{c_{1,j}}}\), which looks like an indexing typo for \((i,j)\).
   - On **Page 5**, the text says canonicalization maps to \([-1,1]^D\), but **Algorithm 1, line 6** on Page 6 says normalize to \([0,1]^D\), and **Algorithm 2, line 11** transforms back from \([0,1]^D\). This is not a cosmetic issue, because the coordinate system defines the denoiser’s data distribution.
   - **Algorithm 1, line 10** omits the standard \(\beta_t/\sqrt{1-\bar\alpha_t}\) scaling if it is intended as DDPM noise prediction training, whereas **Equation (7)** in the appendix gives the standard form.  
   - **Algorithm 2, line 9** uses
     \[
     x_{t-1}= \frac{1}{\sqrt{\alpha_t}}(x_t+\epsilon_\theta(x_t,H,t))+\sigma_t z,
     \]
     which again does not match the usual reverse update implied by **Equation (7)**.  
   - In **Equation (11)** in the appendix, the argument of \(\epsilon_\theta\) includes \(\sqrt{\bar\alpha_t, x_0}\), which is malformed and should presumably be \(\sqrt{\bar\alpha_t}x_0\).  
   A few typos are forgivable, but here the core training/sampling equations, algorithm box, and coordinate normalization do not line up. For a diffusion paper, that is not a small blemish.

3. **The claimed “zero-shot” generalization is weaker than advertised because generation in target regions still requires access to target-region trajectories to compute \(H\).**  
   On **Page 6**, the paper explicitly states that in Algorithm 2, line 3, one computes the heatmap \(H=f(r_c, X_{\text{target}})\) from target trajectories. So the transfer setting is not “generate for a new city from nothing,” it is “generate conditioned on aggregate occupancy statistics extracted from target-city data.” That is a narrower and more conditional setup than the title, abstract, and introduction imply. The model does avoid sample-level conditioning, yes, but it still depends on target-domain trajectory observations. This distinction matters a lot for the stated scientific claim about generalization to new regions.

4. **The comparison is incomplete relative to the paper’s own stated claims about controllable and cross-city trajectory generation.**  
   The paper compares against TimeGAN, TimeVAE, COSCI-GAN, Diffusion-TS, and DiffTraj, and discusses ControlTraj, TrajGen, and COLA only textually. Given that the paper’s pitch is specifically about cross-region generalization and aggregate conditioning, this baseline set feels dated and only partially targeted. Even within the paper’s own narrative, the missing experimental comparison to stronger trajectory-specific or cross-city generation methods weakens the significance of the empirical gains. The benchmark may show improvement over the selected baselines, but it is less convincing as evidence of state-of-the-art progress on the broader problem the paper claims to solve.

5. **The experimental protocol has a serious model-selection issue: hyperparameters are tuned on only Geolife using JS, then reused everywhere.**  
   In **Appendix C.4** on Page 19, hyperparameter optimization uses only Geolife, for 50 trials, and optimizes the same style of distributional objective later emphasized in the main results. This can be defended as a practical choice, but it should be discussed as a limitation because the model is then presented as broadly transferable across cities and datasets. It raises the possibility that architectural and diffusion-step choices are overfit to one dataset’s geometry and sampling characteristics. More concerning, the baselines do not appear to receive equally detailed retuning treatment in the main paper, making the comparison harder to assess as fully fair.

6. **The evidence for robustness/generalization is thinner than the rhetoric suggests, and some numbers in Table 3 point to notable failures.**  
   In **Table 3** on Page 10, city-to-city transfer produces markedly worse KL-based metrics than full in-distribution training. For example, aggregated \(\mathrm{KL}_{\mathrm{sym}}\) rises from \(0.278\) to \(0.795\) when trained on Geolife and transferred, and Length error degrades from \(0.003\) to \(0.060\)-\(0.109\) depending on source city. The paper acknowledges Length deterioration, but the conclusions still read a bit too triumphant. “Robust fidelity and distributional generalization across cities” feels stronger than what the table supports. The model is promising under transfer, but the evidence looks more like partial transferability than a convincing demonstration of city-invariant temporal dynamics.

7. **The benchmark design and reporting are insufficiently rigorous in several places.**  
   The main benchmark tables, especially **Table 1** and **Table 2**, report many metrics without confidence intervals except for TSTR. For stochastic generative models, reporting only one run per dataset and point estimates for most metrics is not great practice. The text on **Page 7** says models are trained, sampled, and evaluated once per dataset, then averaged. That is fragile, especially when making broad comparative claims. Without multi-seed variation on the main distributional metrics, it is hard to know whether the gaps are stable.

8. **The qualitative evidence is helpful but also selectively framed, and some figures expose limitations the text does not discuss.**  
   The paper leans heavily on visual heatmaps like **Figure 2** and the appendix figures. In **Figure 2** on Page 3, TDDM is indeed closest to the original overall, but even there the generated sample panel still appears somewhat simplified relative to the real one, especially in lower-density branches. Likewise, the architecture schematic in **Figure 3** is useful, but it glosses over crucial implementation choices such as patch size, trajectory length handling, and whether variable-length trajectories are padded or cropped. The visuals support the paper’s story, but they do not substitute for careful quantitative uncertainty analysis, and the text occasionally treats them as stronger evidence than they are.

9. **The problem definition in Section 2 is weak and partially incorrect.**  
   On **Page 3**, the paper says the mapping is learned “without direct access to the unknown distribution,” which is standard, but then states the goal is for synthetic samples to be similar to samples from the known distribution, not the unknown target distribution. This is likely a writing mistake, but it is a sloppy one in a section meant to formalize the task. The section also contributes little beyond a generic description of generative modeling and does not sharpen the specific statistical problem solved by TDDM.

10. **The notion of “unconditional” generation is overloaded and somewhat misleading throughout the paper.**  
    The paper positions itself against trajectory-level conditioning and repeatedly refers to unconditional generation, yet the method is clearly conditional on spatial priors \(H\). This is not just semantics. If a method requires a target-region occupancy prior estimated from trajectories, it is a conditional generator, albeit under weaker and aggregate conditioning. The current framing overstates distance from conditional generation baselines.

11. **The exposition is uneven, with multiple notation issues and awkward claims that make the paper harder to trust than it should be.**  
    A non-exhaustive list: duplicated phrase “for new regions (even in unseen cities)” on **Page 4**; confusing use of \(r\), \(r_c\), and \(\mathcal R_{r_c}\) without a clean definition; inconsistent capitalization and metric naming, for example **Table 3** uses “IS” where the rest of the paper uses JS; the algorithms on **Page 6** are under-explained and have formatting artifacts. None of these alone would sink the paper, but together they create avoidable friction.

12. **Some empirical conclusions are stronger than the evidence warrants.**  
    For instance, the conclusion on **Page 10** says TDDM “sets new state of the art,” but the paper evaluates only the included baselines and does not establish broader coverage of current methods strongly enough to support that phrasing. Similarly, the statement that Porto may act as a “representative source dataset” is interesting, but based on only three datasets and should be framed much more cautiously.

## Questions
1. The biggest clarification I need is about the exact statistical object being modeled. Is the intended model
   \[
   p(x)=\sum_{r_c} p(x\mid H_{r_c})p(r_c),
   \]
   where \(H_{r_c}=f(r_c,\mathbb X)\) is deterministic, or is \(H\) supposed to be treated as a latent random variable with its own distribution? Please rewrite **Equations (1)-(5)** in a way that is internally consistent, and explain what is actually learned versus what is computed from data.

2. Please reconcile the coordinate system mismatch between \([-1,1]^D\) in **Section 3** and \([0,1]^D\) in **Algorithms 1 and 2**. Which one is used in implementation? This is central, not cosmetic.

3. Please provide the exact training and reverse-sampling equations actually used in code, especially since **Algorithm 1 line 10**, **Algorithm 2 line 9**, and the appendix DDPM equations do not match. If the algorithm box is shorthand, please say so and give the precise update.

4. For the zero-shot experiments, how much target data is required to estimate \(H\) robustly? A useful rebuttal would quantify performance as a function of the number of target trajectories used only for prior estimation. That would greatly clarify the practical meaning of the transfer claim.

5. Can the authors report multi-seed variance, at least for the main metrics in **Table 1** and **Table 2**? Since the paper currently reports point estimates for most metrics and appears to use one run per dataset, variance information would materially increase confidence.

6. Please explain how baselines were tuned. Were they re-tuned per dataset, or run with default/reference settings? Since TDDM receives dedicated hyperparameter search in **Appendix C.4**, fairness of the comparison matters.

7. The paper argues that sample-specific conditioning can increase memorization risk, but no memorization or privacy audit is presented. Do the authors have any empirical evidence for this claim, or is it purely conceptual? I am not asking for full DP guarantees, but even a nearest-neighbor or train-test leakage analysis would help.

8. The ablation in **Table 2** suggests that \(1\times1\) km improves Pattern but catastrophically hurts Length and KLspeed. What is the mechanism? Is it because shorter windows truncate longer temporal structure, or because region stitching distorts speed distributions? A more mechanistic explanation would make the paper stronger.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper is about generating realistic human mobility trajectories. Even though the authors explicitly note on **Page 11** that the method is not privacy-preserving and has dual-use risks, the application space includes surveillance, tracking, and misuse of synthetic but realistic mobility traces. In addition, the transfer setup uses target-region aggregate trajectory data to estimate spatial priors, so downstream users could mistakenly interpret the method as “safe synthetic generation” despite the absence of privacy guarantees. I do not see an ethics violation in the submission itself, but the topic warrants ethics awareness because of privacy and surveillance implications.

## Soundness Rating
2: fair. The empirical results are directionally interesting, but the mathematical specification, algorithmic consistency, and strength of support for the generalization claims are not strong enough for a higher score.

## Presentation Rating
2: fair. The paper is readable at a high level and figures help, but there are too many notation issues, inconsistencies between equations and algorithms, and overstatements relative to the evidence.

## Contribution Rating
2: fair. The spatial-prior conditioning idea is worthwhile, and the benchmark is useful, but the methodological step beyond existing conditional diffusion modeling is moderate, and the paper does not fully validate the stronger claims it makes.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a clear motivation, some genuinely encouraging empirical results, and a useful ablation, but the current version underspecifies the core model, contains too many inconsistencies in equations/algorithms, and overstates the meaning of its transfer experiments. With a tighter formulation, stronger baselines, and more rigorous evaluation, this could become a stronger submission.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the method, equations, figures, and tables carefully, though there remains some uncertainty because the paper’s own exposition leaves several implementation details ambiguous.