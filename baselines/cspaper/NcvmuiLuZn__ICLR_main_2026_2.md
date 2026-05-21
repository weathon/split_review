---
job_id: 1fe4a7da-a897-49f6-bddd-4cebd01b93d5
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: NcvmuiLuZn.pdf
paper: Noise-to-Process Transformation: A Weak-Prior Paradigm for Single-Trajectory Stochastic Process Modeling
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on probabilistic modeling, uncertainty quantification, generative process modeling, and learning from sparse single-trajectory observations.

## Minimum Quality
Pass ✅. The submission contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments with quantitative/qualitative results, and conclusion. While I see substantial concerns about novelty, methodology, and empirical support, these are review-level weaknesses rather than desk-rejection-level omissions or fatal procedural flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, prompt-injection attempts, or other manipulative content targeting automated reviewers in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes a noise-to-process (N2P) paradigm for single-trajectory stochastic process modeling, where a shared i.i.d. base-noise process is mapped by a single measurable generator to an entire trajectory, with the stated goal of obtaining projective consistency by construction. The paper instantiates this idea with Deconvolution-Based Process Transformation (DBPT), a deconvolutional generator trained from a single observed trajectory using masked MSE on observed indices. Empirically, the authors evaluate DBPT on synthetic trajectories, financial time series, image completion, and black-box optimization, and compare against GP-based, Markov, DKL, SDE, and CNP baselines.

## Strengths
The paper tackles a genuinely interesting setting, single-trajectory stochastic process modeling with uncertainty, which is harder and less saturated than the usual multi-trajectory neural process regime. I appreciate the attempt to formulate a unified pathwise view across time series, images, and surrogate modeling.

The central construction is simple and easy to state: one shared noise source, one generator, one full trajectory sample. That makes the projective-consistency observation in **Proposition 3** mathematically clean. Even if the result itself is straightforward, the paper does a reasonable job of expressing why generating the whole path jointly is preferable to stitching together pointwise conditionals.

The architecture is also easy to understand from **Figure 1**. The pipeline from base noise, to noise encoder, to deconvolution-based decoder, to full target process gives a clear picture of what the authors are trying to operationalize. In particular, the figure helps explain the intended role of deconvolution, namely to impose multi-scale coupling across nearby indices rather than treating target points independently.

The empirical section is broad in coverage. The paper does not restrict itself to one toy benchmark, but includes synthetic examples, finance time series, image completion, and black-box optimization. This breadth is useful for stress-testing whether the method is meant as a general process model rather than a task-specific architecture.

There are some visually convincing qualitative results. In **Figure 3**, DBPT clearly appears better than GP/WGP/Markov and generally cleaner than DKL/CNP on the shown MNIST and CIFAR examples. The additional MNIST/CIFAR examples in **Figures 6 and 7** are also consistent with the claim that the model can produce coherent completions from sparse observations.

Among the quantitative tables, **Table 2** is the strongest piece of evidence in the paper. On the image completion benchmarks, DBPT is first by average rank and outperforms the listed baselines by a substantial margin on both PSNR and SSIM. Whatever one thinks of the broader stochastic-process framing, the deconvolutional generator appears empirically effective on this task.

The ablation-style visualization in **Figure 8** is useful. It at least supports the narrower claim that the deconvolutional decoder is doing something nontrivial relative to MLP and Transformer replacements in the authors' setup.

## Weaknesses
1. **The core conceptual contribution is overstated, and the paper does not adequately distinguish its main idea from prior implicit process / generator-based function-space models.**  
   The main text presents N2P as a new weak-prior paradigm for stochastic-process learning, but the actual construction, sampling base noise and passing it through a measurable generator to obtain a random function or trajectory, is a fairly standard implicit generative view of stochastic processes. The paper discusses GPs, SDEs, NPs, flows, and diffusion models in **Section 3**, but it does not engage with prior work on implicit or generator-defined stochastic processes in a sufficiently direct way. This matters because much of the claimed novelty in **Definition 1**, **Proposition 2**, and **Remark 4** depends on whether the paper is introducing a new modeling principle, or mainly renaming a familiar one with a specific deconvolutional instantiation. As written, the positioning makes the contribution appear broader and more original than the paper substantiates.

2. **The theoretical claims around projective consistency are correct but much weaker than the surrounding framing suggests.**  
   In **Proposition 3**, the paper shows that if a probability law $\mu_\theta$ is defined on the full path space and one takes coordinate projections, then the induced finite-dimensional marginals are projectively consistent. That is true, but it is essentially a basic property of pushforwards and projections, not a deep modeling guarantee. The paper rhetorically treats this as a major differentiator, yet any model that defines a joint law over the full discretized trajectory inherits the same property. So the theory is not wrong, but the gap between the simplicity of the claim and the strength of the advertised takeaway is large. This matters scientifically because the main formal pillar of the paper does not by itself justify the stronger claims of process-level probabilistic modeling quality.

3. **The actual training objective in the main paper is just masked reconstruction with latent noise resampling, and there is no principled probabilistic fitting criterion.**  
   The key learning objective in **Section 2.3.2** is
   $$
   \mathcal{L}(\theta)=\mathbb{E}_{Z}\!\left[\frac{1}{|\tau_o|}\|R_{\tau_o}\widehat X(\mathcal T)-O\|_F^2\right].
   $$
   This is just a masked MSE over observed entries, averaged over latent noise samples. There is no likelihood model, no variational objective, no score matching, no posterior inference, and no calibration term beyond whatever stochasticity the generator chooses to retain. In fact, minimizing expected squared error can easily encourage low-variance or mean-regression behavior unless the architecture itself induces useful randomness. The paper repeatedly claims "flexible uncertainty quantification" and "calibrated uncertainty", but the main-text objective does not make those claims obvious. This is not a nitpick, it goes to the heart of whether DBPT is really learning a process distribution, or simply a stochastic regressor trained by reconstruction loss.

4. **The uncertainty evaluation protocol is weak and potentially quite brittle.**  
   In **Appendix E**, NLL is computed by building per-index histograms from $10{,}000$ trajectory samples and then evaluating a piecewise-constant density at the ground truth. This is an unusual and very coarse density-estimation layer on top of the model outputs. The paper does not justify the choice of number of bins, bin width, sensitivity to histogram construction, or how this interacts with heavy-tailed or multi-modal predictions. Since several main conclusions, especially in **Table 1**, rely on NLL differences, the fragility of the density estimator matters. A method can look better or worse depending on histogram discretization rather than actual probabilistic quality.

5. **The empirical evidence for the flagship single-trajectory stochastic-process claim is not strong enough.**  
   The paper spans many tasks, but each individual evaluation is relatively thin. The synthetic section in **Figure 2** is purely qualitative. It helps visually, but it is not enough to support broad claims about robustness, calibration, or adaptability. On the finance benchmarks in **Table 1**, DBPT is not dominant: WGP has the best average rank, and DBPT trails it overall. The authors argue that DBPT trades MSE for better NLL, but even that story is mixed, because on BIA, CNP beats DBPT in MSE and WGP beats DBPT in NLL and MSE. So the strongest numerical story is really image completion, not general stochastic-process modeling.

6. **Several baselines are either underdeveloped, unfairly contextualized, or insufficiently competitive for the paper's framing.**  
   The paper compares mainly to GP, WGP, Markov, DKL, SDE Matching, and CNP in **Section 4**, but the discussion of data-driven process models is too narrow for the strong claims made against neural-process-style approaches. For example, the paper repeatedly treats CNP as representative of that entire family, yet stronger variants such as attention/convolution/transformer-based NP models are not evaluated in the main paper. This matters because the paper's central positioning is partly "we work in the single-trajectory regime where data-driven process models falter", so the burden is on the authors to compare against stronger representatives of that family, not only a basic CNP.

7. **Some mathematical statements in the appendix are too strong relative to the assumptions actually linked to the main setting.**  
   The "identifiability" discussion in **Appendix D** is especially shaky as support for the main method. **Proposition 19** proves path identifiability under dense random masks, increasing sample sets, Hölder regularity, vanishing empirical risk, and universal approximation. But the actual experiments in the main paper involve a single fixed trajectory with finite sparse observations, not an asymptotic sequence of denser masks. Likewise, **Theorem 22** on process-law identifiability "up to noise isomorphism" is mathematically detached from the practical learning problem because the paper never observes process-law samples, only one partially observed realization. These results may be mathematically valid under their own assumptions, but they do not meaningfully justify the claims made for the finite-data training setting used in the experiments.

8. **The generalization result in Appendix C relies on assumptions that are not connected to the actual DBPT architecture or training procedure.**  
   **Assumption 15** requires uniform boundedness and uniform Lipschitzness in the infinite-dimensional noise input. The paper does not show that the proposed encoder-decoder actually satisfies these conditions, nor what architectural constraints would guarantee them. Then **Theorem 18** derives a uniform convergence statement in terms of Rademacher complexity. This reads more like a generic learning-theory appendix than a theorem tailored to the proposed model. The issue is not that the theorem is false, but that the bridge from theorem assumptions to the instantiated DBPT is missing, so the practical relevance is unclear.

9. **The architecture itself is underspecified in the main paper, which makes the method hard to assess scientifically.**  
   Important implementation details are postponed to the appendix. In **Section 2.3.1**, the paper states that the decoder consists of multiple deconvolution layers with upsampling and convolution, but omits specifics such as kernel sizes, strides, padding choices, channel widths, nonlinearity, and how the output length matches the target grid. Since deconvolution is the central modeling choice, these details are not merely implementation trivia. Similarly, the role of the latent dimensionality $d_z$, the choice of upsampling factors, and whether positional/index information is injected explicitly are all important for understanding the model's inductive bias.

10. **The explanation of why deconvolution should be appropriate for general stochastic-process modeling is too hand-wavy.**  
    In **Section 2.3.1**, the paper argues that stacking deconvolution blocks captures "long-range correlations, hierarchical patterns, non-stationarity, and nonlinear interactions". That is a broad list of desirable properties, but it is asserted rather than demonstrated. Deconvolution imposes a very particular local and multi-scale bias that may be suitable for images and some regular grids, but the paper markets the method as a general weak-prior process model. There is little discussion of when this bias helps, when it hurts, or how it compares to alternative sequence models beyond the small qualitative ablation in **Figure 8**.

11. **The qualitative figures are mixed in what they actually establish.**  
    **Figure 2** does support the narrow claim that GP-like and Markov-like priors can fail under mismatch, but the comparison is heavily illustrative and not quantitative. Also, some methods appear to have very different uncertainty widths, yet the paper interprets those visually as "good" or "bad" calibration without formal calibration metrics. In **Figure 5**, the resolution analysis is interesting, but the claim that higher resolution degrades calibration is again made visually, without a numerical calibration measure. These figures are useful diagnostics, but the paper often leans on them for claims that require stronger quantitative backing.

12. **Some empirical choices are hard to reconcile with the paper's claimed problem setting.**  
    The finance experiment in **Section 4.2** uses daily prices from only one year for two stocks, which is a very narrow dataset for making claims about time-series uncertainty modeling. In image completion, the "single-trajectory" framing is unusual because each image is effectively treated as its own trajectory, yet the task is still closer to sparse image inpainting than to classic stochastic-process extrapolation. In black-box optimization, the search domain is discretized into 200 candidates and EI is evaluated exhaustively, which is a very simplified setting. None of these are invalid, but together they make the paper feel more like a collection of demonstrations than a decisive validation of a general process-learning framework.

13. **Presentation quality is uneven, and there are numerous writing and notation issues in the main text.**  
    Examples include awkward claims such as DBPT being a "shapeshifter" in **Section 3**, grammatical issues throughout, inconsistent use of symbols for the index set $\mathcal T$ versus its cardinality, and occasional ambiguity in whether $X$ denotes a process law, a sampled trajectory, or both. The paper is readable overall, but for a theoretically framed ICLR submission, the exposition needs tightening. The writing does not always help the reader separate elementary measure-theoretic facts from the true methodological claims.

14. **The strongest quantitative evidence, Table 2, may reflect the architecture more than the proposed paradigm.**  
    **Table 2** is indeed favorable to DBPT on MNIST and CIFAR completion, but this is exactly the kind of setting where deconvolutional decoders are expected to shine because of strong local spatial structure. The table therefore supports DBPT as an image-completion model more clearly than it supports the broader N2P thesis. This distinction matters, because the paper argues for a process-modeling paradigm, while the best empirical result is on a domain that heavily rewards convolutional inductive bias.

## Questions
1. The main training objective in **Section 2.3.2** is masked MSE with latent resampling. Can the authors clarify why this objective should be expected to produce calibrated predictive uncertainty, rather than simply a noisy regressor? In rebuttal, it would help to explain whether there is any implicit probabilistic interpretation of
   $$
   \mathcal L(\theta)=\mathbb E_Z\left[\frac{1}{|\tau_o|}\|R_{\tau_o}G_\theta(Z)-O\|_F^2\right]
   $$
   beyond moment matching.

2. Please clarify the exact novelty relative to prior generator-defined stochastic process models. A more careful discussion of what is actually new in the N2P formulation, beyond the general idea of pushing base noise through a neural function generator, would increase my confidence.

3. Could the authors provide stronger quantitative evidence on uncertainty quality, not just NLL computed from histograms? For example, calibration curves, coverage at nominal intervals, CRPS, or proper scoring rules that do not rely on ad hoc histogram density estimation would be more convincing.

4. For **Table 1**, what accounts for the very large NLL magnitudes, and how sensitive are the rankings to the histogram binning choices described in the appendix? A rebuttal with a sensitivity study on the density-estimation procedure would materially affect my confidence in the uncertainty claims.

5. The paper's strongest result is image completion in **Table 2** and **Figure 3**. Can the authors disentangle how much of that gain comes from the deconvolutional architecture itself versus the shared-noise/full-trajectory N2P formulation? An ablation removing stochasticity, or comparing to a deterministic deconvolutional inpainting baseline with similar capacity, would be very useful.

6. In **Figure 8**, the deconvolutional decoder looks much better than MLP and Transformer replacements, but the ablation is qualitative only. Can the authors provide quantitative ablations on the same tasks, ideally with matched parameter counts?

7. The theory appendix contains results on identifiability and generalization under assumptions that seem disconnected from the actual finite sparse-observation setting. Which of these results do the authors view as directly supporting DBPT as used in the experiments, and which are only background compatibility statements?

8. The paper repeatedly argues that neural-process methods are disadvantaged in the single-trajectory regime. Could the authors compare against stronger NP-family baselines, or at least explain why CNP alone is representative enough for the conclusions drawn in **Sections 3 and 4**?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns stood out from the main paper. The datasets and applications described appear standard, and I did not identify a clear issue requiring ethics escalation based on the provided manuscript.

## Soundness Rating
2: fair. The core mathematical statements are mostly elementary and not obviously incorrect, but the stronger methodological and uncertainty-related claims are only partially supported by the actual objective, theory, and experiments.

## Presentation Rating
2: fair. The paper is readable and has helpful figures, especially **Figures 1, 3, and 8**, but the exposition is uneven, the positioning is overstated in places, and several important methodological details are underspecified in the main text.

## Contribution Rating
2: fair. The paper addresses an interesting problem and the deconvolutional instantiation is empirically promising on some tasks, especially image completion, but the conceptual novelty and the strength of evidence for a general stochastic-process modeling advance are limited.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting and has some promising empirical aspects, but in my view it falls short of ICLR standards due to overstated conceptual novelty, a weakly justified probabilistic learning objective, and insufficiently decisive empirical support for the broad claims.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I checked the main technical claims and experiments carefully, but some of the appendix mathematics is not central enough to the practical method to warrant a stronger confidence score.